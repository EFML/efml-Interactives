var ActiveTable = (function () {
    var  NUMERIC, STRING, check_response, placeholder, help_text, column_widths, row_heights;
    //
    createChannel();
    // Input type values must match the type values in the Python code.
    NUMERIC = 1;
    STRING = 2;
    
    // Establish a channel to communicate with edX when the application is used
    // inside a JSInput and hosted completely on a different domain.
    function createChannel() {
        var channel,
            msg = 'The application is not embedded in an iframe. ' +
                  'A channel could not be established';

        // Establish a channel only if this application is embedded in an iframe.
        // This will let the parent window communicate with the child window using
        // RPC and bypass SOP restrictions.
        if (window.parent !== window) {
            channel = Channel.build({
                window: window.parent,
                origin: '*',
                scope: 'JSInput'
            });

            channel.bind('getGrade', getGrade);
            channel.bind('getState', getState);
            channel.bind('setState', setState);
        }
        else {
            console.log(msg);
        }
    }
    
    // Helper function to determine the number of significant digits in a
    // floating point literal.  Significant digits are counted from the first
    // non-zero digit specified, but include trailing zeros.  The string s is
    // assumed to be a valid floating-point literal and is not validated.
    function significant_digits(s) {
        // Regular expression to capture the digits before and after the decimal
        // point, but not the digits in the exponent.
        var re = /([0-9]*)\.([0-9]+)|([0-9]+)/;
        // All specified digits without the decimal point and the exponent.
        var all_digits = re.exec(s).slice(1).join('');
        // The number of digits with leading zero digits removed.
        return all_digits.replace(/^0+/, '').length;
    }

    // Correctness checks for numeric and string inputs.  These functions are
    // reimplementations of the corresponding functions in the Python code.
    check_response = {};
    check_response[NUMERIC] = function(self, student_response) {
        var r = parseFloat(student_response), d;
        if (isNaN(r)) return false;
        if (self.min_significant_digits || self.max_significant_digits) {
            d = significant_digits(student_response);
            if (self.min_significant_digits && d < self.min_significant_digits) {
                return false;
            }
            if (self.max_significant_digits && d > self.max_significant_digits) {
                return false;
            }
        }
        return Math.abs(r - self.answer) <= self.abs_tolerance;
    };
    check_response[STRING] = function(self, student_response) {
        return student_response == self.answer;
    };

    // Placeholder strings for the different input types
    placeholder = {};
    placeholder[NUMERIC] = 'numeric response';
    placeholder[STRING] = 'text response';

    function grade(state) {
        // This function attaches correctness information to each input field.
        // This information is later used to colour the input cells.  The Python
        // function embedded in XML determines correctness independently of this
        // function.
        $('#activeTable input').each(function() {
            var $input = $(this), cell_data = $input.data();
            $input.data('correct', check_response[cell_data.type](cell_data, this.value));
        });
        return state;
    }

    function getState() {
        // Extract the current state of the table.  The state includes the
        // complete problem description and the values entered by the student.
        var data = [];

        function appendRow() {
            var row_state = [];
            var row = $(this);
            row.children().each(function() {
                var $cell = $(this), $input = $('input', this), cell_data;
                if (typeof $input[0] === 'undefined') {
                    row_state.push($cell.text());
                } else {
                    cell_data = $input.data();
                    cell_data.value = $('input', this)[0].value;
                    row_state.push(cell_data);
                }
            });
            data.push(row_state);
        }
        
        $('#activeTable thead tr').each(appendRow);
        $('#activeTable tbody tr').each(appendRow);
        return JSON.stringify({
            data: data,
            help_text: help_text,
            column_widths: column_widths,
            row_heights: row_heights
        });
    }

    function setState(state) {
        console.log("setting State");
        // Regenerate the table based on the state data.  This function is also
        // responsible for initially generating the table based on the initial
        // state exported by the Python code and for setting the background
        // colour of input fields based on the correctness information stored
        // by the grader.

        // Classes used on cells that contain input fields, based on their
        // correctness.
        var cell_classes = {}, $row;
        cell_classes[undefined] = 'unchecked';
        cell_classes[true] = 'right-answer';
        cell_classes[false] = 'wrong-answer';

        function makeHeadRow(row_state) {
            // Generate and return the title row of the table
            var $row = $('<tr>');
            for (var j = 0; j < row_state.length; j++) {
                $row.append($('<th>').text(row_state[j]));
            }
            return $row;
        }

        function makeInput(cell_state) {
            return $('<input/>', {
                type: 'text',
                value: cell_state.value,
                placeholder: placeholder[cell_state.type],
                // The input will always fill the whole width of the table cell,
                // but some browsers will use the size value as a minimum, and
                // assume a default if you don't set the size, so we have to set
                // it to a small value.
                size: '1',
            }).data(cell_state);
        }

        function makeRow(row_state) {
            var $row, cell_state, $cell;
            $row = $('<tr>');
            for (var j = 0; j < row_state.length; j++) {
                cell_state = row_state[j];
                $cell = $('<td>');
                $cell.attr('id', 'cell_' + i + '_' + j);
                if (typeof cell_state === 'object') {
                    $cell.addClass('active');
                    $cell.addClass(cell_classes[cell_state.correct]);
                    $cell.append(makeInput(cell_state));
                } else {
                    $cell.text(cell_state);
                }
                $row.append($cell);
            }
            return $row;
        }

        function makeHelp() {
            var help_active = false;
            if (!help_text) return;
            $('#help-text').text(help_text);
            $('#help-button').click(function(e) {
                $('#help-text').toggle();
                help_active = !help_active;
                $(this).text(help_active ? '-help' : '+help');
            });
            $('#help').show();  // Show the div with the button, not the text.
        }

        function makeColGroup(num_cols) {
            var w;
            for (var i = 0; i < num_cols; i++) {
                w = column_widths !== null ? column_widths[i] : 800 / num_cols;
                $('<col>').css('width', w).appendTo('#activeTable colgroup');
            }
        }

        function setRowHeights() {
            var rows = $('#activeTable tr');
            $(row_heights).each(function (index, value) {
                value = parseInt(value);
                var row = $(rows[index]);
                row.css('height', value + 'px');
                row.find('input').css('height', value - 2 + 'px');
            });
        }

        state = JSON.parse(state);
        makeHeadRow(state.data[0]).appendTo('#activeTable thead');
        for (var i = 1; i < state.data.length; i++) {
            $row = makeRow(state.data[i]);
            if (i % 2 === 0) {
                $row.addClass('odd');
            }
            $row.appendTo('#activeTable tbody');
        }
        help_text = state.help_text;
        makeHelp();
        column_widths = state.column_widths;
        makeColGroup(state.data[0].length);
        row_heights = state.row_heights;
        setRowHeights();
    }

    return {
        grade: grade,
        getState: getState,
        setState: setState
    };
}());

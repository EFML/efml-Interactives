// Used as JSInput
(function(JXG, MacroLib) {
    'use strict';
    var brd1, MS1, MS2, iB1SD, dashS2;

    function init() {
        MacroLib.init(MacroLib.ONE_BOARD);
        ////////////
        // BOARD 1
        ////////////
        var cfx = 800.0 / 12.0;
        var cfy = 27.0 / 12.0;
        var newbbox = [-170, 27, 800, -4.5];

        brd1 = MacroLib.createBoard('jxgbox1', {
            xname: ' ',
            yname: ' ',
            grid: false,
            bboxlimits: newbbox
        });

        var xaxis = brd1.create('axis', [
            [0, 0],
            [1, 0]
        ], {
            name: 'Quantity of Money ($billions)',
            withLabel: false,
        });
        xaxis.removeAllTicks();
        brd1.create('ticks', [xaxis, [0, 100, 200, 300, 400, 500, 600, 700]], {
            strokeColor: 'black',
            majorHeight: 7,
            drawLabels: true,
            label: {
                offset: [0, -20]
            }
        });
        var xlabel1 = brd1.create('text', [380, -3, 'Quantity of Money ($billions)']);

        var yaxis = brd1.create('axis', [
            [0, 0],
            [0, 1]
        ], {
            name: '',
            withLabel: true,
        });
        yaxis.removeAllTicks();
        brd1.create('ticks', [yaxis, [0, 5, 10, 15, 20, 25, 30]], {
            strokeColor: 'black',
            majorHeight: 7,
            drawLabels: true
        });
        var ylabel1 = brd1.create('text', [-150, 24, 'Nominal<br>Interest<br>Rate']);

        //Supply Line 1 - fixed
        MS1 = brd1.create('segment', [
            [cfx * 6.0, cfy * 11.0],
            [cfx * 6.0, cfy * 1.0]
        ], {
            strokeColor: 'gray',
            strokeWidth: 5,
            name: '',
            withLabel: false,
            dash: 1,
        });

        //Demand Line 1 - fixed
        var MD1 = brd1.create('segment', [
            [cfx * 1.45, cfy * 9.0],
            [cfx * 9.0, cfy * 1.45]
        ], {
            strokeColor: 'orange',
            strokeWidth: 5,
            name: 'M<sub>D</sub>',
            withLabel: true,
            label: {
                offset: [150, -140]
            }
        });

        //Supply Line 2 - moveable
        MS2 = brd1.create('segment', [
            [cfx * 6.0, cfy * 11.0],
            [cfx * 6.0, cfy * 1.0]
        ], {
            strokeColor: 'dodgerblue',
            strokeWidth: 5,
            name: 'M<sub>S</sub>',
            withLabel: true,
            fixed: false,
            highlight: true,
            label: {
                offset: [-10, 180]
            }
        });

        ////////////
        // Intersection Box 1
        ////////////
        //S Intersection
        iB1SD = brd1.create('intersection', [MS2, MD1, 0], {
            size: 4,
            visible: true,
            color: 'darkblue',
            strokeColor: 'darkblue'
        });

        ////////////
        // Draggable Dashed Lines for Board 1
        ////////////
        dashS2 = MacroLib.createDashedLines2Axis(brd1, iB1SD, {
            fixed: false,
            withLabel: false,
            xlabel: '',
            ylabel: '',
            color: 'gray'
        });

        //////////////////
        // Interactivity
        //////////////////
        MS2.on('drag', function() {
            brd1.suspendUpdate();
            //Moving 1st set of Dashed Lines in Board 1
            dashS2.Y1.moveTo([0, iB1SD.Y()]);
            dashS2.Y2.moveTo([iB1SD.X(), iB1SD.Y()]);

            dashS2.X1.moveTo([iB1SD.X(), 0]);
            dashS2.X2.moveTo([iB1SD.X(), iB1SD.Y()]);
            brd1.unsuspendUpdate();
        });
    }

    /////////////////////////
    // External DOM button
    /////////////////////////
    var resetAnimationBtn = document.getElementById('resetAnimationBtn');

    resetAnimationBtn.addEventListener('click', function() {
        JXG.JSXGraph.freeBoard(brd1);
        init();
    });

    //Standard edX JSinput functions
    function getGrade() {
        var state = {
            MS1: {
                X1: MS1.point1.X(),
                X2: MS1.point2.X(),
                Y1: MS1.point1.Y(),
                Y2: MS1.point2.Y()
            },
            MS2: {
                X1: MS2.point1.X(),
                X2: MS2.point2.X(),
                Y1: MS2.point1.Y(),
                Y2: MS2.point2.Y()
            }
        };
        var statestr = JSON.stringify(state);

        return statestr;
    }

    function getState() {
        var state = JSON.parse(getGrade());
        var statestr = JSON.stringify(state);
        console.info('State successfully saved.');
        return statestr;
    }

    function setState(transaction, statestr) {
        var state = JSON.parse(statestr);

        if (state.MS1 && state.MS2) {
            MS1.point1.moveTo([state.MS1.X1, state.MS1.Y1], 0);
            MS1.point2.moveTo([state.MS1.X2, state.MS1.Y2], 0);

            MS2.point1.moveTo([state.MS2.X1, state.MS2.Y1], 0);
            MS2.point2.moveTo([state.MS2.X2, state.MS2.Y2], 0);

            dashS2.Y1.moveTo([0, iB1SD.Y()]);
            dashS2.Y2.moveTo([iB1SD.X(), iB1SD.Y()]);

            dashS2.X1.moveTo([iB1SD.X(), 0]);
            dashS2.X2.moveTo([iB1SD.X(), iB1SD.Y()]);
            brd1.update();

        }
        brd1.update();
        console.info('State updated successfully from saved.');
    }

    init();
    MacroLib.onLoadPostMessage();
    MacroLib.createChannel(getGrade, getState, setState);

})(JXG, MacroLib, undefined);

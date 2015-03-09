
# coding: utf-8

# ###Test for Brian Held

# In[2]:

get_ipython().run_cell_magic(u'HTML', u'', u'<!DOCTYPE html>\n<html>\n    <head>\n        <style> \n            body {\n                margin: 10px;\n                /*padding-top: 40px;*/\n            }\n        </style>\n    </head>\n\n    <body>\n        \n        <div style="width: 100%; overflow: hidden;">\n            <div id=\'jxgbox1\' class=\'jxgbox\' style=\'width:350px; height:300px; float:left; border: solid #1f628d 2px;\'></div>        \n        </div>\n\n        <!-- TURNED OFF\n        <input class="btn" type="button" value="Shift in Aggregate Demand" onClick="startAnimation()">\n        <input class="btn" type="button" value="Reset" onClick="resetAnimation()">\n        -->\n        \n        \n        <!-- COMMENT: Where our Javascript begins. -->\n        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.98/jsxgraphcore.js"></script>\n        \n        <!-- COMMENT: Specific Davidson Next calls built on JSXGraph. Must be loaded after JSXgraph. -->\n        <script type="text/javascript" src="../../../JS/Macro_JSXgraph.js"></script>\n        \n        <script type=\'text/javascript\'>\n            \n            //General Parameters for Macro\n            JXG.Options.point.showInfobox = false;\n            JXG.Options.segment.strokeColor = \'Pink\';\n\n            createDragLine = function(board,point1,point2,gname,color,xo,yo) {\n                return board.create(\'segment\',[point1,point2],{strokeColor:color,strokeWidth:\'3\',name:gname,withLabel:true,label:{offset:[xo,yo]}});\n            }\n\n            createSupply = function(board,gname,color) {\n                var c1 = [1.0,2.0];\n                var c2 = [9.0,10.0];\n                var S1 = board.create(\'point\',c1,{withLabel:false,visible:false});\n                var S2 = board.create(\'point\',c2,{withLabel:false,visible:false});\n                return board.create(\'segment\',[S1,S2],{\'strokeColor\':color,\'strokeWidth\':\'3\',\n                                                       \'name\':gname,\'withLabel\':true,\n                                                       \'label\':{\'offset\':[105,105]}\n                                                      });\n            }\n\n            createDemand = function(board,gname,color) {\n                var c1 = [1.0,10.0];\n                var c2 = [9.0,2.0];\n                var D1 = board.create(\'point\',c1,{withLabel:false,visible:false});\n                var D2 = board.create(\'point\',c2,{withLabel:false,visible:false});\n                return board.create(\'segment\',[D1,D2],{\'strokeColor\':color,\'strokeWidth\':\'3\',\n                                                       \'name\':gname,\'withLabel\':true,\n                                                       \'label\':{\'offset\':[105,-105]}\n                                                      });\n            }\n\n\n            /////////////////////////////////////////////////////////////\n            // Dashed Lines\n            createDashedLines2Axis = function(board,intersection,options) {\n                var fixed = options.fixed || true;  // defaults\n                var withLabel = options.withLabel || false;\n                var xlabel = options.xlabel || \'\';  \n                var ylabel = options.ylabel || \'\';\n                var color = options.color || \'gray\';\n\n                var dashYp1 = board.create(\'point\',[0, intersection.Y()],\n                                            {withLabel:withLabel,name:ylabel,visible:true,size:\'0.5\',strokeColor:\'Gray\',\'label\':{\'offset\':[-25,-2]}});\n\n                var dashYp2 = board.create(\'point\',[intersection.X(), intersection.Y()],\n                                            {withLabel:false,visible:false});\n                var dashY1 = board.create(\'segment\',[dashYp1,dashYp2],\n                                           {strokeColor:color,strokeWidth:\'2\',dash:\'1\',fixed:fixed});\n\n                var dashXp1 = board.create(\'point\',[intersection.X(), 0],\n                                            {withLabel:withLabel,name:xlabel,visible:true,size:\'0.5\',strokeColor:\'Gray\',\'label\':{\'offset\':[-5,-8]}});\n\n                var dashXp2 = board.create(\'point\',[intersection.X(), intersection.Y()],\n                                            {withLabel:false,visible:false});\n\n                var dashX1 = board.create(\'segment\',[dashXp1,dashXp2],\n                                           {strokeColor:color,strokeWidth:\'2\',dash:\'1\',fixed:fixed});\n\n                return [dashXp1,dashXp2,dashYp1,dashYp2];\n            }\n            \n            ////////////\n            // BOARD 1\n            ////////////\n            bboxlimits = [-1.5, 12, 12, -1];\n            var brd1 = JXG.JSXGraph.initBoard(\'jxgbox1\', {axis:false, \n                                                    showCopyright: false,\n                                                    showNavigation: false,\n                                                    zoom: false,\n                                                    pan: false,\n                                                    boundingbox:bboxlimits,\n                                                    grid: false,\n                                                    hasMouseUp: true, \n            });\n            \n            xaxis1 = brd1.create(\'axis\', [[0, 0], [11, 0]], {withLabel: false});\n            yaxis1 = brd1.create(\'axis\', [[0, 0], [0, 11]], {withLabel: false});\n\n            //Axes\n            xaxis1.removeAllTicks();\n            yaxis1.removeAllTicks();\n            var xlabel1 = brd1.create(\'text\',[-1.2,10,"PL"],{fixed:true});\n            var ylabel1 = brd1.create(\'text\',[9,-0.5,"RGDP"],{fixed:true});\n            \n            //Supply Line 1 - fixed\n            var Supply = createSupply(brd1,\'SRAS\',\'DodgerBlue\');\n            Supply.setAttribute({\'name\':\'SRAS\',\'fixed\':true,\'highlight\':false});\n            \n            //Demand Line 1 - fixed\n            var AD1 = createDemand(brd1,\'AD1\',\'Orange\');\n            AD1.setAttribute({\'dash\':1,\'fixed\':true,\'highlight\':false});\n            \n            //Demand Line 2 - moveable\n            var AD2 = createDemand(brd1,\'AD2\',\'Orange\');\n            AD2.setAttribute({withLabel:false});\n            \n             \n            ////////////\n            // Intersection Box 1\n            ////////////\n            var iSDfix = brd1.create(\'intersection\', [AD1, Supply, 0], {visible:false}); \n            var iS2D = brd1.create(\'intersection\', [AD2, Supply, 0], {visible:false});\n            \n            ////////////\n            // Draggable Dashed Lines for Board 1\n            ////////////\n            var dashesDragB1 = createDashedLines2Axis(brd1,iS2D,\n                                                      {fixed:false,\n                                                       withLabel:false,\n                                                       xlabel:\'Y2\',\n                                                       ylabel:\'PL2\',\n                                                       color:\'Orange\'});\n            var dashS2Xp1 = dashesDragB1[0];\n            var dashS2Xp2 = dashesDragB1[1];\n            var dashS2Yp1 = dashesDragB1[2];\n            var dashS2Yp2 = dashesDragB1[3];\n            \n            \n            ////////////\n            // Fixed Dashed Lines for Board 1\n            ////////////\n            var dashesFixedB1 = createDashedLines2Axis(brd1,iSDfix,\n                                                      {withLabel:true,\n                                                       xlabel:\'rY1\',\n                                                       ylabel:\'PL1\',\n                                                       color:\'DodgerBlue\'});\n            \n            ////////////\n            //LRAS - straight line\n            ////////////\n            var LRAS = brd1.create(\'segment\',[[7.0,11.0],[7.0,0.0]],\n                                   {\'strokeColor\':\'DodgerBlue\',\'strokeWidth\':\'2\',\n                                    \'name\':\'LRAS\',\'withLabel\':true,\n                                    \'label\':{\'offset\':[-15,140]}});\n            var labelLRAS = brd1.create(\'text\',[6.7,-0.4,"rYF"],{fixed:true});\n            \n            \n        \n            //////////////////\n            // Interactivity\n            //////////////////\n            brd1.on(\'move\', function() {      \n                //Moving Dashed Lines in Board 1\n                dashS2Yp1.moveTo([0, iS2D.Y()]);\n                dashS2Yp2.moveTo([iS2D.X(), iS2D.Y()]);\n\n                dashS2Xp1.moveTo([iS2D.X(), 0]);\n                dashS2Xp2.moveTo([iS2D.X(), iS2D.Y()]);\n        \n            });\n            \n            brd1.on(\'mousedown\', function() {      \n                AD2.setAttribute({withLabel:true});\n                dashS2Yp1.setAttribute({withLabel:true});\n                dashS2Xp1.setAttribute({withLabel:true});\n                brd1.update()\n            });\n            \n            \n            \n            \n        </script>\n    </body>\n</html>')


# ### Generate HTML File

# In[17]:

import re

#tmpfile = _i86
index_htmlinput = [ i for i,x in enumerate(_ih) if "run_cell_magic(u'HTML'" in x and "re.sub('%%HTML','',tmpfile)" not in x]

tmpfile = eval('_i%d' % int(index_htmlinput[-1]))
tmpfile = re.sub('%%HTML','',tmpfile)
tmpfile = re.sub(r'<!--START-BUTTON FOR PASS STATE(.*?)END-BUTTON FOR PASS STATE-->','',tmpfile,flags=re.DOTALL)
tmpfile = re.sub(r'//START-PASS STATE TO IPYTHON KERNEL(.*?)//END-PASS STATE TO IPYTHON KERNEL','',tmpfile,flags=re.DOTALL)

filename = 'MLE_test_4_2'
html_filename = '%s.html' % filename

with open(html_filename,'w') as hfile:
    hfile.write(tmpfile)
print tmpfile


# In[ ]:




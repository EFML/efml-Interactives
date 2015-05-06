
# coding: utf-8

# In[38]:

get_ipython().run_cell_magic(u'HTML', u'', u'<!DOCTYPE html>\n<html>\n    <head>\n        <style> \n            body {\n                margin: 10px;\n                /*padding-top: 40px;*/\n            }\n        </style>\n    </head>\n\n    <body>\n        \n        <div style="width: 100%; overflow: hidden;">\n            <div id=\'jxgbox1\' class=\'jxgbox\' style=\'width:350px; height:300px; float:left; border: solid #1f628d 2px;\'></div>        \n            <div id=\'jxgbox2\' class=\'jxgbox\' style=\'width:350px; height:300px; margin-left: 375px; border: solid #1f628d 2px;\'></div>\n        </div>\n        \n        <!-- COMMENT: Where our Javascript begins. -->\n        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.98/jsxgraphcore.js"></script>\n        \n        <!-- COMMENT: Specific Davidson Next calls built on JSXGraph. Must be loaded after JSXgraph. -->\n        <script type="text/javascript" src="../../js/Macro_t1.0.js"></script>\n        \n        <script type=\'text/javascript\'>\n            \n            //General Parameters for Macro\n            JXG.Options.point.showInfobox = false;\n            JXG.Options.segment.strokeColor = \'Gray\';\n            JXG.Options.segment.strokeWidth = \'5\';\n            JXG.Options.text.fontSize = 15;\n            \n            ////////////\n            // BOARD 1\n            ////////////\n            bboxlimits = [-2.5, 12, 12, -2.0];\n            var brd1 = JXG.JSXGraph.initBoard(\'jxgbox1\', {axis:false, \n                                                    showCopyright: false,\n                                                    showNavigation: false,\n                                                    zoom: false,\n                                                    pan: false,\n                                                    boundingbox:bboxlimits,\n                                                    grid: true,\n                                                    hasMouseUp: true, \n            });         \n\n            xaxis1 = brd1.create(\'axis\', [[0, 0], [11, 0]], {withLabel: false});\n            yaxis1 = brd1.create(\'axis\', [[0, 0], [0, 11]], {withLabel: false});\n\n            //Axes\n            xaxis1.removeAllTicks();\n            yaxis1.removeAllTicks();\n            var xlabel1 = brd1.create(\'text\',[6,-0.5,"Quantity of Money"],{fixed:true});\n            var ylabel1 = brd1.create(\'text\',[-2.45,10,"Nominal<br>Interest<br>Rate"],{fixed:true});\n            \n            ////////////\n            // BOARD 2\n            ////////////\n            bboxlimits2 = [-2.5, 12, 12, -2.0];\n            var brd2 = JXG.JSXGraph.initBoard(\'jxgbox2\', {axis:false, \n                                                    showCopyright: false,\n                                                    showNavigation: false,\n                                                    zoom: false,\n                                                    pan: false,\n                                                    boundingbox:bboxlimits2,\n                                                    grid: true,\n                                                    hasMouseUp: true, \n            });        \n            \n            xaxis2 = brd2.create(\'axis\', [[0, 0], [11, 0]], {withLabel: false});\n            yaxis2 = brd2.create(\'axis\', [[0, 0], [0, 11]], {withLabel: false});\n\n            //Axes\n            xaxis2.removeAllTicks();\n            yaxis2.removeAllTicks();\n            var xlabel2 = brd2.create(\'text\',[3.0,-0.5,"Quantity of Bonds per Period"],{fixed:true,highlight:false});\n            var ylabel2 = brd2.create(\'text\',[-2.45,10,"Price of<br>Bonds"],{fixed:true,highlight:false});\n            \n            //Sliders\n            var sliderx = brd1.create(\'slider\',[[2.0,-1.25],[8,-1.25],[-1.5,0,3.5]],{withLabel:false,snapWidth:0.05,\n                                                                                     color:\'Orange\'});\n            \n            //Postivit Slider Transformation\n            sliderPositive = brd1.create(\'transform\',[\n                function(){return sliderx.Value()},\n                function(){return 0.0}],\n                {type:\'translate\'}\n                );\n        \n            //Negative Slider Transformation\n            sliderNegative = brd1.create(\'transform\',[\n                function(){return sliderx.Value()},\n                function(){return 0.0}],\n                {type:\'translate\'}\n                );\n            \n            //Demand Board 1\n            var D1 = brd1.create(\'segment\',[[2,9.5],[9.5,2]],{\'name\':\'M<sub>D</sub>\',fixed:true,\n                                                              withLabel:true,label:{offset:[100,-100]}});\n            //var S1 = brd1.create(\'segment\',[[5.75,1.0],[5.75,11.0]],{withLabel:true,name:\'M<sub>S</sub>\',label:{offset:[0,115]}});\n            \n            //Supply Board 1 - with slider transformation\n            var s1B1 = brd1.create(\'point\',[3.75,1.0],{visible:false});\n            var s2B1 = brd1.create(\'point\',[3.75,11.0],{visible:false});\n            var pS1 = brd1.create(\'point\',[s1B1,[sliderPositive]],{visible:false});\n            var pS2 = brd1.create(\'point\',[s2B1,[sliderPositive]],{visible:false});\n            \n            var S1fixed = brd1.create(\'segment\',[s1B1,s2B1],{withLabel:false,fixed:true,\'name\':\'M<sub>S1</sub>\',\n                                                         highlight:false,dash:\'1\',strokeWidth:\'3\',\n                                                         label:{offset:[0,115]}});\n            \n            var S1 = brd1.create(\'segment\',[pS1,pS2],{withLabel:true,highlight:false,\'name\':\'M<sub>S2</sub>\',\n                                                      color:\'DodgerBlue\',label:{offset:[0,115]}});\n            \n            //Intersection of SD board 1\n            var iSDB = brd1.create(\'intersection\',[S1,D1],{withLabel:false,highlight:false});\n            //var gSDB1 = brd1.create(\'glider\',[3.75,7.75,S1],{withLabel:false,highlight:false});\n            \n            brd1.addChild(brd2);\n            \n            //Demand Board 2 - with a Positive transformation\n            //var S2 = createSupply(brd2,{withLabel:true,\'name\':\'S<sub>2</sub>\'});\n            var S2 = brd2.create(\'segment\',[[2.0,2.0],[9.5,9.5]],{withLabel:true,name:\'S<sub>2</sub>\',label:{offset:[90,90]}});\n            \n            //Supply Board 2 - with a Negative transformation\n            var d1B2 = brd2.create(\'point\',[2.0,9.5],{visible:false});\n            var d2B2 = brd2.create(\'point\',[9.5,2.0],{visible:false});\n            var As = brd2.create(\'point\',[d1B2,[sliderNegative]],{visible:false});\n            var Bs = brd2.create(\'point\',[d2B2,[sliderNegative]],{visible:false});\n            \n            var D2fixed = brd2.create(\'segment\',[d1B2,d2B2],{withLabel:false,fixed:true,\'name\':\'D<sub>1</sub>\',\n                                                         highlight:false,dash:\'1\',strokeWidth:\'3\',\n                                                         label:{offset:[90,-90]}});\n            \n            var D2 = brd2.create(\'segment\',[As,Bs],{withLabel:true,\'name\':\'D<sub>2</sub>\',highlight:false,\n                                                    color:\'DodgerBlue\',label:{offset:[90,-90]}});\n                        \n            var iSDB2 = brd2.create(\'intersection\',[S2,D2],{withLabel:false,highlight:false});\n            \n            \n            createDashedLines2Axis = function(board,intersection,options) {\n                var fixed = options.fixed || true;  // defaults\n                var withLabel = options.withLabel || false;\n                var xlabel = options.xlabel || \'\';  \n                var ylabel = options.ylabel || \'\';\n                var color = options.color || \'gray\';\n                var visible = options.visible || true;\n\n                var Y1,Y2,YLine,X1,X2,XLine,obj={};\n                var Y1 = board.create(\'point\',[0, intersection.Y()],\n                                 {\'withLabel\':withLabel,\'name\':ylabel,\'visible\':true,\'size\':\'0.5\',\n                                 \'strokeColor\':\'Gray\',\'label\':{\'offset\':[2,12]}});\n\n                var Y2 = board.create(\'point\',[intersection.X(), intersection.Y()],\n                                 {\'withLabel\':false,\'visible\':false,\'size\':\'0.0\',\'strokeColor\':\'\'});\n\n                var YLine = board.create(\'segment\',[Y1,Y2],\n                                    {\'strokeColor\':color,\'strokeWidth\':\'2\',\'dash\':\'1\',\'fixed\':fixed,\'visible\':visible});\n\n                var X1 = board.create(\'point\',[intersection.X(), 0],\n                                 {\'withLabel\':withLabel,\'name\':xlabel,\'visible\':true,\'size\':\'0.5\',\n                                 \'strokeColor\':\'Gray\',\'label\':{\'offset\':[2,12]}});\n\n                var X2 = board.create(\'point\',[intersection.X(), intersection.Y()],\n                                 {\'withLabel\':false,\'visible\':false,\'size\':\'0.0\',\'strokeColor\':\'\'});\n\n                var XLine = board.create(\'segment\',[X1,X2],\n                                    {\'strokeColor\':color,\'strokeWidth\':\'2\',\'dash\':\'1\',\'fixed\':fixed,\'visible\':visible});\n\n\n                var obj = {\n                    Y1: Y1,\n                    Y2: Y2,\n                    YLine: YLine,\n                    X1: X1,\n                    X2: X2,\n                    XLine: XLine\n                }\n\n                return obj;\n            }\n            \n            \n            //Dashed Lines - Board 1\n            var dashB1fixed = createDashedLines2Axis(brd1,iSDB,{fixed:true,withLabel:false,color:\'Gray\'});\n            var dashB1 = createDashedLines2Axis(brd1,iSDB,{fixed:false,withLabel:true,color:\'DodgerBlue\',\n                                                           xlabel:\'Q<sub>S</sub>\',ylabel:\'NIR\'});\n            \n            //Dashed Lines - Board 2\n            var dashB2fixed = createDashedLines2Axis(brd2,iSDB2,{fixed:true,withLabel:false,color:\'Gray\'});\n            var dashB2 = createDashedLines2Axis(brd2,iSDB2,{fixed:false,withLabel:true,color:\'DodgerBlue\',\n                                                            xlabel:\'Q<sub>2</sub>\',ylabel:\'P<sub>2</sub>\'});\n            \n            //////////////////\n            // Interactivity\n            //////////////////\n            brd1.on(\'move\', function() {      \n                //Moving 1st set of Dashed Lines in Board 1\n                dashB1.Y1.moveTo([0, iSDB.Y()]);\n                dashB1.Y2.moveTo([iSDB.X(), iSDB.Y()]);\n\n                dashB1.X1.moveTo([iSDB.X(), 0]);\n                dashB1.X2.moveTo([iSDB.X(), iSDB.Y()]);\n                    \n                //Moving Board 2 Dashed Lines\n                dashB2.Y1.moveTo([0, iSDB2.Y()]);\n                dashB2.Y2.moveTo([iSDB2.X(), iSDB2.Y()]);\n\n                dashB2.X1.moveTo([iSDB2.X(), 0]);\n                dashB2.X2.moveTo([iSDB2.X(), iSDB2.Y()]);\n            });\n            \n        </script>\n    </body>\n</html>')


# In[39]:

import re
from os import path

### Find the HTML cell within the IPython inputs
index_htmlinput = [ i for i,x in enumerate(_ih) if "run_cell_magic(u'HTML'" in x and "re.sub('%%HTML','',tmpfile)" not in x]

tmpfile = eval('_i%d' % int(index_htmlinput[-1]))
tmpfile = re.sub('%%HTML','',tmpfile)

### Would be cool if it just took the title of the notebook
html_filename = 'MMMLC3_SallyScenario2' + '.html'

with open(html_filename,'w') as hfile:
    hfile.write(tmpfile)
print tmpfile


# In[ ]:




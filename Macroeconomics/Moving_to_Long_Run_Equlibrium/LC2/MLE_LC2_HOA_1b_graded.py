
# coding: utf-8

# ###Moving to Long-Run Equilibrium
# https://studio.edge.edx.org/container/i4x://DavidsonCollege/DAP002/vertical/ee567d7e52294aeaa8a32cd1c3f09cf3?action=new

# In[1]:

get_ipython().run_cell_magic(u'HTML', u'', u'<!DOCTYPE html>\n<html>\n    <head>\n        <meta charset="UTF-8">\n        <title>Moving Toward Long-Run Equilibrium</title>\n        <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=AM_HTMLorMML-full"></script>\n        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.98/jsxgraphcore.js"></script>\n        <script type="text/javascript" src="underscore-min.js"></script>\n        <script type="text/javascript" src="jquery.min.js"></script>\n        <script type="text/javascript" src="jquery-ui.min.js"></script>\n        <script type="text/javascript" src="../../JS/Macro.js"></script>\n        <script type="text/javascript" src="MLE_LC2_HOA_1b_graded.js"></script>\n    </head>\n\n    <body>\n        <div style="width: 100%; overflow: hidden;">\n            <div id=\'jxgbox1\' class=\'jxgbox\' style=\'width:350px; height:300px; float:left; border: solid #1f628d 2px;\'></div>        \n        </div>            \n    </body>\n</html>')


# ### Generate HTML File

# In[5]:

import re

#tmpfile = _i86
index_htmlinput = [ i for i,x in enumerate(_ih) if "run_cell_magic(u'HTML'" in x and "re.sub('%%HTML','',tmpfile)" not in x]

tmpfile = eval('_i%d' % int(index_htmlinput[-1]))
tmpfile = re.sub('%%HTML','',tmpfile)
tmpfile = re.sub(r'<!--START-BUTTON FOR PASS STATE(.*?)END-BUTTON FOR PASS STATE-->','',tmpfile,flags=re.DOTALL)
tmpfile = re.sub(r'//START-PASS STATE TO IPYTHON KERNEL(.*?)//END-PASS STATE TO IPYTHON KERNEL','',tmpfile,flags=re.DOTALL)
tmpfile = re.sub(r'<script type="text/javascript" src="../../JS/Macro.js"></script>','<script type="text/javascript" src="/static/Macro.js"></script>',tmpfile,flags=re.DOTALL)

filename = 'MLE_LC2_HOA_1b_graded'
html_filename = '%s.html' % filename

with open(html_filename,'w') as hfile:
    hfile.write(tmpfile)
print tmpfile


# In[ ]:



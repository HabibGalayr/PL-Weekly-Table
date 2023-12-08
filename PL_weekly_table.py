#!/usr/bin/env python
# coding: utf-8

# In[93]:


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from plottable import ColumnDefinition, Table
from plottable.cmap import normed_cmap
from plottable.plots import image


# In[138]:


get_ipython().system('pip install html5lib')


# In[139]:


df = pd.read_html('https://fbref.com/en/comps/9/Premier-League-Stats', attrs={"id": "results2023-202491_overall"})[0]


# In[95]:


df.head()


# In[96]:


df['badge'] = df['Squad'].apply(
    lambda x: f"C:/Users/Habib/team logos/{x.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i')}_logo.png"
)


# In[97]:


df['badge'][0]


# In[98]:


df.columns


# In[99]:


df = df[['Rk', 'badge', 'Squad', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts', 'Pts/MP',
       'xG', 'xGA', 'xGD'
]]


# In[100]:


df.columns


# In[128]:


bg_color = "#FFFFFF"
text_color = "#000000"

row_colors = {
    "top4":"#74E67D",
    "top6":"#FAFA7F",
    "relegation":"#FF6B57",
    "even":"#E2E2E1",
    "odd":"#B3B0B0"
}

plt.rcParams["text.color"] = text_color
plt.rcParams["font.family"] = "monospace"


# In[121]:


df.columns


# In[122]:


col_defs = [
    ColumnDefinition(
            name="Rk",
            textprops={"ha": "center"},
            width=0.5,
        ),
    ColumnDefinition(
            name="badge",
            textprops={"ha": "center", "va": "center", "color": bg_color},
            width=0.5,
            plot_fn=image,
        ),
    ColumnDefinition(
            name="Squad",
            textprops={"ha": "left", "weight": "bold"},
            width=1.75,
         ),
    ColumnDefinition(
            name="MP",
            group="Matches Played",
            textprops={"ha": "center"},
            width=0.5,
         ),
    ColumnDefinition(
            name="W",
            group="Matches Played",
            textprops={"ha": "center"},
            width=0.5,
         ),
    ColumnDefinition(
            name="D",
            group="Matches Played",
            textprops={"ha": "center"},
            width=0.5,
         ),
    ColumnDefinition(
            name="L",
            group="Matches Played",
            textprops={"ha": "center"},
            width=0.5,
         ),
    ColumnDefinition(
            name="GF",
            group="goals",
            textprops={"ha": "center"},
            width=0.5,
         ), 
    ColumnDefinition(
            name="GA",
            group="goals",
            textprops={"ha": "center"},
            width=0.5,
         ),
    ColumnDefinition(
            name="GD",
            group="goals",
            textprops={"ha": "center"},
            width=0.5,
         ),
    ColumnDefinition(
            name="Pts",
            group="points",
            textprops={"ha": "center"},
            width=0.5,
         ),
        ColumnDefinition(
            name="Pts/MP",
            group="points",
            textprops={"ha": "center"},
            width=0.5,
         ),
    ColumnDefinition(
            name="xG",
            group="expected goals ",
            textprops={"ha": "center", "color": text_color, "weight": "bold", "bbox": {"boxstyle": "circle", "pad": .35}},
            cmap=normed_cmap(df['xG'], cmap=matplotlib.cm.PiYG, num_stds=2)
        ),
    ColumnDefinition(
            name="xGA",
            group="expected goals ",
            textprops={"ha": "center", "color": text_color, "weight": "bold", "bbox": {"boxstyle": "circle", "pad": .35}},
            cmap=normed_cmap(df['xGA'], cmap=matplotlib.cm.PiYG, num_stds=2)
        ),
    ColumnDefinition(
            name="xGD",
            group="expected goals ",
            textprops={"ha": "center", "color": text_color, "weight": "bold", "bbox": {"boxstyle": "circle", "pad": .35}},
            cmap=normed_cmap(df['xGD'], cmap=matplotlib.cm.PiYG, num_stds=2)
        ),
]


# In[129]:


fig, ax = plt.subplots(figsize=(20,22))
fig.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

table = Table(
    df,
    column_definitions=col_defs,
    index_col="Rk",
    row_dividers=True,
    row_divider_kw={"linewidth": 1, "linestyle": (0, (1,5))},
    footer_divider=True,
    textprops={"fontsize": 14},
    ax=ax
).autoset_fontcolors(colnames=["xG", "xGA", "xGD"])

for idx in [0, 1, 2, 3]: 
    table.rows[idx].set_facecolor(row_colors["top4"])

for idx in [4, 5, 6]: 
    table.rows[idx].set_facecolor(row_colors["top6"])
    
for idx in [17, 18, 19]: 
    table.rows[idx].set_facecolor(row_colors["relegation"])


# In[137]:


plt.savefig(
    "C:/Users/Habib/team logos/.png",
    facecolor=ax.get_facecolor(),
    dpi=200,
    bbox_inches="tight"
)


# In[ ]:





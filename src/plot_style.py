# src/plot_style.py

import seaborn as sns
import matplotlib.pyplot as plt

TITLE_FONT_SIZE = 14
TITLE_FONT_WEIGHT = 'bold'

def styled_countplot(
    data, 
    x=None, 
    hue=None,
    ax=None,
    order=None,
    hue_order=None,
    stat=None,
    label_type=None
):
    """
    A helper function to create countplots with homogenized styling.
    """
    # Create the countplot
    plot = sns.countplot(
        data=data, 
        x=x, 
        hue=hue,
        hue_order=hue_order,
        stat=stat,
        ax=ax, 
        order=order,
    )

    # Set axis
    if ax is None:
        ax = plt.gca()
        
    # Set title and legend based on hue value
    if hue is not None:
        ax.set_title(f'{str.title(x).replace('_', ' ')} by {str.title(hue).replace('_', ' ')}' , fontsize=TITLE_FONT_SIZE, fontweight=TITLE_FONT_WEIGHT)
        ax.legend(data[hue].unique())
    else:
        ax.set_title(str.title(x).replace('_', ' '), fontsize=TITLE_FONT_SIZE, fontweight=TITLE_FONT_WEIGHT)

    # Remove x and y labels
    ax.set_xlabel('')
    ax.set_ylabel('')

    # The grid is unnecessary with bar labels
    if label_type is not None:
        ax.grid(False) # Remove grid
        
        # The y-axis is somewhat redundant for percentage countplots
        if stat == 'percent':
            ax.set_yticks([]) # Remove y-ticks

    # Set bar labels and label colors
    if label_type == 'center':
        for container in ax.containers:
            ax.bar_label(container, fmt='%.1f%%', label_type=label_type, fontsize=9, fontweight=TITLE_FONT_WEIGHT, color='#EEEEEE')
            
    elif label_type == 'edge':
        for container in ax.containers:
            ax.bar_label(container, fmt='%.1f%%', label_type=label_type, fontsize=9, fontweight=TITLE_FONT_WEIGHT, color='black')

    return plot
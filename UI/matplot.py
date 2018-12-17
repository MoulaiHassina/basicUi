import arabic_reshaper
import matplotlib.pyplot as plt
from bidi.algorithm import get_display


reshaped_text = arabic_reshaper.reshape(u'اللغة العربية رائعة')
bidi_text = get_display(reshaped_text)

x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 9, 10]
xlbl =bidi_text
#ylbl = get_display( arabic_reshaper.reshape('الترتيبات'))
plt.bar(x, y, label='Bar1', color='red')
plt.xlabel(xlbl, fontdict=None, labelpad=None)
plt.ylabel(xlbl, fontdict=None, labelpad=None)
plt.show()
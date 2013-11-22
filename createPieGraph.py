import matplotlib.pyplot as plt
import pylab
import numpy as np

availColors= [
"aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "green", "greenyellow", "honeydew", "hotpink", "indianred ", "indigo  ", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgreen", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen", ] 
# The slices will be ordered and plotted counter-clockwise.
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs', "tan","teal","thistle","tomato","turquoise","violet"
sizes = [15, 30, 45, 10,15, 30, 45, 10,3,54 ]
colors = []
from random import randrange as rand

#for i in xrange(0,len(labels)):
#    randC = availColors[rand(0,len(availColors))]
#    colors.append(randC)
#    availColors.remove(randC)
#colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

#col = lambda x : pylab.cm.prism(x)

#step=1.0/len(labels)

#for i in np.arange(0.0,1.0, step):
#    colors.append(col(i))

colors=[
"0x9E0142", "0xD53E4F", "0xF46D43", "0xFDAE61", "0xFEE08B", "0xFFFFBF", "0xE6F598", "0xABDDA4", "0x66C2A5", "0x3288BD", "0x5E4FA2",
]


explode = (0, 0, 0, 0,0, 0, 0, 0,0,0) # only "explode" the 2nd slice (i.e. 'Hogs')

plt.pie(sizes, colors=colors, explode=explode, labels=labels,autopct='%1.1f%%', shadow=True colors=colors)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.show()

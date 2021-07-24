import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

#parse element ang get data
tree = ET.parse('output.xml')
root = tree.getroot()
data=[]
i=0
for child in root:
    row=[]
    for c in child:
        row.append(c.text)
    if(i<10):
        data.append(row)
        i+=1


#visualize data as atable usi matplotlib library
fig, ax =plt.subplots(1,1)
column_labels=["SSID", "date","Timestamp", "FPS", "Pedestrians"]
column_width=[0.1, 0.3, 0.4, 0.2, 0.3]
ax.axis('tight')
ax.axis('off')
mytable = ax.table(cellText=data,colLabels=column_labels,colWidths=column_width,loc="center")
mytable.auto_set_font_size(False)
mytable.set_fontsize(14)
mytable.scale(1,2)

plt.show()


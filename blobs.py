import streamlit as st
import random
from PIL import Image, ImageGrab
import time


st.set_page_config(layout="wide")
svg_tag = "<svg"
xmlns_tag =  "xmlns="
xmlns = "'http://www.w3.org/2000/svg'"
width_tag = "width="
height_tag = "height="
viewbox_tag = "viewBox="
path_tag="<path d="
close_tag=">"
final_close_tag="/>"
svg_close_tag = "</svg>"
path=[0 for i in range(32)]
path[0]= "M50.3,-48.7C65.1,-35.4,77,-17.7,71.7,-5.3C66.4,7.2,44,14.3,29.1,27.3C14.3,40.2,7.2,59,-6.7,65.7C-20.5,72.3,-40.9,66.9,-50.1,53.9C-59.2,40.9,-57.1,20.5,-55.2,1.9C-53.3,-16.7,-51.7,-33.4,-42.6,-46.6C-33.4,-59.8,-16.7,-69.6,0.5,-70.1C17.7,-70.6,35.4,-61.9,50.3,-48.7Z"
path[1]= "M41.3,-45.3C47.8,-34.8,43.5,-17.4,45.7,2.2C48,21.8,56.7,43.7,50.2,56.7C43.7,69.8,21.8,74.1,-0.1,74.2C-22,74.3,-44.1,70.2,-55,57.1C-65.9,44.1,-65.7,22,-59.6,6.2C-53.4,-9.7,-41.3,-19.5,-30.4,-30C-19.5,-40.5,-9.7,-51.8,3.8,-55.7C17.4,-59.5,34.8,-55.8,41.3,-45.3Z"
path[2]= "M53.2,-50.6C64.6,-41.7,66.8,-20.8,66.7,-0.1C66.6,20.6,64.2,41.2,52.7,47.7C41.2,54.1,20.6,46.4,1,45.4C-18.7,44.5,-37.4,50.3,-50.5,43.8C-63.7,37.4,-71.3,18.7,-72.7,-1.4C-74,-21.4,-69.1,-42.8,-56,-51.8C-42.8,-60.7,-21.4,-57.2,-0.3,-56.9C20.8,-56.6,41.7,-59.5,53.2,-50.6Z"
path[3]= "M48.9,-45.7C62.8,-35,73.1,-17.5,71.2,-1.9C69.4,13.8,55.3,27.5,41.4,36.5C27.5,45.4,13.8,49.5,-2.7,52.2C-19.2,54.9,-38.3,56.2,-49.8,47.3C-61.3,38.3,-65.1,19.2,-64.4,0.8C-63.6,-17.6,-58.2,-35.2,-46.7,-45.9C-35.2,-56.6,-17.6,-60.3,-0.1,-60.3C17.5,-60.2,35,-56.3,48.9,-45.7Z"
path[4]="M54,-66.9C66,-54.3,69,-33.5,68.2,-15.4C67.4,2.8,62.9,18.2,55.9,34.1C49,50,39.5,66.3,24.1,76.3C8.7,86.3,-12.7,89.9,-27.9,82.1C-43.2,74.2,-52.3,54.8,-59.3,37C-66.3,19.2,-71.1,2.9,-67.4,-10.8C-63.7,-24.5,-51.4,-35.5,-38.7,-48C-26.1,-60.4,-13,-74.3,4,-79C21,-83.8,42,-79.4,54,-66.9Z"
path[5]="M44.8,-52.1C55.7,-44.3,60.6,-27.9,66.2,-9.7C71.7,8.6,78.1,28.6,71.7,43.1C65.4,57.6,46.4,66.4,28.6,68.5C10.8,70.6,-5.8,66.1,-19,58.5C-32.1,50.9,-41.9,40.4,-49.8,28.1C-57.8,15.7,-64,1.7,-64.9,-14.6C-65.7,-30.8,-61.2,-49.2,-49.5,-56.9C-37.8,-64.6,-18.9,-61.5,-1,-60.4C17,-59.2,33.9,-59.9,44.8,-52.1Z"
path[6]="M45.6,-36C58.7,-19.9,68.7,-1,65.2,15C61.6,30.9,44.5,43.9,25.7,52.7C6.9,61.4,-13.5,66,-33.7,60.1C-53.9,54.2,-73.8,37.8,-76.8,19.2C-79.7,0.5,-65.7,-20.3,-50.1,-37C-34.4,-53.6,-17.2,-66,-0.5,-65.6C16.3,-65.3,32.5,-52.1,45.6,-36Z"
path[7]="M42.5,-34.7C56.4,-16.4,70.1,1.4,66.9,15.3C63.7,29.2,43.7,39.3,24.3,47.4C4.9,55.6,-13.9,61.8,-31.6,56.7C-49.3,51.7,-65.9,35.2,-67.7,18.1C-69.4,1,-56.3,-16.7,-42.6,-35C-28.8,-53.2,-14.4,-71.9,-0.1,-71.8C14.3,-71.8,28.5,-53,42.5,-34.7Z"
path[8]="M49.6,-38.5C57.9,-29.1,53.9,-8.9,50.3,13.4C46.7,35.6,43.6,59.8,31,66.7C18.5,73.6,-3.5,63.2,-22.2,52C-40.9,40.7,-56.4,28.6,-57.3,15.7C-58.2,2.7,-44.5,-10.9,-32.5,-21.1C-20.6,-31.3,-10.3,-38.1,5.2,-42.2C20.6,-46.4,41.3,-47.9,49.6,-38.5Z"
path[9]="M46.5,-45.3C59.8,-33.2,69.7,-16.6,66,-3.8C62.2,9.1,44.7,18.1,31.4,29.3C18.1,40.5,9.1,53.7,-5.3,59.1C-19.7,64.4,-39.4,61.7,-53.5,50.6C-67.7,39.4,-76.2,19.7,-71.9,4.3C-67.7,-11.1,-50.5,-22.3,-36.4,-34.4C-22.3,-46.4,-11.1,-59.4,2.7,-62.2C16.6,-64.9,33.2,-57.4,46.5,-45.3Z"
path[10]="M47.9,-51.5C58.8,-36.9,62.3,-18.5,60.4,-1.9C58.4,14.6,51.1,29.2,40.2,43.4C29.2,57.6,14.6,71.4,-4.4,75.8C-23.3,80.1,-46.7,75.1,-58.2,60.9C-69.6,46.7,-69.2,23.3,-65.3,3.9C-61.5,-15.6,-54.2,-31.2,-42.7,-45.8C-31.2,-60.3,-15.6,-73.8,1.4,-75.2C18.5,-76.6,36.9,-66,47.9,-51.5Z"
path[11]="M39.3,-37C51,-27.7,60.6,-13.8,62.5,1.9C64.4,17.6,58.7,35.3,47,46.1C35.3,56.9,17.6,60.9,-2.2,63.1C-22.1,65.3,-44.2,65.8,-58.2,55C-72.1,44.2,-77.9,22.1,-73.4,4.6C-68.8,-13,-53.8,-25.9,-39.9,-35.2C-25.9,-44.5,-13,-50.2,0.4,-50.6C13.8,-51.1,27.7,-46.3,39.3,-37Z"
path[12]="M64.7,-52.1C80.1,-32.3,86.3,-5.6,78.6,13.8C70.9,33.2,49.2,45.2,30.7,48.1C12.2,51.1,-3.2,44.8,-20.1,38.1C-37.1,31.4,-55.6,24.1,-60.5,11.3C-65.4,-1.5,-56.7,-19.9,-44.4,-39C-32,-58.2,-16,-78,4.3,-81.5C24.6,-84.9,49.3,-71.9,64.7,-52.1Z"
path[13]="M38.3,-33.8C47.7,-18.8,52.1,-2.9,49.2,11.7C46.2,26.4,35.9,39.9,20.6,50C5.3,60.2,-15.1,67,-35.6,61.8C-56,56.6,-76.5,39.3,-79,20.4C-81.4,1.4,-65.8,-19.3,-49.6,-35.9C-33.5,-52.4,-16.7,-64.8,-1.1,-63.9C14.5,-63,28.9,-48.8,38.3,-33.8Z"
path[14]="M53.9,-45C67.2,-26.3,73.6,-4,69.9,17.5C66.2,39,52.5,59.9,34,67.6C15.5,75.4,-7.9,70.1,-23.5,58.8C-39.1,47.4,-46.9,30,-48.6,13.7C-50.3,-2.7,-45.8,-17.8,-36.7,-35.6C-27.6,-53.4,-13.8,-73.8,3.3,-76.4C20.3,-79,40.6,-63.8,53.9,-45Z"
path[15]="M40,-50C48.3,-40.6,49.1,-24.7,54.9,-7.4C60.7,9.9,71.4,28.7,68,43.7C64.6,58.8,47.2,70.2,29.6,72.9C12.1,75.5,-5.5,69.4,-20.4,61.6C-35.3,53.8,-47.6,44.2,-58.3,31C-69.1,17.9,-78.2,1.2,-76.6,-14.4C-74.9,-30,-62.3,-44.7,-47.7,-52.9C-33.2,-61.2,-16.6,-63.2,-0.4,-62.8C15.8,-62.3,31.6,-59.4,40,-50Z"
path[16]="M58.5,-58.6C74.5,-56.3,85.1,-36.6,81.4,-19.9C77.7,-3.3,59.6,10.4,46.2,20.3C32.9,30.2,24.2,36.5,14.6,40C4.9,43.6,-5.8,44.4,-21.6,44.9C-37.4,45.4,-58.4,45.6,-66.5,36.2C-74.6,26.7,-69.7,7.7,-63.8,-8.7C-57.9,-25.1,-50.9,-38.7,-40.1,-41.9C-29.3,-45,-14.7,-37.5,3.3,-41.5C21.3,-45.4,42.6,-60.8,58.5,-58.6Z"
path[17]="M33.1,-39C36.8,-21.7,29.6,-8.3,28.7,10.9C27.8,30.1,33.2,55.2,24.7,64.3C16.1,73.5,-6.4,66.7,-28.3,56.9C-50.2,47.1,-71.4,34.1,-76.1,16.6C-80.7,-1,-68.8,-23.1,-53.3,-43.1C-37.8,-63,-18.9,-80.8,-2.1,-79.1C14.7,-77.4,29.4,-56.3,33.1,-39Z"
path[18]="M29,-26.7C35.7,-14.7,38,-2.7,38.6,14.5C39.2,31.8,38.2,54.4,27.7,60.6C17.2,66.9,-2.6,56.8,-22,47C-41.4,37.1,-60.4,27.6,-68,10.8C-75.5,-5.9,-71.7,-30,-58.4,-43.5C-45.2,-57,-22.6,-60,-5.7,-55.4C11.1,-50.9,22.3,-38.8,29,-26.7Z"
path[19]="M58.9,-30.5C67.8,-18.6,60.6,6.1,48.1,21.3C35.5,36.6,17.8,42.4,2.8,40.8C-12.2,39.2,-24.3,30.1,-33.1,17.1C-41.8,4,-47,-13.1,-40.9,-23.3C-34.8,-33.5,-17.4,-36.9,3.8,-39.1C25,-41.3,50,-42.3,58.9,-30.5Z"
path[20]="M33.6,27.2C20.7,41.8,-28.5,43.3,-40.1,29.4C-51.8,15.5,-25.9,-13.8,-1.3,-14.6C23.3,-15.3,46.6,12.5,33.6,27.2Z"
path[21]="M40.1,25.4C25.9,47.6,-29.5,48.3,-43.1,26.4C-56.6,4.5,-28.3,-40,-0.6,-40.3C27.1,-40.7,54.2,3.1,40.1,25.4Z"
path[22]="M43.9,23.9C37.9,35.9,0.7,28.5,-11.8,12.8C-24.4,-3,-12.2,-27,6.4,-23.3C25,-19.6,50,11.9,43.9,23.9Z"
path[23]="M62,-47.5C76.2,-31.7,80.5,-6.2,75.1,17C69.7,40.2,54.6,61,36.1,66.8C17.6,72.6,-4.2,63.3,-25.6,53.1C-46.9,42.8,-67.7,31.5,-70.1,17.1C-72.5,2.7,-56.5,-14.8,-41.8,-30.8C-27,-46.7,-13.5,-61.1,5.2,-65.3C23.9,-69.5,47.9,-63.4,62,-47.5Z"
path[24]="M35,-50.7C46.9,-39.6,59,-31.4,63,-20.2C67,-9,62.9,5,59.9,21.1C57,37.2,55.2,55.4,45.4,64.2C35.6,73.1,17.8,72.7,1.5,70.6C-14.7,68.5,-29.4,64.6,-44.9,57.6C-60.5,50.6,-76.8,40.4,-82.6,26C-88.4,11.6,-83.7,-7,-73.2,-19C-62.8,-31,-46.5,-36.4,-33.4,-47C-20.2,-57.7,-10.1,-73.7,0.7,-74.7C11.6,-75.7,23.2,-61.8,35,-50.7Z"
path[25]="M41.5,-16.2C47.9,6.5,43.4,30,25.3,45.7C7.3,61.3,-24.3,69.2,-42.9,56.3C-61.4,43.5,-66.9,10,-57.6,-16.6C-48.2,-43.2,-24.1,-63,-3.3,-61.9C17.5,-60.8,35,-38.9,41.5,-16.2Z"
path[26]="M47.6,-22.4C50.6,-6.1,34.4,9.4,13.5,26.5C-7.4,43.5,-33,62.1,-43,55.6C-53,49.2,-47.4,17.8,-37.7,-7.7C-27.9,-33.3,-13.9,-53,4.2,-54.4C22.3,-55.7,44.5,-38.7,47.6,-22.4Z"
path[27]="M43.9,-58.4C53.1,-44.7,54,-27.2,53.6,-12.1C53.1,3,51.3,15.8,45.8,27.5C40.3,39.2,31.2,50,18.7,57C6.1,64,-9.8,67.4,-27.7,65.5C-45.6,63.6,-65.4,56.4,-71.2,42.8C-77,29.3,-68.7,9.3,-59,-4.3C-49.3,-17.9,-38.3,-25.2,-28.2,-38.7C-18.2,-52.2,-9.1,-72,4.2,-76.9C17.4,-81.9,34.8,-72,43.9,-58.4Z"
path[28]="M42,-30.8C52.3,-20.5,57.2,-3.2,53,10.9C48.9,25.1,35.7,36,19.6,45.7C3.4,55.4,-15.7,63.9,-34.9,59.6C-54.1,55.3,-73.3,38.2,-80,16.2C-86.7,-5.8,-80.8,-32.8,-65.4,-44.2C-49.9,-55.6,-25,-51.4,-4.6,-47.8C15.8,-44.1,31.6,-41,42,-30.8Z"
path[29]="M54.9,-41.9C66.5,-29.2,68.2,-6.6,60.5,8.6C52.9,23.8,36,31.7,19.4,39.5C2.7,47.2,-13.7,54.8,-31.3,51.5C-48.9,48.2,-67.7,34,-75.6,13.2C-83.5,-7.5,-80.6,-34.7,-66.1,-48C-51.7,-61.3,-25.9,-60.7,-2.1,-59C21.6,-57.3,43.3,-54.6,54.9,-41.9Z"
path[30]="M60.3,-46.8C73.7,-31.3,77.1,-6.5,70,12.5C62.9,31.5,45.4,44.7,25.2,55.7C5.1,66.6,-17.8,75.4,-35.6,68.8C-53.5,62.2,-66.3,40.1,-67.9,19.4C-69.5,-1.3,-59.8,-20.6,-46.6,-36.1C-33.4,-51.6,-16.7,-63.2,3.4,-65.8C23.5,-68.5,46.9,-62.3,60.3,-46.8Z"
#path[31]= "M480.8 168.7C524.5 210.6 543.4 285.2 528.9 353.7 514.5 422.2 466.7 484.5 409.7 502.2 352.6 519.8 286.4 492.8 237.5 458.3 188.6 423.8 157 381.8 142.2 331.7 127.4 281.7 129.2 223.5 158.3 184.9 187.4 146.2 243.7 127.1 306.1 122.2 368.5 117.3 437.1 126.7 480.8 168.7Z"
#colour ="fill='#FE940E'"
submit = st.button('Capture screen')
st.markdown("<html><body>",unsafe_allow_html=True)
col_count = 20
row_count = 20
cols = st.beta_columns(col_count) # number of columns in each row! = 2
for i in range(row_count): # number of rows in your table! = 2
    for j in range(col_count):
        width = random.randrange(100,200)
        height = random.randrange(100,200)
        view_1 = str(random.randrange(-80, -60))
        view_2 = str(random.randrange(-80, -60))
        view_3 = str(random.randrange(300, 410))
        view_4 = str(random.randrange(300, 410))
        col = str(random.randrange(500,999)) #colour
        colour="fill='#FE"+col+"E'"
        viewwidth=','.join([view_1,view_2,view_3,view_4])
        viewbox = "'"+viewwidth+"'"
        path_d="'"+str(path[random.randrange(0, 31)])+"'"
        svg_string ="<div>"+ svg_tag + ' ' + xmlns_tag+ xmlns+' '+  width_tag+ str(width) + ' '+ height_tag+str(height)+ ' ' +viewbox_tag +viewbox+ close_tag +' '+ path_tag + path_d+' '+ colour+ ' '+final_close_tag+"transform = translate(10,10)"+svg_close_tag+"</div>"
        cols[j].markdown(svg_string, unsafe_allow_html=True)

st.markdown("</body></html>",unsafe_allow_html=True)
# part of the screen

a = 0
if submit:
    z = str(random.randrange(1,1000000000))
    time.sleep(2)
    im=ImageGrab.grab(bbox=(100,350,2500,4500))
    #im.show()
    im.save(z+".png", dpi=(8000,6400))
    img = Image.open(z+".png")
    imga = img.convert("RGBA")
    datas = imga.getdata()

    newData = list()
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append([255, 255, 255, 0])
        else:
            newData.append(item)

    imgb = Image.frombuffer("RGBA", imga.size, newData, "raw", "RGBA", 0, 1)
    imgb.save(z+".png", "PNG")

# to file

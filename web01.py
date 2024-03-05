import streamlit as st
import pandas as pd
import io
import base64
from PIL import Image

bg_image_path = "background/bg7.jpg"
with open(bg_image_path, "rb") as img_file:
    bg_image = img_file.read()
bg_image_base64 = base64.b64encode(bg_image).decode()
blur_intensity = "4px"
page_bg_img = f'''
        <style>
           .stApp {{
                   background-image: url("data:image/png;base64,{bg_image_base64}");
                   background-size: cover;
           }}
           .stApp::before {{
                   content: "";
                   position: fixed;
                   top: 0;
                   right: 0;
                   bottom: 0;
                   left: 0;
                   background-image: url("data:image/png;base64,{bg_image_base64}");
                   background-size: cover;
                   filter: blur({blur_intensity});
           }}
        </style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
        menu_selection = st.sidebar.radio("เมนู", ["Login","create account","Home"])
        
        if menu_selection == "Login":
                def read_excel_data(file_path):
                        df = pd.read_excel(file_path)
                        return df 
                    
                def login(username, password, user_data):
                        for index, row in user_data.iterrows():
                            if row["username"] == username and row["password"] == password:
                                return True
                        return False
                    
                def main():
                        user_data_file = "user_data1.xlsx"  # แทนที่ด้วยชื่อไฟล์ Excel 
                        user_data = read_excel_data(user_data_file)
                    
                        show_login = True
                    
                        if show_login:
                                st.title("Login")
                                entered_username = st.text_input("Username")
                                entered_password = st.text_input("Password", type="password")
                                st.markdown("[Sing In](https://forms.gle/bhRsg59rZ3zexxKw7)")
                                                    
                                if st.button("Login"):
                                        if login(entered_username, entered_password, user_data):
                                            st.success("Login successful!")
                                            show_login = False
                                        else:
                                            st.error("Invalid username or password")
                    
                if __name__ == "__main__":
                        main()
                                    
        elif menu_selection == "create account" :
                def main(show_login):
                        if show_login:
                                st.title("Create Account")
                                entered_username = st.text_input("Username")
                                #entered_password = st.text_input("Enter Password", type="password")
                                entered_email = st.text_input("Email")
                                entered_phone = st.text_input("Phone Number")
                                #st.markdown("[Create Account](https://forms.gle/bhRsg59rZ3zexxKw7)")
                                uploaded_image = st.file_uploader("Upload Profile ", type=["jpg", "png"])
                                if uploaded_image is not None:
                                        image = Image.open(io.BytesIO(uploaded_image.read()))
                                        image = image.resize((720, 720))
                                        st.image(image, caption="Uploaded Image", use_column_width=True)
                
                        
                                if st.button("Create Account"):
                                    st.success("Account Created Successfully!")
                                    if uploaded_image is not None:
                                        st.image(image, caption="Profile Picture", use_column_width=True)
                                    st.success("Account Created Successfully!")
                                    st.write("Username:", entered_username)
                                    st.write("Email:", entered_email)
                                    st.write("Phone Number:", entered_phone)
                                    
                        
                if __name__ == "__main__":
                    show_login = True
                    main(show_login)
                                        
        elif menu_selection == "Home":
                st.header(':green[จังหวัดอุบลราชธานี]  :car::tulip:')
                video_file = open('video/video.mp4','rb').read()
                #caption="จาก YOUTUBE ช่อง SMOKE STUDIO",
                st.video(video_file)
                cols = st.columns(2)
                st.markdown(''':green[อุบลราชธานี] เป็นจังหวัดใหญ่ในภาคตะวันออกเฉียงเหนือ  มีสถานที่ท่องเที่ยวประจำจังหวัดที่น่าสนใจมากมาย เช่น :red[อุทยานแห่งชาติผาแต้ม หน้าผาสูงที่มีความสวยงามตามธรรมชาติ ด้านข้างหน้าผามีภาพเขียนสีก่อนประวัติศาสตร์ที่มีอายุไม่ต่ำกว่าสามพันถึงสี่พันปี น้ำตกห้วยทรายใหญ่ น้ำตกที่สวยงามแห่งหนึ่งของอีสาน ปราสาทบ้านเบ็ญ] ศาสนสถานขอมขนาดย่อม ประกอบด้วยปรางค์อิฐ 3 หลัง  ตั้งอยู่บนฐานศิลาแลง ที่สร้างแยกกัน
                
หรือถ้าใครชื่นชอบเรื่องงานประเพณีก็พลาดไม่ได้กับ:red[ประเพณีแห่เทียนพรรษา] งานบุญที่ยิ่งใหญ่ที่สุดของจังหวัดอุบลราชธานีที่จัดขึ้นในวันอาสาฬหบูชาและวันเข้าพรรษาของทุกปี ในงานจะมีการประกวดเทียนแกะสลัก และมีการแห่เทียนอย่างยิ่งใหญ่ สร้างความตื่นตาตื่นใจให้กับนักท่องเที่ยว
                
และที่พลาดไม่ได้เลยคือของฝากประจำจังหวัดที่ขึ้นชื่อ :red[อย่างผ้าฝ้ายทอมือ หมอนขิด ผ้าขาวม้า ผ้าไหม หรือเครื่องทองเหลือง] ก็ถือเป็นสินค้าที่ได้รับความนิยมจากนักท่องเที่ยวชาวต่างชาติเป็นอย่างมาก หรือถ้าเป็นนักเดินทางสายกินก็พลาดไม่ได้ที่จะลองลิ้มรสหมูยอ กุนเชียง ไส้กรอกอีสาน หรืออาหารหลนต่าง ๆ ''')
                    
                cols = st.columns(3)
                with cols[0]:
                    GoogleMaps = "https://maps.app.goo.gl/gcaX8qzdUsroe71W7"
                    st.link_button(''':green[Google Maps]''',GoogleMaps)
                    
                with cols[1]:   
                    web_facebook = "https://web.facebook.com/prubon?locale=th_TH"
                    st.link_button(''':blue[web facebook]''',web_facebook)
                    
                with cols[2]:    
                    website = "https://ubonratchathani.go.th/home/"
                    st.link_button(''':red[website]''',website)
                
                tab1, tab2, tab3, tab4 = st.tabs(["โรงแรมยอดฮิต","สถานที่ท่องเที่ยว","ค่าเฟ่","ร้านนั่งชิล"])    
                with tab1:
                        st.header("โรงแรมยอดฮิต")
                        #st.subheader("Minimalist Products")
                        st.image('image/ubu2.jpg')
                        st.markdown(" ")
                        
                        col1, col2, col3 = st.columns(3)
                        
                        
                        original1 = Image.open("image/image1.jpg")
                        col1.write(''':green[โรงแรม เดอ ลีท (de Lit Hotel)]''')
                        col1.image(original1, caption=''' ''', use_column_width=True)
                        col1.markdown(''':black[โรงแรม เดอ ลีท (de Lit Hotel) - ที่พักในเมืองอุบลฯ ไปเช็คอินกันที่แรกสำหรับใครที่แพลนมาเที่ยวอุบลฯ แต่ยังติดใจกับที่พักริมชายหาดแถวทะเลหัวหินอยู่ล่ะก็ขอแนะนำ de Lit Hotel ที่พักโทนสีฟ้าขาวสบายตา อยู่ใกล้วัดดังอย่างพระธาตุหนองบัวและตลาดไนท์สุนีย์แกรนด์ มาในคอนเซ็ปต์เมดิเตอร์เรเนียนหนึ่งเดียวในอุบลฯ ที่ไม่ว่าเราจะเดินไปตรงไหนก็อดคิดไม่ได้จริงๆ ว่าตอนนี้เราอยู่ที่อุบลหรือหัวหิน ซึ่งจุดเด่นเขาก็อยู่ที่ตัวห้องพักบริเวณชั้น 1 ที่นอกจากจะถูกตกแต่งด้วยดีไซน์สุดเก๋แล้ว แค่เพียงเปิดประตูออกมาก็สามารถเดินลงสระว่ายน้ำได้จากหน้าห้องพักเลย รวมถึงมีบริการร้านอาหารและคาเฟ่ภายในโรงแรมด้วยนะ เรียกได้ว่าสะดวกครบครันสุดๆ ไปเลย] ''')
                        GoogleMaps = "https://maps.app.goo.gl/A5qJEbDoVy184kfe6"
                        web_facebook = "https://web.facebook.com/DelitUbon/?locale=th_TH&_rdc=1&_rdr"
                        website = "https://www.booking.com/hotel/th/de-lit.en-gb.html?aid=311984&label=de-lit-5sVzpWE8nEe1JB0jpXDs6gS590196865351%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-168606366032%3Alp9074826%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YbSsBl3MCvHsD8UKUHIRFxY&sid=8c86a85ab54afab8d7a61beb1b8c2800&dest_id=-3256831;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1709565611;srpvid=c84b6bd06b920289;type=total;ucfs=1&#hotelTmpl"
                        col1.link_button(''':green[Google Maps]''',GoogleMaps)
                        col1.link_button(''':blue[web facebook]''',web_facebook)
                        col1.link_button(''':blue[website]''',website)
                        
                
                        original2 = Image.open("image/image2.jpg")
                        col2.write(''':green[เดอะกู๊สเฮาท์ อุบล(The Goose House Ubon)]''')
                        col2.image(original2, caption=" ", use_column_width=True)
                        col2.markdown('''เดอะกู๊สเฮาท์ อุบล (The Goose House Ubon) ที่พักในเมืองอุบลฯพาไปเช็คอินกันต่อแถวๆ  ถนนสรรพสิทธ์ถนนสายหลักที่รายล้อมด้วยสถานศึกษาของจังหวัดอุบลฯ กันที่ เดอะกู๊สเฮาท์ อุบล  เปิดให้บริการห้องพักแบบ Bed&Breakfast ขนาดจิ๋วแต่แจ๋วตกแต่งเรียบง่ายสไตล์มินิมอล มีห้องพักให้บริการทั้งหมด 6 ห้อง 6 สไตล์แบบไม่ซ้ำกัน รวมถึงมีห้องพักแบบ Mixed Dormitory ห้องพักรวมสำหรับ 4 คน ที่สามารถพักได้ทั้งชายและหญิง ภายในที่พักยังเปิดเป็นคาเฟ่ชิคๆ สุดน่ารักที่เน้นบริการอาหารเครื่องดื่มที่ใช้วัตถุดิบที่หามาได้จากภาคอีสานบ้านเฮาด้วยเด้ออ ''')
                        col2.markdown('''''')
                        GoogleMaps = "https://maps.app.goo.gl/BuRTPc2h5qz2paoo8"
                        web_facebook = "https://web.facebook.com/thegoosehouseubon/?locale=th_TH&_rdc=1&_rdr"
                        website = "https://www.agoda.com/en-za/the-goose-cafe-and-hostel-ubon/hotel/ubon-ratchathani-th.html?site_id=1826363&tag=523455c0-f3f7-4b79-acc1-a892778f319c&gad_source=1&device=c&network=g&adid=347518904776&rand=6038747041816566718&expid=&adpos=&gclid=CjwKCAiA3JCvBhA8EiwA4kujZpTSBJF3VNFe6qnvG9AEsrobYU42y9qHnTbew2FhHLcMRnJYeg-zqhoCH3oQAvD_BwE&pslc=1&ds=P7tUMzzabfUnHCgN"
                        col2.link_button(''':green[Google Maps]''',GoogleMaps)
                        col2.link_button(''':blue[web facebook]''',web_facebook)
                        col2.link_button(''':blue[website]''',website)
                        
                
                        original3 = Image.open("image/image3.jpg")
                        col3.write(''':green[ยู โฮเทล อุบลราชธานี (Yuu Hotel)]''')
                        col3.image(original3, caption="", use_column_width=True)
                        col3.markdown('''ยู โฮเทล อุบลราชธานี (Yuu Hotel)- ที่พักในเมืองอุบลฯยูโฮเทล อุบลฯ ที่พักสุดชิคใจกลางเมืองอุบลฯ อยู่ใกล้สนามบินและห่างจากทุ่งศรีเมืองสวนสาธารณะใจกลางอุบลฯเพียง 5 นาทีเท่านั้น ตัวที่พักตกแต่งด้วยสไตล์เฟรนช์โคโลเนียล (French Colonial) ซึ่งได้แรงบันดาลใจมาจากเมืองปากเซ ประเทศลาว เมื่อเข้าไปด้านในแล้วเหมือนกับเราได้ย้อนเวลาเข้าไปในยุโรปช่วงยุคโบราณเลยล่ะค่า ภายในที่พักยังเปิดเป็นคาเฟ่เก๋ๆ สไตล์ยุโรปที่มีบริการเครื่องดื่มและขนมอร่อยๆ รวมถึงไอศกรีมโฮมเมดอีกด้วย แล้วที่นี่เขายังใจดีมีบริการให้ยืมจักรยานปั่นฟรีให้เราได้ปั่นไปไหว้พระในตัวเมืองได้ด้วย''')
                        GoogleMaps = "https://maps.app.goo.gl/WboxohWt3YtBNCMC8"
                        web_facebook = "https://web.facebook.com/yuuhotelandcafe/?locale=th_TH&_rdc=1&_rdr"
                        website = "https://th.trip.com/hotels/ubon-ratchathani-hotel-detail-5633221/yuu-hotel-ubon-ratchathani/?cityId=6160&checkIn=2024-03-04&checkOut=2024-03-05&adult=2&children=0&subStamp=3001547&crn=1&ages=&travelpurpose=0&curr=THB&hasAidInUrl=true&link=title&hoteluniquekey=&subChannel=&masterhotelid_tracelogid=4721066d9c7545a5b8b66f4130e44f20&NewTaxDescForAmountshowtype0=F&detailFilters=17%7C1~17~1&hotelType=meta"
                        col3.link_button(''':green[Google Maps]''',GoogleMaps)
                        col3.link_button(''':blue[web facebook]''',web_facebook)
                        col3.link_button(''':blue[website]''',website)
                        
                        col4, col5, col6 = st.columns(3)
                
                        col4.markdown(" ")
                        
                        original4 = Image.open("image/image4.jpg")
                        col4.write(''':green[วี โฮเทล อุบลฯ (V Hotel Ubon)]''')
                        col4.image(original4, caption="", use_column_width=True)
                        col4.markdown('''วี โฮเทล อุบลฯ (V Hotel Ubon) - ที่พักในเมืองอุบลฯ พาไปเช็คอินกันต่อในที่พักราคาเริ่มต้นหลักร้อยแต่ได้ห้องกว้างสุดๆ กันที่ วี โฮเทล อุบลฯ ซึ่งมาในคอนเซ็ปต์ Modern Contemporery ที่ผสานความร่วมสมัยและดีไซน์โมเดิร์นเข้าไว้ด้วยกันอย่างลงตัว ตอบโจทย์ไลฟ์สไตล์นักเดินทางรุ่นใหม่ที่ชอบที่พักดีไซน์สวยเก๋ ทันสมัย ในราคาที่คุ้มค่า ตั้งอยู่บนถนนแจ้งสนิทใกล้วงเวียนหอนาฬิกา ศูนย์การค้าเอสเค ปาร์ค และวัดพระธาตุหนองบัว จุดเด่นของที่นี่ที่ใครก็ต้องติดใจอยู่อาหารเช้าแบบชาวอุบลฯ ที่มีให้เลือกทั้งไข่กระทะ ต้มเลือดหมู และก๋วยจั๊บญวนสูตรเด็ดของคุณแม่ บอกเลยว่าถ้ามาอุบลฯ ต้องมาทานให้ได้เลยน้า''')
                        GoogleMaps = "https://maps.app.goo.gl/vXGgTQtS8ErMPpfz7"
                        web_facebook = "https://web.facebook.com/vhotelubon/?_rdc=1&_rdr"
                        website = "https://www.vhotelthailand.com/?fbclid=IwAR20jwEmIfp60-ICK2t8eLh7ECcp_VkmEOfZi87IH0IK2-jcO_pffs8HGes"
                        col4.link_button(''':green[Google Maps]''',GoogleMaps)
                        col4.link_button(''':blue[web facebook]''',web_facebook)
                        col4.link_button(''':blue[website]''',website)
                        
                        col5.markdown(" ")
                
                        original5 = Image.open("image/image5.jpg")
                        col5.write(''':green[โรงแรมระพีพรรณ วิลล์ (Rapeepan Ville)]''')
                        col5.image(original5, caption="", use_column_width=True)
                        col5.markdown('''โรงแรมระพีพรรณ วิลล์ (Rapeepan Ville)- ที่พักในเมืองอุบลฯโรงแรมระพีพรรณ วิลล์ ตั้งอยู่บนถนนสุขาอุปถัมภ์ในทำเลที่เงียบสงบในตัวเมืองอุบลราชธานีใกล้ห้างสรรพสินค้าชั้นนําอย่างเซ็นทรัลและวัดพระธาตุหนองบัว อีกทั้งใกล้ๆ โรงแรมก็ยังมีร้านค้า ร้านของกินมากมาย ตัวโรงแรมตกแต่งด้วยสไตล์บูทีคโฮเทลรายล้อมไปด้วยต้นไม้สีเขียวนานาชนิด การตกแต่งภายในห้องพักเน้นเฟอร์นิเจอร์ไม้สีน้ำตาลดูอบอุ่นมาพร้อมสิ่งอำนวยความสะดวกครบครัน มีลานจอดรถและร้านอาหารให้บริการภายในโรงแรม และจุดเด่นของที่นี่ที่ใครๆ เขาก็ว่ากันปากต่อปากคือความสะอาดภายในที่พักและได้รับการบริการที่ดี พนักงานยิ้มแย้มแจ่มใส ''')
                        GoogleMaps = "https://maps.app.goo.gl/iZDbqPjQfFtvbofv6"
                        web_facebook = "https://web.facebook.com/rapeepanville/?locale=th_TH&_rdc=1&_rdr"
                        website = "http://rapeepanvill.com/?fbclid=IwAR1za4uxmsdYSZJ3WjPM78oLRdESIRDIZ4Udlma3eQFtxhePk9KTlZwZQ-Y"
                        col5.link_button(''':green[Google Maps]''',GoogleMaps)
                        col5.link_button(''':blue[web facebook]''',web_facebook)
                        col5.link_button(''':blue[website]''',website)
                        
                        col6.markdown(" ")
                
                        original6 = Image.open("image/image6.jpg")
                        col6.write(''':green[โรงแรมเดอพราวด์ (De’ Proud Hotel)]''')
                        col6.image(original6, caption="", use_column_width=True)
                        col6.markdown('''โรงแรมเดอพราวด์ (De’ Proud Hotel)- ที่พักในเมืองอุบลฯ ใครเบื่อห้องพักแบบเดิมๆ มาทางนี้เลยจ้า ทริปอุบลฯ ครั้งนี้เราจะพาไปพักกันที่ โรงแรมเดอพราวด์ ตั้งอยู่ในอ.เมืองอุบลฯ ใกล้วัดพระธาตุหนองบัวและตลาดโต้รุ่ง อุบลสแควร์ ตัวโรงแรมเป็นอาคาร 4 ชั้น มีที่จอดรถภายในอาคาร ด้านในโรงแรมเน้นการตกแต่งที่หลากหลายสไตล์ ทั้งสไตล์โมเดิร์น สไตล์ลอฟท์  และสไตล์อีสานบ้านเฮาให้เข้ากับบรรยากาศของเมืองอุบลฯ  บอกเลยว่าต้องถูกใจกันทุกเพศทุกวัยกันแน่นอน ที่สำคัญที่โรงแรมนี้เขายังใจดีให้เราได้ใช้บริการฟิตเนสได้ฟรีอีกด้วยน้า ใครติดออกกำลังกายทุกเช้าเย็นล่ะก็แนะนำเลยจ้า''')
                        GoogleMaps = "https://maps.app.goo.gl/gkGxcUu3LRjbAhKV6"
                        web_facebook = "https://web.facebook.com/theproudhotelub/?_rdc=1&_rdr"
                        website = "https://www.agoda.com/de-proud-hotel/hotel/ubon-ratchathani-th.html?cid=1844104&ds=yjP2JjcnfPkcRyIq"
                        col6.link_button(''':green[Google Maps]''',GoogleMaps)
                        col6.link_button(''':blue[web facebook]''',web_facebook)
                        col6.link_button(''':blue[website]''',website)
                        
                        col7, col8, col9 = st.columns(3)
                
                        col7.markdown(" ")
                        
                        original7 = Image.open("image/image7.jpg")
                        col7.write(''':green[Six.Eleven Ubon (หกสิบเอ็ด โฮเทล)]''')
                        col7.image(original7, caption="", use_column_width=True)
                        col7.markdown('''Six.Eleven Ubon (หกสิบเอ็ด โฮเทล)- ที่พักในเมืองอุบลฯ ปิดท้ายที่พักในเมืองกันแบบราคาน่ารักๆ 500 บาท ทุกห้อง ทั้งปี!! แต่ได้ห้องกว้าง สวย และถูกใจสุดๆ ที่ หกสิบเอ็ด โฮเทล ตั้งอยู่ในซอยสุขาอุปถัมภ์ 11 ใกล้ร้านค้า ร้านอาหาร คาเฟ่ และห้างสรรพสินค้าชั้นนําอย่างเซ็นทรัลและวัดพระธาตุหนองบัว ตัวที่พักตกแต่งในสไตล์โคซี่ลอฟท์ บริการห้องพักทั้งหมด 21 ห้อง ซึ่งอยู่ในอาคาร 3 ชั้น และอาคาร 1 ชั้น  ที่เพรียบพร้อมไปด้วยสิ่งอำนวยความสะดวกพื้นฐาน มีที่จอดรถและห้องกาแฟให้นั่งชิลๆ จิบกาแฟ ทานขนมได้ฟรีๆ ทั้งวันเลยล่ะค่ะ หากใครกำลังมองหาที่พักราคาเบาๆ สบายกระเป๋าบอกเลยว่าที่นี่คุ้มค่าสุดๆ เลยจ้า''')
                        GoogleMaps = "https://maps.app.goo.gl/aE3mf1rS8PExMuwk8"
                        web_facebook = "https://web.facebook.com/hotel611ubon/?locale=th_TH&_rdc=1&_rdr"
                        website = "https://611ubonhotel.wixsite.com/website?fbclid=IwAR1UtdTJpr6WyQbpnfeSLRIU81hjNlrBLH1FkD4F-CQmjpY0v4ZrqN3yjdU"
                        col7.link_button(''':green[Google Maps]''',GoogleMaps)
                        col7.link_button(''':blue[web facebook]''',web_facebook)
                        col7.link_button(''':blue[website]''',website)
                        
                        col8.markdown(" ")
                
                        original8 = Image.open("image/image8.jpg")
                        col8.write(''':green[อยู่ด้วยกัน การ์เด้น โฮม (U Duay Gan Garden Home)]''')
                        col8.image(original8, caption="", use_column_width=True)
                        col8.markdown('''อยู่ด้วยกัน การ์เด้น โฮม (U Duay Gan Garden Home) - อ.วารินชําราบ อยู่ด้วยกัน การ์เด้น โฮม (U Duay Gan Garden Home) ที่พักสไตล์โมเดิร์นให้บรรยกาศบ้านสวนเหมือนกับเรามาพักบ้านญาติต่างจังหวัด ตั้งอยู่ในตัวเมืองวารินชำราบซึ่งเป็นอำเภอที่ติดกับตัวอำเภอเมืองอุบล มีบริการห้องพักทั้งหมด 43 ห้อง อยู่บนตัวอาคาร 3 ชั้น ภายในมาพร้อมสิ่งอำนวยความสะดวกครบครัน มีบริการอาหารเช้าบริการแลลฉบับของคนอุบลฯ ให้เลือกอย่าง ก๋วยจั๊บญวน ข้าวต้มกระดูกหมู ขนมปังปิ้ง ไข่กระทะ รวมถึงมีบริการคาเฟ่ภายในห้องพัก จุดเด่นของที่นี่คือตั้งอยู่ใกล้วัดดังอย่างวัดหนองป่าพง หากใครตั้งใจมาไหว้พระ ปฏิบัติธรรมที่วัดนี้ล่ะก็เลือกพักที่ อยู่ด้วยกัน การ์เด้น โฮม ก็สะดวกสุดๆ เลยล่ะค่ะ''')
                        GoogleMaps = "https://maps.app.goo.gl/3xzvNmoofYWz3xJH8"
                        web_facebook = "https://web.facebook.com/uduayganubon/?_rdc=1&_rdr"
                        website = "https://www.agoda.com/u-duay-gan-garden-home/hotel/ubon-ratchathani-th.html?cid=1844104&ds=XCkabtt%2FMaMsqheN"
                        col8.link_button(''':green[Google Maps]''',GoogleMaps)
                        col8.link_button(''':blue[web facebook]''',web_facebook)
                        col8.link_button(''':blue[website]''',website)
                        
                        col9.markdown(" ")
                
                        original9 = Image.open("image/image9.jpg")
                        col9.write(''':green[บลูมูล ริเวอร์ไซด์ รีสอร์ท อุบลราชธานี (Bluemoon Riverside Resort)]''')
                        col9.image(original9, caption="", use_column_width=True)
                        col9.markdown('''บลูมูล ริเวอร์ไซด์ รีสอร์ท อุบลราชธานี (Bluemoon Riverside Resort) -อ.พิบูลมังสาหาร พาไปเปลี่ยนบรรยากาศแถวริมแม่น้ำมูลกันบ้างที่ บลูมูล ริเวอร์ไซด์ รีสอร์ท อุบลราชธานี ที่พักริมน้ำมาพร้อมห้องพักหลากหลายสไตล์เน้นความเรียบง่าย กลมกลืนกับธรรมชาติและวิถีชีวิตชุมชนชาวอีสาน ตั้งอยู่ริมฝั่งคุ้งแม่น้ำมูล อำเภอพิบูลมังสาหาร ใกล้แหล่งท่องเที่ยวยอดนิยมอย่างแก่งสะพือ ภายในที่พักมีร้านอาหารริมน้ำบรรยากาศสุดชิลพร้อมนำเสนอเมนูปลาแม่น้ำมูลแสนอร่อย ที่บอกเลยว่าไม่ควรพลาด แล้วในช่วงฤดูหนาวเรายังสามารถชมพระอาทิตย์ขึ้นและพระอาทิตย์ตกได้จากท่าน้ำในที่พักอีกด้วยนะ ''')
                        GoogleMaps = "https://maps.app.goo.gl/3xzvNmoofYWz3xJH8"
                        web_facebook = "https://web.facebook.com/uduayganubon/?_rdc=1&_rdr"
                        website = "https://www.agoda.com/u-duay-gan-garden-home/hotel/ubon-ratchathani-th.html?cid=1844104&ds=XCkabtt%2FMaMsqheN"
                        col9.link_button(''':green[Google Maps]''',GoogleMaps)
                        col9.link_button(''':blue[web facebook]''',web_facebook)
                        col9.link_button(''':blue[website]''',website)
                        
                        col10, col11, col12 = st.columns(3)
                
                        col10.markdown(" ")
                        
                        original10 = Image.open("image/image10.jpg")
                        col10.write(''':green[เรือนกะยอม เฮ้าส์ แอนด์ รีสอร์ท (Kayom House & Resort)]''')
                        col10.image(original10, caption=" ", use_column_width=True)
                        col10.markdown('''เรือนกะยอม เฮ้าส์ แอนด์ รีสอร์ท (Kayom House & Resort) - อ.โขงเจียม เรือนกะยอม เฮ้าส์ แอนด์ รีสอร์ท รีสอร์ทบรรยากาศสุดชิลที่ได้ทั้งวิวภูเขาและแม่น้ำโขง ตั้งอยู่ไม่ใกล้ไม่ไกลจากอุทยานแห่งชาติผาแต้ม ตัวที่พักเน้นการออกแบบให้กลมกลืนกับธรรมชาติโดยจะใช้ไม้เป็นหลัก ในส่วนของห้องพักมีให้เลือกทั้งแบบห้องพักที่อยู่ภายในตัวอาคารและบ้านพักที่มีระเบียงสามารถมองเห็นวิวแม่น้ำโขงจากหน้าห้องพักได้ด้วย  รวมถึงภายในรีสอร์ทยังมีบริการร้านอาหารริมน้ำบรรยากาศสุดชิลด้วยนะ เรียกได้ว่าไม่ต้องออกไปหาของกินที่ไหนให้เสียเวลาเลย แล้วทางรีสอร์ทยังใจดีทำทางให้เราได้ลงไปเดินเล่นถ่ายรูปริมแม่น้ำโขงได้ด้วยล่ะจ้า ''')
                        GoogleMaps = "https://maps.app.goo.gl/QsoAwfMrhkVNa2mp6"
                        web_facebook = "https://web.facebook.com/reuxnkayom/?locale=th_TH&_rdc=1&_rdr"
                        website = "https://www.agoda.com/th-th/kayom-house-white-meranti-house-resort/hotel/khong-chiam-th.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1891451&numberOfBedrooms=&familyMode=false&adults=1&children=0&rooms=1&maxRooms=0&checkIn=2024-03-13&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=-1&showReviewSubmissionEntry=false&currencyCode=THB&isFreeOccSearch=false&tag=fe625c71-af70-47da-8d26-d5a7406d450d&isCityHaveAsq=false&los=1&searchrequestid=09002a9f-86d9-443b-8be8-25aa442d2513&ds=wmr8qyr0tIU1zJLM"
                        col10.link_button(''':green[Google Maps]''',GoogleMaps)
                        col10.link_button(''':blue[web facebook]''',web_facebook)
                        col10.link_button(''':blue[website]''',website)
                        
                        col11.markdown(" ")
                
                        original11 = Image.open("image/image11.jpg")
                        col11.write(''':green[แลโขง ริเวอร์ รีสอร์ท (Laekhong River Resort)]''')
                        col11.image(original11, caption="", use_column_width=True)
                        col11.markdown('''แลโขง ริเวอร์ รีสอร์ท (Laekhong River Resort) - ที่พัก อ.เขมราฐ พาไปพักริมน้ำกันต่อที่อำเภอเขมราฐ อำเภอที่กำลังมาแรงสุดๆ ของจังหวัดอุบลฯ ในตอนนี้ แลโขง ริเวอร์ รีสอร์ท ที่พักสวยบรรยากาศดีตั้งอยู่ในบริเวณที่สามารถมองเห็นวิวโค้งน้ำแม่น้ำโขงได้สวยสุดๆ ของเขมราฐ  ห้องพักก็มีให้เลือกทั้งแบบในตัวอาคารและบ้านเป็นหลังซึ่งมีลานจอดรถติดกับตัวบ้านบอกเลยว่าเลิฟมากๆ เพราะไม่ต้องเดินขนของไปไกลจอดรถแล้วก็เข้าบ้านได้เลย ในบริเวณของที่พักยังเปิดเป็นร้านอาหารริมน้ำขนาดใหญ่ที่ขึ้นชื่อเรื่องเมนูปลาแม่น้ำโขงมากๆ ไม่ว่าจะเป็นต้มยำปลาคัง ปลาเนื้ออ่อนทอดกระเทียม ก็อร่อยน่าลองสุดๆ ที่สำคัญหากใครไปตรงกับวันเสาร์ที่มีถนนคนเดินเขมราฐทางรีสอร์ทเขาก็ใจดีให้ยืมจักรยานปั่นฟรีไปเที่ยวถนนคนเดินด้วยนะ เพราะจากโรงแรมไปถนนคนเดินใช้เวลาเพียงแค่ 5 นาทีเท่านั้น ''')
                        GoogleMaps = "https://maps.app.goo.gl/iFamnKyfvEdGccuBA"
                        web_facebook = "https://web.facebook.com/laekhongresort/?locale=th_TH&_rdc=1&_rdr"
                        website = "https://www.agoda.com/th-th/h15957884/hotel/default-city-km.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1891451&numberOfBedrooms=&familyMode=false&adults=1&children=0&rooms=1&maxRooms=0&checkIn=2024-03-13&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=-1&showReviewSubmissionEntry=false&currencyCode=THB&isFreeOccSearch=false&tag=4b60fa63-18ce-4b57-b66c-32548b434505&isCityHaveAsq=false&los=1&searchrequestid=02afca97-cd25-4958-82e8-b33971598d30&ds=SFHAkCNIP78QkrVB"
                        col11.link_button(''':green[Google Maps]''',GoogleMaps)
                        col11.link_button(''':blue[web facebook]''',web_facebook)
                        col11.link_button(''':blue[website]''',website)
                        
                        col12.markdown(" ")
                
                        original12 = Image.open("image/image12.jpg")
                        col12.write(''':green[โรงแรม สุนีย์แกรนด์]''')
                        col12.image(original12, caption="", use_column_width=True)
                        col12.markdown('''โรงแรม สุนีย์แกรนด์ นอกจากที่พักจะได้รับการรับรองมาตรฐาน SHA ที่พักยังมีบริการ Wi-Fi ฟรีในทุกห้องพัก และที่จอดรถฟรี ที่พักตั้งอยู่ในย่านตัวเมืองอุบลราชธานีของอุบลราชธานี ผู้เข้าพักจึงได้อยู่ใกล้สถานที่ท่องเที่ยวน่าสนใจและร้านอาหารอร่อยๆ ทริปยังไม่จบถ้าไม่ได้แวะไปที่เที่ยวชื่อดังอย่าง วัดพระธาตุหนองบัว ด้วยอีกสักที่ ที่พัก 4 ดาวคุณภาพสูงแห่งนี้มี บริการนวด, สระว่ายน้ำกลางแจ้ง และ ห้องซาวน่า คอยอำนวยความสะดวกแก่ผู้เข้าพัก แผนกต้อนรับบริการ 24 ชั่วโมง, รูมเซอร์วิส และเจ้าหน้าที่อำนวยความสะดวกเป็นส่วนหนึ่งของบริการที่โรงแรมแห่งนี้ สระว่ายน้ำ และอาหารเช้าฟรีจะช่วยให้การเข้าพักของคุณพิเศษขึ้นไปอีก หากคุณวางแผนที่จะขับรถมาโรงแรมสุนีย์แกรนด์ยังมีที่จอดรถฟรีพร้อมให้บริการ''')
                        GoogleMaps = "https://maps.app.goo.gl/PsxpvDK4PsPKfjCa6"
                        web_facebook = "https://web.facebook.com/suneegrandhotel.ubon/?locale=th_TH&_rdc=1&_rdr"
                        website = "https://www.suneegrandhotel.com/th/index.html"
                        col12.link_button(''':green[Google Maps]''',GoogleMaps)
                        col12.link_button(''':blue[web facebook]''',web_facebook)
                        col12.link_button(''':blue[website]''',website)
                        
                with tab2 :
                        st.header("สถานที่ท่องเที่ยวยอดฮิต")
                        video_file = open('video/video2.mp4','rb').read()
                        st.video(video_file)
                        #st.subheader("Minimalist Products")
                        st.markdown(" ")
                        col13, col14, col15 = st.columns(3)
                
                        original13 = Image.open("travel/image13.jpg")
                        col13.write(''':orange[ทุ่งศรีเมือง]''')
                        col13.image(original13, caption="", use_column_width=True)
                        col13.markdown('''ทุ่งศรีเมือง เดิมมีชื่อว่า “ นาทุ่งศรีเมือง ” เป็นที่ประดิษฐาน ศาลหลักเมือง ตั้งอยู่ใจกลางเมืองอุบลราชธานี ถนนอุปราช บริเวณหน้าศาลากลางจังหวัด (หลังเก่า) เป็นทุ่งกว้างกลางเมือง เดิมเป็นที่ทำนาของเจ้าเมือง ต่อมาสมัยรัชกาลที่ 5 โปรดฯ ให้งดการทำนาที่ทุ่งศรีเมือง เพื่อใช้ประโยชน์เช่นเดียวกับสนามหลวงในกรุงเทพฯ เป็นที่ประกอบพิธีศพเจ้าเมือง จัดงานประเพณีแห่เทียนพรรษา และประเพณีอื่น ๆ ปัจจุบันเป็นที่พักผ่อนของชาวเมือง และเป็นที่จัดเทศกาลงานบุญต่างๆ ภายในทุ่งศรีเมืองยังมีต้นเทียนพรรษาเฉลิมพระเกียรติ พระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช ในหลวงรัชกาลที่ 9 เนื่องในวโรกาสมหามงคลเฉลิมพระชนมพรรษา 6 รอบ 5 ธันวาคม พ.ศ. 2542 และอนุสาวรีย์พระปทุมวรราชสุริยวงษ์ (เจ้าคำผง) ผู้ก่อตั้งเมืองอุบลราชธานี โดยจะมีพิธีบวงสรวงและสดุดีวีรกรรมของท่าน ทุกวันที่ 10 พฤศจิกายน ของทุกปี ณ ทุ่งศรีเมืองแห่งนี้ ''')
                        GoogleMaps13 = "https://maps.app.goo.gl/rCDG26d6znTc2JKH8"
                        col13.link_button(''':green[Google Maps]''',GoogleMaps13)
                        
                                           
                        original14 = Image.open("travel/image14.jpg")
                        col14.write(''':orange[วัดทุ่งศรีเมือง (Tung Sri Muang Temple)]''')
                        col14.image(original14, caption="", use_column_width=True)
                        col14.markdown('''วัดทุ่งศรีเมือง (Tung Sri Muang Temple) เป็นวัดคู่บ้านคู่เมือง ตั้งอยู่ทางทิศตะวันออกของ ทุ่งศรีเมือง สร้างขึ้นในสมัยพระบาทสมเด็จพระนั่งเกล้าเจ้าอยู่หัว จุดเด่นของวัดแห่งนี้ คือ “หอไตรกลางน้ำ” ซึ่งได้รับยกย่องว่า เป็นหอไตรที่สวยงามที่สุดและสมบูรณ์มากที่สุดแห่งหนึ่งในภาคอีสาน จัดเป็นหนึ่งในของดีประจำจังหวัด นอกจากนี้ยังมีหอระฆัง และภาพจิตรกรรมฝาผนัง รวมถึงมีศิลปวัตถุมีค่าอีกหลายอย่าง เช่น พระพุทธบาทจำลอง และองค์พระเจ้าใหญ่เงินฮาง “หอไตรกลางน้ำ” เป็นหอพระไตรปิฏกที่สร้างด้วยไม้ ตั้งอยู่กลางสระน้ำ มีลักษณะผสมผสานกันระหว่างศิลปะของไทย ลาว และพม่า ภายในมีตู้เก็บพระธรรมลงรักปิดทอง หอไตรกลางน้ำยังได้รับรางวัล “อนุรักษ์สถาปัตยกรรมดีเด่น” จากสมเด็จพระกนิษฐาธิราชเจ้า กรมสมเด็จพระเทพรัตนราชสุดาฯ สยามบรมราชกุมารี อีกด้วย''')
                        GoogleMaps14 = "https://maps.app.goo.gl/1E2zcZUyXGMzjZv79"
                        col14.link_button(''':green[Google Maps]''',GoogleMaps14)
                        
                        
                        original15 = Image.open("travel/image15.jpg")
                        col15.write(''':orange[วัดใต้พระเจ้าใหญ่องค์ตื้อ (Wat Tai Phra Chao Yai Ong Tue)]''')
                        col15.image(original15, caption="", use_column_width=True)
                        col15.markdown('''วัดใต้พระเจ้าใหญ่องค์ตื้อ (Wat Tai Phra Chao Yai Ong Tue) วัดใต้พระเจ้าใหญ่องค์ตื้อ หรือวัดใต้เทิง ตั้งอยู่ที่ถนนพรหมราช ในตัวเมืองอุบลราชธานี เป็นวัดเก่าแก่ที่เคยเป็นวัดฝ่ายวิปัสสนา ของพระอาจารย์เสาร์ กันตสีโล และพระอาจารย์มั่น ภูริทัตโต ภายในพระอุโบสถมณฑปเพชร 7 แสงพระเจ้าใหญ่องค์ตื้อ เป็นที่ประดิษฐาน “พระเจ้าใหญ่องค์ตื้อ” พระพุทธรูปเนื้อทองสำริด ปางมารวิชัย มีความสำคัญเป็น 1 ใน 5 องค์ในจำนวนพระเจ้าใหญ่องค์ตื้อทั้งหมดที่มีอยู่ในประเทศไทย  เป็นที่เคารพนับถือของทั้งฝั่งไทยและฝั่งลาว ภายในวัดยังมีโบราณวัตถุ ได้แก่ พระพุทธรูปปางยืนห้ามสมุทร 4 องค์ และพระพุทธรูปเจตมนเพลิงองค์ตื้อ (สีดำสนิท) หลักศิลาจารึกหินทราย 2 หลัก วิหารเฉลิมพระเกียรติ 200 ปี เป็นที่ประดิษฐานพระพุทธมงคลรัตนสิริธัญสถิตและเจดีย์พระบรมสารีริกธาตุและทุกวันที่ 1 - 5 มีนาคม ของทุกปี มีงานเทศกาลอัญเชิญพระพุทธรูปเจตมุนเพลิงองค์ตื้อ เพื่อให้ประชาชนได้นมัสการสรงน้ำตลอด 5 วัน 5 คืน ''')
                        GoogleMaps15 = "https://maps.app.goo.gl/ap751r3BBRZMh1897"
                        col15.link_button(''':green[Google Maps]''',GoogleMaps15)
                        
                        
                        col16, col17, col18 = st.columns(3)
                
                        col16.markdown(" ")
                        
                        original16 = Image.open("travel/image16.jpg")
                        col16.write(''':orange[พระธาตุหนองบัว (Wat Phrathat Nong Bua)]''')
                        col16.image(original16, caption="", use_column_width=True)
                        col16.markdown('''พระธาตุหนองบัว (Wat Phrathat Nong Bua) พระธาตุเจดีย์ศรีมหาโพธิ์ หรือที่ชาวอุบลเรียกกันว่า “พระธาตุหนองบัว” ตั้งอยู่ใจกลางเมิองที่ถนนธรรมวิถี สร้างขึ้นในปี พ.ศ. 2500 เพื่อเป็นสัญลักษณ์ครบรอบ 25 ศตวรรษของพุทธศาสนา พระธาตุเจดีย์ศรีมหาโพธิ์นี้ได้จำลองแบบมาจากเจดีย์พุทธคยา ประเทศอินเดีย สถานที่ตรัสรู้ของพระพุทธเจ้า บริเวณฐานเจดีย์มีประตูทางเข้าสู่ใจกลางเจดีย์ทั้ง 4 ด้าน ภายในองค์พระธาตุบรรจุพระบรมสารีริกธาตุ ซึ่งบรรจุไว้ในสถูปลงรักปิดทองศิลปะอินเดียแบบปาละ สลักลายเรื่องพระเจ้า 500 ชาติ ด้านหลังของพระธาตุฯ มีอุโบสถศาลา ซึ่งสร้างเลียนแบบรูปทรงมาจากปรินิพพานวิหาร เมืองกุสินาราย รัฐอุตร ประเทศประเทศอินเดีย ซึ่งเป็นที่เสด็จดับขันธปรินิพพานของพระพุทธเจ้า อีกหนึ่งไฮไลท์คือรูปปั้นฉัพยาปุตตะ หรือพญานาคสีรุ้ง ที่ขึ้นชื่อในเรื่องของความงดงาม และความหลากหลายของสีวรกาย ''')
                        GoogleMaps16 = "https://maps.app.goo.gl/7Z5XfKmvZcFhZJLv8"
                        col16.link_button(''':green[Google Maps]''',GoogleMaps16)
                        
                        
                        col17.markdown(" ")
                
                        original17 = Image.open("travel/image17.jpg")
                        col17.write(''':orange[วัดสิรินธรวราราม (Wat Sirindhornwararam)]''')
                        col17.image(original17, caption="", use_column_width=True)
                        col17.markdown('''วัดสิรินธรวราราม (Wat Sirindhornwararam) วัดเรืองแสง แห่งตำบลช่องเม็ก อำเภอสิรินธร โดดเด่นด้วยอุโบสถสีปัดทองตั้งเด่นเป็นสง่า ด้านหลังของอุโบสถเป็นจิตรกรรมเรืองแสงสีเขียวของต้นกัลปพฤกษ์ สวยงามตื่นตาตื่นใจในยามค่ำคืน ฝีมือการออกแบบของช่าง “คุณากร ปริญญาปุณโณ” โดยมีแรงบันดาลใจมาจากต้นไม้แห่งชีวิต ในภาพยนตร์เรื่อง “อวตาร” โดยใช้สารเรืองแสงหรือสารฟลูออเรสเซนต์ ซึ่งมีคุณสมบัติรับแสงพระอาทิตย์ในตอนกลางวัน และปล่อยพลังงานออกมาในตอนกลางคืน ช่วงเวลาที่ดีที่สุดสำหรับการชมและถ่ายภาพคือ ตั้งแต่เวลา เวลา 18.00-20.00 น. บริเวณด้านหลังพระอุโบสถเป็นจุดชมวิวลำน้ำโขง ทิวทัศน์ของฝั่งลาว ด่านช่องเม็ก และอ่างเก็บน้ำบริเวณเชิงเขา อีกทั้งยังเป็นจุดชมพระอาทิตย์ตกดินที่สวยงามด้วย ''')
                        GoogleMaps17 = "https://maps.app.goo.gl/qjpR5QhbsvHwpfxTA"
                        col17.link_button(''':green[Google Maps]''',GoogleMaps17)
                        
                        
                        col18.markdown(" ")
                
                        original18 = Image.open("travel/image18.jpg")
                        col18.write(''':orange[พัทยาน้อย (Pattaya Noi หาดพัทยาน้อย หรือ ทะเลอีสานใต้]''')
                        col18.image(original18, caption="", use_column_width=True)
                        col18.markdown('''พัทยาน้อย (Pattaya Noi หาดพัทยาน้อย หรือ ทะเลอีสานใต้ ตั้งอยู่ริมถนนสถิตนิมานการ บ้านใหม่ภูทอง อำเภอสิรินธร ห่างจากตัวเมืองประมาณ 60 กิโลเมตร ในฤดูแล้งระดับน้ำเหนือเขื่อนสิรินธรต่ำลงมาก จนเห็นเป็นหาดทรายขาวทอดตัวยาว สามารถลงเล่นน้ำได้ พื้นที่แห่งนี้จึงได้รับการพัฒนาให้เป็นจุดท่องเที่ยวพักผ่อนหย่อนใจ และเล่นน้ำยอดฮิตของชาวอุบลราชธานี รวมไปจนถึงชาวอีสานใต้ในหลายๆ พื้นที่ใกล้เคียงกัน ที่นี่เพียบพร้อมด้วยบริการอำนวยความสะดวกแก่นักท่องเที่ยว ทั้ง ร้านอาหาร รีสอร์ท ร้านกาแฟ มีลักษณะเป็นเรือนแพกลางน้ำ แถมยังมีเครื่องเล่นทางน้ำ อย่างเช่น บานาน่าโบ๊ค เจ็ตสกีและห่วงยางให้บริการอีกด้วย)  ''')
                        GoogleMaps = "https://maps.app.goo.gl/GPdKJrRRQYHk3ydL7"
                        col18.link_button(''':green[Google Maps]''',GoogleMaps)
                        
                        
                        col7, col8, col9 = st.columns(3)
                
                        original7 = Image.open("travel/image19.jpg")
                        col7.write(''':orange[อุทยานแห่งชาติแก่งตะนะ (Kaeng Tana National Park]''')
                        col7.image(original7, caption=" ", use_column_width=True)
                        col7.markdown('''อุทยานแห่งชาติแก่งตะนะ (Kaeng Tana National Park อุทยานแห่งชาติแก่งตะนะ เดิมชื่อ “อุทยานแห่งชาติดงหินกอง” เกาะแก่งกลางลำน้ำมูลที่ใหญ่ที่สุด มีเนื้อที่ประมาณ 50,000 ไร่ ตั้งอยู่ที่ตำบลคำเขื่อนแก้ว อำเภอสิรินธร มีลักษณะเป็นที่ราบสูงและเนินเขาเตี้ยๆ โดยมียอดเขาบรรทัดเป็นจุดสูงสุด มีแม่น้ำมูลและแม่น้ำโขงไหลผ่าน ไปตามร่องหิน อีกทั้งยังมีถ้ำใต้น้ำหลายแห่ง ซึ่งเป็นจุดเด่นของแก่งตะนะแห่งนี้ “แก่งตะนะ” เป็นแก่งกลางลำน้ำมูลที่ใหญ่ที่สุด ตัวแก่งเป็นแผ่นหินขนาดใหญ่กั้นขวางลำน้ำมูล สายน้ำที่ ไหลผ่านแก่งตะนะนั้นแยกเป็นน้ำตกใหญ่น้อยสวยงามน่าชม มีจุดเล่นน้ำเหนือแก่ง โดยมีเจ้าหน้าที่คอยให้คำแนะนำ และรักษาความปลอดภัยให้นักท่องเที่ยว กิจกรรมห้ามพลาดของที่นี่คือ เดินป่า ค้างคืน ดูพระอาทิตย์ขึ้นบนผาด่าง ซึ่งเป็นจุดชมวิวที่มองเห็นพระอาทิตย์ขึ้นพร้อมๆ กับผาชนะได อีกทั้งยังสามารถมองเห็นหมู่บ้านชาวลาว และสะพานปากแซ เมืองปากแซ แขวงจำปาสัก ของประเทศลาวอีกด้วย) ''')
                        GoogleMaps = "https://maps.app.goo.gl/7weBXJ3WvQjsW1PQA"
                        col7.link_button(''':green[Google Maps]''',GoogleMaps)
                        
                        
                        original8 = Image.open("travel/image20.jpg")
                        col8.write(''':orange[สามพันโบก (Sam Phan Bok)]''')
                        col8.image(original8, caption=" ", use_column_width=True)
                        col8.markdown('''สามพันโบก (Sam Phan Bok) สามพันโบก ได้รับสมญานามว่า “แกรนด์แคนยอนเมืองไทย” ตั้งอยู่ที่บ้านโป่งเป้า ตำบลเหล่างาม อำเภอโพธิ์ไทร เป็นแก่งหินทรายขนาดใหญ่ที่ถูกกระแสน้ำธรรมชาติกัดเซาะมานานหลายพันปี จนกลายเป็นแอ่งหลุมรูปร่างแปลกตา กระจายกินพื้นที่เลียบริมแม่น้ำโขง ทั้งฝั่งไทยและลาว ในช่วงหน้าแล้งจะปรากฏให้เห็นเป็นภาพศิลปะสารพัดรูปร่าง เป็นระยะทางกว่า 5 กิโลเมตร รวมเป็นพื้นที่กว่า 30 ตารางกิโลเมตร จุดถ่ายรูปยอดฮิตคือ ผาหินรูปสะพานโค้ง หินหัวสุนัข สระมรกต  โบกรูปดาว โบกรูปหัวใจ และโบกรูปมิกกี้เม้าส์ ใกล้ๆ กันยังมีจุดน่าเที่ยวอย่างเช่น หลักศิลาเลข ถ้ำนางเข็นฝ้าย แก่งสองคอน ถ้ำนางต่ำหูก หาดหินสี หาดแห่ ภูเขาหิน ช่วงเวลาที่ดีที่สุดในการมาเยือนสามพันโบกคือ ประมาณเดือนพฤศจิกายนถึงมิถุนายน ''')
                        GoogleMaps = "https://maps.app.goo.gl/HcqajMi6p8SWtXzx5"
                        col8.link_button(''':green[Google Maps]''',GoogleMaps)
                        
                        
                        original9 = Image.open("travel/image21.jpg")
                        col9.write(''':orange[หาดหงส์ (Hong Beach)]''')
                        col9.image(original9, caption="", use_column_width=True)
                        col9.markdown('''หาดหงส์ (Hong Beach) อีกหนึ่งที่เที่ยวอุบลราชธานีที่อำเภอโพธิ์ไทร ไม่ไกลจากสามพันโบก เป็นเนินทรายแม่น้ำโขงที่เกิดจากการพัดพาของน้ำ และนำตะกอนทรายมาทับถมกัน จนกลายเป็นทะเลทรายที่กว้างใหญ่ ภายในพื้นที่หาดหงส์ยังมีสระน้ำธรรมชาติขนาดใหญ่ มีพื้นที่หาดลาดเอียงเทตัดลงไป กลายเป็นที่กระโดดหาดทรายเล่นนักท่องเที่ยว การเดินทางมาที่นี่ ต้องมาทางเรือเท่านั้น โดยนั่งมาจากสามพันโบกหรือหาดสลึงก็ได้เช่นกัน แนะนำให้มาหน้าแล้ง จะเห็นเนินทรายกว้างใหญ่และสวยงามที่สุด ช่วงที่เหมาะกับการถ่ายรูปคือ 4 โมงเย็น จนถึงช่วงพระอาทิตย์ใกล้ลับขอบฟ้า จะได้ภาพสวยงามที่สุด อย่าลืมเลือกใส่รองเท้าที่เดินทรายได้สบายๆ รวมทั้งพกน้ำดื่มกันมาด้วย หากต้องการอยู่ถ่ายรูปจนพระอาทิตย์ตกดิน เพื่อความปลอดภัย ควรพกไฟฉายไปด้วย   ''')
                        GoogleMaps = "https://maps.app.goo.gl/qr5muJaaz9Rfh1CZ9"
                        col9.link_button(''':green[Google Maps]''',GoogleMaps)
                        
                        
                        col10, col11, col12 = st.columns(3)
                
                        col10.markdown(" ")
                        
                        original10 = Image.open("travel/image22.jpg")
                        col10.write(''':orange[บ้านผาชัน (Ban Pha Chan)]''')
                        col10.image(original10, caption="", use_column_width=True)
                        col10.markdown('''บ้านผาชัน (Ban Pha Chan) “บ้านผาชัน” หมู่บ้านท่องเที่ยวเชิงอนุรักษ์ริมน้ำโขง ตั้งอยู่ที่ตำบลสำโรง อำเภอโพธิ์ไทร โดยมี “เสาเฉลียงใหญ่” เป็นไฮไลท์สำคัญ เสาเฉลียงยักษ์ใหญ่ที่สุดในประเทศไทยนี้ มีรูปร่างคล้ายดอกเห็ด สูงกว่า 20 เมตร สันนิษฐานว่าอายุประมาณ 100 ล้านปี สามารถขับรถเข้าถึงลานจอดรถ และเดินชมได้ด้วยตนเอง นอกจากนี้ยังมี “ผาชัน” เป็นหน้าผาหินที่มีความสูงชันประมาณ 40-50 เมตร จากระดับน้ำ ตลอดเส้นทางยาวประมาณ 5 กิโลเมตร จนเป็นที่มาของชื่อหมู่บ้าน และยังมีจุดท่องเที่ยวอื่นๆ อีกเช่น ผาตัวเลข หรือที่ชาวบ้านเรียกว่า “ผาศิลาเลข” ผาหัวช้าง ผาหมาว้อ ผาสามหมื่นรู ศิลาปะการัง หินหัวพญานาค สวนหิน ถ้ำนางเข็ญฝ้าย และท่ากกกระดาน ซึ่งเป็นจุดชมพระอาทิตย์ขึ้นริมฝั่งโขง ''')
                        GoogleMaps = "https://maps.app.goo.gl/F82QjGpRAvYBQd9J9"
                        col10.link_button(''':green[Google Maps]''',GoogleMaps)
                        
                        col11.markdown(" ")
                
                        original11 = Image.open("travel/image23.jpg")
                        col11.write(''':orange[อุทยานแห่งชาติผาแต้ม (Pha Taem National Park)]''')
                        col11.image(original11, caption="", use_column_width=True)
                        col11.markdown('''อุทยานแห่งชาติผาแต้ม (Pha Taem National Park) เป็นอุทยานที่ตั้งอยู่ทางตะวันออกสุดของประเทศไทย มีเนื้อที่ครอบคลุมอยู่ในท้องที่อำเภอโขงเจียม อำเภอศรีเมืองใหม่ และอำเภอโพธิ์ไทร มีจุดเด่นที่สวยงามตามธรรมชาติมากมาย เช่น “เสาเฉลียง” เสาหินลักษณะคล้ายดอกเห็ด ที่เกิดจากการกัดเซาะของน้ำและลมเป็นเวลานับล้านปี “ผาชะนะได” หน้าผาสูงชันเป็นจุดชมพระอาทิตย์ขึ้นก่อนใครในประเทศไทย ที่บริเวณผนังหน้าผาด้านล่างมีภาพเขียนสีก่อนประวัติศาสตร์เรียงรายอยู่ประมาณ 300 ภาพ นับเป็นภาพเขียนริมหน้าผาที่ยาวที่สุดในประเทศ นอกจากนี้ยังมีเส้นทางเดินป่าชมธรรมชาติ โดยระหว่างทางจะได้พบกับสิ่งที่น่าสนใจ เช่น น้ำตกห้วยพอก ผาเจ็ก ผาเมย ผากำปั่น ผาหินแตก ภูโลง ภูกระบอ ภูผาขาม ถ้ำปาฎิหาริย์ น้ำตกทุ่งนาเมือง น้ำตกแสงจันทร์ น้ำตกกวางโตน หินโยก ภูจ้อมก้อม หาดวิจิตรา หินโยกมหัศจรรย์ และ น้ำตกสร้อยสวรรค์ ''')
                        GoogleMaps = "https://maps.app.goo.gl/xxSqJMRZNb5B1936A"
                        col11.link_button(''':green[Google Maps]''',GoogleMaps)
                        
                        
                        col12.markdown(" ")
                        
                        original12 = Image.open("travel/image24.jpg")
                        col12.write(''':orange[น้ำตกแสงจันทร์ (Sang Chan Waterfall)]''')
                        col12.image(original12, caption="", use_column_width=True)
                        col12.markdown('''น้ำตกแสงจันทร์ (Sang Chan Waterfall) น้ำตกแสงจันทร์ หรือ น้ำตกรู อยู่ภายในอุทยานแห่งชาติผาแต้ม เป็นน้ำตกหนึ่งเดียวที่ไหลผ่านรูช่องหินเป็นสายสีขาวนวลอย่างสวยงามราวกับแสงจันทร์ จนได้ชื่อว่า น้ำตกรู ถือเป็นที่สุดของอันซีนไทยแลนด์อีกแห่งหนึ่งที่ต้องห้ามพลาด โดยเฉพาะในวันเพ็ญที่แสงจันทร์จะสาดส่องมาตรงรูหินพอดี น้ำตกแลดูเป็นประกายสีนวลสวยงามมาก ซึ่งทั้งหมดนี้คือที่มาของชื่อและเสน่ห์ของน้ำตกแห่งนี้ ซึ่งเกิดจากการกัดเซาะของสายน้ำ โดยเมื่อมีฝนตกลงมามากๆ กระแสน้ำในลำธารก็จะพัดพาเอาก้อนกรวดก้อนหินไหลติดไปด้วย ทำให้หลุมที่เป็นหินทรายขยายตัวเป็นหลุมกว้างขึ้นเรื่อยๆ นานวันเข้าหลุมก็ทะลุกลายเป็นรูอันเป็นที่มาของชื่อ “น้ำตกลงรู” และจุดเด่นอีกอย่างหนึ่งคือ ในบางช่วงและมุมมองที่ดีเราจะเห็นน้ำที่ตกกระทบผิวน้ำในแอ่งข้างล่างเป็นรูปหัวใจอีกด้วย  ''')
                        GoogleMaps = "https://maps.app.goo.gl/nxaP3YS18PM9KGe69"
                        col12.link_button(''':green[Google Maps]''',GoogleMaps)
                        
                        
                    
                with tab3:
                        st.header("ค่าเฟ่ยอดฮิต")
                        st.image('cafe/cafe1.jpg')
                        #st.subheader("Minimalist Products")
                        st.markdown(" ")
                        col1, col2, col3 = st.columns(3)
                
                        original1 = Image.open("cafe/image25.jpg")
                        col1.write(''':white[โฮก้าโฮก้า คาเฟ่]''')
                        col1.image(original1, caption="", use_column_width=True)
                        col1.markdown('''โฮก้าโฮก้า คาเฟ่ เป็นคาเฟ่อุบลราชธานี ตั้งอยู่ในซอยชยางกูร 10/1 อำเภอเมืองอุบลราชธานี เป็นร้านที่ให้บรรยากาศโฮมมี่แสนอบอุ่น ตกแต่งด้วยสไตล์ญี่ปุ่น เป็นบ้านไม้สองชั้น ตกแต่งด้วยงานไม้เป็นเป็นหลัก คุมโทนด้วยสีขาว และสีน้ำตาลเปลือกไม้ เหมือนอยู่ญี่ปุ่นจริงๆเลยค่ะ มุมถ่ายรูปเยอะมากๆ แถมรอบตัวร้านเป็นกระจกใสทำให้ได้แสงสวยๆ จากธรรมชาติ สำหรับเมนูทางร้านมให้เลือำหลากหลายมากๆ ทั้งเครื่องดื่ม ชา กาแฟ และเบเกอรี่อร่อยๆ ใครมาเที่ยวเมืองอุบล แวะมาทานกันได้เลยค่ะ''')
                        web_facebook = "https://web.facebook.com/LANGBAANCAFEANDCHILL/?_rdc=1&_rdr"
                        GoogleMaps = "https://maps.app.goo.gl/TvetmoUwRKWvM5Eh9"
                        col1.link_button(''':green[Google Maps]''',GoogleMaps)
                        col2.link_button(''':blue[web facebook]''',web_facebook)
                        
                        
                        
                        original2 = Image.open("cafe/image26.jpg")
                        col2.write(''':white[หลังบ้าน (LANG BAAN)]''')
                        col2.image(original2, caption=" ", use_column_width=True)
                        col2.markdown('''หลังบ้าน (LANG BAAN) หลังบ้าน เป็นคาเฟ่อุบลราชธานี ตั้งอยู่ที่ ถนนสุขาอุปถัมภ์ ซอยสุขาอุปถัมภ์23 อำเภอเมืองอุบลราชธานี เป็นคาเฟ่ที่ให้ความรู้สึกอบอุ่น ตกแต่งสวยงามคุมโทนด้วยสีน้ำตาลเปลือกไม้ และสีขาว ให้ความสบายตาสุดๆ ภายในร้านตกแต่งด้วยเฟอร์นิเจอร์ไม้ และต้นไม้ มีโซนให้เลือกนั่งทั้งแบบอินดอร์และเอาท์ดอร์ สำหรับเมนูมีให้เลือกหลากหลายทั้งเครื่องดื่ม เบเกอรี่ และอาหารคาว นอกจากนี้ยังมีกิจกรรมวาดรูประบายสีอคิลิคลงบนผ้าใบให้ลองทำกันด้วยนะคะ บอกเลยว่ามาแล้วคุ้มสุดๆ ''')
                        GoogleMaps = "https://maps.app.goo.gl/AsZ8nffLyS13bvo7A"
                        web_facebook = "https://web.facebook.com/prubon?locale=th_TH"
                        col2.link_button(''':green[Google Maps]''',GoogleMaps)
                        col2.link_button(''':blue[web facebook]''',web_facebook)
                        
                        
                        original3 = Image.open("cafe/image27.jpg")
                        col3.write(''':white[115 เบคเฮาส์ เอ็ก คอฟฟี่ บาร์ ]''')
                        col3.image(original3, caption="", use_column_width=True)
                        col3.markdown('''115 เบคเฮาส์ เอ็ก คอฟฟี่ บาร์ (115 Bakehouse x Coffee Bar) 115 เบคเฮาส์ เอ็ก คอฟฟี่ บาร์ เป็นคาเฟ่อุบลราชธานีที่อยู่ท่ามกลางธรรมชาติ ตั้งอยู่ที่ถนนหน้าหมู่บ้านอารียา 5 อำเภอเมืองอุบลราชธานี เป็นคาเฟ่โทนสีขาวสบายตา ออกแบบด้วยสไตล์ box-shaped houses หรือบ้านทรงกล่องสไตล์โมเดิร์น โอบล้อมไปด้วยต้นไม้ใหญ่ที่ช่วยให้บรรยากาศดี ร่มรื่น และเย็นสบาย สำหรับเมนูมีให้เลือกเยอะ ทั้งกาแฟ ชา และเบเกอรี่อร่อยๆ นอกจากนี้ยังมี Slow bar สำหรับชาวกาแฟเลิฟเวอร์ด้วยค่ะ ''')
                        GoogleMaps = "https://maps.app.goo.gl/M2RmUAfT45ix297v9"
                        web_facebook = "https://web.facebook.com/p/115-Bakehouse-x-Coffee-Bar-100064105870375/?locale=th_TH&_rdc=1&_rdr"
                        col3.link_button(''':green[Google Maps]''',GoogleMaps)
                        col3.link_button(''':blue[web facebook]''',web_facebook)
                        
                        
                        col4, col5, col6 = st.columns(3)
                
                        col4.markdown(" ")
                        
                        original4 = Image.open("cafe/image28.jpg")
                        col4.write(''':white[โฮมบาร์ (Homebar) ]''')
                        col4.image(original4, caption="", use_column_width=True)
                        col4.markdown('''โฮมบาร์ (Homebar) โฮมบาร์ เป็นคาเฟ่และบาร์ในตัว ตั้งอยู่ที่ถนนบ่าวโอ๊ต ตำบลแจระแม อำเภอเมืองอุบลราชธานี ท่ามกลางธรรมชาติ ล้อมรอบไปด้วยต้นไม้และแม่น้ำ ช่วงสายถึงเย็นที่ร้านเปิดโซน coffee bar สำหรับเครื่องดื่มอย่าง ชา กาแฟ สปาร์คกลิ้ง และเซ็ตขนมปัง สำหรับช่วงเย็นถึงดึกร้านเป็น Set the Mood Bar เสิร์ฟอาหารและเครื่องดื่ม จะไปช่วงเวลาไหนก็แฮปปี้ ใครชอบนั่งชิลล์ริมแม่น้ำบอกเลยว่าห้ามพลาดค่ะ ''')
                        GoogleMaps = "https://web.facebook.com/p/Homebar-you-feel-like-home-100083061645793/?_rdc=1&_rdr"
                        web_facebook = "https://web.facebook.com/prubon?locale=th_TH"
                        col4.link_button(''':green[Google Maps]''',GoogleMaps)
                        col4.link_button(''':blue[web facebook]''',web_facebook)
                        
                        
                        
                        col5.markdown(" ")
                
                        original5 = Image.open("cafe/image29.jpg")
                        col5.write(''':white[สงบ (SANGOB) ]''')
                        col5.image(original5, caption="", use_column_width=True)
                        col5.markdown('''สงบ (SANGOB) สงบ คาเฟ่ เป็นคาเฟ่ที่อยู่ท่ามกลางโซนเมืองเก่า ตั้งอยู่ที่ถนพรหมเทพ ตำบลในเมือง อำเภอเมืองอุบลราชธานี เป็นคาเฟ่ที่ตกแต่งด้วยสไตล์มินิมอล คุมโทนด้วยสีขาวคลีน ใช้เฟอร์นิเจอร์ไม้ เป็นคาเฟ่ 2 ชั้น ที่ยังคงเอกลักษณ์ของเมืองเก่าไว้ด้านบน มีมุมสวยๆ ให้่ายรูปเพียบ สำหรับเมนูก็มีให้เลือกหลากหลาย ทั้งเครื่องดื่ม ชา กาแฟ และเบเกอรี่แสนอร่อย ใครชอบความเงียบสงบ แนะนำคาเฟ่สงบเลยค่ะ  ''')
                        GoogleMaps = "https://maps.app.goo.gl/XKWQBz4eE2qaAwLC9"
                        web_facebook = "https://web.facebook.com/sangobcoffee/?_rdc=1&_rdr"
                        col5.link_button(''':green[Google Maps]''',GoogleMaps)
                        col5.link_button(''':blue[web facebook]''',web_facebook)
                       
                        col6.markdown(" ")
                
                        original6 = Image.open("cafe/image30.jpg")
                        col6.write(''':white[โรก โรสเตอร์ (Rogue Roasters)]''')
                        col6.image(original6, caption="", use_column_width=True)
                        col6.markdown('''โรก โรสเตอร์ (Rogue Roasters) โรก โรสเตอร์ เป็นอีกหนึ่งคาเฟ่ที่ไม่ควรพลาดถ้ามาเที่ยวเมืองอุบล ตั้งอยู่ที่ถนนสถลมาร์ค ตำบลวารินชำราบ อำเภอวารินชำราบ เป็นคาเฟ่ที่ตกแต่งด้วยสไตล์ลอฟท์ ดีไซน์แบบปูนเปลือย คุมโทนด้วยสีดำ เทา ให้ความรู้สึกเท่ๆ ตัวร้านตั้งอยู่ที่ชั้น 2 ของอาคาร มีมุมสวยๆ ให้ถ่ายรูปเยอะมาก ด้านในมีทั้งโซฯอินดอร์แะเอาท์ดอร์ให้เลือกนั่ง สำหรับเมนูมีให้เลือกเยอะมาก โดยเฉพาะกาแฟที่ทานแล้วรับรองติดใจ ทางร้านมีโรงคั่วกาแฟเป็นของตัวเอง ทำให้ได้รสชาติกาแฟที่เข้มข้น นอกจากนี้ยังมีเบเกอรี่อร่อยๆ ให้ทานด้วยค่ะ  ''')
                        GoogleMaps = "https://web.facebook.com/roguexroasters/?_rdc=1&_rdr"
                        web_facebook = "https://web.facebook.com/prubon?locale=th_TH"
                        col6.link_button(''':green[Google Maps]''',GoogleMaps)
                        col6.link_button(''':blue[web facebook]''',web_facebook)
                        
                        col7, col8, col9 = st.columns(3)
                
                        original7 = Image.open("cafe/image31.jpg")
                        col7.write(''':white[อารมย์กาแฟ ]''')
                        col7.image(original7, caption="", use_column_width=True)
                        col7.markdown('''อารมย์กาแฟ เป็นคาเฟ่ลับอุบลที่ไม่ควรพลาด ตั้งอยู่ที่ซอยสุขาอุปถัมภ์ 5 ตำบลในเมือง อำเภอเมืองอุบลราชธานี เป็นคาเฟ่บ้านเก่าที่ตกแต่งด้วยสไตล์วินเทจที่ยังคงเอกลักษณ์ของบ้านเก่าได้อย่างลงตัว ภายในร้านบรรยากาศอบอุ่น เหมือนไปเที่ยวบ้านสวนต่างจังหวัด ล้อมรอบไปด้วยต้นไม้ ให้ความรู้สึกอบอุ่น สำหรับเมนูมีให้เหลือหลากหลายมากๆ ทั้งเครื่องดื่มแบะเบเกอรี่อร่อยๆ เมนูแนะนำของทางร้านก็คือHoney bomb ค่ะ''')
                        GoogleMaps = "https://web.facebook.com/Aromcoffee/?locale=th_TH&_rdc=1&_rdr"
                        web_facebook = "https://maps.app.goo.gl/Q2r3i1dfYWD24mEz5"
                        col7.link_button(''':green[Google Maps]''',GoogleMaps)
                        col7.link_button(''':blue[web facebook]''',web_facebook)
                        
                        
                        original8 = Image.open("cafe/image32.jpg")
                        col8.write(''':white[แสนสุขโฮมคาเฟ่]''')
                        col8.image(original8, caption="", use_column_width=True)
                        col8.markdown('''แสนสุขโฮมคาเฟ่ เป็นคาเฟ่อุบลราชธานี ที่ตกแต่งด้วยสไตล์มินิมอล ตั้งอยู่ในถนนสถลมาร์ค ตำบล แสนสุข อำเภอวารินชำราบ อุบลราชธานี ตัวร้านตั้งอยู่กลางสวน โอบล้อมไปด้วยต้นไม้สีเขียวขจี ให้ความร่มรื่น เย็นสบาย ภายในร้านมีทั้งโซนอินดอร์และเอาท์ดอร์ให้เลือกนั่ง สำหรับเมนูมีให้เลือกทานหลากหลาย ทั้งเครื่องดื่ม เบเกอรี่ และอาหารวีแกน แถมยังออร์แกนิคแบบ​ 100% ใครสายสุขภาพแวะมาทานกันได้เลย''')
                        GoogleMaps = "https://web.facebook.com/sansookhomecafe/?locale=th_TH&_rdc=1&_rdr"
                        web_facebook = "https://maps.app.goo.gl/dbZwPp1ZAqauDK1Z7"
                        col8.link_button(''':green[Google Maps]''',GoogleMaps)
                        col8.link_button(''':blue[web facebook]''',web_facebook)
                        
                        original9 = Image.open("cafe/image33.jpg")
                        col9.write(''':white[TOP TUBE BIKE & CAFÉ]''')
                        col9.image(original9, caption="", use_column_width=True)
                        col9.markdown('''TOP TUBE BIKE & CAFÉ คาเฟ่อุบลราชธานีสำหรับคนรักจักรยาน ตั้งอยู่ที่ถนน พิชิตรังสรรค์ ตำบล ในเมือง อำเภอเมืองอุบลราชธานี เป็นคาเฟ่ที่ตกแต่งด้วยสไตล์สปอร์ต มีจักรยาน Touring ให้เลือกชม สำหรับเมนูมีให้เลือกหลากหลายทั้งเครื่องดื่ม และเบเกอรี่อร่อยๆ สำหรับเมนูเด็ดของทางร้านคือ กาแฟดริปรสนุ่ม สกัดจากเมล็ดกาแฟอราบิก้าที่ใช้สูตรขอทางร้านเอง ทำให้หอมละมุนมากขึ้น Dark chocolate จากโกโก้นำเข้าก็รสชาติดีไม่แพ้กันค่ะ''')
                        GoogleMaps = "https://web.facebook.com/TopTubeBikeAndCafe/?locale=th_TH&_rdc=1&_rdr"
                        web_facebook = "https://maps.app.goo.gl/VdPo79uxccpeVWsb8"
                        col9.link_button(''':green[Google Maps]''',GoogleMaps)
                        col9.link_button(''':blue[web facebook]''',web_facebook)
                        
                        col10, col11, col12 = st.columns(3)
                        
                        col10.markdown(" ")
                        
                        original10 = Image.open("cafe/image34.jpg")
                        col10.write(''':white[LIFE Roaster]''')
                        col10.image(original10, caption="", use_column_width=True)
                        col10.markdown('''LIFE Roaster เป็นคาเฟ่ในตัวเมืองอุบล ตั้งอยู่ที่ถนนสุริยาตร์ ตำบล ในเมือง อำเภอเมืองอุบลราชธานี เป็นคาเฟ่ที่โอบล้อมไปด้วยธรรมชาติ ตัวร้านเป็นไม้สีโอ๊ค ล้อมรอบไปด้วยต้นไม้สีเขียว บรรยากาศดีมากๆ ใครชอบทากาแฟ้องไม่พลาดเลยค่ะ เพราะที่นี้มีกาแฟอาราบิก้าคั่วบดชั้นดี​ คุณภาพเยี่ยม ที่ปลูกเองให้บริการ เมนู Signature ของทางร้านคือ กาแฟมะพร้าว​ จากกาแฟอาราบิก้าเข้มๆกับน้ำมะพร้าวหอมละมุน นอกจากนี้ยังมีเบเกอรี่อร่อยๆ ให้ทานด้วยค่ะ''')
                        GoogleMaps = "https://web.facebook.com/liferoasters/?locale=th_TH&_rdc=1&_rdr"
                        web_facebook = "https://web.facebook.com/prubon?locale=th_TH"
                        col10.link_button(''':blue[web facebook]''',web_facebook)
                        col10.link_button(''':green[Google Maps]''',GoogleMaps)
                        
                        
                        col11.markdown(" ")
                
                        original11 = Image.open("cafe/image35.jpg")
                        col11.write(''':white[ยวนใจ (Yuanjai)]''')
                        col11.image(original11, caption="", use_column_width=True)
                        col11.markdown('''ยวนใจ (Yuanjai) ยวนใจ เป็นคาเฟ่อุบลราชธานีเล็กๆ ตั้งอยู่หลังบขส. ในถนนคลังอาวุธ ตำบล ขามใหญ่ อำเภอเมืองอุบลราชธานี เป็นคาเฟ่เล็กๆ ที่ตกแต่งด้วยสไตล์ลอฟท์ ประดับด้วยรูปภาพอาร์ตๆ ใครสายติสๆ รับรองถูกใจ สำหรับที่นั่งมีให้ทั้งโซนอินดอร์และเอ้าท์ดอร์ มีดาดฟ้าด้วย สำหรับเมนูมีให้เลือกหลากหลาย ทั้งเครื่องดื่ม ชา กาแฟ และเบเกอรี่อร่อยๆ ใครชอบความเงียบสงบมาที่นี่ได้เลยค่ะ''')
                        GoogleMaps = "https://maps.app.goo.gl/8CBMziE26MGjbjQX6"
                        web_facebook = "https://web.facebook.com/yuanjai.cafe/?_rdc=1&_rdr"
                        col11.link_button(''':green[Google Maps]''',GoogleMaps)
                        col11.link_button(''':blue[web facebook]''',web_facebook)
                        
                        col12.markdown(" ")
                        
                        original12 = Image.open("cafe/image37.jpg")
                        col12.write(''':white[มา นา เด้อ คาเฟ่]''')
                        col12.image(original12, caption="", use_column_width=True)
                        col12.markdown('''มา นา เด้อ คาเฟ่ เป็นคาเฟ่ธรรมชาติ ตั้งอยู่ที่ ตำบลก่อเอ้ อำเภอเขื่องใน อุบลราชธานี เป็นคาเฟ่ที่ตั้งอยู่ท่ามกลางทุ่งนาเขียวขจี มีสะพานไม้ทอดยาวให้เดินเล่น มาเที่ยวช่วงไหนก็สวย โดยเฉพาะช่วงเก็บเกี่ยวจะเห็นต้นข้าวออกรวงเป็นทุ่งนาสีเหลืองทอง สำหรับเมนูบอกเลยว่าเพียบ ทั้งเครื่องดื่ม เบอเกอรี่ และอาหาร ที่มีให้เลือกทั้งอาหารไทย สปาเกตตี้ และสเต็ก ใครผ่านมาแวะมาเช็คอินกันได้เลย''')
                        GoogleMaps = "https://maps.app.goo.gl/2boYrPW4XgxLNYFj7"
                        web_facebook = "https://web.facebook.com/p/%E0%B8%A1%E0%B8%B2-%E0%B8%99%E0%B8%B2-%E0%B9%80%E0%B8%94%E0%B9%89%E0%B8%AD-100064543099086/?locale=th_TH&_rdc=1&_rdr"
                        col12.link_button(''':green[Google Maps]''',GoogleMaps)
                        col12.link_button(''':blue[web facebook]''',web_facebook)
                        
                        
                with tab4:
                        st.header("ร้านนั่งชิลในอุบล")
                        #st.subheader("Minimalist Products")
                        st.image('bar/image38.jpg')
                        st.markdown(" ")
                        col1, col2, col3 = st.columns(3)
                
                        original1 = Image.open("bar/image39.jpg")
                        col1.write(''':red[กา-ริน]''')
                        col1.image(original1, caption="", use_column_width=True)
                        col1.markdown('''กา-ริน เป็นสถานที่ที่มีความเป็นท้องถิ่นและเป็นที่รู้จักของชาวอุบลราชธานีอย่างแพร่หลาย ร้านนี้มีเมนูเหล้าที่หลากหลายและมีบรรยากาศที่เป็นเอกลักษณ์ สายนั่งชิลทุกวัย ไม่พลาดที่จะมาเยี่ยมชมร้านนี้ เนื่องจากมีเพลงที่หลากหลายแนว เช่น สากล, สตริง, ยุค 90’s และสตริงเก่าใหม่ แทบจะครบทุกแนวเพลง นอกจากนี้ยังมีเครื่องดื่มให้บริการอีกมากมาย พนักงานบริการดีและรวดเร็ว ห้องน้ำสะอาด การเดินทางสะดวกสบาย และที่สำคัญคือห้องนั่งเล่นที่มีการปรับอากาศอย่างเหมาะสมสำหรับการนั่งพักผ่อน ''')
                        GoogleMaps = "https://maps.app.goo.gl/BSwhvffsV7K5u1eo8"
                        web_facebook = "https://web.facebook.com/p/%E0%B8%81%E0%B8%B2-%E0%B8%A3%E0%B8%B4%E0%B8%99-l-Ka-rin-l-100064857514431/?_rdc=1&_rdr"
                        col1.link_button(''':green[Google Maps]''',GoogleMaps)
                        col1.link_button(''':blue[web facebook]''',web_facebook)
                        
                        original2 = Image.open("bar/image40.jpg")
                        col2.write(''':red[Tree Café]''')
                        col2.image(original2, caption="", use_column_width=True)
                        col2.markdown('''Tree Café เป็นร้านนั่งเล่นชิล ท่ามกลางสายน้ำและธรรมชาติ ที่มีการจำหน่ายกาแฟ ขนมหวาน อาหารและเครื่องดื่ม โดยมีบรรยากาศดีและเพลงเพราะ ตั้งอยู่ริมแม่น้ำมูล จังหวัดอุบลราชธานี มีเมนูหลากหลายให้เลือกทั้งคาวหวานและเครื่องดื่มอีกมากมาย ร้านอาหารนี้มีทั้งแบบแอร์และแบบลมธรรมชาติ ให้เลือกนั่งได้ตามใจชอบ ชมวิวน้ำมูล ฟังเพลงชิล ๆ และสนุกกับอาหารอร่อย ราคาอาหารไม่แพง ดังนั้น ท่านสามารถมาพักผ่อนได้อย่างสบายใจใน “TREE CAFE” นี้ได้โดยไม่ต้องกังวลเรื่องราคาอาหาร''')
                        GoogleMaps = "https://web.facebook.com/treecafe.rimmoon/?_rdc=1&_rdr"
                        web_facebook = "https://web.facebook.com/prubon?locale=th_TH"
                        col2.link_button(''':green[Google Maps]''',GoogleMaps)
                        col2.link_button(''':blue[web facebook]''',web_facebook)
                        
                        original3 = Image.open("bar/image41.jpg")
                        col3.write(''':red[ชมจันทร์ กินลม ชมดาว]''')
                        col3.image(original3, caption="", use_column_width=True)
                        col3.markdown('''ชมจันทร์ กินลม ชมดาว เป็นการออกแบบที่มีความเป็นระเบียบและเป็นระเบียบอย่างมาก โดยมีการออกแบบให้เหมือนกับเรือ ชั้นล่างของร้านจะมีเวทีแสดงสดและแนวเพลงจะเป็นแนวลูกทุ่ง ส่วนชั้นบนของร้านจะเป็นดาดฟ้าเรือที่ให้ลูกค้านั่งฟินชมวิวและแนวเพลงจะเป็นอะคูสติก นอกจากนี้ยังมีบริการอื่นๆอีกมากมาย เช่น รีสอร์ท ร้านกาแฟ Wawee Coffee ห้องจัดเลี้ยง VIP คาราโอเกะ และร้านอาหารลอยน้ำที่ตั้งอยู่ริมแม่น้ำมูล ชมจันทร์เป็นร้านอาหารที่ได้รับความนิยมอย่างแพร่หลาย ไม่ว่าจะเป็นการชวนสาวมาเดท ชวนเพื่อนแฮงค์เอ้าท์ หรือชวนเจ้านายชนแก้ว ชมจันทร์จะเป็นตัวเลือกอันดับต้ นๆ ของวัยทำงานใน ''')
                        GoogleMaps = "https://maps.app.goo.gl/MsoJxYRnDEkqekqm7"
                        web_facebook = "https://web.facebook.com/ChomjanUbon/?locale=th_TH&_rdc=1&_rdr"
                        col3.link_button(''':green[Google Maps]''',GoogleMaps)
                        col3.link_button(''':blue[web facebook]''',web_facebook)
                        
                        col4, col5, col6 = st.columns(3)
                
                        col4.markdown(" ")
                        
                        original4 = Image.open("bar/image42.jpg")
                        col4.write(''':red[Apollo]''')
                        col4.image(original4, caption="", use_column_width=True)
                        col4.markdown('''Apollo มีการตกแต่งอย่างเรียบง่าย แต่มีความโดดเด่นด้วยการเลือกใช้โซฟาที่เหมาะสำหรับการนั่งเกร๋ๆ หรือนั่งชิวๆ หรือแม้กระทั่งนั่งเปื่อย ๆ เพื่อให้เหมาะสำหรับการเดทหรือพบปะกับเพื่อนฝูง นอกจากนี้ยังมีการบริการอาหารและเครื่องดื่มที่มีคุณภาพดี รวมถึงสามารถเลือกได้ตามความชอบของลูกค้า เช่น สายเบียร์หรือสายเนิร์ด ราคาก็ค่อนข้างเหมาะสมและไม่แพงเกินไป ดังนั้น Apollo จึงเป็นที่ชื่นชอบของผู้คนที่ต้องการหาสถานที่พักผ่อนและพบปะกับเพื่อนฝูงในบรรยากาศที่เป็นกันเองสุดๆ''')
                        GoogleMaps = "https://web.facebook.com/apollo.ubon.ratchathani/?_rdc=1&_rdr"
                        web_facebook = "https://web.facebook.com/prubon?locale=th_TH"
                        col4.link_button(''':green[Google Maps]''',GoogleMaps)
                        col4.link_button(''':blue[web facebook]''',web_facebook)
                        
                        col5.markdown(" ")
                
                        original5 = Image.open("bar/image43.jpg")
                        col5.write(''':red[ U-Bar อุบลราชธานี]''')
                        col5.image(original5, caption="", use_column_width=True)
                        col5.markdown(''' U-Bar อุบลราชธานี อยู่ที่อุบลราชธานี มีบรรยากาศดี และเป็นที่นิยมของชาวท้องถิ่น โดยเฉพาะเวลากลางคืน มีเสียงเพลงและไฟสว่างสดใส ร้านเหล้า U-Bar เป็นร้านไวน์กึ่งผับ/ร้านเหล้า/บาร์อาหารตามสั่ง มีเมนูอาหารหลากหลายให้เลือก แต่ร้านนี้ไม่ได้ขายอาหารเป็นหลัก แต่จะขายเครื่องดื่มและไวน์ให้กับคุณได้ชิมกัน ตามจริงแล้ว Ubar เปิดด้วยกันหลายสาขาในหลายจังหวัดทั่วภาคอีสาน แต่ได้ทำการปิดตัวลงไปจนเหลือเพียงแค่ ยูบาร์ อุบลราชธานี ในปัจจุบัน''')
                        GoogleMaps = "https://maps.app.goo.gl/th59JkSKLKzemThf9"
                        web_facebook = "https://web.facebook.com/ubarfanpage/?locale=th_TH&_rdc=1&_rdr"
                        col5.link_button(''':green[Google Maps]''',GoogleMaps)
                        col5.link_button(''':blue[web facebook]''',web_facebook)
                        
                        
if __name__ == "__main__":
        main()               
                
                
                
                
                
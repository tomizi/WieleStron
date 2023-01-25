import streamlit as st



st.set_page_config(page_title='UMK w liczbach', page_icon = ':page_facing_up:',initial_sidebar_state='expanded',layout='wide')
st.sidebar.success("Wybierz stronę")


streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css?family=Lato&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Lato';
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)





st.markdown(
    """
<style>
[data-testid="stAppViewContainer"] > .main {background-image: url("https://login.umk.pl/themes/umk/images/logo-umk.png");
background-size:400px,400px;
background-position: 1150px 100px;
background-repeat: no-repeat;
background-attachment: local;}
[data-testid="stHeader"]{background-color: rgba(0,0,0,0);}
[class="css-1bh6xo1 e1fqkh3o2"]{
background-color: #0050AA;}
[class="st-bh st-bl st-bm st-bn st-bo st-bp st-az st-b4 st-bq st-br st-bs st-bt st-bu st-bv st-bw st-bx st-by st-bz st-b2 st-c0"]{
background-color: #FFCD00;}
[class="st-d9 st-cl st-bx st-da st-db st-c6 st-dc st-dd st-de"]{
font-family: 'Lato';}
[class="css-1atbdv8 e1fqkh3o1"]{
color: rgb(255,255,255);}
[class="st-av st-aw st-ax st-ay st-cl st-c6 st-b7 st-b4 st-b5 st-cn st-co st-cp st-cq st-cr st-cs st-ct st-cu st-cv st-cw st-b2 st-c2 st-ce st-dz st-e0 st-e1 st-e2 st-d1"]{
border-bottom-color: #0050AA;
border-top-color: #0050AA;
border-right-color: #0050AA;
border-left-color: #0050AA;}
section[data-testid="stSidebar"] label[class="css-1p2iens effi0qh3"]{
color: rgb(255,255,255);}
[class="st-bz st-cd st-ce st-ae st-af st-ag st-ah st-ai st-aj"]{
font-family: 'Lato';
color: rgb(255,255,255);}
</style>
""",
    unsafe_allow_html=True)

new_title = '<b style="color:rgb(0, 80, 170); font-size: 62px;">Strona główna</p>'
st.markdown(new_title, unsafe_allow_html=True)
st.markdown('---')
st.title('UNIWERSYTET MIKOŁAJA KOPERNIKA W TORUNIU')
st.subheader('Uniwersytet podzielony jest na wydziały. Każdy wydział ma unikatowe logo, które charakteryzuje kolor ' +
	      'i pozycja mniejszego kółka na obwodzie większego niebieskiego koła. Poniższa grafika przedstawia loga poszczególnych ' + 
	      'wydziałów. Warto zapoznać się z barwami jednostek, ponieważ są one częścią wizualizacji znajdujących się na pozostałych stronach.'+ 
	      ' Ich znajomość ułatwi interpretację wykresów.')
st.image('https://www.umk.pl/siw/galeria_inspiracje/UMKins8.jpg')


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            [data-testid="stDecoration"]{background-image: linear-gradient(90deg,#FFCD00 ,#0050AA );height: 0.25rem;}
            [class="stActionButton"] {visibility: hidden;}
            
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)










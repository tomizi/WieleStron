import os
import pandas as pd
import numpy as np
import streamlit as st
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path






st.set_page_config(page_title='UMK w liczbach', page_icon = ':page_facing_up:',initial_sidebar_state='expanded',layout='wide')

DF = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='nauczyciele',dtype={'Rok':int})

DF4 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Granty_złożone',dtype={'Rok':int})
DF5 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='nauczyciele_wydziały',dtype={'Rok':str})
DF6 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Granty_przyznane',dtype={'Rok':int})

DF7 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='L_kier_stud',dtype={'Rok':str})
DF8 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='N-wni',dtype={'Rok':int})
DF9 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Z-czni',dtype={'Rok':int})

DF10 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Stacjonarne',dtype={'Rok':int})
DF11 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Niestacjonarne',dtype={'Rok':int})
DF12 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='doktoranci',dtype={'Rok':int})
DF13 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Podyplomowe',dtype={'Rok':int})
DF14 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Ogółem',dtype={'Rok':int})

DF15 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Stud_og',dtype={'Rok':int})

DF16 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Stud_og',dtype={'Rok':int})
DF17 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Absolwenci',dtype={'Rok':int})
DF18 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Abs_og',dtype={'Rok':int})
DF19 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Wydz_sr',dtype={'Rok':int})
DF20 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Styp_min1',dtype={'Rok':int})
DF21 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Nacz_og',dtype={'Rok':int})
DF22 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Prac',dtype={'Rok':int})
DF23 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_pl',dtype={'Rok':int})

DF24 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_wydz',dtype={'Rok':int})
DF25 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_sr',dtype={'Rok':int})

DF26 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_St',dtype={'Rok':int})
DF27 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Pr_npwni',dtype={'Rok':int})

DF28 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Wynagrodzenie',dtype={'Rok':int})
DF29 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Inflacja',dtype={'Rok':int})
DF30 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Inflacja1',dtype={'Rok':float,'dr':str})

DF31 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Sukces',dtype={'Rok':int})

DF32 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='MEiN_pr',dtype={'Rok':int})
DF33 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='MEiN_zl',dtype={'Rok':int})
DF34 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Sukces_mein',dtype={'Rok':float})

DF35 = pd.read_excel(io='Studenci.xlsx',engine='openpyxl',sheet_name='Awanse',dtype={'Rok':float})

lata = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
wydziały = ['Matematyki i Informatyki',
                                                    'Chemii','Humanistyczny','Fizyki, Astronomii i Informatyki Stosowanej','Filozofii i Nauk Społecznych',
                                                    'Nauk Biologicznych i Weterynaryjnych','Nauk Ekonomicznych i Zarządzania','Nauk Historycznych','Nauk o Ziemi i Gospodarki Przestrzennej',
                                                    'Nauk o Polityce i Bezpieczeństwie','Prawa i Administracji','Sztuk Pięknych','Teologiczny','Lekarski',
                                                    'Farmaceutyczny','Nauk o Zdrowiu','Ogółem']
kolor = {'fioletowy':'rgb(170,40,150)','niebieski':'rgb(0,175,250)','zielony':'rgb(0,165,80)','oliwkowy':'rgb(170,210,60)','pomarańczowy':'rgb(255,130,30)','czerwony':'rgb(250,20,20)'}
kolwyd1 = {'Nauk Biologicznych i Weterynaryjnych(2019-2021)':kolor['zielony'],'Biologii i Ochrony Środowiska(2012-2018)':kolor['zielony'],'Filologiczny(2010-2018)':kolor['niebieski'],
           'Chemii':kolor['oliwkowy'],'Humanistyczny':kolor['niebieski'],'Fizyki, Astronomii i Informatyki Stosowanej':kolor['oliwkowy'],
          'Filozofii i Nauk Społecznych(2019-2021)':kolor['fioletowy'],'Matematyki i Informatyki':kolor['oliwkowy'],'Nauk Ekonomicznych i Zarządzania':kolor['fioletowy'],
          'Nauk Historycznych':kolor['niebieski'],'Nauk o Ziemi(2012-2018)':kolor['zielony'],'Nauk Pedagogicznych(2010-2018)':kolor['fioletowy'],'Politologii i Studiów Międzynarodowych(2010-2018)':kolor['fioletowy'],
          'Nauk o Ziemi i Gospodarki Przestrzennej(2019-2021)':kolor['oliwkowy'],'Nauk o Polityce i Bezpieczeństwie(2019-2021)':kolor['fioletowy'],'Prawa i Administracji':kolor['fioletowy'],'Sztuk Pięknych':kolor['pomarańczowy'],
          'Teologiczny':kolor['zielony'],'Lekarski':kolor['czerwony'],'Farmaceutyczny':kolor['czerwony'],'Nauk o Zdrowiu':kolor['czerwony'],'Ogółem':'rgb(0,80,170)',
	 'Interdyscyplinarne Centrum Nowoczesnych Technologii':kolor['oliwkowy'],'Biologii i Nauk o Ziemi(2010-2011)':kolor['zielony']}
kolwyd = {'Nauk Biologicznych i Weterynaryjnych':kolor['zielony'],'Biologii i Ochrony Środowiska':kolor['zielony'],'Filologiczny':kolor['niebieski'],
           'Chemii':kolor['oliwkowy'],'Humanistyczny':kolor['niebieski'],'Fizyki, Astronomii i Informatyki Stosowanej':kolor['oliwkowy'],
          'Filozofii i Nauk Społecznych':kolor['fioletowy'],'Matematyki i Informatyki':kolor['oliwkowy'],'Nauk Ekonomicznych i Zarządzania':kolor['fioletowy'],
          'Nauk Historycznych':kolor['niebieski'],'Nauk o Ziemi':kolor['zielony'],'Nauk Pedagogicznych':kolor['fioletowy'],'Politologii i Studiów Międzynarodowych':kolor['fioletowy'],
          'Nauk o Ziemi i Gospodarki Przestrzennej':kolor['oliwkowy'],'Nauk o Polityce i Bezpieczeństwie':kolor['fioletowy'],'Prawa i Administracji':kolor['fioletowy'],'Sztuk Pięknych':kolor['pomarańczowy'],
          'Teologiczny':kolor['zielony'],'Lekarski':kolor['czerwony'],'Farmaceutyczny':kolor['czerwony'],'Nauk o Zdrowiu':kolor['czerwony'],'Ogółem':'rgb(0,80,170)',
	 'Interdyscyplinarne Centrum Nowoczesnych Technologii':kolor['oliwkowy'],'Biologii i Nauk o Ziemi':kolor['zielony']}

pr_cy = {'Ogółem':'rgb(0,70,180)','Nauczyciele akademiccy':'rgb(0,175,250)','Profesorowie':'rgb(170,40,150)','Adiunkci':'rgb(250,20,20)','Asystenci i lektorzy':'rgb(255,130,30)','Nienauczyciele':'rgb(255,205,0)','Średnia krajowa':'rgb(204,204,204)'}
pr_cy1 = {'Ogółem':0,'Nauczyciele akademiccy':1,'Profesorowie':2,'Adiunkci':3,'Asystenci i lektorzy':4,'Nienauczyciele':5,'Średnia krajowa':6}
pr_cy2 = ['Ogółem','Nauczyciele akademiccy','Profesorowie','Adiunkci','Asystenci i lektorzy','Nienauczyciele','Średnia krajowa']

        
        
        
        
        
        


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
background-size:400px, 400px;
background-position: 1150px 100px;
background-repeat: no-repeat;
background-attachment: fixed;}
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


new_title = '<b style="color:rgb(0, 80, 170); font-size: 62px;">Studenci</p>'
st.markdown(new_title, unsafe_allow_html=True)
st.markdown('---')

st.header('Liczba kierunków studiów w latach 2009-2021')
st.plotly_chart(px.bar(DF7,x='Rok',y='Liczba',width=1400,height=500).update_traces(marker_color='rgb(0,80,170)',texttemplate="%{y:}",hovertemplate = 'Liczba kierunków: %{y:}',
	textposition='inside',textfont=dict( size=14))
	.update_xaxes(title_font=dict(size=12), title='Lata').update_yaxes(title_font=dict(size=12),title = 'Liczba kierunków',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")))

   
st.header('Liczba uczestników studiów w podziale na wydziały w latach 2010-2021')
q1, q2 = st.columns(2)
kat34 = q1.selectbox('Wybierz kategorię : ',['Ogółem','Studia stacjonarne','Studia niestacjonarne','Doktoranckie','Podyplomowe'])


fig = px.bar(DF13,x='Rok',y='Liczba',width=1500,height=500).update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_traces(hovertemplate = 'Liczba uczestników: %{y:}',textfont=dict( size=14),marker_color='rgb(0,70,180)',texttemplate="%{y:}",textposition='inside').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"))
fig1 = px.bar(DF14,x='Rok',y='Liczba',width=1500,height=500).update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_traces(hovertemplate = 'Liczba uczestników: %{y:}',textfont=dict( size=14),marker_color='rgb(0,70,180)',texttemplate="%{y:}",textposition='inside').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"))
if kat34 == 'Studia stacjonarne':
    wydzial34 = q2.selectbox('Wybierz wydział : ',DF12['Wydział'].unique(),index=10)
    st.plotly_chart(px.bar(DF10[DF10['Wydział']==wydzial34],x='Rok',y='Liczba',width=1500,height=500)
			.update_traces(marker_color=kolwyd1[wydzial34],texttemplate="%{y:}",textposition='inside',textfont=dict( size=14),hovertemplate = 'Liczba studentów: %{y:}')
			.update_xaxes(dtick=1)
			.update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba studentów',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
			.update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")))
elif kat34 == 'Studia niestacjonarne':
    wydzial34 = q2.selectbox('Wybierz wydział : ',DF12['Wydział'].unique(),index=10)
    st.plotly_chart(px.bar(DF11[DF11['Wydział']==wydzial34],x='Rok',y='Liczba',width=1500,height=500)
			.update_traces(marker_color=kolwyd1[wydzial34],texttemplate="%{y:}",textposition='inside',textfont=dict( size=14),hovertemplate = 'Liczba studentów: %{y:}')
			.update_xaxes(dtick=1)
			.update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba studentów',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
			.update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")))
elif kat34 == 'Doktoranckie':
    wydzial34 = q2.selectbox('Wybierz wydział : ',DF12['Wydział'].unique(),index=10)
    st.plotly_chart(px.bar(DF12[DF12['Wydział']==wydzial34],x='Rok',y='Liczba',width=1500,height=500)
			.update_traces(hovertemplate = 'Liczba doktorantów: %{y:}',textfont=dict( size=14),marker_color=kolwyd1[wydzial34],texttemplate="%{y:}",textposition='inside').update_xaxes(dtick=1).update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba doktorantów',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
			.update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")))
elif kat34 == 'Podyplomowe':
    st.plotly_chart(fig)
elif kat34 == 'Ogółem':
    st.plotly_chart(fig1)

st.header('Liczba absolwentów na uniwersytecie w latach 2010-2021')
ab = st.selectbox('Wybierz kategorię:    ',['Ogółem','Studia stacjonarne','Studia niestacjonarne','Doktoranckie','Podyplomowe'])	
st.plotly_chart(px.bar(DF17[(DF17['Kategoria']=='Absolwent') & (DF17['Rodzaj']==ab)],x='Rok',y='Liczba',width=1500,height=500)
		    .update_traces(marker_color='rgb(0,70,180)',texttemplate="%{y:}",textposition='inside',textfont=dict( size=14,color='white'),hovertemplate = 'Liczba absolwentów: %{y:}')
		    .update_xaxes(dtick=1)
		    .update_yaxes(tickformat=" ",title='Liczba absolwentów',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")))
	
st.header('Zmiana liczby studentów i absolwentów w stosunku do roku poprzedniego (w %) w latach 2010-2021')
kat43 = st.selectbox('Wybierz kategorię :   ',['Ogółem','Studia stacjonarne','Studia niestacjonarne','Doktoranckie','Podyplomowe'])
st.plotly_chart(px.line(DF17[DF17['Rodzaj']==kat43],x='Rok',y='Zmiana[%]',color = 'Kategoria',hover_name="Kategoria",markers=True,width=1500,height=500,color_discrete_sequence=['blue','red'])
		    .update_traces(hovertemplate = 'Zmiana liczby: %{y:,.2f}%',textposition="top right",texttemplate = "%{y:,.2f}%",textfont=dict( size=14))
	.update_xaxes(title_font=dict(size=12), title='Rok',range=[2010.95,2021+1/5],dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
		    .update_yaxes(title_font=dict(size=12),title = 'Zmiana liczby studentó/absolwentów[%]',tickformat=",",range=[-50,50],zeroline=True, zerolinewidth=4, zerolinecolor='rgba(0,0,0,1)',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')                        
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"))

	
	
	
	


st.header('Odsetek studentów zagranicznych w podziale na rodzaj studiów w latach 2012-2021')
st.plotly_chart(px.line(DF9,x='Rok',y='Odsetek',color = 'Rodzaj',hover_name="Rodzaj",width=1500,height=500,markers=True,color_discrete_sequence=['rgb(0,80,170)','rgb(0,200,255)','red','rgb(255,50,80)'])
		    .update_traces(textposition="top right",hovertemplate = 'Odsetek osób zagranicznych: %{y:,.2f}%',texttemplate = "%{y:.2f}%",textfont=dict( size=14))
	.update_xaxes(title_font=dict(size=12), title='Rok',range=[2011.95,2021+1/5],dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside')
		    .update_yaxes(title_font=dict(size=12),title = 'Odsetek osób zagranicznych[%]',tickformat=",",rangemode='tozero',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"))
	
	
st.header('Odsetek studentów niepełnosprawnych w podziale na rodzaj studiów w latach 2012-2021')
st.plotly_chart(px.line(DF8,x='Rok',y='Odsetek',color = 'Rodzaj',hover_name="Rodzaj",width=1500,height=500,markers=True,color_discrete_sequence=['rgb(0,80,170)','rgb(0,200,255)','red','rgb(255,50,80)'])
		    .update_traces(textposition="top right",hovertemplate = 'Odsetek osób niepełnosprawnych: %{y:,.2f}%',texttemplate = "%{y:,.2f}%",textfont=dict( size=14))
	.update_xaxes(title_font=dict(size=12), title='Rok',range=[2011.95,2021+1/5],dtick=1,showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside').update_yaxes(title_font=dict(size=12),title = 'Odsetek osób niepełnosprawnych[%]',tickformat=",",rangemode='tozero',showline=False,linewidth=1,gridwidth=1,gridcolor='gray')
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',',hovermode="x"))


st.header('Porównanie liczby studentów na wybranych dwóch wydziałach wraz z wydziałem średnim w latach 2010-2021')
q11, q22 = st.columns(2)
wydz11 = q11.selectbox('Wybierz wydział :                                                                          ',DF12[DF12['Wydział']!='Ogółem']['Wydział'].unique(),index=2)
wydz22 = q22.selectbox('Wybierz wydział :                                                                        ',DF12[DF12['Wydział']!='Ogółem']['Wydział'].unique(),index=3)
gz = st.radio('Średnia liczba studentów na wydziałach - Włącz/Wyłącz:',('Włącz','Wyłącz'))
fig4 = px.bar(DF15[(DF15['Wydział'].isin([wydz11,wydz22]))],x='Rok',y='Liczba',barmode = 'group',hover_name="Wydział", color='Wydział',width=1500,height=500,color_discrete_map={wydz11: kolwyd1[wydz11],wydz22: kolwyd1[wydz22]},pattern_shape="Wydział").update_yaxes(tickformat=",",showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',title='Liczba studentów').update_traces(hovertemplate = 'Liczba studentów: %{y:}',textfont=dict( size=14),texttemplate="%{y:}",textposition='inside').update_xaxes(dtick=1).update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
if gz == 'Włącz':
	    fig5 = px.line(DF19,x='Rok',y='Liczba',color_discrete_sequence=['rgb(0,80,170)'],markers=True).update_traces(hovertemplate = 'Średnia liczba studentów: %{y:,.2f}',textfont=dict( size=14),textposition="top left",texttemplate = "%{y:.2f}").update_yaxes(tickformat=",").update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=',')
	    fig4.add_trace(fig5.data[0])
	    st.plotly_chart(fig4)
else:
    st.plotly_chart(fig4)


st.header('Zmiana liczby studentów w stosunku do roku poprzedniego w podziale na wydziały w latach 2011-2021')
wydz1 = st.multiselect('Wybierz wydział :  ',DF12['Wydział'].unique(),['Ogółem','Matematyki i Informatyki'])
st.plotly_chart(px.line(DF15[(DF15['Wydział'].isin(wydz1))].sort_values(by=['Wydział','Rok']),x='Rok',y='Zmiana',hover_name="Wydział",color='Wydział',width=1400,height=500,symbol='Wydział',markers=True,color_discrete_sequence=list(map(lambda x: kolwyd1[x],sorted(wydz1))))
		    .update_traces(marker_size=10,textposition='top right',texttemplate="%{y:,d}",textfont=dict( size=14),hovertemplate='Zmiana liczby studentów: %{y:,.2f}%')
		    .update_xaxes(showline=True,showticklabels=True,linecolor='gray',linewidth=1,ticks='outside',range=[2011-1/5,2021+1/5],dtick=1)
		    .update_yaxes(tickformat = ' ',rangemode='tozero',zeroline=True, zerolinewidth=4, zerolinecolor='rgba(0,0,0,1)',showline=False,linewidth=1,gridwidth=1,gridcolor='gray',title='Zmiana liczby studentów[%]')
		    .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),separators=' ',hovermode="x"))



st.header('Stypendia ministra w podziale na wydziały wraz ze współczynnikiem skuteczności (w %) w latach 2012-2021')
r = st.selectbox('Wybierz rok : ', lata,index=9)

lg = pd.DataFrame(DF20[DF20['Rok']==r].groupby('Wydział')['Przyznane'].agg(np.sum)).sort_values(by='Przyznane')[::-1]
x = lg.index[::-1]
y = lg['Przyznane'][::-1]
lg = lg.reset_index()
lg['kolor']=' '
for j,i in enumerate(lg['Wydział']):
    if i in list(kolwyd.keys()):
        lg['kolor'][j] = kolwyd[i]
else:
    lg['kolor'][j] = 'rgb(0,70,180)'
barwa4 = lg['kolor'][::-1]
lg1 = pd.DataFrame(DF20[DF20['Rok']==r].groupby('Wydział')['Złożone'].agg(np.sum)).sort_values(by='Złożone')[::-1]
x1 = lg1.index[::-1]
y1 = lg1['Złożone'][::-1]
lg1 = lg1.reset_index()
lg1['kolor']=' '
for j,i in enumerate(lg1['Wydział']):
    if i in list(kolwyd.keys()):
        lg1['kolor'][j] = kolwyd[i]
else:
    lg1['kolor'][j] = 'rgb(0,70,180)'
barwa5 = lg1['kolor'][::-1]
fig = go.Figure()      

fig.add_trace(go.Bar(x=y,y=x,orientation='h',text=y,hovertemplate = 'Stypendia przyznane: %{x:}'+"<extra></extra>",
textfont=dict( size=12,color='black'),marker_color=barwa4,
 textposition='outside',texttemplate = "<b>Przyznane-%{x:}"))
	    
fig.add_trace(go.Bar(x=y1,y=x1,orientation='h',text=y1,hovertemplate = 'Wnioski złożone: %{x:}'+"<extra></extra>",
textfont=dict( size=12,color='black'),marker_color=barwa5,
textposition='outside',texttemplate = "<b>Złożone-%{x:}"))
fig.update_xaxes(title='Liczba wniosków',range=[0,y1['Ogółem']+15]).update_traces(marker_line_color='black',marker_line_width=1.5)
fig.update_yaxes(title='Wydział')
fig.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),
height=800,width=1500,plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"),barmode='group',
separators =',',showlegend=False)

st.plotly_chart(fig)
     	       
lg7 = pd.DataFrame(DF20[DF20['Rok']==r].groupby('Wydział')['Skuteczność'].agg(np.sum)).sort_values(by='Skuteczność')[::-1]
x7 = lg7.index[::-1]
y7 = lg7['Skuteczność'][::-1]


lg7 = lg7.reset_index()
lg7['kolor']=' '
for j,i in enumerate(lg7['Wydział']):
    if i in list(kolwyd.keys()):
        lg7['kolor'][j] = kolwyd[i]
    else:
        lg7['kolor'][j] = 'rgb(0,70,180)'
barwa7 = lg7['kolor'][::-1]

fig7 = go.Figure()
fig7.add_trace(go.Bar(x=y7,y=x7,orientation='h',text=y7,hovertemplate = 'Skuteczność: %{x:,.2f}%'+"<extra></extra>",
                    textfont=dict( size=12,color='black')))
fig7.update_traces(marker_color=barwa7,marker_line_color='black',marker_line_width=1.5,
                  textposition='outside',texttemplate = "<b>%{x:,.2f}%")
fig7.update_xaxes(title='Współczynnik skuteczności')
fig7.update_yaxes(title='Wydział')

fig7.update_layout(xaxis=dict(showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray',mirror=True),
                            height=600,width=1600,plot_bgcolor='white',margin=dict(t=100, b=100, l=0, r=200),font=dict(family='Lato',size=18,color="Black"),barmode='group',
                            separators =',',autosize=False)

st.plotly_chart(fig7)


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            [data-testid="stDecoration"]{background-image: linear-gradient(90deg,#FFCD00 ,#0050AA );height: 0.25rem;}
            [class="stActionButton"] {visibility: hidden;}
            
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

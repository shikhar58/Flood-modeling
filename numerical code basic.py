# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 23:52:53 2023

@author: shikh
"""


import numpy as np

length=1000
time=3600

sizex=20
sizet=2

hint=1
hinf=2
houtf=1

vint=1
voutf=1
vinf=2


h=np.zeros((int(time/sizet),int(length/sizex)))


v=np.zeros((int(time/sizet),int(length/sizex),))

h[0,:] = hint


h[:,0]=hinf

h[:,-1]=houtf



v[0,:] = vint

v[:,0]=vinf

v[:,-1]=voutf


rat=sizet/sizex


for i in range(0,int(time/sizet)-1):
    for j in range(1,int(length/sizex)-1):
        h[i+1,j]=h[i,j]+rat*(h[i,j-1]*v[i,j-1]-h[i,j]*v[i,j])
        v[i+1,j]=h[i,j]+rat*(v[i,j]*(v[i,j-1]-v[i,j])+9.8*(h[i,j-1]-h[i,j]))
        print("x and t are",j,i)
        
        
import matplotlib.pyplot as plt

fig=plt.figure()

plt.plot(range(len(v[:,0])),v[:,40])
plt.show()

st.pyplot(fig)

plt.plot(range(len(h[:,0])),h[:,40])



st.pyplot(fig)


"""
# Add a slider widget using the st.slider function
selected_value = st.slider("Select a Range", min_value, max_value, initial_value)



# Display the selected range values
st.write(f"Selected Value: {selected_value}")

headerSection=st.container()

mainsection=st.container()

with headerSection:
    st.title("Streamlit")

"""
        

st.title("temporal evolution of water velocity and height at a distance")

chosenx = st.slider("Select a distance", 0, 1000, 500)
    
status_plott=st.button("plot temporal evolution")

if status_plott:
    plottimeatonex(hr,vr,chosenx)
    
st.title("spatial evolution of water velocity and height at a time")

chosent = st.slider("Select a distance", 0, 3600, 1800)

status_plotx=st.button("plot spatial evolution")

if status_plotx:
    plotxatonetime(hr,vr,chosent)


            
def plottimeatonex(h,v,xtoplot):
    fig=plt.figure()
    plt.plot(range(len(v[:,0])),v[:,int(xtoplot/sizex)])
    plt.show()
    st.pyplot(fig)
    plt.clf()
    fig=plt.figure()
    plt.plot(range(len(h[:,0])),h[:,int(xtoplot/sizex)])
    plt.show()
    st.pyplot(fig)
    plt.clf()

def plotxatonetime(h,v,timetoplot):
    fig=plt.figure()
    plt.plot(range(len(v[0,:])),v[int(timetoplot/sizet),:])
    st.pyplot(fig)
    plt.clf()
    fig=plt.figure()
    plt.plot(range(len(h[0,:])),h[int(timetoplot/sizet),:])
    st.pyplot(fig)
    plt.clf()


        st.title("spatial evolution of water velocity and height at a time")
        
        chosent = st.slider("Select a distance", 0, 3600, 1800)
        
        status_plotx=st.button("plot spatial evolution")
        
        if status_plotx:
            plotxatonetime(hr,vr,chosent)        
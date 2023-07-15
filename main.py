
    
    
import numpy as np

import streamlit as st
import matplotlib
import matplotlib.pyplot as plt

#matplotlib.use('TkAgg')


length=1000
time=3600

sizex=20
sizet=2





st.title("1D flood simulation (beta)")

st.text("Modeling unsteady water flow with Saint-venant equation")

st.image("image.jpg")
# Define the minimum and maximum values for the range
min_value = 0
max_value = 100

initial_value=50


    
def numericalmodel(hint,vint,hinf,vinf,houtf,voutf):
    
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
    return h,v
            
            
def plottimeatonex(h,v,xtoplot):
    a=np.array([sizet*i for i in range(int(time/sizet)) ])
    col1, col2 = st.columns(2)
    with col1:
        fig,ax=plt.subplots()
        ax.plot(a,v[:,int(xtoplot/sizex)])
        ax.set_xlabel("total time (seconds)")
        ax.set_ylabel("water velocity (m/s)")
        st.pyplot(fig)
        plt.clf()
    with  col2:
        fig,ax=plt.subplots()
        ax.plot(a,h[:,int(xtoplot/sizex)])
        ax.set_xlabel("total time (seconds)")
        ax.set_ylabel("water height (m)")
        st.pyplot(fig)
        plt.clf()

def plotxatonetime(h,v,timetoplot):
    b=np.array([sizex*i for i in range(int(length/sizex)) ])
    col1, col2 = st.columns(2)
    with col1:
        fig,ax=plt.subplots()
        ax.plot(b,v[int(timetoplot/sizet),:])
        ax.set_xlabel("length of stream (m)")
        ax.set_ylabel("water velocity (m/s)")
    
        st.pyplot(fig)
        plt.clf()
    with col2:
        fig,ax=plt.subplots()
        ax.plot(b,h[int(timetoplot/sizet),:])
        ax.set_xlabel("length of stream (m)")
        ax.set_ylabel("water height (m)")
    
        st.pyplot(fig)
        plt.clf()


def main():
    st.title("Initial values")
    col1, col2 = st.columns(2)
    
    with col1:
        slider_label1 = "Initial value of water height (m)"
        hint = st.slider(slider_label1, 0, 5, 2)
    
    
    with col2:
        slider_label2 = "Initial value of water velocity (m/s)"
        vint = st.slider(slider_label2, 0, 5, 1)
        
        
    st.title("Inflow condition")
    col1, col2 = st.columns(2)
    
    with col1:
        slider_label1 = "Water height at inflow point (m)"
        hinf = st.slider(slider_label1, 0, 5, 2)
    
    
    with col2:
        slider_label2 = "water velocity at inflow point (m/s)"
        vinf = st.slider(slider_label2, 0, 5, 2)
        
    st.title("outflow condition")
    col1, col2 = st.columns(2)
    
    with col1:
        slider_label1 = "Water height at outflow point (m)"
        houtf = st.slider(slider_label1, 0, 5, 1)
    
    
    with col2:
        slider_label2 = "water velocity at outflow point (m/s)"
        voutf = st.slider(slider_label2, 0, 5,1)
        
    hr,vr=numericalmodel(hint,vint,hinf,vinf,houtf,voutf)
    st.write("model run succcessful")
    
    st.title("Temporal evolution")
    
    chosenx = st.slider("Select a distance", 0, 1000, 500)
        
    plottimeatonex(hr,vr,chosenx)
    
    st.title("Spatial evolution")
    
    chosent = st.slider("Select a time", 0, 3600, 1800)
    
    plotxatonetime(hr,vr,chosent)        
    


if __name__=="__main__":
    main()






    
    




    





    
    
import numpy as np

import streamlit as st
import matplotlib
import matplotlib.pyplot as plt

#matplotlib.use('TkAgg')


length=1000
time=3600

sizex=20
sizet=10

st.title("check this out")
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
    fig=plt.figure()
    plt.plot(range(len(v[:,0])),v[:,int(xtoplot/sizex)])
    
    st.pyplot(fig)
    plt.clf()
    fig=plt.figure()
    plt.plot(range(len(h[:,0])),h[:,int(xtoplot/sizex)])
    
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


def main():
    st.title("Initial values")
    col1, col2 = st.columns(2)
    
    with col1:
        slider_label1 = "Initial value of water height"
        hint = st.slider(slider_label1, 0, 5, 2)
    
    
    with col2:
        slider_label2 = "Initial value of water velocity"
        vint = st.slider(slider_label2, 0, 5, 1)
        
        
    st.title("Inflow condition")
    col1, col2 = st.columns(2)
    
    with col1:
        slider_label1 = "Water height at inflow point"
        hinf = st.slider(slider_label1, 0, 5, 2)
    
    
    with col2:
        slider_label2 = "water velocity at inflow point"
        vinf = st.slider(slider_label2, 0, 5, 2)
        
    st.title("outflow condition")
    col1, col2 = st.columns(2)
    
    with col1:
        slider_label1 = "Water height at outflow point"
        houtf = st.slider(slider_label1, 0, 5, 1)
    
    
    with col2:
        slider_label2 = "water velocity at outflow point"
        voutf = st.slider(slider_label2, 0, 5,1)
        
    hr,vr=numericalmodel(hint,vint,hinf,vinf,houtf,voutf)
    st.write("model run succcessful")
    
    st.title("temporal evolution of water velocity and height at a distance")
    
    chosenx = st.slider("Select a distance", 0, 1000, 500)
        
    plottimeatonex(hr,vr,chosenx)
            



if __name__=="__main__":
    main()






    
    




    




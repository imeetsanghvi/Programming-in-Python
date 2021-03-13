#Code for: WINNER TAKE IT ALL 
#Subject: SOFT COMPUTING 
#STUDENTS: MEET A SANGHVI & DARSHIN K SHAH
#ROLL NO: 50 AND 51
#UNIVERSITY: SVKM'S NMIMS MPSTME
def get_data(): 
  '''gets all data 
  1) inputX = number of input neurons 
  2) outputY = number of output neurons
  3) outs = array to store value open
  4) alpha =  learning constant
  5) Xvals = values of input neurons
  6) lines = weight values for all output neurons with respect to input.
  '''
  inputX, outputY = input("Enter the number of input and output nodes:").split(' ')
  inputX= int(inputX)
  outputY= int(outputY)
  alpha = 1
  lines= np.zeros((outputY,inputX))
  outs = np.asarray([0]*outputY)
  Xvals = np.asarray([0]*inputX)
  beark = '---------------------------------------------------'
  print(beark)
  print('Enter values of all X input')
  for i in range(0,inputX):
    print('Input Index = ',i,' Out of total index = ',inputX-1)
    Xvals[i] = input()
  #print
  return inputX,outputY,alpha,outs,Xvals,lines

def display_data(inputX, outputY, alpha, outs, Xvals, lines):
  beark = '---------------------------------------------------'
  print(beark)
  print('Display Function Here:')
  print(' Number of Input neurons = ',inputX)
  print(' Number of output neurons = ',outputY)
  print(' Learning Constant Aalpha = ',alpha)
  print(' Output Neurons ',outs)
  print(' Values of Input Neurons ',Xvals)
  print(' lines weights ',lines)
  print(beark)

def wtan(inputX,outputY,alpha,outs,Xvals,lines):
  for i in range(0,outputY):
    for j in range(0,inputX):
      print("Enter the ", j ,"th weight for output neuron :",i,' =>')
      lines[i][j] = int(input())
    outs[i] = sum(Xvals*lines[i])
  winer = np.argmax(outs)
  vals = alpha*(Xvals - lines[winer])
  print('Winner node is :',winer)
  print(' Delta W is ',vals)
  lines[winer] = lines[winer]+vals
  display_data(inputX,outputY,alpha,outs,Xvals,lines)
  return inputX,outputY,alpha,outs,Xvals,lines
  
import numpy as np 
#numpy is used for working with arrays
#main here
inputX,outputY,alpha,outs,Xvals,lines = get_data()
display_data(inputX,outputY,alpha,outs,Xvals,lines)
inputX,outputY,alpha,outs,Xvals,lines = wtan(inputX,outputY,alpha,outs,Xvals,lines)
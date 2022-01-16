import pandas as pd
from bokeh.plotting import figure,show,output_file
import matplotlib.pyplot as plt
def calculate_data():
    # Read data from file
    df = pd.read_csv('Desktop/population.csv')
    print("Age below 14 years");
    age1=df.loc[df['Year']==1960,'population'].sum();
    print("1960 population : ", age1) 
    age2=df.loc[df['Year']==1965,'population'].sum();
    print("1965 population : ", age2) 
    age3=df.loc[df['Year']==1970,'population'].sum();
    print("1970 population : ", age3) 
    age4=df.loc[df['Year']==1975,'population'].sum();
    print("1975 population : ", age4) 
    age5=df.loc[df['Year']==1980,'population'].sum();
    print("1980 population : ", age5) 
    age6=df.loc[df['Year']==1985,'population'].sum();
    print("1985 population : ", age6) 
    age7=df.loc[df['Year']==1990,'population'].sum();
    print("1990 population : ", age7) 
    age8=df.loc[df['Year']==1995,'population'].sum();
    print("1995 population : ", age8) 
    age9=df.loc[df['Year']==2000,'population'].sum();
    print("2000 population : ", age9) 
    age10=df.loc[df['Year']==2005,'population'].sum();
    print("2005 population : ", age10) 
    age11=df.loc[df['Year']==2010,'population'].sum();
    print("2010 population : ", age11) 
  
    print("Change in population")
    print("1960-1965",age2-age1);
    print("1965-1970",age3-age2);
    print("1970-1975",age4-age3);
    print("1975-1980",age5-age4);
    print("1980-1985",age6-age5);
    print("1985-1990",age7-age6);
    print("1990-1995",age8-age7);
    print("1995-2000",age9-age8);
    print("2000-2005",age10-age9);
    print("2005-2010",age11-age10);
   
    x=[1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010]
    y=[age1,age2,age3,age4,age5,age6,age7,age8,age9,age10,age11]
    output_file('a.html')
    p=figure(title='change in population(<14 yrs)',x_axis_label='year',y_axis_label='population')
    p.line(x,y,legend_label='population growth',line_width=1,color='red')
    show(p)
    

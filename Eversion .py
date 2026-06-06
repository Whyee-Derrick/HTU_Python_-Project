import streamlit as st
import os

st.title("Introduction to python programming grading system 🧑‍🏫")
st.write("Have fun grading your students 😁")



students_name = st.text_input(" Enter student name ")
students_index_No =st.text_input("Enter student index number")

continuous_assesment=st.number_input("Enter student Continuous Assesment (0-40)", min_value=0,max_value=40,value=0)
exams_score=st.number_input("Enter student Exams score (0-60)",min_value=0,max_value=60,value=0)
result = continuous_assesment + exams_score


grade = ""
if  85 <= result <= 100:
    grade = "A+"
    
elif  80 <= result <= 84:
    grade = "A"
    
elif  75 <= result <= 79:
    grade = "B+"
    
elif  70 <= result <= 74:
    grade = "B"

elif  65 <= result <= 69:
    grade = "C+"
    
elif 60 <= result <= 64: 
    grade = "C"
    
elif 55 <= result <= 59:  
    grade = "D+"
    
elif  50 <= result <= 54:
    grade = "D"
    
else:
    grade = "E"  

st.subheader("Submission and File Saving")
if st.button ("Submit and Record student Data"):
    if students_name.strip() == "" or students_index_No.strip()  =="":
        st.error("Please fill out the student Name and index Number before submitting.")
    else:
        st.success(f"Grading complete for {students_name}!")
        st.write(f"Total Score: {result}") 
        st.write(f"Final Grade: {grade}") 
        
        path = r"C:\Users\PERSONAL\Downloads\programing work.txt"
        
        students_record = f" Name: {students_name}  | Index: {students_index_No} | CA: {continuous_assesment} | Exams: {exams_score} | Total: {result} | Grade: {grade}\n"
        
        try:
            with open(path, "a", encoding ="utf-8") as file:
                file.write(students_record)
                st.info("Data successfully documented to 'programing work.txt'")
        except Exception as e:
            st.error (f"Could not save file . Error : {e}")
                     



         
         
          
         
        
    

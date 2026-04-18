import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title="Dashboard", layout="wide")

st.markdown("""
<style>

.stApp {
    background-color: #f3e5f5;
}

/* cards */
.card {
    padding:20px;
    border-radius:15px;
    color:white;
    box-shadow:0 4px 10px rgba(0,0,0,0.15);
    text-align:center;
    font-size:20px;
    font-weight:bold;
}

.blue {background: linear-gradient(135deg,#2196F3,#21CBF3);}
.green {background: linear-gradient(135deg,#00b09b,#96c93d);}
.orange {background: linear-gradient(135deg,#f7971e,#ffd200);}
.purple {background: linear-gradient(135deg,#8E2DE2,#4A00E0);}

</style>
""", unsafe_allow_html=True)


st.title("🎓📊 Student Result Analysis Dashboard")

data = {
    "Student": ["Aman","Riya","Karan","Neha","Rahul","Simran","Arjun","Priya"],
    "C":[92,88,85,90,78,81,95,84],
    "Python":[37,72,30,68,65,74,91,79],
    "Java":[89,90,78,44,77,79,48,83],
    "Web Development":[91,30,52,55,44,61,94,86],
}

df = pd.DataFrame(data)

def get_grade(marks):

    if marks >= 91:
        return "O"
    elif marks >= 81:
        return "A+"
    elif marks >= 71:
        return "A"
    elif marks >= 61:
        return "B+"
    elif marks >= 51:
        return "B"
    elif marks >= 41:
        return "C"
    elif marks >= 33:
        return "D"
    else:
        return "F"


df["C Grade"] = df["C"].apply(get_grade)
df["Python Grade"] = df["Python"].apply(get_grade)
df["Java Grade"] = df["Java"].apply(get_grade)
df["Web Development Grade"] = df["Web Development"].apply(get_grade)

df["Total"] = df[["C","Python","Java","Web Development"]].sum(axis=1)

topper = df.loc[df["Total"].idxmax()]

st.success(f"🥇 Topper: {topper['Student']} with {topper['Total']} marks")

avg_c = df["C"].mean()
avg_python = df["Python"].mean()
avg_java = df["Java"].mean()
avg_web = df["Web Development"].mean()

st.subheader("📊 Overall Performance")

col1,col2,col3,col4 = st.columns(4)

col1.markdown(f"""
<div class="card blue">
💻 C <br>
{round(avg_c,2)}
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="card green">
🐍 Python <br>
{round(avg_python,2)}
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="card orange">
☕ Java <br>
{round(avg_java,2)}
</div>
""", unsafe_allow_html=True)

col4.markdown(f"""
<div class="card purple">
🌐 Web Dev <br>
{round(avg_web,2)}
</div>
""", unsafe_allow_html=True)


st.divider()

st.subheader("🔎 View Individual Result")

student_name = st.selectbox("Select Student", df["Student"])

student_data = df[df["Student"] == student_name]

st.subheader(f"📈 Result of {student_name}")

c1,c2,c3,c4 = st.columns(4)

c1.markdown(f"""
<div class="card blue">
💻 C <br>
{int(student_data["C"].values[0])}
</div>
""", unsafe_allow_html=True)

c2.markdown(f"""
<div class="card green">
🐍 Python <br>
{int(student_data["Python"].values[0])}
</div>
""", unsafe_allow_html=True)

c3.markdown(f"""
<div class="card orange">
☕ Java <br>
{int(student_data["Java"].values[0])}
</div>
""", unsafe_allow_html=True)

c4.markdown(f"""
<div class="card purple">
🌐 Web Dev <br>
{int(student_data["Web Development"].values[0])}
</div>
""", unsafe_allow_html=True)

if (
    student_data["C"].values[0] >= 33
    and student_data["Python"].values[0] >= 33
    and student_data["Java"].values[0] >= 33
    and student_data["Web Development"].values[0] >= 33
):

    st.success("✔️ Result: PASS")

else:

    st.error("❌ Result: FAIL")

df.index = df.index + 1
df.index.name = "S.No"

st.subheader("📋 Student Details")
st.dataframe(df)

st.subheader("📊 Performance Charts")

col_chart1, col_chart2 = st.columns(2)

with col_chart1:

    all_grades = pd.concat([
        df["C Grade"],
        df["Python Grade"],
        df["Java Grade"],
        df["Web Development Grade"]
    ])

    grade_count = all_grades.value_counts()

    fig1, ax1 = plt.subplots(figsize=(3,3))

    ax1.pie(
        grade_count,
        labels=grade_count.index,
        autopct='%1.1f%%'
    )

    ax1.set_title("Grade Distribution")

    st.pyplot(fig1)

with col_chart2:

    subjects = ["C","Python","Java","Web Dev"]
    averages = [avg_c, avg_python, avg_java, avg_web]

    fig2, ax2 = plt.subplots(figsize=(3,3))

    ax2.bar(subjects, averages)

    ax2.set_title("Average Marks by Subject")

    ax2.set_xlabel("Subjects")

    ax2.set_ylabel("Average Marks")

    st.pyplot(fig2)

st.subheader("📘 Grading System")

st.write("""
O  = Outstanding ⭐  
A+ = Excellent 🎯  
A  = Very Good 👍  
B+ = Good 🙂  
B  = Above Average 👌  
C  = Average 📚  
D  = Pass ✔️  
F  = Fail ❌
""")

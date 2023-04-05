from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in  locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Nitish_Senior_Python _Developer_for_RT.pdf"
Python_certificate_file = current_dir / "assets" / "Flask_cerificate.jfif"
profile_pic = current_dir / "assets" / "profile-pic-c.png"


PAGE_TITLE="RESUME|SINGIDI NITISH REDDY"
NAME = "SINGIDI NITISH REDDY"
DESCRIPTION="""I am an analytical, solutions-oriented senior Python software development professional with 7 years of experience in automating tasks with Python,
 building REST APIs, creating Python modules, conducting unit testing, designing backend architecture, and managing teams."""

PAGE_ICON = ":simle:"

EMAIL = "snitishreddy@gmail.com"
SOCIAL_MEDIA_LINKS = {
    "LinkedIn": "https://www.linkedin.com/in/nitishreddy",
    "GitHub": "https://github.com/nitish0565",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout='wide')


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# with open(Python_certificate_file, "rb") as pdf_file:
#     certificate = pdf_file.read()

profile_pic = Image.open(profile_pic)
certificate = Image.open(Python_certificate_file)



# --- HERO SECTION ---
# header_left_col = st.columns(1)
# with header_left_col:
st.image(profile_pic,width=250)
st.write("Python Developer at RandomTrees | 7+ Years | Backend Developer| Flask")
st.subheader(NAME)

st.write(DESCRIPTION)
st.write(EMAIL)
cols = st.columns(len(SOCIAL_MEDIA_LINKS))
for index, (platform, link) in enumerate(SOCIAL_MEDIA_LINKS.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ► I am experienced in project code management and structuring, and I am knowledgeable in both
    monolithic and microservices architectures..
- ► I have a strong knowledge in creating web REST APIs using Flask, FlaskRestx, and Django
    frameworks, and working with databases such as Redis, PostgreSQL, Elasticsearch, MySQL,
    MongoDB, and SQL Alchemy.
- ►️I have ensured web API security by using JWT/OAuth tokenization, encrypting sensitive data,
    logging each process, properly handling DB communication, encrypting data in DB, and
    implementing user-level authorization and authentication..
- ►️I have Implemented Redis Queues for handling API/tasks. Eased Deployment Code Optimization with Docker and Docker Compose file.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- ● Programming: Python (Flask, Flask-restx, FastAPI, Airflow, Azure Function App)
- ● Software and tools: Visual Studio, pycharm,Anaconda,Spyder, Jupiter, photoshop,Postman, Swagger
- ● Cloud Knowledge: Azure(Blob Storage, CosmosDB, Function APP’s, Azure Devops) , AWS(S3, Ec2, Lambda
    functions)
- ● Databases: Redis, SQLAlchemy, MySQL, PostgreSQL, MongoDB, ElasticSearch and Azure CosmosDB
"""
)


st.write('\n')
st.subheader("Certifications")
st.write("---")

st.image(certificate)



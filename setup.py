import setuptools
with open("readme.md", "r", encoding='utf-8') as f:
     long_description = f.read()
     
__version__="0.0.0"
REPO_NAME = "Text-Summarizer-NLP"
AUTHOR_USER_NAME = 'Dj-1000'
SRC_REPO = "text_summarizer"
AUTHOR_EMAIL = "work.djsharma1000@gmail.com"

setuptools.setup (
    name='SRC_REPO',
    version='__version__',
    description='A small python package for NLP app',
    long_description='long_description',
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    long_description_content='text/markdown',
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        f"https://github.com/{AUTHOR_USER_NAME}/{AUTHOR_EMAIL}/issues",
    },
    package_dir={"":"src"},
    packages= setuptools.find_packages(where='src')
)
from setuptools import setup, find_packages

setup(
    name='Simple-CLI-Assistant',
    description='A Python-based virtual assistant that can perform simple tasks, such as searching the web, accessing Wikipedia, opening desktop and system applications, and more.',
    author='CodingCraft',
    author_email='paliwalm4321@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'SpeechRecognition',
        'pyttsx3',
        'pywhatkit',
        'wikipedia'
    ],
    entry_points={
        'console_scripts': [
            'virtualassistant = virtualassistant..__main__:main'            
        ]
    },
)

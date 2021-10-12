from distutils.core import setup

setup(
    name="DoSer",
    py_modules=["DoSer"],
    entry_points={"console_scripts": ["DoSer=DoSer:main"]},
    version="0.2.3",
    description="Low bandwidth DoS tool. DoSer rewrite in Python.",
    author="D4RK~D3VIL",
    author_email="hac4allofficial@gmail.com",
    url="https://github.com/hac4allofficial",
    keywords=["dos", "http", "DoSer"],
    license="MIT",
)

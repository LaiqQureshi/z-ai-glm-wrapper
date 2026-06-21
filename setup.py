from setuptools import setup, find_packages

setup(
    name="z-ai-glm-wrapper",
    version="0.1.0",
    description="A simple, universal Python wrapper for Z AI GLM 5.2 API.",
    author="Laiq Ahmed Qureshi",
    author_email="your-email@example.com",
    url="https://github.com/LaiqQureshi/z-ai-glm-wrapper",
    py_modules=["glm_wrapper"],
    install_requires=[
        "requests>=2.25.0"
    ],
    python_requires=">=3.6",
)

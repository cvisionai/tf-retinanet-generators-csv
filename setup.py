from setuptools import setup

setup(
    name="tf-retinanet-generators-csv",
    version="1",
    description="CSV generator for tf-retinanet",
    long_description="",
    author="Jokke Ruokolainen",
    author_email="jokke.ruokolainen@vaisto.io",
    license="",
    packages=["tf_retinanet_generators.csv"],
    install_requires=["tf-retinanet"],
    zip_safe=False,
)

from setuptools import setup
import wget


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'  
wget.download(url, '/home/kaustubh/ApolloAI/ApolloAI_Ass_2/ieee_ml')

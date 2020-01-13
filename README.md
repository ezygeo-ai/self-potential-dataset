[![HitCount](http://hits.dwyl.com/ezygeo-ai/self-potential-dataset.svg)](http://hits.dwyl.com/ezygeo-ai/self-potential-dataset)
![GitHub contributors](https://img.shields.io/github/contributors/ezygeo-ai/self-potential-dataset)
![GitHub last commit](https://img.shields.io/github/last-commit/ezygeo-ai/self-potential-dataset)
![GitHub top language](https://img.shields.io/github/languages/top/ezygeo-ai/Self-Potential-Dataset)
![GitHub language count](https://img.shields.io/github/languages/count/ezygeo-ai/Self-Potential-Dataset)
![GitHub repo size](https://img.shields.io/github/repo-size/ezygeo-ai/Self-Potential-Dataset)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ezygeo-ai/Self-Potential-Dataset)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat&logo=linkedin&colorB=555)](https://www.linkedin.com/company/28696953)

# Self Potential Dataset
Self-Potential (SP) Datasets contain two datasets first one is synthetic dataset and second one is real dataset.

## Synthetic SP Dataset
We created the synthetic dataset for testing neural-network architecture used. This synthetic dataset is created with refering [H.M. El-Kaliouby and M.A. AL-Garni. J. Geophys. Eng. **6** (2009) 29-34](https://academic.oup.com/jge/article/6/1/29/5127394). Below, there are 6125 outputs of data ([SP_Dataset.pickle](https://github.com/ezygeo-ai/Self-Potential-Dataset/blob/master/SP_Dataset.pickle)) and you can get its code [here](https://github.com/ezygeo-ai/Self-Potential-Dataset/blob/master/make_dataset.py):

<p align="center"> 
  <img src="https://github.com/ezygeo-ai/Self-Potential-Dataset/blob/master/SP_datasets.png" width="50%" href="https://ezygeo.com/2019/10/28/self-potential-datasets/">
</p>

**Input Layer**: Location and SP data.
**Output Layer**: centre of the sheet, halfwidth of the sheet, polarization amplitude, zero distance from the origin, and angle of inclination of the sheet.

## Real SP Dataset
Google has [Google Dataset Search](https://toolbox.google.com/datasetsearch) for getting [Real SP Data](https://toolbox.google.com/datasetsearch/search?query=self-potential&docid=XeF5UDUFSocm8R%2F8AAAAAA%3D%3D), such us:
1. Self-Potential Survey, Roosevelt Hot Springs, Utah [link](https://catalog.data.gov/dataset/self-potential-survey-roosevelt-hot-springs-utah)
2. 14.86 km Profiles of the Electric and Self-potential Fields Measured in the Lower Guadalupe River Channel, Texas Interior Gulf Coastal Plain, September 2016 [link](https://data.doi.gov/dataset/14-86-km-profiles-of-the-electric-and-self-potential-fields-measured-in-the-lower-guadalup-2016)
3. Self-potential power spectral density from 2012 to 2017 [link](https://data.mendeley.com/datasets/97m454zgc6/1) 

## Annotation Tool for SP Data

## Testing Using TensorFlow and PyTorch
#### PyTorch

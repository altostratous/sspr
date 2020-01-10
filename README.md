# SSPR
Crawler and Page Rank on [www.semanticscholar.org](http://www.semanticscholar.org)

## Setup
```bash
pip install -r requirements.txt
```

## Usage
Sample usage of page rank algorithm and its highest ranked papers:
```bash
~$ python main.py
Enter alpha: 
~$ 0.85
(0.002116296638096687, 'https://www.semanticscholar.org/paper/Normalized-Cuts-and-Image-Segmentation-Shi-Malik/d5d02b093162096005834ee22def530de6c1f7eb')
(0.001619934007658015, 'https://www.semanticscholar.org/paper/Distinctive-Image-Features-from-Scale-Invariant-Dorst/bcae70dce393c1796d4f15c7b8bbf0ed6f468be1')
(0.0015853375246016586, 'https://www.semanticscholar.org/paper/MapReduce%3A-simplified-data-processing-on-large-Dean-Ghemawat/b6c771e3c407e183f49ebbccfbfcdb88be6a5231')
(0.0015664809258425126, 'https://www.semanticscholar.org/paper/Learning-Generative-Visual-Models-from-Few-Training-Li-Fergus/ed9db7b20e019cdb1c7db8b7921221ee2d9f36e2')
(0.0015412670779342348, 'https://www.semanticscholar.org/paper/High-performance-sorting-on-networks-of-Arpaci-Dusseau-Arpaci-Dusseau/f52e00b312adb320caeb734c09d71ceed0eff008')
(0.0015298686774790034, 'https://www.semanticscholar.org/paper/Snakes%3A-Active-contour-models-Kass-Witkin/9394a5d5adcb626128b6a42c8810b9505a3c6487')
(0.0014444189364042769, 'https://www.semanticscholar.org/paper/Object-class-recognition-by-unsupervised-learning-Fergus-Perona/62837ab473124ea43cb8d7c6a4b4ee0f6f14e8c5')
(0.001337631832869845, 'https://www.semanticscholar.org/paper/A-training-algorithm-for-optimal-margin-classifiers-Boser-Guyon/2599131a4bc2fa957338732a37c744cfe3e17b24')
(0.0013062848361726906, 'https://www.semanticscholar.org/paper/WRL-Research-Report-93%2F5%3A-An-Enhanced-Access-and-Wilton-Jouppi/822e74d90c010f7301b23500971034af6f0fbfee')
(0.0012834432401836427, 'https://www.semanticscholar.org/paper/Conditional-Random-Fields%3A-Probabilistic-Models-for-Lafferty-McCallum/f4ba954b0412773d047dc41231c733de0c1f4926')
```

## Run Crawler Test
```bash
python -m unittest tests
```

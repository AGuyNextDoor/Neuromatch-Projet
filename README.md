# Neuromatch-Projet

Project group from Neuromatch 2022 session

## Abstract 

> Roses are red, BCIs are cool, data is frail, and our model too. 

Brain-computer interface (BCI) is an emerging technology that can help patients with various disabilities, such as psychiatric disorders, paralysis, or motor coordination impairment. It is based on the principle that we can decode behaviour from brain activity, which can be measured by many different methods. One of them is electrocorticogram (ECoG) - an invasive method, but with high spatial and temporal precision. Here, we are testing whether patients’ actions could be predicted from the ECoG recordings. For this purpose, we use a 
dataset obtained from patients performing an n-back  task, which is a standard paradigm for investigating increasing load on working memory. Working memory overload  arises when working memory cannot retain relevant information. In an ECoG study, two patients undertook an n-back task, where they were presented with a sequence of images and asked to press the button when they recognised a previously presented image, in a set of experiments with increasing difficulty. We used different classifier algorithms on this dataset in order to identify the best model for decoding responses and predict whether the patients are still able to retain relevant information in memory and press the button when needed. We applied principal component analysis (PCA) to identify brain regions explaining the most variance in our data and to reduce the dimensionality of the channels. A logistic model on the raw data did not predict responses well (Recall: 0.001, bounded between 0 and 1), but fitting the model on the dataset with reduced dimensions after PCA increased our prediction score (Recall: 0.111). A Random Forest classifier improved it even further (Recall: 0.388). We plan to implement more models with enhanced data processing to further ameliorate our predictions and interpret distinguishable properties of the signals.

## Metadata Notes 

3 subjects
5 experiments
- Fixation 1
- exp 1
- exp 2
- exp 3
- Fixation 2


Variables for each block within each subject:
- `dat['V']`: continuous voltage data (time by channels)
- `dat['expinfo']`: experiment type for this block
- `dat['srate']`: sampling rate for voltage data, always 1000Hz
- `dat['t_on']`: time of stimulus onset in data samples
- `dat['t_off']`: time of stimulus offset, usually 600 samples after `t_on`
- `dat['stim_id`]: identity of house stimulus from 1 to 40. Stimulus 10 was the target in the 0-back task. 
- `dat['target']`: 0 or 1, indicates if this stimulus requires a response
- `dat['response']`: 0 or 1, indicates if the subject actually made a response
- `dat['rt']`: reaction time for trials with a response in voltage data samples (1000Hz).
- `dat['locs']`: 3D locations of the electrodes on the cortical surface

## Links 

### Papers
- EEG
  - [Estimating workload using EEG spectral power and ERPs in the n-back task](https://iopscience.iop.org/article/10.1088/1741-2560/9/4/045008) (given in the notebook)
  - [Electroencephalography Based Analysis of Working Memory Load and Affective Valence in an N-back Task with Emotional Stimuli](https://www.frontiersin.org/articles/10.3389/fnhum.2017.00616/full) (given in the notebook)
  - [Machine learning for neural decoding.](https://arxiv.org/abs/1708.00909)
  - [Within- and across-trial dynamics of human EEG reveal cooperative interplay between reinforcement learning and working memory](https://www.ocf.berkeley.edu/~acollins/pdfs/papers/Collins_Frank_PNAS_EEG.pdf)
- ECoG
  - [Frequency-specific electrocorticographic correlates of working memory delay period fMRI activity](https://pubmed.ncbi.nlm.nih.gov/21356314/)
- Model Comparison
  - [Neurocognitive Architecture of WM](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4605545/)
  - [Factorial comparison of working memory models](https://www.researchgate.net/publication/260064113_Factorial_Comparison_of_Working_Memory_Models)
  
### Raw Data

- https://exhibits.stanford.edu/data/catalog/zk881ps0522

### Code

- [Decoding Toolbox (MNE Package)](https://mne.tools/stable/auto_examples/decoding/decoding_csp_eeg.html#ex-decoding-csp-eeg) (An example, maybe not to use in the project?)

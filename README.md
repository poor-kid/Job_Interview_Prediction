# Project Title:
Analysis and Prediction of Job Interview Performance Using Lexical and Prosodic Features.

**Our framework will:-**
* automatically quantify both verbal and non-verbal behaviours in the context of job interviews
* the relative inﬂuences of diﬀerent low level features on the interview performance.
* learns regression models to predict interview ratings and the likelihood of hiring using automatically extracted features.
* predicts several other high-level personality traits such as engagement, friendliness, and excitement.

`The objective of the project is to extract the various lexical and Prosodic features responsible for diﬀerent personality traits and predict scores for various personality traits given an Interview.The proposed framework is trained by analyzing the audio recordings of 19 internship-seeking undergraduates in our institute (IIIT Allahabad). These Interviews were conducted b PhD Scholars from IIITA`

# Dependencies:
* Numpy
* Pysptk
* Pandas
* Openpyxl
* NLTK
* Matplotlib
* sklearn
* Python3

Use [pip](https://pypi.org/project/pip/) to install any missing dependencies.



# Overview:
**Steps followed for this project:**
## Lexical features:
The Lexical features include:


* First we extract 21 features in dataset and some of them are using Linguistic Inquiry Word Count(LIWC)
* We calculate Mutual Information of all features for each personality traits. `Mutual information (MI) between two random variables is a non-negative value, which measures the dependency between the variables. It is equal to zero if and only if two random variables are independent, and higher values mean higher dependency.`
* Top seven feature is selected based on Mutual Information for applying Support vector regression(SVR). Here we also do feature scaling.


## Prosody features

```sh
prosody.py
```

Compute prosody features from continuous speech based on duration, fundamental frequency and energy.


The static feature vector is formed with 13 features and include

1. Average fundamental frequency in voiced segments
2. Standard deviation of fundamental frequency in Hz
3. Variablity of fundamental frequency in semitones
4. Maximum of the fundamental frequency in Hz
5. Average energy in dB
6. Standard deviation of energy in dB
7. Maximum energy
8. Voiced rate (number of voiced segments per second)
9. Average duration of voiced segments
10. Standard deviation of duration of voiced segments
11. Pause rate (number of pauses per second)
12. Average duration of pauses
13. Standard deviation of duration of pauses
 <br /> NEW MEASURES <br />
14. Average tilt of fundamental frequency
15. Tilt regularity of fundamental frequency
16. Mean square error of the reconstructed F0 with a  1-degree polynomial
17. (Silence duration)/(Voiced+Unvoiced durations)
18. (Voiced duration)/(Unvoiced durations)
19. (Unvoiced duration)/(Voiced+Unvoiced durations)
20. (Voiced duration)/(Voiced+Unvoiced durations)
21. (Voiced duration)/(Silence durations)
22. (Unvoiced duration)/(Silence durations)
23. Unvoiced duration Regularity
24. Unvoiced energy Regularity
25. Voiced duration Regularity
26. Voiced energy Regularity
27. Pause duration Regularity
28. Maximum duration of voiced segments
29. Maximum duration of unvoiced segments
30. Minimum duration of voiced segments
31. Minimum duration of unvoiced segments
32. rate (# of voiced segments) / (# of unvoiced segments)
33. Average tilt of energy contour
34. Regression coefficient between the energy contour and a linear regression
35. Mean square error of the reconstructed energy contour with a  1-degree polynomial
34. Regression coefficient between the F0 contour and a linear regression
37. Average Delta energy within consecutive voiced segments
38. Standard deviation of Delta energy within consecutive voiced segments


prosody features are based on
Najim Dehak, "Modeling Prosodic Features With Joint Factor Analysis for Speaker Verification", 2007

### Notes:

1. The fundamental frequency is computed using Praat. To use the RAPT algorithm change the "pitch method" variable in the function phonation_vowel.
2.  We also apply SVR to the dataset. And then apply K-Fold cross validation to all algorithm. `K-Folds cross-validator provides train/test indices to split data in train/test sets. Split dataset into k consecutive folds (without shuffling by default). Each fold is then used once as a validation while the k - 1 remaining folds form the training set.`
3. We finally calculate accuracy of each model and comapare them. 

### Runing
Script is called as follows
```sh
python prosody.py <file_or_folder_audio> <file_features.txt> [dynamic_or_static (default static)] [plots (true or false) (default false)] 
```

### Examples:
```sh
python prosody.py "./P1.wav" "featuresDDKst.txt" "static" "true"
```

#### Results:


The comparison of different audio features used for prosodic features extraction by different participants
![Image](https://github.com/poor-kid/Job_Interview_Prediction/blob/master/Output/Figure_1.png?Raw=true)



lexical analysis
![Image](https://github.com/poor-kid/Job_Interview_Prediction/blob/master/Output/Screenshot%20from%202018-11-19%2017-09-25.png?Raw=true)

Prosody analysis from continuous speech static
![Image](https://github.com/poor-kid/Job_Interview_Prediction/blob/master/Output/freq_amp.png?Raw=true)

The correlation between different traits predicted and the possibility for an individual to be hired
![Image](https://github.com/poor-kid/Job_Interview_Prediction/blob/master/Output/correations.png?Raw=true)

#### References

[[1]](http://ieeexplore.ieee.org/abstract/document/4291597/). N., Dehak, P. Dumouchel, and P. Kenny. "Modeling prosodic features with joint factor analysis for speaker verification." IEEE Transactions on Audio, Speech, and Language Processing 15.7 (2007): 2095-2103.

[[2]](http://www.sciencedirect.com/science/article/pii/S105120041730146X). J. R. Orozco-Arroyave, J. C. Vásquez-Correa et al. "NeuroSpeech: An open-source software for Parkinson's speech analysis." Digital Signal Processing (2017).

[[3]](https://ieeexplore.ieee.org/document/7579163/). Iftekhar Naim, Student Member, IEEE, M. Iftekhar Tanveer, Student Member, IEEE, Daniel Gildea "Automated Analysis and Prediction of Job Interview Performance" (2018)

[[4]](https://journals.sagepub.com/doi/abs/10.1177/0261927X09351676).Yla R. Tausczik and James W. Pennebaker "The Psychological Meaning of Words: LIWC and Computerized Text Analysis Methods"



##### `You can contact me at: dileepmokana@gmail.com`

# load libraies

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.cm as cm
from matplotlib.ticker import LinearLocator
import sklearn
from sklearn import metrics
from sklearn.svm import SVC, LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_classification
from sklearn.linear_model import RidgeCV
from sklearn.multiclass import OneVsRestClassifier
from sklearn.tree import (DecisionTreeClassifier, export_graphviz, export_text)
from sklearn.inspection import (DecisionBoundaryDisplay, permutation_importance)
from sklearn.feature_selection import (SelectFromModel, r_regression)
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_selector as selector
from sklearn.impute import SimpleImputer
from sklearn.utils import check_consistent_length
from sklearn.model_selection import (train_test_split, KFold, GridSearchCV, cross_val_score, StratifiedKFold)
from sklearn.preprocessing import (LabelEncoder, PolynomialFeatures, label_binarize, LabelBinarizer, 
                                   StandardScaler, OneHotEncoder, MinMaxScaler, RobustScaler, MaxAbsScaler)
from sklearn.metrics import (precision_recall_curve, roc_curve, auc, roc_auc_score, RocCurveDisplay, 
                             make_scorer, accuracy_score, precision_score, recall_score, f1_score, 
                             confusion_matrix, classification_report, matthews_corrcoef,
                             mean_squared_error, PrecisionRecallDisplay)
from sklearn.ensemble import (RandomForestClassifier,HistGradientBoostingClassifier,
                              GradientBoostingRegressor)

from tqdm import tqdm
from IPython.display import display
# import tensorflow as tf
# from tensorflow import keras
import os
import tempfile
from scipy import stats
from scipy import interpolate
from scipy.interpolate import splev, splrep
import statistics
import collections
import time
import seaborn as sns
import midas as md # (un comment for imputation)
import smpl_sz_adeq as smpl_adeq # (use for sample size adequacy analysis)
import re
from tableone import TableOne, load_dataset # generating tables

# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()

import warnings
warnings.filterwarnings('ignore')

# !jupyter --version
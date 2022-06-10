

Welcome! The goal of this first week is to give an introduction to some useful skills and concepts in data science, and leave you with some resources to learn more. Some things might be to totally new, while others might be familiar to you already.

## Schedule

Tuesday 10-12 and 1-3, JCC 502

Wednesday 10-12 and 1-2:30 JCC 502

Thursday 10-12 and 1-2:30 JCC 502

Friday 9:30-11 and 1:30-3 JCC 502

## Pre-workshop tasks

It will be helpful if you can complete tasks A and B below before Tuesday. But if you can't or you run into trouble, don't worry - we can also work through these steps together.

### Preworkshop task A: Git setup

1. If you have never used the terminal / command prompt before, go through this [introductory tutorial](https://tutorial.djangogirls.org/en/intro_to_command_line/). The commands you will need to know for this course are `ls` (for Mac and Linux users), `dir` (for Windows users), and `cd` (for everyone). (15 min)
2. Install Git, following these [instructions](https://karink520.github.io/git-and-github-intro/install_git.html). (10 min)
3. Create an account on [GitHub](https://github.com). (5 min)

### Preworkshop task B: Installing miniconda and a text editor:

Follow **steps 1, 2 and 7** (you can skip steps 3-6 for now- we'll come back to them) in these [setup instructions](https://karinknudson.com/python_setup.pdf). Again, if you have trouble or the instructions don't make sense, don't worry at all. We'll troubleshoot together in class. Note: if you already have a) miniconda or Anaconda and b) a text editor that you like (Visual Studio code, Atom, and Sublime are all popular text editors), you're all set.

### Preworkshop task C (optional): Python basics:

If you've never used Python before, check out the [Python basics notebook](https://colab.research.google.com/drive/1-xnnJtSNYMwsizsR0q2Wc8Ys_jNt6srR). It is a Google collab notebook, so you will be able to run the code and see the output. Your task here is just to explore, see what you notice, and think about what questions you have. You can make changes to the code, but you won't be able to save them unless you make your own copy of the notebook (with the "Copy to Drive" button.

## Outline of the week

- Day 1 (Tuesday) - Python setup, cleaning and manipulating dataframes, Git and Github
- Day 2 (Wednesday) - Data visualization
- Day 3 (Thursday) - Machine learning
- Day 4 (Friday) - Machine learning, writing robust code with tests

## Materials

### Intro and Data Wrangling

Notebooks:

- [Introduction to Python Basics](https://colab.research.google.com/drive/1-xnnJtSNYMwsizsR0q2Wc8Ys_jNt6srR)
- [Introduction to Pandas DataFrames](https://colab.research.google.com/drive/1LoMojpmzeu8dxX6Uc6Wt9ky-MYy0ttq0)
- [Data Preparation with Python and Pandas](https://colab.research.google.com/drive/1YjYPxfbRPBlLT8w5wHpsDY2667EYeU4U)

Resources:

- [Pandas cheatsheet 1](https://drive.google.com/file/d/1UHK8wtWbADvHKXFC937IS6MTnlSZC_zB/view)
- [Pandas cheatsheet 2](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Pandas tutorial from W3Schools](https://www.w3schools.com/python/pandas/default.asp)
- [Command Line Interface Intro](https://www.w3schools.com/whatis/whatis_cli.asp)
- [Introductory Python Tutorial from W3Schools](https://www.w3schools.com/python/python_variables.asp)

Additional data wrangling activity if you have significant existing pandas experience:
 - Try SQL with this [tutorial](https://www.w3schools.com/sql/)

### Git and GitHub

- [Git and GitHub tutorial](https://karink520.github.io/git-and-github-intro/git_workshop.html)
- [Git and GitHub slides](https://karink520.github.io/git-and-github-intro/git_workshop_slides.pdf)

Resources:
- [Git workflow concise explainer](https://karinknudson.com/git_workflow.html)
- Additional resources are at the bottom of the [Git and GitHub tutorial](https://karink520.github.io/git-and-github-intro/git_workshop.html).

Additional Git and GitHub activities if you have significant existing experience:
- [A browser game to practice branching](https://learngitbranching.js.org/)
- Try making yourself an academic website using GitHub pages

### HW due Wednesday:
- Practice with this [Exercise: Exploratory Data Analysis with Python](https://colab.research.google.com/drive/1CAP_k6HF88O-19wngS_5x2KN7Sfiwypo). Here are [sample solutions](https://colab.research.google.com/drive/1duLnyhAwB-THIKNzXDNEsGhHILtZ2KbP#scrollTo=2WUdwbKcvTpG)
- Clone and follow instructions on the following [repo](https://github.com/merterden98/intros)

### Data visualization

Notebooks:
- [Classic charts with Matplotlib](https://colab.research.google.com/drive/1BymAOKBf1arAYSLvpytrT0GetZK0zyLu)

Resources:
- [Fundamentals of Data Visualization, by Claus Wilke](https://clauswilke.com/dataviz/) An awesome book on the principles of making your data visualizations good and effective, with tons of examples. Chapter 5 is a "Directory of Data Visualizations" that's a nice resource for when you need ideas for the kinds of visualizations you can make.
- [Seaborn example gallery](https://seaborn.pydata.org/examples/index.html)
- [Streamlit Example](streamlit_example.py) Code for the streamlit demo from class 
- [Streamlit.io](https://streamlit.io/) A tool for making interactive dashboards

HW/additional practice:
- [Exercise: Intro to Plotting with Python](https://colab.research.google.com/drive/14WX9amWra-ChZj_PO6J37zrFc_sDRQ0J?usp=sharing)
- If you like, try making a basic Streamlit app. For significantly more information than we had in our (very!) brief demo, check out the [documentation](https://docs.streamlit.io/library/get-started/main-concepts)

### Machine Learning Introduction

Notebooks:
- [Intro to Classification](https://colab.research.google.com/drive/1ZV0PdqZYhwZTX3B2GI3U38phlavMxJne#scrollTo=WE9k86L-r6tv)
- [Intro to Classification, Regression Clustering with SciKitLearn](https://colab.research.google.com/drive/1DgGR6lTZ_V3gfAQZf29b1K1k2WJXQpge)
- [Exercise: Intro to Classification, Regression, Clustering with SciKitLearn](https://colab.research.google.com/drive/18yqgvYmSoe6RKHjf_B4Sgb-J0CL4UwUX?usp=sharing)
- [Regression practice activity](https://colab.research.google.com/drive/1coaQICnO6ghV88HGZ_-_-M7GZJBzJCcv) Activity for Friday morning

Resources:
- [Intro slides](https://docs.google.com/presentation/d/1p2O5dcB8nK-H2BQN-0Xjn5TWTqxacOq64HPfUsG8MlY/edit#slide=id.g11e0ab7bc9c_0_86) from the start of today's class
- [An Introduction to Statistical Learning](https://www.statlearning.com/) A book that gives an excellent introduction to machine learning. Note: A related book that goes a bit more in depth in some places and assumes more math prerequisite is *Elements of Statistical Learning*. Christopher Bishop's *Pattern Matching and Machine Learning* is another one of my all-time favorite machine learning books.)
- [Scikit Learn tutorial](https://inria.github.io/scikit-learn-mooc/index.html) I haven't looked through all of this yet, but it looks like a good introductory resource.
- For an introduction to neural networks and deep learning, I think Andrew Ng's courses on Coursera are nice (the audit option is free)
- [A video introduction to Principle Component Analysis (PCA)](https://www.youtube.com/watch?v=FgakZw6K1QQ)
- [Friday afternoon tSNE/UMAP exercise](https://github.com/merterden98/intros/blob/main/LDE.md)

HW for Friday:
- Glance at some of the resources above. What are some areas of machine learning you'd like to learn more about this summer? What are some resources you could use to do so?
- In class we looked at several different classification approaches, but only one approach each for clustering and regression. Identify another regression approach you'd like to try out (you can look around in the resources above if you need ideas, or choose something from the scikitlearn flow chart that's in the slides), and run it on either the penguins dataset or the dataset of your choice. Do the same for another clustering method.

### Tufts cluster access

To request access to the Tufts cluster, fill out the form [here](https://access.tufts.edu/research-cluster-account).

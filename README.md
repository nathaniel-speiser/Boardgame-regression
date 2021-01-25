# Boardgame linear regression analysis


## Description

The goal of this project is to find what factors contribute to a board game's success using linear regression techniques. This success is measured by two metrics: the number of plays the game has recieved and its average rating (out of 10), both from [BoardGameGeek](https://boardgamegeek.com/). The featuers used in the linear regression model include things that a board game maker could control, such as the number of players, the game's complexity, and categorical data (whether a game is a fantasy game, card game, etc.). Scikit-learn's PolynomialFeature was also used to generate interaction features. The final model used Lasso regression in order to cut down the total number of features used in the model.

The final model achieved an R^2 of 0.49 and 0.27 on the rating and number of plays models, respectively. Interestingly, the most impactful features differed greatly between the models. The most predictive features of the rating model were mostly continuous variables, those of the number of plays model were mostly categorical (see below.)

![graph1](https://github.com/nathaniel-speiser/Boardgame-regression/blob/main/pics/rating%20coefficients.png)
![graph2](https://github.com/nathaniel-speiser/Boardgame-regression/blob/main/pics/logplays%20coefficients.png)

## Data

All data was scraped from [Boardgamegeek.com](https://boardgamegeek.com/). Most of the data was scraped directly from the board games' pages, but marketplace data was found using Boardgamegeeks [xmlapi2](https://boardgamegeek.com/wiki/page/BGG_XML_API2#).

## Tools

* BeautifulSoup
* numpy
* pandas
* scikit-learn
* matplotlib
* seaborn


## Impacts

This project could be use as a reference for board game makers seeking to maximize their upcoming board game's popularity, or to predict the popularity of a board game during the early stages of development (see the last page of the presentation PDF for an example). It should be noted that this project is limited in scope to the popularity of board games among presumed enthusiasts, rather than the general public

## Future directions

Given the models' performance, there is likely still room for improvement in model and feature selection. Better marketplace data would also be highly desireable, as price data for many games is most likely inaccurate given it came from a marketplace, not direcly from the publisher or supplier. Finally I would like to make the model more interactive so it is easier to make predictions on fictional games.

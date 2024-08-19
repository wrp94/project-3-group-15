# project-3-group-15

Project 3 - Interactive Visualizations

<https://wrp94.pythonanywhere.com/>

## Background

In this project, we used a [Kaggle dataset](https://www.kaggle.com/datasets/sudarshan24byte/online-food-dataset) to view and analyze demographic trends in online food orders. To do this, we used a [`Flask`](https://flask.palletsprojects.com/en/3.0.x/) backend to handle our API requests and query the database we created. Then, the data was visualized using [`Plotly`](https://plotly.com/javascript/) and [`Leaflet`](https://leafletjs.com/) in `JavaScript` to generate the frontend.

## Data

The data was found as a CSV and needed to be converted to a SQL database. To do this, the table was read into a Pandas data frame and then loaded into a SQLite file. The only cleaning that was required was to change the column titles and drop irrelevant columns like "Order Feedback".

## App

Our app contains five webpages and combines Python with JavaScript to create a seamless data visualization experience. Two of these pages make calls to our Flask API to retrieve data from our database. This happens in dynamically so the user can filter the data to dive deeper into their analysis. The whole site uses Bootstrap/Bootswatch to create and theme the pages.

### How to use

Simply navigate to [our website](https://wrp94.pythonanywhere.com/) and begin exploring. The [dashboard](https://wrp94.pythonanywhere.com/dashboard) has two options for filtering the data: gender and marital status. Use the graphs to search for trends in education, employment, and age. Our [map](https://wrp94.pythonanywhere.com/map) shows the order location and education levels for any given occupation in the dataset.

## Conclusions

The only trends we could find in the limited time we worked on this project were that single people are more likely to be students and have a slightly lower education level than their married counterparts. This could be due to married people being four years older on average.

## Works Cited

###### Dataset: <https://www.kaggle.com/datasets/sudarshan24byte/online-food-dataset>

###### Coolors (for theming): <https://coolors.co/05668d-427aa1-ebf2fa-679436-a5be00>

###### Inspiration: <https://www.kaggle.com/datasets/rajatkumar30/food-delivery-time>

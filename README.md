# BirdsDeploy

Included in this respository is the code needed to build and compile the Docker image for my Feather Classification application. 

You can find the five sample pictures in the 'Static' and then 'Sample' folders. 

This project relies on a ResNet-50 based model. The model was trained and tested in Python, using Tensorflow. Interpreting model results can be tricky at best. We used Flask to stand up this service as a web application, to ensure that we deliver a UI that is accessible and quickly communicates key results without overly-involving the user in the minutiae of deep learning. We used Materialize as a front-end for the project, given its ability to extend seamlessly across mobile devices.

Several packages and databases were absolutely essential in standing up this application. The Integrated Taxonomic Information System (ITIS) provided a fantastic source of species information and was the primary source of linking scientific names with common names. Finally, the Wikipedia library helped to provide links to further information for a given species.



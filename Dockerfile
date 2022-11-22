# syntax=docker/dockerfile:1

FROM tensorflow/tensorflow:2.11.0

WORKDIR /my-tf-image


# copy the requirements file into the image
COPY requirements.txt requirements.txt

#RUN pip install --upgrade pip
#RUN apk update
#RUN apk add make automake gcc g++ subversion python3-dev

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

#RUN python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.11.0-cp39-cp39-#manylinux_2_17_x86_64.manylinux2014_x86_64.whl

# copy every content from the local file to the image
COPY . .

#ENV FLASK_DEBUG=1

# configure the container to run in an executed manner
#ENTRYPOINT [ "python" ]

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
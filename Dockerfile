FROM centos:latest

RUN yum install python3 -y

RUN pip3 install Flask

RUN pip3 install scikit-learn

RUN pip3 install pandas

RUN pip3 install numpy

WORKDIR /app

COPY .

EXPOSE 4000

ENTRYPOINT  ["python"]

CMD["app.py']

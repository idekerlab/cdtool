# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

RUN apt-get --allow-releaseinfo-change update
RUN apt-get install -y build-essential 

RUN mkdir /tmp/cdtool
COPY ./ /tmp/cdtool/
RUN pip install /tmp/cdtool

RUN rm -rf /tmp/cdtool

ENTRYPOINT ["/opt/conda/bin/cdtoolcmd.py"]

CMD ["--help"]

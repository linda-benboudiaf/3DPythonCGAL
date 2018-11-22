FROM ubuntu:18.04
MAINTAINER Linda Benboudiaf
ENV DATADIR /tmp/cgal-data
RUN set -x; \
    apt-get update \
    && apt-get install -y --no-install-recommends \
        g++ \
        python3 \
        python3-pip \
        git \
        build-essential cmake autoconf automake libtool bison libpcre3-dev
RUN  apt-get update && apt-get install -y swig


#https://cgal.geometryfactory.com/CGAL/doc/master/Manual/installation.html#secprerequisites
#CGAL on Linux  debian/Ubuntu, use apt-get in the following way:
RUN apt-get install -y libcgal-dev
#To get the demos use:
RUN apt-get install -y libcgal-demo

RUN apt-get install -y ca-certificates \ 
    && git clone https://github.com/CGAL/cgal-swig-bindings.git \
    && cd cgal-swig-bindings \
    && mkdir -p build/CGAL_release && cd build/CGAL_release \
RUN cmake -DCGAL_DIR=/usr/lib/CGAL -DBUILD_PYTHON=ON \	
	-DPYTHON_OUTDIR_PREFIX=../../examples/python \
	make -j $(grep --count ^processor /proc/cpuinfo)

#CGAL_DIR=/opt/local/share/CGAL/cmake BUILD_JAVA=FALSE 
#BUILD_PYTHON=TRUE 
#PYTHON_OUTDIR_PREFIX=/Users/USERNAME/cgal-bindings/build-python

RUN export PYTHONPATH=$PYTHONPATH:/cgal-swig-bindings/CGAL
#PYTHON_OUTDIR_PREFIX
#PYTHON_OUTDIR_PREFIX\CGAL
#PYTHON_OUTDIR_PREFIX\CGAL\Release


# clean sys
RUN apt-get remove -y autoconf automake libtool bison git libpcre3-dev python3-pip \
&&  rm -rf /var/lib/apt/lists/*

RUN mkdir -p $DATADIR/data && mkdir -p $DATADIR/output

VOLUME ["$DATADIR","$DATADIR/data", "$DATADIR/output"]

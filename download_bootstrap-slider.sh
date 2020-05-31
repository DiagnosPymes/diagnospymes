#!/bin/sh

CURR_DIR=`pwd`
STATIC_DIR=$CURR_DIR/mm_evaluation/static/mm_evaluation
wget --directory-prefix=$STATIC_DIR/js/ https://raw.githubusercontent.com/seiyria/bootstrap-slider/master/dist/bootstrap-slider.js

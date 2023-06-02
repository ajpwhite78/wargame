import streamlit as st
import pandas as pd
import numpy as np
from numpy import nanpercentile
from PIL import Image, ImageDraw, ImageFont, ImageOps
from matplotlib import font_manager
import urllib
import pathlib
import base64
import time
import os
import io
import dataframe_image as dfi
from tempfile import mkstemp
import zipfile
from scipy.stats import norm
import scipy.linalg as sclinalg
from scipy.interpolate import UnivariateSpline

timestr = time.strftime("%Y%m%d-%H%M%S")

marker_spinner_css = """
<style>
    #spinner-container-marker {
        display: flex;
        align-items: center;
        justify-content: center;
        position: fixed;
        top: 0%;
        left: 0%;
        transform: translate(54%, 0%);
        width: 100%;
        height: 100%;
        z-index: 9999;
    }

    .marker0 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 0 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 0 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 0 / 50))), calc(5em * sin(2 * 3.14159 * 0 / 50)));        
    }
    
    .marker1 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 1 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 1 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 1 / 50))), calc(5em * sin(2 * 3.14159 * 1 / 50)));
    }
    
    .marker2 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 2 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 2 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 2 / 50))), calc(5em * sin(2 * 3.14159 * 2 / 50)));
    }
    
    .marker3 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 3 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 3 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 3 / 50))), calc(5em * sin(2 * 3.14159 * 3 / 50)));
    }
    
    .marker4 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 4 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 4 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 4 / 50))), calc(5em * sin(2 * 3.14159 * 4 / 50)));
    }
    
    .marker5 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 5 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 5 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 5 / 50))), calc(5em * sin(2 * 3.14159 * 5 / 50)));
    }
    
    .marker6 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 6 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 6 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 6 / 50))), calc(5em * sin(2 * 3.14159 * 6 / 50)));
    }
    
    .marker7 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 7 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 7 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 7 / 50))), calc(5em * sin(2 * 3.14159 * 7 / 50)));
    }
    
    .marker8 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 8 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 8 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 8 / 50))), calc(5em * sin(2 * 3.14159 * 8 / 50)));
    }
    
    .marker9 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 9 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 9 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 9 / 50))), calc(5em * sin(2 * 3.14159 * 9 / 50)));
    }
    
    .marker10 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 10 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 10 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 10 / 50))), calc(5em * sin(2 * 3.14159 * 10 / 50)));
    }
    
    .marker11 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 11 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 11 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 11 / 50))), calc(5em * sin(2 * 3.14159 * 11 / 50)));
    }
    
    .marker12 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 12 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 12 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 12 / 50))), calc(5em * sin(2 * 3.14159 * 12 / 50)));
    }
    
    .marker13 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 13 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 13 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 13 / 50))), calc(5em * sin(2 * 3.14159 * 13 / 50)));
    }
    
    .marker14 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 14 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 14 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 14 / 50))), calc(5em * sin(2 * 3.14159 * 14 / 50)));
    }
    
    .marker15 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 15 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 15 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 15 / 50))), calc(5em * sin(2 * 3.14159 * 15 / 50)));
    }
    
    .marker16 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 16 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 16 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 16 / 50))), calc(5em * sin(2 * 3.14159 * 16 / 50)));
    }
    
    .marker17 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 17 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 17 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 17 / 50))), calc(5em * sin(2 * 3.14159 * 17 / 50)));
    }
    
    .marker18 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 18 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 18 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 18 / 50))), calc(5em * sin(2 * 3.14159 * 18 / 50)));
    }
    
    .marker19 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 19 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 19 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 19 / 50))), calc(5em * sin(2 * 3.14159 * 19 / 50)));
    }
    
    .marker20 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 20 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 20 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 20 / 50))), calc(5em * sin(2 * 3.14159 * 20 / 50)));
    }
    
    .marker21 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 21 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 21 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 21 / 50))), calc(5em * sin(2 * 3.14159 * 21 / 50)));
    }
    
    .marker22 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 22 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 22 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 22 / 50))), calc(5em * sin(2 * 3.14159 * 22 / 50)));
    }
    
    .marker23 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 23 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 23 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 23 / 50))), calc(5em * sin(2 * 3.14159 * 23 / 50)));
    }
    
    .marker24 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 24 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 24 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 24 / 50))), calc(5em * sin(2 * 3.14159 * 24 / 50)));
    }
    
    .marker25 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 25 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 25 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 25 / 50))), calc(5em * sin(2 * 3.14159 * 25 / 50)));
    }
    
    .marker26 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 26 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 26 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 26 / 50))), calc(5em * sin(2 * 3.14159 * 26 / 50)));
    }
    
    .marker27 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 27 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 27 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 27 / 50))), calc(5em * sin(2 * 3.14159 * 27 / 50)));
    }
    
    .marker28 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 28 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 28 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 28 / 50))), calc(5em * sin(2 * 3.14159 * 28 / 50)));
    }
    
    .marker29 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 29 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 29 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 29 / 50))), calc(5em * sin(2 * 3.14159 * 29 / 50)));
    }
    
    .marker30 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 30 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 30 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 30 / 50))), calc(5em * sin(2 * 3.14159 * 30 / 50)));
    }
    
    .marker31 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 31 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 31 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 31 / 50))), calc(5em * sin(2 * 3.14159 * 31 / 50)));
    }
    
    .marker32 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 32 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 32 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 32 / 50))), calc(5em * sin(2 * 3.14159 * 32 / 50)));
    }
    
    .marker33 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 33 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 33 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 33 / 50))), calc(5em * sin(2 * 3.14159 * 33 / 50)));
    }
    
    .marker34 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 34 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 34 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 34 / 50))), calc(5em * sin(2 * 3.14159 * 34 / 50)));
    }
    
    .marker35 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 35 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 35 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 35 / 50))), calc(5em * sin(2 * 3.14159 * 35 / 50)));
    }
    
    .marker36 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 36 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 36 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 36 / 50))), calc(5em * sin(2 * 3.14159 * 36 / 50)));
    }
    
    .marker37 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 37 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 37 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 37 / 50))), calc(5em * sin(2 * 3.14159 * 37 / 50)));
    }
    
    .marker38 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 38 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 38 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 38 / 50))), calc(5em * sin(2 * 3.14159 * 38 / 50)));
    }
    
    .marker39 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 39 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 39 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 39 / 50))), calc(5em * sin(2 * 3.14159 * 39 / 50)));
    }
    
    .marker40 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 40 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 40 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 40 / 50))), calc(5em * sin(2 * 3.14159 * 40 / 50)));
    }
    
    .marker41 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 41 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 41 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 41 / 50))), calc(5em * sin(2 * 3.14159 * 41 / 50)));
    }
    
    .marker42 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 42 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 42 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 42 / 50))), calc(5em * sin(2 * 3.14159 * 42 / 50)));
    }
    
    .marker43 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 43 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 43 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 43 / 50))), calc(5em * sin(2 * 3.14159 * 43 / 50)));
    }
    
    .marker44 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 44 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 44 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 44 / 50))), calc(5em * sin(2 * 3.14159 * 44 / 50)));
    }
    
    .marker45 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 45 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 45 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 45 / 50))), calc(5em * sin(2 * 3.14159 * 45 / 50)));
    }
    
    .marker46 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 46 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 46 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 46 / 50))), calc(5em * sin(2 * 3.14159 * 46 / 50)));
    }
    
    .marker47 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 47 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 47 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 47 / 50))), calc(5em * sin(2 * 3.14159 * 47 / 50)));
    }
    
    .marker48 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 48 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 48 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 48 / 50))), calc(5em * sin(2 * 3.14159 * 48 / 50)));
    }
    
    .marker49 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 49 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 49 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 49 / 50))), calc(5em * sin(2 * 3.14159 * 49 / 50)));
    }

    @keyframes animateBlink {
    0% {
        background: #6f72de;
    }
    25% {
        background: rgba(0, 0, 0, 0);
    }   
}
@media (max-width: 600px) {
    #spinner-container-marker {
        transform: translate(57.4%, 0%);
    }
    .marker0 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 0 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 0 / 50))), calc(10em * sin(2 * 3.14159 * 0 / 50)));
    }
    .marker1 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 1 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 1 / 50))), calc(10em * sin(2 * 3.14159 * 1 / 50)));
    }
    .marker2 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 2 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 2 / 50))), calc(10em * sin(2 * 3.14159 * 2 / 50)));
    }
    .marker3 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 3 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 3 / 50))), calc(10em * sin(2 * 3.14159 * 3 / 50)));
    }
    .marker4 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 4 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 4 / 50))), calc(10em * sin(2 * 3.14159 * 4 / 50)));
    }
    .marker5 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 5 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 5 / 50))), calc(10em * sin(2 * 3.14159 * 5 / 50)));
    }
    .marker6 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 6 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 6 / 50))), calc(10em * sin(2 * 3.14159 * 6 / 50)));
    }
    .marker7 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 7 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 7 / 50))), calc(10em * sin(2 * 3.14159 * 7 / 50)));
    }
    .marker8 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 8 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 8 / 50))), calc(10em * sin(2 * 3.14159 * 8 / 50)));
    }
    .marker9 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 9 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 9 / 50))), calc(10em * sin(2 * 3.14159 * 9 / 50)));
    }
    .marker10 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 10 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 10 / 50))), calc(10em * sin(2 * 3.14159 * 10 / 50)));
    }
    .marker11 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 11 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 11 / 50))), calc(10em * sin(2 * 3.14159 * 11 / 50)));
    }
    .marker12 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 12 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 12 / 50))), calc(10em * sin(2 * 3.14159 * 12 / 50)));
    }
    .marker13 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 13 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 13 / 50))), calc(10em * sin(2 * 3.14159 * 13 / 50)));
    }
    .marker14 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 14 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 14 / 50))), calc(10em * sin(2 * 3.14159 * 14 / 50)));
    }
    .marker15 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 15 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 15 / 50))), calc(10em * sin(2 * 3.14159 * 15 / 50)));
    }
    .marker16 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 16 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 16 / 50))), calc(10em * sin(2 * 3.14159 * 16 / 50)));
    }
    .marker17 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 17 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 17 / 50))), calc(10em * sin(2 * 3.14159 * 17 / 50)));
    }
    .marker18 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 18 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 18 / 50))), calc(10em * sin(2 * 3.14159 * 18 / 50)));
    }
    .marker19 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 19 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 19 / 50))), calc(10em * sin(2 * 3.14159 * 19 / 50)));
    }
    .marker20 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 20 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 20 / 50))), calc(10em * sin(2 * 3.14159 * 20 / 50)));
    }    
    .marker21 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 21 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 21 / 50))), calc(10em * sin(2 * 3.14159 * 21 / 50)));
    }
    .marker22 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 22 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 22 / 50))), calc(10em * sin(2 * 3.14159 * 22 / 50)));
    }
    .marker23 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 23 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 23 / 50))), calc(10em * sin(2 * 3.14159 * 23 / 50)));
    }
    .marker24 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 24 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 24 / 50))), calc(10em * sin(2 * 3.14159 * 24 / 50)));
    }
    .marker25 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 25 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 25 / 50))), calc(10em * sin(2 * 3.14159 * 25 / 50)));
    }
    .marker26 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 26 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 26 / 50))), calc(10em * sin(2 * 3.14159 * 26 / 50)));
    }
    .marker27 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 27 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 27 / 50))), calc(10em * sin(2 * 3.14159 * 27 / 50)));
    }
    .marker28 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 28 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 28 / 50))), calc(10em * sin(2 * 3.14159 * 28 / 50)));
    }
    .marker29 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 29 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 29 / 50))), calc(10em * sin(2 * 3.14159 * 29 / 50)));
    }
    .marker30 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 30 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 30 / 50))), calc(10em * sin(2 * 3.14159 * 30 / 50)));
    }
    .marker31 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 31 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 31 / 50))), calc(10em * sin(2 * 3.14159 * 31 / 50)));
    }
    .marker32 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 32 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 32 / 50))), calc(10em * sin(2 * 3.14159 * 32 / 50)));
    }
    .marker33 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 33 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 33 / 50))), calc(10em * sin(2 * 3.14159 * 33 / 50)));
    }
    .marker34 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 34 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 34 / 50))), calc(10em * sin(2 * 3.14159 * 34 / 50)));
    }
    .marker35 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 35 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 35 / 50))), calc(10em * sin(2 * 3.14159 * 35 / 50)));
    }
    .marker36 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 36 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 36 / 50))), calc(10em * sin(2 * 3.14159 * 36 / 50)));
    }
    .marker37 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 37 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 37 / 50))), calc(10em * sin(2 * 3.14159 * 37 / 50)));
    }
    .marker38 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 38 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 38 / 50))), calc(10em * sin(2 * 3.14159 * 38 / 50)));
    }
    .marker39 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 39 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 39 / 50))), calc(10em * sin(2 * 3.14159 * 39 / 50)));
    }
    .marker40 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 40 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 40 / 50))), calc(10em * sin(2 * 3.14159 * 40 / 50)));
    }
    .marker41 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 41 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 41 / 50))), calc(10em * sin(2 * 3.14159 * 41 / 50)));
    }
    .marker42 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 42 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 42 / 50))), calc(10em * sin(2 * 3.14159 * 42 / 50)));
    }
    .marker43 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 43 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 43 / 50))), calc(10em * sin(2 * 3.14159 * 43 / 50)));
    }
    .marker44 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 44 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 44 / 50))), calc(10em * sin(2 * 3.14159 * 44 / 50)));
    }
    .marker45 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 45 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 45 / 50))), calc(10em * sin(2 * 3.14159 * 45 / 50)));
    }
    .marker46 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 46 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 46 / 50))), calc(10em * sin(2 * 3.14159 * 46 / 50)));
    }
    .marker47 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 47 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 47 / 50))), calc(10em * sin(2 * 3.14159 * 47 / 50)));
    }
    .marker48 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 48 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 48 / 50))), calc(10em * sin(2 * 3.14159 * 48 / 50)));
    }
    .marker49 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 49 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 49 / 50))), calc(10em * sin(2 * 3.14159 * 49 / 50)));
    }
</style>

<div id="spinner-container-marker">
    <div class="marker0"></div>
    <div class="marker1"></div>
    <div class="marker2"></div>
    <div class="marker3"></div>
    <div class="marker4"></div>
    <div class="marker5"></div>
    <div class="marker6"></div>
    <div class="marker7"></div>
    <div class="marker8"></div>
    <div class="marker9"></div>
    <div class="marker10"></div>
    <div class="marker11"></div>
    <div class="marker12"></div>
    <div class="marker13"></div>
    <div class="marker14"></div>
    <div class="marker15"></div>
    <div class="marker16"></div>
    <div class="marker17"></div>
    <div class="marker18"></div>
    <div class="marker19"></div>
    <div class="marker20"></div>
    <div class="marker21"></div>
    <div class="marker22"></div>
    <div class="marker23"></div>
    <div class="marker24"></div>
    <div class="marker25"></div>
    <div class="marker26"></div>
    <div class="marker27"></div>
    <div class="marker28"></div>
    <div class="marker29"></div>
    <div class="marker30"></div>
    <div class="marker31"></div>
    <div class="marker32"></div>
    <div class="marker33"></div>
    <div class="marker34"></div>
    <div class="marker35"></div>
    <div class="marker36"></div>
    <div class="marker37"></div>
    <div class="marker38"></div>
    <div class="marker39"></div>
    <div class="marker40"></div>
    <div class="marker41"></div>
    <div class="marker42"></div>
    <div class="marker43"></div>
    <div class="marker44"></div>
    <div class="marker45"></div>
    <div class="marker46"></div>
    <div class="marker47"></div>
    <div class="marker48"></div>
    <div class="marker49"></div>
</div>
"""

spinner_css = """
<style>
    #spinner-container {
        display: flex;
        align-items: center;
        justify-content: center;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 9999;
    }

    #custom-spinner {
        display: inline-block;
        width: 20vmin;
        height: 20vmin;
        border: 8px solid #6f72de;
        border-left-color: rgba(0, 0, 0, 0);
        border-radius: 50%;
        animation: spin 1s ease-in-out infinite;
    }

    @keyframes spin {
        to {
            transform: rotate(360deg);
        }
    }

    @media (max-width: 600px) {
        #custom-spinner {
            display: inline-block;
            width: 20vmin;
            height: 20vmin;
            border: 6px solid #6f72de;
            border-left-color: rgba(0, 0, 0, 0);
            border-radius: 50%;
            animation: spin 1s ease-in-out infinite;
        }
    }

</style>
<div id="spinner-container">
    <div id="custom-spinner"></div>
</div>
"""

spinner_image_css = """
<style>
    .image-container {{
        display: inline-block;
        width: 25%;
        text-align: center;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 9999;
    }}

    @media (max-width: 600px) {{
        .image-container {{
            width: 50%;
        }}
    }}
</style>
<div class="image-container">
    <img src="data:image/png;base64,{}" class="img-fluid" alt="logo" width="30%">
</div>
"""

def img_to_bytes(img_path):
    img_bytes = pathlib.Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def highlight_diff_by_row(row, color1, color2):
    numeric_row = pd.to_numeric(row, errors='coerce')
    is_diff_list = []
    no_diff_list = []
    if numeric_row.iloc[1:].dtype == np.object:
        is_diff = [False for _ in range(numeric_row.iloc[1:].shape[0])]
    else:
        is_diff = numeric_row.iloc[1:].nunique() > 1
    no_diff = [False for _ in range(numeric_row.iloc[1:].shape[0])]
    is_diff_list.append(is_diff)
    no_diff_list.append(no_diff)
#    list1 = ["background: %s" % color2 if cell else "background: %s" % color2 for cell in no_diff_list]
    list1 = ["background: rgba(%s, %s, %s, %s)" % (
    color2[0], color2[1], color2[2], color2[3]) if cell else "background: rgba(%s, %s, %s, %s)" % (
    color2[0], color2[1], color2[2], color2[3]) for cell in is_diff_list]
    list2 = list1
#    list3 = ["background: %s" % color1 if cell else "background: %s" % color2 for cell in is_diff_list]
    list3 = ["background: rgba(%s, %s, %s, %s)" % (
    color1[0], color1[1], color1[2], color1[3]) if cell else "background: rgba(%s, %s, %s, %s)" % (
    color2[0], color2[1], color2[2], color2[3]) for cell in is_diff_list]
    final_list = list1+list2+list3
    return final_list

class MultiFileDownloader(object):

    def __init__(self):
        super(MultiFileDownloader, self).__init__()

    def download_manual_figures(self, files, name):
        zip_file = io.BytesIO()
        with zipfile.ZipFile(zip_file, mode='w') as zf:
            for i, (data, filename, file_ext) in enumerate(files):
                new_filename = "Comrate_{}_{}_{}.{}".format(name, filename.replace("whatif_", ""), timestr, file_ext)
                zf.writestr(new_filename, data)
        zip_file.seek(0)
        b64 = base64.b64encode(zip_file.getvalue()).decode()
        st.markdown("""
            <style>
                button.css-1n1yxpq.edgvbvh10 {
                    background-color: #25476A;
                    color: #FAFAFA;
                    border-color: #FAFAFA;
                    border-width: 3px;
                    width: 6em;
                    height: 1.8em;
                    margin-top: 1.5em;
                }

                button.css-1n1yxpq.edgvbvh10:hover {
                    background-color: rgba(111, 114, 222, 0.6);
                    color: #25476A;
                    border-color: #25476A;
                }

                @media (max-width: 600px) {
                    button.css-1n1yxpq.edgvbvh10 {
                        width: 100% !important;
                        height: 10em !important;
                        margin-top: -3em;
                    }
                }
            </style>
            """, unsafe_allow_html=True)
        filename_out = "Comrate_{}_financial_statements_manual_analysis_{}".format(name, timestr)
        st.download_button(
            label="Download",
            data=zip_file.getvalue(),
            file_name=f"{filename_out}.zip",
            mime="application/zip",
        )     

    def download_simulation_figures(self, files, name):
        zip_file = io.BytesIO()
        with zipfile.ZipFile(zip_file, mode='w') as zf:
            for i, (data, filename, file_ext) in enumerate(files):
                new_filename = "Comrate_{}_{}_{}.{}".format(name, filename.replace("whatif_", ""), timestr, file_ext)
                zf.writestr(new_filename, data)
        zip_file.seek(0)
        b64 = base64.b64encode(zip_file.getvalue()).decode()
        st.markdown("""
            <style>
                button.css-1n1yxpq.edgvbvh10 {
                    background-color: #25476A;
                    color: #FAFAFA;
                    border-color: #FAFAFA;
                    border-width: 3px;
                    width: 6em;
                    height: 1.8em;
                    margin-top: 1.5em;
                }

                button.css-1n1yxpq.edgvbvh10:hover {
                    background-color: rgba(111, 114, 222, 0.6);
                    color: #25476A;
                    border-color: #25476A;
                }

                @media (max-width: 600px) {
                    button.css-1n1yxpq.edgvbvh10 {
                        width: 100% !important;
                        height: 10em !important;
                        margin-top: -3em;
                    }
                }
            </style>
            """, unsafe_allow_html=True)
        filename_out = "Comrate_{}_financial_statements_simulation_analysis_{}".format(name, timestr)
        st.download_button(
            label="Download",
            data=zip_file.getvalue(),
            file_name=f"{filename_out}.zip",
            mime="application/zip",
        )

    def download_table_alt(self, data, filename, file_ext, name, logo_position, label, company_name):
        file, path = mkstemp()
        os.close(file)
        new_filename = "Comrate_{}_{}_{}.{}".format(name, filename.replace("whatif_", ""), timestr, file_ext)
        dfi.export(data, path, table_conversion="matplotlib")
        image = Image.open(path)
        new_image = Image.new(image.mode, size=(image.size[0], image.size[1]))
        new_image.putdata(image.getdata())
        new_image = ImageOps.expand(new_image, border=70, fill=(255, 255, 255))
        logo = Image.open("images/Paydar-logo-black-transparent-update.png")
        resize_ratio = 0.15
        resize = (int(int(logo.size[0])*resize_ratio), int(int(logo.size[1])*resize_ratio))
        logo = logo.resize(resize)
        new_image.paste(logo, (image.size[0]-logo_position, 5), logo)
        ImageDraw.Draw(new_image).text(xy=(70, 15), text=label, align="left", font=ImageFont.truetype(font=font_manager.findfont(font_manager.FontProperties(family='sans-serif', weight='normal')), size=30), fill="#25476A")
        text = company_name
        font = ImageFont.truetype(
            font=font_manager.findfont(font_manager.FontProperties(family='sans-serif', weight='normal')),
            size=36)
        fill = "#25476A"
        draw = ImageDraw.Draw(new_image)
        text_width, text_height = draw.textsize(text, font=font)
        x = (new_image.width - text_width) // 2
        ImageDraw.Draw(new_image).text(xy=(x, 15), text=text, align="center", font=font, fill=fill)
        byte_array = io.BytesIO()
        new_image.save(byte_array, format='PNG', subsampling=0, quality=100)
        byte_array = byte_array.getvalue()
        os.remove(path)
        return byte_array, new_filename

    def download_figure_alt(self, data, filename, file_ext, name, logo_position, company_name):
        new_filename = "Comrate_{}_{}_{}.{}".format(name, filename.replace("whatif_", ""), timestr, file_ext)
        image = Image.open(io.BytesIO(data))
        new_image = Image.new(image.mode, size=(image.size[0], image.size[1]))
        new_image.putdata(image.getdata())
        new_image = ImageOps.expand(new_image, border=30, fill=(255, 255, 255))
        logo = Image.open("images/Paydar-logo-black-transparent-update.png")
        resize_ratio = 0.15
        resize = (int(int(logo.size[0])*resize_ratio), int(int(logo.size[1])*resize_ratio))
        logo = logo.resize(resize)
        new_image.paste(logo, (image.size[0]-logo_position, 10), logo)
        ImageDraw.Draw(new_image).text(xy=(40, 10), text=company_name, align="left", font=ImageFont.truetype(font=font_manager.findfont(font_manager.FontProperties(family='sans-serif', weight='normal')), size=30), fill="#25476A")
        byte_array = io.BytesIO()
        new_image.save(byte_array, format='PNG', subsampling=0, quality=100)
        byte_array = byte_array.getvalue()
        return byte_array, new_filename

    def export_tables_figures(self, files, name):
        zip_file = io.BytesIO()
        with zipfile.ZipFile(zip_file, mode='w') as zf:
            for i, (data, filename, file_ext, logo_position, file_type, label, company_name) in enumerate(files):
                if file_type == "table":
                    byte_array, new_filename = MultiFileDownloader().download_table_alt(data=data, filename=filename, file_ext=file_ext, name=name, logo_position=logo_position, label=label, company_name=company_name)
                if file_type == "figure":
                    byte_array, new_filename = MultiFileDownloader().download_figure_alt(data=data, filename=filename,
                                                                                        file_ext=file_ext, name=name,
                                                                                        logo_position=logo_position, company_name=company_name)
                zf.writestr(new_filename, byte_array)
        zip_file.seek(0)
        b64 = base64.b64encode(zip_file.getvalue()).decode()

        st.markdown(
            """<style>button.css-1n1yxpq.edgvbvh10 {background-color:#25476A; color: #FAFAFA; border-color: #FAFAFA; border-width: 2.2px; width:6em; height:2em} button.css-1n1yxpq.edgvbvh10:hover {background-color: rgba(111, 114, 222, 0.6); color: #25476A; border-color: #25476A}</style>""",
            unsafe_allow_html=True)
        filename_out = "Comrate_{}_financial_statements_manual_analysis_{}".format(name, timestr)
        st.download_button(
            label="Download",
            data=zip_file.getvalue(),
            file_name=f"{filename_out}.zip",
            mime="application/zip",
        )


    def download_table(self, data, filename, file_ext, label, name, font_size):
        file, path = mkstemp()
        os.close(file)
        new_filename = "Comrate_{}_{}_{}.{}".format(name, filename.replace("whatif_", ""), timestr, file_ext)
        dfi.export(data, path, table_conversion="selenium")
        image = Image.open(path)
        new_image = Image.new(image.mode, size=(image.size[0], image.size[1]))
        new_image.putdata(image.getdata())
        new_image = ImageOps.expand(new_image, border=70, fill=(255, 255, 255))
        logo = Image.open("images/Paydar-logo-black-transparent-update.png")
        resize_ratio = 0.15
        resize = (int(int(logo.size[0])*resize_ratio), int(int(logo.size[1])*resize_ratio))
        logo = logo.resize(resize)
        ImageDraw.Draw(new_image).text(xy=(70, image.size[1]+80), text="blue fields indicate change", align="left", font=ImageFont.truetype(font=font_manager.findfont(font_manager.FontProperties(family='sans-serif', weight='normal', style='italic')), size=18), fill="#25476A")
        ImageDraw.Draw(new_image).text(xy=(70, 15), text=label, align="left", font=ImageFont.truetype(font=font_manager.findfont(font_manager.FontProperties(family='sans-serif', weight='normal')), size=font_size), fill="#25476A")
        new_image.paste(logo, (image.size[0]-90, 5), logo)
        byte_array = io.BytesIO()
        new_image.save(byte_array, format='PNG', subsampling=0, quality=100)
        byte_array = byte_array.getvalue()
        os.remove(path)
        return byte_array, new_filename

    def export_tables(self, files, name):
        zip_file = io.BytesIO()
        with zipfile.ZipFile(zip_file, mode='w') as zf:
            for i, (data, filename, file_ext, label, font_size) in enumerate(files):
                byte_array, new_filename = MultiFileDownloader().download_table(data=data, filename=filename, file_ext=file_ext, label=label, name=name, font_size=font_size)
                zf.writestr(new_filename, byte_array)
        zip_file.seek(0)
        b64 = base64.b64encode(zip_file.getvalue()).decode()

        st.markdown(
            """<style>button.css-1n1yxpq.edgvbvh10 {background-color:#25476A; color: #FAFAFA; border-color: #FAFAFA; border-width: 2.2px; width:6em; height:2em} button.css-1n1yxpq.edgvbvh10:hover {background-color: rgba(111, 114, 222, 0.6); color: #25476A; border-color: #25476A}</style>""",
            unsafe_allow_html=True)
        filename_out = "Comrate_{}_financial_statements_manual_analysis_{}".format(name, timestr)
        st.download_button(
            label="Download",
            data=zip_file.getvalue(),
            file_name=f"{filename_out}.zip",
            mime="application/zip",
        )

class FileDownloader(object):

    def __init__(self, data, filename, file_ext):
        super(FileDownloader, self).__init__()
        self.data = data
        self.filename = filename
        self.file_ext = file_ext

    def download_figure(self):
        b64 = base64.b64encode(self.data).decode()
        new_filename = "{}_{}.{}".format(self.filename, timestr, self.file_ext)
        href = f'<a style="padding-left:0.6em; color:#25476A" href="data:file/{self.file_ext};base64,{b64}" download="{new_filename}">Click Here</a>'
        st.markdown(href, unsafe_allow_html=True)

    def download_table(self, label, font_size):
        file, path = mkstemp()
        os.close(file)
        new_filename = "{}_{}.{}".format(self.filename, timestr, self.file_ext)
        dfi.export(self.data, path)
#        bytes = read_file(path)
#        b64 = base64.b64encode(bytes).decode()
        image = Image.open(path)
        new_image = Image.new(image.mode, size=(image.size[0], image.size[1]))
        new_image.putdata(image.getdata())
        new_image = ImageOps.expand(new_image, border=70, fill=(255, 255, 255))
        logo = Image.open("images/Paydar-logo-black-transparent-update.png")
        resize_ratio = 0.1
        resize = (int(int(logo.size[0])*resize_ratio), int(int(logo.size[1])*resize_ratio))
        logo = logo.resize(resize)
        ImageDraw.Draw(new_image).text(xy=(70, image.size[1]+80), text="blue fields indicate change", align="left", font=ImageFont.truetype(font=font_manager.findfont(font_manager.FontProperties(family='sans-serif', weight='normal', style='italic')), size=18), fill="#25476A")
        ImageDraw.Draw(new_image).text(xy=(70, 15), text=label, align="left", font=ImageFont.truetype(font=font_manager.findfont(font_manager.FontProperties(family='sans-serif', weight='normal')), size=font_size), fill="#25476A")
        new_image.paste(logo, (image.size[0]-100, 12), logo)
        byte_array = io.BytesIO()
        new_image.save(byte_array, format='PNG', subsampling=0, quality=100)
        byte_array = byte_array.getvalue()
        b64 = base64.b64encode(byte_array).decode()
        os.remove(path)
        href = f'<a style="padding-left:0.6em; color:#25476A" href="data:file/{self.file_ext};base64,{b64}" download="{new_filename}">Click Here</a>'
        st.markdown(href, unsafe_allow_html=True)



@st.cache_data(show_spinner=False)
def get_default_fields(select_user_entity_name, select_user_period):

    def get_financials(datafame, user_entity_name, user_period):
        entity_financials = datafame.loc[
            (datafame['entity_name'] == user_entity_name) & (datafame['period'] == user_period)]
        return entity_financials

    def get_financial_field(dataframe, field_name):
        try:
            financial_field = dataframe[field_name].replace(np.nan, 0)
            financial_field = np.float64(financial_field.iloc[0])
        except:
            financial_field = 0
        return financial_field

    if int(select_user_period[5]) - 1 == 0:
        prior_quarter = 4
        prior_year = int(select_user_period[:4]) - 1
    else:
        prior_quarter = int(select_user_period[5]) - 1
        prior_year = int(select_user_period[:4])

    select_user_period_prior = str(prior_year) + "/" + str(prior_quarter) + "F"
    df_financials = get_financials(st.session_state.df_input, select_user_entity_name, select_user_period)
    df_financials_prior = get_financials(st.session_state.df_input, select_user_entity_name, select_user_period_prior)


    ### Actual data ###

    # Income statement
    sales_revenue = get_financial_field(df_financials, 'sales')
    sales_revenue_prior = get_financial_field(df_financials_prior, 'sales')
    sales_revenue_growth = (sales_revenue / sales_revenue_prior - 1) * 100
    cost_of_goods_sold_excl_DA = get_financial_field(df_financials, 'cost_of_goods_sold_excl_DA_AW_WI') # New
    cost_of_goods_sold_excl_DA_margin = cost_of_goods_sold_excl_DA / sales_revenue * 100  # New
    depreciation_and_amortization_expenses = get_financial_field(df_financials, 'depreciation_amortization') # New
    cost_of_goods_sold_incl_depreciation_amortization = cost_of_goods_sold_excl_DA + depreciation_and_amortization_expenses
#    cost_of_goods_sold = get_financial_field(df_financials, 'cost_of_goods_sold_incl_depreciation_amortization')
#    cost_of_goods_sold_margin = cost_of_goods_sold / sales_revenue * 100
#    cost_of_goods_sold_incl_DA_margin = cost_of_goods_sold_incl_depreciation_amortization / sales_revenue * 100 # New
#    gross_profit = sales_revenue - cost_of_goods_sold
    gross_profit = sales_revenue - cost_of_goods_sold_incl_depreciation_amortization # New
    gross_profit_margin = gross_profit / sales_revenue * 100
#    sales_general_and_admin_expenses = get_financial_field(df_financials, 'sg_a_expense')
    sga_oth = get_financial_field(df_financials, 'sga_oth_AW_WI') # New
    research_and_development_expenses = get_financial_field(df_financials, 'r_d_expense')
    sales_general_and_admin_expenses = research_and_development_expenses + sga_oth # New
#    depreciation_and_amortization_expenses = get_financial_field(df_financials, 'depreciation_amortization')
#    ebit = gross_profit - sales_general_and_admin_expenses - research_and_development_expenses - depreciation_and_amortization_expenses
    ebit = gross_profit - sales_general_and_admin_expenses # New
    ebit_margin = ebit / sales_revenue * 100
#    non_operating_income = get_financial_field(df_financials, 'no_field_value_1')
#    unusual_expenses = get_financial_field(df_financials, 'no_field_value_2')
    other_income_expense = get_financial_field(df_financials, 'other_income_expense_AW_WI') # New
    interest_expense = get_financial_field(df_financials, 'net_interest_Expense')
    long_term_notes_payable = get_financial_field(df_financials, 'long_term_debt')
    other_long_term_liabilities = get_financial_field(df_financials, 'other_long_term_liabilities_AW_WI')  # New
#    other_long_term_liabilities = get_financial_field(df_financials, 'no_field_value_20')
    total_non_current_liabilities = long_term_notes_payable + other_long_term_liabilities
    interest_rate = interest_expense / total_non_current_liabilities * 100
#    pbt = ebit - non_operating_income - unusual_expenses - interest_expense
    pbt = ebit + other_income_expense - interest_expense # New
    income_tax_expense = get_financial_field(df_financials, 'income_tax')
    tax_rate = get_financial_field(df_financials, 'tax_rate')
    tax_rate = np.float64(max(income_tax_expense / pbt * 100, 0))
    net_income = pbt - income_tax_expense
    net_income_margin = net_income / sales_revenue * 100
#    dividend_or_distributions_paid = get_financial_field(df_financials, 'common_dividends')
    dividend_or_distributions_paid = get_financial_field(df_financials, 'dividend_or_distributions_paid') # New
    dividend_payout_ratio = dividend_or_distributions_paid / net_income * 100


    # Cash flow statement
    depreciation_and_amortization_expenses_sales = depreciation_and_amortization_expenses / sales_revenue * 100
#    increase_in_other_items = get_financial_field(df_financials, 'no_field_value_5')
    increase_decrease_in_other_items = get_financial_field(df_financials, 'increase_decrease_in_other_items_AW_WI') # New
#    funds_from_operations = net_income + depreciation_and_amortization_expenses + increase_in_other_items
    funds_from_operations = net_income + depreciation_and_amortization_expenses + increase_decrease_in_other_items # New
    change_in_working_capital = get_financial_field(df_financials, 'change_in_working_capital')
    net_cash_from_operating_activities = funds_from_operations + change_in_working_capital
    capital_expenditure = get_financial_field(df_financials, 'capex_fixed_assets')
    capital_expenditure_sales = capital_expenditure / sales_revenue * 100
#    other_investing_activities = get_financial_field(df_financials, 'no_field_value_99')
    other_investing_activities = get_financial_field(df_financials, 'other_investing_activities_AW_WI') # New
    net_cash_from_investing_activities = other_investing_activities - capital_expenditure
#    sale_repurchase_of_equity = get_financial_field(df_financials, 'no_field_value_8')
    sale_repurchase_of_equity = get_financial_field(df_financials, 'sale_repurchase_of_equity') # New
#    proceeds_from_issuance_of_debt = get_financial_field(df_financials, 'no_field_value_9')
#    repayments_of_long_term_debt = get_financial_field(df_financials, 'no_field_value_10')
    issuance_reduction_of_debt = get_financial_field(df_financials, 'issuance_reduction_of_debt') # New
#    other_financing_activities = get_financial_field(df_financials, 'no_field_value_11')
    other_financing_activities = get_financial_field(df_financials, 'other_financing_activities_AW_WI') # New
#    net_cash_from_financing_activities = sale_repurchase_of_equity + proceeds_from_issuance_of_debt + repayments_of_long_term_debt + other_financing_activities - dividend_or_distributions_paid
    net_cash_from_financing_activities = sale_repurchase_of_equity + issuance_reduction_of_debt + other_financing_activities - dividend_or_distributions_paid # New
#    exchange_rate_fluctuations = get_financial_field(df_financials, 'no_field_value_13')
#    net_increase_in_cash_and_equivalents = net_cash_from_operating_activities + net_cash_from_investing_activities + net_cash_from_financing_activities + exchange_rate_fluctuations
    net_increase_in_cash_and_equivalents = net_cash_from_operating_activities + net_cash_from_investing_activities + net_cash_from_financing_activities # New


    # Balance sheet
    cash_and_short_term_investments = get_financial_field(df_financials, 'cash_short_term_investments')
    accounts_receivable = get_financial_field(df_financials, 'total_receivables')
    accounts_receivable_days = accounts_receivable / sales_revenue * 365
    inventory = get_financial_field(df_financials, 'inventory')
#    inventory_days = inventory / cost_of_goods_sold * 365
    inventory_days = inventory / cost_of_goods_sold_excl_DA * 365 # New
#    prepaid_expenses = get_financial_field(df_financials, 'prepaid_expenses')
    other_current_assets = get_financial_field(df_financials, 'other_current_assets_AW_WI') # New
#    total_current_assets = cash_and_short_term_investments + accounts_receivable + inventory + prepaid_expenses
    total_current_assets = cash_and_short_term_investments + accounts_receivable + inventory + other_current_assets # New
    property_plant_and_equipment = get_financial_field(df_financials, 'ppe_gross')
    accumulated_depreciation = get_financial_field(df_financials, 'ppe_accumulated_depreciation')
    net_fixed_assets = property_plant_and_equipment - accumulated_depreciation
    intangible_assets = get_financial_field(df_financials, 'intangibles_assets')
#    total_other_assets = get_financial_field(df_financials, 'no_field_value_18')
    total_other_assets = get_financial_field(df_financials, 'total_other_assets_AW_WI') # New
    total_assets = total_current_assets + net_fixed_assets + intangible_assets + total_other_assets
    accounts_payable = get_financial_field(df_financials, 'accounts_payable')
#    accounts_payable_days = accounts_payable / cost_of_goods_sold * 365
    accounts_payable_days = accounts_payable / cost_of_goods_sold_excl_DA * 365 # New
#    accrued_expenses_payable = get_financial_field(df_financials, 'accrued_expenses')
#    short_term_notes_payable = get_financial_field(df_financials, 'short_term_debt')
    short_term_notes_payable = get_financial_field(df_financials, 'short_term_notes_AW_WI') # New
#    other_short_term_liabilities = get_financial_field(df_financials, 'current_lt_debt')
    other_short_term_liabilities = get_financial_field(df_financials, 'other_short_term_liabilities_AW_WI') # New
#    total_current_liabilities = accounts_payable + accrued_expenses_payable + short_term_notes_payable + other_short_term_liabilities
    total_current_liabilities = accounts_payable + short_term_notes_payable + other_short_term_liabilities # New
    long_term_notes_payable = get_financial_field(df_financials, 'long_term_debt')
#    other_long_term_liabilities = get_financial_field(df_financials, 'no_field_value_20')
    other_long_term_liabilities = get_financial_field(df_financials, 'other_long_term_liabilities_AW_WI') # New
    total_non_current_liabilities = long_term_notes_payable + other_long_term_liabilities
    total_liabilities = total_current_liabilities + total_non_current_liabilities
#    capital_stock = get_financial_field(df_financials, 'common_equity_total')
    stock_value = get_financial_field(df_financials, 'stock_value_AW_WI') # New
    retained_earnings = get_financial_field(df_financials, 'retained_earnings')
    capital_stock = stock_value + retained_earnings # New
    other_equity = get_financial_field(df_financials, 'other_equity_AW_WI') # New
#    adjustments = total_assets - (total_liabilities + capital_stock + retained_earnings)
#    total_shareholders_equity = capital_stock + retained_earnings + adjustments
    adjustments = total_assets - (total_liabilities + capital_stock + other_equity) # New
    total_shareholders_equity = capital_stock + other_equity + adjustments # New
    balance_check = total_assets - total_liabilities - total_shareholders_equity


    ### What-if data ###

    # Income statement
    # User input fields
    default_whatif_sales_revenue_growth_user = sales_revenue_growth
#    default_whatif_cost_of_goods_sold_margin_user = cost_of_goods_sold_margin
    default_whatif_cost_of_goods_sold_margin_user = cost_of_goods_sold_excl_DA_margin # New
#    default_whatif_sales_general_and_admin_expenses_user = sales_general_and_admin_expenses
    default_whatif_sales_general_and_admin_expenses_user = sga_oth # New
    default_whatif_research_and_development_expenses_user = research_and_development_expenses
    default_whatif_depreciation_and_amortization_expenses_sales_user = depreciation_and_amortization_expenses_sales
    default_whatif_depreciation_and_amortization_split_user = 100
    default_whatif_interest_rate_user = interest_rate
    default_whatif_tax_rate_user = tax_rate
    default_whatif_dividend_payout_ratio_user = dividend_payout_ratio


    # Cash flow statement / balance sheet
    # User input fields
    default_whatif_accounts_receivable_days_user = accounts_receivable_days
    default_whatif_inventory_days_user = inventory_days
    default_whatif_capital_expenditure_sales_user = capital_expenditure_sales
    default_whatif_capital_expenditure_user = capital_expenditure
    default_whatif_capital_expenditure_indicator_user = "Dollar"
    default_whatif_tangible_intangible_split_user = 100
    default_whatif_accounts_payable_days_user = accounts_payable_days
    default_whatif_sale_of_equity_user = 0.00
    default_whatif_repurchase_of_equity_user = 0.00
    default_whatif_proceeds_from_issuance_of_debt_user = 0.00
    default_whatif_repayments_of_long_term_debt_user = 0.00
    default_whatif_notes_other_split_user = 50

    return default_whatif_sales_revenue_growth_user, default_whatif_cost_of_goods_sold_margin_user, default_whatif_sales_general_and_admin_expenses_user, default_whatif_research_and_development_expenses_user, default_whatif_depreciation_and_amortization_expenses_sales_user, default_whatif_depreciation_and_amortization_split_user, default_whatif_interest_rate_user, default_whatif_tax_rate_user, default_whatif_dividend_payout_ratio_user, default_whatif_accounts_receivable_days_user, default_whatif_inventory_days_user, default_whatif_capital_expenditure_sales_user, default_whatif_capital_expenditure_user, default_whatif_capital_expenditure_indicator_user, default_whatif_tangible_intangible_split_user, default_whatif_accounts_payable_days_user, default_whatif_sale_of_equity_user, default_whatif_repurchase_of_equity_user, default_whatif_proceeds_from_issuance_of_debt_user, default_whatif_repayments_of_long_term_debt_user, default_whatif_notes_other_split_user


@st.cache_data(show_spinner=False)
def run_whatif(select_user_entity_name, select_user_period, select_user_whatif_sales_revenue_growth, select_user_whatif_cost_of_goods_sold_margin, select_user_whatif_sales_general_and_admin_expenses, select_user_whatif_research_and_development_expenses, select_user_whatif_depreciation_and_amortization_expenses_sales, select_user_whatif_depreciation_and_amortization_split, select_user_whatif_interest_rate, select_user_whatif_tax_rate, select_user_whatif_dividend_payout_ratio, select_user_whatif_accounts_receivable_days, select_user_whatif_inventory_days, select_user_whatif_capital_expenditure_sales, select_user_whatif_capital_expenditure, select_user_whatif_capital_expenditure_indicator, select_user_whatif_tangible_intangible_split, select_user_whatif_accounts_payable_days, select_user_whatif_sale_of_equity, select_user_whatif_repurchase_of_equity, select_user_whatif_proceeds_from_issuance_of_debt, select_user_whatif_repayments_of_long_term_debt, select_user_whatif_notes_other_split):

    def get_financials(datafame, user_entity_name, user_period):
        entity_financials = datafame.loc[
            (datafame['entity_name'] == user_entity_name) & (datafame['period'] == user_period)]
        return entity_financials

    def get_financial_field(dataframe, field_name):
        try:
            financial_field = dataframe[field_name].replace(np.nan, 0)
            financial_field = np.float64(financial_field.iloc[0])
        except:
            financial_field = 0
        return financial_field

    if int(select_user_period[5]) - 1 == 0:
        prior_quarter = 4
        prior_year = int(select_user_period[:4]) - 1
    else:
        prior_quarter = int(select_user_period[5]) - 1
        prior_year = int(select_user_period[:4])

    select_user_period_prior = str(prior_year) + "/" + str(prior_quarter) + "F"
    df_financials = get_financials(st.session_state.df_input, select_user_entity_name, select_user_period)
    df_financials_prior = get_financials(st.session_state.df_input, select_user_entity_name, select_user_period_prior)


    ### Actual data ###

    # Income statement
    sales_revenue = get_financial_field(df_financials, 'sales')
    sales_revenue_prior = get_financial_field(df_financials_prior, 'sales')
    sales_revenue_growth = (sales_revenue / sales_revenue_prior - 1) * 100
    cost_of_goods_sold_excl_DA = get_financial_field(df_financials, 'cost_of_goods_sold_excl_DA_AW_WI')  # New
    cost_of_goods_sold_excl_DA_margin = cost_of_goods_sold_excl_DA / sales_revenue * 100  # New
    depreciation_and_amortization_expenses = get_financial_field(df_financials, 'depreciation_amortization')  # New
    cost_of_goods_sold_incl_depreciation_amortization = cost_of_goods_sold_excl_DA + depreciation_and_amortization_expenses
    #    cost_of_goods_sold = get_financial_field(df_financials, 'cost_of_goods_sold_incl_depreciation_amortization')
    #    cost_of_goods_sold_margin = cost_of_goods_sold / sales_revenue * 100
    #    cost_of_goods_sold_incl_DA_margin = cost_of_goods_sold_incl_depreciation_amortization / sales_revenue * 100 # New
    #    gross_profit = sales_revenue - cost_of_goods_sold
    gross_profit = sales_revenue - cost_of_goods_sold_incl_depreciation_amortization  # New
    gross_profit_margin = gross_profit / sales_revenue * 100
    #    sales_general_and_admin_expenses = get_financial_field(df_financials, 'sg_a_expense')
    sga_oth = get_financial_field(df_financials, 'sga_oth_AW_WI')  # New
    research_and_development_expenses = get_financial_field(df_financials, 'r_d_expense')
    sales_general_and_admin_expenses = research_and_development_expenses + sga_oth  # New
    #    depreciation_and_amortization_expenses = get_financial_field(df_financials, 'depreciation_amortization')
    #    ebit = gross_profit - sales_general_and_admin_expenses - research_and_development_expenses - depreciation_and_amortization_expenses
    ebit = gross_profit - sales_general_and_admin_expenses  # New
    ebit_margin = ebit / sales_revenue * 100
    #    non_operating_income = get_financial_field(df_financials, 'no_field_value_1')
    #    unusual_expenses = get_financial_field(df_financials, 'no_field_value_2')
    other_income_expense = get_financial_field(df_financials, 'other_income_expense_AW_WI')  # New
    interest_expense = get_financial_field(df_financials, 'net_interest_Expense')
    long_term_notes_payable = get_financial_field(df_financials, 'long_term_debt')
    other_long_term_liabilities = get_financial_field(df_financials, 'other_long_term_liabilities_AW_WI')  # New
    #    other_long_term_liabilities = get_financial_field(df_financials, 'no_field_value_20')
    total_non_current_liabilities = long_term_notes_payable + other_long_term_liabilities
    interest_rate = interest_expense / total_non_current_liabilities * 100
    #    pbt = ebit - non_operating_income - unusual_expenses - interest_expense
    pbt = ebit + other_income_expense - interest_expense  # New
    income_tax_expense = get_financial_field(df_financials, 'income_tax')
    tax_rate = get_financial_field(df_financials, 'tax_rate')
    tax_rate = np.float64(max(income_tax_expense / pbt * 100, 0))
    net_income = pbt - income_tax_expense
    net_income_margin = net_income / sales_revenue * 100
    #    dividend_or_distributions_paid = get_financial_field(df_financials, 'common_dividends')
    dividend_or_distributions_paid = get_financial_field(df_financials, 'dividend_or_distributions_paid')  # New
    dividend_payout_ratio = dividend_or_distributions_paid / net_income * 100


    # Cash flow statement
    depreciation_and_amortization_expenses_sales = depreciation_and_amortization_expenses / sales_revenue * 100
    #    increase_in_other_items = get_financial_field(df_financials, 'no_field_value_5')
    increase_decrease_in_other_items = get_financial_field(df_financials,
                                                           'increase_decrease_in_other_items_AW_WI')  # New
    #    funds_from_operations = net_income + depreciation_and_amortization_expenses + increase_in_other_items
    funds_from_operations = net_income + depreciation_and_amortization_expenses + increase_decrease_in_other_items  # New
    change_in_working_capital = get_financial_field(df_financials, 'change_in_working_capital')
    net_cash_from_operating_activities = funds_from_operations + change_in_working_capital
    capital_expenditure = get_financial_field(df_financials, 'capex_fixed_assets')
    capital_expenditure_sales = capital_expenditure / sales_revenue * 100
    #    other_investing_activities = get_financial_field(df_financials, 'no_field_value_99')
    other_investing_activities = get_financial_field(df_financials, 'other_investing_activities_AW_WI')  # New
    net_cash_from_investing_activities = other_investing_activities - capital_expenditure
    #    sale_repurchase_of_equity = get_financial_field(df_financials, 'no_field_value_8')
    sale_repurchase_of_equity = get_financial_field(df_financials, 'sale_repurchase_of_equity')  # New
    #    proceeds_from_issuance_of_debt = get_financial_field(df_financials, 'no_field_value_9')
    #    repayments_of_long_term_debt = get_financial_field(df_financials, 'no_field_value_10')
    issuance_reduction_of_debt = get_financial_field(df_financials, 'issuance_reduction_of_debt')  # New
    #    other_financing_activities = get_financial_field(df_financials, 'no_field_value_11')
    other_financing_activities = get_financial_field(df_financials, 'other_financing_activities_AW_WI')  # New
    #    net_cash_from_financing_activities = sale_repurchase_of_equity + proceeds_from_issuance_of_debt + repayments_of_long_term_debt + other_financing_activities - dividend_or_distributions_paid
    net_cash_from_financing_activities = sale_repurchase_of_equity + issuance_reduction_of_debt + other_financing_activities - dividend_or_distributions_paid  # New
    #    exchange_rate_fluctuations = get_financial_field(df_financials, 'no_field_value_13')
    #    net_increase_in_cash_and_equivalents = net_cash_from_operating_activities + net_cash_from_investing_activities + net_cash_from_financing_activities + exchange_rate_fluctuations
    net_increase_in_cash_and_equivalents = net_cash_from_operating_activities + net_cash_from_investing_activities + net_cash_from_financing_activities  # New


    # Balance sheet
    cash_and_short_term_investments = get_financial_field(df_financials, 'cash_short_term_investments')
    accounts_receivable = get_financial_field(df_financials, 'total_receivables')
    accounts_receivable_days = accounts_receivable / sales_revenue * 365
    inventory = get_financial_field(df_financials, 'inventory')
    #    inventory_days = inventory / cost_of_goods_sold * 365
    inventory_days = inventory / cost_of_goods_sold_excl_DA * 365  # New
    #    prepaid_expenses = get_financial_field(df_financials, 'prepaid_expenses')
    other_current_assets = get_financial_field(df_financials, 'other_current_assets_AW_WI')  # New
    #    total_current_assets = cash_and_short_term_investments + accounts_receivable + inventory + prepaid_expenses
    total_current_assets = cash_and_short_term_investments + accounts_receivable + inventory + other_current_assets  # New
    property_plant_and_equipment = get_financial_field(df_financials, 'ppe_gross')
    accumulated_depreciation = get_financial_field(df_financials, 'ppe_accumulated_depreciation')
    net_fixed_assets = property_plant_and_equipment - accumulated_depreciation
    intangible_assets = get_financial_field(df_financials, 'intangibles_assets')
    #    total_other_assets = get_financial_field(df_financials, 'no_field_value_18')
    total_other_assets = get_financial_field(df_financials, 'total_other_assets_AW_WI')  # New
    total_assets = total_current_assets + net_fixed_assets + intangible_assets + total_other_assets
    accounts_payable = get_financial_field(df_financials, 'accounts_payable')
    #    accounts_payable_days = accounts_payable / cost_of_goods_sold * 365
    accounts_payable_days = accounts_payable / cost_of_goods_sold_excl_DA * 365  # New
    #    accrued_expenses_payable = get_financial_field(df_financials, 'accrued_expenses')
    #    short_term_notes_payable = get_financial_field(df_financials, 'short_term_debt')
    short_term_notes_payable = get_financial_field(df_financials, 'short_term_notes_AW_WI')  # New
    #    other_short_term_liabilities = get_financial_field(df_financials, 'current_lt_debt')
    other_short_term_liabilities = get_financial_field(df_financials, 'other_short_term_liabilities_AW_WI')  # New
    #    total_current_liabilities = accounts_payable + accrued_expenses_payable + short_term_notes_payable + other_short_term_liabilities
    total_current_liabilities = accounts_payable + short_term_notes_payable + other_short_term_liabilities  # New
    long_term_notes_payable = get_financial_field(df_financials, 'long_term_debt')
    #    other_long_term_liabilities = get_financial_field(df_financials, 'no_field_value_20')
    other_long_term_liabilities = get_financial_field(df_financials, 'other_long_term_liabilities_AW_WI')  # New
    total_non_current_liabilities = long_term_notes_payable + other_long_term_liabilities
    total_liabilities = total_current_liabilities + total_non_current_liabilities
    #    capital_stock = get_financial_field(df_financials, 'common_equity_total')
    stock_value = get_financial_field(df_financials, 'stock_value_AW_WI')  # New
    retained_earnings = get_financial_field(df_financials, 'retained_earnings')
    capital_stock = stock_value + retained_earnings  # New
    other_equity = get_financial_field(df_financials, 'other_equity_AW_WI')  # New
    #    adjustments = total_assets - (total_liabilities + capital_stock + retained_earnings)
    #    total_shareholders_equity = capital_stock + retained_earnings + adjustments
    adjustments = total_assets - (total_liabilities + capital_stock + other_equity)  # New
    total_shareholders_equity = capital_stock + other_equity + adjustments  # New
    balance_check = total_assets - total_liabilities - total_shareholders_equity


    ### What-if data ###

    # Income statement
    # User input fields
    whatif_sales_revenue_growth_user = select_user_whatif_sales_revenue_growth
    whatif_cost_of_goods_sold_margin_user = select_user_whatif_cost_of_goods_sold_margin
    whatif_sales_general_and_admin_expenses_user = select_user_whatif_sales_general_and_admin_expenses
    whatif_research_and_development_expenses_user = select_user_whatif_research_and_development_expenses
    whatif_depreciation_and_amortization_expenses_sales_user = select_user_whatif_depreciation_and_amortization_expenses_sales
    whatif_depreciation_and_amortization_split_user = select_user_whatif_depreciation_and_amortization_split
    whatif_interest_rate_user = select_user_whatif_interest_rate
    whatif_tax_rate_user = select_user_whatif_tax_rate
    whatif_dividend_payout_ratio_user = select_user_whatif_dividend_payout_ratio


    # Cash flow statement / balance sheet
    # User input fields
    whatif_accounts_receivable_days_user = select_user_whatif_accounts_receivable_days
    whatif_inventory_days_user = select_user_whatif_inventory_days
    whatif_capital_expenditure_sales_user = select_user_whatif_capital_expenditure_sales
    whatif_capital_expenditure_user = select_user_whatif_capital_expenditure
    whatif_capital_expenditure_indicator_user = select_user_whatif_capital_expenditure_indicator
    whatif_tangible_intangible_split_user = select_user_whatif_tangible_intangible_split
    whatif_accounts_payable_days_user = select_user_whatif_accounts_payable_days
    whatif_sale_of_equity_user = select_user_whatif_sale_of_equity
    whatif_repurchase_of_equity_user = select_user_whatif_repurchase_of_equity
    whatif_proceeds_from_issuance_of_debt_user = select_user_whatif_proceeds_from_issuance_of_debt
    whatif_repayments_of_long_term_debt_user = select_user_whatif_repayments_of_long_term_debt
    whatif_notes_other_split_user = select_user_whatif_notes_other_split


    # Income statement
    # Other fields
    whatif_sales_revenue = sales_revenue * (1 + whatif_sales_revenue_growth_user / 100)
#    whatif_cost_of_goods_sold = whatif_sales_revenue * whatif_cost_of_goods_sold_margin_user / 100
    whatif_cost_of_goods_sold_excl_DA = whatif_sales_revenue * whatif_cost_of_goods_sold_margin_user / 100 # New
    whatif_depreciation_and_amortization_expenses = whatif_depreciation_and_amortization_expenses_sales_user * whatif_sales_revenue / 100 # New
    whatif_cost_of_goods_sold_incl_depreciation_amortization = whatif_cost_of_goods_sold_excl_DA + whatif_depreciation_and_amortization_expenses # New
#    whatif_gross_profit = whatif_sales_revenue - whatif_cost_of_goods_sold
    whatif_gross_profit = whatif_sales_revenue - whatif_cost_of_goods_sold_incl_depreciation_amortization # New
    whatif_gross_profit_margin = whatif_gross_profit / whatif_sales_revenue * 100
#    whatif_depreciation_and_amortization_expenses = whatif_depreciation_and_amortization_expenses_sales_user * whatif_sales_revenue / 100
    whatif_sales_general_and_admin_expenses = whatif_research_and_development_expenses_user + whatif_sales_general_and_admin_expenses_user  # New
#    whatif_ebit = whatif_gross_profit - whatif_sales_general_and_admin_expenses_user - whatif_research_and_development_expenses_user - whatif_depreciation_and_amortization_expenses
    whatif_ebit = whatif_gross_profit - whatif_sales_general_and_admin_expenses # New
    whatif_ebit_margin = whatif_ebit / whatif_sales_revenue * 100
    whatif_other_income_expense = other_income_expense # New
#    whatif_non_operating_income = non_operating_income
#    whatif_unusual_expenses = unusual_expenses
    whatif_long_term_notes_payable = long_term_notes_payable + (whatif_proceeds_from_issuance_of_debt_user - whatif_repayments_of_long_term_debt_user) * whatif_notes_other_split_user / 100
    whatif_other_long_term_liabilities = other_long_term_liabilities + (whatif_proceeds_from_issuance_of_debt_user - whatif_repayments_of_long_term_debt_user) * (1 - whatif_notes_other_split_user / 100)
    whatif_total_non_current_liabilities = whatif_long_term_notes_payable + whatif_other_long_term_liabilities
    whatif_interest_expense = whatif_interest_rate_user * whatif_total_non_current_liabilities / 100
#    whatif_pbt = whatif_ebit - whatif_non_operating_income - whatif_unusual_expenses - whatif_interest_expense
    whatif_pbt = whatif_ebit + whatif_other_income_expense - whatif_interest_expense # New
    whatif_income_tax_expense = whatif_tax_rate_user * whatif_pbt / 100
    whatif_net_income = whatif_pbt - whatif_income_tax_expense
    whatif_net_income_margin = whatif_net_income / whatif_sales_revenue * 100
    whatif_dividend_or_distributions_paid = whatif_dividend_payout_ratio_user * whatif_net_income / 100


    # Cash flow statement / balance sheet
    # Other fields
#    whatif_increase_in_other_items = increase_in_other_items
    whatif_increase_decrease_in_other_items = increase_decrease_in_other_items # New
#    whatif_funds_from_operations = whatif_net_income + whatif_depreciation_and_amortization_expenses + whatif_increase_in_other_items
    whatif_funds_from_operations = whatif_net_income + whatif_depreciation_and_amortization_expenses + whatif_increase_decrease_in_other_items # New
    whatif_accounts_receivable = whatif_accounts_receivable_days_user * whatif_sales_revenue / 365
    whatif_inventory = whatif_inventory_days_user * whatif_cost_of_goods_sold_excl_DA / 365
    whatif_accounts_payable = whatif_accounts_payable_days_user * whatif_cost_of_goods_sold_excl_DA / 365
#    whatif_accrued_expenses_payable = accrued_expenses_payable
#    whatif_change_in_working_capital_user = (accounts_receivable + inventory - accounts_payable - accrued_expenses_payable) - (whatif_accounts_receivable + whatif_inventory - whatif_accounts_payable - whatif_accrued_expenses_payable)
    whatif_change_in_working_capital_user = (accounts_receivable + inventory - accounts_payable) - (whatif_accounts_receivable + whatif_inventory - whatif_accounts_payable) # New
    whatif_net_cash_from_operating_activities = whatif_funds_from_operations + whatif_change_in_working_capital_user
    if whatif_capital_expenditure_indicator_user == "Sales %":
        whatif_capital_expenditure = whatif_sales_revenue * whatif_capital_expenditure_sales_user / 100
    elif whatif_capital_expenditure_indicator_user == "Dollar":
        whatif_capital_expenditure = whatif_capital_expenditure_user
    whatif_capital_expenditure_sales = whatif_capital_expenditure / whatif_sales_revenue * 100
    whatif_other_investing_activities = other_investing_activities
    whatif_net_cash_from_investing_activities = whatif_other_investing_activities - whatif_capital_expenditure
    whatif_sale_repurchase_of_equity = whatif_sale_of_equity_user - whatif_repurchase_of_equity_user
    whatif_issuance_reduction_of_debt = whatif_proceeds_from_issuance_of_debt_user - whatif_repayments_of_long_term_debt_user # New
    whatif_other_financing_activities = other_financing_activities
#    whatif_net_cash_from_financing_activities = whatif_sale_repurchase_of_equity + whatif_proceeds_from_issuance_of_debt_user - whatif_repayments_of_long_term_debt_user + whatif_other_financing_activities - whatif_dividend_or_distributions_paid
    whatif_net_cash_from_financing_activities = whatif_sale_repurchase_of_equity + whatif_issuance_reduction_of_debt + whatif_other_financing_activities - whatif_dividend_or_distributions_paid # New
#    whatif_exchange_rate_fluctuations = exchange_rate_fluctuations
#    whatif_net_increase_in_cash_and_equivalents = whatif_net_cash_from_operating_activities + whatif_net_cash_from_investing_activities + whatif_net_cash_from_financing_activities + whatif_exchange_rate_fluctuations
    whatif_net_increase_in_cash_and_equivalents = whatif_net_cash_from_operating_activities + whatif_net_cash_from_investing_activities + whatif_net_cash_from_financing_activities # New

    whatif_cash_and_short_term_investments = cash_and_short_term_investments + whatif_net_increase_in_cash_and_equivalents
#    whatif_accounts_receivable = whatif_accounts_receivable_days_user * whatif_sales_revenue / 365
    whatif_accounts_receivable_days = whatif_accounts_receivable / whatif_sales_revenue * 365
#    whatif_inventory = whatif_inventory_days_user * whatif_cost_of_goods_sold / 365
#    whatif_inventory_days = whatif_inventory / whatif_cost_of_goods_sold * 365
    whatif_inventory_days = whatif_inventory / whatif_cost_of_goods_sold_excl_DA * 365
#    whatif_prepaid_expenses = prepaid_expenses
#    whatif_other_current_assets = other_current_assets
    whatif_other_current_assets = other_current_assets - whatif_increase_decrease_in_other_items # New
#    whatif_total_current_assets = whatif_cash_and_short_term_investments + whatif_accounts_receivable + whatif_inventory + whatif_prepaid_expenses
    whatif_total_current_assets = whatif_cash_and_short_term_investments + whatif_accounts_receivable + whatif_inventory + whatif_other_current_assets # New
    whatif_property_plant_and_equipment = property_plant_and_equipment + whatif_capital_expenditure * whatif_tangible_intangible_split_user / 100
    whatif_accumulated_depreciation = accumulated_depreciation + whatif_depreciation_and_amortization_expenses * whatif_depreciation_and_amortization_split_user / 100
    whatif_net_fixed_assets = whatif_property_plant_and_equipment - whatif_accumulated_depreciation
    whatif_intangible_assets = intangible_assets + whatif_capital_expenditure * (1 - whatif_tangible_intangible_split_user / 100) - whatif_depreciation_and_amortization_expenses * (1 - whatif_depreciation_and_amortization_split_user / 100)
#    whatif_total_other_assets = total_other_assets
    whatif_total_other_assets = total_other_assets - whatif_other_investing_activities - whatif_other_financing_activities # New
    whatif_total_assets = whatif_total_current_assets + whatif_net_fixed_assets + whatif_intangible_assets + whatif_total_other_assets
#    whatif_accounts_payable = whatif_accounts_payable_days_user * whatif_cost_of_goods_sold / 365
#    whatif_accounts_payable_days = whatif_accounts_payable / whatif_cost_of_goods_sold * 365
    whatif_accounts_payable_days = whatif_accounts_payable / whatif_cost_of_goods_sold_excl_DA * 365 # New
#    whatif_accrued_expenses_payable = accrued_expenses_payable
    whatif_short_term_notes_payable = short_term_notes_payable
    whatif_other_short_term_liabilities = other_short_term_liabilities
#    whatif_total_current_liabilities = whatif_accounts_payable + whatif_accrued_expenses_payable + whatif_short_term_notes_payable + whatif_other_short_term_liabilities
    whatif_total_current_liabilities = whatif_accounts_payable +  whatif_short_term_notes_payable + whatif_other_short_term_liabilities # New

#    whatif_long_term_notes_payable = long_term_notes_payable + (whatif_proceeds_from_issuance_of_debt_user - whatif_repayments_of_long_term_debt_user) * whatif_notes_other_split_user / 100
#    whatif_other_long_term_liabilities = other_long_term_liabilities + (whatif_proceeds_from_issuance_of_debt_user - whatif_repayments_of_long_term_debt_user) * (1 - whatif_notes_other_split_user / 100)
#    whatif_total_non_current_liabilities = whatif_long_term_notes_payable + whatif_other_long_term_liabilities
    whatif_total_liabilities = whatif_total_current_liabilities + whatif_total_non_current_liabilities
#    whatif_capital_stock = capital_stock + whatif_sale_repurchase_of_equity
    whatif_stock_value = stock_value + whatif_sale_repurchase_of_equity # New
    whatif_retained_earnings = retained_earnings + whatif_net_income - whatif_dividend_or_distributions_paid
    whatif_capital_stock = whatif_stock_value + whatif_retained_earnings  # New
    whatif_other_equity = other_equity
#    whatif_adjustments = whatif_total_assets - (whatif_total_liabilities + whatif_capital_stock + whatif_retained_earnings)
#    whatif_total_shareholders_equity = whatif_capital_stock + whatif_retained_earnings + whatif_adjustments
    whatif_adjustments = whatif_total_assets - (whatif_total_liabilities + whatif_capital_stock + whatif_other_equity)  # New
    whatif_total_shareholders_equity = whatif_capital_stock + whatif_other_equity + whatif_adjustments  # New
    whatif_balance_check = whatif_total_assets - whatif_total_liabilities - whatif_total_shareholders_equity


    ### Output tables ###

    # Income statement
    df_income_statement = pd.DataFrame(columns=[select_user_entity_name+" ("+df_financials['currency_iso'].values[0]+ " Millions)", select_user_period, "Scenario"])
#    df_income_statement.loc[0] = ['Sales Revenue', '{:,.0f}'.format(sales_revenue), '{:,.0f}'.format(whatif_sales_revenue)]
#    df_income_statement.loc[1] = ['Sales Revenue Growth %', '{:,.2f}'.format(sales_revenue_growth), '{:,.2f}'.format(whatif_sales_revenue_growth_user)]
#    df_income_statement.loc[2] = ['COGS', '{:,.0f}'.format(-cost_of_goods_sold), '{:,.0f}'.format(-whatif_cost_of_goods_sold)]
#    df_income_statement.loc[3] = ['COGS Margin %', '{:,.2f}'.format(cost_of_goods_sold_margin), '{:,.2f}'.format(whatif_cost_of_goods_sold_margin_user)]
#    df_income_statement.loc[4] = ['Gross Profit', '{:,.0f}'.format(gross_profit), '{:,.0f}'.format(whatif_gross_profit)]
#    df_income_statement.loc[5] = ['Gross Profit Margin %', '{:,.2f}'.format(gross_profit_margin), '{:,.2f}'.format(whatif_gross_profit_margin)]
#    df_income_statement.loc[6] = ['SG&A Expenses', '{:,.0f}'.format(-sales_general_and_admin_expenses), '{:,.0f}'.format(-whatif_sales_general_and_admin_expenses_user)]
#    df_income_statement.loc[7] = ['R&D Expenses', '{:,.0f}'.format(-research_and_development_expenses), '{:,.0f}'.format(-whatif_research_and_development_expenses_user)]
#    df_income_statement.loc[8] = ['D&A Expenses', '{:,.0f}'.format(-depreciation_and_amortization_expenses), '{:,.0f}'.format(-whatif_depreciation_and_amortization_expenses)]
#    df_income_statement.loc[9] = ['EBIT', '{:,.0f}'.format(ebit), '{:,.0f}'.format(whatif_ebit)]
#    df_income_statement.loc[10] = ['EBIT Margin %', '{:,.2f}'.format(ebit_margin), '{:,.2f}'.format(whatif_ebit_margin)]
#    df_income_statement.loc[11] = ['Non-Operating Income', '{:,.0f}'.format(non_operating_income), '{:,.0f}'.format(whatif_non_operating_income)]
#    df_income_statement.loc[12] = ['Unusual Expenses', '{:,.0f}'.format(-unusual_expenses), '{:,.0f}'.format(-whatif_unusual_expenses)]
#    df_income_statement.loc[13] = ['Interest Expenses', '{:,.0f}'.format(-interest_expense), '{:,.0f}'.format(-whatif_interest_expense)]
#    df_income_statement.loc[14] = ['Interest Rate %', '{:,.2f}'.format(interest_rate), '{:,.2f}'.format(whatif_interest_rate_user)]
#    df_income_statement.loc[15] = ['PBT', '{:,.0f}'.format(pbt), '{:,.0f}'.format(whatif_pbt)]
#    df_income_statement.loc[16] = ['Income Tax Expense', '{:,.0f}'.format(-income_tax_expense), '{:,.0f}'.format(-whatif_income_tax_expense)]
#    df_income_statement.loc[17] = ['Tax Rate %', '{:,.2f}'.format(tax_rate), '{:,.2f}'.format(whatif_tax_rate_user)]
#    df_income_statement.loc[18] = ['Net Income', '{:,.0f}'.format(net_income), '{:,.0f}'.format(whatif_net_income)]
#    df_income_statement.loc[19] = ['Net Income Margin %', '{:,.2f}'.format(net_income_margin), '{:,.2f}'.format(whatif_net_income_margin)]
#    df_income_statement.loc[20] = ['Dividend or Distributions Paid', '{:,.0f}'.format(dividend_or_distributions_paid), '{:,.0f}'.format(whatif_dividend_or_distributions_paid)]
#    df_income_statement.loc[21] = ['Dividend Payout Ratio %', '{:,.2f}'.format(dividend_payout_ratio), '{:,.2f}'.format(whatif_dividend_payout_ratio_user)]

    df_income_statement.loc[0] = ['Sales Revenue', '{:,.0f}'.format(sales_revenue), '{:,.0f}'.format(whatif_sales_revenue)]
    df_income_statement.loc[1] = ['Sales Revenue Growth %', '{:,.2f}'.format(sales_revenue_growth), '{:,.2f}'.format(whatif_sales_revenue_growth_user)]
    df_income_statement.loc[2] = ['COGS (Excluding D&A)', '{:,.0f}'.format(-cost_of_goods_sold_excl_DA), '{:,.0f}'.format(-whatif_cost_of_goods_sold_excl_DA)]
    df_income_statement.loc[3] = ['COGS (Excluding D&A) Margin %', '{:,.2f}'.format(cost_of_goods_sold_excl_DA_margin), '{:,.2f}'.format(whatif_cost_of_goods_sold_margin_user)]
    df_income_statement.loc[4] = ['D&A Expenses', '{:,.0f}'.format(-depreciation_and_amortization_expenses), '{:,.0f}'.format(-whatif_depreciation_and_amortization_expenses)]
    df_income_statement.loc[5] = ['COGS (Including D&A)', '{:,.0f}'.format(-cost_of_goods_sold_incl_depreciation_amortization), '{:,.0f}'.format(-whatif_cost_of_goods_sold_incl_depreciation_amortization)]
    df_income_statement.loc[6] = ['Gross Profit', '{:,.0f}'.format(gross_profit), '{:,.0f}'.format(whatif_gross_profit)]
    df_income_statement.loc[7] = ['Gross Profit Margin %', '{:,.2f}'.format(gross_profit_margin), '{:,.2f}'.format(whatif_gross_profit_margin)]
    df_income_statement.loc[8] = ['SG&A (Other) Expenses', '{:,.0f}'.format(-sga_oth), '{:,.0f}'.format(-whatif_sales_general_and_admin_expenses_user)]
    df_income_statement.loc[9] = ['R&D Expenses', '{:,.0f}'.format(-research_and_development_expenses), '{:,.0f}'.format(-whatif_research_and_development_expenses_user)]
    df_income_statement.loc[10] = ['SG&A (Including R&D) Expenses', '{:,.0f}'.format(-sales_general_and_admin_expenses), '{:,.0f}'.format(-whatif_sales_general_and_admin_expenses)]
    df_income_statement.loc[11] = ['EBIT', '{:,.0f}'.format(ebit), '{:,.0f}'.format(whatif_ebit)]
    df_income_statement.loc[12] = ['EBIT Margin %', '{:,.2f}'.format(ebit_margin), '{:,.2f}'.format(whatif_ebit_margin)]
    df_income_statement.loc[13] = ['Other Income (Expenses)', '{:,.0f}'.format(other_income_expense), '{:,.0f}'.format(whatif_other_income_expense)]
    df_income_statement.loc[14] = ['Interest Expenses', '{:,.0f}'.format(-interest_expense), '{:,.0f}'.format(-whatif_interest_expense)]
    df_income_statement.loc[15] = ['Interest Rate %', '{:,.2f}'.format(interest_rate), '{:,.2f}'.format(whatif_interest_rate_user)]
    df_income_statement.loc[16] = ['PBT', '{:,.0f}'.format(pbt), '{:,.0f}'.format(whatif_pbt)]
    df_income_statement.loc[17] = ['Income Tax Expense', '{:,.0f}'.format(-income_tax_expense), '{:,.0f}'.format(-whatif_income_tax_expense)]
    df_income_statement.loc[18] = ['Tax Rate %', '{:,.2f}'.format(tax_rate), '{:,.2f}'.format(whatif_tax_rate_user)]
    df_income_statement.loc[19] = ['Net Income', '{:,.0f}'.format(net_income), '{:,.0f}'.format(whatif_net_income)]
    df_income_statement.loc[20] = ['Net Income Margin %', '{:,.2f}'.format(net_income_margin), '{:,.2f}'.format(whatif_net_income_margin)]
    df_income_statement.loc[21] = ['Dividend or Distributions Paid', '{:,.0f}'.format(dividend_or_distributions_paid), '{:,.0f}'.format(whatif_dividend_or_distributions_paid)]
    df_income_statement.loc[22] = ['Dividend Payout Ratio %', '{:,.2f}'.format(dividend_payout_ratio), '{:,.2f}'.format(whatif_dividend_payout_ratio_user)]


    # Cash flow statement
    df_cash_flow_statement = pd.DataFrame(columns=[select_user_entity_name+" ("+df_financials['currency_iso'].values[0]+ " Millions)", select_user_period, "Scenario"])
#    df_cash_flow_statement.loc[0] = ['Net Income', '{:,.0f}'.format(net_income), '{:,.0f}'.format(whatif_net_income)]
#    df_cash_flow_statement.loc[1] = ['D&A Expenses', '{:,.0f}'.format(depreciation_and_amortization_expenses), '{:,.0f}'.format(whatif_depreciation_and_amortization_expenses)]
#    df_cash_flow_statement.loc[2] = ['D&A Expenses / Sales %', '{:,.2f}'.format(depreciation_and_amortization_expenses_sales), '{:,.2f}'.format(whatif_depreciation_and_amortization_expenses_sales_user)]
#    df_cash_flow_statement.loc[3] = ['Increase (Decrease) in Other Items', '{:,.0f}'.format(increase_in_other_items), '{:,.0f}'.format(whatif_increase_in_other_items)]
#    df_cash_flow_statement.loc[4] = ['Funds from Operations', '{:,.0f}'.format(funds_from_operations), '{:,.0f}'.format(whatif_funds_from_operations)]
#    df_cash_flow_statement.loc[5] = ['Change in Working Capital', '{:,.0f}'.format(change_in_working_capital), '{:,.0f}'.format(whatif_change_in_working_capital_user)]
#    df_cash_flow_statement.loc[6] = ['Net Cash from Operating Activities', '{:,.0f}'.format(net_cash_from_operating_activities), '{:,.0f}'.format(whatif_net_cash_from_operating_activities)]
#    df_cash_flow_statement.loc[7] = ['Capital Expenditure', '{:,.0f}'.format(-capital_expenditure), '{:,.0f}'.format(-whatif_capital_expenditure)]
#    df_cash_flow_statement.loc[8] = ['Capital Expenditure / Sales %', '{:,.2f}'.format(capital_expenditure_sales), '{:,.2f}'.format(whatif_capital_expenditure_sales)]
#    df_cash_flow_statement.loc[9] = ['Other Investing Activities', '{:,.0f}'.format(other_investing_activities), '{:,.0f}'.format(whatif_other_investing_activities)]
#    df_cash_flow_statement.loc[10] = ['Net Cash from Investing Activities', '{:,.0f}'.format(net_cash_from_investing_activities), '{:,.0f}'.format(whatif_net_cash_from_investing_activities)]
#    df_cash_flow_statement.loc[11] = ['Dividend or Distributions Paid', '{:,.0f}'.format(-dividend_or_distributions_paid), '{:,.0f}'.format(-whatif_dividend_or_distributions_paid)]
#    df_cash_flow_statement.loc[12] = ['Sale (Repurchase) of Equity', '{:,.0f}'.format(sale_repurchase_of_equity), '{:,.0f}'.format(whatif_sale_repurchase_of_equity)]
#    df_cash_flow_statement.loc[13] = ['Proceeds from Issuance of Debt', '{:,.0f}'.format(proceeds_from_issuance_of_debt), '{:,.0f}'.format(whatif_proceeds_from_issuance_of_debt_user)]
#    df_cash_flow_statement.loc[14] = ['Repayments of Long Term Debt', '{:,.0f}'.format(repayments_of_long_term_debt), '{:,.0f}'.format(-whatif_repayments_of_long_term_debt_user)]
#    df_cash_flow_statement.loc[15] = ['Other Financing Activities', '{:,.0f}'.format(other_financing_activities), '{:,.0f}'.format(whatif_other_financing_activities)]
#    df_cash_flow_statement.loc[16] = ['Net Cash from Financing Activities', '{:,.0f}'.format(net_cash_from_financing_activities), '{:,.0f}'.format(whatif_net_cash_from_financing_activities)]
#    df_cash_flow_statement.loc[17] = ['Exchange Rate Fluctuations', '{:,.0f}'.format(exchange_rate_fluctuations), '{:,.0f}'.format(whatif_exchange_rate_fluctuations)]
#    df_cash_flow_statement.loc[17] = ['Net Increase in Cash & Equivalents', '{:,.0f}'.format(net_increase_in_cash_and_equivalents), '{:,.0f}'.format(whatif_net_increase_in_cash_and_equivalents)]

    df_cash_flow_statement.loc[0] = ['Net Income', '{:,.0f}'.format(net_income), '{:,.0f}'.format(whatif_net_income)]
    df_cash_flow_statement.loc[1] = ['D&A Expenses', '{:,.0f}'.format(depreciation_and_amortization_expenses), '{:,.0f}'.format(whatif_depreciation_and_amortization_expenses)]
    df_cash_flow_statement.loc[2] = ['D&A Expenses / Sales %', '{:,.2f}'.format(depreciation_and_amortization_expenses_sales), '{:,.2f}'.format(whatif_depreciation_and_amortization_expenses_sales_user)]
    df_cash_flow_statement.loc[3] = ['Increase (Decrease) in Other Items', '{:,.0f}'.format(increase_decrease_in_other_items), '{:,.0f}'.format(whatif_increase_decrease_in_other_items)]
    df_cash_flow_statement.loc[4] = ['Funds from Operations', '{:,.0f}'.format(funds_from_operations), '{:,.0f}'.format(whatif_funds_from_operations)]
    df_cash_flow_statement.loc[5] = ['Change in Working Capital', '{:,.0f}'.format(change_in_working_capital), '{:,.0f}'.format(whatif_change_in_working_capital_user)]
    df_cash_flow_statement.loc[6] = ['Net Cash from Operating Activities', '{:,.0f}'.format(net_cash_from_operating_activities), '{:,.0f}'.format(whatif_net_cash_from_operating_activities)]
    df_cash_flow_statement.loc[7] = ['Capital Expenditure', '{:,.0f}'.format(-capital_expenditure), '{:,.0f}'.format(-whatif_capital_expenditure)]
    df_cash_flow_statement.loc[8] = ['Capital Expenditure / Sales %', '{:,.2f}'.format(capital_expenditure_sales), '{:,.2f}'.format(whatif_capital_expenditure_sales)]
    df_cash_flow_statement.loc[9] = ['Other Investing Activities', '{:,.0f}'.format(other_investing_activities), '{:,.0f}'.format(whatif_other_investing_activities)]
    df_cash_flow_statement.loc[10] = ['Net Cash from Investing Activities', '{:,.0f}'.format(net_cash_from_investing_activities), '{:,.0f}'.format(whatif_net_cash_from_investing_activities)]
    df_cash_flow_statement.loc[11] = ['Dividend or Distributions Paid', '{:,.0f}'.format(-dividend_or_distributions_paid), '{:,.0f}'.format(-whatif_dividend_or_distributions_paid)]
    df_cash_flow_statement.loc[12] = ['Sale (Repurchase) of Equity', '{:,.0f}'.format(sale_repurchase_of_equity), '{:,.0f}'.format(whatif_sale_repurchase_of_equity)]
    df_cash_flow_statement.loc[13] = ['Issuance (Reduction) of Debt', '{:,.0f}'.format(issuance_reduction_of_debt), '{:,.0f}'.format(whatif_issuance_reduction_of_debt)]
    df_cash_flow_statement.loc[14] = ['Other Financing Activities', '{:,.0f}'.format(other_financing_activities), '{:,.0f}'.format(whatif_other_financing_activities)]
    df_cash_flow_statement.loc[15] = ['Net Cash from Financing Activities', '{:,.0f}'.format(net_cash_from_financing_activities), '{:,.0f}'.format(whatif_net_cash_from_financing_activities)]
    df_cash_flow_statement.loc[16] = ['Net Increase in Cash & Equivalents', '{:,.0f}'.format(net_increase_in_cash_and_equivalents), '{:,.0f}'.format(whatif_net_increase_in_cash_and_equivalents)]


    # Balance sheet
    df_balance_sheet = pd.DataFrame(columns=[select_user_entity_name+" ("+df_financials['currency_iso'].values[0]+ " Millions)", select_user_period, "Scenario"])
#    df_balance_sheet.loc[0] = ['Cash & Short Term Investments', '{:,.0f}'.format(cash_and_short_term_investments), '{:,.0f}'.format(whatif_cash_and_short_term_investments)]
#    df_balance_sheet.loc[1] = ['Accounts Receivable', '{:,.0f}'.format(accounts_receivable), '{:,.0f}'.format(whatif_accounts_receivable)]
#    df_balance_sheet.loc[2] = ['Accounts Receivable Days', '{:,.0f}'.format(accounts_receivable_days), '{:,.0f}'.format(whatif_accounts_receivable_days)]
#    df_balance_sheet.loc[3] = ['Inventory', '{:,.0f}'.format(inventory), '{:,.0f}'.format(whatif_inventory)]
#    df_balance_sheet.loc[4] = ['Inventory Days', '{:,.0f}'.format(inventory_days), '{:,.0f}'.format(whatif_inventory_days)]
#    df_balance_sheet.loc[5] = ['Prepaid Expenses', '{:,.0f}'.format(prepaid_expenses), '{:,.0f}'.format(whatif_prepaid_expenses)]
#    df_balance_sheet.loc[6] = ['Total Current Assets', '{:,.0f}'.format(total_current_assets), '{:,.0f}'.format(whatif_total_current_assets)]
#    df_balance_sheet.loc[7] = ['Property, Plant & Equipment', '{:,.0f}'.format(property_plant_and_equipment), '{:,.0f}'.format(whatif_property_plant_and_equipment)]
#    df_balance_sheet.loc[8] = ['Accumulated Depreciation', '{:,.0f}'.format(-accumulated_depreciation), '{:,.0f}'.format(-whatif_accumulated_depreciation)]
#    df_balance_sheet.loc[9] = ['Net Fixed Assets', '{:,.0f}'.format(net_fixed_assets), '{:,.0f}'.format(whatif_net_fixed_assets)]
#    df_balance_sheet.loc[10] = ['Intangible Assets', '{:,.0f}'.format(intangible_assets), '{:,.0f}'.format(whatif_intangible_assets)]
#    df_balance_sheet.loc[11] = ['Total Other Assets', '{:,.0f}'.format(total_other_assets), '{:,.0f}'.format(whatif_total_other_assets)]
#    df_balance_sheet.loc[12] = ['Total Assets', '{:,.0f}'.format(total_assets), '{:,.0f}'.format(whatif_total_assets)]
#    df_balance_sheet.loc[13] = ['Accounts Payable', '{:,.0f}'.format(accounts_payable), '{:,.0f}'.format(whatif_accounts_payable)]
#    df_balance_sheet.loc[14] = ['Accounts Payable Days', '{:,.0f}'.format(accounts_payable_days), '{:,.0f}'.format(whatif_accounts_payable_days)]
#    df_balance_sheet.loc[15] = ['Accrued Expenses Payable', '{:,.0f}'.format(accrued_expenses_payable), '{:,.0f}'.format(whatif_accrued_expenses_payable)]
#    df_balance_sheet.loc[16] = ['Short Term Notes Payable', '{:,.0f}'.format(short_term_notes_payable), '{:,.0f}'.format(whatif_short_term_notes_payable)]
#    df_balance_sheet.loc[17] = ['Other Short Term Liabilities', '{:,.0f}'.format(other_short_term_liabilities), '{:,.0f}'.format(whatif_other_short_term_liabilities)]
#    df_balance_sheet.loc[18] = ['Total Current Liabilities', '{:,.0f}'.format(total_current_liabilities), '{:,.0f}'.format(whatif_total_current_liabilities)]
#    df_balance_sheet.loc[19] = ['Long Term Notes Payable', '{:,.0f}'.format(long_term_notes_payable), '{:,.0f}'.format(whatif_long_term_notes_payable)]
#    df_balance_sheet.loc[20] = ['Other Long Term Liabilities', '{:,.0f}'.format(other_long_term_liabilities), '{:,.0f}'.format(whatif_other_long_term_liabilities)]
#    df_balance_sheet.loc[21] = ['Total Non Current Liabilities', '{:,.0f}'.format(total_non_current_liabilities), '{:,.0f}'.format(whatif_total_non_current_liabilities)]
#    df_balance_sheet.loc[22] = ['Total Liabilities', '{:,.0f}'.format(total_liabilities), '{:,.0f}'.format(whatif_total_liabilities)]
#    df_balance_sheet.loc[23] = ['Capital Stock', '{:,.0f}'.format(capital_stock), '{:,.0f}'.format(whatif_capital_stock)]
#    df_balance_sheet.loc[24] = ['Retained Earnings', '{:,.0f}'.format(retained_earnings), '{:,.0f}'.format(whatif_retained_earnings)]
#    df_balance_sheet.loc[25] = ['Adjustments', '{:,.0f}'.format(adjustments), '{:,.0f}'.format(whatif_adjustments)]
#    df_balance_sheet.loc[26] = ['Total Shareholders Equity', '{:,.0f}'.format(total_shareholders_equity), '{:,.0f}'.format(whatif_total_shareholders_equity)]
#    df_balance_sheet.loc[27] = ['Balance Check', '{:,.0f}'.format(balance_check), '{:,.0f}'.format(whatif_balance_check)]

    df_balance_sheet.loc[0] = ['Cash & Short Term Investments', '{:,.0f}'.format(cash_and_short_term_investments), '{:,.0f}'.format(whatif_cash_and_short_term_investments)]
    df_balance_sheet.loc[1] = ['Accounts Receivable', '{:,.0f}'.format(accounts_receivable), '{:,.0f}'.format(whatif_accounts_receivable)]
    df_balance_sheet.loc[2] = ['Accounts Receivable Days', '{:,.0f}'.format(accounts_receivable_days), '{:,.0f}'.format(whatif_accounts_receivable_days)]
    df_balance_sheet.loc[3] = ['Inventory', '{:,.0f}'.format(inventory), '{:,.0f}'.format(whatif_inventory)]
    df_balance_sheet.loc[4] = ['Inventory Days', '{:,.0f}'.format(inventory_days), '{:,.0f}'.format(whatif_inventory_days)]
    df_balance_sheet.loc[5] = ['Other Current Assets', '{:,.0f}'.format(other_current_assets), '{:,.0f}'.format(whatif_other_current_assets)]
    df_balance_sheet.loc[6] = ['Total Current Assets', '{:,.0f}'.format(total_current_assets), '{:,.0f}'.format(whatif_total_current_assets)]
    df_balance_sheet.loc[7] = ['Property, Plant & Equipment', '{:,.0f}'.format(property_plant_and_equipment), '{:,.0f}'.format(whatif_property_plant_and_equipment)]
    df_balance_sheet.loc[8] = ['Accumulated Depreciation', '{:,.0f}'.format(-accumulated_depreciation), '{:,.0f}'.format(-whatif_accumulated_depreciation)]
    df_balance_sheet.loc[9] = ['Net Fixed Assets', '{:,.0f}'.format(net_fixed_assets), '{:,.0f}'.format(whatif_net_fixed_assets)]
    df_balance_sheet.loc[10] = ['Intangible Assets', '{:,.0f}'.format(intangible_assets), '{:,.0f}'.format(whatif_intangible_assets)]
    df_balance_sheet.loc[11] = ['Total Other Assets', '{:,.0f}'.format(total_other_assets), '{:,.0f}'.format(whatif_total_other_assets)]
    df_balance_sheet.loc[12] = ['Total Assets', '{:,.0f}'.format(total_assets), '{:,.0f}'.format(whatif_total_assets)]
    df_balance_sheet.loc[13] = ['Accounts Payable', '{:,.0f}'.format(accounts_payable), '{:,.0f}'.format(whatif_accounts_payable)]
    df_balance_sheet.loc[14] = ['Accounts Payable Days', '{:,.0f}'.format(accounts_payable_days), '{:,.0f}'.format(whatif_accounts_payable_days)]
    df_balance_sheet.loc[15] = ['Short Term Notes Payable', '{:,.0f}'.format(short_term_notes_payable), '{:,.0f}'.format(whatif_short_term_notes_payable)]
    df_balance_sheet.loc[16] = ['Other Short Term Liabilities', '{:,.0f}'.format(other_short_term_liabilities), '{:,.0f}'.format(whatif_other_short_term_liabilities)]
    df_balance_sheet.loc[17] = ['Total Current Liabilities', '{:,.0f}'.format(total_current_liabilities), '{:,.0f}'.format(whatif_total_current_liabilities)]
    df_balance_sheet.loc[18] = ['Long Term Notes Payable', '{:,.0f}'.format(long_term_notes_payable), '{:,.0f}'.format(whatif_long_term_notes_payable)]
    df_balance_sheet.loc[19] = ['Other Long Term Liabilities', '{:,.0f}'.format(other_long_term_liabilities), '{:,.0f}'.format(whatif_other_long_term_liabilities)]
    df_balance_sheet.loc[20] = ['Total Non Current Liabilities', '{:,.0f}'.format(total_non_current_liabilities), '{:,.0f}'.format(whatif_total_non_current_liabilities)]
    df_balance_sheet.loc[21] = ['Total Liabilities', '{:,.0f}'.format(total_liabilities), '{:,.0f}'.format(whatif_total_liabilities)]
    df_balance_sheet.loc[22] = ['Stock Value', '{:,.0f}'.format(stock_value), '{:,.0f}'.format(whatif_stock_value)]
    df_balance_sheet.loc[23] = ['Retained Earnings', '{:,.0f}'.format(retained_earnings), '{:,.0f}'.format(whatif_retained_earnings)]
    df_balance_sheet.loc[24] = ['Capital Stock', '{:,.0f}'.format(capital_stock), '{:,.0f}'.format(whatif_capital_stock)]
    df_balance_sheet.loc[25] = ['Other Equity', '{:,.0f}'.format(other_equity), '{:,.0f}'.format(whatif_other_equity)]
    df_balance_sheet.loc[26] = ['Adjustments', '{:,.0f}'.format(adjustments), '{:,.0f}'.format(whatif_adjustments)]
    df_balance_sheet.loc[27] = ['Total Shareholders Equity', '{:,.0f}'.format(total_shareholders_equity), '{:,.0f}'.format(whatif_total_shareholders_equity)]
    df_balance_sheet.loc[28] = ['Balance Check', '{:,.0f}'.format(balance_check), '{:,.0f}'.format(whatif_balance_check)]

    return df_income_statement , df_cash_flow_statement, df_balance_sheet


@st.cache_data(show_spinner=False)
def run_simulation(select_user_seed_value, select_user_sector, select_user_field_names, select_user_manual_names, select_user_iterations, select_user_whatif_sim_sales_revenue_growth, select_user_whatif_sim_cost_of_goods_sold_margin, select_user_whatif_sim_sales_general_and_admin_expenses, select_user_whatif_sim_research_and_development_expenses, select_user_whatif_sim_depreciation_and_amortization_expenses_sales, select_user_whatif_sim_depreciation_and_amortization_split, select_user_whatif_sim_interest_rate, select_user_whatif_sim_tax_rate, select_user_whatif_sim_dividend_payout_ratio, select_user_whatif_sim_accounts_receivable_days, select_user_whatif_sim_inventory_days, select_user_whatif_sim_capital_expenditure_sales, select_user_whatif_sim_capital_expenditure, select_user_whatif_sim_capital_expenditure_indicator, select_user_whatif_sim_tangible_intangible_split, select_user_whatif_sim_accounts_payable_days, select_user_whatif_sim_sale_of_equity, select_user_whatif_sim_repurchase_of_equity, select_user_whatif_sim_proceeds_from_issuance_of_debt, select_user_whatif_sim_repayments_of_long_term_debt, select_user_whatif_sim_notes_other_split):

#    select_user_whatif_sim_sales_revenue_growth_ind = False
#    select_user_whatif_sim_cost_of_goods_sold_margin_ind = False
#    select_user_whatif_sim_depreciation_and_amortization_expenses_sales_ind = False
#    select_user_whatif_sim_accounts_receivable_days_ind = False
#    select_user_whatif_sim_inventory_days_ind = False
#    select_user_whatif_sim_capital_expenditure_sales_ind = False
#    select_user_whatif_sim_accounts_payable_days_ind = False
    np.random.seed(select_user_seed_value)
    st.write("")
    progress = st.empty()
    setup_text = st.empty()
#    setup_text = st.markdown(
#        '<p style="margin-bottom: 0px ;"><span style="font-family:sans-serif; color:#6f72de; font-size: 24px; ">Preparing Simulation ...</span></p>',
#        unsafe_allow_html=True)

#    st.markdown("""
#    <style>
#        @keyframes slide-in {
#          from {
#            transform: translateX(-100vw);
#          }
#          to {
#            transform: translateX(100vw);
#          }
#        }
    
#        .animate-text {
#            display: inline-block;
#            animation-name: slide-in;
#            animation-duration: 10s;
#            animation-timing-function: linear;
#            animation-fill-mode: forwards;
#            animation-delay: 1s;
#            animation-iteration-count: infinite;
#        }
#    </style>
#    """, unsafe_allow_html=True)
#    st.markdown("""
#    <style>
#        body {
#            margin-bottom: 0;
#        }
#    </style>
#    """, unsafe_allow_html=True)

#    setup_text = st.markdown("<span class='animate-text' style='font-family:sans-serif; color:#7983FF; font-size: 40px;'>... Preparing Simulation ...</span>", unsafe_allow_html=True)

    spinner = st.markdown(marker_spinner_css, unsafe_allow_html=True)
    spinner_image = st.markdown(spinner_image_css.format(img_to_bytes("images/spinner_center.png")), unsafe_allow_html=True)
    def get_financials(datafame, user_entity_name, user_period):
        entity_financials = datafame.loc[
            (datafame['entity_name'] == user_entity_name) & (datafame['period'] == user_period)]
        return entity_financials

    def get_sector_financials(datafame, user_sector):
        sector_financials = datafame.loc[
            (datafame['sector'] == user_sector)]
        return sector_financials

    def get_entity_financials(datafame, user_entity_name):
        entity_financials = datafame.loc[
            (datafame['entity_name'] == user_entity_name)]
        entity_financials = entity_financials.sort_values(by=['period'], ascending=True)
        return entity_financials

    df_sector_financials = get_sector_financials(st.session_state.df_input, select_user_sector)


    def generate_correlated_values(dataframe, field_names, iterations):
        df_financials = dataframe[['period', 'entity_name', 'sales', 'cost_of_goods_sold_incl_depreciation_amortization', 'depreciation_amortization', 'total_receivables', 'inventory', 'capex_fixed_assets', 'accounts_payable']]

        df_financials_update = pd.DataFrame()
        entity_list = sorted(df_financials['entity_name'].apply(str).unique())
        for entity in entity_list:
            df_entity_financials = pd.DataFrame(get_entity_financials(df_financials, entity))
            df_entity_financials['Sales Growth %'] = df_entity_financials['sales'].pct_change() * 100
            df_financials_update = pd.concat([df_financials_update, df_entity_financials])

        df_financials_update['COGS Margin %'] = df_financials_update['cost_of_goods_sold_incl_depreciation_amortization'] / df_financials_update['sales'] * 100
        df_financials_update['D&A Expenses / Sales %'] = df_financials_update['depreciation_amortization'] / df_financials_update['sales'] * 100
        df_financials_update['Accounts Receivable Days'] = df_financials_update['total_receivables'] / df_financials_update['sales'] * 365
        df_financials_update['Inventory Days'] = df_financials_update['inventory'] / df_financials_update['cost_of_goods_sold_incl_depreciation_amortization'] * 365
        df_financials_update['Capital Expenditure / Sales %'] = df_financials_update['capex_fixed_assets'] / df_financials_update['sales'] * 100
        df_financials_update['Accounts Payable Days'] = df_financials_update['accounts_payable'] / df_financials_update['cost_of_goods_sold_incl_depreciation_amortization'] * 365

        df_financials_update = df_financials_update[['Sales Growth %', 'COGS Margin %', 'D&A Expenses / Sales %', 'Accounts Receivable Days', 'Inventory Days', 'Capital Expenditure / Sales %', 'Accounts Payable Days']]
        df_financials_update.dropna(inplace=True)
        df_financials_update = df_financials_update[np.isfinite(df_financials_update).all(1)]

        df_financials_update_normal = pd.DataFrame()
        for name in field_names:
            df_financials_update_normal[name] = pd.DataFrame(norm.ppf((df_financials_update[name].rank(ascending=True) - 0.5) / len(df_financials_update[name])))

        correlation_matrix = df_financials_update_normal[field_names].corr(method="pearson")
        cholesky_matrix = sclinalg.cholesky(correlation_matrix, lower=True)

        df_financials_update_random_normal = pd.DataFrame()
        for name in field_names:
            df_financials_update_random_normal[name] = pd.DataFrame(np.random.standard_normal(size=iterations))

        df_financials_update_correlated_normal = pd.DataFrame((np.matmul(cholesky_matrix, df_financials_update_random_normal.transpose())).transpose())
        df_financials_update_correlated_uniform = pd.DataFrame(norm.cdf(df_financials_update_correlated_normal))
        df_financials_update_correlated_uniform.columns = field_names

        df_financials_update_correlated_variables = pd.DataFrame()
        for name in field_names:
            df_name = df_financials_update[name].drop_duplicates()
            q25, q75 = nanpercentile(df_name, 25), nanpercentile(df_name, 75)
            iqr = q75 - q25
            cutoff = iqr * 1.5
            lower, upper = q25 - cutoff, q75 + cutoff
            df_name = df_name[(df_name > lower) & (df_name < upper)]
            df_cdf = pd.DataFrame(np.sort(df_name))
            df_x = pd.DataFrame((df_cdf.rank(ascending=True) - 0.5) / len(df_cdf))
            interp_func = UnivariateSpline(df_x, df_cdf)
            df_financials_update_correlated_variables[name] = pd.DataFrame(interp_func(df_financials_update_correlated_uniform[name]))
        df_financials_mean = pd.DataFrame(np.mean(df_financials_update_correlated_variables), columns=['Mean'])
        df_financials_mean["Field"] = field_names
        df_financials_mean = df_financials_mean[['Field', 'Mean']]

        return df_financials_update_correlated_variables, df_financials_mean

    correlated_variables, mean_values = generate_correlated_values(df_sector_financials, select_user_field_names, select_user_iterations)

    field_options = ["Sales Growth %", "COGS Margin %", "SG&A Expenses $", "R&D Expenses $", "D&A Expenses / Sales %",
                     "D&A Split %", "Interest Rate %", "Tax Rate %", "Dividend Payout Ratio %",
                     "Accounts Receivable Days", "Inventory Days", "Capital Expenditure / Sales %",
                     "Capital Expenditure $", "Capital Expenditure Type", "Capex Tangible / Intangible Split %",
                     "Accounts Payable Days", "Sale of Equity $", "Repurchase of Equity $",
                     "Proceeds from Issuance of Debt $", "Repayments of Long Term Debt $", "Notes / Other Split %"]
    field_names_alt = ["user_whatif_sim_sales_revenue_growth", "user_whatif_sim_cost_of_goods_sold_margin",
                       "user_whatif_sim_sales_general_and_admin_expenses",
                       "user_whatif_sim_research_and_development_expenses",
                       "user_whatif_sim_depreciation_and_amortization_expenses_sales",
                       "user_whatif_sim_depreciation_and_amortization_split", "user_whatif_sim_interest_rate",
                       "user_whatif_sim_tax_rate", "user_whatif_sim_dividend_payout_ratio",
                       "user_whatif_sim_accounts_receivable_days", "user_whatif_sim_inventory_days",
                       "user_whatif_sim_capital_expenditure_sales", "user_whatif_sim_capital_expenditure",
                       "user_whatif_sim_capital_expenditure_indicator", "user_whatif_sim_tangible_intangible_split",
                       "user_whatif_sim_accounts_payable_days", "user_whatif_sim_sale_of_equity",
                       "user_whatif_sim_repurchase_of_equity", "user_whatif_sim_proceeds_from_issuance_of_debt",
                       "user_whatif_sim_repayments_of_long_term_debt", "user_whatif_sim_notes_other_split"]
    select_field_names = ["select_user_whatif_sim_sales_revenue_growth",
                          "select_user_whatif_sim_cost_of_goods_sold_margin",
                          "select_user_whatif_sim_sales_general_and_admin_expenses",
                          "select_user_whatif_sim_research_and_development_expenses",
                          "select_user_whatif_sim_depreciation_and_amortization_expenses_sales",
                          "select_user_whatif_sim_depreciation_and_amortization_split",
                          "select_user_whatif_sim_interest_rate",
                          "select_user_whatif_sim_tax_rate", "select_user_whatif_sim_dividend_payout_ratio",
                          "select_user_whatif_sim_accounts_receivable_days", "select_user_whatif_sim_inventory_days",
                          "select_user_whatif_sim_capital_expenditure_sales",
                          "select_user_whatif_sim_capital_expenditure",
                          "select_user_whatif_sim_capital_expenditure_indicator",
                          "select_user_whatif_sim_tangible_intangible_split",
                          "select_user_whatif_sim_accounts_payable_days", "select_user_whatif_sim_sale_of_equity",
                          "select_user_whatif_sim_repurchase_of_equity",
                          "select_user_whatif_sim_proceeds_from_issuance_of_debt",
                          "select_user_whatif_sim_repayments_of_long_term_debt",
                          "select_user_whatif_sim_notes_other_split"]

    df_income_statement_sim_out = pd.DataFrame()
    df_cash_flow_statement_sim_out = pd.DataFrame()
    df_balance_sheet_statement_sim_out = pd.DataFrame()
    new_colnames = []
    st.markdown("""<style> .stProgress > div > div > div {border: 3px solid #25476A !important; background-color: rgba(0, 0, 0, 0) !important; border-radius: 2px !important; height: 20px !important; margin-bottom: 0px !important; margin-top: 0px !important;} .stProgress > div > div > div > div {border-radius: 2px !important; background-color: #6f72de !important;}</style>""",
                unsafe_allow_html=True)
    progress.progress(0)
    spinner.empty()
    spinner_image.empty()

#    defaults = {
#        "Sales Growth %": select_user_whatif_sim_sales_revenue_growth,
#        "COGS Margin %": select_user_whatif_sim_cost_of_goods_sold_margin,
#        "D&A Expenses / Sales %": select_user_whatif_sim_depreciation_and_amortization_expenses_sales,
#        "Accounts Receivable Days": select_user_whatif_sim_accounts_receivable_days,
#        "Inventory Days": select_user_whatif_sim_inventory_days,
#        "Capital Expenditure / Sales %": select_user_whatif_sim_capital_expenditure_sales,
#        "Accounts Payable Days": select_user_whatif_sim_accounts_payable_days
#    }

#    defaults = {k: v for k, v in defaults.items() if not pd.isna(v)}

#    timer_start = time.perf_counter()
    for i in range(0, select_user_iterations, 1):
        setup_text.markdown('<p style="margin-bottom: 0px;"><span style="font-family:sans-serif; color:#6f72de; font-size: 24px;">%s</span></p>' %('Running Simulation: Iteration '+str('{:,.0f}'.format(i+1))+' of '+str('{:,.0f}'.format(select_user_iterations))), unsafe_allow_html=True)
        progress.progress((i+1)/select_user_iterations)
        df_iter = correlated_variables.iloc[i]

#        select_user_whatif_sim_sales_revenue_growth = defaults.get("Sales Growth %", df_iter["Sales Growth %"])
#        select_user_whatif_sim_cost_of_goods_sold_margin = defaults.get("COGS Margin %", df_iter["COGS Margin %"])
#        select_user_whatif_sim_depreciation_and_amortization_expenses_sales = defaults.get("D&A Expenses / Sales %",
#                                                                                           df_iter[
#                                                                                               "D&A Expenses / Sales %"])
#        select_user_whatif_sim_accounts_receivable_days = defaults.get("Accounts Receivable Days",
#                                                                       df_iter["Accounts Receivable Days"])
#        select_user_whatif_sim_inventory_days = defaults.get("Inventory Days", df_iter["Inventory Days"])
#        select_user_whatif_sim_capital_expenditure_sales = defaults.get("Capital Expenditure / Sales %",
#                                                                        df_iter["Capital Expenditure / Sales %"])
#        select_user_whatif_sim_accounts_payable_days = defaults.get("Accounts Payable Days",
#                                                                    df_iter["Accounts Payable Days"])
        if "Sales Growth %" in select_user_field_names:
            select_user_whatif_sim_sales_revenue_growth = df_iter["Sales Growth %"] - mean_values.loc[(mean_values['Field'] == "Sales Growth %"), 'Mean'].values[0] + st.session_state.default_whatif_sales_revenue_growth_user_out
        if "COGS Margin %" in select_user_field_names:
            select_user_whatif_sim_cost_of_goods_sold_margin = df_iter["COGS Margin %"] - mean_values.loc[(mean_values['Field'] == "COGS Margin %"), 'Mean'].values[0] + st.session_state.default_whatif_cost_of_goods_sold_margin_user_out
        if "D&A Expenses / Sales %" in select_user_field_names:
            select_user_whatif_sim_depreciation_and_amortization_expenses_sales = df_iter["D&A Expenses / Sales %"] - mean_values.loc[(mean_values['Field'] == "D&A Expenses / Sales %"), 'Mean'].values[0] + st.session_state.default_whatif_depreciation_and_amortization_expenses_sales_user_out
        if "Accounts Receivable Days" in select_user_field_names:
            select_user_whatif_sim_accounts_receivable_days = df_iter["Accounts Receivable Days"] - mean_values.loc[(mean_values['Field'] == "Accounts Receivable Days"), 'Mean'].values[0] + st.session_state.default_whatif_accounts_receivable_days_user_out
        if "Inventory Days" in select_user_field_names:
            select_user_whatif_sim_inventory_days = df_iter["Inventory Days"] - mean_values.loc[(mean_values['Field'] == "Inventory Days"), 'Mean'].values[0] + st.session_state.default_whatif_inventory_days_user_out
        if "Capital Expenditure / Sales %" in select_user_field_names:
            select_user_whatif_sim_capital_expenditure_sales = df_iter["Capital Expenditure / Sales %"] - mean_values.loc[(mean_values['Field'] == "Capital Expenditure / Sales %"), 'Mean'].values[0] + st.session_state.default_whatif_capital_expenditure_sales_user_out
        if "Accounts Payable Days" in select_user_field_names:
            select_user_whatif_sim_accounts_payable_days = df_iter["Accounts Payable Days"] - mean_values.loc[(mean_values['Field'] == "Accounts Payable Days"), 'Mean'].values[0] + st.session_state.default_whatif_accounts_payable_days_user_out

#        try:
#            select_user_whatif_sim_sales_revenue_growth = df_iter["Sales Growth %"] #- mean_values["Sales Growth %"].values[0] / 100
#        except:
#            select_user_whatif_sim_sales_revenue_growth = select_user_whatif_sim_sales_revenue_growth
#        try:
#            select_user_whatif_sim_cost_of_goods_sold_margin = df_iter["COGS Margin %"]
#        except:
#            select_user_whatif_sim_cost_of_goods_sold_margin = select_user_whatif_sim_cost_of_goods_sold_margin
#        try:
#            select_user_whatif_sim_depreciation_and_amortization_expenses_sales = df_iter["D&A Expenses / Sales %"]
#        except:
#            select_user_whatif_sim_depreciation_and_amortization_expenses_sales = select_user_whatif_sim_depreciation_and_amortization_expenses_sales
#        try:
#            select_user_whatif_sim_accounts_receivable_days = df_iter["Accounts Receivable Days"]
#        except:
#            select_user_whatif_sim_accounts_receivable_days = select_user_whatif_sim_accounts_receivable_days
#        try:
#            select_user_whatif_sim_inventory_days = df_iter["Inventory Days"]
#        except:
#            select_user_whatif_sim_inventory_days = select_user_whatif_sim_inventory_days
#        try:
#            select_user_whatif_sim_capital_expenditure_sales = df_iter["Capital Expenditure / Sales %"]
#        except:
#            select_user_whatif_sim_capital_expenditure_sales = select_user_whatif_sim_capital_expenditure_sales
#        try:
#            select_user_whatif_sim_accounts_payable_days = df_iter["Accounts Payable Days"]
#        except:
#            select_user_whatif_sim_accounts_payable_days = select_user_whatif_sim_accounts_payable_days

#        if "Sales Growth %" in select_user_field_names:
#        if np.isnan(select_user_whatif_sim_sales_revenue_growth) or select_user_whatif_sim_sales_revenue_growth_ind == True:
#            select_user_whatif_sim_sales_revenue_growth_ind = True
#            select_user_whatif_sim_sales_revenue_growth = df_iter["Sales Growth %"]
#        if "COGS Margin %" in select_user_field_names:
#        if np.isnan(select_user_whatif_sim_cost_of_goods_sold_margin) or select_user_whatif_sim_cost_of_goods_sold_margin_ind == True:
#            select_user_whatif_sim_cost_of_goods_sold_margin_ind = True
#            select_user_whatif_sim_cost_of_goods_sold_margin = df_iter["COGS Margin %"]
#        if "D&A Expenses / Sales %" in select_user_field_names:
#        if np.isnan(select_user_whatif_sim_depreciation_and_amortization_expenses_sales) or select_user_whatif_sim_depreciation_and_amortization_expenses_sales_ind == True:
#            select_user_whatif_sim_depreciation_and_amortization_expenses_sales_ind = True
#            select_user_whatif_sim_depreciation_and_amortization_expenses_sales = df_iter["D&A Expenses / Sales %"]
#        if "Accounts Receivable Days" in select_user_field_names:
#        if np.isnan(select_user_whatif_sim_accounts_receivable_days) or select_user_whatif_sim_accounts_receivable_days_ind == True:
#            select_user_whatif_sim_accounts_receivable_days_ind = True
#            select_user_whatif_sim_accounts_receivable_days = df_iter["Accounts Receivable Days"]
#        if "Inventory Days" in select_user_field_names:
#        if np.isnan(select_user_whatif_sim_inventory_days) or select_user_whatif_sim_inventory_days_ind == True:
#            select_user_whatif_sim_inventory_days_ind = True
#            select_user_whatif_sim_inventory_days = df_iter["Inventory Days"]
#        if "Capital Expenditure / Sales %" in select_user_field_names:
#        if np.isnan(select_user_whatif_sim_capital_expenditure_sales) or select_user_whatif_sim_capital_expenditure_sales_ind == True:
#            select_user_whatif_sim_capital_expenditure_sales_ind = True
#            select_user_whatif_sim_capital_expenditure_sales = df_iter["Capital Expenditure / Sales %"]
#        if "Accounts Payable Days" in select_user_field_names:
#        if np.isnan(select_user_whatif_sim_accounts_payable_days) or select_user_whatif_sim_accounts_payable_days_ind == True:
#            select_user_whatif_sim_accounts_payable_days_ind = True
#            select_user_whatif_sim_accounts_payable_days = df_iter["Accounts Payable Days"]

#        for name in select_user_field_names:
#            globals()[select_field_names[field_options.index(name)]] = df_iter[name]

        df_income_statement_iter_out, df_cash_flow_statement_iter_out, df_balance_sheet_statement_iter_out = run_whatif(
            select_user_entity_name=st.session_state.user_entity_name,
            select_user_period=st.session_state.user_reporting_period,
            select_user_whatif_sales_revenue_growth=select_user_whatif_sim_sales_revenue_growth,
            select_user_whatif_cost_of_goods_sold_margin=select_user_whatif_sim_cost_of_goods_sold_margin,
            select_user_whatif_sales_general_and_admin_expenses=select_user_whatif_sim_sales_general_and_admin_expenses,
            select_user_whatif_research_and_development_expenses=select_user_whatif_sim_research_and_development_expenses,
            select_user_whatif_depreciation_and_amortization_expenses_sales=select_user_whatif_sim_depreciation_and_amortization_expenses_sales,
            select_user_whatif_depreciation_and_amortization_split=select_user_whatif_sim_depreciation_and_amortization_split,
            select_user_whatif_interest_rate=select_user_whatif_sim_interest_rate,
            select_user_whatif_tax_rate=select_user_whatif_sim_tax_rate,
            select_user_whatif_dividend_payout_ratio=select_user_whatif_sim_dividend_payout_ratio,
            select_user_whatif_accounts_receivable_days=select_user_whatif_sim_accounts_receivable_days,
            select_user_whatif_inventory_days=select_user_whatif_sim_inventory_days,
            select_user_whatif_capital_expenditure_sales=select_user_whatif_sim_capital_expenditure_sales,
            select_user_whatif_capital_expenditure=select_user_whatif_sim_capital_expenditure,
            select_user_whatif_capital_expenditure_indicator=select_user_whatif_sim_capital_expenditure_indicator,
            select_user_whatif_tangible_intangible_split=select_user_whatif_sim_tangible_intangible_split,
            select_user_whatif_accounts_payable_days=select_user_whatif_sim_accounts_payable_days,
            select_user_whatif_sale_of_equity=select_user_whatif_sim_sale_of_equity,
            select_user_whatif_repurchase_of_equity=select_user_whatif_sim_repurchase_of_equity,
            select_user_whatif_proceeds_from_issuance_of_debt=select_user_whatif_sim_proceeds_from_issuance_of_debt,
            select_user_whatif_repayments_of_long_term_debt=select_user_whatif_sim_repayments_of_long_term_debt,
            select_user_whatif_notes_other_split=select_user_whatif_sim_notes_other_split)

        new_colnames.append('Iter '+str(i+1))
#        df_income_statement_sim_out[i] = df_income_statement_iter_out.iloc[:,2].copy()
#        df_cash_flow_statement_sim_out[i] = df_cash_flow_statement_iter_out.iloc[:, 2].copy()
#        df_balance_sheet_statement_sim_out[i] = df_balance_sheet_statement_iter_out.iloc[:, 2].copy()

        df_income_statement_sim_out = pd.concat([df_income_statement_sim_out, df_income_statement_iter_out.iloc[:,2].copy()], axis=1)
        df_cash_flow_statement_sim_out = pd.concat([df_cash_flow_statement_sim_out, df_cash_flow_statement_iter_out.iloc[:, 2].copy()],
                                                axis=1)
        df_balance_sheet_statement_sim_out = pd.concat([df_balance_sheet_statement_sim_out, df_balance_sheet_statement_iter_out.iloc[:, 2].copy()],
                                                axis=1)

    df_income_statement_sim_out.columns = new_colnames
    df_cash_flow_statement_sim_out.columns = new_colnames
    df_balance_sheet_statement_sim_out.columns = new_colnames
    df_income_statement_sim_out = pd.concat([df_income_statement_iter_out.iloc[:, 0:2], df_income_statement_sim_out], axis=1)
    df_cash_flow_statement_sim_out = pd.concat([df_cash_flow_statement_iter_out.iloc[:, 0:2], df_cash_flow_statement_sim_out],
                                            axis=1)
    df_balance_sheet_statement_sim_out = pd.concat([df_balance_sheet_statement_iter_out.iloc[:, 0:2], df_balance_sheet_statement_sim_out],
                                            axis=1)
    
    df_income_statement_sim_save = df_income_statement_sim_out.copy()
    df_cash_flow_statement_sim_save = df_cash_flow_statement_sim_out.copy()
    df_balance_sheet_statement_sim_save = df_balance_sheet_statement_sim_out.copy()

    currency = get_financials(st.session_state.df_input, st.session_state.user_entity_name, st.session_state.user_reporting_period)['currency_iso'].values[0]

    df_income_statement_sim_save[st.session_state.user_entity_name+" ("+currency+ " Millions)"] = df_income_statement_sim_save[st.session_state.user_entity_name+" ("+currency+ " Millions)"].map(st.session_state.df_field_name_mapping.set_index('field_name')['comrate_field_name'])
    df_cash_flow_statement_sim_save[st.session_state.user_entity_name+" ("+currency+ " Millions)"] = df_cash_flow_statement_sim_save[st.session_state.user_entity_name+" ("+currency+ " Millions)"].map(st.session_state.df_field_name_mapping.set_index('field_name')['comrate_field_name'])
    df_balance_sheet_statement_sim_save[st.session_state.user_entity_name+" ("+currency+ " Millions)"] = df_balance_sheet_statement_sim_save[st.session_state.user_entity_name+" ("+currency+ " Millions)"].map(st.session_state.df_field_name_mapping.set_index('field_name')['comrate_field_name'])

#    timer_stop = time.perf_counter()
#    st.write(f"{timer_stop - timer_start:0.4f} seconds")
    progress.empty()
    setup_text.empty()

    ratings = np.random.normal(10, 5, select_user_iterations)
    categories = [(-float("inf"), 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21), (21, float("inf"))]
    labels = ['AAA', 'AA+', 'AA', 'AA-', 'A+', 'A', 'A-', 'BBB+', 'BBB', 'BBB-', 'BB+', "BB", 'BB-', 'B+', 'B', 'B-', 'CCC+', 'CCC', 'CCC-', 'CC', 'C', 'D']
    ordinal_ratings = [labels[next(i for i, c in enumerate(categories) if c[0] <= r <= c[1])] for r in ratings]
    ratings_sim_out = pd.DataFrame(ordinal_ratings, columns=['Credit Rating'])
    num_rows = len(ratings_sim_out.index)
    ratings_sim_out = ratings_sim_out.assign(new_col=["Iter" + str(i + 1) for i in range(num_rows)])
    ratings_sim_out.columns = ['Credit Rating', 'Iteration']
    ratings_sim_out = ratings_sim_out[['Iteration', 'Credit Rating']]

    df_income_statement_sim_save.to_csv(r'income_statement_out.csv', index=None, header=True)
    df_cash_flow_statement_sim_save.to_csv(
        r'cash_flow_statement_out.csv', index=None, header=True)
    df_balance_sheet_statement_sim_save.to_csv(
        r'balance_sheet_statement_out.csv', index=None, header=True)

    return ratings_sim_out, df_income_statement_sim_out, df_cash_flow_statement_sim_out, df_balance_sheet_statement_sim_out

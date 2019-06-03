"""
 * Copyright 2018 University of Liverpool
 * Author: John Heap, Computational Biology Facility, UoL
 * Based on original scripts of Sara Silva Pereira, Institute of Infection and Global Health, UoL
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 """
#import subprocess
#import re
import os
import sys
#import pandas as pd
#import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
#from matplotlib.mlab import PCA
import Tryp_G
import Tryp_T
import Tryp_V
import Tryp_V_T
import argparse
#Entry .sort out the arguments

pdfExport = False
#parser = argparse.ArgumentParser(description='Variant Antigen Profiler - the VAP.')
#parser.add_argument('name')
#parser.add_argument('-t','-T', action = 'store_true', default = False, help = "Transciptomic Pathway")
#parser.add_argument('-p','-P', action = 'store_true', default = False, help = "Export PDFs to HTML directory")
#parser.add_argument('strain')
#parser.add_argument('Forward_Read_File')
#parser.add_argument('Reverse_Read_File')
#parser.add_argument('htmlfile')
#parser.add_argument('htmlresource')
#parser.add_argument('heatmapFile')
#parser.add_argument('PCAFile')
#parser.add_argument('devheatmapFile')
#args = parser.parse_args()

#we have numerous parameters....
#hard code it for differnt types?


arguments = sys.argv
htmldir = arguments[len(arguments)-1]   #last argument is always html_resource
if not os.path.exists(htmldir):
    os.mkdir(htmldir)

if arguments[1] == 'g_assemble':
    argdict = {'name':2, 'pdfexport':3, 'kmers':4,'inslen':5, 'covcut':6, 'forward':7, 'reverse':8, 'html_file':9, 'html_resource':10}
    Tryp_G.assemble(arguments,argdict)
if arguments[1] == 'g_contigs':
    argdict = {'name':2, 'pdfexport':3, 'contigs':4, 'html_file':5, 'html_resource':6}
    Tryp_G.contigs(arguments,argdict)
if arguments[1] == 'transcipt':
    argdict = {'name':2, 'pdfexport': 3, 'strain': 4, 'forward': 5, 'reverse': 6, 'html_file': 7, 'html_resource': 8}
    Tryp_T.transcriptomicProcess(arguments,argdict)
if arguments[1] == 'v_assemble':
    argdict = {'name':2, 'pdfexport':3, 'kmers':4,'inslen':5, 'covcut':6, 'forward':7, 'reverse':8, 'html_file':9, 'html_resource':10}
    Tryp_V.vivax_assemble(arguments,argdict)
if arguments[1] == 'v_contigs':
    argdict = {'name':2, 'pdfexport':3, 'contigs':4, 'html_file':5, 'html_resource':6}
    Tryp_V.vivax_contigs(arguments,argdict)
if arguments[1] == 'v_transcript':
    argdict = {'name':2, 'pdfexport': 3, 'refFastq': 4, 'forward': 5, 'reverse': 6, 'html_file': 7, 'html_resource': 8}
    Tryp_V_T.transcriptomicProcess(arguments,argdict)


sys.exit()


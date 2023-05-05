# SillyTavernAutoExpressions

SillyTavernAutoExpressions is a simple Python script that automates the process of creating and populating character expression folders in the public\characters directory of SillyTavern. 

## Installation

To use, simply place DefaultExpressionsFromCard.py in the public\characters directory of SillyTavern. 

## Usage

To use on all files in directory, open a cmd prompt in the characters directory and run 
```
python DefaultExpressionsFromCard.py --all
```

To use, drag and drop a valid Tavern character card PNG onto the DefaultExpressionsFromCard.py icon in Windows Explorer. The script will automatically create the character expression folder if it doesn't already exist, and populate any missing expressions by making copies of the original character image. The folder will be named after the character name extracted from the card. 

Alternatively, if you want to use a different image that is not a Tavern character card, copy DefaultExpressionsFromAnyImage.py to a folder named after the character. Then, drag any image onto the DefaultExpressionsFromAnyImage.py icon, and it will copy that image to all the expression images that do not already exist. 

If drag and dropping files is not working you can also open a cmd prompt from the directory containing the desired script and do:
```
python DefaultExpressionsFromCard.py yourCardFile.png
```
or:
```
python DefaultExpressionsFromAnyImage.py yourImageFile.png
```

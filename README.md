# Master Function GLM Populator

## Project Description
This script is developed to create GridLAB-D objects individually. For the sake of simplicity, the script is built based on functions where each function is dedicated to one object. Furthermore, each function has its own arguments depending on the object. For example, triplex_load object in GridLAB-D tends to have triplex_line connected to it. As a result, the name of the triplex_line SHALL be provided when calling triplex_load function. However, other parameters tend to be constant. For example, triplex_load object tend to have 120V per phase. Thus, the voltage value is already assigned and does not need to be called. To understand what arguments need to be provided to each function, all we need to do is to look at the function arguments. It’s worth noting that each argument must be passed as a string. Otherwise, a syntax error will be produced when running the script.

**NOTE:** GridLAB-D has a limitation in the number of CSV files that can be opened at once, CSV profiles and recorder objects writing to CSV both count toward this limitation. The structure of the final GLM used in the PGE-GEL feeder model was modified to accommodate this limitation by halving the number of load profiles used for the simulation from 960 to 480. The 480 load profiles used in the simulation were distributed among the transformers originally paired with profiles 481-960 in a different order. The redistribution preserved the 50% EV penetration and one zero dryer profile per 8-house transformer while ensuring no transformer is loaded with the same eight load profiles as another. This modification was done using regular expressions in a text editor and is not reflected in this program.


## Requirements
```
pip install dateutil glm
```

### To get the code
```
git clone https://github.com/neighdeen84/Master_Function_GLM_Populator.git
```


## Usage
```
cd Master_Function_GLM_Populator
python main.py
```

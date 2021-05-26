# Master Function GLM Populator

## Project Description
This script is developed to create GridLAB-D objects individually. For the sake of simplicity, the script is built based on functions where each function is dedicated to one object. Furthermore, each function has its own arguments depending on the object. For example, triplex_load object in GridLAB-D tends to have triplex_line connected to it. As a result, the name of the triplex_line SHALL be provided when calling triplex_load function. However, other parameters tend to be constant. For example, triplex_load object tend to have 120V per phase. Thus, the voltage value is already assigned and does not need to be called. To understand what arguments need to be provided to each function, all we need to do is to look at the function arguments. It’s worth noting that each argument must be passed as a string. Otherwise, a syntax error will be produced when running the script.

**NOTE:** due to GridLAB-D's limitations at the number of CSVs that can be opened at once, the structure of the final GLM was modified to reflect that. 


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

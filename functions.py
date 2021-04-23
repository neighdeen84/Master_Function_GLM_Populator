import glm
import json
import random

def trip_load_with_player(name,phases,house_no,file):
	return "object triplex_load {\n"+f"\tname {name};\n"+ f"\tphases {phases};\n"+f"\tvoltage_1 120;\n"+f"\tvoltage_2 120;\n"+f"\tvoltage_N 0;\n"+f"\tnominal_voltage 120;\n"+"\tobject player {\n"+f"\t\tname House{house_no};\n"+f"\t\tfile {file}.csv;\n"+f"\t\tproperty constant_power_1;\n"+"\n\t};"+"\n}"



def player_obj(name,file):
    return "object player {\n" + f"\tname {name};\n" + f"\tfile \"{file}.csv\";\n"+"};"

def triplex_obj(name,phases,volt1, volt2,const_power,nominal):
    return "object triplex_load {\n"+ f"\tname {name};\n"+ f"\tphases {phases};\n" + f"\tvoltage_1 {volt1};\n" +f"\tvoltage_2 {volt2};\n"+\
           "\tvoltage_N 0;\n"+ f"\tconstant_power_1 {const_power};\n"+ f"\tnominal_voltage {nominal};\n"+"}"+'\n'
def triplex_line(name,From, to, phases, length, config):
    return "object triplex_line {\n"+f'\tname {name};\n'+f'\tfrom {From};\n'+f'\tto {to};\n'+f'\tphases {phases}S;\n\tlength {length};\n'+\
            f'\tconfiguration {config};'+'\n}\n'
def house(name,parent):
    return "object house {\n"+f'\tname {name};\n'+f'\tparent {parent};\n'+'}\n'

def powerflow_module(method, default,line_limits):
    return 'module powerflow{\n'+f"\tsolver_method {method};\n\tdefault_maximum_voltage_error {default};\n\tline_limits {line_limits};\n"+'};'
def residential_module(name,implicit,ansi):
    return 'module residential {\n'+f"\timplicit_enduses {implicit};\n"+f"\tANSI_voltage_check {ansi};\n"+"};"
def player_class(value):
    return 'class player {\n'+f"\tdouble {value};\n"+'}'
def clock(timezone,timestamp,stoptime):
    '''
    might need to wrap timezone/timestamp with ''
    '''
    return 'clock {\n'+f"\ttimezone {timezone};\n"+f"\ttimestamp '{timestamp}';\n"+f"\tstoptime '{stoptime}';\n"+'}\n'
def triplex_line_conductor(name,resistance, geometric):
    return 'object triplex_line_conductor {\n'+f'\tname {name};\n'+f'\tresistance {resistance};\n'+f'\tgeometric_mean_radius {geometric};\n'+'}'

def center_tapped_xfmr_config(name,power_rating,phase):
    return 'object transformer_configuration {\n'+f'\tname {name};\n'+f'\tconnect_type SINGLE_PHASE_CENTER_TAPPED;\n'+f'\tinstall_type POLETOP;\n'+f'\tpower{phase}_rating {power_rating};\n'+f'\tprimary_voltage 480.0;\n'+f'\tsecondary_voltage 120.0;\n'+f'\timpedance 0.006+0.0136j;\n'+'}'

def padmount_xfmr_config(connect_type,power_rating,primary_voltage,secondary_voltage):
    return 'object transformer_configuration {\n'+f'\tconnect_type {connect_type};\n'+f'\tinstall_type PADMOUNT;\n'+f'\tpower_rating {power_rating};\n'+f'\tprimary_voltage {primary_voltage};\n'+f'\tsecondary_voltage {secondary_voltage};\n'+f'\timpedance 0.011+0.02j;\n'+'}'

def meter_object(name,phases):
    return 'object meter {\n'+f'\tname {name};\n'+f'\tphases {phases};\n'+f'\tnominal_voltage 2401.7771;\n'+'}'

def overhead_lines_objects(name,phases,from_node,to_node):
    return 'object overhead_line {\n'+f'\tname OH{name};\n'+f'\tphases {phases};\n'+f'\tfrom {from_node};\n'+f'\tto {to_node};\n'+f'\tlength {10};\n'+f'\tconfiguration line_configurationn:605;\n'+'}'

def one_line_module(name):
    return f'module {name};\n'
def multi_line_object(name,attr):
    header = f'object {name}'+' {\n'
    body = ''
    for k,v in zip(attr.keys(),attr.values()):
        body += f'\t{k} {v};\n'
    footer = '}\n'
    return header+body+footer
def multi_line_module(name,attr):
    header = f'module {name}'+' {\n'
    body = ''
    for k,v in zip(attr.keys(),attr.values()):
        body += f'\t{k} {v};\n'
    footer = '}\n'
    return header+body+footer
def directives(d):
    body = f"#set {d['name']}={d['value']};\n"
    return body
def glm_load(fn):
    '''
        Def: This function parses through a given glm file and returns the objects & modules of the passed glm file
        Input: name of of the glm file (string)
        Output: objects, modules (tuple of lists)
        Note: objs & mods are lists of DICTS!
            objs: {'name': ..., 'attributes':..., 'children':...}
            mods: {'name': ..., 'attributes':...}
    '''
    with open(fn,'r') as f:
        G = glm.load(f)
    #del G['includes']
    #del G['schedules']
    return G
def load_filter(objs):
    '''
        :param objs: list of objects
        :return: list of loads (list of dicts)
    '''
    loads = list(filter(lambda x: x['name'] == 'triplex_load', x))
    return loads
def glm_to_str(loads):
    a = ''
    for i in loads:
        for j in i:
            a+=j
    return a
def glm_write(loads, fn):
    with open(fn,'w') as f:
        for i in loads:
            for j in i:
                f.write(j)
'''
x,y = glm_load('Base_Case_Wintter.glm')
loads = load_filter(x)
node = 632
tl = []
TL = []
H = []
for i in range(1,132):
    h = house(f'House{node}_{i}',f'Load_trip{node}_{i}')
    f = f'trip_meter{node}_{i}'
    #if i < 38:
        #phase = 'B'
    if i < 41:
        phase = 'A'
    else:
        phase = 'C'
    triplexLine = triplex_line(f'to_Load_line{node}_{i}',f,f'Load_trip{node}_{i}',phase)
    tl.append(triplexLine)
    triplexLoad = triplex_obj(f'Load_trip{node}_{i}','WW'+str(random.randint(1,199)),phase)
    TL.append((triplexLoad))
    H.append(h)
arr = [tl, TL,H]
'''

#Author-Aninyi Ifeanyi
#Description-Creates a flat head screw.


import adsk.core, adsk.fusion, adsk.cam, traceback
from urllib.parse import urlencode, urlparse
from urllib.request import urlopen
import math
from math import cos, sin, radians, pi
import sys
import os
from ...lib import fusion360utils as futil
from ...validation.login import entry
from ... import config
from datetime import datetime, timedelta
import json


# Globals
_app = adsk.core.Application.cast(None)
_ui = adsk.core.UserInterface.cast(None)
_units = ''
app = adsk.core.Application.get()
_ui = app.userInterface

# Command inputs
_imgInputEnglish = adsk.core.ImageCommandInput.cast(None)
_imgInputMetric = adsk.core.ImageCommandInput.cast(None)
_standard = adsk.core.DropDownCommandInput.cast(None)
_length = adsk.core.DropDownCommandInput.cast(None)
_lengthcustom = adsk.core.ValueCommandInput.cast(None)
_diameter = adsk.core.DropDownCommandInput.cast(None)

USER_DETAILS_URL = "http://127.0.0.1:5000/user?email=charlie@example.com"
user_name = "charlie"

_user = adsk.core.StringValueCommandInput.cast(None)
_user_email = adsk.core.StringValueCommandInput.cast(None)
user_email = "charlie@example.com"


_handlers = []





# TODO *** Specify the command identity information. ***
CMD_ID = f'{config.COMPANY_NAME}_{config.ADDIN_NAME}_fhs'
CMD_NAME = 'FLAT HEAD SCREW'
CMD_Description = 'creates a flat head screw with DIN 8245 starndards'

# Specify that the command will be promoted to the panel.
IS_PROMOTED = False

# TODO *** Define the location where the command button will be created. ***
# This is done by specifying the workspace, the tab, and the panel, and the 
# command it will be inserted beside. Not providing the command to position it
# will insert it at the end.
WORKSPACE_ID = 'FusionSolidEnvironment'
PANEL_ID = 'SolidScriptsAddinsPanel'
COMMAND_BESIDE_ID = 'ScriptsManagerCommand2'

# Resource location for command icons, here we assume a sub folder in this directory named "resources".
ICON_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', '')

# Local list of event handlers used to maintain a reference so
# they are not released and garbage collected.
local_handlers = []




def start():
    
    cmd_def = _ui.commandDefinitions.addButtonDefinition(CMD_ID, CMD_NAME, CMD_Description, ICON_FOLDER)

   


    # Define an event handler for the command created event. It will be called when the button is clicked.
    futil.add_handler(cmd_def.commandCreated,  command_created)
   

    # ******** Add a button into the UI so the user can run the command. ********
    # Get the target workspace the button will be created in.
    workspace = _ui.workspaces.itemById(WORKSPACE_ID)

    # Get the panel the button will be created in.
    panel = workspace.toolbarPanels.itemById(PANEL_ID)

    # Create the button command control in the UI after the specified existing command.
    control = panel.controls.addCommand(cmd_def, COMMAND_BESIDE_ID, False)

    # Specify if the command is promoted to the main toolbar. 
    control.isPromoted = IS_PROMOTED


  



# Executed when add-in is stopped.
def stop():
    # Get the various UI elements for this command
    workspace = _ui.workspaces.itemById(WORKSPACE_ID)
    panel = workspace.toolbarPanels.itemById(PANEL_ID)
    command_control = panel.controls.itemById(CMD_ID)
    command_definition = _ui.commandDefinitions.itemById(CMD_ID)

    # Delete the button command control
    if command_control:
        command_control.deleteMe()

    # Delete the command definition
    if command_definition:
        command_definition.deleteMe()    

# Event handler for the commandCreated event.
def command_created(args: adsk.core.CommandCreatedEventArgs):
    futil.log(f'{CMD_NAME} Command Created Event')

    inputs = args.command.commandInputs

    
    futil.log(f'{CMD_NAME} Command Created Event')

    eventArgs = adsk.core.CommandCreatedEventArgs.cast(args)

    # Verify that a Fusion design is active.
    des = adsk.fusion.Design.cast(app.activeProduct)
    if not des:
        _ui.messageBox('A Fusion design must be active when invoking this command.')
        return()

    inputs = args.command.commandInputs




  






  
        



def getCommandInputValue(commandInput, unitType):
    try:
        valCommandInput = adsk.core.ValueCommandInput.cast(commandInput)
        if not valCommandInput:
            return (False, 0)

        # Verify that the expression is valid.
        des = adsk.fusion.Design.cast(_app.activeProduct)
        unitsMgr = des.unitsManager
        
        if unitsMgr.isValidExpression(valCommandInput.expression, unitType):
            value = unitsMgr.evaluateExpression(valCommandInput.expression, unitType)
            return (True, value)
        else:
            return (False, 0)
    except:
        if _ui:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

# Event handler for the commandCreated event.
def command_created(args: adsk.core.CommandCreatedEventArgs):
    futil.log(f'{CMD_NAME} Command Created Event')

    inputs = args.command.commandInputs

    
    futil.log(f'{CMD_NAME} Command Created Event')

    eventArgs = adsk.core.CommandCreatedEventArgs.cast(args)

    # Verify that a Fusion design is active.
    des = adsk.fusion.Design.cast(app.activeProduct)
    if not des:
        _ui.messageBox('A Fusion design must be active when invoking this command.')
        return()
    


    
    try:
        file_pathnew = os.path.join(os.path.expanduser("~/AppData/Roaming/Autodesk/ApplicationPlugins/DINFASTENERS.bundle/contents/commands/login"), "datesnewuser.json")
        file_path = os.path.join(os.path.expanduser("~/AppData/Roaming/Autodesk/ApplicationPlugins/DINFASTENERS.bundle/contents/commands/login"), "dates.json")
        file_pathtwo = os.path.join(os.path.expanduser("~/AppData/Roaming/Autodesk/ApplicationPlugins/DINFASTENERS.bundle/contents/commands/login"), "datesfreeuser.json")
        with open(file_pathnew, 'r') as file:
                dates_dict = json.load(file)
        current_datenewuser = datetime.strptime(dates_dict["current_date"], "%a, %d %b %Y %H:%M:%S GMT")
        current_datetime = datetime.now()
        
        time_difference = current_datetime - current_datenewuser
        time_compare = timedelta(minutes=10)
        
        file = None
        if time_difference < time_compare:
            file = file_pathnew
        else:
            file = file_path
        # Define the path where the JSON file is stored
        file_path = os.path.join(os.path.expanduser("~/AppData/Roaming/Autodesk/ApplicationPlugins/DINFASTENERS.bundle/contents/commands/login"), "dates.json")
        with open(file, 'r') as file:
                dates_dict = json.load(file)
        
        with open(file_pathtwo, 'r') as file:
                dates_dictnew = json.load(file)
            
        install_date = datetime.strptime(dates_dict["install_date"], "%a, %d %b %Y %H:%M:%S GMT")
        current_datenew = datetime.strptime(dates_dict["current_date"], "%a, %d %b %Y %H:%M:%S GMT")
        current_date_str = current_datenew.strftime("%a, %d %b %Y %H:%M:%S GMT")
        current_datefree = datetime.strptime(dates_dictnew["current_datenew"], "%a, %d %b %Y %H:%M:%S GMT")
        current_datenew_str = current_datefree.strftime("%a, %d %b %Y %H:%M:%S GMT")
        
        current_dateused = None
        if time_difference < time_compare:
            current_dateused = current_datefree
        else:
            current_dateused = current_datenew


        current_datetime = datetime.now()
        current_datetime_addition = current_datetime - timedelta(minutes=5)
        if current_dateused < current_datetime_addition:
            _ui.messageBox('please login into your profile')
            return()
        if current_datetime>install_date:
            _ui.messageBox("your trail period has expired")
            sys.exit()

        

    


            
        defaultUnits = des.unitsManager.defaultLengthUnits 
        _ui.messageBox('please select the point to create flat head screw. note selected point must be perfectly circular')


    


            
        # Determine whether to use inches or millimeters as the intial default.
        global _units
        if defaultUnits == 'in' or defaultUnits == 'ft':
            _units = 'in'
        else:
            _units = 'mm'
                    
        # Define the default values and get the previous values from the attributes.
        diameter = 'M1'
        diameterAttrib = des.attributes.itemByName('flatheadscrew', 'diameter')
        if diameterAttrib:
            diameter = diameterAttrib.value


        length = '6'
        lengthAttrib = des.attributes.itemByName('flatheadscrew', 'length')
        if lengthAttrib:
            length = lengthAttrib.value
        
        lengthcustom = 0.6
        lengthcustomAttrib = des.attributes.itemByName('flatheadscrew', 'lengthcustom')
        if lengthcustomAttrib:
            lengthcustom = float(lengthcustomAttrib.value)  


    


    



        cmd = eventArgs.command
        cmd.isExecutedWhenPreEmpted = False
        inputs = cmd.commandInputs
        global _standard, _length, _lengthcustom, _diameter, selObj
        
        imagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'flatheadscrewEnglish.png')
        _imgInputEnglish = inputs.addImageCommandInput('flatheadscrewImageEnglish', '', imagePath)
        _imgInputEnglish.isFullWidth = True



        

        
    



        _diameter = inputs.addDropDownCommandInput('diameter', 'Diameter', adsk.core.DropDownStyles.TextListDropDownStyle)
        if diameter == 'M0.4':
            _diameter.listItems.add('M0.4', True)
        else:
            _diameter.listItems.add('M0.4', False)

        if diameter == 'M0.5':
            _diameter.listItems.add('M0.5', True)
        else:
            _diameter.listItems.add('M0.5', False)

        if diameter == 'M0.6':
            _diameter.listItems.add('M0.6', True)
        else:
            _diameter.listItems.add('M0.6', False)

        if diameter == 'M0.7':
            _diameter.listItems.add('M0.7', True)
        else:
            _diameter.listItems.add('M0.7', False) 

        if diameter == 'M0.8':
            _diameter.listItems.add('M0.8', True)
        else:
            _diameter.listItems.add('M0.8', False)

        if diameter == 'M0.9':
            _diameter.listItems.add('M0.9', True)
        else:
            _diameter.listItems.add('M0.9', False)

        if diameter == 'M1':
            _diameter.listItems.add('M1', True)
        else:
            _diameter.listItems.add('M1', False)             
                                
        if diameter == 'M1.2':
            _diameter.listItems.add('M1.2', True)
        else:
            _diameter.listItems.add('M1.2', False)

        if diameter == 'M1.4':
            _diameter.listItems.add('M1.4', True)
        else:
            _diameter.listItems.add('M1.4', False)

                    
                                                            

        _length = inputs.addDropDownCommandInput('length', 'Length', adsk.core.DropDownStyles.TextListDropDownStyle)
        if length == '0.6':
            _length.listItems.add('0.6', True)
        else:
            _length.listItems.add('0.6', False)

        if length == '0.7':
            _length.listItems.add('0.7', True)
        else:
            _length.listItems.add('0.7', False)

        if length == '0.8':
            _length.listItems.add('0.8', True)
        else:
            _length.listItems.add('0.8', False)

        if length == '1.2':
            _length.listItems.add('1.2', True)
        else:
            _length.listItems.add('1.2', False) 

        if length == '1.4':
            _length.listItems.add('1.4', True)
        else:
            _length.listItems.add('1.4', False)

        if length == '1.6':
            _length.listItems.add('1.6', True)
        else:
            _length.listItems.add('1.6', False)

        if length == '1.8':
            _length.listItems.add('1.8', True)
        else:
            _length.listItems.add('1.8', False)             
                                
        if length == '2':
            _length.listItems.add('2', True)
        else:
            _length.listItems.add('2', False)

        if length == '2.2':
            _length.listItems.add('2.2', True)
        else:
            _length.listItems.add('2.2', False)

        if length == '2.5':
            _length.listItems.add('2.5', True)
        else:
            _length.listItems.add('2.5', False)  

        if length == '3':
            _length.listItems.add('3', True)
        else:
            _length.listItems.add('3', False) 

        if length == '4':
            _length.listItems.add('4', True)
        else:
            _length.listItems.add('4', False)   

        if length == '5':
            _length.listItems.add('5', True)
        else:
            _length.listItems.add('5', False)             
                                                                
        if length == '6':
            _length.listItems.add('6', True)
        else:
            _length.listItems.add('6', False)                                                         
                                                                
        
        if length == 'custom':
            _length.listItems.add('custom', True)
        else:
            _length.listItems.add('custom', False)

        _lengthcustom = inputs.addValueInput('lengthcustom', 'custom length', 'mm', adsk.core.ValueInput.createByReal(lengthcustom))
        if length != 'custom':
            _lengthcustom.isVisible = False


        sel = _ui.selectEntity('Select a point to create flat head screw', 'Edges,SketchCurves')
        selObj = sel.entity    

    

        
                                    
        # Connect to the command related events.
        onExecute = flatheadscrewCommandExecuteHandler()
        cmd.execute.add(onExecute)
        _handlers.append(onExecute)        
        
        
        
    except FileNotFoundError:
            _ui.messageBox('please login into your profile')
    except RuntimeError:
            _ui.messageBox('Error you interrupted your selection process please cancel the command and restart command')   




    


               
# Event handler for the execute event.
class flatheadscrewCommandExecuteHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
       
        try:
            eventArgs = adsk.core.CommandEventArgs.cast(args)




            des = adsk.fusion.Design.cast(app.activeProduct)
            attribs = des.attributes
            attribs.add('flatheadscrew', 'length', _length.selectedItem.name)
            attribs.add('flatheadscrew', 'lengthcustom', str(_lengthcustom.value))
            attribs.add('flatheadscrew', 'diameter', _diameter.selectedItem.name)
           

              # Get the current values.



         

            if _diameter.selectedItem.name == 'M0.4':
                diameter = 0.04/2
            elif _diameter.selectedItem.name == 'M0.5':
                diameter = 0.05/2
            elif _diameter.selectedItem.name == 'M0.6':
                diameter = 0.06/2

            elif _diameter.selectedItem.name == 'M0.7':
                diameter = 0.07/2
            
            elif _diameter.selectedItem.name == 'M0.8':
                diameter = 0.08/2
            
            elif _diameter.selectedItem.name == 'M0.9':
                diameter = 0.09/2

            elif _diameter.selectedItem.name == 'M1':
                diameter = 0.1/2  

            elif _diameter.selectedItem.name == 'M1.2':
                diameter = 0.12/2 

            elif _diameter.selectedItem.name == 'M1.4':
                diameter = 0.14/2

           

            if _length.selectedItem.name == 'custom':
                length = _lengthcustom.value
            else:
                if _length.selectedItem.name == '0.6':
                    length = (0.06+(diameter*2)*(-0.13))
                elif _length.selectedItem.name == '0.7':
                    length = (0.07+(diameter*2)*(-0.13))
                elif _length.selectedItem.name == '0.8':
                    length = (0.08+(diameter*2)*(-0.13))

                elif _length.selectedItem.name == '0.9':
                    length = (0.09+(diameter*2)*(-0.13))
                
                elif _length.selectedItem.name == '1':
                    length = (0.1+(diameter*2)*(-0.13))
                
                elif _length.selectedItem.name == '1.2':
                    length = (0.12+(diameter*2)*(-0.13))

                elif _length.selectedItem.name == '1.4':
                    length = (0.14+(diameter*2)*(-0.13)) 

                elif _length.selectedItem.name == '1.6':
                    length = (0.16+(diameter*2)*(-0.13)) 

                elif _length.selectedItem.name == '1.8':
                    length = (0.18+(diameter*2)*(-0.13))

                elif _length.selectedItem.name == '2':
                    length = (0.2+(diameter*2)*(-0.13))

                elif _length.selectedItem.name == '2.2':
                    length = (0.22+(diameter*2)*(-0.13))

                elif _length.selectedItem.name == '2.5':
                    length = (0.25+(diameter*2)*(-0.13))

                elif _length.selectedItem.name == '3':
                    length = (0.3+(diameter*2)*(-0.13))

                elif _length.selectedItem.name == '4':
                    length = (0.4+(diameter*2)*(-0.13))

                elif _length.selectedItem.name == '5':
                    length = (0.5+(diameter*2)*(-0.13))




                if _length.selectedItem.name == '6':
                    length = (0.6+(diameter*2)*(-0.13))
                
            threadlenght = None
            if (length < (0.061)) :
                threadlenght = 0.042

            elif (length == 0.06 or length < (0.141)) :
                 threadlenght = 0.042   

            elif (length == 0.16 or length < (0.31)) :
                 threadlenght = 0.112   

            elif (length > (0.3)) :
                 threadlenght = 0.28/2   

           

                 

           

            
            headdia = None

            if _diameter.selectedItem.name == 'M0.4' :
                headdia = 0.07/2
            
            elif _diameter.selectedItem.name == 'M0.5':
                headdia = 0.08/2
            elif _diameter.selectedItem.name == 'M0.6':
                headdia = 0.09/2

            elif _diameter.selectedItem.name == 'M0.7':
                headdia = 0.11/2
            
            elif _diameter.selectedItem.name == 'M0.8':
                headdia = 0.12/2
            
            elif _diameter.selectedItem.name == 'M0.9':
                headdia = 0.14/2

            elif _diameter.selectedItem.name == 'M1':
                headdia = 0.16/2  

            elif _diameter.selectedItem.name == 'M1.2':
                headdia = 0.19/2 

            elif _diameter.selectedItem.name == 'M1.4':
                headdia = 0.23/2

           

                 



            
            keysizeb = (headdia)
            bottom = (diameter*(-0.19))
            tophead = length 
           
            hexdistance = None


            if _diameter.selectedItem.name == 'M0.4' :
                hexdistance = -0.01
            
            elif _diameter.selectedItem.name == 'M0.5':
                hexdistance = -0.015
            elif _diameter.selectedItem.name == 'M0.6':
                hexdistance = -0.015

            elif _diameter.selectedItem.name == 'M0.7':
                hexdistance = -0.015
            
            elif _diameter.selectedItem.name == 'M0.8':
                hexdistance = -0.025
            
            elif _diameter.selectedItem.name == 'M0.9':
                hexdistance = -0.025

            elif _diameter.selectedItem.name == 'M1':
                hexdistance = -0.025  

            elif _diameter.selectedItem.name == 'M1.2':
                hexdistance = -0.03 

            elif _diameter.selectedItem.name == 'M1.4':
                hexdistance = -0.03



            


            
            keysize = None 
            if _diameter.selectedItem.name == 'M0.4' :
                keysize = 0.014/2
            
            elif _diameter.selectedItem.name == 'M0.5':
                keysize = 0.014/2
            elif _diameter.selectedItem.name == 'M0.6':
                keysize = 0.014/2

            elif _diameter.selectedItem.name == 'M0.7':
                keysize = 0.016/2
            
            elif _diameter.selectedItem.name == 'M0.8':
                keysize = 0.016/2
            
            elif _diameter.selectedItem.name == 'M0.9':
                keysize = 0.02/2

            elif _diameter.selectedItem.name == 'M1':
                keysize = 0.02/2 

            elif _diameter.selectedItem.name == 'M1.2':
                keysize = 0.02/2

            elif _diameter.selectedItem.name == 'M1.4':
                keysize = 0.02/2


            headlengtha = None    

            if _diameter.selectedItem.name == 'M0.4' :
                headlengtha = -0.005
            
            elif _diameter.selectedItem.name == 'M0.5':
                headlengtha = -0.010
            elif _diameter.selectedItem.name == 'M0.6':
                headlengtha = -0.010

            elif _diameter.selectedItem.name == 'M0.7':
                headlengtha = -0.010
            
            elif _diameter.selectedItem.name == 'M0.8':
                headlengtha = -0.015
            
            elif _diameter.selectedItem.name == 'M0.9':
                headlengtha = -0.015

            elif _diameter.selectedItem.name == 'M1':
                headlengtha = -0.015 

            elif _diameter.selectedItem.name == 'M1.2':
                headlengtha = -0.015

            elif _diameter.selectedItem.name == 'M1.4':
                headlengtha = -0.015

            cone = length-((0.3*diameter)-(headlengtha))
            cone2 = (length+headlengtha)  

             
            

                
            # VALIDATE INPUTS
            if diameter == 0.04/2 and length < 0.051 :
                _ui.messageBox('length must be less than 1.3mm for M0.4')
                return  

            elif diameter == 0.05/2 and length < 0.0551  :
                _ui.messageBox('length must be less than 1.65mm or greater than 0.55mm for M0.5')
                return 
                 

            elif diameter == 0.06/2 and length < 0.0651 :
                _ui.messageBox('length must be less than 2.35mm or greater than 0.65mm for M0.6')
                return 

            elif diameter == 0.07/2 and length < 0.0851  :
                _ui.messageBox('length must be less than 0.55mm or greater than 1.65mm for M0.7')
                return 

            elif diameter == 0.08/2 and length < 0.0951  :
                _ui.messageBox('length must be less than 0.65mm or greater than 2.35mm for M0.8')
                return         

            elif diameter == 0.09/2 and length < 0.1151  :
                _ui.messageBox('length must be less than 0.85mm or greater than 3.75mm for M0.9')
                return      

            elif diameter == 0.1/2 and length < 0.1151  :
                _ui.messageBox('length must be less than 0.95mm or greater than 4.75mm for M1')
                return       

            elif diameter == 0.12/2 and length < 0.1311 :
                _ui.messageBox('length must be less than 1.15mm or greater than 5.75mm for M1.2')
                return          

            elif diameter == 0.14/2 and length < 0.1311  :
                _ui.messageBox('length must be less than 80mm or greater than 12mm for M1.4')
                return         

                                          
            


            # VALIDATE INPUTS OF UPPER LIMITS

          
            elif diameter == 0.04/2 and length > 0.131:
                 _ui.messageBox('length must be less than 1.3mm or greater than 0.5mm for M0.4')
                 return 

            elif diameter == 0.05/2 and length > 0.165  :
                 _ui.messageBox('length must be less than 1.65mm or greater than 0.55mm for M0.5')
                 return 

            elif diameter == 0.06/2 and length > 0.236  :
                 _ui.messageBox('length must be less than 2.35mm or greater than 0.65mm for M0.6')
                 return        

            elif diameter == 0.07/2 and length > 0.286  :
                 _ui.messageBox('length must be less than 2.85mm or greater than 0.85mm for M0.7')
                 return      

            elif diameter == 0.08/2 and length > 0.376  :
                 _ui.messageBox('length must be less than 3.75mm or greater than 0.95mm for M0.8')
                 return       

            elif diameter == 0.09/2 and length > 0.476  :
                 _ui.messageBox('length must be less than 4.75mm or greater than 1.15mm for M0.9')
                 return          

            elif diameter == 0.1/2 and length > 0.576 :
                 _ui.messageBox('length must be less than 5.75mm or greater than 1.15mm for M1.0')
                 return         

            elif diameter == 0.12/2 and length > 0.571 :
                 _ui.messageBox('length must be less than 5.7mm or greater than 1.3mm for M1.2')
                 return       

            elif diameter == 0.14/2 and length > 0.61  :
                 _ui.messageBox('length must be less than 6mm or greater than 1.3mm for M1.4')
                 return                 

          





  
                

            

            flatheadscrewComp = drawflatheadscrew( des, diameter, length, threadlenght, headdia, keysizeb, bottom, tophead, hexdistance, cone, cone2, keysize, headlengtha, selObj)
             
        except:
            if _ui:
                _ui.messageBox('Failed:\n{}'.format(traceback.format_exc())) 





       



            
                          



# Builds a flat head screw SCREW.
def drawflatheadscrew(design, diameter, length, threadlenght, headdia, keysizeb, bottom, tophead, hexdistance, cone, cone2, keysize, headlengtha, selObj):
    try:                
    

        
        # create a new component
       
        rootComp = design.rootComponent
        allOccs = rootComp.occurrences
        newOcc = allOccs.addNewComponent(adsk.core.Matrix3D.create())
        newComponent = adsk.fusion.Component.cast(newOcc.component)
        newComponent.name = "flat_head_screw"
        
        



        


        extrudes = newComponent.features.extrudeFeatures
        constructionPlanes = rootComp.constructionPlanes
        filletFeats = newComponent.features.filletFeatures
        chamferFeats = newComponent.features.chamferFeatures
        loft_features = newComponent.features.loftFeatures
       
        sketches = newComponent.sketches
        sketch1 = sketches.add(rootComp.xZConstructionPlane)

        # Create sketch lines
        circles = sketch1.sketchCurves.sketchCircles

        # Create some 3D points
        circle1 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), diameter)

        # Create an extrusion
        prof = sketch1.profiles.item(0)
        distance = adsk.core.ValueInput.createByReal(length)
        extrude1 = extrudes.addSimple(prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        body1 = extrude1.bodies.item(0)
        body1.name = "shank"

        # create an offset plane
        planeInput = constructionPlanes.createInput()
        planeInput.setByOffset(rootComp.xZConstructionPlane, adsk.core.ValueInput.createByReal(length))
        offsetPlane = constructionPlanes.add(planeInput)

        # create the second sketch
        sketches = newComponent.sketches
        sketch2 = sketches.add(offsetPlane)

        # Create sketch lines
        sketchCircles = sketch2.sketchCurves.sketchCircles

        # Create some 3D points
        circle2 = sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), headdia)

        # create the second extrusion
        # Create an extrusion
        prof = sketch2.profiles.item(0)
        distance = adsk.core.ValueInput.createByReal(headlengtha)
        extrude2 = extrudes.addSimple(prof, distance, adsk.fusion.FeatureOperations.JoinFeatureOperation)
        body1 = extrude2.bodies.item(0)

        # create an offset plane
        planeInput = constructionPlanes.createInput()
        planeInput.setByOffset(rootComp.xZConstructionPlane, adsk.core.ValueInput.createByReal(tophead))
        offsetPlane2 = constructionPlanes.add(planeInput)

        # create the hexagon
        sketches = newComponent.sketches
        sketch3 = sketches.add(offsetPlane2)


        
        # Create sketch lines
        sketchLines = sketch3.sketchCurves.sketchLines
        
        # Create some 3D points
        point1 = adsk.core.Point3D.create(0.0, 0.0, 0.0)
        point2 = adsk.core.Point3D.create((keysizeb), (keysize), 0.0)
        
        # Create sketch rectangle
        sketchLines.addCenterPointRectangle(point1, point2)

       
        # create the third extrusion
        prof = sketch3.profiles.item(0)
        distance = adsk.core.ValueInput.createByReal(hexdistance)
        extrude3 = extrudes.addSimple(prof, distance, adsk.fusion.FeatureOperations.CutFeatureOperation)
        body1 = extrude3.bodies.item(0)

       
        # create 4th extrusion
        planeInput = constructionPlanes.createInput()
        planeInput.setByOffset(rootComp.xZConstructionPlane, adsk.core.ValueInput.createByReal(threadlenght))
        offsetPlane3 = constructionPlanes.add(planeInput)

        sketches = newComponent.sketches
        sketch4 = sketches.add(offsetPlane3)
        circles = sketch4.sketchCurves.sketchCircles

        # Create some 3D points
        circle1 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), diameter)
        circle2 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), diameter*0.73)

        prof = sketch4.profiles.item(0)
        distance = adsk.core.ValueInput.createByReal((diameter*2)*0.055)
        extrude4 = extrudes.addSimple(prof, distance, adsk.fusion.FeatureOperations.CutFeatureOperation)
        body1 = extrude4.bodies.item(0)

       

        planeInput = constructionPlanes.createInput()
        planeInput.setByOffset(rootComp.xZConstructionPlane, adsk.core.ValueInput.createByReal(threadlenght+(diameter*2)*0.055))
        offsetPlane4 = constructionPlanes.add(planeInput)

        sketches = newComponent.sketches
        sketch5 = sketches.add(offsetPlane4)
        circles = sketch5.sketchCurves.sketchCircles

        # Create some 3D points
        circle3 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), diameter)


        loft_input = loft_features.createInput(adsk.fusion.FeatureOperations.JoinFeatureOperation)

        # Add the profiles (circles) to the loft input
        loft_input.loftSections.add(sketch4.profiles.item(1))
        loft_input.loftSections.add(sketch5.profiles.item(0))

        # Set the loft input to be a solid
        loft_input.isSolid = True

        # Create the loft feature
        loft_features.add(loft_input)


        planeInput = constructionPlanes.createInput()
        planeInput.setByOffset(rootComp.xZConstructionPlane, adsk.core.ValueInput.createByReal(0))
        offsetPlane5 = constructionPlanes.add(planeInput)


        sketches = newComponent.sketches
        sketch6 = sketches.add(offsetPlane5)

        sketchCircles = sketch6.sketchCurves.sketchCircles

        # Create some 3D points
        circle2 = sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), diameter)

       

        planeInput = constructionPlanes.createInput()
        planeInput.setByOffset(rootComp.xZConstructionPlane, adsk.core.ValueInput.createByReal(bottom))
        offsetPlane6 = constructionPlanes.add(planeInput)
    


        sketches = newComponent.sketches
        sketch7 = sketches.add(offsetPlane6)


        
        

        # Create a point at coordinates (1, 2, 0) in the sketch
        point = sketch7.sketchPoints.add(adsk.core.Point3D.create(0, 0, 0))


        loft_input1 = loft_features.createInput(adsk.fusion.FeatureOperations.JoinFeatureOperation)

        # Add the profiles (circles) to the loft input
        loft_input1.loftSections.add(sketch6.profiles.item(0))
        loft_input1.loftSections.add(point)

        # Set the loft input to be a solid
        loft_input1.isSolid = True

        # Create the loft feature
        loft_features.add(loft_input1)


        planeInput = constructionPlanes.createInput()
        planeInput.setByOffset(rootComp.xZConstructionPlane, adsk.core.ValueInput.createByReal(cone2))
        offsetPlane7 = constructionPlanes.add(planeInput)

        sketches = newComponent.sketches
        sketch8 = sketches.add(offsetPlane7)

        sketchCircles = sketch8.sketchCurves.sketchCircles

        # Create some 3D points
        circle9 = sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), headdia)

        planeInput = constructionPlanes.createInput()
        planeInput.setByOffset(rootComp.xZConstructionPlane, adsk.core.ValueInput.createByReal(cone))
        offsetPlane8 = constructionPlanes.add(planeInput)

        sketches = newComponent.sketches
        sketch9 = sketches.add(offsetPlane8)

        sketchCircles = sketch9.sketchCurves.sketchCircles

        # Create some 3D points
        circle2 = sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), diameter)

        loft_input1 = loft_features.createInput(adsk.fusion.FeatureOperations.JoinFeatureOperation)

        # Add the profiles (circles) to the loft input
        loft_input1.loftSections.add(sketch8.profiles.item(0))
        loft_input1.loftSections.add(sketch9.profiles.item(0))

        # Set the loft input to be a solid
        loft_input1.isSolid = True

        # Create the loft feature
        loft_features.add(loft_input1)

        # create an offset plane
        planeInput = constructionPlanes.createInput()
        planeInput.setByOffset(rootComp.xZConstructionPlane, adsk.core.ValueInput.createByReal(tophead))
        offsetPlane2 = constructionPlanes.add(planeInput)

        # create the hexagon
        sketches = newComponent.sketches
        sketch10 = sketches.add(offsetPlane2)


        
        # Create sketch lines
        sketchLines = sketch10.sketchCurves.sketchLines
        
        # Create some 3D points
        point1 = adsk.core.Point3D.create(0.0, 0.0, 0.0)
        point2 = adsk.core.Point3D.create((keysizeb), (keysize), 0.0)
        
        # Create sketch rectangle
        sketchLines.addCenterPointRectangle(point1, point2)

       
        # create the third extrusion
        prof = sketch10.profiles.item(0)
        distance = adsk.core.ValueInput.createByReal(hexdistance)
        extrude10 = extrudes.addSimple(prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        body2 = extrude10.bodies.item(0)
        body2.name = "cut body"

        # Create the first joint geometry with the end face
        geo0 = adsk.fusion.JointGeometry.createByCurve(circle9, adsk.fusion.JointKeyPointTypes.CenterKeyPoint)
        # Create the second joint geometry with the sketch line
        geo1 = adsk.fusion.JointGeometry.createByCurve(selObj, adsk.fusion.JointKeyPointTypes.CenterKeyPoint)
         
        # Create joint input
        joints = rootComp.joints
        jointInput = joints.createInput(geo0, geo1)

        # Set the joint input
        angle = adsk.core.ValueInput.createByString('90 deg')
        offset = adsk.core.ValueInput.createByReal(0)
        jointInput.angle = angle
        jointInput.offset = offset
        jointInput.isFlipped = True
        jointInput.setAsRigidJointMotion
        
        # Create the joint
        joint = joints.add(jointInput)

        # Group everything used to create the gear in the timeline.
        timelineGroups = design.timeline.timelineGroups
        newOccIndex = newOcc.timelineObject.index
        screwIndex = extrude10.timelineObject.index
        timelineGroup = timelineGroups.add(newOccIndex, screwIndex)
        timelineGroup.name = 'screw'

      
        
        
        design.activateRootComponent()


            
    
        
    



       


    except:
        if _ui:
            _ui.messageBox('It seems you selected a point that is not circular, undo and restart command')
            
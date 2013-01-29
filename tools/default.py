import mc
from libs import boxeehal
from libs import dir

dict = {
	'ethernet'	:	{  'GetInfo':{ 'instance' : 0}  },
	'wireless'	:	{  'GetInfo':{ 'instance' : 0}  },
	'clock'		:	{  'GetTimeZone':{}  },
	'power'		:	{  'Standby':{}, 'Shutdown':{}, 'Reboot':{}  },
	'host'		:	{  'GetHostName':{}  },
	'thermals'	:	{  'GetCPUTemperature':{}, 'GetFanSpeed':{}  },
	'system'	:	{  'GetHardwareInfo':{}, 'GetSoftwareInfo':{}  },
}

def init():
	dir.CreateDir()
	for item in dict.keys()
		dir.AddToDir( item,	 '', item, 	'thumb.png', {},  mc.ListItem.MEDIA_UNKNOWN))
	dir.PushDir()

def getInfo():
    list = mc.GetWindow(14000).GetList(90)
    item = list.GetItem(list.GetFocusedItem())
	label = item.GetLabel()
    path = item.GetPath()
	mc.GetWindow(14000).PushState()
	if label in dict.keys():
		for item in dict[label].keys():
			dir.AddToDir( item,	 '', path, 	'thumb.png', {},  mc.ListItem.MEDIA_UNKNOWN))	
	else:
		result = boxeehal.get(path, label, dict[path][label])
		for item in result.keys():
			dir.AddToDir( str(item) + ': ' + str(result[item]),	 '', '', 	'thumb.png', {},  mc.ListItem.MEDIA_UNKNOWN))	
	
if ( __name__ == "__main__" ):
    mc.ActivateWindow(14000)
	init()





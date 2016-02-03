import wx
import subprocess,os
import re,mess,mail

wildcard =  "All files (*.*)|*.*"
files={}
class PanelOne(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.st1 = wx.StaticText(self, label='Phone Number')
        self.st1.SetFont(font)
        hbox1.Add(self.st1, flag=wx.RIGHT, border=8)
        self.tc = wx.TextCtrl(self)
        hbox1.Add(self.tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.st2=wx.StaticText(self,label='Text')
        self.st2.SetFont(font)
        hbox2.Add(self.st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc2 = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        hbox3.Add(self.tc2, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, 
            border=10)
        vbox.Add((-1, 25))
        
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        self.btn1 = wx.Button(self, label='Send', size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.onSend, self.btn1)
        hbox5.Add(self.btn1)
        self.btn2 = wx.Button(self, label='Close', size=(70, 30))
        self.btn2.Bind(wx.EVT_BUTTON, self.onC)
        hbox5.Add(self.btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        
        self.SetSizer(vbox)

    def onSend(self,event):
        num=re.compile(r'\+\d+')
        if num.search(str(self.tc.GetValue()))==None:
            dial = wx.MessageDialog(None, 'Please enter valid phone number', 'Error', 
            wx.OK | wx.ICON_EXCLAMATION)
            dial.ShowModal()
        elif str(self.tc2.GetValue()).strip()=='':
            dial = wx.MessageDialog(None, 'Please enter valid text', 'Error', 
            wx.OK | wx.ICON_EXCLAMATION)
            dial.ShowModal()
        else:
        	pat=mess.bhejo(str(self.tc.GetValue()),str(self.tc2.GetValue()))
        	if pat=='Error sending message':
        		dial1 = wx.MessageDialog(None, 'Error sending the message', 'Check the details!', 
        			wx.OK | wx.ICON_ERROR)
        		dial1.ShowModal()
        	else:
        		dial2 = wx.MessageDialog(None, 'Message successfully sent', 'Success!!', wx.OK)
        		dial2.ShowModal()

    def onC(self,event):
        self.Close()


class PanelTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        self.currentDirectory = os.getcwd()
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.st1 = wx.StaticText(self, label='Your Email ID')
        self.st1.SetFont(font)
        hbox1.Add(self.st1, flag=wx.RIGHT, border=8)
        self.tc = wx.TextCtrl(self)
        hbox1.Add(self.tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.st3 = wx.StaticText(self, label='Password')
        self.st3.SetFont(font)
        hbox3.Add(self.st3, flag=wx.RIGHT, border=33)
        self.tc3 = wx.TextCtrl(self,style=wx.TE_PASSWORD)
        hbox3.Add(self.tc3, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.st2 = wx.StaticText(self, label='Send To')
        self.st2.SetFont(font)
        hbox2.Add(self.st2, flag=wx.RIGHT, border=45)
        self.tc2 = wx.TextCtrl(self)
        hbox2.Add(self.tc2, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        vbox.Add((-1, 10))


        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.st4 = wx.StaticText(self, label='Subject')
        self.st4.SetFont(font)
        hbox4.Add(self.st4, flag=wx.RIGHT, border=50)
        self.tc4 = wx.TextCtrl(self)
        hbox4.Add(self.tc4, proportion=1)
        vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        vbox.Add((-1, 10))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        self.st5 = wx.StaticText(self, label='Body')
        self.st5.SetFont(font)
        hbox5.Add(self.st5, flag=wx.RIGHT, border=50)
        vbox.Add(hbox5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc6 = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        hbox6.Add(self.tc6, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox6, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, 
            border=5)

        vbox.Add((-1, 25))

        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        self.btn1 = wx.Button(self, label='Attach', size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.onAttach, self.btn1)
        hbox7.Add(self.btn1)
        self.st7 = wx.StaticText(self,wx.ID_ANY ,label='Number of attachments')
        self.st7.SetFont(font)
        hbox7.Add(self.st7, flag=wx.RIGHT, border=50)
        vbox.Add(hbox7, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, 
            border=5)

        hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        self.btn2 = wx.Button(self, label='Send', size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.onSend, self.btn2)
        hbox8.Add(self.btn2)
        self.btn3 = wx.Button(self, label='Close', size=(70, 30))
        self.btn3.Bind(wx.EVT_BUTTON, self.onC)
        hbox8.Add(self.btn3, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox8, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=5)

        self.SetSizer(vbox)

    def onAttach(self,event):
    	dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.currentDirectory, 
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
        	
        	paths = dlg.GetPaths()
        	self.st7.SetLabel(str(paths[0]).encode('utf-8').encode('ascii'))

        	print "You chose the following file(s):"
        	for path in paths:
        		name=str(paths[0]).encode('utf-8').encode('ascii').rfind('\\')
        		namee=str(paths[0]).encode('utf-8').encode('ascii')[name+1:]
        		files[namee]=str(paths[0]).encode('utf-8').encode('ascii')	
        	#print files
        	self.st7.SetLabel(str(len(files))+" files attached.")
        dlg.Destroy()

    def onSend(self,event):
    	if ('.com' not in str(self.tc2.GetValue())) or ('.com' not in str(self.tc.GetValue())):
    		dial = wx.MessageDialog(None, 'Please enter valid email id', 'Error', wx.OK | wx.ICON_EXCLAMATION)            
    		dial.ShowModal()
    		return
    	sender=str(self.tc.GetValue())
    	passs=str(self.tc3.GetValue())
    	receiver=str(self.tc2.GetValue())
    	filess=files
    	body=str(self.tc6.GetValue())
    	sub=str(self.tc4.GetValue())
    	pat=mail.bhejomail(sender,passs,receiver,sub,body,files)
    	if pat=='Error sending mail':
    		dial1 = wx.MessageDialog(None, 'Error sending the mail', 'Check the details!',wx.OK | wx.ICON_ERROR)
    		dial1.ShowModal()
        else:
        	dial2 = wx.MessageDialog(None, 'Mail successfully sent', 'Success!!', wx.OK)
        	dial2.ShowModal()
    def onC(self,event):
    	self.Close()


class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Messenger")
        self.panel_one = PanelOne(self)
        self.panel_two = PanelTwo(self)
        self.panel_two.Hide()
 
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
 
        toolbar = self.CreateToolBar()
        qtool = toolbar.AddLabelTool(wx.ID_ANY, 'Mail', wx.Bitmap('gmail.png'))
        toolbar.SetBackgroundColour(wx.Colour(192,192,192))
        toolbar.AddControl(wx.StaticBitmap(toolbar, -1,wx.Image('space.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 
        wx.DefaultPosition, wx.DefaultSize)) 
        self.ToolBar.AddSeparator()
        toolbar.AddControl(wx.StaticBitmap(toolbar, -1,wx.Image('space.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 
        wx.DefaultPosition, wx.DefaultSize)) 
        mtool=toolbar.AddLabelTool(wx.ID_ANY,'Message',wx.Bitmap('message.png'))
        toolbar.Realize()
        self.Bind(wx.EVT_TOOL, self.onSwitchPanels2, qtool)
        self.Bind(wx.EVT_TOOL, self.onSwitchPanels1, mtool)
    def OnQuit(self, e):
        self.Close()
    def onSwitchPanels2(self, event):
        self.SetTitle("Mail")
        self.panel_one.Hide()
        self.panel_two.Show()
        self.Layout()
    def onSwitchPanels1(self,event):
        self.SetTitle("Message")
        self.panel_one.Show()
        self.panel_two.Hide()
        self.Layout()
 
if __name__ == '__main__':
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
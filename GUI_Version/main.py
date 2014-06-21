import wx
import SpTest

class Myframe(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Speed calculater',size=(600,300))

        self.panel=wx.Panel(self) #create a pannel

        wx.StaticText(self.panel,-1,"""
                     This result is can be used a relative way to compare processing speed of computers
                                                                  &&&&&&
                     This result is calculated using average time taken by equal number of assigment,
                      randome number generation b/w 1 to 99,addition,subtraction, multipication,
                      division and lots of assignment operations
        
        """ ,(5,-1))
        
        button=wx.Button(self.panel,label="Start testing",pos=(225,120),size=(100,70)) #add button
        self.Bind(wx.EVT_BUTTON,self.startcal, button)  #bind button with an event

    def startcal(self,event): #event binded with button
        testSpeed = SpTest.SpeedTest() #create instance
        
        T_operation = testSpeed.operations()   #do all opearion it return  number of operation
        time_interval =testSpeed.stop_time() - testSpeed.start_time  #calculate time interval
        T_Speed = int(T_operation/time_interval)   # calculating Opearation/sec
        
        #wx.StaticText(self.panel,-1,"----->>> "  +str(T_Speed)+' Operation/Sec ',(100,220))

        custom = wx.StaticText(self.panel,-1,"   ------>>> "  +str(T_Speed)+' calculation/sec  <<<-----   ',(150,220),(260,-1))
        custom.SetForegroundColour('red')
        custom.SetBackgroundColour('white')
        
        #print "        ------>>> "  +str(testSpeed)+' calculation/sec"
        
if __name__=='__main__':
    app = wx.PySimpleApp()
    frame=Myframe(parent=None,id=-1)
    frame.Show()
    app.MainLoop()

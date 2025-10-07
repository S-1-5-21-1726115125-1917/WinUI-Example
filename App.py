from win32more.appsdk.xaml import XamlApplication,XamlType
from MainWindow import MainWindow,TypeKind
from Test1 import Test1Page
from Test2 import Test2Page

class App(XamlApplication):
    def OnLaunched(self,args):
        self.MainWindow=MainWindow()
        self.MainWindow.Activate()
    
    def GetXamlTypeByFullName(self,fullName):
        if fullName=="Test1":
            return XamlType("Test1",TypeKind.Custom,activate_instance=Test1Page)
        elif fullName=="Test2":
            return XamlType("Test2",TypeKind.Custom,activate_instance=Test2Page) #NotImplemented
        elif fullName=="Settings":
            return XamlType("Settings",TypeKind.Custom,activate_instance=Test1Page) #NotImplemented
        return super().GetXamlTypeByFullName(fullName)

XamlApplication.Start(App)
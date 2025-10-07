from win32more.appsdk.xaml import XamlClass
from win32more.Microsoft.UI.Xaml.Controls import Page
from pathlib import Path

class Test2Page(XamlClass,Page):
    def __init__(self):
        super().__init__(own=True)
        self.InitializeComponent()
    
    def InitializeComponent(self)->None:
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))
    
    def OnButtonClick(self,sender,args):
        self.TestButton.Content="已点击"
        args.Handled=True

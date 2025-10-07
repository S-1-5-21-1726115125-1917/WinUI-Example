from win32more.appsdk.xaml import XamlClass,xaml_typename
from win32more.winrt.base import unbox_value
from win32more.Microsoft.UI.Xaml import Window,RoutedEventArgs,Thickness
from win32more.Microsoft.UI.Xaml.Controls import NavigationViewItem,NavigationView,Frame,Grid,NavigationViewDisplayModeChangedEventArgs,NavigationViewDisplayMode,NavigationViewSelectionChangedEventArgs,NavigationViewBackRequestedEventArgs
from win32more.Windows.Foundation import IInspectable
from win32more.Windows.UI.Xaml.Interop import TypeKind
from win32more.Microsoft.UI.Windowing import OverlappedPresenter
from pathlib import Path

class MainWindow(XamlClass,Window):
    def __init__(self):
        super().__init__(own=True)
        self.InitializeComponent()
        self.MainNavView:NavigationView
        self.ContentFrame:Frame
        self.AppTitleBar:Grid
        Presenter:OverlappedPresenter=OverlappedPresenter.Create()
        Presenter.IsAlwaysOnTop=True
        self.AppWindow.SetPresenter(Presenter)
    
    def InitializeComponent(self)->None:
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))
    
    def OnWindowLoaded(self,sender:IInspectable,args:RoutedEventArgs)->None:
        self.MainNavView.SelectedItem=self.MainNavView.MenuItems[2] #自动触发选择事件
        args.Handled=True

    def OnNavigationSelectionChanged(self,sender:IInspectable,args:NavigationViewSelectionChangedEventArgs)->None:
        TagName:str=unbox_value(args.SelectedItem.as_(NavigationViewItem).Tag)
        print("[INFO] Navigate to page:"+TagName)
        self.ContentFrame.Navigate(xaml_typename(TagName,TypeKind.Custom))
    
    def OnBackRequested(self,sender:IInspectable,args:NavigationViewBackRequestedEventArgs):
        args.Handled=True
        pass #NotImplemented
    
    def OnDisplayModeChanged(self,sender:IInspectable,args:NavigationViewDisplayModeChangedEventArgs):
        if self.MainNavView.DisplayMode==NavigationViewDisplayMode.Minimal:
            self.AppTitleBar.Margin=Thickness(96,0,0,0)
        else:
            self.AppTitleBar.Margin=Thickness(48,0,0,0)


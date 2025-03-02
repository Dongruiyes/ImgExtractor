import wx
import wx.xrc
import os
import gettext
_ = gettext.gettext

# 导入对话框类
from ImgExtractor_Dialog1 import MyDialog3
from ImgExtractor_Dialog2 import MyDialog2
import ImgExtractor

class MyFrame2 ( wx.Frame ):

	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		self.SetBackgroundColour(wx.Colour( 239, 235, 235 ))

		self.m_statusBar2 = self.CreateStatusBar(1, wx.STB_DEFAULT_STYLE|wx.STB_SIZEGRIP, wx.ID_ANY)
		self.m_toolBar2 = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
		self.m_tool6 = self.m_toolBar2.AddLabelTool(wx.ID_ANY, _(u"tool"), wx.Bitmap( u"./icons/medglob64.dll_3685032.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, _(u"选择路径"), _(u"选择路径"), None)

		self.m_tool10 = self.m_toolBar2.AddLabelTool(wx.ID_ANY, _(u"tool"), wx.Bitmap( u"./icons/medglob64.dll_3698200.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, _(u"退出程序"), _(u"退出程序"), None)

		self.m_toolBar2.Realize()

		self.m_menubar3 = wx.MenuBar(0)
		self.m_menu12 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem(self.m_menu12, wx.ID_ANY, _(u"选择路径")+ u"\t" + u"Ctrl+I", _(u"选择路径Ctrl+I"), wx.ITEM_NORMAL)
		self.m_menuItem3.SetBitmap(wx.Bitmap( u"./icons/medglob64.dll_3669008.png", wx.BITMAP_TYPE_ANY ))
		self.m_menu12.Append(self.m_menuItem3)

		self.m_menu12.AppendSeparator()

		self.m_menuItem5 = wx.MenuItem(self.m_menu12, wx.ID_ANY, _(u"退出")+ u"\t" + u"Esc", _(u"退出程序"), wx.ITEM_NORMAL)
		self.m_menuItem5.SetBitmap(wx.Bitmap( u"./icons/medglob64.dll_3674376.png", wx.BITMAP_TYPE_ANY ))
		self.m_menu12.Append(self.m_menuItem5)

		self.m_menubar3.Append(self.m_menu12, _(u"文件"))

		self.m_menu15 = wx.Menu()
		self.m_menuItem8 = wx.MenuItem(self.m_menu15, wx.ID_ANY, _(u"关于ImgExtractor"), _(u"关于ImgExtractor"),
									   wx.ITEM_NORMAL)
		self.m_menuItem8.SetBitmap(wx.Bitmap(u"./icons/ImgExtractor-16.png", wx.BITMAP_TYPE_ANY))
		self.m_menu15.Append(self.m_menuItem8)

		self.m_menubar3.Append(self.m_menu15, _(u"帮助"))

		self.SetMenuBar(self.m_menubar3)

		bSizer2 = wx.BoxSizer(wx.VERTICAL)

		sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

		self.m_radioBtn3 = wx.RadioButton(self, wx.ID_ANY, _(u"扫描文件中的图标"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_radioBtn3.SetValue(True)
		sbSizer2.Add(self.m_radioBtn3, 0, wx.ALL, 5)

		self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, _(u"选择要提取图标的文件的完整路径，可以使用文件夹路径"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText3.Wrap(-1)

		sbSizer2.Add(self.m_staticText3, 0, wx.LEFT, 25)


		sbSizer2.Add((0, 10), 0, wx.EXPAND, 5)

		# 获取用户桌面路径
		desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
		self.m_dirPicker1 = wx.DirPickerCtrl(self, wx.ID_ANY, desktop_path, _(u"选择文件夹"), wx.DefaultPosition, wx.DefaultSize, wx.DIRP_CHANGE_DIR|wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL|wx.DIRP_USE_TEXTCTRL)
		sbSizer2.Add(self.m_dirPicker1, 0, wx.BOTTOM|wx.EXPAND|wx.RIGHT|wx.TOP, 5)


		sbSizer2.Add((0, 15), 0, wx.EXPAND, 5)

		sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _(u"图标类型")), wx.VERTICAL)

		gSizer3 = wx.GridSizer(3, 5, 0, 0)

		self.m_checkBox50 = wx.CheckBox(self, wx.ID_ANY, _(u".jpg"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_checkBox50.SetValue(True)
		gSizer3.Add(self.m_checkBox50, 0, wx.ALL, 5)

		self.m_checkBox51 = wx.CheckBox(self, wx.ID_ANY, _(u".png"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_checkBox51.SetValue(True)
		gSizer3.Add(self.m_checkBox51, 0, wx.ALL, 5)

		self.m_checkBox52 = wx.CheckBox(self, wx.ID_ANY, _(u".jpeg"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_checkBox52.SetValue(True)
		gSizer3.Add(self.m_checkBox52, 0, wx.ALL, 5)

		self.m_checkBox54 = wx.CheckBox(self, wx.ID_ANY, _(u".gif"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_checkBox54.SetValue(True)
		gSizer3.Add(self.m_checkBox54, 0, wx.ALL, 5)

		self.m_checkBox55 = wx.CheckBox(self, wx.ID_ANY, _(u".bmp"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_checkBox55.SetValue(True)
		gSizer3.Add(self.m_checkBox55, 0, wx.ALL, 5)

		self.m_checkBox56 = wx.CheckBox(self, wx.ID_ANY, _(u".ico"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_checkBox56.SetValue(True)
		gSizer3.Add(self.m_checkBox56, 0, wx.ALL, 5)

		self.m_checkBox57 = wx.CheckBox(self, wx.ID_ANY, _(u".webp"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_checkBox57.SetValue(True)
		gSizer3.Add(self.m_checkBox57, 0, wx.ALL, 5)

		self.m_checkBox58 = wx.CheckBox(self, wx.ID_ANY, _(u".svg"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_checkBox58.SetValue(True)
		gSizer3.Add(self.m_checkBox58, 0, wx.ALL, 5)

		self.m_checkBox59 = wx.CheckBox(self, wx.ID_ANY, _(u".heif"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_checkBox59.SetValue(True)
		gSizer3.Add(self.m_checkBox59, 0, wx.ALL, 5)

		self.m_checkBox60 = wx.CheckBox(self, wx.ID_ANY, _(u".psd"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_checkBox60.SetValue(True)
		gSizer3.Add(self.m_checkBox60, 0, wx.ALL, 5)

		self.m_checkBox61 = wx.CheckBox(self, wx.ID_ANY, _(u".raw"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_checkBox61.SetValue(True)
		gSizer3.Add(self.m_checkBox61, 0, wx.ALL, 5)

		self.m_checkBox62 = wx.CheckBox(self, wx.ID_ANY, _(u".tiff"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_checkBox62.SetValue(True)
		gSizer3.Add(self.m_checkBox62, 0, wx.ALL, 5)


		sbSizer3.Add(gSizer3, 1, wx.EXPAND, 5)


		sbSizer2.Add(sbSizer3, 1, wx.EXPAND|wx.RIGHT, 118)


		sbSizer2.Add((0, 5), 0, wx.EXPAND, 5)

		bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_button8 = wx.Button(self, wx.ID_ANY, _(u"提取图标"), wx.DefaultPosition, wx.DefaultSize, 0)

		self.m_button8.SetDefault()
		bSizer7.Add(self.m_button8, 0, wx.ALL, 5)

		sbSizer2.Add(bSizer7, 0, wx.ALIGN_RIGHT, 5)


		bSizer2.Add(sbSizer2, 1, wx.ALL|wx.EXPAND, 10)


		self.SetSizer( bSizer2 )
		self.Layout()
		bSizer2.Fit( self )

		self.Centre(wx.BOTH)

		# Connect Events
		self.Bind(wx.EVT_TOOL, self.Path, id = self.m_tool6.GetId())
		self.Bind(wx.EVT_TOOL, self.exit, id = self.m_tool10.GetId())
		self.Bind(wx.EVT_MENU, self.Path, id = self.m_menuItem3.GetId())
		self.Bind(wx.EVT_MENU, self.exit, id = self.m_menuItem5.GetId())
		self.Bind(wx.EVT_MENU, self.about, id = self.m_menuItem8.GetId())
		self.m_button8.Bind(wx.EVT_BUTTON, self.extract)

	def __del__( self ):
		# Disconnect Events
		pass

	def Path( self, event ):
		dlg = wx.DirDialog(self, u"选择文件夹", style=wx.DD_DEFAULT_STYLE)
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			self.m_dirPicker1.SetPath(path)
		dlg.Destroy()

	def exit( self, event ):
		# event.Skip()
		# 关闭程序
		self.Close()



	def about( self, event ):
		# event.Skip()
		dlg = MyDialog2(self)
		dlg.ShowModal()
		dlg.Destroy()

	def extract( self, event ):
		self.selected_path = self.m_dirPicker1.GetPath()

		# 存储勾选的 wx.CheckBox 的 label 名称
		self.selected_checkboxes = set()
		for checkbox in [
			self.m_checkBox50, self.m_checkBox51, self.m_checkBox52,
			self.m_checkBox54, self.m_checkBox55, self.m_checkBox56, self.m_checkBox57,
			self.m_checkBox58, self.m_checkBox59, self.m_checkBox60, self.m_checkBox61,
			self.m_checkBox62
		]:
			if checkbox.GetValue():
				self.selected_checkboxes.add(checkbox.GetLabel())
		# print(self.selected_checkboxes)
		ImgExtractor.SUPPORTED_IMAGE_FORMATS = self.selected_checkboxes

		dlg = MyDialog3(self)
		dlg.ShowModal()
		dlg.Destroy()

class myApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame2(None)
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()

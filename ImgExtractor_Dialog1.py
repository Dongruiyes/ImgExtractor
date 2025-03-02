import wx
import wx.xrc
import os
import gettext
_ = gettext.gettext
import ImgExtractor

class MyDialog3 ( wx.Dialog ):

	def __init__(self, parent):
		wx.Dialog.__init__ (self, parent, id = wx.ID_ANY, title = _(u"保存选定的图标"), pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.STAY_ON_TOP)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		bSizer14 = wx.BoxSizer(wx.VERTICAL)

		sbSizer11 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

		self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, _(u"选择保存文件夹路径："), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText6.Wrap(-1)

		sbSizer11.Add(self.m_staticText6, 0, wx.RIGHT, 360)

		# 获取用户桌面路径
		desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

		self.m_filePicker1 = wx.DirPickerCtrl(self, wx.ID_ANY, desktop_path, _(u"选择文件夹"), wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE | wx.DIRP_SMALL | wx.FLP_USE_TEXTCTRL)
		sbSizer11.Add(self.m_filePicker1, 0, wx.BOTTOM|wx.EXPAND|wx.RIGHT|wx.TOP, 5)

		bSizer16 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_button8 = wx.Button(self, wx.ID_ANY, _(u"开始执行"), wx.DefaultPosition, wx.DefaultSize, 0)

		self.m_button8.SetDefault()
		bSizer16.Add(self.m_button8, 0, wx.ALL, 5)

		self.m_button9 = wx.Button(self, wx.ID_ANY, _(u"取消"), wx.DefaultPosition, wx.DefaultSize, 0)

		self.m_button9.SetDefault()
		bSizer16.Add(self.m_button9, 0, wx.ALL, 5)


		sbSizer11.Add(bSizer16, 0, wx.ALIGN_RIGHT, 5)


		bSizer14.Add(sbSizer11, 1, wx.ALL, 15)


		self.SetSizer( bSizer14 )
		self.Layout()
		bSizer14.Fit( self )

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_button8.Bind(wx.EVT_BUTTON, self.Execution)
		self.m_button9.Bind(wx.EVT_BUTTON, self.cancel)

	def Execution( self, event ):
		# 获取用户选择的输出目录
		self.output_directory = self.m_filePicker1.GetPath()
		# 获取需要提取图片的目录
		self.selected_path = self.Parent.selected_path
		# 调用 ImgExtractor.py 的 main 函数

		# 关闭当前窗口
		self.Hide()
		# self.Parent.m_statusBar2状态栏增加显示："图标提取中"
		self.Parent.m_statusBar2.SetStatusText(_(u"图标提取中，请勿关闭窗口···"))

		ImgExtractor.m_statusBar2 = self.Parent.m_statusBar2
		try:
			ImgExtractor.main(self.selected_path, self.output_directory)
			# print(output_directory)
			# 待程序结束后self.m_statusBar2状态栏显示处理完成
			self.Parent.m_statusBar2.SetStatusText(_(u"文件/文件夹：{}").format(os.path.basename(self.selected_path)) + _(u" 图标提取完成"))
			# 打开输出目录
			wx.LaunchDefaultApplication(self.output_directory)
		except Exception as e:
			self.Parent.m_statusBar2.SetStatusText(f"Error: {e}")

		self.Destroy()



	def cancel( self, event ):
		self.Destroy()




class myApp(wx.App):
    def  OnInit(self):
        self.frame = MyDialog3(None)
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()
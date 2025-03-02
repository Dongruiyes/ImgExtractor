import wx
import wx.xrc
import wx.adv
import gettext
import os
import sys
_ = gettext.gettext

class MyDialog2 ( wx.Dialog ):

	def __init__(self, parent):
		wx.Dialog.__init__ (self, parent, id = wx.ID_ANY, title = _(u"关于ImgExtractor"), pos = wx.DefaultPosition,
							size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.STAY_ON_TOP)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		self.SetFont(wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ))

		bSizer7 = wx.BoxSizer(wx.VERTICAL)

		bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

		self.running_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
		self.icon_path = os.path.join(self.running_dir, "icons", "Logo-64.png")
		self.m_bitmap3 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(self.icon_path, wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer6.Add(self.m_bitmap3, 0, wx.ALL, 20)

		self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, _(u"ImgExtractor v1.0\nCopyright (©)™ 2025-2030 DONG"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText2.Wrap(-1)

		self.m_staticText2.SetFont(wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI" ))

		bSizer6.Add(self.m_staticText2, 0, wx.EXPAND|wx.RIGHT|wx.TOP, 28)


		bSizer7.Add(bSizer6, 0, wx.EXPAND, 5)

		bSizer9 = wx.BoxSizer(wx.VERTICAL)

		self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, _(u"作者主页："), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText3.Wrap(-1)

		bSizer9.Add(self.m_staticText3, 0, wx.LEFT, 20)


		bSizer9.Add((0, 5), 1, wx.EXPAND, 5)

		self.m_hyperlink1 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, _(u"https://github.com/Dongruiyes"), u"https://github.com/Dongruiyes", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_CONTEXTMENU|wx.adv.HL_DEFAULT_STYLE)

		self.m_hyperlink1.SetNormalColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ))
		self.m_hyperlink1.SetFont(wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ))

		bSizer9.Add(self.m_hyperlink1, 0, wx.BOTTOM|wx.EXPAND|wx.LEFT, 20)


		bSizer7.Add(bSizer9, 0, wx.EXPAND, 5)

		bSizer61 = wx.BoxSizer(wx.VERTICAL)

		self.m_button31 = wx.Button(self, wx.ID_ANY, _(u"确定"), wx.DefaultPosition, wx.DefaultSize, 0)

		self.m_button31.SetDefault()
		bSizer61.Add(self.m_button31, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT, 10)


		bSizer7.Add(bSizer61, 0, wx.EXPAND|wx.RIGHT, 5)


		self.SetSizer( bSizer7 )
		self.Layout()
		bSizer7.Fit( self )

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_button31.Bind(wx.EVT_BUTTON, self.esc)

	def __del__( self ):
		pass

	def esc( self, event ):
		# event.Skip()
		# 关闭对话框
		self.Close()


class myApp(wx.App):
    def  OnInit(self):
        self.frame = MyDialog2(None)
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()
#!/usr/bin/env python3
#
# 2019年 05月 05日 星期日 20:43:40 CST

import wx
from wx.lib.scrolledpanel import ScrolledPanel
cb = wx.CheckBox
cbb = wx.ComboBox
ci = wx.Choice
sl = wx.Slider
sp = wx.SpinCtrl
st = wx.StaticText
tc = wx.TextCtrl


class Page1Notebook(wx.Notebook):
  def __init__(self, parent, handlers):
    '''
    最大的宽应该是由最长的 request定制的第一行 决定

    以"其他"标签的height作为标准高,
    高于此height的标签页使用ScrolledPanel, 显示滚动条
    '''
    super().__init__(parent)

    self._handlers = handlers

    page1_setting = self.build_page1_setting()
    page1_request = self.build_page1_request()
    page1_enumeration = self.build_page1_enumeration()
    page1_file = self.build_page1_file()
    page1_other = self.build_page1_other()

    self.AddPage(page1_setting, '测试(&Q)')
    self.AddPage(page1_request, '请求(&W)')
    self.AddPage(page1_enumeration, '枚举(&E)')
    self.AddPage(page1_file, '文件(&E)')
    self.AddPage(page1_other, '其他(&T)')

  def build_page1_other(self):
    p = wx.Panel(self)

    vbox = wx.BoxSizer(wx.VERTICAL)
    page1_other_general_area = self.build_page1_other_general(p)
    page1_other_misc_area = self.build_page1_other_misc(p)

    expand_border = wx.SizerFlags().Expand().Border(wx.LEFT | wx.RIGHT, 5)

    vbox.Add(page1_other_general_area, expand_border)
    vbox.Add(page1_other_misc_area, expand_border)
    p.SetSizerAndFit(vbox)
    return p

  def build_page1_other_misc(self, panel):
    page1_other_misc_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '杂项')
    _page1_other_misc_area = page1_other_misc_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 5)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 5)

    row1 = wx.BoxSizer()
    self._page1_misc_web_root_ckbtn = cb(_page1_other_misc_area, label = '远程web的root目录')
    self._page1_misc_web_root_entry = tc(_page1_other_misc_area)
    self._page1_misc_tmp_dir_ckbtn = cb(_page1_other_misc_area, label = '本地临时目录')
    self._page1_misc_tmp_dir_entry = tc(_page1_other_misc_area)
    self._page1_misc_tmp_dir_chooser = wx.Button(_page1_other_misc_area, label = '打开')
    self._page1_misc_tmp_dir_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._page1_misc_tmp_dir_entry, '选择 本地临时目录']:
        self._handlers.set_file_entry_text(evt, data))

    row1.Add(self._page1_misc_web_root_ckbtn, border)
    row1.Add(self._page1_misc_web_root_entry, proportion_border)
    row1.Add(self._page1_misc_tmp_dir_ckbtn, border)
    row1.Add(self._page1_misc_tmp_dir_entry, proportion = 1)
    row1.Add(self._page1_misc_tmp_dir_chooser, border)

    row2 = wx.BoxSizer()
    self._page1_misc_identify_waf_ckbtn = cb(_page1_other_misc_area, label = '鉴别WAF')
    self._page1_misc_skip_waf_ckbtn = cb(_page1_other_misc_area, label = '跳过对WAF/IPS保护的启发式侦测')
    self._page1_misc_smart_ckbtn = cb(_page1_other_misc_area, label = '只对明显注入点进行详细测试')
    self._page1_misc_list_tampers_ckbtn = cb(_page1_other_misc_area, label = '列出可用的tamper脚本')
    self._page1_misc_sqlmap_shell_ckbtn = cb(_page1_other_misc_area, label = '打开sqlmap交互shell')
    self._page1_misc_disable_color_ckbtn = cb(_page1_other_misc_area, label = '禁用终端输出的颜色')

    row2.Add(self._page1_misc_identify_waf_ckbtn, border)
    row2.Add(self._page1_misc_skip_waf_ckbtn, border)
    row2.Add(self._page1_misc_smart_ckbtn, border)
    row2.Add(self._page1_misc_list_tampers_ckbtn, border)
    row2.Add(self._page1_misc_sqlmap_shell_ckbtn, border)
    row2.Add(self._page1_misc_disable_color_ckbtn, border)

    row3 = wx.BoxSizer()
    self._page1_misc_offline_ckbtn = cb(_page1_other_misc_area, label = '离线模式(只使用保存的会话数据)')
    self._page1_misc_mobile_ckbtn = cb(_page1_other_misc_area, label = '模拟手机请求')
    self._page1_misc_beep_ckbtn = cb(_page1_other_misc_area, label = '响铃')
    self._page1_misc_purge_ckbtn = cb(_page1_other_misc_area, label = '彻底清除所有记录')
    self._page1_misc_dependencies_ckbtn = cb(_page1_other_misc_area, label = '检查丢失的(非核心的)sqlmap依赖')
    self._page1_general_update_ckbtn = cb(_page1_other_misc_area, label = '更新sqlmap')

    row3.Add(self._page1_misc_offline_ckbtn, border)
    row3.Add(self._page1_misc_mobile_ckbtn, border)
    row3.Add(self._page1_misc_beep_ckbtn, border)
    row3.Add(self._page1_misc_purge_ckbtn, border)
    row3.Add(self._page1_misc_dependencies_ckbtn, border)
    row3.Add(self._page1_general_update_ckbtn, border)

    row4 = wx.BoxSizer()
    self._page1_misc_answers_ckbtn = cb(_page1_other_misc_area, label = '设置交互时的问题答案:')
    self._page1_misc_answers_entry = tc(_page1_other_misc_area)
    self._page1_misc_alert_ckbtn = cb(_page1_other_misc_area, label = '发现注入时运行本地命令:')
    self._page1_misc_alert_entry = tc(_page1_other_misc_area)
    self._page1_misc_gpage_ckbtn = cb(_page1_other_misc_area, label = 'GOOGLEDORK时的页码')
    self._page1_misc_gpage_spinbtn = sp(_page1_other_misc_area, value = '1', min = 1, max = 100)

    row4.Add(self._page1_misc_answers_ckbtn, border)
    row4.Add(self._page1_misc_answers_entry, proportion_border)
    row4.Add(self._page1_misc_alert_ckbtn, border)
    row4.Add(self._page1_misc_alert_entry, proportion_border)
    row4.Add(self._page1_misc_gpage_ckbtn, border)
    row4.Add(self._page1_misc_gpage_spinbtn, border)

    row5 = wx.BoxSizer()
    self._page1_misc_z_ckbtn = cb(_page1_other_misc_area, label = '使用短的助记符')
    self._page1_misc_z_entry = tc(_page1_other_misc_area)

    row5.Add(self._page1_misc_z_ckbtn, border)
    row5.Add(self._page1_misc_z_entry, proportion_border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 3)
    page1_other_misc_area.Add(row1, spacing)
    page1_other_misc_area.Add(row2, spacing)
    page1_other_misc_area.Add(row3, spacing)
    page1_other_misc_area.Add(row4, spacing)
    page1_other_misc_area.Add(row5, spacing)

    return page1_other_misc_area

  def build_page1_other_general(self, panel):
    page1_other_general_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '通用项')
    _page1_other_general_area = page1_other_general_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 5)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 5)

    row1 = wx.BoxSizer()
    self._page1_general_check_internet_ckbtn = cb(_page1_other_general_area, label = '检查与目标的网络连接')
    self._page1_general_fresh_queries_ckbtn = cb(_page1_other_general_area, label = '刷新此次查询')
    self._page1_general_flush_session_ckbtn = cb(_page1_other_general_area, label = '清空目标的会话文件')
    self._page1_general_eta_ckbtn = cb(_page1_other_general_area, label = '显示剩余时间')
    self._page1_general_binary_fields_ckbtn = cb(_page1_other_general_area, label = '生成有二进制值的字段')
    self._page1_general_binary_fields_entry = tc(_page1_other_general_area)

    row1.Add(self._page1_general_check_internet_ckbtn, border)
    row1.Add(self._page1_general_fresh_queries_ckbtn, border)
    row1.Add(self._page1_general_flush_session_ckbtn, border)
    row1.Add(self._page1_general_eta_ckbtn, border)
    row1.Add(self._page1_general_binary_fields_ckbtn, border)
    row1.Add(self._page1_general_binary_fields_entry, border)

    row2 = wx.BoxSizer()
    self._page1_general_forms_ckbtn = cb(_page1_other_general_area, label = '解析和测试目标url内的表单')
    self._page1_general_parse_errors_ckbtn = cb(_page1_other_general_area, label = '解析并显示DB错误信息')
    self._page1_misc_cleanup_ckbtn = cb(_page1_other_general_area, label = '清理DBMS中sqlmap产生的UDF和表')
    self._page1_general_preprocess_ckbtn = cb(_page1_other_general_area, label = '指定预处理响应数据的脚本')
    self._page1_general_preprocess_entry = tc(_page1_other_general_area)
    self._page1_general_preprocess_chooser = wx.Button(_page1_other_general_area, label = '打开')
    self._page1_general_preprocess_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._page1_general_preprocess_entry]:
        self._handlers.set_file_entry_text(evt, data))

    row2.Add(self._page1_general_forms_ckbtn, border)
    row2.Add(self._page1_general_parse_errors_ckbtn, border)
    row2.Add(self._page1_misc_cleanup_ckbtn, border)
    row2.Add(self._page1_general_preprocess_ckbtn, border)
    row2.Add(self._page1_general_preprocess_entry, proportion = 1)
    row2.Add(self._page1_general_preprocess_chooser, border)

    row3 = wx.BoxSizer()
    self._page1_general_crawl_ckbtn = cb(_page1_other_general_area, label = '爬网站(的层级/深度)')
    self._page1_general_crawl_entry = tc(_page1_other_general_area)
    self._page1_general_crawl_exclude_ckbtn = cb(_page1_other_general_area, label = '爬站时排除(正则)页面')
    self._page1_general_crawl_exclude_entry = tc(_page1_other_general_area)

    row3.Add(self._page1_general_crawl_ckbtn, border)
    row3.Add(self._page1_general_crawl_entry, proportion_border)
    row3.Add(self._page1_general_crawl_exclude_ckbtn, border)
    row3.Add(self._page1_general_crawl_exclude_entry, proportion_border)

    row4 = wx.BoxSizer()
    self._page1_general_charset_ckbtn = cb(_page1_other_general_area, label = '盲注所用的字符集合')
    self._page1_general_charset_entry = tc(_page1_other_general_area)
    self._page1_general_encoding_ckbtn = cb(_page1_other_general_area, label = '字符编码(用于数据获取)')
    self._page1_general_encoding_entry = tc(_page1_other_general_area)

    row4.Add(self._page1_general_charset_ckbtn, border)
    row4.Add(self._page1_general_charset_entry, proportion_border)
    row4.Add(self._page1_general_encoding_ckbtn, border)
    row4.Add(self._page1_general_encoding_entry, border)

    row5 = wx.BoxSizer()
    self._page1_general_session_file_ckbtn = cb(_page1_other_general_area, label = '指定会话文件')
    self._page1_general_session_file_entry = tc(_page1_other_general_area)
    self._page1_general_session_file_chooser = wx.Button(_page1_other_general_area, label = '打开')
    self._page1_general_session_file_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._page1_general_session_file_entry]:
        self._handlers.set_file_entry_text(evt, data))

    self._page1_general_output_dir_ckbtn = cb(_page1_other_general_area, label = '输出的保存目录')
    self._page1_general_output_dir_entry = tc(_page1_other_general_area)
    self._page1_general_output_dir_chooser = wx.Button(_page1_other_general_area, label = '打开')
    self._page1_general_output_dir_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._page1_general_output_dir_entry, '选择 结果保存在哪']:
        self._handlers.set_file_entry_text(evt, data))

    row5.Add(self._page1_general_session_file_ckbtn, border)
    row5.Add(self._page1_general_session_file_entry, proportion = 1)
    row5.Add(self._page1_general_session_file_chooser, border)
    row5.Add(self._page1_general_output_dir_ckbtn, border)
    row5.Add(self._page1_general_output_dir_entry, proportion = 1)
    row5.Add(self._page1_general_output_dir_chooser, border)

    row6 = wx.BoxSizer()
    self._page1_general_dump_format_ckbtn = cb(_page1_other_general_area, label = 'dump结果的文件格式')
    self._page1_general_dump_format_entry = tc(_page1_other_general_area)
    self._page1_general_csv_del_ckbtn = cb(_page1_other_general_area, label = '(csv文件的)分隔符')
    self._page1_general_csv_del_entry = tc(_page1_other_general_area)

    row6.Add(self._page1_general_dump_format_ckbtn, border)
    row6.Add(self._page1_general_dump_format_entry, border)
    row6.Add(self._page1_general_csv_del_ckbtn, border)
    row6.Add(self._page1_general_csv_del_entry, border)

    row7 = wx.BoxSizer()
    self._page1_general_traffic_file_ckbtn = cb(_page1_other_general_area, label = '转存所有http流量到文本')
    self._page1_general_traffic_file_entry = tc(_page1_other_general_area)
    self._page1_general_traffic_file_chooser = wx.Button(_page1_other_general_area, label = '打开')
    self._page1_general_traffic_file_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._page1_general_traffic_file_entry]:
        self._handlers.set_file_entry_text(evt, data))

    self._page1_general_har_ckbtn = cb(_page1_other_general_area, label = '转存至HAR文件')
    self._page1_general_har_entry = tc(_page1_other_general_area)
    self._page1_general_har_chooser = wx.Button(_page1_other_general_area, label = '打开')
    self._page1_general_har_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._page1_general_har_entry]:
        self._handlers.set_file_entry_text(evt, data))

    row7.Add(self._page1_general_traffic_file_ckbtn, border)
    row7.Add(self._page1_general_traffic_file_entry, proportion = 1)
    row7.Add(self._page1_general_traffic_file_chooser, border)
    row7.Add(self._page1_general_har_ckbtn, border)
    row7.Add(self._page1_general_har_entry, proportion = 1)
    row7.Add(self._page1_general_har_chooser, border)

    row8 = wx.BoxSizer()
    self._page1_general_save_ckbtn = cb(_page1_other_general_area, label = '保存选项至INI文件')
    self._page1_general_save_entry = tc(_page1_other_general_area)
    self._page1_general_save_chooser = wx.Button(_page1_other_general_area, label = '打开')
    self._page1_general_save_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._page1_general_save_entry]:
        self._handlers.set_file_entry_text(evt, data))

    self._page1_general_scope_ckbtn = cb(_page1_other_general_area, label = '从代理日志过滤出目标(正则)')
    self._page1_general_scope_entry = tc(_page1_other_general_area)
    self._page1_general_scope_chooser = wx.Button(_page1_other_general_area, label = '打开')
    self._page1_general_scope_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._page1_general_scope_entry]:
        self._handlers.set_file_entry_text(evt, data))

    row8.Add(self._page1_general_save_ckbtn, border)
    row8.Add(self._page1_general_save_entry, proportion = 1)
    row8.Add(self._page1_general_save_chooser, border)
    row8.Add(self._page1_general_scope_ckbtn, border)
    row8.Add(self._page1_general_scope_entry, proportion = 1)
    row8.Add(self._page1_general_scope_chooser, border)

    row9 = wx.BoxSizer()
    self._page1_general_test_filter_ckbtn = cb(_page1_other_general_area, label = '测试过滤器(从payload/title选择)')
    self._page1_general_test_filter_entry = tc(_page1_other_general_area)
    self._page1_general_test_skip_ckbtn = cb(_page1_other_general_area, label = '测试跳过(从payload/title选择)')
    self._page1_general_test_skip_entry = tc(_page1_other_general_area)

    row9.Add(self._page1_general_test_filter_ckbtn, border)
    row9.Add(self._page1_general_test_filter_entry, proportion_border)
    row9.Add(self._page1_general_test_skip_ckbtn, border)
    row9.Add(self._page1_general_test_skip_entry, proportion_border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 3)
    page1_other_general_area.Add(row1, spacing)
    page1_other_general_area.Add(row2, spacing)
    page1_other_general_area.Add(row3, spacing)
    page1_other_general_area.Add(row4, spacing)
    page1_other_general_area.Add(row5, spacing)
    page1_other_general_area.Add(row6, spacing)
    page1_other_general_area.Add(row7, spacing)
    page1_other_general_area.Add(row8, spacing)
    page1_other_general_area.Add(row9, spacing)

    return page1_other_general_area

  def build_page1_file(self):
    p = wx.Panel(self)

    vbox = wx.BoxSizer(wx.VERTICAL)
    file_read_area = self.build_page1_file_read(p)
    file_write_area = self.build_page1_file_write(p)
    file_os_access_area = self.build_page1_file_os_access(p)
    file_os_registry_area = self.build_page1_file_os_registry(p)

    vbox.Add(file_read_area, flag = wx.EXPAND | wx.ALL, border = 15)
    vbox.Add(file_write_area, flag = wx.EXPAND | wx.ALL, border = 15)
    vbox.Add(file_os_access_area, flag = wx.EXPAND | wx.ALL, border = 15)
    vbox.Add(file_os_registry_area, flag = wx.EXPAND | wx.ALL, border = 15)
    p.SetSizerAndFit(vbox)
    return p

  def build_page1_file_os_registry(self, panel):
    file_os_registry_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '访问WIN下注册表')
    _file_os_registry_area = file_os_registry_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 5)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 5)

    row1 = wx.BoxSizer()
    self._file_os_registry_reg_ckbtn = cb(_file_os_registry_area, label = '键值操作:')
    self._file_os_registry_reg_choice = ci(_file_os_registry_area,
                                           choices = ['--reg-read', '--reg-add', '--reg-del'])
    self._file_os_registry_reg_choice.SetSelection(0)

    row1.Add(self._file_os_registry_reg_ckbtn, border)
    row1.Add(self._file_os_registry_reg_choice, border)

    row2 = wx.BoxSizer()
    self._file_os_registry_reg_key_label = st(_file_os_registry_area, label = '键')
    self._file_os_registry_reg_key_entry = tc(_file_os_registry_area)
    self._file_os_registry_reg_value_label = st(_file_os_registry_area, label = '值')
    self._file_os_registry_reg_value_entry = tc(_file_os_registry_area)

    row2.Add(self._file_os_registry_reg_key_label, border)
    row2.Add(self._file_os_registry_reg_key_entry, proportion_border)
    row2.Add(self._file_os_registry_reg_value_label, border)
    row2.Add(self._file_os_registry_reg_value_entry, proportion_border)

    row3 = wx.BoxSizer()
    self._file_os_registry_reg_data_label = st(_file_os_registry_area, label = '数据')
    self._file_os_registry_reg_data_entry = tc(_file_os_registry_area)
    self._file_os_registry_reg_type_label = st(_file_os_registry_area, label = '类型')
    self._file_os_registry_reg_type_entry = tc(_file_os_registry_area)

    row3.Add(self._file_os_registry_reg_data_label, border)
    row3.Add(self._file_os_registry_reg_data_entry, proportion_border)
    row3.Add(self._file_os_registry_reg_type_label, border)
    row3.Add(self._file_os_registry_reg_type_entry, proportion_border)

    file_os_registry_area.Add(row1, flag = wx.EXPAND)
    file_os_registry_area.Add(row2, flag = wx.EXPAND)
    file_os_registry_area.Add(row3, flag = wx.EXPAND)

    return file_os_registry_area

  def build_page1_file_os_access(self, panel):
    file_os_access_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '访问后端OS')
    _file_os_access_area = file_os_access_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 5)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 5)

    row1 = wx.BoxSizer()
    self._file_os_access_os_cmd_ckbtn = cb(_file_os_access_area, label = '执行CLI命令')
    self._file_os_access_os_cmd_entry = tc(_file_os_access_area)

    row1.Add(self._file_os_access_os_cmd_ckbtn, border)
    row1.Add(self._file_os_access_os_cmd_entry, proportion_border)

    row2 = wx.BoxSizer()
    self._file_os_access_os_shell_ckbtn = cb(_file_os_access_area, label = '获取交互shell')
    self._file_os_access_os_pwn_ckbtn = cb(_file_os_access_area, label = '--os-pwn')
    self._file_os_access_os_smbrelay_ckbtn = cb(_file_os_access_area, label = '--os-smbrelay')
    self._file_os_access_os_bof_ckbtn = cb(_file_os_access_area, label = '--os-bof')
    self._file_os_access_priv_esc_ckbtn = cb(_file_os_access_area, label = '--priv-esc')

    row2.Add(self._file_os_access_os_shell_ckbtn, border)
    row2.Add(self._file_os_access_os_pwn_ckbtn, border)
    row2.Add(self._file_os_access_os_smbrelay_ckbtn, border)
    row2.Add(self._file_os_access_os_bof_ckbtn, border)
    row2.Add(self._file_os_access_priv_esc_ckbtn, border)

    row3 = wx.BoxSizer()
    self._file_os_access_msf_path_ckbtn = cb(_file_os_access_area, label = '本地Metasploit安装路径')
    self._file_os_access_msf_path_entry = tc(_file_os_access_area)
    self._file_os_access_msf_path_chooser = wx.Button(_file_os_access_area, label = '打开')
    self._file_os_access_msf_path_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._file_os_access_msf_path_entry, '选择 本地Metasploit安装目录']:
        self._handlers.set_file_entry_text(evt, data))

    self._file_os_access_tmp_path_ckbtn = cb(_file_os_access_area, label = '远程临时目录(绝对路径)')
    self._file_os_access_tmp_path_entry = tc(_file_os_access_area)

    row3.Add(self._file_os_access_msf_path_ckbtn, border)
    row3.Add(self._file_os_access_msf_path_entry, proportion = 1)
    row3.Add(self._file_os_access_msf_path_chooser, border)
    row3.Add(self._file_os_access_tmp_path_ckbtn, border)
    row3.Add(self._file_os_access_tmp_path_entry, proportion_border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 3)
    file_os_access_area.Add(row1, spacing)
    file_os_access_area.Add(row2, spacing)
    file_os_access_area.Add(row3, spacing)

    return file_os_access_area

  def build_page1_file_write(self, panel):
    file_write_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '文件上传')
    _file_write_area = file_write_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 5)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 5)

    row1 = wx.BoxSizer()
    self._file_write_area_udf_ckbtn = cb(_file_write_area, label = '注入(默认sqlmap自带的)用户定义函数')
    self._file_write_area_shared_lib_ckbtn = cb(_file_write_area, label = '本地共享库路径(--shared-lib=)')
    self._file_write_area_shared_lib_entry = tc(_file_write_area)
    self._file_write_area_shared_lib_chooser = wx.Button(_file_write_area, label = '打开')
    self._file_write_area_shared_lib_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._file_write_area_shared_lib_entry]:
        self._handlers.set_file_entry_text(evt, data))

    row1.Add(self._file_write_area_udf_ckbtn, border)
    row1.Add(self._file_write_area_shared_lib_ckbtn, border)
    row1.Add(self._file_write_area_shared_lib_entry, proportion = 1)
    row1.Add(self._file_write_area_shared_lib_chooser, border)

    row2 = wx.BoxSizer()
    self._file_write_area_file_write_ckbtn = cb(_file_write_area, label = '本地文件路径(--file-write=)')
    self._file_write_area_file_write_entry = tc(_file_write_area)
    self._file_write_area_file_write_chooser = wx.Button(_file_write_area, label = '打开')
    self._file_write_area_file_write_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._file_write_area_file_write_entry]:
        self._handlers.set_file_entry_text(evt, data))

    row2.Add(self._file_write_area_file_write_ckbtn, border)
    row2.Add(self._file_write_area_file_write_entry, proportion = 1)
    row2.Add(self._file_write_area_file_write_chooser, border)

    row3 = wx.BoxSizer()
    self._file_write_area_file_dest_ckbtn = cb(_file_write_area, label = '远程文件路径(--file-dest=)')
    self._file_write_area_file_dest_entry = tc(_file_write_area)

    row3.Add(self._file_write_area_file_dest_ckbtn, border)
    row3.Add(self._file_write_area_file_dest_entry, proportion_border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 6)
    file_write_area.Add(row1, spacing)
    file_write_area.Add(row2, spacing)
    file_write_area.Add(row3, spacing)

    return file_write_area

  def build_page1_file_read(self, panel):
    file_read_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '读取远程文件')
    _file_read_area = file_read_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 10)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 10)

    row1 = wx.BoxSizer()
    self._file_read_area_file_read_ckbtn = cb(_file_read_area, label = '远程文件路径(--file-read=)')
    self._file_read_area_file_read_entry = tc(_file_read_area)

    row1.Add(self._file_read_area_file_read_ckbtn, border)
    row1.Add(self._file_read_area_file_read_entry, proportion_border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 6)
    file_read_area.Add(row1, spacing)

    return file_read_area

  def build_page1_enumeration(self):
    p = wx.Panel(self)

    hbox1 = wx.BoxSizer()
    enum_area = self.build_page1_enumeration_enum(p)
    dump_area = self.build_page1_enumeration_dump(p)
    limit_area = self.build_page1_enumeration_limit(p)
    blind_area = self.build_page1_enumeration_blind(p)

    spacing = wx.SizerFlags().Expand().Border(wx.ALL, 15)
    hbox1.Add(enum_area, spacing)
    hbox1.Add(dump_area, spacing)
    hbox1.Add(limit_area, spacing)
    hbox1.Add(blind_area, spacing)

    hbox2 = wx.BoxSizer()
    meta_area = self.build_page1_enumeration_meta(p)
    hbox2.Add(meta_area, proportion = 1, flag = wx.ALL, border = 15)

    hbox3 = wx.BoxSizer()
    runsql_area = self.build_page1_enumeration_runsql(p)
    hbox3.Add(runsql_area, proportion = 1, flag = wx.ALL, border = 15)

    hbox4 = wx.BoxSizer()
    brute_force_area = self.build_page1_enumeration_brute_force(p)
    hbox4.Add(brute_force_area, flag = wx.ALL, border = 15)

    vbox = wx.BoxSizer(wx.VERTICAL)
    vbox.Add(hbox1)
    vbox.Add(hbox2, flag = wx.EXPAND)
    vbox.Add(hbox3, flag = wx.EXPAND)
    vbox.Add(hbox4)
    p.SetSizerAndFit(vbox)
    return p

  def build_page1_enumeration_brute_force(self, panel):
    brute_force_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '暴破表名/列名')
    _brute_force_area = brute_force_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 6)

    row1 = wx.BoxSizer()
    self._brute_force_area_common_tables_ckbtn = cb(_brute_force_area, label = '常用表名')
    self._brute_force_area_common_columns_ckbtn = cb(_brute_force_area, label = '常用列名')

    row1.Add(st(_brute_force_area, label = '检查是否存在:'), border)
    row1.Add(self._brute_force_area_common_tables_ckbtn, border)
    row1.Add(self._brute_force_area_common_columns_ckbtn, border)

    brute_force_area.Add(row1, flag = wx.EXPAND | wx.ALL, border = 6)

    return brute_force_area

  def build_page1_enumeration_runsql(self, panel):
    runsql_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '执行SQL语句')
    _runsql_area = runsql_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 10)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 10)

    row1 = wx.BoxSizer()
    self._runsql_area_sql_query_ckbtn = cb(_runsql_area, label = 'SQL语句:')
    self._runsql_area_sql_query_entry = tc(_runsql_area)

    row1.Add(self._runsql_area_sql_query_ckbtn, border)
    row1.Add(self._runsql_area_sql_query_entry, proportion_border)

    row2 = wx.BoxSizer()
    self._runsql_area_sql_shell_ckbtn = cb(_runsql_area, label = '打开个SQL交互shell')
    self._runsql_area_sql_file_ckbtn = cb(_runsql_area, label = '本地SQL文件:')
    self._runsql_area_sql_file_entry = tc(_runsql_area)
    self._runsql_area_sql_file_chooser = wx.Button(_runsql_area, label = '打开')
    self._runsql_area_sql_file_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._runsql_area_sql_file_entry]:
        self._handlers.set_file_entry_text(evt, data))

    row2.Add(self._runsql_area_sql_shell_ckbtn, border)
    row2.Add(self._runsql_area_sql_file_ckbtn, border)
    row2.Add(self._runsql_area_sql_file_entry, proportion = 1)
    row2.Add(self._runsql_area_sql_file_chooser, border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 6)
    runsql_area.Add(row1, spacing)
    runsql_area.Add(row2, spacing)

    return runsql_area

  def build_page1_enumeration_meta(self, panel):
    meta_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '数据库名, 表名, 列名...')
    _meta_area = meta_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 10)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 10)

    row1 = wx.BoxSizer()
    self._meta_area_D_ckbtn = cb(_meta_area, label = '指定库名')
    self._meta_area_D_entry = tc(_meta_area)
    self._meta_area_T_ckbtn = cb(_meta_area, label = '指定表名')
    self._meta_area_T_entry = tc(_meta_area)
    self._meta_area_C_ckbtn = cb(_meta_area, label = '指定列名')
    self._meta_area_C_entry = tc(_meta_area)
    self._meta_area_U_ckbtn = cb(_meta_area, label = '指定用户')
    self._meta_area_U_entry = tc(_meta_area)

    row1.Add(self._meta_area_D_ckbtn, border)
    row1.Add(self._meta_area_D_entry, proportion_border)
    row1.Add(self._meta_area_T_ckbtn, border)
    row1.Add(self._meta_area_T_entry, proportion_border)
    row1.Add(self._meta_area_C_ckbtn, border)
    row1.Add(self._meta_area_C_entry, proportion_border)
    row1.Add(self._meta_area_U_ckbtn, border)
    row1.Add(self._meta_area_U_entry, proportion_border)

    row2 = wx.BoxSizer()
    self._meta_area_X_ckbtn = cb(_meta_area, label = '排除标志符')
    self._meta_area_X_entry = tc(_meta_area)
    self._meta_area_pivot_ckbtn = cb(_meta_area, label = '指定Pivot列名')
    self._meta_area_pivot_entry = tc(_meta_area)

    row2.Add(self._meta_area_X_ckbtn, border)
    row2.Add(self._meta_area_X_entry, border)
    row2.Add(self._meta_area_pivot_ckbtn, border)
    row2.Add(self._meta_area_pivot_entry, border)

    row3 = wx.BoxSizer()
    self._meta_area_where_ckbtn = cb(_meta_area, label = 'where子句')
    self._meta_area_where_entry = tc(_meta_area)

    row3.Add(self._meta_area_where_ckbtn, border)
    row3.Add(self._meta_area_where_entry, proportion_border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 6)
    meta_area.Add(row1, spacing)
    meta_area.Add(row2, spacing)
    meta_area.Add(row3, spacing)
    return meta_area

  def build_page1_enumeration_blind(self, panel):
    blind_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '盲注选项')
    _blind_area = blind_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 10)

    row1 = wx.BoxSizer()
    self._blind_area_first_ckbtn = cb(_blind_area, label = '首字符:')
    self._blind_area_first_entry = tc(_blind_area)

    row1.Add(self._blind_area_first_ckbtn, border)
    row1.Add(self._blind_area_first_entry, border)

    row2 = wx.BoxSizer()
    self._blind_area_last_ckbtn = cb(_blind_area, label = '末字符:')
    self._blind_area_last_entry = tc(_blind_area)

    row2.Add(self._blind_area_last_ckbtn, border)
    row2.Add(self._blind_area_last_entry, border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 10)
    blind_area.Add(row1, spacing)
    blind_area.Add(row2, spacing)

    return blind_area

  def build_page1_enumeration_limit(self, panel):
    limit_area = wx.StaticBoxSizer(wx.VERTICAL, panel, 'limit(dump时的限制)')
    _limit_area = limit_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 5)

    row1 = wx.BoxSizer()
    self._limit_area_start_ckbtn = cb(_limit_area, label = '始于第')
    self._limit_area_start_entry = tc(_limit_area)

    row1.Add(self._limit_area_start_ckbtn, border)
    row1.Add(self._limit_area_start_entry)
    row1.Add(st(_limit_area, label = '条'), border)

    row2 = wx.BoxSizer()
    self._limit_area_stop_ckbtn = cb(_limit_area, label = '止于第')
    self._limit_area_stop_entry = tc(_limit_area)
    row2.Add(self._limit_area_stop_ckbtn, border)
    row2.Add(self._limit_area_stop_entry)
    row2.Add(st(_limit_area, label = '条'), border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 10)
    limit_area.Add(row1, spacing)
    limit_area.Add(row2, spacing)

    return limit_area

  def build_page1_enumeration_dump(self, panel):
    dump_area = wx.StaticBoxSizer(wx.VERTICAL, panel, 'Dump(转储)')
    _dump_area = dump_area.GetStaticBox()

    self._dump_area_dump_ckbtn = cb(_dump_area, label = 'dump(某库某表的条目)')
    self._dump_area_dump_all_ckbtn = cb(_dump_area, label = '全部dump(拖库)')
    self._dump_area_search_ckbtn = cb(_dump_area, label = '搜索')
    self._dump_area_no_sys_db_ckbtn = cb(_dump_area, label = '排除系统库')
    self._dump_area_repair_ckbtn = cb(_dump_area, label = '重新获取有未知符号(?)的条目')

    spacing = wx.SizerFlags().Expand().Border(wx.LEFT | wx.RIGHT, 10)
    dump_area.Add(self._dump_area_dump_ckbtn, spacing)
    dump_area.Add(self._dump_area_dump_all_ckbtn, spacing)
    dump_area.Add(self._dump_area_search_ckbtn, spacing)
    dump_area.Add(self._dump_area_no_sys_db_ckbtn, spacing)
    dump_area.Add(self._dump_area_repair_ckbtn, spacing)

    return dump_area

  def build_page1_enumeration_enum(self, panel):
    enum_area = wx.StaticBoxSizer(wx.HORIZONTAL, panel, '枚举')
    _enum_area = enum_area.GetStaticBox()

    _enum_area_enum_labels = (
      ('DB banner', '当前用户', '当前数据库', '主机名', '是否是DBA'),
      ('用户', '密码', '权限', '角色', '数据库'),
      ('表', '字段', '架构', '计数', '备注'))
    self._enum_area_opts_ckbtns = ([], [], [])
    _enu_area_opts_cols = [wx.BoxSizer(wx.VERTICAL),
                           wx.BoxSizer(wx.VERTICAL),
                           wx.BoxSizer(wx.VERTICAL)]

    spacing = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 13)

    for _x in range(len(_enum_area_enum_labels)):  # 三列
      for _y in _enum_area_enum_labels[_x]:
        _ckbtn = cb(_enum_area, label = _y)
        self._enum_area_opts_ckbtns[_x].append(_ckbtn)
        # 每列, 至上往下add
        _enu_area_opts_cols[_x].Add(_ckbtn)

      enum_area.Add(_enu_area_opts_cols[_x], spacing)

    return enum_area

  def build_page1_request(self):
    p = ScrolledPanel(self, style=wx.TAB_TRAVERSAL | wx.SUNKEN_BORDER)
    p.SetupScrolling(scroll_x = False)

    vbox = wx.BoxSizer(wx.VERTICAL)
    request_header_area = self.build_page1_request_header(p)
    request_data_area = self.build_page1_request_data(p)
    request_custom_area = self.build_page1_request_custom(p)
    request_proxy_area = self.build_page1_request_proxy(p)

    spacing = wx.SizerFlags().Expand().Border(wx.ALL, 5)
    vbox.Add(request_header_area, spacing)
    vbox.Add(request_data_area, spacing)
    vbox.Add(request_custom_area, spacing)
    vbox.Add(request_proxy_area, spacing)
    # 不能用SetSizerAndFit, Fit会自适应的, 从而没有滚动条
    p.SetSizer(vbox)
    return p

  def build_page1_request_proxy(self, panel):
    request_proxy_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '隐匿/代理')
    _request_proxy_area = request_proxy_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 5)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 5)

    row1 = wx.BoxSizer()
    self._request_area_safe_url_ckbtn = cb(_request_proxy_area, label = '顺便掺杂地访问一个安全url')
    self._request_area_safe_url_entry = tc(_request_proxy_area)
    self._request_area_safe_post_ckbtn = cb(_request_proxy_area, label = '提交到安全url的post数据')
    self._request_area_safe_post_entry = tc(_request_proxy_area)

    row1.Add(self._request_area_safe_url_ckbtn, border)
    row1.Add(self._request_area_safe_url_entry, proportion_border)
    row1.Add(self._request_area_safe_post_ckbtn, border)
    row1.Add(self._request_area_safe_post_entry, proportion_border)

    row2 = wx.BoxSizer()
    self._request_area_safe_req_ckbtn = cb(_request_proxy_area, label = '从文件载入safe HTTP请求')
    self._request_area_safe_req_entry = tc(_request_proxy_area)
    self._request_area_safe_req_chooser = wx.Button(_request_proxy_area, label = '打开')
    self._request_area_safe_req_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._request_area_safe_req_entry]:
        self._handlers.set_file_entry_text(evt, data))

    self._request_area_safe_freq_ckbtn = cb(_request_proxy_area, label = '访问安全url的频率')
    self._request_area_safe_freq_entry = tc(_request_proxy_area)

    row2.Add(self._request_area_safe_req_ckbtn, border)
    row2.Add(self._request_area_safe_req_entry, proportion = 1)
    row2.Add(self._request_area_safe_req_chooser, border)
    row2.Add(self._request_area_safe_freq_ckbtn, border)
    row2.Add(self._request_area_safe_freq_entry, border)

    row3 = wx.BoxSizer()
    self._request_area_ignore_proxy_ckbtn = cb(_request_proxy_area, label = '忽略系统默认代理')
    self._request_area_proxy_ckbtn = cb(_request_proxy_area, label = '使用代理')
    self._request_area_proxy_file_ckbtn = cb(_request_proxy_area, label = '代理列表文件')
    self._request_area_proxy_file_entry = tc(_request_proxy_area)
    self._request_area_proxy_file_chooser = wx.Button(_request_proxy_area, label = '打开')
    self._request_area_proxy_file_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._request_area_proxy_file_entry]:
        self._handlers.set_file_entry_text(evt, data))

    row3.Add(self._request_area_ignore_proxy_ckbtn, border)
    row3.Add(self._request_area_proxy_ckbtn, border)
    row3.Add(self._request_area_proxy_file_ckbtn, border)
    row3.Add(self._request_area_proxy_file_entry, proportion = 1)
    row3.Add(self._request_area_proxy_file_chooser, border)

    row4 = wx.BoxSizer()
    self._request_area_proxy_ip_label = st(_request_proxy_area, label = 'IP:')
    self._request_area_proxy_ip_entry = tc(_request_proxy_area)
    self._request_area_proxy_port_label = st(_request_proxy_area, label = 'PORT:')
    self._request_area_proxy_port_entry = tc(_request_proxy_area)
    self._request_area_proxy_username_label = st(_request_proxy_area, label = 'username:')
    self._request_area_proxy_username_entry = tc(_request_proxy_area)
    self._request_area_proxy_password_label = st(_request_proxy_area, label = 'password:')
    self._request_area_proxy_password_entry = tc(_request_proxy_area)

    row4.Add(self._request_area_proxy_ip_label, border)
    row4.Add(self._request_area_proxy_ip_entry, proportion_border)
    row4.Add(self._request_area_proxy_port_label, border)
    row4.Add(self._request_area_proxy_port_entry, border)
    row4.Add(self._request_area_proxy_username_label, border)
    row4.Add(self._request_area_proxy_username_entry, proportion_border)
    row4.Add(self._request_area_proxy_password_label, border)
    row4.Add(self._request_area_proxy_password_entry, proportion_border)

    row5 = wx.BoxSizer()
    self._request_area_tor_ckbtn = cb(_request_proxy_area, label = '使用Tor匿名网络')
    self._request_area_tor_port_ckbtn = cb(_request_proxy_area, label = 'Tor端口:')
    self._request_area_tor_port_entry = tc(_request_proxy_area)
    self._request_area_tor_type_ckbtn = cb(_request_proxy_area, label = 'Tor代理类型')
    self._request_area_tor_type_entry = tc(_request_proxy_area)
    self._request_area_check_tor_ckbtn = cb(_request_proxy_area, label = '检查Tor连接')

    row5.Add(self._request_area_tor_ckbtn, border)
    row5.Add(self._request_area_tor_port_ckbtn, border)
    row5.Add(self._request_area_tor_port_entry, border)
    row5.Add(self._request_area_tor_type_ckbtn, border)
    row5.Add(self._request_area_tor_type_entry, border)
    row5.Add(self._request_area_check_tor_ckbtn, border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 2)
    request_proxy_area.Add(row1, spacing)
    request_proxy_area.Add(row2, spacing)
    request_proxy_area.Add(wx.StaticLine(_request_proxy_area), spacing)
    request_proxy_area.Add(row3, spacing)
    request_proxy_area.Add(row4, spacing)
    request_proxy_area.Add(row5, spacing)

    return request_proxy_area

  def build_page1_request_custom(self, panel):
    request_custom_area = wx.StaticBoxSizer(wx.VERTICAL, panel, 'request定制')
    _request_custom_area = request_custom_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 5)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 5)

    row1 = wx.BoxSizer()
    self._request_area_ignore_redirects_ckbtn = cb(_request_custom_area, label = '忽略重定向')
    self._request_area_ignore_timeouts_ckbtn = cb(_request_custom_area, label = '忽略连接超时')
    self._request_area_ignore_code_ckbtn = cb(_request_custom_area, label = '忽略错误型状态码:')
    self._request_area_ignore_code_entry = tc(_request_custom_area)
    self._request_area_skip_urlencode_ckbtn = cb(_request_custom_area, label = 'payload不使用url编码')
    self._request_area_force_ssl_ckbtn = cb(_request_custom_area, label = '强制使用HTTPS')
    self._request_area_chunked_ckbtn = cb(_request_custom_area, label = '用Chunked编码发送POST请求')
    self._request_area_hpp_ckbtn = cb(_request_custom_area, label = '使用HTTP参数污染')

    row1.Add(self._request_area_ignore_redirects_ckbtn, border)
    row1.Add(self._request_area_ignore_timeouts_ckbtn, border)
    row1.Add(self._request_area_ignore_code_ckbtn, border)
    row1.Add(self._request_area_ignore_code_entry, proportion_border)
    row1.Add(self._request_area_skip_urlencode_ckbtn, border)
    row1.Add(self._request_area_force_ssl_ckbtn, border)
    row1.Add(self._request_area_chunked_ckbtn, border)
    row1.Add(self._request_area_hpp_ckbtn, border)

    row2 = wx.BoxSizer()
    self._request_area_delay_ckbtn = cb(_request_custom_area, label = '请求间隔(秒)')
    self._request_area_delay_entry = tc(_request_custom_area)
    self._request_area_timeout_ckbtn = cb(_request_custom_area, label = '几秒超时')
    self._request_area_timeout_entry = tc(_request_custom_area)
    self._request_area_retries_ckbtn = cb(_request_custom_area, label = '超时重试次数')
    self._request_area_retries_entry = tc(_request_custom_area)
    self._request_area_randomize_ckbtn = cb(_request_custom_area, label = '指定要随机改变值的参数')
    self._request_area_randomize_entry = tc(_request_custom_area)

    row2.Add(self._request_area_delay_ckbtn, border)
    row2.Add(self._request_area_delay_entry, border)
    row2.Add(self._request_area_timeout_ckbtn, border)
    row2.Add(self._request_area_timeout_entry, border)
    row2.Add(self._request_area_retries_ckbtn, border)
    row2.Add(self._request_area_retries_entry, border)
    row2.Add(self._request_area_randomize_ckbtn, border)
    row2.Add(self._request_area_randomize_entry, proportion_border)

    row3 = wx.BoxSizer()
    self._request_area_eval_ckbtn = cb(_request_custom_area, label = '--eval=')
    self._request_area_eval_entry = tc(_request_custom_area)

    row3.Add(self._request_area_eval_ckbtn, border)
    row3.Add(self._request_area_eval_entry, proportion_border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 2)
    request_custom_area.Add(row1, spacing)
    request_custom_area.Add(row2, spacing)
    request_custom_area.Add(row3, spacing)

    return request_custom_area

  def build_page1_request_data(self, panel):
    request_data_area = wx.StaticBoxSizer(wx.VERTICAL, panel, 'HTTP data')
    _request_data_area = request_data_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 5)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 5)

    row1 = wx.BoxSizer()
    self._request_area_method_ckbtn = cb(_request_data_area, label = 'HTTP请求方式')
    self._request_area_method_entry = tc(_request_data_area)
    self._request_area_param_del_ckbtn = cb(_request_data_area, label = '指定分隔data参数值的字符')
    self._request_area_param_del_entry = tc(_request_data_area)

    row1.Add(self._request_area_method_ckbtn, border)
    row1.Add(self._request_area_method_entry, border)
    row1.Add(self._request_area_param_del_ckbtn, border)
    row1.Add(self._request_area_param_del_entry, border)

    row2 = wx.BoxSizer()
    self._request_area_post_ckbtn = cb(_request_data_area, label = '通过POST提交data:')
    self._request_area_post_entry = tc(_request_data_area)

    row2.Add(self._request_area_post_ckbtn, border)
    row2.Add(self._request_area_post_entry, proportion_border)

    row3 = wx.BoxSizer()
    self._request_area_cookie_ckbtn = cb(_request_data_area, label = '请求中要包含的Cookie:')
    self._request_area_cookie_entry = tc(_request_data_area)
    self._request_area_cookie_del_ckbtn = cb(_request_data_area, label = '指定cookie分隔符')
    self._request_area_cookie_del_entry = tc(_request_data_area)

    row3.Add(self._request_area_cookie_ckbtn, border)
    row3.Add(self._request_area_cookie_entry, proportion_border)
    row3.Add(self._request_area_cookie_del_ckbtn, border)
    row3.Add(self._request_area_cookie_del_entry, border)

    row4 = wx.BoxSizer()
    self._request_area_load_cookies_ckbtn = cb(_request_data_area, label = '本地Cookie文件')
    self._request_area_load_cookies_entry = tc(_request_data_area)
    self._request_area_load_cookies_chooser = wx.Button(_request_data_area, label = '打开')
    self._request_area_load_cookies_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._request_area_load_cookies_entry]:
        self._handlers.set_file_entry_text(evt, data))

    self._request_area_drop_set_cookie_ckbtn = cb(_request_data_area, label = '丢弃Set-Cookie头')

    row4.Add(self._request_area_load_cookies_ckbtn, border)
    row4.Add(self._request_area_load_cookies_entry, proportion = 1)
    row4.Add(self._request_area_load_cookies_chooser, border)
    row4.Add(self._request_area_drop_set_cookie_ckbtn, border)

    row5 = wx.BoxSizer()
    self._request_area_auth_type_ckbtn = cb(_request_data_area, label = 'http认证类型')
    self._request_area_auth_type_entry = tc(_request_data_area)
    self._request_area_auth_cred_ckbtn = cb(_request_data_area, label = 'http认证账密')
    self._request_area_auth_cred_entry = tc(_request_data_area)
    self._request_area_auth_file_ckbtn = cb(_request_data_area, label = 'http认证文件')
    self._request_area_auth_file_entry = tc(_request_data_area)
    self._request_area_auth_file_chooser = wx.Button(_request_data_area, label = '打开')
    self._request_area_auth_file_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._request_area_auth_file_entry]:
        self._handlers.set_file_entry_text(evt, data))

    row5.Add(self._request_area_auth_type_ckbtn, border)
    row5.Add(self._request_area_auth_type_entry, proportion_border)
    row5.Add(self._request_area_auth_cred_ckbtn, border)
    row5.Add(self._request_area_auth_cred_entry, proportion_border)
    row5.Add(self._request_area_auth_file_ckbtn, border)
    row5.Add(self._request_area_auth_file_entry, proportion = 1)
    row5.Add(self._request_area_auth_file_chooser, border)

    row6 = wx.BoxSizer()
    self._request_area_csrf_token_ckbtn = cb(_request_data_area, label = 'csrf_token')
    self._request_area_csrf_token_entry = tc(_request_data_area)
    self._request_area_csrf_url_ckbtn = cb(_request_data_area, label = '获取csrf_token的url')
    self._request_area_csrf_url_entry = tc(_request_data_area)

    row6.Add(self._request_area_csrf_token_ckbtn, border)
    row6.Add(self._request_area_csrf_token_entry, proportion_border)
    row6.Add(self._request_area_csrf_url_ckbtn, border)
    row6.Add(self._request_area_csrf_url_entry, proportion_border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 2)
    request_data_area.Add(row1, spacing)
    request_data_area.Add(row2, spacing)
    request_data_area.Add(wx.StaticLine(_request_data_area), spacing)
    request_data_area.Add(row3, spacing)
    request_data_area.Add(row4, spacing)
    request_data_area.Add(wx.StaticLine(_request_data_area), spacing)
    request_data_area.Add(row5, spacing)
    request_data_area.Add(row6, spacing)

    return request_data_area

  def build_page1_request_header(self, panel):
    request_header_area = wx.StaticBoxSizer(wx.VERTICAL, panel, 'HTTP header')
    _request_header_area = request_header_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 5)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 5)

    row1 = wx.BoxSizer()
    self._request_area_random_agent_ckbtn = cb(_request_header_area, label = '随机User-Agent头')
    self._request_area_user_agent_ckbtn = cb(_request_header_area, label = '指定User-Agent头')
    self._request_area_user_agent_entry = tc(_request_header_area)

    row1.Add(self._request_area_random_agent_ckbtn, border)
    row1.Add(self._request_area_user_agent_ckbtn, border)
    row1.Add(self._request_area_user_agent_entry, proportion_border)

    row2 = wx.BoxSizer()
    self._request_area_host_ckbtn = cb(_request_header_area, label = 'Host头')
    self._request_area_host_entry = tc(_request_header_area)
    self._request_area_referer_ckbtn = cb(_request_header_area, label = 'referer头')
    self._request_area_referer_entry = tc(_request_header_area)

    row2.Add(self._request_area_host_ckbtn, border)
    row2.Add(self._request_area_host_entry, proportion_border)
    row2.Add(self._request_area_referer_ckbtn, border)
    row2.Add(self._request_area_referer_entry, proportion_border)

    row3 = wx.BoxSizer()
    self._request_area_header_ckbtn = cb(_request_header_area, label = '额外的header(-H)')
    self._request_area_header_entry = tc(_request_header_area)
    self._request_area_headers_ckbtn = cb(_request_header_area, label = '额外的headers')
    self._request_area_headers_entry = tc(_request_header_area)

    row3.Add(self._request_area_header_ckbtn, border)
    row3.Add(self._request_area_header_entry, proportion_border)
    row3.Add(self._request_area_headers_ckbtn, border)
    row3.Add(self._request_area_headers_entry, proportion_border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 2)
    request_header_area.Add(row1, spacing)
    request_header_area.Add(row2, spacing)
    request_header_area.Add(row3, spacing)

    return request_header_area

  def build_page1_setting(self):
    p = ScrolledPanel(self, style=wx.TAB_TRAVERSAL | wx.SUNKEN_BORDER)
    p.SetupScrolling(scroll_x = False)

    spacing = wx.SizerFlags().Expand().Border(wx.ALL, 5)

    hbox1 = wx.BoxSizer()
    inject_area = self.build_page1_setting_inject(p)
    detection_area = self.build_page1_setting_detection(p)
    tech_area = self.build_page1_setting_tech(p)

    hbox1.Add(inject_area, spacing)
    hbox1.Add(detection_area, proportion = 1, flag = wx.EXPAND | wx.ALL, border = 5)
    hbox1.Add(tech_area, spacing)

    hbox2 = wx.BoxSizer()
    tamper_area = self.build_page1_setting_tamper(p)
    optimize_area = self.build_page1_setting_optimize(p)
    general_area = self.build_page1_setting_general(p)

    hbox2.Add(tamper_area, spacing)
    hbox2.Add(optimize_area, spacing)
    hbox2.Add(general_area, spacing)

    vbox = wx.BoxSizer(wx.VERTICAL)
    vbox.Add(hbox1, flag = wx.EXPAND)
    vbox.Add(hbox2, flag = wx.EXPAND)
    # 不能用SetSizerAndFit, Fit会自适应的, 从而没有滚动条
    p.SetSizer(vbox)
    return p

  def build_page1_setting_general(self, panel):
    general_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '常用选项')
    _general_area = general_area.GetStaticBox()

    row1 = wx.BoxSizer()
    self._general_area_verbose_ckbtn = cb(_general_area, label = '输出详细程度')
    self._general_area_verbose_scale = sl(_general_area,
                                          value = 1,
                                          minValue = 0,
                                          maxValue = 6,
                                          style = wx.SL_VALUE_LABEL)

    row1.Add(self._general_area_verbose_ckbtn)
    row1.Add(self._general_area_verbose_scale, proportion = 1)

    self._general_area_finger_ckbtn = cb(_general_area, label = '执行宽泛的DB版本检测')
    self._general_area_hex_ckbtn = cb(_general_area, label = '获取数据时使用hex转换')
    self._general_area_batch_ckbtn = cb(_general_area, label = '非交互模式, 一切皆默认')
    self._page1_misc_wizard_ckbtn = cb(_general_area, label = '新手向导')

    spacing = wx.SizerFlags().Expand().Border(wx.ALL, 3)
    general_area.Add(row1, spacing)
    general_area.Add(self._general_area_finger_ckbtn, spacing)
    general_area.Add(self._general_area_hex_ckbtn, spacing)
    general_area.Add(self._general_area_batch_ckbtn, spacing)
    general_area.Add(self._page1_misc_wizard_ckbtn, spacing)
    return general_area

  def build_page1_setting_optimize(self, panel):
    optimize_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '性能优化')
    _optimize_area = optimize_area.GetStaticBox()

    self._optimize_area_turn_all_ckbtn = cb(_optimize_area, label = '启用所有优化选项')
    self._optimize_area_turn_all_ckbtn.Bind(wx.EVT_CHECKBOX, self.optimize_area_controller)

    row2 = wx.BoxSizer()
    self._optimize_area_thread_num_ckbtn = cb(_optimize_area, label = '使用线程数:')
    self._optimize_area_thread_num_spinbtn = sp(_optimize_area, value = '2', min = 2, max = 10000)

    row2.Add(self._optimize_area_thread_num_ckbtn)
    row2.Add(self._optimize_area_thread_num_spinbtn, proportion = 1, flag = wx.RIGHT, border = 10)

    self._optimize_area_predict_ckbtn = cb(_optimize_area, label = '预测通常的查询结果')
    self._optimize_area_keep_alive_ckbtn = cb(_optimize_area, label = 'http连接使用keep-alive')
    self._optimize_area_null_connect_ckbtn = cb(_optimize_area, label = '只用页面长度报头来比较, 不去获取实际的响应体')

    spacing = wx.SizerFlags().Expand().Border(wx.ALL, 3)
    optimize_area.Add(self._optimize_area_turn_all_ckbtn, spacing)
    optimize_area.Add(row2, spacing)
    optimize_area.Add(self._optimize_area_predict_ckbtn, spacing)
    optimize_area.Add(self._optimize_area_keep_alive_ckbtn, spacing)
    optimize_area.Add(self._optimize_area_null_connect_ckbtn, spacing)

    return optimize_area

  def optimize_area_controller(self, event):
    if self._optimize_area_turn_all_ckbtn.IsChecked():
      self._optimize_area_predict_ckbtn.SetValue(False)
      self._optimize_area_keep_alive_ckbtn.SetValue(False)
      self._optimize_area_null_connect_ckbtn.SetValue(False)

      self._optimize_area_predict_ckbtn.Disable()
      self._optimize_area_keep_alive_ckbtn.Disable()
      self._optimize_area_null_connect_ckbtn.Disable()
    else:
      self._optimize_area_predict_ckbtn.Enable()
      self._optimize_area_keep_alive_ckbtn.Enable()
      self._optimize_area_null_connect_ckbtn.Enable()

  def build_page1_setting_tamper(self, panel):
    tamper_area = wx.StaticBoxSizer(wx.VERTICAL, panel, 'tamper脚本')
    _tamper_area = tamper_area.GetStaticBox()
    # 多行文本框的默认size太小了
    self._tamper_area_tamper_view = tc(_tamper_area,
                                       size = (300, -1),
                                       style = wx.TE_MULTILINE)
    tamper_area.Add(self._tamper_area_tamper_view, proportion = 1)

    return tamper_area

  def build_page1_setting_tech(self, panel):
    tech_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '各注入技术的选项')
    _tech_area = tech_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 5)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 5)
    expand_border = wx.SizerFlags().Expand().Border(wx.LEFT | wx.RIGHT, 5)

    grid = wx.GridSizer(5, 2, 6, 0)
    self._tech_area_tech_ckbtn = cb(_tech_area, label = '注入技术')
    self._tech_area_tech_entry = tc(_tech_area)

    grid.Add(self._tech_area_tech_ckbtn, expand_border)
    grid.Add(self._tech_area_tech_entry, expand_border)

    self._tech_area_time_sec_ckbtn = cb(_tech_area, label = '指定DB延迟多少秒响应')
    self._tech_area_time_sec_entry = tc(_tech_area)

    grid.Add(self._tech_area_time_sec_ckbtn, expand_border)
    grid.Add(self._tech_area_time_sec_entry, expand_border)

    self._tech_area_union_col_ckbtn = cb(_tech_area, label = '指定最大union列数')
    self._tech_area_union_col_entry = tc(_tech_area)

    grid.Add(self._tech_area_union_col_ckbtn, expand_border)
    grid.Add(self._tech_area_union_col_entry, expand_border)

    self._tech_area_union_chr_ckbtn = cb(_tech_area, label = '指定枚举列数时所用字符')
    self._tech_area_union_chr_entry = tc(_tech_area)

    grid.Add(self._tech_area_union_chr_ckbtn, expand_border)
    grid.Add(self._tech_area_union_chr_entry, expand_border)

    self._tech_area_union_from_ckbtn = cb(_tech_area, label = '指定枚举列数时from的表名')
    self._tech_area_union_from_entry = tc(_tech_area)

    grid.Add(self._tech_area_union_from_ckbtn, expand_border)
    grid.Add(self._tech_area_union_from_entry, expand_border)

    row6 = wx.BoxSizer()
    self._tech_area_dns_ckbtn = cb(_tech_area, label = '指定DNS')
    self._tech_area_dns_entry = tc(_tech_area)

    row6.Add(self._tech_area_dns_ckbtn, border)
    row6.Add(self._tech_area_dns_entry, proportion_border)

    row7 = wx.BoxSizer()
    self._tech_area_second_url_ckbtn = cb(_tech_area, label = '指定二阶响应的url')
    self._tech_area_second_url_entry = tc(_tech_area)

    row7.Add(self._tech_area_second_url_ckbtn, border)
    row7.Add(self._tech_area_second_url_entry, proportion_border)

    row8 = wx.BoxSizer()
    self._tech_area_second_req_ckbtn = cb(_tech_area, label = '使用含二阶HTTP请求的文件:')

    row8.Add(self._tech_area_second_req_ckbtn, border)

    row9 = wx.BoxSizer()
    self._tech_area_second_req_entry = tc(_tech_area)
    self._tech_area_second_req_chooser = wx.Button(_tech_area, label = '打开')
    self._tech_area_second_req_chooser.Bind(
      wx.EVT_BUTTON,
      lambda evt, data = [self._tech_area_second_req_entry]:
        self._handlers.set_file_entry_text(evt, data))

    row9.Add(self._tech_area_second_req_entry, proportion_border)
    row9.Add(self._tech_area_second_req_chooser, border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 3)
    tech_area.Add(grid, spacing)
    tech_area.Add(row6, spacing)
    tech_area.Add(row7, spacing)
    tech_area.Add(row8, spacing)
    tech_area.Add(row9, spacing)

    return tech_area

  def build_page1_setting_detection(self, panel):
    detection_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '探测选项')
    _detection_area = detection_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 5)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 5)

    row1 = wx.BoxSizer()
    self._detection_area_level_ckbtn = cb(_detection_area, label = '探测等级(范围)')
    self._detection_area_level_scale = sl(_detection_area,
                                          value = 1,
                                          minValue = 1,
                                          maxValue = 5,
                                          style = wx.SL_VALUE_LABEL)

    row1.Add(self._detection_area_level_ckbtn, border)
    row1.Add(self._detection_area_level_scale, proportion_border)

    row2 = wx.BoxSizer()
    self._detection_area_risk_ckbtn = cb(_detection_area, label = 'payload危险等级')
    self._detection_area_risk_scale = sl(_detection_area,
                                         value = 1,
                                         minValue = 1,
                                         maxValue = 3,
                                         style = wx.SL_VALUE_LABEL)

    row2.Add(self._detection_area_risk_ckbtn, border)
    row2.Add(self._detection_area_risk_scale, proportion_border)

    row3 = wx.BoxSizer()
    self._detection_area_str_ckbtn = cb(_detection_area, label = '指定字符串')
    self._detection_area_str_entry = tc(_detection_area)

    row3.Add(self._detection_area_str_ckbtn, border)
    row3.Add(self._detection_area_str_entry, proportion_border)

    row4 = wx.BoxSizer()
    self._detection_area_not_str_ckbtn = cb(_detection_area, label = '指定字符串')
    self._detection_area_not_str_entry = tc(_detection_area)

    row4.Add(self._detection_area_not_str_ckbtn, border)
    row4.Add(self._detection_area_not_str_entry, proportion_border)

    row5 = wx.BoxSizer()
    self._detection_area_re_ckbtn = cb(_detection_area, label = '指定正则')
    self._detection_area_re_entry = tc(_detection_area)

    row5.Add(self._detection_area_re_ckbtn, border)
    row5.Add(self._detection_area_re_entry, proportion_border)

    row6 = wx.BoxSizer()
    self._detection_area_code_ckbtn = cb(_detection_area, label = '指定http状态码')
    self._detection_area_code_entry = tc(_detection_area)

    row6.Add(self._detection_area_code_ckbtn, border)
    row6.Add(self._detection_area_code_entry, border)

    row7 = wx.GridSizer(1, 2, 0, 0)
    self._detection_area_text_only_ckbtn = cb(_detection_area, label = '仅对比文本')
    self._detection_area_titles_ckbtn = cb(_detection_area, label = '仅对比title')

    row7.Add(self._detection_area_text_only_ckbtn, border)
    row7.Add(self._detection_area_titles_ckbtn, border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 3)
    detection_area.Add(row1, spacing)
    detection_area.Add(row2, spacing)
    detection_area.Add(row3, spacing)
    detection_area.Add(row4, spacing)
    detection_area.Add(row5, spacing)
    detection_area.Add(row6, spacing)
    detection_area.Add(row7, spacing)

    return detection_area

  def build_page1_setting_inject(self, panel):
    inject_area = wx.StaticBoxSizer(wx.VERTICAL, panel, '注入选项')
    _inject_area = inject_area.GetStaticBox()

    border = wx.SizerFlags().Border(wx.LEFT | wx.RIGHT, 6)
    proportion_border = wx.SizerFlags(1).Border(wx.LEFT | wx.RIGHT, 6)

    row1 = wx.BoxSizer()
    self._inject_area_param_ckbtn = cb(_inject_area, label = '可测试的参数')
    self._inject_area_param_entry = tc(_inject_area)

    row1.Add(self._inject_area_param_ckbtn, border)
    row1.Add(self._inject_area_param_entry, proportion_border)

    row2 = wx.BoxSizer()
    self._inject_area_skip_static_ckbtn = cb(_inject_area, label = '跳过无动态特性的参数')
    row2.Add(self._inject_area_skip_static_ckbtn, border)

    row3 = wx.BoxSizer()
    self._inject_area_prefix_ckbtn = cb(_inject_area, label = 'payload前缀')
    self._inject_area_prefix_entry = tc(_inject_area)
    row3.Add(self._inject_area_prefix_ckbtn, border)
    row3.Add(self._inject_area_prefix_entry, proportion_border)

    row4 = wx.BoxSizer()
    self._inject_area_suffix_ckbtn = cb(_inject_area, label = 'payload后缀')
    self._inject_area_suffix_entry = tc(_inject_area)
    row4.Add(self._inject_area_suffix_ckbtn, border)
    row4.Add(self._inject_area_suffix_entry, proportion_border)

    row5 = wx.BoxSizer()
    self._inject_area_skip_ckbtn = cb(_inject_area, label = '排除参数')
    self._inject_area_skip_entry = tc(_inject_area)
    row5.Add(self._inject_area_skip_ckbtn, border)
    row5.Add(self._inject_area_skip_entry, proportion_border)

    row6 = wx.BoxSizer()
    self._inject_area_param_exclude_ckbtn = cb(_inject_area, label = '排除参数(正则)')
    self._inject_area_param_exclude_entry = tc(_inject_area)
    row6.Add(self._inject_area_param_exclude_ckbtn, border)
    row6.Add(self._inject_area_param_exclude_entry, proportion_border)

    row7 = wx.BoxSizer()
    self._inject_area_dbms_ckbtn = cb(_inject_area, label = '固定DB类型为')
    self._inject_area_dbms_combobox = cbb(_inject_area, choices = ['mysql', 'sqlite', 'sqlserver'])
    row7.Add(self._inject_area_dbms_ckbtn, border)
    row7.Add(self._inject_area_dbms_combobox, proportion_border)

    row8 = wx.BoxSizer()
    self._inject_area_dbms_cred_ckbtn = cb(_inject_area, label = 'DB认证')
    self._inject_area_dbms_cred_entry = tc(_inject_area)
    row8.Add(self._inject_area_dbms_cred_ckbtn, border)
    row8.Add(self._inject_area_dbms_cred_entry, proportion_border)

    row9 = wx.BoxSizer()
    self._inject_area_os_ckbtn = cb(_inject_area, label = '固定OS为')
    self._inject_area_os_entry = tc(_inject_area)
    row9.Add(self._inject_area_os_ckbtn, border)
    row9.Add(self._inject_area_os_entry, proportion_border)

    row10 = wx.BoxSizer()
    self._inject_area_no_cast_ckbtn = cb(_inject_area, label = '关掉payload变形机制')
    self._inject_area_no_escape_ckbtn = cb(_inject_area, label = '关掉string转义')
    row10.Add(self._inject_area_no_cast_ckbtn, border)
    row10.Add(self._inject_area_no_escape_ckbtn, border)    # 需要右对齐

    row11 = wx.BoxSizer()
    _invalid_label = st(_inject_area, label = '对payload中的废值:')
    self._inject_area_invalid_logic_ckbtn = cb(_inject_area, label = '使用逻辑运算符')
    row11.Add(_invalid_label, border)
    row11.Add(self._inject_area_invalid_logic_ckbtn, border)

    row12 = wx.BoxSizer()
    self._inject_area_invalid_bignum_ckbtn = cb(_inject_area, label = '使用大数')
    self._inject_area_invalid_str_ckbtn = cb(_inject_area, label = '使用随机字符串')
    row12.Add(self._inject_area_invalid_bignum_ckbtn, border)
    row12.Add(self._inject_area_invalid_str_ckbtn, border)

    spacing = wx.SizerFlags().Expand().Border(wx.TOP | wx.BOTTOM, 3)
    inject_area.Add(row1, spacing)
    inject_area.Add(row2, spacing)
    inject_area.Add(row3, spacing)
    inject_area.Add(row4, spacing)
    inject_area.Add(row5, spacing)
    inject_area.Add(row6, spacing)
    inject_area.Add(row7, spacing)
    inject_area.Add(row8, spacing)
    inject_area.Add(row9, spacing)
    inject_area.Add(row10, spacing)
    inject_area.Add(row11, flag = wx.ALIGN_RIGHT | wx.TOP | wx.BOTTOM, border = 3)
    inject_area.Add(row12, flag = wx.ALIGN_RIGHT | wx.TOP | wx.BOTTOM, border = 3)

    return inject_area  # 一定要返回StaticBoxSizer, 不然会段错!


def main():
  from handlers import Handler
  app = wx.App()

  win = wx.Frame(None, title = 'sqlmap-page1')

  n = Page1Notebook(win, Handler(win))

  box = wx.BoxSizer()
  box.Add(n, proportion = 1)
  win.SetSizerAndFit(box)

  win.Centre()
  win.Show()

  app.MainLoop()


if __name__ == '__main__':
  main()
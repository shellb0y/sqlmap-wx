## sqlmap-wx
sqlmap GUI, using wxpython4.0  

#### SCREENSHORT
![screenshot](https://github.com/needle-wang/sqlmap-ui/blob/master/screenshots/sqlmap-wx1.png)

#### INSTALLATION
1. **REQUIRED**  
  - python3.5+
  - wxpython4.0.4:  
     win: `pip3 install wxPython`  
     linux: go to wxPython's website for help  
  - requests: `pip3 install requests`
  - [sqlmap](https://github.com/sqlmapproject/sqlmap): `pip2 install sqlmap` #hope sqlmap ports to python3 in future...
2. **GET**
  - `git clone https://github.com/needle-wang/sqlmap-wx.git`
3. **RUN**  
  - `./sqlmap_wx.py`  

#### TODO
- ~~重写完成, 功能和界面完全一样~~
- 继续重构, 优化?

#### ABOUT
1. V0.2  
   2019年 05月 12日 星期日 03:31:44 CST  
   作者: needle wang ( needlewang2011@gmail.com )  
2. 使用wxPthon4重写sqlmap-ui(using PyGObject)  
5. 感谢[sqm](https://github.com/kxcode/gui-for-sqlmap)带来的灵感, 其作者: [KINGX](https://github.com/kxcode) (sqm UI 使用的是python2 + tkinter)  

#### REFERENCE
1. wxpython教程: https://wiki.wxpython.org/ , http://zetcode.com/wxpython/  
2. wxpython API: https://wxpython.org/Phoenix/docs/html/index.html  

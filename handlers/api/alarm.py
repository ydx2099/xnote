# -*- coding:utf-8 -*-  
# Created by xupingmao on 2017/06/08
# 

"""闹钟"""

import time
import xutils
import xconfig

class handler:
    def GET(self, msg):
        if xconfig.is_mute():
            return dict(code="fail", message="mute")
        msg = xutils.unquote(msg)
        for i in range(3):
            xutils.say(msg)
            time.sleep(5)
        return dict(code="success")

xurls = (
    r"/api/alarm/(.*)", handler,
    r"/api/alert/(.*)", handler
)
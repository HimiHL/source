class ExceptionHandle(Exception):
    # 默认错误码
    code = 404;
    def __init__(self, message = None, code = None, payload = {}):
        Exception.__init__(self);
        self.message = message;
        if message is not None:
            self.message = message;
        else:
            self.message = '好像有点不对劲呢';
                
        if code is not None:
            self.code = code;
        self.payload = payload;
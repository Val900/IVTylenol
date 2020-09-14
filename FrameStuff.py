#VALLEY WALLEY'S FACE IN THE VIDEO STUFF FOR TO BE DUMB AS FUCK

class Frame:
    def __init__(self, **kwargs):
        
        #initialize frame variables
        
        #default webcam source
        self.src = 0
        #default capture method, other option is imutils.video.VideoStream()
        self.capture_method = "cv2.VideoCapture()"
        #if quit == True, then exit the program
        self.quit = False

        self.use_full_camera_resolution = False
        self.FPS_cap = 30
        self.frame_resize_width = 600
        self.frame_resize_keep_ratio = True
        self.swapRB = False

        allowed_keys = [i for i in dir(self) if "__" not in i and any([j.endswith(i) for j in self.__dict__.keys()])]

        self.__dict__.update((k, False) for k in allowed_keys)

        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

        rejected_keys = set(kwargs.keys()) - set(allowed_keys)
        if rejected_keys:
            raise ValueError("Invalid arguments in constructor:{}".format(rejected_keys))
        
    @property
    def use_full_camera_resolution(self):
        return self._use_full_camera_resolution
    
    @use_full_camera_resolution.setter
    def use_full_camera_resolution(self, value):

        allowed_values_aff = [
            "1",
            "yes",
            "y",
            "true"
        ]

        allowed_values_neg = [
            "0",
            "no",
            "n",
            "false"
        ]

        if value.lower() in allowed_values_aff:
            value = True
        elif value.lower() in allowed_values_neg:
            value = False
        else:
            print("Input not recognized, setting to default (False)")
            value = False

        self._use_full_camera_resolution = value

    @use_full_camera_resolution.deleter
    def use_full_camera_resolution(self):
        self._use_full_camera_resolution = False

    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, value):

        if not isinstance(value, int):
            print("Input not recognized, setting to default (0)")
            self._src = int(0)
        
        self._src = value

    @src.deleter
    def src(self):
        self._src = 0

    @property
    def capture_method(self):
        return self._capture_method

    @capture_method.setter
    def capture_method(self,value):
        
        allowed_values_opencv = [
            "opencv",
            "cv2",
            "videocapture",
            "cv"
        ]





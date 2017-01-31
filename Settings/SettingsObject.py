class SettingsObject(object):

    def __init__(self, dict = None, deserialize=None):
        self.configDict = dict
        if(deserialize != None):
            import json
            self.configDict = json.loads(deserialize)

    def serialize(self):
        import json
        return json.dumps(self.configDict)

    def get_dbname(self):
        return str(self.configDict["dbname"][0])

    def get_threads_number(self):
        return int(self.configDict["threads"][0])

    def get_min_idaudio(self):
        return int(self.configDict["min_idaudio"][0])

    def get_max_idaudio(self):
        return int(self.configDict["max_idaudio"][0])

    def get_path_music(self):
        return str(self.configDict["path_music"][0])

    def get_m2o_reloaded_url(self):
        return str(self.configDict["m2o_reloaded_url"][0])

    def __str__(self):
        string = "Configuration:\n"
        for (key,value) in self.configDict.iteritems() :
            string += key + " : " + str(value) + "\n"
        string += "End Of Configuration\n"
        return string

    def printAll(self):
        print self

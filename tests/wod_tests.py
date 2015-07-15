from wodpy import wod

class TestClass:
   def setUp(self):
        filenames = main.readInput('datafiles.json')
        profiles = main.extractProfiles(filenames)

        # Set up any keyword arguments needed by tests.
        kwargs = {'profiles' : profiles}

        testResults  = []
        testVerbose  = []
        trueResults  = []
        trueVerbose  = []
        firstProfile = True
        delete       = []
        currentFile  = ''
        self.profiles = []
        for iprofile, pinfo in enumerate(profiles):
          # Load the profile data.
          if pinfo.file_name != currentFile:
            if currentFile != '': f.close()
            currentFile = pinfo.file_name
            f = open(currentFile)
          if f.tell() != pinfo.file_position: f.seek(pinfo.file_position)
          self.profiles.append(wod.WodProfile(f))

 
   def tearDown(self):
       return

   def test_check_time_type(self):
        for p in self.profiles:
            time = p.time()
            assert type(time) is float or time is None, 'profile time should be either a float or None.'  
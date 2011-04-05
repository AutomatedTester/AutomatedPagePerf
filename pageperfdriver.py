#
#Copyright 2010 - David Burns
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
#



from selenium import webdriver
import os

class PagePerfDriver(webdriver.Firefox):

    def __init__(self, firefox_profile=None, firefox_binary=None):
        self.perf_profile = firefox_profile
        if self.perf_profile is None:
            self.perf_profile = webdriver.FirefoxProfile()
        self._update_profile()
        webdriver.Firefox.__init__(self, self.perf_profile, firefox_binary)

    def _update_profile(self):
        runner_dir = os.path.dirname(__file__)
        self.perf_profile.add_extension(os.path.join(runner_dir, 
                                        "firebug-1.6.0.xpi"))
        self.perf_profile.set_preference(
            "extensions.firebug.currentVersion", "\"9.99\"")
        self.perf_profile.set_preference(
            "extensions.firebug.DBG_NETEXPORT", "false")
        self.perf_profile.set_preference(
            "extensions.firebug.onByDefault", "true")
        self.perf_profile.set_preference(
            "extensions.firebug.net.enableSites", "true")
     
        self.perf_profile.add_extension(os.path.join(runner_dir,
                                        "fireStarter-0.1.a5.xpi"))
        self.perf_profile.add_extension(os.path.join(runner_dir,
                                        "netExport-0.8b9.xpi"))
        self.perf_profile.set_preference(
            "extensions.firebug.netexport.alwaysEnableAutoExport", "true")
        self.perf_profile.set_preference(
            "extensions.firebug.netexport.autoExportToFile", "true")
        self.perf_profile.set_preference(
            "extensions.firebug.netexport.autoExportToServer", "false")
        self.perf_profile.set_preference(
            "extensions.firebug.netexport.showPreview", "false")
        self.perf_profile.set_preference(
            "extensions.firebug.netexport.sendToConfirmation", "false")
        self.perf_profile.set_preference(
            "extensions.firebug.netexport.pageLoadedTimeout", "1500")
        self.perf_profile.update_preferences()

    @property
    def har_directory(self):
        return os.path.join(self.perf_profile.path, "firebug", "netexport", "logs")


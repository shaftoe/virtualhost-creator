class virtualhost():
    def __init__(self, ServerName="", DocumentRoot="", ServerAdmin=""):
        self.baseconfig = { "ServerAdmin" : "",
                    "DocumentRoot" : "/var/www",
                    "ServerName" : "default_virtualhost",
                    "ServerAlias" : ""}
        self.dirconfig = { "Options": "-Indexes",
                    "AllowOverride" : "all",
                    "Order": "allow,deny",
                    "Allow from" : "all",
                    "Deny from" : ""
                    }
        if ServerName:
            self.baseconfig["ServerName"] = ServerName
        if DocumentRoot:
            self.baseconfig["DocumentRoot"] = DocumentRoot
        if ServerAdmin:
            self.baseconfig["ServerAdmin"] = ServerAdmin
        self.baseconfig["DocumentRoot"] = self.baseconfig["DocumentRoot"] + "/" + self.baseconfig["ServerName"]
        self.baseconfig["ServerAlias"] = "www." + self.baseconfig["ServerName"]

    def getbaseconfig(self):
        print self.baseconfig

    def getdirconfig(self):
        print self.dirconfig

    def printconfig(self):
        # print base directives
        finalconfig = "<VirtualHost *:80>\n"
        for i in self.baseconfig:
            if self.baseconfig[i]:
                finalconfig = finalconfig + " " * 4 + i + " " + self.baseconfig[i] + "\n"
        # print directory directives
        finalconfig = finalconfig + "\n" + " " * 4 + "<Directory " + self.baseconfig["DocumentRoot"] + ">\n"
        for i in self.dirconfig:
            if self.dirconfig[i]:
                finalconfig = finalconfig + " " * 8 + i + " " + self.dirconfig[i] + "\n"
        finalconfig = finalconfig + " " * 4 + "</Directory>\n\n"
        # print log info
        finalconfig = finalconfig + " " * 4 + "LogLevel warn\n"
        finalconfig = finalconfig + " " * 4 + "ErrorLog ${APACHE_LOG_DIR}/error-" + self.baseconfig["ServerName"] + ".log\n"
        finalconfig = finalconfig + " " * 4 + "CustomLog ${APACHE_LOG_DIR}/access-" + self.baseconfig["ServerName"] + ".log custom\n"
        finalconfig = finalconfig + "</VirtualHost>\n"
        return finalconfig

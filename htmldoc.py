import os
from datetime import datetime

class HtmlDoc:
    def __init__(self,path,fileName, title):
        self.path = path
        self.fileName = fileName
        self.handle = open(path + "/" + fileName,"w")
        self.handle.write("<!DOCTYPE html>\n");
        self.handle.write('<html>\n<head><title>' + title + '</title>' +
            '<style>body{font-family: Arial}' + 
            'h1 {text-align: center;}' +
            '.container {text-align: center;}' + 
            '.table-container {display: inline-block;}' + 
            '.table-style {border-collapse: collapse;}' +
            '.table-style th, td{border: 1px solid #ccc;padding: 8px;}' +
            '</style>\n</head>\n<body>\n');
        self.handle.write("<h1>" + title + "</h1>\n");

    def __del__(self):
        if not self.handle.closed:
            self.handle.write("</body>\n</html>\n");
            self.handle.close()

    def addTable(self, c):
        data = datetime.utcfromtimestamp(c['creation_time'])
        data_formattata = data.strftime('%d/%m/%Y')

        self.handle.write('<div class="container">')
        self.handle.write('\n<div class="table-container">\n<table class="table-style">')
        self.handle.write("<tr><td>ID</td><td>" + str(c['id']) + "</td><td>Data</td><td>" + data_formattata + "</td></tr>")
        self.handle.write("<tr><td>Nome</td><td>" +  str(c['name']) + "</td><td>Slug</td><td>" + c['slug'] + "</td></tr>")
        self.handle.write("<tr><td>Tempo</td><td>" +  c['weather_condition'] + "</td><td>Temperatura</td><td>" +  
            str(c['weather_temperature']) + "</td></tr>\n")
        l = c['location']
        self.handle.write("<tr><td>Posto</td><td>" + l['name'] + "</td><td>Posizione lat/log</td><td>" + str(l['lat']) + "|" + str(l['lon']) + "</td></tr>")
        self.handle.write("</table></div><br>\n")
        imagePath = c['slug'] + '_' + str(c['id']) + '/photos/'
        videoPath = c['slug'] + '_' + str(c['id']) + '/videos/'
        self.printMultimediaFiles("Immagini", self.path, imagePath);
        self.printMultimediaFiles("Video", self.path , videoPath);
        self.handle.write("</div>")
        self.handle.write("<hr>\n")

    def addText(self,text):
        self.handle.write(text)                    

    def printMultimediaFiles(self,whatType, path,pathFiles):
        
        fullOsPath = path + "/" + pathFiles
        if os.path.isdir(fullOsPath) == False :
            return
        self.handle.write("<p>Tipo di file:" + whatType + "<br>Percorso:")
        multimediaFiles = os.listdir(fullOsPath)
        if len(multimediaFiles) != 0:
            for f in multimediaFiles:
                fullHtmlPath = pathFiles + f
                self.handle.write(fullHtmlPath + "<br>\n")
                if whatType == "Immagini":
                    self.handle.write('<img style="height: 100%;max-height: 1024px;width: auto;" src="' + fullHtmlPath + '"><br>\n')
                if whatType == "Video":
                    self.handle.write('<video controls style="height: 100%;max-height: 1024px;width: auto;"><source src="' + fullHtmlPath + '" type="video/mp4"></video><br>\n')
        self.handle.write("</p>")


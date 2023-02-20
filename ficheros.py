
import requests, os, time





def verificar_fichero():
  
    try:
        if os.path.isfile("liga_espanola.json")== False:
        
           liga_espanola = "https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/es.1.clubs.json"
           r=requests.get(liga_espanola)
           f= open("liga_espanola.json", "wb")
           f.write(r.content)
           r.close()
           f.close()
           
        
        
        if os.path.isfile("liga_alemana.json")== False:
        
            liga_alemana = "https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/de.1.clubs.json"
            r=requests.get(liga_alemana)
            f= open("liga_alemana.json", "wb")
            f.write(r.content)
            r.close()
            f.close()
            
        
        if os.path.isfile("liga_italiana.json")== False:
        
            liga_italiana = "https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/it.1.clubs.json"
            r=requests.get(liga_italiana)
            f= open("liga_italiana.json", "wb")
            f.write(r.content)
            r.close()
            f.close()
            
        
        if os.path.isfile("liga_austriaca.json")== False:
       
            liga_austriaca= "https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/at.2.clubs.json"
            r=requests.get(liga_austriaca)
            f= open("liga_austriaca.json", "wb")
            f.write(r.content)
            r.close()
            f.close()
            
        
        if os.path.isfile("liga_inglesa.json")== False:
        
            liga_inglesa = "https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/en.1.clubs.json"
            r=requests.get(liga_inglesa)
            f= open("liga_inglesa.json", "wb")
            f.write(r.content)
            r.close()
            f.close()
        
    except requests.ConnectionError:
        print("No tiene conexión a Internet")
        time.sleep(1)
        print("Verifique su conexión y vuelva a intentarlo")
        exit()

        


import subprocess

Services = ["apache2", "docker"]


def status():
    Dirct = {"id":[],"Service Name":[],"Status":[]}
    for i in range(len(Services)):
        stat = subprocess.call(["systemctl", "is-active", "--quiet", Services[i]])
        if(stat == 0):
            Dirct["id"].append(i)
            Dirct["Service Name"].append(Services[i])
            Dirct["Status"].append("Active")
            print(Dirct)
        else:
            Dirct["id"].append(i)
            Dirct["Service Name"].append(Services[i])
            Dirct["Status"].append("Not Active")
            print(Dirct)
        
    print(type(Dirct))
    return Dirct

import xml.etree.ElementTree as ET
def ip_check(ip,filename):
    tree = ET.parse(str(filename))
    root = tree.getroot()
    ip_correct = 0
    for i in range (0,len(ip.split('.'))):
        if len(ip.split('.'))==4 and ip.split('.')[i].isdigit():
            ip_correct += 1
    if ip_correct==4:
        x = []
        for i in range (len(ip.split('.'))):
            x.append(ip.split('.')[i])
        for child in root:
            for child in child:
                range_az= child.attrib['Subnet'].split('.')
                match = 0
                for j in range(len(range_az)):
                    if x[j]==range_az[j]:
                        match+=1
                if match >= 3:
                    print "Hoster is Microsoft Azure."
    else:
        print "Incorrect data! Please, type again."
        
ip = raw_input('Enter IP to find a host: ')
ip_check(ip,'ip_ranges.xml')


                    
                            

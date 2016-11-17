import xml.etree.ElementTree as ET
tree = ET.parse('ip_ranges.xml')
root = tree.getroot()
while True:
    x = []
    ip_correct = 0
    ip = raw_input('Enter IP to find a host: ')
    for i in range (0,len(ip.split('.'))):
        if len(ip.split('.'))==4 and ip.split('.')[i].isdigit():
            ip_correct += 1
    if ip_correct==4:
        for i in range (0,len(ip.split('.'))):
            x.append(ip.split('.')[i])
        print x
        for child in root:
            for child in child:
                print child.attrib['Subnet']

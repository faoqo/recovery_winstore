import zipfile
import platform
win_vers = platform.architecture()
Win_64_text = "('64bit', 'WindowsPE')"
Win_32_text = "('32bit', 'WindowsPE')"
str_winvers = str(win_vers)

if str_winvers == Win_64_text:
    fantasy_zip = zipfile.ZipFile('pack_64.zip')
    fantasy_zip.extractall('C:\\Ps\\Store')
    fantasy_zip.close()
    print ("unpack 64 to C")

elif str_winvers == Win_32_text:
    fantasy_zip = zipfile.ZipFile('pack_32.zip')
    fantasy_zip.extractall('C:\\Ps\\Store')
    fantasy_zip.close()
    print ("unpack 32 to C")
    
else:
    print("error win version")
import os
import os.path

# inputPath = input("Input the directory with all the files where you want to generate the deeplink pages with:")
# print(inputPath)
inputPath = "D:\Git\_Xamarin\HuhSoundboard\HuhSoundboard\HuhSoundboard\Sounds"
outputPath = ".\sound\\"

fileList = []

for dirpath, dirnames, filenames in os.walk(inputPath):
    for filename in [f for f in filenames if f.endswith(".mp3")]:
        fileList.append(filename[:-4])

for filestring in fileList:
    f = open(outputPath + filestring + ".html",'w')
    message = """
    <html>
    <head></head>
    <body>
        <h4>{0}</h4>
        <a
            href='http://play.google.com/store/apps/details?id=tm.appdevelopment.HuhSoundboard&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1'>
            <img alt='Ontdek het op Google Play' src='https://play.google.com/intl/en_us/badges/static/images/badges/nl_badge_web_generic.png' />
        </a>
    </body>
    </html>
    """.format(filestring)

    f.write(message)
    f.close()
from inui.toinui import HtmlToInui as hti

h = hti()

h.fromUrl("https://nextjs.org/")
h.save("nextjs.py")

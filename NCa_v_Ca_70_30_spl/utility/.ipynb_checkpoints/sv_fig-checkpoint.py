import matplotlib.pyplot as plt
import matplotlib as mpl
from PIL import Image
import io

# import matplotlib.pyplot as plt

# def savefig(filename, crop = True):
#     plt.savefig('{}.pdf'.format(filename))

def savefig(filename,crop=False,dpi=600,quality=95):
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    from PIL import Image
    import io

    fig = plt.gcf()

    mpl.rcParams['savefig.bbox'] = None
    bbox = 'tight' if crop else None

    buf = io.BytesIO()
    fig.savefig(
        buf,
        format='png',   
        bbox_inches=bbox,
        pad_inches=0,
        dpi=dpi
    )
    buf.seek(0)

    img = Image.open(buf).convert("RGB")
    img.save(
        f"{filename}.jpg",
        format="JPEG",
        quality=quality,      
        subsampling=0 
    )

    buf.close()
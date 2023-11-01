from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill

from .models import SiteIcon


class IconImage(ImageSpec):
    processors = [ResizeToFill(100, 100)]
    format = 'JPEG'
    options = {'quality': 60}


register.generator('siteicon:icon', IconImage)

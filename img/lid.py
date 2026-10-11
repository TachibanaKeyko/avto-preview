# оставляет от ноутбука только крышку с экраном: режем там, где строка становится шире крышки (начало корпуса)
import numpy as np
from PIL import Image

for f in ['tier1.png', 'tier2.png', 'tier3.png']:
    im = Image.open(f); a = np.array(im)[..., 3] > 128
    w = a.sum(1); h = len(w)
    lid = np.median(w[int(h * .2):int(h * .5)])
    cut = next(y for y in range(int(h * .5), h) if w[y] > lid * 1.03)
    im.crop((0, 0, im.size[0], cut - 2)).save(f.replace('tier', 'lid'))
    print(f, h, cut, lid)

# вырезает товар с кремовой подложки: фон тёплый (R заметно больше B), предмет нейтральный
import numpy as np
from PIL import Image
from scipy import ndimage as nd
import sys

for fn, out in [('Wb_89f76779be.png', 'wb.png'), ('2_6fb72f57f6.png', 'tier1.png'),
                ('3_dbf7ce1e83.png', 'tier2.png'), ('4_5d670bc67a.png', 'tier3.png')]:
    rgb = np.array(Image.open('src/' + fn).convert('RGB')).astype(np.int16)
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    warm = ((r - b) >= 8) & (r >= 120) & ((r - g) >= 2)
    lab, n = nd.label(warm)
    border = set(np.unique(np.r_[lab[0], lab[-1], lab[:, 0], lab[:, -1]])) - {0}
    bg = np.isin(lab, list(border))
    bg = nd.binary_closing(bg, iterations=2)
    fg = ~bg
    fg = nd.binary_fill_holes(nd.binary_opening(fg, iterations=2))
    fg = nd.binary_erosion(fg, iterations=2)
    # оставляем только крупнейший кусок
    lab2, n2 = nd.label(fg)
    if n2 > 1:
        s = nd.sum(fg, lab2, range(1, n2 + 1)); fg = lab2 == (np.argmax(s) + 1)
    alpha = nd.gaussian_filter(fg.astype(np.float32), 0.8)
    ys, xs = np.where(fg)
    im = np.dstack([rgb.astype(np.uint8), (alpha * 255).astype(np.uint8)])
    Image.fromarray(im, 'RGBA').crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)).save(out)
    print(out, xs.min(), ys.min(), xs.max(), ys.max())

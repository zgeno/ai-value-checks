# AI Value Checks: the shared one-page signature frame (1080x1350). Results are drawn as diagrams (path + tinted icon panels),
# in the accepted diagram style of infographics/WK46-FRI-gartner-service-roi/card.html.
# Same frame as The AI Value Gap Frameworks (infographics/FRAMEWORKS-BATCH-1/build.py, approved 8 Nov):
# header label left, wordmark centre, "No. NN" right, rule at 96px, teal kicker, 62px white+orange h1,
# notes block, rule at 1252px, footer. Header label: "AI VALUE CHECKS". Footer: "AN ORIGINAL SCALEBOTICS TOOL".
import os, html

HERE = os.path.dirname(os.path.abspath(__file__))
CARD = os.path.normpath(os.path.join(HERE, 'assets'))

T = '#2FD8B4'; OR = '#F3A55B'; CO = '#EE6F78'; PU = '#B58BEF'; BL = '#7E93F2'; CY = '#3FC6C9'
GR = '#93A19E'; TX = '#DDE5E3'; MU = '#C9D2D0'
STATUS = {'Ready': T, 'Partly': OR, 'Missing': CO, 'Not visible': BL}

I = {
 'target': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
 'flow': '<rect x="3" y="3" width="8" height="8" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect x="13" y="13" width="8" height="8" rx="2"/>',
 'chart': '<path d="M3 3v18h18"/><path d="M18 17V9M13 17V5M8 17v-3"/>',
 'coins': '<circle cx="8" cy="8" r="6"/><path d="M18.1 10.4A6 6 0 1 1 10.3 18"/><path d="M7 6h1v4"/>',
 'scale': '<path d="M12 3v18"/><path d="M5 7h14"/><path d="m5 7-3 6a3 3 0 0 0 6 0Z"/><path d="m19 7-3 6a3 3 0 0 0 6 0Z"/>',
 'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 'clock': '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 'plus': '<circle cx="12" cy="12" r="10"/><path d="M8 12h8M12 8v8"/>',
 'route': '<circle cx="12" cy="12" r="10"/><path d="M8 12h8"/><path d="m12 16 4-4-4-4"/>',
 'pointer': '<path d="m4 4 7 17 2.5-7.5L21 11Z"/>',
 'tick': '<path d="M20 6 9 17l-5-5"/>',
 'eye': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/><path d="M4 4l16 16"/>',
 'arrow': '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
 'trophy': '<path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/>',
}

def e(s):
    return html.escape(str(s), quote=False)

def ic(k, c, s=28):
    return ('<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round">%s</svg>') % (s, s, c, I[k])

def tile(k, c, s=46, i=24, r=12):
    return ('<div style="width:%dpx;height:%dpx;border-radius:%dpx;background:%s22;display:flex;align-items:center;'
            'justify-content:center;flex:none">%s</div>') % (s, s, r, c, ic(k, c, i))

def lab(t, c=GR, sz=15):
    return '<div style="font-size:%dpx;font-weight:700;letter-spacing:.18em;color:%s">%s</div>' % (sz, c, t)

CSS = '''*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;background:#070B0F;font-family:'Inter Tight',sans-serif;color:#F2F5F4;overflow:hidden;position:relative}
.bg{position:absolute;inset:0;background:radial-gradient(900px 500px at 50% -120px,rgba(47,216,180,.10),transparent 70%)}
.top{position:absolute;top:44px;left:72px;right:72px;height:36px;display:flex;align-items:center;justify-content:space-between;font-size:15px;font-weight:700;letter-spacing:.2em;color:#93A19E}
.top img{width:150px}
.kick{position:absolute;top:106px;left:72px;right:72px;text-align:center;font-size:15px;font-weight:700;letter-spacing:.22em;color:#2FD8B4}
.hr{position:absolute;left:72px;right:72px;border-top:1px solid rgba(255,255,255,.14)}
h1{position:absolute;top:136px;left:72px;right:72px;text-align:center;font-size:58px;font-weight:800;line-height:1.02;letter-spacing:-.025em}
h1 span{color:#F3A55B}
.dek{position:absolute;top:268px;left:96px;right:96px;text-align:center;font-size:20px;line-height:1.35;color:#B8C4C1}
.dek b{color:#F2F5F4}
.row{position:absolute;left:72px;right:72px;border-radius:16px;display:flex;align-items:center;gap:16px;padding:0 18px;overflow:hidden}
.row .pt{width:184px;flex:none}
.row .pt b{display:block;font-size:22px;font-weight:800;line-height:1.1}
.row .pt span{display:block;font-size:15px;color:#93A19E;line-height:1.3;margin-top:3px}
.row .have{flex:1;min-width:0;font-size:17px;line-height:1.3;color:#DDE5E3}
.row .gap{font-size:16px;line-height:1.3;color:#F2F5F4;margin-top:4px;font-weight:600}
.row .st{flex:none;width:108px;text-align:center;font-size:15px;font-weight:800;letter-spacing:.14em;padding:8px 0;border-radius:10px;border:1.5px solid}
.acts{position:absolute;left:72px;right:72px;list-style:none;counter-reset:a}
.acts li{counter-increment:a;display:flex;gap:14px;align-items:flex-start;font-size:19px;line-height:1.3;color:#DDE5E3;margin-top:10px}
.acts li:before{content:counter(a);flex:none;width:28px;height:28px;border-radius:8px;background:#2FD8B422;color:#2FD8B4;font-size:16px;font-weight:800;display:flex;align-items:center;justify-content:center}
.notes{position:absolute;left:72px;right:72px;font-size:15px;line-height:1.5;color:#93A19E}
.notes b{color:#F2F5F4}
.ft{position:absolute;top:1272px;left:72px;right:72px;display:flex;justify-content:space-between;font-size:15px;letter-spacing:.16em;font-weight:600;color:#5E6C69}'''

def page(out_path, no, kick, title, dek, body, notes, notes_top=1150):
    """Wrap a body in the signature frame. Asset paths are relative to the output file."""
    root = os.path.relpath(CARD, os.path.dirname(os.path.abspath(out_path)))
    nt = ''.join('<div>%s</div>' % n for n in notes)
    return ('<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="%s/fonts.css">'
            '<style>%s</style></head><body><div class="bg" data-layer="bg"></div>'
            '<div class="top"><span style="color:#2FD8B4">AI VALUE CHECKS</span><img src="%s/brand/wordmark.svg"><span>FREE TOOL</span></div>'
            '<div class="hr" style="top:96px"></div><div class="kick">%s</div>'
            '<h1>%s</h1><div class="dek">%s</div>%s'
            '<div class="hr" style="top:%dpx"></div><div class="notes" style="top:%dpx">%s</div>'
            '<div class="hr" style="top:1252px"></div><div class="ft"><span>AN ORIGINAL SCALEBOTICS TOOL</span>'
            '<span>SCALEBOTICS.IO · © 2026</span></div></body></html>'
            % (root, CSS, root, kick, title, dek, body, notes_top - 16, notes_top, nt))

def check_len(label, s, cap):
    if len(s) > cap:
        raise SystemExit('%s is %d characters; the one-page record allows %d. Shorten it in the JSON (do not cut meaning).'
                         % (label, len(s), cap))

def panel(x, y, w, h, c):
    """Colour-tinted panel background (bg layer, like the approved diagram cards)."""
    return ('<div data-layer="bg" style="position:absolute;left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:16px;'
            'background:linear-gradient(180deg,%s24,%s06 75%%);border:1.5px solid %s55"></div>') % (x, y, w, h, c, c, c)

def chip(status):
    c = STATUS[status]
    return ('<span style="display:inline-block;font-size:15px;font-weight:800;letter-spacing:.12em;padding:4px 10px;border-radius:8px;'
            'color:%s;background:%s1A;border:1.5px solid %s88">%s</span>') % (c, c, c, status.upper())

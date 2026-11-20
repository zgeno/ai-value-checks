# AI Value Checks No. 01, The What-Changed Check: renders the value record (JSON from the skill) as a one-page
# DIAGRAM, 1080x1350: the six parts as one path, left to right, each node joined to a colour-tinted icon panel
# (panels alternate above and below the path), then the next three actions as a three-step path.
# Usage: python3 render.py <record.json> <out.html>
#   then open the HTML in a browser (or screenshot it).
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from frame import page, tile, lab, ic, e, check_len, panel, chip, STATUS, T, OR, GR

PARTS = [('Boundary', 'What are we measuring?', 'target'),
         ('Workflow', 'Where does AI enter?', 'flow'),
         ('Baseline', 'Compared with what?', 'chart'),
         ('Full cost', 'At what full cost?', 'coins'),
         ('Attribution', 'How much is due to AI?', 'scale'),
         ('Ownership', 'Who owns it, who stops it?', 'user')]
NEXT = 'If you want help closing the gaps: an AI Deployment Readiness Review, scalebotics.io'

LINE_Y = 676
PW, PH = 300, 254
COLS = [72, 390, 708]                      # panel lefts; parts 1,3,5 above, 2,4,6 below
ABOVE_Y, BELOW_Y = LINE_Y - 40 - PH, LINE_Y + 40


def render(d, out):
    assert len(d['parts']) == 6 and all(p['status'] in STATUS for p in d['parts'])
    outside = d.get('view') == 'outside'
    check_len('use', d['use'], 60); check_len('why', d['why'], 125)
    ready = sum(p['status'] == 'Ready' for p in d['parts'])
    visible = sum(p['status'] != 'Not visible' for p in d['parts'])
    if outside:
        check_len('answer', d['answer'], 40); check_len('source', d['source'], 110)
        title = 'What did it change?<br><span>%s</span>' % e(d['answer'])
        count = 'FROM THE OUTSIDE: %d OF 6 VISIBLE · %d READY' % (visible, ready)
    else:
        res = '<span style="color:%s">Yes.</span>' % T if ready == 6 else '<span>Not yet: %d of 6 ready.</span>' % ready
        title = 'Can you show what it changed?<br>%s' % res
        count = '%d OF 6 READY' % ready

    svg = ['<svg data-layer="bg" width="1080" height="1350" style="position:absolute;left:0;top:0">',
           '<line x1="96" y1="%d" x2="984" y2="%d" stroke="#2FD8B4" stroke-opacity=".55" stroke-width="5" stroke-linecap="round"/>' % (LINE_Y, LINE_Y),
           '<path d="M972 %d l14 0" stroke="#2FD8B4" stroke-width="5"/><path d="m976 %d 12 8-12 8" fill="none" stroke="#2FD8B4" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>' % (LINE_Y, LINE_Y - 8)]
    body = ''
    for i, ((name, q, k), p) in enumerate(zip(PARTS, d['parts'])):
        c = STATUS[p['status']]
        col = COLS[i // 2]
        up = i % 2 == 0
        nx = col + PW // 2 + (-58 if up else 58)
        py = ABOVE_Y if up else BELOW_Y
        edge = py + PH if up else py
        svg.append('<path d="M%d %d L%d %d" stroke="%s" stroke-width="3" stroke-dasharray="8 7" fill="none"/>'
                   % (nx, LINE_Y + (-24 if up else 24), col + PW // 2, edge, c))
        svg.append('<circle cx="%d" cy="%d" r="24" fill="#070B0F" stroke="%s" stroke-width="4"/>' % (nx, LINE_Y, c))
        body += ('<div style="position:absolute;left:%dpx;top:%dpx;width:48px;text-align:center;font-size:20px;font-weight:800;color:%s;line-height:1">%d</div>'
                 % (nx - 24, LINE_Y - 10, c, i + 1))
        check_len('part %d have' % (i + 1), p['have'], 110)
        gap = ''
        if p['status'] != 'Ready':
            check_len('part %d close' % (i + 1), p.get('close', ''), 100)
            gap = '<div style="margin-top:8px;font-size:16px;line-height:1.3;color:#F2F5F4;font-weight:600">→ %s</div>' % e(p['close'])
        body += panel(col, py, PW, PH, c)
        body += ('<div data-fit style="position:absolute;left:%dpx;top:%dpx;width:%dpx;height:%dpx;overflow:hidden">'
                 '<div style="display:flex;gap:12px;align-items:center">%s<div><b style="display:block;font-size:20px;line-height:1.1;color:%s">%s</b>'
                 '<div style="font-size:15px;color:#93A19E;margin-top:2px">%s</div></div></div>'
                 '<div style="margin-top:8px">%s</div>'
                 '<div style="margin-top:8px;font-size:16px;line-height:1.3;color:#DDE5E3">%s</div>%s</div>'
                 % (col + 16, py + 14, PW - 32, PH - 24, tile(k, c, 42, 22, 11), c, name, q, chip(p['status']), e(p['have']), gap))
    svg.append('</svg>')

    # where the count sits: on the path, left end
    body += ('<div style="position:absolute;left:72px;right:72px;top:%dpx;text-align:center;font-size:15px;font-weight:700;letter-spacing:.18em;color:%s">%s</div>'
             % (LINE_Y + 40 + PH + 18, GR, count))
    # next three actions: a three-step path
    ay = LINE_Y + 40 + PH + 52
    body += '<div style="position:absolute;top:%dpx;left:72px;right:72px">%s</div>' % (ay, lab('NEXT THREE ACTIONS', OR))
    for a in d['actions'][:3]:
        check_len('action', a, 82)
    aw = 288
    for j, a in enumerate(d['actions'][:3]):
        x = 72 + j * (aw + 36)
        body += panel(x, ay + 30, aw, 96, OR)
        body += ('<div data-fit style="position:absolute;left:%dpx;top:%dpx;width:%dpx;height:80px;overflow:hidden;display:flex;gap:10px;align-items:flex-start">'
                 '<b style="flex:none;width:26px;height:26px;border-radius:8px;background:#F3A55B22;color:#F3A55B;font-size:16px;display:flex;align-items:center;justify-content:center">%d</b>'
                 '<div style="font-size:16px;line-height:1.3;color:#DDE5E3">%s</div></div>' % (x + 12, ay + 38, aw - 24, j + 1, e(a)))
        if j < 2:
            body += '<div style="position:absolute;left:%dpx;top:%dpx;width:28px;height:28px">%s</div>' % (x + aw + 4, ay + 64, ic('arrow', OR, 28))
    notes = []
    if outside:
        notes.append('<b>Source:</b> %s' % e(d['source']))
    notes.append('<b>Next step:</b> ' + NEXT + '. <b>Method:</b> “How to show what your AI changed”, L. Okiy, <i>The AI Value Gap</i> (2026).')
    return page(out, 1, 'THE WHAT-CHANGED CHECK', title, '<b>%s.</b> %s' % (e(d['use']), e(d['why'])),
                ''.join(svg) + body, notes, notes_top=1176)


if __name__ == '__main__':
    d = json.load(open(sys.argv[1]))
    open(sys.argv[2], 'w').write(render(d, sys.argv[2]))

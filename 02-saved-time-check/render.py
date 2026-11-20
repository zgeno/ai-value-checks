# AI Value Checks No. 02, The Saved-Time Check: renders the check result (JSON from the skill) as a one-page
# DIAGRAM, 1080x1350: the three levels the hours can reach as a path (estimated capacity -> measured capacity
# -> value), the four questions as gates on the path, each joined to a colour-tinted icon panel, the usage
# question below, then the next three actions as a three-step path.
# Usage: python3 render.py <check.json> <out.html>
#   then open the HTML in a browser (or screenshot it).
# It never computes money. The only numbers on the page are the ones the user gave.
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from frame import page, tile, lab, ic, e, check_len, panel, chip, STATUS, T, OR, GR

QS = [('How was the time measured?', 'clock'),
      ('What work was added?', 'plus'),
      ('Where did the capacity go?', 'route'),
      ('Which outcome changed?', 'target'),
      ('What does usage data prove?', 'pointer')]
LEVELS = ['Estimated capacity', 'Measured capacity', 'Value']
NEXT = 'If you want help turning hours into results: an Executive Briefing, scalebotics.io'

PW, PH, GAP = 222, 290, 16
LEFTS = [72 + i * (PW + GAP) for i in range(4)]
LV_Y, LINE_Y, PANEL_Y = 384, 500, 546


def level(parts):
    s = [p['status'] for p in parts]
    if s[0] != 'Ready' or s[1] != 'Ready':
        return 0          # gross, guessed or unseen hours: estimated capacity at most
    if s[2] == 'Ready' and s[3] == 'Ready':
        return 2          # measured, net of added work, put to named work, and an outcome moved
    return 1


def render(d, out):
    assert len(d['parts']) == 5 and all(p['status'] in STATUS for p in d['parts'])
    outside = d.get('view') == 'outside'
    check_len('use', d['use'], 60); check_len('claim', d['claim'], 125)
    ans = sum(p['status'] == 'Ready' for p in d['parts'][:4])
    lv = level(d['parts'])
    if outside:
        check_len('answer', d['answer'], 40); check_len('source', d['source'], 110)
        res = '<span>%s</span>' % e(d['answer'])
    else:
        res = '<span style="color:%s">Yes.</span>' % T if lv == 2 else '<span>Not yet: %d of 4 answered.</span>' % ans

    # 1. the three levels, as a path; the level the hours reach today is filled
    body = '<div style="position:absolute;top:%dpx;left:72px;right:72px;text-align:center">%s</div>' % (
        LV_Y - 26, lab('WHERE THE HOURS STAND' + (' FROM THE OUTSIDE' if outside else ' TODAY'), GR))
    body += '<div style="position:absolute;top:%dpx;left:72px;right:72px;display:flex;align-items:center;gap:10px">' % (LV_Y + 4)
    for i, name in enumerate(LEVELS):
        on = i == lv
        c = [OR, OR, T][i] if on else GR
        body += ('<div style="flex:1;height:52px;border-radius:26px;display:flex;align-items:center;justify-content:center;gap:10px;'
                 'font-size:16px;font-weight:800;letter-spacing:.12em;%s">%s%s</div>'
                 % ('background:%s;color:#06090C' % c if on else 'background:%s12;border:1.5px dashed %s66;color:%s' % (GR, GR, GR),
                    ic('tick', '#06090C', 20) if on else '', name.upper()))
        if i < 2:
            body += ic('arrow', GR, 24)
    body += '</div>'

    # 2. the gates: questions 1-4 on one path, joined to their panels
    svg = ['<svg data-layer="bg" width="1080" height="1350" style="position:absolute;left:0;top:0">',
           '<line x1="96" y1="%d" x2="980" y2="%d" stroke="#2FD8B4" stroke-opacity=".55" stroke-width="5" stroke-linecap="round"/>' % (LINE_Y, LINE_Y),
           '<path d="m974 %d 12 8-12 8" fill="none" stroke="#2FD8B4" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>' % (LINE_Y - 8)]
    for i, ((q, k), p) in enumerate(zip(QS[:4], d['parts'][:4])):
        c = STATUS[p['status']]
        x = LEFTS[i]; cx = x + PW // 2
        svg.append('<path d="M%d %d L%d %d" stroke="%s" stroke-width="3" stroke-dasharray="8 7"/>' % (cx, LINE_Y + 24, cx, PANEL_Y, c))
        svg.append('<circle cx="%d" cy="%d" r="24" fill="#070B0F" stroke="%s" stroke-width="4"/>' % (cx, LINE_Y, c))
        body += ('<div style="position:absolute;left:%dpx;top:%dpx;width:48px;text-align:center;font-size:20px;font-weight:800;color:%s;line-height:1">%d</div>'
                 % (cx - 24, LINE_Y - 10, c, i + 1))
        check_len('question %d have' % (i + 1), p['have'], 110)
        gap = ''
        if p['status'] != 'Ready':
            check_len('question %d close' % (i + 1), p.get('close', ''), 100)
            gap = '<div style="margin-top:8px;font-size:15px;line-height:1.3;color:#F2F5F4;font-weight:600">→ %s</div>' % e(p['close'])
        body += panel(x, PANEL_Y, PW, PH, c)
        body += ('<div data-fit style="position:absolute;left:%dpx;top:%dpx;width:%dpx;height:%dpx;overflow:hidden">'
                 '<div style="display:flex;gap:10px;align-items:center">%s<b style="font-size:17px;line-height:1.15;color:%s">%s</b></div>'
                 '<div style="margin-top:8px">%s</div>'
                 '<div style="margin-top:8px;font-size:15px;line-height:1.3;color:#DDE5E3">%s</div>%s</div>'
                 % (x + 14, PANEL_Y + 14, PW - 28, PH - 22, tile(k, c, 38, 20, 10), c, q, chip(p['status']), e(p['have']), gap))
    svg.append('</svg>')

    # 3. also ask: usage data, one slim panel
    p = d['parts'][4]; c = STATUS[p['status']]; uy = PANEL_Y + PH + 18
    check_len('usage have', p['have'], 110)
    close = ''
    if p['status'] != 'Ready':
        check_len('usage close', p.get('close', ''), 100)
        close = ' <b style="color:#F2F5F4">→ %s</b>' % e(p['close'])
    body += panel(72, uy, 936, 92, c)
    body += ('<div data-fit style="position:absolute;left:88px;top:%dpx;width:904px;height:76px;overflow:hidden;display:flex;gap:14px;align-items:center">'
             '%s<div style="flex:none;width:200px"><div style="font-size:15px;font-weight:700;letter-spacing:.16em;color:%s">ALSO ASK</div>'
             '<b style="font-size:17px;color:%s">%s</b></div><div style="flex:none">%s</div>'
             '<div style="font-size:15px;line-height:1.3;color:#DDE5E3">%s%s</div></div>'
             % (uy + 8, tile(QS[4][1], c, 38, 20, 10), c, c, QS[4][0], chip(p['status']), e(p['have']), close))

    # 4. next three actions: a three-step path
    ay = uy + 92 + 18
    body += '<div style="position:absolute;top:%dpx;left:72px;right:72px">%s</div>' % (ay, lab('NEXT THREE ACTIONS', OR))
    for a in d['actions'][:3]:
        check_len('action', a, 82)
    aw = 288
    for j, a in enumerate(d['actions'][:3]):
        x = 72 + j * (aw + 36)
        body += panel(x, ay + 28, aw, 92, OR)
        body += ('<div data-fit style="position:absolute;left:%dpx;top:%dpx;width:%dpx;height:78px;overflow:hidden;display:flex;gap:10px;align-items:flex-start">'
                 '<b style="flex:none;width:26px;height:26px;border-radius:8px;background:#F3A55B22;color:#F3A55B;font-size:16px;display:flex;align-items:center;justify-content:center">%d</b>'
                 '<div style="font-size:16px;line-height:1.3;color:#DDE5E3">%s</div></div>' % (x + 12, ay + 36, aw - 24, j + 1, e(a)))
        if j < 2:
            body += '<div style="position:absolute;left:%dpx;top:%dpx;width:28px;height:28px">%s</div>' % (x + aw + 4, ay + 60, ic('arrow', OR, 28))
    notes = []
    if outside:
        notes.append('<b>Source:</b> %s' % e(d['source']))
    notes.append('<b>Next step:</b> ' + NEXT + '. <b>Method:</b> “Saved time is capacity, not cash”, L. Okiy, <i>The AI Value Gap</i> (2026). No hours × salary.')
    return page(out, 2, 'THE SAVED-TIME CHECK', 'Do the hours count as value?<br>%s' % res,
                '<b>%s.</b> %s%s' % (e(d['use']), 'The usual claim for this kind of assistant: ' if outside else '', e(d['claim'])), ''.join(svg) + body, notes, notes_top=1176)


if __name__ == '__main__':
    d = json.load(open(sys.argv[1]))
    open(sys.argv[2], 'w').write(render(d, sys.argv[2]))

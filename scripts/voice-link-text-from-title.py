#!/usr/bin/env python3
"""Voice drain step 1 (epic qou-d4kh, owner ruling 2026-11-20, #8526 comment 7041693067).

Replaces link text that is a raw block label ([`rem:x`](#rem:x)) with the target
block's title, or a short form of it cut at the first " — ", ": ", " (", ", ", " via " or
" and " (<=100 chars). Skipped and left for hand editing: titles over 110 chars
with no cut point, titles naming Lean/Mathlib, titles containing | [ ] or a
backtick, labels with no title, and links whose anchor/file is a different block.

Needs /tmp/w14b/labels.json (label -> title), produced by
`bun run scripts/voice-block-labels.ts > /tmp/w14b/labels.json`.
Usage: python3 scripts/voice-link-text-from-title.py dry|apply [excluded .md ...]
"""
import json,re,sys,glob,collections
L=json.load(open('/tmp/w14b/labels.json')); labels=L['labels']
excl=set(sys.argv[2:]) if len(sys.argv)>2 else set()
apply=len(sys.argv)>1 and sys.argv[1]=='apply'
RE=re.compile(r'\[`((?:def|thm|lem|prop|cor|conj|rem|ex|sim|sec|chap|app|eq|fig|tab|alg|defn|obs|prf):[\w.:-]+)`\]\(([^)\s]*)\)')
stats=collections.Counter(); lens=[]; samples=[]
def short(t):
    t=t.strip().rstrip('.')
    if len(t)<=110: return t
    for sep in [' — ',' -- ',': ',' (',', ',' via ',' and ']:
        i=t.find(sep)
        if 15<=i<=100 and t[:i].count('$')%2==0 and t[:i].count('(')==t[:i].count(')'): return t[:i].rstrip(' ,;:')
    return None
files=0
for f in glob.glob('folio/quantum-observable-universe/**/*.md',recursive=True):
    if f in excl: continue
    s=open(f).read(); 
    def rep(m):
        lab,tgt=m.group(1),m.group(2)
        anchor=tgt.split('#',1)[1] if '#' in tgt else None
        if anchor and anchor!=lab: stats['anchor-mismatch']+=1; return m.group(0)
        info=labels.get(lab)
        if not info or not info.get('title'): stats['no-title']+=1; return m.group(0)
        if not anchor:
            # file link: check it points to the label's file
            if not tgt.endswith(info['file'].split('/')[-1]): stats['file-mismatch']+=1; return m.group(0)
        t=short(info['title'])
        if t is None: stats['too-long']+=1; samples.append(info['title']); return m.group(0)
        if re.search(r'\bLean\b|\bMathlib\b|formali[sz]|\bproof assistant\b',t,re.I): stats['lean-title']+=1; return m.group(0)
        if '|' in t or ']' in t or '[' in t or '`' in t: stats['unsafe-char']+=1; return m.group(0)
        stats['fixed']+=1; lens.append(len(t))
        return '['+t+']('+tgt+')'
    n=RE.sub(rep,s)
    if n!=s:
        files+=1
        if apply: open(f,'w').write(n)
print(dict(stats),'files',files)
print('too long examples:',samples[:8])

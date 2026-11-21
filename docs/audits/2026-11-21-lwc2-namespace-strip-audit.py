import re, sys, pathlib, json
diff = open(sys.argv[1]).read()
repo = pathlib.Path(sys.argv[2])
KW = r'(?:private\s+|protected\s+|noncomputable\s+|@\[[^\]]*\]\s*)*(?:theorem|lemma|def|abbrev|instance|structure|class|inductive)'
pairs = []
cur = None; minus = []
for line in diff.splitlines():
    if line.startswith('diff --git'):
        cur = line.split(' b/')[-1]; minus = []
        continue
    if not cur or not cur.endswith('.lean'): continue
    m = re.match(r'^-\s*(' + KW + r')\s+([\w\'.₀-₉]+)', line)
    if m and not line.startswith('---'):
        minus.append((m.group(1), m.group(2))); continue
    p = re.match(r'^\+\s*(' + KW + r')\s+([\w\'.₀-₉]+)', line)
    if p and not line.startswith('+++') and minus:
        kw, old = minus.pop(0); new = p.group(2)
        if old.endswith('.' + new) or old != new:
            pairs.append((cur, old, new))
def ns_at(lines, idx):
    st = []
    for l in lines[:idx]:
        m = re.match(r'^\s*namespace\s+(\S+)', l)
        if m: st.append(m.group(1)); continue
        m = re.match(r'^\s*end\s+(\S+)\s*$', l)
        if m and st and st[-1] == m.group(1): st.pop()
    return '.'.join(st)
out = {'repaired':[], 'correct':[], 'suspect':[], 'gone':[]}
for f, old, new in pairs:
    path = repo / f.replace('content/', 'folio/', 1)
    if not path.exists():
        path = repo / f
    if not path.exists():
        out['gone'].append((f, old, new, 'file missing')); continue
    lines = path.read_text().splitlines()
    prefix = old[:-len(new)-1] if old.endswith('.'+new) else None
    hit_old = [i for i,l in enumerate(lines) if re.match(r'^\s*'+KW+r'\s+'+re.escape(old)+r'\b', l)]
    hit_new = [i for i,l in enumerate(lines) if re.match(r'^\s*'+KW+r'\s+'+re.escape(new)+r'(?![\w\'.])', l)]
    if hit_old:
        out['repaired'].append((str(path.relative_to(repo)), old, new)); continue
    if not hit_new:
        out['gone'].append((str(path.relative_to(repo)), old, new, 'decl not found')); continue
    ns = ns_at(lines, hit_new[0])
    if prefix and (ns == prefix or ns.endswith('.'+prefix)):
        out['correct'].append((str(path.relative_to(repo)), old, new, ns))
    else:
        out['suspect'].append((str(path.relative_to(repo)), old, new, ns, hit_new[0]+1))
print(len(pairs), {k:len(v) for k,v in out.items()})
json.dump(out, open(sys.argv[3],'w'), indent=1, ensure_ascii=False)

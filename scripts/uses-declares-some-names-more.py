#!/usr/bin/env python3
"""The class fwr10's scan cannot see.

fwr10 scopes to blocks with an EMPTY `uses[]`. A block that declares two
prerequisites while naming five in its prose is invisible to that scan, yet
it is the *same* defect — and arguably a stronger signal, because the author
demonstrably was declaring dependencies and still missed some.

`prf:genus-filtration-ideal` is the worked case: four lemmas named in prose,
one declared.

As with fwr10: the prose count PRIORITISES a reading. It is never a source to
populate from.
"""
import json
import os
import re
import sys
from collections import Counter

ROOT = "folio/quantum-observable-universe"
LAB = re.compile(r'label:\s*"([^"]+)"')
USES = re.compile(r'uses:\s*\[(.*?)\]', re.S)
STR = re.compile(r'"([^"]+)"')
KIND = re.compile(r'export default (\w+)\(')
MD_LINK = re.compile(r'\]\(#([a-z]+:[a-z0-9-]+)\)')
MD_TICK = re.compile(r'`(#?[a-z]+:[a-z0-9-]+)`')


def strip_comments(s):
    return re.sub(r'(?m)//.*$', '', re.sub(r'/\*.*?\*/', '', s, flags=re.S))


def main():
    blocks = {}
    for dp, _d, fs in os.walk(ROOT):
        for f in fs:
            if not f.endswith(".ts") or f[:-3] == os.path.basename(dp):
                continue
            p = os.path.join(dp, f)
            s = open(p, encoding="utf-8").read()
            m = LAB.search(s)
            if not m:
                continue
            u = USES.search(s)
            k = KIND.search(s)
            md_p = p[:-3] + ".md"
            md = open(md_p, encoding="utf-8").read() if os.path.exists(md_p) else ""
            blocks[m.group(1)] = dict(
                kind=k.group(1) if k else "?",
                uses=STR.findall(u.group(1)) if u else [],
                md=md, ts=p)

    labels = set(blocks)
    rows = []
    for lbl, b in blocks.items():
        if not b["uses"]:
            continue                      # fwr10's scope; not ours
        named = {h for h in MD_LINK.findall(b["md"])} | \
                {h.lstrip("#") for h in MD_TICK.findall(b["md"])}
        named = {n for n in named if n in labels and n != lbl}
        undeclared = named - set(b["uses"])
        if undeclared:
            rows.append((len(undeclared), lbl, b, sorted(undeclared)))
    rows.sort(key=lambda r: -r[0])

    print(f"blocks with a NON-empty uses[] that name undeclared blocks in prose: "
          f"{len(rows)}", file=sys.stderr)
    buckets = Counter("5+" if n >= 5 else ("3-4" if n >= 3 else "1-2")
                      for n, _l, _b, _u in rows)
    print(f"by undeclared count: {dict(buckets)}", file=sys.stderr)
    head = [r for r in rows if r[0] >= 3]
    print(f"high-signal head (3+ undeclared): {len(head)}", file=sys.stderr)
    print(f"kinds in head: {dict(Counter(b['kind'] for _n, _l, b, _u in head))}\n",
          file=sys.stderr)
    for n, lbl, b, und in head[:25]:
        print(f"  {n:2d} undeclared  {lbl:52s} declares {len(b['uses'])}", file=sys.stderr)
    json.dump([dict(label=l, kind=b["kind"], ts=b["ts"], declares=b["uses"],
                    undeclared=u, n=n) for n, l, b, u in rows],
              open(sys.argv[1], "w"), indent=1)
    print(f"\nwrote {len(rows)} -> {sys.argv[1]}", file=sys.stderr)


main()

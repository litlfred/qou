#!/usr/bin/env python3
"""Deterministic sampler + blind-packet builder for the qou-ncxf round-trip audits.

Read-only. Population: provable blocks (theorem/proposition/lemma/corollary)
in folio/quantum-observable-universe that have
  (1) a statement .md,
  (2) a prf:* block whose uses[] names the label, with a non-empty .md,
  (3) a lean.ref whose declaration is found in a .lean file under the paper
      and is a theorem/lemma (not `: True`, not containing `sorry`).
Sampling rule: sort eligible labels by sha256(label) and take the first N.
Blind packets strip Lean comments/docstrings and rename the target
declaration to `thm` so the name cannot leak the claim.

Usage:
  roundtrip-blind-sample.py [N] [--offset K] > packets.json
      first N eligible packets after skipping the first K eligible labels
      (pass 1 used N=10, K=0; pass 2 continues with K = the pass-1 cursor).
  roundtrip-blind-sample.py --ref-audit > refs.json
      classify what every provable block's qou: lean.ref names
      (theorem / lemma / def / structure / class / abbrev / instance /
      module / not-found). Population: every provable block with a qou: ref,
      not only the proof-bearing ones. Mechanical; no agents.

Declaration lookup accepts a dotted written name: a ref
`QOU.Foo.Bar.baz` matches `theorem baz`, `theorem Bar.baz` or
`theorem Foo.Bar.baz` (any dotted suffix of the ref), longest first.
(Pass 1 missed `QuantumObservableUniverse.exists_instance` this way.)
"""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPER = ROOT / "folio/quantum-observable-universe"
ARGS = [a for a in sys.argv[1:]]
REF_AUDIT = "--ref-audit" in ARGS
OFFSET = 0
if "--offset" in ARGS:
    OFFSET = int(ARGS[ARGS.index("--offset") + 1])
_pos = [a for i, a in enumerate(ARGS) if not a.startswith("--")
        and not (i > 0 and ARGS[i - 1] == "--offset")]
N = int(_pos[0]) if _pos else 10

KIND_RE = re.compile(r'^export default (theorem|proposition|lemma|corollary|proof)\(', re.M)
LABEL_RE = re.compile(r'label:\s*"([^"]+)"')
REF_RE = re.compile(r'ref:\s*"qou:([^"]+)"')
USES_RE = re.compile(r'uses:\s*\[(.*?)\]', re.S)

def strip_lean_comments(s: str) -> str:
    out, i, depth = [], 0, 0
    while i < len(s):
        if s.startswith("/-", i):
            depth += 1; i += 2; continue
        if depth and s.startswith("-/", i):
            depth -= 1; i += 2; continue
        if depth:
            i += 1; continue
        if s.startswith("--", i):
            j = s.find("\n", i); i = len(s) if j < 0 else j; continue
        out.append(s[i]); i += 1
    return re.sub(r'\n\s*\n+', '\n', "".join(out))

TOP = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private |protected |noncomputable )*'
                 r'(theorem|lemma|def|abbrev|structure|class|instance|example|namespace|end|section|variable|open|noncomputable)\b', re.M)

def _suffixes(ref: str):
    parts = ref.split(".")
    return [".".join(parts[i:]) for i in range(len(parts) - 1, -1, -1)][::-1]

_LEAN_FILES = None
def _lean_files():
    global _LEAN_FILES
    if _LEAN_FILES is None:
        _LEAN_FILES = []
        for f in sorted(PAPER.rglob("*.lean")):
            if ".lake" in f.parts: continue
            try: _LEAN_FILES.append((f, f.read_text()))
            except Exception: continue
    return _LEAN_FILES

DECL_KINDS = r'(theorem|lemma|def|abbrev|structure|class|instance|inductive|opaque|axiom)'

def locate(ref: str, kinds: str = r'(theorem|lemma)'):
    """First (file, text, match) whose declaration name is a dotted suffix of ref."""
    alts = "|".join(re.escape(x) for x in sorted(_suffixes(ref), key=len, reverse=True))
    pat = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private |protected |noncomputable )*'
                     + kinds + r'\s+(?:' + alts + r')(?![\w.\'])', re.M)
    for f, txt in _lean_files():
        m = pat.search(txt)
        if m: return f, txt, m
    return None

def find_decl(ref: str):
    hit = locate(ref)
    if not hit: return None
    f, txt, m = hit
    if True:
        nxt = TOP.search(txt, m.end())
        body = txt[m.start(): nxt.start() if nxt else len(txt)]
        # variable lines in effect before the decl (generic-ring binders)
        vars_ = re.findall(r'^variable .*$', txt[:m.start()], re.M)
        ctx = []
        for dm in re.finditer(r'^(?:@\[[^\]]*\]\s*)?(?:private |protected |noncomputable )*(def|abbrev|structure|class|instance|inductive)\b', txt, re.M):
            if dm.start() == m.start(): continue
            dn = TOP.search(txt, dm.end())
            ctx.append(strip_lean_comments(txt[dm.start(): dn.start() if dn else len(txt)]).strip())
        context = "\n".join(ctx)
        if len(context) > 6000: context = context[:6000] + "\n... [truncated]"
        return f, body, vars_, context
    return None

def classify_ref(ref: str):
    """What does a qou: lean.ref name? Returns (class, file-or-None, detail)."""
    hit = locate(ref, DECL_KINDS)
    if hit:
        f, txt, m = hit
        kind = m.group(1)
        detail = ""
        if kind in ("def", "abbrev"):
            nxt = TOP.search(txt, m.end())
            head = strip_lean_comments(txt[m.start(): nxt.start() if nxt else len(txt)]).partition(":=")[0]
            if re.search(r':\s*Prop\s*$', head.strip()): detail = "Prop-valued definition"
        return kind, str(f.relative_to(ROOT)), detail
    # module: ref spells a file path QOU/A/B.lean (or a sibling paper file)
    rel = ref.replace(".", "/") + ".lean"
    for f, _ in _lean_files():
        if str(f).endswith("/" + rel) or str(f).endswith("/lean/" + rel):
            return "module", str(f.relative_to(ROOT)), ""
    return "not-found", None, ""

def main():
    blocks = {}
    for ts in PAPER.glob("*/*.ts"):
        t = ts.read_text()
        km = KIND_RE.search(t); lm = LABEL_RE.search(t)
        if not km or not lm: continue
        blocks[lm.group(1)] = (km.group(1), ts, t)
    proofs = {}
    for lab, (k, ts, t) in blocks.items():
        if k != "proof": continue
        um = USES_RE.search(t)
        if not um: continue
        for u in re.findall(r'"([^"]+)"', um.group(1)):
            md = ts.with_suffix(".md")
            if md.exists() and md.read_text().strip():
                proofs.setdefault(u, (lab, md))
    elig = []
    for lab, (k, ts, t) in blocks.items():
        if k == "proof" or lab not in proofs: continue
        md = ts.with_suffix(".md"); rm = REF_RE.search(t)
        if not md.exists() or not rm: continue
        elig.append(lab)
    elig.sort(key=lambda l: hashlib.sha256(l.encode()).hexdigest())
    if REF_AUDIT:
        rows, counts = [], {}
        for lab, (k, ts, t) in sorted(blocks.items(), key=lambda kv: hashlib.sha256(kv[0].encode()).hexdigest()):
            if k == "proof": continue
            rm = REF_RE.search(t)
            if not rm: continue
            cls, f, detail = classify_ref(rm.group(1))
            key = cls + (" (" + detail + ")" if detail else "")
            counts[key] = counts.get(key, 0) + 1
            rows.append({"label": lab, "kind": k, "lean_ref": rm.group(1), "names": cls,
                         "detail": detail, "file": f, "has_proof_block": lab in proofs,
                         "stmt_ts": str(ts.relative_to(ROOT))})
        json.dump({"population": len(rows), "counts": counts, "rows": rows}, sys.stdout, indent=1)
        return
    out, skipped = [], []
    for lab in elig[OFFSET:]:
        if len(out) >= N: break
        k, ts, t = blocks[lab]
        ref = REF_RE.search(t).group(1); short = ref.split(".")[-1]
        hit = find_decl(ref)
        if not hit: skipped.append((lab, "decl-not-found")); continue
        f, body, vars_, context = hit
        clean = strip_lean_comments(body).strip()
        if "sorry" in clean: skipped.append((lab, "sorry")); continue
        head, sep, proof = clean.partition(":=")
        if re.search(r':\s*True\s*$', head.strip()): skipped.append((lab, "True")); continue
        head = re.sub(r'\b(theorem|lemma)\s+' + re.escape(short) + r'\b', r'\1 thm', head, count=1)
        plab, pmd = proofs[lab]
        out.append({
            "label": lab, "kind": k, "lean_ref": ref,
            "stmt_md": str(ts.with_suffix(".md").relative_to(ROOT)),
            "proof_label": plab, "proof_md": str(pmd.relative_to(ROOT)),
            "lean_file": str(f.relative_to(ROOT)),
            "lean_variables": [strip_lean_comments(v).strip() for v in vars_],
            "lean_context": context, "lean_statement": head.strip(), "lean_proof": proof.strip(),
            "md_statement": ts.with_suffix(".md").read_text(),
            "md_proof": pmd.read_text(),
        })
    json.dump({"population": len(elig), "sample_rule": "first N eligible by sha256(label)",
               "N": N, "offset": OFFSET, "skipped": skipped, "packets": out}, sys.stdout, indent=1)

main()

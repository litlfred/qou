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

Usage: roundtrip-blind-sample.py [N] > packets.json
"""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPER = ROOT / "folio/quantum-observable-universe"
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10

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

def find_decl(short: str):
    pat = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private |protected )*(theorem|lemma)\s+' + re.escape(short) + r'\b', re.M)
    for f in sorted(PAPER.rglob("*.lean")):
        if ".lake" in f.parts: continue
        try: txt = f.read_text()
        except Exception: continue
        m = pat.search(txt)
        if not m: continue
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
    out, skipped = [], []
    for lab in elig:
        if len(out) >= N: break
        k, ts, t = blocks[lab]
        ref = REF_RE.search(t).group(1); short = ref.split(".")[-1]
        hit = find_decl(short)
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
               "N": N, "skipped": skipped, "packets": out}, sys.stdout, indent=1)

main()

#!/usr/bin/env python3
"""Which self-assuming Lean declarations back a PAPER claim?

`lean-self-assuming-audit.py` finds theorems whose body projects a class field
whose type IS the conclusion (AGENTS.md §3b-cond item 5).  It reports them as
Lean declarations, which is the right unit for repairing Lean and the wrong
unit for asking what the PAPER asserts.

A projection sitting in a library file is an API accessor and harms nothing.
The same projection reached by a content block's `lean.ref` is a paper-level
`theorem` / `proposition` / `corollary` whose formal backing assumes what it
states.  §3b-cond permits that -- item 3 requires the `.md` to open with an
explicit conditional banner naming the hypothesis.  This joins the two so the
banner can be checked.

MATCHING.  On the FULLY-QUALIFIED declaration name, never on its last segment.
A first version matched the last segment and paired `prop:quantum-universe-
exists` with `QuantumObservableUniverse.exists_instance` -- two real, distinct
declarations in two files, both ending `exists_instance`.  That inflated the
count by one and would have reported a defect in a block that has none.

OUTPUT IS A CANDIDATE LIST, NOT A VERDICT.  The banner check is a regex over
prose and is measuring phrasing, not honesty: `prop:sw-period-residue-sum`
scores zero and its 725-word `.md` is scrupulously scoped, with the open
geometric content named and beaned.  Read the narrative before calling
anything an over-claim.

Usage:  scripts/lean-self-assuming-content-join.py [--root content]
"""
from __future__ import annotations
import argparse, collections, pathlib, re, subprocess, sys

AUDIT = "scripts/lean-self-assuming-audit.py"
ENTRY_RE = re.compile(r"\n  (?:theorem|lemma) (\S+)\n    (\S+?):(\d+)\n", re.S)
KIND_RE = re.compile(
    r"\b(definition|theorem|lemma|proposition|corollary|conjecture|remark|prose|example)"
    r"\s*\(\s*\{")
PROVABLE = {"theorem", "lemma", "proposition", "corollary"}
BANNER = re.compile(
    r"conditional on|assuming\b|hypothes[ei]s class|given the class|"
    r"\baccessor\b|\bprojection\b|item 5", re.I)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="folio")
    a = ap.parse_args()

    r = subprocess.run([sys.executable, AUDIT, a.root], capture_output=True, text=True)
    cands = {}
    for name, path, line in ENTRY_RE.findall(r.stdout + r.stderr):
        cands.setdefault(name, []).append(f"{path}:{line}")
    print(f"{len(cands)} distinct self-assuming declaration name(s)")

    refs = collections.defaultdict(list)
    for p in pathlib.Path(a.root).rglob("*.ts"):
        for m in re.finditer(r'ref:\s*"([^"]+)"', p.read_text(errors="ignore")):
            refs[m.group(1)].append(p)

    rows = []
    for ref, tsfiles in refs.items():
        decl = ref.split(":", 1)[1] if ":" in ref else ref
        # strip the library root namespace (`QOU.`, `Fred2005.`, `UGB.`) and
        # any chapter namespace, then require the REMAINING suffix to match a
        # candidate's fully-qualified name exactly.
        for name, locs in cands.items():
            if decl == name or decl.endswith("." + name):
                for ts in tsfiles:
                    md = ts.with_suffix(".md")
                    src = ts.read_text(errors="ignore")
                    km = KIND_RE.search(src)
                    kind = km.group(1) if km else "?"
                    body = md.read_text(errors="ignore") if md.exists() else ""
                    rows.append(dict(name=name, ref=ref, ts=str(ts), kind=kind,
                                     lean=locs[0], banner=bool(BANNER.search(body)),
                                     words=len(body.split())))

    prov = [r for r in rows if r["kind"] in PROVABLE]
    print(f"{len(rows)} content block(s) whose lean.ref is such a declaration; "
          f"{len(prov)} of provable kind\n")
    for r in sorted(prov, key=lambda x: x["words"]):
        flag = "banner" if r["banner"] else "NO BANNER"
        print(f"  {r['kind']:<12} {r['name']}")
        print(f"      {r['ts']}")
        print(f"      lean {r['lean']}   md {r['words']}w   {flag}")
    n = sum(1 for r in prov if not r["banner"])
    print(f"\n{n} of {len(prov)} carry no §3b-cond item-3 conditional banner —")
    print("candidates for reading, not verdicts (see the module docstring).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

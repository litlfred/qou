#!/usr/bin/env python3
"""Measure the SIBLING-vs-LIBRARY mirror surface: names declared in both a
content-block `.lean` sibling and the Lake library tree.

WHY THIS EXISTS. A content-block sibling (`content/<paper>/<chapter>/<block>.lean`)
compiles standalone and cannot import the library, so a sibling that needs a library
type restates it. That is deliberate. What is not deliberate is the two copies
drifting -- because a co-located sibling wins **candidate 1** of `lean.ref`
resolution (AGENTS.md §0a), ahead of anything in the Lake tree. So every per-block
checker aimed at that block (`q-usage-*`, `wall-side-correct`,
`proof-statement-integrity`, the `da-*` family) audits the SIBLING'S copy and never
sees the declaration `lake build` actually compiles.

WHAT WAS HERE BEFORE. Nothing. `prepare-merge` §4a prescribed
`check-mirror-drift.ts`, which does not exist in this repo or in the
`folio-assistant` clone -- a gate naming a script that is not there, which reads as
covered. The one adjacent audit,
`scripts/lean-duplicate-fqn-audit.py`, says in its own SCOPE note that it walks the
library tree only and that "a clean run here is not evidence that a name is
unambiguous in the corpus". This script is that missing half.

🛑 THE TRAP, AND IT IS THE WHOLE REASON THIS SCRIPT REFUSES TO FIX ANYTHING.
The obvious disposition is "the library is canonical; delete the sibling copies."
Measured, that is wrong about half the time. Of the substantive drifts, 91 have the
library side edited more recently and 70 have the sibling side more recently -- and
recency is not canonicality. The worked case:

    library  QOU/MathConstants.lean
      noncomputable def speedOfLight (sp : ArchimedeanSubstrateField M) (p : M) : ℝ :=
        1 / (sp.field p - 1)

    sibling  information-theory/information-speed-of-light.lean
      def speedOfLight (d : kˣ) : k := (↑d⁻¹ : k)
      theorem speedOfLight_mul (d : kˣ) : speedOfLight d * (d : k) = 1 := Units.inv_mul d

The SIBLING is the §7c-compliant one -- generic base ring, division-free, defining
relation discharged as a theorem -- and the library is the older `ℝ` version, even
though the library file was touched later. Every reconciliation is a per-name
judgement that requires reading both sides. This script measures and gates; it never
edits.

THE THREE POPULATIONS, and only the third is actionable today:

  shared    a fully-qualified name declared in BOTH a sibling and the library.
  drifted   ... where the declaration signatures differ. Latent: if the block's
            `lean.ref` points elsewhere, nothing is currently misdirected.
  LIVE      ... where the block's own `.ts` `lean.ref` names THAT EXACT FQN. Here
            the checker demonstrably reads the sibling. This is the gate.

Usage:
    python3 scripts/mirror-drift-audit.py
    python3 scripts/mirror-drift-audit.py --json
    python3 scripts/mirror-drift-audit.py --baseline docs/audits/mirror-drift-baseline.json
    python3 scripts/mirror-drift-audit.py --self-test
"""

from __future__ import annotations

import argparse
import collections
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
PAPER = REPO / "content" / "quantum-observable-universe"
LEANROOT = PAPER / "lean"
BASELINE = REPO / "docs" / "audits" / "mirror-drift-baseline.json"


def _load_parser():
    """Reuse lean-duplicate-fqn-audit's parser.

    Deliberately imported rather than copied: that module's namespace-stack and
    comment-stripping behaviour was calibrated against four measured
    false-positive classes (an `import` indented inside a docstring; `namespace`
    text inside a `/- -/`; `section ... end` popping the stack; a dotted
    declaration name truncated at its first component). Re-implementing it here
    would re-open all four.
    """
    spec = importlib.util.spec_from_file_location(
        "lean_dup_fqn", HERE / "lean-duplicate-fqn-audit.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)   # safe: that module guards on __main__
    return mod


DFA = _load_parser()


def declarations(path: Path) -> dict[str, tuple[int, str]]:
    """FQN -> (1-based line, the raw declaration line)."""
    out: dict[str, tuple[int, str]] = {}
    stripped = DFA.strip_block_comments(path.read_text(errors="replace")).splitlines()
    raw = path.read_text(errors="replace").splitlines()
    stack: list[tuple[str, str]] = []
    for i, ln in enumerate(stripped):
        if DFA.IMP.match(ln):
            continue
        if (m := DFA.NS.match(ln)):
            stack.append(("ns", m.group(1)))
            continue
        if DFA.SEC.match(ln) and not DFA.DECL.match(ln):
            stack.append(("sec", ""))
            continue
        if DFA.END.match(ln) and stack:
            stack.pop()
            continue
        if (m := DFA.DECL.match(ln)):
            if DFA.PRIV.match(ln):
                continue
            ns = ".".join(x for kind, x in stack if kind == "ns")
            fq = f"{ns}.{m.group(1)}" if ns else m.group(1)
            out[fq] = (i + 1, raw[i].strip() if i < len(raw) else "")
    return out


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def block_ref(sibling: Path) -> str:
    """The `lean.ref` FQN declared by this block's `.ts`, without the `qou:` prefix."""
    ts = sibling.with_suffix(".ts")
    if not ts.exists():
        return ""
    m = re.search(r'ref:\s*"qou:([^"]+)"', ts.read_text(errors="replace"))
    return m.group(1) if m else ""


def audit() -> list[dict]:
    lib: dict[str, list[tuple[str, int, str]]] = collections.defaultdict(list)
    for p in sorted((LEANROOT / "QOU").rglob("*.lean")):
        if ".lake" in p.parts:
            continue
        for fq, (ln, sig) in declarations(p).items():
            lib[fq].append((str(p.relative_to(REPO)), ln, sig))

    rows: list[dict] = []
    for p in sorted(PAPER.rglob("*.lean")):
        if ".lake" in p.parts or "/lean/" in str(p):
            continue
        ref = block_ref(p)
        for fq, (ln, sig) in declarations(p).items():
            if fq not in lib:
                continue
            lp, ll, ls = lib[fq][0]
            rows.append(
                {
                    "fqn": fq,
                    "sibling": str(p.relative_to(REPO)),
                    "sibling_line": ln,
                    "sibling_sig": sig,
                    "library": lp,
                    "library_line": ll,
                    "library_sig": ls,
                    "faithful": norm(sig) == norm(ls),
                    "ref": ref,
                    "live": ref == fq,
                }
            )
    return rows


def self_test() -> int:
    ok = True

    if not hasattr(DFA, "strip_block_comments"):
        print("FAIL: parser import broke -- lean-duplicate-fqn-audit changed shape")
        ok = False

    import tempfile

    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "x.lean"
        # A declaration inside a /- -/ comment must NOT be seen, and the
        # namespace stack must qualify the real one. Both are the imported
        # parser's calibration; this asserts the import still delivers it.
        f.write_text(
            "namespace QOU.Demo\n"
            "/- def notARealDecl : Nat := 0 -/\n"
            "noncomputable def realDecl : Nat := 0\n"
            "end QOU.Demo\n"
        )
        got = set(declarations(f))
        if "QOU.Demo.realDecl" not in got:
            print("FAIL: namespace-qualified `noncomputable def` not found ->", got)
            ok = False
        if "QOU.Demo.notARealDecl" in got:
            print("FAIL: declaration inside /- -/ was counted")
            ok = False

    # `live` must key on the ref naming THIS fqn, not merely on a ref existing.
    r = {"ref": "QOU.A.b", "fqn": "QOU.A.b"}
    if not (r["ref"] == r["fqn"]):
        print("FAIL: live predicate")
        ok = False

    print("self-test: PASS" if ok else "self-test: FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--baseline", nargs="?", const=str(BASELINE))
    ap.add_argument("--only-live", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    rows = audit()
    live = [r for r in rows if r["live"]]
    drifted = [r for r in rows if not r["faithful"]]
    shared = {r["fqn"] for r in rows}

    if args.json:
        print(json.dumps(rows if not args.only_live else live, indent=1))
        return 0

    for r in (live if args.only_live else rows):
        if r["faithful"] and not args.only_live:
            continue
        tag = "LIVE " if r["live"] else "     "
        print(f"{tag}{'DRIFT' if not r['faithful'] else 'faithful'}  {r['fqn']}")
        print(f"        sib {r['sibling']}:{r['sibling_line']}")
        print(f"        lib {r['library']}:{r['library_line']}")

    print()
    print(f"shared FQNs (sibling AND library): {len(shared)}")
    print(f"  sibling declarations involved:   {len(rows)}")
    print(f"  faithful:                        {len(rows) - len(drifted)}")
    print(f"  drifted:                         {len(drifted)}")
    print(f"  LIVE (block lean.ref names it):  {len(live)}")

    if args.baseline:
        bp = Path(args.baseline)
        if not bp.exists():
            print(f"\nno baseline at {bp} -- nothing to ratchet against")
            return 0
        base = json.loads(bp.read_text())
        allowed = set(base.get("live", []))
        now = {r["fqn"] for r in live}
        new = sorted(now - allowed)
        drained = sorted(allowed - now)
        print(f"\nbaseline {bp.name}: allows {len(allowed)} live shadow(s)")
        for d in drained:
            print(f"  drained (remove from baseline): {d}")
        if new:
            print(f"  🛑 NEW live shadow(s), not in baseline: {len(new)}")
            for n in new:
                print(f"     {n}")
            print("  The ratchet drains and never grows (AGENTS.md).")
            return 1
        print("  no new live shadows")
    return 0


if __name__ == "__main__":
    sys.exit(main())

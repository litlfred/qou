#!/usr/bin/env python3
"""Flag a Lean `def` that DISCARDS an argument, has a CONSTANT body, and is
CONSTRAINED BY AN AXIOM.

Why this exact conjunction, and not any one of the three alone:

* A constant body is usually CORRECT.  `dim_q([3]) = [3]_q!/([3]_q[2]_q[1]_q)`
  really is 1 for every q, and convention D's `ySign` really is 0 (a Schur
  polynomial in two variables vanishes on a three-row partition).  Both are
  `_q`-discarding constants with docstrings deriving exactly that.  24 such
  defs are live and the two spot-checked are sound, so "constant body" on its
  own is not a defect signal.
* An axiom over a placeholder is usually fine too — that is the ordinary
  Mathlib-gap pattern.

It is the CONJUNCTION that bites.  A `def` that discards its index is
*definitionally constant* in it, so two different indices give the SAME TERM.
An axiom that then distinguishes those indices collapses the object.  Realised:
`QOU.BraidKnot.IwahoriHeckeAPI.centralIdempotent` was

    noncomputable def centralIdempotent (H : _) (_lam : List ℕ) : H.carrier :=
      Classical.ofNonempty

so `centralIdempotent H [1]` and `centralIdempotent H [2]` were one term, and
`centralIdempotent_orthogonal_axiom` gave `e*e = e` (λ=μ) and `e*e = 0` (λ≠μ),
forcing **every central idempotent to zero** — machine-checked before the fix.
The two sibling axioms then held trivially (`0` commutes, `star 0 = 0`), so the
API asserted nothing.  Fix: make the placeholder `opaque`, not `def`.

NOT detectable by scanning the axiom's text: that axiom mentions `lam` on both
sides.  The vacuity is in the definition.

Usage:
    python3 scripts/lean-constant-def-under-axiom-audit.py [ROOT]
    python3 scripts/lean-constant-def-under-axiom-audit.py --selftest

Exit 1 if any site is flagged, or if the self-test fails.
"""
import re, sys, pathlib, tempfile, textwrap

BLOCK = re.compile(r"/-.*?-/", re.S)
ID    = r"[^\W\d][\w'₀-₉ₐ-ₜ!?]*"
DEF   = re.compile(r"^\s*(?:noncomputable\s+|private\s+|protected\s+)*(?:def|abbrev)\s+(" + ID + r")", re.U)
AX    = re.compile(r"^\s*(?:noncomputable\s+)?axiom\s+(" + ID + r")", re.U)
NEXT  = re.compile(r"^\s*(?:@\[|/--|noncomputable |private |protected |theorem |lemma |def |opaque "
                   r"|abbrev |axiom |structure |class |inductive |instance |end |namespace |section |/-!)")
UNDER = re.compile(r"\(\s*((?:_" + ID + r"\s*)+):", re.U)


def _strip(src: str) -> str:
    """Remove block comments, docstrings and line comments, preserving line count."""
    src = BLOCK.sub(lambda m: "\n" * m.group(0).count("\n"), src)
    return "\n".join(re.sub(r"--.*$", "", ln) for ln in src.split("\n"))


def _decl(lines, i):
    body = [lines[i]]
    for k in range(i + 1, len(lines)):
        if lines[k].strip() and NEXT.match(lines[k]):
            break
        body.append(lines[k])
    return "\n".join(body)


def scan(root: pathlib.Path):
    const_defs, axioms = {}, []
    for p in sorted(root.rglob("*.lean")):
        lines = _strip(p.read_text(encoding="utf-8", errors="replace")).split("\n")
        for i, ln in enumerate(lines):
            m = DEF.match(ln)
            if m:
                stmt = _decl(lines, i)
                if ":=" in stmt:
                    sig, rhs = stmt.split(":=", 1)
                    rhs = rhs.strip()
                    # constant body: a bare identifier / literal, e.g. `1`, `0`,
                    # `True`, `Classical.ofNonempty`
                    if UNDER.findall(sig) and re.fullmatch(r"[\w'.]+", rhs):
                        const_defs[m.group(1)] = (p, rhs)
            a = AX.match(ln)
            if a:
                axioms.append((a.group(1), _decl(lines, i)))
    hits = []
    for nm, (p, rhs) in sorted(const_defs.items()):
        used = [an for an, st in axioms
                if re.search(r"(?<![\w'])" + re.escape(nm) + r"(?![\w'])", st)]
        if used:
            hits.append((nm, p, rhs, used))
    return const_defs, axioms, hits


def _selftest() -> bool:
    src = textwrap.dedent("""
        structure Alg where carrier : Type
        noncomputable def widget (A : Alg) (_lam : List Nat) : A.carrier :=
          Classical.ofNonempty
        axiom widget_orthogonal :
            forall (A : Alg) (lam mu : List Nat),
              widget A lam = widget A mu
    """)
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        (root / "T.lean").write_text(src, encoding="utf-8")
        _, _, hits = scan(root)
    ok = len(hits) == 1 and hits[0][0] == "widget"
    print(f"selftest: {'PASS' if ok else 'FAIL'} (flagged {[h[0] for h in hits]})")
    return ok


def main() -> int:
    if "--selftest" in sys.argv:
        return 0 if _selftest() else 1
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    root = pathlib.Path(args[0]) if args else pathlib.Path(
        "folio/quantum-observable-universe/lean/QOU")
    if not _selftest():
        print("ABORT: self-test failed — a clean result would be meaningless.")
        return 1
    const_defs, axioms, hits = scan(root)
    print(f"\nroot: {root}")
    print(f"constant-bodied argument-discarding defs: {len(const_defs)}")
    print(f"axioms: {len(axioms)}")
    for nm, p, rhs, used in hits:
        print(f"\n*** {nm} := {rhs}\n    {p}\n    constrained by: {used}")
    print(f"\nflagged: {len(hits)}")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())

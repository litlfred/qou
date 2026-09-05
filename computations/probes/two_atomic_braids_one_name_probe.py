#!/usr/bin/env python3
"""`def:atomic-braid` is not the object the mass law traces. Two objects, one name.

Bean `qou-atbr`. Follow-on from `qou-oots` / PR #6806, which reported the strand
count as "unreconciled" between `H_{A+Z}` and `H_{3A}` and did not measure it.
Measured, it is not a disagreement about a number -- they are different
constructions:

  def:atomic-braid                     production `atom_braid_word_3A`
  ------------------------------       --------------------------------
  H_{A+Z}(q)                           H_{3A}(q)
  A nucleons + Z ELECTRONS             3 quarks per nucleon, NO electrons
  one strand per nucleon               three strands per nucleon
  6 pair types, 3 of them electronic   intra-nucleon confinement core
    (pe, ne, ee)                         (beta_Bor) + inter-nucleon bonds

`H_{A+Z}(q)` is not merely a different convention: it is TOO SMALL TO HOLD the
word production builds, at every A (check 1). The proton's word needs 3 strands
and A+Z gives 2; iron-56 needs 168 and A+Z gives 82.

WHY IT MATTERS: 12 content blocks cite `def:atomic-braid`, and six of them are
in `mass-theory/` and `mass-endomorphism/` -- the chapters whose compute is
3A. `wedderburn-mass-formula.md` states `A ∈ H_{A+Z}(q)` and links
`#def:atomic-braid` while sitting in the chapter that traces the 3A object.
Both objects are written `A` (script A) and both are called "the atomic braid".

WHAT THIS PROBE DOES NOT DECIDE
    Which definition is canonical. That is an author decision and it is NOT
    a choice between a right and a wrong number:

      * `def:atomic-braid` may be a genuine, separate, currently-uncomputed
        object -- an atom INCLUDING its electron shell -- in which case the
        defect is that two objects share one name and one symbol, and the fix
        is naming, not deletion. Its electron rows (pe = EM attraction,
        ne = no interaction, ee = EM repulsion) are content that the 3A
        object has nowhere to put.
      * Or it may be superseded by the 3A construction, in which case it
        needs retiring and its 12 citations rehoming.

    This probe measures that they differ and how; it takes no position on
    which survives. Nothing here is a claim that the mass law is wrong --
    production is self-consistent at 3A throughout (824 strand-count lines
    across 377 files, against 9 lines across 4 files for A+Z, of which one
    file carries deprecation markers and one is a test).

Precision: this probe measures STRUCTURE (strand counts, generator indices,
substring presence), not physical quantities, so it carries no q-dependence
and emits no witness. mpmath is used only to supply the q the producer
requires. No builtin-float coercion, no numpy, no statistics.

Run:
    PYTHONPATH=computations:tools/qou-substrate/python:tools/pyhecke/python \
      python3 -u computations/probes/two_atomic_braids_one_name_probe.py
"""

from __future__ import annotations

import inspect
import pathlib
import sys

import mpmath as mp

mp.mp.dps = 40

from qou_substrate.constants import q_at  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parents[2]
Q = q_at(35)

ATOMS = [(1, 0, "proton  H-1"), (2, 2, "helium-4"), (26, 30, "iron-56")]


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    # ---- 1. H_{A+Z} cannot hold the production word ----------------------
    print("[1] strands the production word NEEDS vs what def:atomic-braid supplies")
    print(f"    {'atom':12s} {'A':>3} {'A+Z (def)':>10} {'3A':>5} {'word needs':>11}  fits A+Z?")
    all_overflow = True
    for Z, N, label in ATOMS:
        A = Z + N
        w = atom_braid_word_3A(Z, N, q=Q, include_inter=True)
        need = max(g for _, _, g in w) + 2
        fits = need <= A + Z
        all_overflow &= not fits
        print(f"    {label:12s} {A:>3} {A + Z:>10} {3 * A:>5} {need:>11}  {'yes' if fits else 'NO'}")
        assert need == 3 * A, f"word needs {need}, expected 3A={3 * A}"
    checks.append(("H_{A+Z} is too small for the word at every A", all_overflow,
                   "proton needs 3, A+Z gives 2"))
    checks.append(("the word needs exactly 3A strands", True,
                   "asserted per atom above"))

    # ---- 2. production has no electrons at all ---------------------------
    src = inspect.getsource(atom_braid_word_3A)
    has_e = "electron" in src.lower()
    print(f"[2] production word source mentions 'electron': {has_e}")
    checks.append(("production carries no electron strand", not has_e,
                   "def:atomic-braid assembles Z of them"))

    # ---- 3. the definition's own table is 3/6 electronic ------------------
    tbl = (REPO / "content/quantum-observable-universe/knots-particles-confinement"
           / "atomic-braid-table1-data.md").read_text()
    e_rows = [r for r in ("mathfrak{p}e", "mathfrak{n}e", "$ee$") if r in tbl]
    print(f"[3] def:atomic-braid Table 1 electronic pair rows present: {e_rows}")
    checks.append(("the definition specifies electron interactions", len(e_rows) == 3,
                   "pe / ne / ee -- content 3A has nowhere to put"))

    # ---- 4. blast radius: who cites the definition ------------------------
    cites = sorted(
        str(p.relative_to(REPO))
        for p in (REPO / "content/quantum-observable-universe").rglob("*")
        if p.suffix in (".md", ".ts") and "def:atomic-braid" in p.read_text(errors="ignore")
    )
    mass = [c for c in cites if "/mass-theory/" in c or "/mass-endomorphism/" in c]
    print(f"[4] blocks citing def:atomic-braid: {len(cites)}; of those in mass chapters: {len(mass)}")
    for c in mass:
        print(f"      {c}")
    checks.append(("the definition is cited from the mass chapters", len(mass) > 0,
                   f"{len(mass)} of {len(cites)}"))

    print()
    n_ok = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}  ({detail})")
    print(f"\n{n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())

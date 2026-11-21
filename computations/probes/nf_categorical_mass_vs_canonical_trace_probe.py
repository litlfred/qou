#!/usr/bin/env python3
"""Does the NF `categorical_mass` agree with the canonical p(3A) trace?

Settles item 3.2 of bean `qou-zgg2`, which `qou-hu1f` names as unmeasured.

THE TWO OBJECTS, and they are NOT the same construction:

* `compound_shift_nf.compound_shift(Z, N).categorical_mass` is
  `Σ_{i<6} nf_mp[i] · tr_w[i]` — the SIX-vector `H_3` normal form contracted
  against the `H_3` Markov weights.  A collapsed object, no tower.
* `tr_m_atom_via_transfer.tr_m_atom_zn(Z, N)` is the canonical route's default
  path: the fine-Bratteli transfer matrix summing the Frobenius pairing over
  EVERY partition of `3A` — full-tower in `n` (measured on `main`
  `30b3568404`: `2H` 11 = p(6), `3He` 30 = p(9), `4He` 77 = p(12)).

WHY IT MATTERS.  `categorical_mass` is serialised into
`compound-shift-nf.witness.json` uncaveated, under a name that says "mass".
No consumer reads it today.  If the two agree, the field is a faithful
order-zero rendering and only its NAME is loose; if they disagree, that witness
carries a "mass" that is not the framework's, and every downstream reading of
it is about the wrong object.

WHAT THIS PROBE DOES *NOT* SETTLE.  Agreement would NOT show the NF route is
full-tower — it would show the collapse is faithful AT THESE `A`.  Disagreement
would NOT by itself condemn the NF route; the NF is a legitimate object for the
questions it was built for (see `qou-zgg2` category 2).  The claim under test is
narrow and is only about this one serialised field.

NO FLOAT64.  `mpmath.mpf` end to end; `float()` appears nowhere.  Comparison is
by exact `mpf` subtraction and an `mpf` relative ratio, never by `==` on
floats and never by a float64 tolerance.

-- Ref: [manuscript] bean `qou-zgg2` item 3.2; bean `qou-hu1f`; main 30b3568404.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mpmath import mp, mpf, nstr  # noqa: E402

DPS = 50
mp.dps = DPS

from compound_shift_nf import ATOMS_TO_VERIFY, compound_shift  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402


def main() -> int:
    print(f"NF categorical_mass  vs  canonical p(3A) trace   (dps={DPS})")
    print()
    print("| atom | A | n=3A | categorical_mass (NF, 6-vec) | tr_M_atom (canonical) | |Δ| | rel |")
    print("|---|--:|--:|---|---|---|---|")

    rows = []
    for Z, N, atom in ATOMS_TO_VERIFY:
        A = Z + N
        t0 = time.monotonic()
        cs = compound_shift(Z, N, atom, dps=DPS)
        cat = mpf(getattr(cs, "nf_trace_pairing", getattr(cs, "categorical_mass", None)))
        tr_atom, _tr_free, _chi, _wall = tr_m_atom_zn(Z, N, dps=DPS)
        tr_atom = mpf(tr_atom)
        delta = cat - tr_atom
        rel = abs(delta) / abs(tr_atom) if tr_atom != 0 else mpf("nan")
        rows.append((atom, A, cat, tr_atom, delta, rel, time.monotonic() - t0))
        print(f"| {atom} | {A} | {3*A} | {nstr(cat, 20)} | {nstr(tr_atom, 20)} "
              f"| {nstr(abs(delta), 6)} | {nstr(rel, 6)} |")

    print()
    # A relative agreement at or below the 50-dps serialisation floor is the
    # only thing that would license calling the collapse faithful.  Anything
    # larger is a real disagreement, and is reported as one.
    floor = mpf(10) ** (-(DPS - 5))
    worst = max((r[5] for r in rows), default=mpf(0))
    agree = worst <= floor
    print(f"worst relative difference : {nstr(worst, 6)}")
    print(f"50-dps serialisation floor: {nstr(floor, 6)}")
    print()
    if agree:
        print("VERDICT: AGREE at the compute floor.  The NF `categorical_mass` is a")
        print("faithful order-zero rendering of the canonical trace at these A;")
        print("only the FIELD NAME is loose.")
    else:
        print("VERDICT: DISAGREE.  `compound-shift-nf.witness.json` carries a field")
        print("named `categorical_mass` that is NOT the framework's canonical trace.")
        print("Any downstream reading of it is about the wrong object.")
    print()
    print("Scope: this is a statement about ONE serialised field at A = 2..6.")
    print("It does not make the NF route full-tower, and it does not condemn the")
    print("NF route for the questions it was actually built for.")
    for atom, A, _c, _t, _d, _r, wall in rows:
        print(f"  wall {atom:>4}: {wall:.1f}s")
    return 0 if agree else 2


if __name__ == "__main__":
    raise SystemExit(main())

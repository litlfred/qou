#!/usr/bin/env python3
# polynomial_q_not_applicable: braid words, Reidemeister/Vogel isotopy, exact
# integer Kauffman brackets. No q, no float, nothing evaluated at q0.
"""The curvature floor `2π(2A+1)` is SHARP: every canonical closure is a closed
braid on exactly `2A+1` strands, so its bridge number is `2A+1` and Milnor's
infimum of total curvature is `2π(2A+1)` exactly.

WHAT WAS OPEN
-------------
`total_curvature_is_the_computable_half_probe` (bean `qou-m3sh`) proved the
floor: every multi-strand component of the canonical closure is a `(2,odd)`-
torus knot, so `b(L) ≥ μ + #knotted = (A+1) + A = 2A+1`, and Milnor gives
`inf ∫κ ds = 2π·b(L) ≥ 2π(2A+1)`. The braid presentation on `3A` strands gave
only `b(L) ≤ 3A`. The owner asked whether the floor is sharp. It needed a
`(2A+1)`-bridge presentation, and the round-chain picture that would have
supplied one was refuted there.

WHAT CLOSES IT, COMPUTATIONALLY
-------------------------------
A closed braid on `n` strands is an `n`-bridge presentation. So it is enough
to find a braid on `2A+1` strands whose closure is the link. Spherogram's
global Reidemeister simplification followed by Vogel's algorithm does exactly
that, for every nucleus and both classical branches of the averaged letters:

    A   floor 2A+1   braid found   (strands, from 3A)
    2       5             5             (from 6)
    3       7             7             (from 9)
    4       9             9             (from 12)
    6      13            13             (from 18)

Hence `b(L) ≤ 2A+1 ≤ b(L)`, i.e.

    b(L) = 2A + 1      and      inf ∫κ ds = 2π (2A + 1)      EXACTLY.

The extensive slope `4π` per nucleon is a value, not a bound. The SYMBOLIC
proof of the same statement, valid for every `A`, is
`the_canonical_closure_is_a_chain_of_torus_links_probe.py`: the canonical word
is a chain form, and its `A-1` interface generators are connected-sum bands.

HOW IT IS CHECKED, INDEPENDENTLY OF SPHEROGRAM
----------------------------------------------
Isotopy software can be wrong. Two invariants of the returned braid's closure
are recomputed by this probe's own exact-integer machinery and compared with
the original closure's:

  * the Jones polynomial (Kauffman bracket on the TL algebra, self-tested in
    the parent probe), and
  * the component count and the multiset of per-component Jones polynomials.

Both must agree. They do, on every line of the table. A Jones match is not a
proof of isotopy, but a mismatch would have refuted the presentation, and
Vogel's algorithm is a theorem: the closure of the braid it returns IS the
input diagram's link. The check is against implementation error only.

WHAT THIS DOES NOT SAY
----------------------
Nothing about binding, nothing about the twist. It sharpens the geometric
statement the curvature half makes to an equality; it does not make that half
the one that is missing.
"""
from __future__ import annotations

import random
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))
import _path_bridge  # noqa: F401,E402

import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "tc", HERE / "total_curvature_is_the_computable_half_probe.py")
tc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tc)

try:
    import spherogram  # noqa: E402
except ImportError:  # pragma: no cover
    spherogram = None

TRIALS = 6


def components_of_word(k, sw):
    """Component count and per-component Jones multiset of a braid closure."""
    comp, cyc = tc.components(k, sw)
    per = []
    for cycle in cyc:
        kk, sub = tc.sub_braid(k, sw, cycle)
        V = tc.jones_closure(kk, sub)
        per.append(tc.pstr(V, "A"))
    return len(cyc), Counter(per)


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    if spherogram is None:
        print("\n  spherogram not available: install snappy to run this probe")
        return 2
    random.seed(20260903)
    rows = []
    for Z, N, name in tc.ISOTOPES:
        A = Z + N
        n = 3 * A
        for avg, bname in ((1, "sigma"), (-1, "sigma^-1")):
            word = tc.resolve(Z, N, avg)
            sg = [(g + 1) * s for g, s in word]
            best = None
            for _ in range(TRIALS):
                L = spherogram.Link(braid_closure=sg)
                L.simplify("global")
                bw = L.braid_word()
                strands = (max(abs(x) for x in bw) + 1) if bw else 1
                if best is None or strands < best[0]:
                    best = (strands, bw)
            strands, bw = best
            sub = [(abs(x) - 1, 1 if x > 0 else -1) for x in bw]
            V0 = tc.jones_closure(n, word)
            V1 = tc.jones_closure(strands, sub)
            mu0, per0 = components_of_word(n, word)
            mu1, per1 = components_of_word(strands, sub)
            same = (V0 == V1) and (mu0 == mu1) and (per0 == per1)
            rows.append((name, bname, A, n, strands, len(bw), same))
            print(f"  {name:4s} {bname:8s} A={A} n={n:2d}  floor {2*A+1:2d}  "
                  f"braid on {strands:2d} strands ({len(bw)} letters)  "
                  f"Jones+components match: {same}")
            check(f"{name} {bname}: braid on 2A+1 = {2*A+1} strands found",
                  strands == 2 * A + 1)
            check(f"{name} {bname}: returned braid's closure has the same Jones, μ and "
                  f"per-component Jones as the original", same)

    print("\n" + "=" * 68)
    print("§Σ  b(L) = 2A+1 and inf ∫κ = 2π(2A+1), exactly")
    print("=" * 68)
    print("  A   μ    floor   braid strands   bridge number   inf ∫κ / 2π")
    seen = set()
    for name, bname, A, n, strands, _, same in rows:
        if A in seen:
            continue
        seen.add(A)
        print(f"  {A}   {A+1}    {2*A+1:3d}        {strands:3d}             {2*A+1:3d}            {2*A+1}")
    check("every nucleus, both branches: bridge number = 2A+1 (floor met from above)",
          all(r[4] == 2 * r[2] + 1 and r[6] for r in rows))

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "The curvature floor 2*pi*(2A+1) is sharp. Spherogram (global "
            "Reidemeister simplification + Vogel) returns a closed braid on "
            "exactly 2A+1 strands for every canonical closure, A = 2, 3, 4, 6, "
            "both classical branches; a closed n-braid is an n-bridge "
            "presentation, so b(L) <= 2A+1, and the parent probe's floor gives "
            "b(L) >= 2A+1. Hence b(L) = 2A+1 and, by Milnor, inf total curvature "
            "= 2*pi*(2A+1) exactly. Each returned braid's closure is checked "
            "against the original by this probe's own exact Kauffman bracket "
            "(Jones polynomial, component count, per-component Jones). The "
            "all-A symbolic proof is the chain-form probe.")
        for name, bname, A, n, strands, ln, same in rows:
            wb.add_data(f"{name}_{bname.replace('^', '')}_braid_strands", str(strands))
            wb.add_data(f"{name}_{bname.replace('^', '')}_braid_length", str(ln))
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "Depends on spherogram (snappy) for the isotopy search. Vogel's "
            "algorithm is a theorem, so the returned braid's closure is the "
            "input link; the Jones/component cross-check guards against "
            "implementation error, not against the mathematics.")
        wb.add_caveat(
            "Per classical branch of the 2A+1 averaged letters, as everything "
            "geometric about this closure must be. Nothing about binding or "
            "the twist.")
        print(f"\nWitness: {wb.save(extra={"q0Anchor": "independent", "q0AnchorReason": (
            "braid words, Reidemeister/Vogel isotopy and exact integer Kauffman brackets; no q is evaluated, q0 is never read")})}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())

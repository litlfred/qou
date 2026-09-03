#!/usr/bin/env python3
"""integer_lp_gluon_convention_d.py — the gluon-placement integer LP, re-run
under convention D with the corrected trace rule.

WHY THIS EXISTS (bean `qou-1qsw`).

The 2 x sigma_0 "gluon self-coupling" that takes each nucleon from 9 to 11
crossings is DERIVED, not decorative. Its derivation is
`computations/_deprecated/integer-lp-gluon.py`:

    For each nucleon (proton uud, neutron udd), the 9-crossing element
    B_3 x Delta_3(quarks) is LP UNSTABLE (Frobenius positivity Gx[gamma] < 0).
    The integer LP enumerates all feasible gluon combinations from
    {sigma_0, sigma_1, L+, L-} and selects the one with minimum |tr_M|
    that is stable at every intermediate step.

      Proton:  sigma_0 -> sigma_0  (2 crossings, 11 total)
      Neutron: L+ -> L-            (4 crossings, 13 total)

and `validate_isotope_nf_stability` confirmed the mechanism across 82 nuclides:
*"2/11 intermediate steps are unstable per nucleon — the terminal gluon pair
restores stability"*.

**That derivation is stale in two independent ways.** Its line 29 reads
`z = 1.0 / (q0**0.5 + qi0**0.5)` — convention C, excised 2026-08-15 — and its
Gram is built on `tr_M(e-) = z^3`, which is exactly the rule `pyhecke.gram`
marks `# fix 2026-05-19 (was _Z_FRAC ** 3)`. It also computes in float64 and
sits in `_deprecated/`. So the argument that selects the gluon term rests on a
convention and a trace rule the corpus has both retired.

WHAT IS CHANGED HERE, AND WHAT IS NOT.

Held fixed, so the comparison is like-for-like:
  * the two base words, letter for letter, INCLUDING the original's
    pair->generator assignment (see the note on `_base` below);
  * the operation set {sigma_0, sigma_1, L+ = sigma_0.sigma_1,
    L- = sigma_1.sigma_0} — note both L's are POSITIVE crossings, not
    inverses;
  * the feasibility criterion: every component of `G.nf >= 0`, checked after
    EVERY operation, not only at the end;
  * the objective: minimum |tr_M|;
  * `max_depth = 3`.

Changed:
  * convention D throughout — `z_D = q^3/(q^2+1)`, and the Gram + trace vector
    taken from `pyhecke.gram.gram_matrix_mp` / `tr_m_mp` rather than
    hardcoded, so the corrected `tr_M(e-)` rule is used;
  * mpmath at 50 dps end to end, no float64 (AGENTS.md
    §"PROBES ARE NOT EXEMPT"); the original's `abs(nf[src]) < 1e-15` cutoff is
    gone, `hm_mp` tests exact zero.

A NOTE ON THE BASE WORD, because it is not the one the live builders use.
The original LP's proton base is `uu@gen0, ud@gen1, ud@gen0`; `build_nucleon_nf`
assigns pairs (0,1)->gen0, (0,2)->gen0, (1,2)->gen1, i.e. `uu@0, ud@0, ud@1`.
Same multiset, different order, and H_3(q) is not commutative. This script
reproduces the LP's own base so that a difference in the RESULT is
attributable to the convention change and not to a substituted input; the
discrepancy itself is recorded as a finding rather than silently harmonised.

Anchor: experimental (proton) pin, per the 2026-08-07 owner directive.
Scope-(a): this reports what the LP returns under D. It does not by itself
establish which crossing budget is canonical.
"""
from __future__ import annotations

import sys
from itertools import product as cartprod
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401, E402

from witness_base import WitnessBuilder  # noqa: E402
from pyhecke.gram import h_mp, hm_mp, gram_matrix_mp, tr_m_mp, z_mp  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

DPS = 50
_H = h_mp(DPS)
_G = gram_matrix_mp(DPS)
_TR = tr_m_mp(DPS)
ONE, ZERO = mp.mpf(1), mp.mpf(0)
#: Feasibility tolerance. The original used -1e-10 against float64 noise; at
#: 50 dps a true zero is exact, so this only absorbs representation dust.
TOL = mp.mpf("1e-40")


def _mul(nf, c, d, gen):
    return hm_mp(nf, c, d, gen, DPS)


def _trM(nf):
    return sum(nf[i] * _TR[i] for i in range(6))


def _Gx(nf):
    return [sum(_G[i][j] * nf[j] for j in range(6)) for i in range(6)]


def _is_stable(nf):
    return all(v >= -TOL for v in _Gx(nf))


def _margin(nf):
    """Smallest component of G.nf — how close feasibility comes to failing."""
    return min(_Gx(nf))


def _b3():
    nf = [ONE] + [ZERO] * 5
    for _ in range(3):
        nf = _mul(nf, ONE, ZERO, 0)      # sigma_0
        nf = _mul(nf, ONE, -_H, 1)       # sigma_1^-1
    return nf


def _base(kind):
    """The LP's own 9-crossing bases, letter for letter."""
    nf = _b3()
    if kind == "proton":                 # B_3 x uu(s0) x ud(s1 mixed) x ud(s0 mixed)
        nf = _mul(nf, ONE, ZERO, 0)
        nf = _mul(nf, ONE, -_H / 2, 1)
        nf = _mul(nf, ONE, -_H / 2, 0)
    else:                                # B_3 x ud(s0 mixed) x dd(s1^-1) x ud(s0 mixed)
        nf = _mul(nf, ONE, -_H / 2, 0)
        nf = _mul(nf, ONE, -_H, 1)
        nf = _mul(nf, ONE, -_H / 2, 0)
    return nf


OPS = [
    ("s0", 1, lambda nf: _mul(nf, ONE, ZERO, 0)),
    ("s1", 1, lambda nf: _mul(nf, ONE, ZERO, 1)),
    ("L+", 2, lambda nf: _mul(_mul(nf, ONE, ZERO, 0), ONE, ZERO, 1)),
    ("L-", 2, lambda nf: _mul(_mul(nf, ONE, ZERO, 1), ONE, ZERO, 0)),
]


def solve(base, max_depth: int = 3):
    out = []
    if _is_stable(base):
        out.append((0, [], base[:], _trM(base)))
    for depth in range(1, max_depth + 1):
        for combo in cartprod(range(len(OPS)), repeat=depth):
            nf, names, ncross, ok = base[:], [], 0, True
            for oi in combo:
                nm, cost, fn = OPS[oi]
                nf = fn(nf)
                names.append(nm)
                ncross += cost
                if not _is_stable(nf):
                    ok = False
                    break
            if ok:
                out.append((ncross, names, nf[:], _trM(nf)))
    seen, uniq = set(), []
    for r in out:
        key = tuple(mp.nstr(v, 25) for v in r[2])
        if key not in seen:
            seen.add(key)
            uniq.append(r)
    uniq.sort(key=lambda r: abs(r[3]))
    return uniq


def main() -> int:
    print("=" * 78)
    print(" INTEGER LP FOR GLUON PLACEMENT — convention D, corrected trace rule")
    print("=" * 78)
    print(f"\n  z_D = {mp.nstr(z_mp(DPS), 20)}   h = {mp.nstr(_H, 20)}")
    print(f"  tolerance {mp.nstr(TOL, 3)}, mpmath {DPS} dps, no float64\n")

    data = {}
    for kind, recorded in (("proton", "s0 -> s0 (2 crossings, 11 total)"),
                           ("neutron", "L+ -> L- (4 crossings, 13 total)")):
        b = _base(kind)
        stable = _is_stable(b)
        marg = _margin(b)
        print(f"  ---- {kind.upper()} ----")
        print(f"    9-crossing base: tr_M = {mp.nstr(_trM(b), 16)}")
        print(f"      LP stable under D? {stable}   min(G.nf) = {mp.nstr(marg, 12)}")
        print(f"      convention-C result on record: {recorded}")
        res = solve(b)
        print(f"    {len(res)} feasible solutions; top 5 by |tr_M|:")
        print(f"      {'cross':>5} {'ops':>16} {'|tr_M|':>18}")
        for nc, ns, nf, tm in res[:5]:
            print(f"      {nc:>5} {('->'.join(ns) if ns else '(none)'):>16} "
                  f"{mp.nstr(abs(tm), 14):>18}")
        best = res[0]
        print(f"    OPTIMAL under D: {'->'.join(best[1]) if best[1] else '(none)'}"
              f"   total crossings = {9 + best[0]}\n")
        data[kind] = {
            "base_9_crossing_stable_under_D": bool(stable),
            "base_min_G_dot_nf": fmt(marg),
            "base_tr_M": fmt(_trM(b)),
            "n_feasible": len(res),
            "optimal_ops": best[1],
            "optimal_added_crossings": best[0],
            "optimal_total_crossings": 9 + best[0],
            "optimal_abs_tr_M": fmt(abs(best[3])),
            "convention_C_result_on_record": recorded,
        }

    p, n = data["proton"], data["neutron"]
    print("=" * 78)
    print(" Reading")
    print("=" * 78)
    print(f"""
  The convention-C LP selected a gluon term BECAUSE the 9-crossing base was
  infeasible. Under D that premise is what has to be re-checked first, and it
  is reported above as `base_9_crossing_stable_under_D`.

  proton  base stable under D : {p['base_9_crossing_stable_under_D']}
  neutron base stable under D : {n['base_9_crossing_stable_under_D']}

  If both are stable, the empty gluon set is feasible and — the objective being
  minimum |tr_M| — the LP selects whichever feasible combination minimises it,
  with no stability pressure to add crossings at all. That does not make the
  gluon term wrong; it means LP stability under D no longer SELECTS it, and the
  9-vs-11 question needs a criterion this LP cannot supply.
""")

    wb = WitnessBuilder("integer-lp-gluon-convention-d", engine="mpmath")
    wb.set_description(
        "Re-runs the gluon-placement integer LP of the deprecated "
        "integer-lp-gluon.py under convention D with the corrected trace rule "
        "(tr_M(e-), fixed 2026-05-19) and mpmath at 50 dps, holding the base "
        "words, the operation set {s0, s1, L+, L-}, the every-step Frobenius "
        "feasibility criterion and the minimum-|tr_M| objective fixed. The "
        "original selected 2 sigma_0 for the proton and L+L- for the neutron "
        "BECAUSE the 9-crossing base was LP-infeasible; it was built on "
        "convention C (z = 1/(sqrt q + 1/sqrt q)) and on the superseded "
        "tr_M(e-) = z^3, both since retired. Reports whether that premise "
        "survives under D. Scope-(a): reports what the LP returns; does not by "
        "itself establish which crossing budget is canonical. Bean qou-1qsw."
    )
    wb.add_data("q0_anchor", "proton")
    wb.add_data("dps", DPS)
    wb.add_data("z_D", fmt(z_mp(DPS)))
    wb.add_data("h", fmt(_H))
    wb.add_data("results", data)
    wb.add_assertion(
        name="convention_C_premise_re_evaluated_under_D",
        computed=str(int(
            p["base_9_crossing_stable_under_D"] == n["base_9_crossing_stable_under_D"])),
        expected="1", tolerance=0,
        source=(
            "Both nucleons' 9-crossing bases return the same feasibility verdict "
            f"under D (proton {p['base_9_crossing_stable_under_D']}, neutron "
            f"{n['base_9_crossing_stable_under_D']}), so the convention-C claim "
            "that the base is LP-infeasible is answered uniformly rather than "
            "for one nucleon only."
        ),
    )
    # Stamp the anchor on the witness itself, not only in `data` — the
    # q0-anchor ratchet reads the top-level field, and an unstamped new
    # witness is a refill of exactly the backlog that ratchet exists to drain.
    wb.save({"q0Anchor": "proton", "q0Value": str(Q_50_DIGIT_STR)})
    print(f"\nWitness: {Path(__file__).with_name('integer-lp-gluon-convention-d.witness.json')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

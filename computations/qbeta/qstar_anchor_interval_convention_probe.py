#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical sensitivity probe; emits no witness.
"""qstar_anchor_interval_convention_probe — is the q* landmark's position
between the anchors a fact, or a convention?

`content/quantum-observable-universe/mass-theory/rem-qstar-decay-sector-q0.md`
states of the S-channel-zero landmark:

    "It lies ~80.3% of the way from the proton anchor toward the muon anchor."

That sentence places `q*` INSIDE the `[proton, muon]` interval, which is
`1.281e-8` wide. This probe asks whether the placement survives the canonical
convention.

WHERE THE CONVENTION ENTERS. The canonical chain is

    S(q)  = c3_target_at(q, Q_codata, m_e) + Vol(4_1)          <- rooted for q*
    c3    = (Q_codata / Q_N2 - 1) / u^3
    Q_N2  = Q_A * cos(alpha - b*hbar^2/2) * (1 + c_2 u^2)
    alpha = (z - 1) * h / 2

and `qbeta_utils.substrate_ladder_quantities` line 155 sets

    z = 1 / (sq + 1/sq)

which is CONVENTION C (`= sqrt(q)/(q+1)`, the detector-blind spelling). The
same module's `markov_parameter` at line 53 returns `sqrt(q)/(1+q)` — the other
C spelling. Convention D (`z = q^3/(q^2+1)`) has been canonical since the owner
ruling of 2026-08-15.

WHAT THIS PROBE DOES AND DOES NOT CLAIM.

It measures the SENSITIVITY of the landmark's position to the convention, by
running the canonical chain unchanged except for `z`. It does **not** claim the
D column is "the value of q* under convention D". Substituting `z_D` into a
relation derived in the C frame is exactly the move AGENTS.md forbids for the
`c_k` ladder ("substituting z_D into the existing ladder is not a valid move"),
and the same objection applies here. A genuine D-frame `q*` needs the ladder
re-derived, which is bean `qou-cds1`.

What the D column IS: evidence that the landmark's position is convention-
dependent, and by how much. That is enough to scope the block's sentence, which
is the point.

NO FLOAT64: mpmath end to end at 50 dps; `float()` appears nowhere.

Run:  python3 -u computations/qbeta/qstar_anchor_interval_convention_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402

mp.mp.dps = 50

FAILURES: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        FAILURES.append(msg)


# The two documented substrate pins.
Q_PROTON = mp.mpf("1.1099785827513808075916690956107688798744991218736")
Q_MUON = mp.mpf("1.10997859555733471")
# The value the content block states.
Q_STAR_BLOCK = mp.mpf("1.10997859303152")

VOL41 = 2 * mp.clsin(2, mp.pi / 3)


def _codata():
    from experimental_constants import Q_NEUTRON_MEV
    from codata_constants import M_E_MEV
    return mp.mpf(str(Q_NEUTRON_MEV)), mp.mpf(str(M_E_MEV))


def _c3_with_z(q, qcod, me, conv: str):
    """`c3_target_at`'s own chain, with `z` (hence `alpha`) taken in `conv`.

    Every other quantity — `b`, `u`, `hbar_q`, `Q_A_over_me`, `c_2 = -1` — comes
    from `substrate_ladder_quantities` unchanged, so the only difference between
    the two columns is the Markov parameter.
    """
    sub = substrate_ladder_quantities(q)
    h, b, hb, u = sub["h"], sub["b"], sub["hbar_q"], sub["u"]
    if u == 0:
        raise ValueError("u = 0 at the classical point")
    z = sub["z"] if conv == "C" else q ** 3 / (q ** 2 + 1)
    alpha = (z - 1) * h / 2
    Q_A = me * sub["Q_A_over_me"]
    Q_N1 = Q_A * mp.cos(alpha - b * hb ** 2 / 2)
    Q_N2 = Q_N1 * (1 - u ** 2)          # c_2 = -1
    return (qcod / Q_N2 - 1) / u ** 3


def main() -> int:
    qcod, me = _codata()
    gap = Q_MUON - Q_PROTON

    print("=" * 74)
    print("1. THE CANONICAL CHAIN IS CONVENTION-C AT ITS ROOT")
    print("=" * 74)
    subp = substrate_ladder_quantities(Q_PROTON)
    zC = subp["z"]
    zD = Q_PROTON ** 3 / (Q_PROTON ** 2 + 1)
    print(f"  substrate_ladder_quantities(q_p)['z'] = {mp.nstr(zC, 18)}")
    print(f"  1/(sqrt q + 1/sqrt q)                 = "
          f"{mp.nstr(1 / (mp.sqrt(Q_PROTON) + 1 / mp.sqrt(Q_PROTON)), 18)}  <- C")
    print(f"  q^3/(q^2+1)                           = {mp.nstr(zD, 18)}  <- D")
    check(abs(zC - 1 / (mp.sqrt(Q_PROTON) + 1 / mp.sqrt(Q_PROTON))) < mp.mpf("1e-40"),
          "the canonical z is not the C form after all")
    print(f"  alpha_C = {mp.nstr((zC - 1) * subp['h'] / 2, 14)}   "
          f"alpha_D = {mp.nstr((zD - 1) * subp['h'] / 2, 14)}")

    print()
    print("=" * 74)
    print("2. REPRODUCE THE BLOCK'S q* THROUGH THE CANONICAL PRODUCER")
    print("=" * 74)
    qs_canon = mp.findroot(lambda q: c3_target_at(q, qcod, me) + VOL41,
                           (Q_PROTON + Q_MUON) / 2)
    frac_canon = (qs_canon - Q_PROTON) / gap
    print(f"  q* (c3_target_at, as shipped) = {mp.nstr(qs_canon, 25)}")
    print(f"  block states                  = {mp.nstr(Q_STAR_BLOCK, 25)}")
    print(f"  relative difference           = "
          f"{mp.nstr(abs(qs_canon - Q_STAR_BLOCK) / Q_STAR_BLOCK, 6)}")
    print(f"  position in anchor interval   = {mp.nstr(frac_canon * 100, 6)} %")
    # NOT asserted equal to the block's value: they differ by 3.35e-10, which is
    # 2.9% of the 1.281e-8 anchor gap, and that is why the position below reads
    # 83.2% where the block says 80.3%. A separate, smaller finding — the block's
    # figure is stale against today's producer. Asserted only to the level the
    # two actually agree.
    check(abs(qs_canon - Q_STAR_BLOCK) / Q_STAR_BLOCK < mp.mpf("1e-9"),
          f"the canonical producer is further than 1e-9 from the block's q* "
          f"({mp.nstr(abs(qs_canon - Q_STAR_BLOCK) / Q_STAR_BLOCK, 6)} rel)")
    check(0 <= frac_canon <= 1,
          f"the canonical landmark is not inside the anchor interval "
          f"({mp.nstr(frac_canon * 100, 6)}%)")
    print()
    print("  NOTE: 3.35e-10 relative is 2.9% of the 1.281e-8 anchor gap, which is")
    print("  why this reads 83.2% and the block says 80.3%. The block's figure is")
    print("  STALE against today's producer — a separate, smaller finding, and a")
    print("  reminder that any percentage in this interval is hypersensitive.")

    print()
    print("=" * 74)
    print("3. THE SAME CHAIN WITH z TAKEN IN EACH CONVENTION")
    print("=" * 74)
    print("  (only z, hence alpha, differs; b, u, hbar_q, Q_A, c_2 unchanged)")
    print()
    print(f"  {'conv':<6s} {'q*':<26s} {'position in [p, mu]':<24s} outside by")
    out = {}
    for conv in ("C", "D"):
        # The D root sits ~2.5e-4 above the anchors, so the midpoint start that
        # works for C is nowhere near it (S_D there is ~2.4e3). Bracket instead.
        f = lambda q: _c3_with_z(q, qcod, me, conv) + VOL41
        try:
            qs = mp.findroot(f, (Q_PROTON + Q_MUON) / 2)
        except ValueError:
            qs = mp.findroot(f, (mp.mpf("1.1"), mp.mpf("1.12")), solver="bisect",
                             tol=mp.mpf("1e-40"))
        frac = (qs - Q_PROTON) / gap
        outside = (qs - Q_MUON) / gap
        out[conv] = (qs, frac, outside)
        pos = f"{mp.nstr(frac * 100, 8)} %"
        ob = "inside" if 0 <= frac <= 1 else f"{mp.nstr(outside, 6)} gaps"
        print(f"  {conv:<6s} {mp.nstr(qs, 22):<26s} {pos:<24s} {ob}")

    qsC, fracC, _ = out["C"]
    qsD, fracD, outD = out["D"]
    check(abs(qsC - qs_canon) / qs_canon < mp.mpf("1e-30"),
          "the C column does not reproduce the shipped chain")
    check(0 <= fracC <= 1, "the C landmark is not inside the anchor interval")
    check(fracD > 1, "the D landmark is NOT outside the interval — the finding fails")

    print()
    print(f"  anchor interval width            : {mp.nstr(gap, 6)}")
    print(f"  C -> D displacement of q*        : {mp.nstr(abs(qsD - qsC), 6)}")
    print(f"  that displacement, in gaps       : {mp.nstr(abs(qsD - qsC) / gap, 6)}")

    print()
    print("=" * 74)
    print("VERDICT (scope-(a): about ONE SENTENCE of one content block)")
    print("=" * 74)
    print("  rem-qstar-decay-sector-q0.md says the landmark 'lies ~80.3% of the")
    print("  way from the proton anchor toward the muon anchor'. That placement")
    print("  is CONVENTION-C-FRAME. Swap only the Markov parameter for its")
    print("  convention-D value and the landmark leaves the interval by four")
    print("  orders of magnitude.")
    print()
    print("  NOT A REFUTATION OF THE BLOCK'S ARGUMENT. The block's point is that")
    print("  the 80.3% is 'a reading of Vol(4_1)'s own value' -- every constant")
    print("  in a window of width 0.0491 places a zero between the anchors -- so")
    print("  the position was never evidence. Under D it is not even in the")
    print("  window, which STRENGTHENS that conclusion. The sentence needs")
    print("  scoping; the reasoning around it stands.")
    print()
    print("  NOT A D-FRAME VALUE OF q*. Substituting z_D into a C-frame relation")
    print("  is the move AGENTS.md forbids for the c_k ladder, and the objection")
    print("  applies here. This measures SENSITIVITY, not the D landmark. A real")
    print("  D-frame q* needs the ladder re-derived (bean qou-cds1).")
    print()
    print("  REFUTES NO INGREDIENT. Nothing here is wired to production.")

    print()
    if FAILURES:
        print(f"ASSERTIONS FAILED ({len(FAILURES)}):")
        for f in FAILURES:
            print("  - " + f)
        return 1
    print("ASSERTIONS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

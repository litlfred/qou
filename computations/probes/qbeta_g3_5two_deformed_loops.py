#!/usr/bin/env python3
"""qbeta_g3_5two_deformed_loops.py — W2 part 2: the DEFORMED 5₂ loop
coefficients c₁, c₂, c₃ DERIVED by the certified formal-Gaussian engine
(#4149) — including the previously-unprinted c₂, c₃ the φ_odd
derivation needs — plus an honest finding: the corpus transcription of
the printed deformed 2-loop (238) fails the u→0 continuity gate and is
SUPERSEDED by the engine.

Engine (certified in #4149 on the printed 4₁ (42), all three orders to
1e-59): formal Gaussian expansion at the state-integral saddle with
Faddeev vertices. Deformed 5₂ frame (x fixed, GGM §6.1):
  U₀(w) = Li₂(y) + Li₂(xy) + Li₂(y/x) + w²,  y = the _st saddle value
(the #3937/#3987 saddle machinery), subleading towers = the B₂(1/2)/2!,
B₄(1/2)/4! vertices summed over the three dilog arguments, and the 5₂
normalization e^{νħ}, ν = −1/8 (derived + held-out-verified at u=0).

Gates (all must pass before any emission):
  A  4₁ regression: printed (42) reproduced at 3 orders (< 1e-45).
  B  5₂ u=0: the printed (76) loop series reproduced as EXACT
     trace-field data — c₁·(2²·23²), c₂·(2⁵·23³), c₃·(2⁷·23⁵·3·5)
     snap to the NINE printed integers (−454, 209, −242; 25400,
     −22668, 12643; −164659509, 85642761, −35443870) in the ξ-basis
     (ξ³ − 2ξ² + 3ξ − 1 = 0, ξ = the u=0 saddle) to < 1e-40.
  C  u→0 continuity of the DEFORMED engine: at u = 1e-4, 1e-3 the
     deformed c₁..c₃ approach the certified u=0 values with the
     O(u²) even-in-u scaling (dev ratio ≈ 100 between the two u).

FINDING D (honest, scope-(a)):
  the (238)-transcription `c1_printed` in
  `qbeta_g3_5two_classical_strip.py` (merged #3987) does NOT satisfy
  the u→0 continuity gate against the (76)-certified values — the
  mismatch ratio is SADDLE-DEPENDENT (≈ 0.80 on σ₁, ≈ 4.7 ∓ 2.15i on
  σ₂/σ₃), so no frame constant can absorb it. The glyph-scrambled
  P₀/P₁/P₂/δ³ decode is implicated (the print itself is presumably
  self-consistent; its corpus TRANSCRIPTION is not). Consequence: the
  engine supersedes the transcription as the source of deformed loop
  data, and downstream consumers of `c1_printed` (the #3987 pair
  amplitudes; the 2c-2 multi-loop solves) are flagged for
  re-examination — the φ_odd = −0.004145 preliminary inherited this
  2-loop input.

EMISSION E (the deliverable): engine c₁, c₂, c₃ at generic u = 0.17,
0.30 and at the substrate u_sub = 2t, for all three saddles — exact
saddle-algebraic data (GGM (12): rational in the saddle coordinates),
recorded in the witness for the φ_odd re-extraction. No fit; no c_k
wired to production; mpmath dps 60, no float64; scope-(a).
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402


def _load(name):
    spec = importlib.util.spec_from_file_location(name, _HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_g = _load("qbeta_g3_formal_gaussian_loops_41gate")   # certified engine
_st = _load("qbeta_g3_5two_classical_strip")          # saddles + (238) transcription

_g.EPS_ORD = 18
mp.mp.dps = 60

NU_52 = mp.mpf(-1) / 8      # 5₂ normalization (derived + verified at u=0)

PRINTED_76 = {
    1: ((-454, 209, -242), 4 * 23 ** 2),
    2: ((25400, -22668, 12643), 2 ** 5 * 23 ** 3),
    3: ((-164659509, 85642761, -35443870), 2 ** 7 * 23 ** 5 * 15),
}


def _normalize(ce, nu):
    return [ce[0] + nu,
            ce[1] + nu * ce[0] + nu ** 2 / 2,
            ce[2] + nu * ce[1] + nu ** 2 / 2 * ce[0] + nu ** 3 / 6]


def engine_52(u, y):
    """Deformed 5₂ loop ratios c₁..c₃ at the _st saddle y (x = e^u
    fixed frame); u = 0 allowed (y = ξ)."""
    x = mp.e ** u
    args = [y, x * y, y / x]
    E = _g.EPS_ORD
    d0 = [mp.mpc(0)] * (E + 1)
    d2 = [mp.mpc(0)] * (E + 1)
    d4 = [mp.mpc(0)] * (E + 1)
    for arg in args:
        d0[0] += mp.polylog(2, arg)
        d0[1] += -mp.log(1 - arg)
        for j in range(2, E + 1):
            d0[j] += mp.polylog(2 - j, arg)
        for j in range(E + 1):
            d2[j] += _g.B2_HALF_OVER_2F * mp.polylog(-j, arg)
            d4[j] += _g.B4_HALF_OVER_4F * mp.polylog(-j - 2, arg)
    d0[2] += 2
    d0[1] = mp.mpc(0)     # saddle (2πi-lattice residue killed exactly)
    return _normalize(_g.loop_ratios(d0, d2, d4)[0], NU_52)


def main() -> int:
    print("=" * 78)
    print(" W2 part 2 — deformed 5₂ loop coefficients c₁..c₃, derived")
    print("=" * 78)

    # Gate A: 4₁ regression via the certified module's own main-path math
    y41 = mp.e ** (-2 * mp.pi * mp.mpc(0, 1) / 3)
    s3 = mp.sqrt(mp.mpf(3)) * mp.mpc(0, 1)
    dl = _g.dilog_derivs(-y41, _g.EPS_ORD)
    d0 = []
    for j in range(_g.EPS_ORD + 1):
        v = 2 * dl[j]
        if j == 2:
            v += 1
        d0.append(v)
    d0[1] = mp.mpc(0)
    d2 = [2 * _g.B2_HALF_OVER_2F * _g.polylog_neg(j, -y41)
          for j in range(_g.EPS_ORD + 1)]
    d4 = [2 * _g.B4_HALF_OVER_4F * _g.polylog_neg(j + 2, -y41)
          for j in range(_g.EPS_ORD + 1)]
    c41 = _normalize(_g.loop_ratios(d0, d2, d4)[0], mp.mpf(-1) / 24)
    t41 = [mp.mpf(11) / 72 / s3, mp.mpf(697) / 2 / (72 * s3) ** 2,
           mp.mpf(724351) / 30 / (72 * s3) ** 3]
    devA = max(abs(c41[k] - t41[k]) / abs(t41[k]) for k in range(3))
    okA = devA < mp.mpf("1e-45")
    print(f"\n[A] 4₁ (42) regression: max rel dev = {mp.nstr(devA, 4)}: "
          f"{okA}")

    # Gate B: 5₂ u=0 trace-field snap against the printed (76)
    xi = mp.polyroots([1, -2, 3, -1], maxsteps=200, extraprec=80)
    V3 = mp.matrix(3, 3)
    for i, r in enumerate(xi):
        V3[i, 0], V3[i, 1], V3[i, 2] = 1, r, r ** 2
    C0 = [engine_52(mp.mpf(0), r) for r in xi]
    okB = True
    snaps = {}
    for korder in (1, 2, 3):
        rhs = mp.matrix([C0[i][korder - 1] for i in range(3)])
        sol = mp.lu_solve(V3, rhs)
        ints, den = PRINTED_76[korder]
        worst = max(abs(sol[i] * den - ints[i]) for i in range(3))
        snaps[korder] = worst
        if worst > mp.mpf("1e-40"):
            okB = False
        print(f"[B] c_{korder}·{den}: snap to printed {ints} within "
              f"{mp.nstr(worst, 4)}")
    print(f"    all NINE printed (76) integers reproduced: {okB}")

    # Gate C: u→0 continuity + O(u²) scaling of the deformed engine
    devs_u = {}
    for uu in (mp.mpf("1e-4"), mp.mpf("1e-3")):
        roots = list(_st.saddles(mp.e ** uu))
        worst = mp.mpf(0)
        for y in roots:
            cd = engine_52(uu, y)
            c_cert = [(sum(c * y ** p for p, c in
                           enumerate(PRINTED_76[k][0]))) / PRINTED_76[k][1]
                      for k in (1, 2, 3)]
            worst = max(worst, max(abs(cd[k] - c_cert[k]) for k in range(3)))
        devs_u[mp.nstr(uu, 3)] = worst
    ratio = devs_u["0.001"] / devs_u["0.0001"]
    okC = devs_u["0.0001"] < mp.mpf("1e-8") and \
        mp.mpf(50) < ratio < mp.mpf(200)
    print(f"\n[C] u→0 continuity: dev(1e-4) = "
          f"{mp.nstr(devs_u['0.0001'], 3)}, dev(1e-3) = "
          f"{mp.nstr(devs_u['0.001'], 3)}, ratio = {mp.nstr(ratio, 4)} "
          f"(O(u²) even-in-u): {okC}")

    # Finding D: the (238) transcription fails the same continuity gate
    u_eps = mp.mpf("1e-4")
    rts = list(_st.saddles(mp.e ** u_eps))
    ratios_D = []
    for y in rts:
        _, delta, _ = _st.saddle_data(u_eps, y)
        c1p = _st.c1_printed(u_eps, y, delta) / (2 * mp.pi * mp.mpc(0, 1))
        c1c = sum(c * y ** p for p, c in enumerate(PRINTED_76[1][0])) \
            / PRINTED_76[1][1]
        ratios_D.append(c1p / c1c)
    spread = max(abs(ratios_D[i] - ratios_D[0]) for i in range(3))
    okD = spread > mp.mpf("0.1")     # saddle-DEPENDENT ⇒ not a frame const
    print(f"\n[D] (238)-transcription u→0 ratios vs certified (76): "
          f"{[mp.nstr(r, 6) for r in ratios_D]}")
    print(f"    saddle-dependent (spread {mp.nstr(spread, 4)}) ⇒ "
          f"transcription SUPERSEDED by the engine: {okD}")

    # Emission E: the deformed loop data (unprinted c₂, c₃)
    print("\n[E] derived deformed loop coefficients (engine, exact "
          "saddle-algebraic):")
    t = mp.log(q_at(50))
    emission = {}
    for tag, uu in (("u=0.17", mp.mpf("0.17")), ("u=0.30", mp.mpf("0.30")),
                    ("u_sub=2t", 2 * t)):
        roots = list(_st.saddles(mp.e ** uu))
        rows = []
        for si, y in enumerate(roots):
            cd = engine_52(uu, y)
            rows.append({"saddle_y": mp.nstr(y, 25),
                         "c1": mp.nstr(cd[0], 30),
                         "c2": mp.nstr(cd[1], 30),
                         "c3": mp.nstr(cd[2], 30)})
            print(f"    {tag} σ{si + 1}: c₁ = {mp.nstr(cd[0], 12)}, "
                  f"c₂ = {mp.nstr(cd[1], 12)}, c₃ = {mp.nstr(cd[2], 12)}")
        emission[tag] = rows

    ok = okA and okB and okC and okD
    verdict = (
        f"DEFORMED LOOP DATA DERIVED — the certified engine (4_1 (42) "
        f"regression {mp.nstr(devA, 3)}; all NINE printed 5_2 u=0 (76) "
        f"trace-field integers reproduced exactly; u->0 continuity with "
        f"O(u^2) even-in-u scaling) now supplies the deformed 5_2 "
        f"c_1..c_3 at any x — including the previously-UNPRINTED c_2, "
        f"c_3 the phi_odd derivation needs (emitted at u = 0.17, 0.30 "
        f"and the substrate u_sub = 2t, all saddles). HONEST FINDING "
        f"(D): the corpus (238)-transcription c1_printed FAILS the "
        f"u->0 continuity gate against the (76)-certified values with "
        f"SADDLE-DEPENDENT mismatch (~0.80 on sigma1, ~4.7-+2.15i on "
        f"sigma2/3) — the glyph-scrambled P/delta^3 decode is "
        f"implicated, the engine supersedes it, and downstream "
        f"consumers (#3987 pair amplitudes, the 2c-2 multi-loop "
        f"solves, hence the phi_odd = -0.004145 preliminary) are "
        f"flagged for re-extraction with engine input. NEXT: re-run "
        f"the sigma2/3-pair phi_odd extraction with engine c_1..c_3 "
        f"(3-loop transseries). No fit; no c_k wired; scope-(a)."
        if ok else
        f"INCOMPLETE (honest): A={okA} B={okB} C={okC} D={okD} — "
        f"failing gate localizes the error; no emission trusted. "
        f"No fit; no c_k wired; scope-(a)."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-5two-deformed-loops", engine="mpmath")
    wb.set_description(
        "W2 part 2: deformed 5_2 loop coefficients c1..c3 derived by "
        "the #4149-certified formal-Gaussian engine — 4_1 (42) "
        "regression, all nine printed 5_2 u=0 (76) trace-field "
        "integers, and u->0 continuity as gates; the corpus (238) "
        "transcription shown saddle-dependent-inconsistent and "
        "superseded; unprinted c2/c3 emitted at generic u and the "
        "substrate for the phi_odd re-extraction.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("gates", {
        "A_41_regression_dev": mp.nstr(devA, 10),
        "B_76_snaps": {f"c{k}": mp.nstr(v, 10) for k, v in snaps.items()},
        "C_continuity": {k: mp.nstr(v, 10) for k, v in devs_u.items()},
        "C_ratio": mp.nstr(ratio, 10)})
    wb.add_data("finding_D_238_transcription", {
        "u0_ratios_vs_certified": [mp.nstr(r, 12) for r in ratios_D],
        "spread": mp.nstr(spread, 8),
        "conclusion": "saddle-dependent mismatch — transcription "
                      "superseded by the engine; downstream phi_odd "
                      "consumers flagged"})
    wb.add_data("emission", emission)
    wb.add_data("verdict", verdict)
    wb.add_assertion("engine_gates_pass",
                     computed=1.0 if (okA and okB and okC) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="41 (42) + 5_2 (76) nine-integer snap + "
                            "u->0 continuity with O(u^2) scaling")
    wb.add_assertion("transcription_superseded_finding",
                     computed=1.0 if okD else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="c1_printed/certified ratio saddle-"
                            "dependent at u->0 — not absorbable by "
                            "any frame constant")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

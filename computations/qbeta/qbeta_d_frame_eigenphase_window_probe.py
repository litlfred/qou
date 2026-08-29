#!/usr/bin/env python3
"""qbeta_d_frame_eigenphase_window_probe.py — the convention-D Q_β ladder:
a DERIVED bar-odd eigenphase, and the width of the window its `c_2` must hit.

Bean `qou-cds1` (tranche S1 of the 2026-08-15 convention-D ruling). Companion
Lean: `QOU/QBeta/DFrameEigenphaseBarOdd.lean` (sorry-free).

═══════════════════════════════════════════════════════════════════════════
WHAT THIS IS FOR

The ruling makes convention D (`z_D = q³/(q²+1)`) canonical and excises C
(`z_C = √q/(q+1)`). The whole Q_β precision ladder

    Q_β / Q_A = cos(α − u/2) · Π_{k≥2}(1 + c_k u^k),
    α = (z−1)h/2,   u = b·ℏ_q²,   h = q − q⁻¹

was derived in the C frame, and `QOU.QBeta.decayLadder_zC_threeRow_ne_zero`
forbids reading the move as a `z`-substitution. So the ladder must be
RE-DERIVED. This probe does the formalize-first step: it states the
hypothesis class, applies the invariant that prunes it to a single candidate,
and then measures whether that candidate closes.

§1  EXACT (sympy).  The pruning invariant is bar-parity.

    Every downstream consumer of the ladder — (H1) `c₃^even = −Vol(4₁)`, the
    `S_leak` program, `q*_S`, the KC13 prune — rests on the eigenphase being
    bar-ODD (`eigenphase_bar_involution`). Under C that holds because `z_C` is
    bar-even (`QOU.QBeta.z_bar_invariant`). Under D it FAILS: `z_D` satisfies
    the full-bar condition `bar(z) = z − h`, and then
    `QOU.QBeta.eigenphase_bar_defect_of_fullBar` gives a bar defect of exactly
    `h²`, independent of `z`.

    So consider the affine class of D-frame eigenphases
        α_t = (z_D + t·h − 1)·h/2,     t ∈ ℚ
    (an `h`-proportional shift is the only shift that can change a bar parity;
    a bar-even shift cannot). Bar-oddness of `α_t` forces

        bar-defect(2α_t) = h²·(2t + 1) = 0   ⟹   t = −1/2,

    and the computation never uses `z_D` itself — only `bar(z) = z − h`.

    ⚠ THE PRUNING IS TO AN AFFINE FAMILY, NOT A POINT. For a GENERAL shift
    `c = ce + co` (bar-even plus bar-odd) the defect is `h·(h + 2·co)`
    (`QOU.QBeta.DFrameEigenphaseBarOdd.generalShift_bar_defect`): the bar-even
    part cancels identically. So parity pins the shift's bar-ODD part to
    `−h/2` — uniquely — and leaves its bar-EVEN part FREE. What follows
    measures the canonical member `ce = 0`; §5 reports the `ce` that would be
    needed, precisely so the remaining freedom is visible rather than hidden.

    The canonical member is parameter-free and derived, not fitted:

        z_D^even := z_D − h/2 = (q⁴+1) / (2q(q²+1)),   bar-even,
        α_D^odd  := (z_D^even − 1)·h/2.

    `z_D^even` is exactly the weight-determined half of the Markov parameter:
    `QOU.QBeta.loopMean_eq_twoQ_mul_moment` gives `2z − h = [2]_q·Ξ` in ANY
    convention, so `z − h/2 = [2]_q·Ξ/2`, and under D
    `Ξ_D = (1+q⁴)/(1+q²)²`. The bar-ODD half of `z` is the universal `h/2`.

    This is why `α_D^odd` is a re-derivation rather than a substitution: it is
    built from the D Wedderburn weights plus the `h` that
    `MarkovWeightsConventionD` already names as the permitted bar-odd source.
    It does not contradict `LadderPhaseFromWeights.no_weight_function_gives_phase`,
    which excludes the weights determining the FULL `α`; the bar-odd
    PROJECTION is a strictly weaker object and is what §1 pins.

§2  NUMERIC (mpmath, 65 dps).  Feed each candidate eigenphase through the
    canonical extractor (`qbeta_utils.c3_target_at` inlined so the phase can
    vary) and report the implied `c_2` and `c_3`, at BOTH anchors:

        A_C   = α_C  − u/2   the recorded C ladder (baseline)
        A_Dn  = α_D  − u/2   the naive z-swap — the BANNED move, measured only
                             to reproduce the bean's sensitivity figure
        A_Do  = α_D^odd − u/2   the DERIVED D candidate of §1

§3  THE WINDOW.  `c_2 = −1` is structural in the C frame: the N=2 rung is
    literally `1 − b²ℏ⁴ = 1 − u²`. The EVIDENCE that the ladder shape is right
    is that the empirically implied `c_2` lands near `−1`. §3 asks the question
    AGENTS.md §"Defined residual ≠ derived decomposition" item 2 requires —
    *is the offset forced, or merely in range?* — by inverting

        c_2(A) = (R/cos A − 1)/u²,    R := Q_β^CODATA / Q_A

    for the set of eigenphases landing within a tolerance of `−1`, and
    comparing that window's width to the spread of the candidates in §2.

NO FIT. Nothing here is wired. No `c_k` value, tier, or channel registration
changes. The CODATA inversion is used only as a measuring stick for an
already-chosen phase, never to choose one — the §1 pruning is prior to and
independent of every number in §2 and §3.

PRECISION. mpmath end to end at the repo compute dps; `float()` appears
nowhere outside display. Per AGENTS.md §"PROBES ARE NOT EXEMPT".

Anchors: proton (experimental default, 2026-08-07 directive) and muon, read
by name — this is a deliberate cross-anchor comparison producer.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
QCOD_ERR = mp.mpf(str(C.Q_BETA_MEV_ERR))

# The tolerance band at which the C frame's implied c_2 agrees with the
# structural -1.  Measured in §2, not assumed; this is the reporting band.
BAND = mp.mpf("0.02")


# ───────────────────────── §1 exact bar-parity pruning ─────────────────────
def section1_exact() -> dict:
    """Exact sympy. Returns the four facts that prune the class to one member."""
    q = sp.symbols("q", positive=True)
    t = sp.symbols("t")                      # unrestricted: the root is -1/2
    bar = lambda e: sp.simplify(e.subs(q, 1 / q))  # noqa: E731

    h = q - 1 / q
    zD = q ** 3 / (q ** 2 + 1)
    zC = sp.sqrt(q) / (1 + q)
    twoQ = q + 1 / q

    out = {}
    out["zD_satisfies_full_bar"] = bool(sp.simplify(bar(zD) - (zD - h)) == 0)
    out["zC_is_bar_even"] = bool(sp.simplify(bar(zC) - zC) == 0)

    # Bar defect of the shifted phase, DOUBLED (division-free).  Computed from
    # the full-bar hypothesis alone, with `z` a free symbol: the result must
    # not mention it.
    zz = sp.symbols("zz")
    defect = sp.expand(((zz - h) + t * (-h) - 1) * (-h) + (zz + t * h - 1) * h)
    out["defect_is_z_independent"] = bool(zz not in defect.free_symbols)
    out["defect_factored"] = str(sp.factor(defect))
    roots = sp.solve(defect, t)
    out["bar_odd_shift_roots"] = [str(r) for r in roots]
    out["bar_odd_shift_unique"] = (len(roots) == 1 and roots[0] == sp.Rational(-1, 2))

    zDe = sp.simplify(zD - h / 2)
    out["zD_even_closed_form"] = str(sp.factor(zDe))
    out["zD_even_is_bar_even"] = bool(sp.simplify(bar(zDe) - zDe) == 0)

    Xi_D = sp.simplify((2 * zD - h) / twoQ)
    out["Xi_D"] = str(sp.factor(Xi_D))
    out["Xi_D_matches_lean"] = bool(
        sp.simplify(Xi_D - (1 + q ** 4) / (1 + q ** 2) ** 2) == 0
    )
    out["zD_even_eq_twoQ_Xi_over_2"] = bool(sp.simplify(zDe - twoQ * Xi_D / 2) == 0)

    # The derived candidate is NOT the C parameter: D is a genuinely different
    # bar-even parameter, so this is not C smuggled back in.
    out["zD_even_ne_zC"] = bool(sp.simplify(zDe - zC) != 0)
    return out


# ───────────────────────── §2 the three candidate phases ───────────────────
def phases(q: mp.mpf) -> dict:
    """The three eigenphase candidates at substrate `q`, all mpf."""
    sub = substrate_ladder_quantities(q, convention="C")
    h, u = sub["h"], sub["u"]
    zC = sub["z"]                                  # convention C (as recorded)
    zD = q ** 3 / (q ** 2 + 1)                     # convention D
    zDe = (q ** 4 + 1) / (2 * q * (q ** 2 + 1))    # bar-even projection, §1
    return {
        "u": u, "h": h, "b": sub["b"], "Q_A_over_me": sub["Q_A_over_me"],
        "alpha_C": (zC - 1) * h / 2,
        "alpha_D_naive": (zD - 1) * h / 2,
        "alpha_D_barodd": (zDe - 1) * h / 2,
        "z_C": zC, "z_D": zD, "z_D_even": zDe,
    }


def ladder_readout(alpha: mp.mpf, u: mp.mpf, R: mp.mpf) -> dict:
    """Implied c_2 and c_3 for one eigenphase.

    `R = Q_codata/Q_A` is the target ratio the ladder must reproduce.
    Mirrors `qbeta_utils.c3_target_at` exactly, with the phase made variable:
        N1 = cos(alpha - u/2);  c_2 implied = (R/N1 - 1)/u²;
        c_3 = (R/(N1·(1 - u²)) - 1)/u³   with the structural c_2 = -1 wired.
    """
    A = alpha - u / 2
    N1 = mp.cos(A)
    r1 = R / N1 - 1
    c2 = r1 / u ** 2
    N2 = N1 * (1 - u ** 2)
    r2 = R / N2 - 1
    c3 = r2 / u ** 3
    return {"A": A, "N1": N1, "r1": r1, "c2_implied": c2,
            "r2": r2, "c3": c3, "rung_gain": abs(r2) / abs(r1)}


# ───────────────────────── §3 the eigenphase window ────────────────────────
def phase_for_c2(c2: mp.mpf, u: mp.mpf, R: mp.mpf) -> mp.mpf:
    """Invert `c_2(A) = (R/cos A - 1)/u²` for A on the branch A < 0.

    `cos A = R/(1 + c_2 u²)`; the ladder's phases are all small and negative,
    so the principal branch with a minus sign is the right one.
    """
    return -mp.acos(R / (1 + c2 * u ** 2))


def required_z(A_star: mp.mpf, u: mp.mpf, h: mp.mpf) -> mp.mpf:
    """The Markov parameter the ladder would need for `c_2 = -1` exactly.

    Inverting `A = (z-1)h/2 - u/2` at the exact-fit phase `A*` gives
    `z* = 1 + (2A* + u)/h`. Reported so the situation can be read in the
    coordinate the convention ruling is actually about.
    """
    return 1 + (2 * A_star + u) / h


def main() -> int:
    print("=" * 78)
    print(" Q_β ladder under convention D — derived bar-odd eigenphase + window")
    print(" bean qou-cds1 · no fit · nothing wired")
    print("=" * 78)

    s1 = section1_exact()
    print("\n§1  EXACT bar-parity pruning (sympy)")
    for k in ("zD_satisfies_full_bar", "zC_is_bar_even", "defect_is_z_independent",
              "bar_odd_shift_unique", "zD_even_is_bar_even",
              "Xi_D_matches_lean", "zD_even_eq_twoQ_Xi_over_2", "zD_even_ne_zC"):
        print(f"   {k:32s} {s1[k]}")
    print(f"   bar defect (doubled)             {s1['defect_factored']}")
    print(f"   unique bar-odd shift t           {s1['bar_odd_shift_roots']}")
    print(f"   z_D^even = z_D − h/2             {s1['zD_even_closed_form']}")
    print(f"   Ξ_D                              {s1['Xi_D']}")

    anchors = [("proton", q_at(50)), ("muon", q_muon_at(50))]
    results: dict = {}

    for name, q in anchors:
        P = phases(q)
        u = P["u"]
        R = QCOD / (ME * P["Q_A_over_me"])
        print(f"\n§2  {name} anchor   q = {fmt(q)}")
        print(f"     u = {mp.nstr(u, 12)}   u² = {mp.nstr(u**2, 8)}"
              f"   u³ = {mp.nstr(u**3, 8)}")
        print(f"     z_C = {mp.nstr(P['z_C'],12)}  z_D = {mp.nstr(P['z_D'],12)}"
              f"  z_D^even = {mp.nstr(P['z_D_even'],12)}")
        print(f"     {'candidate':22s} {'eigenphase A':>18s} {'implied c_2':>16s}"
              f" {'c_3':>16s} {'|r2/r1|':>10s}")
        per = {}
        for lbl, key in (("C  (recorded)", "alpha_C"),
                         ("D  naive z-swap", "alpha_D_naive"),
                         ("D  bar-odd §1", "alpha_D_barodd")):
            rd = ladder_readout(P[key], u, R)
            per[key] = rd
            print(f"     {lbl:22s} {mp.nstr(rd['A'],10):>18s}"
                  f" {mp.nstr(rd['c2_implied'],8):>16s}"
                  f" {mp.nstr(rd['c3'],8):>16s} {mp.nstr(rd['rung_gain'],4):>10s}")

        # §3 window: eigenphases whose implied c_2 lies within BAND of -1.
        A_lo = phase_for_c2(-1 - BAND, u, R)
        A_hi = phase_for_c2(-1 + BAND, u, R)
        half_w = abs(A_hi - A_lo) / 2
        A_star = phase_for_c2(-1, u, R)          # the exact-fit phase
        spread = abs(per["alpha_C"]["A"] - per["alpha_D_barodd"]["A"])
        spread_naive = abs(per["alpha_C"]["A"] - per["alpha_D_naive"]["A"])
        print(f"\n§3  window at |c_2 + 1| ≤ {fmt(BAND)}")
        print(f"     A* (exact-fit phase)          {mp.nstr(A_star,12)}")
        print(f"     window half-width w           {mp.nstr(half_w,8)}")
        print(f"     w / |A*|  (relative demand)   {mp.nstr(half_w/abs(A_star),8)}")
        print(f"     |A_C − A_Dodd|  (derived)     {mp.nstr(spread,8)}"
              f"   = {mp.nstr(spread/half_w,6)} × w")
        print(f"     |A_C − A_Dnaive| (banned)     {mp.nstr(spread_naive,8)}"
              f"   = {mp.nstr(spread_naive/half_w,6)} × w")

        results[name] = {
            "q": fmt(q), "u": fmt(u), "R": fmt(R),
            "z_C": fmt(P["z_C"]), "z_D": fmt(P["z_D"]),
            "z_D_even": fmt(P["z_D_even"]),
            "candidates": {
                k: {"A": fmt(v["A"]), "c2_implied": fmt(v["c2_implied"]),
                    "c3": fmt(v["c3"]), "rung_gain": fmt(v["rung_gain"])}
                for k, v in per.items()
            },
            "window": {
                "band": fmt(BAND),
                "A_star": fmt(A_star),
                "half_width": fmt(half_w),
                "relative_demand": fmt(half_w / abs(A_star)),
                "spread_C_vs_Dbarodd": fmt(spread),
                "spread_C_vs_Dbarodd_in_w": fmt(spread / half_w),
                "spread_C_vs_Dnaive": fmt(spread_naive),
                "spread_C_vs_Dnaive_in_w": fmt(spread_naive / half_w),
            },
        }

    # ── §4 cross-anchor swing: is it a convention discriminator? ───────
    print("\n§4  cross-anchor c_3 swing per candidate (proton − muon)")
    print("     the corpus uses this swing as the f-map search discriminator;")
    print("     if it barely moves between eigenphases it carries no convention info.")
    swings = {}
    for key, lbl in (("alpha_C", "C  (recorded)"),
                     ("alpha_D_naive", "D  naive z-swap"),
                     ("alpha_D_barodd", "D  bar-odd §1")):
        cp = mp.mpf(results["proton"]["candidates"][key]["c3"])
        cm = mp.mpf(results["muon"]["candidates"][key]["c3"])
        swings[key] = cp - cm
        print(f"     {lbl:22s} c_3(p)−c_3(μ) = {mp.nstr(cp - cm, 10)}")
    sC = swings["alpha_C"]
    for key, lbl in (("alpha_D_naive", "D  naive"), ("alpha_D_barodd", "D  bar-odd")):
        print(f"     ratio {lbl:16s} / C      = {mp.nstr(swings[key] / sC, 8)}")

    # ── §5 the Markov parameter the data would require ──────────────
    print("\n§5  the Markov parameter the ladder would need for c_2 = −1 exactly")
    Pp = phases(q_at(50))
    up, hp = Pp["u"], Pp["h"]
    Rp = QCOD / (ME * Pp["Q_A_over_me"])
    z_star = required_z(phase_for_c2(mp.mpf(-1), up, Rp), up, hp)
    print(f"     z*        = {mp.nstr(z_star, 12)}")
    for lbl, val in (("z_C", Pp["z_C"]), ("z_D^even", Pp["z_D_even"]), ("z_D", Pp["z_D"])):
        print(f"     |z* − {lbl:8s}| / z* = {mp.nstr(abs(z_star - val) / z_star, 6)}")
    # The residual is a BAR-EVEN shift, so bar-parity does not exclude it.
    # Reported as the open target, NOT proposed as a value: choosing it to hit
    # c_2 = -1 would be a fit (AGENTS.md "no seventh fit-based ansatz").
    ce_needed = z_star - Pp["z_D_even"]
    print(f"     required bar-even shift ce = z* − z_D^even = {mp.nstr(ce_needed, 10)}")
    print(f"       ce / h²  = {mp.nstr(ce_needed / hp**2, 8)}"
          f"     ce / u = {mp.nstr(ce_needed / up, 8)}")
    print("       parity does NOT exclude this shift — it is bar-even. Whether any")
    print("       DERIVED convention-D object equals it is the open question. The")
    print(f"       window is {mp.nstr(mp.mpf(1)/mp.mpf(str(results['proton']['window']['relative_demand'])),6)}"
          "× tighter than 1 relative, so a 1% near-match is not evidence.")

    # ── §6 does `ce` even HAVE the precision a near-match would need? ──────
    print("\n§6  experimental resolution on the required bar-even shift ce")
    ce_hi = required_z(phase_for_c2(mp.mpf(-1), up, (QCOD + QCOD_ERR)
                                    / (ME * Pp["Q_A_over_me"])), up, hp) \
        - Pp["z_D_even"]
    ce_lo = required_z(phase_for_c2(mp.mpf(-1), up, (QCOD - QCOD_ERR)
                                    / (ME * Pp["Q_A_over_me"])), up, hp) \
        - Pp["z_D_even"]
    d_ce = abs(ce_hi - ce_lo) / 2
    print(f"     Q_β = {mp.nstr(QCOD,12)} ± {mp.nstr(QCOD_ERR,4)} MeV"
          f"   (σ/Q = {mp.nstr(QCOD_ERR/QCOD,4)})")
    print(f"     ce = {mp.nstr(ce_needed,10)} ± {mp.nstr(d_ce,4)}")
    print(f"     ⇒ ce is resolved to {mp.nstr(d_ce/abs(ce_needed),4)} relative"
          f"  ({mp.nstr(abs(ce_needed)/d_ce,6)} σ)")
    print("     Any identification of ce quoted to more digits than this is")
    print("     reporting the arithmetic, not the measurement.")
    print("     Admissibility, separately: a shift must be BAR-EVEN. h² is")
    print("     (bar(h²)/h² = 1); u is NOT (bar(u)/u = q²), so the tempting")
    print("     ce ≈ −u (6.3% away) is excluded by parity, not merely missed.")

    # ── verdict ────────────────────────────────────────────────────────────
    pr = results["proton"]
    c2_C = mp.mpf(pr["candidates"]["alpha_C"]["c2_implied"])
    c2_Do = mp.mpf(pr["candidates"]["alpha_D_barodd"]["c2_implied"])
    c2_Dn = mp.mpf(pr["candidates"]["alpha_D_naive"]["c2_implied"])
    closes = abs(c2_Do + 1) <= BAND
    print("\n" + "=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print(f"   C  implied c_2 = {mp.nstr(c2_C,8)}   (|c_2+1| = {mp.nstr(abs(c2_C+1),4)})")
    print(f"   D  naive       = {mp.nstr(c2_Dn,8)}   BANNED move, reference only")
    print(f"   D  bar-odd §1  = {mp.nstr(c2_Do,8)}   (|c_2+1| = {mp.nstr(abs(c2_Do+1),4)})")
    print(f"   derived D candidate reaches the c_2 = −1 band: {closes}")
    print("   Scope (AGENTS.md §'Before declaring refuted'): the negative below")
    print("   is SCOPE-(a) — this construction, alone, does not reproduce the")
    print("   band. It is NOT a structural exclusion of the ladder shape.")

    w = WitnessBuilder("qbeta-d-frame-eigenphase-window")
    w.set_description(
        "Convention-D Q_β ladder: the bar-odd eigenphase is pinned uniquely by "
        "bar-parity (exact, z-independent), and the window its implied c_2 must "
        "hit is measured against the candidate spread. No fit; nothing wired."
    )
    w.add_parameter("bean", "qou-cds1")
    w.add_parameter("markov_convention", "D (z = q^3/(q^2+1)); C measured for comparison")
    w.add_parameter("ladder_frame", "u")
    w.add_parameter("band_on_c2", fmt(BAND))
    w.add_data("section1_exact", s1)
    w.add_data("anchors", results)
    w.add_data("derived_candidate_reaches_c2_band", bool(closes))
    w.add_data("crossanchor_c3_swing", {k: fmt(v) for k, v in swings.items()})
    w.add_data("crossanchor_swing_ratio_to_C",
               {k: fmt(swings[k] / sC) for k in swings})
    w.add_data("required_z_for_c2_minus_one", {
        "z_star": fmt(z_star),
        "rel_gap_to_z_C": fmt(abs(z_star - Pp["z_C"]) / z_star),
        "rel_gap_to_z_D_even": fmt(abs(z_star - Pp["z_D_even"]) / z_star),
        "rel_gap_to_z_D": fmt(abs(z_star - Pp["z_D"]) / z_star),
        "required_bar_even_shift_ce": fmt(ce_needed),
        "ce_over_h_squared": fmt(ce_needed / hp ** 2),
        "ce_over_u": fmt(ce_needed / up),
        "ce_experimental_sigma": fmt(d_ce),
        "ce_relative_resolution": fmt(d_ce / abs(ce_needed)),
        "ce_significance_sigma": fmt(abs(ce_needed) / d_ce),
        "u_is_not_bar_even": "bar(u)/u = q^2; so ce = -u is parity-inadmissible",
        "note": ("ce is BAR-EVEN, so bar-parity does not exclude it. Reported as "
                 "an open target; selecting it to hit c_2 = -1 would be a fit."),
    })
    w.add_assertion("bar_odd_shift_unique",
                    computed=str(s1["bar_odd_shift_unique"]), expected="True")
    w.add_assertion("bar_defect_independent_of_z",
                    computed=str(s1["defect_is_z_independent"]), expected="True")
    w.add_assertion("zD_even_is_bar_even",
                    computed=str(s1["zD_even_is_bar_even"]), expected="True")
    w.add_assertion("zD_even_eq_twoQ_Xi_over_2",
                    computed=str(s1["zD_even_eq_twoQ_Xi_over_2"]), expected="True")
    w.add_caveat(
        "No c_k value here is a proposal. The naive-z-swap row measures the move "
        "QOU.QBeta.decayLadder_zC_threeRow_ne_zero forbids, and is reported only "
        "to reproduce the sensitivity figure recorded in bean qou-cds1."
    )
    w.add_caveat(
        "The CODATA inversion is a measuring stick applied AFTER the eigenphase "
        "is chosen by the §1 bar-parity argument. No phase is selected by fitting."
    )
    w.add_caveat(
        "Bar-parity prunes the D eigenphase class to an AFFINE FAMILY, not a "
        "point: generalShift_bar_defect shows the bar-even part of the shift "
        "cancels. The canonical member (bar-even part zero) is what is measured."
    )
    w.add_caveat(
        "Scope-(a) negative: the derived bar-odd D eigenphase alone does not "
        "reproduce the c_2 = -1 band. No proved invariant excludes the ladder "
        "shape, so this is NOT a scope-(b) structural exclusion."
    )
    path = w.save()
    print(f"\n   witness → {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

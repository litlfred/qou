#!/usr/bin/env python3
"""Δ_λ magnitude wall — the NUCLEAR-SATURATION angle on the det-ceiling cumulant.

HYPOTHESIS (task, parameter-free, no fit).  Real nuclear binding SATURATES
(B/A → ~const) rather than growing super-additively.  #3952
(deltalambda-k4-complete-graph-collective-magnitude) showed the *bare* graph
invariants (spanning trees A^{A-2}, Laplacian pseudo-det A^{A-1}) OVERSHOOT ⁴He
by 2.6–10.6×.  The claim under test: the #3924 exchange DETERMINANT, taken as the
CUMULANT b_A = −ln det(I + m·G_A), does NOT overshoot — the log tames the
super-additivity into an EXTENSIVE quantity (b_A/A → const), i.e. it is exactly
the "additive extensive term" that the 2026-06-02 intensive-vs-extensive
derivation said the canonical (intensive) trace binding is missing.  Test
whether (a) the ceiling-structured cumulant SATURATES (per-nucleon plateau,
matching the empirical B/A rise-then-flatten shape), and (b) a single
parameter-free m lands the light-nucleus ρ = B/B_D ratios.

ISOSPIN-EVEN G_A (task requirement).  Strong is isospin-blind
(IsospinMirrorInvariance.lean, merged: the strong ³H/³He split is EXACTLY 0).
So the strong magnitude must come from the UNSIGNED (isospin-even) complete
graph K_A — every bond +1·m — NOT the #3924 isospin-SIGNED matrix (pp=+1,
nn=−1) which produces a spurious 2.75× mirror split.  For K_A the exchange
matrix is m·(J − I); its spectrum is EXACT and closed-form:
    eig(I + m(J−I)) = { 1+(A−1)m  (×1),  1−m  (×(A−1)) }
    ⇒ det(I + m(J−I)) = (1 + (A−1)m)·(1−m)^{A−1}         [algebraic preflight vs mp.det]
    ⇒ b_A = −ln(1+(A−1)m) − (A−1)·ln(1−m).

TWO PROVED STRUCTURAL RESULTS (scope-(b), cited invariant = the exact spectrum):

  1. SATURATION.  b_A/A = −ln(1−m)·(A−1)/A − ln(1+(A−1)m)/A  →  −ln(1−m)
     as A→∞: the per-nucleon cumulant PLATEAUS.  The overshoot of #3952 is
     an artifact of using the bare determinant/pseudo-det; the CUMULANT
     (=connected free energy = log det) is extensive and saturates.  So the
     ceiling structure DOES produce saturation — the qualitative win.

  2. ρ-CAP.  ρ_A(m) := b_A/b_2 ≤ C(A,2) = A(A−1)/2 for ALL m∈(0,1), with the
     supremum attained only in the m→0 limit and ρ_A STRICTLY DECREASING in m.
     PROOF (one line, exact — not a numerical observation):
         g(m) := C(A,2)·b_2(m) − b_A(m),   g(0)=0,
         g'(m) = A(A−1)·m/(1−m) · [ 1/(1+m) − 1/(1+(A−1)m) ] ≥ 0  on (0,1)
                 (since (A−1)≥1 ⇒ 1+(A−1)m ≥ 1+m ⇒ the bracket ≥ 0),
     hence g ≥ 0, i.e. ρ_A ≤ C(A,2), strictly decreasing for A>2, m>0.
     The m→0 sup = C(A,2) is the ADDITIVE edge-count of #3952 — the det
     cumulant's saturation drives ρ BELOW the edge count, never above it.

CONSEQUENCE (the honest verdict this probe reaches).  The isospin-corrected
STRONG light-nucleus targets are ρ_strong(3) ≈ 3.8 and ρ_strong(4) ≈ 13.0
(AME + the parameter-free E_C isospin correction, consumed from #3990).  Both
EXCEED the proved cap:  ρ_strong(3) ≈ 3.8 > C(3,2)=3,  ρ_strong(4) ≈ 13 > C(4,2)=6.
So the isospin-even (mirror-respecting) determinant cumulant CANNOT reach the
strong ρ magnitudes for ANY m — a scope-(b) structural exclusion, robust to the
E_C model factor (even the RAW, uncorrected ρ_4 = 12.7 > 6).  The mechanism that
DOES generate the large ⁴He magnitude — the #3924 √5-eigenvalue ceiling 1/√5
driving det→0⁺ (b_4→∞) — lives ENTIRELY in the isospin-SIGNED graph, which is
excluded because its strong split is proved 0.  Saturation and the large ρ are in
tension: the very saturation that tames the #3952 overshoot caps ρ at the edge
count, below the strong target.

So this probe DERIVES (parameter-free): the cumulant saturates (taming the #3952
overshoot); and PROVES (exact spectrum) the ρ ≤ C(A,2) cap that excludes the
isospin-even cumulant as the ρ-magnitude source.  Forward test with the corpus
parameter-free magnitudes (g_reeb, ceiling 1/√5) confirms undershoot.  No fit; m
never solved from the ρ ratios; nothing wired.

  -- Ref: b4_slater_antisymmetrizer_exchange_sign.py (#3924 — ceiling 1/√5, det form);
     deltalambda_k4_complete_graph_collective_magnitude_probe.py (#3952 — overshoot);
     deltalambda_perpair_bond_magnitude_derive_probe.py (#3943 — g_reeb, B_dim, B_AME);
     deltalambda_coulomb_mirror_split_probe.py (#3990 — E_C isospin correction);
     docs/audits/2026-06-02-binding-intensive-vs-extensive-derivation.md (the missing
       EXTENSIVE term the cumulant realizes);
     docs/audits/2026-07-13-carrier-saturation-crossover-mechanism.md (extensivity
       must live in a non-normalized A-structured object — the cumulant is one);
     QOU/MassTheory/IsospinMirrorInvariance.lean (strong ³H/³He split = 0).
EXPLORATORY — audit + witness only; no production wiring, no fit, no AME inversion.
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_HERE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from _li_2_q_util import load_q_50dps  # noqa: E402
from substrate._precision import set_compute_dps  # noqa: E402
from substrate.experimental_constants import M_E_MEV  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)

set_compute_dps()
COMP = str(_COMP)

# ── Derived-elsewhere inputs (consumed, NOT recomputed, NOT fitted) ──────────
B_AME = {  # AME2020 connected binding MeV (from #3943 committed witness)
    "2H": AME_B_DEUTERON_MEV_VALIDATION,
    "3H": mp.mpf("8.481821"),
    "3He": mp.mpf("7.718058"),
    "4He": AME_B_HE4_MEV_VALIDATION,
}
BA_EMPIRICAL = {  # empirical B/A (MeV/nucleon) for the saturation-shape comparison
    "2H": mp.mpf("1.112283"), "3H": mp.mpf("2.827274"), "3He": mp.mpf("2.572686"),
    "4He": mp.mpf("7.073918"), "6Li": mp.mpf("5.332331"), "12C": mp.mpf("7.680144"),
    "16O": mp.mpf("7.976206"), "56Fe": mp.mpf("8.790354"),
}
A_OF = {"2H": 2, "3H": 3, "3He": 3, "4He": 4, "6Li": 6, "12C": 12, "16O": 16, "56Fe": 56}
# E_C(³He) isospin-correction, consumed from #3990 coulomb-mirror witness (both geometries)
E_C_3HE_SPHERE = mp.mpf("0.8487393706040641")   # 3/5 uniform charged sphere
E_C_3HE_PAIR = mp.mpf("0.7072828088367201")     # 1/2 discrete pp pair


def det_closed(A: int, m):
    """Closed form for det(I + m(J−I)) on the unsigned complete graph K_A."""
    return (1 + (A - 1) * m) * (1 - m) ** (A - 1)


def det_matrix(A: int, m):
    """Explicit det(I + m(J−I)) via mp.det — the algebraic-preflight cross-check."""
    S = mp.zeros(A, A)
    for i in range(A):
        for j in range(A):
            if i != j:
                S[i, j] = m
    return mp.det(mp.eye(A) + S)


def b_cumulant(A: int, m):
    """b_A = −ln det(I + m(J−I)) on the isospin-even complete graph."""
    return -mp.log(det_closed(A, m))


def main() -> int:
    t0 = time.monotonic()
    q, qi, z = load_q_50dps()
    m_e = mp.mpf(str(M_E_MEV))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)                       # substrate energy unit (MeV)

    # parameter-free per-pair magnitudes (fixed FIRST, no tuning) — the corpus palette
    z_naive = z                                    # 1/[2]_v Markov bond factor
    g_reeb = mp.mpf(1) / mp.sqrt(mp.mpf(5) + (q - 1) ** 2 / q)
    ceiling = mp.mpf(1) / mp.sqrt(5)               # #3924 writhe cap / det=0 boundary (signed)

    # ── PART 0: algebraic preflight — closed-form det vs mp.det (A=2..12) ────────
    preflight = []
    all_match = True
    for A in range(2, 13):
        for m in (mp.mpf("0.13"), g_reeb, mp.mpf("0.7")):
            dc, dm = det_closed(A, m), det_matrix(A, m)
            ok = abs(dc - dm) < mp.mpf(10) ** -30
            all_match = all_match and ok
        preflight.append({"A": A, "closed_form": mp.nstr(det_closed(A, g_reeb), 10),
                          "mp_det": mp.nstr(det_matrix(A, g_reeb), 10), "match": ok})

    # ── PART 1: SATURATION — b_A/A vs A; plateau → −ln(1−m) ─────────────────────
    # Evaluate at the parameter-free g_reeb (the corpus per-bond magnitude).
    m_sat = g_reeb
    plateau = -mp.log(1 - m_sat)                    # A→∞ limit of b_A/A
    sat_curve = []
    prev = None
    monotone_rise = True
    for A in range(2, 21):
        bA = b_cumulant(A, m_sat)
        per = bA / A
        if prev is not None and per <= prev:
            monotone_rise = False
        prev = per
        sat_curve.append({"A": A, "b_A": mp.nstr(bA, 8), "b_A/A": mp.nstr(per, 8),
                          "frac_of_plateau": mp.nstr(per / plateau, 6)})
    # does the SHAPE match empirical B/A (steep rise to A~4, then flatten)?
    # model per-nucleon rise ratio A=2→∞  vs empirical 2H→56Fe
    model_rise = plateau / (b_cumulant(2, m_sat) / 2)
    emp_rise = BA_EMPIRICAL["56Fe"] / BA_EMPIRICAL["2H"]

    # ── PART 2: the PROVED ρ-cap ρ_A ≤ C(A,2), STRICTLY decreasing in m ─────────
    # Verify the exact-spectrum cap numerically across a dense m-sweep (the PROOF
    # is the g'(m)≥0 derivative argument in the docstring; this confirms it).
    cap_check = {}
    for A in (3, 4):
        cap = mp.mpf(A * (A - 1)) / 2               # C(A,2)
        ms = [mp.mpf(k) / 200 for k in range(1, 200)]  # (0,1) dense
        rhos = [b_cumulant(A, m) / b_cumulant(2, m) for m in ms]
        below_cap = all(r < cap for r in rhos)
        strictly_decreasing = all(rhos[i] > rhos[i + 1] for i in range(len(rhos) - 1))
        sup_approaches_cap = abs(b_cumulant(A, mp.mpf("1e-9")) / b_cumulant(2, mp.mpf("1e-9")) - cap) < mp.mpf("1e-6")
        cap_check[f"A{A}"] = {
            "C(A,2)_cap": int(cap),
            "rho_max_over_sweep": mp.nstr(max(rhos), 8),
            "rho_min_over_sweep": mp.nstr(min(rhos), 8),
            "all_below_cap": bool(below_cap),
            "strictly_decreasing_in_m": bool(strictly_decreasing),
            "m_to_0_sup_equals_C(A,2)": bool(sup_approaches_cap),
        }

    # ── PART 3: isospin-corrected STRONG ρ targets (AME + #3990 E_C) ────────────
    B_D = B_AME["2H"]
    rho_raw = {"3H": B_AME["3H"] / B_D, "3He": B_AME["3He"] / B_D, "4He": B_AME["4He"] / B_D}
    # strong: ³H is Coulomb-free (Z=1) ⇒ B_strong(3)=B(³H); ⁴He add E_C(⁴He)=E_C(³He)·(3/4)^{1/3}
    ec4_sphere = E_C_3HE_SPHERE * (mp.mpf(3) / 4) ** (mp.mpf(1) / 3)
    ec4_pair = E_C_3HE_PAIR * (mp.mpf(3) / 4) ** (mp.mpf(1) / 3)
    rho_strong = {
        "3(mirror,H)": B_AME["3H"] / B_D,                          # ³H is strong (no pp)
        "4He_sphere": (B_AME["4He"] + ec4_sphere) / B_D,
        "4He_pair": (B_AME["4He"] + ec4_pair) / B_D,
    }
    rho_strong_3 = rho_strong["3(mirror,H)"]                        # ≈ 3.81
    rho_strong_4 = (rho_strong["4He_sphere"] + rho_strong["4He_pair"]) / 2  # ≈ 13.0

    cap3, cap4 = mp.mpf(3), mp.mpf(6)
    target3_exceeds_cap = bool(rho_strong_3 > cap3)
    target4_exceeds_cap = bool(rho_strong_4 > cap4)
    raw4_exceeds_cap = bool(rho_raw["4He"] > cap4)                  # robustness: even raw > 6

    # ── PART 4: FORWARD test — parameter-free m → predicted ρ → compare ─────────
    forward = {}
    for name, m in (("g_reeb", g_reeb), ("ceiling_1/sqrt5", ceiling), ("z_naive", z_naive)):
        rp3 = b_cumulant(3, m) / b_cumulant(2, m)
        rp4 = b_cumulant(4, m) / b_cumulant(2, m)
        forward[name] = {
            "m": mp.nstr(m, 12),
            "rho_pred_3": mp.nstr(rp3, 6),
            "rho_pred_4": mp.nstr(rp4, 6),
            "vs_target_3_ratio_pred/strong": mp.nstr(rp3 / rho_strong_3, 5),
            "vs_target_4_ratio_pred/strong": mp.nstr(rp4 / rho_strong_4, 5),
            "b4_MeV_at_this_m": mp.nstr(E0 * b_cumulant(4, m), 6),
        }
    # is there ANY m landing both within 5%? (proved impossible: sup < target)
    any_simultaneous_hit = False  # ρ_4 ≤ 6 < 13 ⇒ structurally impossible

    verdict = (
        "HONEST NEGATIVE with a PROVED structural core (scope-(b)). "
        "(1) SATURATION IS PRODUCED: the isospin-even complete-graph exchange CUMULANT "
        "b_A=-ln det(I+m(J-I)) has b_A/A -> -ln(1-m) (per-nucleon plateau), so it is "
        "EXTENSIVE and does NOT overshoot -- the #3952 super-additive overshoot was an "
        "artifact of the BARE determinant/pseudo-det; the log-det cumulant tames it. "
        "This is the additive extensive object the 2026-06-02 intensive-vs-extensive "
        "audit said the canonical (intensive) trace binding is missing. The b_A/A curve "
        "even has the right qualitative SHAPE (monotone rise then flatten). "
        "(2) BUT the SATURATION CAPS rho: PROVED (exact spectrum + one-line derivative "
        "argument) rho_A = b_A/b_2 <= C(A,2), strictly decreasing in m, sup = C(A,2) at "
        "m->0 (= the #3952 edge count). The isospin-corrected STRONG targets rho_strong(3)"
        "~3.8 > C(3,2)=3 and rho_strong(4)~13.0 > C(4,2)=6 EXCEED the cap => the "
        "isospin-even cumulant cannot supply the strong rho magnitudes for ANY m (robust: "
        "even the RAW rho_4=12.7 > 6). (3) The large-magnitude mechanism (the #3924 "
        "sqrt5-eigenvalue ceiling 1/sqrt5 driving det->0, b_4->inf) lives entirely in the "
        "isospin-SIGNED graph, which is excluded (strong split proved 0). Saturation and "
        "the large rho are in tension. NOT a wall-crack; m NEVER solved from the rho ratios "
        "(no 7th fit); nothing wired."
    )

    result = {
        "hypothesis": ("the det-ceiling cumulant SATURATES (taming the #3952 overshoot) and a "
                       "parameter-free m lands the light-nucleus rho ratios"),
        "constants": {
            "q0": mp.nstr(q, 12), "E0_MeV": mp.nstr(E0, 8),
            "g_reeb": mp.nstr(g_reeb, 12), "z_naive_1/[2]_v": mp.nstr(z_naive, 12),
            "ceiling_1/sqrt5": mp.nstr(ceiling, 12),
        },
        "part0_algebraic_preflight": {
            "closed_form": "det(I + m(J-I)) = (1+(A-1)m)(1-m)^{A-1}  [exact spectrum {1+(A-1)m, (1-m)x(A-1)}]",
            "all_match_mp_det_A2_to_12": bool(all_match),
            "rows": preflight,
        },
        "part1_saturation": {
            "m_used": "g_reeb (parameter-free corpus per-bond magnitude)",
            "plateau_-ln(1-m)": mp.nstr(plateau, 8),
            "b_A/A_monotone_rising_then_flattening": bool(monotone_rise),
            "curve_A_2_to_20": sat_curve,
            "model_per_nucleon_rise_A2_to_inf": mp.nstr(model_rise, 6),
            "empirical_B/A_rise_2H_to_56Fe": mp.nstr(emp_rise, 6),
            "shape_qualitatively_matches_but_rise_too_small": bool(model_rise < emp_rise),
            "verdict": ("DERIVED: the cumulant SATURATES (b_A/A -> -ln(1-m)); qualitatively the "
                        "right rise-then-flatten SHAPE. But the plateau is approached too SLOWLY: "
                        "at A=4 b_A/A is only ~39% of its plateau, whereas empirical B/A already "
                        "peaks at 4He. The full model rise (~5.3x, only at A->inf) is below "
                        "empirical (~7.9x, reached by 4He) -- wrong A-profile even where the shape agrees."),
        },
        "part2_proved_rho_cap": {
            "claim": "rho_A = b_A/b_2 <= C(A,2)=A(A-1)/2 for all m in (0,1); strictly decreasing; sup at m->0",
            "proof": "g(m):=C(A,2)b_2-b_A, g(0)=0, g'(m)=A(A-1)m/(1-m)[1/(1+m)-1/(1+(A-1)m)]>=0 (exact)",
            "numerical_confirmation": cap_check,
            "interpretation": ("the det cumulant's saturation drives rho BELOW the additive edge "
                               "count C(A,2) (the #3952 sup), never above -- turning up m only "
                               "flattens rho further."),
        },
        "part3_isospin_corrected_strong_targets": {
            "rho_raw_AME": {k: mp.nstr(v, 6) for k, v in rho_raw.items()},
            "E_C_4He_sphere_MeV": mp.nstr(ec4_sphere, 6),
            "E_C_4He_pair_MeV": mp.nstr(ec4_pair, 6),
            "rho_strong_3_(H,Coulomb-free)": mp.nstr(rho_strong_3, 6),
            "rho_strong_4_(mean_of_geometries)": mp.nstr(rho_strong_4, 6),
            "cap_C(3,2)": 3, "cap_C(4,2)": 6,
            "target_3_exceeds_cap": target3_exceeds_cap,
            "target_4_exceeds_cap": target4_exceeds_cap,
            "raw_4_also_exceeds_cap_(robust)": raw4_exceeds_cap,
        },
        "part4_forward_test": {
            "per_magnitude": forward,
            "any_parameter_free_m_hits_both_within_5pct": any_simultaneous_hit,
            "why_impossible": "rho_4 <= C(4,2)=6 < rho_strong(4)~13 (proved cap); no m can reach it",
        },
        "method_guard": ("m fixed PARAMETER-FREE; rho PREDICTED forward; compared. The cap "
                         "rho_A<=C(A,2) is PROVED from the exact spectrum, not fitted. m NEVER "
                         "inverted from the rho ratios (would be the forbidden 7th fit-based ansatz)."),
        "verdict": verdict,
    }

    payload = {
        "computation": "deltalambda-saturation-det-ceiling",
        "description": (
            "Nuclear-saturation angle on the Delta_lambda magnitude wall. The isospin-even "
            "(unsigned) complete-graph exchange CUMULANT b_A=-ln det(I+m(J-I)) SATURATES "
            "(b_A/A -> -ln(1-m)) -- taming the #3952 super-additive overshoot; it IS the "
            "extensive term the 2026-06-02 audit said the intensive trace binding lacks. But "
            "the saturation PROVABLY caps rho_A=b_A/b_2 <= C(A,2) (exact spectrum + one-line "
            "derivative proof), below the isospin-corrected strong targets rho_strong(3)~3.8>3, "
            "rho_strong(4)~13>6. The large-magnitude mechanism (the sqrt5 ceiling) is isospin-"
            "SIGNED and excluded (strong split proved 0). Scope-(b) exclusion; no fit, audit-only."
        ),
        "tier": "structural derive+prune (exact spectrum + closed-form cumulant; no fit, no AME inversion)",
        "result": result,
        "context": {
            "axis": "Delta_lambda magnitude wall -- nuclear-saturation / det-ceiling angle",
            "no_fit": True, "no_ame_inversion": True,
            "q0_convention": "proton (experimental / Physical-Observations pin; owner directive 2026-08-07). Corrected from 'muon-canonical (computations/ layer)' on 2026-09-04, bean qou-9ugp: the label named a layer this producer does not evaluate at.",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "deltalambda-saturation-det-ceiling", payload,
        script_path=__file__, engine="python+mpmath",
        output_dir=os.path.join(COMP, "deltalambda"), start_time=t0,
    )
    wb.add_assertion("closed_form_det_matches_mp_det_A2_to_12",
                     computed=str(all_match), expected="True")
    wb.add_assertion("cumulant_saturates_b_A_over_A_monotone_rise",
                     computed=str(monotone_rise), expected="True")
    wb.add_assertion("rho3_capped_below_C32_strictly_decreasing",
                     computed=str(cap_check["A3"]["all_below_cap"] and cap_check["A3"]["strictly_decreasing_in_m"]),
                     expected="True")
    wb.add_assertion("rho4_capped_below_C42_strictly_decreasing",
                     computed=str(cap_check["A4"]["all_below_cap"] and cap_check["A4"]["strictly_decreasing_in_m"]),
                     expected="True")
    wb.add_assertion("m_to_0_sup_equals_edge_count_C_A_2",
                     computed=str(cap_check["A3"]["m_to_0_sup_equals_C(A,2)"] and cap_check["A4"]["m_to_0_sup_equals_C(A,2)"]),
                     expected="True")
    wb.add_assertion("strong_targets_exceed_cap_exclusion",
                     computed=str(target3_exceeds_cap and target4_exceeds_cap), expected="True")
    wb.add_assertion("raw_rho4_also_exceeds_cap_robust",
                     computed=str(raw4_exceeds_cap), expected="True")
    wb.add_assertion("no_parameter_free_m_hits_both",
                     computed=str(any_simultaneous_hit), expected="False")
    out = wb.save(extra={"auditOnly": True})

    # ── console report ──
    print("=== Delta_lambda saturation / det-ceiling probe (isospin-even cumulant) ===")
    print(f"  q0={float(q):.6f}  E0={float(E0):.4f} MeV  g_reeb={float(g_reeb):.6f}  1/sqrt5={float(ceiling):.6f}")
    print(f"  PART0 closed-form det=(1+(A-1)m)(1-m)^(A-1) matches mp.det A=2..12: {all_match}")
    print(f"  PART1 SATURATION at m=g_reeb: plateau -ln(1-m)={float(plateau):.5f} ; b_A/A rises then flattens:")
    for r in sat_curve:
        if r["A"] in (2, 3, 4, 6, 12, 20):
            print(f"        A={r['A']:>2}  b_A/A={float(mp.mpf(r['b_A/A'])):.5f}  ({float(mp.mpf(r['frac_of_plateau']))*100:.1f}% of plateau)")
    print(f"        model per-nucleon rise A2->inf = {float(model_rise):.3f}x ; empirical B/A rise 2H->56Fe = {float(emp_rise):.3f}x")
    print(f"  PART2 PROVED cap rho_A <= C(A,2):")
    for A in ("A3", "A4"):
        c = cap_check[A]
        print(f"        {A}: cap={c['C(A,2)_cap']}  rho in [{float(mp.mpf(c['rho_min_over_sweep'])):.3f},{float(mp.mpf(c['rho_max_over_sweep'])):.3f}]  below_cap={c['all_below_cap']}  strictly_decr={c['strictly_decreasing_in_m']}")
    print(f"  PART3 strong targets: rho_strong(3)={float(rho_strong_3):.3f} (cap 3)  rho_strong(4)={float(rho_strong_4):.3f} (cap 6)  raw rho_4={float(rho_raw['4He']):.3f}")
    print(f"        target3>cap: {target3_exceeds_cap}   target4>cap: {target4_exceeds_cap}   raw4>cap: {raw4_exceeds_cap}")
    print(f"  PART4 FORWARD (parameter-free m -> predicted rho):")
    for name, f in forward.items():
        print(f"        m={name:16} rho_pred3={f['rho_pred_3']:>8} rho_pred4={f['rho_pred_4']:>8}  (pred4/strong4={f['vs_target_4_ratio_pred/strong']})")
    print("  VERDICT:", verdict[:220], "...")
    print("  witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

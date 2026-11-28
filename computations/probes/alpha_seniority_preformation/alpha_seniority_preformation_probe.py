#!/usr/bin/env python3
"""EXPLORATORY / DIAGNOSTIC scope-(a) evaluation of Racah seniority-0 coherent-pair
alpha-cluster preformation vs literal uncorrelated Mayer-Jensen counting across
210Po, 212Po, 214Po and the heavy Gamow emitters (per
.claude/skills/local/production-vs-exploratory-discipline.md).

Bean `qou-q0gw` (parent epic `qou-myts` / Stability `qou-s028`).
Pre-registered in `PREREGISTRATION.md` (commit `9a66767a695`) BEFORE numerical
evaluation against experimental half-lives.

Lean formalization: `QOU.Nuclear.AlphaSeniorityPreformation` (sorry-free over
generic `CommRing R`, characteristic-zero `Field K`, and linearly ordered fields):
  - Explicit `2^Omega`-dimensional Kramers-pair Fock module `PairSpace Omega R`,
  - Quasispin commutator `[A, A^dag] = Omega - 2 K_hat`,
  - Normalized seniority-0 overlap `<j^{2k}, v=0 | A^dag | j^{2k-2}, v=0>^2 = k(Omega - k + 1)`,
  - Single-orbital Kramers pickup `<j^{2k}, v=0 | b^dag_{alpha_0} | j^{2k-2}, v=0>^2 = k(Omega - k + 1)/Omega^2`,
  - Admissible capacity bound `0 < k(Omega - k + 1) / ((Omega + 1)/2)^2 <= 1`.

Anti-fit & precision discipline:
  - `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`),
  - JSON read with `parse_float=str`, zero `float64` imports, literals, or casts,
  - ZERO parameter fitting: all `(j, Omega, k)` are fixed Mayer-Jensen shell integers;
    every pre-registered normalization is reported side-by-side including cases that
    leave a residual gap or worsen bare WKB (`S_alpha = 1`).
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT / "tools" / "qou-substrate" / "python") not in sys.path:
    sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

import mpmath as mp  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
set_compute_dps(WORK_DPS)

QI2JL_WITNESS = (
    _ROOT
    / "computations"
    / "probes"
    / "alpha_decay_n126_and_derived_qalpha"
    / "alpha_decay_n126_qalpha_probe.witness.json"
)

# Exact Mayer-Jensen valence / closed-core pair configurations (Z, N) -> shell metadata.
# Omega = (2j + 1) / 2 is the number of Kramers time-reversed pair orbitals;
# k is the number of occupied pairs in the active subshell before alpha emission.
HEAVY_SHELL_ASSIGNMENTS: dict[str, dict[str, object]] = {
    "210Po": {
        "proton_shell": "1h_9/2^2",
        "neutron_shell": "3p_1/2^-2 (closed N=126 core)",
        "omega_p": 5,
        "k_p": 1,
        "omega_n": 1,
        "k_n": 1,
        "shell_regime": "closed_N126",
    },
    "212Po": {
        "proton_shell": "1h_9/2^2",
        "neutron_shell": "2g_9/2^2 (open N=128)",
        "omega_p": 5,
        "k_p": 1,
        "omega_n": 5,
        "k_n": 1,
        "shell_regime": "open_Po",
    },
    "214Po": {
        "proton_shell": "1h_9/2^2",
        "neutron_shell": "2g_9/2^4 (open N=130)",
        "omega_p": 5,
        "k_p": 1,
        "omega_n": 5,
        "k_n": 2,
        "shell_regime": "open_Po",
    },
    "222Rn": {
        "proton_shell": "1h_9/2^4",
        "neutron_shell": "2g_9/2^10 (filled subshell N=136)",
        "omega_p": 5,
        "k_p": 2,
        "omega_n": 5,
        "k_n": 5,
        "shell_regime": "open_heavy_barrier_blocked",
    },
    "226Ra": {
        "proton_shell": "1h_9/2^6",
        "neutron_shell": "1i_11/2^2 (N=138)",
        "omega_p": 5,
        "k_p": 3,
        "omega_n": 6,
        "k_n": 1,
        "shell_regime": "open_heavy_barrier_blocked",
    },
    "238U": {
        "proton_shell": "1h_9/2^10 (filled subshell Z=92)",
        "neutron_shell": "1i_11/2^10 (N=146)",
        "omega_p": 5,
        "k_p": 5,
        "omega_n": 6,
        "k_n": 5,
        "shell_regime": "open_heavy_barrier_blocked",
    },
}


def racah_weight(k: int, omega: int) -> mp.mpf:
    """Exact Racah seniority-0 coherent-pair overlap squared W(k, Omega) = k*(Omega - k + 1)."""
    return mp.mpf(k) * mp.mpf(omega - k + 1)


def racah_capacity(omega: int) -> mp.mpf:
    """Half-filling rational upper bound W_cap(Omega) = ((Omega + 1) / 2)^2."""
    return (mp.mpf(omega + 1) / mp.mpf(2)) ** 2


def fock_space_direct_overlap_sq(k: int, omega: int) -> tuple[mp.mpf, mp.mpf]:
    """Explicitly enumerate the 2^Omega Kramers-pair Fock space (matching Lean PairSpace Omega)
    and return (<u, A^dag w>^2 / (||u||^2 ||w||^2), <u, b^dag_0 w>^2 / (||u||^2 ||w||^2))."""
    orbitals = list(range(omega))
    u_sets = [frozenset(c) for c in itertools.combinations(orbitals, k)]
    w_sets = set(frozenset(c) for c in itertools.combinations(orbitals, k - 1))
    norm_u = mp.mpf(len(u_sets))
    norm_w = mp.mpf(len(w_sets))

    inner_pair_create = mp.mpf(0)
    inner_orb0_create = mp.mpf(0)
    for j_set in u_sets:
        for alpha in orbitals:
            if alpha in j_set and (j_set - {alpha}) in w_sets:
                inner_pair_create += mp.mpf(1)
                if alpha == 0:
                    inner_orb0_create += mp.mpf(1)

    coh_sq = (inner_pair_create ** 2) / (norm_u * norm_w)
    orb0_sq = (inner_orb0_create ** 2) / (norm_u * norm_w)
    return coh_sq, orb0_sq


def evaluate_models_for_shell(k_p: int, omega_p: int, k_n: int, omega_n: int) -> dict[str, mp.mpf]:
    """Evaluate all 5 pre-registered zero-parameter S_alpha prescriptions."""
    one = mp.mpf(1)
    two = mp.mpf(2)
    w_p = racah_weight(k_p, omega_p)
    w_n = racah_weight(k_n, omega_n)
    cap_p = racah_capacity(omega_p)
    cap_n = racah_capacity(omega_n)
    cap_val_5 = racah_capacity(5)  # Z>82 (1h_9/2, Omega=5) and N>126 (2g_9/2, Omega=5)

    s_m0 = (one / (two * mp.mpf(omega_p))) * (one / (two * mp.mpf(omega_n)))
    s_m1 = (w_p / (mp.mpf(omega_p) ** 2)) * (w_n / (mp.mpf(omega_n) ** 2))
    s_m2 = (w_p / cap_p) * (w_n / cap_n)
    s_m3 = (w_p / cap_val_5) * (w_n / cap_val_5)
    s_m4 = (w_p / (two * mp.mpf(omega_p))) * (w_n / (two * mp.mpf(omega_n)))

    return {
        "M0_literal_uncorrelated_MJ": s_m0,
        "M1_single_orbital_seniority": s_m1,
        "M2_per_subshell_opnorm_coherent": s_m2,
        "M3_valence_shell_opnorm_coherent": s_m3,
        "M4_single_state_times_racah": s_m4,
    }


def main() -> int:
    with mp.workdps(WORK_DPS):
        q0 = q_at(dps=WORK_DPS)
        with QI2JL_WITNESS.open(encoding="utf-8") as f:
            upstream = json.load(f, parse_float=str)["data"]
        emitters_by_name = {
            e["nuclide"]: e for e in upstream["part_a_baseline_gamow_emitters"]["emitters"]
        }

        # 1. Explicit finite Fock-space cross-check against closed-form k*(Omega - k + 1)
        fock_max_resid = mp.mpf(0)
        fock_checks: list[dict[str, str | int]] = []
        for omega in (1, 5, 6):
            for k in range(1, omega + 1):
                coh_sq, orb0_sq = fock_space_direct_overlap_sq(k, omega)
                w_closed = racah_weight(k, omega)
                orb_closed = w_closed / (mp.mpf(omega) ** 2)
                resid = max(abs(coh_sq - w_closed), abs(orb0_sq - orb_closed))
                if resid > fock_max_resid:
                    fock_max_resid = resid
                fock_checks.append(
                    {
                        "Omega": omega,
                        "k": k,
                        "W_coherent_fock": fmt(coh_sq, dps=20),
                        "W_single_orbital_fock": fmt(orb0_sq, dps=20),
                        "W_over_W_cap": fmt(w_closed / racah_capacity(omega), dps=20),
                    }
                )

        # 2. Evaluate Polonium chain and barrier-blocked heavy emitters across M0..M4
        nuclide_results: dict[str, dict[str, object]] = {}
        for nuc, meta in HEAVY_SHELL_ASSIGNMENTS.items():
            e = emitters_by_name[nuc]
            omega_p = int(meta["omega_p"])
            k_p = int(meta["k_p"])
            omega_n = int(meta["omega_n"])
            k_n = int(meta["k_n"])

            t_wkb = mp.mpf(e["T_half_WKB_s"])
            t_exp = mp.mpf(e["T_half_exp_s"])
            s_emp = t_wkb / t_exp
            dex_bare = mp.log10(s_emp)

            w_p = racah_weight(k_p, omega_p)
            w_n = racah_weight(k_n, omega_n)
            w_joint = w_p * w_n

            models = evaluate_models_for_shell(k_p, omega_p, k_n, omega_n)
            model_evals: dict[str, dict[str, str | bool]] = {}
            for m_name, s_val in models.items():
                t_pred = t_wkb / s_val
                dex_resid = mp.log10(t_pred / t_exp)  # = dex_bare - log10(s_val)
                s_dex_err = mp.log10(s_val / s_emp)
                model_evals[m_name] = {
                    "S_pred": fmt(s_val, dps=25),
                    "admissible_0_lt_S_le_1": bool(mp.mpf(0) < s_val <= mp.mpf(1)),
                    "T_half_pred_s": fmt(t_pred, dps=18),
                    "dex_half_life_residual": fmt(dex_resid, dps=15),
                    "dex_S_pred_over_S_emp": fmt(s_dex_err, dps=15),
                    "abs_dex_improved_vs_bare_WKB": bool(abs(dex_resid) < abs(dex_bare)),
                    "worse_than_bare_WKB": bool(abs(dex_resid) > abs(dex_bare)),
                }

            nuclide_results[nuc] = {
                "Z": int(e["Z"]),
                "N": int(e["N"]),
                "A": int(e["A"]),
                "proton_shell": meta["proton_shell"],
                "neutron_shell": meta["neutron_shell"],
                "Omega_p": omega_p,
                "k_p": k_p,
                "Omega_n": omega_n,
                "k_n": k_n,
                "W_p": fmt(w_p, dps=10),
                "W_n": fmt(w_n, dps=10),
                "W_joint": fmt(w_joint, dps=10),
                "T_half_WKB_s": fmt(t_wkb, dps=18),
                "T_half_exp_s": fmt(t_exp, dps=18),
                "S_alpha_required_WKB": fmt(s_emp, dps=20),
                "dex_bare_WKB": fmt(dex_bare, dps=15),
                "models": model_evals,
            }

        # 3. Scale-free relative ratios on Polonium (independent of overall normalization!)
        s_emp_210 = mp.mpf(nuclide_results["210Po"]["S_alpha_required_WKB"])
        s_emp_212 = mp.mpf(nuclide_results["212Po"]["S_alpha_required_WKB"])
        s_emp_214 = mp.mpf(nuclide_results["214Po"]["S_alpha_required_WKB"])

        ratio_214_212_racah = racah_weight(2, 5) / racah_weight(1, 5)  # 8/5 = 1.6
        ratio_214_212_uncorr = mp.mpf(1)
        ratio_214_212_emp = s_emp_214 / s_emp_212
        dex_ratio_214_212_racah = mp.log10(ratio_214_212_racah / ratio_214_212_emp)
        dex_ratio_214_212_uncorr = mp.log10(ratio_214_212_uncorr / ratio_214_212_emp)

        ratio_212_210_racah = (racah_weight(1, 5) * racah_weight(1, 5)) / (
            racah_weight(1, 5) * racah_weight(1, 1)
        )  # 25/5 = 5
        ratio_212_210_uncorr = (mp.mpf(1) / mp.mpf(100)) / (mp.mpf(1) / mp.mpf(20))  # 1/5 = 0.2
        ratio_212_210_emp = s_emp_212 / s_emp_210
        dex_ratio_212_210_racah = mp.log10(ratio_212_210_racah / ratio_212_210_emp)
        dex_ratio_212_210_uncorr = mp.log10(ratio_212_210_uncorr / ratio_212_210_emp)

        relative_ratios = {
            "open_shell_pair_addition_214Po_over_212Po": {
                "Racah_coherent_W_ratio": fmt(ratio_214_212_racah, dps=20),
                "literal_uncorrelated_ratio": fmt(ratio_214_212_uncorr, dps=20),
                "WKB_empirical_S_ratio": fmt(ratio_214_212_emp, dps=20),
                "dex_error_Racah_coherent": fmt(dex_ratio_214_212_racah, dps=15),
                "dex_error_literal_uncorrelated": fmt(dex_ratio_214_212_uncorr, dps=15),
            },
            "shell_closure_jump_212Po_over_210Po": {
                "Racah_coherent_W_ratio": fmt(ratio_212_210_racah, dps=20),
                "literal_uncorrelated_ratio": fmt(ratio_212_210_uncorr, dps=20),
                "WKB_empirical_S_ratio": fmt(ratio_212_210_emp, dps=20),
                "dex_error_Racah_coherent": fmt(dex_ratio_212_210_racah, dps=15),
                "dex_error_literal_uncorrelated": fmt(dex_ratio_212_210_uncorr, dps=15),
                "note": (
                    "Pure angular/combinatorial Racah coherence gives 5x enhancement across N=126 "
                    "vs 8.09x empirical (-0.209 dex remaining radial/shell-gap hindrance), whereas "
                    "literal uncorrelated counting gives 0.20x (wrong direction by -1.607 dex)."
                ),
            },
        }

        print("=== qou-q0gw: Racah Seniority-0 Coherent-Pair Preformation (80 dps, Proton Pin) ===")
        print(f"  Fock-space vs k*(Omega-k+1) max residual = {fmt(fock_max_resid, dps=10)}")
        print(
            f"  214Po / 212Po S_alpha ratio: Racah = {mp.nstr(ratio_214_212_racah, 6)} "
            f"vs empirical = {mp.nstr(ratio_214_212_emp, 6)} "
            f"(dex err = {mp.nstr(dex_ratio_214_212_racah, 5)}; uncorr = {mp.nstr(dex_ratio_214_212_uncorr, 5)})"
        )
        print(
            f"  212Po / 210Po S_alpha ratio: Racah = {mp.nstr(ratio_212_210_racah, 6)} "
            f"vs empirical = {mp.nstr(ratio_212_210_emp, 6)} "
            f"(dex err = {mp.nstr(dex_ratio_212_210_racah, 5)}; uncorr = {mp.nstr(dex_ratio_212_210_uncorr, 5)})"
        )
        for nuc in ("210Po", "212Po", "214Po", "222Rn", "226Ra", "238U"):
            nr = nuclide_results[nuc]
            print(
                f"\n  {nuc} (W_p={nr['W_p']}, W_n={nr['W_n']}, W_joint={nr['W_joint']}, "
                f"S_req={mp.nstr(mp.mpf(nr['S_alpha_required_WKB']), 5)}, "
                f"bare_dex={mp.nstr(mp.mpf(nr['dex_bare_WKB']), 5)}):"
            )
            for m_key, m_val in nr["models"].items():
                print(
                    f"    {m_key:<36} S={mp.nstr(mp.mpf(m_val['S_pred']), 5):<8} "
                    f"dex={mp.nstr(mp.mpf(m_val['dex_half_life_residual']), 5):>8} "
                    f"({'WORSE' if m_val['worse_than_bare_WKB'] else 'IMPROVED'})"
                )

        # Honest findings assertions (testing proved algebraic invariants & refutations)
        m2_beats_m0_open_po = int(
            abs(mp.mpf(nuclide_results["212Po"]["models"]["M2_per_subshell_opnorm_coherent"]["dex_half_life_residual"]))
            < abs(mp.mpf(nuclide_results["212Po"]["models"]["M0_literal_uncorrelated_MJ"]["dex_half_life_residual"]))
            and abs(mp.mpf(nuclide_results["214Po"]["models"]["M2_per_subshell_opnorm_coherent"]["dex_half_life_residual"]))
            < abs(mp.mpf(nuclide_results["214Po"]["models"]["M0_literal_uncorrelated_MJ"]["dex_half_life_residual"]))
        )
        # Honest record: on 214Po, bare WKB has |dex| = 0.1388 while M2 gives S = 40/81 = 0.4938
        # (+0.1676 dex), so M2 slightly overshoots bare WKB in |dex| on 214Po while cutting M0's +1.861 dex by 11x!
        m2_214po_overshoots_bare = int(
            bool(nuclide_results["214Po"]["models"]["M2_per_subshell_opnorm_coherent"]["worse_than_bare_WKB"])
        )
        # Barrier-blocked actinides/Rn/Ra worsen under EVERY admissible 0 < S < 1 model
        actinides_all_worsen_under_m2 = int(
            all(
                bool(nuclide_results[n]["models"]["M2_per_subshell_opnorm_coherent"]["worse_than_bare_WKB"])
                for n in ("222Rn", "226Ra", "238U")
            )
        )

        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "80-dps zero-fit evaluation of Racah seniority-0 coherent-pair alpha-cluster "
            "preformation W(k, Omega) = k*(Omega - k + 1) (Lean QOU.Nuclear.AlphaSeniorityPreformation) "
            "contrasting literal uncorrelated single-pair counting with seniority-0 pair coherence "
            "across 210Po (N=126 closed), open-shell 212Po and 214Po, and barrier-blocked heavy "
            "emitters (222Rn, 226Ra, 238U) under five pre-registered normalizations (Bean qou-q0gw)."
        )
        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("output_dps", OUT_DPS)
        wb.add_parameter("preregistration_commit", "9a66767a695")
        wb.add_parameter("source_witness", str(QI2JL_WITNESS.relative_to(_ROOT)))
        wb.add_data("fock_space_verification", {
            "max_residual_vs_closed_form": fmt(fock_max_resid, dps=OUT_DPS),
            "grid": fock_checks,
        })
        wb.add_data("scale_free_polonium_ratios", relative_ratios)
        wb.add_data("nuclide_evaluations", nuclide_results)
        wb.add_data("honest_summary", {
            "what_racah_coherence_resolves": (
                "Replaces the inverted 0.20x open-vs-closed ratio and flat 1.00x 214Po/212Po ratio "
                "of literal uncorrelated counting with W(214Po)/W(212Po) = 8/5 = 1.6000 (within "
                "-0.0066 dex of empirical 1.6245) and W(212Po)/W(210Po) = 5.0000 (77% of the log10 "
                "jump across N=126), reducing 212Po/214Po half-life errors from +1.65/+1.86 dex "
                "(M0) to +0.161/+0.168 dex (M2, S = 25/81 and 40/81)."
            ),
            "what_still_misses": (
                "1. Per-subshell normalization M2 fails on closed 210Po (S = 5/9, -1.002 dex) "
                "because a 2-state 3p_1/2 subshell has W_cap(1) = 1; normalizing against the "
                "Z>82, N>126 valence shell capacity W_cap(5)^2 = 81 (M3) gives S(210Po) = 5/81 "
                "= 0.0617 (-0.048 dex), leaving a -0.209 dex radial/shell-gap residual on the "
                "212Po/210Po jump. 2. On 214Po, M2/M3 give +0.168 dex vs -0.139 dex bare WKB "
                "(slightly worse in |dex| by 0.029 dex because S = 40/81 = 0.494 < S_req = 0.726). "
                "3. Deformed/heavy emitters 222Rn, 226Ra, 238U have S_req > 1 and worsen under "
                "every admissible 0 < S <= 1 preformation factor."
            ),
        })

        wb.add_assertion(
            "fock_space_exact_match_to_racah_formula",
            fmt(fock_max_resid, dps=15),
            "0",
            "1e-70",
            source="QOU.Nuclear.AlphaSeniorityPreformation.coherent_pair_overlap_sq_field",
        )
        wb.add_assertion(
            "open_shell_214Po_over_212Po_racah_ratio_within_0p02_dex",
            fmt(abs(dex_ratio_214_212_racah), dps=15),
            "0",
            "2e-2",
            source="W(2,5)/W(1,5) = 8/5 vs WKB S_req(214Po)/S_req(212Po)",
        )
        wb.add_assertion(
            "coherent_opnorm_M2_beats_literal_MJ_M0_on_open_shell_Po",
            m2_beats_m0_open_po,
            1,
            0,
            source="212Po and 214Po |dex| under M2 vs M0",
        )
        wb.add_assertion(
            "honest_negative_M2_slightly_overshoots_bare_WKB_on_214Po",
            m2_214po_overshoots_bare,
            1,
            0,
            source="S_M2(214Po) = 40/81 -> +0.1676 dex vs bare WKB -0.1388 dex",
        )
        wb.add_assertion(
            "barrier_blocked_actinides_worsen_under_admissible_seniority_S",
            actinides_all_worsen_under_m2,
            1,
            0,
            source="QOU.Nuclear.AlphaPreformationBound.preformation_cannot_close_of_lt",
        )
        wb.add_caveat(
            "Diagnostic zero-fit evaluation (pre-registered in PREREGISTRATION.md). T_exp is "
            "used solely at the comparison boundary; no normalization or shell occupancy was "
            "adjusted against half-life data."
        )
        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"\nwitness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())

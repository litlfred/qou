"""Yekutieli +0.5·h² observable hunt — does it appear elsewhere?

Task 3 of PR #1617 closed-route follow-ups, per audit
2026-06-01-closed-route-reexamination-roundup.md step (3):

The Yekutieli natural-reading +0.5 (probe 2026-06-01) is an EXACT
rational from H_4 partition combinatorics:
  (1/4) · Σ_classes (κ_λ + κ_λ^T)/2 = 2/4 = 1/2

It does NOT contribute to m_p closure (the proton's linking_weight
needs −G·h², not +0.5·h²). But +0.5·h² is a clean categorical
quantity at H_4 — it SHOULD contribute to SOME physical observable.

This probe scans candidate observables to see if +0.5·h² appears
naturally in any of:

  - m_He / m_d / m_T linking_weights (need ≥ H_4 = 4 nucleons)
  - Deuteron binding-energy residual
  - 4-strand braid Markov-trace identities
  - Multi-nucleon interface operator coefficients

## Method

For each candidate observable O at q_0, compute its residual after
subtracting the leading H_3 contribution (which is the Borromean
Markov-trace), divided by h². If +0.5 emerges at h² order, the
candidate is a Yekutieli-extension observable.

## Cross-references

- merged PR #1581 (yekutieli_natural_reading_precision_floor_check)
- audit 2026-06-01-closed-route-reexamination-roundup.md §3
- audit 2026-05-23-yekutieli-bijection-natural-reading-negative.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import M_D_MEV_VALIDATION, M_N_MEV_VALIDATION, M_P_MEV_VALIDATION, M_T_MEV_VALIDATION  # noqa: E402 (codata sweep)
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def qint(k, q):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def qfact(k, q):
    out = mp.mpf(1)
    for i in range(1, k + 1):
        out *= qint(i, q)
    return out


def main() -> int:
    set_compute_dps(60)
    q = Q_MP

    print("=" * 78)
    print("Yekutieli +0.5·h² observable hunt (60 dps)")
    print("=" * 78)
    print(f"\nq_0 = {Q_50_DIGIT_STR}\n")

    h = q - 1 / q
    h2 = h * h

    # CODATA-anchored mass ratios (proton + 4He + deuteron + tritium)
    m_e_MeV = mp.mpf("0.51099895069")
    m_p_MeV = mp.mpf(M_P_MEV_VALIDATION)
    m_n_MeV = mp.mpf(M_N_MEV_VALIDATION)
    m_d_MeV = mp.mpf(M_D_MEV_VALIDATION)   # deuteron
    m_T_MeV = mp.mpf(M_T_MEV_VALIDATION)   # tritium
    m_He3_MeV = mp.mpf("2808.39160743") # ³He
    m_He4_MeV = mp.mpf("3727.37941")    # ⁴He

    # Binding energies (Δm = atomic_mass − Σ_constituents)
    B_d = (m_p_MeV + m_n_MeV) - m_d_MeV
    B_T = (m_p_MeV + 2 * m_n_MeV) - m_T_MeV
    B_He3 = (2 * m_p_MeV + m_n_MeV) - m_He3_MeV
    B_He4 = (2 * m_p_MeV + 2 * m_n_MeV) - m_He4_MeV

    print(f"[Binding energies (CODATA)]")
    print(f"  B(d) = {mp.nstr(B_d, 12)} MeV")
    print(f"  B(T) = {mp.nstr(B_T, 12)} MeV")
    print(f"  B(³He) = {mp.nstr(B_He3, 12)} MeV")
    print(f"  B(⁴He) = {mp.nstr(B_He4, 12)} MeV")

    # The Yekutieli H_4 quantity:
    # κ_(4) = 0, κ_(3,1) = 1, κ_(2,2) = 1, κ_(2,1,1) = 1, κ_(1,1,1,1) = 0
    # Family A: (1/4) Σ_λ dim_q V_λ → h² coefficient = +3/4
    # Yekutieli natural reading: (1/4) Σ_classes (κ_λ + κ_λ^T)/2 = 1/2
    yekutieli_value = mp.mpf("0.5")
    family_a_value = mp.mpf("0.75")

    # H_4 = 24 (|S_4|), q-deformed [4]_q! at q_0
    dim_H_4 = mp.mpf(24)
    qfact_4 = qfact(4, q)

    print(f"\n[Yekutieli H_4 quantities]")
    print(f"  +0.5 (natural reading)  | structurally: (1/4)·Σ(κ_λ+κ_λT)/2")
    print(f"  +3/4 (Family A)         | structurally: (1/4)·Σ dim_q V_λ at h²")
    print(f"  dim H_4 = 24            | |S_4|")
    print(f"  [4]_q! at q_0           = {mp.nstr(qfact_4, 12)}")

    # Candidate observables
    # For each, compute residual / m_e (dimensionless), then test against
    # the +0.5·h² prediction.
    candidates = []

    # 1. Deuteron binding energy / m_e
    B_d_ratio = B_d / m_e_MeV
    candidates.append(("B(d) / m_e", B_d_ratio, "deuteron binding ÷ electron"))

    # 2. ⁴He binding energy / m_e
    B_He4_ratio = B_He4 / m_e_MeV
    candidates.append(("B(⁴He) / m_e", B_He4_ratio, "⁴He binding ÷ electron"))

    # 3. ⁴He / ³He binding ratio
    candidates.append(("B(⁴He) / B(³He)", B_He4 / B_He3, "binding ratio"))

    # 4. (B(⁴He) − 4·B(d)) / m_e — multi-nucleon residual
    candidates.append(("[B(⁴He) − 4·B(d)] / m_e",
                       (B_He4 - 4 * B_d) / m_e_MeV,
                       "multi-nucleon non-additive residual"))

    # 5. T/³He mirror residual
    candidates.append(("(B(T) − B(³He)) / m_e",
                       (B_T - B_He3) / m_e_MeV,
                       "isospin mirror residual"))

    # Now test each candidate's residual at h² order
    # The hypothesis: residual = leading + 0.5·h²·m_e at some normalization
    print(f"\n[Candidate observables — does +0.5·h² appear?]")
    for name, val, desc in candidates:
        # Take the residual modulo various leading terms
        leading_candidates = [
            ("0", mp.mpf(0)),
            ("integer floor", mp.floor(val)),
            ("3/4·integer", mp.mpf("0.75") * mp.floor(val)),
        ]
        for ld_name, ld_val in leading_candidates:
            residual = val - ld_val
            h2_coef = residual / h2
            rel_to_half = (h2_coef - mp.mpf("0.5")) / mp.mpf("0.5") * 100
            if abs(h2_coef) < mp.mpf(10) and abs(rel_to_half) < mp.mpf(10):
                marker = "  ⭐⭐ matches +0.5 within 10%"
                if abs(rel_to_half) < mp.mpf("1"):
                    marker = "  ⭐⭐⭐ MATCHES +0.5 within 1%"
                print(f"  {desc}")
                print(f"    {name:<28} = {mp.nstr(val, 12)}")
                print(f"    leading      = {ld_name}")
                print(f"    h² coef      = {mp.nstr(h2_coef, 8)} (vs +0.5)")
                print(f"    Δ%           = {mp.nstr(rel_to_half, 6)}{marker}")

    # Alternative: scan a wide range of normalizations (val / Z·h²)
    # Looking for Z such that val/(Z·h²) ≈ 0.5
    print(f"\n[Wide-net scan — for each observable, find normalization Z]")
    print(f"  Such that observable / (Z · h²) ≈ +0.5")
    print(f"  Test Z ∈ {{small integers, m_e, [k]_q, q-factorials}}")
    z_basis = [
        ("1", mp.mpf(1)),
        ("2", mp.mpf(2)),
        ("4", mp.mpf(4)),
        ("8", mp.mpf(8)),
        ("[2]_q", q + 1 / q),
        ("[3]_q", qint(3, q)),
        ("[4]_q", qint(4, q)),
        ("[3]_q!", qfact(3, q)),
        ("[4]_q!", qfact(4, q)),
        ("dim H_4 = 24", mp.mpf(24)),
        ("dim H_3 = 6", mp.mpf(6)),
        ("h", h),
        ("m_p/m_e", m_p_MeV / m_e_MeV),
    ]

    matches = []
    pairs_scored = 0          # a NULL verdict is only as strong as its coverage
    pairs_failed = []
    for obs_name, obs_val, desc in candidates:
        for z_name, z_val in z_basis:
            try:
                coef = obs_val / (z_val * h2)
                rel = (coef - mp.mpf("0.5")) / mp.mpf("0.5") * 100
                pairs_scored += 1
                if abs(rel) < mp.mpf("0.5"):
                    matches.append((desc, obs_name, z_name,
                                    mp.nstr(coef, 10), mp.nstr(rel, 4)))
            except Exception as exc:
                # Was a bare `except Exception: pass`. A pair that blew up
                # simply did not appear, and the run still reported NULL over
                # "5 obs × 13 normalizers" — a coverage claim it no longer had.
                pairs_failed.append(f"{obs_name} / {z_name}: {type(exc).__name__}")

    if matches:
        print(f"\n  ⭐ Within 0.5% matches:")
        for desc, obs, z, coef, rel in matches:
            print(f"    {obs} / ({z} · h²) = {coef} (Δ% = {rel}) — {desc}")
    else:
        print(f"\n  NULL — no observable normalizes to +0.5 within 0.5% under "
              f"{len(z_basis)} natural normalizers.")

    # Verdict
    print(f"\n[Verdict]")
    if matches:
        verdict = (
            f"OBSERVABLE FOUND: {len(matches)} natural normalization(s) bring "
            f"a candidate observable to coefficient +0.5 at h² order. The "
            f"Yekutieli H_4 partition-combinatoric quantity may have a "
            f"physical home."
        )
    else:
        verdict = (
            f"NULL — none of {len(candidates)} candidate observables "
            f"(deuteron/⁴He/³He/T binding, multi-nucleon residuals, "
            f"isospin mirrors) normalizes to +0.5·h² under {len(z_basis)} "
            f"natural normalizers. The Yekutieli +0.5 may be a STRUCTURAL "
            f"quantity without a corresponding L2 observable — common for "
            f"partition-combinatoric quantities."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "yekutieli-half-h2-observable-hunt",
        engine="python",
    )
    w.set_description(
        "Task 3 of PR #1617: search for physical observables that exhibit "
        "+0.5·h² (the Yekutieli natural-reading H_4 partition quantity) at "
        "their h² coefficient. Tests deuteron/⁴He/³He/tritium binding "
        "energies, multi-nucleon non-additive residuals, isospin mirror "
        "residuals under various natural normalizations."
    )
    w.add_parameter("q_60dps", Q_50_DIGIT_STR)
    w.add_data("matches_count", len(matches))
    w.add_data("candidates_count", len(candidates))
    w.add_data("normalizers_count", len(z_basis))
    w.add_data("verdict", verdict)

    # ── Was `observable_hunt_completed`, computed=True / expected=True ───
    # Its own source line ("Scanned 5 obs × 13 normalizers") was the coverage
    # claim; the True/True pair carried none of it, and a run that scored
    # zero pairs produced the same True. Replaced by the three things that
    # decide whether this NULL means anything.

    # (1) The inputs. Route A: the binding energies this file builds as a
    #     mass defect, Σ m_constituents − m_nucleus, from the CODATA-2022
    #     nuclear masses. Route B: ame_binding_mev(Z, A), AME2020's own
    #     quoted binding-energy-per-nucleon × A — a different table, not a
    #     rearrangement of the first. Every candidate observable below is a
    #     ratio of these four numbers, so if they are wrong the NULL is
    #     meaningless. Bound 1e-4 MeV: d and T agree to <5e-7, ³He and ⁴He to
    #     ~5e-5 because their masses are hand-typed here at 5–6 dp (see the
    #     caveat). Swapping a proton for a neutron moves B by 1.29 MeV.
    from codata_constants import ame_binding_mev  # noqa: E402
    ame_rows = [("d", 1, 2, B_d), ("T", 1, 3, B_T),
                ("3He", 2, 3, B_He3), ("4He", 2, 4, B_He4)]
    ame_agree = sum(1 for _n, Z, A, B in ame_rows
                    if abs(B - ame_binding_mev(Z, A)) < mp.mpf("1e-4"))
    w.add_data("binding_vs_ame2020", {
        n: {"mass_defect_MeV": mp.nstr(B, 14),
            "ame2020_MeV": mp.nstr(ame_binding_mev(Z, A), 14),
            "abs_gap_MeV": mp.nstr(abs(B - ame_binding_mev(Z, A)), 4)}
        for n, Z, A, B in ame_rows})
    w.add_assertion(
        name="binding_energies_match_ame2020_table",
        computed=str(ame_agree),
        expected=str(len(ame_rows)),
        tolerance=0,
        unit="nuclides agreeing to <1e-4 MeV",
        source=("Route A: Σ m_constituents − m_nucleus from CODATA-2022 nuclear "
                "masses, as computed here. Route B: ame_binding_mev(Z, A), the "
                "AME2020 quoted binding-energy-per-nucleon × A. Expected = the "
                "nuclide list rebuilt from the rows the scan actually uses."),
    )

    # (2) Coverage of the NULL. Route A: pairs that produced a coefficient
    #     inside the loop. Route B: len(candidates) × len(z_basis), rebuilt
    #     from the two declaration lists. Before this, the bare `except`
    #     could drop a pair and the NULL would read the same.
    w.add_data("pairs_scored", pairs_scored)
    w.add_data("pairs_failed", pairs_failed)
    w.add_assertion(
        name="scan_scored_every_observable_normalizer_pair",
        computed=str(pairs_scored),
        expected=str(len(candidates) * len(z_basis)),
        tolerance=0,
        unit="(observable, normalizer) pairs",
        source=("Route A: the pair counter incremented only after the "
                "coefficient is computed. Route B: len(candidates) × "
                "len(z_basis) rebuilt from the input lists. The NULL below is "
                "only worth its coverage, so these must agree."),
    )

    # (3) The verdict itself. Route A: this run's match list at the 0.5%
    #     gate. Route B: the NULL recorded in audit
    #     2026-06-01-closed-route-reexamination-roundup.md §3, which is what
    #     this probe was opened to confirm. A later normalizer or observable
    #     that does land on +0.5 flips this red instead of quietly rewriting
    #     the verdict string.
    w.add_assertion(
        name="no_observable_normalizes_to_half_h2_within_0p5pct",
        computed=str(len(matches)),
        expected="0",
        tolerance=0,
        unit="observable/normalizer pairs within 0.5% of +0.5",
        source=("Route A: the 0.5%-gate match list from this run's scan. "
                "Route B: the NULL recorded in audit 2026-06-01 §3 (Task 3 of "
                "PR #1617). Falsifiable in the direction that matters: a new "
                "hit fails it."),
    )
    w.add_caveat(
        "m_He3_MeV and m_He4_MeV are hand-typed here at 5–6 dp rather than "
        "read from the CODATA/AME registry, which is why B(³He) and B(⁴He) sit "
        "~5e-5 MeV from AME2020 while B(d) and B(T) — built from registry "
        "masses — agree to <5e-7 MeV. Recorded, not repaired; the "
        "binding_energies_match_ame2020_table bound is set wide enough to "
        "carry it and tight enough to catch a real error."
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

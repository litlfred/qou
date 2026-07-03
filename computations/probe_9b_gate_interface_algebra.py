#!/usr/bin/env python3
"""PROBE 1-c (step-9b follow-up, bean cywi) — derive-or-refute the [Z>N]
proton-excess gate of model M3 from the Phase-5q interface algebra.

EXPLORATORY PROBE — derive-or-refute; NOT wired to production; introduces
NO new constants (every quantity below is read off the Phase-5q closed
form's own structural constants + vendored AME2020 data; nothing fitted).

Context. probe_9b_h_power_asymmetry.py found that model
    M3:  log_q₀Δ_λ = −log_q₀h·(2A−1)/3 + κ·[Z>N],
    κ  = log_q₀(tr_n/tr_p) = −1.3718  (derived, Phase-5l traces)
collapses the ³He outlier +1.40 → +0.033. Open question: is the
one-sided [Z>N] gate a DERIVED consequence of the closed form
tr_M(𝓑_K) = tr_p^Z·tr_n^N·∏f_i, or an A=3 numerical coincidence?

METHOD (50-dps mpmath per qou_substrate.precision; exact identities
checked to ≤1e-30):

  1. EXACT mirror decomposition. For a mirror pair (Z,N) vs (N,Z),
     Z<N, with the chain census (Z−1)·pp + 1·pn + (N−1)·nn:
       log_q₀Δ_λ(n-rich) − log_q₀Δ_λ(p-rich) = asym + swap + mirror,
       asym   = −κ = (N−Z)·log_q₀(tr_p/tr_n)        [trace side]
       swap   = log_q₀[(1−P_pr)/(1−P_nr)],           [interface side]
                P_(Z,N) = f_pp^(Z−1)·f_pn·f_nn^(N−1)
       mirror = log_q₀[B_AME(n-rich)/B_AME(p-rich)]  [experimental side]
     This is an algebraic identity of the Δ_λ definition (asserted).
     Sign reconciliation of the PROBE-1 "0.06 gap": the ³He law-residual
     (+1.404) minus the T law-residual (+0.066) IS the mirror gap
     (1.338) exactly, because both A=3 isobars share the law value 25 —
     the "missing term" is exactly T's own residual, not a δ/tr_free
     effect (asserted to 1e-30).

  2. WHAT THE GATE IS. M3 puts the whole mirror gap into asym, so
       gate exact ⟺ swap + mirror = 0,   and identically
       res_M3(p-rich) − res_M3(n-rich) = swap + mirror.
     At A=3: swap + mirror = −0.938014 + 0.904360 = −0.033654 — a
     NEAR-CANCELLATION with computable residual, NOT an identity
     (swap is interface algebra at q₀; mirror is AME data; no shared
     structure ties them).

  3. GENERALITY. (i) The candidate factorization "swap = log g_pp −
     log g_nn (A-independent)", g_x = 1−f_x, is FALSE: 1−∏f is not
     multiplicative over interfaces (naive ratio −3.344 vs actual
     −0.938 at A=3). (ii) Since every interface factor satisfies
     0 < f < 1 at q₀ (asserted), P_(Z,N) → 0 geometrically with A and
     swap → 0: −0.938 (A=3) → −0.117 (A=5) → −0.0167 (A=7). (iii) The
     AME mirror term does NOT decay: +0.904 (A=3), +0.438 (A=5),
     +0.410 (A=7, ⁷Li/⁷Be — both bound, clean AME test). Hence
     swap+mirror = −0.034 (A=3) but +0.320 (A=5) / +0.394 (A=7): the
     cancellation FAILS at every AME-testable mirror pair beyond A=3.

VERDICT (tiered per the (a)/(b) refutation discipline):
  - "[Z>N] gate is a derived generic rule of the interface algebra":
    REFUTED — scope (a) ONLY. The swap term is a derived, geometrically
    A-decaying property of the interface algebra, while the mirror term
    is experimental and stays O(0.4); their A=3 cancellation is not
    structural. This constrains the gate-as-rule reading only; it does
    NOT exclude the trace asymmetry κ from a larger closure (no proved
    invariant claimed; scope-(b) NOT claimed).
  - M3 at A=3 remains NEAR-MATCH with the exact stated residual
    swap+mirror = −0.03365 (= res_M3(³He) − res_M3(T), identity).

Caveats: A=5 mirror pair (⁵He/⁵Li) is particle-unstable — corroborating
only; A=7 (⁷Li/⁷Be) is the clean bound-pair test. A≥5 rows use the same
chain interface census that defines the Δ_λ baseline (internal
consistency; PROBE 3's many-body ceiling does not affect the swap-term
decay, which is a property of the interface factors alone).

Run:  python3 -u computations/probe_9b_gate_interface_algebra.py
Witness: probe-9b-gate-interface-algebra.witness.json (audit-only)

Ref: docs/audits/2026-07-02-9b-probes-laurent-degree-manybody.md
Ref: docs/audits/2026-06-09-delta-lambda-canonical-residual.md
Ref: computations/closed_form_tau_M.py (Phase 5q closed form)
Ref: computations/probe_9b_h_power_asymmetry.py (models M0–M3)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from closed_form_tau_M import canonical_interface_kinds  # noqa: E402
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402
from qou_substrate import Q_50_DIGIT_STR, WitnessBuilder  # noqa: E402
from qou_substrate.precision import COMPUTE_DPS  # noqa: E402
# Validation-only AME2020 binding energies (comparison targets, never
# prediction inputs). ⁷Be has no public module-level constant yet, so the
# vendored-AME accessor is used directly for the full mirror-pair set.
from substrate.codata_constants import _ame_binding_mev  # noqa: E402

mp.mp.dps = COMPUTE_DPS + 15

HERE = Path(__file__).resolve().parent
PROBE1_WITNESS = HERE / "probe-9b-laurent-degree-10a5.witness.json"
HPOWER_WITNESS = HERE / "probe-9b-h-power-asymmetry.witness.json"

IDENTITY_TOL = mp.mpf("1e-30")   # pure-arithmetic identities at 50 dps

# Mirror pairs (Z<N side): label_n_rich, label_p_rich, (Z,N), AME (Z,A) keys.
MIRROR_PAIRS = [
    ("T", "3He", (1, 2), ((1, 3), (2, 3)), "both bound (anchor pair)"),
    ("5He", "5Li", (2, 3), ((2, 5), (3, 5)),
     "both particle-unstable (resonances) — corroborating only"),
    ("7Li", "7Be", (3, 4), ((3, 7), (4, 7)), "both bound — clean AME test"),
]


def main() -> int:
    t0 = time.monotonic()
    q0 = mp.mpf(Q_50_DIGIT_STR)
    lnq = mp.log(q0)

    def logq(x):
        return mp.log(x) / lnq

    # Structural constants of the closed form (exact formulas at 50 dps).
    z = 1 / (mp.sqrt(q0) + 1 / mp.sqrt(q0))
    h = q0 - 1 / q0
    delta = flavor_split_leading(q0)
    f = {
        "positive": z,                                   # f_pp
        "negative": z - h,                               # f_nn
        "averaged": z - h * (mp.mpf(1) / 2 - delta / 4),  # f_pn (bring)
    }
    qb = mp.mpf(str(Q_NEUTRON_MEV))

    # Nucleon traces: 50-digit strings from the committed PROBE 1 witness
    # (computed there via the full symbolic canonical Jones–Markov trace).
    src = json.loads(PROBE1_WITNESS.read_text())
    nt = src["data"]["nucleon_traces"]
    ed = src["data"]["exponent_dictionary_q0_units"]
    tr_p = mp.mpf(nt["tr_p_at_q0"])
    tr_n = mp.mpf(nt["tr_n_at_q0"])
    kappa = logq(tr_n / tr_p)
    H = -mp.mpf(str(ed["log_q0_h"]))          # −log_q₀ h = 15.000206
    hp = json.loads(HPOWER_WITNESS.read_text())
    hp_res = {r["atom"]: r["residuals_model_minus_measured"]
              for r in hp["data"]["isotope_rows"]}

    w = WitnessBuilder("probe-9b-gate-interface-algebra",
                       engine="mpmath")
    w.set_audit_only(
        "docs/audits/2026-07-02-9b-probes-laurent-degree-manybody.md")
    w.add_parameter("compute_dps", mp.mp.dps)
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("Q_beta_n_MeV", float(Q_NEUTRON_MEV))
    w.add_parameter("kappa_log_q0_trn_over_trp", float(kappa))
    w.add_parameter("source_witnesses",
                    [PROBE1_WITNESS.name, HPOWER_WITNESS.name])
    w.add_parameter("pn_convention", "bring_color_weighted (proven leading δ)")

    # Cross-check recomputed constants vs the PROBE 1 dictionary floats.
    w.add_assertion(
        name="structural_constants_match_probe1",
        computed=float(max(
            abs(float(logq(f["positive"])) - ed["log_q0_f_pp"]),
            abs(float(logq(f["averaged"])) - ed["log_q0_f_pn"]),
            abs(float(logq(f["negative"])) - ed["log_q0_f_nn"]),
            abs(float(kappa) - ed["log_q0_tr_n_over_tr_p"]))),
        expected=0.0, tolerance=1e-9,
        source="f_pp/f_pn/f_nn and κ recomputed from exact formulas at "
               "50 dps vs the committed PROBE 1 exponent dictionary",
    )

    # 0 < f < 1 at q₀ — the invariant behind the geometric swap decay.
    w.add_assertion(
        name="interface_factors_in_unit_interval",
        computed=1.0 if all(0 < v < 1 for v in f.values()) else 0.0,
        expected=1.0, tolerance=0.0,
        source="all three interface factors lie in (0,1) at q₀ "
               "(f_pp≈0.499, f_pn≈0.395, f_nn≈0.290), so the interface "
               "product P_(Z,N) decays geometrically with A and the swap "
               "term → 0",
    )

    def prod_f(Z: int, N: int) -> mp.mpf:
        P = mp.mpf(1)
        for k in canonical_interface_kinds(Z, N):
            P *= f[k]
        return P

    def log_delta_lambda(Z: int, N: int, B: mp.mpf) -> mp.mpf:
        trf = tr_p ** Z * tr_n ** N
        return logq(B / (qb * trf * (1 - prod_f(Z, N))))

    # ── Mirror decomposition table (A = 3, 5, 7) ────────────────────
    print("── mirror decomposition: gap = asym + swap + mirror (q₀-units) ──")
    print(f"  {'pair':>9} {'A':>2} {'asym':>8} {'swap':>9} {'mirror':>8} "
          f"{'swap+mirror':>12} {'gap':>9}")
    table = []
    by_A = {}
    for nr, pr, (Z, N), ((Zn, An), (Zp, Ap)), note in MIRROR_PAIRS:
        A = Z + N
        B_nr = _ame_binding_mev(Zn, An)
        B_pr = _ame_binding_mev(Zp, Ap)
        asym = -kappa * (N - Z)
        swap = logq((1 - prod_f(N, Z)) / (1 - prod_f(Z, N)))
        mirror = logq(B_nr / B_pr)
        gap = log_delta_lambda(Z, N, B_nr) - log_delta_lambda(N, Z, B_pr)
        row = {
            "pair": f"{nr}/{pr}", "A": A, "Z_n_rich": Z, "N_n_rich": N,
            "census_n_rich": canonical_interface_kinds(Z, N),
            "census_p_rich": canonical_interface_kinds(N, Z),
            "B_AME_n_rich_MeV": mp.nstr(B_nr, 12),
            "B_AME_p_rich_MeV": mp.nstr(B_pr, 12),
            "asym": float(asym), "swap": float(swap),
            "mirror": float(mirror),
            "swap_plus_mirror": float(swap + mirror),
            "gap_log_Delta_n_rich_minus_p_rich": float(gap),
            "decomposition_identity_residual": float(
                abs(gap - (asym + swap + mirror))),
            "note": note,
        }
        table.append(row)
        by_A[A] = row
        print(f"  {row['pair']:>9} {A:>2} {float(asym):>8.4f} "
              f"{float(swap):>9.4f} {float(mirror):>8.4f} "
              f"{float(swap + mirror):>12.4f} {float(gap):>9.4f}")
    w.add_data("mirror_decomposition_table", table)

    # 1. The decomposition is an exact identity (T/³He anchor pair).
    w.add_assertion(
        name="decomposition_identity_T_3He",
        computed=table[0]["decomposition_identity_residual"],
        expected=0.0, tolerance=float(IDENTITY_TOL),
        source="gap(T−³He) computed directly from Δ_λ equals "
               "asym + swap + mirror — algebraic identity of the "
               "closed-form Δ_λ definition, checked at 50 dps",
    )

    # 1b. Reconcile PROBE 1's "0.06 gap": law-residual difference of the
    # A=3 isobars IS the mirror gap; the missing term is T's own residual.
    B_T = _ame_binding_mev(1, 3)
    B_3He = _ame_binding_mev(2, 3)
    lT = log_delta_lambda(1, 2, B_T)
    l3 = log_delta_lambda(2, 1, B_3He)
    res_M0 = {"T": 25 - lT, "3He": 25 - l3}   # law 10A−5 = 25 at A=3
    recon = abs((res_M0["3He"] - res_M0["T"])
                - (lT - l3))
    w.add_assertion(
        name="outlier_reconciliation_exact",
        computed=float(recon), expected=0.0, tolerance=float(IDENTITY_TOL),
        source="res_M0(³He) − res_M0(T) = mirror gap EXACTLY (isobars "
               "share the law value 25): the PROBE-1 '1.404 vs 1.338' "
               "0.066 discrepancy is precisely T's own law residual — "
               "no missing δ/tr_free term",
    )
    print(f"  reconciliation: res_M0(³He) {float(res_M0['3He']):+.4f} = "
          f"res_M0(T) {float(res_M0['T']):+.4f} + gap "
          f"{float(lT - l3):+.4f}  (identity, residual {float(recon):.1e})")

    # 2. What the gate IS: res_M3(³He) − res_M3(T) = swap + mirror.
    res_M3_T = H * 5 / 3 - lT
    res_M3_3 = H * 5 / 3 + kappa - l3
    sm3 = mp.mpf(str(table[0]["swap"])) + mp.mpf(str(table[0]["mirror"]))
    # exact mp version:
    sm3_exact = (logq((1 - prod_f(2, 1)) / (1 - prod_f(1, 2)))
                 + logq(B_T / B_3He))
    w.add_assertion(
        name="gate_residual_identity",
        computed=float(abs((res_M3_3 - res_M3_T) - sm3_exact)),
        expected=0.0, tolerance=float(IDENTITY_TOL),
        source="res_M3(³He) − res_M3(T) = swap + mirror identically: "
               "M3 puts the whole mirror gap into the trace asymmetry, "
               "so 'gate exact' ⟺ 'swap + mirror = 0'",
    )
    w.add_assertion(
        name="gate_near_cancellation_A3",
        computed=float(sm3_exact), expected=-0.033654, tolerance=1e-4,
        source="A=3 swap+mirror = −0.938014 + 0.904360 = −0.033654: a "
               "near-cancellation with computable residual, NOT an "
               "identity (swap = interface algebra at q₀; mirror = AME "
               "data; no shared structure)",
    )
    # Consistency with the committed h-power witness residuals.
    w.add_assertion(
        name="m3_residuals_match_hpower_witness",
        computed=float(max(
            abs(float(res_M3_T)
                - hp_res["T"]["M3_proton_excess_gate"]),
            abs(float(res_M3_3)
                - hp_res["3He"]["M3_proton_excess_gate"]))),
        expected=0.0, tolerance=1e-9,
        source="M3 residuals recomputed here (T +0.0665, ³He +0.0329) vs "
               "the committed probe-9b-h-power-asymmetry witness",
    )
    print(f"  gate: res_M3(³He) − res_M3(T) = swap+mirror = "
          f"{float(sm3_exact):+.6f}")

    # 3(i). The naive A-independent factorization swap = log g_pp − log g_nn
    # is FALSE (1−∏f is not multiplicative over interfaces).
    g_ratio = logq((1 - f["positive"]) / (1 - f["negative"]))
    w.add_assertion(
        name="swap_not_naive_g_ratio",
        computed=float(abs(mp.mpf(str(table[0]["swap"])) - g_ratio)),
        expected=2.406147, tolerance=1e-3,
        source="candidate 'swap = log g_pp − log g_nn = −3.344 "
               "(A-independent)' REFUTED: actual A=3 swap is −0.938; "
               "1−∏f does not factor over interfaces, so the swap term "
               "is A-dependent",
    )

    # 3(ii). Swap decays geometrically with A (derived: 0 < f < 1).
    w.add_assertion(
        name="swap_decays_with_A",
        computed=float(abs(mp.mpf(str(by_A[7]["swap"])))),
        expected=0.0, tolerance=0.02,
        source="|swap| shrinks −0.938 (A=3) → −0.117 (A=5) → −0.0167 "
               "(A=7): geometric decay of the interface product, a "
               "DERIVED property of the closed form (all f ∈ (0,1) at q₀)",
    )

    # 3(iii). The cancellation fails at the clean A=7 AME pair.
    w.add_assertion(
        name="cancellation_fails_A7",
        computed=float(by_A[7]["swap_plus_mirror"]),
        expected=0.3935, tolerance=0.005,
        source="⁷Li/⁷Be (both bound, vendored AME2020): swap+mirror = "
               "−0.0167 + 0.4102 = +0.394 — an order of magnitude above "
               "the A=3 residual −0.0337; the near-cancellation behind "
               "the [Z>N] gate is A=3-specific, not generic",
    )

    # ── Verdict ─────────────────────────────────────────────────────
    verdict = {
        "question": "is the [Z>N] proton-excess gate of M3 a derived "
                    "consequence of the Phase-5q interface algebra, or an "
                    "A=3 coincidence?",
        "gate_statement": "gate exact ⟺ swap + mirror = 0, where swap is "
                          "the interface-sign-swap term (closed form) and "
                          "mirror is the AME mirror-binding ratio "
                          "(experimental); identically res_M3(p-rich) − "
                          "res_M3(n-rich) = −(swap + mirror)",
        "tier": "REFUTED as a generic derived rule — scope (a) ONLY; "
                "NEAR-MATCH retained at A=3 with exact stated residual",
        "scope_a_statement": (
            "The interface algebra, ALONE, does not derive the [Z>N] "
            "gate: the swap term it supplies decays geometrically with A "
            "(−0.938 → −0.117 → −0.0167 at A=3/5/7; derived from "
            "0 < f < 1 at q₀), while the AME mirror term it must cancel "
            "stays O(0.4) (+0.904 / +0.438 / +0.410). The A=3 "
            "cancellation (residual −0.0337) is a numerical coincidence "
            "of that one pair; at ⁷Li/⁷Be the same combination is +0.394. "
            "This constrains the gate-as-rule reading only — it does NOT "
            "exclude the trace asymmetry κ from a larger closure, and "
            "the A=3 near-match stands with its residual stated (no "
            "proved invariant; scope-(b) NOT claimed)."
        ),
        "A3_status": "M3 remains NEAR-MATCH at A=3: residuals D +0.011 / "
                     "T +0.067 / ³He +0.033 / ⁴He −0.272; the ³He "
                     "collapse works exactly because swap+mirror = "
                     "−0.0337 ≈ 0 there",
        "caveats": [
            "A=5 pair (⁵He/⁵Li) is particle-unstable — corroborating only; "
            "A=7 (⁷Li/⁷Be) is the clean bound-pair test",
            "A≥5 rows use the same chain interface census that defines "
            "the Δ_λ baseline (internal-consistency test; the PROBE-3 "
            "many-body ceiling does not affect the swap-term decay, "
            "which is a property of the interface factors alone)",
        ],
    }
    w.add_data("verdict", verdict)
    w.set_description(
        "PROBE 1-c (9b, bean cywi): derive-or-refute the [Z>N] "
        "proton-excess gate of model M3 from the Phase-5q interface "
        "algebra. Exact mirror decomposition gap = asym + swap + mirror "
        "(identity ≤1e-30); gate exact ⟺ swap+mirror = 0. At A=3 the "
        "cancellation holds to −0.0337 (= res_M3(³He) − res_M3(T), "
        "identity), but the swap term decays geometrically with A "
        "(derived: all f ∈ (0,1) at q₀) while the AME mirror term stays "
        "O(0.4): at ⁷Li/⁷Be swap+mirror = +0.394. VERDICT: gate-as-"
        "derived-rule REFUTED scope-(a); A=3 near-match retained with "
        "stated residual. Exploratory; NOT wired; no new constants.")
    out = w.save()
    print(f"\nVerdict: {verdict['tier']}")
    print(f"Witness: {out}  [{time.monotonic() - t0:.1f}s]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

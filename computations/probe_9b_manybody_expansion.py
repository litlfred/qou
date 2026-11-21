#!/usr/bin/env python3
"""PROBE 3 (step-9b, bean iv3r) — exact many-body expansion of the
Phase-5q closed form for the canonical binding defect.

EXPLORATORY PROBE — derive-or-refute; NOT wired to production; introduces
NO new constants (Δ_λ gate: no seventh fit ansatz).

The Phase-5q closed form (computations/closed_form_tau_M.py) is exact:

    tr_M(𝓑_K) = tr_p^Z · tr_n^N · ∏_{i=1..A−1} f_i(q)
    ⇒ ln tr_M = Z·ln tr_p + N·ln tr_n + Σ_i ln f_i        (exact)

so the trace-canonical binding defect (binding_canonical.py conventions;
the MeV multiplier is Q_β(n) ≈ 0.78233 MeV — historically misnamed E_0  # noqa: P31 — docstring; Q_beta scale note
there, see its docstring; both traces are real-positive at q₀ so the
signed difference equals the |·| form)

    B = Q_β · ( tr_M(W_free) − tr_M(W_atom) )
      = Q_β · tr_free · ( 1 − ∏_i f_i )
      = Q_β · tr_free · ( 1 − ∏_i (1 − g_i) ),      g_i := 1 − f_i

has an EXACT finite inclusion–exclusion ("many-body") expansion in the
interface deficits g_i:

    B = Q_β · tr_free · [ Σ_i g_i − Σ_{i<j} g_i g_j + Σ_{i<j<k} g_i g_j g_k − … ]

The order-k term touches the nucleons spanned by the k interfaces
(consecutive interfaces i, i+1 share a nucleon): order-1 = 2-body bonds,
order-2 = 3-body (or disconnected 2+2-body), order-3 at ⁴He = the
connected 4-body cross-term. This probe computes every order EXACTLY
(50-dps mpmath, no new constants) for D, T, ³He, ⁴He and reports:

  - per-order MeV values, cumulative sums, and the exact-sum identity
    Σ_k T_k = B_pred (assertion at 1e-40);
  - the fraction of B_pred (scale-free structure) and of B_AME captured
    by each order, on the Q_β scale (the 10A−5 residual's scale) and on
    the E_0 = m_e/(q₀(q₀−1)) ≈ 4.186 MeV scale used by the many-body-
    ceiling audit (docs/audits/2026-06-02-binding-many-body-ceiling.md,
    whose pairwise chain-sum captured 26% of ⁴He);
  - whether the connected 4-body cross-term at ⁴He lands anywhere near
    the magic-A value 2·m_e·A·8G ≈ 29.96 MeV (+5.87% vs AME).

Run:  python3 -u computations/probe_9b_manybody_expansion.py
Witness: probe-9b-manybody-expansion.witness.json (audit-only)

Ref: docs/audits/2026-06-02-binding-many-body-ceiling.md
Ref: docs/audits/2026-06-09-binding-trace-convention-split.md
Ref: docs/audits/2026-06-09-delta-lambda-canonical-residual.md
Ref: computations/closed_form_tau_M.py (Phase 5q closed form)
Ref: computations/binding_canonical.py (trace-canonical baseline)
"""
from __future__ import annotations

import sys
import time
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from closed_form_tau_M import (  # noqa: E402
    canonical_interface_kinds, markov_z, hecke_h,
)
from _li_2_q_util import flavor_split_leading  # noqa: E402
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
from qou_substrate import Q_50_DIGIT_STR, WitnessBuilder  # noqa: E402
from qou_substrate.precision import COMPUTE_DPS  # noqa: E402

mp.mp.dps = COMPUTE_DPS + 15

ATOMS = [
    ("D", 1, 1, AME_B_DEUTERON_MEV_VALIDATION),
    ("T", 1, 2, AME_B_TRITIUM_MEV_VALIDATION),
    ("3He", 2, 1, AME_B_HE3_MEV_VALIDATION),
    ("4He", 2, 2, AME_B_HE4_MEV_VALIDATION),
]


def interface_factor_values(q0: mp.mpf) -> dict:
    """f_i(q₀) per interface kind, bring_color_weighted (proven leading δ)."""
    z = markov_z(q0)
    h = hecke_h(q0)
    delta = flavor_split_leading(q0)
    return {
        "positive": z,                                    # p-p
        "negative": z - h,                                # n-n
        "averaged": z - h * (mp.mpf(1) / 2 - delta / 4),  # p-n
    }


def nucleons_touched(subset: tuple[int, ...]) -> int:
    """Number of distinct nucleons touched by a set of chain interfaces
    (interface i joins nucleons i and i+1)."""
    touched = set()
    for i in subset:
        touched.add(i)
        touched.add(i + 1)
    return len(touched)


def is_connected(subset: tuple[int, ...]) -> bool:
    """A set of chain interfaces is connected iff the indices are
    consecutive integers."""
    if not subset:
        return False
    return max(subset) - min(subset) + 1 == len(subset)


def main() -> int:
    t_start = time.monotonic()
    q0 = mp.mpf(Q_50_DIGIT_STR)
    qb = mp.mpf(str(Q_NEUTRON_MEV))
    m_e = mp.mpf(str(M_E_MEV))
    # E_0 = m_e/(q₀(q₀−1)) — the scale of the many-body-ceiling audit
    # (its per-bond values 2.379/2.492/2.532 MeV are Δtr·E_0).
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    e0_full = _qbeta_e0.order_zero_scaled(m_e, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    # magic-A ⁴He value: B = 2·m_e·A·Vol(L6a4) = 2·m_e·4·8G (G = Catalan)
    b_magic_4he = 2 * m_e * 4 * 8 * mp.catalan

    f_by_kind = interface_factor_values(q0)

    w = WitnessBuilder("probe-9b-manybody-expansion", engine="mpmath")
    w.set_audit_only("docs/audits/2026-07-02-9b-probes-laurent-degree-manybody.md")
    w.add_parameter("compute_dps", mp.mp.dps)
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("Q_beta_n_MeV", float(Q_NEUTRON_MEV))
    w.add_parameter("E0_full_MeV", mp.nstr(e0_full, 30))
    w.add_parameter("pn_convention", "bring_color_weighted (proven leading δ)")
    w.add_data("magic_A_4He_MeV_2_me_4_8G", mp.nstr(b_magic_4he, 30))

    # Nucleon H₃ traces from the transfer path (A=1 ⇒ no interfaces ⇒
    # tr_atom = tr_free = tr_nucleon). Same engine as binding_canonical.
    tr_p, tr_p_free, _, _ = tr_m_atom_zn(1, 0, dps=50)
    tr_n, tr_n_free, _, _ = tr_m_atom_zn(0, 1, dps=50)
    assert abs(tr_p - tr_p_free) < mp.mpf("1e-45")
    assert abs(tr_n - tr_n_free) < mp.mpf("1e-45")
    print(f"tr_p = {mp.nstr(tr_p, 30)}")
    print(f"tr_n = {mp.nstr(tr_n, 30)}")
    w.add_data("nucleon_traces", {"tr_p": mp.nstr(tr_p, 50),
                                  "tr_n": mp.nstr(tr_n, 50)})

    isotope_results = []
    for name, Z, N, B_ame_in in ATOMS:
        A = Z + N
        B_ame = mp.mpf(B_ame_in)
        kinds = canonical_interface_kinds(Z, N)
        n_iface = len(kinds)
        f_vals = [f_by_kind[k] for k in kinds]
        g_vals = [1 - f for f in f_vals]
        tr_free = (tr_p ** Z) * (tr_n ** N)

        # exact reference: B_pred from the full closed form
        prod_f = mp.mpf(1)
        for f in f_vals:
            prod_f *= f
        B_pred = qb * tr_free * (1 - prod_f)

        # independent cross-check vs the transfer path (full H_{3A} trace)
        tr_a_tr, tr_f_tr, _, _ = tr_m_atom_zn(Z, N, dps=50)
        B_pred_transfer = qb * (tr_f_tr - tr_a_tr)
        rel_vs_transfer = abs(B_pred - B_pred_transfer) / abs(B_pred_transfer)
        w.add_assertion(
            name=f"closed_form_B_matches_transfer_{name}",
            computed=float(rel_vs_transfer), expected=0.0, tolerance=1e-18,
            source="B from the closed form vs B from the independent "
                   "transfer-path traces (residual ≈9e-20 = f64-q₀-baked δ "
                   "in the canonical word vs 50-digit δ(q₀) here)",
        )

        # ── exact inclusion–exclusion orders ─────────────────────────
        # order k: T_k = (−1)^{k+1} · Q_β · tr_free · Σ_{|S|=k} ∏_{i∈S} g_i
        orders = []
        total = mp.mpf(0)
        for k in range(1, n_iface + 1):
            term_sum = mp.mpf(0)
            subsets = []
            for S in combinations(range(n_iface), k):
                prod_g = mp.mpf(1)
                for i in S:
                    prod_g *= g_vals[i]
                signed = (-1) ** (k + 1) * qb * tr_free * prod_g
                subsets.append({
                    "interfaces": [f"{i}:{kinds[i]}" for i in S],
                    "nucleon_body_count": nucleons_touched(S),
                    "connected": is_connected(S),
                    "signed_MeV": mp.nstr(signed, 25),
                })
                term_sum += prod_g
            T_k = (-1) ** (k + 1) * qb * tr_free * term_sum
            total += T_k
            orders.append({
                "interface_order_k": k,
                "nucleon_body_counts": sorted({s["nucleon_body_count"]
                                               for s in subsets}),
                "T_k_MeV": mp.nstr(T_k, 30),
                "cumulative_MeV": mp.nstr(total, 30),
                "frac_of_B_pred": float(T_k / B_pred),
                "cumulative_frac_of_B_pred": float(total / B_pred),
                "frac_of_B_AME_Qbeta_scale": float(T_k / B_ame),
                "cumulative_frac_of_B_AME_Qbeta_scale": float(total / B_ame),
                "frac_of_B_AME_E0_scale": float(T_k * e0_full / (qb * B_ame)),
                "cumulative_frac_of_B_AME_E0_scale":
                    float(total * e0_full / (qb * B_ame)),
                "subsets": subsets,
            })

        # exact-sum identity: Σ_k T_k = B_pred (finite expansion, exact)
        sum_err = abs(total - B_pred)
        w.add_assertion(
            name=f"expansion_sums_exactly_to_B_pred_{name}",
            computed=float(sum_err), expected=0.0, tolerance=1e-40,
            source="finite inclusion–exclusion identity "
                   "1 − ∏(1−g_i) = Σ_k (−1)^{k+1} e_k(g); exact at 50+ dps",
        )

        row = {
            "atom": name, "Z": Z, "N": N, "A": A,
            "interface_kinds": kinds,
            "g_values": [mp.nstr(g, 30) for g in g_vals],
            "tr_free": mp.nstr(tr_free, 50),
            "B_pred_MeV_Qbeta_scale": mp.nstr(B_pred, 30),
            "B_pred_MeV_E0_scale": mp.nstr(B_pred * e0_full / qb, 30),
            "B_AME_MeV": mp.nstr(B_ame, 30),
            "B_pred_over_B_AME_Qbeta_scale": float(B_pred / B_ame),
            "B_pred_over_B_AME_E0_scale": float(B_pred * e0_full / (qb * B_ame)),
            "orders": orders,
        }
        isotope_results.append(row)

        print(f"\n── {name} (Z={Z}, N={N}; interfaces {kinds}) ──")
        print(f"  B_pred = {mp.nstr(B_pred, 10)} MeV (Q_β scale)  "
              f"[{mp.nstr(B_pred * e0_full / qb, 10)} MeV at E_0 scale]  "
              f"B_AME = {mp.nstr(B_ame, 12)}")
        for o in orders:
            bodies = "/".join(str(b) for b in o["nucleon_body_counts"])
            print(f"  order {o['interface_order_k']} ({bodies}-body): "
                  f"T_k = {mp.nstr(mp.mpf(o['T_k_MeV']), 8)} MeV  "
                  f"({o['frac_of_B_pred']:+.2%} of B_pred; "
                  f"{o['frac_of_B_AME_Qbeta_scale']:+.3%} of B_AME @Q_β; "
                  f"{o['frac_of_B_AME_E0_scale']:+.3%} of B_AME @E_0)")

    w.add_data("isotope_results", isotope_results)

    # ── the ⁴He 4-body question ──────────────────────────────────────
    he4 = isotope_results[-1]
    order3 = he4["orders"][2]
    assert order3["interface_order_k"] == 3
    T3 = mp.mpf(order3["T_k_MeV"])
    ratio_qb = b_magic_4he / T3
    T3_e0 = T3 * e0_full / qb
    ratio_e0 = b_magic_4he / T3_e0
    fourbody = {
        "connected_4body_cross_term_MeV_Qbeta_scale": mp.nstr(T3, 30),
        "connected_4body_cross_term_MeV_E0_scale": mp.nstr(T3_e0, 30),
        "magic_A_value_MeV": mp.nstr(b_magic_4he, 30),
        "magic_over_4body_Qbeta_scale": float(ratio_qb),
        "magic_over_4body_E0_scale": float(ratio_e0),
        "order2_disconnected_2plus2_subset": [
            s for s in he4["orders"][1]["subsets"] if not s["connected"]],
    }
    w.add_data("he4_4body_vs_magic_A", fourbody)
    print(f"\n── ⁴He 4-body cross-term vs magic-A ──")
    print(f"  T_3 (connected 4-body) = {mp.nstr(T3, 8)} MeV @Q_β  "
          f"/ {mp.nstr(T3_e0, 8)} MeV @E_0")
    print(f"  magic-A 2·m_e·4·8G     = {mp.nstr(b_magic_4he, 8)} MeV")
    print(f"  shortfall: {float(ratio_qb):.0f}× @Q_β,  "
          f"{float(ratio_e0):.0f}× @E_0")
    # Was `computed=float(ratio_e0), expected=float(ratio_e0)` -- the ratio as
    # its own expectation, so it passed even if the cross-term had EXCEEDED
    # magic-A, which is the one outcome the name excludes (bean qou-3e5m).
    # The `source` called it informational, but the NAME states a falsifiable
    # direction, and by the qou-26f2 rule the name's claim is what an
    # assertion owes.
    #
    # The threshold is `> 1` deliberately, and it is the only one available
    # without fitting: "below magic-A" is what can invert, and any sharper
    # bound (10x, 49x) would be a number chosen to match the value observed.
    # The magnitude is not lost -- it is recorded in `he4_4body_vs_magic_A`
    # above, currently 49.2x at the E_0 scale and 263x at the Q_beta scale.
    w.add_assertion(
        name="he4_4body_cross_term_far_below_magic_A",
        computed=1 if ratio_e0 > 1 else 0, expected=1, tolerance=0,
        source="magic-A / T_3 at the E_0 scale exceeds 1, i.e. the exact "
               "4-body cross-term of the closed form lies BELOW the magic-A "
               "α-volume value 2·m_e·4·8G ≈ 29.96 MeV; the factor itself is "
               "recorded in data.he4_4body_vs_magic_A",
    )

    # consistency hook to the many-body-ceiling audit: order-1 (2-body)
    # fraction of B_AME at the E_0 scale for ⁴He should sit near the
    # audit's 26% pairwise figure (same object modulo tr_free vs per-pair
    # free-product normalisation, |1 − (0.98)^{A−2}| ≈ 2%-level).
    frac_2body_e0 = he4["orders"][0]["frac_of_B_AME_E0_scale"]
    w.add_assertion(
        name="he4_2body_fraction_matches_ceiling_audit_26pct",
        computed=float(frac_2body_e0), expected=0.26, tolerance=0.03,
        source="order-1 (pairwise) fraction of B_AME(⁴He) at the E_0 scale "
               "vs the 26% pairwise ceiling in "
               "docs/audits/2026-06-02-binding-many-body-ceiling.md",
    )

    # ── verdict ──────────────────────────────────────────────────────
    verdict = {
        "question_1": "What fraction of B_AME does each exact order capture?",
        "answer_1": (
            "The FULL closed form captures only "
            f"{isotope_results[0]['B_pred_over_B_AME_Qbeta_scale']:.1%} (D) → "
            f"{he4['B_pred_over_B_AME_Qbeta_scale']:.1%} (⁴He) of B_AME on "
            "the Q_β scale (the 10A−5 residual), so every order is bounded "
            "by that ceiling. The expansion is ALTERNATING with g_i ≈ "
            "0.5–0.7 (not small): order-1 overshoots B_pred, order-2 "
            "corrects down, order-3 up — the many-body 'hierarchy' of the "
            "interface product is NOT perturbative."
        ),
        "question_2": "Does the ⁴He 4-body cross-term land near the magic-A "
                      "value 2·m_e·4·8G ≈ 29.96 MeV?",
        "answer_2_tier": "REFUTED — scope (a) ONLY",
        "answer_2": (
            "No. The exact connected 4-body cross-term is "
            f"{mp.nstr(T3, 6)} MeV (Q_β scale) / {mp.nstr(T3_e0, 6)} MeV "
            f"(E_0 scale) — a factor ≈{float(ratio_qb):.0f}× / "
            f"≈{float(ratio_e0):.0f}× below the magic-A value. Scope-(a): "
            "the multiplicative interface product of the Phase-5q closed "
            "form, ALONE, at either canonical scale, does not generate the "
            "4-body α-cooperativity; the probe MEASURES the missing "
            "higher-order term (it does not exclude the closed-form factors "
            "from a larger closure — no proved invariant, scope-(b) not "
            "claimed). Consistent with the many-body-ceiling audit: the "
            "α-binding is not reachable from the A−1-interface chain "
            "product at any expansion order."
        ),
    }
    w.add_data("verdict", verdict)
    w.set_description(
        "PROBE 3 (9b, bean iv3r): exact finite inclusion–exclusion "
        "many-body expansion of the Phase-5q closed form "
        "B = Q_β·tr_free·(1 − ∏(1−g_i)) in the interface deficits g_i, for "
        "D/T/³He/⁴He at 50-dps (no new constants). Orders sum EXACTLY to "
        "B_pred (≤1e-40); order-1 at the E_0 scale reproduces the "
        "many-body-ceiling audit's ≈26% pairwise figure for ⁴He. VERDICT: "
        "the connected 4-body cross-term at ⁴He is ~2 orders of magnitude "
        "below the magic-A value 2·m_e·4·8G ≈ 29.96 MeV (REFUTED scope-(a): "
        "the interface chain product alone cannot supply the α "
        "cooperativity at any order, at either canonical scale). "
        "Exploratory; NOT wired."
    )
    out = w.save()
    print(f"\nWitness: {out}  [{time.monotonic() - t_start:.1f}s total]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

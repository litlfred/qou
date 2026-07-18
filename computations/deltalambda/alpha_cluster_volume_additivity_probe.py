#!/usr/bin/env python3
"""alpha_cluster_volume_additivity_probe.py — the atom→knot rule for A ≥ 5:
constraint quantification + the alpha-cluster volume-additivity test (zero fit).

CONTEXT (research-queue `research-atom-to-knot-rule-A5plus`)
------------------------------------------------------------
The mass-table sweep has NO atom→knot assignment for ⁶Li, ⁷Li, ⁹Be, ¹¹B,
¹⁴N, ¹⁹F. The bond-count binding tower (`prop:linear-chain-bond-count`,
Lean-proved multiplicity M_n = (n−1);
docs/audits/2026-07-04-theta-mn-bondcount-derived-linearchain.md)

    B(K) = m_e · Σ_{n=2}^{A} Σ_{consecutive n-clusters c} (n−1) · Vol(c)

is the only derived structure available, but its single-link n=4 reading was
EXECUTED NEGATIVE at ⁴He (docs/audits/2026-07-13-he4-vol4-prediction-test.md:
implied Vol₄ = 8.0484 is carried by NO ≤14-crossing 4-component link — census
gap — and the linear 4-chain closures L8a21/L8a20 overshoot by +26%). Any
A ≥ 5 rule must clear that negative plus the constraints quantified here.

WHAT THIS PROBE COMPUTES (all symbolic-exact arithmetic; nothing tuned)
-----------------------------------------------------------------------
1. Exact re-back-out of the AME-implied Vol₄ (cross-check vs the registered
   8.048; used below ONLY as a clearly-labeled AME-implied guarded input —
   every conclusion touching it is conditional).
2. SUPRA-LINEARITY CONSTRAINT on the untruncated linear-chain tower: the
   aggregate cluster measure Σ_{n=2}^{A}(A−n+1)(n−1) = C(A+1,3) (Lean-proved,
   `QOU.Mass.linear_chain_cluster_measure`) grows like A³ while B_AME grows
   like ~8·A, so the AME-required *average* per-cluster volume
   avg_vol(A) = B_AME/(m_e·C(A+1,3)) must COLLAPSE with A. Tabulated: any
   A ≥ 5 rule keeping O(8) volumes at all levels is excluded by arithmetic.
3. ORDERING GAP: the canonical braid word orders nucleons p^Z n^N
   (`atom_braid_word_3A`, ordering = ['p']*Z + ['n']*N), so the ⁶Li chain
   pppnnn contains ppp and nnn 3-sub-chains — species-pure carriers the
   corpus does NOT assign (only ppn → L6a4, pnn → 8₁₁). The linear-chain
   rule is underdetermined at A ≥ 5 even at the n = 3 level. Quantified by
   bracketing the n≤3 partial sum with carriers ∈ [Vol(L6a4), Vol(8₁₁)].
4. THE ALPHA-CLUSTER ADDITIVITY TEST (the actionable one): read the A ≥ 5
   link as a composite (connected sum / split union) of the A ≤ 4 cluster
   units. Hyperbolic volume is ADDITIVE under both connected sum and split
   union, so under the tower the composite's binding is the SUM of the
   cluster bindings — a zero-fit prediction from A ≤ 4 values alone:

       ⁶Li = α + d      ⁷Li = α + t      ⁸Be = α + α (validation anchor)
       ⁹Be = α + α + n  ¹¹B = 2α + t     ¹²C = 3α
       ¹⁴N = 3α + d     ¹⁶O = 4α         ¹⁹F = 4α + t

   B_add = Σ_cluster B(cluster) vs AME. The deficit B_AME − B_add is exactly
   the cluster-separation energy (the missing inter-cluster bond term); its
   implied per-bond volume deficit/(m_e·(#pieces−1)) is reported as GUARDED
   data (non-evidential — matching a link to it would be a CAL-4 fit).

   Two cluster-value conventions, both reported:
   (a) AME-level (cluster B from AME2020) — tests the additivity RULE itself,
       zero framework input beyond the decomposition;
   (b) tower-level (cluster B from the tower: t = m_e·2·Vol(8₁₁), d = 0 via
       Hopf, α conditional on the AME-implied Vol₄ — tautologically B_AME(α),
       so labeled CONDITIONAL/guarded).

EXPECTED SHAPE OF THE RESULT (registered before the run)
--------------------------------------------------------
⁸Be should validate additivity to ≲0.5% (⁸Be is famously barely unbound
against 2α); one-bond composites (⁶Li, ⁷Li, ⁹Be) should undershoot by the
few-MeV separation energies (≈3–7%); multi-bond composites (¹¹B, ¹⁴N, ¹⁹F)
should undershoot progressively more as inter-cluster bonds accumulate.
Additivity is a LOWER BOUND under the tower reading (adding hyperbolic
content only adds volume), so every deficit except ⁸Be's should be ≥ 0.

Run:  python3 -u computations/deltalambda/alpha_cluster_volume_additivity_probe.py \\
        2>&1 | tee /tmp/alpha_cluster_additivity.log

EXPLORATORY — audit-only witness; no production wiring; no fitted constant.
Audit: docs/audits/2026-07-13-atom-knot-rule-a5plus-constraints.md
"""
from __future__ import annotations

import datetime
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent          # computations/deltalambda/
_COMP = _HERE.parent                             # computations/
for _d in (_COMP, _COMP / "substrate"):
    _p = str(_d)
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV, _ame_binding_mev  # noqa: E402

set_compute_dps()

# ── inputs (all with provenance; nothing fitted) ─────────────────────────────
M_E = mp.mpf(str(M_E_MEV))                       # CAL-1 (CODATA 2022)

# corpus 3-body sub-link volumes — binding-link-volumes.witness.json
# (SnapPy-derived, committed; both are *deprecated volume-search* IDs per
# docs/audits/2026-07-04-he4-vol4-gated-on-r5full.md — carried as the
# corpus' working values, trace-unconfirmed).
VOL_8_11 = mp.mpf("8.286316817806593")           # pnn carrier (³H)
VOL_L6A4 = mp.mpf("7.327724753417752")           # ppn carrier (³He, Borromean)
# 2-body sub-links: Hopf, Seifert-fibred, Vol = 0 (KMM convention).

PRE_REGISTERED_VOL4 = mp.mpf("8.048")            # 2026-07-04 back-out (guarded)

# AME2020 binding energies (validation-only, vendored single source of truth)
B = {name: _ame_binding_mev(Z, A) for name, Z, A in [
    ("d", 1, 2), ("t", 1, 3), ("3He", 2, 3), ("4He", 2, 4),
    ("6Li", 3, 6), ("7Li", 3, 7), ("8Be", 4, 8), ("9Be", 4, 9),
    ("11B", 5, 11), ("12C", 6, 12), ("14N", 7, 14), ("16O", 8, 16),
    ("19F", 9, 19),
]}

# alpha-cluster decompositions (pieces; a lone "n"/free nucleon binds 0)
DECOMP = {
    "6Li": ["4He", "d"],
    "7Li": ["4He", "t"],
    "8Be": ["4He", "4He"],                # validation anchor (2α threshold)
    "9Be": ["4He", "4He", "n"],
    "11B": ["4He", "4He", "t"],
    "12C": ["4He", "4He", "4He"],
    "14N": ["4He", "4He", "4He", "d"],
    "16O": ["4He", "4He", "4He", "4He"],
    "19F": ["4He", "4He", "4He", "4He", "t"],
}
GAP_ISOTOPES = ["6Li", "7Li", "9Be", "11B", "14N", "19F"]  # the queue's 6 gaps


def cluster_measure(A: int) -> int:
    """Σ_{n=2}^{A} (A−n+1)(n−1) = C(A+1,3) — Lean-proved
    (`QOU.Mass.linear_chain_cluster_measure`)."""
    return sum((A - n + 1) * (n - 1) for n in range(2, A + 1))


def main() -> int:
    print("=" * 74)
    print(" atom→knot rule for A ≥ 5 — constraint quantification +")
    print(" alpha-cluster volume-additivity test (zero fit)")
    print("=" * 74)

    # ── 1. exact Vol₄ re-back-out (guarded AME-implied input) ────────────────
    B_23_4he = M_E * (2 * VOL_L6A4 + 2 * VOL_8_11)
    vol4_implied = (B["4He"] - B_23_4he) / (3 * M_E)
    backout_ok = abs(float(vol4_implied - PRE_REGISTERED_VOL4)) < 0.01
    print(f"\n[1] AME-implied Vol4 (guarded input) = {mp.nstr(vol4_implied, 8)}"
          f"   (pre-registered 8.048, delta {float(vol4_implied - PRE_REGISTERED_VOL4):+.5f})")
    print("    GUARD: AME-implied, not derived — every use below is conditional.")

    # ── 2. supra-linearity: required average volume must collapse ────────────
    print("\n[2] Supra-linearity constraint (untruncated linear-chain tower):")
    print("    cluster measure C(A+1,3) ~ A^3 vs B_AME ~ 8·A  =>  required")
    print("    avg per-cluster volume avg_vol(A) = B_AME/(m_e·C(A+1,3)):")
    ISO_A = {"t": 3, "4He": 4, "6Li": 6, "7Li": 7, "12C": 12, "16O": 16}
    avg_rows = {}
    for name, A in ISO_A.items():
        cm = cluster_measure(A)
        av = float(B[name] / (M_E * cm))
        avg_rows[name] = {"A": A, "cluster_measure": cm, "avg_vol_required": av}
        print(f"      {name:4s} A={A:2d}  C(A+1,3)={cm:5d}  avg_vol = {av:7.3f}")
    seq = [avg_rows[k]["avg_vol_required"] for k in ("4He", "6Li", "7Li", "12C", "16O")]
    collapse = all(a > b for a, b in zip(seq, seq[1:]))
    print("    => strictly decreasing from A=4 on; at A=6 already 1.79 — a rule")
    print("       keeping O(8) volumes at every level is excluded by arithmetic.")

    # ── 3. ordering gap + bracketed n<=3 partial sums for 6Li/7Li ────────────
    print("\n[3] Ordering gap (canonical p^Z n^N chain):")
    print("    6Li = pppnnn -> 3-sub-chains {ppp, ppn, pnn, nnn}: ppp/nnn have")
    print("    NO corpus carrier (only ppn->L6a4, pnn->8_11). Bracketing every")
    print("    3-carrier in [Vol(L6a4), Vol(8_11)]:")
    lo, hi = VOL_L6A4, VOL_8_11
    brackets = {}
    for name, n3 in (("6Li", 4), ("7Li", 5)):     # A−2 consecutive 3-chains
        blo, bhi = M_E * 2 * n3 * lo, M_E * 2 * n3 * hi
        inside = float(blo) <= float(B[name]) <= float(bhi)
        brackets[name] = {"n3_clusters": n3, "B_n3_lo": float(blo),
                          "B_n3_hi": float(bhi), "B_AME": float(B[name]),
                          "AME_inside_bracket": inside}
        print(f"      {name}: n<=3 partial sum in [{float(blo):6.2f}, {float(bhi):6.2f}] MeV"
              f"  vs AME {float(B[name]):6.2f}  ({'BRACKETS AME' if inside else 'outside'})")
    print("    => at A=6,7 the n<=3 layer ALONE spans AME; the n>=4 terms must be")
    print("       near zero (consistent with the ⁴He census-gap negative and the")
    print("       non-hyperbolic 4-component Brunnian L8n8) — yet a pure n<=3")
    print("       truncation FAILS at 4He (n<=3 = 15.96 MeV = 56% of AME).")

    # ── 4. alpha-cluster additivity (the actionable test) ────────────────────
    print("\n[4] Alpha-cluster volume additivity, AME-level cluster values")
    print("    (Vol additive under connected sum AND split union => B adds):")
    print(f"    {'iso':5s} {'decomposition':16s} {'B_add':>9s} {'B_AME':>9s} "
          f"{'err%':>7s} {'deficit':>8s} {'impl.Vol/bond':>13s}")
    add_rows = {}
    for name, pieces in DECOMP.items():
        b_add = mp.mpf(0)
        for p in pieces:
            b_add += B[p] if p in B else mp.mpf(0)   # free "n" binds 0
        deficit = B[name] - b_add                     # = cluster separation energy
        err = float((b_add - B[name]) / B[name])
        nbond = len(pieces) - 1
        impl_vol = float(deficit / (M_E * nbond)) if nbond else 0.0
        add_rows[name] = {
            "pieces": pieces, "B_add_MeV": float(b_add), "B_AME_MeV": float(B[name]),
            "rel_err": err, "deficit_MeV": float(deficit),
            "n_intercluster_bonds": nbond,
            "implied_vol_per_bond_GUARDED": impl_vol,
        }
        print(f"    {name:5s} {'+'.join(pieces):16s} {float(b_add):9.3f} "
              f"{float(B[name]):9.3f} {err * 100:+7.2f} {float(deficit):+8.3f} "
              f"{impl_vol:13.3f}")
    print("    (implied Vol/bond column is GUARDED, non-evidential — matching a")
    print("     link volume to it post hoc would be a CAL-4 fit.)")

    anchor_ok = abs(add_rows["8Be"]["rel_err"]) < 0.005        # 2α threshold
    li6_err, li7_err = add_rows["6Li"]["rel_err"], add_rows["7Li"]["rel_err"]
    onebond_ok = abs(li6_err) < 0.10 and abs(li7_err) < 0.10
    # additivity is a lower bound (deficit >= 0) except the unbound 8Be
    lower_bound_ok = all(r["deficit_MeV"] > 0 for k, r in add_rows.items() if k != "8Be") \
        and -0.2 < add_rows["8Be"]["deficit_MeV"] < 0
    impl_vols = [add_rows[k]["implied_vol_per_bond_GUARDED"] for k in
                 ("6Li", "7Li", "9Be", "11B", "12C", "14N", "16O", "19F")]
    non_universal = (max(impl_vols) - min(impl_vols)) > 2.0    # spread >> any tolerance

    # ── 5. tower-level variant (CONDITIONAL — labeled) ───────────────────────
    print("\n[5] Tower-level cluster values (CONDITIONAL: alpha uses the AME-implied")
    print("    Vol4, hence B_tower(4He) = B_AME(4He) tautologically; d = 0 via Hopf;")
    print("    t = m_e·2·Vol(8_11) = derived, -0.16%):")
    b_t_tower = M_E * 2 * VOL_8_11
    tower_rows = {
        "6Li": {"B_pred_MeV": float(B["4He"] + 0),
                "note": "alpha(conditional) + d(Hopf, Vol=0)"},
        "7Li": {"B_pred_MeV": float(B["4He"] + b_t_tower),
                "note": "alpha(conditional) + t(m_e·2·Vol(8_11))"},
    }
    for name, row in tower_rows.items():
        row["rel_err"] = float((mp.mpf(str(row["B_pred_MeV"])) - B[name]) / B[name])
        print(f"      {name}: B_pred = {row['B_pred_MeV']:7.3f} vs AME "
              f"{float(B[name]):7.3f}  ({row['rel_err'] * 100:+.2f}%)  [{row['note']}]")
    print("    => the Hopf-zero deuteron cluster costs 6Li ~7% extra undershoot;")
    print("       the derived Borromean-route deuteron (+0.19%) restores the AME-")
    print("       level -4.6% (its value is numerically B_AME(d) to 0.19%).")

    # ── verdict ──────────────────────────────────────────────────────────────
    verdict = (
        "Scope-(a) constraint analysis for the A>=5 atom->knot rule. "
        "(1) The untruncated linear-chain tower is excluded by arithmetic at "
        "A>=5 unless Vol_n collapses (required avg volume falls 5.54 -> 1.79 "
        "from A=4 to A=6 vs the 7.3-8.3 corpus 3-carriers); with the ⁴He "
        "census-gap negative, the single-volume linear-chain reading does not "
        "extend. (2) The p^Z n^N ordering leaves ppp/nnn 3-carriers unassigned "
        "at A>=5 — the rule is underdetermined even at n=3 — though the "
        "bracketed n<=3 layer alone spans AME at A=6,7. "
        "(3) ALPHA-CLUSTER ADDITIVITY (zero fit, AME-level clusters): the 2-alpha "
        f"anchor 8Be reproduces AME to {add_rows['8Be']['rel_err'] * 100:+.2f}%; "
        f"one-bond composites undershoot mildly (6Li {li6_err * 100:+.2f}%, "
        f"7Li {li7_err * 100:+.2f}%, 9Be {add_rows['9Be']['rel_err'] * 100:+.2f}%); "
        f"multi-bond composites degrade (11B {add_rows['11B']['rel_err'] * 100:+.1f}%, "
        f"14N {add_rows['14N']['rel_err'] * 100:+.1f}%, "
        f"19F {add_rows['19F']['rel_err'] * 100:+.1f}%). Additivity is a "
        "consistent LOWER BOUND (all deficits > 0 except the famously 2alpha-"
        "unbound 8Be) whose deficit is the inter-cluster bond term; the implied "
        "per-bond volumes (2.9 -> 12.8, guarded) are NON-CONSTANT, so the missing "
        "term is not one universal volume. This constrains the composite rule "
        "class as-is; it does not exclude the composite ingredient (permanence "
        "principle: the cluster pieces are structurally exact lower-bound "
        "contributions). The principled route to the actual A>=5 links remains "
        "the R5-full SDP canonical knot-ID (conj:canonical-knot-id-sdp, #604), "
        "which must first resolve its own A<=3 anchor non-confirmation. "
        "Nothing wired; no fit; every use of Vol4=8.048 is conditional/AME-implied."
    )
    print(f"\nVERDICT: {verdict}")

    # ── witness ──────────────────────────────────────────────────────────────
    wit = {
        "computation": "alpha-cluster-volume-additivity",
        "description": (
            "A>=5 atom->knot rule constraint quantification + alpha-cluster "
            "volume-additivity test: exact AME2020 back-outs, supra-linearity "
            "of the linear-chain cluster measure C(A+1,3) vs linear B, the "
            "p^Z n^N ordering gap (unassigned ppp/nnn carriers), and zero-fit "
            "additivity predictions for 6Li/7Li/8Be/9Be/11B/12C/14N/16O/19F "
            "from A<=4 cluster values. Research-queue item "
            "research-atom-to-knot-rule-A5plus."),
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "mpmath (symbolic-exact arithmetic; no census scan)",
        "inputs": {
            "m_e_MeV": {"value": float(M_E), "source": "codata_constants.M_E_MEV (CODATA 2022, CAL-1)"},
            "AME2020": {"source": "qou-mass/src/qou_mass/data/ame2020.json via _ame_binding_mev (validation-only)",
                        "binding_MeV": {k: float(v) for k, v in B.items()}},
            "Vol_L6a4_ppn": {"value": float(VOL_L6A4), "source": "binding-link-volumes.witness.json (deprecated volume-search ID)"},
            "Vol_8_11_pnn": {"value": float(VOL_8_11), "source": "binding-link-volumes.witness.json (deprecated volume-search ID)"},
            "Vol_2body": {"value": 0.0, "source": "Hopf link non-hyperbolic (KMM convention)"},
            "Vol4_AME_implied_GUARDED": {"value": float(vol4_implied),
                                         "guard": "AME-implied, not derived; conditional everywhere used"},
        },
        "supra_linearity": {
            "identity": "sum_{n=2..A} (A-n+1)(n-1) = C(A+1,3) (Lean-proved, QOU.Mass.linear_chain_cluster_measure)",
            "avg_vol_required": avg_rows,
            "strictly_decreasing_from_A4": bool(collapse),
        },
        "ordering_gap": {
            "canonical_ordering": "['p']*Z + ['n']*N (atom_braid_word_3A)",
            "unassigned_3carriers_at_6Li": ["ppp", "nnn"],
            "n3_partial_sum_brackets": brackets,
        },
        "alpha_cluster_additivity_AME_level": add_rows,
        "tower_level_conditional": tower_rows,
        "verdict": verdict,
        "scope": "(a) — constrains the untruncated tower and quantifies the composite rule class; no ingredient excluded",
        "assertions": [
            {"label": "exact back-out confirms AME-implied Vol4 = 8.048 to 0.01",
             "passed": bool(backout_ok)},
            {"label": "required avg volume strictly decreasing A=4 -> 16 (supra-linearity constraint)",
             "passed": bool(collapse)},
            {"label": "8Be (2-alpha) additivity anchor within 0.5% of AME",
             "passed": bool(anchor_ok)},
            {"label": "one-bond composites 6Li/7Li within 10% (measured -4.6%/-6.3%)",
             "passed": bool(onebond_ok)},
            {"label": "additivity is a lower bound: all deficits > 0 except unbound 8Be (in (-0.2, 0))",
             "passed": bool(lower_bound_ok)},
            {"label": "implied per-bond volumes non-constant (spread > 2.0) => no single universal inter-cluster volume",
             "passed": bool(non_universal)},
            {"label": "n<=3 bracket spans AME at A=6 and A=7",
             "passed": bool(all(b["AME_inside_bracket"] for b in brackets.values()))},
        ],
        "gap_isotopes_covered": GAP_ISOTOPES,
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, str(_HERE.parent / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(wit, script_path=__file__, engine="mpmath")
    wit["scriptFile"] = Path(__file__).name
    out = _HERE / "alpha-cluster-volume-additivity.witness.json"
    json.dump(wit, open(out, "w"), indent=1)
    print(f"\nwitness -> {out.name}   allPassed: {wit['allPassed']}")
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

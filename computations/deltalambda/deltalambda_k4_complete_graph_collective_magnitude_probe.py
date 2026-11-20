#!/usr/bin/env python3
"""Δ_λ gate, ATTACK VECTOR 1 — the collective magnitude as a K₄ GRAPH object.

CONTEXT.  #3943 (deltalambda_perpair_bond_magnitude_derive_probe.py) proved that
an ADDITIVE per-pair magnitude `B = m_e·Σ_n M_n(A)·Vol_n(K)` (with additive
`M_n = (n−1)`) FAILS on the four light isotopes, and that the ³H/³He mirror split
shows the residual is COLLECTIVE / non-additive.  Attack Vector 1 (attack-vector
map 2026-07-18, §4 row 1) asks the next question: is the missing collective term
a parameter-free GRAPH object on the 4-nucleon complete coordination graph K₄
(6 edges) — a Laplacian-spectrum / spanning-tree / graph-determinant invariant —
rather than a sum of independent pair terms?

THE HYPOTHESIS (parameter-free, no fit).  The 4-nucleon coordination graph is the
complete graph K_A on A vertices (²H = K₂, ³H/³He = K₃, ⁴He = K₄).  Its
parameter-free invariants are:
  • edge count            C(A,2)                = {1, 3, 3, 6}
  • Laplacian spectrum    {0, A^{×(A−1)}}       ⇒ K₄: {0,4,4,4}
  • spanning-tree count   τ(K_A) = A^{A−2}      = {1, 3, 3, 16}   (Cayley)
  • Laplacian pseudo-det  ∏ nonzero λ = A^{A−1} = {2, 9, 9, 64}
  • algebraic connectivity  λ₂ = A             = {2, 3, 3, 4}
A hyperbolic volume of a K₄-associated link is ALSO a candidate here, but it is a
topological invariant carrying NO proton/neutron label, so it falls under the same
isospin-blindness argument below (Part C) — not computed separately.

THE FORWARD TEST (non-fit).  Consume the #3943 committed deficits (target − B_dim,
NOT recomputed, NOT refit) and ask whether ONE parameter-free graph invariant,
scaled by the substrate energy unit E₀ = m_e/(q₀(q₀−1)) with NO free prefactor,
reproduces all four deficits simultaneously.  Solving a prefactor from the
deficits would be the forbidden seventh fit-based ansatz (AGENTS.md) — this probe
NEVER does that; it reports the required prefactor per isotope and shows it is
non-constant.

THE MIRROR DIAGNOSTIC (the crux).  ³H and ³He are the SAME graph K₃.  Every
parameter-free UNSIGNED graph invariant therefore predicts deficit(³H)=deficit(³He)
(ratio 1.000), whereas the data needs 1.223.  The ONLY K₄ graph object that can
split the mirror pair is the SIGNED/colored graph (pp=+1, nn=−1, pn=±1) — but that
is exactly the b4 exchange determinant (#3924) which needs the GATED per-pair
magnitude m and, at the corpus parameter-free m's, gives the WRONG split (~2.75×,
#3943).  So neither the unsigned (isospin-blind) nor the signed (needs gated m,
wrong split) K₄ graph object supplies the collective deficit.

VERDICT (double honest negative, well-scoped):
  (b) STRUCTURAL EXCLUSION — a parameter-free UNSIGNED K_A graph invariant cannot
      supply the p/n mirror split.  Cited invariant: the coordination graph K_A is
      a function of A = Z+N only (isospin-blind), the same invariant proved for the
      antisymmetrizer trace / Reeb pn-magnitude det-conjugation (attack-vector map
      §2.1; QOU/MassTheory/ReebPnMagnitude.lean).
  (a) SCOPE-LIMITED NEGATIVE — no single parameter-free graph invariant × E₀
      reproduces the four-isotope deficit magnitudes: required prefactors span
      1.4–6.8×.  The super-additive COLLECTIVE invariants (spanning trees, Laplacian
      pseudo-det) OVERSHOOT ⁴He 2.6–10.6×; only the ADDITIVE edge count matches ⁴He
      (0.99×) but overshoots the lighter isotopes ~2×.  ⇒ the deficit's magnitude
      does NOT scale as a super-additive graph object.
REFINED READING: the "collective" character of the #3943 residual is an ISOSPIN
(p/n) degree of freedom, NOT a super-additive graph magnitude.  Vector 1 sharpens
the search — the missing DOF is the mirror split, and it is not a K₄ graph-collective
term.

  -- Ref: deltalambda_perpair_bond_magnitude_derive_probe.py (#3943, additive negative +
     committed deficits, consumed here);
     b4_slater_antisymmetrizer_exchange_sign.py (#3924, K₄ exchange spectrum {±√5,±1},
     signed-graph det, gated magnitude);
     mnk_coordination_graph_selection.py (coordination-graph tower framing);
     docs/audits/2026-07-18-deltalambda-attack-vector-map.md (Vector 1 spec, §2.1 isospin prune);
     docs/audits/2026-07-18-deltalambda-k4-collective-magnitude.md (this probe's report);
     QOU/MassTheory/ReebPnMagnitude.lean (pn-sign det invariance = isospin-blindness invariant).
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
from codata_constants import AME_B_HE3_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)

set_compute_dps()
COMP = str(_COMP)

# ── Derived-elsewhere inputs (consumed from #3943, NOT recomputed, NOT fitted) ──
ISO = ["2H", "3H", "3He", "4He"]
A_OF = {"2H": 2, "3H": 3, "3He": 3, "4He": 4}
TYPES = {"2H": ["p", "n"], "3H": ["p", "n", "n"],
         "3He": ["p", "p", "n"], "4He": ["p", "p", "n", "n"]}
B_DIM = {  # |B_dim| MeV, single-trace undershoot (#3542 sign, q-hook dim)
    "2H": mp.mpf("0.38007125148431475"),
    "3H": mp.mpf("1.9085327584765543"),
    "3He": mp.mpf("2.3446056813751914"),
    "4He": mp.mpf("3.0381869604868865"),
}
B_AME = {  # AME2020 connected binding MeV
    "2H": AME_B_DEUTERON_MEV_VALIDATION,
    "3H": AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
}


# ── parameter-free invariants of the complete graph K_A (functions of A ONLY) ──
def edge_count(a: int) -> int:
    """|E(K_A)| = C(A,2) — the additive pair count."""
    return a * (a - 1) // 2


def spanning_trees(a: int) -> int:
    """τ(K_A) = A^{A-2} (Cayley's formula); collective / super-additive."""
    return a ** (a - 2) if a >= 2 else 1


def laplacian_pseudo_det(a: int) -> int:
    """∏ nonzero Laplacian eigenvalues of K_A = A^{A-1} (spectrum {0, A^{×(A-1)}})."""
    return a ** (a - 1)


def algebraic_connectivity(a: int) -> int:
    """λ₂(K_A) = A — the Laplacian spectral gap (second-smallest eigenvalue)."""
    return a


GRAPH_INVARIANTS = {
    "edge_count_C(A,2)": edge_count,
    "spanning_trees_A^(A-2)": spanning_trees,
    "laplacian_pseudo_det_A^(A-1)": laplacian_pseudo_det,
    "algebraic_connectivity_A": algebraic_connectivity,
}


def _signed_det_I_plus_G(types, m, w_pn=1):
    """det(I + m·S) on the signed complete graph (pp=+1, nn=−1, pn=w_pn).
    The ONLY K_A graph object that distinguishes ³H (pnn) from ³He (ppn)."""
    n = len(types)
    S = mp.zeros(n, n)
    for i in range(n):
        for j in range(i + 1, n):
            if types[i] == types[j]:
                s = 1 if types[i] == "p" else -1
            else:
                s = w_pn
            S[i, j] = S[j, i] = s * m
    return mp.det(mp.eye(n) + S)


def main() -> int:
    t0 = time.monotonic()
    q, qi, z = load_q_50dps()
    m_e = mp.mpf(str(M_E_MEV))
    E0 = m_e / (q * (q - 1))                        # substrate energy unit (MeV)
    g_reeb = mp.mpf(1) / mp.sqrt(mp.mpf(5) + (q - 1) ** 2 / q)  # parameter-free m
    ceiling = mp.mpf(1) / mp.sqrt(5)

    deficit = {iso: B_AME[iso] - B_DIM[iso] for iso in ISO}

    # ── Part A: graph-invariant table (parameter-free, functions of A only) ──
    inv_table = {}
    for iso in ISO:
        a = A_OF[iso]
        inv_table[iso] = {name: f(a) for name, f in GRAPH_INVARIANTS.items()}
    inv_table["_K4_laplacian_spectrum"] = [0, 4, 4, 4]

    # ── Part B: forward test — E0·invariant vs deficit, NO free prefactor ──
    per_invariant = {}
    for name, f in GRAPH_INVARIANTS.items():
        rows = []
        prefactors = []
        for iso in ISO:
            a = A_OF[iso]
            pred = E0 * f(a)
            need_pref = deficit[iso] / pred          # prefactor a FIT would need
            prefactors.append(need_pref)
            rows.append({
                "iso": iso, "A": a, "invariant": f(a),
                "pred_MeV_E0_times_inv": mp.nstr(pred, 8),
                "deficit_MeV": mp.nstr(deficit[iso], 8),
                "pred/deficit": mp.nstr(pred / deficit[iso], 6),
                "required_prefactor": mp.nstr(need_pref, 6),
            })
        pref_spread = max(prefactors) / min(prefactors)
        # a genuine parameter-free match would need a CONSTANT prefactor (spread≈1)
        simultaneous_match = bool(pref_spread < mp.mpf("1.05"))
        per_invariant[name] = {
            "rows": rows,
            "required_prefactor_spread_max/min": mp.nstr(pref_spread, 6),
            "simultaneous_parameter_free_match": simultaneous_match,
        }

    # ── Part C: mirror diagnostic — ³H vs ³He (identical graph K₃) ──
    # (i) unsigned invariants are isospin-blind: ratio is EXACTLY 1
    unsigned_mirror_ratio = mp.mpf(1)          # both ³H,³He are K₃ ⇒ any f(A) equal
    data_mirror_ratio = deficit["3H"] / deficit["3He"]
    # (ii) the signed/colored K₃ graph (the only graph object that splits the pair):
    #      it needs the GATED magnitude m; evaluate at the parameter-free g_reeb.
    d_3h = _signed_det_I_plus_G(TYPES["3H"], g_reeb)
    d_3he = _signed_det_I_plus_G(TYPES["3He"], g_reeb)
    signed_mirror_ratio = (-mp.log(d_3h)) / (-mp.log(d_3he))

    mirror = {
        "data_deficit_ratio_3H/3He": mp.nstr(data_mirror_ratio, 6),
        "unsigned_graph_invariant_ratio": mp.nstr(unsigned_mirror_ratio, 6),
        "unsigned_note": ("³H (pnn) and ³He (ppn) are the SAME graph K₃; every "
                          "parameter-free UNSIGNED invariant f(A) gives ratio 1.000 "
                          "≠ data 1.223 — isospin-blind (scope-(b), cited invariant)."),
        "signed_graph_det_ratio_at_g_reeb": mp.nstr(signed_mirror_ratio, 6),
        "signed_note": ("the SIGNED graph (pp=+1,nn=−1,pn=+1) is the only K_A graph "
                        "object that splits ³H/³He, but it needs the GATED per-pair m "
                        "(so it is not a parameter-free 'collective' object) and at "
                        "g_reeb gives ~2.75× — WRONG magnitude/direction vs data 1.223× "
                        "(reproduces #3943)."),
    }

    # ── verdict ──
    any_simultaneous = any(v["simultaneous_parameter_free_match"] for v in per_invariant.values())
    # super-additive collective invariants overshoot 4He; additive edge-count matches 4He only
    ec = per_invariant["edge_count_C(A,2)"]["rows"][-1]        # 4He row
    tr = per_invariant["spanning_trees_A^(A-2)"]["rows"][-1]
    edge_matches_he4 = bool(abs(mp.mpf(ec["pred/deficit"]) - 1) < mp.mpf("0.02"))
    trees_overshoot_he4 = bool(mp.mpf(tr["pred/deficit"]) > mp.mpf("2"))

    verdict = (
        "DOUBLE HONEST NEGATIVE — a parameter-free K₄ (K_A) GRAPH object does NOT "
        "supply the collective Δ_λ deficit; Vector 1 sharpens the search rather than "
        "closing it. (b) STRUCTURAL EXCLUSION: an UNSIGNED K_A graph invariant is a "
        "function of A=Z+N only, so it predicts deficit(³H)=deficit(³He) (ratio 1.000) "
        "vs data 1.223 — isospin-blind; cited invariant = coordination graph K_A "
        "depends on A only (ReebPnMagnitude.lean det-conjugation, attack-vector map "
        "§2.1). (a) SCOPE-LIMITED: no single parameter-free graph invariant × E₀ "
        "reproduces the four-isotope deficit magnitudes (required prefactors span "
        "~1.4–6.8×); the super-additive COLLECTIVE invariants (spanning trees, "
        "Laplacian pseudo-det) OVERSHOOT ⁴He 2.6–10.6×, while only the ADDITIVE edge "
        "count matches ⁴He (0.99×) yet overshoots the lighter isotopes ~2×. The signed "
        "graph — the only K_A object that splits the mirror pair — needs the gated m and "
        "gives the wrong 2.75× split. REFINED READING: the residual's collective "
        "character is an ISOSPIN (p/n) DOF, not a super-additive graph magnitude. "
        "NOT a derivation; NOT wired; deficits NOT inverted (no 7th fit)."
    )

    result = {
        "hypothesis": ("the missing collective Δ_λ term is a parameter-free invariant of "
                       "the complete coordination graph K_A (²H=K₂, ³H/³He=K₃, ⁴He=K₄), "
                       "not an additive sum of per-pair terms (#3943)"),
        "constants": {
            "q0": mp.nstr(q, 12),
            "E0_MeV_m_e/(q(q-1))": mp.nstr(E0, 8),
            "g_reeb_parameter_free_m": mp.nstr(g_reeb, 12),
            "ceiling_1/sqrt5": mp.nstr(ceiling, 12),
        },
        "derived_inputs_not_fitted": {
            "B_dim_MeV_single_trace": {k: mp.nstr(v, 8) for k, v in B_DIM.items()},
            "B_AME_MeV": {k: mp.nstr(v, 8) for k, v in B_AME.items()},
            "deficit_MeV_target_minus_Bdim": {k: mp.nstr(deficit[k], 8) for k in ISO},
            "source": "deltalambda-perpair-bond-magnitude-derive.witness.json (#3943, consumed)",
        },
        "partA_graph_invariants": inv_table,
        "partB_forward_test_per_invariant": per_invariant,
        "partC_mirror_diagnostic": mirror,
        "method_guard": ("every candidate is a parameter-free graph invariant × E₀ with NO "
                         "free prefactor; the required prefactor is REPORTED, never solved "
                         "for. Solving it from the deficits = forbidden 7th fit (AGENTS.md)."),
        "verdict": verdict,
    }

    payload = {
        "computation": "deltalambda-k4-complete-graph-collective-magnitude",
        "description": (
            "Δ_λ attack Vector 1: tests whether a parameter-free invariant of the K_A "
            "complete coordination graph (Laplacian spectrum {0,4,4,4}, spanning trees 16, "
            "edge count, pseudo-det, algebraic connectivity) supplies the collective "
            "deficit the #3943 additive per-pair route missed. Forward test vs the four "
            "committed deficits with NO free prefactor + the ³H/³He mirror diagnostic. "
            "Double honest negative: unsigned invariants are isospin-blind (scope-(b)), and "
            "no invariant reproduces the deficit magnitudes (scope-(a)); the collective DOF "
            "is isospin, not a super-additive graph term. No fit, no AME inversion, audit-only."
        ),
        "tier": "structural forward-test (parameter-free graph invariant -> predicted deficit -> compare; no tuning)",
        "result": result,
        "context": {
            "axis": "Δ_λ Track-A gate — attack Vector 1 (K₄ collective graph magnitude)",
            "no_fit": True,
            "no_ame_inversion": True,
            "q0_convention": "proton (experimental / Physical-Observations pin; owner directive 2026-08-07). Corrected from 'muon-canonical (computations/ layer)' on 2026-09-04, bean qou-9ugp: the label named a layer this producer does not evaluate at.",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "deltalambda-k4-complete-graph-collective-magnitude", payload,
        script_path=__file__, engine="python+mpmath",
        output_dir=os.path.join(COMP, "deltalambda"), start_time=t0,
    )
    wb.add_assertion("no_parameter_free_graph_invariant_matches_all_four",
                     computed=str(not any_simultaneous), expected="True")
    wb.add_assertion("unsigned_invariant_isospin_blind_mirror_ratio_1",
                     computed=str(bool(abs(unsigned_mirror_ratio - 1) < mp.mpf("1e-9"))), expected="True",
                     source="³H,³He both K₃ ⇒ any f(A) equal (ratio 1.000); data needs 1.223 (isospin split)")
    wb.add_assertion("data_mirror_split_exceeds_unity",
                     computed=str(bool(data_mirror_ratio > 1)), expected="True",
                     source="deficit(³H)/deficit(³He) = 1.223 (the isospin DOF a graph invariant cannot carry)")
    wb.add_assertion("additive_edge_count_matches_He4_only",
                     computed=str(edge_matches_he4), expected="True")
    wb.add_assertion("collective_spanning_trees_overshoot_He4",
                     computed=str(trees_overshoot_he4), expected="True")
    wb.add_assertion("signed_graph_mirror_split_wrong_at_g_reeb",
                     computed=str(bool(signed_mirror_ratio > mp.mpf("2"))), expected="True",
                     source="signed K₃ det ratio ~2.75× vs data 1.223× (reproduces #3943)")
    out = wb.save(extra={"auditOnly": True})

    # ── console report ──
    print("=== Δ_λ Vector 1 — K₄ collective GRAPH magnitude (forward, non-fit) ===")
    print(f"  q0={float(q):.6f}  E0={float(E0):.4f} MeV  K₄ Laplacian spectrum = {{0,4,4,4}}")
    print(f"  deficits (target−B_dim) MeV: " +
          "  ".join(f"{iso}:{float(deficit[iso]):.3f}" for iso in ISO))
    print("\n  Part A — parameter-free graph invariants of K_A (functions of A only):")
    print(f"    {'iso':4} {'A':>1} {'edges':>6} {'trees':>6} {'lapPD':>6} {'algc':>5}")
    for iso in ISO:
        t = inv_table[iso]
        print(f"    {iso:4} {A_OF[iso]:>1} {t['edge_count_C(A,2)']:>6} "
              f"{t['spanning_trees_A^(A-2)']:>6} {t['laplacian_pseudo_det_A^(A-1)']:>6} "
              f"{t['algebraic_connectivity_A']:>5}")
    print("\n  Part B — forward test  E0·invariant vs deficit (required prefactor should be CONSTANT):")
    for name, pv in per_invariant.items():
        print(f"    [{name}]  prefactor spread max/min = {pv['required_prefactor_spread_max/min']}  "
              f"match={pv['simultaneous_parameter_free_match']}")
        for r in pv["rows"]:
            print(f"       {r['iso']:4} A={r['A']} inv={r['invariant']:>2}  "
                  f"pred={float(mp.mpf(r['pred_MeV_E0_times_inv'])):8.3f}  "
                  f"def={float(mp.mpf(r['deficit_MeV'])):8.3f}  "
                  f"pred/def={float(mp.mpf(r['pred/deficit'])):6.3f}  "
                  f"need_pref={float(mp.mpf(r['required_prefactor'])):6.4f}")
    print("\n  Part C — ³H/³He mirror diagnostic (the crux):")
    print(f"    data deficit ratio            = {mirror['data_deficit_ratio_3H/3He']}")
    print(f"    unsigned graph-invariant ratio = {mirror['unsigned_graph_invariant_ratio']}  (isospin-blind)")
    print(f"    signed-graph det ratio @g_reeb = {mirror['signed_graph_det_ratio_at_g_reeb']}  (needs gated m; wrong)")
    print("\n  VERDICT:", verdict)
    print("  witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

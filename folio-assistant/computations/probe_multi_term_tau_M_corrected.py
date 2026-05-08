#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""Multi-term mass formula re-run under canonical τ_M (Wenzl-bridge).

This is `probe_multi_term_canonical.py` redone with the trace
functional CORRECTED per pr-442's selection theorem:

  prop:markov-trace-frobenius-selection
  (content/quantum-observable-universe/braids-and-knots/
   markov-trace-frobenius-selection.md, on pr-442)

The selection theorem proves that the QOU mass formula's
Frobenius co-Casimir construction
  C_dim_q = Σ_λ [1/(dim_q(λ)·τ(p_λ))]·p_λ
requires τ NON-DEGENERATE on every Wedderburn block. The
Schur-Weyl form τ_SW (with weights s_λ(q,q⁻¹)·d_λ/H_q(λ))
vanishes on height>2 blocks (Schur-Weyl vanishing theorem),
hence is degenerate. The canonical Markov trace is therefore
τ_M (Jones-Markov, Wenzl-bridge y_λ from Markov axioms).

The values in `D-tr-M-q0.derivation.json` (= 0.177437 for D)
and the parallel n/p registry files came from the polynomial
path `habiro_coefficients_atomic.py` which uses Schur-Weyl
weights — this is τ_SW, NOT τ_M, and was MISLABELED as
"canonical Markov trace".

The canonical τ_M values (Wenzl-bridge, Markov-axiom solve)
come from `from_scratch/wedderburn_markov.py` and the existing
`atomic-tr-m-wenzl-bridge.witness.json` on this branch:

  atom  | n_strands | τ_M (Wenzl-bridge) | τ_SW (registry, wrong-form)
  D     | 3         | 0.288326           | 0.177437
  T     | 5         | 0.012889           | (not in registry)
  ³He   | 3         | 0.998367           | (not in registry)
  p     | 3         | 0.998367           | 2.122583  (registry; convention TBD)
  n     | 3         | 0.998367           | 1.589393  (registry; convention TBD)

For p and n, the Wenzl-bridge witness gives 0.998367 (3-strand
SDP-canonical), versus registry's 2.123 / 1.589 (different
braid recipe + different weight convention). The current
investigation only re-runs the binding-energy assembly for D,
T, ³He where the Wenzl-bridge τ_M is unambiguous.

Output: `multi-term-tau-M-corrected.witness.json`
"""
from __future__ import annotations
import json
import sys
from itertools import combinations
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from atom_per_generator_volumes_sym import (  # noqa: E402
    atom_per_generator_volumes_sym, q, z_sym,
)
from q_parameter import Q as Q0_FLOAT  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# τ_M (Wenzl-bridge) values are stored at 50 dps in the wenzl-bridge witness;
# carry that precision through the assembly via mpmath. Final outputs are
# float for printing/JSON only.
mp.mp.dps = 50
m_e = mp.mpf(str(M_E_MEV))


def load_canonical_tau_M():
    """τ_M (Wenzl-bridge / Markov-axiom-derived) from the existing
    `atomic-tr-m-wenzl-bridge.witness.json` on this branch.

    These are the Frobenius-non-degenerate values per pr-442's
    selection theorem; the prior registry's `target_value` for
    `*-tr-M-q0.derivation.json` is τ_SW (Schur-Weyl, degenerate)
    and was MISLABELED as canonical."""
    w = json.loads((HERE / "atomic-tr-m-wenzl-bridge.witness.json").read_text())
    out = {}
    label_map = {
        "deuteron-2H":   "deuteron",
        "tritium-3H":    "tritium",
        "helium3-3He":   "helium-3",
        "proton":        "proton",
        "neutron":       "neutron",
        "electron":      "electron",
    }
    for r in w["results"]:
        out[label_map[r["atom"]]] = mp.mpf(r["tr_M_mixed_precision"])
    return out


def load_tau_SW_registry():
    """τ_SW from the (mislabeled) `*-tr-M-q0.derivation.json` registry.
    Loaded for side-by-side comparison only. Values are kept as strings
    (50-dp registry inputs) and converted to mpmath downstream."""
    out = {}
    for atom_short, label in [("p", "proton"), ("n", "neutron"), ("D", "deuteron")]:
        path = HERE / f"{atom_short}-tr-M-q0.derivation.json"
        out[label] = mp.mpf(str(json.loads(path.read_text())["target_value"]))
    return out


def vol_q_tower_at_q0(Z, N, q0):
    """Algebraic Vol_q^tower(β) at q_0 via symbolic Wedderburn port.
    Returns an mp.mpf at 50 dps, computed by evaluating the symbolic
    Vol_q^tower expression (Laurent in q^{1/2}) at q_0 to dps."""
    vols = atom_per_generator_volumes_sym(Z, N, include_inter=True)
    Vs = [mp.mpf(str(sp.N(vd["full"].subs(q, q0), 50))) for vd in vols]
    z0 = mp.mpf(str(sp.N(z_sym.subs(q, q0), 50)))
    n = len(Vs)
    prod = mp.mpf(1)
    for v in Vs:
        prod *= v
    single = z0 * sum(Vs)
    pair = z0**2 * sum(Vs[i]*Vs[j] for i, j in combinations(range(n), 2))
    return mp.fabs(prod) + single + pair


def main() -> int:
    q0 = sp.Rational(str(Q0_FLOAT))
    tau_M  = load_canonical_tau_M()
    tau_SW = load_tau_SW_registry()

    inv_2q = 1 / (q0 + 1/q0)
    T4_pervortex = m_e * (mp.mpf(2) + mp.mpf(str(sp.N(inv_2q, 50))))

    w_6term = json.loads((HERE / "mass-formula-6term.witness.json").read_text())
    T5 = {label: w_6term["rows"][label]["term5_bw_chirality_binding"]
          for label in ["D", "T", "3He"]}

    print("=" * 100)
    print("Multi-term mass formula — RE-RUN under canonical τ_M (Wenzl-bridge)")
    print("=" * 100)
    print()
    print(f"  Per pr-442 selection theorem: QOU mass formula needs τ_M (non-degenerate),")
    print(f"  NOT τ_SW (degenerate on height>2). Registry's `target_value` for")
    print(f"  *-tr-M-q0.derivation.json is τ_SW (mislabeled as canonical).")
    print()
    print(f"  q_0 = {float(q0):.10f}")
    print(f"  m_e = {float(m_e):.10f} MeV")
    print(f"  T4 (Frobenius co-Casimir, n=3) = m_e·(2+1/[2]_q) = {float(T4_pervortex):.6f} MeV")
    print()
    print(f"  Trace values side-by-side:")
    print(f"  {'atom':<10} {'τ_M (Wenzl-bridge)':<22} {'τ_SW (registry, wrong)':<22}")
    print(f"  " + "-" * 58)
    for label in ["deuteron", "tritium", "helium-3"]:
        tau_M_v  = tau_M.get(label)
        tau_SW_v = tau_SW.get(label)
        m_str  = f"{float(tau_M_v):.6f}"  if tau_M_v  is not None else "n/a"
        sw_str = f"{float(tau_SW_v):.6f}" if tau_SW_v is not None else "n/a"
        print(f"  {label:<10} {m_str:<22} {sw_str:<22}")
    print()

    # ³He is intentionally excluded — its τ_M entry in the wenzl-bridge
    # witness shares the bit-exact buggy 0.998… value with the
    # (also buggy) proton/neutron entries (per
    # probe_wenzl_bridge_witness_audit) and would require H_8 Wenzl-bridge
    # computation to verify. Re-include once a verified τ_M(³He) is
    # available (e.g. via PR #484's generalized per-λ infrastructure).
    atoms = [
        ("D",   "deuteron", 1, 1, 2.22456612, 1),
        ("T",   "tritium",  1, 2, 8.4817984,  1),
        # ("3He", "helium-3", 2, 1, 7.7180375,  1),  # τ_M unverified — see audit
    ]

    print(f"  Multi-term assembly under τ_M (CANONICAL):")
    print(f"  Note: ³He omitted — τ_M(³He) entry in wenzl-bridge witness is")
    print(f"        suspect per probe_wenzl_bridge_witness_audit; needs H_8.")
    print(f"  {'atom':<4} {'τ_M':<10} {'Vol_q':<8} {'T1':<9} {'T2+T3':<9} "
          f"{'T4':<7} {'T5':<10} {'B_naive':<9} {'AME':<8} {'err %':<10}")
    print("  " + "-" * 100)

    results = []
    for short, full_name, Z, N, ame, rho in atoms:
        t_atom = tau_M[full_name]
        T1 = m_e * rho * mp.fabs(t_atom)
        Vol_q = vol_q_tower_at_q0(Z, N, q0)
        T23 = m_e * Vol_q
        T4 = T4_pervortex
        T5_val = mp.mpf(str(T5[short]))
        T6 = mp.mpf(0)

        B_naive = T1 + T23 + T4 + T5_val + T6
        err = float((B_naive - ame) / ame * 100)

        # Comparison: same assembly under τ_SW (only D has a registry entry)
        if full_name in tau_SW:
            t_atom_sw = tau_SW[full_name]
            T1_sw = m_e * rho * mp.fabs(t_atom_sw)
            B_sw = T1_sw + T23 + T4 + T5_val + T6
            err_sw = float((B_sw - ame) / ame * 100)
        else:
            T1_sw, B_sw, err_sw = None, None, None

        print(f"  {short:<4} {float(t_atom):<10.4f} {float(Vol_q):<8.3f} "
              f"{float(T1):<9.4f} {float(T23):<9.4f} {float(T4):<7.4f} "
              f"{float(T5_val):<+10.4f} {float(B_naive):<9.4f} {ame:<8.4f} "
              f"{err:<+10.2f}")
        results.append({
            "atom": full_name, "Z": Z, "N": N, "rho": rho,
            "tau_M_canonical_wenzl_bridge": mp.nstr(t_atom, 30),
            "tau_SW_registry_mislabeled": (mp.nstr(tau_SW[full_name], 30)
                                           if full_name in tau_SW else None),
            "Vol_q_tower": mp.nstr(Vol_q, 30),
            "T1_descended_MeV_under_tau_M":  mp.nstr(T1, 30),
            "T1_descended_MeV_under_tau_SW": (mp.nstr(T1_sw, 30)
                                              if T1_sw is not None else None),
            "T2_T3_brane_MeV":   mp.nstr(T23, 30),
            "T4_frobenius_MeV":  mp.nstr(T4, 30),
            "T5_chirality_MeV":  float(T5_val),
            "T6_habiro_MeV":     float(T6),
            "B_naive_under_tau_M_MeV":  mp.nstr(B_naive, 20),
            "B_naive_under_tau_SW_MeV": (mp.nstr(B_sw, 20)
                                         if B_sw is not None else None),
            "AME_binding_MeV": ame,
            "err_pct_tau_M":  err,
            "err_pct_tau_SW": err_sw,
        })
    print()
    print("  Comparison vs. τ_SW assembly (PR #475's `multi-term-canonical-assembly.witness.json`):")
    for r in results:
        if r["B_naive_under_tau_SW_MeV"] is not None:
            dT1 = float(mp.mpf(r["T1_descended_MeV_under_tau_M"])
                       - mp.mpf(r["T1_descended_MeV_under_tau_SW"]))
            print(f"    {r['atom']:<10}: τ_M → {r['err_pct_tau_M']:+.2f}%   "
                  f"τ_SW → {r['err_pct_tau_SW']:+.2f}%   "
                  f"(ΔT1 = {dT1:+.4f} MeV)")
    print()
    print("  Note: T2+T3 (algebraic Vol_q^tower) is unchanged — it depends only on")
    print("        per-generator volumes, not on the trace functional. T1 is the only")
    print("        term that shifts under the τ_M-vs-τ_SW correction.")

    w = (
        WitnessBuilder("multi-term-tau-M-corrected", engine="sympy+mpmath")
        .set_description(
            "Multi-term mass formula assembly RE-RUN under canonical τ_M "
            "(Wenzl-bridge / Markov-axiom-derived) per pr-442's selection "
            "theorem (prop:markov-trace-frobenius-selection). The earlier "
            "`multi-term-canonical-assembly.witness.json` (PR #475) used "
            "τ_SW from `D-tr-M-q0.derivation.json`'s `target_value` field; "
            "that value is τ_SW (Schur-Weyl, degenerate on height>2), "
            "NOT τ_M (Jones-Markov, non-degenerate). The QOU mass "
            "formula's Frobenius co-Casimir construction requires "
            "non-degeneracy, hence τ_M is canonical. Only T1 shifts; "
            "T2+T3+T4+T5+T6 are unchanged."
        )
        .add_parameter("q_0", float(q0))
        .add_parameter("m_e_MeV", m_e)
        .add_parameter("T4_pervortex_MeV", T4_pervortex)
        .add_parameter("tau_M_source", "atomic-tr-m-wenzl-bridge.witness.json")
        .add_parameter("tau_SW_source", "{D,n,p}-tr-M-q0.derivation.json (mislabeled)")
        .add_parameter("selection_theorem_ref",
                       "prop:markov-trace-frobenius-selection (pr-442)")
        .add_data("results", results)
    )
    out_path = w.save()
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

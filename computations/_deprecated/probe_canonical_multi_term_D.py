#!/usr/bin/env python3
"""Probe the literal multi-term formula on D with the CANONICAL tr_M.

`tr_M(D, q_0)` is loaded at runtime from the derivation-chain
registry `D-tr-M-q0.derivation.json` (PR #473), whose chain
derives the value step-by-step from the 7 first-principles
entrypoints (Hecke.Energy, Wedderburn, Schur, …). PR #472's
`prop:habiro-residue-sum-equivalence` cross-validates the
registry value via two independent paths (polynomial-ring +
residue-spectral-sum) at relative tolerance ≤ 10⁻⁹. The
canonical value at the time of writing is
  tr_M(D, q_0) = 0.17743692421543206
but the probe always reads `target_value` from the registry
JSON so it tracks any future re-derivations automatically.

This probe re-tests the LITERAL paper formulas under that
canonical convention:

  (S1) Single-term:     B = m_e · ρ · |tr_M(T_w)|
  (S2) +T4 Frobenius:   B = m_e · ρ · |tr_M(T_w)| + m_e · tr_M(C_dim_q)
  (S3) +T2+T3 brane:    S2 + Σ Φ_q(|V|) + z²·Σ Φ_q(|V V|)
  (S4) +T5 chirality:   S3 + a_K · B_bulk
  (S5) +T6 Habiro:      S4 + Habiro residue (placeholder = 0)

And per the paper's prose:
  (P1) descended ALONE: m_e · |tr_M(T_w)|     (no ρ)
  (P2) trace deficit:   E_0 · ||tr_M(free)| - |tr_M(atom)||  (compute heuristic)

For each, report B_pred vs AME and residual %.

NO census data used — T_w(D) is the GB-NF reduction of the
canonical 3A-strand atom braid `atom_braid_word_3A(1, 1)`, period.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from q_parameter import Q as Q0_FLOAT  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402

mp.mp.dps = 50
q = mp.mpf(repr(Q0_FLOAT))

# --- canonical tr_M(D) at q_0, loaded from the registered derivation
# chain `D-tr-M-q0.derivation.json` (PR #473 registry). The chain
# derives the value step-by-step from the 7 first-principles
# entrypoints (Hecke.Energy, Wedderburn, Schur, …); PR #472's
# `prop:habiro-residue-sum-equivalence` cross-validates via two
# independent paths (polynomial-ring + residue-spectral-sum) at
# relative tolerance ≤ 10⁻⁹. Loading from the registry keeps the
# value in a single source of truth.
_REGISTRY_PATH = HERE / "D-tr-M-q0.derivation.json"
with _REGISTRY_PATH.open() as _f:
    TR_M_D_ATOM_ATQ0 = mp.mpf(str(json.load(_f)["target_value"]))
TR_M_D_FREE = mp.mpf("0")  # placeholder; paper requires "free" T_w too

# AME deuteron binding
B_AME_D_MEV = 2.22456612

# Structural ρ for D (paper: ℓ ≤ 1 rule → 1; SDP: 1)
RHO_D = 1


def main() -> int:
    print("=" * 95)
    print("Multi-term formula probe on D — canonical tr_M from symbolic chain")
    print("=" * 95)
    print(f"  tr_M(T_w(D))|_{{q_0}} = +{mp.nstr(TR_M_D_ATOM_ATQ0, 30)}")
    print(f"  ρ(D) = {RHO_D}")
    print(f"  m_e (CODATA)        = {M_E_MEV} MeV")
    print(f"  AME B(D)            = {B_AME_D_MEV} MeV")
    print()

    m_e = mp.mpf(str(M_E_MEV))
    abs_tr = abs(TR_M_D_ATOM_ATQ0)

    # T1 (descended): |tr_M(T_w)|
    T1 = abs_tr  # dimensionless

    # T4 (Frobenius co-Casimir): m_e · Σ_λ 1/dim_q(λ) for n_0 = 3 (per-vortex)
    # From prop:knot-mass-formula-unified §"single-vortex (n=3)":
    #     Σ 1/dim_q = 2 + 1/[2]_q ≈ 1.2762/m_e (so the m_e prefactor gives ~1.276 MeV)
    # For D, the paper text suggests per-vortex (n=3) Frobenius applies, giving
    # T4 ≈ 1.276 MeV. We compute it canonically:
    inv_2q = 1 / (q + 1/q)  # 1/[2]_q = 1/(q+q^-1)... wait, [2]_q = q+q^-1, so 1/[2]_q = 1/(q+q^-1)
    sum_inv_dim_n3 = mp.mpf(2) + inv_2q  # 2 hooks + 1 from (2,1) — wait, n=3 partitions
    # Recompute properly: n=3 partitions (3), (2,1), (1,1,1) with dim_q = 1, [2]_q, 1
    # so Σ 1/dim_q = 1 + 1/[2]_q + 1 = 2 + 1/[2]_q
    T4_pervortex_MeV = m_e * sum_inv_dim_n3
    print(f"  T4 per-vortex (Frobenius, n=3) = m_e · (2 + 1/[2]_q) = "
          f"{mp.nstr(T4_pervortex_MeV, 12)} MeV")

    # T2, T3, T5, T6: pull from the regenerated `mass-formula-6term.witness.json`.
    # The brane-tower terms use the canonical `Φ_q(|V_i^full|)` formula with
    # the `full` channel extracted from `atom_per_generator_volumes` (the
    # earlier silent-bug version returned dicts and silently caught the
    # TypeError, leaving T2=T3=0). Witness `rows` has top-level dict keyed
    # on iso label.
    witness_path = HERE / "mass-formula-6term.witness.json"
    T2_raw = T3_raw = T5_raw = T6_raw = mp.mpf(0)
    if witness_path.exists():
        try:
            w = json.loads(witness_path.read_text())
            d_row = w.get("rows", {}).get("D", {})
            t23 = d_row.get("term23_tower_atom", {})
            T2_raw = mp.mpf(str(t23.get("single", 0)))   # dimensionless Φ_q sum
            T3_raw = mp.mpf(str(t23.get("pair", 0)))      # dimensionless (z² folded in)
            T5_raw = mp.mpf(str(d_row.get("term5_bw_chirality_binding", 0)))  # already MeV
            T6_raw = mp.mpf(0)  # placeholder
        except Exception as e:
            print(f"  [warn] could not load mass-formula-6term witness: {e}")

    # Convert dimensionless brane-tower to MeV via m_e prefactor (Option A
    # from docs/paper-formula-reconciliation-diagnostic.md).
    T2_MeV = m_e * T2_raw
    T3_MeV = m_e * T3_raw
    T5_MeV = T5_raw       # already MeV in witness
    T6_MeV = T6_raw       # placeholder

    print(f"  T2 (brane single, dimensionless Σ Φ_q) = {float(T2_raw):.4e} → "
          f"× m_e = {float(T2_MeV):.4e} MeV")
    print(f"  T3 (brane pair, dimensionless z²·Σ Φ_q²) = {float(T3_raw):.4e} → "
          f"× m_e = {float(T3_MeV):.4e} MeV")
    print(f"  T5 (BW chirality, MeV)               = {float(T5_MeV):+.6f} MeV")
    print(f"  T6 (Habiro residue, placeholder)     = {float(T6_MeV):+.6f} MeV")
    print()
    print(f"  ⚠ T2 and T3 are DIVERGENT (Φ_q has a pole at z=1; D's atom "
          f"volumes are ~0.99, near the pole).")
    print(f"  ⚠ Naive sum of literal multi-term formula gives nonsense.")
    print()

    # --- Variant assembles ---
    # Convention: each dimensionless term gets m_e prefactor when added in MeV.
    # The paper's two top-level forms are:
    #   single-term:  B = m_e · ρ · |tr_M|         (deuteron prediction)
    #   unified:      m = |tr_M| + Σ Φ_q + ... + m_e · tr_M(C)
    # Treating the unified form as if every term is in m_e units:
    variants = {}
    variants["S1: m_e · ρ · |tr_M|"] = m_e * RHO_D * abs_tr
    variants["S2: + T4 Frobenius (m_e · (2 + 1/[2]_q))"] = (
        m_e * RHO_D * abs_tr + T4_pervortex_MeV
    )
    variants["S3: + T2 + T3 brane"] = (
        m_e * RHO_D * abs_tr + T4_pervortex_MeV + T2_MeV + T3_MeV
    )
    variants["S4: + T5 chirality"] = (
        m_e * RHO_D * abs_tr + T4_pervortex_MeV + T2_MeV + T3_MeV + T5_MeV
    )
    variants["S5: + T6 Habiro (placeholder)"] = (
        m_e * RHO_D * abs_tr + T4_pervortex_MeV + T2_MeV + T3_MeV + T5_MeV + T6_MeV
    )

    print(f"  {'variant':<48} {'B_pred [MeV]':>15} {'err [%]':>10}")
    print(f"  {'-'*48} {'-'*15} {'-'*10}")
    for label, B in variants.items():
        err = (float(B) - B_AME_D_MEV) / B_AME_D_MEV * 100
        marker = " ← matches AME" if abs(err) < 5 else (" (still off)" if abs(err) > 50 else "")
        print(f"  {label:<48} {float(B):>15.6f} {err:>+10.2f}%{marker}")
    print()

    # Conclusion
    best_label = min(variants.keys(),
                     key=lambda k: abs(float(variants[k]) - B_AME_D_MEV))
    print(f"  Best literal-formula variant: {best_label}")
    print(f"    → B_pred = {float(variants[best_label]):.6f} MeV "
          f"({(float(variants[best_label]) - B_AME_D_MEV) / B_AME_D_MEV * 100:+.2f}%)")

    # Compare to compute's heuristic (NOT in paper)
    # The compute uses E_0 · |tr_M(free) - tr_M(atom)|, but free vs atom for D
    # both come from the same 3A-strand construction with include_inter ∈ {False, True}.
    # We don't have tr_M(free) symbolic yet; that's a next step.
    print()
    print(f"  Note on compute heuristic (E_0 · |tr_M(free) - tr_M(atom)|, NOT in paper):")
    print(f"    Requires both tr_M(T_w(D, free)) and tr_M(T_w(D, atom)) symbolic.")
    print(f"    Atom value: +{mp.nstr(TR_M_D_ATOM_ATQ0, 12)} (this branch's symbolic).")
    print(f"    Free value: TODO — symbolic with include_inter=False.")
    print()

    out = {
        "computation": "probe-canonical-multi-term-D",
        "description": (
            "Tests literal multi-term formula on D with canonical tr_M "
            "loaded at runtime from D-tr-M-q0.derivation.json (PR #473 "
            "derivation-chain registry, cross-validated by PR #472's "
            "habiro-residue-sum-equivalence). NO census data; T_w(D) is "
            "the GB-NF reduction of atom_braid_word_3A(1, 1)."
        ),
        "tr_M_D_atom_q0_canonical": str(TR_M_D_ATOM_ATQ0),
        "AME_B_D_MeV": B_AME_D_MEV,
        "rho_D": RHO_D,
        "T4_pervortex_MeV": str(T4_pervortex_MeV),
        "T2_MeV": str(T2_MeV),
        "T3_MeV": str(T3_MeV),
        "T5_MeV": str(T5_MeV),
        "T6_MeV": str(T6_MeV),
        "variants": {k: {"B_pred_MeV": float(v),
                         "err_pct": (float(v) - B_AME_D_MEV) / B_AME_D_MEV * 100}
                     for k, v in variants.items()},
        "best_variant": best_label,
    }
    out_path = HERE / "probe-canonical-multi-term-D.witness.json"
    with open(out_path, "w") as fp:
        json.dump(out, fp, indent=2)
    print(f"  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

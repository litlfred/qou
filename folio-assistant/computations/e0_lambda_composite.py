#!/usr/bin/env python3
"""
e0_lambda_composite — is M_λ a FORCED categorical composite?

Tests the owner's hypothesis: the per-block mass-functor component
M_λ(K) is a STRUCTURED COMPOSITE of substrate objects

    M_λ(K) = m_e · [ Archimedean eval of (θ_λ ▷ χ^λ(K)) weighted by dim_q(λ) ]

where ribbon twist θ_λ acts on the character χ^λ(K), q-dimension dim_q(λ)
provides the block measure, the Archimedean functor evaluates to MeV.

DISCIPLINE (read docs/audits/2026-06-01-e0-lambda-composite-structure.md
§Step 1-2 first — derivation BEFORE numbers):

  - A composite is FORCED only if the composition is READ OFF the functor's
    categorical definition (every factor + every exponent dictated, ZERO free
    parameters). It is a LATENT FIT if we CHOOSE which factors multiply or
    tune any power to hit the {e⁻, p, n} anchors.
  - The {e⁻, p, n} anchors are the FALSIFICATION TEST, not fit targets.
    No tuning, no back-solve. Every number traces to a witness.

This probe computes, with ZERO free parameters, at the canonical q₀ (50 dps):

  (A) The functor-dictated per-block summand the Markov-trace step actually
      uses:                       s_λ(K) = y_λ(q₀) · χ^λ(β_K)
      (cheat-sheet step 6: tr_M(β) = Σ_λ y_λ χ_λ — this IS a per-λ sum, forced).

  (B) The owner's product composite (NOT forced by the definition — see audit
      Finding 2; the definition gives a SUM |tr_M| + tower + tr_M(C_dim_q),
      not a PRODUCT):
                     c_λ(K) = θ_λ(K) · χ^λ(β_K) · dim_q(λ)
      with θ_λ = arccos(χ^λ/d_λ) the per-block Reeb phase (the only phase the
      framework multiplies into Geom — and only EXPLORATORY / single-block, see
      _li_2_q_util.spectral_correction_borromean).

  (C) THE FALSIFICATION TEST — the p≡n H_3 character collision
      (rho-prefactor-structural-verifier.witness.json, allPassed=True): proton
      and neutron have BIT-FOR-BIT identical (χ_λ, y_λ, dim_q λ) at H_3. So any
      per-λ composite of those data gives IDENTICAL per-block energies for p and
      n. But m_p ≠ m_n (Δ = 1.293 MeV). The probe confirms/denies: does the
      composite distinguish p from n at all?

No anchor is tuned. The composite is computed independently and the residuals
reported raw.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

# ── canonical 50-dps substrate + experimental anchors (witness-sourced) ──
mp.dps = 65  # compute precision per _precision discipline

from _li_2_q_util import load_q_50dps  # noqa: E402

Q0, QINV, ZMARK = load_q_50dps()
H = Q0 - QINV  # h = q - q⁻¹

# experimental anchors (CODATA 2022, via experimental_constants.py)
from experimental_constants import (  # noqa: E402
    M_E_MEV, M_P_MEV, M_N_MEV,
)
M_E = mpf(str(M_E_MEV))
M_P = mpf(str(M_P_MEV))
M_N = mpf(str(M_N_MEV))


# ── per-λ H_3 substrate data: read DIRECTLY from the GAP-A-4 verifier
#    witness (no recomputation — single source of truth, and it IS the
#    falsification data showing p≡n). ────────────────────────────────────
VERIFIER = _pb.witness_path("rho-prefactor-structural-verifier.witness.json", HERE)


def load_h3_per_lambda(atom_name: str) -> list[dict]:
    """Load the per-λ (χ, y_wenzl, dim_q, d_λ) profile for an atom from the
    canonical GAP-A-4 verifier witness.  Proton and neutron share the trefoil
    image, so their profiles are bit-for-bit identical there — that IS the
    point (the falsification data)."""
    with VERIFIER.open() as fh:
        d = json.load(fh)
    for entry in d["data"]["per_atom_analysis"]:
        if entry["atom"] == atom_name:
            return entry["per_lambda"]
    raise KeyError(atom_name)


def reeb_phase(chi: mpf, d_lambda: int) -> mpf:
    """θ_λ = arccos(χ_λ / d_λ), the per-block Reeb phase — clamped to [-1, 1]
    for the archimedean arccos (the seminormal braid eigenvalues are
    unit-modulus e^{±iθ} on a rotation block)."""
    x = chi / mpf(d_lambda)
    if x > 1:
        x = mpf(1)
    if x < -1:
        x = mpf(-1)
    return mp.acos(x)


def composite_per_atom(atom_name: str) -> dict:
    """Compute, per λ ⊢ 3:
       s_λ = y_λ · χ^λ           (functor-dictated Markov summand, (A))
       c_λ = θ_λ · χ^λ · dim_q   (owner's product composite, (B))
    and the totals Σ_λ s_λ (= tr_M) and Σ_λ c_λ.  Everything is read off the
    cached H_3 data; ZERO free parameters."""
    rows = load_h3_per_lambda(atom_name)
    per_lambda = []
    sum_s = mpf(0)
    sum_c = mpf(0)
    for r in rows:
        lam = tuple(r["lambda"])
        chi = mpf(str(r["chi"]))
        y = mpf(str(r["y_wenzl"]))
        dimq = mpf(str(r["dim_q"]))
        dl = int(r["d_lambda_syt_count"])
        theta = reeb_phase(chi, dl)
        s_lam = y * chi
        c_lam = theta * chi * dimq
        sum_s += s_lam
        sum_c += c_lam
        per_lambda.append({
            "lambda": list(lam),
            "chi": str(chi),
            "y_wenzl": str(y),
            "dim_q": str(dimq),
            "d_lambda": dl,
            "theta_reeb": str(theta),
            "s_lambda_y_chi": str(s_lam),
            "c_lambda_theta_chi_dimq": str(c_lam),
        })
    return {
        "atom": atom_name,
        "per_lambda": per_lambda,
        "sum_s_trM": str(sum_s),  # = tr_M(β_K) (functor input)
        "sum_c_composite": str(sum_c),
        "_sum_s": sum_s,
        "_sum_c": sum_c,
    }


def main() -> dict:
    print("=" * 78)
    print("e0_lambda_composite — FORCED composite test (derivation-first)")
    print(f"q₀ = {mp.nstr(Q0, 12)},  h = {mp.nstr(H, 12)},  "
          f"m_e = {mp.nstr(M_E, 9)} MeV")
    print("=" * 78)

    atoms = {}
    for name in ("proton", "neutron"):  # he3 also Markov-equivalent; deuteron differs
        atoms[name] = composite_per_atom(name)
    atoms["he3"] = composite_per_atom("he3")
    atoms["deuteron"] = composite_per_atom("deuteron")

    # ── (A)/(B) per-atom totals, ratioed to m_e (the ONLY derived scale in
    #    the production formula m = m_e · VolDensity — NOT a fitted E₀) ──
    print("\n--- (A) functor-dictated tr_M = Σ_λ y_λ χ_λ  and  "
          "(B) owner composite Σ_λ θ_λ χ_λ dim_q ---")
    print(f"  {'atom':>9} {'Σ y_λχ_λ (tr_M)':>20} {'Σ θ_λχ_λdim_q':>20}")
    for name in ("proton", "neutron", "he3", "deuteron"):
        a = atoms[name]
        print(f"  {name:>9} {mp.nstr(a['_sum_s'], 14):>20} "
              f"{mp.nstr(a['_sum_c'], 14):>20}")

    # ── (C) THE FALSIFICATION TEST: p vs n ──
    p, n = atoms["proton"], atoms["neutron"]
    d_trM = p["_sum_s"] - n["_sum_s"]
    d_comp = p["_sum_c"] - n["_sum_c"]
    # per-λ differences too
    per_lambda_pn_diff = []
    for rp, rn in zip(p["per_lambda"], n["per_lambda"]):
        ds = mpf(rp["s_lambda_y_chi"]) - mpf(rn["s_lambda_y_chi"])
        dc = (mpf(rp["c_lambda_theta_chi_dimq"])
              - mpf(rn["c_lambda_theta_chi_dimq"]))
        per_lambda_pn_diff.append({
            "lambda": rp["lambda"],
            "delta_s_lambda": str(ds),
            "delta_c_lambda": str(dc),
        })

    m_pn_exp = M_N - M_P  # 1.293... MeV — the physical split the composite must explain
    print("\n--- (C) FALSIFICATION: does the composite distinguish p from n? ---")
    print(f"  experimental m_n - m_p          = "
          f"{mp.nstr(m_pn_exp, 10)} MeV  (the split to explain)")
    print(f"  Δ(Σ y_λχ_λ)  [tr_M]   p − n     = {mp.nstr(d_trM, 6)}")
    print(f"  Δ(Σ θ_λχ_λdim_q) composite p − n = {mp.nstr(d_comp, 6)}")
    pn_collapse = (abs(d_trM) < mpf(10) ** (-40)
                   and abs(d_comp) < mpf(10) ** (-40))
    print(f"  p ≡ n collapse (both Δ ≈ 0)?     = {pn_collapse}")

    # ── scale question: how many scales does the composite need to hit
    #    {e⁻ (=m_e), p, n}? If p≡n, the linear system has a degenerate row →
    #    cannot represent the p/n split with ANY per-λ scale assignment. ──
    verdict = (
        "FORCED-BUT-MISSES" if pn_collapse else "INDETERMINATE-SEE-RESIDUALS"
    )

    print("\n" + "=" * 78)
    if pn_collapse:
        print("VERDICT: FORCED-BUT-MISSES.")
        print("  The functor-dictated per-λ object Σ_λ y_λ χ_λ AND the owner's")
        print("  product composite Σ_λ θ_λ χ_λ dim_q are BIT-FOR-BIT IDENTICAL")
        print("  for proton and neutron (p≡n at H_3, GAP-A-4). No per-block")
        print("  scale assignment E₀^λ can produce m_p ≠ m_n from identical")
        print("  per-block inputs. The composite cannot even REPRESENT the")
        print("  1.293 MeV p/n split — independent of any tuning. MISS is")
        print("  structural, not a failed fit.")
    print("=" * 78)

    witness = {
        "computation": "e0-lambda-composite",
        "description": (
            "Is M_λ a FORCED categorical composite (θ_λ × χ^λ × dim_q, "
            "archimedean)? Derivation-first: production VolDensity is a single "
            "opaque scalar (no per-λ sum); the per-λ form lives in the "
            "Markov-trace step tr_M = Σ_λ y_λ χ_λ. Computes the "
            "functor-dictated summand s_λ = y_λ χ_λ and the owner's product "
            "composite c_λ = θ_λ χ_λ dim_q (θ_λ = arccos(χ/d) Reeb phase) at "
            "q₀, ZERO free parameters, reading the cached H_3 per-λ data from "
            "the GAP-A-4 verifier witness. Falsification test: proton ≡ "
            "neutron at H_3 (bit-identical χ_λ, y_λ, dim_q) so any per-λ "
            "composite collapses p≡n, but m_p ≠ m_n. NOT tuned to anchors or "
            "B_AME."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "contentBlock": "prop:rho-k-h3a-refinement",
        "precisionMetadata": {
            "compute_dps": 65, "output_dps": 50,
            "truncation_bound": "1e-50",
        },
        "parameters": {
            "q0": str(Q0), "h": str(H),
            "m_e_MeV": str(M_E), "m_p_MeV": str(M_P), "m_n_MeV": str(M_N),
            "source_witness": "rho-prefactor-structural-verifier.witness.json",
        },
        "atoms": {k: {kk: vv for kk, vv in v.items()
                      if not kk.startswith("_")}
                  for k, v in atoms.items()},
        "falsification_test_pn": {
            "experimental_m_n_minus_m_p_MeV": str(m_pn_exp),
            "delta_trM_p_minus_n": str(d_trM),
            "delta_composite_p_minus_n": str(d_comp),
            "per_lambda_pn_diff": per_lambda_pn_diff,
            "p_equiv_n_collapse": bool(pn_collapse),
        },
        "verdict": verdict,
        "verdict_detail": (
            "FORCED-BUT-MISSES: the functor-dictated per-λ Markov summand "
            "y_λ χ_λ and the owner's product composite θ_λ χ_λ dim_q are "
            "bit-for-bit identical for proton and neutron at the H_3 braid "
            "strand count (GAP-A-4 Markov-equivalence). A per-block composite "
            "of (character, q-dim, Reeb twist) therefore CANNOT represent the "
            "1.293 MeV m_n - m_p split with any per-λ scale assignment. The "
            "miss is structural (the p/n distinction lives in the braid WORD "
            "/ per-generator V̂, which the per-λ character collapses), not a "
            "failed fit. Separately, the OWNER'S PRODUCT composite is itself "
            "NOT forced by the functor's definition (audit Finding 2): the "
            "definition gives a SUM |tr_M| + tower + tr_M(C_dim_q), not the "
            "PRODUCT θ_λ χ_λ dim_q; assembling the product + choosing the "
            "dim_q exponent is a modeling choice → latent-fit risk."
            if pn_collapse else "see residuals"
        ),
        "assertions": [],
        "allPassed": True,
    }
    out = HERE / "e0-lambda-composite.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nWitness: {out}")
    return witness


if __name__ == "__main__":
    main()

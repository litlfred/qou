#!/usr/bin/env python3
"""
Plan F — Terms 2 + 3 (single- and pair-generator brane tower) at MPFR @ 50 dps.

Term 2 = Σ_{i=0..n-2} Φ_q(|V̂_i^full|)
Term 3 = z² · Σ_{i<j} Φ_q(|V̂_i^full · V̂_j^full|)

where:
    Φ_q(z) = ∏_{k≥1} (1 − q^{-k}·z)^{-1}    (quantum dilogarithm)
    V̂_i^full = w_sym·V_sym(σ_i) + w_std·V_std(σ_i) + w_alt·V_alt(σ_i)
    z = 1/(√q + 1/√q)                       (Markov parameter)
    w_λ = dim_q(λ)² / [n]!_q                  (Wedderburn weights)

The per-channel V_sym, V_std, V_alt are computed from the multi-Hecke-
factor crossings dictionary (one list per generator; each list element
is a (c, d) coefficient pair).

This script ports `mass_endomorphism.py` from f64 to mpmath at 50 dps
for the proton, neutron, and electron Hecke elements.

Output: `terms-2-3-brane-tower-mpfr-50dps.witness.json`
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

from mpmath import mp, mpf, sqrt as mp_sqrt

mp.dps = 50

HERE = Path(__file__).parent
import sys
sys.path.insert(0, str(HERE))
Q0 = HERE / "q-pinning-50-digit.witness.json"
OUT = HERE / "terms-2-3-brane-tower-mpfr-50dps.witness.json"

M_E_MEV = mpf("0.51099895")


from _phi_q_util import phi_q as Phi_q  # noqa: E402  (after sys.path setup)


def additive_wedderburn_volumes(crossings_per_gen, n_gens, q, h, w_sym, w_std, w_alt, z_mark):
    """V̂_i^full per generator via additive Wedderburn (mpmath)."""
    q_inv = mpf(1) / q
    vols = []
    for gen in range(n_gens):
        a, b = mpf(0), mpf(1)
        sp_, ap_ = mpf(1), mpf(1)
        for c, d in crossings_per_gen.get(gen, []):
            a_new = a * c * h + a * d + b * c
            b_new = a * c + b * d
            a, b = a_new, b_new
            sp_ *= c * q + d
            ap_ *= -c * q_inv + d
        Vs = z_mark * a + b
        Vf = w_sym * sp_ + w_std * Vs + w_alt * ap_
        vols.append({"std": Vs, "sym": sp_, "alt": ap_, "full": Vf})
    return vols


def terms_2_3(vols, q_inv, z_mark):
    """Term 2 = Σ Φ_q(|V̂_i|); Term 3 = z² · Σ_{i<j} Φ_q(|V̂_i V̂_j|)."""
    n = len(vols)

    term2 = mpf(0)
    for v in vols:
        term2 += Phi_q(mp.fabs(v["full"]), q_inv)

    term3 = mpf(0)
    for i in range(n):
        for j in range(i + 1, n):
            prod = mp.fabs(vols[i]["full"] * vols[j]["full"])
            term3 += z_mark * z_mark * Phi_q(prod, q_inv)

    return term2, term3


def main() -> int:
    q_str = json.load(open(Q0))["derived_50_digit"]["q"]
    q = mpf(q_str)
    q_inv = mpf(1) / q
    h = q - q_inv
    z_mark = mpf(1) / (mp_sqrt(q) + mp_sqrt(q_inv))
    print(f"  q_0 = {q_str}")
    print(f"  h = q - 1/q = {h}")
    print(f"  z = 1/(√q + 1/√q) = {z_mark}")

    # Wedderburn weights at n=3 (for proton/neutron baryon level).
    # dim_q((3)) = 1, dim_q((2,1)) = [3]_q/[2]_q is computed via q-hook,
    # but the weights w_sym + w_std + w_alt = 1 normalisation holds.
    # Use the same formula as full-tower-mass.witness.json:
    #   w_λ = dim_q(λ)² / [n]!_q with n=3 normalisation.
    # At q_0 the witness reports w_sym = 0.16546, w_std = 0.66907, w_alt = 0.16546.
    # Compute exactly in mpmath via q-integers:
    def q_int(k):
        if k == 0:
            return mpf(0)
        return sum(q ** (k - 1 - 2 * i) for i in range(k))

    q_fact_3 = q_int(1) * q_int(2) * q_int(3)
    dim_q_3 = mpf(1)
    dim_q_21 = q_int(3) * q_int(2) * q_int(1) / (q_int(3) * q_int(1) * q_int(1))
    dim_q_111 = mpf(1)
    w_sym = dim_q_3 ** 2 / q_fact_3
    w_std = dim_q_21 ** 2 / q_fact_3
    w_alt = dim_q_111 ** 2 / q_fact_3
    wt = w_sym + w_std + w_alt
    w_sym /= wt
    w_std /= wt
    w_alt /= wt
    print(f"  w_sym = {w_sym}")
    print(f"  w_std = {w_std}")
    print(f"  w_alt = {w_alt}")

    HA = h  # alias

    # Crossings per particle (same as mass_endomorphism.py)
    particles = {
        "electron": {
            "crossings": {0: [(mpf(1), mpf(0))] * 3},
            "n_gens": 1,
        },
        "proton": {
            "crossings": {
                0: [(mpf(1), mpf(0))] * 3              # B₃: 3 × σ₀
                   + [(mpf(1), mpf(0))]                  # uu quark pair
                   + [(mpf(1), -HA / 2)]                  # ud quark pair
                   + [(mpf(1), mpf(0))] * 2,              # 2 gluon self-coupling
                1: [(mpf(1), -HA)] * 3                   # B₃: 3 × σ₁⁻¹
                   + [(mpf(1), -HA / 2)],                 # ud quark pair
            },
            "n_gens": 2,
        },
        "neutron": {
            "crossings": {
                0: [(mpf(1), mpf(0))] * 3
                   + [(mpf(1), -HA)]                      # dd quark pair (σ⁻¹)
                   + [(mpf(1), -HA / 2)]                  # ud
                   + [(mpf(1), mpf(0))] * 2,
                1: [(mpf(1), -HA)] * 3
                   + [(mpf(1), -HA / 2)],
            },
            "n_gens": 2,
        },
    }

    rows = []
    for label, p in particles.items():
        vols = additive_wedderburn_volumes(
            p["crossings"], p["n_gens"], q, h, w_sym, w_std, w_alt, z_mark,
        )
        term2, term3 = terms_2_3(vols, q_inv, z_mark)
        # The original mass_endomorphism formula gives the SUM
        #   𝔪 = |Π V̂| + Σ Φ_q(|V̂|) + Σ z² · Φ_q(|V̂_i V̂_j|)
        # as the categorical mass (not a binding energy; a mass).
        # Term 2 and Term 3 here are the brane-tower contributions.
        # Multiply by m_e to convert to MeV.
        term2_mev = M_E_MEV * term2
        term3_mev = M_E_MEV * term3
        print(f"\n  === {label} ===")
        for i, v in enumerate(vols):
            print(f"    V̂_{i}: full = {v['full']}, sym = {v['sym']}, std = {v['std']}, alt = {v['alt']}")
        print(f"    Term 2 (Σ Φ_q(|V̂|)) = {term2}")
        print(f"    Term 3 (z² Σ Φ_q(|V̂_i V̂_j|)) = {term3}")
        print(f"    Term 2 × m_e = {term2_mev} MeV")
        print(f"    Term 3 × m_e = {term3_mev} MeV")
        rows.append({
            "particle": label,
            "n_gens": p["n_gens"],
            "wedderburn_vols": [
                {k: str(vv) for k, vv in v.items()} for v in vols
            ],
            "term2_50dps": str(term2),
            "term3_50dps": str(term3),
            "term2_b_pred_mev_50dps": str(term2_mev),
            "term3_b_pred_mev_50dps": str(term3_mev),
        })

    out = {
        "computation": "terms-2-3-brane-tower-mpfr-50dps",
        "description":
            "Plan F — Terms 2 (single-generator) and 3 (pair-generator) "
            "of the unified mass formula at MPFR @ 50 dps via the "
            "quantum dilogarithm Φ_q(z) = Π (1 − q^{-k}·z)^{-1}. Ports "
            "mass_endomorphism.py from f64 to mpmath. Restricted to "
            "{electron, proton, neutron} since their crossing chains "
            "are explicit; heavier-atom crossings via atom_per_generator_"
            "volumes need a separate port.",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "precision": "mpfr_50dps",
        "q_0_50dps": q_str,
        "h_50dps": str(h),
        "z_markov_50dps": str(z_mark),
        "wedderburn_weights": {
            "w_sym_50dps": str(w_sym),
            "w_std_50dps": str(w_std),
            "w_alt_50dps": str(w_alt),
        },
        "phi_q_definition": "Φ_q(z) = Π_{k≥1} (1 − q^{-k}·z)^{-1}",
        "phi_q_truncation": "max_k=2000, eps=1e-55",
        "results": rows,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n  Output: {OUT.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Plan F — Terms 2 + 3 for heavier atoms via 3A-strand atom braid.

Ports `hecke_core.atom_per_generator_volumes` to mpmath @ 50 dps.
Computes per-generator V̂_i^full, then:
    Term 2 = Σ_i Φ_q(|V̂_i^full|)
    Term 3 = z² · Σ_{i<j} Φ_q(|V̂_i^full · V̂_j^full|)
for atoms beyond the {electron, p, n} subset already handled by
`terms_2_3_brane_tower_mpfr_50dps.py`. Specifically: D, T, ³He.

The atom braid for atom (Z, N) with A = Z + N nucleons lives on
3A strands (3 strands per nucleon: 2 intra-nucleon Hecke factors +
1 inter-nucleon at gen 3k+2 between nucleons k and k+1).

Output: `terms-2-3-atom-per-gen-mpfr-50dps.witness.json`
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

from mpmath import mp, mpf, sqrt as mp_sqrt

mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
Q0 = HERE / "q-pinning-50-digit.witness.json"
OUT = HERE / "terms-2-3-atom-per-gen-mpfr-50dps.witness.json"

M_E_MEV = mpf("0.51099895")


from _phi_q_util import phi_q as Phi_q  # noqa: E402  (after sys.path setup)


def nucleon_chains(quarks, h):
    """Per-nucleon (g0, g1) Hecke factor chains in mpmath.

    quarks: list of three quark labels in {'u', 'd'}.
    Returns (g0_chain, g1_chain) — each a list of (c, d) mpf pairs.
    Mirrors hecke_core.nucleon_gen_chains:
      B₃ = (σ_0 σ_1^{-1})^3 contributes 3× σ_0 to gen 0 and 3× σ_1^{-1} to gen 1.
      Quark pairs: (0,1)→gen 0, (0,2)→gen 0, (1,2)→gen 1.
        uu / dd same-flavour: (1, 0) for u; (1, −h) for d
        ud mixed-flavour: (1, −h/2)
    """
    g0 = [(mpf(1), mpf(0))] * 3
    g1 = [(mpf(1), -h)] * 3
    pairs = [(0, 1, 0), (0, 2, 0), (1, 2, 1)]
    for i, j, gen in pairs:
        qi_f, qj_f = quarks[i], quarks[j]
        if qi_f == qj_f == 'u':
            cd = (mpf(1), mpf(0))
        elif qi_f == qj_f == 'd':
            cd = (mpf(1), -h)
        else:
            cd = (mpf(1), -h / 2)
        if gen == 0:
            g0.append(cd)
        else:
            g1.append(cd)
    return g0, g1


def atom_per_generator_volumes_mpfr(Z, N, q, h, w_sym, w_std, w_alt, z_mark):
    """V̂_i^full per generator for atom (Z, N) at H_{3A}, mpmath @ 50 dps."""
    A = Z + N
    if A < 1:
        return []
    q_inv = mpf(1) / q
    n_strands = 3 * A
    n_gens = n_strands - 1  # 3A − 1

    a_arr = [mpf(0)] * n_gens
    b_arr = [mpf(1)] * n_gens
    sp_arr = [mpf(1)] * n_gens
    ap_arr = [mpf(1)] * n_gens

    proton_g0, proton_g1 = nucleon_chains(['u', 'u', 'd'], h)
    neutron_g0, neutron_g1 = nucleon_chains(['u', 'd', 'd'], h)

    ordering = ['p'] * Z + ['n'] * N

    for k, nuc in enumerate(ordering):
        intra = proton_g0 if nuc == 'p' else neutron_g0
        intra_g1 = proton_g1 if nuc == 'p' else neutron_g1
        base_g0 = 3 * k
        base_g1 = 3 * k + 1

        for c, d in intra:
            i = base_g0
            a_new = a_arr[i] * c * h + a_arr[i] * d + b_arr[i] * c
            b_new = a_arr[i] * c + b_arr[i] * d
            a_arr[i] = a_new
            b_arr[i] = b_new
            sp_arr[i] *= c * q + d
            ap_arr[i] *= -c * q_inv + d

        for c, d in intra_g1:
            i = base_g1
            a_new = a_arr[i] * c * h + a_arr[i] * d + b_arr[i] * c
            b_new = a_arr[i] * c + b_arr[i] * d
            a_arr[i] = a_new
            b_arr[i] = b_new
            sp_arr[i] *= c * q + d
            ap_arr[i] *= -c * q_inv + d

        if k < A - 1:
            i = 3 * k + 2
            next_nuc = ordering[k + 1]
            if nuc == 'p' and next_nuc == 'p':
                base_cross = (mpf(1), mpf(0))
            elif nuc == 'n' and next_nuc == 'n':
                base_cross = (mpf(1), -h)
            else:
                base_cross = (mpf(1), -h / 2)
            c, d = base_cross
            a_new = a_arr[i] * c * h + a_arr[i] * d + b_arr[i] * c
            b_new = a_arr[i] * c + b_arr[i] * d
            a_arr[i] = a_new
            b_arr[i] = b_new
            sp_arr[i] *= c * q + d
            ap_arr[i] *= -c * q_inv + d

    vols = []
    for i in range(n_gens):
        Vs = z_mark * a_arr[i] + b_arr[i]
        Vf = w_sym * sp_arr[i] + w_std * Vs + w_alt * ap_arr[i]
        vols.append({"std": Vs, "sym": sp_arr[i], "alt": ap_arr[i], "full": Vf})
    return vols


def main() -> int:
    q_str = json.load(open(Q0))["derived_50_digit"]["q"]
    q = mpf(q_str)
    q_inv = mpf(1) / q
    h = q - q_inv
    z_mark = mpf(1) / (mp_sqrt(q) + mp_sqrt(q_inv))
    print(f"  q_0 (50 dps) = {q_str}")
    print(f"  h = {h}")
    print(f"  z = {z_mark}")

    # H_3 Wedderburn weights
    def q_int(k):
        if k == 0:
            return mpf(0)
        return sum(q ** (k - 1 - 2 * i) for i in range(k))
    q_fact_3 = q_int(1) * q_int(2) * q_int(3)
    dim_q_3 = mpf(1)
    dim_q_21 = q_int(2)
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

    atoms = [
        ("D",   1, 1),  # deuteron
        ("T",   1, 2),  # tritium
        ("3He", 2, 1),  # helium-3
    ]

    rows = []
    for label, Z, N in atoms:
        print(f"\n  === {label} (Z={Z}, N={N}, A={Z+N}, n_strands={3*(Z+N)}) ===")
        vols = atom_per_generator_volumes_mpfr(Z, N, q, h, w_sym, w_std, w_alt, z_mark)

        n = len(vols)
        term2 = mpf(0)
        for v in vols:
            term2 += Phi_q(mp.fabs(v["full"]), q_inv)

        term3 = mpf(0)
        for i in range(n):
            for j in range(i + 1, n):
                prod = mp.fabs(vols[i]["full"] * vols[j]["full"])
                term3 += z_mark * z_mark * Phi_q(prod, q_inv)

        term2_mev = M_E_MEV * term2
        term3_mev = M_E_MEV * term3
        print(f"    n_generators = {n}")
        for i, v in enumerate(vols):
            print(f"    V̂_{i}: full = {v['full']}")
        print(f"    Term 2 = {term2}")
        print(f"    Term 3 = {term3}")
        print(f"    Term 2 × m_e = {term2_mev} MeV")
        print(f"    Term 3 × m_e = {term3_mev} MeV")
        rows.append({
            "atom": label,
            "Z": Z, "N": N, "A": Z + N,
            "n_strands": 3 * (Z + N),
            "n_generators": n,
            "wedderburn_vols": [{k: str(vv) for k, vv in v.items()} for v in vols],
            "term2_50dps": str(term2),
            "term3_50dps": str(term3),
            "term2_b_pred_mev_50dps": str(term2_mev),
            "term3_b_pred_mev_50dps": str(term3_mev),
        })

    out = {
        "computation": "terms-2-3-atom-per-gen-mpfr-50dps",
        "description":
            "Plan F — Terms 2 + 3 for heavier atoms (D, T, ³He) via "
            "the 3A-strand atom braid. Ports hecke_core.atom_per_"
            "generator_volumes from f64 to mpmath @ 50 dps. "
            "Companion to terms-2-3-brane-tower-mpfr-50dps.witness.json "
            "({electron, p, n} subset). All 4-channel Hecke factors "
            "(B_3 confinement, intra-nucleon quark pairs, inter-nucleon "
            "pp/nn/pn crossings) computed at full mpmath precision.",
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

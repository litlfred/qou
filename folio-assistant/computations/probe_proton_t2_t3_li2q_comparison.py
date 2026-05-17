#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical comparison at q = q_0,
# not symbolic-in-q.
"""Probe — compare T2+T3 under Φ_q (divergent) vs Li_2^q (bounded).

Companion to `terms_2_3_atom_per_gen_mpfr_50dps.py` (PR-this-branch,
m_p chain Item A). Consumes the per-generator Wedderburn volumes
from `terms-2-3-atom-per-gen-mpfr-50dps.witness.json` and computes
T2+T3 under two tower-function candidates:

  Φ_q (current):    Σ Φ_q(|V̂_i|)  + z² · Σ Φ_q(|V̂_i V̂_j|)
                    — divergent as |V| → 1; matches
                    `mass_formula_6term_mpfr_50dps.term_23_brane_tower_mp`.

  Li_2^q (closure candidate per `conj:alpha-k-categorical-closure`):
                    Σ (-Li_2^q(-|V̂_i|))  +  z² · Σ (-Li_2^q(-|V̂_i V̂_j|))
                    — bounded for |V| < 1; matches
                    `prop:mass-endomorphism-tower` lines 162-183
                    (the Kashaev-correct symmetric q-dilogarithm,
                    distinct from the divergent Faddeev Φ_q).

The Li_2^q helper is inlined here (single source of truth at
`folio-assistant/computations/derived_masses.py:li2q_symmetric`
on PR #675; duplicated here to avoid a cherry-pick dependency
between branches before #675 merges — to be deduplicated once
#675 lands).

Output: `probe-proton-t2-t3-li2q-comparison.witness.json`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402


def li2q_symmetric(z: mp.mpf, q: mp.mpf, terms: int = 200) -> mp.mpf:
    """Symmetric q-dilogarithm Li_2^q(z) = Σ z^n / (n · [n]_q).

    With symmetric q-integer [n]_q = (q^n − q^{-n})/(q − q^{-1}).
    Incremental powers (q_pow *= q) for performance.

    Duplicate of `derived_masses.li2q_symmetric` on PR #675; will be
    replaced with an import once #675 merges to main.
    """
    q_minus_qinv = q - 1 / q
    total = mp.mpf(0)
    z_pow = mp.mpf(1)
    q_pow = q
    q_inv_pow = 1 / q
    for n in range(1, terms + 1):
        z_pow *= z
        n_q = (q_pow - q_inv_pow) / q_minus_qinv
        total += z_pow / (n * n_q)
        q_pow *= q
        q_inv_pow /= q
    return total


def _load_q0_50dps() -> tuple[mp.mpf, mp.mpf]:
    path = HERE / "q-pinning-50-digit.witness.json"
    with path.open() as fh:
        d = json.load(fh)
    q0 = mp.mpf(d["derived_50_digit"]["q"])
    z = 1 / (mp.sqrt(q0) + mp.sqrt(1 / q0))
    return q0, z


def _load_vols(Z: int, N: int) -> list[mp.mpf]:
    path = HERE / "terms-2-3-atom-per-gen-mpfr-50dps.witness.json"
    with path.open() as fh:
        data = json.load(fh)
    for rec in data["results"]:
        if rec["Z"] == Z and rec["N"] == N:
            return [mp.mpf(e["full"]) for e in rec["wedderburn_vols"]]
    raise KeyError(f"no witness entry for Z={Z}, N={N}")


def t23_li2q(vols: list[mp.mpf], q0: mp.mpf, z: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """T2+T3 under the bounded symmetric Li_2^q closure."""
    t2 = mp.mpf(0)
    for v in vols:
        t2 += -li2q_symmetric(-mp.fabs(v), q0)
    t3 = mp.mpf(0)
    for i in range(len(vols)):
        for j in range(i + 1, len(vols)):
            t3 += -li2q_symmetric(-mp.fabs(vols[i] * vols[j]), q0)
    t3 *= z ** 2
    return t2, t3


def t23_phi_q(Z: int, N: int) -> tuple[mp.mpf, mp.mpf]:
    """T2+T3 under the divergent Faddeev Φ_q (existing form)."""
    from mass_formula_6term_mpfr_50dps import term_23_brane_tower_mp
    return term_23_brane_tower_mp(Z, N)


ATOMS = [
    ("proton",   1, 0),
    ("neutron",  0, 1),
    ("deuteron", 1, 1),
    ("tritium",  1, 2),
    ("helium3",  2, 1),
]


def main() -> int:
    q0, z = _load_q0_50dps()
    print("=" * 96)
    print(" T2 + T3 brane-tower comparison: Φ_q (divergent) vs Li_2^q (bounded)")
    print(f" q_0 = {mp.nstr(q0, 14)},  z = {mp.nstr(z, 14)}")
    print("=" * 96)
    print(f"  {'atom':>9}  {'T2+T3 (Φ_q)':>15}  {'T2+T3 (Li_2^q)':>15}  {'ratio':>10}")
    print("  " + "-" * 60)

    results = []
    for label, Z, N in ATOMS:
        vols = _load_vols(Z, N)
        t2_l, t3_l = t23_li2q(vols, q0, z)
        sum_l = t2_l + t3_l
        try:
            t2_p, t3_p = t23_phi_q(Z, N)
            sum_p = t2_p + t3_p
            ratio = float(sum_l / sum_p) if sum_p != 0 else None
            sum_p_str = mp.nstr(sum_p, 8)
            ratio_str = f"{ratio:+.4e}" if ratio is not None else "n/a"
        except Exception as e:
            sum_p = mp.inf
            sum_p_str = f"err:{type(e).__name__}"
            ratio_str = "n/a"
        print(f"  {label:>9}  {sum_p_str:>15}  {mp.nstr(sum_l, 8):>15}  {ratio_str:>10}")
        results.append({
            "atom": label,
            "Z": Z,
            "N": N,
            "T2_li2q_MeV": str(t2_l),
            "T3_li2q_MeV": str(t3_l),
            "T2_plus_T3_li2q_MeV": str(sum_l),
            "T2_plus_T3_phi_q_MeV": str(sum_p) if not mp.isinf(sum_p) else "inf",
        })
    print()

    builder = WitnessBuilder.wrap_legacy(
        "probe-proton-t2-t3-li2q-comparison",
        {
            "description": (
                "Comparison of T2+T3 brane-tower values under the "
                "divergent Faddeev Φ_q form (current "
                "`mass_formula_6term_mpfr_50dps.term_23_brane_tower_mp`) "
                "vs the bounded symmetric Li_2^q closure candidate "
                "(per `prop:mass-endomorphism-tower` lines 162-183 + "
                "`conj:alpha-k-categorical-closure`). Computed at A=1, "
                "2, 3 from the per-generator Wedderburn volumes in "
                "`terms-2-3-atom-per-gen-mpfr-50dps.witness.json` "
                "(PR-this-branch, m_p chain Item A). The Li_2^q form is "
                "bounded for all atoms; the Φ_q form diverges as "
                "|V| → 1 (proton |V_0| ≈ 0.989). Cross-cuts the m_p "
                "chain closure analysis from PR #671 and the closure "
                "conjecture from PR #675."
            ),
            "parameters": {
                "q_0_50dps": mp.nstr(q0, 50, strip_zeros=False),
                "z_markov_50dps": mp.nstr(z, 50, strip_zeros=False),
                "li2q_terms": 200,
            },
            "results": results,
        },
        script_path=__file__,
        engine="mpmath",
    )
    out = builder.save()
    print(f"  Witness: {Path(out).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

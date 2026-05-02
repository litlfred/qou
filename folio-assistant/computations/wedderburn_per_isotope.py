#!/usr/bin/env python3
"""
CONVENTION NOTE: the "markov_trace" computed via Σ w_λ·χ_λ with
w_λ = d_q²/[n]_q! is technically the PLANCHEREL trace, not the
Jones-Ocneanu Markov trace (these differ at q ≠ 1).  See
markov_weight_verification.py.

Wedderburn profile per isotope: tests whether the per-atom
"complexity correction" rho_F_eff/rho_nominal correlates with
specific partition characters of the atom braid.

For each atom (Z, N):
  1. Build atom_braid_word_3A(Z, N) - 3A-strand Hecke element
  2. Compute chi_lambda(beta_atom) at q_0 for all partitions of 3A
  3. Compute Plancherel-weighted Markov trace (total)
  4. Record per-channel contributions

Then cross-tabulate with:
  - rho_F_eff = B_AME / V_catalog (from single-knot census match)
  - deviation from nominal m_e or 2m_e

Expected insight: one or more partition characters should correlate
with the atom-dependent deviation, identifying the "algebraic
complexity" measure.
"""
from __future__ import annotations

import sys
import json
import time
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401

from hecke_characters import partitions_of, dim_q, qfac
from mass_at_3A_proper import _cached_seminormal, atom_braid_word_3A
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV


ATOMS = [
    # (name, Z, N, B_AME, nominal_rho_F, catalog_knot_vol)
    ("D",    1, 1,   2.22456612, "m_e",   4.4008325161),    # 6_2
    ("T",    1, 2,   8.4817984,  "2m_e",  8.2863168178),    # 8_11
    ("3He",  2, 1,   7.7180375,  "2m_e",  7.3277247534),    # Borromean 8G
    ("4He",  2, 2,  28.2956912,  "2m_e", 29.3108990137),    # 4·8G (magic)
]


def _sigmas_to_numeric(sigmas, dim):
    """Convert symbolic seminormal matrices to numeric arrays at q=Q0.

    Called once per shape; result is reused across callers.  Uses
    sp.lambdify on the whole matrix for a single numpy evaluation per
    sigma (vs element-wise sp.N which is O(dim²·sympy-overhead)).
    """
    q_sym = sp.Symbol('q')
    sigmas_num = []
    for S in sigmas:
        if hasattr(S, "toarray"):
            S_arr = S.toarray()
        else:
            S_arr = np.asarray(S)
        S_mat = sp.Matrix(S_arr.tolist())
        try:
            numeric_fn = sp.lambdify(q_sym, S_mat, modules="numpy")
            arr = np.asarray(numeric_fn(complex(Q0)), dtype=complex)
        except Exception:
            arr = np.empty((dim, dim), dtype=complex)
            for i in range(dim):
                for j in range(dim):
                    e = S_arr[i, j]
                    if hasattr(e, "subs"):
                        arr[i, j] = complex(sp.N(e.subs(q_sym, Q0)))
                    else:
                        arr[i, j] = complex(e)
        sigmas_num.append(arr)
    return sigmas_num


def chi_lambda_at_q0(sigmas_num, dim, word):
    """Character χ_λ(β) from pre-converted numeric sigmas."""
    if dim == 0:
        return 0j
    I = np.eye(dim, dtype=complex)
    prod = I.copy()
    for (c, d, g) in word:
        if g < len(sigmas_num):
            prod = prod @ (c * sigmas_num[g] + d * I)
        else:
            return 0j
    return complex(np.trace(prod))


def profile_atom(Z, N):
    n = 3 * (Z + N)
    word = atom_braid_word_3A(Z, N)
    nfac = float(qfac(n))
    parts = list(partitions_of(n))
    rows = []
    for shape in parts:
        sigmas, dim, _ = _cached_seminormal(shape)
        if dim == 0:
            continue
        dq = float(dim_q(shape))
        w_lambda = (dq * dq) / nfac
        sigmas_num = _sigmas_to_numeric(sigmas, dim)
        chi = chi_lambda_at_q0(sigmas_num, dim, word)
        contribution = w_lambda * chi.real / dim
        rows.append({
            "shape": list(shape),
            "dim": dim,
            "dim_q": dq,
            "w_lambda": w_lambda,
            "chi": chi.real,
            "contribution": contribution,
            "is_alt": all(s == 1 for s in shape),
            "is_sym": shape == (n,),
        })
    return rows, sum(r["contribution"] for r in rows)


def main() -> int:
    print("=" * 120)
    print("WEDDERBURN PROFILE PER ISOTOPE")
    print("=" * 120)
    print(f"\n  {'atom':>5} {'B_AME':>10} {'V_cat':>10} {'rho_nom':>8} "
          f"{'rho_eff':>10} {'ratio':>10} {'deviation':>12}")
    print("  " + "-" * 80)
    atoms_data = {}
    for (name, Z, N, B, rho_label, V) in ATOMS:
        rho_eff = B / V
        nominal = M_E_MEV * (2 if rho_label == "2m_e" else 1)
        ratio = rho_eff / nominal
        dev = (ratio - 1) * 100
        print(f"  {name:>5} {B:>10.5f} {V:>10.5f} {rho_label:>8} "
              f"{rho_eff:>10.6f} {ratio:>10.6f} {dev:>+11.4f}%")
        atoms_data[name] = {
            "Z": Z, "N": N, "B_AME": B, "V_catalog": V,
            "rho_nominal_label": rho_label,
            "rho_nominal_MeV": nominal,
            "rho_eff_MeV": rho_eff,
            "ratio_eff_to_nominal": ratio,
            "deviation_pct": dev,
        }

    print(f"\n{'=' * 120}")
    print("Per-atom Wedderburn profile:")
    print('=' * 120)
    profiles = {}
    for (name, Z, N, B, rho_label, V) in ATOMS:
        A = Z + N
        n = 3 * A
        print(f"\n  [{name}] Z={Z} N={N} 3A={n}  "
              f"(computing {len(list(partitions_of(n)))} partitions…)")
        t0 = time.time()
        rows, tr = profile_atom(Z, N)
        dt = time.time() - t0
        print(f"    tr_M = {tr:.6f}  ({dt:.1f}s)")

        # Key characters
        sym_row = next((r for r in rows if r["is_sym"]), None)
        alt_row = next((r for r in rows if r["is_alt"]), None)
        print(f"    chi_sym  = {sym_row['chi']:+.4f}  (dim {sym_row['dim']}, w={sym_row['w_lambda']:.3e})")
        print(f"    chi_alt  = {alt_row['chi']:+.4f}  (dim {alt_row['dim']}, w={alt_row['w_lambda']:.3e})")
        # Top 5 by |contribution|
        top = sorted(rows, key=lambda r: abs(r["contribution"]), reverse=True)[:5]
        print(f"    Top 5 contributing partitions:")
        for r in top:
            print(f"      {str(r['shape']):<18} chi={r['chi']:+.3f}  "
                  f"contrib={r['contribution']:+.4f}")

        profiles[name] = {
            "n_strands": n,
            "markov_trace": tr,
            "chi_sym": sym_row["chi"],
            "chi_alt": alt_row["chi"],
            "rows": rows,
        }

    print(f"\n{'=' * 120}")
    print("Correlation probe: does chi_alt or chi_sym correlate with deviation?")
    print('=' * 120)
    print(f"\n  {'atom':>5} {'deviation%':>12} {'chi_sym':>10} "
          f"{'chi_alt':>10} {'chi_alt/dim_q(alt)':>20} {'tr_M':>10}")
    print("  " + "-" * 80)
    for (name, *_) in ATOMS:
        d = atoms_data[name]
        p = profiles[name]
        cs = p["chi_sym"]
        ca = p["chi_alt"]
        tr = p["markov_trace"]
        # chi_alt weight scaled
        chi_alt_row = next(r for r in p["rows"] if r["is_alt"])
        alt_scaled = ca / chi_alt_row["dim_q"]
        print(f"  {name:>5} {d['deviation_pct']:>+11.4f}% "
              f"{cs:>+10.4f} {ca:>+10.4f} {alt_scaled:>+20.6f} {tr:>+10.4f}")

    witness = {
        "computation": "wedderburn-per-isotope",
        "description": (
            "Per-atom Wedderburn profile: chi_lambda(beta_atom) for all "
            "partitions of 3A, cross-tabulated with the per-atom "
            "rho_F_eff / rho_F_nominal deviation.  Tests whether "
            "algebraic-complexity corrections to rho_F correlate with "
            "specific Wedderburn characters."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        # P2.5: sympy-as-matrix-stepping-stone pattern.  This script
        # uses sp.Symbol('q') only inside _sigmas_to_numeric to build
        # Hoefsmit seminormal matrices ρ_λ(σ_i) ∈ Mat(ℚ(q)); each
        # matrix is then immediately lambdified at q = q_0 and the
        # downstream products / traces run in numpy.  The algebraic
        # truth IS symbolic at the per-irrep matrix level, but the
        # per-trace output is numerical because sympy doesn't scale
        # for the block-matrix products on partitions of n = 3A up to
        # 12.  The symbolic seminormal matrices are produced by
        # build_seminormal_matrices in hecke_characters.py — see
        # that module for the algebraic source.
        "symbolic_q_form": {
            "engine": "sympy (matrix construction only)",
            "q_symbol": "q (sp.Symbol('q'))",
            "pattern_note": (
                "sympy-as-matrix-stepping-stone: ρ_λ(σ_i) ∈ "
                "Mat_{d_λ × d_λ}(ℚ(q)) is symbolic in _sigmas_to_numeric; "
                "the lambdify-at-q_0 step eagerly converts to numpy "
                "before computing products.  Per-trace χ_λ(β_atom) "
                "values reported here are numerical specialisations, "
                "not Laurent polynomials in q."
            ),
            "symbolic_source": "hecke_characters.build_seminormal_matrices",
            "specialisation_point": "q = q_0",
        },
        "atoms": atoms_data,
        "profiles": profiles,
    }
    out = Path(__file__).parent / "wedderburn-per-isotope.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

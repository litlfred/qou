#!/usr/bin/env python3
"""
q-deformed Hecke character χ^λ_q(T_w) — SYMBOLIC in q.

The Hoefsmit seminormal form gives explicit matrix representations
ρ_λ: H_n(q) → End(S^λ) for each partition λ ⊢ n. With q kept
symbolic (sympy.Symbol), multiplying crossing matrices through an
atomic braid word and tracing gives the exact q-character χ^λ_q(T_w)
as a rational function of q.

Compared to hecke_characters.py (numerical at q = q_0) and
murnaghan_nakayama.py (classical q = 1), this module gives the
**full q-dependent** character, distinguishing σ from σ^{-1} that
the classical MN character collapses.

Hoefsmit formulas:
  For SYT T with entries i, i+1 in cells c_i, c_{i+1}:
    ρ = content(c_{i+1}) - content(c_i)  (axial distance)

  If i, i+1 in same row (ρ = 1):
    ρ_λ(T_i) T = q · T                    (eigenvalue q)

  If i, i+1 in same column (ρ = -1):
    ρ_λ(T_i) T = -q^{-1} · T              (eigenvalue -q^{-1})

  Otherwise (ρ ≠ ±1):
    2×2 block on {T, T'} where T' swaps i, i+1:
    [[ a,    b  ],
     [ b,    a' ]]
    with a = h/(1-q^{-2ρ}), a' = h/(1-q^{2ρ}), b² = a·a'+1, h=q-q^{-1}

Scope of this module:
  - A=1 (proton, neutron): 3 partitions, max dim 2.  Fast.
  - A=2: 11 partitions, max dim 9.  Minutes symbolically.
  - A=3: 30 partitions, max dim 42.  Heavy; use with caution.
  - A=4: 77 partitions, max dim 132.  Do NOT run symbolically.
    (For A ≥ 3 use numerical hecke_characters.py with q → q_0.)

Witness: hecke-character-symbolic.witness.json
"""
import functools
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from sympy import Symbol, Rational, Integer, Matrix, simplify, sqrt, together

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as _Q_CANONICAL
from murnaghan_nakayama import (
    partitions_of, dim_specht, hook_lengths,
    atomic_braid_word,
)


def young_diagram_cells(shape):
    cells = []
    for i, r in enumerate(shape):
        for j in range(r):
            cells.append((i, j))
    return cells


def standard_young_tableaux(shape):
    """Enumerate all SYT of given shape as a list of dicts
    {entry: cell_index}.  Returns (syts, cells, contents).
    """
    n = sum(shape)
    cells = young_diagram_cells(shape)
    contents = [c - r for r, c in cells]

    def _gen(filling, used, next_entry):
        if next_entry > n:
            yield dict(filling)
            return
        for idx, cell in enumerate(cells):
            if idx in used:
                continue
            r, c = cell
            # Check SYT validity: entry above (r-1, c) and left (r, c-1)
            # must be filled with smaller numbers.
            ok = True
            if r > 0:
                # entry above must already be filled (smaller value)
                try:
                    above = cells.index((r - 1, c))
                    if above not in used:
                        ok = False
                except ValueError:
                    pass
            if c > 0:
                try:
                    left = cells.index((r, c - 1))
                    if left not in used:
                        ok = False
                except ValueError:
                    pass
            if not ok:
                continue
            filling[next_entry] = idx
            used.add(idx)
            yield from _gen(filling, used, next_entry + 1)
            del filling[next_entry]
            used.remove(idx)

    syts = list(_gen({}, set(), 1))
    return syts, cells, contents


@functools.lru_cache(maxsize=None)
def _hoefsmit_cached(shape_key, q_name):
    """Internal cache for Hoefsmit construction keyed by (shape, q symbol name).
    `shape_key` must be a hashable tuple; `q_name` identifies the symbol so
    calls with the same `q` share the cached matrices."""
    q = sp.Symbol(q_name, positive=True, real=True)
    return _hoefsmit_build(list(shape_key), q)


def _hoefsmit_build(shape, q):
    """Uncached Hoefsmit build (used by the cached wrapper and for
    tests where q is not a named Symbol)."""
    n = sum(shape)
    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], 0, []

    h = q - q ** (-1)

    matrices = []
    for k in range(1, n):
        M = sp.zeros(dim, dim)
        processed = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]

            # Diagonal entry a — `cancel` reduces the rational quickly.
            a = sp.cancel(h / (1 - q ** (-2 * rho)))

            # Find swap partner
            swap_map = dict(syts[i])
            swap_map[k], swap_map[k + 1] = ci_k1, ci_k
            j = None
            for jj in range(dim):
                if jj == i:
                    continue
                if syts[jj] == swap_map:
                    j = jj
                    break

            if j is None:
                # 1×1 block: eigenvalue q (same row, rho=1) or -q^{-1}
                # (same column, rho=-1).
                M[i, i] = a
                processed.add(i)
            else:
                # 2×2 block
                a_prime = sp.cancel(h / (1 - q ** (2 * rho)))
                b_sq = sp.cancel(a * a_prime + 1)
                b = sp.sqrt(b_sq)
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = b
                M[j, i] = b
                processed.add(i)
                processed.add(j)
        matrices.append(M)
    return matrices, dim, syts


def hoefsmit_matrices_symbolic(shape, q):
    """Build symbolic Hoefsmit matrices ρ_λ(T_1), ..., ρ_λ(T_{n-1})
    for partition `shape`.  Entries are rational functions of q.

    Cached when `q` is a named sympy Symbol; falls back to an uncached
    build otherwise (e.g. when `q` is a concrete Rational for evaluation).
    """
    if isinstance(q, sp.Symbol):
        return _hoefsmit_cached(tuple(shape), q.name)
    return _hoefsmit_build(shape, q)


def q_character_on_braid_word(shape, braid_crossings, q):
    """Compute χ^λ_q(T_w) symbolically for a braid word represented as
    a list of (gen_index, (c, d)) pairs.  Each crossing contributes
    c · ρ_λ(T_gen) + d · I_dim to the product; the final trace is the
    q-character.

    For the atomic braid: c = 1, d ∈ {0, -h, -h/2} depending on
    crossing type (σ, σ^{-1}, averaged).

    Returns sympy expression for χ^λ_q(T_w).
    """
    matrices, dim, _ = hoefsmit_matrices_symbolic(shape, q)
    if dim == 0:
        return Integer(0)
    h = q - q ** (-1)

    M = sp.eye(dim)
    for gen_idx, cross_d in braid_crossings:
        if gen_idx < 0 or gen_idx >= len(matrices):
            raise IndexError(f"gen_idx {gen_idx} out of range for shape {shape}")
        sigma = matrices[gen_idx]
        # cross_d is one of 0, -h, -h/2
        d_val = {"sigma": Integer(0), "sigma_inv": -h,
                 "averaged": -h / 2}[cross_d]
        # crossing matrix = 1·σ + d·I
        cross = sigma + d_val * sp.eye(dim)
        M = M * cross
        # `cancel` — polynomial-division on rationals — is 5–10×
        # faster than `simplify` and sufficient to keep entry
        # complexity bounded for Hecke-algebra traces.
        M = M.applyfunc(sp.cancel)
    return sp.cancel(M.trace())


def atomic_braid_to_crossings(Z, N, include_inter=True):
    """Translate proton_cross/neutron_cross into the gen_idx, cross_type
    pairs suitable for q_character_on_braid_word.

    cross_type ∈ {"sigma", "sigma_inv", "averaged"} depending on (c, d):
      (1, 0)    → "sigma"
      (1, -h)   → "sigma_inv"
      (1, -h/2) → "averaged"
    """
    from mass_endomorphism import proton_cross, neutron_cross, HA
    A = Z + N
    nucleon_types = ['p'] * Z + ['n'] * N
    out = []
    h_val = HA  # numerical value for (c,d) key matching

    def classify(c, d):
        if d == 0.0:
            return "sigma"
        if abs(d - (-h_val)) < 1e-9:
            return "sigma_inv"
        if abs(d - (-h_val / 2)) < 1e-9:
            return "averaged"
        raise ValueError(f"Unknown crossing (c={c}, d={d})")

    for k, nt in enumerate(nucleon_types):
        src = proton_cross if nt == 'p' else neutron_cross
        for c, d in src.get(0, []):
            out.append((3 * k, classify(c, d)))
        for c, d in src.get(1, []):
            out.append((3 * k + 1, classify(c, d)))
    if include_inter:
        for k in range(A - 1):
            pair = (nucleon_types[k], nucleon_types[k + 1])
            if pair == ('p', 'p'):
                out.append((3 * k + 2, "sigma"))
            elif pair == ('n', 'n'):
                out.append((3 * k + 2, "sigma_inv"))
            else:
                out.append((3 * k + 2, "averaged"))
    return out


# ─── Main: prove q-character distinguishes proton from neutron ──────────

if __name__ == "__main__":
    print("HECKE q-CHARACTER SYMBOLIC — closes the parity-blind gap")
    print("=" * 80)

    q = sp.Symbol('q', positive=True, real=True)
    q0 = Rational(int(_Q_CANONICAL * 10 ** 16), 10 ** 16)

    # A = 1 full test: proton and neutron
    print("\n── A = 1 q-character across all 3 partitions ──")
    results = {}
    for label, Z, N in [("p", 1, 0), ("n", 0, 1)]:
        crossings = atomic_braid_to_crossings(Z, N, include_inter=False)
        print(f"\n  {label}: braid length = {len(crossings)}")
        per_lambda = {}
        for lam in partitions_of(3):
            chi = q_character_on_braid_word(lam, crossings, q)
            chi_at_q0 = float(chi.subs(q, q0).evalf(30))
            chi_at_q0_polynomial_q = expose_polynomial(chi, q)
            per_lambda[str(lam)] = {
                "symbolic": str(sp.nsimplify(chi)),
                "at_q0": chi_at_q0,
            }
            print(f"    λ = {lam!s:<12}  χ^λ_q(T_w) @ q_0 = "
                  f"{chi_at_q0:+.6e}")
        results[label] = per_lambda

    # Verify p and n differ at q_0
    print("\n── Proton vs Neutron comparison ──")
    p_chars = results["p"]
    n_chars = results["n"]
    for lam_str in p_chars:
        p_val = p_chars[lam_str]["at_q0"]
        n_val = n_chars[lam_str]["at_q0"]
        diff = p_val - n_val
        print(f"  λ = {lam_str:<12}  χ^λ_q(p) - χ^λ_q(n) @ q_0 = "
              f"{diff:+.6e}  "
              f"[{'SAME' if abs(diff) < 1e-9 else 'DIFFER'}]")

    # Schur-Weyl sum for p and n at A=1
    print("\n── Schur-Weyl mass trace at A = 1 ──")
    from schur_weyl_symbolic import schur_weyl_weight
    for label in ["p", "n"]:
        total = Integer(0)
        for lam in partitions_of(3):
            w = schur_weyl_weight(lam, q)
            chi = q_character_on_braid_word(
                lam, atomic_braid_to_crossings(
                    {"p": 1, "n": 0}[label], {"p": 0, "n": 1}[label],
                    include_inter=False),
                q,
            )
            total += w * chi
        total = sp.simplify(total)
        total_q0 = float(total.subs(q, q0).evalf(30))
        total_q0_polynomial_q = expose_polynomial(total, q)
        print(f"  |tr_M({label})| @ q_0 = {abs(total_q0):+.6e}")
        results[f"{label}_total"] = {
            "symbolic": str(sp.nsimplify(total)),
            "at_q0": total_q0,
        }

    # Proton-neutron splitting
    if "p_total" in results and "n_total" in results:
        Q_cat = results["n_total"]["at_q0"] - results["p_total"]["at_q0"]
        print(f"\n  Q_cat = tr_M(n) - tr_M(p) = {Q_cat:+.6e}")
        if abs(Q_cat) > 1e-12:
            E_0 = 0.782 / abs(Q_cat)
            print(f"  E_0 = 0.782 MeV / |Q_cat| = {E_0:+.6e} MeV/cat.unit")
            print(f"  [CALIBRATION SUCCEEDS — q-character distinguishes p/n]")
        else:
            print(f"  [Q_cat = 0: q-character STILL parity-blind for this "
                  f"crossing structure]")

    witness = {
        "computation": "hecke-character-symbolic",
        "description": (
            "q-deformed Hecke character χ^λ_q(T_w) symbolic in q via "
            "Hoefsmit seminormal matrices.  Replaces the classical "
            "Murnaghan-Nakayama character (parity-blind at q=1) for A=1. "
            "For A ≥ 2 the symbolic matrix product is costly; use "
            "numerical hecke_characters.py instead."
        ),
        "reference_blocks": [
            "prop:schur-weyl-mass-decomposition",
            "rem:mn-classical-parity-blind",
        ],
        "scope": "A = 1 only (p, n) — demonstrates q-character distinguishes.",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": str(float(_Q_CANONICAL)),
            "engine": "sympy Matrix (exact in q)",
        },
        "results": results,
    }
    out = Path(__file__).parent / "hecke-character-symbolic.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")

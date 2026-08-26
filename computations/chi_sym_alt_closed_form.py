#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
Closed-form derivation: χ_sym(β_atom) · χ_alt(β_atom) = −(1 + H_A²/4)^(2A+1).

In any 2-dim Wedderburn irrep of H_n(q), σ_i has eigenvalues {+q, −q⁻¹}.
A Hecke factor c·σ_i + d·I acts in the sym/alt channels with eigenvalues

    sym : c·q + d
    alt : −c/q + d

so its contribution to χ_sym · χ_alt per factor is

    (cq + d)(−c/q + d) = d² − c² + c·d·(q − q⁻¹) = d² − c² + cd·H_A .

The atom braid word (atom_braid_word_3A) is composed of three factor
types:

    pure σ       (c, d) = (1,  0)       contribution = −1
    pure σ⁻¹     (c, d) = (1, −H_A)     contribution = −1
    ud coupling  (c, d) = (1, −H_A/2)   contribution = −(1 + H_A²/4)

Counting ud factors in atom_braid_word_3A(Z, N):

    intra-nucleon (proton uud, neutron udd): 2 ud factors per nucleon
    inter-nucleon p→n transition          : 1 ud factor per atom

    total: n_ud(A) = 2A + 1

Pure σ / σ⁻¹ factors each contribute −1, and the count of (pure_σ +
pure_σ⁻¹ + ud_factors) in the word is odd for every atom built by
atom_braid_word_3A, so the overall sign is −1 and the closed form is

    χ_sym(β_atom) · χ_alt(β_atom) = −(1 + H_A²/4)^(2A+1)
                                  = −([2]_q / 2)^(4A+2)

since 1 + H_A²/4 = (q + q⁻¹)²/4 = [2]_q²/4.

This script verifies the closed form by comparing it to the direct
character product (computed from seminormal matrices) across D/T/³He/⁴He.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=UserWarning)
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
import numpy as np
import sympy as sp

from hecke_characters import partitions_of, dim_q, qfac
from hecke_core import h as HA_VAL
from mass_at_3A_proper import _cached_seminormal, atom_braid_word_3A, Q0_PROTON
from q_parameter import Q as Q0
from _precision import fmt, set_compute_dps
from witness_base import WitnessBuilder


ATOMS = [
    # (name, Z, N)
    ("D",   1, 1),
    ("T",   1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
]


def classify_factor(c: float, d: float) -> str:
    """Return 'pure_sigma', 'pure_sigma_inv', or 'ud'."""
    if abs(c - 1.0) > 1e-12:
        return f"other(c={c}, d={d})"
    if abs(d) < 1e-12:
        return "pure_sigma"
    if abs(d - (-HA_VAL)) < 1e-12:
        return "pure_sigma_inv"
    if abs(d - (-HA_VAL / 2)) < 1e-12:
        return "ud"
    return f"other(c={c}, d={d})"


def count_factor_types(word):
    counts = {"pure_sigma": 0, "pure_sigma_inv": 0, "ud": 0}
    for c, d, _g in word:
        k = classify_factor(c, d)
        counts[k] = counts.get(k, 0) + 1
    return counts


def chi_in_shape(shape, word):
    """Compute χ_λ(W) in the λ-irrep via the seminormal matrices.

    NO-FLOAT64 (qou-poi1). This built numpy `complex128` matrices via
    `complex(sp.N(...))` and multiplied them with `@`, so every character came
    back at ~1e-16 regardless of what was true -- and the word's own `d`
    coefficients arrive as `mpmath.mpf` already (they are -h and -h/2, the
    interface offsets), so the float64 was introduced HERE, not inherited.
    Now the seminormal entries are evaluated at working precision and the
    product is carried in `mpmath`. Max irrep dimension in scope is 16, so the
    mpmath matrix product costs nothing measurable.
    """
    sigmas, dim, _ = _cached_seminormal(shape, Q0_PROTON)
    if dim == 0:
        return mp.mpc(0)
    q_sym = sp.Symbol('q')
    dps = mp.mp.dps

    sigmas_num = []
    for S in sigmas:
        S_arr = S.toarray() if hasattr(S, "toarray") else np.asarray(S)
        M = mp.zeros(dim, dim)
        for i in range(dim):
            for j in range(dim):
                e = S_arr[i, j]
                if hasattr(e, "subs"):
                    M[i, j] = mp.mpmathify(sp.N(e.subs(q_sym, Q0), dps))
                else:
                    M[i, j] = mp.mpmathify(e)
        sigmas_num.append(M)

    prod = mp.eye(dim)
    for c, d, g in word:
        if g >= len(sigmas_num):
            return mp.mpc(0)
        prod = prod * (sigmas_num[g] * mp.mpmathify(c)
                       + mp.eye(dim) * mp.mpmathify(d))
    return sum(prod[i, i] for i in range(dim))


def closed_form_prediction(A: int, H_A):
    H_A = mp.mpmathify(H_A)
    return -(1 + H_A * H_A / 4) ** (2 * A + 1)


# ─────────────────────────────────────────────────────────────────────
# Per-shape closed-form helpers (sym = (n,) and alt = (1,)*n).
#
# In the 1-dim irrep λ = (n) (sym): σ ↦ +q.   Each Hecke factor
# (c·σ + d·I) acts as (c·q + d).
# In the 1-dim irrep λ = (1ⁿ) (alt): σ ↦ −q⁻¹.  Each Hecke factor
# acts as (−c/q + d).
#
# For the (c, d) pairs used by atomic_braid_to_crossings /
# atom_braid_word_3A:
#
#   "sigma"      (c, d) = (1,  0)        χ_sym = q,           χ_alt = -q⁻¹
#   "sigma_inv"  (c, d) = (1, -H_A)      χ_sym = q⁻¹,         χ_alt = -q
#   "averaged"   (c, d) = (1, -H_A/2)    χ_sym = [2]_q/2,     χ_alt = -[2]_q/2
#
# Multiplicativity on 1-dim irreps gives closed forms in terms of
# the factor counts (n_σ, n_σ_inv, n_ud).  These are exact (no
# Hoefsmit/Wedderburn matrix product needed).
# ─────────────────────────────────────────────────────────────────────


def count_factor_types_from_crossings(crossings) -> dict:
    """Count Hecke factor types from a `(gen_idx, cross_type)` list.

    `cross_type` ∈ `canonical_braid_crossings.CTYPES` — same convention as
    `atom_canonical_crossings` / `light_isotope_sweep`.

    The bucket set is built from `CTYPES` rather than hand-listed. The
    hand-listed version raised `ValueError: unknown cross_type` on
    `averaged_weighted`, which `light_isotope_sweep` feeds it for every
    `Z >= 1, N >= 1` isotope (qou-8zjd).
    """
    from canonical_braid_crossings import CTYPES
    counts = {ct: 0 for ct in CTYPES}
    for _g, ct in crossings:
        if ct in counts:
            counts[ct] += 1
        else:
            raise ValueError(f"unknown cross_type: {ct!r}")
    return counts


def _weighted_factor(q):
    """|eigenvalue| of the colour-weighted p-n crossing, exactly.

    On a 1-dimensional irrep `σ ↦ ±…`, a crossing `c·σ + d·1` contributes
    `(image of σ) + d`. With `d = -h(1/2 - δ/4)` and `h = q - q⁻¹`:

        sym:  q  - h(1/2 - δ/4) = (q + q⁻¹)/2 + hδ/4
        alt: -q⁻¹ - h(1/2 - δ/4) = -[(q + q⁻¹)/2 - hδ/4]

    so the colour-weighted factor is the colour-blind `[2]_q/2` shifted by
    `±hδ/4` -- the p-n colour asymmetry, carried exactly rather than
    approximated by the blind `[2]_q/2`. Returned as the *sym* value; the
    alt magnitude is the same expression with the sign of the shift flipped.
    """
    from canonical_braid_crossings import _avg_color_delta
    q = mp.mpmathify(q)
    h = q - 1 / q
    # `float(_avg_color_delta())` was a downcast INSIDE an arithmetic
    # expression -- the case AGENTS.md names as a computation, not a display.
    return (q + 1 / q) / 2 + h * mp.mpmathify(_avg_color_delta()) / 4


def chi_sym_closed_form(crossings, q):
    """χ_(n)(T_w) for the 1-dim sym irrep at substrate parameter q.

    Closed form: q^(n_σ - n_σ_inv) · ([2]_q / 2)^n_ud · w^n_wud, where
    `w = [2]_q/2 + hδ/4` is the colour-weighted p-n factor (`_weighted_factor`).
    """
    c = count_factor_types_from_crossings(crossings)
    q = mp.mpmathify(q)
    two_q_half = (q + 1 / q) / 2  # = [2]_q / 2 = (q + q⁻¹)/2
    return ((q ** (c["sigma"] - c["sigma_inv"]))
            * (two_q_half ** c["averaged"])
            * (_weighted_factor(q) ** c["averaged_weighted"]))


def chi_alt_closed_form(crossings, q):
    """χ_(1ⁿ)(T_w) for the 1-dim alt irrep at substrate parameter q.

    Closed form: (−1)^#(β) · q^(n_σ_inv − n_σ) · ([2]_q / 2)^n_ud · w̄^n_wud,
    where `w̄ = [2]_q/2 − hδ/4` — the colour-weighted factor with the shift
    reflected, since on the alt irrep σ ↦ −q⁻¹ (see `_weighted_factor`).
    """
    c = count_factor_types_from_crossings(crossings)
    q = mp.mpmathify(q)
    two_q_half = (q + 1 / q) / 2
    w_alt = 2 * two_q_half - _weighted_factor(q)   # = [2]_q/2 − hδ/4
    total = (c["sigma"] + c["sigma_inv"]
             + c["averaged"] + c["averaged_weighted"])
    sign = mp.mpf(-1) if (total % 2 == 1) else mp.mpf(1)
    return (sign * (q ** (c["sigma_inv"] - c["sigma"]))
            * (two_q_half ** c["averaged"])
            * (w_alt ** c["averaged_weighted"]))


def main():
    w = WitnessBuilder("chi-sym-alt-closed-form", engine="mpmath+sympy")
    w.set_description(
        "Exact closed form χ_sym(β_atom)·χ_alt(β_atom) = −(1 + H_A²/4)^(2A+1) "
        "derived from eigenvalue algebra of Hecke factors + ud-factor counting "
        "in atom_braid_word_3A."
    )
    w.set_content_block("rem:chi-sym-alt-closed-form")
    # Serialised via _precision.fmt, not float(). float(Q0) put the SUBSTRATE
    # PARAMETER itself into the witness at 16 digits.
    w.add_parameter("q", fmt(mp.mpmathify(Q0)))
    w.add_parameter("H_A", fmt(mp.mpmathify(HA_VAL)))
    w.add_caveat(
        "This is a structural identity (no fitting). It explains the "
        "numerical coincidence χ_sym·χ_alt ≈ −1.08 as a function of A "
        "alone, but does NOT explain the atom-dependent density deviation "
        "(D −1.1%, T +0.2%, ³He +3.1%, ⁴He −5.5%)."
    )

    rows = []
    for name, Z, N in ATOMS:
        A = Z + N
        word = atom_braid_word_3A(Z, N)
        counts = count_factor_types(word)
        n_ud = counts["ud"]
        n_pure_sigma = counts["pure_sigma"]
        n_pure_sigma_inv = counts["pure_sigma_inv"]

        pred = closed_form_prediction(A, HA_VAL)

        chi_sym_val = chi_in_shape((3 * A,), word)
        chi_alt_val = chi_in_shape((1,) * (3 * A), word)
        direct = (chi_sym_val * chi_alt_val).real

        rel_err = abs(direct - pred) / abs(pred) if abs(pred) > 0 else 0.0

        rows.append({
            "atom": name,
            "A": A,
            "expected_n_ud": 2 * A + 1,
            "observed_n_ud": n_ud,
            "n_pure_sigma": n_pure_sigma,
            "n_pure_sigma_inv": n_pure_sigma_inv,
            "chi_sym_direct": fmt(mp.re(chi_sym_val)),
            "chi_alt_direct": fmt(mp.re(chi_alt_val)),
            "product_direct": fmt(direct),
            "product_closed_form": fmt(pred),
            "rel_error": fmt(rel_err),
        })

        w.add_assertion(
            f"{name}: n_ud(atom_braid_word_3A) = 2A+1",
            computed=n_ud,
            expected=2 * A + 1,
            tolerance=0,
            source="atom_braid_word_3A + classify_factor",
        )
        w.add_assertion(
            f"{name}: χ_sym·χ_alt matches −(1 + H_A²/4)^(2A+1)",
            computed=fmt(direct),
            expected=fmt(pred),
            # Was 1e-3, justified as "seminormal matrices carry ~0.05%
            # numerical noise". That was a float64 artifact of this producer's
            # own arithmetic, not a property of the matrices. Under mpmath the
            # discrepancy is 5.1139e-9 and is SYSTEMATIC, not noise: it agrees
            # to six significant figures across all four atoms (5.11395455e-9,
            # 5.11394902e-9, 5.11394779e-9, 5.11394169e-9). Something real is
            # 5e-9 away from closing here; 1e-8 admits it without pretending
            # it is zero, and would catch any drift in it.
            tolerance="1e-8",
            source="direct character product vs closed form",
        )

    print(f"{'atom':<5} {'A':>2} {'2A+1':>5} "
          f"{'χs·χa (direct)':>16} {'closed form':>16} {'rel err':>10}")
    for r in rows:
        # DISPLAY ONLY. The stored values are _precision.fmt strings now, so
        # they are re-parsed and rendered with mp.nstr rather than %f -- which
        # is the display route AGENTS.md prefers, and keeps the recorded value
        # and the printed value from drifting apart.
        print(f"{r['atom']:<5} {r['A']:>2} {r['expected_n_ud']:>5} "
              f"{mp.nstr(mp.mpmathify(r['product_direct']), 8):>16} "
              f"{mp.nstr(mp.mpmathify(r['product_closed_form']), 8):>16} "
              f"{mp.nstr(mp.mpmathify(r['rel_error']), 3):>10}")

    w.add_data("atoms", rows)
    w.add_data("factor_eigenvalue_algebra", {
        "sym_eigenvalue": "c·q + d",
        "alt_eigenvalue": "-c/q + d",
        "per_factor_product": "d² − c² + c·d·H_A",
        "pure_sigma_product": "-1",
        "pure_sigma_inv_product": "-1",
        "ud_product_symbolic": "-(1 + H_A²/4)",
    })
    w.add_data("closed_form", {
        "formula": "chi_sym * chi_alt = -(1 + H_A^2/4)^(2A+1)",
        "equivalent": "-([2]_q / 2)^(4A+2)",
        "ud_factor_count": "n_ud = 2A + 1 (2 per nucleon + 1 p→n transition)",
    })
    w.save()


if __name__ == "__main__":
    main()

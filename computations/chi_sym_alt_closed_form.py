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
from mass_at_3A_proper import _cached_seminormal, atom_braid_word_3A, Q0_PROTON
from q_parameter import Q_50_DIGIT_STR, Q_MP
from _precision import fmt, set_compute_dps
from witness_base import WitnessBuilder

# ---------------------------------------------------------------------------
# PRECISION SETUP.  This must run BEFORE any module-level mpf is constructed.
#
# `set_compute_dps` was imported here and never called, so this producer ran at
# mpmath's DEFAULT dps=15 while `fmt` serialised at 50 -- `chi_in_shape` reads
# `dps = mp.mp.dps` as its working precision, so every seminormal entry was
# evaluated at 15 digits and then printed at 50.  That is the whole of the
# float64-padding red on this witness.  The call is idempotent.
set_compute_dps()

# The substrate parameter and the Hecke skein parameter, at FULL precision.
#
# Both were float64 before: `q_parameter.Q` is a Python float (AGENTS.md names
# this hazard explicitly -- "q_parameter.Q is a FLOAT64.  Use Q_50_DIGIT_STR"),
# and `hecke_core.h` is a float built from it.  `mp.mpmathify` of either
# preserves 17 digits and no more, which is exactly the fake precision the
# padding ratchet detects.
#
# `Q_50_DIGIT_STR` is ANCHOR-ADAPTIVE in the same way `Q` is -- `q_parameter`
# rebinds it from the anchor witness under `QOU_Q0_ANCHOR=ideal` -- so this
# swap fixes the precision without pinning the producer to proton.
Q0 = Q_MP
HA_VAL = Q0 - 1 / Q0


ATOMS = [
    # (name, Z, N)
    ("D",   1, 1),
    ("T",   1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
]


def classify_factor(c: float, d: float) -> str:
    """Return 'pure_sigma', 'pure_sigma_inv', 'ud', or 'pn_color'.

    `pn_color` used to fall through to the `other(...)` branch, where
    `count_factor_types` filed it under a key nothing asserted on. It is the
    colour-weighted p-n interface, `d = -h·(1/2 - δ/4)` with δ =
    flavor_split_subleading(q₀) ≈ 0.001376 — averaged like a `ud` letter but
    NOT equal to one, and there is exactly ONE of them per atom regardless of A.

    The distinction is load-bearing, not cosmetic: see `closed_form_prediction`
    below, where treating this letter as a `ud` letter is the entire source of
    the ~5.11e-9 residual this producer reports.
    """
    if abs(c - 1.0) > 1e-12:
        return f"other(c={c}, d={d})"
    if abs(d) < 1e-12:
        return "pure_sigma"
    if abs(d - (-HA_VAL)) < 1e-12:
        return "pure_sigma_inv"
    if abs(d - (-HA_VAL / 2)) < 1e-12:
        return "ud"
    # Averaged but not exactly -h/2: the colour-weighted p-n interface. The
    # window is wide (δ/4 ≈ 3.4e-4 of h) but far outside the 1e-12 `ud` test.
    if abs(d + HA_VAL / 2) < abs(HA_VAL) * 1e-2:
        return "pn_color"
    return f"other(c={c}, d={d})"


def count_factor_types(word):
    counts = {"pure_sigma": 0, "pure_sigma_inv": 0, "ud": 0, "pn_color": 0}
    for c, d, _g in word:
        k = classify_factor(c, d)
        counts[k] = counts.get(k, 0) + 1
    return counts


def pn_color_d(word):
    """The p-n interface's `d`, read off the word rather than recomputed.

    Returns None if the word has no colour-weighted letter (a colour-blind
    `pn_convention="strict_averaged"` word has none — its p-n interface is an
    ordinary `-h/2`, indistinguishable from a `ud` letter).
    """
    for c, d, _g in word:
        if classify_factor(c, d) == "pn_color":
            return mp.mpmathify(d)
    return None


def _q_sympy(dps):
    """The substrate parameter as a sympy Float at `dps` digits.

    Built from the 50-digit string so the substitution carries real digits;
    `sp.Float(<python float>)` would carry 17 whatever `dps` says.
    """
    return sp.Float(Q_50_DIGIT_STR, dps)


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
                    # sp.Float from the 50-digit STRING at working precision.
                    # Substituting the old float64 `Q0` capped every entry at
                    # 17 digits however large `dps` was.
                    M[i, j] = mp.mpmathify(sp.N(e.subs(q_sym, _q_sympy(dps)), dps))
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
    """Colour-BLIND closed form: -(1 + H_A²/4)^(2A+1).

    Kept as-is because it is the form stated in the corpus and formalised in
    `content/.../braids-and-knots/chi-sym-alt-closed-form.lean`. It raises the
    `ud` factor to the power 2A+1 — i.e. it treats the one colour-weighted p-n
    letter as though it were a 2A+1-th `ud` letter. It is not one, and that
    substitution is exactly the residual this producer reports. See
    `closed_form_prediction_exact`.
    """
    H_A = mp.mpmathify(H_A)
    return -(1 + H_A * H_A / 4) ** (2 * A + 1)


def _per_factor(d, H_A):
    """χ_sym·χ_alt for the Hecke element σ + d·1: (q+d)(-1/q+d) = d² - 1 + d·H_A."""
    d, H_A = mp.mpmathify(d), mp.mpmathify(H_A)
    return d * d - 1 + d * H_A


def closed_form_prediction_exact(A: int, H_A, d_pn=None):
    """Closed form with the p-n interface carried as itself: f_ud^(2A) · f_pn.

    The word has 2A `ud` letters at `d = -h/2` and ONE p-n letter at
    `d = -h(1/2 - δ/4)`. The colour-blind form above folds the second into the
    first; this one does not.

    WHY THE DIFFERENCE IS SO SMALL, which is the part worth understanding. The
    per-factor product is `f(d) = d² - 1 + d·h`, so `f'(d) = 2d + h`, which
    **vanishes identically at d = -h/2**. The `ud` letter sits at a stationary
    point of `f`. So perturbing it by the colour weighting costs second order,
    not first: `Δd/d ≈ 6.88e-4` produces `Δf ≈ (Δd)² ≈ 5.170e-9`.

    Predicted from that alone: 5.11397e-9. Measured by this producer before the
    correction: 5.11395e-9 (D), 5.11395e-9 (T), 5.11395e-9 (³He), 5.11394e-9
    (⁴He). Six significant figures.

    That stationary point is also why float64 hid this. The old `tolerance=1e-3`
    was justified by a comment about "~0.05% numerical noise" in the seminormal
    matrices; there is no such noise, and under exact arithmetic a real,
    identifiable, second-order colour term was sitting 200,000× inside it.
    """
    H_A = mp.mpmathify(H_A)
    f_ud = _per_factor(-H_A / 2, H_A)
    if d_pn is None:
        return f_ud ** (2 * A + 1)
    return f_ud ** (2 * A) * _per_factor(d_pn, H_A)


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
    # prop:, not rem:. This pointed at "rem:chi-sym-alt-closed-form", a block
    # that did not exist anywhere in content/ -- the label was a guess at a
    # block nobody had written. The block now exists as a PROPOSITION (the
    # Lean proves it sorry-free, and a proposition is the kind that takes the
    # .lean sibling), which also un-orphans chi-sym-alt-closed-form.lean.
    w.set_content_block("prop:chi-sym-alt-closed-form")
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

        n_pn = counts["pn_color"]
        d_pn = pn_color_d(word)

        pred = closed_form_prediction(A, HA_VAL)                       # colour-blind
        pred_exact = closed_form_prediction_exact(A, HA_VAL, d_pn)     # p-n carried

        chi_sym_val = chi_in_shape((3 * A,), word)
        chi_alt_val = chi_in_shape((1,) * (3 * A), word)
        direct = (chi_sym_val * chi_alt_val).real

        rel_err = abs(direct - pred) / abs(pred) if abs(pred) > 0 else 0.0
        rel_err_exact = (abs(direct - pred_exact) / abs(pred_exact)
                         if abs(pred_exact) > 0 else 0.0)

        rows.append({
            "atom": name,
            "A": A,
            # 2A, NOT 2A+1. The word has two `ud` letters per nucleon and one
            # colour-weighted p-n interface; the old expectation folded the
            # interface into the `ud` count, which is also what the closed form
            # does and is why it carries a residual. `nUd` in the Lean sibling
            # (chi-sym-alt-closed-form.lean) is likewise the 2A count.
            "expected_n_ud": 2 * A,
            "observed_n_ud": n_ud,
            "expected_n_averaged": 2 * A + 1,
            "observed_n_averaged": n_ud + n_pn,
            "n_pn_color": n_pn,
            "d_pn_color": fmt(d_pn) if d_pn is not None else None,
            "product_closed_form_exact": fmt(pred_exact),
            "rel_error_exact": fmt(rel_err_exact),
            "n_pure_sigma": n_pure_sigma,
            "n_pure_sigma_inv": n_pure_sigma_inv,
            "chi_sym_direct": fmt(mp.re(chi_sym_val)),
            "chi_alt_direct": fmt(mp.re(chi_alt_val)),
            "product_direct": fmt(direct),
            "product_closed_form": fmt(pred),
            "rel_error": fmt(rel_err),
        })

        w.add_assertion(
            f"{name}: n_ud(atom_braid_word_3A) = 2A",
            computed=n_ud,
            expected=2 * A,
            tolerance=0,
            source="two ud letters per nucleon; the p-n interface is NOT one",
        )
        w.add_assertion(
            f"{name}: n_averaged(atom_braid_word_3A) = 2A+1",
            computed=n_ud + n_pn,
            expected=2 * A + 1,
            tolerance=0,
            source="2A ud letters plus exactly one colour-weighted p-n "
                   "interface, independent of A (pp is σ, nn is σ⁻¹ — both "
                   "braid generators, neither averaged)",
        )
        w.add_assertion(
            f"{name}: χ_sym·χ_alt matches f_ud^(2A)·f_pn (p-n carried exactly)",
            computed=fmt(direct),
            expected=fmt(pred_exact),
            tolerance="1e-12",
            source="closed form with the colour-weighted p-n interface carried "
                   "as itself rather than folded into the ud power",
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

    print(f"{'atom':<5} {'A':>2} {'n_ud':>5} "
          f"{'χs·χa (direct)':>16} {'closed form':>16} {'rel(blind)':>11} "
          f"{'rel(exact)':>11}")
    for r in rows:
        # DISPLAY ONLY. The stored values are _precision.fmt strings now, so
        # they are re-parsed and rendered with mp.nstr rather than %f -- which
        # is the display route AGENTS.md prefers, and keeps the recorded value
        # and the printed value from drifting apart.
        print(f"{r['atom']:<5} {r['A']:>2} {r['expected_n_ud']:>5} "
              f"{mp.nstr(mp.mpmathify(r['product_direct']), 8):>16} "
              f"{mp.nstr(mp.mpmathify(r['product_closed_form']), 8):>16} "
              f"{mp.nstr(mp.mpmathify(r['rel_error']), 3):>11} "
              f"{mp.nstr(mp.mpmathify(r['rel_error_exact']), 3):>11}")

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

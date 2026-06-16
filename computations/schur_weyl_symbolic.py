#!/usr/bin/env python3
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
# DEPRECATION-CANDIDATE: witness was moved to computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""
Global H_{3A} Schur-Weyl decomposition — SYMBOLIC in q.

Per content/braids-and-knots/schur-weyl-mass-decomposition.md:

    tr_M(𝒜) = Σ_{λ ⊢ 3A} w_λ(q) · χ^λ(𝒜)

with
    w_λ(q) = s_λ(q, q⁻¹) / H_q(λ)           — Schur / q-hook weight
    H_q(λ) = Π_{x ∈ λ} [h_x(λ)]_q            — q-hook product
    s_λ(q, q⁻¹)                              — Schur function at two-variable spec.

Keeps q symbolic (sympy.Symbol) through the entire partition sum;
final evaluation at q₀ uses sympy.evalf(dps) for arbitrary precision.

Why symbolic (not numerical float / mpmath):

  1. The partition sum has p(3A) terms with alternating signs and
     cancellations of order 10^3—10^6.  Float/mpmath loses precision
     catastrophically; symbolic rational arithmetic is exact.
  2. q-integers [k]_q = (q^k − q^{-k})/(q − q^{-1}) vanish at roots
     of unity; symbolic sympy tracks the zero factor (cancels
     against numerators), avoids spurious "division by zero" at
     roots of unity.
  3. Output extends to residue computation: evaluating the symbolic
     expression at q = ζ_n via sympy.limit gives the residue directly,
     no contour integration needed.
  4. Exact verification of small-A cases (A=1: three partitions of 3,
     recovers prop:three-parameters-wedderburn).

Start with A ∈ {1, 2, 3, 4} — p(3) = 3, p(6) = 11, p(9) = 30,
p(12) = 77 partitions.  A = 4 (⁴He) is the first case where the
additive-H_3 approximation fails by ~5%.

Witness: schur-weyl-symbolic.witness.json
"""
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
from sympy import Rational, Symbol, Integer, latex

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as _Q_CANONICAL
from partition_utils import hook_lengths  # noqa: E402


# ─── Partition utilities ───────────────────────────────────────────────

def partitions_of(n):
    """Generate all partitions of n as decreasing tuples.

    Example: partitions_of(3) = [(3,), (2, 1), (1, 1, 1)].
    """
    def _gen(n, max_part):
        if n == 0:
            yield ()
            return
        for k in range(min(n, max_part), 0, -1):
            for tail in _gen(n - k, k):
                yield (k,) + tail
    return list(_gen(n, n))


# ─── Symbolic q-integers and q-hook product ───────────────────────────

def q_integer(k, q):
    """Symbolic [k]_q = (q^k - q^{-k}) / (q - q^{-1}).

    For k = 0 returns 0; for k = 1 returns 1.
    """
    if k == 0:
        return Integer(0)
    if k == 1:
        return Integer(1)
    return (q ** k - q ** (-k)) / (q - q ** (-1))


def q_hook_product(partition, q, simplify=True):
    """Symbolic H_q(λ) = Π_{x ∈ λ} [h_x(λ)]_q, as a sympy expression.

    F10 (PR #565): added `simplify=True` opt-out (default kept True
    for back-compat). Pass `simplify=False` from hot loops where the
    caller will further-process the expression. The product of
    q_integers is a pure rational expression in q, so `sp.cancel`
    suffices for normalisation and is significantly faster than
    `sp.simplify`. Ref: 2834792d (gemini review on PR #565).
    """
    hooks = hook_lengths(partition)
    result = Integer(1)
    for h in hooks:
        result *= q_integer(h, q)
    return sp.cancel(result) if simplify else result


def schur_at_two_vars(partition, q, simplify=True):
    """Schur function s_λ(q, q⁻¹) — specialisation to two Schur variables.

    By the principal specialisation formula for two variables:
        s_λ(q, q⁻¹)
          = Π_{x ∈ λ} [n - c_x(λ)]_q / [h_x(λ)]_q   (only for λ of
            length ≤ 2; generalises).

    For length-1 partition (n,): s_{(n)}(q, q⁻¹) = Σ_{k=0}^n q^{n-2k}
                                                = [n+1]_q (q-number)
    For length-2 partition (a, b) with b ≤ a:
        s_{(a,b)}(q, q⁻¹) = q^{-(a+b)} · (q^{2(a+1)} - q^{2b}) / (q² - 1)
    For length ≥ 3 the Schur function s_λ(q, q⁻¹) vanishes (only
    two variables, so any partition of length > 2 has zero Schur
    value via the Jacobi-Trudi / determinantal formula).
    """
    length = len(partition)
    if length > 2:
        return Integer(0)
    if length == 1:
        n = partition[0]
        # s_(n)(x_1, x_2) = h_n(x_1, x_2) = Σ_{k=0}^n x_1^k x_2^{n-k}
        # With x_1 = q, x_2 = q⁻¹ this is Σ q^{2k - n} = [n+1]_q · q^...
        # Direct computation:
        return sum(q ** (n - 2 * k) for k in range(n + 1))
    # length == 2
    a, b = partition
    # s_(a,b)(x_1, x_2) = (x_1^{a+1} x_2^b - x_1^b x_2^{a+1}) / (x_1 - x_2)
    # With x_1 = q, x_2 = q⁻¹:
    numer = q ** (a + 1) * q ** (-b) - q ** b * q ** (-(a + 1))
    denom = q - q ** (-1)
    # Pure rational in q; cancel suffices and is far faster than
    # simplify (gemini review on PR #565).
    return sp.cancel(numer / denom) if simplify else (numer / denom)


def schur_weyl_weight(partition, q, simplify=True):
    """w_λ(q) = s_λ(q, q⁻¹) / H_q(λ), simplified symbolically.

    .. warning::
        This is the **2-variable Schur weight**, NOT the canonical
        Jones-Markov weight y_λ(q).  The 2-variable Schur
        s_λ(q, q⁻¹) **vanishes for partitions with > 2 rows** —
        callers using this for Markov-trace assembly will silently
        drop the `(1^p)` sign-rep contribution and any other
        ≥3-row partition.

        For Markov-trace contexts (the QOU paper's tr_M = Σ y_λ χ^λ),
        use `wedderburn_jones_markov.global_wedderburn_sum_jones_markov`
        which calls `markov_weights_symbolic.solve_y_lambda` (Wenzl
        Schur principal specialization, the canonical y_λ).

        See `docs/audits/2026-05-08-p3-h-3a-divergence.md` for the
        full divergence quantification (-73.6% at D, -95.6% at T/³He).

    F10 (PR #565): `simplify=True` opt-out parameter; default kept
    True for back-compat. Hot-loop callers should pass False.
    Per gemini review, propagate `simplify` into `schur_at_two_vars`
    and use `sp.cancel` (not `sp.simplify`) since the result is a
    rational expression in q.
    """
    s = schur_at_two_vars(partition, q, simplify=simplify)
    if s == 0:
        return Integer(0)
    H = q_hook_product(partition, q, simplify=simplify)
    result = s / H
    return sp.cancel(result) if simplify else result


# ─── Specht character — Murnaghan–Nakayama ────────────────────────────
# Full classical χ^λ(π(𝒜)) via the S_n permutation cycle type of the
# atomic-braid word and the Murnaghan–Nakayama recursion.  This is
# the q = 1 limit of the Hecke-algebra character χ^λ_q; the full
# q-dependent refinement is a separate module (ribbon-tableau q-weights).

def specht_character_placeholder(partition, braid_word=None):
    """Trivial character χ^λ = 1 (legacy path). Use
    specht_character_atomic for the real Murnaghan–Nakayama value."""
    return Integer(1)


def specht_character_atomic(partition, Z, N, include_inter=True,
                             m_pp=1, m_pn=1, m_nn=1):
    """Classical χ^λ(π(𝒜)) — S_{3A} character evaluated on the
    permutation underlying the atomic braid word.  Uses
    Murnaghan–Nakayama.  Returns an integer (symbolic in no variables).

    P2.1 wiring: threads m_pp/m_pn/m_nn through.
    """
    from murnaghan_nakayama import character_on_atomic_braid
    chi, _cycle_type = character_on_atomic_braid(
        partition, Z, N, include_inter, m_pp, m_pn, m_nn)
    return Integer(chi)


# ─── Assembly ─────────────────────────────────────────────────────────

def global_wedderburn_sum_symbolic(A, q, char_kind="trivial",
                                     Z=None, N=None, include_inter=True,
                                     m_pp=1, m_pn=1, m_nn=1, simplify=True):
    """Σ_{λ ⊢ 3A} w_λ(q) · χ^λ(𝒜) as a sympy expression.

    Enumerates all p(3A) partitions of 3A.

    char_kind:
      "trivial"   — χ^λ = 1 (legacy path; partition of unity)
      "mn-atom"   — Murnaghan–Nakayama χ^λ(π(𝒜)) on the atomic-braid
                    permutation, parameterised by (Z, N) and the
                    dressed-quark mass multiplicities (m_pp, m_pn, m_nn).

    P2.1 wiring: threads m_pp/m_pn/m_nn through to specht_character_atomic
    and atomic_braid_word so that dressed-quark mass differentiation
    reaches the SW character at A ≥ 2 (where inter-nucleon structure
    differs by proton/neutron pairing). The q=1 limit of the Hecke
    character is still implicit; full q-deformation is a separate
    refinement (q-ribbon-tableau weights).

    Returns (sympy_expr, partitions_with_weights_list).
    """
    if char_kind == "mn-atom":
        if Z is None or N is None:
            raise ValueError("char_kind='mn-atom' requires Z and N.")
        if Z + N != A:
            raise ValueError(f"Z + N = {Z+N} != A = {A}")

    partitions = partitions_of(3 * A)
    terms = []
    total = Integer(0)
    for lam in partitions:
        w = schur_weyl_weight(lam, q, simplify=simplify)
        if char_kind == "mn-atom":
            chi = specht_character_atomic(lam, Z, N, include_inter,
                                          m_pp, m_pn, m_nn)
        else:
            chi = specht_character_placeholder(lam)
        if chi == 0:
            continue  # skip zero-character partitions entirely
        contrib = w * chi
        total += contrib
        terms.append({
            "partition": lam,
            # Per-term display values: keep simplify ON for human-
            # readable output regardless of outer caller's choice.
            "weight": sp.simplify(w),
            "character": chi,
            "contribution": sp.simplify(contrib),
        })
    return (sp.simplify(total) if simplify else total), terms


# ─── Per-stratum Schur-Weyl sums (P2.2b) ──────────────────────────────
#
# Per `prop:phi-q-tower-algebraic-stratification`, the mass formula sums
# over algebraic strata indexed by subsets S ⊆ {0, …, n-2} of crossings:
#
#   𝔪 = Σ_{λ ⊢ 3A} w_λ χ^λ(π_atomic)            (descended carrier)
#       + Σ_{|S|=1} Φ_q(|Σ_λ w_λ χ^λ(π_S)|)    (singleton tower)
#       + z² Σ_{|S|=2} Φ_q(|Σ_λ w_λ χ^λ(π_S)|) (pair tower)
#
# where π_S ∈ S_{3A} is the permutation of β_S = ∏_{i∈S} σ_i (each σ_i
# is the transposition (i, i+1) on 3A strands) and π_∅ = identity.
#
# The current `global_wedderburn_sum_symbolic` handles π_atomic via
# Murnaghan-Nakayama on the atomic-braid cycle type. The functions
# below extend this to the per-stratum permutations needed for the
# Φ_q tower terms, replacing the H_3-at-H_{3A} per-generator V_full
# approximation that drove |V̂_i| close to q_0 at light atoms.

def stratum_permutation(A, S):
    """Permutation π_S ∈ S_{3A} for the stratum braid β_S = ∏_{i∈S} σ_i.

    Each generator σ_i acts as the transposition (i, i+1) on the
    3A strands. Compose them in order of increasing i.
    """
    n = 3 * A
    perm = list(range(n))
    for i in sorted(S):
        if i + 1 >= n:
            raise ValueError(f"Generator {i} out of range for n=3A={n}")
        perm[i], perm[i + 1] = perm[i + 1], perm[i]
    return tuple(perm)


def per_stratum_sum_symbolic(A, S, q, simplify=True):
    """Σ_{λ ⊢ 3A} w_λ(q) · χ^λ(π_S) where π_S is the stratum permutation.

    Parameters
    ----------
    A : int        Number of nucleons (so 3A strands).
    S : iterable   Subset of generator indices (each in {0, …, 3A-2}).
    q : sympy.Symbol or rational

    Returns
    -------
    (sympy_expr, terms_list)
    """
    from murnaghan_nakayama import (
        cycle_type_of_permutation,
        mn_character,
    )
    perm = stratum_permutation(A, S)
    cyc = cycle_type_of_permutation(perm)
    partitions = partitions_of(3 * A)
    terms = []
    total = Integer(0)
    for lam in partitions:
        w = schur_weyl_weight(lam, q, simplify=simplify)
        chi = mn_character(lam, cyc)
        if chi == 0:
            continue
        contrib = w * chi
        total += contrib
        terms.append({
            "partition": lam,
            # Per-term display: simplify ON for readability.
            "weight": sp.simplify(w),
            "character": chi,
            "contribution": sp.simplify(contrib),
        })
    return (sp.simplify(total) if simplify else total), terms


def h3_additive_approximation_symbolic(A, q, simplify=True):
    """Additive-H_3 approximation: only partitions of shape (3), (2,1), (1,1,1).

    For A nucleons the current engine sums w_(3) + w_(2,1) + w_(1,1,1) per
    generator, for each of the 3A-1 generators — a crude approximation.

    Returns a sympy expression representing (w_sym + w_std + w_alt)^{3A-1}.

    F10 (PR #565): `simplify=True` opt-out parameter.
    """
    w_sym = schur_weyl_weight((3,), q, simplify=simplify)
    w_std = schur_weyl_weight((2, 1), q, simplify=simplify)
    w_alt = schur_weyl_weight((1, 1, 1), q, simplify=simplify)
    total_h3 = w_sym + w_std + w_alt
    raised = total_h3 ** (3 * A - 1)
    return sp.simplify(raised) if simplify else raised


def analyze_pole_structure(A, q, max_cyclotomic=12):
    """Find the roots of unity ζ_n where any w_λ(q) has a pole, for n ≤ max.

    A pole appears where [k]_q = 0 for some hook length k appearing in
    any λ ⊢ 3A.  [k]_q vanishes at primitive 2k-th roots of unity (for q
    as primitive m-th root of unity: [k]_q = 0 iff k divides m/2 for
    even m, or similar).

    More concretely we test each n in 2..max and each hook length h used.
    """
    partitions = partitions_of(3 * A)
    hook_set = set()
    for lam in partitions:
        hook_set.update(hook_lengths(lam))
    return {
        "partitions_count": len(partitions),
        "hook_lengths_used": sorted(hook_set),
        "roots_of_unity_relevant": sorted(hook_set),
    }


# ─── Main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("SCHUR–WEYL SYMBOLIC — global H_{3A} Wedderburn sum at q symbolic")
    print("=" * 80)

    q = sp.Symbol('q', positive=True, real=True)

    for A in [1, 2, 3, 4]:
        partitions = partitions_of(3 * A)
        print(f"\nA = {A}: p(3A = {3*A}) = {len(partitions)} partitions")
        print("-" * 50)

        # Global Wedderburn sum
        total, terms = global_wedderburn_sum_symbolic(A, q)
        # Additive-H_3 approximation
        h3_approx = h3_additive_approximation_symbolic(A, q)
        diff = sp.simplify(total - h3_approx)

        print(f"  Global Σ_{{λ⊢{3*A}}} w_λ · χ^λ (χ=1)  = "
              f"{sp.nsimplify(total)}")
        print(f"  Additive H_3^{{{3*A-1}}} approximation = "
              f"{sp.nsimplify(h3_approx)}")

        # Numerical at q_0
        q0 = Rational(int(_Q_CANONICAL * 10 ** 16), 10 ** 16)
        tot_num = float(total.subs(q, q0).evalf(30))
        tot_num_polynomial_q = expose_polynomial(total, q)
        h3_num = float(h3_approx.subs(q, q0).evalf(30))
        h3_num_polynomial_q = expose_polynomial(h3_approx, q)
        err_num = float(diff.subs(q, q0).evalf(30))
        err_num_polynomial_q = expose_polynomial(diff, q)
        err_rel = (err_num / tot_num * 100) if tot_num else 0.0
        print(f"  Global @ q₀ ≈ {q0!s:.<30}  = {tot_num:.12e}")
        print(f"  H_3 approx @ q₀ ≈ {q0!s:.<30}  = {h3_num:.12e}")
        print(f"  Residual (global - H_3_approx):          = {err_num:+.6e}")
        print(f"  Relative error of H_3 approx:            = {err_rel:+.4f}%")

        # Sample top-weight partitions
        terms_sorted = sorted(
            terms,
            key=lambda t: abs(float(t["contribution"].subs(q, q0).evalf(30))),
            reverse=True,
        )
        print(f"  Top 5 partitions by |contribution @ q₀|:")
        for t in terms_sorted[:5]:
            v = float(t["contribution"].subs(q, q0).evalf(30))
            v_polynomial_q = expose_polynomial(t["contribution"], q)
            print(f"    λ = {t['partition']!s:<24} w_λ(q₀) = {v:+.6e}")

    # Pole/hook structure
    print("\nHOOK / ROOT-OF-UNITY STRUCTURE")
    print("-" * 50)
    for A in [1, 2, 3, 4]:
        info = analyze_pole_structure(A, q)
        print(f"  A = {A}: {info['partitions_count']} partitions, "
              f"hook lengths used = {info['hook_lengths_used']}")
        print(f"    (every hook length h gives poles at primitive 2h-th "
              f"roots of unity via [h]_q = 0)")

    # Witness
    q0 = Rational(int(_Q_CANONICAL * 10 ** 16), 10 ** 16)
    results = {}
    for A in [1, 2, 3, 4]:
        total, terms = global_wedderburn_sum_symbolic(A, q)
        h3 = h3_additive_approximation_symbolic(A, q)
        results[f"A={A}"] = {
            "partition_count": len(partitions_of(3 * A)),
            "global_sum_symbolic": str(total),
            "global_sum_at_q0": str(total.subs(q, q0).evalf(30)),
            "h3_approx_symbolic": str(h3),
            "h3_approx_at_q0": str(h3.subs(q, q0).evalf(30)),
            "relative_err_pct": float(
                ((total - h3) / total * 100).subs(q, q0).evalf(30)
            ),
        }

    witness = {
        "computation": "schur-weyl-symbolic",
        "description": (
            "Global H_{3A} Wedderburn sum vs additive-H_3 approximation, "
            "computed symbolically in sympy with q kept as a Symbol. "
            "Implements prop:schur-weyl-mass-decomposition. Uses trivial "
            "Specht character (future iteration: plug in actual braid "
            "word's cycle type via Murnaghan-Nakayama)."
        ),
        "reference_block": "prop:schur-weyl-mass-decomposition",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": str(float(q0)),
            "evalf_dps": 30,
            "engine": "sympy",
        },
        "results_by_A": results,
    }
    out = Path(__file__).parent / "schur-weyl-symbolic.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
    print("\nLimitation: Specht character set to χ^λ(𝒜) = 1 (trivial).")
    print("Real braid plug-in requires Murnaghan-Nakayama evaluation at")
    print("the cycle type of the atomic braid word — next iteration.")

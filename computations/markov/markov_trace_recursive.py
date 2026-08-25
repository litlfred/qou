#!/usr/bin/env python3
"""
Recursive symbolic Markov-trace computer for arbitrary words in H_n(q).

Builds on the existing `gb_filtration_jet_tracker.HeckeElement` class
(which is already symbolic via the sympy `q` symbol) to expand any
braid word into the Hecke basis {T_w : w ∈ S_n}, then computes the
Markov trace by RECURSIVE descent on n via the Markov axiom

  tr_M(α · σ_n) = z · tr_M(α),    α ∈ H_n.

Plus base cases:
  tr_M(1_{H_n}) = 1   for all n,
  tr_M(σ_i)     = z   (Markov-axiom-derived).

Algorithm for tr_M(T_w) where w ∈ S_n:
  1. If w fixes position n (i.e., reduced word doesn't use σ_{n-2},
     0-indexed), then T_w ∈ H_{n-1} and recurse with smaller n.
  2. Otherwise, w uses σ_{n-2} (the highest generator of H_n).
     Find rightmost σ_{n-2} in canonical reduced word, cyclically
     rotate to put it at the end, drop it (Markov axiom), and
     reduce the remainder back into the H_n basis via HeckeElement.
     Each strip removes exactly one σ_{n-2} factor; ℓ(w) strictly
     decreases per recursive call → termination.
  3. Identity returns 1.

Memoization on `(perm, n)` keeps the computation fast across
atoms: S_n has finitely many basis elements, so each is computed
at most once per ambient n.

Output: markov-trace-recursive.witness.json (with H_3, H_4, H_5
example computations).
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402

from gb_filtration_jet_tracker import HeckeElement, perm_apply_s

# Sympy q, h, z (matching the jet_tracker convention)
q = sp.symbols("q", positive=True)
h_sym = q - 1 / q
z_sym = q**3 / (q**2 + 1)


def coxeter_length(perm: tuple) -> int:
    n = len(perm)
    return sum(1 for i in range(n) for j in range(i + 1, n) if perm[i] > perm[j])


def reduced_word(perm: tuple) -> list[int]:
    """Canonical reduced word for `perm` ∈ S_n via greedy descent.
    Returns list of generator indices (0-indexed: σ_0, σ_1, ...,
    σ_{n-2})."""
    n = len(perm)
    word = []
    p = list(perm)
    while coxeter_length(tuple(p)) > 0:
        for i in range(n - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]
                word.append(i)
                break
    return list(reversed(word))


@lru_cache(maxsize=None)
def tr_m_basis_element(perm: tuple, n: int | None = None) -> sp.Expr:
    """Compute tr_M(T_perm) for `perm` ∈ S_n recursively.

    Indexing convention: gen indices are 0-based; H_n's generators
    are σ_0, σ_1, ..., σ_{n-2} (n-1 generators).  The "highest"
    generator σ_{n-2} is the one peeled off via the Markov axiom
    (tr_M(α · σ_{n-2}) = z · tr_M(α) for α ∈ H_{n-1}).

    Memoised on (perm, n): each S_n basis element is reduced once
    per ambient algebra size."""
    if n is None:
        n = len(perm)
    if perm == tuple(range(1, n + 1)):
        return sp.Integer(1)
    word = reduced_word(perm)
    if not word:
        return sp.Integer(1)
    max_gen = max(word)
    # If max_gen < n - 2, w uses only generators σ_0..σ_{max_gen}, so
    # w ∈ H_{max_gen+2} ⊂ H_n.  Truncate to actual S_{max_gen+2} perm.
    if max_gen < n - 2:
        sub_perm = perm[: max_gen + 2]
        return tr_m_basis_element(sub_perm, max_gen + 2)
    # max_gen == n - 2: w uses the highest generator. Apply Markov
    # axiom via cyclic rotation.  Find rightmost σ_{n-2} in canonical
    # reduced word; remove it, cyclic-rotate the remainder.
    k = max(i for i, g in enumerate(word) if g == max_gen)
    rotated = word[k + 1 :] + word[:k]
    # `rotated` may still contain σ_{n-2} (if w had multiple occurrences).
    # In that case the basis-element expansion of `rotated` via
    # HeckeElement will produce a sum of T_{w'} with ℓ(w') ≤ ℓ(rotated)
    # = ℓ(w) - 1, so recursion strictly decreases length.
    #
    # MEASURED 2026-08-23: THAT CASE NEVER ARISES, and the distinction
    # matters for CORRECTNESS, not just termination. The Markov axiom
    # `tr(α·σ_{n-2}) = z·tr(α)` needs `α ∈ H_{n-1}`; below, `z_sym`
    # multiplies the trace of `rotated`, so if `rotated` still used
    # σ_{n-2} the axiom would be applied outside its hypothesis. Two
    # agents independently read this code and could not see the
    # argument (PR #5592 declined to depend on this module for exactly
    # this reason).
    #
    # It is safe because `reduced_word`'s canonical form uses the TOP
    # generator AT MOST ONCE. Verified exhaustively — every element of
    # S_3..S_7 (6, 24, 120, 720, 5040), max occurrence count 1, zero
    # elements with two. So `rotated` is always free of σ_{n-2} and
    # `α ∈ H_{n-1}` genuinely holds.
    #
    # The reason is the coset decomposition: S_n = ⊔_k S_{n-1}·d_k with
    # d_k = σ_{n-2}σ_{n-3}···σ_k and ℓ(w) = ℓ(u) + ℓ(d_k), so a reduced
    # word is a σ_{n-2}-free `u` followed by a `d_k` using it once.
    #
    # CAVEAT, because this is a property of the CANONICAL FORM and not
    # of reduced words in general: braid moves change the count
    # (`σ_1σ_2σ_1` has one σ_2, `σ_2σ_1σ_2` has two). A different
    # canonical form would break the argument silently. If `reduced_word`
    # is ever changed, re-run the exhaustive check before trusting this.
    E = HeckeElement.identity(n)
    for i in rotated:
        E = E.right_mul_T(i + 1)  # jet-tracker is 1-indexed
    result = sp.Integer(0)
    for w_prime, c in E.terms.items():
        result += c * tr_m_basis_element(w_prime, n)
    return sp.cancel(z_sym * result)


def markov_trace_of_word(n: int, word: list[int]) -> sp.Expr:
    """Compute tr_M(β) for β specified by `word` (signed integers,
    positive = σ_i, negative = σ_i^{-1}; jet-tracker 1-indexed).

    Reduces β to T_w basis via HeckeElement, then applies
    `tr_m_basis_element` to each basis term.  Memoisation across
    calls makes repeated atom evaluations cheap.
    """
    E = HeckeElement.identity(n)
    for i in word:
        if i > 0:
            E = E.right_mul_T(i)
        else:
            E = E.right_mul_T_inv(-i)
    result = sp.Integer(0)
    for w, c in E.terms.items():
        result += c * tr_m_basis_element(w, n)
    return sp.cancel(result)


def main() -> int:
    print("=" * 96)
    print(f"  Recursive symbolic Markov-trace reducer for arbitrary H_n words")
    print(f"  Memoised on basis elements; uses HeckeElement for braid + Hecke reductions.")
    print("=" * 96)

    from q_parameter import Q_MP
    from _precision import fmt, set_compute_dps

    # Set the mpmath working precision to COMPUTE_DPS.  Without this call
    # mp.dps sits at its default 15 and EVERY mpf below is really a float64
    # widened on output -- the "mp.dps no-op" failure the precision gates
    # exist to catch.  It was invisible while the only check was a 1e-3
    # comparison; the exact closed forms above disagreed at digit 17 and
    # the trailing digits came back dyadic, which is the signature.
    set_compute_dps()

    # Q_MP is an mpf carrying OUTPUT_DPS digits; float() would discard ~45
    # of them.  The legacy `results` fields below stay float (they are on
    # the raw-float64 baseline at 13 entries and draining them is a
    # separate arc), but everything ASSERTED is kept in mpmath and
    # serialized with _precision.fmt, so this producer adds zero new
    # float64 to the witness.  Baselines drain, they do not grow.
    q0_mp = Q_MP
    q0 = float(q0_mp)

    # Expected values are CLOSED FORMS in z and h, evaluated from this
    # module's own z_sym -- not decimals.  The Markov axioms fix
    # tr_M(σ_i) = z, tr_M(σ_iσ_j) = z², and so on for ANY z, so these
    # state what the axioms require rather than what one convention
    # happened to produce.  The reducer reaches the same numbers by an
    # independent route (braid expansion into the Hecke basis, then
    # recursive descent), so agreement is a real check.
    #
    # This column previously held convention-C decimals -- 0.4993,
    # 0.2493, 0.5514, 1.6332 -- which stayed put when z moved to D and
    # went on describing a convention the file no longer used.  A closed
    # form cannot go stale that way.
    z0 = sp.lambdify(q, z_sym, modules=["mpmath"])(q0_mp)
    h0 = q0_mp - 1 / q0_mp

    test_cases = [
        # (name, n, word, expected_at_q0, ref)
        ("identity_H3",                 3, [],                      mp.mpf(1),    "tr_M(1) = 1"),
        ("σ_1",                         3, [1],                     z0,           "Markov axiom: tr_M(σ_i) = z"),
        ("σ_1²",                        3, [1, 1],                  h0 * z0 + 1,  "Hecke quadratic: h z + 1"),
        ("σ_1σ_2",                      3, [1, 2],                  z0 ** 2,      "tr_M = z²"),
        ("σ_1σ_2σ_1 (w_0)",             3, [1, 2, 1],               z0 + h0 * z0 ** 2, "z + h z²"),
        ("σ_1^7 σ_2^4 (proton)",        3, [1] * 7 + [2] * 4,       None,         "no independent closed form — see note below"),
        ("σ_1^6 σ_2^4 σ_1^{-1} (neutron-like)", 3, [1] * 6 + [2] * 4 + [-1], None, "Markov 11-cross with inverse"),
        # H_4
        ("σ_1σ_2σ_3 (H_4)",             4, [1, 2, 3],               z0 ** 3,      "tr_M = z³"),
        ("σ_1σ_2σ_3σ_2σ_1 (H_4)",       4, [1, 2, 3, 2, 1],         None,         "non-trivial 4-strand"),
        # H_5
        ("σ_1σ_2σ_3σ_4 (H_5)",          5, [1, 2, 3, 4],            z0 ** 4,      "tr_M = z^4"),
        # H_6 deuteron-equivalent (disjoint clusters)
        ("σ_1σ_2σ_4σ_5 (deuteron disjoint)", 6, [1, 2, 4, 5],       z0 ** 4,      "tr_M = z^4 (disjoint H_3 ⊗ H_3)"),
    ]

    print(f"\n  {'name':<40} {'n':>2} {'tr_M(q_0)':>14} {'expected':>10} ref")
    print("  " + "-" * 92)

    results = []
    assertions = []
    # Full-precision values kept aside for the disjoint-product check, so
    # it compares mpf against mpf rather than the float64 legacy fields.
    mp_by_name: dict = {}
    # The closed forms are exact identities, so the only slack needed is
    # mpmath round-off at COMPUTE_DPS.  The old 1e-3 would have passed a
    # value wrong in its fourth decimal.
    TOL = mp.mpf("1e-45")

    for name, n, word, expected, ref in test_cases:
        try:
            tr_M_sym = markov_trace_of_word(n, word)
            # Evaluated at the full-precision mpf q_0, not float(q_0).
            tr_M_mp = sp.lambdify(q, tr_M_sym, modules=["mpmath"])(q0_mp)
            tr_M_at_q0 = float(tr_M_mp)
            mp_by_name[name] = tr_M_mp
            sym_str_short = (
                str(tr_M_sym)[:60] + ("..." if len(str(tr_M_sym)) > 60 else "")
            )
            ok = expected is None or abs(tr_M_mp - expected) < TOL
            tag = "✓" if ok else "✗"
            exp_str = mp.nstr(expected, 12) if expected is not None else "—"
            print(f"  {name:<40} {n:>2} {tr_M_at_q0:>14.6f} {exp_str:>16} {tag} {ref}")
            if expected is not None:
                # Serialized as strings via _precision.fmt: the drained
                # convention (qou-t0rf), and what keeps these 3n fields off
                # the raw-float64 baseline.
                assertions.append({
                    "name": f"closed_form::{name}",
                    "computed": fmt(tr_M_mp),
                    "expected": fmt(expected),
                    "passed": bool(ok),
                    "tolerance": fmt(TOL),
                    "source": f"Markov axioms — {ref}",
                })
            results.append({
                "name": name,
                "n": n,
                "word": word,
                "tr_M_at_q0": tr_M_at_q0,
                "tr_M_symbolic_short": sym_str_short,
                "tr_M_symbolic_full": str(tr_M_sym),
                "expected_at_q0": None if expected is None else fmt(expected),
                "reference": ref,
            })
        except Exception as exc:
            print(f"  {name:<40} {n:>2} ERROR: {type(exc).__name__}: {exc}")
            # An exception is a failure, not an absence of a result.  Record
            # it as one so it cannot leave allPassed true.
            assertions.append({
                "name": f"evaluates::{name}",
                "computed": "0",
                "expected": "1",
                "passed": False,
                "tolerance": "0",
                "source": f"{type(exc).__name__}: {exc}",
            })
            results.append({
                "name": name,
                "n": n,
                "word": word,
                "error": f"{type(exc).__name__}: {exc}",
                "reference": ref,
            })

    # Cache stats — evidence the memoisation pays off.
    cache_info = tr_m_basis_element.cache_info()
    print(f"\n  Memoisation stats:")
    print(f"    cache hits   = {cache_info.hits}")
    print(f"    cache misses = {cache_info.misses}")
    print(f"    cache size   = {cache_info.currsize}")

    # Disjoint-product property — the proposition's headline claim:
    #   tr_M(α ⊗ β) = tr_M(α) · tr_M(β)
    # for α on strands {1..k} and β on {k+2..n}.  Checked as
    # tr_M(H_6; σ_1σ_2σ_4σ_5) against tr_M(H_3; σ_1σ_2)², since σ_4σ_5 on
    # strands {4,5,6} is a copy of σ_1σ_2 on {1,2,3}.  A real test of the
    # reducer rather than of arithmetic: the left side runs the full H_6
    # descent, the right side never leaves H_3.
    print(f"\n  Disjoint-product property:")
    lhs_mp = mp_by_name.get("σ_1σ_2σ_4σ_5 (deuteron disjoint)")
    rhs_base = mp_by_name.get("σ_1σ_2")
    if lhs_mp is not None and rhs_base is not None:
        rhs_mp = rhs_base ** 2
        ok = abs(lhs_mp - rhs_mp) < TOL
        print(f"    tr_M(H_6; σ_1σ_2σ_4σ_5) = {mp.nstr(lhs_mp, 25)}")
        print(f"    tr_M(H_3; σ_1σ_2)²      = {mp.nstr(rhs_mp, 25)}   "
              f"{'✓' if ok else '✗'}")
        assertions.append({
            "name": "disjoint_product",
            "computed": fmt(lhs_mp),
            "expected": fmt(rhs_mp),
            "passed": bool(ok),
            "tolerance": fmt(TOL),
            "source": "prop:markov-trace-recursive-reducer § disjoint-product property",
        })
    else:
        print(f"    ✗ one of the two words failed to evaluate — cannot check")
        assertions.append({
            "name": "disjoint_product",
            "computed": "0",
            "expected": "1",
            "passed": False,
            "tolerance": "0",
            "source": "prop:markov-trace-recursive-reducer § disjoint-product property",
        })

    # The proton and neutron words carry NO expected value, deliberately.
    # What this file used to compare them against — "char_fast ≈ 1.6334" —
    # was a hardcoded convention-C decimal, not a live computation: there
    # is no char_fast function in the tree to call.  Under D the reducer
    # gives 1.8843…, so the check printed "✗ disagrees with char_fast"
    # while both the code and its output were correct; the stale constant
    # was the wrong party.  Checking a migrated value against a frozen
    # pre-migration decimal is worse than not checking it, because the
    # disagreement it reports is really agreement with the wrong thing.
    # No independent convention-D reference for these two words exists
    # yet.  When one does, assert against it here.
    print(f"\n  Proton / neutron: computed, NOT cross-checked — no live "
          f"independent reference (see comment).")

    witness = {
        "computation": "markov-trace-recursive",
        "description": (
            "Recursive symbolic Markov-trace computer for arbitrary "
            "H_n(q) words. Uses gb_filtration_jet_tracker.HeckeElement "
            "(symbolic in q via sympy) to expand braids into the "
            "Hecke basis, then applies recursive Markov-axiom descent "
            "for each basis element with LRU memoisation on (perm, n). "
            "Tested up to H_6 for representative atomic-braid words "
            "(proton, neutron-like, deuteron disjoint cluster)."
        ),
        "reference_blocks": [
            "prop:atomic-mass-gb-nf",
            "prop:categorical-mass-markov",
            "prop:markov-trace-axiomatic-closed-form",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        # Cache stats are runtime/ordering-dependent; printed to stdout
        # but deliberately omitted from the witness to avoid spurious
        # drift. Fresh runs reproduce identical mathematical content.
        "test_cases": results,
    }
    builder = WitnessBuilder.wrap_legacy(
        "markov-trace-recursive", witness, script_path=__file__, engine="sympy"
    )
    for a in assertions:
        builder.add_assertion(
            a["name"],
            a["computed"],
            a["expected"],
            tolerance=a["tolerance"],
            source=a["source"],
        )
    out = builder.save()
    print(f"\n  Witness: {out}")

    # This producer previously returned 0 unconditionally and published
    # `assertions: []` with `allPassed: true`, while printing "✗ disagrees
    # with char_fast" in the same run.  A gate that reports success without
    # examining anything is not a gate.
    failed = [a for a in assertions if not a["passed"]]
    if failed:
        print(f"\n  FAILED {len(failed)} of {len(assertions)} assertions:")
        for a in failed:
            print(f"    ✗ {a['name']}: computed {a['computed']!r}, "
                  f"expected {a['expected']!r}")
        return 1
    print(f"\n  All {len(assertions)} assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

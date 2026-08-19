#!/usr/bin/env python3


# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Canonical Jones-Markov trace for H_n(q) elements.

Implements the unique trace satisfying
  (M1) tr_M(ab) = tr_M(ba)         (cyclicity)
  (M2) tr_M(x · σ_{n-2}) = z · tr_M(x)   for x ∈ H_{n-1}
  (M3) tr_M(1) = 1
where z = q^3/(q^2 + 1) is the Markov parameter -- **convention D**
(SU(2)/Temperley-Lieb, Jones). Convention C's z = 1/(q^{1/2}+q^{-1/2})
was excised by owner ruling 2026-08-09; see
docs/coordination/trace-convention-registry.md.

This is the CANONICAL trace referenced in prop:categorical-mass-markov
explicit-values table:
  tr_M(1)         = 1
  tr_M(σ_0)       = z
  tr_M(σ_0σ_1)    = z²
  tr_M(σ_0σ_1σ_0) = hz² + z      (where h = q − q⁻¹)
  tr_M((σ_0σ_1⁻¹)²) ≈ 0.280     (figure-8)

PUBLISHED-VALUE CHANGE (2026-08-09, bean qou-wgta). The figure-8 entry read
0.182 above, and `prop:categorical-mass-markov` still publishes that. 0.182
is the CONVENTION-C value; measured at the proton pin, 40 dps:
    C  0.1823044859381152055431166494555094402144
    D  0.2801956422726949814331225775762076206173   (+53.70 %)
The exact form under D is (q^8-q^6+q^4-q^2+1)/(q^6+2q^4+q^2), with
chi^(2,1)(fig8) = q^4 - 2q^2 + 1 - 2q^-2 + q^-4. The content block has NOT
been updated -- that is bean item 19 (the paper) and needs an owner pass over
the table, not a silent edit here.

Differs from the Plancherel-weighted trace
  tr_Pl(x) = Σ_λ (d_q(λ)²/[n]_q!) χ_λ(x)/d_λ
used in hecke_core.atom_markov_trace and binding_3A — these do NOT
satisfy (M2) with the canonical z and give different values.

Strategy:
  1. Each H_n element is a linear combination of words over σ_0..σ_{n-2}.
  2. For each word, recursively reduce via:
     - if empty: tr = 1
     - if max_gen < n-2: recurse at H_{max_gen + 2}
     - if max_gen appears once: cyclic rotate to end → Markov II
     - if max_gen appears multiple times: commute via far-commutativity,
       apply Hecke σ² = hσ + 1, recurse.
  3. Braid-relation cases (σ_{top-1} between two σ_{top}) reduce via
     explicit σ_iσ_{i+1}σ_i = σ_{i+1}σ_iσ_{i+1}, then retry.
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
del _sys, _Path

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# Symbolic z, h — can be overridden numerically
import sympy as sp
from hecke_symbolic import q, HA as H_SYMB, z_markov as Z_SYMB


# Manual cache so we can pass depth THROUGH to _tr_M_word_impl
# (preserving the recursion-depth guard) while keeping depth OUT of
# the cache key (the result depends only on (word, n, z, h, max_depth)).
_TR_M_WORD_CACHE: dict = {}


def tr_M_word(word: tuple, n: int, z, h, *,
               depth: int = 0, max_depth: int = 200):
    """See _tr_M_word_impl.  Memoized when (z, h) are hashable (typical
    symbolic / numeric usage); falls back to direct call when they are
    not (e.g. mutable mpf wrappers).

    Many subwords repeat across the recursion tree at H_n with multiple
    top-generator occurrences, so caching collapses the worst-case
    2^(n-1) branching factor to polynomial in distinct (word, n) pairs.

    The recursion-depth guard is preserved: ``depth`` is propagated
    through the cached path to ``_tr_M_word_impl``, while the cache
    key intentionally excludes ``depth`` (the result of tr_M is
    depth-independent).
    """
    if depth > max_depth:
        raise RecursionError(
            f"tr_M recursion too deep: word={word}, n={n}")
    word_t = tuple(word)
    try:
        key = (word_t, n, z, h, max_depth)
        if key in _TR_M_WORD_CACHE:
            return _TR_M_WORD_CACHE[key]
    except TypeError:
        # z or h unhashable — bypass cache entirely.
        return _tr_M_word_impl(word_t, n, z, h,
                                depth=depth, max_depth=max_depth)
    result = _tr_M_word_impl(word_t, n, z, h,
                              depth=depth, max_depth=max_depth)
    _TR_M_WORD_CACHE[key] = result
    return result


def _tr_M_word_impl(word: tuple, n: int, z, h, *,
                     depth: int = 0, max_depth: int = 200):
    """Canonical Markov trace of a Hecke word in H_n(q).

    word: tuple of non-negative ints (generator indices σ_i).
    n: strand count (H_n has generators σ_0..σ_{n-2}).
    z, h: Markov parameter and q - q⁻¹ (symbolic or numeric).
    """
    if depth > max_depth:
        raise RecursionError(
            f"tr_M recursion too deep: word={word}, n={n}")
    if not word:
        return sp.Integer(1) if hasattr(z, "is_number") else 1
    max_gen = max(word)
    # Normalize to the word's natural algebra H_{max_gen+2}: the Markov
    # trace value is independent of the ambient n (the trace is consistent
    # under the H_{n} ⊂ H_{n+1} embedding), so n is advisory. We already
    # SHRINK when n is too large (max_gen < n-2); handle the symmetric
    # PROMOTE case (max_gen > n-2, a generator above σ_{n-2}) the same way.
    # Without this, top = n-2 is absent from the word, top_positions is
    # empty, and `top_positions[-1]` below raised IndexError on any word
    # whose highest generator exceeds σ_{n-2} (e.g. tr_M_word([1], 2)).
    if max_gen != n - 2:
        return tr_M_word(word, max_gen + 2, z, h,
                          depth=depth + 1, max_depth=max_depth)
    top = n - 2

    # Count top occurrences
    top_positions = [i for i, g in enumerate(word) if g == top]
    if len(top_positions) == 1:
        pos = top_positions[0]
        rest = word[pos + 1:] + word[:pos]
        return z * tr_M_word(rest, n - 1, z, h,
                              depth=depth + 1, max_depth=max_depth)

    # Multiple tops: rotate so the last top is at the rightmost position.
    last_top = top_positions[-1]
    rotated = word[last_top + 1:] + word[:last_top + 1]
    # Now rotated ends with top. rest = rotated[:-1].
    rest = rotated[:-1]
    if top not in rest:
        return z * tr_M_word(rest, n - 1, z, h,
                              depth=depth + 1, max_depth=max_depth)

    # rest contains another top. Find its position.
    inner_pos = len(rest) - 1 - rest[::-1].index(top)
    # Segment between inner_pos and end of rest
    segment = rest[inner_pos + 1:]

    # Case A: segment has no top-1 → we can commute inner top to end.
    if (top - 1) not in segment:
        # New word: prefix + segment + (top, top) → apply σ² = hσ + 1.
        prefix = rest[:inner_pos]
        new_base = prefix + segment  # type: ignore
        # tr_M((new_base) · σ² · 1) = h · tr_M(new_base · σ) + tr_M(new_base)
        term1 = tr_M_word(new_base + (top,), n, z, h,
                           depth=depth + 1, max_depth=max_depth)
        term2 = tr_M_word(new_base, n, z, h,
                           depth=depth + 1, max_depth=max_depth)
        return h * term1 + term2

    # Case B: segment contains σ_{top-1}.  The two adjacent tops bracket a
    # top-free segment that uses σ_{top-1} (and possibly lower generators):
    #
    #   prefix · σ_top · segment · σ_top      (prefix = rest[:inner_pos];
    #                                            segment is top-free)
    #
    # We must consume one σ_top so the word's length / top-count strictly
    # drops, using only the braid relation, the Hecke quadratic, and
    # far-commutativity — all exact in (z, h).
    prefix = rest[:inner_pos]
    tm1_positions = [i for i, g in enumerate(segment) if g == top - 1]

    # ── Sub-case B1: exactly one σ_{top-1} in the segment ────────────
    # segment = alpha · σ_{top-1} · beta with alpha, beta both top-1-free
    # (hence commuting with σ_top).  Slide both σ_top inward and braid:
    #   σ_top·alpha·σ_{top-1}·beta·σ_top
    #     = alpha · (σ_top σ_{top-1} σ_top) · beta            (far-commute)
    #     = alpha · (σ_{top-1} σ_top σ_{top-1}) · beta        (braid)
    # The result has exactly ONE σ_top, so the next call hits the
    # single-top Markov peel and descends.
    if len(tm1_positions) == 1:
        first_tm1 = tm1_positions[0]
        alpha = segment[:first_tm1]
        beta = segment[first_tm1 + 1:]
        new_word = prefix + alpha + (top - 1, top, top - 1) + beta
        return tr_M_word(new_word, n, z, h,
                          depth=depth + 1, max_depth=max_depth)

    # ── Sub-case B2: ≥2 occurrences of σ_{top-1} in the segment ──────
    # A single braid here leaves the remaining σ_{top-1}'s wedged between
    # two σ_top, so the top-count would not drop.  Instead, expand the
    # bracketed block  B = σ_top · segment · σ_top  into a (z,h)-linear
    # combination of words each carrying AT MOST ONE σ_top, via the
    # dedicated reducer below (braid + Hecke + far-commute only).  Each
    # resulting word descends through the single-top peel.
    expansion = _reduce_two_top_block(top, segment, z, h)
    total = sp.Integer(0)
    for sub_word, coeff in expansion:
        total += coeff * tr_M_word(prefix + sub_word, n, z, h,
                                    depth=depth + 1, max_depth=max_depth)
    return total


def _reduce_two_top_block(top: int, segment: tuple, z, h):
    """Reduce the bracketed block  B = σ_top · segment · σ_top  (where
    ``segment`` is *top-free*, i.e. uses only generators ≤ top-1) into a
    list of ``(word, coeff)`` pairs such that

        B  =  Σ_i coeff_i · word_i      (equal in H_top+2, exact in h)

    and every ``word_i`` contains AT MOST ONE occurrence of σ_top.

    The block is rewritten by the generic Hecke word reducer
    :func:`_hecke_normalize`, which applies the Hecke quadratic
    σ_i² = h·σ_i + 1 and the braid / commutation relations to drive every
    word to a unique Coxeter-reduced normal form (length-lexicographic
    least word per permutation).  In any reduced word for an element of
    H_{top+2}, the highest generator σ_top can appear at most once per
    descent run; the seminormal/Gröbner–Shirshov normal form for S_{top+2}
    in fact uses σ_top at most once.  We therefore obtain exactly the
    ≤1-top words required by the single-top Markov peel.
    """
    block = (top,) + tuple(segment) + (top,)
    return _hecke_normalize(block, h)


# Generic Hecke-algebra word reducer (braid + Hecke quadratic), exact in h.
_HECKE_NORM_CACHE: dict = {}


def _hecke_normalize(word: tuple, h):
    """Expand a Hecke word (tuple of non-negative generator indices) into
    its T_w normal-form basis: a list of ``(reduced_word, coeff)`` pairs,
    exact in ``h``.

    Implements the standard right-multiplication recursion in the
    Iwahori–Hecke algebra H_n(q) with σ_i² = h·σ_i + 1:

        T_w · σ_i = T_{w·s_i}                if ℓ(w·s_i) > ℓ(w),
                  = h·T_w + T_{w·s_i}        if ℓ(w·s_i) < ℓ(w).

    Each basis key is the permutation ``w`` (as a tuple); the stored word
    is the canonical reduced word, so every returned word is automatically
    Coxeter-reduced (hence uses each generator the minimal number of
    times).  Equal in H to the input word, independent of z.
    """
    try:
        key = (tuple(word), h)
        if key in _HECKE_NORM_CACHE:
            return _HECKE_NORM_CACHE[key]
    except TypeError:
        key = None

    n = (max(word) + 2) if word else 1
    # State: dict perm(tuple) -> coeff.  Start at identity.
    ident = tuple(range(n))
    terms = {ident: sp.Integer(1)}
    for g in word:
        new_terms: dict = {}
        for perm, coeff in terms.items():
            # Apply s_g (swap positions g, g+1) on the RIGHT: w -> w·s_g.
            lp = list(perm)
            lp[g], lp[g + 1] = lp[g + 1], lp[g]
            wsg = tuple(lp)
            if _coxeter_len(wsg) > _coxeter_len(perm):
                # length increases: T_w σ_g = T_{w s_g}
                new_terms[wsg] = new_terms.get(wsg, sp.Integer(0)) + coeff
            else:
                # length decreases: T_w σ_g = h T_w + T_{w s_g}
                new_terms[perm] = new_terms.get(perm, sp.Integer(0)) + h * coeff
                new_terms[wsg] = new_terms.get(wsg, sp.Integer(0)) + coeff
        terms = new_terms

    result = []
    for perm, coeff in terms.items():
        c = sp.cancel(coeff) if isinstance(coeff, sp.Basic) else coeff
        if c == 0:
            continue
        result.append((_reduced_word_for(perm), c))
    if key is not None:
        _HECKE_NORM_CACHE[key] = result
    return result


def _coxeter_len(perm: tuple) -> int:
    """Number of inversions of ``perm`` = Coxeter length in S_n."""
    nn = len(perm)
    return sum(1 for i in range(nn) for j in range(i + 1, nn)
               if perm[i] > perm[j])


def _reduced_word_for(perm: tuple) -> tuple:
    """Canonical reduced word (0-indexed generators) for ``perm`` ∈ S_n
    via greedy bubble-sort descent.  Returns a tuple of generator indices
    whose product (left-to-right) equals ``perm``."""
    nn = len(perm)
    p = list(perm)
    word = []
    changed = True
    while changed:
        changed = False
        for i in range(nn - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]
                word.append(i)
                changed = True
                break
    return tuple(reversed(word))


def tr_M_element(elem, n: int, z=Z_SYMB, h=H_SYMB,
                  ocneanu_fallback: bool = True,
                  simplify: bool = True):
    """Canonical Markov trace of a SymbolicHeckeElement.

    TRACE CONVENTION: **convention D** — SU(2)/Temperley-Lieb (Jones),
    z = q^3/(q^2+1), y_(1^3) = 0. The default `z=Z_SYMB` is
    `hecke_symbolic.z_markov`, switched C -> D on 2026-08-09 (bean qou-wgta
    item 4), so every call site that omits `z` gets D.

    Convention C (the full-Hecke Ocneanu trace with the axiom-pinned
    z = 1/(q^{1/2}+q^{-1/2}) of `rem:markov-axioms-primitive`, y_(1^3) != 0)
    was EXCISED by owner ruling 2026-08-09; the two differ by 195.8 ppm on
    beta_Bor. Registry: docs/coordination/trace-convention-registry.md.

    Note the name: under D this IS the trace whose closure gives the Jones
    polynomial, so "Jones-Markov" is now accurate. Under C it was not, and
    this docstring said so.

    Uses the recursive Markov-axiom reduction tr_M_word.  For braid
    words that the recursion cannot handle directly (e.g., multiple
    top-1 occurrences in both alpha and beta segments around a top
    generator), falls back to the Ocneanu-weight path
    (ocneanu_weights.canonical_markov_trace_via_ocneanu) which
    computes the same canonical trace via ω-weighted seminormal
    character sum.  Set ``ocneanu_fallback=False`` to keep the
    original NotImplementedError behaviour.

    ``simplify`` (default True for back-compat): apply ``sp.simplify``
    to the aggregated total before returning.  For elements with
    many terms this dominates the runtime — at A=3 (³He, 128 reduced
    terms, ~5000 sympy ops) the simplify step exceeds 30 minutes
    while the aggregation itself takes 60 ms.  Pass ``simplify=False``
    to return the unsimplified total; numerical evaluation
    (``.subs(q, q₀).evalf(...)``) is unaffected by simplification.
    The Markov-peel production path
    (`markov_peel.tr_M_atomic`) opts out of simplification.
    """
    total = sp.Integer(0)
    fallback_terms = {}
    for word, coeff in elem.terms.items():
        # Only non-negative generator indices (skip formal variables)
        if any(g < 0 for g in word):
            continue
        try:
            tr_w = tr_M_word(word, n, z, h)
            total += coeff * tr_w
        except (NotImplementedError, RecursionError):
            if not ocneanu_fallback:
                raise
            # Collect for Ocneanu fallback
            fallback_terms[word] = coeff
    if fallback_terms:
        # Rebuild a mini-element and delegate
        from hecke_symbolic import SymbolicHeckeElement
        sub_elem = SymbolicHeckeElement(fallback_terms)
        from ocneanu_weights import canonical_markov_trace_via_ocneanu
        from q_parameter import Q as _Q0
        # Ocneanu path wants the *substrate* parameter q, not the
        # Markov parameter z.  Determine whether z and h are purely
        # numeric; if so evaluate the fallback at the canonical q₀,
        # otherwise emit a tagged symbolic placeholder.
        def _is_symbolic(x):
            return isinstance(x, sp.Basic) and not x.is_number
        if _is_symbolic(z) or _is_symbolic(h):
            # Symbolic path — add a tagged placeholder
            # (caller evaluates numerically downstream).
            total += sp.Symbol(
                f"_ocneanu_fallback_n{n}_" + str(len(fallback_terms)),
                real=True)
        else:
            num = canonical_markov_trace_via_ocneanu(sub_elem, n,
                                                        q_val=float(_Q0))
            total += num
    if simplify and isinstance(total, sp.Basic):
        return sp.simplify(total)
    return total


# ── Prop table sanity ───────────────────────────────────────────

if __name__ == "__main__":
    from q_parameter import Q_50_DIGIT_STR
    import mpmath as _mp
    # NO FLOAT64 (standing owner directive). This block prints the
    # prop:categorical-mass-markov values table, so it runs at 50 dps.
    # It was `z_num = 1.0/(q0_num**0.5 + q0_num**(-0.5))` with an f64
    # `HA` -- convention C *and* float64 in one line. Both fixed here.
    _mp.mp.dps = 50
    q0_num = _mp.mpf(Q_50_DIGIT_STR)
    h_num = q0_num - 1 / q0_num
    z_num = q0_num ** 3 / (q0_num ** 2 + 1)   # convention D

    print("=" * 80)
    print("CANONICAL MARKOV TRACE — prop:categorical-mass-markov table")
    print(f"q₀ = {q0_num:.6f}, z = {z_num:.6f}, h = {h_num:.6f}")
    print("=" * 80)

    # Prop table
    TESTS = [
        ("𝟏 (photon)",           (),                1.0),
        ("σ₀ (polarisation)",    (0,),              z_num),
        ("σ₀σ₁ (gluon)",          (0, 1),            z_num ** 2),
        ("σ₀σ₁σ₀ (electron)",    (0, 1, 0),        h_num * z_num ** 2 + z_num),
        ("σ₁σ₀σ₁ (braid-equiv)", (1, 0, 1),        h_num * z_num ** 2 + z_num),
        ("σ₀² = hσ₀ + 1",        (0, 0),           h_num * z_num + 1),
    ]

    # The witness. This script is cited BY NAME in prf:categorical-mass-markov
    # as the way to reproduce its table, and it emitted nothing -- so the
    # block had nothing to put in `computation.witness`, and its nine quoted
    # values were traceable only by coincidence. A script cited as
    # authoritative while emitting no witness is unfalsifiable by the
    # pipeline: the 1e-40 gate below was real inside this file and invisible
    # outside it. Bean qou-ft3p.
    from witness_base import WitnessBuilder
    w = WitnessBuilder("markov-trace-canonical", engine="sympy")
    w.add_data("q0_50dps", _mp.nstr(q0_num, 50))
    w.add_data("z_convention_D", _mp.nstr(z_num, 50))
    w.add_data("h", _mp.nstr(h_num, 50))
    failures = 0

    print(f"\n  {'Word':>24} {'Computed':>14} {'Expected':>14} "
          f"{'Match':>6}")
    print("  " + "-" * 68)
    for name, word, expected in TESTS:
        n = max(word) + 2 if word else 1
        computed = _mp.mpf(str(tr_M_word(word, n, z_num, h_num)))
        expected = _mp.mpf(str(expected))
        # 1e-40, not 1e-9: at 50 dps a 1e-9 gate would pass a convention flip
        # (C vs D differ by 0.11 on z) AND an f64 regression.
        _ok = abs(computed - expected) < _mp.mpf("1e-40")
        failures += not _ok
        match = "✓" if _ok else "✗"
        print(f"  {name:>24} {float(computed):>+14.6f} "
              f"{float(expected):>+14.6f} {match:>6}")
        w.add_assertion("trM_" + name.split()[0], _mp.nstr(computed, 50),
                        _mp.nstr(expected, 50), tolerance=_mp.mpf("1e-40"))

    # Additional: figure-8 (σ₀σ₁⁻¹)². σ₁⁻¹ = σ₁ - h in our convention.
    print("\nFigure-8 (σ₀σ₁⁻¹)² via tr_M_element (symbolic q, eval at q₀):")
    from hecke_symbolic import (SymbolicHeckeElement, SymbolicHeckeDivision,
                                  HA as H_SYMB_full, q as q_sym)
    div = SymbolicHeckeDivision()
    s0 = SymbolicHeckeElement({(0,): sp.Integer(1)})
    s1_inv = SymbolicHeckeElement({(1,): sp.Integer(1),
                                     (): -H_SYMB_full})
    figure_8 = s0 * s1_inv * s0 * s1_inv
    figure_8, _ = div.reduce(figure_8, engine='laurent')
    # Symbolic trace
    tr_sym = tr_M_element(figure_8, 3)
    tr_num = complex(tr_sym.subs(q_sym, q0_num))
    tr_num_re = tr_num.real if abs(tr_num.imag) < 1e-9 else tr_num
    print(f"  tr_M (symbolic) = {sp.simplify(tr_sym)}")
    # "prop says ~ 0.182" was the CONVENTION C column of that same table.
    # Under D the figure-8 value is 0.280195642273 -- the table's other
    # column. The annotation stayed on C when the computation above moved to
    # D: the exact stale-annotation failure the table itself documents.
    print(f"  tr_M at q₀      = {tr_num_re}   (prop table, convention D: 0.280195642273)")
    w.add_data("figure8_trM_at_q0_convention_D", str(tr_num_re))
    w.add_data("figure8_trM_symbolic", str(sp.simplify(tr_sym)))
    path = w.save()
    print(f"\n  Witness: {path}")
    if failures:
        print(f"  FAILED {failures} of {len(TESTS)} prop-table assertions at 1e-40.")
    # The table printed a tick column and exited 0 regardless, so a convention
    # flip would have shown as a row of crosses that nothing acted on.
    raise SystemExit(1 if failures else 0)

#!/usr/bin/env python3
"""
Habiro cyclotomic coefficients a_m(K) for atomic braids.

Per content/braids-and-knots/full-pole-structure-mass-trace.md and
habiro-ring.md, the Markov trace of an atomic braid admits a
Habiro / cyclotomic expansion

    tr_M(T_w, q)  =  Σ_{m ≥ 0}  a_m(T_w) · (q; q)_m

with  (q;q)_m = (1-q)(1-q²)···(1-q^m)  the q-Pochhammer.

For finite-degree Laurent polynomials the cyclotomic expansion is
computed by sequential polynomial division:

    a_0(q)  =  p(q)  mod (1 - q)              (a constant in ℤ)
    p_1(q)  = (p(q) - a_0) / (1 - q)
    a_1(q)  =  p_1(q) mod (1 - q²)            (degree ≤ 1 in q)
    p_2(q)  = (p_1(q) - a_1) / (1 - q²)
    ...

For atomic-braid Markov traces, p(q) ∈ ℤ[q^{1/2}, q^{-1/2}].  Setting
check_q = q^{1/2} and clearing denominators gives p(check_q) ∈ ℤ[check_q, check_q^{-1}], to
which we apply the cyclotomic algorithm in check_q (i.e. expand in
(check_q;check_q)_m).  The Habiro property to verify is:

    INTEGRALITY:  every a_m(check_q) ∈ ℤ[check_q, check_q^{-1}]
    TERMINATION:  a_m = 0 for m exceeding the polynomial degree

Witness: habiro-coefficients-atomic.witness.json
"""

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import mpmath as mp
import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from sympy import Symbol, Rational, Integer, simplify, together, nsimplify

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as _Q_CANONICAL
from hecke_character_symbolic import q_character_on_braid_word
from canonical_braid_crossings import atom_canonical_crossings as atomic_braid_to_crossings
from schur_weyl_symbolic import partitions_of
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic


# (Z, N, include_inter) → chi-witness atom label.  Maps the canonical
# atomic-braid recipe to the chi-{label}-h{n}.witness.json cache so
# q_character_on_braid_word can return cached chi values.
_ATOM_CHI_LABEL_BY_ZN: dict[tuple[int, int, bool], str] = {
    (1, 0, False): "proton",
    (1, 0, True):  "proton",
    (0, 1, False): "neutron",
    (0, 1, True):  "neutron",
    (1, 1, True):  "deuteron",
    (1, 2, True):  "tritium",
    (2, 1, True):  "helium-3",
    (2, 2, True):  "helium-4",
}


def markov_trace_symbolic(Z, N, q, include_inter=True):
    """tr_M(T_w(Z,N), q) = Σ_{λ ⊢ 3A} y_λ(q) · χ^λ_q(T_w).

    Canonical Wenzl-bridge convention: y_λ via Wenzl Schur principal
    specialization (`y_lambda_wenzl_bridge_symbolic`).  Replaces the
    legacy 2-variable Schur weight `s_λ(q, q^{-1})/H_q(λ)` (which
    vanishes for partitions with > 2 rows, dropping the sign-rep
    contribution).  Per `docs/audits/2026-05-08-p3-h-3a-divergence.md`,
    y_λ is the canonical Markov-trace weight for q ≠ 1; the q=1
    classical Plancherel point is the only place where the two
    conventions agree.  Cross-checks against the 1 ppb canonical
    50-dps reducer (`cross-check-trM-1ppb.witness.json`) at q_0:
      proton:   1.0653062286131670
      neutron:  0.9232332971861535
      deuteron: 0.388286471547713  (`include_inter=True`)

    Performance: y_λ has sqrt(q) factors that make `sp.cancel`
    catastrophic for the deuteron's n=6 partition sum.  Workaround:
    work internally in check_q with q = u², so the sqrt(q) factors become
    polynomial check_q; the final result is back-substituted to q via
    check_q → sqrt(q).  Combined with the y_λ witness cache (n = 2..12)
    and the chi witness caches (`chi-{atom}-h{n}.witness.json`) for
    p / n / D / T / ³He / ⁴He, the full p + n + D pipeline runs in
    seconds instead of minutes.

    Returns a sympy expression in q.
    """
    A = Z + N
    crossings = atomic_braid_to_crossings(Z, N, include_inter=include_inter)
    q_pos = sp.Symbol("q", positive=True)

    # Work internally in u_internal where u_internal² = q.  This
    # eliminates sqrt(q) factors from y_λ before the symbolic
    # multiplication, keeping per-term sp.cancel polynomial-time
    # instead of catastrophic on the n=6 partition sum.
    u_int = sp.Symbol("_markov_trace_u_internal", positive=True)
    total_u = Integer(0)
    for lam in partitions_of(3 * A):
        try:
            w = y_lambda_wenzl_bridge_symbolic(tuple(lam))
            # y_lambda_wenzl_bridge_symbolic uses Symbol("q", positive=True)
            # internally; substitute u_int² for that q.
            w_u = w.subs(q_pos, u_int ** 2)
            if w_u == 0:
                continue
            # The witness-backed chi cache and its selector were removed
            # (bean qou-tnrz): the cache's glob had been inert since Phase-6,
            # so the selector argument chose nothing.
            chi = q_character_on_braid_word(lam, crossings, q)
            chi_u = chi.subs(q, u_int ** 2)
            if chi_u == 0:
                continue
            # Skip per-term sp.cancel: the deuteron n=6 case had
            # sympy spending minutes on cancel even after q→u² (the
            # accumulated chi numerators are large polynomials in check_q);
            # final sp.together at the end is sufficient for the
            # downstream to_u_polynomial and runs in ~1 s for D.
            if (w_u * chi_u).has(sp.nan) or (w_u * chi_u).has(sp.zoo):
                raise ValueError(f"NaN/Inf in λ = {lam}")
            total_u += w_u * chi_u
        except Exception as exc:
            raise RuntimeError(
                f"Markov trace symbolic failed at λ = {lam} "
                f"(A = {A}): {type(exc).__name__}: {exc}") from exc

    # Combine into a single fraction in u_int and reduce.  Working
    # in check_q (where u² = q, no sqrt) keeps sp.cancel polynomial-time
    # — the same operation on the back-substituted q-expression
    # (with sqrt(q) factors) hits the heuristic-GCD ceiling for
    # certain partition sums (e.g. the neutron's mixed σ/σ^{-1}/avg
    # word).  Cancel here in check_q, then back-substitute.
    total_u = sp.cancel(sp.together(total_u))
    return total_u.subs(u_int, sp.sqrt(q))


# The canonical output symbol for anything this module SERIALIZES (bean
# qou-0ndb). The witness fields are named `p_in_u` / `denom_in_u`, so their
# strings must say `u` — regardless of which symbol the caller happened to
# compute with. Before this, the name in the string was a property of the CALL
# SITE: `_habiro_coefficient_extract` passes `u`, `analyse_atomic_braid` passes
# `check_q`, and the same two field names therefore carried two different
# symbols. Every consumer then had to know which producer wrote the file, and
# the ones that guessed wrong failed SILENTLY — `sympify` mints a fresh symbol,
# `.subs` no-ops, and the expression stays symbolic until something far away
# tries to make a number of it. Four instances (bean qou-0ndb), the worst of
# which published `phi_8_mult: 0` for a documented scaling law (bean qou-s41x).
U_CANONICAL = sp.Symbol('u', positive=True, real=True)


def str_in_u(expr, sym) -> str:
    """Serialize `expr` (written in `sym`) as a string in the canonical `u`.

    Use this for ANY expression leaving this module as text. Keeping the
    in-memory expression in the caller's symbol is fine and intended — only the
    SERIALIZED form is normalised, which is what consumers parse.
    """
    if sym == U_CANONICAL:
        return str(expr)
    return str(sp.sympify(expr).subs(sym, U_CANONICAL))


def to_u_polynomial(expr_in_q, q, check_q):
    """Substitute q → u² and clear ALL check_q-denominators (including any
    cyclotomic / Markov-normalisation factors).  Returns
    (p_in_u, shift, denom) such that

        p_in_u(check_q)  =  check_q^{shift} · denom(check_q) · expr_in_q(u²)

    is a polynomial in check_q with no negative powers.  The Habiro
    expansion is then computed for p_in_u and the result is the
    cyclotomic decomposition of the Markov-renormalised Jones-like
    object (the Markov normalisation z^n = (check_q + check_q^{-1})^{-n} is
    absorbed into the prefactor).
    """
    expr_u = sp.together(expr_in_q.subs(q, check_q ** 2))
    num, den = sp.fraction(expr_u)
    num = sp.expand(num)
    den = sp.expand(den)
    # Clear check_q-denominator entirely: multiply by den and shift to make
    # the result a polynomial in check_q.
    p_raw = num
    if den != 1:
        # Already cleared: p_raw = num, total = num/den; multiply by den
        pass
    # Normalise to non-negative powers of check_q
    p_expanded = sp.expand(p_raw)
    poly = sp.Poly(p_expanded, check_q)
    coeffs = poly.all_coeffs()
    # Determine min and max exponent
    monoms = poly.monoms()
    if not monoms:
        return Integer(0), 0, str_in_u(den, check_q)
    min_pow = min(int(m[0]) for m in monoms)
    shift = -min_pow if min_pow < 0 else 0
    p_shifted = sp.expand(p_expanded * check_q ** shift)
    # The EXPRESSION keeps the caller's symbol (callers go on computing with
    # it); only the serialized denom is normalised to `u`. See str_in_u.
    return p_shifted, shift, str_in_u(sp.expand(den), check_q)


def cyclotomic_expansion(p_in_u, check_q, max_m=20):
    """Expand p(check_q) = Σ_m a_m(check_q) · (check_q;check_q)_m by sequential polynomial
    division.

    Algorithm.  At step m, p_m(check_q) is the running remainder.  We
    define

        a_m(check_q)  =  p_m(check_q)  mod (1 - check_q^{m+1})        (deg ≤ m)
        p_{m+1} = (p_m(check_q) - a_m(check_q)) / (1 - check_q^{m+1}) (exact division)

    so that p(check_q) = a_0 + a_1(1-check_q) + a_2(1-check_q)(1-u²) + ⋯.  The
    iteration terminates exactly when p_{m+1} = 0; if p has finite
    degree this happens at some m_max ~ √(2·deg p).

    Returns a list of dicts, one per m.
    """
    p = sp.Poly(sp.expand(p_in_u), check_q)
    coeffs = []
    current = p
    for m in range(max_m):
        if current.is_zero:
            break
        next_factor = sp.Poly(1 - check_q ** (m + 1), check_q)
        # Single sp.div gives BOTH a_m (= remainder, degree < m+1) and
        # quotient (= (current - a_m) / next_factor) in one call.
        # The previous implementation recomputed the quotient via a
        # second sp.div on `current.as_expr() - a_m_expr`, doubling
        # the work per iteration on a deg-194 polynomial.
        quotient, a_m = sp.div(current, next_factor, check_q)
        a_m_expr = a_m.as_expr()
        coeffs.append({
            # Normalised to the canonical `u` (bean qou-0ndb). This is THE field
            # the breakage rode on: `reconstruct` and every `load_a_m` parse it,
            # and until now its variable name depended on which symbol this
            # function was handed.
            "m": m,
            "a_m": str_in_u(a_m_expr, check_q),
            "deg_a_m": int(a_m.degree()) if a_m.as_expr() != 0 else 0,
            "integral": all(c.is_Integer for c in a_m.all_coeffs())
                          if a_m.as_expr() != 0 else True,
            # `current = quotient * next_factor + a_m` is exact by
            # construction of sp.div (the second sp.div in the prior
            # implementation always returned remainder=0); only flag
            # nonzero on a true PolynomialError.
            "remainder_nonzero": False,
        })
        current = quotient
    return coeffs


def reconstruct(coeffs_data, check_q, max_m=20):
    """Reconstruct p(check_q) = Σ a_m · (check_q;check_q)_m from the list to verify.

    `max_m` is VESTIGIAL — the loop iterates `coeffs_data`, not `range(max_m)`.
    Kept only because callers pass it positionally. Do not read it as a bound.

    BOTH symbol names, and that is the whole bug this function had (bean
    qou-s41x; root cause is bean qou-0ndb). `cyclotomic_expansion` renders its
    `a_m` strings using WHATEVER SYMBOL the caller handed it, so the name in the
    string is a property of the call site:

        habiro_coefficients_atomic.analyse_atomic_braid  passes `check_q`
        _habiro_coefficient_extract.analyse_atom         passes `u`

    Sympifying with only `check_q` in `locals` therefore left the `u`-rendered
    strings referring to a FRESH `Symbol('u')` — same name, but no assumptions,
    so not the caller's `Symbol('u', positive=True, real=True)`. The two never
    cancel:

        sympify("8 - 3*u**2", locals={"check_q": u}) - (8 - 3*u**2)
            ->  -3*u**2 + 3*u**2          # not 0

    which made `diff == 0` false for EVERY atom regardless of size, and so
    `reconstruction_matches` false corpus-wide. Mapping both names onto the
    caller's symbol is the fix; it cannot misfire, because a given string uses
    one name or the other and both resolve to the same object.
    """
    total = Integer(0)
    for entry in coeffs_data:
        m = entry["m"]
        a_m = sp.sympify(entry["a_m"], locals={"u": check_q, "check_q": check_q})
        poch = Integer(1)
        for k in range(1, m + 1):
            poch *= 1 - check_q ** k
        total += sp.expand(a_m * poch)
    return sp.expand(total)


class HabiroReconstructionFailed(RuntimeError):
    """A witness was asked for its coefficients while flagging its own
    reconstruction check as failed."""


def load_a_m(slug, sym, witness_dir=None, *, allow_failed_reconstruction=False):
    """Load `habiro-coefficients-<slug>.witness.json` as {m: a_m expression}.

    REFUSES a witness whose own `reconstruction_matches` is false (owner
    ruling, bean qou-s41x). That flag is the producer's statement that the
    coefficients it is handing you do not rebuild the polynomial they came
    from; a reader that takes them anyway is building on something the
    producer already disowned. Every previous reader ignored it — three
    verbatim copies of this function, none of which looked at the flag,
    while 21 of 25 witnesses advertised a failed self-check.

    Refuse rather than warn: the consumers compose these into a mirror
    difference and read off a cyclotomic multiplicity, and a warning on
    stderr in a long batch run is indistinguishable from no warning at all.
    That is how `phi_8_mult: 0` stayed published against a documented
    scaling law.

    `allow_failed_reconstruction=True` is the deliberate override, for
    diagnosing a bad witness rather than computing with it. It exists so
    that the escape hatch has to be written down at the call site.

    Both symbol names are mapped onto `sym` for the reason in `reconstruct`
    above: whether a string says `u` or `check_q` is a property of which
    producer wrote the file, not of the format (bean qou-0ndb).
    """
    import json
    from pathlib import Path

    base = Path(witness_dir) if witness_dir is not None else Path(__file__).resolve().parent
    path = Path(base) / f"habiro-coefficients-{slug}.witness.json"
    if not path.exists():                       # cluster subdir layout
        alt = Path(base).parent / f"habiro-coefficients-{slug}.witness.json"
        if alt.exists():
            path = alt
    data = json.loads(path.read_text())

    matches = data.get("reconstruction_matches")
    if matches is False and not allow_failed_reconstruction:
        raise HabiroReconstructionFailed(
            f"{path.name} carries reconstruction_matches: false — its own "
            f"check says these coefficients do not rebuild p(u). Refusing to "
            f"hand them to a caller. Regenerate the witness from its "
            f"producer; pass allow_failed_reconstruction=True only to "
            f"diagnose the file, not to compute with it."
        )

    out = {}
    for c in data.get("habiro_coefficients", []):
        out[c["m"]] = sp.sympify(
            c["a_m"].replace("^", "**"), locals={"u": sym, "check_q": sym}
        )
    return out


# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

def mirror_trace_diff_numerator(slug_x, slug_y, sym, witness_dir=None,
                                *, allow_failed_reconstruction=False):
    """Numerator of `tr_X - tr_Y`, in `sym` (= u, with q -> sym**2).

    THE THING NOT TO DO is subtract Habiro coefficients. `p = d * t` is the
    denominator-cleared numerator of a trace, so

        Sum d_a_m (sym;sym)_m  =  p_X - p_Y  =  d_X*t_X - d_Y*t_Y

    which is proportional to `t_X - t_Y` only when the denominators agree AT
    THE EVALUATION POINT. Proved in
    `QOU/Habiro/MirrorPairNormalisation.lean` (sorry-free):

        coeffDiff_at_coincidence : dX*t - dY*t = (dX - dY)*t

    so where the traces coincide the coefficient-difference collapses to the
    denominator GAP times the common value, and vanishes iff dX = dY there.

    Measured: under convention C, dX(1) = dY(1) on all seven canonical mirror
    pairs, so the shortcut was accidentally valid and the published C results
    stand as computed. Under convention D they differ by exactly a factor of 4
    on all seven, and every cyclotomic multiplicity collapses to 0 — including
    Phi_1, which MUST divide a true mirror difference because the halves
    coincide at q = 1.

    This helper is convention-agnostic: it differences the traces themselves,
    over a common denominator, which is correct in C and D alike (qou-0ndb).
    """
    import json
    from pathlib import Path

    q_local = sp.Symbol('q', positive=True, real=True)
    # Build in the CANONICAL positive `u`, not in whatever `sym` the caller
    # passed, and map to `sym` only at the end. An atomic tr_M lives in
    # Z[q^{1/2}, q^{-1/2}] (module docstring), so q -> sym**2 produces
    # (sym**2)**(k/2) for odd k; sympy denests that to sym**k ONLY when the
    # symbol is known positive. Against a bare Symbol('u') it stays nested and
    # every downstream Poly call dies with
    #     PolynomialError: (u**2)**(3/2) contains an element of the set of
    #     generators
    # Both callers construct their `u` with sp.symbols('u') — assumption-free —
    # so the helper cannot rely on the caller's symbol carrying the assumption.
    # This is the same defect class as qou-0ndb itself (a symbol that prints
    # identically but is a different sympy object), which is why the fix is the
    # same shape as `str_in_u` above: normalise inside, translate at the edge.
    def _load(slug):
        base = Path(witness_dir) if witness_dir is not None else Path(__file__).resolve().parent
        path = Path(base) / f"habiro-coefficients-{slug}.witness.json"
        if not path.exists():
            alt = Path(base).parent / f"habiro-coefficients-{slug}.witness.json"
            if alt.exists():
                path = alt
        d = json.loads(path.read_text())
        if d.get("reconstruction_matches") is False and not allow_failed_reconstruction:
            raise HabiroReconstructionFailed(
                f"{path.name} carries reconstruction_matches: false — refusing."
            )
        return d["tr_M_in_q"]

    return trace_diff_numerator(_load(slug_x), _load(slug_y), sym,
                                label=f"{slug_x} - {slug_y}")


def am_difference_is_valid(tr_x, tr_y, sym=None):
    """Is subtracting two witnesses' a_m a valid way to form their difference?

    Only when the two denominators AGREE. A witness's a_m expand its own
    denominator-cleared numerator `p = d*t`, so `Sum (a_m^X - a_m^Y)(u;u)_m` is
    `d_X*t_X - d_Y*t_Y`; that is proportional to `t_X - t_Y` iff `d_X = d_Y`
    (`QOU/Habiro/MirrorPairNormalisation.lean`, `coeffDiff_of_common_denom` /
    `coeffDiff_at_coincidence`, sorry-free).

    Whether it holds is a property of the CONVENTION, not of the code, which is
    why this is a runtime check rather than a rule anyone can apply by reading:

        convention C   d_p = d_n = 4u^19(u^2+1)          IDENTICAL -> valid
        convention D   d_p = 4u^18(u^4+1)^2, d_n = 4u^18  DIFFER   -> invalid

    So the same script is correct under C and wrong under D with no edit in
    between. Under C the atomic-STEP pairs (D-n, 3He-D, 4He-3He) already
    differed and were never valid. Measured, bean qou-lnog.
    """
    u_can = U_CANONICAL
    q_local = sp.Symbol('q', positive=True, real=True)

    def _den(tr_str):
        tr = sp.sympify(tr_str, locals={"q": q_local})
        tr_s = sp.powdenest(sp.expand(tr.subs(q_local, u_can ** 2)), force=True)
        return sp.fraction(sp.together(tr_s))[1]

    return sp.simplify(_den(tr_x) - _den(tr_y)) == 0


def require_am_differenceable(tr_x, tr_y, *, label="pair"):
    """Raise unless `am_difference_is_valid`. Preflight for a_m-differencing.

    Fails loudly instead of returning a plausible wrong polynomial. Nothing
    raises on its own here: the coefficient difference factors, carries
    cyclotomic content, and prints fine -- it is simply not the pair's. The
    honest fix at a call site that trips this is `trace_diff_numerator`.
    """
    if not am_difference_is_valid(tr_x, tr_y):
        raise AmDifferenceInvalid(
            f"{label}: the two witnesses' denominators differ, so subtracting "
            f"their a_m builds d_X*t_X - d_Y*t_Y, not the pair difference. "
            f"Use trace_diff_numerator(tr_x, tr_y, sym) and expand THAT "
            f"(bean qou-0ndb / qou-lnog)."
        )


class AmDifferenceInvalid(ValueError):
    """Raised when a_m-differencing would silently build the wrong object."""


def trace_diff_numerator(tr_x, tr_y, sym, *, label="pair"):
    """Numerator of `tr_x - tr_y` over a common denominator, in `sym`.

    Core of `mirror_trace_diff_numerator`, taking the two `tr_M_in_q` STRINGS
    directly so it also serves callers reading the combined atomic witness
    (`habiro-coefficients-atomic.witness.json`, whose entries are nested under
    `results` rather than living in per-slug files).
    """
    q_local = sp.Symbol('q', positive=True, real=True)
    # Build in the CANONICAL positive `u`, not in whatever `sym` the caller
    # passed, and map to `sym` only at the end. An atomic tr_M lives in
    # Z[q^{1/2}, q^{-1/2}] (module docstring), so q -> sym**2 produces
    # (sym**2)**(k/2) for odd k; sympy denests that to sym**k ONLY when the
    # symbol is known positive. Against a bare Symbol('u') it stays nested and
    # every downstream Poly call dies with
    #     PolynomialError: (u**2)**(3/2) contains an element of the set of
    #     generators
    # Every caller builds its `u` with sp.symbols('u') — assumption-free — so
    # the helper cannot rely on the caller's symbol carrying the assumption.
    # This is the same defect class as qou-0ndb itself (a symbol that prints
    # identically but is a different sympy object), which is why the fix has the
    # same shape as `str_in_u` above: normalise inside, translate at the edge.
    u_can = U_CANONICAL

    def _num_den(tr_str):
        tr = sp.sympify(tr_str, locals={"q": q_local})
        tr_s = sp.powdenest(sp.expand(tr.subs(q_local, u_can ** 2)), force=True)
        return sp.fraction(sp.together(tr_s))

    nx, dx = _num_den(tr_x)
    ny, dy = _num_den(tr_y)
    out = sp.expand(sp.expand(nx * dy) - sp.expand(ny * dx))
    if out.has(sp.Rational(1, 2)) or any(
        not e.is_Integer for e in out.atoms(sp.Pow)
        if e.base == u_can and not e.exp.is_Integer
    ):
        raise ValueError(
            f"{label}: half-integer powers of u survived denesting; "
            "the difference is not in Z[u, u^-1] and the cyclotomic expansion "
            "would be meaningless"
        )
    return out.subs(u_can, sym) if sym != u_can else out


def analyse_atomic_braid(label, Z, N, include_inter, q):
    print(f"\n── {label} (Z={Z}, N={N}) ──")
    p_q = markov_trace_symbolic(Z, N, q, include_inter=include_inter)
    # Skip sp.nsimplify in the log line — for the deuteron's
    # ~degree-194 rational over q this call alone takes >30 s while
    # adding zero diagnostic value (the polynomial is already in
    # its symbolic form).  Use the raw repr instead.
    print(f"  tr_M (in q) computed (free symbols: {p_q.free_symbols})")
    check_q = sp.Symbol('check_q', positive=True, real=True)
    p_u, shift, denom = to_u_polynomial(p_q, q, check_q)
    deg_p = int(sp.Poly(p_u, check_q).degree()) if p_u != 0 else 0
    print(f"  → p(check_q) := check_q^{shift} · denom · tr_M(u²), shift = check_q^{shift}, "
          f"denom (in check_q) = {denom}")
    print(f"     deg p(check_q) = {deg_p}")
    coeffs = cyclotomic_expansion(p_u, check_q, max_m=20)
    print(f"  Habiro coefficients (in check_q = q^{{1/2}} = \\check{{q}}, spinor rate):")
    for entry in coeffs:
        flag = "✓" if entry["integral"] else "✗"
        print(f"    a_{entry['m']}(check_q) = {entry['a_m']}    "
              f"deg = {entry['deg_a_m']}, integral: {flag}")
    # Verify reconstruction
    recon = reconstruct(coeffs, check_q)
    diff = sp.expand(recon - p_u)
    if diff == 0:
        print(f"  ✓ reconstruction matches  Σ a_m·(check_q;check_q)_m  =  p(check_q)")
    else:
        print(f"  ✗ reconstruction error:  diff = {diff}")
    # Numerical check
    q0 = Rational(int(_Q_CANONICAL * 10 ** 16), 10 ** 16)
    u0 = sp.sqrt(q0)
    # Keep substrate precision via mp.mpf (was float() — flagged by
    # compute_no_mpf_to_float_cast). The witness field "tr_M_at_q0"
    # below requires it as the substrate-precision value.
    p_at_q0 = mp.mpf(str(p_q.subs(q, q0).evalf(50)))
    p_at_q0_polynomial_q = expose_polynomial(p_q, q)
    p_u_at_u0 = mp.mpf(str(p_u.subs(check_q, u0).evalf(50))) / mp.mpf(str(
        (u0 ** shift if shift else 1).evalf(50) if shift else 1))
    print(f"  tr_M @ q_0 = {mp.nstr(p_at_q0, 6, strip_zeros=False)}  "
          f"(via check_q-poly: {mp.nstr(p_u_at_u0, 6, strip_zeros=False)})")
    return {
        "Z": Z, "N": N, "include_inter": include_inter,
        # str(p_q) directly — sp.nsimplify on a degree-194 rational
        # adds 30+ seconds with no benefit for the witness consumer
        # (downstream re-parses with sp.sympify).
        "tr_M_in_q": str(p_q),
        "shift": int(shift),
        "denom_in_u": denom,
        "p_in_u": str_in_u(p_u, check_q),
        "deg_p_u": deg_p,
        "habiro_coefficients": coeffs,
        "all_integral": all(c["integral"] for c in coeffs),
        "reconstruction_matches": (diff == 0),
        "tr_M_at_q0": mp.nstr(p_at_q0, 30),
    }


if __name__ == "__main__":
    print("HABIRO CYCLOTOMIC COEFFICIENTS — atomic braids")
    print("=" * 80)
    print(f"q_0 = {float(_Q_CANONICAL):.6f}")

    q = sp.Symbol('q', positive=True, real=True)

    # A=1 (proton, neutron): tractable in symbolic q (~1 min total).
    # A=2 (deuteron): 11 partitions of 6 with Hoefsmit dim up to 9 in
    #   symbolic q over a 12-crossing braid — heavy (>10 min).  Run via
    #   `--with-deuteron` flag once a faster symbolic pipeline is wired
    #   up, or evaluate numerically at q_0 and verify integer coefficients
    #   of the resulting Laurent polynomial.
    import os
    cases = [
        ("p (proton, A=1)",      1, 0, False),
        ("n (neutron, A=1)",     0, 1, False),
    ]
    if os.environ.get("HABIRO_WITH_DEUTERON"):
        cases.append(("D (deuteron, A=2)", 1, 1, True))
    # A=3 (tritium, helium-3): 35-crossing braids over partitions of 9
    # (30 partitions) — substantially heavier than the deuteron's
    # 23-crossing / 11-partition case.  Gated behind HABIRO_WITH_A3 so
    # the default (p, n only) and the deuteron-only run stay cheap.  T and
    # ³He let path_b_habiro_mass_probe.py fill the A=3 rows and test the
    # sub-1% binding claim (bean t6ba follow-up).  Mirrors the
    # HABIRO_WITH_DEUTERON gate above.
    if os.environ.get("HABIRO_WITH_A3"):
        cases.append(("T (tritium, A=3)", 1, 2, True))
        cases.append(("3He (helium-3, A=3)", 2, 1, True))

    results = {}
    for label, Z, N, inter in cases:
        try:
            results[label] = analyse_atomic_braid(label, Z, N, inter, q)
        except Exception as exc:
            print(f"  {label}: ERROR {type(exc).__name__}: {exc}")
            results[label] = {"error": f"{type(exc).__name__}: {exc}"}

    print("\n── Summary ──")
    for label, r in results.items():
        if "error" in r:
            print(f"  {label}: ERROR {r['error']}")
            continue
        print(f"  {label}: deg p(check_q) = {r['deg_p_u']:>3}, "
              f"#Habiro coeffs = {len(r['habiro_coefficients']):>2}, "
              f"all integral: {r['all_integral']}, "
              f"reconstruction: {r['reconstruction_matches']}")

    # Merge-preserve (bean t6ba follow-up): a DEFAULT run (no HABIRO_WITH_DEUTERON
    # / HABIRO_WITH_A3) computes only p,n.  Writing `results` fresh would CLOBBER
    # an existing D / T / ³He row, silently regressing the witness below its
    # richest committed scope and re-breaking `path_b_habiro_mass_probe` (which
    # calibrates α_M off D).  Load any on-disk witness and preserve entries for
    # cases this run did not (re)compute; freshly computed cases always win.
    # Habiro coefficients are exact integers (deterministic), so a preserved
    # entry never goes stale unless the algorithm itself changes.
    _out_path = Path(__file__).parent / "habiro-coefficients-atomic.witness.json"
    if _out_path.exists():
        try:
            _prior = json.loads(_out_path.read_text()).get("results", {})
            for _label, _entry in _prior.items():
                if _label not in results and "error" not in _entry:
                    results[_label] = _entry
                    print(f"  [merge-preserve] kept prior witness entry: {_label}")
        except (json.JSONDecodeError, OSError):
            pass  # corrupt/unreadable prior — fall back to a fresh write

    witness = {
        "computation": "habiro-coefficients-atomic",
        "description": (
            "Habiro / cyclotomic expansion tr_M(T_w, q) = Σ_m a_m·(check_q;check_q)_m "
            "(check_q = q^{1/2}) for atomic braids p, n (default), D "
            "(HABIRO_WITH_DEUTERON=1), and T / ³He (HABIRO_WITH_A3=1). "
            "Verifies the integrality "
            "and termination properties of the Habiro coefficients claimed "
            "in habiro-ring.md and full-pole-structure-mass-trace.md."
        ),
        "reference_blocks": [
            "def:habiro-ring",
            "prop:full-pole-structure-mass-trace",
            "thm:knot-mass-formula-unified",
            "prop:e-infinity-page-identifications",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(_Q_CANONICAL),
            "engine": "sympy Poly + sequential cyclotomic division",
        },
        "results": results,
    }
    out = Path(__file__).parent / "habiro-coefficients-atomic.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")

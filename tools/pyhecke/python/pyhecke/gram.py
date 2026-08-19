"""Gram matrix G on the H_3(q) NF basis, NF multiplication, and exact
(Fraction) variants — canonical owner.

Authoritative source for:
  Constants   NF_BASIS, NF_NAMES, TR_M, z, W_SYM, W_STD, W_ALT, G,
              G_PINV, RADICAL
  Functions   hm, hm_exact, nf_tr, nf_net, gram_quotient_inverse
  Internals   _hm_dict, _reduce_nf, _build_gram

Moved here (with inversion in M2b) from the 3425-line
computations/hecke_core.py so there is a single
source of truth that downstream code can depend on. `hecke_core.py`
now imports these back for backward compatibility.

TRACE CONVENTION D (z = q^3/(q^2+1)) since 2026-08-15 — see the banner
at `z` below. Note for anyone comparing against a pre-2026-08-15
witness: values are NOT byte-identical to the pre-inversion
implementation any more. The M2b inversion preserved them exactly; the
C -> D convention change did not, and was not meant to (z moves +22.70%).
`G_INV` is GONE rather than renamed — under D the form is singular, so a
6x6 inverse does not exist; `G_PINV` is the inverse on the quotient
H_3(q)/rad and `RADICAL` is the null direction it quotients by.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np

from . import _legacy  # noqa: F401  — adjusts sys.path

# Prefer the in-repo computations/q_parameter shim (which
# _legacy puts on sys.path).  Fall back to the published qou_substrate
# package when pyhecke is used outside the repo (e.g. inside a Sage
# docker, on PyPI installs, in Pyodide, …).  Same fallback chain the
# `constants` module already uses — making it consistent here unblocks
# the SageMath + Pyodide smokes.
try:
    from q_parameter import Q as q0, Q_INV as qi, HA as h  # type: ignore[import-not-found]
except ImportError:
    from qou_substrate.constants import (  # type: ignore[import-not-found]
        Q as q0, Q_INV as qi, HA as h,
    )

# ⚠ `q0`, `qi`, `h` above are the **float64** path. They are deliberately
# bit-stable — `constants.py` says "Don't change them — downstream f64
# callers depend on stability" — so they are correct for existing witness
# scripts and must not be converted.
#
# They are ALSO an entry point into float64 for anything doing exact work:
# `h` differs from q₀ − q₀⁻¹ by 5.0e-17, and a caller who writes
# `float(G.h)` or drops `G.h` into mpmath arithmetic silently pins the
# whole computation to double precision with no signal.
#
# **The mpf counterparts already exist in this module** — use them:
#     h_mp(dps=50)   z_mp(dps=50)   tr_m_mp(dps=50)   gram_matrix_mp(dps=50)
# `h_mp()` agrees with q₀ − q₀⁻¹ to the last bit (1.3e-51 at 50 dps).
#
# Bean qou-jtbo; AGENTS.md "PROBES ARE NOT EXEMPT" (2026-08-18).


# ══════════════════════════════════════════════════════════════
# Scalar constants
# ══════════════════════════════════════════════════════════════

# ┌─────────────────────────────────────────────────────────────────────┐
# │ TRACE CONVENTION D. The C → D migration COMPLETED here 2026-08-15.  │
# └─────────────────────────────────────────────────────────────────────┘
#
# Owner ruling 2026-08-09 excised convention C (z = 1/(q^1/2 + q^-1/2)) in
# favour of convention D (z = q^3/(q^2 + 1)) repo-wide — registry
# docs/coordination/trace-convention-registry.md, bean qou-wgta. This module
# was the LAST deliberate exception, stopped at item 11 of that bean because
# `G_INV = np.linalg.inv(G)` ran unconditionally at import and convention D
# makes that Gram SINGULAR.
#
# The two facts the exception rested on were measured under qou-w8zz (PR #5025)
# and NEITHER SURVIVED. Both are recorded below, because the reasoning that
# held this line on C for months is worth more than the line itself.
#
# 1. THE DEGENERACY IS EXACT, not a precision artefact. This banner used to
#    quote det = 3.998e-17 / cond 4.9e+16 and note that even mpmath at 60 dps
#    "bottoms out at f64 noise, not a resolved eigenvalue". That is a
#    limitation of THIS module's float64 NF path, not of the question:
#    `z_D = q^3/(q^2+1)` and `h = q - 1/q` are RATIONAL in q, so at rational q
#    the whole Gram is exactly rational and sympy settles it —
#
#        q = 11/10, 7/5, 13/7  ->  det(G) = 0 EXACTLY, rank 5 of 6,
#                                  nullspace dimension exactly 1
#        convention C, same q  ->  rank 6, det != 0
#
#    and the null direction has a CLOSED FORM: the q-antisymmetriser
#    SUM_w (-1/q)^len(w) T_w, verified as `G @ v == 0` exactly at all three q.
#    It is carried below as `RADICAL`. That is also the Gram-side confirmation
#    of qou-u2jg, reached independently of the trace-side argument.
#
# 2. "EVERY CONSUMER EXPECTS A 6x6 INVERSE" was not so. Surveyed over .py
#    sources: constants.py 0 mentions, molecular.py 0, sdp.py 0, atom.py 1 (a
#    COMMENT recording the M2b move), __init__.py export list only. NOTHING in
#    the corpus multiplies by `G_INV` — no `@`, no `.dot`, no indexing. The one
#    thing the switch broke is a test asserting `G @ G_INV ~ I`, an identity
#    convention D makes FALSE — the test reporting the mathematics correctly.
#
# WHAT REPLACES IT. `G_PINV`, the inverse on the quotient H_3(q)/rad; see its
# note below for why the pseudoinverse is the honest object here and why
# `G_INV` is left UNDEFINED rather than rebound.
#
# STILL DIVERGENT — the Rust mirror. tools/hecke-engine/src/gram.rs ends
# `trace_weights` with `z*z*z` where `TR_M` below ends `h*z^2 + z` (the
# 2026-05-19 fix). That bug is load-bearing there for exactly the reason it was
# here: with the CORRECT TR_M[5] the form is singular, with `z^3` it is not
# (proved on the same probe, three q). So the Rust side needs TR_M[5] AND the
# quotient in ONE change — fixing the trace alone drops a singular Gram into
# the native path. Tracked as qou-m7py.
#
# ── historical record: what convention C measured here ───────────────
#
# Kept because the numbers are how the singularity was first noticed, and a
# future reader comparing against an older witness will need them.
#
# Measured here at the proton pin, on the BILINEAR form this module actually
# builds (`_build_gram` pairs b_i with b_j, no star):
#
#     convention C   eigenvalues -0.855067 +0.101797 +0.855067 x3 +3.476950
#                    det -0.18920521914403668     cond 3.4e+01   NON-singular
#
#     convention D   eigenvalues -0.752702  0.000000 +0.752702 x3 +4.230339
#                    det  3.998e-17                cond 4.9e+16  SINGULAR
#
# READ THE LEAN FILE'S OWN RETRACTION (commit 748ba9b1) BEFORE QUOTING THE
# SIGNATURE. Its original "(5,1) / (4,1) + null, LORENTZIAN" reading is
# WITHDRAWN: that used the bilinear pairing, and the Hecke *-structure is
# T_w* = T_{w^-1}, which on this NF basis swaps L+ <-> L-. Under the correct
# star pairing the form is C (6,0,0) POSITIVE DEFINITE, D (5,0,1) POSITIVE
# SEMIDEFINITE. What does NOT change, and is the only thing this note relies
# on: under D there is exactly ONE null direction, the row-cap one, under
# BOTH pairings. So det G = 0 and G_INV does not exist. C stays invertible
# either way, because y_(1^3) = 0.0227 != 0.
#
# And numpy does not protect you: `np.linalg.inv` on the D matrix RAISES
# NOTHING. It returns entries up to 7.6e15 with ||G @ G_INV - I|| = 1.64.
# A silently wrong `G_INV`, exported at import into constants.py, atom.py,
# molecular.py, sdp.py and nine corpus consumers, is far worse than the
# stale convention.
#
# AND THIS MODULE CANNOT SEE THE PROBLEM, because it is float64 end to end:
# `_hm_dict` / `_reduce_nf` build the NF coefficients in f64 and prune at
# `abs(c) > 1e-15`, so `G` carries ~16 good digits however much precision a
# caller wraps around it. Measured: driving this same NF path at mpmath 60 dps
# still bottoms out at |lambda_min| = 3.9e-17 and det = -5.3e-17 under D --
# f64 noise, not a resolved eigenvalue. The true value is 0; the branch's
# 50-dps figure (det = 2.89e-51, GramSignature.lean) comes from an exact NF,
# not from here. So the degeneracy is INVISIBLE to this module's own
# precision, and `np.linalg.inv` is inverting rounding noise -- which is
# exactly the observed cond 4.9e16 and ||G G_INV - I|| = 1.64.
#
# The exactness itself does not rest on any determinant: under D,
# y_(1^3) = 0 SYMBOLICALLY (verified three independent ways -- the sympy
# Wenzl solve in markov_weights_symbolic, the mpmath product formula in
# schur_principal_mpmath, and y_lambda_wenzl_bridge), so the (1^3)
# Wedderburn block contributes nothing to the trace form and IS the radical.
#
# The Lean file names the repair — quotient by the radical. Post-retraction
# that is a strictly better prospect than it first looked: the quotient is a
# genuine positive-definite inner product, not a causal form. The owner
# approved it 2026-08-15 and it is what `G_PINV` implements; the objection
# this paragraph used to carry ("every consumer expects a 6x6 inverse") is
# the one item 2 above measured and refuted, so it is struck rather than
# left standing next to its own refutation.
#
# THE NATIVE SPLIT — and note what it is NOT. The Rust mirror
# (tools/hecke-engine/src/gram.rs) IS convention D: `markov_z` there is
# already q^3/(q^2+1). Do not describe the crate as "on convention C".
# It diverges in the trace RULE and the ANCHOR instead:
#
#   * `trace_weights` ends `z*z*z` where `TR_M` below ends `h*z^2 + z`.
#     This is what keeps the crate's Gram non-singular, so it has no
#     radical and no quotient — hence the trace fix and the quotient must
#     land together (fixing the trace alone drops a singular Gram into a
#     path with nothing to handle it).
#   * `Q_0` is hardcoded to 1.1099785955541805, the MUON pin, against
#     AGENTS.md's proton default (2.19e-8 relative on z).
#
# `build_atom_nf` / `atom_per_generator_volumes` below dispatch to the
# compiled `pyhecke_native` wheel built from that crate. Since this module
# moved to D those two functions would return numbers from a different
# trace rule at a different anchor, so the dispatch now REFUSES rather
# than silently diverging — see the guard near `has_native`. Tracked as
# qou-m7py.
z = q0 ** 3 / (q0 ** 2 + 1)

# Wedderburn-Artin weights for H_3(q)
_q2 = q0 ** 2
_denom_w = _q2 ** 2 + 4 * _q2 + 1
W_SYM = _q2 / _denom_w
W_STD = (_q2 + 1) ** 2 / _denom_w
W_ALT = _q2 / _denom_w


# ══════════════════════════════════════════════════════════════
# NF basis and Markov-trace weights
# ══════════════════════════════════════════════════════════════

NF_BASIS: list[tuple[int, ...]] = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES: list[str] = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
# Markov-Ocneanu-Wenzl trace tr_M on the GB-NF basis of H_3(q).
# tr_M(γ) = 1; tr_M(σ_i) = z; tr_M(σ_i σ_j) = z² (i ≠ j, by Markov axiom).
# For e⁻ = σ_0·σ_1·σ_0: via Markov-trace recursion (cyclicity + σ_0² =
# h·σ_0 + 1) the correct value is h·z² + z, NOT z³ as listed prior to
# the 2026-05-19 fix (see docs/audits/2026-05-19-trm5-markov-bug.md).
TR_M = np.array([1.0, z, z, z ** 2, z ** 2, h * z ** 2 + z])


# Bond operators for molecular binding (per-generator crossing chains)
INV_TREFOIL_G0 = [(1, -h), (1, -h)]  # σ₀⁻¹σ₀⁻¹
INV_TREFOIL_G1 = [(1, -h)]  # σ₁⁻¹


# ══════════════════════════════════════════════════════════════
# NF multiplication in H_3(q)
# ══════════════════════════════════════════════════════════════

def hm(nf, c, d, gen):
    """Multiply NF element by (c·σ_gen + d·I). Returns new NF."""
    r = [0.0] * 6
    if gen == 0:
        tables = [
            (0, [(1, c), (0, d)]),
            (1, [(1, c * h), (0, c), (1, d)]),
            (2, [(3, c), (2, d)]),
            (3, [(3, c * h), (2, c), (3, d)]),
            (4, [(5, c), (4, d)]),
            (5, [(5, c * h), (4, c), (5, d)]),
        ]
    else:
        tables = [
            (0, [(2, c), (0, d)]),
            (1, [(4, c), (1, d)]),
            (2, [(2, c * h), (0, c), (2, d)]),
            (3, [(5, c), (3, d)]),
            (4, [(4, c * h), (1, c), (4, d)]),
            (5, [(5, c * h), (3, c), (5, d)]),
        ]
    for si, tgts in tables:
        if abs(nf[si]) < 1e-15:
            continue
        for ti, co in tgts:
            r[ti] += nf[si] * co
    return r


def nf_tr(nf):
    """Markov trace of NF element."""
    return sum(nf[i] * TR_M[i] for i in range(6))


def nf_net(nf):
    """Net (sum of NF coefficients)."""
    return sum(nf)


def nf_of_word(word, *, exact=False):
    """Normal-form 6-vector of a braid word in H_3(q).

    `word` is a tuple/list of generator indices (0 or 1); `()` is the
    identity. Built by right-multiplying the identity NF by each σ_gen
    (via `hm` / `hm_exact`, which fold in the GB reduction). With
    `exact=True` the result is a list of `Fraction`s."""
    if exact:
        nf = [Fraction(1), Fraction(0), Fraction(0),
              Fraction(0), Fraction(0), Fraction(0)]
        for g in word:
            nf = hm_exact(nf, Fraction(1), Fraction(0), g)
        return nf
    nf = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for g in word:
        nf = hm(nf, 1.0, 0.0, g)
    return nf


def markov_trace_combo(terms, *, exact=False):
    """Markov trace of a linear combination Σ cᵢ·σ_{wᵢ} in H_3(q).

    `terms` is an iterable of `(coeff, word)` pairs, where `word` is a
    tuple of generator indices (0/1). Because `nf_tr` is linear (a dot
    product with `TR_M`), the trace of a linear combination is

        tr_M(Σ cᵢ σ_{wᵢ}) = Σ cᵢ · tr_M(NF(σ_{wᵢ})).

    This is the thin linear-combination extension point called out in
    `docs/scope/2026-06-04-fibre-composite4-implementation-spec.md`
    Step 1. With `exact=True` the Fraction path (`hm_exact`/`_TR_M_FRAC`)
    is used; pass rational `coeff`s (int/Fraction) in that mode.

    Caveat (exact mode): under **convention D** both the NF reduction
    and the Markov weights are exact in ℚ — `_Z_FRAC` is now the exact
    `q³/(q²+1)` at the rational model, not the old 4-digit truncation
    that convention C's irrational `z = 1/(q^½+q^−½)` forced. The one
    remaining approximation is the *model* itself: the exact path runs
    at q = 111/100, not at the true substrate q₀ = 1.1099785827513808
    (1.93e-5 relative). So exact-mode and float-mode still differ at
    the ~1e-4 level, but the cause is now solely the rational q model;
    the float path remains the accurate one for the trace value."""
    if exact:
        acc = [Fraction(0)] * 6
        for c, word in terms:
            if isinstance(c, Fraction):
                cf = c
            elif isinstance(c, int):
                cf = Fraction(c)
            else:
                raise TypeError(
                    "markov_trace_combo(exact=True) requires int|Fraction "
                    f"coeffs (got {type(c).__name__}); pass exact rationals, "
                    "or use exact=False for float coeffs."
                )
            nfw = nf_of_word(word, exact=True)
            for i in range(6):
                acc[i] += cf * nfw[i]
        return sum(acc[i] * _TR_M_FRAC[i] for i in range(6))
    acc = [0.0] * 6
    for c, word in terms:
        nfw = nf_of_word(word)
        for i in range(6):
            acc[i] += c * nfw[i]
    return sum(acc[i] * TR_M[i] for i in range(6))


# ══════════════════════════════════════════════════════════════
# Gram matrix
# ══════════════════════════════════════════════════════════════

def _hm_dict(t1, t2):
    r = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            r[w] = r.get(w, 0.0) + c1 * c2
    return {w: c for w, c in r.items() if abs(c) > 1e-15}


def _reduce_nf(terms):
    changed = True
    while changed:
        changed = False
        new = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            for p in range(len(word) - 1):
                if word[p] == word[p + 1]:
                    i = word[p]
                    pre, suf = word[:p], word[p + 2:]
                    new[pre + (i,) + suf] = new.get(pre + (i,) + suf, 0) + coeff * h
                    new[pre + suf] = new.get(pre + suf, 0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            for p in range(len(word) - 2):
                a, b, c = word[p], word[p + 1], word[p + 2]
                if a == c and abs(a - b) == 1:
                    nt = (b, a, b)
                    if nt < (a, b, a):
                        nw = word[:p] + nt + word[p + 3:]
                        new[nw] = new.get(nw, 0) + coeff
                        done = changed = True
                        break
            if not done:
                new[word] = new.get(word, 0) + coeff
        terms = {w: c for w, c in new.items() if abs(c) > 1e-15}
    return terms


def _build_gram():
    G = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            prod = _hm_dict({NF_BASIS[i]: 1.0}, {NF_BASIS[j]: 1.0})
            nf = _reduce_nf(prod)
            vec = np.array([nf.get(b, 0.0) for b in NF_BASIS])
            G[i, j] = sum(vec[k] * TR_M[k] for k in range(6))
    return G


G = _build_gram()

#: The radical of the trace form under convention D, in closed form.
#:
#: `v_i = (-1/q)^len(w_i)` over NF_BASIS — the three-strand q-antisymmetriser
#: `SUM_w (-1/q)^len(w) T_w`. Established exactly over Q (rational arithmetic,
#: no floating point) at three independent rational q in
#: `computations/probes/gram_radical_exact_probe.py`: `det G = 0` EXACTLY,
#: rank 5 of 6, nullspace dimension exactly 1, and `G @ RADICAL == 0`.
#:
#: This is the Gram-side confirmation of `qou-u2jg` — "z_D is the unique
#: non-trivial Markov trace on H_3(q) whose radical contains the three-strand
#: antisymmetriser". Carried explicitly so the quotient below is built from the
#: proved projector rather than a numerically-extracted null vector, which at
#: this module's float64 precision would be indistinguishable from noise (the
#: old convention-C banner had to quote |lambda_min| = 3.9e-17 for exactly that
#: reason).
RADICAL = np.array([(-1.0 / q0) ** len(w) for w in NF_BASIS])

#: Inverse of the trace form ON THE QUOTIENT H_3(q)/rad.
#:
#: `G` is SINGULAR under convention D — that is what the radical above says —
#: so a 6x6 inverse does not exist and `np.linalg.inv(G)` does not say so: it
#: raises nothing and returns entries up to 7.6e15 with ||G @ G_INV - I|| = 1.64.
#: The Moore-Penrose pseudoinverse of a symmetric matrix with a one-dimensional
#: kernel IS the inverse on the orthogonal complement of that kernel, which is
#: the quotient. So this is the honest object, not an approximation to a
#: non-existent one.
#:
#: `G_INV` is deliberately NOT defined. It is not a rename: the old name meant
#: "inverse of G", an object convention D removes, and quietly rebinding it to
#: something else is how a wrong number keeps circulating under a trusted label.
#: A survey of the corpus found ZERO arithmetic consumers of it — no `@`, no
#: `.dot`, no indexing — so nothing is broken by its absence; see
#: `gram_inverse()` below for the migration error.
G_PINV = np.linalg.pinv(G)

# Identity NF: the trivial braid [1, 0, 0, 0, 0, 0]
_ID_NF = np.array([1.0, 0, 0, 0, 0, 0])


# ══════════════════════════════════════════════════════════════
# Exact rational NF computation via Fraction arithmetic
# ══════════════════════════════════════════════════════════════
# H_3(q) at q = 111/100 is exact in ℚ. Uses Python's Fraction — no
# floating point, no overflow.

_Q_FRAC = Fraction(111, 100)
_QI_FRAC = Fraction(100, 111)
_H_FRAC = _Q_FRAC - _QI_FRAC  # h = q - 1/q (exact rational)

# z = q³/(q²+1) — **convention D**, and now genuinely EXACT in ℚ.
#
# This is a structural win of the C → D migration, not a re-tuning.
# Under convention C, z = 1/(q^½ + q^−½) is irrational at q = 111/100
# (it needs √q), so the exact path could only carry the 4-digit
# truncation `Fraction(4993, 10000)` — an ~1e-4 error deliberately
# injected into an "exact" code path. Convention D's z is a rational
# *function* of q, so at a rational q it is a rational *number*:
#     z = (111/100)³ / ((111/100)² + 1) = 1367631/2232100
# exactly (1367631 = 3³·37³, 2232100 = 2²·5²·13·17·101 — coprime, so
# this is already in lowest terms). The `_Z_FRAC` truncation error is
# therefore GONE; the only remaining approximation on the exact path is
# the rational model q = 111/100 itself vs the true substrate
# q₀ = 1.1099785827513808 (a 1.93e-5 relative difference).
_Z_FRAC = _Q_FRAC ** 3 / (_Q_FRAC ** 2 + 1)  # == Fraction(1367631, 2232100)

_TR_M_FRAC = [Fraction(1), _Z_FRAC, _Z_FRAC,
              _Z_FRAC ** 2, _Z_FRAC ** 2,
              _H_FRAC * _Z_FRAC ** 2 + _Z_FRAC]  # fix 2026-05-19 (was _Z_FRAC ** 3)

_SYM_EIG_FRAC = [Fraction(1), _Q_FRAC, _Q_FRAC,
                 _Q_FRAC ** 2, _Q_FRAC ** 2, _Q_FRAC ** 3]
_ALT_EIG_FRAC = [Fraction(1), -_QI_FRAC, -_QI_FRAC,
                 _QI_FRAC ** 2, _QI_FRAC ** 2, -_QI_FRAC ** 3]


def hm_exact(nf, c, d, gen):
    """Exact Fraction multiplication: NF × (c·σ_gen + d·I).

    Same logic as hm() but with Fraction arithmetic — no rounding.
    """
    r = [Fraction(0)] * 6
    if gen == 0:
        tables = [
            (0, [(1, c), (0, d)]),
            (1, [(1, c * _H_FRAC), (0, c), (1, d)]),
            (2, [(3, c), (2, d)]),
            (3, [(3, c * _H_FRAC), (2, c), (3, d)]),
            (4, [(5, c), (4, d)]),
            (5, [(5, c * _H_FRAC), (4, c), (5, d)]),
        ]
    else:
        tables = [
            (0, [(2, c), (0, d)]),
            (1, [(4, c), (1, d)]),
            (2, [(2, c * _H_FRAC), (0, c), (2, d)]),
            (3, [(5, c), (3, d)]),
            (4, [(4, c * _H_FRAC), (1, c), (4, d)]),
            (5, [(5, c * _H_FRAC), (3, c), (5, d)]),
        ]
    for si, tgts in tables:
        if nf[si] == 0:
            continue
        for ti, co in tgts:
            r[ti] += nf[si] * co
    return r


# ══════════════════════════════════════════════════════════════
# Public API
# ══════════════════════════════════════════════════════════════

__all__ = [
    # Scalar constants
    "z", "W_SYM", "W_STD", "W_ALT",
    # NF basis
    "NF_BASIS", "NF_NAMES", "TR_M",
    # Bond operators
    "INV_TREFOIL_G0", "INV_TREFOIL_G1",
    # NF multiplication
    "hm", "hm_exact", "nf_tr", "nf_net", "nf_of_word", "markov_trace_combo",
    # Gram matrix
    "G", "G_PINV", "RADICAL", "gram_matrix", "gram_inverse",
    "gram_quotient_inverse",
    # 50-dps mpmath Gram / trace (NO float64)
    "z_mp", "h_mp", "tr_m_mp", "hm_mp", "gram_matrix_mp",
    "radical_mp", "gram_inverse_mp", "gram_quotient_solve_mp",
    "gram_matrix_mp_strings", "tr_m_mp_strings",
    # Native-dispatched atom kernels
    "build_atom_nf", "atom_per_generator_volumes", "has_native",
    # Exact-rational internals (rarely used externally)
    "_H_FRAC", "_Z_FRAC", "_TR_M_FRAC",
    "_SYM_EIG_FRAC", "_ALT_EIG_FRAC",
]


def gram_matrix() -> np.ndarray:
    """Return the 6x6 Gram matrix on the NF basis at q = q_0.

    NOTE: float64.  For a high-precision (50-dps) Gram with NO float64,
    use `gram_matrix_mp()` / `tr_m_mp()` instead — see the rationale in
    their docstrings (the irrational `z = 1/(q^½+q^−½)` makes an exact
    Fraction Gram impossible, so mpmath at 50 dps is the faithful path).
    """
    return G


def gram_inverse() -> np.ndarray:
    """REMOVED under convention D — `G` is singular, so `G^-1` does not exist.

    Raises rather than returning `G_PINV`. Silently substituting the
    pseudoinverse would answer a question the caller did not ask: they asked for
    an inverse, and under convention D there isn't one. A caller that wants the
    quotient must say so, because the two objects differ on the radical and that
    difference is the entire content of the convention change.
    """
    raise NotImplementedError(
        "gram_inverse() is removed: under convention D the H_3(q) trace form is "
        "SINGULAR (rank 5 of 6; the radical is the q-antisymmetriser, exported "
        "here as RADICAL), so G^-1 does not exist. Use G_PINV — the inverse on "
        "the quotient H_3(q)/rad — and check that the quotient is what you "
        "actually want. See the convention-D banner at the top of this module."
    )


def gram_quotient_inverse() -> np.ndarray:
    """Inverse of the trace form on the quotient `H_3(q)/rad` (float64)."""
    return G_PINV


def safe_inverse(M, *, what: str = "matrix", rcond: float = 1e-12) -> np.ndarray:
    """`np.linalg.inv` with the singularity guard numpy does not give you.

    **`np.linalg.inv` does NOT raise on the convention-D Markov Gram.** It
    returns a matrix with entries up to 7.6e15 and ``‖M @ inv - I‖ = 4.14``,
    measured. A caller that trusts it silently propagates numerical garbage
    into every downstream witness — which is precisely what happened to the
    two `gram_inverse` producers when this module moved C -> D, since they
    build their Gram from this module's `TR_M` but invert it themselves.

    This raises `LinAlgError` instead, naming the quotient inverse as the
    replacement. Use it anywhere a Gram-like form is inverted; the cost is
    one `svd` per call, which is nothing next to shipping a wrong witness.

    `rcond` is the relative singular-value floor: a value is treated as zero
    when it falls below ``rcond * s_max``. The default is deliberately far
    above float64 epsilon, because the smallest singular value of the
    degenerate Gram is ~5e-16 — i.e. *at* the noise floor, not
    distinguishable from it by magnitude alone (that is the whole reason
    `computations/probes/gram_radical_exact_probe.py` had to settle the
    question over ℚ rather than numerically).
    """
    M = np.asarray(M, dtype=float)
    s = np.linalg.svd(M, compute_uv=False)
    if s.size == 0 or s[0] == 0.0 or (s[-1] / s[0]) < rcond:
        rank = int((s > rcond * s[0]).sum()) if s.size and s[0] > 0.0 else 0
        cond = f"{s[0] / s[-1]:.2e}" if s.size and s[-1] > 0.0 else "inf"
        raise np.linalg.LinAlgError(
            f"{what} is singular (rank {rank} of {M.shape[0]}, "
            f"cond {cond}) -- "
            "np.linalg.inv would NOT have raised here, it would have returned "
            "inverted rounding noise. Under trace convention D the Markov Gram "
            "is degenerate and has no inverse; use "
            "`pyhecke.gram.gram_quotient_inverse()` (the inverse on "
            "H_3(q)/rad) and record it under a DIFFERENT witness key, since "
            "it is a different object from the G^-1 that older witnesses hold."
        )
    return np.linalg.inv(M)


# ══════════════════════════════════════════════════════════════
# 50-dps mpmath Gram / Markov trace — NO float64
# ══════════════════════════════════════════════════════════════
# Under **convention C** this block's premise held: `z = 1/(q^{1/2} +
# q^{-1/2})` is irrational at q = 111/100, so an exact rational Gram was
# impossible and the Fraction path had to approximate z by 4993/10000
# (4 digits, ~1e-4).
#
# Under **convention D** that premise is FALSE: `z = q³/(q²+1)` is a
# rational function, so at any rational q the whole Gram is exactly
# computable in ℚ. `computations/probes/gram_radical_exact_probe.py`
# does exactly that, and it is the only path that can *prove* the form
# is degenerate — over ℚ the determinant is exactly 0, where float64 can
# only report 3.998e-17 and mpmath only a smaller epsilon. Neither
# numeric path can distinguish "singular" from "very small".
#
# The mpmath path below is therefore no longer the *most faithful*
# path, only the most convenient high-precision numeric one: the NF
# reduction is exact in ℚ (via `nf_of_word(..., exact=True)`) and the
# Markov weight is evaluated at 50 dps at the true substrate q₀ (which
# the exact-ℚ path cannot do, since q₀ is not rational). Consumers that
# need a float64-free Gram (e.g. the clarabel-MPFR LP dual, which marshals
# 50-dps decimal strings across the FFI boundary) should source the Gram
# and trace here, not from the float64 `G` / `TR_M`.

import mpmath as _mp  # noqa: E402

_GRAM_MP_DPS = 60  # 50-dps target + 10 guard digits (compute-author §1)


def _q0_50dps_str() -> str:
    """Canonical 50-digit substrate q_0 as a decimal string (no float)."""
    try:
        from q_parameter import Q_50_DIGIT_STR  # type: ignore[import-not-found]
        return Q_50_DIGIT_STR
    except ImportError:
        from qou_substrate import Q_50_DIGIT_STR  # type: ignore[import-not-found]
        return Q_50_DIGIT_STR


def z_mp(dps: int = _GRAM_MP_DPS) -> "_mp.mpf":
    """z = q³/(q² + 1) at 50-dps mpmath — **convention D**, no float64.

    MIGRATED 2026-08-16 (bean qou-cds2). This returned convention C's
    1/(q^½ + q^−½) = 0.4993203…, and its docstring justified that by being
    "in lockstep with the module's float64 `z`". That stopped being true on
    2026-08-15, when the float64 `z` moved to D (commit 6086572c4): the
    justification outlived the fact it rested on. The mpmath mirror then sat
    18.5 % from the float64 original behind one import — and note which way
    that ran, because it is the opposite of the usual worry: the NO-FLOAT64
    path was the WRONG-convention one, so the more precise answer was the
    incorrect answer.

    Now rational, so the former "irrational" caveat no longer applies.
    """
    with _mp.workdps(dps):
        q = _mp.mpf(_q0_50dps_str())
        return +(q ** 3 / (q ** 2 + 1))  # unary + pins precision


def tr_m_mp(dps: int = _GRAM_MP_DPS) -> list:
    """Markov trace TR_M on the NF basis at 50-dps mpmath (NO float64).

    Mirrors the float64 `TR_M` exactly: [1, z, z, z², z², h·z²+z] with
    h = q − q⁻¹ and z the Markov weight at 50 dps.

    **Convention D**, genuinely in lockstep with the module's `z` as of
    2026-08-16 (bean qou-cds2) — the claim this docstring already made, now
    true. It was written when both were C, and survived the float64 side
    moving to D, which is how a module came to export two conventions while
    every docstring in it said otherwise.
    """
    with _mp.workdps(dps):
        q = _mp.mpf(_q0_50dps_str())
        qi_ = 1 / q
        hh = q - qi_
        z_ = q ** 3 / (q ** 2 + 1)
        return [_mp.mpf(1), +z_, +z_, +(z_ ** 2), +(z_ ** 2),
                +(hh * z_ ** 2 + z_)]


def _hm_mp(nf, c, d, gen, h_mp):
    """mpmath left-fold NF × (c·σ_gen + d·I), at the TRUE substrate q_0.

    Same structure-constant tables as the float64 `hm`, but with all
    coefficients in `mpmath.mpf` and `h = q_0 − q_0⁻¹` evaluated at the
    true 50-dps substrate q_0 (NOT the 111/100 rational of `hm_exact`).
    """
    r = [_mp.mpf(0)] * 6
    if gen == 0:
        tables = [
            (0, [(1, c), (0, d)]),
            (1, [(1, c * h_mp), (0, c), (1, d)]),
            (2, [(3, c), (2, d)]),
            (3, [(3, c * h_mp), (2, c), (3, d)]),
            (4, [(5, c), (4, d)]),
            (5, [(5, c * h_mp), (4, c), (5, d)]),
        ]
    else:
        tables = [
            (0, [(2, c), (0, d)]),
            (1, [(4, c), (1, d)]),
            (2, [(2, c * h_mp), (0, c), (2, d)]),
            (3, [(5, c), (3, d)]),
            (4, [(4, c * h_mp), (1, c), (4, d)]),
            (5, [(5, c * h_mp), (3, c), (5, d)]),
        ]
    for si, tgts in tables:
        if nf[si] == 0:
            continue
        for ti, co in tgts:
            r[ti] += nf[si] * co
    return r


def _nf_of_word_mp(word, h_mp):
    nf = [_mp.mpf(1)] + [_mp.mpf(0)] * 5
    for g in word:
        nf = _hm_mp(nf, _mp.mpf(1), _mp.mpf(0), g, h_mp)
    return nf


def h_mp(dps: int = _GRAM_MP_DPS) -> "_mp.mpf":
    """h = q_0 − q_0⁻¹ at 50-dps mpmath — the mpf counterpart of the float
    module constant `h`, which callers need to express σ_gen⁻¹ = σ_gen − h·I."""
    with _mp.workdps(dps):
        q = _mp.mpf(_q0_50dps_str())
        return +(q - 1 / q)


def hm_mp(nf, c, d, gen, dps: int = _GRAM_MP_DPS) -> list:
    """mpmath analogue of `hm`: NF × (c·σ_gen + d·I), NO float64.

    The mp path already had `_nf_of_word_mp`, but that folds only plain
    generators — it cannot express an INVERSE, which needs
    σ_gen⁻¹ = σ_gen − h·I, i.e. (c, d) = (1, −h). This is the public
    general-multiply the float side has exposed as `hm` all along; without
    it a caller wanting braid words with inverses has to reach for the
    private `_hm_mp` or re-implement the structure constants.
    """
    with _mp.workdps(dps):
        return [+v for v in _hm_mp([_mp.mpf(x) for x in nf],
                                   _mp.mpf(c), _mp.mpf(d), gen, h_mp(dps))]


def gram_matrix_mp(dps: int = _GRAM_MP_DPS, q=None) -> list:
    """6×6 Gram matrix G_{ij} = tr_M(b_i·b_j) at 50-dps mpmath — NO float64.

    Computed entirely at the TRUE substrate q_0 (Q_50_DIGIT_STR): the NF
    of the product word b_i·b_j is built by the left-fold `_hm_mp` with
    h = q_0 − q_0⁻¹ at 50 dps, and contracted with the 50-dps Markov
    weights `tr_m_mp` (which carry the irrational z).  Returns a
    list-of-lists of `mpmath.mpf`.

    This is the float64-free analogue of the canonical `G`: it agrees with
    `G` to ~1e-15 (both are at q_0).  Do NOT confuse with the
    `nf_of_word(..., exact=True)` / `hm_exact` Fraction path, which uses
    the *approximate* rational q = 111/100 (≈ 2e-4 from q_0) — see the
    `gram.py` 111/100-approximation audit note.

    `q` rebuilds the Gram at a DIFFERENT modulus (both h and the Markov
    weight z move with it), for controls that ask whether a property of G
    is structural in q or an accident at q_0. Default `None` keeps q_0, so
    every existing caller is unaffected. This is the supported replacement
    for assigning to the module global `_gram.h` and calling `_build_gram()`:
    that mutates shared state, is not thread-safe, and only ever gave the
    float64 Gram.
    """
    with _mp.workdps(dps):
        q = _mp.mpf(_q0_50dps_str()) if q is None else _mp.mpf(q)
        qi_ = 1 / q
        h_mp = q - qi_
        # Convention D (migrated 2026-08-16, qou-cds2; was C's
        # 1/(q^½ + q^−½)). Under D this Gram is SINGULAR on the full NF
        # basis — that is the fact which forced `G_INV`'s deletion on the
        # float64 side. It does not block anything here: this accessor only
        # BUILDS G and never inverts it, so a corank-1 form is a correct
        # return value rather than a hazard. The plan called this the
        # highest-risk item by carrying the float64 inverse's problem across
        # to a path that has no inverse.
        z_ = q ** 3 / (q ** 2 + 1)
        trm = [_mp.mpf(1), +z_, +z_, +(z_ ** 2), +(z_ ** 2),
               +(h_mp * z_ ** 2 + z_)]
        Gm = [[_mp.mpf(0)] * 6 for _ in range(6)]
        for i in range(6):
            for j in range(6):
                nf = _nf_of_word_mp(NF_BASIS[i] + NF_BASIS[j], h_mp)
                Gm[i][j] = +_mp.fsum(nf[k] * trm[k] for k in range(6))
        return Gm


def radical_mp(dps: int = _GRAM_MP_DPS, q=None) -> list:
    """The Gram radical at 50-dps mpmath — NO float64.

    The three-strand q-antisymmetriser `v_i = (-1/q)^len(w_i)` over
    `NF_BASIS`, i.e. the float64-free twin of the module constant `RADICAL`.
    Established exactly over Q at three independent rational q in
    `computations/probes/gram_radical_exact_probe.py` (det G = 0 EXACTLY,
    rank 5 of 6, nullspace dimension exactly 1), so this is the PROVED null
    direction, not one extracted numerically.

    Carried in mpmath because the numerical check that it *is* the null
    direction is precision-bound: `||G . v||` is 4.5e-62 at 60 dps and
    4.3e-121 at 120 dps — it tracks the working precision, which is what
    "exactly zero" looks like in floating point. At float64 it would be
    indistinguishable from noise.
    """
    with _mp.workdps(dps):
        qq = _mp.mpf(_q0_50dps_str()) if q is None else _mp.mpf(q)
        return [+((-1 / qq) ** len(w)) for w in NF_BASIS]


def gram_inverse_mp(dps: int = _GRAM_MP_DPS):
    """REMOVED under convention D — the mp Gram is singular, so `G^-1` does
    not exist. The mpmath twin of `gram_inverse()`.

    Raises rather than returning a quotient solve, for the same reason the
    float64 version does: the caller asked for an inverse, and under
    convention D there isn't one. Substituting the quotient silently would
    answer a different question.
    """
    raise NotImplementedError(
        "gram_inverse_mp() is removed: under convention D the H_3(q) trace "
        "form is SINGULAR (rank 5 of 6; the radical is the q-antisymmetriser, "
        "`radical_mp()`), so G^-1 does not exist. Note that `mp.lu_solve` "
        "does NOT raise on this matrix either — it returns entries of order "
        "1e50 with a visibly nonzero residual — so a caller who reached for "
        "lu_solve instead has the same bug without the error message. Use "
        "`gram_quotient_solve_mp` and check that the quotient is what you "
        "actually want."
    )


def gram_quotient_solve_mp(rhs, dps: int = _GRAM_MP_DPS, q=None):
    """Solve `G x = rhs` on the quotient `H_3(q)/rad` at mpmath precision.

    Returns `(x, radical_component)`:

      x                  the minimum-norm solution, orthogonal to the radical
      radical_component  the part of `rhs` ALONG the radical

    `G` is symmetric with a one-dimensional kernel spanned by the
    q-antisymmetriser `v`, so its range is exactly `v`-perp. An exact
    solution therefore exists **iff** `radical_component` is zero (to working
    precision); when it is not, the returned `x` solves the projected system
    and `radical_component` is the part that no `x` can reach. It is returned
    rather than discarded so a caller cannot mistake an unsolvable system for
    a solved one — which is precisely what `mp.lu_solve` does here, returning
    ~1e50 garbage without raising.

    Method: with `P` the projector off `v`, solve `(G + P_v) x = P rhs`. That
    matrix is invertible (it acts as `G` on `v`-perp, which is a bijection
    there, and as the identity on `v`), and its solution already lies in
    `v`-perp, so this is the exact minimum-norm solution — not a regularised
    approximation to one. This is the mpmath analogue of `G_PINV`, which is
    the Moore-Penrose pseudoinverse for exactly the same reason.
    """
    with _mp.workdps(dps):
        Gm = _mp.matrix(gram_matrix_mp(dps, q))
        v = _mp.matrix(radical_mp(dps, q))
        vv = _mp.fsum(v[i] * v[i] for i in range(6))
        b = _mp.matrix([_mp.mpf(x) for x in rhs])
        coeff = _mp.fsum(v[i] * b[i] for i in range(6)) / vv
        b_perp = _mp.matrix([b[i] - coeff * v[i] for i in range(6)])
        A = _mp.matrix(6, 6)
        for i in range(6):
            for j in range(6):
                A[i, j] = Gm[i, j] + v[i] * v[j] / vv
        x = _mp.lu_solve(A, b_perp)
        return [+x[i] for i in range(6)], +(coeff * _mp.sqrt(vv))


def gram_matrix_mp_strings(dps: int = _GRAM_MP_DPS) -> list:
    """`gram_matrix_mp` as decimal strings — ready to marshal across the
    PyO3 / CLI boundary to the clarabel-MPFR solver without any float64."""
    Gm = gram_matrix_mp(dps)
    return [[_mp.nstr(Gm[i][j], dps - 5) for j in range(6)] for i in range(6)]


def tr_m_mp_strings(dps: int = _GRAM_MP_DPS) -> list:
    """`tr_m_mp` as decimal strings (no float64) for FFI marshalling."""
    return [_mp.nstr(v, dps - 5) for v in tr_m_mp(dps)]


# ══════════════════════════════════════════════════════════════
# Native-accelerated atom kernels
# ══════════════════════════════════════════════════════════════
# When the `pyhecke_native` wheel is installed, these dispatch to the
# Rust implementation (~100× on ⁴⁰Ca). Fallback is hecke_core's pure
# Python. hecke_core is imported lazily at call time to avoid
# circular-import with pyhecke.gram's own loading.

try:
    import pyhecke_native as _native  # type: ignore[import-not-found]
    _HAS_NATIVE = True
except ImportError:
    _native = None
    _HAS_NATIVE = False


# ── NATIVE DISPATCH: convergence self-check (qou-m7py RESOLVED 2026-08-15) ──
#
# The qou-m7py port brought the crate and every language binding onto
# convention D: `gram::trace_weights_markov` (`TR_M[5] = h·z² + z`) drives
# `gram_matrix`/`nf_tr` and every binding's `trace_weights` export, `Q_0` is
# the proton pin, and `gram_inverse` was removed in favour of
# `gram_quotient_inverse` + `gram_radical`. A freshly-built wheel now matches
# this module exactly.
#
# The one residual risk is BUILD PROVENANCE: an OLD wheel (built before the
# port) is still on the legacy `z³` trace and/or the muon pin, and nothing in
# the wheel reports its build date. Merely installing such a wheel would
# silently change results. So rather than trust installation, `_native_ok()`
# runs a RUNTIME CONVERGENCE SELF-CHECK — it compares the installed wheel's
# `trace_weights`/`gram_matrix` against this module's convention-D reference
# (`TR_M`, `G`) at `q0`, and refuses LOUDLY on any mismatch. A correct wheel
# is enabled (~100× on ⁴⁰Ca); an old/divergent wheel is refused with a rebuild
# hint — no silent divergence either way. `QOU_DISABLE_NATIVE=1` is the
# explicit opt-out (debugging / forcing the pure-Python path).
_NATIVE_STALE_MSG = (
    "pyhecke_native is installed but DIVERGES from pyhecke.gram at q0 "
    "(convention-D self-check failed). This is almost certainly a wheel built "
    "before the qou-m7py convention-D port (2026-08-15): its trace_weights "
    "still ends z^3 and/or Q_0 is the muon pin. REBUILD it — "
    "`bash scripts/build-pyhecke-native.sh` (or `maturin develop` in "
    "tools/pyhecke-native) — then retry. Refusing rather than silently "
    "returning divergent numbers. Set QOU_DISABLE_NATIVE=1 to force the "
    "pure-Python path without rebuilding."
)

#: Cached result of the one-time runtime convergence self-check.
_NATIVE_VERIFIED: "bool | None" = None


def _verify_native_convergence() -> bool:
    """Compare the installed wheel against this module's convention-D
    reference at q0. Returns True iff it matches within f64 tolerance;
    otherwise emits a loud warning (never silently degrades) and returns
    False. Cached by `_native_ok`."""
    import warnings
    try:
        tw = np.asarray(_native.trace_weights(q0), dtype=float)
        gm = np.asarray(_native.gram_matrix(q0), dtype=float)
    except Exception as exc:  # pragma: no cover - defensive
        warnings.warn(
            f"pyhecke_native convention-D self-check could not run ({exc!r}); "
            "refusing the native path. " + _NATIVE_STALE_MSG,
            RuntimeWarning,
            stacklevel=2,
        )
        return False
    tol = 1e-9
    if np.allclose(tw, TR_M, atol=tol) and np.allclose(gm, G, atol=tol):
        return True
    warnings.warn(_NATIVE_STALE_MSG, RuntimeWarning, stacklevel=2)
    return False


def _native_ok() -> bool:
    """True iff the native path may be used: the wheel is installed, not
    explicitly disabled, and passes the runtime convention-D self-check.

    Resolved by qou-m7py (2026-08-15): the crate + bindings are on
    convention D, so an up-to-date wheel is ENABLED by default. An old,
    divergent wheel fails the self-check and is refused loudly (never
    silently). `QOU_DISABLE_NATIVE=1` forces the pure-Python path."""
    global _NATIVE_VERIFIED
    if not _HAS_NATIVE:
        return False
    import os
    if os.environ.get("QOU_DISABLE_NATIVE") == "1":
        return False
    if _NATIVE_VERIFIED is None:
        _NATIVE_VERIFIED = _verify_native_convergence()
    return _NATIVE_VERIFIED


def has_native() -> bool:
    """True iff the pyhecke_native wheel is installed.

    Reports *installation*. Usability additionally requires passing the
    runtime convention-D self-check and not being disabled via
    `QOU_DISABLE_NATIVE=1` — see `_native_ok`."""
    return _HAS_NATIVE


def build_atom_nf(Z: int, N: int):
    """Build the atom NF for (Z, N). Native-dispatched; falls back
    to hecke_core.build_atom_nf when the wheel is absent."""
    if _native_ok():
        return _native.build_atom_nf(Z, N)
    import hecke_core  # type: ignore[import-not-found]
    return hecke_core.build_atom_nf(Z, N)


def atom_per_generator_volumes(
    Z: int,
    N: int,
    include_inter: bool = True,
    crossings_per_pair: int = 1,
    m_pp=None, m_pn=None, m_nn=None,
):
    """Per-generator Wedderburn volumes for the atom braid. Native-
    dispatched; falls back to hecke_core.atom_per_generator_volumes
    when the wheel is absent."""
    if _native_ok():
        return _native.atom_per_generator_volumes(
            Z, N,
            include_inter=include_inter,
            crossings_per_pair=crossings_per_pair,
            m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
        )
    import hecke_core  # type: ignore[import-not-found]
    return hecke_core.atom_per_generator_volumes(
        Z, N,
        include_inter=include_inter,
        crossings_per_pair=crossings_per_pair,
        m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
    )

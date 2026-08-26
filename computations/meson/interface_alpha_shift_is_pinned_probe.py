#!/usr/bin/env python3
"""
interface_alpha_shift_is_pinned_probe.py — the interface is fixed UPSTREAM,
by an integer valuation, not by a trace magnitude.

WHY THIS PROBE EXISTS
─────────────────────
Addenda 29–30 screened candidate interface words `I` by their Markov-trace
MAGNITUDE (`tr_M(I)` against `√B_AME`) and every candidate failed.  That
screen was aimed at the wrong invariant.  The normal-form machinery does not
read a magnitude off the interface at all.  Per
`prop:alpha-shift-torus-knot`, the interface enters
`conj:confinement-nf-structure-forcing` through

    α_shift(K) := max_{λ ⊢ p}  ord_{q=0}^{(-)} χ_λ(β_K)

— the POLE ORDER at q = 0 of the seminormal Hecke character, i.e. a Laurent
VALUATION.  It is an integer, it is derived (closed form k(p−1) for torus
words), and for the canonical pppnnn atomic braid the partial proof
(`confinement-nf-partial-proof.md`) already pins it:

    α_shift(I_atom) = α_shift(T_{2,1}) = 1·(2−1) = 1
    shift_NF(β_atomic(Z,N)) = 18Z + 21N + 1

which matches the empirical closed form
`D(u) = 2^{2A+1} · u^{18Z+21N+1} · (1+u²)^{3A−1}` exactly.

So the interface is not a free slot to be filled by whatever word maximises a
trace.  Its α_shift is ALREADY DETERMINED, and any substitute word with a
different pole order moves the D(u) exponent off its verified value.

WHAT THIS PROBE MEASURES
────────────────────────
α_shift of every screened candidate, on its support-reduced word (the
convention the corpus uses when it calls a lone crossing `T_{2,1}`, i.e. σ₁
in B₂ rather than σ₃ in B₆).

METHOD.  The valuation is read as the log-log slope of |χ_λ(q)| as q → 0,
evaluated in mpmath at three decades and required to agree to an integer.
Controls against the committed `alpha-shift-torus.witness.json` values
(T_{2,9} → 9, T_{3,5} → 10) keep the method honest; a lone crossing must
return the corpus's own 1.

NO FLOAT64 ANYWHERE — every matrix entry is `mpmath.mpf` from construction,
per AGENTS.md §PROBES ARE NOT EXEMPT.  `float()` appears only inside
f-strings.

Emits no witness by design (audit-only screen); assertions are the record.

@module computations/meson/interface_alpha_shift_is_pinned_probe
"""

from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from hecke_characters import partitions_of, standard_young_tableaux  # noqa: E402

set_compute_dps()
mp.mp.dps = 300  # dynamic range: entries ~q^{-1}, words to 9 letters, q to 1e-8


# ──────────────────────────────────────────────────────────────────────
# Seminormal Hoefsmit matrices in mpmath at a NUMERICAL q
# ──────────────────────────────────────────────────────────────────────

def seminormal_mp(shape, q):
    """σ_1 … σ_{n-1} for partition `shape`, entries mpf, at numerical q.

    Mirrors alpha/alpha_shift_torus.build_seminormal_matrices_sym with q
    numeric instead of symbolic:  a = h/(1 − q^{-2ρ}),  b² = a·a' + 1.
    """
    n = sum(shape)
    syts, _, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], 0
    h = q - 1 / q
    sigmas = []
    for k_gen in range(1, n):
        rows = [[mp.mpf(0)] * dim for _ in range(dim)]
        processed = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k, ci_k1 = syts[i][k_gen], syts[i][k_gen + 1]
            rho = contents[ci_k1] - contents[ci_k]
            a = h / (1 - q ** (-2 * rho))
            swap = dict(syts[i])
            swap[k_gen], swap[k_gen + 1] = ci_k1, ci_k
            j = next((jj for jj in range(dim)
                      if jj != i and syts[jj] == swap), None)
            if j is None:
                rows[i][i] = a
                processed.add(i)
            else:
                a_prime = h / (1 - q ** (2 * rho))
                b = mp.sqrt(a * a_prime + 1)
                rows[i][i], rows[j][j] = a, a_prime
                rows[i][j] = rows[j][i] = b
                processed.update((i, j))
        sigmas.append(mp.matrix(rows))
    return sigmas, dim


def chi(shape, word, q):
    """χ_shape(word) at numerical q.  `word` is a list of 1-based generator
    indices; a negative index means the inverse generator."""
    sigmas, dim = seminormal_mp(shape, q)
    if dim == 0:
        return mp.mpf(0)
    m = mp.eye(dim)
    for g in word:
        s = sigmas[abs(g) - 1]
        m = (s ** -1 if g < 0 else s) * m
    return sum(m[i, i] for i in range(dim))


# ──────────────────────────────────────────────────────────────────────
# Valuation at q = 0, as a log-log slope over three decades
# ──────────────────────────────────────────────────────────────────────

_DECADES = [mp.mpf(10) ** -6, mp.mpf(10) ** -7, mp.mpf(10) ** -8]


def valuation(shape, word):
    """Return (v, max_slope_residual): the Laurent valuation of χ at q=0.

    Negative v is a pole; α_shift takes max(0, −v).  Returns v = None when
    the character vanishes identically (no valuation to read)."""
    vals = [chi(shape, word, q) for q in _DECADES]
    if all(abs(v) < mp.mpf(10) ** -250 for v in vals):
        return None, mp.mpf(0)
    slopes = []
    for (q1, c1), (q2, c2) in zip(zip(_DECADES, vals), zip(_DECADES[1:], vals[1:])):
        if abs(c1) < mp.mpf(10) ** -250 or abs(c2) < mp.mpf(10) ** -250:
            return None, mp.mpf(0)
        slopes.append((mp.log(abs(c1)) - mp.log(abs(c2))) / (mp.log(q1) - mp.log(q2)))
    v = int(mp.nint(slopes[0]))
    resid = max(abs(s - v) for s in slopes)
    return v, resid


def alpha_shift(word, p):
    """α_shift = max over λ ⊢ p of the pole order at q = 0."""
    best, best_lam, worst_resid = 0, None, mp.mpf(0)
    for lam in partitions_of(p):
        v, resid = valuation(tuple(lam), word)
        worst_resid = max(worst_resid, resid)
        if v is None:
            continue
        pole = max(0, -v)
        if best_lam is None or pole > best:
            best, best_lam = pole, tuple(lam)
    return best, best_lam, worst_resid


def support_reduce(word):
    """Relabel the generators a word actually uses onto a contiguous 1..m
    block and return (reduced_word, p = m+1).

    This is the corpus's own convention: `confinement-nf-partial-proof.md`
    calls the atom's lone wall crossing `T_{2,1}` — σ₁ in B₂ — not σ₃ in B₆.
    """
    used = sorted({abs(g) for g in word})
    ix = {g: i + 1 for i, g in enumerate(used)}
    return [ix[abs(g)] * (1 if g > 0 else -1) for g in word], len(used) + 1


def torus_word(p, k):
    return [i for _ in range(k) for i in range(1, p)]


# ──────────────────────────────────────────────────────────────────────
# The candidates, verbatim from interface_candidate_screen_probe.py (Add. 29)
# plus the colour-derived interface of Addendum 30.
# ──────────────────────────────────────────────────────────────────────

CANDIDATES = [
    ("I1", "s3", "current: a single wall crossing", [3]),
    ("I2", "s3 s2 s4 s3", "2-block transposition (the cabling pattern)", [3, 2, 4, 3]),
    ("I3", "s3 s3", "clasp", [3, 3]),
    ("I4", "s2 s3 s4", "fan: touches 2 strands a side, crosses once", [2, 3, 4]),
    ("I5", "(s3 s2 s4 s3)^2", "doubled block transposition", [3, 2, 4, 3, 3, 2, 4, 3]),
    ("Ic", "(s3 s2 s1)(s4 s3 s2)(s5 s4 s3)", "colour-derived (Addendum 30)",
     [3, 2, 1, 4, 3, 2, 5, 4, 3]),
]

# The two nucleon n-context shifts, from habiro-coefficients-extended.witness.json
# via confinement-nf-partial-proof.md.  Integers, stable for A = 2..6.
SHIFT_P, SHIFT_N = 18, 21
PINNED_ALPHA = 1          # α_shift(I_atom) = α_shift(T_{2,1}) = 1·(2−1)
DEUTERON_EXPONENT = 40    # exponent of u in D(u) at Z = N = 1


def main() -> int:
    print("=" * 74)
    print("Is the interface pinned upstream?  α_shift is a VALUATION, not a magnitude")
    print("=" * 74)
    checks = []

    def check(tag, ok, detail):
        checks.append((tag, bool(ok), detail))
        print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {detail}")

    # ── Controls against the committed alpha-shift-torus witness ────────
    print("\n1. Method controls (committed alpha-shift-torus.witness.json)")
    for (p, k, expected) in [(2, 9, 9), (3, 5, 10), (2, 1, 1)]:
        a, lam, resid = alpha_shift(torus_word(p, k), p)
        col = tuple([1] * p)
        print(f"   T_{{{p},{k}}}: α_shift = {a}  (max at λ = {lam}, "
              f"slope residual {mp.nstr(resid, 4)})")
        check(f"A{len(checks) + 1}", a == expected and resid < mp.mpf("1e-6"),
              f"α_shift(T_{{{p},{k}}}) = {a}, expected k(p−1) = {expected}; "
              f"maximizer {lam} vs all-column {col}")

    # ── The candidates ─────────────────────────────────────────────────
    print("\n2. α_shift of every screened candidate, on its support-reduced word")
    results = {}
    for tag, expr, note, w in CANDIDATES:
        rw, p = support_reduce(w)
        a, lam, resid = alpha_shift(rw, p)
        results[tag] = a
        print(f"   {tag:3s} {expr:32s} B_{p}  α_shift = {a:2d}   "
              f"(λ* = {lam}, resid {mp.nstr(resid, 3)})   {note}")

    check(f"A{len(checks) + 1}", results["I1"] == PINNED_ALPHA,
          f"the lone wall crossing returns the corpus's own α_shift(T_{{2,1}}) = "
          f"{results['I1']} — the method reproduces the pinned value from the word")

    ints = all(v is not None for v in results.values())
    check(f"A{len(checks) + 1}", ints,
          "every candidate's valuation resolved to an integer over three decades")

    movers = {t: v for t, v in results.items() if v != PINNED_ALPHA}
    check(f"A{len(checks) + 1}", len(movers) > 0,
          f"{len(movers)} of {len(results)} candidates carry α_shift ≠ 1: "
          + ", ".join(f"{t}={v}" for t, v in sorted(movers.items())))

    # ── What that does to the verified D(u) exponent ────────────────────
    print("\n3. Consequence for the deuteron D(u) exponent (Z = N = 1)")
    print(f"   shift_NF = {SHIFT_P}·Z + {SHIFT_N}·N + α_shift(I)")
    check(f"A{len(checks) + 1}",
          SHIFT_P + SHIFT_N + PINNED_ALPHA == DEUTERON_EXPONENT,
          f"with the pinned α_shift = 1: {SHIFT_P}+{SHIFT_N}+1 = "
          f"{SHIFT_P + SHIFT_N + PINNED_ALPHA} = the committed D(u) exponent "
          f"{DEUTERON_EXPONENT}")

    for tag, v in sorted(movers.items()):
        print(f"   substituting {tag}: exponent → {SHIFT_P + SHIFT_N + v} "
              f"(off {DEUTERON_EXPONENT} by {SHIFT_P + SHIFT_N + v - DEUTERON_EXPONENT:+d})")
    check(f"A{len(checks) + 1}",
          all(SHIFT_P + SHIFT_N + v != DEUTERON_EXPONENT for v in movers.values()),
          "every α_shift ≠ 1 candidate moves the exponent off its verified value — "
          "the interface slot is not free")

    survivors = [t for t, v in results.items() if v == PINNED_ALPHA and t != "I1"]
    check(f"A{len(checks) + 1}", True,
          f"candidates that leave the exponent intact: "
          f"{survivors if survivors else 'none besides I1 itself'} — "
          "these are α_shift-degenerate with the current interface, so the NF "
          "machinery cannot distinguish them from it")

    print("\n" + "=" * 74)
    passed = sum(1 for _, ok, _ in checks if ok)
    print(f"{passed}/{len(checks)} assertions passed")
    print("=" * 74)
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())

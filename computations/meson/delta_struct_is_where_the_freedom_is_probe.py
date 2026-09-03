#!/usr/bin/env python3
"""
delta_struct_is_where_the_freedom_is_probe.py — does the missing binding
magnitude live in Δ(β₁, β₂; A), the nucleon words carrying the 18 and 21?

THE QUESTION.  `conj:confinement-nf-structure-forcing` decomposes

    shift_NF(β) = α_shift(I) + Δ(β₁, β₂; A),   |Δ| ≤ duality_gap(β) = 0,

and Addendum 31 closed the α_shift(I) term: on POSITIVE words the all-column
channel gives one unit of pole order per letter, so the interface is pinned to
exactly one crossing.  Addendum 31 explicitly did NOT cover words with inverse
generators.  The nucleon words are exactly that case, so this probe asks
whether Δ is pinned the same way or carries real freedom.

THE MECHANISM, AND WHY THE ANSWER CAN DIFFER.  On V_(1^p) each generator acts
by the scalar −q⁻¹ (valuation −1).  Its inverse therefore acts by −q
(valuation +1).  So on a MIXED word the column valuation is not the length but
the WRITHE, p − m: inverse letters CANCEL pole order rather than adding it.
Two consequences the probe measures:

  1. the column channel can stop being the maximizer, and
  2. when it does, α_shift is no longer any word statistic — which is where
     structure beyond word length, and hence a magnitude, could live.

The averaged letters are a third case.  `atom_braid_word_3A`'s own docstring
records that its letters are HECKE ELEMENTS `c·σ_g + d·1`, not braid
generators, and that `2A + 1` of them are weight-½ averages `(σ + σ⁻¹)/2`.
On the column channel such a letter is `−(q + q⁻¹)/2`, of valuation −1 —
the same as a bare σ, since the q⁻¹ term leads.

A LAYER ERROR THIS PROBE MADE FIRST, recorded because the failing assertion is
what caught it.  The first version built the word ONCE via
`atom_braid_word_3A(1, 1)` — which bakes in the canonical `q₀` — and then
varied `q` inside the representation.  That freezes every letter's offset `d`
at a CONSTANT while the character is evaluated at `q → 0`, so every letter's
leading term is the representation's own `−q⁻¹` no matter what the letter was
meant to be, and the column pole order comes out as the LENGTH (23) for any
word whatsoever.  It is the straddle AGENTS.md names: an input from one layer
against an input from another inside one computed number.

The fix is the `q=` keyword the producer already provides — it materialises
every crossing template `{0, −h, −h/2, −h(½−δ/4)}` at the given `q`, with
`h = q − q⁻¹` and `δ = flavor_split_leading(q)`.  The word is therefore
REBUILT at each of the three evaluation points, and the valuation is of a genuine
q-family rather than of a q₀ snapshot.

NO FLOAT64: every matrix entry is `mpmath.mpf` from construction; `float()`
appears only inside f-strings.  Audit-only, emits no witness.

@module computations/meson/delta_struct_is_where_the_freedom_is_probe
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
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from pyhecke.gram import h as _h_f  # noqa: E402
from q_parameter import HA_MP  # noqa: E402 — exact mpf, not the f64 twin

set_compute_dps()
mp.mp.dps = 300

# Recorded in confinement-nf-partial-proof.md from
# habiro-coefficients-extended.witness.json; stable for A = 2..6.
SHIFT_P, SHIFT_N, ALPHA_I = 18, 21, 1
DEUTERON_EXPONENT = SHIFT_P + SHIFT_N + ALPHA_I     # 40


def seminormal_mp(shape, q):
    """σ_1 … σ_{n−1} for `shape`, entries mpf, at numerical q."""
    n = sum(shape)
    syts, _, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], 0
    hq = q - 1 / q
    sigmas = []
    for k_gen in range(1, n):
        rows = [[mp.mpf(0)] * dim for _ in range(dim)]
        seen = set()
        for i in range(dim):
            if i in seen:
                continue
            ci_k, ci_k1 = syts[i][k_gen], syts[i][k_gen + 1]
            rho = contents[ci_k1] - contents[ci_k]
            a = hq / (1 - q ** (-2 * rho))
            swap = dict(syts[i])
            swap[k_gen], swap[k_gen + 1] = ci_k1, ci_k
            j = next((jj for jj in range(dim) if jj != i and syts[jj] == swap), None)
            if j is None:
                rows[i][i] = a
                seen.add(i)
            else:
                a_p = hq / (1 - q ** (2 * rho))
                b = mp.sqrt(a * a_p + 1)
                rows[i][i], rows[j][j] = a, a_p
                rows[i][j] = rows[j][i] = b
                seen.update((i, j))
        sigmas.append(mp.matrix(rows))
    return sigmas, dim


def chi_hecke(shape, letters, q):
    """χ_shape of a product of HECKE ELEMENTS.

    `letters` is a list of `(c, d, g)` triples denoting `c·σ_g + d·1` with `g`
    zero-based — the shape `atom_braid_word_3A` returns."""
    sigmas, dim = seminormal_mp(shape, q)
    if dim == 0:
        return mp.mpf(0)
    m = mp.eye(dim)
    for (c, d, g) in letters:
        cc, dd = mp.mpf(str(c)), mp.mpf(str(d))
        m = (cc * sigmas[g] + dd * mp.eye(dim)) * m
    return sum(m[i, i] for i in range(dim))


# Evaluation points for the q → 0 slope.  Powers of 1/3, not of 1/10, and the
# reason is a guard rather than taste: `pyhecke.atom.reject_float64_q` refuses
# any q that round-trips exactly through float64 — "deliberately simple sweep
# values (q = 1.1 and the like)" — because in this pipeline such a value is
# usually the `mpf(str(q_parameter.Q))` idiom smuggling 17 digits into a 50-dps
# path.  A power of 1/10 is exactly that shape and is refused.  Powers of 1/3
# are genuinely 300-dps values, so the word is materialised at full precision
# and no `allow_float64` override is needed.  Any three points work for a slope;
# decades were never load-bearing.
_DECADES = [mp.mpf(3) ** -13, mp.mpf(3) ** -15, mp.mpf(3) ** -17]
_ZERO = mp.mpf(10) ** -250


def word_at(q, conv="bring_color_weighted"):
    """The deuteron word MATERIALISED at `q` — offsets rebuilt, not frozen at q₀."""
    return atom_braid_word_3A(1, 1, q=q, pn_convention=conv)


def column_valuation_by_letter(q, conv):
    """Per-letter valuation on the all-column channel, where σ ↦ −q⁻¹.

    Each letter `c·σ_g + d·1` acts by the SCALAR `c·(−q⁻¹) + d`, so its
    valuation is read directly off that number — no matrices needed.  Returns
    (total_pole_order, [(index, gen, valuation) for letters that are neither
    −1 nor +1])."""
    scal = -1 / q
    total, odd = 0, []
    for k, (c, d, g) in enumerate(word_at(q, conv)):
        v = int(mp.nint(mp.log(abs(mp.mpf(c) * scal + mp.mpf(d))) / mp.log(q)))
        total += v
        if v not in (-1, 1):
            odd.append((k, g, v))
    return -total, odd


def valuation(shape, words_by_q):
    """Laurent valuation of χ at q = 0, as a log-log slope over three q → 0 evaluation points.

    `words_by_q` maps each evaluation q to the word rebuilt AT that q."""
    vals = [chi_hecke(shape, words_by_q[q], q) for q in _DECADES]
    if any(abs(v) < _ZERO for v in vals):
        return None, mp.mpf(0)
    slopes = [(mp.log(abs(c1)) - mp.log(abs(c2))) / (mp.log(q1) - mp.log(q2))
              for (q1, c1), (q2, c2) in zip(zip(_DECADES, vals), zip(_DECADES[1:], vals[1:]))]
    v = int(mp.nint(slopes[0]))
    return v, max(abs(s - v) for s in slopes)


def alpha_shift(words_by_q, n):
    """α_shift = max over λ ⊢ n of the pole order at q = 0, with the argmax."""
    best, best_lam, resid = -1, None, mp.mpf(0)
    per = {}
    for lam in partitions_of(n):
        v, r = valuation(tuple(lam), words_by_q)
        resid = max(resid, r)
        pole = None if v is None else max(0, -v)
        per[tuple(lam)] = pole
        if pole is not None and pole > best:
            best, best_lam = pole, tuple(lam)
    return best, best_lam, resid, per


def classify(letters, hq):
    """Split letters into σ / σ⁻¹ / averaged, per the module's own convention
    (`d == 0` is σ, `d == −h` is σ⁻¹, anything else is not a braid generator)."""
    pos = neg = avg = 0
    for (_c, d, _g) in letters:
        t = -mp.mpf(str(d)) / hq
        if abs(t) < mp.mpf("1e-9"):
            pos += 1
        elif abs(t - 1) < mp.mpf("1e-9"):
            neg += 1
        else:
            avg += 1
    return pos, neg, avg


def main() -> int:
    print("=" * 76)
    print("Does the missing magnitude live in Δ(β₁,β₂;A) — the nucleon words?")
    print("=" * 76)
    checks = []

    def check(ok, detail):
        checks.append((bool(ok), detail))
        print(f"  [{'PASS' if ok else 'FAIL'}] A{len(checks)}: {detail}")

    hq = HA_MP
    word = atom_braid_word_3A(1, 1)          # at q₀ — the physical word, for counting
    words_by_q = {q: word_at(q) for q in _DECADES}   # the q-family, for the valuation
    n = 6
    check_lengths = {len(w) for w in words_by_q.values()} | {len(word)}
    pos, neg, avg = classify(word, hq)
    print(f"\n1. The deuteron word: {len(word)} letters — "
          f"{pos} σ, {neg} σ⁻¹, {avg} averaged")

    check(len(check_lengths) == 1,
          f"the word has the same {len(word)} letters at q₀ and at all three "
          f"evaluation decades — only the offsets move, so the letter counts below "
          f"describe the same object the valuation is taken of")
    check(neg > 0,
          f"the nucleon words are NOT positive: {neg} inverse letters. Addendum 31's "
          f"exclusion covered positive words only, so it does not reach Δ")
    check(avg == 2 * 2 + 1,
          f"averaged (non-braid) letters = {avg} = 2A+1 at A=2, matching "
          f"atom_braid_word_3A's own docstring")

    writhe = pos + avg - neg
    print(f"\n2. Column-channel valuation.  σ ↦ −q⁻¹ (val −1), σ⁻¹ ↦ −q (val +1).")
    print(f"   Naive prediction — the WRITHE, not the length:")
    print(f"      {pos} + {avg} − {neg} = {writhe}   (length would be {len(word)})")

    col = tuple([1] * n)
    v_col, r_col = valuation(col, words_by_q)
    pole_col = None if v_col is None else max(0, -v_col)
    print(f"   measured on λ = {col}: pole order {pole_col} "
          f"(slope residual {mp.nstr(r_col, 3)})")

    check(pole_col != len(word),
          f"the column pole order {pole_col} is NOT the length ({len(word)}): the "
          f"Addendum-31 identity α_shift = letter count fails once the word is mixed")

    # 🛑 The writhe prediction FAILED, and running it down found the carrier.
    q_probe = _DECADES[1]
    pole_w, odd_w = column_valuation_by_letter(q_probe, "bring_color_weighted")
    pole_b, odd_b = column_valuation_by_letter(q_probe, "strict_averaged")
    print(f"\n2b. 🛑 That prediction is WRONG for the canonical convention, and the")
    print(f"    gap has a single carrier.  Per-letter column valuations:")
    print(f"      strict_averaged      (colour-BLIND)  pole {pole_b:3d}   anomalous {odd_b}")
    print(f"      bring_color_weighted (canonical)     pole {pole_w:3d}   anomalous {odd_w}")

    check(pole_b == writhe,
          f"colour-BLIND, the writhe prediction is exactly right: pole {pole_b} = "
          f"{pos}+{avg}−{neg}. So the naive argument was sound; it was the "
          f"convention that was wrong")
    check(pole_w != writhe and len(odd_w) == 1,
          f"canonical colour-weighted, it is {pole_w}, and the entire {pole_w - writhe}-unit "
          f"excess sits in ONE letter: index {odd_w[0][0]}, generator {odd_w[0][1]}, "
          f"valuation {odd_w[0][2]} where every other letter is ±1")
    check(len(odd_b) == 0,
          f"and that letter is anomalous ONLY under colour weighting — colour-blind has "
          f"no anomalous letter at all. The carrier is the p–n interface's colour weight "
          f"δ = flavor_split_leading(q), which is q-DEPENDENT where every other "
          f"coefficient is a constant or a multiple of h")

    print("\n3. Is the column still the maximizer over all λ ⊢ 6?")
    best, lam_star, resid, per = alpha_shift(words_by_q, n)
    print(f"   α_shift(deuteron word) = {best} at λ* = {lam_star}   "
          f"(worst slope residual {mp.nstr(resid, 3)})")
    for lam in sorted(per, key=lambda L: (-(per[L] if per[L] is not None else -1), L)):
        mark = " ←" if lam == lam_star else ""
        print(f"      λ = {str(lam):18s} pole {per[lam]}{mark}")

    moved = lam_star != col
    check(True,
          f"the maximizer is {lam_star}" +
          (f" — NOT the all-column {col}, so α_shift is not any word statistic here"
           if moved else
           f" — still the all-column channel, so α_shift = writhe = {writhe}"))

    print("\n4. Against the recorded decomposition")
    print(f"   confinement-nf-partial-proof.md: shift_NF = {SHIFT_P}Z + {SHIFT_N}N + "
          f"{ALPHA_I} = {DEUTERON_EXPONENT} at Z=N=1")
    print(f"   measured q-pole order of the same word: {best}")
    check(best != DEUTERON_EXPONENT,
          f"the measured q-pole order {best} is NOT the recorded exponent "
          f"{DEUTERON_EXPONENT} — these are exponents in DIFFERENT variables "
          f"(q here, u = b·ℏ_q² in D(u)); do not equate them")

    check(moved,
          "VERDICT: Δ carries structure beyond any word count. The maximizer moved off "
          f"the column channel (to {lam_star}, pole {best}, against the column's "
          f"{pole_col}), so no length- or writhe-identity pins it the way "
          "colPole_faithful pins the interface. The freedom the interface does not "
          "have, Δ has")

    # Which of the max-pole channels survive the convention-D row cap?
    live = [L for L in per if per[L] == best and len(L) <= 2]
    check(len(live) > 0,
          f"and it is not confined to the Temperley–Lieb kernel: {len(live)} of the "
          f"max-pole channels have ℓ(λ) ≤ 2 ({live}), so they carry nonzero y_λ under "
          f"convention D — live blocks, not radical")

    print("\n" + "=" * 76)
    passed = sum(1 for ok, _ in checks if ok)
    print(f"{passed}/{len(checks)} assertions passed")
    print("=" * 76)
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""classical_floor_is_markov_cycle_count_probe.py — the ℏ_q⁰ floor in closed form. (qou-zrx2)

WHAT `qou-zrx2` ESTABLISHED, and what it left open. That bean measured that the signed trace
difference `tr_M(W_free) − tr_M(W_atom)` does **not** vanish at `q = 1`: it has a classical floor of
**1/8** for the deuteron and **7/128** for ⁴He, extrapolated to 1.3e-10 and 3.0e-10 — "simple dyadic
rationals, which is not what a numerical artefact looks like". Its reading was qualitative:

> *"It returns a topological remainder: the free word and the atom word close to different links
> whatever `q` is."*

Right, and not yet a number. This probe gives the floor in closed form.

THE CLAIM. Let `cyc(w)` be the number of cycles of the permutation `w ∈ S_n` (fixed points counted).
Then

    floor  =  z₁^(n − cyc W_free)  −  z₁^(n − cyc W_atom),        z₁ := z(q=1) = 1/2

with **no free parameter**. Under convention D the Markov parameter is `z = q³/(q²+1)`, so
`z(1) = 1/2` exactly.

WHY THE WORDS BECOME PERMUTATIONS AT q=1, which is what makes this computable. `atom_braid_word_3A`
returns Hecke letters `c·σ_g + d·1` of three classes — `σ` (`d = 0`), `σ⁻¹` (`d = −h`), and the
**averaged** `σ − (h/2)·1` that is outside the image of `ρ : B_n → H_n(q)`. At `q = 1` the deformation
parameter `h = q − 1/q` is **0**, so all three collapse to the same transposition `s_g`. Both words
are then plain products of transpositions, and the Ocneanu/Markov trace on `ℂ[S_n]` is
`tr(w) = z^(n − cyc w)` — fixed by `tr(1) = 1` and `tr(x·σ_n) = z·tr(x)`.

So the floor is not a remainder needing interpretation. It is the classical Markov trace of two
permutations that differ in cycle count, and the difference of cycle counts is the whole content.

IT IS A DERIVATION, NOT A TWO-POINT MATCH. An earlier draft of this probe rested on the two measured
floors agreeing with the formula; two points fixing a zero-parameter form is suggestive and nothing
more, and this session has had three such patterns refuted by their next data point. The formula
follows instead from three steps, of which only the third needs checking:

  1. Convention D gives `y_λ = [n−2k+1]_q / [2]_q^n`, zero off ≤2 rows. At `q = 1` that is
     `(n−2k+1)/2^n`, and `n − 2k + 1` is exactly `dim V_λ`, the `sl₂` irrep dimension of `(n−k, k)`.
  2. Hence `tr_M(w)|_1 = Σ_λ y_λ χ^λ(w) = (1/2^n) · Σ_λ dim(V_λ) · χ^λ(w)`.
  3. `Σ_λ dim(V_λ) · χ^λ(w)` is the trace of `w` **place-permuting** `(ℂ²)^⊗n` — Schur-Weyl — and
     equals `2^cyc(w)`. **This is the step the probe verifies**, exactly, in integers, by counting
     the basis states `w` fixes: 6/6 across D, T and ⁴He, free and atom words.
  4. Therefore `tr_M(w)|_1 = 2^(cyc w − n) = z₁^(n − cyc w)`, and the floor is the difference.

So the two agreements below are a **consequence check**, not the evidence.

VERIFIED, 2 for 2, on values this probe did not fit to:

    atom    n    cyc W_free   cyc W_atom   predicted        bean's measured
    D       6        4            3        z²−z³ = 1/8      1/8
    ⁴He    12        8            5        z⁴−z⁷ = 7/128    7/128

The cycle counts are computed from the words; the floors come from `qou-zrx2`'s independent ℏ_q
sweep. Nothing is tuned — `z₁ = 1/2` is forced by convention D and the exponents by the words.

WHAT THIS DOES AND DOES NOT SETTLE. It settles **what the floor is**: exact, parameter-free, and
predictable for any `(Z, N)` — the table below emits predictions for isotopes the bean never
measured, which is how this claim can be falsified.

It does **not** resolve what `qou-zrx2` is actually about. That bean's subject is the **ℏ_q index**
and the `E_0` convention collision it drives (two live producers disagreeing by exactly 5.35× on the
identical deuteron trace difference). Explaining the floor does not choose a convention, and this
probe deliberately makes no claim there. If anything it sharpens the bean's own point: a floor with
a clean closed form is *more* clearly a genuine ℏ_q⁰ term and *less* dismissible as noise, so
"the observable's two parts sit at different orders, and no single scale can pair with it" stands
undisturbed.

SCOPE — (a) scope-limited. Exact rational arithmetic (`Fraction`), no floating point anywhere, no
witness, nothing wired. The `q=1` degeneration is standard Hecke theory, not a new result; what is
new here is only its application to these two words.
"""
from __future__ import annotations

import itertools
import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(_HERE))

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402


def tensor_trace(p):
    """Trace of the permutation `p` place-permuting `(ℂ²)^⊗n`, by exact enumeration.

    A basis state is a map `{0..n−1} → {0,1}`; `w` sends `s ↦ s∘w⁻¹`, so a diagonal entry is 1
    exactly when the state is constant on every cycle of `w`. The trace therefore COUNTS fixed
    states, and is an integer — no arithmetic to get wrong.

    This is the one step of the derivation that is checked rather than quoted. Cost is `2^n`, so it
    is run only on the small atoms; that is enough, because it is verifying a standard identity, not
    establishing a trend.
    """
    n = len(p)
    tr = 0
    for bits in itertools.product((0, 1), repeat=n):
        if all(bits[i] == bits[p[i]] for i in range(n)):
            tr += 1
    return tr


def perm_of(word, n):
    """The permutation a word becomes at q=1.

    Every letter class collapses to `s_g` there (h = 0), so this ignores `c` and `d` BY DERIVATION,
    not by the truncation that `[int(t[2]) for t in ...]` performs elsewhere in the corpus — that
    idiom is wrong at general `q` (it drops σ⁻¹ and the averaged letters) and is right only here.
    """
    p = list(range(n))
    for _c, _d, g in word:
        g = int(g)
        p[g], p[g + 1] = p[g + 1], p[g]
    return p


def cycles(p):
    """Number of cycles of a permutation, fixed points included."""
    n = len(p)
    seen = [False] * n
    c = 0
    for i in range(n):
        if not seen[i]:
            c += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return c


def floor_of(Z, N, z1=Fraction(1, 2)):
    A = Z + N
    n = 3 * A
    wf = [(t[0], t[1], int(t[2])) for t in atom_braid_word_3A(Z, N, include_inter=False)]
    wa = [(t[0], t[1], int(t[2])) for t in atom_braid_word_3A(Z, N, include_inter=True)]
    cf, ca = cycles(perm_of(wf, n)), cycles(perm_of(wa, n))
    return n, cf, ca, z1 ** (n - cf) - z1 ** (n - ca)


def main():
    z1 = Fraction(1, 2)   # z_D = q³/(q²+1) at q = 1, exact
    print("[floor] The ℏ_q⁰ floor of tr_M(W_free) − tr_M(W_atom), in closed form (qou-zrx2).")
    print(f"[floor] floor = z₁^(n−cyc W_free) − z₁^(n−cyc W_atom),  z₁ = q³/(q²+1)|_(q=1) = {z1}")
    print("[floor] At q=1, h = q−1/q = 0, so σ, σ⁻¹ and the averaged letters all become s_g.\n")

    # THE DERIVATION'S ONE CHECKED STEP. Everything else is quotation:
    #   (1) convention D gives y_λ = [n−2k+1]_q/[2]_q^n, zero off ≤2 rows; at q=1 that is
    #       (n−2k+1)/2^n, and n−2k+1 is exactly dim V_λ for the sl₂ irrep of shape (n−k, k);
    #   (2) so tr_M(w)|_1 = Σ_λ y_λ χ^λ(w) = (1/2^n)·Σ_λ dim(V_λ)·χ^λ(w);
    #   (3) Σ_λ dim(V_λ)·χ^λ(w) is the trace of w place-permuting (ℂ²)^⊗n — Schur-Weyl — and
    #       equals 2^cyc(w).  ← THIS is what is verified below, exactly, in integers.
    #   (4) hence tr_M(w)|_1 = 2^(cyc w − n) = z₁^(n − cyc w).
    # So the floor is DERIVED, not fitted to the two measured values.
    print("  SCHUR-WEYL STEP — trace of w on (ℂ²)^⊗n  ==  2^cyc(w)?  (exact integers)")
    print(f"    {'atom':<6}{'word':<7}{'n':>4}{'cyc':>5}{'2^cyc':>10}{'tensor trace':>15}  verdict")
    sw_ok = True
    for nm, (Zc, Nc) in (("D", (1, 1)), ("T", (1, 2)), ("⁴He", (2, 2))):
        nn = 3 * (Zc + Nc)
        for tag, inter in (("free", False), ("atom", True)):
            w = [(t[0], t[1], int(t[2]))
                 for t in atom_braid_word_3A(Zc, Nc, include_inter=inter)]
            pp = perm_of(w, nn)
            cc = cycles(pp)
            tt = tensor_trace(pp)
            good = (tt == 2 ** cc)
            sw_ok = sw_ok and good
            print(f"    {nm:<6}{tag:<7}{nn:>4}{cc:>5}{2 ** cc:>10}{tt:>15}"
                  f"  {'ok' if good else 'FAIL'}")
    print(f"    ⇒ {'Schur-Weyl step verified 6/6 — the closed form is DERIVED, not fitted.' if sw_ok else 'FAILED — the derivation is broken; do not quote the closed form.'}\n")

    # The two the bean measured, by an independent ℏ_q sweep. Not fitted to.
    known = {(1, 1): ("D", Fraction(1, 8)), (2, 2): ("⁴He", Fraction(7, 128))}
    print("  CHECK against qou-zrx2's measured floors")
    print(f"    {'atom':<7}{'n':>4}{'cyc_free':>10}{'cyc_atom':>10}{'predicted':>14}"
          f"{'measured':>12}  verdict")
    ok = True
    for (Z, N), (name, target) in known.items():
        n, cf, ca, pred = floor_of(Z, N, z1)
        good = (pred == target)
        ok = ok and good
        print(f"    {name:<7}{n:>4}{cf:>10}{ca:>10}{str(pred):>14}{str(target):>12}"
              f"  {'MATCH' if good else 'MISMATCH'}")
    print(f"\n  {'2/2 exact — the floor is the classical Markov trace of two permutations.' if ok else 'MISMATCH: the closed form is wrong; do not quote it.'}")

    # Predictions for isotopes the bean never measured. This is the falsifiable half: any ℏ_q
    # sweep on these must return exactly these rationals, or the closed form is wrong.
    print("\n  PREDICTIONS — falsifiable; an ℏ_q sweep must return these exactly")
    print(f"    {'atom':<7}{'Z':>3}{'N':>3}{'n':>4}{'cyc_free':>10}{'cyc_atom':>10}"
          f"{'predicted floor':>18}{'decimal':>14}")
    for name, Z, N in (("T", 1, 2), ("³He", 2, 1), ("⁶Li", 3, 3), ("⁷Li", 3, 4), ("¹²C", 6, 6)):
        n, cf, ca, pred = floor_of(Z, N, z1)
        print(f"    {name:<7}{Z:>3}{N:>3}{n:>4}{cf:>10}{ca:>10}{str(pred):>18}"
              f"{float(pred):>14.10f}")

    # The predictions are all (2^m − 1)/2^k, which the algebra explains: with cf > ca,
    #   z₁^(n−cf) − z₁^(n−ca) = 2^(ca−n)·(2^(cf−ca) − 1)
    # so the numerator is a MERSENNE number 2^(cf−ca) − 1 and the denominator a power of two.
    print("\n  EQUIVALENT CLOSED FORM (same statement, rearranged):")
    print("    floor = (2^(cyc_free − cyc_atom) − 1) / 2^(n − cyc_atom)")
    print("    — Mersenne numerator, power-of-two denominator. Verified against the table above:")
    for (Z, N), (name, _t) in known.items():
        n, cf, ca, pred = floor_of(Z, N, z1)
        alt = Fraction(2 ** (cf - ca) - 1, 2 ** (n - ca))
        print(f"      {name:<5} (2^{cf - ca}−1)/2^{n - ca} = {alt}"
              f"   {'agrees' if alt == pred else 'DISAGREES'}")

    # MIRROR NUCLEI. T (Z=1,N=2) and ³He (Z=2,N=1) came out with identical floors above. If that
    # holds across mirror pairs, the classical floor is blind to the p/n split at fixed A — a
    # structural statement, and one that a p/n-sensitive floor would refute.
    print("\n  MIRROR PAIRS — is the floor blind to the p/n split at fixed A?")
    print(f"    {'pair':<16}{'A':>3}{'floor (Z,N)':>18}{'floor (N,Z)':>18}  same?")
    allsame = True
    for Z, N in ((1, 2), (2, 3), (3, 4), (1, 3), (2, 5)):
        if Z == N:
            continue
        _n1, _c1, _a1, f1 = floor_of(Z, N, z1)
        _n2, _c2, _a2, f2 = floor_of(N, Z, z1)
        same = (f1 == f2)
        allsame = allsame and same
        print(f"    {f'({Z},{N}) vs ({N},{Z})':<16}{Z + N:>3}{str(f1):>18}{str(f2):>18}"
              f"  {'YES' if same else 'NO'}")
    print(f"    ⇒ {'the classical floor depends only on A, not on the p/n split' if allsame else 'the floor DOES distinguish mirror nuclei — the A-only reading is refuted'}")
    print("      (A statement about the q=1 limit only. The full trace difference at q₀ is not")
    print("       claimed to be mirror-symmetric, and nothing here measures it.)")

    print("\n  A prediction here is only as good as the two matches above — two points fixing a")
    print("  zero-parameter form is suggestive, not established. The way to break it is to run")
    print("  the ℏ_q sweep on one of these rows and get a different rational.")


if __name__ == "__main__":
    main()

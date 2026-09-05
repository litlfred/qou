# `f₁/f₀` is NOT a per-letter functional — the hypothesis is built, tested, and REFUTED

**Attempted** the step named highest-value by the `L1` audit: derive
`f₁/f₀ = (21Z + 16N)/2`. Reached a per-letter reduction, established that
`(Z,N)` data **cannot test it**, built the entry point that can, and the test
**refutes it**. Beans `qou-brng` / `qou-pdg9`.

## 🛑 HEADLINE: the per-letter reduction is false

An earlier revision of this document proposed
`f₁/f₀ = 2n₊ − n₋/2` and called it a reduction of two per-nucleon constants to
two per-letter weights. **That is refuted.** It is a coincidence of the cone the
`(Z,N)` family spans, not a per-letter law.

## Two errors of mine, in order

**Error 1 — I read the census off a comment instead of the word.** The probe's
line 554 says *"proton 6σ+3σ⁻¹ → 21, neutron 5σ+4σ⁻¹ → 16"*, and I took the
census to be two-dimensional. Measured from
`atom_canonical_crossings` directly, the free word for one proton is **11
letters: 6 σ, 3 σ⁻¹, and 2 `averaged`** — a *third* letter type the comment does
not mention. So the system is 2 equations in **three** unknowns:

    6w₊ + 3w₋ + 2w_a = 21
    5w₊ + 4w₋ + 2w_a = 16   ⟹   w₊ = 4 − 2w_a/9,  w₋ = −1 − 2w_a/9

a **one-parameter family**. My reported `(2, −½)` is the `w_a = 0` member. `w_a = 0`
is what the probe's `W_OF` uses — but that is for the `[★]` *permutation*
formula, a different formula from this log-derivative, so importing it here was
unjustified.

**Error 2 — the six-case agreement was never evidence**, which the previous
revision did get right and is worth keeping: every `(Z,N)` has census
`Z·(6,3,2) + N·(5,4,2)`, so all six lie in the cone spanned by the two nucleon
words that fixed the weights. A linear functional agreeing on two generators
agrees on their whole cone identically. **No `(Z,N)` at any A can test it.**

## The entry point, and the test

`tr_M_series(Z, N, …)` builds `crossings` and never uses `Z`, `N` again — the
word is the only channel — so a word-level entry point is a wrapper, not a
rewrite:
[`computations/probes/word_level_trace_entry_point.py`](../../computations/probes/word_level_trace_entry_point.py).
It does not modify the probe (that is `qou-pdg9`'s); it imports its internals.
Its `_selftest` **gates on reproducing the `(Z,N)` route exactly** — 37/2, 21,
16 — and passes, so the tool is validated before it is trusted.

Taking the `pn` free word, census `(n₊, n₋, n_a) = (11, 7, 4)`, `f₁/f₀ = 37/2`,
and deleting one letter of each type — which moves the census **off the cone**:

    word                census       f₁/f₀     Δ        per-letter predicts
    base (pn)           (11, 7, 4)    37/2      —        —
    drop one averaged   (11, 7, 3)    19/2     −9         0
    drop one σ          (10, 7, 4)     9      −19/2      −2
    drop one σ⁻¹        (11, 6, 4)    16       −5/2      +½

**All three predictions fail.** And the failure is not a bad choice of `w_a`:
back-solving the three deltas gives `(w₊, w₋, w_a) = (19/2, 5/2, 9)`, which then
gives `6(19/2) + 3(5/2) + 2(9) = 165/2 ≠ 21`. **No assignment of fixed
per-letter weights reproduces both the nucleon values and the deltas.**

So `f₁/f₀` is a function of the **word**, not of its letter census. The
coefficients `21` and `16` are properties of the two specific nucleon words, and
the linear-in-`(Z,N)` form of `f₁/f₀` follows from the words being concatenated,
not from any per-letter additivity.

## What survives

- **`f₁/f₀ = (21Z + 16N)/2` itself is untouched** — it is the probe's verified
  result over A = 2..20 and nothing here bears on it. Only my proposed
  *explanation* of it is refuted.
- **The `L1` chain is unaffected in truth-value** and still rests on `f₁/f₀` as
  an empirical input. This attempt to remove that dependence failed.
- **The unfalsifiability observation stands** and is now doubly worth recording:
  it is what motivated building the entry point instead of running more `(Z,N)`.

## The convention note, kept because it is still true

The weights invited reading `2 = 1/z(1)`, `−½ = −z(1)` since `z(1) = ½`. That was
never evidence for convention D: `z(1) = ½` in **both** C and D. The derivative
*does* discriminate — `d/dq log z|₁ = 2` for D against `0` for C. With the
per-letter reading refuted, this is now an observation in search of an object
rather than support for a weight.

## Scope

- The refutation is exact-`Fraction` arithmetic on four words at `P = 3`, `n = 6`.
- Deleting a letter changes the word's algebra, not merely its census — which is
  precisely the point: the hypothesis under test was that only the census
  matters.
- **Not a claim that no closed form exists** for `f₁/f₀`; only that a
  fixed-per-letter-weight functional is not it. Scope-(a).

---

# Follow-on: what `f₁/f₀` does NOT track, and one thing it might

With the entry point in hand, the two obvious explanations are cheap to test.
Both fail.

## Not the cycle count either

The natural next candidate, and the one the corpus has traction on: the `[★]`
formula is built on `cycles_of_product`, and `qou-tjys` established
`c_free = 2A`, `c_atom = A + 1` across 228 `(Z,N)` pairs.

Holding the letter **multiset** fixed and permuting the order — so the census is
constant by construction — over nine words of the `pn` free word:

    cycles = 4 for every one          (invariant)
    f₁/f₀  = 37/2, 31/2, 8, 5, 17, 25/2   (six distinct, spanning ~4×)

The cycle count is *invariant* across these words while `f₁/f₀` varies fourfold,
so **`f₁/f₀` is strictly finer than the cycle count.** Together with the census
refutation above, both invariants the corpus already had for this object are now
excluded.

## The canonical ordering is extremal — measured, and stated at its true strength

The canonical word gave the largest value of the nine. That is a 1-in-9 draw and
worth nothing alone, so it was re-run against **40** random same-multiset
shuffles:

    canonical                    f₁/f₀ = 37/2 = 18.5
    40 shuffles                  range  1/2 .. 17
    strictly above canonical     0
    equal                        0
    cycle counts seen            {4}

**What this is worth, precisely.** Under the null "the canonical ordering is a
typical ordering of its own letters", the probability it is the strict maximum of
41 draws is `1/41 ≈ 0.024`. So this is **suggestive at p ≈ 0.024 — not a proof of
maximality**, and it must not be quoted as one. The space is
`22!/(11!·7!·4!) = 232,792,560` orderings; 40 random draws cannot establish a
maximum over that, and no number of random draws would.

It is, though, a **well-posed conjecture** that the tool makes cheap to attack:
*the canonical ordering maximises `f₁/f₀` among orderings of its own letters.*
Attacking it properly means a directed search (hill-climbing from the canonical
word, or exhaustive enumeration on a smaller nucleus), not more random sampling.

## Scope on the follow-on

- **One nucleus** (`pn`, `n = 6`, 22 letters), `P = 3`, exact `Fraction`.
- **40 random shuffles**, one seed. Not a search, not exhaustive.
- The cycle-count refutation is the solid half: it needs only that the count is
  invariant while the value varies, which is directly observed.
- The extremality is the speculative half and is labelled as such.
- Scope-(a) throughout.

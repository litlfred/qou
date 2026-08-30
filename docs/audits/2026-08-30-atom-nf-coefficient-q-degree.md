# The q-degree of the six NF coefficients — measured to A = 30

**Bean `qou-c0yc`. PR [#6308](https://github.com/litlfred/qou/pull/6308).
Producer: [`computations/probes/atom_nf_q_degree_probe.py`](../../computations/probes/atom_nf_q_degree_probe.py).
Witness: `computations/probes/atom-nf-q-degree.witness.json`.**

`hecke_core_symbolic.build_atom_nf_sym(Z, N)` returns the atom braid's normal
form as six coefficients in the NF basis `[γ, σ₀, σ₁, L₊, L₋, e⁻]`, word
lengths `ℓ = 0, 1, 1, 2, 2, 3`. This records what those coefficients actually
are and how their q-degree behaves.

## 1. The ring — the docstring was wrong twice over

It said `ℚ(q, √q)`. Under **convention D** neither half survives.

* **No `√q`.** The half-power branch was a convention-C artefact of `z`, and
  `z` does not enter `hm_sym` in either convention. The module banner twelve
  lines above already records deleting the module-level `sqrt_q` for exactly
  this reason — the *function* docstring was simply not updated with it. That
  is the ordinary way a correction goes stale: it lands where the author was
  looking and not where a reader arrives.
* **Not general rational functions.** `build_atom_nf_sym` only ever calls
  `hm_sym` with `c = 1` and `d ∈ {0, −h, −h/2}`, `h = q − q⁻¹`. So every
  coefficient is a **Laurent polynomial over the dyadic rationals**,
  `ℤ[½][q, q^{±1}]`.

The `½` is not decoration: it compounds through the mixed crossings and
denominators reach `2^32` by A = 8, so `ℤ[q^{±1}]` would be wrong in the
opposite direction. The probe's first version asserted "denominator divides 2"
and **failed itself** on that — `ℤ[½]` is every `a/2^k`, not only halves.

Everything above is visible in a single coefficient, from the unmodified
function at A = 1, Z = 1:

```
nf[1] = (-q^22 + 5q^20 - 15q^18 + 31q^16 - 47q^14 + 59q^12 - 59q^10
         + 47q^8 - 31q^6 + 15q^4 - 5q^2 + 1) / (4 q^11)
```

Exponents −11 … 11 — symmetric, all even, antipalindromic — over a
denominator of 4.

## 2. Structure

| property | result |
|---|---|
| support symmetric, `lo = −hi` | 540/540 components (90 nuclei, A ≤ 12), 0 exceptions |
| one exponent parity per component | 0 exceptions |
| `exponent parity + ℓ(w)` constant per nucleus | 90/90 |
| `cᵢ(1/q) = (−1)^p cᵢ(q)` | 0 exceptions (A ≤ 10) |

The grading has a one-line reason. The `c = 1` entries of `hm_sym` change the
NF word length by one and carry no power of q; the `c·h` and `d` entries keep
the word and carry an odd power. So exponent parity and word-length parity are
locked, and each coefficient is a `±1` eigenvector of the bar involution with
the sign fixed by word length.

## 3. Degree

Quadratic in A, driven by the `A(A−1)/2` inter-nucleon pair steps, with a
constant that depends sharply on isospin.

**All-proton ray (N = 0).** `deg(σ₀) = 12A + A(A−1)/2 − 1`, exact for
A = 1 … 30 — *one less than the number of `hm_sym` calls*. Proton–proton pairs
carry `d = 0`, nothing cancels, and every step contributes a full degree.

**Pure-neutron ray (Z = 0).** `deg(γ) = A(A+1)/2`, the triangular number — on
`7 ≤ A ≤ 26`. It **breaks at A = 27**, and the excess then grows by 2 per unit
A. This is a scoped observation, not a law.

> **Why that scoping is the point.** The first sweep in this session stopped at
> A = 16. On `7 ≤ A ≤ 16` the triangular law is exact, with no hint of a
> boundary — twenty consecutive values agreeing. Reported from that window it
> would have read as a closed form. It is the third instance of the same
> failure mode in one session: a window chosen for compute cost, mistaken for
> the domain of a law. (The other two: an A = 12–16 binding "plateau" that
> resumes climbing at ²⁰Ne, and a per-witness sampling rate dragged down by one
> producer appearing 119 times.) The cheap defence is not a better prior — it
> is extending the sweep until it breaks, and reporting the window when it
> does not.

## 4. The max-plus bound is not tight, and misses by a lot

Taking degrees of the *effective* step matrix — same-target contributions
summed first, so `σ⁻¹`'s vanishing diagonal `c·h + d = 0` is already inside the
model — gives a max-plus recursion for the degree vector.

It is a genuine upper bound: **0 violations in 540 components**. But it is
attained in only **197/540**, on 29 of 90 nuclei. The gap is always even (the
ℤ/2 grading again), is **zero on the proton-rich side**, and reaches **104 in
degree at A = 12** — the largest nucleus in that sweep, where it is still
growing, so 104 is a floor rather than a maximum.

So neutron-rich coefficients cancel at leading order, heavily, in a way no
degree-only model sees. **No mechanism is claimed for this, nor for the A = 27
break.** Both are measured.

## 5. Cost — the symbolic path is unnormalised, not intractable

`build_atom_nf_sym` is exponential: `hm_sym` never canonicalises, so the sympy
tree fans out at each of the `11A + A(A−1)/2 + Z` calls. A = 1 takes 0.13 s;
**A = 2 did not finish in 15 minutes.**

The corpus had already diagnosed this correctly.
[`compound_shift_nf.py`](../../computations/compound_shift_nf.py) names
"expression fan-out … without intermediate canonicalization" and
[`crystal_shift_nf_atomic.py`](../../computations/crystal_shift_nf_atomic.py)
calls the symbolic-q path abandoned; both route around it through crystal pole
counting. Two things follow and only the second is new:

1. wrapping each `hm_sym` result in `sp.expand` is value-preserving (checked
   against the stock function at A = 1) and brings **A = 8 to ~8.5 s**;
2. carrying the coefficients as `dict[int, Fraction]` — exact, no sympy —
   reaches **A = 30 in seconds**.

Whether the crystal route remains preferable for `shift_NF` is a separate
question and is not reopened here. What is no longer true is that the
symbolic-q path cannot be run.

## 6. What this does not touch

* **`shift_NF(β) = 18Z + 21N + 1`** (`prop:per-nucleon-shift-additive-linearity`)
  is a **different quantity** — a `D(u)` exponent shift read off the crystal
  pole order, not an NF-coefficient q-degree. It matches nothing measured here
  (deuteron: 40 against `deg(σ₀) = 23`, support span 46). Recorded so a later
  reader does not attempt to reconcile two unrelated numbers.
* Nothing here is anchor-dependent. `q` is a formal Laurent variable
  throughout; no q₀ is substituted, so neither pin can move any number in the
  witness (`q0Anchor: "independent"`).
* A > 30, and the tropical comparison above A = 12, are not measured.

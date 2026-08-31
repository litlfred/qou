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
degree-only model sees.

### 4a. Where the gap opens — and it is one step kind

Running the build step by step against the max-plus model localises it. The
three inter-nucleon coefficients are, **per the already-published table** in
[`appendix-nf-witnesses/witness-computation-method.md`](../../content/quantum-observable-universe/appendix-nf-witnesses/witness-computation-method.md):

| pair | `d` | factor `σ₀ + d` |
|---|---|---|
| pp | `0` | `σ₀` — positive crossing |
| nn | `−h` | `σ₀ − h = σ₀⁻¹` — negative crossing |
| pn | `−h/2` | `½(σ₀ + σ₀⁻¹)` — averaged; not a braid element |

That reading is **not new here** — the appendix states all three rows,
including the average. This probe re-derived it (and re-verified `σ₀·(σ₀−h) = 1`
in the 6-dimensional NF representation) only to attribute the degree gap. The
attribution *is* new:

| step kind | times run | gap units opened |
|---|---:|---:|
| `gen0 d = −h` — the nn **negative** crossing | 495 | **531** |
| `gen0 d = 0` | 2915 | 135 |
| `gen1 d = −h` | 1760 | 169 |
| `gen0 d = −h/2` — **averaged** | 1155 | **0** |
| `gen1 d = −h/2` — **averaged** | 220 | **0** |

Two things fall out, over all 65 nuclei with A ≤ 10.

* **The averaged pn crossing never opens a gap** — 0 units in 1375
  occurrences. Being the mean of the positive and negative crossings, it is
  degree-benign.
* **The nn negative crossing opens 64 % of the total** from 13 % of the steps.
  The remainder is downstream: once `σ₀⁻¹` has knocked the top term out, later
  generic steps are no longer tight either.

The criterion this suggests is **necessary but not sufficient**, and it is
worth stating the failed version because it is the one that looks right. Every
one of the 26 tight nuclei has `N ≤ 2` — at most one nn pair. But three nuclei
with `N ≤ 2` are *not* tight: `(Z, N) = (0, 2), (1, 2), (2, 2)`. I had written
the criterion as an "iff" and the count caught it: 26 tight against 29 with
`N ≤ 2`.

The step trace says what the extra condition is. A *single* negative crossing's
degree loss is transiently recovered by the steps that **follow** it — at
A = 3 the loss at step 22 is recovered at step 23 — and the three exceptions
are exactly the cases where the nn step sits too near the end of the sequence
for that to happen. So the tightness condition is about the *position* of the
negative crossing, not only the count — and the two populations separate
cleanly rather than marginally:

| | steps remaining after the last nn step |
|---|---|
| not tight — `(0,2)`, `(1,2)`, `(2,2)` | **≤ 3** |
| tight | **≥ 19** |

Nothing falls between 3 and 19. So "the loss is recovered by the steps that
follow it" is a measurement with a 16-step margin, not a story fitted to three
exceptions. Measured, not asserted: the producer records steps-after-last-nn
for the whole `N ≤ 2` set.

**Still not derived:** no *mechanism* for either. But both quantities now
have measured closed forms — see §6.

### 4b. The denominator is the published `2^{p_n}`, from the other side

The same appendix records that the engine tracks a denominator `2^{p_n}`
counting averaged pn crossings. That is stated for the **Rust hecke-engine**;
`hecke_core_symbolic` is an independent Python implementation, and its
denominators match it exactly — the deepest power of two in the coefficients
equals the number of `d = −h/2` steps, on all 65 nuclei with A ≤ 10.

A cross-implementation agreement rather than a new claim, and worth recording
as one: it is the kind of bookkeeping that drifts silently between two engines.

Note also that the engine genuinely carries **half-integer q-exponents**
(`laurent_poly_q.rs` stores `2 × exponent` keys; the certificate is "exact in
`t = q^{1/2}`"), so the appendix's `ℤ[q̌, q̌^{-1}]` is correct for it and is
**not** a convention-C residue — checked, because it looked like one.

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


## 6. Two measured closed forms

Producer: [`computations/probes/atom_nf_degree_laws_probe.py`](../../computations/probes/atom_nf_degree_laws_probe.py).
Witness: `computations/probes/atom-nf-degree-laws.witness.json`.

**The size of the shortfall.** For `Z ≥ 5` and `N ≥ 5`:

    gap(Z, N) = 6N − 19 + [Z > N]

zero exceptions on the tested grid. It does **not** depend on `Z` beyond that
indicator — once a nucleus carries five or more protons, the leading-order loss
is a function of the **neutron count alone**, linear, at **6 degrees per
neutron**.

My first version of this was `6N − 19` flat, and it was **wrong**: for `Z > N`
the value is `6N − 18`. The failure is structured rather than noisy, and it was
found by widening the sweep, not by inspection — the same lesson as §3.

`Z ≤ 4` is a different and larger regime, but the *slope* still converges:
`Z = 2` and `Z = 4` both settle to **+6** per neutron (offsets `6N + 41` from
N = 10, `6N + 7` from N = 9), and `Z = 0` alone settles to **+8** (`8N + 2`
from N = 8). So the pure-neutron chain is an outlier in **slope**, not merely
in offset. Those three offsets are read off the last few increments of a short
sequence and are the weakest claims in the witness.

**The A = 27 break**, extended to A = 40, is one clean two-branch maximum:

    deg(γ)|_{Z=0} = A(A+1)/2 + 2·max(0, A − 26)

Two branches with the **same quadratic leading term** whose linear parts differ
by `2A − 52`, crossing exactly at A = 26. The excess grows by exactly 2 per
unit A past the break with no further transition, and `deg(σ₀) = deg(γ) − 1`
holds **for A = 8…40** — across the break as well as away from it — so it is
not a reordering of which component dominates; both move together.

**A = 7 is the sole exception**, at offset `+7` rather than `−1`. I first
asserted the offset over 7…40 and *the producer failed itself on it*; the
exception is a single value and it is not a stray, because A = 7 is the lower
edge of the triangular window (§3's window is 7…26). The regime simply has not
settled at its own first point.

**Neither law is derived.** No mechanism for the coefficient 6, the constant
−19, the `Z ≥ 5` threshold, or the crossover at 26. They are fits to exact
integer data over a stated range, and the range is stated for the reason §3
gives.

### 6a. One lead, checked and refuted

The obvious first guess for "6 per neutron" is that it counts negative-crossing
(`d = −h`) steps. It does not, and the refutation is one line of arithmetic
against the `Z`-independence:

| | `d = −h` steps | gap |
|---|---:|---:|
| `Z = 5, N = 5` | 50 | 11 |
| `Z = 9, N = 5` | 66 | 12 |

The step count moves by **16** while the gap moves by **1**. The count is
`4Z + 4N + N(N−1)/2` — it grows with `Z` at 4 per proton plus one per electron —
whereas the gap is `Z`-independent for `Z ≥ 5` by construction of the law. So
the two cannot be proportional.

**And the asymmetry that motivated the guess does not exist.** I had said a
neutron block carries four `d = −h` steps against a proton's three. Counted
from the sequence itself, a proton block *plus its electron* also carries
**four** — the electron step supplies the missing one. Both nucleons contribute
4. The 6-per-neutron rate therefore has no candidate mechanism at all yet, which
is a cleaner statement of the open problem than the one it replaces.

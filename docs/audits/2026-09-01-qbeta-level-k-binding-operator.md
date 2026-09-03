# The level-`k` operator is binding — and the trace is blind to 588 of the 720 dimensions it lives in

**Date:** 2026-09-01 · **Beans:** `qou-cds1` (Step 27) / `qou-tower` (the cause) ·
**Scope:** (a).


> ## 🛑 THE HEADLINE READING IS CORRECTED (2026-09-01, bean `qou-i9gk`)
>
> This audit says the `>2`-row blocks carry *"information the observable cannot
> see."* They carry **no states at `N = 2`**.
>
> Measured at `n = 3..8` (`qbeta_blind_sector_is_the_tl_kernel_probe.py`, 4/4):
> `ω_λ = 0 ⟺ ℓ(λ) > 2` exactly, and `∑ d_λ²` over the `≤2`-row blocks is
> `Catalan(n)` at every `n`. So those blocks **are** `TL_n` and the rest span the
> **kernel** of `H_n(q) → TL_n(q)`. Since `TL_n = End_{U_q(sl₂)}(V^{⊗n})`, the
> kernel acts as zero on the `N = 2` physical space: this is the Schur–Weyl row
> cap (`qou-fvzm`), not a second vanishing. §"the finding" below re-measured a
> proved fact and mis-glossed it.
>
> **And the reading contradicts convention D, in which it was measured.**
> `FibreCategoricalTraceForcesJones.lean` (bean `qou-n1dj`) proves the `ℓ > 2`
> channels are absent at `N = 2` and that `y_{(1³)} = 0` forces Jones, with one
> **open premise** between them: that the mass trace *is* the categorical trace of
> the fibre action on `V^{⊗n}`. D is forced **by** the premise that empties the
> blind sector. Under it there are no states there; under its negation D is not
> forced and D's weights are the wrong ones. The headline reduces to `qou-n1dj`.
>
> **The coincidence dies more cleanly than §"the 0.13 % coincidence" says.**
> `N_min(λ) = ℓ(λ)`, so the `0.0252506` phase in `(3,2,1)` needs `N ≥ 3` and the
> `0.0195531` in `(2,2,1,1)` needs `N ≥ 4`. **The sum requires `N ≥ 4`**, which
> nothing in the corpus motivates — a structural kill rather than a
> degeneracy-wall argument.
>
> **What survives.** `qou-fvzm` says the super-pairwise binding term *requires*
> `N ≥ 3`, and `(3,2,1)` — carrying both the largest binding character
> (`−9.598`) and the smaller phase — is an `ℓ = 3` block. So this audit measured
> **what an `N = 3` extension would carry**. Weaker and different from what it
> claimed, and the part that stands. The construction (§"the construction"), its
> validation, and the chain-vs-all-pairs finding are untouched.


**Artifacts.**
[`QOU/QBeta/TraceBlindSector.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/TraceBlindSector.lean)
(8 theorems, sorry-free) ·
[`qbeta_level_k_binding_operator_probe.py`](../../computations/qbeta/qbeta_level_k_binding_operator_probe.py)
(8/8). Sequel to
[the discriminant curve](./2026-08-31-qbeta-discriminant-curve-in-q.md).

---

## The correction

Step 25 concluded "the corpus is H₃-valued at every mass number `A`, so the
level-`k` avenue is **not instantiated**", on the evidence that
`build_atom_nf(Z,N)` returns a 6-vector in the H₃ normal-form basis for every
`A`. That reads the evidence backwards, and bean `qou-tower` had already measured
the same fact and named its cause: `build_atom_nf_mp` applies the H₃
Gröbner–Shirshov reduction **after every crossing**, so the `H_{3A}` structure is
destroyed as it is built. A 6-vector at every `A` is not evidence that the atom
*lives* in H₃. It is evidence that H₃ is where the production chain can **observe**
it.

The faithful object was already in the corpus. `atom_braid_word_3A(Z, N,
include_inter=…)` returns the honest `3A`-strand word with no eager reduction,
and its `include_inter` switch is exactly the composite/constituent distinction.

## The construction

Binding is never observed. What is observed is the mass of the free constituents
and the mass of the bound composite; binding is their **difference**. Do the same
subtraction one level up — not to the numbers but to the **operators**:

```
Δ_bind  =  β_atom − β_free                     ∈ H_{3A}(q)
```

`tr_M` is linear, so `tr_M(Δ_bind)` is exactly the binding number the corpus
already computes (`markov_trace_binding`). But `Δ_bind` is an **operator**, and an
operator has a spectrum that no linear functional determines.

For the deuteron (`Z = N = 1`, `3A = 6`) the word factors exactly:

```
β_atom = P · I · N        P = proton,   11 letters on gens {0,1}
β_free = P · N            N = neutron,  11 letters on gens {3,4}
                          I = the one interface letter at gen 2
⟹  Δ_bind = P · (I − 1) · N        exact in all 11 blocks
```

`β_free` uses only gens `{0,1,3,4}` and **is** an element of `H₃ ⊗ H₃`. But
`I − 1 = σ₂ + (d−1)·1` carries `σ₂` with coefficient 1, and `σ₂` is not a word in
those generators. **So `Δ_bind` is genuinely `H₆`-valued, and Step 24's
block-diagonality / branching argument — the thing that let Steps 24–26 dismiss
the tower — does not reach it.** It is the level-`k` operator the arc has been
missing.

Validated against the corpus's own `chi_lambda_of_word` to `5.4·10⁻¹⁵` in all
eleven blocks, which is the float64 floor of that path. The operator is the
corpus's object, not a re-derivation of it.

## The finding: the observable's blind spot is structural

Convention D is the SU(2) / Temperley–Lieb (Jones) trace, `z = q³/(q²+1)`, so it
factors through the TL quotient — whose irreps are the partitions with **at most
two rows**.

| λ ⊢ 6 | rows | dim | `\|ω_λ\|` | `χ_λ(binding)` | seen? |
|---|---|---|---|---|---|
| `(6)` | 1 | 1 | `1.2·10⁻¹` | `+0.00856` | yes |
| `(5,1)` | 2 | 5 | `3.9·10⁻¹` | `−2.7149` | yes |
| `(4,2)` | 2 | 9 | `4.1·10⁻¹` | `−7.3315` | yes |
| `(3,3)` | 2 | 5 | `7.6·10⁻²` | `−0.3766` | yes |
| `(4,1,1)` | 3 | 10 | `5.6·10⁻¹⁷` | `−5.8358` | **no** |
| **`(3,2,1)`** | 3 | 16 | `1.9·10⁻¹⁶` | **`−9.5979`** | **no** |
| `(3,1,1,1)` | 4 | 10 | `8.7·10⁻¹⁷` | `+1.4275` | **no** |
| `(2,2,2)` | 3 | 5 | `5.8·10⁻¹⁷` | `−7.2453` | **no** |
| `(2,2,1,1)` | 4 | 9 | `6.1·10⁻¹⁷` | `−1.6639` | **no** |
| `(2,1⁴)` | 5 | 5 | `1.2·10⁻¹⁷` | `+4.3857` | **no** |
| `(1⁶)` | 6 | 1 | `5.7·10⁻¹⁸` | `−1.3501` | **no** |

Confirmed by arithmetic independent of the numerics: `Σ d² = 720 = 6! = dim H₆`
over all eleven, and `132 = C₆ = dim TL₆` over the four visible ones.

> **588 of 720 dimensions — 81.7 % — are invisible to the observable**, and the
> binding character is **largest in an invisible block**: `χ_{(3,2,1)} = −9.598`,
> against `+0.009` in the one-dimensional visible block.

`blind_sector` in Lean is the formal content: a weighted sum whose weights vanish
on a set is unchanged by altering the summand there. And
`spectrum_not_determined_by_trace` is why it matters — two operators can share
every trace the corpus computes and differ in discriminant, so a blind block's
eigenphases are not merely unmeasured, they are **unconstrained**.

## What is in the blind sector

The first **small** eigenphases found anywhere in this arc, and all of them are in
blocks the trace cannot see:

| λ | dim | visible? | small eigenphase |
|---|---|---|---|
| `(3,2,1)` | 16 | no | **`0.0252506`** |
| `(2,2,1,1)` | 9 | no | **`0.0195531`** |
| `(4,2)` | 9 | yes | — (only `3.1220`, i.e. near `π`) |

Every previous candidate was **above** the required ladder phase `0.0447444`:
Step 25's smallest species-pair eigenphase was `4.41×` too large, Step 26's
cyclotomic minimum `24.8×`. These are the first below it.

## The 0.13 % coincidence, and why it is not a result

At `q₀` the two small phases sum to `0.0448038` against the required `0.0447444`.
**Recorded as a target, not a finding.** The falsification test says it is a wall
artefact:

- Both blocks are simultaneously elliptic only on a narrow window,
  `q ∈ (≈1.0925, 1.1121238)`. The `(2,2,1,1)` pair collides on the real axis at
  the upper wall, so `θ₂ → 0` there and the **sum sweeps down through every value
  below it** — a crossing with `θ_req` is guaranteed to exist; only its location
  carries information.
- It is at `q* = 1.109988469`, `9.89·10⁻⁶` above `q₀` — **`1.07·10⁷ σ_q₀`**. Four
  orders of magnitude closer than Step 26's `3·10¹¹`, and still ten million σ.
- `q*` sits `0.19200 %` below the wall; `q₀` sits `0.19289 %`. The agreement is
  that both are hard against the **same degeneracy** — the same structure Step 26
  found for `Δ_L`, not a new phenomenon.
- And "sum of two block eigenphases" has **no derivation** behind it. It was
  chosen because two numbers added up, which is exactly what the corpus's
  anti-fit rule forbids searching on.

## How far this reaches, and where it stops

**The blindness deepens with the nucleus.** The observable sees `Cₙ` of `n!`
dimensions at `n = 3A` strands:

| A | n | `dim Hₙ = n!` | `dim TLₙ = Cₙ` | visible |
|---|---|---|---|---|
| 1 | 3 | 6 | 5 | 83.3 % |
| 2 | 6 | 720 | 132 | 18.3 % |
| 3 | 9 | 362 880 | 4 862 | 1.34 % |
| 4 | 12 | 479 001 600 | 208 012 | 0.043 % |
| 6 | 18 | 6.4·10¹⁵ | 477 638 700 | 7.5·10⁻⁶ % |

`Cₙ/n! ~ 4ⁿ/n!` — super-exponential. The heavier the nucleus, the smaller the
fraction of it any corpus measurement can reach.

**And the corpus's word is a nearest-neighbour chain, not all pairs.**
`atom_braid_word_3A` walks `ordering = ['p']*Z + ['n']*N` and places an interface
at `gen 3k+2` for `k < A−1`:

| A | interfaces (`A−1`) | all pairs `A(A−1)/2` | missing |
|---|---|---|---|
| **2** | 1 | 1 | **0** |
| 3 | 2 | 3 | 1 |
| 4 | 3 | 6 | 3 |
| 8 | 7 | 28 | 21 |
| 12 | 11 | 66 | 55 |

The deficit is `(A−1)(A−2)/2` and it is **zero at A = 2**, so everything above is
exact for the deuteron. From `A = 3` it bites. Permuting the arbitrary ordering
at `A = 3` (He-3: `ppn` / `pnp` / `npp`) moves the binding character across the
visible blocks of `H₉` by **22.54 %** — and an all-pairs coupling would show no
such dependence, by symmetry. So the chain truncation is a **first-order
modelling choice** at `A ≥ 3`, not a small correction, and every heavy-nucleus
number in the corpus inherits it.

**Not proposed here:** an all-pairs word with a distance decay. A decay rate per
bond type is three free parameters with no derivation, and a non-adjacent nucleon
pair has **no single generator to sit on** — `σ_g` couples strands `g` and `g+1`
only — so the coupling is a genuine modelling choice rather than a letter to
insert. Recorded as the next construction, not made here.

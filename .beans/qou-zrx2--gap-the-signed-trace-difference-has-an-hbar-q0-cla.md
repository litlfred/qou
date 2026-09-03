---
# qou-zrx2
title: 'GAP: the signed trace difference has an hbar_q^0 classical floor -- it is not a pure deformation observable'
status: in-progress
type: bug
priority: high
created_at: 2026-08-31T10:13:14Z
updated_at: 2026-09-03T15:01:58Z
---


## What was measured

Probe: `computations/probes/hbar_q_order_of_binding_observables_probe.py`
(5 assertions, all passing). Sweep in the substrate's own parameter,
`q = exp(η)`, `η = 1e-3 … 1e-6` — `exp(η)` is a genuine 60-dps value, so
`reject_float64_q` is satisfied rather than bypassed; no `allow_float64`
override is used anywhere.

| observable | classical floor | deformation order | verdict |
|---|---|---|---|
| `Δ(net) = h(h−2)/2`, `h = q − 1/q` | `0` exact | `0.99993` → **ℏ_q¹** | PASSES |
| Plancherel block sum (D, ⁴He, ¹²C) | `0` exact | `2.00021` → **ℏ_q²** | PASSES |
| `tr_M(W_free) − tr_M(W_atom)` | **`1/8` (D), `7/128` (⁴He)** | `1.0008`, `1.0021` → ℏ_q¹ | **FAILS** |

The floors extrapolate to `0.124999999874` and `0.054687499701` — `1/8` to
`1.3e-10` and `7/128` to `3.0e-10`. Simple dyadic rationals, which is not what a
numerical artefact looks like.

## Why it matters

At `q = 1` the Hecke algebra degenerates to `ℂ[S_n]` and no deformation remains.
`Δ(net)` and the block sum both vanish there — they are pure deformation
observables and they are the right kind of object. **The trace difference does
not vanish.** It returns a topological remainder: the free word and the atom word
close to different links whatever `q` is.

So it is two quantities at different orders,

    tr_M(W_free) − tr_M(W_atom) = c₀ + c₁·ℏ_q + O(ℏ_q²)

and at `q₀` the classical part is **22.46 %** of it for the deuteron, **4.88 %**
for ⁴He. That fraction of any binding read off this observable is present in a
framework with the braiding switched off.

## The registry's ℏ_q index is wrong for it

`derivation_chain.E_0_CONVENTIONS["B_q_value_absorbed"]` states:

> "Atom-level binding `B(Z,N) = E_0·(|tr_M(W_free)| − |tr_M(W_atom)|)` at
> `H_{3A}`. **The trace-difference operator carries the ℏ_q² scaling**; `E_0` is
> the unit-action scale."

Measured, it carries neither an `ℏ_q²` leading term nor a vanishing limit. This
matters because the `ℏ_q` index is exactly what selects the `E_0` convention, and
it is what the "≈ 102× error" warning is computed from (`qou-59j5`).

1. `B = E_0^{(B)}·Δtr` totals `ℏ_q⁰`, not `ℏ_q²`. It predicts nonzero deuteron
   binding at `q = 1`: `0.78233 × 1/8 = 0.0978 MeV`.
2. Strip the floor and the deformation part is `ℏ_q¹`, which pairs with
   convention **A** (`ℏ_q¹`) to total `ℏ_q²` — the same total as `Δ(net)×A`.
   The registry's rule says atom level MUST use **B**.
3. Neither pairs consistently with the observable *as a whole*, because its two
   parts sit at different orders. **No single scale can.**

## Two live producers already disagree, by exactly the convention ratio

On the identical deuteron trace difference `0.556544660404`:

| producer | convention | scale | binding | vs AME 2.22456637 |
|---|---|---|---|---|
| `binding_canonical.binding_canonical` | B | `Q_β = 0.78233340931` | **0.4354 MeV** | 5.11× short |
| `derive_binding_chain_cooperative.bond_binding` | A | `E₀ = 4.18598136` | **2.3297 MeV** | 1.047× |

`4.18598/0.78233 = 5.35` — the `E₀` convention ratio, exactly. This is the
collision `qou-59j5` catalogued in the registry, found in the wild.

⚠ **The A row lands within 4.7 % of AME and that is NOT evidence for A.**
Choosing the convention that lands closest to the target is precisely the fit
this lane has walked into three times (`qou-78pt`'s withdrawn refutation,
`qou-59j5`'s scale artefact, the six Δ_λ ansätze). The inconsistency is recorded,
not resolved. Resolving it needs the `ℏ_q` index fixed first, and the index is
what this bean shows is wrong.

## Correcting my own claim

I closed the previous turn recommending this lane with:

> "the **ℏ_q-suppressed** observables — `Δ(net)`, the trace differences — which
> do vanish classically and do pair with `E₀` consistently. Those are the right
> kind of thing to carry a binding magnitude."

**Half wrong, and the wrong half is the one the binding chain actually uses.**
`Δ(net)` does vanish classically and does pair consistently. The trace
differences do neither. I asserted it from the registry's prose instead of
measuring it — the same failure that produced the `m_e`-vs-`E₀` artefact earlier
in the session.

## What is NOT concluded

That the ℏ_q-suppressed route is refuted. `Δ(net)` and the Plancherel block sum
pass cleanly, and `Δ(net) × A` still predicts `Q_β` to 0.168 %. What is removed
is the assumption that the trace difference belongs to that category.

## Follow-ups worth opening

1. **Is the floor derivable?** `1/8 = 2⁻³` at `n_strands = 6`, `7/128 = 7·2⁻⁷` at
   `n_strands = 12`. Both dyadic. If the floor has a closed form in `n` it can be
   subtracted exactly, leaving a clean `ℏ_q¹` deformation observable that pairs
   with convention A — which would repair the construction rather than only
   diagnosing it. This is the highest-value next step.
2. **Fix the registry entry.** `E_0_CONVENTIONS["B_q_value_absorbed"]`'s operator
   class should record `ℏ_q⁰ + ℏ_q¹`, not `ℏ_q²`, and the "≈ 102×" warning
   recomputed from the corrected index.
3. **Adjudicate the two producers** — but only after (1) and (2).

---

## 2026-08-31 (later) — the floor has a CLOSED FORM, confirmed as a prediction

`c₀·2^{3A}` is an integer for every nucleus measured — **8, 48, 48, 224, 960,
960** at `A = 2, 3, 3, 4, 5, 5` — and those integers are `2^{A+1}(2^{A−1}−1)`. So

    c₀(A)  =  2^{−A} − 2^{1−2A}  =  (2^{A−1} − 1)/2^{2A−1}

**It depends only on `A`, not on the Z/N split.** T and ³He agree exactly; so do
⁵Li and ⁵He. That is required behaviour rather than luck: at `q = 1` every
one-crossing eigenvalue is `±1` and the flavour distinction disappears.

Read off `A = 2,3,4`, then **tested** at `A = 5` on two isobars that did not
enter the reading: predicted `15/512 = 0.029296875`, measured `0.0292968747`
(⁵Li) and `0.0292968747` (⁵He). Agreement to `9e-9` — Richardson extrapolation
error, which grows with `A` exactly as it should.

### So the floor is exactly subtractable — which turns this into a repair

`Δtr − c₀(A)` is a pure `ℏ_q¹` deformation observable, pairing with convention A
to total `ℏ_q²` — the same bookkeeping as `Δ(net)×A`. Follow-up (1) above is
therefore **done**, and it was the highest-value one.

### ⚠ And the repair costs the route its best number

| | conv A, raw | conv A, floor removed | AME |
|---|---|---|---|
| deuteron | 2.3297 MeV (0.955×) | **1.8064 MeV (1.231× short)** | 2.22456637 |
| ⁴He | 4.6875 MeV | 4.4586 MeV (6.346× short) | 28.29561 |

**The A-route's apparent 4.7 % near-hit at the deuteron was 22.46 % classical
contamination.** Removing the floor — which the ℏ_q bookkeeping requires —
degrades it to 1.23× short. ⁴He is ~6× short either way, consistent with the
known 4-body α-residual (`derive_binding_chain_cooperative`'s own finding).

Recorded prominently because a repair that makes a headline number *worse* is
the part most likely to be quietly dropped, and because it removes the one piece
of evidence that looked like it favoured convention A. It does not favour A; it
was the floor.

### Revised follow-ups

1. ~~Is the floor derivable?~~ **DONE** — `c₀(A) = 2^{−A} − 2^{1−2A}`, verified
   as a prediction at `A = 5`.
2. **Fix `E_0_CONVENTIONS["B_q_value_absorbed"]`** — the operator class should
   record `ℏ_q⁰ + ℏ_q¹` with the floor named, not `ℏ_q²`, and the "≈ 102×"
   warning recomputed. Now unblocked, since the floor has a form to name.
3. **Re-run the binding chain against `Δtr − c₀(A)`** and see what the per-bond
   constants become. The current `b_pp/b_pn/b_nn = 2.38/2.49/2.53` (signed) and
   `2.91/3.89/5.18` (log) all carry the floor.
4. **Prove `c₀(A) = 2^{−A} − 2^{1−2A}`** from the `q → 1` limit of the Markov
   trace. At `q = 1` the trace is a permutation-character sum over `2^{3A}`
   states, so a dyadic rational with denominator `2^{3A}` is exactly the
   expected shape — this should be a finite combinatorial argument, not an
   analytic one, and it would make the subtraction exact rather than measured.

---

## 2026-08-31 (later still) — the floor is DERIVED, and the arithmetic core is in Lean

Follow-up (4) is done, and it subsumes (1): the closed form no longer rests on
the Richardson extrapolation it was read off.

Probe: `computations/probes/classical_floor_derivation_probe.py` (5 assertions).
Lean: `QOU/MassTheory/ClassicalTraceFloor.lean` (sorry-free; axioms
`[propext, Classical.choice, Quot.sound]`, and `cAtom_eq_of_free_and_merges`
needs only `[propext, Quot.sound]`).

### Step 1 — Schur–Weyl at `q = 1`: `tr_M(β) = 2^{c(σ_β) − n}`

The Markov weights are `y_λ = s_λ(1,Q)/(1+Q)^n` (`qou-ssz6`); at `Q = 1`,
`s_λ(1,1) = dim V_λ^{GL(2)}` — zero for `ℓ(λ) > 2`, the corpus's row cap — and
`Σ_λ dim V_λ · χ^λ(σ)` is the character of `σ` permuting the factors of
`(ℂ²)^{⊗n}`, which is `2^{c(σ)}` because `σ` fixes exactly the basis vectors
constant on each cycle.

**Verified against the transfer kernel**, which is an entirely separate
computation: each trace limit is an exact power of two with an integer exponent
matching the independently-counted cycles, worst relative error `1.05e-8`
(extrapolation error, growing with `A`).

| | A | n | c_atom | c_free | tr_atom → | tr_free → |
|---|---|---|---|---|---|---|
| D | 2 | 6 | 3 | 4 | `2⁻³` | `2⁻²` |
| T | 3 | 9 | 4 | 6 | `2⁻⁵` | `2⁻³` |
| ³He | 3 | 9 | 4 | 6 | `2⁻⁵` | `2⁻³` |
| ⁴He | 4 | 12 | 5 | 8 | `2⁻⁷` | `2⁻⁴` |
| ⁵Li | 5 | 15 | 6 | 10 | `2⁻⁹` | `2⁻⁵` |

### Step 2 — the cycle counts, straight off the braid words

Every letter `(c, d, g)` of `atom_braid_word_3A` carries `d ∈ {0, −h, −h/2}` with
`h = q − 1/q`, so **every `d` vanishes at `q = 1`** and each letter degenerates
to the transposition `s_g`. The permutation is therefore `q`-independent and the
count is a product of transpositions:

    c(σ_free) = 2A        c(σ_atom) = A + 1        c_free − c_atom = A − 1

verified for **A = 2 … 20** (18 isotopes) with no trace evaluation at all — so it
holds far past `A = 5`, where the Markov trace stops being computable. ⁶Li
(`n = 18`) and ⁸Be (`n = 24`) are included.

**`c_free − c_atom = A − 1` is the finding inside the finding.** Each of the
`A−1` inter-nucleon interfaces merges exactly one pair of cycles — the same
`(A−1)`-bond chain adjacency `derive_binding_chain_cooperative` sums over,
arrived at from the permutation rather than from the interface list. **The
floor's A-dependence *is* the chain structure.**

### Step 3 — therefore

    c₀(A) = 2^{2A − 3A} − 2^{(A+1) − 3A} = 2^{−A} − 2^{1−2A}

exactly, for every `A`. Not fitted, not extrapolated.

### What is formal and what is not

`ClassicalTraceFloor.lean` proves step 3 and the decay bounds. Steps 1 and 2
enter `classical_floor_of_cycle_counts` as **explicit hypotheses in the
statement**, not as a class with no instance — deliberately, because step 1 is a
published theorem Mathlib lacks (no Schur–Weyl development) and step 2 is an
18-point computation on a concrete word. A reader sees exactly what is assumed.

`hmerge` is stated as `c_free = c_atom + (A − 1)` rather than as two tabulated
counts, so the chain adjacency is visible in the hypothesis rather than buried in
a table.

Also proved: `classicalTraceFloor_pos` (`0 < c₀(A)` for `A ≥ 2`) and
`classicalTraceFloor_lt` (`c₀(A) < 2^{−A}`) — the formal content of the measured
decay. Note the hypothesis is `A ≥ 2`, **not** `A ≥ 1`: at `A = 1` the two
exponents coincide and the floor is exactly `0`. Every nucleus has `A ≥ 2` so
nothing is lost, but the boundary case is real and Lean caught it — my first
draft asserted `A ≥ 1` and `omega` rejected it.

### The contamination, measured, dies as predicted

| | A | c₀(A) | classical share of `Δtr(q₀)` |
|---|---|---|---|
| D | 2 | `1/8` | **22.46 %** |
| T | 3 | `3/32` | 10.55 % |
| ³He | 3 | `3/32` | 10.50 % |
| ⁴He | 4 | `7/128` | 4.88 % |
| ⁵Li | 5 | `15/512` | 2.16 % |

Halving per nucleon, as `c₀ ~ 2^{−A}` requires. **The floor is a light-nucleus
contaminant.** So the deuteron's apparent agreement under convention A was
floor-driven and does not survive subtraction, while the ⁴He 4-body α-residual
story is essentially untouched.

### Follow-ups, revised

1. ~~Is the floor derivable?~~ **DONE.**
2. **Fix `E_0_CONVENTIONS["B_q_value_absorbed"]`** — still open. Its operator
   class should record `ℏ_q⁰ + ℏ_q¹` with the floor named `2^{−A} − 2^{1−2A}`,
   not `ℏ_q²`, and the "≈ 102×" warning recomputed.
3. **Re-run the binding chain against `Δtr − c₀(A)`** — still open, and now
   cheap, since `c₀` is exact for every `A` and needs no trace.
4. ~~Prove the floor from the `q → 1` limit.~~ **DONE** (steps 1–3 above; the
   arithmetic in Lean, steps 1–2 as stated hypotheses).
5. **NEW — formalise step 2.** "The ordered product of these transpositions has
   `A+1` cycles" is Lean-sized in principle: composing with a transposition
   changes the orbit count by exactly ±1, and decreases it exactly when the two
   points lie in different cycles. Mathlib has `Equiv.Perm.cycleType` but no
   direct orbit-count-under-swap lemma, so this needs the lemma built first. It
   would remove the last computational input other than Schur–Weyl.

---

## 2026-08-31 — follow-ups (2) and (3) done. Two binding derivation gaps closed.

Probe: `computations/probes/binding_chain_floor_corrected_probe.py` (3
assertions). Registry: `computations/derivation_chain.py`.

### (3) The chain against `Δtr − c₀(A)`: pairwise additivity improves 2.4×

`derive_binding_chain_cooperative` sums `(A−1)` **2-nucleon** bonds, so the chain
accumulates `(A−1)·c₀(2) = (A−1)/8` of floor while the whole-atom trace carries
only `c₀(A)`. Removing both:

| | chain/atom raw | floors removed |
|---|---|---|
| D | 1.0000 | 1.0000 (D *is* the pn bond) |
| T | 1.2812 | 1.1178 |
| ³He | 1.1927 | **1.0198** |
| ⁴He | 1.4706 | 1.1941 |

Worst-case deviation **47.1 % → 19.4 %**, a factor of 2.4. And **60.8 % of the
⁴He pairwise-vs-exact gap was floor bookkeeping**, not many-body physics.

⚠ **The binding residual gets *larger*** — ⁴He 21.40 → 22.97 MeV under
convention A — because the correction removes binding from the chain sum. Not in
tension: the floor was inflating the pairwise sum, so removing it makes the
pairwise picture more accurate *and* leaves more for the cooperative α term.

### The leading-order discrepancy is an EXACT RATIONAL — gap closed, not narrowed

`c₁ = lim (Δtr − c₀)/ℏ_q` is an exact dyadic rational in every case (≤ 1.3e-9):

    pp 19/8    pn 37/16    nn 9/4    T 163/64    ³He 85/32    ⁴He 259/128

so both orders of `Δtr` are dyadic — `c₀` derived, `c₁` measured — and the
chain-vs-exact ratios follow with **no fitting**:

    T    (37/16 + 9/4)/(163/64)        = 292/163 = 1.7914110429…
    ³He  (19/8 + 37/16)/(85/32)        = 30/17   = 1.7647058824…
    ⁴He  (19/8 + 37/16 + 9/4)/(259/128)= 888/259 = 24/7 = 3.4285714…

matching the extrapolated ratios to 1e-8–1e-11. **The pairwise-vs-exact
discrepancy at leading order is exactly known**, not a measured residual.

### ⚠ And that says the q₀ agreement is a cancellation, not a structure

At `q₀` the corrected ratios are 1.118 / 1.020 / 1.194; at **leading order** they
are 1.791 / 1.765 / **3.429**. The chain over-counts by 3.4× at ⁴He as
`ℏ_q → 0`, and the good agreement at `q₀` is higher-order terms partially
cancelling that. **Pairwise additivity of the signed functor is not a controlled
approximation** — its accuracy at `q₀` is a coincidence of the deformation size.

Not a contradiction of `2026-06-16-b-sym-linear-chain-closed-form.md`, which
reports exact additivity for the **log** functor `α·ln(tr_free/tr_atom)`. This is
the **signed** functor, which is what `derive_binding_chain_cooperative` uses.
Different objects — but the exactness claim must not be carried across, and they
are easy to conflate.

### (2) The registry entry, corrected — and the convention becomes *derived*

`E_0_CONVENTIONS["B_q_value_absorbed"]` said its operator class "carries the
ℏ_q² scaling". Corrected in place (original text kept, per the retraction
discipline):

* the operator is **ℏ_q⁰ + ℏ_q¹**, with the floor now named and derived;
* **the "≈ 102×" warning cannot be recomputed as stated.** `1/ℏ_q² = 101.862` is
  arithmetically right but its premise is false. The actual mismatch between
  using A and B on the same trace difference is the scale ratio
  `E₀^A/E₀^B = 5.35` — and two live producers differ by exactly that
  (`binding_canonical` B → 0.4354 MeV; `derive_binding_chain_cooperative` A →
  2.3297 MeV at the deuteron). The "MUST use B" rule rests on the wrong index
  and cannot adjudicate them.

**The gap this closes:** subtract the floor and `Δtr − c₀(A)` is a pure `ℏ_q¹`
observable, which pairs with **A** to total `ℏ_q²` — the same bookkeeping as
`Δ(net) × A`, which predicts `Q_β` to 0.168 %. So the atom-level scale is now
**selected by ℏ_q bookkeeping** rather than by fiat or by proximity to AME.
Before the subtraction no convention paired consistently at all.

Recorded as a measured fact. **Re-designating the canonical convention is an
owner decision and is not taken here** — that is the change that would move
downstream numbers, and doing it because it lands closer to AME is the fit this
lane has withdrawn three times.

### (5) formalising the cycle count — attempted below / deferred

See the next note. It is formal hygiene rather than a binding gap, so it was
taken last per the owner's redirect to the binding primary goal.

## (5) formalising — the binding half landed, the permutation half scoped and NOT landed

`QOU/MassTheory/PairwiseChainLeadingOrder.lean`, sorry-free (axioms
`[propext, Classical.choice, Quot.sound]`).

**Landed**, and it is the binding-relevant half: the leading-order
pairwise-vs-exact ratios, proved exactly.

* `c1_dyadic` — every leading coefficient is dyadic, stated as `c₁·2^k = m`
  (`Rat.den` does not reduce under `decide` for a division literal).
* `chain_over_atom_T = 292/163`, `chain_over_atom_He3 = 30/17`,
  `chain_over_atom_He4 = 24/7` — the ⁴He one simplifies because `259 = 7·37`
  and `888 = 24·37`.
* `chain_over_atom_He4_gt_three` — the formal statement that the leading-order
  error is **large**: the pairwise chain exceeds the exact `H_{3A}` trace by more
  than a factor of three as `ℏ_q → 0`. This is the warning, not a result to be
  pleased about.
* `chains_overcount` — all three over-count.

The `c₁` values enter as **definitions**, flagged as measurements. Only what
follows from them is proved. That is the honest line: `c₀` is derived
(`ClassicalTraceFloor`), `c₁` is not.

**NOT landed: the permutation half.** Formalising `c(σ_atom) = A+1` needs
"composing with a transposition changes the orbit count by exactly ±1, and
decreases it exactly when the two points lie in different cycles". Mathlib at the
pinned rev has `Equiv.Perm.cycleType`, `Equiv.Perm.SameCycle` and
`card_support_swap_mul` (a support-cardinality *inequality*) — but **no
orbit-count-under-swap lemma**. Orbit count would have to be built as
`cycleType.card + (n − support.card)` and the swap behaviour proved from the
cycle decomposition. That is a real development, and it is formal hygiene rather
than a binding gap, so it was taken last and left open per the owner's redirect
to the binding primary goal.

It stays as the one remaining computational input other than Schur–Weyl.


## 2026-09-03 — cross-reference (session on qou-pdg9)

Follow-up "c1 is measured, not derived" is now closed elsewhere: bean `qou-pdg9`
derives `c1 = 2^{-n} Σ_ℓ w_ℓ 2^{c(σ^{(ℓ)})}` (free − atom) by the same Schur–Weyl
route as the floor, obtains all six values EXACTLY by series arithmetic (no
Richardson), and finds the closed form
`c1(Z,N) = (21Z+16N)(2^{-A-1} − 2^{-2A}) − 4(I_pp − I_nn)2^{-2A}`. Lean:
`QOU/MassTheory/LeadingOrderTraceCoefficient.lean`. Follow-up (5) here — the
permutation-half formalisation (orbit count under a deleted transposition) —
is still open and is now needed for BOTH c0 and c1.

## Classical-floor closed form: one mechanism tested and REFUTED (2026-09-03)

Scope (a) — this construction, alone, does not reproduce the floors. It does
NOT exclude a dyadic origin; see what survives below.

**The hypothesis.** Under convention D, z = q³/(q²+1), so **z(q=1) = 1/2
exactly**. That makes a dyadic classical floor the EXPECTED shape rather than a
coincidence, and the measured values decompose suggestively:

    deuteron   1/8   = 2⁻² − 2⁻³
    ⁴He        7/128 = 2⁻⁴ − 2⁻⁷

If the q=1 Markov trace on a braid closing to a c-component link were
z^(n−c), the floor would be 2^-(n−c_free) − 2^-(n−c_atom).

**Refuted by measurement.** Using the corpus's own accessor —
`TR.atom_braid_word_3A(Z, N, include_inter=False)` is the free word, the
keyword I initially missed — the underlying permutations are:

    atom      n    c_free  c_atom   predicted   measured
    deuteron  6    6       5        1/2         1/8
    ⁴He       12   12      11       1/2         7/128
    |word|         22/23 (D), 44/47 (⁴He)

c_free = n both times, i.e. **the free word's underlying permutation is the
IDENTITY** — it closes to the n-component unlink, which is the right topology
for non-interacting nucleons. c_atom = n−1: one inter-nucleon crossing merges
exactly two components. Both are sensible, and neither yields the floor.

**What this rules out:** that the classical limit is the naive cycle-count
trace z^(n−c). It is not — the words carry 22-47 generators with signs and
multiplicities, and at q=1 the Hecke algebra degenerates to C[S_n] but the
Markov trace of a general element is not z^(n−c) unless the element is a
positive permutation braid.

**What survives, and is worth the next attempt:** z(1) = 1/2 is exact, so the
floor being dyadic is structural rather than numerical, and the exponents (3
for A=2, 7 for A=4) satisfy 2A−1. A closed form should exist; it just is not
this one. The next thing I would test is the q=1 trace computed through the
actual transfer/seminormal path rather than a cycle-count shortcut — i.e.
evaluate TR.tr_m_atom_multi_q at q → 1 for both include_inter values and read
the limit, instead of predicting it.

I am recording this as a refuted mechanism rather than leaving it untried-
looking, because the guess is the obvious one and the next agent will make it.

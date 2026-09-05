# Which weight family does Φ_k require? — a derivation, a prune, and a discriminator that flips

**Date:** 2026-09-05
**Bean:** `qou-oots`
**Lean:** [`QOU/BraidKnot/DepthStratifiedWeightRequirements.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/DepthStratifiedWeightRequirements.lean) — `lean`-direct exit 0, 0 `sorry`, `#print axioms` = `[propext, Classical.choice, Quot.sound]` on all six declarations
**Probe:** [`computations/probes/phi_k_weight_family_discriminator.py`](../../computations/probes/phi_k_weight_family_discriminator.py)
**Witness:** [`computations/probes/phi-k-weight-family-discriminator.witness.json`](../../computations/probes/phi-k-weight-family-discriminator.witness.json)
**Builds on:** [`2026-09-04-plancherel-convention-gap.md`](2026-09-04-plancherel-convention-gap.md) (`qou-7o7h`), [`2026-06-20-keystone-wlambda-beasley-witten-localization.md`](2026-06-20-keystone-wlambda-beasley-witten-localization.md), [`2026-06-16-keystone-plancherel-target-clarification.md`](2026-06-16-keystone-plancherel-target-clarification.md), beans `qou-sf1t`, `qou-uk8o`

---

## 0. The verdict up front

The depth-stratified binding functional

$$
\Phi_k(\beta) \;=\; \sum_{\lambda \,:\, \mathrm{depth}\,k} w_\lambda \,
  \log\!\big(|\chi^\lambda(\beta)| \cdot d_q(\lambda)\big),
\qquad
B \;=\; \sum_k \alpha_k\big(\Phi_k^{\text{free}} - \Phi_k^{\text{atom}}\big)
$$

carries three derivable requirements on `w_λ`. They **retire two of the four
live candidates outright**, both scope-(b) with a proved invariant:

| # | requirement | derived from | retires |
|---|---|---|---|
| **R1** | nonzero support on the depth-`k` stratum | `phi_eq_zero_of_weights_vanish` | **(4) `y_λ`** — the SU(N) row cap makes it *exactly* zero on every stratum of depth ≥ N, so Φ₃ ≡ 0 |
| **R2** | `n`-independent total mass (weaker than "probability measure") | `crossRatio_smul` | **(1) `d_q²/[n]_q!`** — mass drifts 0.991 → 1.517 over `n = 6…12` |
| **R3** | *no* Markov property is required — Φ is not a trace | `phiDiff_eq_sum_log_ratio` | nothing; it removes the *reason* to want `y_λ` and blocks a scope error |

**Two survive: `(2) d_q²/D²` and `(3) the Molien family` `f^λ q^{−κ_λ} d_q(λ)/[n]_q!`.**
The choice between them is **not settled** here, and I recommend against
declaring it settled by either party's current evidence. But there is a real
evidential asymmetry, and it does not favour my own earlier switch:

- `(2)` is mass-one **by construction** — a self-normalised family, which bean
  `qou-sf1t` records in as many words as *not evidence* that its normaliser is
  canonical.
- `(3)` is mass-one **by theorem** — `molienSum_eq_qFactorial`, sorry-free for
  every `n` and every `q > 1`, with a normaliser (`[n]_q!`) that was named
  independently of this question — and, established exactly here for the first
  time, **`(3)` *is* the literature's q-Plancherel measure** (Féray–Méliot)
  under the corpus's own `Q = q²` bridge.

**And the choice is empirically load-bearing.** The k=3 FR-pullback ranking is
**not** weight-family-invariant. The three families that can score it at all
name **three different best knots**, and under the structurally best-credentialed
family the paper's named `6₁` is the **worst** of the three and the only one
that makes its own baseline worse.

---

## 1. What Φ_k actually requires — derived, not surveyed

All three are proved generically in the Lean companion, over abstract
`w, m, c : ι → ℝ`. No `q₀`, no anchor, no character theory enters.

### R3 first, because it reframes the other two: **Φ is not a trace**

`phiDiff_eq_sum_log_ratio`. Free and atom are summed over the *same* index set
(verified: `atom-chi-rust-*.witness.json` carry identical partition lists for
the two configurations) with the *same* weights, so the `d_q(λ)` inside the
logarithm **cancels**:

$$
\Phi_k^{\text{free}} - \Phi_k^{\text{atom}}
  \;=\; \sum_{\lambda:\,\mathrm{depth}\,k} w_\lambda \,
        \log\frac{|\chi^\lambda(\beta_{\text{free}})|}{|\chi^\lambda(\beta_{\text{atom}})|}.
$$

So `B` is a `w`-weighted mean of log character-ratios — a weighted *geometric
mean*. It is **not linear** in the braid-group algebra element. Two consequences
run in opposite directions and both matter:

1. **`y_λ`'s only claim to privilege here evaporates.** `y_λ` is canonical
   because `tr_M = Σ_λ y_λ χ^λ` is a *Markov* trace: `tr(βσ_n^{±1}) = z^{±1}
   tr(β)`, hence braid-closure invariance. Φ never forms that linear sum, never
   evaluates `z`, and has no move-invariance to inherit. "It is the canonical
   Frobenius pairing weight" is true and is not an argument about Φ.
2. **The corpus's own regular-trace exclusion must not be imported here.**
   [`q_plancherel_vs_y_lambda_probe.py`](../../computations/probes/q_plancherel_vs_y_lambda_probe.py)
   (lines 87–95, and its `wider_exclusion` witness block) concludes: *"any
   weight system arising from a trace that VANISHES on non-identity braid
   elements yields `z = 0` … so the search should be restricted to Markov
   traces, which excludes the whole regular-trace/Plancherel family."* That is
   correct **and is scoped to the A=4 interface bond scalar `m = z = tr(σ₁)`**,
   a linear trace evaluation. Applying it to Φ_k would be a scope error of
   exactly the arity-conflation class AGENTS.md §"Grep the claim SHAPE"
   describes. It does **not** exclude the Molien/q-Plancherel family from this
   functional.

### R1 — nonzero support on the stratum

`phi_eq_zero_of_weights_vanish`: if `w_λ = 0` throughout the depth-`k` stratum
then `Φ_k = 0` for *every* braid — the stratum carries no information at all.

The SU(N) Markov weight is `y_λ ∝ ∏_□ [N + c(□)]_q / [h(□)]_q`. A `λ` with more
than `N` rows has a cell at `(N+1, 1)` of content `−N`, contributing
`[N + (−N)]_q = [0]_q = 0`, which kills the whole weight. This is
[`RowCapObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/RowCapObstruction.lean)
arriving as arithmetic, and `y_lambda_su_n.py`'s own docstring states it.

Depth `k` means `k+1` rows. Therefore **`y_λ = 0` on every stratum of depth
`≥ N`.** Production is `N = 2` (convention D), so that is *every stratum from
depth 2 up*, including the depth-3 chirality channel. Verified symbolically in
`Q(q)` at `n = 3,4,5,6` for `N = 2` and at `n = 4,6` for `N = 3` — and at
`N = 3` the cap still lands on depth ≥ 3, so **`k = 3` is vacuous under `y_λ`
at both the mass (`N = 2`) and colour (`N = 3`) readings.**

This is a **scope-(b) exclusion**: not "`y_λ` performs badly", but "`y_λ` makes
the object identically zero", with the invariant cited.

Measured consequence, §B of the probe: under `y_λ` all three candidate knots
reproduce the no-FR baseline **to the last recorded digit** (max/min `5.3561249`
for all four rows). The FR test is not merely insensitive under `y_λ`; it is
undefined-by-vanishing.

### R2 — `n`-independent total mass

`crossRatio_smul`: `Φ` is linear in `w`, so `w → k_n·w` sends `B(A) → k_{n}B(A)`
and multiplies the cross-nucleus metric `(B₁/E₁)/(B₂/E₂)` by exactly `k₁/k₂`.
Since `n = 3A` differs between nuclei, a normaliser that drifts with `n`
distorts every cross-nucleus comparison.

**Note the requirement is weaker than "probability measure."** Any `n`-independent
constant works; mass-one is sufficient, not necessary. That is worth stating
because the `qou-7o7h` correction is sometimes read as "Φ needs a probability
measure", and it does not — it needs `n`-independence.

This is the cross-`n` complement of
[`WLambdaNormalizationInvariance.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaNormalizationInvariance.lean)'s
`ratio_invariant`, which proves the *same-`n`* **ratio of two `w`-weighted
quantities** is normalisation-invariant.

> **Do not over-read that as "the choice is invisible at fixed `n`" — it is
> not, and I wrote it that way first.** A λ-independent `k_n` cancels from a
> *ratio of two `w`-weighted sums at the same `n`*, and from nothing else. `B(A)`
> itself scales by `k_n`; so does the scored `B(A)/B_exp(A)`, since `B_exp`
> carries no weights. The choice is invisible only where the observable is
> already such a ratio. (Correction supplied by the merge coordinator against my
> first phrasing.)

So the C1 normalisation choice is decisive across `n`, and Φ is a cross-`n`
use.

Measured (proton pin, `mp.dps = 50`):

| `n` | `Σ_λ d_q²/[n]_q!` | `Σ d_q²/D²` | `Σ` Molien | `Σ y_λ f^λ` |
|---|---|---|---|---|
| 2 | 0.9945810912 | 1 | 1 | 1 |
| 3 | 0.9874402298 | 1 | 1 | 1 |
| 4 | 0.9821653238 | 1 | 1 | 1 |
| 5 | 0.9822241483 | 1 | 1 | 1 |
| 6 | 0.9910795236 | 1 | 1 | 1 |

and at the nuclear `n = 3A`: `c_6 = 0.99107952`, `c_9 = 1.1109231`,
`c_12 = 1.5171332`. **(1) fails R2**; the other three pass.

Note `y_λ` enters as the **block mass** `y_λ f^λ`, not as bare `y_λ`. `y_λ`
lives in the *trace* slot (`Σ y_λ χ^λ = tr_M`, normalised by `Σ y_λ f^λ = 1`);
Φ sums one term per block, which is the *measure* slot. Using the block mass is
the only reading under which `y` is comparable with the other three at all — and
it does not rescue it, because R1 kills it either way.

### What is NOT a requirement: conjugation symmetry

The depth-3 stratum is called "the chirality channel", which invites the
requirement *"`w` must be chirally asymmetric"*. **That does not follow.**
Measured: the `d_q²` families are conjugation-**symmetric** exactly
(`W_λ = W_{λ'}`, since `λ` and `λ'` share their hook multiset), while the Molien
family is conjugation-**asymmetric**, carrying `q^{−κ_λ}` with
`κ_λ = Σ_□ c(□) = n(λ') − n(λ)`. But the **depth stratification itself already
separates `λ` from `λ'`** — they generally sit in different strata — so a
symmetric `w` is not per se incompatible with a chiral channel. This is recorded
as a property that distinguishes the two survivors, **not** as a derived
requirement, and it should not be used as one without an argument that the
asymmetry must live in `w` rather than in the stratification.

---

## 2. A new identification: the Molien family **is** the q-Plancherel measure

Established exactly in `Q(q)`, every partition, `n = 2,3,4,5`
(assertion `molien_equals_feray_meliot_q_plancherel`).

The corpus's Lean-proved Molien / fake-degree weight and Féray–Méliot's
q-Plancherel measure `M_{n,Q}(λ) = Q^{b(λ)}\dim\lambda/\prod_□\{h(□)\}_Q`
([`library/arxiv-1001.2180v2`](../../library/arxiv-1001.2180v2/)) are **the same
object** under `Q = q²` — the same convention bridge
`q_plancherel_vs_y_lambda_probe` derived independently from matching Hecke
eigenvalue ratios (`(T−q)(T+1) = 0` vs `(σ−q)(σ+q⁻¹) = 0` ⇒ `T = qσ`).

The bridge is one line of hook arithmetic. With `[h]_q` balanced and
`\{h\}_Q = 1 + Q + \dots + Q^{h−1}`,

$$
\prod_\square [h]_q = q^{-(n(\lambda)+n(\lambda'))}\prod_\square \{h\}_{q^2},
\qquad
\kappa_\lambda = \sum_\square c(\square) = n(\lambda') - n(\lambda),
$$

so `f^λ q^{−κ_λ}/∏[h]_q = f^λ Q^{n(λ)}/∏{h}_Q` exactly, and `b(λ) = n(λ)`.

**Three things follow, and the naming one is the most consequential.**

1. **The corpus's "q-Plancherel" is not the q-Plancherel measure.**
   `computations/deltalambda/` and the s5-so3 keystone call `d_q²/[n]_q!`
   "Ocneanu / q-Plancherel"; the object the literature calls the q-Plancherel
   measure is the Molien family, which the corpus holds under a different name
   and never connected to it. `q_plancherel_vs_y_lambda_probe` §7 already proved
   the corpus's `W_λ` and the paper's `M_{n,q}` are **different** objects; what
   was missing is that the paper's object is *also already in the corpus*, as
   `molienSum`.
2. **It is the only one of the four whose exact normalisation is a theorem
   rather than a construction or a definition.** `Σ = 1` for `(2)` is
   `Finset.sum_div`; `Σ = 1` for `(3)` is `molienSum_eq_qFactorial`, whose proof
   runs through the general-`X` Macdonald telescope and the convention bridge.
3. **It is the correct `q`-lift of Burnside.** `Σ_λ (f^λ)² = n!` q-lifts by
   replacing **one** factor with a quantum dimension, giving
   `Σ_λ f^λ q^{−κ_λ} d_q(λ) = [n]_q!` — not both, which is what `d_q²` does and
   what the `qou-7o7h` audit already identified as the structural defect. At
   generic `q`, `H_n(q) ≅ ℂ[S_n]`, so the Wedderburn **block dimensions are the
   classical `f^λ`**; `d_q` is the *Schur–Weyl dual* quantum dimension. The
   natural pairing of a Hecke block against its dual multiplicity space is
   `f^λ · d_q(λ)`, and `d_q²` pairs the dual against itself.

---

## 3. The discriminator: the k=3 ranking is **not** weight-family-invariant

Method: a read-only companion re-runs the k=3 FR sweep of
[`fr_pullback_k3_test.py`](../../computations/fr_pullback_k3_test.py) under each
family, from that producer's own upstream character witnesses. The FR pullback
is generalised the only way that keeps the comparison controlled — the depth-3
mass `S₃ = Σ_{depth 3} w_λ` is preserved and redistributed proportionally to
`w_λ|χ^λ(K)|`, which at `w = d_q²/D²` is the producer's formula verbatim.

**Harness validation.** Under `d_q²/D²` the companion reproduces the committed
producer witness on all four rows to `≤ 2.07e-16` relative. (The residual is not
noise: `fr_pullback_k3_test` takes `q₀` from `qou_substrate.constants.Q`, which
is a Python **`float`** — measured `2.725e-17` relative from the 50-digit string
this probe uses. See §5.)

| family | no FR | 4₁ | 5₂ | 6₁ | best | beat own baseline |
|---|---|---|---|---|---|---|
| **(1)** `d_q²/[n]_q!` | 1.562126 | **1.5014667** | 1.5394226 | 1.6040329 | **4₁** | 2/3 |
| **(2)** `d_q²/D²` | 1.0659881 | 1.2425297 | 1.2911323 | **1.0478474** | **6₁** | 1/3 |
| **(3)** Molien | 1.5488755 | 1.2308566 | **1.2168828** | 1.6067832 | **5₂** | 2/3 |
| **(4)** `y_λ` | 5.3561249 | 5.3561249 | 5.3561249 | 5.3561249 | — (vacuous) | 0/3 |

Improvement on each family's **own** no-FR baseline:

| family | 4₁ | 5₂ | 6₁ |
|---|---|---|---|
| (1) `d_q²/[n]_q!` | +3.88 % | +1.45 % | **−2.68 %** |
| (2) `d_q²/D²` | −16.6 % | −21.1 % | **+1.70 %** |
| (3) Molien | +20.5 % | +21.4 % | **−3.74 %** |

**Three families, three different orderings, three different winners.** The
k=3 verdict is a statement about the weight family at least as much as about
the knot.

Three specific readings, each of which someone will otherwise take:

- **The published `4₁`-is-best result is family (1)** — and (1) is retired by
  R2. Its ranking difference from (2) is *pure normalisation*: verified to
  `< 5.1e-50` relative that the per-atom ratios differ by exactly the
  λ-independent `c_n` (`wPlanch_eq_global_factor` arriving as arithmetic). So
  (1) vs (2) is the `qou-7o7h` reversal, re-derived independently here.
- **The current `6₁`-is-best result is family (2)**, and it is a **+1.7 %**
  effect — consistent with `2026-09-04` §7.2, which already collapsed the
  headline magnitude from "42 %" to that figure.
- **Under family (3), the paper's named `6₁` is the worst of the three and the
  only one that makes its own baseline worse**, while `4₁` and `5₂` are nearly
  tied at ~+21 % — a far *larger* FR effect than any family has shown, pointing
  at a different knot. The robust Molien statement is *"{4₁, 5₂} both close ~21 %
  of the variance, 6₁ opens it"*, not *"5₂ specifically"* — the two are 1.1 %
  apart, which this metric does not resolve.

**Why the families are not interchangeable, mechanically.** They do not merely
rescale one another; they put materially different mass on the very stratum the
FR test acts on:

| atom | `n` | `S₃` under (1) | (2) | (3) Molien | (4) |
|---|---|---|---|---|---|
| D | 6 | 0.24714993 | 0.24937446 | 0.34872803 | 0 |
| T | 9 | 0.52082291 | 0.46881993 | 0.39164009 | 0 |
| ⁴He | 12 | 0.49912731 | 0.32899373 | 0.13668037 | 0 |

Molien's `q^{−κ_λ}` skews mass toward deep (column-like) partitions at small `n`
and away at large `n` — the opposite `A`-trend from `d_q²/D²`. That is the
mechanism behind the ranking flip, and it is a *within-`n` profile* difference,
which no normalisation argument can settle.

---

## 4. Adversarial pass on `d_q²/D²`, which is my own earlier choice

Stated plainly, because I switched to it and the switch deserves the hostile
reading:

- **Its Lean support proves nothing about canonicity.** `sum_measureOn_eq_one`
  and `wPlanch_sum_one` are one line from `Finset.sum_div` — true of *any*
  self-normalised family. Bean `qou-sf1t` says this in its own SCOPE section.
  Citing "it is Lean-proved to be a probability measure" as evidence it is the
  right measure is circular, and the switch was made partly on that footing.
- **Its literature support is real but is about a different question.** The
  Beasley–Witten / RT–Verlinde argument
  ([`2026-06-20`](2026-06-20-keystone-wlambda-beasley-witten-localization.md))
  is a genuine mechanism and it answers **C1 for the s5-so3 keystone's `W_λ`** —
  an `S¹`-equivariant index over an MTC's `S²×S¹` Hilbert space. Φ_k is not
  that object: it is a log-weighted character functional over Hecke blocks at
  `n = 3A`, in the nuclear sector. The keystone clarification note
  ([`2026-06-16`](2026-06-16-keystone-plancherel-target-clarification.md)) is
  explicit that the lepton-tower Plancherel sector and the nuclear-atom sector
  are *different sectors, correctly weighted differently* — and warns **"do not
  bridge them."** Importing the keystone's C1 answer into Φ_k is exactly that
  bridge.
- **It is conjugation-symmetric**, in a functional whose k=3 stratum the paper
  calls the chirality channel. Not disqualifying (see §1), but the asymmetry
  then has to come entirely from the stratification, and nobody has argued that
  it does.
- **`d_q²` pairs the Schur–Weyl dual against itself**, where the Hecke block
  dimension is `f^λ`. `qou-7o7h` already recorded this; §2.3 above is the same
  point from the Burnside side.

**If (3) Molien is the principled one, say so plainly.** On the evidence
assembled here, **Molien has the better structural case and I would take it**
— exact normalisation by theorem rather than construction, the correct
one-factor `q`-lift of Burnside, an independently-named normaliser, and an exact
identification with the literature's q-Plancherel measure. *That is my
judgement, not a finding.* What stops it being a finding is that none of those
properties is derived **from Φ_k**: they are reasons the family is canonical
*as a measure on Wedderburn blocks*, and R1–R3 do not select between two
families that both satisfy them. Adopting Molien on this basis would be
substituting a good argument for a derivation, and the corpus has a standing
rule against exactly that trade.

---

## 5. Two defects found while doing this

Recorded because one is mine and the other is upstream of a published number.

1. **My own hand-typed `B_AME["T"]`.** I typed `8.481798` where
   `codata_constants.AME_B_TRITIUM_MEV_VALIDATION` is `8.4817962` — a uniform
   `2.12219e-7` relative disagreement with the producer on **three of four**
   rows. It was visible only because §B1 compares against the committed witness,
   and *diagnosable* only because the fourth row (`6₁`) agreed to `3e-16`: T is
   the argmin for the other three and is not for `6₁`, so the defect had to be
   in `B_AME["T"]` and nowhere else. Fixed by importing the constant. **The
   lesson is the producer's own recorded one** — `fr_pullback_k3_test` already
   carries a caveat about a hand-typed AME literal in a self-comparing
   assertion; I reproduced the same class of error one file over, and only a
   cross-check against an independent second source caught it.
2. **The k=3 anchor is float64-sourced.** `fr_pullback_k3_test` takes `q₀` from
   `qou_substrate.constants.Q`, which is a Python `float`; the corpus also ships
   `Q_50_DIGIT_STR`. Measured deviation `2.725e-17` relative. This is **not**
   material to anything in this document (fifteen orders below the ~30 % ranking
   effects) and is **not** fixed here, because changing a producer's anchor
   moves its published numbers and would break the controlled comparison this
   probe rests on. This companion uses the decimal string and is float64-clean;
   the producer's anchor is flagged for its owner. No claim is made that any
   recorded k=3 number is wrong because of it.

---

## 6. Scope — what this does and does not establish

**Established.**

- R1/R2/R3 as stated, Lean-proved generically, sorry-free, axioms clean.
- `y_λ` is excluded for this functional, scope-(b), invariant cited — at `N = 2`
  *and* `N = 3`, for every stratum of depth ≥ N.
- `d_q²/[n]_q!` is excluded for cross-nucleus use, scope-(b), invariant cited
  (`crossRatio_smul` + the measured drift). It remains valid wherever the
  observable is a **ratio of two `w`-weighted quantities at one `n`**, by
  `ratio_invariant` — which is narrower than "any same-`n` quantity", since
  `B(A)` and `B(A)/B_exp(A)` both still carry the factor.
- Molien ≡ Féray–Méliot q-Plancherel at `Q = q²`, exactly, in `Q(q)`.
- The k=3 ranking is weight-family-dependent, with the harness cross-validated
  against the committed producer to `2.07e-16`.

**Not established, and not to be read in.**

- **Which of `(2)` and `(3)` is right.** This is **open**. §4 states a
  preference and marks it a judgement.
- **That any k=3 knot identification is correct or incorrect.** The result here
  is that the *test does not currently determine one*, which is weaker than
  either verdict and is the honest state.
- **That the FR conjecture is supported or refuted.** Under (3) the mechanism
  looks *stronger* than previously reported (~21 % vs 1.7 %) and points
  elsewhere; that is a reason to derive the family before reading the test, not
  a verdict on the conjecture.
- **Anything about the s5-so3 keystone's `W_λ`.** Different sector; the
  2026-06-16 "do not bridge them" ruling is respected in both directions.

## 7. What single measurement or proof would close it

One of these, in decreasing order of how decisive it would be:

1. **A derivation of the block measure from the Schur–Weyl decomposition of the
   nuclear braid representation.** Φ weights Wedderburn blocks of `H_{3A}(q)`;
   the measure a block "should" carry is its share of whatever object the
   nucleus is a state in. If that object is `V^{⊗n}` with `V` the `U_q(sl_N)`
   fundamental, the share is `f^λ d_q(λ)/[n]_q!`-shaped (Molien) and the
   question is closed. If it is the endomorphism algebra `End(V^{⊗n})`, the
   share is `d_q²/D²`-shaped and the question is closed the other way.
   **Naming which object the nucleus is a state in is the whole content**, and
   it is a structural question, not a numerical one.
2. **A same-`n`, within-stratum observable.** Built as a ratio of two
   `w`-weighted quantities at one `n`, it is normalisation-invariant by
   `ratio_invariant`; but the *profile* is not, and (2)
   and (3) differ per-λ (§3, `S₃` table). Any observable that resolves the
   within-`n` weight profile at fixed `A` separates them without needing the
   cross-nucleus metric at all — and would be immune to the `c_n` artifact
   entirely.
3. **A cross-nucleus metric with more than four points.** Four atoms spanning
   `n ∈ {6, 9, 9, 12}` is too few for a max/min statistic to be stable against a
   ~1 % ranking gap (Molien's 4₁ vs 5₂). Extending to ⁶Li/⁷Li/⁹Be would say
   whether any of these orderings survives.

Until one of those lands, **no k=3 knot conclusion should be quoted without
naming the weight family it was computed under** — which, given §3, is the
practical output of this note.

---

## 8. Coordination — what this means for the `qou-uk8o` sweep, which landed today

The sibling sweep
([`2026-09-05-plancherel-weight-sweep.md`](2026-09-05-plancherel-weight-sweep.md),
`qou-uk8o`) migrated ~8 producers from `d_q²/[n]_q!` to the **self-normalised**
`d_q²/D²`. **Nothing in this note asks for any of that to be reverted**, and I
want to be explicit about the scope of the interaction:

- **The sweep's direction is right and this note supports it.** R2 retires
  `d_q²/[n]_q!` for cross-`n` use with a proved invariant; every migration it
  performed moves off a family this note independently excludes. That agreement
  was reached from two directions — the sweep from the measured `c_n` drift,
  this note from `crossRatio_smul` — and neither depends on the other.
- **The sweep's *destination* is one of two survivors, not the derived answer.**
  `d_q²/D²`'s exact normalisation is `Finset.sum_div`; it is true of any
  self-normalised family and is not evidence about canonicity (`qou-sf1t`,
  quoted in its own words in §4). A later derivation could land on the Molien
  family instead, and — §3 — that would move numbers, not merely labels.
- **Concrete ask, cheap:** where a migrated producer records its weight, record
  it as `d_q²/D²` *by name* rather than as "the self-normalised q-Plancherel
  measure". The second phrasing is doubly misleading now: it reads as though the
  normalisation were derived, and §2 establishes that the object the literature
  calls the q-Plancherel measure is a **different family** (Molien) that the
  corpus also already holds. Naming the family is what makes a later re-migration
  a mechanical grep instead of a re-derivation.

Two of the sweep's own corrections are consumed here rather than re-litigated:
`6a343ef7726` narrowed the cancellation rule to *a ratio of two `w`-weighted
sums at one `n`* — §1 R2 carries that narrowing, and my first draft had the
over-permissive form — and `f5ecb3ae68b` established that the `[n]_q!` defect is
**structural rather than a convention artifact**, which is what makes R2 an
exclusion rather than a convention preference.

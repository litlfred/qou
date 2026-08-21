# The Q_β ladder phase `α`, against the actual Wedderburn weights

Bean [`qou-q2oa`](../../.beans/qou-q2oa--the-ladder-phase-alpha-has-no-derivation-from-the.md)
(high, parent `qou-cdx1`, tranche `qou-cds1`). PR #5353.

**Status: RESOLVED in both directions.** The bean asked to *"derive `α` from
the weight vector, or establish that it is not determined by the weights alone
— a clean negative is a result here."* Both halves are settled, and they are
consistent: `α` is **not** a function of the weights (proved, structural), and
`α` **is** determined by the weights **together with `h`**, with an explicit
closed form whose `n`-dependence vanishes.

---

## 1. What `α` is, recovered from the corpus

`α` enters at exactly one place. In
[`qbeta_d_frame_ladder_structure_probe.py`](../../computations/qbeta/qbeta_d_frame_ladder_structure_probe.py)
the N=1 rung's cosine argument is `cos_arg(q,z) = α − u/2` with

```
α = (z − 1)·h/2 ,     h = q − q⁻¹
```

and that probe's assertion A1 establishes it is **the ONLY place a
Markov-trace convention enters the entire Q_β ladder** — every other
ingredient (`Q_A`, `h`, `ℏ_q`, `b`, `u`, the N=2 factor `1 − b²ℏ_q⁴`) is
`z`-free. In Lean it is
[`QOU.QBeta.phaseTwice`](../../content/quantum-observable-universe/lean/QOU/QBeta/LadderPhaseMirrorCovariance.lean)
`z h = (z−1)*h`, carried doubled so parity bookkeeping needs no division.

**`α` is asserted upstream, not derived.** `LadderPhaseMirrorCovariance`'s own
docstring calls it *"the asserted phase"*. Nothing below derives the ansatz;
what is derived is what the ansatz **equals** in terms of the weights.

### 1a. What the retracted derivation actually claimed — and its real defect

PR #5187 asserted `α = −h/4 − (h/2)·y₍₂,₁₎` and retracted it after PR #5185
showed the instance `(z, 1/2−z, z)` satisfies only the normalisation and fails
the other two Markov conditions.

The probe reconstructs the algebra (check A0): setting `y₍₂,₁₎ := 1/2 − z`
gives `z = 1/2 − y₍₂,₁₎`, and substituting into `(z−1)h/2` returns
`−h/4 − (h/2)y₍₂,₁₎` identically. So the relation was a **change of variable
off a false identity**.

**A sharpening of the retraction (check A0b).** The retracted formula was not
merely inaccurate — it was **tautological**. Fed its own bogus instance it
returns `α` *exactly*: at the proton pin both print
`−0.040485777340642764919`. No arithmetic check could ever have caught it,
because there was no arithmetic error to catch. Only checking the instance's
**defining conditions** could — which is precisely AGENTS.md §"Grep the claim
SHAPE, not only the topic". It diverges only when fed the **real** weight:

| quantity | value at the proton pin |
|---|---|
| true `α_D` | `−0.040485777340642764919` |
| retracted formula on its own bogus `y` | `−0.040485777340642764919` (identical) |
| retracted formula on the **real** `y₍₂,₁₎` | `−0.078115159746446971546` |

---

## 2. The weights, and where they come from

The corpus's own D-frame weights are the **two-variable Schur measure**.
[`schur_principal_mpmath.py`](../../computations/schur_principal_mpmath.py)
carries `Q = q²`, `Q^r = q⁴ = Q²` — Wenzl level `r = 2` exactly — and
`y_λ = s_λ / Σ_μ f^μ s_μ`. Since `Σ_μ f^μ s_μ(x) = p₁(x)^n`, that is

```
y_λ = s_λ(1, Q) / (1 + Q)^n ,   Q = q² ,   zero for ℓ(λ) > 2.
```

Verified against the **live** producer `y_lambda_at_q0_mpmath` (never the
muon-serving cache) for n = 2..9: max deviation **4.612e-61** (check A1). At
n = 3 it reproduces PR #5185's triple exactly:

| λ | `y_λ` | at q₀ |
|---|---|---|
| `(3)` | `(q⁴+1)/(q²+1)²` | 0.50540422650393080319 |
| `(2,1)` | `q²/(q²+1)² = 1/[2]_q²` | 0.24729788674803459841 |
| `(1³)` | `0` | 0 |

---

## 3. The negative half — `α` is NOT a function of the weights

**Scope-(b) structural exclusion, with a named proved invariant: bar-parity.**
(AGENTS.md §"Before declaring refuted": a (b) claim requires a proved
invariant, cited. Here it is.)

1. Every D-frame weight is **bar-EVEN** — proved in this corpus as
   `markovWeightsD_y21_barEven` / `markovWeightsD_y3_barEven`
   ([`MarkovWeightsConventionD.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/MarkovWeightsConventionD.lean)),
   and re-verified symbolically for n = 2..9 in the probe. Hence **any**
   function of the weight vector is bar-invariant.
2. `α` is not: `phaseTwice_bar_anomaly` gives `bar(α) + α = h²/2`, so `α` is
   bar-invariant **iff** `α = h²/4`, i.e. iff `2z − h = 2`.
3. Under D that fails. `2z_D − h − 2` has numerator `q⁴ − 2q³ − 2q + 1`
   (`zD_loopMean_sub_two_num`), which is **strictly negative on `[1,2]`**
   (`quartic_neg_on_Icc_one_two`), an interval containing the proton pin
   `q₀ ≈ 1.1099785827513808`. Value at q₀: **−2.4371**.

Lean: `phaseTwice_not_bar_fixed` (the core clash) and
`no_weight_function_gives_phase` (its reading), both sorry-free.
The hypothesis `2z − h ≠ 2` is **not decorative** — without it the two sides
coincide and a constant function would do.

> **This is the bean's "clean negative", and it is the answer to the question
> as posed.** No amount of work on the weight vector alone will produce `α`.

---

## 4. The positive half — what the weights DO determine

The exclusion is sharp, not total. `MarkovWeightsConventionD` already
concluded *"no quantity built from the D-frame weights alone carries a bar-odd
part … it must come from elsewhere (the `h` factor, the Kashiwara `f̃₁` shift,
or the framing) or not exist."* That is correct. What is added here is that
the source **is** the `h` factor, and that the weights **pin its multiplier**.

### 4a. The character collapse (`chi_sigma_collapse`)

`σ₁` acts on `V_λ` with eigenvalues `q` (multiplicity `m₊`) and `−q⁻¹`
(multiplicity `m₋`), so `χ_λ(σ₁) = q·m₊ − q⁻¹·m₋` and `f^λ = m₊ + m₋`. Then

```
2·χ_λ(σ₁) − h·f^λ  =  [2]_q · (m₊ − m₋)  =  [2]_q · χ^λ(τ)
```

where `χ^λ(τ)` is the **ordinary** `S_n` character at a transposition (the
`q → 1` value, where `σ₁ ↦ τ`). **This is where the bar-odd `h` cancels**: the
bar-odd half of the character is annihilated against `h·f^λ`, leaving the
bar-EVEN `[2]_q`.

### 4b. The loop-mean identity (`loopMean_eq_twoQ_mul_moment`)

Summing 4a against the two Markov conditions — `Σ f^λ y_λ = 1` and
`Σ χ_λ(σ₁) y_λ = z` — gives, over any finite index and in **any** convention:

```
2z − h  =  [2]_q · Ξ ,        Ξ := Σ_λ χ^λ(τ)·y_λ.
```

Both sides are bar-even, consistent with §3. `2z − h` is the **loop mean** —
the mean of the two Markov stabilisation loop values `z` and `z − h` — which
`LadderPhaseMirrorCovariance` §4 already identified as the unique
mirror-covariant projection of the phase.

### 4c. `Ξ` does not depend on `n` (`moment_independent_of_index`)

`2z − h` contains no `n`. So if two different `n` both satisfy 4b against the
same `q` and `z`, their moments coincide. **The `n`-independence is forced by
the identity, not observed across a table.**

Its value under D is `Ξ = (1+Q²)/(1+Q)² = (q⁴+1)/(q²+1)²` — at q₀,
**0.50540422650393080319**, the same for every `n ≥ 2`. Independently
confirmed for n = 2..9 by computing `Σ_λ χ^λ(τ)y_λ` from the actual weights
(check A4); by Frobenius `Σ_λ χ^λ(μ)s_λ = p_μ` with a transposition being
`μ = (2,1^{n−2})`, the numerator is `p₂(1,Q)·p₁(1,Q)^{n−2} = (1+Q²)(1+Q)^{n−2}`
against the normaliser `(1+Q)^n`.

> **Caveat against a tempting misreading.** At n = 3, `Ξ` coincides
> numerically with the single weight `y₍₃₎`. That is special to n = 3 —
> `χ^(2,1)(τ) = 0`, `y₍₁³₎ = 0`, and `[4]_Q = (1+Q)(1+Q²)`. It is **not** the
> case that `Ξ = y₍ₙ₎` in general.

### 4d. The phase (`phaseTwice_eq_moment_form`)

```
α  =  (h/4)·( [2]_q·Ξ + h − 2 )
```

`Ξ` and `[2]_q` are bar-even; the entire bar-odd content sits in the outer
`h`. So the phase is `h × (bar-even, pinned by the weights)` — which is why
§3 and §4 do not conflict: `h` is exactly the bar-odd datum the weights cannot
see, because `h` distinguishes `q` from `q⁻¹` and the weights do not.

---

## 5. Does the affine-in-`y₍₂,₁₎` shape survive? **No.**

The bean expected this to be the likely outcome. It is, and the reason is now
precise rather than merely observed.

Using `y₍₃₎ = 1 − 2y₍₂,₁₎` at n = 3, the phase superficially reads

```
α = (h/4)([2]_q + h − 2) − (h·[2]_q/2)·y₍₂,₁₎
```

— which *looks* affine, with the coefficient `−h·[2]_q/2` against the
retracted `−h/2`: the retracted formula dropped exactly one factor of `[2]_q`
(check A6). But that reading is wrong, because **`y₍₂,₁₎ = 1/[2]_q²`
exactly**, so `[2]_q = y₍₂,₁₎^{−1/2}` and the "coefficient" is itself a
function of `y`. Written in `y` alone:

```
α = (h/4)·( y^{−1/2} + h − 2 ) − (h/2)·y^{1/2}
```

— half-integer powers. **Not affine.**

The affine shape in the retracted formula was an artifact of the bogus
instance, in which `y₍₂,₁₎ := 1/2 − z` is affine in `z` **by construction**.
The real `y₍₂,₁₎` is quadratic-reciprocal in `[2]_q` while `z_D = q²/[2]_q`,
so the true relation carries a square root and cannot be affine.

---

## 6. Tiers

| Claim | Tier |
|---|---|
| `α = (z−1)h/2` is the ladder phase | **asserted** upstream — not derived here or anywhere |
| `chi_sigma_collapse` | **proved-lean**, sorry-free, generic `[Field F]` |
| `2z − h = [2]_q·Ξ` (any convention) | **proved-lean**, from the Markov *defining* conditions |
| `Ξ` independent of `n` | **proved-lean** (forced by the above) |
| `Ξ_D = (q⁴+1)/(q²+1)²` | **proved-lean** + symbolic-exact for n = 2..9 |
| `α` is not a function of the weights | **proved-lean**, scope-(b), invariant = bar-parity |
| exclusion non-vacuous at q₀ | **proved-lean** over `ℝ` on `[1,2]` |
| `y_λ = s_λ(1,Q)/(1+Q)^n` | **symbolic-exact**, 4.6e-61 against the live producer |

**A caveat on 4b.** It is an identity following from the Markov *defining*
conditions, so it is not an independent determination of `z` from the weights.
§3 proves no such determination exists. The content of 4b is that the specific
mirror-forced combination `2z − h` is `[2]_q` times a **weight functional**,
and 4c that the functional is `n`-free.

---

## 7. Anti-fit statement

Nothing here inverts an experimental Q_β. Production `c₃` is
`(Q_codata/Q_N2 − 1)/u³` — a CODATA inversion, and therefore **a fit in every
convention** — and is neither used nor computed. Every number in this document
is the value of an exact rational function of `q` at the substrate pin;
**change the experimental Q_β and not one of them moves.** No `c_k` is
extracted, no registry tier moves, no value is wired to production.

The derived `α_D = −0.0405` is *not* compared against experiment here, and
deliberately so: the comparison would require the `c_k` ladder, which is
convention-C-frame throughout and has **not** been re-derived under D
(bean `qou-cds1`). `decayLadder_zC_threeRow_ne_zero` makes the C-frame ladder
and the two-row forcing mutually exclusive, so substituting `z_D` into the old
ladder is not a valid move.

## 8. Scope — what is untouched

- No `c_k` value, tier, or wiring changes; the `qbeta-decay` channel stays
  `disputed` (bean `qou-b3nk`).
- Convention D remains canonical (owner ruling 2026-08-15). Nothing here
  reopens the convention question.
- Pin: proton / experimental, `q₀ ≈ 1.1099785827513808`, from the package
  constant `Q_50_DIGIT_STR` — never a witness, never a muon-built cache. No
  layer straddling.

## 9. Artifacts

| File | What |
|---|---|
| [`LadderPhaseFromWeights.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/LadderPhaseFromWeights.lean) | §3 + §4, generic `[Field F]`, sorry-free |
| [`LadderPhaseSubstratePin.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/LadderPhaseSubstratePin.lean) | the `ℝ` half (§7c split), sorry-free |
| [`qbeta_ladder_phase_from_wedderburn_weights.py`](../../computations/qbeta/qbeta_ladder_phase_from_wedderburn_weights.py) | checks A0–A6, exact over ℚ(q) |
| [`qbeta-ladder-phase-from-wedderburn-weights.json`](../../computations/qbeta/qbeta-ladder-phase-from-wedderburn-weights.json) | results |

**Verification** (CI is `workflow_dispatch`-only, so agent verification is the
gate): `lean`-direct **exit 0** on all four modules of the import cone against
the real Mathlib import cone; `#print axioms` clean
(`propext, Classical.choice, Quot.sound` only) on all **11** declarations;
`scripts/check-sidecars.sh` clean; `scripts/precision-gates.sh` **exit 0**,
*"All blocking precision gates green"* (its one `!!` advisory,
`qbeta_t4_stokes3_crux_probe.py:60 A_omega = 3`, is pre-existing and outside
this work's closure); probe `verdict: all-checks-pass`. The shared Mathlib
olean cache was verified at **6990 before and after** every build —
read-only, no `lake build` (bean `qou-r13s`).

`check-sidecars.sh` earned its keep here: the first draft put the `ℝ` lemma
in the generic file and it flagged the §7c mix, which is why there are two
Lean files rather than one.

## 10. What remains open

`qou-q2oa` is answered. What it does **not** close:

1. **The ansatz itself.** `α = (z−1)h/2` is still asserted. Deriving it — from
   the framing prefactor, the writhe, or the Yekutieli transport — is a
   separate and larger question.
2. **`qou-cds1` — the D-frame `c_k` ladder.** Untouched. §4d supplies the
   phase in weight terms, which is an *input* a re-derivation would need, not
   the re-derivation.
3. **Whether the ladder's phase should be `α` or its mirror-covariant
   projection `α − h²/4`.** `LadderPhaseMirrorCovariance` §4 argues the
   projection is forced by mirror covariance; §4d here gives both
   (`α − h²/4 = (h/4)([2]_q·Ξ − 2)`). Which one the decay channel actually
   carries is a question about the framing, not about the weights, and is not
   settled here.

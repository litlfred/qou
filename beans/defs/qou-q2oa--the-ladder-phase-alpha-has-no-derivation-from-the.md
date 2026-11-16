---
# qou-q2oa
title: The ladder phase alpha has no derivation from the actual Wedderburn weights
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T11:40:16Z
updated_at: 2026-11-16T17:56:00Z
parent: qou-wxhi
---

Parent tranche: `qou-cds1` (S1 — re-derive the Q_β `c_k` ladder under D).
This bean names **where the S1 wall actually sits** after PR #5187's
retraction; `qou-cds1` predates that finding and does not enumerate it.

## The claim

**There is no derivation of the ladder's phase `α` from the actual
Wedderburn weights — in either convention frame.**

Stated as the wall by PR #5187 (merged `fdd58a4f39`), verbatim:

> The D-frame weight vector is no longer open — S2 computed it, and
> `y_(1³) = 0` falls out. What *is* open is the **phase**: the relation
> `α = −h/4 − (h/2)·y_(2,1)` was read off the bogus instance, so **there is
> no derivation of the ladder's `α` from the actual Wedderburn weights in
> either frame.** That is the wall, and it is narrower and differently
> placed than this PR originally said.

## What was retracted, and why

The affine relation `α = −h/4 − (h/2)·y_(2,1)` was read off the vector
`(z, 1/2−z, z)`, which satisfies **only** the normalisation condition of
`CanonicalMarkovWeightsH3` and **fails** the other two Markov conditions
(h2/h3). It is therefore not a weight vector of `H₃(q)` at all, and
`1/2 − z_D` is simply not `y_(2,1)` — at `q ≈ 1.11` the two differ in sign
as well as magnitude (`−0.1127` vs `+0.2473`).

PR #5187 classes this as a **symbol-collision / claim-shape failure**: a
formula was given the name of an object whose defining conditions it does
not satisfy. A topic grep returned plenty and read as corroboration; the
skipped step was checking the defining conditions. (AGENTS.md §"Grep the
claim SHAPE, not only the topic".)

## The input now exists; the derivation does not

S2 solved the corpus's own three defining conditions for the `H₃(q)` Markov
weights at `z = z_D`:

| λ | rows | `y_λ` under D | sign for `q > 1` |
|---|---|---|---|
| `(3)`   | 1 | `(q⁴+1)/(q²+1)²` | positive |
| `(2,1)` | 2 | `q²/(q²+1)²`     | positive |
| `(1³)`  | 3 | `0`              | identically zero |

Signature `(5, 0, 1)` — positive semidefinite. So the D-frame weight vector
is **known**. What is missing is any argument connecting it to the ladder's
phase. The gap is a derivation, not a measurement.

## What survives and must not be re-broken

- **The Lean stands, renamed.** `1/2 − z_D < 0` for `q > 1` is true and was
  never in question; only the interpretation was wrong.
  `threeRowMiddleWeight*` → `ladderPhaseCoeff*`, so the names now describe
  what is actually proved. Sorry-free; `#print axioms` clean on all ten
  declarations.
- **`κ(z) = 1/2 − z` is an affine coefficient in one ansatz.** Its sign
  carries **no trace-positivity content.** Do not re-read a `κ` sign change
  as a statement about either trace.
- **Convention D does not fail positivity.** That scope-(b) structural
  exclusion was withdrawn — the invariant it cited (a negative Wedderburn
  weight) does not exist. The surviving statement is scope-**(a)**: the C
  ladder's phase formula does not transport to D by substituting the
  parameter.
- **`−974.43` is a sensitivity measurement, not a proposed value.** It is
  what the current extractor returns when fed `z_D`. Do not wire it
  anywhere. (Also recorded on `qou-cds1`.)

## What to do

1. Derive `α` from the weight vector above, or establish that it is not
   determined by the weights alone — a clean negative is a result here.
2. **Do not** re-read a relation off an instance without first checking it
   satisfies the defining conditions of the object it is named for. That is
   the exact failure this bean records; PR #5187's probe A7r exists to stop
   the specific conflation returning (asserts D weights PSD and
   `κ(z_D) = −0.1127 < 0 < 0.2473 = y_(2,1)`), but it guards one instance,
   not the habit.
3. Keep the anti-fit discipline: a phase obtained by inverting the Q_β
   anchor is a **fit**, must be labelled one, and may not be wired to
   production as canonical.

## Provenance

Filed 2026-08-16 from an agent that could not reach the `beans` CLI. All
quotations from PR #5187's merged body (`fdd58a4f39`, merged 2026-08-16);
the D weight table is S2's, PR #5185 §3bis, cited there rather than
re-derived.

---

## RESOLUTION (2026-08-21, PR #5353)

Both halves of item 1 are settled, and they are consistent. Audit:
`docs/audits/2026-08-21-ladder-phase-from-wedderburn-weights.md`.

**NEGATIVE — the clean negative this bean invited, and the answer as posed.**
`α` is **not a function of the weights**. Scope-(b) structural exclusion whose
named proved invariant is bar-parity: every D-frame weight is bar-EVEN
(`markovWeightsD_y21_barEven` / `_y3_barEven`, plus symbolic re-verification
for n = 2..9), so any function of them is bar-invariant; `α` is not, since
`bar(α) + α = h²/2` while `α ≠ h²/4`. Lean: `phaseTwice_not_bar_fixed`,
`no_weight_function_gives_phase`. Non-vacuous at the pin: the witness
`q⁴ − 2q³ − 2q + 1` is `−2.4371` at q₀ and `< 0` on all of `[1,2]`
(`quartic_neg_on_Icc_one_two`).

**POSITIVE — what the weights DO determine, once `h` is supplied.**

    2z − h = [2]_q · Ξ ,   Ξ := Σ_λ χ^λ(τ)·y_λ        (ANY convention)
    α      = (h/4)·( [2]_q·Ξ + h − 2 )

from `2χ_λ(σ₁) − h·f^λ = [2]_q·χ^λ(τ)` (`chi_sigma_collapse`) summed against
the two Markov conditions. **`Ξ` does not depend on `n`** — forced, because
`2z − h` contains no `n` (`moment_independent_of_index`). Under D,
`Ξ = (q⁴+1)/(q²+1)² = 0.50540422650393080319` at every `n ≥ 2` (Frobenius:
a transposition is `μ = (2,1^{n−2})`, so the numerator is
`p₂(1,Q)p₁(1,Q)^{n−2}`). Confirmed for n = 2..9 against the live producer.

The two halves agree because the bar-odd content is entirely the outer `h`,
which is exactly the datum the weights cannot see. This **refines** the prune
in `MarkovWeightsConventionD` ("it must come from elsewhere — the `h` factor,
…"): the source is the `h` factor, and the weights pin its multiplier.

**SHAPE — the affine form does NOT survive**, as this bean anticipated.
`y_(2,1) = 1/[2]_q²` exactly, so the apparent coefficient `−h·[2]_q/2` is
itself a function of `y`; in `y` alone the phase carries half-integer powers
`α = (h/4)(y^{−1/2} + h − 2) − (h/2)y^{1/2}`. The retracted formula's affine
shape was an artifact of the bogus instance, where `y_(2,1) := 1/2 − z` is
affine in `z` **by construction**. (It also dropped exactly one factor of
`[2]_q`.)

**Sharpening of the retraction, for the record.** The retracted formula was
**tautological**, not numerically wrong: fed its own bogus instance it returns
`α` *exactly* — both `−0.040485777340642764919` at the pin. So no arithmetic
check could ever have caught it; only checking the defining conditions could,
which is exactly the lesson item 2 records. It diverges only on the real
weight (`−0.0781` vs `−0.0405`).

**Item 3 (anti-fit) honoured.** No experimental Q_β is inverted; no `c_k` is
extracted; no tier moves; nothing is wired. Every number is an exact rational
function of `q` at the proton pin — change the experimental Q_β and none of
them moves. `α_D` is deliberately **not** compared against experiment, since
that needs the `c_k` ladder, which is C-frame and un-re-derived under D.

**Verification** (CI is dispatch-only): `lean`-direct exit 0 on all four
modules of the import cone; `#print axioms` clean on all 11 declarations;
`check-sidecars` clean; `precision-gates` exit 0, all blocking gates green;
mathlib oleans 6990 before and after (read-only, no `lake build`).

**Not closed by this** — see audit §10: the ansatz `α = (z−1)h/2` is still
asserted upstream and undrived; `qou-cds1` (the D-frame `c_k` ladder) is
untouched; and whether the decay channel carries `α` or its mirror-covariant
projection `α − h²/4` is a question about the framing, not the weights.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-21 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.



2026-11-15: moved under epic `qou-wxhi` (c_k ladder under convention D). Previous parent kept in history.


## Round 46 Update (2026-11-16 — PR `litlfred/qou#8142`)

- **Status**: `in-progress` (claimed and updated in Round 46; kept `in-progress` per strict non-closure rule).
- **Lean Formalization (`0` `sorry`, `#print axioms` clean)**:
  - Extended `folio/quantum-observable-universe/nuclear-interactions/q-beta-cos-resummation.lean` and `folio/quantum-observable-universe/lean/QOU/QBeta/DecayLadderConventionDPositivity.lean` with:
    - `wedderburnMiddleWeightD` and `wedderburnMiddleWeightD_pos`: for every $q > 1$, the actual Convention-D $H_3(q)$ middle Wedderburn weight $y_{(2,1)}(z_D) = q^2 / (q^2 + 1)^2 > 0$ is strictly positive;
    - `ladderPhaseCoeff_zD_eq` and `ladderPhaseCoeff_neg_at_zD`: $\kappa(z_D) = 1/2 - z_D = (1 + q^2 - 2 q^3) / (2(q^2 + 1)) < 0$ for every $q > 1$;
    - `ladderPhaseCoeff_ne_wedderburnMiddleWeight`: $\kappa(z_D) \neq y_{(2,1)}(z_D)$ for every $q > 1$;
    - `eigenphase_eq_affine_ladderPhaseCoeff`: $\alpha_D(q) = -h(q)/4 - (h(q)/2)\kappa(z_D)$;
    - `eigenphase_bar_sum_eq_half_heckeH_sq`: $\alpha_D(q^{-1}) + \alpha_D(q) = h(q)^2 / 2$;
    - `eigenphase_mirror_covariant_projection`, `eigenphase_mirror_covariant_projection_sub_harmonic`, and `eigenphase_mirror_covariant_projection_bar_odd`.
- **PR**: `https://github.com/litlfred/qou/pull/8142` (`7ba86df415ad231cf6e834adee99dcb383115c6d`).

# The surreal squeeze cannot decide algebraic independence — a formalize-first prune

**Date:** 2026-08-09
**Branch / PR:** `claude/algebraic-independence-obstruction-e8hiex` — [#4884](https://github.com/litlfred/qou/pull/4884)
**Lean:** [`QOU/Archimedean/SurrealGradingPrune.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SurrealGradingPrune.lean) (sorry-free, 7 declarations, `#print axioms` clean)

## The question

The corpus now carries substantial bounds/squeezing infrastructure — the
P-vs-NP budget bound, the q-Collatz drift bound, the q-NS blowup bound, and the
surreal blow-up calculus underneath all three. The standing conjecture
[`rem:yekutieli-transcendence-shadow`](../../content/quantum-observable-universe/predicted-spectra/yekutieli-transcendence-shadow.md)
asserts that `Vol(4₁)`, `Vol(5₂)`, `Vol(𝓑₃)` are algebraically independent over
`ℚ[q,q⁻¹]`, because a polynomial relation would force the Yekutieli obstruction
tower to close at finite height.

*Can the squeeze mechanism deliver that independence, the way it bounds NS
blowup?*

This is exactly the situation AGENTS.md §"Formalize-first probe discipline"
governs: before running a wide search over a hypothesis class, find the
invariant that prunes it and formalize that. The answer is **no**, and the
obstruction is structural.

## What the mechanism actually is

Every surreal bound in `appendix-surreals` runs on one engine
([`lem:surreal-squeeze`](../../content/quantum-observable-universe/appendix-surreals/surreal-squeeze.md)):
place a *cost* and a *budget* at different `ordω` grades and read off the
strict inequality. Both the q-Collatz and P-vs-NP remarks write it in exactly
this form:

> `ordω(δ² · Ω_q) = 1 > −3 = ordω(Δ_q)`  ⟹  `δ² · Ω_q > Δ_q`.

The soundness of that step — and the *only* property of `ordω` these arguments
use — is **grade dominance is archimedean-class dominance**: a strictly larger
grade means every standard multiple of the smaller element stays below the
larger. This is the Conway–Gonshor archimedean-class comparison. The Lean
structure `SqueezeGrading` has that single field and nothing else, so the prune
applies to *any* grading with this property, not to one particular `ordω`.

Note what the mechanism does **not** consume: `δ` enters only through its
grade, which is `0` for every nonzero standard real. The argument runs
identically for `δ = 1` and `δ = 10⁻¹⁰⁰`. That insensitivity is the source of
the obstruction.

## The obstruction

`ℝ` is a **single archimedean class**. The very property that makes dominance
sound therefore forces the grading to be *constant on the positive reals* —
derived in Lean, not assumed:

| Declaration | Statement |
|---|---|
| `not_infinitelySmaller_of_pos` | no positive real is infinitely smaller than any real (archimedean property — the cited invariant) |
| `grade_eq_of_pos` | ⟹ `g a = g b` for all positive reals `a, b` |
| `no_separation_of_standard` | the squeeze derives **no** strict inequality between two positive standard reals; the premise `g b < g a` is *false* |
| `nonvanishing_premise_circular` | under `ordω(0) = −∞`, `g 0 < g x ↔ x ≠ 0` |
| `grade_blind_to_rationality` | the grading cannot separate a rational from an irrational |
| `grade_aeval_const` | for `P, Q ∈ ℚ[x,y,z]` and any real `v`, non-vanishing values share one grade |
| `grade_separation_needs_nonstandard` | positive half — separation requires leaving the standard archimedean class |

Three independent readings of why the transfer fails:

**1. The grading is blind (the decisive one).** `Vol(4₁)`, `Vol(5₂)`,
`Vol(𝓑₃)` are standard reals, so for any `P ∈ ℚ[x,y,z]` the value `P(V)` is a
standard real and sits at grade `0` whenever it is nonzero. Writing the
conjecture as `ordω(P(V)) = 0` is a change of notation, not a step of the
proof: `nonvanishing_premise_circular` makes the circularity exact — the grade
premise that would certify `P(V) ≠ 0` is *logically equivalent* to `P(V) ≠ 0`.

**2. No height parameter.** Deriving `∀P ≠ 0, P(V) ≠ 0` from inequalities
requires a uniform bound `|P(V)| > Φ(deg P, H(P)) > 0` — a transcendence
measure, which is precisely the Nesterenko-type input the `.md` already names
as the missing tool. The squeeze has no slot for the height `H(P)`; it is not
merely a hard instance of the mechanism, it is type-mismatched to it.

**3. Quantifier mismatch.** The squeeze proves *one* inequality between two
named quantities. Algebraic independence is a countably infinite family of
non-vanishing claims, unbounded in degree and height.

**Sanity check on the strength of the claim.** `grade_blind_to_rationality`
gives a falsification test the mechanism also fails: the corpus's own ladder in
`HyperbolicVolumeTranscendence.lean` begins at `SingleVolumeIrrational`
(`Vol(4₁) ∉ ℚ`) — strictly weaker than independence, and a genuinely open
problem in the literature (Milnor's question on `Λ(π/3)`). A method that cannot
reach rung 1 will not reach rung 3.

## Why the NS/Collatz/P-vs-NP bounds are unaffected

`grade_separation_needs_nonstandard` is the positive half. Grade separation is
available *exactly* when a comparison leaves the standard archimedean class.
`Ω_q ≍ ε⁻¹` and `Δ_q ≍ ε³` sit at grades `+1` and `−3` — genuinely different
classes, so those uses are legitimate on this axis. `Vol(4₁)`, `Vol(5₂)`,
`Vol(𝓑₃)` and every `P(V)` sit at grade `0`. The volume target is outside the
mechanism's domain, not at a hard corner of it.

(This audit takes no position on the *other* premises of those three bounds —
the Reeb-period budget accounting, the non-compressibility conjecture, the
`std`-of-the-skein-resolution assumption. It addresses only the grade-separation
step they share.)

## Scope classification (AGENTS.md §"Before declaring refuted")

**Scope-(b) structural exclusion**, citing a proved invariant
(`not_infinitelySmaller_of_pos`), for the **narrow** claim:

> Grade separation alone cannot decide a polynomial relation among standard
> reals.

It is **not** a scope-(b) exclusion of surreal or non-Archimedean methods from
the algebraic-independence problem, and must not be cited as one. Specifically
untouched:

- A route that manufactures a genuinely **non-standard** object whose standard
  part is the relation — including the corpus's own
  `JetOrderIndependence` + effective-tower-height route.
- The **tower-height contrapositive** that
  `rem:yekutieli-transcendence-shadow` actually proposes: if a degree-`d`
  relation forces `κ_n` to close at height `h(d) < ∞`, perpetual obstruction
  gives a contradiction. That is a well-foundedness / effective-bound argument,
  **not** a squeeze, and it is where the corpus's bounds infrastructure could
  legitimately bite. Its open input is *effectivity* of `d ↦ h(d)`.
- Using the squeeze for its actual job in this neighbourhood: controlling the
  **error** in the volume-conjecture limit (a genuine grade separation, since
  the error is infinitesimal and `Vol` is not). That yields "the limit equals
  `Vol`", never "no polynomial relation".

## Related defect found and fixed

`JetOrderIndependence.lean` carried two global instances that discharged their
conjectures with no content — the same failure mode that file's own history
note records for `HyperbolicVolumeIndependence` on 2026-06-10, recurring one
class down. Both are removed per AGENTS.md §3b-tax ("do not fabricate a trivial
instance to close it"):

1. **`SurrealParallelTransportBound` — vacuous.** All three shadow functions
   were `fun _ => 0`, satisfying (I2) and (I3) by `rfl`. Since `transportShadow`
   is a class *field*, the instance chose the shadow it was supposed to
   constrain. This mattered directly here: the corpus *appeared* to carry a
   surreal bridge to `HyperbolicVolumeIndependence`, discharged for free.
   The two "PROVED" lemmas `transport_shadow_vanishes` /
   `transport_uniform_bound` are unaffected — they are honest statements about
   a *given* instance.
2. **`JetOrderIndependence` — fabricated data.** `ofPivots` was applied to
   `jetPivots = fun _ => (1/4, 2, 1/8)`, a constant extension of the order-3
   pivots to every order, thereby asserting the open conjecture. All genuine
   content is kept: `jetOrder3_certificate` (`∏ pivots = 1/16 ≠ 0`),
   `jetJacobianBase_rank = 3`, `eliminationDet_ne_zero`, `ofPivots`,
   `jacobianRank_eq_three_of_base`.

**Residual design defect (follow-up).** Removing the instance stops the free
discharge but does not make `SurrealParallelTransportBound` content-bearing —
a future instance may re-pick the zero functions. The shadows belong as class
*parameters*, which needs a Lean definition of the transport error.

## Verification (agent-owned; CI unavailable per AGENTS.md)

- `lean`-direct, real import cone, root `.lake` oleans restored from
  `lake-cache/qou-v4-24-0`:
  - `QOU/Archimedean/SurrealGradingPrune.lean` — exit 0, no warnings
  - `QOU/Archimedean/JetOrderIndependence.lean` — exit 0, no warnings
  - `QOU/Archimedean/HyperbolicVolumeIndependence.lean` — exit 0, one
    pre-existing documented §3b `sorry` (the open conjecture itself)
- `#print axioms` on all 7 new declarations:
  `[propext, Classical.choice, Quot.sound]` — no `sorryAx`.
- **Not** machine-verified: the `QOU.Archimedean` aggregator. The restored
  cache predates `QOU/Archimedean/PauliWitness.lean`, whose olean is absent, so
  `lean`-direct fails there before reaching the new import. Pre-existing
  sandbox gap, unrelated to this change; the added import is a one-line
  addition matching its neighbours.
- §7c base ring: `ℝ` is correct and load-bearing — the archimedean property of
  `ℝ` *is* the invariant being cited.

## Takeaway for future agents

Answering "can the squeeze do X?" reduces to one question: **do the two sides
of X sit in different archimedean classes?** If both are standard reals, the
answer is no, provably, and no amount of restructuring changes it. Reach for
the squeeze when a genuinely non-standard object is in play; reach for
effective bounds (heights, tower closure orders) when the target is arithmetic.

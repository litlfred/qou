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

## The one lift where a grade *does* become informative

The prune is about the volumes as **standard reals**. There is a precise sense
in which lifting them changes the picture, and it is worth stating because it
is the only place in this neighbourhood where the surreal formalism carries
real content.

Suppose each volume is realised as a surreal `Ṽᵢ ∈ **No**` with
`std(Ṽᵢ) = Vᵢ` — for instance the `q`-deformed volume as a function of the Reeb
infinitesimal `ε`, whose `ω`-expansion the framework could in principle compute.
Then for `P ∈ ℚ[x,y,z]`,

```
P(Ṽ) = P(V) + (infinitesimal corrections),
```

so `ordω(P(Ṽ)) = 0` when `P(V) ≠ 0`, and `ordω(P(Ṽ)) < 0` when `P(V) = 0`
(the standard part cancels and only the infinitesimal tail survives).
**At the lifted level the grade genuinely separates relation from
non-relation** — unlike at the standard level, where both live at grade `0`.

This does not evade the prune, and it is not a proof strategy on its own: to
*use* the criterion you must already know `ordω(P(Ṽ))`, which is
`nonvanishing_premise_circular` one level up. What it does is relocate the
problem to something the framework might actually have a handle on: instead of
"is this standard real zero?", the question becomes "does the `ω`-expansion of
the `q`-deformed volume triple have a negative-grade annihilator?" — a question
about a computable deformation, with the Yekutieli tower supplying the
expansion. A negative answer at every finite grade would be the perpetual-
obstruction statement in a form the squeeze's own machinery can express.

That is the productive reading of the user's intuition, and it is the route the
prune leaves open. Note it still needs the same effectivity input as the
tower-height contrapositive: a bound on which grades can be reached at a given
polynomial degree.

## The tower-height contrapositive, examined

The prune above kills the *squeeze* route. The corpus's other route is the
contrapositive in `rem:yekutieli-transcendence-shadow`: a relation forces the
tower to close at finite height, contradicting perpetual obstruction. Attacked
in [`QOU/Archimedean/TowerHeightAttack.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/TowerHeightAttack.lean)
(sorry-free, 7 declarations, axioms clean). Three results.

**1. The stated inference is invalid** (`relation_does_not_force_closure`,
`geomDecomp_relation`). `VolumeTowerDecomposition` is **ungraded** — its
content is `HasSum levelContribution totalVolume`, a convergent sum of reals.
A relation among the *totals* is therefore **one real equation**, and one
equation cannot force term-wise vanishing. Counterexample, over any brane
tower: `Φ_A(n) = (1/2)ⁿ` and `Φ_B(n) = 2·(1/3)ⁿ` have every level non-zero,
yet their totals `2` and `3` satisfy `3A − 2B = 0`. Linear relations are
polynomial relations, so the general step falls.

**2. Step 3 has no instance to run on** (`perpetual_excludes_baseline`). The
only concrete decompositions in the corpus — `volumeTowerDecomp_4_1`,
`volumeTowerDecomp_5_2`, `volumeTowerDecomp_B3` — are all
`baselineDecomposition`: `Φ₀ = Vol`, `Φ_n = 0` for `n ≥ 1`. That is a tower
closed at height `0`, the *opposite* of perpetual obstruction. Proved that no
`CSEvaluationFaithful` over a perpetual tower can use one. (The source flags
the baseline as trivial and promises a "REFINEMENT"; the refinement does not
exist.)

**3. The repair — and effectivity turns out to be free.** Suppose the
decomposition is **graded**: level `n` at `q`-grade `n`, with a relation over
`ℚ[q,q⁻¹]` holding grade by grade. Then a relation is one equation *per level*
rather than one in total, and everything the contrapositive wants follows:
`gradewise_determines_level` pins each level of one tower to the other's;
`gradewise_closure_propagates` transfers closure level-by-level; and
`recurrence_step` gives the general shape — a relation of `q`-degree `D`
convolves grade `k` of the relation with grade `n−k` of the tower, so the
grade-`n` equation is `Σ_{k≤D} c_k Φ_{n−k} = 0`, an **order-`D` linear
recurrence**. With `c₀ ≠ 0`, a vanishing window of width `D` closes the tower
forever (`closed_above_window`).

So **`h(P) = deg_q P`** — the height is read straight off the relation, no
arithmetic input required. The difficulty migrates entirely from *"bound the
height"* to *"grade the tower"*.

That is the same target the prune reaches from the other side:
`grade_separation_needs_nonstandard` says separation needs a non-standard
object, and a graded tower (level `n` at `ω`-grade `n`) is exactly one. **Both
routes converge on constructing the grading.**

Findings 1 and 2 are **scope-(a)**: statements about the *stated argument*,
not about the conjecture, which may well be true via a graded version of this
same route.

## Probe: how far does fibre-level independence actually go?

[`computations/jet_algebraic_independence_probe.py`](../../computations/jet_algebraic_independence_probe.py)
upgrades the corpus's *linear* jet certificate (rank-3 Jacobian at order 2) to
a *polynomial* one: is there a non-zero `P ∈ ℚ[x,y,z]` of degree `≤ d` with
`P(tr_M(4₁), tr_M(5₂), tr_M(𝓑₃)) = O(gᴺ⁺¹)`?

Exact throughout — rational power-series division, exact null space over `ℚ`,
no floats. The traces carry a framing `√q`, so the expansion is in `g = √q − 1`
rather than `h = q − 1`; since `h = 2g + g²` is a formal change of variable
with non-zero linear term, annihilators are preserved either way.

The test is only meaningful once the number of equations `N+1` reaches the
number of monomials `M = C(d+3,3)`; the probe sets `N = M + 8` and reports
both. Results are in `jet-algebraic-independence.witness.json`.

**Result — the relations exist, and the minimal degree is 7.** This corrects
the framing this probe was written under. All three traces are rational in
`u = √q` (numerator/denominator `u`-degrees 14/9, 16/9, 18/9), so all three lie
in `ℚ(u)`, which has **transcendence degree 1 over ℚ**. Any *two* elements of
such a field are already algebraically dependent — so a relation among the
three is **forced**. The probe therefore does not test *whether*; it measures
*where*:

| degree `d` | equations | null space | stable under 3× the equations? |
|---|---|---|---|
| ≤ 6 | 93 → 385 | `0` | yes — no relation |
| 7 | 129 → 421 | `3` | yes — **genuine**, 3-dimensional |

Positive control **PASS** (plants `z − x² + 2y`, recovers it). Stability is the
load-bearing check: adding equations can only raise the rank, so a dimension
surviving a large margin increase is not a truncation artifact.

**Consequence for the reduction.** `JetOrderIndependence` is a **rank**
certificate — *linear* independence of the jet coefficient vectors. The
series it certifies are *algebraically dependent*. So
`JetTransportImpliesIndependence` cannot be a transfer *of independence* from
the series to the volumes: the series-level algebraic independence it would
transfer is false. `TowerHeightAttack.linearIndependent_not_algebraicallyIndependent`
records the general reason in the cheapest form — `t`, `t²`, `t³` are linearly
independent yet satisfy `z = x·y`.

This does **not** refute `conj:hyperbolic-volume-transcendence`. The `q → 1`
jet of `tr_M` is not an expansion of `Vol(K)` — the volume lives in the
root-of-unity asymptotics — so dependence downstairs says nothing about
independence upstairs. What it does is remove one apparent route to it, and
sharpen what the bridge must actually do.

## Aligning with the Ramanujan / quantum-modularity side

Asked whether the Ramanujan-style `q`-series identities in the framework can be
aligned with this. They can, and more concretely than expected — **the corpus
already contains the graded object the tower attack says is missing.**

`docs/audits/2026-08-01-fibre-to-observable-bridge-verdict.md` §1a and
[`rem-ohtsuki-tower-bar-parity.md`](../../content/quantum-observable-universe/mass-theory/rem-ohtsuki-tower-bar-parity.md)
/ `OhtsukiTowerBarParity.lean` carry the Ohtsuki tower, Lean-scaffolded
sorry-free:

$$\mathfrak{V}_b = \mathfrak{V}_0 + \sum_{n\ge 1}\kappa_n\,(2\pi b^2)^n,
\qquad \kappa_n \in \mathbb{Q}(\sqrt 3)\cdot \pi^{\lceil n/2\rceil}.$$

Read against this audit:

* **This is the graded tower.** Level `n` sits at grade `n` in `ℏ = 2πb²`, with
  the complex volume at grade `0` and arithmetic coefficients above it. That is
  exactly the shape `TowerHeightAttack §3` requires and
  `VolumeTowerDecomposition` (a bare `HasSum`) does not supply.
* **It is also the surreal lift.** `𝔙 = Vol + (infinitesimal corrections)` is
  the `Ṽ` of the lifted-grade section above: `ord_ω(P(𝔙)) < 0` exactly when
  `P(Vol) = 0`. So a volume relation forces an infinite family of conditions on
  the `κ_n` — objects in a *known, computable* ring, not opaque reals.
* **Where Ramanujan enters.** The Kashaev invariant of `4₁` is the
  Kontsevich–Zagier strange series `F(q) = Σ (q;q)_n`, a false-theta object in
  the Ramanujan circle; `kashaev-surreal.md` already records that its Stokes
  constants are **integer `q`-series identified with 3d-index data** and, under
  the Fantini–Rella modular-resurgence template, are coefficients of an
  L-function. The Ramanujan-style identities are the arithmetic of the `κ_n`
  and the Stokes data — precisely the input needed to constrain the graded
  conditions.

So the alignment is: **squeeze/bounds → wrong tool (proved here); graded
Ohtsuki tower → right tool, already present; Ramanujan/quantum-modular
identities → the arithmetic that constrains its coefficients.** The corpus has
all three pieces and does not currently connect them to the independence
question — no file mentioning Ohtsuki also mentions
`hyperbolic-volume-transcendence`.

Honest limits: the `κ_n` live in a fixed number field times powers of `π`, and
`𝔙_0` is the *complex* volume (`Vol + i·CS`), so extracting a real-volume
relation from tower conditions is not automatic; and the Ohtsuki expansion is
per-knot at its own root of unity, so a *joint* graded object over the three
knots still has to be built. That construction is the live target (bean
`qou-5b23`), now with a named starting point rather than a blank page.

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

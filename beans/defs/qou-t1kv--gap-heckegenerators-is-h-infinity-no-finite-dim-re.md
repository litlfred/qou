---
# qou-t1kv
title: 'GAP: HeckeGenerators is H_infinity — Schur cascade (PROVED, #5766) blocks stdRep3; dim>1 IsJMWeight witness needs a bounded-index class variant'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T10:48:07Z
updated_at: 2026-11-18T08:43:19Z
parent: qou-59vq
---

## The defect

`QOU.BraidKnot.Hecke.HeckeGenerators` (HeckeJucysMurphyElements.lean:63) quantifies its
relations over **all** `i : ℕ`:

    hecke : ∀ i, σ i * σ i = algebraMap R A (q - q⁻¹) * σ i + 1
    braid : ∀ i, σ i * σ (i+1) * σ i = σ (i+1) * σ i * σ (i+1)
    far   : ∀ i j, i + 1 < j → σ i * σ j = σ j * σ i

That is the STABLE algebra H_∞(q). H_∞ has no nontrivial finite-dimensional
representations, so **no finite-dimensional rep can be an instance** — and therefore
`IsJMWeight` (HeckeSeminormalWeight.lean) cannot be discharged at `dim V_λ > 1`.

This is why the non-vacuity witness that shipped with #5746 is the ONE-DIMENSIONAL
`scalarGenerators`. That was not a choice of convenience; it is the only shape the class
admits.

## Padding does not work — checked, not assumed

The obvious workaround is to embed H_3 ⊂ H_∞ by padding σ_i for i ≥ 2 with a scalar `s`.
It fails at the boundary. Braid at i = 1 with σ_2 = s:

    LHS = σ_1 · s · σ_1 = s·σ_1²        RHS = s · σ_1 · s = s²·σ_1

so it needs `σ_1² = s·σ_1`. With the Hecke relation `σ_1² = (q−q⁻¹)σ_1 + 1` that becomes
`1 = (s − q + q⁻¹)·σ_1`, i.e. **σ_1 must be a scalar**. False in any rep of dim > 1.
So padding is not merely inelegant; it is inconsistent.

## What is already sitting there unused

`QOU/Archimedean/HeckeH3.lean` has **`stdRep3 : HeckeRep 3 2`** — the (2,1) representation
of H_3(q), dimension 2, with `stdRep3_hecke0`, `stdRep3_hecke1`, `stdRep3_braid` all PROVED
and packaged with `hecke_rel` / `braid_adj` / `braid_far`. It is exactly the multi-dimensional
instance needed, and it cannot be used because of the arity above.

Expected eigenvalues for λ = [2,1] at n = 3 (contents of (0,0),(0,1),(1,0) are 0, 1, −1;
two SYT): `L_0 = 1`; `L_1 = σ_0²` with the two Hecke roots squared, `q²` and `q⁻²`, matching
`q^{2·(+1)}` and `q^{2·(−1)}`. So the check is concrete and falsifiable.

## The fix

A bounded-index variant — relations required only for indices `< n−1`. `jmRaw H k` for
`k < n` touches only `σ_0 … σ_{n−2}`, so every theorem in the chain (`jmRaw_comm`,
`jmProd_eq_delta_pow`, `IsJMWeight`, `fullTwist_smul_eq_theta_sq`) goes through unchanged
on the bounded class. Then `stdRep3` instantiates it directly and the `dim > 1` gap closes
at n = 3 without any seminormal construction.

Estimated small: a class variant plus re-parameterising the existing proofs by the bound.

## Do NOT start a parallel Hecke seminormal form

See bean `sv8b` (priority HIGH) and `QOU/BraidKnot/JucysMurphy.lean` (830 lines, "brick 5
of the Okounkov–Vershik tower"): the corpus already has the CLASSICAL (q = 1) seminormal /
Gelfand–Zetlin construction with Specht modules, SYT adjacent-swap and entry-monotonicity
infrastructure, and three honestly-stubbed `sorry` + `-- Ref:` cores. `sv8b` has a
division of labour agreed on PR #4702. Building a second one from scratch would duplicate
mechanical, settled work — which the AGENTS.md overlap rule permits only for open-outcome
research, not for this.


---

## RETRACTED, same day, by me — "no finite-dim rep can instantiate it" is FALSE

The claim above is wrong and machine-refuted. Two counterexamples, the first of which was
already merged and axiom-checked **in the very file this bean cites**:

1. **`scalarGenerators : HeckeGenerators R R q`** (HeckeSeminormalWeight.lean). `A = R` is a
   finite-dimensional algebra — dimension 1. So a finite-dimensional instance not only can
   exist, one already shipped.
2. **Constant-σ, in ANY ring.** Take any `X` with `X * X = algebraMap (q − q⁻¹) * X + 1` and
   set `σ i = X` for every `i`. Braid degenerates to `X³ = X³` and far to `X² = X²`, both
   `rfl`. Verified: `constGenerators` compiles, `lean`-direct **exit 0**. So
   `Matrix (Fin 2) (Fin 2) R` carries an instance too.

I reasoned "H_∞ has no finite-dim reps" and did not check it against the instance I had
written myself an hour earlier. The estimate that followed from it — "hours, not
Wenzl-scale" — is retracted with it.

## The ACTUAL obstruction, stated correctly

It is not finite-dimensionality. It is that **`stdRep3` specifically does not extend to
H_∞**, and the mechanism is Schur, not dimension:

- `σ_0`, `σ_1` in the (2,1) rep are irreducible on `R²`, so together they generate all of
  `M_2(R)`.
- `far` forces `σ_3` to commute with **both** `σ_0` and `σ_1` (`0+1 < 3`, `1+1 < 3`), so by
  Schur `σ_3` is **scalar**, say `s`.
- `braid` at `i = 2` then gives `s·σ_2² = s²·σ_2`, so `σ_2² = s·σ_2`; with the Hecke
  relation that forces `σ_2` scalar too, say `t`.
- `braid` at `i = 1` then gives `t·σ_1² = t²·σ_1`, forcing **`σ_1` scalar** — contradicting
  2-dimensionality.

So the cascade runs downward from `σ_3` and kills the rep. That IS a real obstruction and it
does block using `stdRep3`. **This argument is reasoning, not machine-checked** — unlike the
refutation above. It should be Lean-proved before anyone relies on it, and it is a good
candidate for the formalize-first rule: prove the exclusion, then stop searching for the
instance.

## Revised estimate — NOT hours

The bounded-index class variant is still the right fix, but the cost was understated. Bounds
must be threaded through every lemma in the chain (~700 lines across eight files), and the
inductions in `run_push` / `delta_pow_run` carry indices up to `b + j + 1`, so the bound
bookkeeping is not mechanical. Call it a day of careful work with real risk of the bounds
failing to line up — not an afternoon.

Whether that is worth it for one `dim = 2` witness at `n = 3` is now a genuine question, and
I do not think the answer is obviously yes. `sv8b` may be the better use of the same effort.


---

## The Schur cascade is now MACHINE-CHECKED (2026-08-25, PR #5766)

The caveat above — *"This argument is reasoning, not machine-checked ... It should be
Lean-proved before anyone relies on it"* — is discharged. New library file
`QOU/BraidKnot/HeckeStableScalarCascade.lean`, 13 declarations, no `sorry`:

    sigma_eq_of_succ_scalar   sigma (i+1) = algebraMap s  ->  sigma i = THAT SAME s
    sigma_eq_of_le_of_scalar  downward propagation to every i <= j
    sigma_scalar_of_schur     Schur on {sigma 0, sigma 1}  ->  sigma 1 is scalar
    stdTwo_no_stable_extension   no HeckeGenerators restricts to the seminormal pair

`far` puts `sigma 3` in the centralizer of `sigma 0` and `sigma 1` (0+1<3, 1+1<3), Schur
makes it scalar, and the braid relation cascades down. **The obstruction is Schur, not
finite-dimensionality** — the retraction above stands and nothing in the proof leans on it.

Non-vacuity is carried, not assumed: the 2x2 Young seminormal pair is PROVED to satisfy
the Hecke and braid relations over any field with q != 0, and restated in the class's own
`algebraMap` vocabulary (`stdTwo_hecke0_algebraMap` / `stdTwo_hecke1_algebraMap`) so the
claim is literally the relation `HeckeGenerators.hecke` demands, not a `smul` lookalike.
Their joint centralizer is proved to be exactly the scalars.

Verified: `lean`-direct exit 0 against a cone built FROM SOURCE (8 QOU modules), and
`#print axioms` on all 13 declarations = [propext, Classical.choice, Quot.sound] — no
`sorryAx`. The container's root Mathlib cache is restored (oleans=6990, traces=0), the
state that yields phantom `sorryAx`, so `lake build` was never run.

### What this settles, and what it does NOT

SETTLED: the bounded-index class variant is not merely the tidier route to a `dim > 1`
witness — it is the ONLY one. This is a scope-(b) structural exclusion with a proved
invariant, so no cheaper instantiation exists to be found and nobody should look for one.

STILL OPEN — this bean stays open for it: the bounded-index refactor itself (~700 lines
across eight files, bounds threaded through `run_push` / `delta_pow_run`). The revised
"about a day, with real risk" estimate above is UNCHANGED; proving the exclusion does not
shrink the refactor, it only removes the possibility of avoiding it.

The cost question above — *"whether that is worth it for one dim=2 witness at n=3"* — is
now a cleaner decision: the alternative of finding some other instantiation is provably
empty, so the choice is the refactor or no `dim > 1` witness at all.


## SHARPNESS — the exclusion does NOT reach reducible reps (2026-08-25, #5766 d9deb89ac)

Raised from sibling PR #5764 (Sym2 gate), where an irrep-level exclusion was being read as
covering arbitrary objects. Answered with a proof, not a caveat:

    constGenerators                  any Hecke-quadratic unit gives an instance
    existsNonscalar_heckeGenerators  a HeckeGenerators on 2x2 matrices with
                                     NON-SCALAR generators: diag(q, -q^-1)

The load-bearing hypothesis of `sigma_scalar_of_schur` is the CENTRALIZER CONDITION, not
"irreducible" and not "dim > 1". A reducible rep has a non-scalar idempotent in its
centralizer, fails the hypothesis, and the cascade never reaches it. Needs q^2 != -1; at
q^2 = -1 the two Hecke eigenvalues collide and the diagonal is scalar.

**This directly re-refutes the claim this bean's title used to make.** `dim > 1` instances
DO exist, now by explicit construction in matrix form — so the retracted "no finite-dim rep
can instantiate it" is refuted a second time, and from the opposite direction (the first
refutation was `scalarGenerators`, dimension 1; this one is dimension 2 and non-scalar).
What H_infinity cannot host is an IRREDUCIBLE action, not a big one.

All 23 declarations re-checked: [propext, Classical.choice, Quot.sound], no sorryAx.


## BOUNDED CLASS BUILT + JM SPECTRAL HALF HAS ITS FIRST INSTANCE (2026-08-25, PR #5778)

    HeckeGeneratorsBelow R A q n   relations only for i + 1 < n
    stdTwoBelow3                   the 2-dim (2,1) rep AS AN INSTANCE at n = 3
    stdTwoBelow3_jm_content        L_k act on e0 = (1,0) by q^(2c), c = 0, 1, -1

At n = 3 the bounded class collapses to two Hecke-quadratic generators plus one
braid relation; far-commutation is VACUOUS (needs i+1 < j with j+1 < 3). All three
obligations were already proved by #5766, so the instance assumes nothing new. The
two results are exactly complementary: the unbounded class CANNOT admit this pair,
the bounded class DOES.

**The prize did not require the full port.** The eigenvalues q^0, q^2, q^-2 are
q^(2c) for the contents of (0,0), (0,1), (1,0) — the SYT [[1,2],[3]] on (2,1).
`HeckeJucysMurphyElements.lean` records the spectral half as "Untouched here. It
needs Young's seminormal form, which the corpus does not carry." It now has one
instance. ONE TABLEAU AT ONE n — not Young's theorem; the general-n statement is
exactly as open as before.

### Side finding: three fields of the UNBOUNDED class are redundant
`hecke_mul_sub_eq_one` / `sub_mul_hecke_eq_one` derive sigma^-1 = sigma - (q-q^-1)
from the Hecke relation alone (scalars are central; no invertibility hypothesis).
So `HeckeGenerators.sigma_inv` / `mul_sigma_inv` / `sigma_inv_mul` are derivable
data, not axioms. NOT changed in #5778 — removing them touches every downstream
instance. Worth a separate scoped pass.

### STILL OPEN — the ~1-day estimate is UNCHANGED
The full port (jmRaw_comm, jmProd_eq_delta_pow, fullTwist_smul_eq_theta_sq
re-proved on the bounded class, ~700 lines / 8 files) is NOT done. #5778 took the
minimum path to the dim>1 content-spectrum realisation, which turned out not to
need the general theory ported first. That port remains this bean's actual scope.


## THE PORT IS SUBSTANTIALLY DONE (2026-08-25, PR #5778, 4 files / 780 lines / 63 decls)

The dim>1 IsJMWeight witness THIS BEAN EXISTS FOR now exists:

    stdTwoBelow3_isJMWeight   e0 = (1,0) is a JM weight vector of the 2-dim (2,1)
                              rep of H_3(q), eigenvalues q^(2c), c = 0, 1, -1
    stdTwoBelow3_jmProd_eq_fullTwist   L_0 L_1 L_2 = (s0 s1)^3 on that same rep

Ported: HeckeGeneratorsBelow; the downcast + JM basics; delta/run/push law/power
identity/jmProd_eq_delta_pow; IsJMWeightB + jmProdB_smul_of_weight +
fullTwistB_smul_of_weight; HeckeGeneratorsBelow.map (transport along an AlgEquiv).

Architecture: the port GENERALIZES rather than forks. HeckeGenerators.toBelow
downcasts at every n and the *_toBelow lemmas show the constructions agree, so each
ported result RECOVERS its unbounded counterpart instead of copying it.

### CORRECTION to this bean's own estimate
"~700 lines across eight files" is wrong. Measured: the original cone is 1577
lines / 81 declarations across SIX files. The bounds claim was right though --
they are NOT uniform, and two of eight lemmas need no bound at all (they use no
Hecke/braid/far relation). The load-bearing arithmetic is that run_push's
induction reaches p+1 = m and braids there, needing m+2 < n, so both big
inductions carry m+1 < n, NOT the m < n a naive reading suggests.

### STILL OPEN -- this bean stays open
1. jmRaw_comm (JM commutativity). Its machinery is HeckeTranspositionExpansion
   (562 lines) + HeckeJucysMurphyCommutation (263) + AdjacentNormalForm (210).
   NOT attempted.
2. The theta / content-sum tie-in: prod_jmEigen, fullTwist_smul_eq_theta_sq,
   twist_scalar_eq_theta_sq. fullTwistB_smul_of_weight is the key half; the
   specialization to theta_lambda^2 is not ported.

### Side finding, unchanged and still unactioned
HeckeGenerators.sigma_inv / mul_sigma_inv / sigma_inv_mul are DERIVABLE from the
Hecke relation (hecke_mul_sub_eq_one). Removing them touches every downstream
instance -- wants its own scoped pass, not a rider on this one.


## THETA TIE-IN DONE (2026-08-25, PR #5786) -- only jmRaw_comm remains

    fullTwistB_smul_eq_theta_sq   twist acts by theta_lambda^2
    twistB_scalar_eq_theta_sq     that scalar is PINNED
    stdTwo_fullTwist_eq_one       (s0 s1)^3 = 1, direct matrix computation
    stdTwoBelow3_twist_eq_theta_sq   the routes agree

prod_jmEigen NEEDED NO PORT AT ALL -- it mentions no HeckeGenerators, being a
statement about the eigenvalue function and the combinatorics of `cells`. Only the
two theorems touching a presentation moved. Check what a lemma quantifies over
before assuming it needs redoing.

FALSIFIABILITY: c((2,1)) = 0+1-1 = 0, so theta^2 = 1 -- the full twist of B_3 is
PREDICTED to act trivially. Confirmed by an independent route: (s0 s1)^3 = 1 from
the matrices alone, no JM input. Same check HeckeSeminormalWeight runs for the
one-row block, now on a 2-dim block the unbounded class cannot host.

### REMAINING SCOPE OF THIS BEAN IS NOW EXACTLY ONE ITEM
jmRaw_comm (JM commutativity). Machinery: HeckeTranspositionExpansion (562) +
HeckeJucysMurphyCommutation (263) + HeckeJucysMurphyAdjacentNormalForm (210) =
~1035 lines. NOT attempted. Both headline results (the dim>1 IsJMWeight witness
and the twist) landed WITHOUT it, so whether it is worth porting is a genuine
open judgement call, not an obvious yes.


## jmRaw_comm PORTED — every item of this bean is now done (2026-08-25, PR #5791)

    jmRawB_comm              L_i L_k = L_k L_i for all i, k < n
    stdTwoBelow3_jmRaw_comm  ...on the 2-DIMENSIONAL (2,1) rep of H_3(q)
    jmRaw_comm_of_below      recovers the unbounded theorem via the downcast

634 lines / 35 decls / 3 files, all sorry-free.

### CORRECTION to my own scoping, twice over
I said "~1035 lines across three files". The chain is LINEAR and has FIVE files
(1305 lines) -- it also includes HeckeJucysMurphyReduction (115) and
HeckeAdditiveJucysMurphy (155). But the port needed only 634, because jmRaw_comm
is NOT proved directly: HeckeTranspositionExpansion identifies L_k = 1 + A_k and
does the work on the ADDITIVE side. HeckeJucysMurphyCommutation and
HeckeJucysMurphyReduction are an EARLIER, SUPERSEDED route (the one that stayed
conditional on the adjacent case) and are not on the path at all.

Surface larger than I said; work smaller. Trace the actual proof before quoting
either number.

### The bound findings
- FINAL BOUND IS THE NATURAL ONE: i < n and k < n, exactly the well-formedness
  condition for L_i. No slack -- the sign the bounds are right.
- sigma_comm_transpB_far bounds a DIFFERENT index than its statement's i (it is m,
  the outside generator, that must exist). A uniform i < n would be silently wrong.
- sigma_comm_partialSumB_ne is the only lemma needing TWO bounds; it splits on
  j < m vs j > m and the branches constrain different indices.
- SIX lemmas across the whole port need NO bound at all, including the sum
  expansion A_k = d.sum T_(i,k) -- the conceptual heart of Jucys's argument does
  not touch the Hecke presentation.

### THIS BEAN IS COMPLETE pending the merge of #5791
#5766 obstruction proved; #5778 bounded class + dim>1 IsJMWeight witness; #5786
theta tie-in; #5791 JM commutativity. Close on merge.


---

## Navigation note (2026-08-29) — read §SHARPNESS before the cascade paragraph above

The paragraph above ("The ACTUAL obstruction, stated correctly") ends *"forcing **σ_1 scalar** —
contradicting 2-dimensionality."* **That last clause is mine and it is too strong.** The cascade
contradicts **irreducibility**, not dimension.

The §SHARPNESS section further down says this correctly and proves it:
`existsNonscalar_heckeGenerators` exhibits a genuine `HeckeGenerators` instance on 2×2 matrices
with non-scalar generators, `σᵢ = diag(q, −q⁻¹)` — reducible, so it fails the Schur hypothesis
and the exclusion never reaches it. `dim > 1` instances exist. Machine-checked,
`[propext, Classical.choice, Quot.sound]`.

Both statements are left standing per the retract-visibly convention, but they sit ~75 lines
apart and a reader hitting the earlier one first gets the wrong claim. This pointer is here so
that does not happen.

Successors: `qou-0o6j` (bridge the arc onto the real H_n(q)), `qou-ayyi` (the `Quotient.lean`
header defect found while scoping it).

## 2026-09-08 — reopened: `status` disagreed with this bean's OWN body (§13a sweep, `qou-7sin`)

This bean was `completed` while the text above says, in its author's own words,
that the bean itself is still open. Nothing about its mathematics was judged
here and no finding was revisited — only the `status` field was made to agree
with the body.

Found by the `qou-7sin` sweep of the tracker against AGENTS.md **§13a** (owner,
2026-09-06: *"Don't close beans with open conjectures!!!"*), which landed after
most of these were closed. 18 of 2627 completed beans carry this
self-contradiction. It is decidable without judgement — the discriminator is
the bean asserting *its own* openness, not merely mentioning something open.

Re-close it when the work its body names is actually done.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- Round 75 (`lane-e667`): Formalized `qou-sh62`, `qou-ss88`, `qou-t1kv`, `qou-csgy`, `qou-fq1i` in `QOU.Foundations.CoordinationPeriodSeparationDisjointBlockFactorizationScalarCascadeQuadraticConventionBridgeInvolutionTrace` with 80-dps `mpmath` 2-commit witness stamp (`c9c8117f7aa28b67e2bf3a4e9b287ae17a2e5af6` -> `6d8ea219d4427f09f7950c85f1a067b42a3dd728`, `scriptHash=3a53f4d978a21ce6466ea7c8d24a6d3d41b356bea8717db46a8c42f512a4c41e`) in PR `litlfred/qou#8402` (`status: in-progress`).

---
# qou-argp
title: Argument principle on an annulus — the single missing lemma for the converse theta zero locus
status: completed
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T08:00:00Z
updated_at: 2026-11-20T08:27:17Z
parent: qou-c8p8
---

Split out of `qou-c1ln` row 2, which is otherwise closed. Everything the
converse zero locus needs is proved except one named lemma.

## Where it stands

`QOU/QBeta/C1ConnectionPoles.lean` proves, all sorry-free:

| | |
|---|---|
| `θ_p` holomorphic on `ℂ*` | `differentiableOn_qThetaC` |
| `θ_p(pw) = w·θ_p(w)` over `ℂ` | `qThetaC_functional_equation` |
| differentiated, and in log form | `deriv_…`, `logDeriv_qThetaC_functional_equation` |
| **the contour identity** | `qTheta_winding_step` |
| `θ_p(−p^k) = 0` | `qTheta_neg_zpow_eq_zero` |

`qTheta_winding_step` is `∮_{|z|=pρ} θ'/θ = 2πi + ∮_{|z|=ρ} θ'/θ` — the exact
form the argument principle consumes. What is missing is only the inference

> winding difference over an annulus = number of zeros inside, with multiplicity

after which: exactly one zero per fundamental annulus, `qTheta_neg_zpow_eq_zero`
supplies it at `−p^k`, so it is simple and the only one, so the zero set is
exactly `−p^ℤ` and the C1 pole divisor is exact rather than `⊇`.

Checked to hold at our substrate in `computations/qbeta/c3_w2_c1_theta_zero_count.py`
(5/5) — so this is a formalisation gap, not a mathematical doubt.

## What Mathlib has and lacks

**Lacks** (name scan at HEAD, 2026-08-07): `argumentPrinciple`, any
`windingNumber`, any complex residue (every `residue` hit is `IsLocalRing`),
`countZeros`.

**Has**: the full `circleIntegral` API including
`Complex.circleIntegral_eq_of_differentiable_on_annulus_off_countable` (annulus
Cauchy), `circleIntegral.integral_sub_center_inv` (`∮ (z−c)⁻¹ = 2πi`),
`circleIntegral.integral_add`, `circleIntegrable_sub_zpow_iff`,
`Analysis/Meromorphic/{Divisor, IsolatedZeros, Order}`, `AnalyticAt.order`,
`AnalyticOnNhd.deriv`. Plus, from this arc,
`C1ConnectionPoles.circleIntegral_scale` — change of variables for
`circleIntegral`, which Mathlib does not have at all.

## The decomposition, in the order to attempt it

1. ✅ **DONE 2026-08-08 — argument principle GIVEN a factorisation.** If `f = (∏_j (z − a_j)^{m_j}) · u` on a neighbourhood of the closed
   annulus with `u` holomorphic and non-vanishing there, then
   `(1/2πi)[∮_R − ∮_ρ] f'/f = Σ_j m_j·[ρ < |a_j| < R]`. Every ingredient exists:
   `logDeriv_mul` / `logDeriv_prod` split the integrand; `u'/u` is holomorphic on
   the annulus so its two circle integrals agree by the annulus Cauchy theorem;
   each `(z − a_j)⁻¹` contributes `2πi` when `|a_j| < R` (ball case) and `0` when
   `|a_j| > R` (holomorphic in the disc). `argumentPrinciple_annulus_single` in `C1ConnectionPoles.lean`: for
   `f = (·−a)^m·u` with `u` analytic and non-vanishing on an open `A` containing
   the closed annulus, and `r < ‖a‖ < R`,

       ∮_{|z|=R} f'/f − ∮_{|z|=r} f'/f = m·2πi.

   Supporting lemmas, all `θ`-free and upstreamable: `integral_inv_sub_inside`
   (`∮(z−a)⁻¹ = 2πi` inside), `integral_inv_sub_outside` (`= 0` outside),
   `logDeriv_pow_sub_mul` (the split `m/(z−a) + u'/u`). All sorry-free,
   `[propext, Classical.choice, Quot.sound]`.

   **And the payoff is proved**: `multiplicity_eq_one_of_winding_step` composes
   it with `qTheta_winding_step` (winding difference `= 2πi`) to force `m = 1`.
   So *conditional only on the factorisation existing*, the zero in each
   fundamental annulus is **simple**, and with `qTheta_neg_zpow_eq_zero` it is
   `−p^k` and there is no other. The converse zero locus now hangs on step 2 and
   on nothing else.
2. **Existence of the factorisation** — *see the 2026-08-08 revision below;
   Mathlib appears to have this already and my earlier scan missed it.* Zeros of
   a non-identically-zero holomorphic function on a compact annulus are finite
   (`AnalyticOnNhd` + isolated zeros + compactness), each has a finite order
   (`AnalyticAt.order`), and dividing them out leaves a non-vanishing
   holomorphic factor.
3. **Assemble** into the annulus argument principle, then apply to `θ_p`.

## Honest cost — revised after doing (1)

(1) took one session, as estimated, and is landed. (3) collapsed into it:
`multiplicity_eq_one_of_winding_step` already performs the assembly, so there is
no separate step 3 left.

**Everything now rests on (2) alone**: given `θ_P` holomorphic and not
identically zero on a neighbourhood of a closed annulus, produce
`θ_P = (·−a)^m·u` there with `u` analytic and non-vanishing. Mathlib has the
single-point factorisation (`AnalyticAt.order`, `IsolatedZeros`); what is
missing is the global-on-a-compact-set version — finitely many zeros by
compactness plus discreteness, then divide them all out. That is the
multi-session, upstreamable piece, and it is now the *only* thing between this
corpus and an exact C1 pole divisor.

## What it unlocks

The converse zero locus, hence an exact C1 pole divisor. Note `qou-c1wr`
established that **nothing consumes the divisor** — so this is worth doing for
the Mathlib contribution and for closing a named gap honestly, not because a
downstream number depends on it. Do not let it displace work that is consumed.

Relates: `qou-c1ln` (row 2), `qou-c1wr`, `qou-wgnx`.

## 2026-08-08 — step 2 is probably NOT a gap; my scan was looking for the wrong names

Reading the Mathlib source on disk (`/workspace/leanprover-community/mathlib4`,
rev `ac10dc7`) turns up all three of the things this bean calls missing:

| what step 2/3 needs | Mathlib declaration |
|---|---|
| finitely many zeros on a compact set | `MeromorphicOn.divisor_support_finite_of_subset (hf : MeromorphicOn f U) (hU : IsCompact U) (hV : V ⊆ U) : (divisor f V).support.Finite` |
| **the global factorisation** | `MeromorphicOn.extract_zeros_poles` — `f =ᶠ[codiscreteWithin U] (∏ᶠ u, (· - u) ^ divisor f U u) • g` with `g` analytic and nowhere zero on `U` |
| finset linearity of the circle integral | `circleIntegral.integral_fun_sum` |

`Mathlib/Analysis/Meromorphic/FactorizedRational.lean` is the file, and
`Mathlib/Topology/LocallyFinsupp.lean` carries the `finiteSupport`-on-compact
lemma underneath it.

**This is a correction, not a Mathlib update.** The scan recorded above searched
for `argumentPrinciple`, `windingNumber`, `residue`, `countZeros` — and
`extract_zeros_poles` is none of those. The negative result was real for the
*argument principle*; it was never evidence about the *factorisation*. I should
have searched by what the statement says, not by what the theorem is called.

I could not verify whether the pinned revision has them: the checkout on disk is
shallow, `f897ebcf` (the `lakefile.toml` pin) is not among its objects, and the
`.lake/packages/mathlib` directory is empty in this container, so nothing Lean
can be compiled here to check. **Confirm against the pin before planning around
this.** If the pin predates them, this becomes a version-bump question, which is
a corpus-wide re-verification and a much bigger decision than one lemma.

## The route, if step 2 is available

1. `K := closedBall 0 R' \ ball 0 r'` with `0 < r' < r < R < R'` — compact, and
   contained in `ℂ*`, so `θ_P` is analytic hence `MeromorphicOn` on it.
2. `V := ball 0 R' \ closedBall 0 r'` — open, connected, `V ⊆ K`, contains the
   closed annulus between `r` and `R`.
3. `divisor_support_finite_of_subset` gives `(divisor θ V).support.Finite`.
4. `extract_zeros_poles` gives `θ =ᶠ[codiscreteWithin V] (∏ᶠ u, (·-u)^m_u) • g`.
5. **Upgrade the codiscrete equality to genuine equality on `V`.** Both sides are
   analytic there — `θ` by hypothesis, the RHS because `θ` has no poles so the
   divisor is `≥ 0` — and `V` is connected, so the identity theorem applies.
   *This is the step to cost first; it is the one that is not a citation.*
6. `logDeriv_prod` + `circleIntegral.integral_fun_sum` + the existing
   `integral_inv_sub_inside` / `integral_inv_sub_outside` / annulus-Cauchy
   lemmas turn (4) into `Σ_u m_u` over the zeros between the two circles.
7. `qTheta_winding_step` says that sum is `1`. Since `qTheta_neg_zpow_eq_zero`
   puts `−p^k` in the annulus with `m ≥ 1`, the sum being `1` forces: exactly one
   zero, simple, equal to `−p^k`. **That is the converse zero locus.**

Steps 1–4 and 6 are citations. Step 5 is the only real work, and it is a
standard identity-theorem argument rather than a new theory. So the honest cost
above ("multi-session, upstreamable") is **too pessimistic** if the pin carries
these — revise to one session, contingent on that check.

Unchanged: `qou-c1wr` established that nothing downstream consumes the divisor.
This is worth doing to close a named gap honestly, not because a number depends
on it. Do not let it displace consumed work.

## 2026-08-08 — claim released; still open

The branch that held this (`claude/c1-theta-canonical-solutions-2026-08-07`)
merged as #4672. Step 1 is landed and sorry-free; **step 2 is unstarted**, and
the correction above stands: Mathlib appears to carry the factorisation already
under names the original scan never searched for. Whether the *pinned* revision
has them is still unverified — that check is the first thing to do, and it is
cheap.

Unclaimed. Status moved `in-progress` → `todo` so a sibling does not read it as
actively held.

## 2026-08-08 — TWO corrections. The gap was smaller than this bean has ever said.

Both are the same error: recording something as missing without checking whether
it already exists, then planning around the record.

**1. The pinned Mathlib carries what the previous entry hoped it might.**
Verified directly against `.lake/packages/mathlib` at `f897ebcf`, not against a
newer checkout:

| | at the pin |
|---|---|
| `MeromorphicOn.extract_zeros_poles` | **present** |
| `Function.locallyFinsuppWithin.finiteSupport` (compact ⇒ finite support) | **present** |
| `intervalIntegral.integral_finset_sum` | **present** |
| `CircleIntegrable.sum`, `circleIntegral.integral_add`, `integral_sub_inv_of_mem_ball`, annulus Cauchy, `AnalyticOnNhd.deriv` | **present** |
| `MeromorphicOn.divisor_support_finite_of_subset` | absent — *four-line wrapper*, now proved |
| `circleIntegral.integral_fun_sum` | absent — *four-line proof*, now proved |

Both absentees are in `QOU/Mathlib/CircleIntegralFinsetSum.lean`, sorry-free,
stated in Mathlib's own shape so a pin bump deletes the file rather than
requiring a rewrite. The earlier note guessed `finiteSupport` was missing; the
grep failed only because it is declared inside a namespace.

**2. The corpus already has a sorry-free argument principle.**
`QOU/Mathlib/ArgumentPrinciple.lean` — 687 lines, bean `qou-bmyx`, verified
`exit 0` — proves `argument_principle` on a **closed disc**, global, via
Weierstrass factorization, plus `entire_zero_count`. This bean has said "Mathlib
has no argument principle" since it was opened. True, and irrelevant: the
*corpus* has one, in a file of that name, from a bean that appears in the same
`beans list` output this one does.

**What is actually left**, and it is not step 2:

`argument_principle` is on a disc. `θ_p` is holomorphic on `ℂ*` but has an
essential singularity at `0`, so the disc form does not apply to it — the
annulus form does, and that is `argumentPrinciple_annulus_single` in
`C1ConnectionPoles.lean`, which is proved *for a single factor*. The remaining
work is therefore:

1. **`Finset`-index the annulus statement** — now unblocked: `integral_fun_sum`
   splits the contour integral over the factors, `divisor_support_finite_of_subset`
   makes the index set a `Finset`, `logDeriv_prod` splits the integrand.
2. ~~**Upgrade `extract_zeros_poles`'s codiscrete equality to genuine
   equality**~~ — **DONE**, same day. `eqOn_of_eventuallyEq_codiscreteWithin`
   in `QOU/Mathlib/CircleIntegralFinsetSum.lean`, sorry-free. Six lines: Mathlib's
   `eqOn_or_eventually_ne_of_preconnected` gives *either* `EqOn f g U` *or*
   `f ≠ g` codiscretely; the second contradicts the hypothesis on a non-trivial
   filter. `codiscreteWithin_neBot` supplies that non-triviality for a nonempty
   open set — without it the lemma would have been vacuous, which is worth
   stating since Mathlib has no `NeBot` instance for `codiscreteWithin` at the
   pin.
3. Apply to `θ_p` with `qTheta_winding_step`, which already gives winding
   difference `= 1`, forcing exactly one simple zero per fundamental annulus.

Revised cost: **one session**, not multi-session, and not blocked on Mathlib.

**Method note.** Twice now the fix was to search by what the statement *says*
rather than what the theorem is *called* — `extract_zeros_poles` is not named
"factorisation", and the corpus's own argument principle was never going to
answer a grep for `windingNumber`. Before recording anything as missing here,
grep the corpus as well as Mathlib.

## 2026-08-08 (later) — step 2 is done; only the assembly is left

The step this bean called "the one that is not a citation" is proved. All four
supporting lemmas now sit sorry-free in
`QOU/Mathlib/CircleIntegralFinsetSum.lean`:

| | |
|---|---|
| `integral_fun_sum` | circle integral over a `Finset` sum |
| `divisor_support_finite_of_subset` | finitely many zeros/poles on a compact set |
| `eqOn_of_eventuallyEq_codiscreteWithin` | codiscrete equality ⇒ equality, via the identity theorem |
| `codiscreteWithin_neBot` | the above is not vacuous on a nonempty open set |

**What is left is assembly, not new mathematics.** Take `V` the open annulus,
`K` a slightly larger closed one; `divisor_support_finite_of_subset` makes the
zero set a `Finset`; `extract_zeros_poles` factors `θ_P` there;
`eqOn_of_eventuallyEq_codiscreteWithin` turns that into genuine equality;
`logDeriv_prod` and `integral_fun_sum` split the contour integral;
`argumentPrinciple_annulus_single` handles each factor; `qTheta_winding_step`
pins the total at `1`, forcing one simple zero per fundamental annulus, which
`qTheta_neg_zpow_eq_zero` identifies as `−p^k`.

That is the converse zero locus, and hence an exact C1 pole divisor. Estimate:
part of a session. Note `qou-c1wr`'s finding still stands — **nothing downstream
consumes the divisor**, so this is worth finishing for the Mathlib contribution
and to close a named gap honestly, not because a number depends on it.

## 2026-08-08 — the annulus argument principle is `Finset`-indexed and proved

`argumentPrinciple_annulus_finset` in `C1ConnectionPoles.lean`, sorry-free. For
`F = (∏ a ∈ S, (·−a)^{m a})·u` with `u` analytic and non-vanishing on a
neighbourhood of the closed annulus and every `a ∈ S` strictly inside it, the
winding difference is `(∑ a ∈ S, m a)·2πi`. With it,
`logDeriv_prod_pow_sub_mul` — the pointwise split, via Mathlib's
`logDeriv_prod`.

That was the step this bean called "assembly, not new mathematics", and it was:
every ingredient existed, the work was matching their shapes. Two of the three
compile errors were function-valued versus pointwise `Finset` sums
(`∑ i ∈ S, fun z => f i z` against `fun z => ∑ i ∈ S, f i z`), which needed an
explicit `funext` bridge — `simpa [Finset.sum_apply]` does not cross it.

**Everything the converse zero locus needs is now proved.** What remains is to
instantiate it for `θ_P`:

* `V` the open annulus, `K` a slightly larger closed one;
* `divisor_support_finite_of_subset` makes the zero set of `θ_P` on `V` a
  `Finset`;
* `extract_zeros_poles` factors `θ_P` as `(∏ (·−a)^{m a})·g` modulo a
  codiscrete set;
* `eqOn_of_eventuallyEq_codiscreteWithin` makes that equality genuine on `V`
  (both sides analytic, `V` connected);
* `argumentPrinciple_annulus_finset` gives `∑ m a` as the winding difference;
* `qTheta_winding_step` says that difference is `1`, so `∑ m a = 1`;
* `qTheta_neg_zpow_eq_zero` puts a zero at `−p^k`, so `S = {−p^k}` and `m = 1`.

That last step is bookkeeping over a one-element `Finset`, not analysis.

Still true, and still the reason not to rush it: `qou-c1wr` established that
**nothing downstream consumes the divisor**.

## 2026-08-08 — the chain is complete; only θ-specific instantiation is left

`exists_finset_factorisation` closes the last general gap: an analytic function
on a relatively compact, connected open `V` factorises as
`(∏ a ∈ S, (·−a)^{m a})·g` with `g` analytic and non-vanishing, *as genuine
equality on `V`*, in exactly the shape `argumentPrinciple_annulus_finset`
consumes.

Assembled from the four earlier lemmas plus `finprod_zpow_eq_finset_prod_npow`,
which normalises `extract_zeros_poles`'s output: that theorem returns a
`finprod` of **functions** with **ℤ** exponents, and the argument principle
takes a `Finset.prod` of **values** with **ℕ** exponents. Three conversions:
`finprod_apply` (functions → pointwise), `finprod_eq_prod_of_mulSupport_subset`
(finprod → Finset.prod), and `zpow_natCast` under
`AnalyticOnNhd.divisor_nonneg` (ℤ → ℕ, valid because an analytic function has
no poles).

**Every general ingredient is now proved.** What remains is θ-specific:
instantiate `V` as the open annulus and `K` as a slightly larger closed one,
check `meromorphicOrderAt θ_P u ≠ ⊤` (θ_P is not locally zero — it has a zero at
`−p^k` and is analytic, so this is the identity theorem again), feed the result
through `argumentPrinciple_annulus_finset`, and equate with
`qTheta_winding_step`'s `2πi`. That gives `∑ m a = 1`, and
`qTheta_neg_zpow_eq_zero` names the one zero.

### The recurring papercut, recorded because it cost three iterations

Lean distinguishes `∑ i ∈ S, fun z => f i z` from `fun z => ∑ i ∈ S, f i z`,
and `∏ᶠ i, f i` from `fun z => ∏ᶠ i, f i z`. Three separate errors in this arc
were that distinction and nothing else. `simpa [Finset.sum_apply]` does **not**
cross it — the bridges are an explicit `funext` for `Finset`, and
`finprod_apply` (which needs a finiteness hypothesis) for `finprod`. Mathlib
often ships both forms, e.g. `DifferentiableAt.finset_prod` versus
`DifferentiableAt.fun_finset_prod`; reach for the `fun_` variant first.


## 2026-08-08 — claimed for the θ-specific instantiation

Branch `claude/c1-theta-zero-locus-instantiation-2026-08-08`. Working the last
item: instantiate the general chain for `θ_P`.

One thing the plan above glosses. `exists_finset_factorisation` produces `g`
analytic on the **open** `V`, but `argumentPrinciple_annulus_finset` wants `u`
non-vanishing on an open set containing the **closed** contour annulus — so `V`
must be strictly larger than the contours, and then `S` can contain zeros in the
two collars, which violates that theorem's `∀ a ∈ S, r < ‖a‖ < R`.

Two ways out: prove no zeros sit in a thin enough collar (needs a
positive-distance argument against a finite set), or drop the hypothesis to
`‖a‖ ≠ r, R` and count with a filter. The second is strictly more general, is
the honest statement of the argument principle, and needs no collar at all —
taking it.

## 2026-08-08 — DONE. The converse zero locus is proved.

`qThetaC_eq_zero_iff` in `QOU/QBeta/C1ThetaZeroLocus.lean`:

    for w ≠ 0,  θ_P(w) = 0  ↔  ∃ k : ℤ, w = −P^{2k}

and `qThetaC_analyticOrderAt_neg_zpow`: every such zero has
`analyticOrderAt = 1`. Together that is the **whole divisor of `θ_P` on `ℂ*`** —
the orbit `−p^ℤ`, reduced — so the three C1 pole loci are exact and carry
multiplicity one rather than being containments. Sorry-free,
`[propext, Classical.choice, Quot.sound]`.

No hypothesis survives except `w ≠ 0`, and that only because `0` is an essential
singularity where `θ_P` is not an analytic object at all.

### What the plan above got wrong, and it is the same error a third time

The plan said the remaining work was "θ-specific instantiation, bookkeeping over
a one-element `Finset`, not analysis". Two of the three things that actually
blocked it were neither:

1. **The strict-between hypothesis is undischargeable here.**
   `argumentPrinciple_annulus_finset` requires `r < ‖a‖ < R` for *every* factor.
   But `exists_finset_factorisation` produces a factorisation analytic on an
   **open** set, which must therefore be strictly larger than the closed contour
   annulus — and its zero set can then sit in the two collars. Discharging the
   hypothesis would need a positive-distance argument against a finite set,
   *before* knowing the set is finite in the relevant sense.
   Fix: `argumentPrinciple_annulus_filter`, which asks only that factors avoid
   the two circles and counts with a filter. A factor inside the inner circle
   contributes `2πi` to both integrals and cancels; one outside contributes to
   neither. Strictly more general, and the honest statement of the theorem. The
   old form is now a two-line corollary.

2. **`a ∈ S` carried no information.** `exists_finset_factorisation` returned
   `S` and `m` with nothing tying them to `θ`. Reading "`a` is a zero" off
   membership needs `0 < m a` *and* `S ⊆ V`; reading multiplicity off it needs
   `analyticOrderAt f a = m a`. All three added
   (`analyticOrderAt_eq_of_finset_factorisation` is the last, and is general).

The genuinely θ-specific pieces were smaller than either:

| | |
|---|---|
| `isPreconnected_openAnnulus` | an annulus is `exp` of a convex strip — the identity theorem wants a connected domain, and Mathlib has nothing about annuli |
| `qThetaC_ne_zero_outer` | `θ(P²w) = w·θ(w)` carries non-vanishing from `‖z‖ = ρ` out to `‖z‖ = P²ρ`, so `qTheta_winding_step`'s single hypothesis cleans both contours |
| `qTheta_pos_of_pos` | every term of `∑ P^{−n(n+1)}wⁿ` is positive for `w > 0` — the cheapest proof that `θ` is not identically zero |
| `qThetaC_ofReal` | the bridge real facts cross to reach the complex statements; unconditional, `Complex.ofReal_tsum` needs no summability |
| `exists_clean_radius` | only finitely many radii carry a zero, and an interval of reals is infinite |

`exists_clean_radius` is what removed the hypotheses. `qTheta_winding_step` has
always needed "no zero on `‖z‖ = ρ`", and every downstream statement inherited
it. That is not a restriction — it is a *choice*, and this lemma is the proof.
With it, `⌊logb (P²) ‖w‖⌋` places any `w` in a fundamental annulus and a clean
contour goes just below the lattice point, in an interval that is nonempty
exactly because `‖w‖ < P^{2k+2}`.

### Consumer status — unchanged, and worth repeating

`qou-c1wr` established that **nothing downstream consumes the divisor**. This
was worth finishing to close a named gap honestly and for the upstreamable
lemmas (`argumentPrinciple_annulus_filter`,
`analyticOrderAt_eq_of_finset_factorisation`,
`exists_finset_factorisation`, `isPreconnected_openAnnulus`, and the two Mathlib
wrappers), not because a number moved.

Content updated in the same pass: `prop:c1-theta-zero-locus-and-pole-divisor`
no longer says the converse is unproved, its `lean.ref` points at
`qThetaC_eq_zero_iff`, and the stale "Mathlib has no argument principle"
docstrings in `C1ConnectionPoles.lean` are gone.

Closing.

### Progress Update (2026-11-17, Round 60 — lane-e667)
- **PR:** `litlfred/qou#8299` (`https://github.com/litlfred/qou/pull/8299`), head `7794a07bbdcd4212b670d7ed777098efe60dc9a4` (`COMMIT1 = a21b136d3f122bac6df50bab417b7232ca55064f`), labeled `ready-to-merge` + `release`, `ready: 7794a07bbdcd4212b670d7ed777098efe60dc9a4` (`https://github.com/litlfred/qou/pull/8299#issuecomment-6945265144`).
- **Lean 4.24.0 Module:** `folio/quantum-observable-universe/lean/QOU/Foundations/AnnulusWindingLogCountingLieCurvatureHemisphereInversionZAxisBound.lean` (wired into `QOU.lean`; `0` `sorry`, `0` `axiom`, `0` warnings, `0` CRITICAL/major/advisory across all 6 static vacuity & borrowed-name audits):
  - `qou-argp`: `annulus_winding_step_and_single_zero_uniqueness`.
  - `qou-bp5n`: `radial_log_counting_decomposition_and_increment`.
  - `qou-ghc6`: `matrix_one_form_commutator_trace_and_flat_curvature`.
  - `qou-h2mb`: `hemisphere_inversion_radial_reversal_and_tangential_fix`.
  - `qou-i0sr`: `vertical_step_energy_dominance_and_telescoping_bound`.
- **80-dps Probe & 2-Commit Witness:** `computations/probes/annulus_winding_log_counting_lie_curvature_hemisphere_inversion_z_axis_bound_probe.py` + `computations/probes/annulus-winding-log-counting-lie-curvature-hemisphere-inversion-z-axis-bound.witness.json` (`scriptHash = 001b12183bba`, `scriptCommitSha = a21b136d3f122bac6df50bab417b7232ca55064f`, `allPassed = True`).
- **Adversarial Cross-Review (Round 60):** Verified `litlfred/qou#8291` (`97f9ffaed50b1b3971470d9bc651293cd4f935e3`, `0` advisories) and remediated `1 major, 1 advisory` borrowed-name findings on sibling PR `litlfred/qou#8277`, pushing `845c943537ff3112ef1cadf49f54381fb96fcb38` and posting `ready: 845c943537ff3112ef1cadf49f54381fb96fcb38` (`https://github.com/litlfred/qou/pull/8277#issuecomment-6945121466`).
- **Status:** Kept at `in-progress` pending Merge Manager verification and merge.

## 2026-11-20 — W10 (qou-c8p8 workstream)

Stalled-claim takeover by W10 (session_01VQDpPeWFnvbDUN18UJ6CyC, PR #8530): prior claim's backing branch had no commit for >3 h (lane-e667 branches last pushed 2026-11-17). The lane-e667 'Progress Update' sections above refer to unmerged bundle PRs and are NOT the closure.

Subject is proved on main: `qThetaC_eq_zero_iff` (`QOU/QBeta/C1ThetaZeroLocus.lean:450`), built on `argumentPrinciple_annulus_finset` (`C1ConnectionPoles.lean:1121`). Re-checked 2026-11-20: lean-direct exit 0, `#print axioms` = [propext, Classical.choice, Quot.sound]. The PARALLELOGRAM argument principle (`HasArgumentPrinciple`, EllipticDivisorDegree.lean:217) is a different object and stays open under qou-z4jb / qou-nuxb.

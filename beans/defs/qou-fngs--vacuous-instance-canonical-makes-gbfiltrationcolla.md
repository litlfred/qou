---
# qou-fngs
title: 'Vacuous: instance canonical makes GBFiltrationCollapsesAtE2 free for every R'
status: in-progress
type: bug
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T14:13:08Z
updated_at: 2026-11-16T18:28:22Z
parent: qou-6qbv
---

`QOU/Mathlib/SpectralSequence.lean:125`:

```lean
instance canonical (R : Type u) : GBFiltrationCollapsesAtE2 R where
  ss := trivial R          -- every cell PUnit, every differential zero
  collapses := trivial_collapses_at_E2 R
```

The file says it outright: *"the trivial spectral sequence **vacuously**
discharges the §3b-cond hypothesis."* Because it is an `instance`, typeclass
resolution supplies it for **every** `R` — so any downstream theorem taking
`[GBFiltrationCollapsesAtE2 R]` is unconditional, and the substrate axiom
`S-GB-spectral-collapse` asserts nothing.

Same self-assuming shape `main` removed twice this week:
`hasDqSquaredNonvanishing_of_fact` and
`hasCategoricalIrreducibility_of_subsingleton`, both deleted for producing a
class from a trivial witness of its own conclusion.

Four more instances have the same shape: `trivial_converges`,
`gb_trivial_converges`, `wedderburnSS_n2_converges`,
`gb_wedderburn_generic_converges`.

## Blast radius is small — fix it before anything is built on it

Only `UpstreamSubstrateBridge.lean` and `Summary.lean` reference the classes,
and both are *about* the API rather than doing mathematics with it. Nothing
substantive consumes the hypothesis yet, which is exactly why now is the time.

## The fix, in the corpus's own idiom

`TauFunctorTargetSpec.interface_alone_is_trivially_inhabitable` is the
precedent: keep the trivial model, **demote it from `instance` to `def`**, and
state its triviality as a named theorem so a reader sees how little it costs to
inhabit. Then `[GBFiltrationCollapsesAtE2 R]` becomes a real hypothesis that a
genuine GB filtration must discharge.

## Fixed 2026-08-24

Seven `instance` declarations demoted to `def` in
`QOU/Mathlib/SpectralSequence.lean` — `canonical` (renamed
`canonicalTrivial`), `trivial_converges`, `gb_trivial_converges`,
`wedderburnSS_n2_converges`, `gb_wedderburn_n2_converges`,
`wedderburnSS_generic_converges`, `gb_wedderburn_generic_converges`. The file
now declares **no instances at all**, so `[GBFiltrationCollapsesAtE2 R]` is a
real hypothesis again.

### `collapse_is_definitional`

Added in the idiom of `TauFunctorTargetSpec.interface_alone_is_trivially_inhabitable`:
every spectral sequence constructed in this file has `differential _ _ := default`,
so `CollapsesAt` holds by `rfl` at every page. Collapse is **built into the
models, not proved of anything** — including `wedderburnSS_n2`, whose cells are
genuinely `Fin 2 → R` at the origin but whose differentials are still constant.

### The rename that mattered most

`UpstreamSubstrateBridge.gb_spectral_collapse_at_E2_discharged` →
`exists_collapsing_spectralSequence`. The old name read as though the substrate
axiom `S-GB-spectral-collapse` had been discharged. The statement is
`∃ S, CollapsesAtE2 S` — it never mentions the Gröbner filtration, and the
witness performs no computation. Four call sites updated; no block `lean.ref`
pointed at it.

`Summary.inventory_check` used `inferInstance` for the spectral-sequence
conjunct; it now names `canonicalTrivial R` explicitly, so a reader sees the
witness is `PUnit`.

    SpectralSequence.lean         exit 0
    UpstreamSubstrateBridge.lean  exit 0

## Found alongside, NOT caused here: `QOU.Mathlib.Summary` is red on `main`

`inventory_check` asserts `Nonempty (IwahoriHeckeAlgebra R 2 q)` and
`Nonempty (WedderburnIsomorphism R 2 q)` via `inferInstance`, and
**`IwahoriHeckeAlgebra` has no instance anywhere in the corpus** — so the
theorem cannot have compiled. Verified red at `origin/main`, independent of
this change (`lean-direct-cone.sh QOU.Mathlib.Summary` → exit 1 both before and
after my edits).

It went unnoticed because `Summary.lean` is one of the **871 of 2085 modules
not reachable from `QOU.lean`** — the root target never builds it. That is
exactly the "green by omission" hazard `prepare-merge` §4 warns about: a module
you touched can be green because nothing compiles it.

Not fixed here: the honest repair is either a real `IwahoriHeckeAlgebra`
instance or dropping an inventory line that claims one exists, and both are
owner calls about what the upstream bundle is asserting.

## Deeper than the instances: the PREDICATE is weaker than its name

Asked whether `differential _ _ := default` is itself an issue. It is, and it is
worse than the vacuous instances. Two defects, now **exhibited in Lean** rather
than asserted.

### (i) `zero` is a marked element, not an additive zero

`SpectralSequence` carries `zero : ∀ c, cell c` — with no additive structure on
`cell` and no law relating `zero` to anything. So

```lean
CollapsesAt S r₀ := ∀ c, c.r ≥ r₀ → ∀ x, S.differential c x = S.zero c.next
```

asserts "the differential equals whatever element the model nominated", which
**any constant differential satisfies**. `constTrue` is a model whose every
differential is the constant `true`; `constTrue_collapses` holds at every page,
and `constTrue_differential_is_true` shows the differential is not the additive
zero of `Bool` under any reading.

So `CollapsesAt` does not mean "the differential vanishes".

### (ii) No page-turning, so collapse relates no two pages

A spectral sequence requires `E_{r+1} ≅ ker d_r ⧸ im d_r`. This structure has no
such field, so `cell {r := 2, …}` and `cell {r := 3, …}` are **unrelated types**.

`EInfinityCell S r₀ h p q` is then *defined* as `S.cell {r := r₀, p, q}`, and
`eInfinity_eq_page_is_rfl` proves `E_∞ = E_{r₀}` by `rfl` — for **any** spectral
sequence and **any** collapse proof. The docstring's "collapse immediately
implies `E_{r₀} = E_{r₀+1} = … = E_∞`" is true only in that circular sense.

### How to resolve — and this part needs no missing infrastructure

Value cells in `ModuleCat R`, make `differential` `R`-linear, and add the two
absent laws: `d ∘ d = 0` and the page-turning isomorphism. Then
`CollapsesAt r₀ → E_{r₀} ≅ E_∞` becomes a **theorem** rather than a definition.

`LinearMap.ker`, `LinearMap.range` and quotients are all in Mathlib. It is the
*general* spectral-sequence theory that is missing (`qou-pan0`), **not this** —
so the honest minimal version is buildable today, and my earlier framing
("spectral sequences absent from Mathlib, therefore blocked") was too pessimistic
about this particular file. Correcting that here.

## The repair, built 2026-08-24

Two new modules. The defect is now not just documented but replaced.

### `QOU/Mathlib/PagedSpectralSequence.lean` — collapse becomes a theorem

Supplies the three things the old API lacks, which are exactly what a spectral
sequence *is*:

| law | why the old API needed it |
|---|---|
| pages are `R`-modules | so "the differential is zero" means the zero map, not "equals a nominated element" |
| `d ∘ d = 0` | without it `ker ⊇ im` fails and the page quotient is not well-posed |
| `turn : E_{r+1} ≅ ker d_r ⧸ im d_r` | what makes the pages a **sequence** rather than unrelated indexed objects |

`page_stabilises_of_collapse` is then a real theorem. The old API's counterpart,
`eInfinity_eq_page_is_rfl`, is true by definition for every spectral sequence,
collapsing or not.

Worth recording: `next (prev c) = c` holds by **arithmetic on ℤ, not by `rfl`**,
so the incoming differential lands in a syntactically different page and needs
the `reindex` transport. Without it `incoming` does not typecheck.

No trivial witness is shipped, deliberately — naming one is what let the old
placeholder be reached for and then cited.

### `QOU/Mathlib/BarGradedCollapse.lean` — collapse *proved* from a grading

`QOU/QBeta/ZBarParity.lean` already had the argument at the **scalar** level:
`z` bar-even, `κ_{(2,1)}` bar-odd, and `bar_even_ne_bar_odd_of_ne_zero`
excluding their coincidence — the `c₃`-odd exclusion. Structurally that is a
ℤ/2 grading, and it is the most classical reason a spectral sequence
degenerates.

The missing step was the lift from scalars to **maps between modules**:

- `map_eq_zero_of_parity_mismatch` — a bar-equivariant map from a purely even
  module to a purely odd one is the zero map;
- `collapses_of_parity_mismatch` — hence a `PagedSS` running even → odd from
  page `r₀` collapses at `r₀`;
- `page_stabilises_of_parity` — chained, `E_{r+1} ≅ E_r`.

**2-torsion-freeness is an explicit hypothesis, not a field assumption**, so
this works over `R_q = ℤ[q, q⁻¹]` where the corpus actually is.
`ZBarParity`'s field-based version needs specialisation to `ℝ` first; this
does not.

### Still assumed, and said plainly in the docstrings

The parity **data**. Someone must exhibit the involution and show the pages are
purely even / purely odd, for the Gröbner filtration specifically. Neither file
does that. What is gone is the step where collapse *itself* was assumed.

### Verification

```
lean-direct-cone      exit 0 (both modules)
#print axioms         propext / Classical.choice / Quot.sound — no sorry
run-validate          Valid — 26 issues, 0 errors
mirror drift  @35     exit 0   (wall-crossers 0, regime-only 0)
duplicate decls @57   exit 0
self-discharging      125 unconditional, 17 trivial (new gate)
```

### One process failure worth keeping

`PagedSpectralSequence.lean` was written, compiled and axiom-checked — and then
**not committed** before the container reset, so it had to be reconstructed
from scratch. Compiling is not landing. Commit before moving to the next file.

THE DOWNSTREAM CONSUMER, found 2026-08-24. The spectral-collapse work is not decorative — the exactness of every binding energy in the corpus rests on it.

`prop:atom-knot-mass-derivation` (folio/quantum-observable-universe/mass-theory/):

    M(H) = nu_SDP * [ tr_M(T_w) + tower(T_w) + tr_M(C_dimq) ]
    B(H) = m_e * M(H) |_{q=q0}

and the load-bearing sentence: "Since the GB spectral sequence collapses at E_2, no higher slices contribute. The computation relies entirely on the pre-Archimedean data encoded in the GB-filtration jet-order certificate."

So M is an EXACT FINITE SUM only because the GB spectral sequence collapses at E_2. That is S-GB-spectral-collapse — the assertion whose fifteen classes have zero instances between them. If the collapse fails, M is a truncation and every binding energy is approximate, not exact.

Three consequences for the arc, all actionable:

1. `SpectralCollapseCriteria.legacyOfPaged` (landed today) is the route by which a real filtration can discharge `GBFiltrationCollapsesAtE2`. Before today the only discharge was `canonicalTrivial` (PUnit), so the binding-energy derivation was resting on a hypothesis that only a trivial model had ever satisfied.

2. `EulerCharacteristic.eulerChar_bump_eq` bounds the damage if collapse fails: an ALTERNATING SUM of page ranks is page-independent with no collapse hypothesis, while an individual graded piece is not (`finrank_bump_eq_iff`). So whichever part of M is index-like survives a collapse failure; whichever part reads an individual slice does not. Splitting M along that line is the next concrete task, and it does not need the collapse to be proved first.

3. The certificate named is the GB-filtration JET-ORDER certificate — which is exactly the filtration `DqTwist.dq_sq_eq_curvature` points at, since the curvature of d_q is first order in (1 - q^-1) and therefore sits in filtration degree >= 1. The twist thread and the collapse thread meet here, at a formula the physics actually uses.

Also settled this session (binding channel question): the "action" is not the normal-form net. net(p) ~ 0.999, net(bare qqbar) ~ 1.418, net(M_+) ~ 1.515 are commensurable (same H_3(q), same NF basis, same q0) but binding RAISES net by 0.097, so net cannot be the minimised functional. The minimisation is the confinement SDP (`confined(P,q)` strict feasibility; sigma_F the optimal dual objective), and nu_SDP is what enters M above.

THE COLLAPSE IS LOCALISED TO ONE TERM, AND IT IS A BOUNDEDNESS CLAIM.

`prop:phi-q-categorical-truncation` (content/.../mass-theory/):

    m_tower(T_w) = sum_{k=0}^{k*(T_w)} alpha_k * m^(k)(T_w)
    "The depth k*(T_w) is exactly the maximum GB-depth among the support
     partitions. Truncation at any deeper level k >= k* yields the identical
     categorical value."

Two things follow, both narrowing the arc considerably.

**1. Only one of the three terms of M is collapse-dependent.** M = nu_SDP * [tr_M(T_w) + tower(T_w) + tr_M(C_dimq)]. The two tr_M terms are Markov traces — linear functionals, not slice sums — so a collapse failure does not touch them. `tower(T_w)` is the slice sum, and it is the whole exposure. That is the split the previous note asked for, and it did not need the collapse proved to find.

**2. The claim is BOUNDEDNESS, not collapse-at-E2, and boundedness is the weaker and provable one.** "Truncation at k >= k* yields the identical value" says the slices above k* vanish. A spectral sequence with finitely many non-zero terms per total degree degenerates at SOME finite page — that is standard and needs no Groebner input. So:

  * collapse at some finite r: follows from boundedness. Provable.
  * collapse at E_2 SPECIFICALLY: still an assertion, and it is what fixes k* to be the max GB-depth rather than something larger.

The mass formula needs the specific k*, so it needs E_2, not merely "some page". Do not conflate them; the corpus currently states only the strong form.

**Formalisation target, now concrete.** Build a `PagedSS` whose pages vanish above k*, i.e. `Subsingleton (page c)` for c.r > k*. Then `LongExactSequence.map_eq_zero_of_subsingleton` / `_target` and `equivOfFlankingTermsZero` apply directly, `Collapses` follows, and `SpectralCollapseCriteria.legacyOfPaged` discharges `GBFiltrationCollapsesAtE2` from a real object rather than PUnit. This is the bounded case that `EulerCharacteristic`s docstring named as the remaining work; it is now identified as the thing the mass formula actually rests on.


---

## Status audit 2026-08-24 — the titled defect is closed, the bean is not

Two things are tangled in this bean and a reader should not have to untangle
them, so, explicitly:

**1. The defect in the title is FIXED and verified.**
`QOU/Mathlib/SpectralSequence.lean` now declares **zero instances** — checked by
`grep -c '^instance'` on the working tree, which returns 0. `canonical` is
`canonicalTrivial`, a `def` at line 136, and the other six demotions listed
above are in place. `[GBFiltrationCollapsesAtE2 R]` is a real hypothesis again.
Nothing further is owed on the title.

**2. Deliberately left open, because the bean grew an arc.** The notes below the
fix are not about that instance at all. They establish:

- the binding-energy derivation `M(H) = nu_SDP * [tr_M(T_w) + tower(T_w) +
  tr_M(C_dimq)]` is an exact finite sum **only** because the GB spectral
  sequence collapses at E_2 — so `S-GB-spectral-collapse` is load-bearing for
  the physics, not decorative;
- the exposure is **localised to one term**: the two `tr_M` terms are Markov
  traces (linear functionals, not slice sums) and survive a collapse failure;
  `tower(T_w)` is the whole exposure;
- the claim the manuscript actually needs is **boundedness** ("truncation at
  k >= k* yields the identical value"), and collapse at *some* finite page follows
  from boundedness with no Groebner input — but the mass formula needs k* to be
  the max GB-depth, which is collapse at **E_2 specifically**. Do not conflate
  the two; the corpus states only the strong form;
- the concrete formalisation target: a `PagedSS` with `Subsingleton (page c)`
  for `c.r > k*`, after which `LongExactSequence.map_eq_zero_of_subsingleton` /
  `equivOfFlankingTermsZero` apply, `Collapses` follows, and
  `SpectralCollapseCriteria.legacyOfPaged` discharges
  `GBFiltrationCollapsesAtE2` from a real object rather than `PUnit`.

That is a live work item with a named next step, so this bean stays
**in-progress**. Closing it on the strength of the demotion would lose the arc.
Whoever picks it up: consider splitting (2) into its own bean and closing this
one, but do not close this one without doing the split first.


---

## Re-measured 2026-09-03 — the stated formalisation target was already delivered, and the reasoning above it conflates two filtrations

Three corrections, in increasing order of how much they change the arc.

### 1. The "formalisation target, now concrete" is done

The closing paragraph asks for: *"Build a PagedSS whose pages vanish above `k⋆` … then `Collapses` follows, and `SpectralCollapseCriteria.legacyOfPaged` discharges `GBFiltrationCollapsesAtE2`."* That criterion is `collapses_of_bounded_support`, `SpectralCollapseCriteria.lean:168`, landed in the same tranche this bean records. It takes exactly the `Subsingleton` hypothesis named, and yields `Collapses S (N+1)`. Nothing was left to build on that side.

### 2. Nothing has ever been on the other side of it

Measured on `origin/main`: **every** occurrence of `PagedSS` in the corpus is a hypothesis — `imRank (S : PagedSS K pageK)`, `Collapses (S : PagedSS R page)`, `toLegacy (S : PagedSS R pageU)`, `legacyOfPaged (S : PagedSS R pageU)`. **Not one declaration constructs a `PagedSS`.**

So the whole paged tower — `page_stabilises_of_collapse`, both bounded-support criteria, `toLegacy`, `legacyOfPaged`, the Euler-characteristic results — had never been applied to anything, and consequence 1 above ("`legacyOfPaged` is the route by which a real filtration can discharge `GBFiltrationCollapsesAtE2`") describes a route with zero traffic. `canonicalTrivial` remained the only discharge, exactly as before the repair.

That is the sharper version of this bean's own finding: the defect was not only that a `PUnit` witness was reachable, but that after it was demoted, **nothing replaced it**.

### 3. `p` and `k` are different filtrations — this is the substantive correction

The section "THE COLLAPSE IS LOCALISED TO ONE TERM" concludes:

> collapse at E_2 SPECIFICALLY: still an assertion, and it is what fixes k* to be the max GB-depth rather than something larger

and

> The mass formula needs the specific k*, so it needs E_2, not merely "some page".

Both sentences read the page/column index and the GB-depth as one index. They are not, and `phi-q-categorical-truncation-proof.md` uses them in two different steps:

- **`p`** — the Hochschild / filtration degree, the **column** index (`CellIndex.p`). Step 1 asserts `E_∞^{p,*} = Z(A)` at `p = 0` and `0` for `p ≥ 1`. Collapse is a statement about differentials between columns, and this is the only thing the proof asks collapse for.
- **`k`** — the GB-depth of a *partition*. Step 3 uses it to stratify `Z(A) = ⊕_{k=0}^{k⋆} Z^{(k)}(A)`: a decomposition **inside** the single surviving column `E_∞^{0,*}`. It indexes no page and no column.

`k⋆ := max_{λ ∈ supp(T_w)} depth_GB(λ)` is finite for the reason Step 3 states — a maximum over a finite NF support — and the spectral sequence plays no part in fixing it. So collapse at E₂ does not fix `k⋆`, and needing a specific `k⋆` is not a reason to need E₂ rather than some other page.

**And separating them is what makes the E₂ claim reachable.** Read as a statement about `p`, Step 1 *is* concentration in one column — the `N = 0` case — and `collapses_two_of_bounded_support` already covers `N ≤ 1`. The bean treats E₂ as the hard strong form that boundedness cannot reach; for the window the mass formula actually states, boundedness reaches it exactly.

### What landed (PR #6452)

`QOU/Mathlib/ConcentratedColumnCollapse.lean` — the `p = 0`-column page family, `concentrated_collapses` (concentration ⇒ `Collapses S 2`, for **every** differential the family admits; the proof never inspects `S.d`), and `gbCollapsesOfConcentrated`, the first `GBFiltrationCollapsesAtE2` in the corpus whose witness is neither `PUnit` nor an assumption. Inhabitation is an existence theorem rather than a named model, following `PagedSpectralSequence.lean`'s stated reason.

`lean`-direct exit 0 (7/7, no warnings); `#print axioms` clean on all five declarations; an `example` confirms the discharge applies at a concrete `R`. Registered in `QOU.lean`, which carried none of this cluster.

### Still open, and unchanged by any of the above

**The concentration itself.** Nothing shows the Gröbner-filtration spectral sequence of `H_n(R,q)` is concentrated in the `p = 0` column. That is `S-GB-spectral-collapse`, it is what the binding-energy exactness rests on, and it is still an assertion. What is no longer assumed is the step from concentration to collapse.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-03 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Verification & Audit Note (2026-11-16 — Round 47, PR #8147)

- Verified on `main` (`folio/quantum-observable-universe/lean/QOU/Mathlib/`) that:
  1. All 7 vacuous `instance` declarations in `QOU/Mathlib/SpectralSequence.lean` were demoted to `def` in commit `b61f6a4fd3` (`0` `instance` declarations remain in `SpectralSequence.lean`).
  2. `QOU/Mathlib/PagedSpectralSequence.lean` (`571147350c`) and `QOU/Mathlib/ConcentratedColumnCollapse.lean` (`1949f25d71`, `gbCollapsesOfConcentrated`, `concentrated_collapses`) are landed (`0` `sorry`) and wired into `QOU.lean`.
- Kept at `status: in-progress` per owner rule (no unilateral bean closure).

---
# qou-fngs
title: 'Vacuous: instance canonical makes GBFiltrationCollapsesAtE2 free for every R'
status: in-progress
type: bug
priority: high
created_at: 2026-08-24T14:13:08Z
updated_at: 2026-08-24T18:38:26Z
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

`prop:atom-knot-mass-derivation` (content/quantum-observable-universe/mass-theory/):

    M(H) = nu_SDP * [ tr_M(T_w) + tower(T_w) + tr_M(C_dimq) ]
    B(H) = m_e * M(H) |_{q=q0}

and the load-bearing sentence: "Since the GB spectral sequence collapses at E_2, no higher slices contribute. The computation relies entirely on the pre-Archimedean data encoded in the GB-filtration jet-order certificate."

So M is an EXACT FINITE SUM only because the GB spectral sequence collapses at E_2. That is S-GB-spectral-collapse — the assertion whose fifteen classes have zero instances between them. If the collapse fails, M is a truncation and every binding energy is approximate, not exact.

Three consequences for the arc, all actionable:

1. `SpectralCollapseCriteria.legacyOfPaged` (landed today) is the route by which a real filtration can discharge `GBFiltrationCollapsesAtE2`. Before today the only discharge was `canonicalTrivial` (PUnit), so the binding-energy derivation was resting on a hypothesis that only a trivial model had ever satisfied.

2. `EulerCharacteristic.eulerChar_bump_eq` bounds the damage if collapse fails: an ALTERNATING SUM of page ranks is page-independent with no collapse hypothesis, while an individual graded piece is not (`finrank_bump_eq_iff`). So whichever part of M is index-like survives a collapse failure; whichever part reads an individual slice does not. Splitting M along that line is the next concrete task, and it does not need the collapse to be proved first.

3. The certificate named is the GB-filtration JET-ORDER certificate — which is exactly the filtration `DqTwist.dq_sq_eq_curvature` points at, since the curvature of d_q is first order in (1 - q^-1) and therefore sits in filtration degree >= 1. The twist thread and the collapse thread meet here, at a formula the physics actually uses.

Also settled this session (binding channel question): the "action" is not the normal-form net. net(p) ~ 0.999, net(bare qqbar) ~ 1.418, net(M_+) ~ 1.515 are commensurable (same H_3(q), same NF basis, same q0) but binding RAISES net by 0.097, so net cannot be the minimised functional. The minimisation is the confinement SDP (`confined(P,q)` strict feasibility; sigma_F the optimal dual objective), and nu_SDP is what enters M above.

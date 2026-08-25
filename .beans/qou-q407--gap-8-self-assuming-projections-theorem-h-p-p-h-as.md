---
# qou-q407
title: 'GAP: 8 self-assuming projections — ''theorem (h : P) : P := h'' asserts nothing'
status: in-progress
type: task
priority: high
tags:
    - lean
created_at: 2026-08-07T18:24:34Z
updated_at: 2026-08-21T15:23:31Z
---

Eight provable declarations have the shape 'theorem name ... (h : P) : P := h' — hypothesis identical to conclusion, proof term the identity. They assert nothing about the objects named, and stay true if every definition is swapped.

Found via the folio-assistant triviality probe (6/40 closed; 2 genuine, 4 legit decide/simp), then swept statically by scripts/lean-self-assuming-audit.py (2590 files, 4.5 s). Full analysis + quoted bodies: docs/audits/2026-08-07-self-assuming-projection-sweep.md

Findings (lines on main @ b48ce882fa):
1. defect_legendrian_knot — brings-surface/defect-legendrian-knot.lean:47
2. topological_charge_quantization — brings-surface/topological-charge-quantization.lean:43
3. fomin_identity — lean/QOU/Archimedean/BranchingConvergence.lean:138
4. fomin_identity_n3 — lean/QOU/Archimedean/BranchingConvergence.lean:152
5. length_bound_necessary — lean/QOU/BraidKnot/PSDFeasibilityProxy.lean:94
6. universal_ilp_selects_minimum — nuclear-interactions/universal-ilp-algorithm.lean:43
7. variational_transport — quantum-observable-universes/categorical-action.lean:109
8. ordering_extends — unital-groebner-bases/lean/UGB/GrobnerShirshov/JetOrder.lean:213

Why no existing gate caught them: no sorry, no axiom, no True conclusion, type-checks clean. AGENTS.md 3b-cond item 5 names the pattern; there was no detector.

NOT fixed in the detector PR — rewriting a theorem statement changes what the corpus claims. Per 1a the honest dispositions are prove / state-with-sorry+Ref / demote-to-conjecture, chosen per declaration. fomin_identity needs real SYT definitions rather than its uninterpreted dim_fn/mult_fn parameters.

Scope-(a): the Lean carries no content. NOT a claim the underlying math is wrong — Fomin's identity is a true theorem of the literature.

Follow-ups: wire as a proof-self-assuming criterion in content/pipeline/lean-vacuity-axiom-audit.ts; run the triviality probe corpus-wide to reach the ':= by exact h' variants the static pass cannot see.



## Re-verified 2026-08-19 (current main @ 5b158ef0)
Re-ran scripts/lean-self-assuming-audit.py: **all 8 still live** — none fixed in the 5-week gap. Same 8 decls, same lines (defect_legendrian_knot, topological_charge_quantization, fomin_identity, fomin_identity_n3, length_bound_necessary, universal_ilp_selects_minimum, variational_transport, ordering_extends). Ready to work; still the most concrete item in the vacuity arc.



## DONE 2026-08-21 — all 8 self-assuming projections eliminated
Vacuity audit over all 8 files → 0 defects; static lean-self-assuming-audit.py → 0 of the 8 remain.
- Library cluster (fomin_identity ×2 → def:Prop; length_bound_necessary → def withinLengthBound; ordering_extends → embedding-explicit derived theorem). lean-direct exit 0.
- Content-block cluster (defect_legendrian_knot, topological_charge_quantization, variational_transport, universal_ilp_selects_minimum → def:Prop; universal_ilp gains a real optimality predicate). lean-direct exit 0.
Follow-up: demote the 2 provable-kind blocks (proposition/theorem) to conjecture — filed. PR #5356.
---

## 2026-08-21 — the count was wrong, and one is now proved

### The detector under-reported by a third: 12, not 8

`scripts/lean-self-assuming-audit.py` parsed explicit binders with a regex
whose type alternation admitted only **one** level of parentheses. Any
hypothesis nesting two deep was unparseable, so the binder was dropped and the
declaration could never be reported — **silently**: a declaration it could not
parse and one it parsed and found clean produced identical output. The bias ran
against exactly the elaborate statements most likely to hide a tautology.

Fixed with balanced-delimiter scanning (`parse_binders`, no depth limit, also
reads `{..}` / `⦃..⦄` / `[..]`). Corrected sweep over 3008 files (the original
saw 2590) finds **five more**:

- `structurallyValidBinding_necessary` — `QOU/BraidKnot/PSDFeasibilityProxy.lean:103`
- `jet_preserves_channel_separation` — `QOU/ChannelSeparation.lean:162`
- `adjoint_has_no_degree_zero` — `QOU/GradedFrobeniusHopf.lean:116`
- `plancherel_total_bound` — `mass-theory/plancherel-term-7-formulation.lean:61`
- `plancherel_sum_eq_one` — `mass-theory/plancherel-term-7-formulation.lean:71`

`structurallyValidBinding_necessary` sits **nine lines below**
`length_bound_necessary`, which the original sweep *did* report. It differs
only by having a more complicated hypothesis.

### `universal_ilp_selects_minimum` — proved (§1a "prove it")

The docstring already named a genuine claim: "The LP selects the
minimum-crossing feasible knot operator." That is an **attainment** statement,
and `crossing_number : ℕ` makes it provable by well-ordering. Restated and
proved sorry-free; the file compiles clean.

```lean
theorem universal_ilp_selects_minimum (q : ℝ) (state : Fin 6 → ℝ)
    (K₀ : KnotOperator q) (hK₀ : universal_ilp q state K₀) :
    ∃ K, universal_ilp q state K ∧
      ∀ K', universal_ilp q state K' → K.crossing_number ≤ K'.crossing_number
```

The pattern generalises: **read the docstring first.** Where the prose names a
real claim, the disposition is usually "prove it" and the statement to prove is
already written down in English.

### Dispositions for the remaining 11 — analysis, not yet applied

Grouped by what the honest disposition turns on. Several need an owner ruling
because rewriting a statement changes what the corpus claims.

**(A) No definitions exist to state the claim — needs `sorry`+Ref or demotion.**
`defect_legendrian_knot`, `topological_charge_quantization`,
`variational_transport`, `jet_preserves_channel_separation`,
`adjoint_has_no_degree_zero`. All quantify over an *arbitrary* category with
uninterpreted morphisms. In `defect_legendrian_knot`, `zero : A ⟶ A` is a free
variable merely *named* "zero" — not the zero morphism. Nothing about contact
forms, Reeb residues or Legendrian knots is expressible until the substrate
structures exist. Note `PSDFeasibilityProxy.lean` already uses `axiom` + `Ref`
for exactly this situation, so the file-local idiom is established.

**(B) True by definition — the "theorem" records a convention.**
`length_bound_necessary`, `structurallyValidBinding_necessary`. The docstring
of the first concedes it: "Any candidate violating this bound is excluded from
the search **by hypothesis**." These are not results; naming the enumerator's
search space as a `def` and stating necessity against *that* would at least
make them about something, but adding a definition solely to dignify a
tautology may be worse than deleting. **Owner call.**

**(C) Honest in prose, vacuous in Lean.**
`plancherel_total_bound`, `plancherel_sum_eq_one`. Docstrings already say
"a parametric restatement, not a proof". Lower stakes, but a `**Theorem**`
docstring over `theorem X (h : P) : P := h` is what §3b-cond item 5 forbids
regardless of what the prose concedes.

**(D) Needs real combinatorics.** `fomin_identity`, `fomin_identity_n3`.
As the original audit says: `dim_fn` / `mult_fn` are uninterpreted parameters.
Genuine proof needs real SYT definitions; `sorry`+Ref is the honest interim.

**(E) Vacuous by choice of representation.** `ordering_extends`. Its docstring
claims "the substantive content is that the embedding is order-preserving" —
but **there is no embedding**: the module models monomials as bare `List ℕ` at
every level, and `degLexNat` never mentions an alphabet bound. Nothing can be
proved because nothing is being mapped. A substantive statement *is* available
in this representation — a fully-descended word is deg-lex below a fully
transient one of the same length, which is what would justify processing
descended parts first — but that is a different theorem from the one claimed.
**Owner call.**

### Adjacent, out of scope, worth separate beans

- `phi_k_finite` (`plancherel-term-7-formulation.lean:78`):
  `∃ x : ℝ, phi_k k blocks = x := ⟨phi_k k blocks, rfl⟩`. Vacuous — every term
  equals itself; "well-defined" is not a theorem in a total type theory. A
  *different* vacuity shape the detector cannot see, since the proof is not a
  bare identifier. Matches the original audit's own follow-up about
  `:= by exact h` variants.
- `KnotOperator.is_knot : Prop` is an opaque `Prop` field — the §3b-cond
  "projected opaque Prop" pattern, in the same file as the ILP fix.
- `gram_matrix _q = 0` in `universal-ilp-algorithm.lean` makes
  `frobenius_positive` vacuously true. Disclosed in its docstring, so not
  hidden, but it means the newly proved attainment theorem ranges over a
  feasible set whose Frobenius constraint constrains nothing.

## Next

- [x] Fix the detector's binder parsing; re-sweep corpus-wide
- [x] `universal_ilp_selects_minimum` — proved
- [ ] Owner ruling on groups (B) and (E), where the honest fix changes what the
      corpus claims
- [ ] Apply (A), (C), (D) dispositions once (B)/(E) are settled, so the whole
      set lands as one reviewable change
- [x] Extend the detector to the `:= by exact h` and `⟨x, rfl⟩` shapes —
      done; `by exact h`/`by assumption` found **nothing** new (measured
      negative), `⟨e, rfl⟩` found **15**, and a second silent parser bug
      (conclusion taken at the last top-level `:`, wrong for every
      `∃ x : T,` conclusion) was fixed in passing. Corpus total: **27**.
- [ ] Disposition the 15 `trivial-existential` findings. Two are not merely
      vacuous but mis-titled: `wenzl_annihilator` carries three literature
      Refs for `∃ x : R, x = 0` with its `firstCol ≥ 4` hypothesis unused,
      and `nuclear_knot_classification` proves the `.borromean` constructor
      exists with `Z`, `N`, `hA` unused. **Owner call** — same class of
      decision as groups (B)/(E).
- [ ] Consider an unused-binder heuristic: every one of the 27 has hypotheses
      that never appear in the conclusion. Not sufficient on its own, but a
      cheap corpus-wide pre-filter for the shapes no regex will catch.

---

## 2026-08-21, dispositions applied — 27 → 22, all compile-verified

**Group (E) did not need a ruling.** The corpus had already answered it:
`QOU.AlgebraicSubstrate.AtomicityJetIndependence` records that "the block's
`axiom ordering_extends` is tautological there" and recovers the genuine
extension leg as `ltAt_extends`, derived from `level_mono`. I mirrored that
accepted precedent in `JetOrder.lean`'s own vocabulary — `degLexAt n` for the
level-restricted order, and `ordering_extends : m ≤ n → degLexAt m a b →
degLexAt n a b`. The levels are alphabet bounds; the docstring's "embedding"
never existed. Proved.

**Group (B) taken as B1 (delete).** Both were conventions of
`binding-k-enumerator` written as results, neither had any caller, and both
conventions are now recorded as prose in the file. B2 was rejected on the
grounds given in the brief: a definition existing only to be echoed is the
same defect one level up.

**`nuclear_knot_classification` could not be deleted** — it is the `lean.ref`
target of `prop:nuclear-knot-classification`. Its classification table existed
only in constructor comments; transcribed to `nuclearKnotType` and proved, so
`hA` now does work. Added `bindingScale_of_borromean`, which is the
proposition's own title and was not previously derivable.

**`wenzl_annihilator` weakened to what the file supports**: `∃ j ≤ firstCol,
qInt ζ j = 0`, proved from its own `qInt_four_eq_zero`. The character
statement stays open and is now documented as open rather than implied proved.

Verification: every touched file compiles clean under `lean_leanpath`. Two
container-cache gaps had to be cleared first (19 stale UGB oleans; four missing
`QOU.Mass.*` / `QOU.MathlibExt.*` oleans) — neither was a corpus defect.

### Remaining: 22 (9 self-assuming, 13 trivial-existential)

Groups (A), (C) and (D) are untouched and unchanged in character. Of the 13
trivial-existentials, **three are `lean.ref` targets and must be restated
rather than deleted** (`knot_factor_spectral_form`, `habiro_integral`,
`spectral_decomposition_qvalue`); the other ten have no reference beyond their
own definition site. That check is done, so the next pass is mechanical.

### The unused-binder heuristic: implemented, measured, rejected as a gate

854 hits corpus-wide; 447 requiring a relation-bearing binder — ~15% of
provable declarations. Ordinary theorems about global constants mention
globals, not binders. Shipped behind `--heuristic`, off by default, as a triage
aid only. Recorded rather than dropped because the negative is the useful part.

## Next

- [ ] Groups (A)/(C)/(D) — mechanical now that ref-targeting is known
- [ ] Restate the three ref-bound trivial-existentials
- [ ] Consider wiring the detector into `lean-vacuity-axiom-audit.ts` as a
      `proof-self-assuming` criterion (the original audit's follow-up)

## 2026-08-21 — groups (A)/(C)/(D) applied: self-assuming reaches 0

Corpus sweep now reports **0 self-assuming**, 13 trivial-existential. All twelve
of the original defect are discharged.

- **Ref-bound (2)** — `defect_legendrian_knot`, `topological_charge_quantization`.
  Converted from vacuous theorems to **`def`s naming the condition**, blocks
  moved to `validation: "stub"`. Deletion was unavailable (they are `lean.ref`
  targets); `def` targets are established practice
  (`QOU.Braiding.r_matrix_braiding_structure`), so the refs still resolve.
- **Deleted (7)** — `variational_transport`, `jet_preserves_channel_separation`,
  `adjoint_has_no_degree_zero`, `plancherel_total_bound`,
  `plancherel_sum_eq_one`, `fomin_identity`, `fomin_identity_n3`. No references
  beyond their own definition sites.

**Two were already diagnosed in place** — `jet_preserves_channel_separation`
and `adjoint_has_no_degree_zero` carried inline `⚠` comments naming the `P → P`
shape and citing bean `qou-fav8`. The diagnosis was correct and had been sitting
there; both still type-checked clean, so every gate still read them as proved.
A comment is not a disposition.

**Near-miss:** two distinct declarations are named `variational_transport`
(`categorical-action.lean` and `GaugeTheory.lean`); only the first is vacuous.
A name-based edit would have hit the wrong one.

All seven touched files compile clean.

## Next

- [ ] The 13 trivial-existentials. Ref-targeting is already checked: three must
      be restated (`knot_factor_spectral_form`, `habiro_integral`,
      `spectral_decomposition_qvalue`), ten can be deleted.
- [ ] Wire the detector into `lean-vacuity-axiom-audit.ts` as a
      `proof-self-assuming` criterion — the original audit's own follow-up, and
      the thing that stops this recurring.

## 2026-08-21 — trivial-existentials: 13 found, 16 real, 0 actionable left

### The detector was under-reporting again, by the same *kind* of gap

`trivial_existential_witness` required the witness to be **spelled out**:
`⟨e, rfl⟩` matched, `⟨_, rfl⟩` did not. But `⟨_, rfl⟩` is the same defect and a
*stronger* tell — the author did not even name the value, the elaborator
recovered it by unifying `rfl`. Three more findings, and the one that matters:

- `knot_factor_amphicheiral` — **`lean.ref` target** of
  `cor:knot-factor-amphicheiral`, two substantive-looking hypotheses, both
  unused. Its sibling thirteen lines below, `knot_factor_amphicheiral_value`, is
  the identical shape with the witness written out and **was** reported. The
  scan was blind to exactly the more consequential of the two.
- `magic_crossing_Q_value`, `compound_beta_y_target_extraction` —
  `compound-beta-shell-calibration.lean`.

Third time this bean has found the detector short of its own hardest cases
(binder depth → conclusion colon → unnamed witness). All three were *silent*:
unparsed and clean produced identical output.

### `vacuous-by-design`: an opt-out that does not hide

`qou_standardPart_image_exists` (`AppendixSurreals/Conjectures.lean`) is a
trivial existential **on purpose** — it records that a conjunct of the original
`VacuumEpsilon` conjecture was provable for every `SQ`, so the surviving
conjecture asserts only what is irreducibly open, and it is *used* by
`VacuumEpsilon'.exists_epsilon_vacuum_with_st_image` to rebuild the wider form.
Deleting it destroys a narrowing audit.

Marked `-- vacuous-by-design: <reason>` above the declaration. The finding is
**still reported**, in its own `trivial-existential-by-design` section — a check
that silently excuses cases is indistinguishable from one that never ran, which
is the whole defect class here. The marker must carry a reason; a bare mute is
rejected.

### Dispositions — 7 deleted, 6 restated, 2 demoted to `def`, 1 acknowledged

**Restated (6)** — each now uses hypotheses that were inert:

- `knot_factor_spectral_form` → the unfolding equation the block actually
  claims, plus `knotFactor_self` (the "sum of positive squares" the `.ts`
  title names).
- `knot_factor_amphicheiral` → derives the pairing from `Amphicheiral` and the
  normalisation. **See the content finding below.**
- `archimedean_eval_well_defined` → *uniqueness*: any ring hom `ℝ[q] → ℝ`
  fixing constants with `X ↦ q₀` **is** `evalAtQZero`. Existence was never the
  question; `evalAtQZero` is existence.
- `habiro_integral` → integrality in the **ambient ring**. `HabiroCoeff` is
  `Polynomial ℤ`, so `∃ z : ℤ, (h.coeffs m).eval u₀ = z` restated a *typing*
  fact. What can fail is about `HabiroExpansion.eval`, which goes through
  `Int.castRingHom R`; over `ℚ[u]` coefficients the statement is false, which
  is the distinction the md draws.
- `spectral_decomposition_qvalue` → the expanded `log`-form, so `hq`, `hp`,
  `hd` all do work; plus `bareQValue_nonneg` for `hme`.
- `q_0_well_defined` → *independence of the identification chosen*, which is
  what "well-defined" means. The old form was provable with
  `identification_witness` deleted from the class.

**Deleted (7)** — no reference beyond their own definition site, and no genuine
statement available: `knot_factor_amphicheiral_value`,
`n{6,7,8}_dimq_at_well_defined`, `regime_switched_binding_defined`,
`phi_k_finite`, `plancherel_term_7_finite`. Each leaves a `/-! -/` note saying
what stood there and why it said nothing. Precedent: the same file that holds
`knot_factor_borromean` already carries such a note for
`knot_factor_borromean_value`.

**Demoted to `def` (2)** — `magicCrossingQ`, `compoundBetaYTarget`. `Float`
admits no useful reasoning (no `ring`, no associativity), so a theorem about
them cannot say more than the `def` does. Promoting them properly needs the
quantities to be `ℝ`-valued first — a larger change than this pass.

### Content finding: the amphicheiral corollary does not give `a = 1 - h²`

Proving it from the stated hypotheses yields

> `a_K(β, β*) = 1 - w_alt · (1 + h²)`

not the displayed `1 - h²`. The alternating block contributes `-w_alt h²` via
the mirror sign flip; the rest contribute `1 - w_alt` **by `off_block_norm` as
written**. Recovering `1 - h²` needs the non-alternating blocks to sum to `1`.
The two agree only at `w_alt = 0`, where the corollary says nothing about `h`.

Which normalisation the chapter intends is an **authoring decision**, recorded
as a `caveat` authorNote on `cor:knot-factor-amphicheiral` rather than
reconciled here. The block is `not_checked`, so nothing over-claims meanwhile.
This was invisible while the theorem was `⟨_, rfl⟩`.

### Incidental: a `def` whose body was `sorry`, under a `lean.ref`

`predicted-spectra/spectral-decomposition-qvalue.lean` did **not compile** on
this branch: `Real.log` was an unknown constant (only `Mathlib.Data.Real.Basic`
was imported), so `bareQValue`'s body elaborated to `sorry` and every statement
about it was a statement about `sorry`. The trivial-existential proof never
forced the definition open, which is how it survived. Fixed by importing
`Mathlib.Analysis.SpecialFunctions.Log.Basic`.

### Pre-existing breakage found, NOT fixed here (out of scope)

Two downstream files fail to compile on `main`, both from the 2026-08-09
`HeckeExpansion` genericisation dropping `Mathlib.Data.Real.Basic` from the
transitive import set. Same 12 errors before and after this change:

- `mass-theory/knot-factor-borromean-composite.lean` — `HPow ℝ ℕ` /
  `HSub ℕ ℝ` unsynthesizable; one missing import.
- `mass-theory/knot-factor-shell-closed.lean` — still writes
  `HeckeExpansion n`, which now passes `n : ℕ` as the base ring. Needs an
  authoring decision on which `R`.

## 2026-08-21 — wired into the pipeline, and the two detectors audited each other

The bean's original follow-up is done, and doing it produced the fourth and
fifth silent gaps. Cross-checking two independent implementations is what found
both; neither found its own.

### What the pipeline could not see

`content/pipeline/lean-vacuity-axiom-audit.ts` already had
`proof-no-unused-hypothesis-rfl`, which matches `⟨…, rfl⟩` bodies. But it fires
only when an **explicit Prop-shaped binder is unused** — a property of the
decoration, not of the claim. A statement that binds nothing and concludes a
tautology has no unused binder to notice. Measured over the six pre-fix files
holding eleven trivial existentials: **0 hits**.

Added `trivial-existential` (under `proof-no-trivial-true`) and `binder-echo`
(under `proof-no-self-assuming-projection`). Deliberately **no new criterion
ids** — both shapes are instances of criteria that already exist, already
`critical`, already ledger-wired. Same six files after: 10 hits.

### The pipeline carried the identical binder-depth bug (gap 4)

Its binder regex admitted one level of parentheses — the same defect fixed in
the Python sweep earlier in this bean, reached independently in two codebases.
`knot_factor_amphicheiral`'s `_off_block_norm` nests two deep, so the binder
was dropped and `proof-no-unused-hypothesis-rfl` reported nothing on the one
declaration it was designed for. Balanced scanning alone recovers it: 0 → 1.

### The Python sweep was losing declarations to a missing keyword (gap 5)

`DECL_TERMINATORS` omitted `axiom`. A theorem followed by one swallowed it:
`y_base_case_singleton` yielded a 361-char "proof" reading `hbase axiom
plancherel_completeness_axiom {R : Type u} …`, which the 200-char guard
rejected — silently. Two textbook findings were invisible for that reason
alone, both surfaced by the TS scanner, which splits declarations differently.

`/--` and `--` were dead alternatives in that terminator list: the regex runs
over comment-stripped source, so no comment marker can ever match. Every real
terminator has to be a keyword, which is why one missing keyword was enough.

The length guard now **counts** its rejections (`--diagnostics` lists them),
since a mis-split looks exactly like a long proof. Current: 1528 skipped, of
which **0** contain a top-level terminator keyword — no residual mis-splits.

### The two new findings

- `y_base_case_singleton` — `(hbase : y ⟨[1]⟩ = 1) : y ⟨[1]⟩ = 1 := hbase`.
  Restated as the anchoring the docstring already claimed: on any edge out of
  `(1)` the recursion leaves the bare Bratteli factor. §7c `CommRing` →
  `Field`; the old form divided by nothing because it did nothing.
- `unified_mass_finite` — deleted, same shape as `phi_k_finite`.

### Agreement

Both detectors now report the same corpus: **0 actionable, 1
`vacuous-by-design`** (visible, in its own section). The pipeline's totals are
back to the 96 / 122-exempt baseline, so the wiring lands without turning the
gate red — which is only true because the dispositions went first.

### Noted, not acted on: the diff-scoped ledger gate

`--check-ledger` (`.github/workflows/lean-content-siblings.yml`) fails locally
on this branch: 9 candidates in touched files lack a fresh agent verdict. **4
of the 9 predate today** (`branching_convergence`, `adjoint_vanishing_propagation`,
`kahler_differentials_no_sym_component`, `degree_zero_dim_one`); the other 5
were pulled into the diff-scope by touching `Conjectures.lean` and
`UpstreamSubstrateBridge.lean`. **None comes from the two new patterns.**

The five are `∃ Y : SomeClass, True` "discharge" theorems — a *different*
defect, and arguably a real claim badly stated: `∃ Y : C, True` is `Nonempty C`,
which is genuine content when `C` might be uninhabited. Restating them as
`Nonempty C` would both say what is meant and stop the detector firing. Not
done here: it is a separate class with its own adjudication story, and the
aggregates (`upstream_discharge_complete`, `extended_upstream_discharge`,
`complete_upstream_discharge`) carry the same conjuncts.

GitHub reports **no check runs at all** on PR #5371 and denies combined-status
to this integration (403), so I cannot confirm what CI actually does with this.

## Next

- [ ] Owner: the `1 - h²` vs `1 - w_alt(1 + h²)` normalisation on
      `cor:knot-factor-amphicheiral`.
- [ ] `∃ C, True` → `Nonempty C` across the `_discharged` family, and ledger
      verdicts for the 4 pre-existing candidates. Own bean.
- [ ] `qou/29pv` — the two pre-existing broken knot-factor files.

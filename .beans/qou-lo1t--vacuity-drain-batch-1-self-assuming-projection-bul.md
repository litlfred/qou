---
# qou-lo1t
title: 'VACUITY drain batch 1: self-assuming-projection bulk (118 genuine remaining)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-22T21:28:27Z
updated_at: 2026-08-23T17:23:27Z
---

## Batch 2 (2026-08-23) — Instanton.lean cluster, 4 defects

Two dispositions, and a **detector limitation** worth recording.

**2 re-adjudicated genuine -> legit.** `kernelIncl_exact` and
`categorical_jet_prolongation` project fields of `CategoricalJet` /
`CategoricalJetProlongation` — but those are STRUCTURES DEFINING AN OBJECT,
whose fields are the definition's own axioms (exactness; the prolongation
commuting square). The theorems are universally quantified over the structure,
i.e. the standard Lean field-accessor idiom — exactly Mathlib's
`mul_assoc := Group.mul_assoc`.

**The detector cannot tell these apart from real defects.** A definition's
accessor and a conjecture-carrier's conclusion projection are *syntactically
identical* — both are `:= x.field` where the field type is the conclusion.
The discriminator is semantic: does the structure DEFINE an object (fields =
axioms of the definition) or ASSERT a result (field = the claim)? Likely a
meaningful fraction of the remaining genuine queue is this false-positive
class; worth a triage pass before treating the count as a work-list.

**2 fixed — circular instances removed.** `categorical_irreducible` and
`categorical_dq_squared_nonvanishing` had inhabitation routes that started
from their own conclusions:
- `hasCategoricalIrreducibility_of_subsingleton` took
  `[Subsingleton ((𝟙_C) ⟶ adjointObj)]` — the conclusion verbatim — and
  returned `⟨hsub⟩`.
- `hasDqSquaredNonvanishing_of_fact` produced the class from
  `[Fact (dq ≫ dq ≠ 0)]`, ignoring all three of the class's hypotheses
  (`hq`, `hd_sq`, `hcross`) that the theorem binds — so the statement read
  as a substantive conditional while none of them was load-bearing.
Both removed (0 external refs each); the classes are now honest open carriers.

**A ledger evidence correction.** `categorical_irreducible`'s recorded
evidence said 'UNINHABITED carrier … no instance exists'. That was **wrong** —
the instance existed at line 120. The defect was circularity, not absence.


## Batch 3 (PR #5533)

**The A/B triage heuristic failed — recorded so it is not re-derived.**
Classified the 116 `genuine` entries by binder style (86 instance-binder /
30 explicit-arg) on the theory that explicit-arg entries were more likely
legitimate definition-accessors. Read all 30 of bucket B rather than
sampling: every one has the identical shape as bucket A. Binder style is
bookkeeping, not adjudication.

What does separate them is whether the **docstring claims more than the
projection delivers** — `factors_def`, `binding_eq_bond_energy`,
`knot_eigenbasis_density`, `rho_eq_qdim_via_canonical_knot` all say in
their own docstrings that they are the field under another name; whereas
`uncertainty_vanishes` ("so ω₀ = 0"), `mobius_energy_nonneg` (a real
Freedman–He–Wang theorem, assumed), `noncocomm_iff_quantum` (named "iff",
no iff), `descartes_universality` ("Full proof: χ = −6 ⟹ … ⟹ Bring's
surface" written as a comment where a proof belongs) assert derivations
they do not perform.

**Landed:** `diagram_commutes` (redundant `commutativity` field dropped,
derived from the three arrows); `prop:mi-sw-abelianisation` rewired to the
honest library class its own authorNotes described but its `lean.ref`
never named; `TrefoilElectronMassConj` restated (see `qou-0w42` for the
residual). Six ledger entries pruned, 133 → 127.

**Next in this arc:** the claim-shaped restatements above.
`descartes_universality` and `descartes_terminal` share one LaTeX label
and neither is fixable by derivation — the universality content is not in
the corpus. `TannakaKreinRigidity` is a self-certifying carrier (default
field values make `⟨⟩` an instance), which is `qou-ewc4`.

## Handover 2026-08-23 — the two `MobiusEnergy` defects are a SHADOW PAIR (delete-the-sibling variant)

Not fixed here: this is your drain and it is mechanical work with one owner.
Recording the specifics so the pair is not triaged twice.

Both entries are the same declaration, in a shadowing pair:

| file | line | what it declares |
|---|---|---|
| `climax-volume-mass/mobius-energy-proof.lean` | 105 | `theorem MobiusEnergy ... := cme.classicalLimit` (content SIBLING) |
| `lean/QOU/MobiusEnergy.lean` | 148 | `theorem MobiusEnergy ... := cme.classicalLimit` (LIBRARY) |

Both `promoted_from_exempt`, severity critical, `exempt: false`, same detail
(`cme.classicalLimit` type-identical to the conclusion).

**`mobius-energy-proof.ts` carries `lean: { ref: "qou:QOU.MobiusEnergy" }`.**
Per AGENTS.md §0a the sibling resolves FIRST, so the ref lands on the sibling
and the library declaration is shadowed.

**Which is stronger — this is the delete-the-sibling case, unlike `qou-w61k`.**

- LIBRARY (`QOU/MobiusEnergy.lean`) is stronger: the coefficient is the
  explicit `(1 / 4)`, and it carries a companion `MobiusEnergy_nonneg` with a
  real proof body (`rw [cme.classicalLimit]; have := cme.classicalEnergy.nonneg`).
- SIBLING (`mobius-energy-proof.lean`) is weaker: a generic
  `cme.classicalLimitCoeff` instead of `1/4`, and its non-negativity is
  commented out (the docstring explains `R_q = Z[q,q^-1]` carries no order).

So this is the SAME shape as the three fixed in PR #5533 (library better ->
delete the shadowing sibling), and the OPPOSITE of `qou-w61k`
(`prop:volume-from-rigidity`, where the library holds the worse one and w61k
warns it must not be fixed the same way). Worth keeping the two apart when
draining.

Note the projection defect survives either way: deleting the sibling leaves
the library's `theorem MobiusEnergy := cme.classicalLimit`, which is still a
self-assuming projection. Un-shadowing and de-vacuifying are two steps here,
not one.

Found while executing the ledger disposition on `mobius_energy_nonneg` (a
different declaration, in `mobius-energy.lean`, which `8dd1881a57` deleted
outright — my PR #5541 was superseded by that and is closed).


## Batch 5 (2026-08-23) — the last four shadow pairs, PR #5562

Shadow-pair sweep CLOSED. Four adjudications, four different answers — which is
why "delete the sibling" was never adoptable as a rule.

- `descended_level_zero` — sibling re-introduced the projection the library had
  explicitly removed. **Sibling deleted** (0 references); ref now lands on the
  library's named `Prop`.
- `core_levi_form` — opposite: the sibling is much stronger (a real case-split
  derivation) and the library's twin is the five-field projection. Fixed the
  sibling's own `:= ctx.cond_def` in place, restating it as the two-sided
  pinning `1 <= cond` and `|cond - max/min| <= C0*hbar^2`.
- `exclusionRadius_eq` — free field + defining-equation field. Radius made a
  `def`; added `exclusionRadius_pos` derived from `q_gt_one`.
- `categorical_irreducible` — **two blocks carrying the IDENTICAL `lean.ref`
  resolved to DIFFERENT declarations**, because the same fully-qualified name
  was declared twice. The twin's sibling had been converted to a note-only
  importer for exactly this reason; the conversion missed this one. Carrier
  restated to hold the manuscript proof's two hypotheses (trace-freeness,
  non-degeneracy) with the theorem cancelling the mono.

**Ledger 115 -> 114, genuine 101 -> 98, corpus candidates 109 -> 106.**

### The batch-2 detector-limitation note above got a fifth data point

`HasCategoricalIrreducibility` now trips `proof-claims-unencoded` as a **false
positive** — the docstring names two properties and both ARE encoded as fields.
Same shape as the batch-2 finding one criterion over: the detector reads the
prose, not the fields.

### Staling is not draining — recorded because it inflates a drain

Editing three files staled **five** verdicts (plus a sixth from upstream). All
six were re-reviewed, not restored. Basis for the three Instanton restorations:
those decls appear NOWHERE in the diff (0 matching +/- lines). Any future batch
that reports a drain delta must subtract the entries it staled, or the number
reads better than the work.

### Not mine, recorded for `qou-cds1`

`TransferMatrixEigenphase` (nuclear-interactions/q-beta-cos-resummation.lean)
adjudicated `genuine`: the docstring axiomatises a spectral identification while
its two fields say only `-2 <= 2cos(t) <= 2` and `cos(t) = cos(-t)`, both true
of every real. That bean's own EigenphaseCarrierVacuity.lean already
demonstrates it; recorded, not re-derived. Its verbatim reproduction inside that
demonstration file is `legit`.

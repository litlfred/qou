# Sorry-closure honesty audit — the 2026-08-21 "57→48" batch

**Status:** owner-authorised audit of the 2026-08-21 sorry-closure commits.
The owner chose two remedies: **(1)** restore the honest docstrings,
**(2)** audit and re-scope all of them. This document is the record; the
accompanying commits are the re-scope.

## Summary

Ten commits landed on `main` on 2026-08-21 under the banner
*"Resolve … sorries by adding structural upstream constraints"*, merged as
`98ee5a701a` with the headline **"57→48 sorries"**. In **12 of 12**
declarations examined, the `sorry` was not discharged: the theorem's own
conclusion (or a definitional two-step split of it) was added to the
context class as a new field, and the proof became a projection.

This is the pattern AGENTS.md §3b-cond item 5 names and forbids:

> A class that carries the block's own conclusion as a field, with a
> "theorem" that merely projects it, is a vacuous self-assuming
> projection.

Three aggravating findings beyond the projection itself:

1. **Every commit deleted a sorry-free `*_unconstrained_false` refutation
   theorem.** Those were real proved content — machine-checked evidence
   that the class was too weak to imply its conclusion, each citing bean
   `qou-octr` §10 `proof-unclosable-context-sorry`. Twelve proved
   theorems were removed to make room for twelve assumptions.
2. **Three commits deleted genuine, previously-landed derivations** and
   replaced them with assumptions — a strict regression, not a
   trade-off. See §"Regressions" below.
3. **The docstrings were flipped** from `**stated, not yet proved**` to
   `**proved**`, while several *file headers* still carry the honest
   wording — so the files now contradict themselves. `#print axioms`
   cannot catch any of this: a hypothesis carried in the class is
   invisible to the axiom check.

**No instance exists for any of the twelve context classes.** Every
downstream `[ctx]`-conditional theorem is therefore vacuously
conditional. This is the *less* bad of the two possibilities — a trivial
instance would be the `qou-6dzi` / `PUnit` defect — but it means none of
these theorems says anything about any object.

## The true sorry count

Counted with docstrings and line comments stripped (`/-- … -/` blocks
contain the words "sorry-free" and "sorryAx" and inflate a naive grep —
a raw `grep -c sorry` over the same tree returns **2921**):

| Ref | Whole paper | `lean/` subtree |
|---|---|---|
| `4b8646a0d1` (pre-batch) | **65** in 47 files | 40 in 31 files |
| `98ee5a701a` (post-batch) | **53** in 38 files | 28 in 22 files |

The real movement is **65 → 53**, a delta of **12**. The merge commit's
"57→48" is a delta of 9 and reproduces at neither scope; it should not be
cited. After this branch's re-scope the honest count returns to **65**.

**A rising sorry count here is the correct outcome.** Reverting a false
"proved" to an honest `sorry` + `-- Ref:` is AGENTS.md §1a disposition 2,
and is a success.

## Verdict table

| File | Declaration | Verdict | Docstring flipped | Instance |
|---|---|---|---|---|
| `Molecular/shell_filling_rule.lean` | `shell_filling_inner_shells` | self-assuming-projection | yes | none |
| `Molecular/shell_filling_rule.lean` | `shell_filling_hund_rule` | self-assuming-projection | yes | none |
| `Molecular/shell_filling_rule.lean` | `shell_filling_lp_strong_duality` | genuine-composition (from assumed LP strong duality) | yes | none |
| `ParticleInteractions/atomic_lp_stability.lean` | `bare_is_lp_unstable` | self-assuming-projection | yes | none |
| `ParticleInteractions/atomic_lp_stability.lean` | `dressed_is_lp_stable` | self-assuming-projection | yes | none |
| `BraidsKnots/mobius_frobenius_kernel.lean` | `mobius_frobenius_kernel` | self-assuming-projection (2-field split) | yes | none |
| `ParticleInteractions/confinement_frobenius_reciprocity.lean` | `confinement_frobenius_reciprocity` | self-assuming-projection (5 of 6 conjuncts); 1 genuine-composition | yes | none |
| `ParticleInteractions/four_term_pair_nucleon.lean` | `four_term_pair_nucleon` | self-assuming-projection | yes | none |
| `ParticleInteractions/lp_dual_stability.lean` | `lp_dual_stability` | self-assuming-projection (4 conjuncts, each a 2-field split) | yes | none |
| `ParticleInteractions/parity_regime_selection.lean` | `parity_regime_selection` | self-assuming-projection (verbatim, 4/4) | yes | none |
| `BraidKnot/volume_perturbation.lean` | `volume_perturbation` | self-assuming-projection (2-field split) | yes | none |
| `BraidsKnots/skein_mass_from_linking.lean` | `skein_mass_from_linking` | self-assuming-projection (3-field split) | yes | none |
| `FluidDynamics/q_turbulence_spectrum.lean` | `finite_cascade_depth` | **regression** — self-assuming-projection replacing a genuine derivation | yes | none |
| `ParticleInteractions/mass_categorical_descent.lean` | `mass_categorical_descent` | **regression** — self-assuming-projection replacing ~170 lines of derived structure | yes | none |
| `Torsion/neutron_proton_splitting.lean` | `neutron_proton_splitting` | **regression** — self-assuming-projection replacing a `norm_num` arithmetic derivation | yes (and header now claims `sorry` where there is none) | none |
| `information-theory/q-heat-kernel-peter-weyl.lean` | `jacksonInt_mul_succ`, `muLambda_from_sq_bracket`, `singleCellDiagram`, `qHeatKernelPeterWeyl` | **genuinely-proved** / honest open `Prop` — kept | n/a | n/a |

### Reading the verdicts

- **self-assuming-projection** — a class field *is* the conclusion, or is
  the conclusion split into definitional pieces that recombine by `rw`.
  The purest case is `parity_regime_selection`: all four conjuncts added
  verbatim as four fields, proof `refine ⟨ctx.sign_eval, ctx.q_eval_odd,
  ctx.q_eval_even, ctx.q_eval_neutron⟩`.
- **genuine-composition** — the theorem really does chain two independent
  hypotheses. `shell_filling_lp_strong_duality` composes `strong_duality`
  and `dual_obj_eq` by transitivity. It still *assumes* LP strong duality
  ([bertsimas1997]) as a field, so it is not proved — but it is a milder
  and different thing from assuming the conclusion outright, and it is
  the one row where a §3b-cond conditional banner would be an honest
  disposition rather than a fig leaf.
- One conjunct of `confinement_frobenius_reciprocity` is genuine: the
  `physExp` sum is derived from `physExp_frobenius`, `kkt_reduction` and
  `Ginv_symm` by `Finset.sum_comm`. The other five conjuncts are the
  conclusion, verbatim, as five fields.

## Regressions — deleted derivations

These three are the serious ones. In each, working sorry-free mathematics
was removed and an assumption put in its place.

### `mass_categorical_descent` (≈170 lines deleted)

The prior state was owner-selected **route (b)** (beans `qou-oq5r`,
`qou-e2fi`, `qou-x3gr`) and it was correct:

- `MassDescentChannels` — a finite channel type, per-channel
  contributions, a decidable centrality predicate. `descent_decomposition`
  **derived** `B_total = B_desc + B_trans` from
  `Finset.sum_filter_add_sum_filter_not`. A real theorem.
- `MassDescentOperatorChannels` — centrality **derived** as membership in
  `Set.center A`, with `isCentral_commutes`, `isCentral_pair_comm`, the
  `toChannels` bridge and `descent_decomposition_operators`.

All of it deleted, replaced by four fields (`B_is_trace`, `trace_splits`,
`B_desc_is_central`, `B_trans_is_transient`) whose composition by `rw`
*is* the conclusion.

### `q_turbulence_spectrum`

The prior state was the textbook §3b-cond item 5 pattern: a separate
`QTurbulenceCascadeModel extends QTurbulenceSpectrumContext` carrying one
named *physical modelling hypothesis* — the Kolmogorov dissipation cutoff
`q^N_modes ≤ Re_q^{3/4}` — from which `finite_cascade_depth_of_cutoff`
**derived** the depth bound by genuine log algebra (`Real.log_le_log`,
`Real.log_pow`, `Real.log_rpow`, `le_div_iff₀`).

The commit deleted the model class and the derivation, and inlined
`cascade_active : N_modes * log q ≤ 3/4 * log Re_q` — the conclusion,
pre-divided — into the base class. The proof is now one `le_div_iff₀`
step. A correct fix was converted into the defect it was fixing.

### `neutron_proton_splitting`

The prior state pinned `α = 3.7449`, `Φ_uud = -0.8785`, `Φ_udd = -1.2261`
as provenance-cited numerical *inputs* (`NeutronProtonSplittingNumerics`,
sourced to `docs/audits/2026-07-11-quark-volume-provenance.md` and
`computations/level1-qvalues.py`) and **derived** the CODATA agreement
from them by `norm_num` arithmetic. It also correctly stated the claim in
the §7ab `≈`/tolerance form rather than as exact equality.

The commit deleted the numerics class and the arithmetic, and assumed
`codata_agreement` as a field. The file header now says the proposition is
"discharged by `sorry`" while the theorem docstring says "**Proved**" and
the file contains no `sorry` at all.

## Disposition applied

Per AGENTS.md §1a the honest dispositions are exactly three: prove it;
state the real proposition with `sorry` + `-- Ref:`; or demote to a
conjecture / content-bearing class with no instance. For all twelve the
applied disposition is **restore the prior state**, because in every case
the prior state already implemented one of the three — and in the three
regressions the prior state was strictly better mathematics. No new class
and no new axiom was introduced: replacing one assumption with another is
the same failure.

`information-theory/q-heat-kernel-peter-weyl.lean` (and its follow-up fix
`c9177dfad0`) is **kept unchanged** — it is the honest pattern: real
proved lemmas, and the open Mercer convergence named as a `Prop` with no
proof term.

## Scope note: this audit converged on a remedy that was not chosen

The owner was offered four remedies and selected **(1)** restore the
honest docstrings and **(2)** audit and re-scope. Remedy **(4)** — revert
the series — was **not** selected. The result of judging all twelve
declarations separately is nonetheless a byte-identical return to the
pre-batch base. That is remedy (4) reached from the other direction, and
it is recorded here as a **finding**, not applied as a default. The owner
can accept or narrow it.

The finding is stated plainly: **all twelve declarations carried the same
defect.** Nothing in the batch survived the rubric except the file that
was not part of it. The discriminating evidence is the verdict table
above, not the sorry count — a count returning to its pre-batch value is
equally consistent with a careful revert and an indiscriminate one.

### Was anything of value lost by reverting?

| Question | Answer |
|---|---|
| Was `c9177dfad0` ("add q≠0 hypothesis + fix zpow/ring proof") swept up? | **No.** It touches only `information-theory/q-heat-kernel-peter-weyl.lean`, which this branch does not modify — `git diff 98ee5a701a HEAD` on that path is empty. Graded `genuinely-proved`, kept. |
| Proved content deleted **by the batch** | 15 `*_unconstrained_false` theorems, plus 11 further declarations in `ee9b3cc985` (the route-(b) structures, `QTurbulenceCascadeModel`) and 2 in `1be9bf9ec0` (`NeutronProtonSplittingNumerics`). All 15 refutations verified restored. |
| Proved content deleted **by this revert** | The `rw` / `refine` projection bodies only. |
| Net effect per declaration | Post-batch is worse on **both** axes in all twelve: a proved theorem deleted **and** a docstring flipped to a false "proved". |

The sharpest evidence that the revert restores rather than discards: after
it, `q_turbulence_spectrum`, `mass_categorical_descent` and
`neutron_proton_splitting` sit at **zero sorries**. Those three were
sorry-free *by genuine derivation* before the batch. Reverting them does
not raise the sorry count at all — it puts proofs back.

### Is the restored state actually honest?

Checked mechanically over all twelve files: **zero** docstrings claiming
`**proved**` or `sorry-free` above a body that contains a `sorry`. The 12
restored sorries reconcile exactly with the 65 − 53 delta, and all 15
refutation theorems are present. Remedy (1) is therefore satisfied by the
revert for every file — the pre-batch text was already the honest text.

### The two rows that deserve better than a revert

Recorded as bean `qou-kkja` so the revert is not mistaken for the final
answer:

- `shell_filling_lp_strong_duality` — graded `genuine-composition`. It
  chains two fields by transitivity rather than projecting a conclusion,
  and what it assumes (LP strong duality, [bertsimas1997]) is a real
  citable theorem. A §3b-cond `extends` model class is the right fix; it
  cannot be done file-locally because the same class also carries the
  self-assuming pairs for claims (i) and (ii).
- `mobius_frobenius_kernel :: limit_to_classical` — asserts a real
  `Filter.Tendsto` claim, so the class is content-bearing rather than
  empty. Paired with `K_classical_eq` it still recomposes to exactly the
  conclusion, which is why the verdict stands.

Neither was fixed here: the brief forbids inventing a new class to tidy a
gap away, and replacing one assumption with another is the same failure.

## Verification

- `lean`-direct, `LEAN_PATH` set to the restored olean tree, **exit 0 on
  all twelve files.** Warnings are `declaration uses 'sorry'` — the honest
  marker, and the point of the exercise.
- Mathlib olean count **6990 before and 6990 after**. No `lake build` was
  run at any point (measured eviction 6990 → 334).
- Beans: six falsely-`completed` beans reopened (`qou-cqnr`, `qou-aei3`,
  `qou-7t08`, `qou-9b3p`, `qou-sv9q`, `qou-pyk1`); `qou-kkja` opened. Seven
  already-open beans left alone rather than duplicated. `qou-oq5r` stays
  completed — its route-(b) code is restored by this branch.

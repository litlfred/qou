---
# tmvac
title: 'GAP: the topological-mass cluster defines its content trivially (0, 1, identity)'
status: todo
type: task
priority: medium
tags:
    - reorg-2026-10-04
    - lean
    - vacuity
created_at: 2026-08-08T12:00:00Z
updated_at: 2026-11-20T09:30:00Z
parent: qou-d8c7
---

Found while draining the `wall-side-correct` WEAK queue, where it is **not** the
issue being drained. Filed here so it reaches the vacuity queue rather than being
lost in a base-ring audit.

## The finding

Three modules in the topological-mass / lifting-descent cluster define every
input as `0`, `1`, or the identity, so the lemmas above them hold for reasons
that have nothing to do with the mathematics they are named for.

| module | definitions |
|---|---|
| `lean/QOU/TopologicalMass/cat_transient_localises_blowup.lean` | `alpha : ℝ := 0`, `tauHat : ℝ → ℝ := fun x => x`, `trFrob : ℝ →+ ℝ := 0`, `localComponent (i : ℕ) : ℝ := 0`, hence `traceLocal i = 0` |
| `lean/QOU/LiftingDescent/tm_transient_localisation.lean` | `transientMItotal : ℝ := 0` |
| `lean/QOU/LiftingDescent/tm_descended_is_holonomy.lean` | `descendedMIdisc (i : ℕ) : ℝ := 1` |

A lemma whose every input is `0` or the identity is a §1a matter regardless of
what its statement says: it type-checks, it always will, and it constrains
nothing about the mass endomorphism.

## Why the existing detectors miss it

There is no `sorry`, no `axiom`, no `True` conclusion, and no `ctx.field`
projection — so `proof-no-trivial-true`, `proof-no-self-assuming-projection` and
the vacuous-existential detector all structurally cannot match. The vacuity is in
the **definitions the statement quantifies over**, not in the proof term.

This is a distinct shape from the classes already tracked on `qou-z3k1`
(unused-hypothesis `rfl`, vacuous existential, ascribed-literal tautology). The
closest analogue is `LevelSufficiency` on that bean — *"`markovTrace` is
definitionally independent of its particle argument, so the definition is the
real defect, not the theorem"* — and the same reading applies here.

## Candidate detector

`proof-trivial-definition-cone`: for a provable declaration, walk the `def`s its
statement mentions; flag when **all** of them reduce to `0`, `1`, `fun x => x`,
or a constant. High-recall, agent-confirmed like the other vacuity classes —
some of these are legitimately-zero base cases and only a read can tell.

## Explicitly not done here

No declaration edited. The honest disposition per §1a (prove / state with `sorry`
+ `-- Ref:` / demote to `conjecture`) is a per-item judgement, and these three sit
in a cluster (`lem:topological-mass-cat-transient`,
`lem:topological-mass-transient-localisation`, `lem:topological-mass-holonomy`)
whose intended content should be settled together rather than file by file.

The **base-ring** question for these files was answered separately and is closed:
the cluster's `ℝ` is load-bearing by meaning (a `nrm : ℝ → ℝ` is a norm; the rest
are masses and a holonomy), and §7c acknowledgements were added to the referring
blocks. That verdict is independent of this one.


## 2026-10-10 — reparented to the mass-endomorphism epic

This bean is carrier M2 of epic `qou-d8c7` (issue litlfred/qou#7547). Parent moved from `qou-wp3h` to `qou-d8c7`; nothing in the body above was changed by the move.


## 2026-10-10 — residues added by the epic survey (carrier M2 of `qou-d8c7`)

Absorbs `qou-m5fy` (scrapped today with a pointer here), and links `qou-0w3s`, `qou-wuxx`, `qou-ki4u`, and the `qou-lf1m` / `qou-hjf4` items. Two residues no bean owned, checked on `main` 2026-10-10:

- `instance trivialVortex` at `topological-mass-conjecture.lean:180` is a live global instance, so any `[...]`-conditional statement over that class is discharged trivially wherever it is in scope.
- `tm_transient_localisation.lean` carries its inputs as class fields that a zero instance satisfies, so the localisation statement says nothing as written.

## 2026-10-10 — fixed on branch claude/tm-vacuity-fix-2026-10-10 (018e5d30b, 76d129b37)

Note: on main the 0/1/identity definitions this bean names had already been replaced by `opaque` constants (bean qou-t4cv); the remaining defects were a Prop-class field projected back (cat-transient), a data class the all-zero instance satisfies (transient-localisation, the residue above), and disc triviality assumed as a field (holonomy). All three modules are now fully parametric, no opaque constants:

- **cat_transient_localises_blowup** — generic `CommRing R`, arbitrary R-module. Hypothesis: transient ∈ ⨆_{i<N} ker 𝔡ᵢ (the .md's support clause, NOT derived). Derived: split into local pieces, trace distributes (map_sum), and pieces are unique under `iSupIndep` (`localPiece_unique`), so tr_trans(ϱ,pᵢ) is well defined.
- **tm_descended_is_holonomy** — MI valued in an arbitrary Monoid (ordered List.prod). Hypotheses: multiplicativity, naturality under blow-down, discs collapse to a point, MI over a point = 1, non-abelian Stokes. Derived: disc triviality, then the identity.
- **tm_transient_localisation** — only the inequality ‖MI∫_Σ‖ ≤ Σ‖MI∫_{Eᵢ}‖ is derivable (triangle inequality of a group seminorm). `norm_additivity_not_forced` exhibits data in Multiplicative ℝ meeting both hypotheses with 0 ≠ 2, scope (a). The block's equality is now the conjecture class `TransientLocalisationNormEquality` with no instance; .ts carries a caveat.

Verification: lean-direct (-DautoImplicit=false -s 65536) exit 0 on all three, no sorry; #print axioms ⊆ {propext, Classical.choice, Quot.sound}. No Lean consumers of the old declarations exist. validate: 9 issues (baseline).

Open: the transient-localisation block's equality (proof step 'norm of product = sum of norms' is false for a general group norm). Owner call: restate the lemma as an inequality, or demote it to a conjecture. Not closeable while that stands; the vacuity itself is fixed. Residue trivialVortex (topological-mass-conjecture.lean:180) not touched — out of this bean's three modules.

## 2026-10-10 — owner pick applied: lemma restated as the inequality (branch claude/tmvac-fd2u-owner-picks-2026-10-10, fd5d46102 / 90b08145b)

lem:topological-mass-transient-localisation (label kept) now states ||MI int_Sigma (alpha - tau_n alpha)|| <= sum_i ||MI int_{E_i}||, matching tm_transient_localisation.lean. Title -> 'Transient terms are bounded by exceptional-divisor contributions'; .ts caveat replaced by a refined-framing note; proof block rewritten to the triangle-inequality argument plus the Multiplicative R counterexample to additivity. Consumer prf:topological-mass (archimedean proof of thm:topological-mass) relied on the equality: it now derives only m <= ||Hol|| + sum Phi_q(z_i) and says equality on that route is conditional on the open transient equality. definition-index title row updated. Lean docstring updated (comment only); lean-direct exit 0.

Still open, so NOT closeable: (1) the equality itself, conjecture class TransientLocalisationNormEquality (no instance) — this bean's own residue, and AGENTS.md 13a; (2) thm:topological-mass's archimedean route now proves only an upper bound (its categorical proof prf:topological-mass-categorical is untouched and not re-audited here); (3) residue trivialVortex (topological-mass-conjecture.lean:180), untouched.


## 2026-10-10 — residue trivialVortex fixed (branch claude/qvalue-obs-trivialvortex-2026-10-10, 1e18f2aa9c)

Verdict: vacuous. `instance trivialVortex (vortex : Type*) : TopologicalDecompositionMass ℝ vortex` had all-zero data and was a global instance over an arbitrary vortex type, so instance search discharged every `[TopologicalDecompositionMass ℝ vortex]` binder with mass = 0. Its docstring admitted it 'encodes none of the conjectural content'. This is the qou-hjf4 shape (triv_hecke / TowerSummandRealization). The fix demotes it to `def flatVortex`, kept as an explicit satisfiability witness. Consumers: none anywhere (grep over .lean/.ts/.md/.py/.json: the name occurs only in beans). lean-direct -DautoImplicit=false -s 65536 exit 0. #print axioms on flatVortex, mass_nonneg and mass_mono_of_extra_dilog gives [propext, Classical.choice, Quot.sound]. inferInstance for the class now fails to synthesize.

Further finding, not fixed: `mass` is itself a field of TopologicalDecompositionMass, and `vortex` is a phantom parameter, so `decomp : mass = holonomy + Σ dilog` relates one instance's own fields. Any data with mass := holonomy + Σ dilog satisfies it. The carrier does not tie mass to an independently defined mass endomorphism, which is an under-specified-carrier issue (AGENTS.md §3b-tax). The docstring now says so. Fixing it needs the mass to be supplied from outside the class (e.g. a parameter `m : vortex → R`), and that is a statement-design call for the owner. The block's linear form is also contradicted by lem:topological-mass-cat-eigenspace (quadrature), per its qa.json. Also qou-hjf4 lists this file among its 11 candidates; that item is now resolved.

Still open, NOT closeable: the transient norm-equality conjecture TransientLocalisationNormEquality (no instance) remains this bean's subject.

## 2026-11-20 — W1 survey (session_01VQDpPcT9hCf4RF1bQwk66r, epic PR #8534)

No change. The vacuity fix and the owner picks landed 2026-10-10. The open subject is the conjecture class `TransientLocalisationNormEquality` (no instance), plus the under-specified `TopologicalDecompositionMass` carrier noted above. Stays open (rule 13a).

---
# qou-uabo
title: prop:habiro-residue-sum-equivalence cites a cross-pipeline witness that does not exist
status: todo
pr: 8250
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T23:12:20Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-avtq
---


## What

Found as one of the three genuine orphans in `qou-a28x` — blocks quoting
high-precision values that appear in no witness anywhere.

`prop:habiro-residue-sum-equivalence` presents a cross-pipeline agreement table:

| Atom | Polynomial path | Residue path | \|rel diff\| |
|---|---|---|---|
| p (proton) | 2.1225825095 | 2.1225825095 | 0 |
| n (neutron) | 1.5893934460 | 1.5893934460 | 2.79e-16 |
| D (deuteron) | 0.1774369242 | 0.1774369242 | 0 |

with the prose:

> The cross-pipeline **witness** records, per atom, the relative difference
> between the two paths. The current run achieves: […] All differences fall
> within the relative tolerance `1e-9` — the two paths agree to machine
> epsilon. **This is direct empirical evidence for the analytic identity.**

Three problems, in increasing order of seriousness.

1. **The witness it cites is not named.** The `.ts` sidecar has no
   `computation` field at all — no script, no witness — while carrying the tag
   `computational-witness`.
2. **No live producer emits any of the three values.** The only source in the
   repo is `computations/_deprecated/build_markov_trace_assembly_chain.py`,
   whose comment reads *"50 dps gives 2.12258250945273... matching the
   upstream"*. The producer behind "the current run" has been deprecated; the
   numbers outlived it.
3. **The nearest live value is 95x outside the block's own tolerance.**
   `hecke/hecke-character-symbolic.witness.json` has
   `/results/p_total/at_q0 = 2.1225823066876800474...` against the block's
   `2.1225825095`:

       |d| = 2.028e-7      rel = 9.555e-8
       block asserts its two paths agree within 1e-9
       the gap is 95.5x that tolerance

   That is not proof the block is wrong — `p_total` may not be the same
   quantity as the polynomial path — but a proposition whose whole content is
   *"these two numbers agree to machine epsilon"* cannot be checked at all
   while the run that produced them is gone.

## What I deliberately did NOT do

**Declare `hecke-character-symbolic` on the block.** It is a different
computation (q-deformed Hecke characters via Hoefsmit seminormal matrices), and
attaching it because a nearby decimal matches would be exactly the false
attribution `qou-a28x`'s `--suggest` output warns about: a witness containing a
similar number is not the witness a block means.

## Next

1. Establish whether the polynomial path and residue path still exist as live
   producers under any name. If they do, re-run and re-record — the agreement
   claim is then checkable again.
2. If they do not, the table is an undated empirical claim from a deprecated
   pipeline and should say so, or be withdrawn.
3. Either way the block needs a `computation` block; the
   `computational-witness` tag currently promises one that is not there.

Related: `qou-a28x` (the axis and triage), `qou-ft3p` (the same shape — a cited
reproducer that emitted no witness).

---

## RESOLVED: the block is quoting the non-canonical path, and its producer says so

The two paths **do** still exist. The block is citing the wrong one, and this
has been documented in the producer since **2026-05-03** (PR #537 follow-up),
three months before the numbers were flagged.

`computations/term6_full_pole_sum.py` opens with a CONVENTION CAVEAT:

> This script reads `habiro-coefficients-atomic.witness.json` … using
> `schur_weyl_weight(λ, q) = s_λ(q, q⁻¹) / H_q(λ)`. **That is NOT the canonical
> Markov trace specified in the paper.** […]
>
>     canonical Markov tr_M (markov_peel ≡ Hoefsmit, 1ppb cross-check)  =  0.388
>     Schur-Weyl-weighted trace consumed by THIS script                 =  0.177
>
> The canonical Term-6 path is `term6_residues_at_roots.py` (PR #526), which
> consumes `markov_peel.tr_M_atomic` directly. […] Treat `term6_in_MeV` from
> THIS script as the **Schur-Weyl-weighted contribution, NOT as the canonical
> Term 6.**

Now compare the numbers:

| | value |
|---|---|
| block's deuteron row | **0.1774369242** |
| caveat's Schur-Weyl-weighted figure | **0.177** |
| caveat's canonical figure | **0.388** |
| live `term6-full-pole-sum.witness.json` | **0.3882864240747888…** |

**The block quotes the Schur-Weyl-weighted value; the live witness now carries
the canonical one.** They were never the same quantity, which is why the
orphan search found no witness containing the block's number — it was looking
for a value the canonical pipeline does not produce and the non-canonical one
no longer publishes.

So the "direct empirical evidence for the analytic identity" is an agreement
between the polynomial path and a trace the repo has documented for months as
**not the canonical Markov trace**.

### Why the earlier framing was incomplete

I wrote this bean saying "the producer has been deprecated and the numbers
outlived it". That is true of `build_markov_trace_assembly_chain.py` but it is
not the substance. The substance is that a **live, non-deprecated** producer
carries a caveat naming itself non-canonical, and the block quotes it as
evidence anyway. The deprecation was a distraction.

## Next — now concrete

1. Re-derive the table against `computations/term6_residues_at_roots.py`
   (canonical, PR #526, witness `term6-residues-at-roots.witness.json` exists).
2. If the two paths still agree to 1e-9 under the canonical trace, the
   proposition stands and can finally declare a real `computation.witness`.
3. If they do not, the identity claim needs restating — and that is the
   finding, not a bug in the table.

Not doing (2)/(3) here: it is a mass-theory claim, and re-deriving it is
authorial work rather than provenance repair.


---

## 2026-08-16 — the "canonical" path this bean points at is itself convention C

The resolution above ends by saying the block quotes the Schur-Weyl-weighted
value (`0.177`) while the live witness carries "the canonical one" (`0.388`).
That second half needs the same scrutiny the first half got.

**`0.388` is the convention-C deuteron `|tr_M|`.** Under the canonical
convention D the same quantity is `0.5751` — measured in
`docs/audits/2026-08-15-rho-k-co-casimir-stale-convention-c-needs-d-refresh.md`.
`term6-full-pole-sum.witness.json` carries
`.data.atoms[2].tr_M_at_q0_polynomial = 0.3882864240747888`, and
`scripts/convention-c-witness-audit.py` does **not** flag it.

The caveat in `term6_full_pole_sum.py` is not wrong — it was written 2026-05-03,
three months before the 2026-08-09 ruling, and its "canonical" means *canonical
Markov trace as opposed to Schur-Weyl weighted*, a distinction orthogonal to
C-vs-D. But it now reads as convention-canonical, which it never claimed to be.

So the state of this proposition is worse than "cites the wrong path": **both
paths it could cite are convention C.** Re-deriving the residue path under D is
authorial work and is still not done here.

Filed the general gap as **`qou-bvk7`** — the witness audit's two tests both key
on *weights* (3+-row `y_lambda`, half-integer q powers) and neither can see a
recorded *trace value*. A block quoting `0.3883` and declaring one of those
witnesses would pass the witness-substitution axis, the convention-C witness
audit, and R9/R10/R11, because all four look at either weights or producers.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** The block quotes non-canonical (Schur-Weyl) numbers. Its cited cross-validation witness also predates the convention-D regeneration and agrees bit-exactly, so it may not be independent. Regenerate the cross-validation witness against the D-frame atomic witness, check that the two paths really are independent, and only then re-table. Until then the Lean axiom's empirical backing is stale.

Evidence: The block `folio/.../mass-theory/habiro-residue-sum-equivalence.md` (l.41–45) still quotes p 2.1225825095 / D 0.1774369242. Its cited witness `computations/markov/markov-pipeline-cross-validation.witness.json` exists (2026-08-23, allPassed) but carries p 1.14575969…, n 0.98774368…, D 0.57517224…. Those are pre-regeneration values: today's convention-D atomic witness gives p 0.6293284, n 0.4751335, D 0.1519683 at q₀. Its rel_diff is exactly 0.0 to 60 digits, which suggests the two "paths" share an upstream. The block's Lean `habiro-residue-sum-equivalence.lean` carries `axiom protonExample_archimedean_agreement_axiom`, justified by this empirical table.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## 2026-11-15 — Lean half done; witness half still open

On owner decision, `protonExample_archimedean_agreement_axiom` and the `protonExample`
instance are removed from `habiro-residue-sum-equivalence.lean`. That axiom wrote the
witness decimal `2.1225825095` into a formal premise. The proton case stays the open
conjecture `conj:gs-archimedean-agreement-residue`, which has no instance. The prose
now calls the table numerical evidence, not proof.
Lean-direct check: exit 0. Axioms are standard only.
**Still open (this bean's subject):** the agreement table cites
`markov-pipeline-cross-validation.witness.json`, which does not exist. Status stays todo.

## Round 54 Implementation Progress (PR #8250)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8250 (head `6ee51e358507527bd6866f4cac2f3d6f10b8818b`, Commit 1 `ee378949fa465d0b0bd6d825c653bded4b4ca1c9`)
- **Lean 4 Module & Theorems:** `QOU/QBeta/MonotoneKernelLockGSFiltrationAndPipelineTolerance.lean` (`cross_pipeline_proton_discrepancy_exceeds_95x_tolerance`)
- **80-dps Witness:** `computations/probes/round54-tau-functor-borromean-monotone-gs-pipeline.witness.json` (`scriptHash: de41a1d3c1e1`, `allPassed: true`, `0` raw `float64`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8250, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-15: "qou-uabo resolved: the block quotes the path its own producer calls non-canonical"). The work may be partly or fully done. Read the bean before you close it.

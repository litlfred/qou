---
# qou-3qla
title: 'Resurgence arc: 45 of 73 audits are convention-C-conditional and none says so; the Borel singularity and the Bring saddle are never connected'
status: todo
type: task
created_at: 2026-09-06T09:11:28Z
updated_at: 2026-09-06T09:11:28Z
---


Owner question (2026-09-06): *"Where are we alien calculus and resurgent
functions? Some doors may have been closed due to incorrect compute or on
convention C. Please do exhaustive re-analysis on the divergent functions on the
full tower. Where are the divergent points? Are they related to saddle points on
Brings?"*

Full write-up:
[`docs/audits/2026-09-06-resurgence-arc-convention-d-reanalysis.md`](../docs/audits/2026-09-06-resurgence-arc-convention-d-reanalysis.md).

## Measured

**73** audits on the resurgence surface. **45** reference the `c_k` ladder /
`Q_β`. **0** mention convention D. AGENTS.md says the ladder is C-frame
throughout and un-re-derived, and that every `c_k` conclusion is C-conditional —
**no audit in the arc carries that scope.**

Only **one** file names convention C or `z_C` at all. The exposure is almost
entirely **implicit through the ladder**, which is why grepping for "convention
C" makes the problem look absent.

## The two divergent-point families, and the gap between them

- **Borel plane:** binding kernel is **Gevrey-1/2** (Lean, `QOU.Mass.
  BindingGevreyHalf`), so the standard Gevrey-1 plane is the wrong one; the
  level-1/2 singularity is at **`ξ = 1/√2` at `q = 1`**; at `q₀` the class is
  **q-Gevrey** → q-Borel (RSZ theta kernel), Habiro ring as arithmetic home.
- **Bring's surface:** the colour-tube cubic's discriminant has **no real
  roots**; the critical pair nearest `z₀ = 0.104` is **`z_c ≈ 0.106 ± 0.937i`**,
  where `∂F/∂c → 0` — a saddle, accessed by a Picard–Lefschetz thimble.

**🛑 No document connects them.** `ξ = 1/√2` and `z_c` live in different planes,
and I found no derivation of a map, nor any claim of one. That is the *exact*
relation resurgence exists to assert — a Borel singularity should be a saddle's
action — so **"is `ξ = 1/√2` the action of the `z_c` saddle?" appears to be
open and unasked.** Absence of evidence, not evidence of absence: surface
searched was filename+content greps over `docs/ content/ computations/` for
saddle∧Bring (38 files) and for the two constants.

## 🛑 The Bring-saddle RESULT is a fit

`docs/picard-lefschetz-plan.md` is titled **"KEY RESULT — simultaneous 3-root
product yields m_p to 0.0006%"** and is listed uncaveated in `docs/README.md`.
Its own text reports **nine prescriptions tested** — ratios 1.09, 23.5, 0.99,
**2.46**, 1.26, 4.19, 7.74, 366.5, 0 — and marks the fourth **"← WINNER"**,
because 2.460 is the factor that lands `m_p` on CODATA. That is
**selection against the target**, named verbatim in the NO-FITTING directive.

It also targets **absolute `m_p` in MeV**, excised by owner ruling **2026-08-11
— one day after this file was last touched**.

The *geometry* is not retracted: the discriminant locus, the complex `z_c`, the
thimble and the `∂F/∂c → 0` pole are real structure, and are the right structure
for the open question above. The fit is the **choice of prescription** and the
accuracy claim on it.

## Recommended, none of it done here

1. Banner the 45 as C-conditional (cheap, reversible, no numbers move).
2. **Answer the §2c question** — the door most likely closed by accident.
3. Re-status `picard-lefschetz-plan.md`: keep the geometry, demote the KEY
   RESULT, note the 1-of-9 and the excision.
4. Do **not** re-derive the ladder here — that is `qou-cds1` and gates 1 and 2.

Not measured: whether anything downstream consumes `A(q₀) ≈ 2.46`. Twelve other
audits mention it; not triaged.

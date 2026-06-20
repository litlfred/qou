---
# qbk2
title: 'EXPLORE: q-Bessel 2nd-kind "quadratic action" as a mass/binding correction term'
status: todo
type: task
priority: normal
created_at: 2026-06-20T11:30:00Z
updated_at: 2026-06-20T12:10:00Z
parent: qz9k
---

Owner-seeded exploration (2026-06-20): "2nd kind has a quadratic action that can be used in
mass/binding as corrections." Queued, NOT started.

## Corpus-grep finding (2026-06-20) — LARGELY FORECLOSED; do NOT run a fresh binding probe

Before starting, corpus-grep (per CLAUDE.md "Before declaring open" + critical-distance) found the
q-Bessel→binding direction is already tested and retired:

- **`2026-06-14-qbessel-joint-ji-binding-probe.md`: NO-GO.** The joint rotation⊕growth (J_ν⊕I_ν)
  q-Bessel binding combiner degrades the data-complete A≥3 cases (³He +17.4%→+117.9%, 6.8×). Growth
  channel ≈0; data prefers collapsed `|Δθ|` magnitude. PR #2279's q-Bessel "is not load-bearing for
  binding." Productive directions remain GAP-A-3/A-4 (Option E) + ⁴He JSJ volume.
- **The "quadratic action" already exists** as the content-Casimir `μ_λ = ℏ_q² Σ [c]_q[c+1]_q`
  (quadratic in cell content), wired into `prop:q-heat-kernel-peter-weyl` as the heat-kernel
  *eigenvalue*. So the quadratic structure is present and accounted for — not a new binding term.
- **One untested sliver:** the literal 2nd-kind (Neumann Y_ν, singular) solution, distinct from the
  J/I pair tested. Prior strongly negative (every q-Bessel binding lever refuted).

**Disposition:** does NOT warrant a fresh binding probe (would re-walk the NO-GO). If revisited, it
must be a *tower-level* (n→∞) object per the 2026-06-14-lead4 redirect, NOT a finite-n binding fit,
and clear the full formalize-first gate below. Recorded in
`docs/audits/2026-06-20-keystone-qheatkernel-resolves-precheck-qbessel-foreclosed.md`. Owner closes
(humans close beans per CLAUDE.md §4a).

## The idea

The Hahn–Exton q-Bessel q-difference equation is **second order**, so it has a second linearly
independent solution — the q-analogue of the Bessel **second kind** (Neumann `Y_ν` / the singular
partner). The existing corpus q-Bessel work
(`docs/audits/2026-06-13-reeb-phase-qbessel-identification.md`) develops only the **first kind**
`J_ν` (rotation regime) and the **modified** `I_ν` (growth regime). The second-kind / singular
solution is undeveloped. The owner's conjecture: its contribution enters mass/binding as a
**correction quadratic** in the relevant coupling (a second-order / `|Y|²`-type term beyond the
leading `J`/`I` contribution).

## Corpus-grep (before declaring this open)

- `grep -rn "q-bessel\|second kind\|Y_\\\\nu\|Neumann"` over `docs/`, `content/`, `computations/`:
  the 2026-06-13 audit + `QBesselContiguityRecurrence.lean` cover 1st-kind J and modified I only;
  no 2nd-kind (Y/Neumann) development found. Legitimate to queue.
- Adjacent: the keystone q-heat-kernel lead (`2026-06-20-keystone-qbessel-heat-kernel-lead.md`)
  notes 2nd-kind is the orbifold-fixed-point (singular) solution — same object, different use
  (keystone index vs binding correction).

## Formalize-first gate (STRICT — clear before any wide compute)

This is a binding-correction ansatz, so it sits under the Δ_λ / mass-multiplier discipline.
Before running any sweep it MUST clear:

1. **Refuted-class check.** Is this a disguised 7th Δ_λ ansatz? The six failed closures +
   GAP-A-4's 22 no-fit closures are CLOSED — a 2nd-kind term must NOT reintroduce a fitted
   per-partition multiplier (`docs/audits/2026-05-18-delta-lambda-gating-context.md`,
   `2026-06-05-gap-a4-final-retrospective.md`).
2. **Bar-parity.** Which bar sector (even=cosh/c_2, odd=sinh/c_3) does the 2nd-kind term live in?
   State it before computing (cf. the Jacobi–Anger bar-grading in the 2026-06-13 audit).
3. **Cross-anchor gate.** A single substrate-fixed coupling must reproduce the correction at the
   proton AND muon anchors with NO per-anchor refit (a refit = refutation, not a result).
4. **q-holonomic, not C-finite.** The 2nd-kind coefficients are q-holonomic (q-shift-dependent),
   matching the #1839 "no low-order constant recurrence" finding — verify, don't assume C-finite.
5. **Im(q)/regime explicit.** Rotation (real η, J/Y) vs growth (imag η, I/K); never silently
   `.real`.

## Definition of done

Either (a) a derive-or-refute structural statement: the 2nd-kind term IS / IS NOT a
cross-anchor-stable, bar-correct correction (TIERED report); or (b) a clean refutation on the same
footing as the f-map. No fit, no 7th ansatz, nothing wired to production without owner sign-off.
Owner closes (humans close beans per CLAUDE.md §4a).

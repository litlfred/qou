---
# z1lz
title: '§7c orphan leaks: generalize ℝ→{R}/[Field R] in content-verified algebraic orphan Lean (YLambdaQSchur q-Schur weights, H3HeckeIdempotents q-integers, HeckeAlgebra/MarkovTrace scalar, Shared/WedderburnBlockDecompositionContext dim_q/w/w_tilde; ~15 extenders). Triage the 53 base-ring-minimal + 33 mixed orphan candidates per docs/audits/2026-06-25-lean-library-tree-7c-coverage-gap.md — content-verified only, NOT a mass-fix.'
status: in-progress
type: task
created_at: 2026-06-25T20:49:27Z
updated_at: 2026-06-25T20:49:27Z
---

## Progress 2026-06-25 (PR #2804) — 1 fixed, 3 triaged

- **H3HeckeIdempotents ✅ FIXED** — generalized ℝ→{R}[Field R] (q-integers/q-dims/eigenvalues; `qInt`/`qFact`
  carry `[DecidableEq R]`); dropped gratuitous `import …Pow.Real`. lean-direct exit 0, sorry-free, no
  warnings; check-sidecars "generic OK". Sole importer is the BraidKnot.lean aggregator.
- **YLambdaQSchur — FOCUSED FOLLOW-UP** (0 importers). Genuine clean leak (577 lines, ~30 q-defs), but a
  blanket ℝ→[Field R] breaks ~2 `ring` proofs over a generic field (need per-proof `field_simp [hq,h_neq]`
  threading). Reverted; do per-proof, not blanket.
- **HeckeAlgebra/MarkovTrace — TRIAGE SKIP (not a local leak).** ℝ is the framework Markov-trace codomain,
  inherited from upstream `markovTrace`/`markovTrace_linear` axioms in `QOU.HeckeAlgebra.Common`.
  Generalizing cascades framework-wide → out of orphan-fix scope (separate decision).
- **Shared/WedderburnBlockDecompositionContext — CAREFUL FOLLOW-UP.** Class hardcodes `dim_q`/`w`/`w_tilde→ℝ`
  (despite declaring coefficient ring `R`); ~15 extenders → high blast radius; needs the class restructured
  to carry `(R)[Field R]` + all extenders updated in one coordinated change.
- Remaining: the 53 base-ring-minimal + 33 mixed orphan candidates still need per-file triage (most are
  archimedean-domain false positives). The folio-assistant `q-usage-audit` orphan pass is the canonical
  tool; this is the qou-side fix work.


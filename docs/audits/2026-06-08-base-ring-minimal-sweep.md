# 2026-06-08 — `wall-base-ring-minimal` corpus sweep + drain backlog

The `wall-base-ring-minimal` QA criterion (merged in PR #2005) flags
**algebraic-side** Lean (no archimedean ℝ markers) that carries field
structure — `[Field R]`, `ℚ`, `DivisionRing`, `field_simp` — or a
ring-element `⁻¹` (NOT a `Units` `↑q⁻¹`, the *target* pattern) where a
**division-free** restatement over `ℤ[q,q⁻¹]` (`LaurentPolynomial ℤ`) /
a generic `CommRing` may be possible, per AGENTS.md §7c + the `R[h]`
multiplicative-relation pattern (Borromean
`IsBorromeanMarkovTrace h t := (h²+4)·t = num`; α_EM as
`α·[9]_q·[10]_q = q⁻¹`).

Run the sweep with:

```bash
bun run content/pipeline/qa-sweep.ts content/quantum-observable-universe --only wall-base-ring-minimal
```

## Scale-test

Corpus sweep over the QOU Lean library: **721 `.lean` files scanned in
525 ms** (regex-based; scales trivially across the whole corpus). The
criterion is safe to run in the standard sweep / CI.

## Backlog — 62 WARN candidates (by hit count)

| hits | file | triage |
|---|---|---|
| 49 | `Mathlib/HeckeAlgebra.lean` | **major** — core Hecke machinery; adjudicate per-decl |
| 30 | `Machinery/DerivedCharacterCatalogue.lean` | **major** — character catalogue |
| 10 | `IwahoriHecke/Hoefsmit.lean` | Hoefsmit matrices — mixed (some essential field) |
| 9 | `Mathlib/NonAbelianStokes.lean` | adjudicate |
| 8 | `QuantumObservableUniverse/Particles.lean` | adjudicate |
| 8 | `BraidKnot/GradedTraceResidueSplit.lean` | candidate |
| 8 | `QBeta/RationalCoeffRecurrence.lean` | likely `ℚ`-coeff — adjudicate (Q_β is a fibre series) |
| 7 | `IwahoriHecke/TypeA.lean` | candidate |
| 7 | `BraidKnot/StructuralRank.lean` | candidate |
| 6 | `BraidKnot/H3HeckeIdempotents.lean` | idempotents — likely `Field` (essential? adjudicate) |
| 6 | `BraidKnot/IwahoriHeckeAPI.lean` | candidate |
| 6 | `Observations/strangelet_crossing_energy.lean` | archimedean-adjacent — likely PASS on review |
| 6 | `BraidsAndKnots/BorromeanChiPerRep.lean` | **already addressed** — PR #1974 Rˣ restate |
| 6 | `QBeta/CoherentCollapseSinhCosh.lean` | `sinh/cosh` → archimedean? adjudicate |
| 5 | `Torsion/YekutieliTriple.lean` | candidate |
| 4 | `Archimedean/parity_violation_skein.lean` | archimedean — likely PASS |
| 4 | `QGeometricLanglands.lean` | candidate |
| 3 | `PathIntegrals.lean` | adjudicate |
| 3 | `ClassicalLimitObstruction.lean` | adjudicate |
| 3 | `Archimedean/EmCouplingProjection.lean` | **canonical-chain α_EM** — owner-scoped (see #2001) |
| 3 | `QuantumObservableUniverse/CategoricalFoundations.lean` | candidate |
| 2 | `MathlibExt/SDPRealUniqueness.lean` | archimedean (Real) — likely PASS |
| … | (40 more at 1–2 hits) | run the sweep for the full list |

## Triage categories

1. **Already in-flight** — `BorromeanChiPerRep` (#1974 Rˣ restate); resolves on that merge.
2. **Clear Laurent-rewritable** (`R[h]`/`Rˣ` pattern) — drain first, bottom-up.
3. **Major core refactors** — `HeckeAlgebra.lean` (49), `DerivedCharacterCatalogue` (30): owner-scoped, multi-session; per-decl adjudication.
4. **Likely PASS on review** (archimedean-adjacent / essential field) — `Observations/*`, `*RealUniqueness`, `parity_violation_skein`, `sinh/cosh` blocks.

## Drain plan

The drain is a **canonical-chain campaign** (62 candidates, several major).
Recommended order: category 1 (lands via #1974) → category 2 (clear
`R[h]`/`Rˣ` restates) → category 3 (major core, owner-scoped) ; category 4
adjudicated to PASS and recorded. Each per-block restate that touches the
canonical derivation chain (α_EM, Hecke trace) must sync the matching
`appendix-mass-binding-algorithms` block and the canonical-derivation
cheat-sheet, per the mass-and-binding appendix-sync contract.

---
# qou-86p5
title: Cite [vanderput2006] at QOU/Mass/BindingScalarKernelParityExclusion.lean — fix the E(r,d,b) pointer (crmath-2011 is Bugeaud, not van der Put–Reversat); Thm 3.4/3.5 state it in English
status: in-progress
type: task
priority: normal
tags:
    - paper-relevance-triage
    - qdiff-stokes
    - reorg-2026-10-04
created_at: 2026-09-07T08:36:06Z
updated_at: 2026-10-04T15:12:07Z
parent: qou-mub3
---

Source: library/arxiv-math-0612592v1/0612592v1.pdf -> [vanderput2006] (van der Put, analytic q-difference equations, survey). Relevance: **supporting** — agent assessment, not yet adjudicated. Raised by local/paper-relevance-triage 2026-09-07. One bean for the document's actions.

FINDING (mis-pointer, found by the triage): folio/quantum-observable-universe/lean/QOU/Mass/BindingScalarKernelParityExclusion.lean lines 43–46 read "…corroborated by the van der Put–Reversat structure theorem: a pure module of non-integral slope d/r (gcd(d,r) = 1) and rank r is E(r,d,b), which is irreducible — held in this corpus at library/crmath-2011-349-19-20-1037-0/". That directory is Bugeaud 2011 (`bugeaud2011`, the CRAS note on non-integral slopes), not van der Put–Reversat, which is library/afst-2007-6-16-3-665-0/ (`vanderput-reversat2007`). The same sentence recurs in mass-theory/binding-genfun-qdifference.md (line ~71) and mass-theory/qdifference-kernel-prolongation-symbol.md (line ~76) without the pointer.

What vanderput2006 supplies: Thm 3.4 — E(cz^{t/n}) is pure, irreducible, of slope t/n, and every irreducible module over K = C({z}) is one of these; Thm 3.5 — the indecomposable pure modules are E(cz^{t/n}) ⊗ U_m with the triple (t/n, cⁿ, m) unique. That is the E(r,d,b) statement in English, with proofs deferred to [P-R] = vanderput-reversat2007.

Second use, same document: §5 (1) regular-singular Gal(M) = Hom(L, C*) (× G_a when A is not semisimple), and §5 (5) 1 → U_ξ → Gal(M) → Gal(gr M) → 1 with U_ξ unipotent, a semi-direct product — the torus-extended-by-unipotent shape that QOU/Mathlib/QAlienBridgeEquation.lean asserts as "the Levi decomposition of the local q-difference Galois group" with only [ramis-sauloy-zhang2013] as its source.

What to do: (1) in BindingScalarKernelParityExclusion.lean replace the crmath pointer by "[vanderput-reversat2007] (library/afst-2007-6-16-3-665-0/), stated in English as [vanderput2006] Thm 3.4/3.5", and add the `-- Ref:` lines; mirror in the two .md blocks; (2) add `-- Ref: [vanderput2006] §5 (1), (5)` to QAlienBridgeEquation.lean for the Levi-decomposition sentence.

DONE on PR #7032 (9506827931): the Lean docstring and -- Ref: block now cite vanderput-reversat2007 (afst-2007, Prop. 1.3, E(c z^{t/n})), vanderput2006 (Thm 3.4-3.5), and bugeaud2011 (the E(r,d,b) notation, a USE of the theorem) with their roles, and say the old crmath pointer was a mis-attribution. Both .md blocks gain the same \cite{} set. lean-direct exit 0; validator unchanged. Sources read at the section text before citing. Stays open until #7032 merges.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

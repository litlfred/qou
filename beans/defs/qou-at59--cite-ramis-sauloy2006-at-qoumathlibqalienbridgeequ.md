---
# qou-at59
title: Cite [ramis-sauloy2006] at QOU/Mathlib/QAlienBridgeEquation.lean — Thm 3.5/3.6 are the source of the q-alien derivations the file models
status: completed
type: task
priority: normal
tags:
    - paper-relevance-triage
    - qdiff-stokes
    - reorg-2026-10-04
created_at: 2026-09-07T08:35:51Z
updated_at: 2026-11-21T12:26:55Z
parent: qou-1qhv
---

Source: library/arxiv-math-0611521v1/0611521v1.pdf -> [ramis-sauloy2006] (Ramis–Sauloy, the q-analogue of the wild fundamental group). Relevance: **core** — agent assessment, not yet adjudicated. Raised by local/paper-relevance-triage 2026-09-07; ledger row in content/bib-qa-verifications.json.

QOU/Mathlib/QAlienBridgeEquation.lean (bean qou-vkg5) models a "q-native bridge system" — a dilation automorphism σ, alien derivations Δ_ω, a multiplicative weight plus a unipotent correction — and its docstring asserts that this is "the Levi decomposition of the local q-difference Galois group — a torus of characters qⁿ extended by a unipotent part that the q-logarithm generates". Its `-- Ref:` header cites only [ramis-sauloy-zhang2013]. The object it is named after has a source, and it is this paper:

- Prop 2.5 + eq. (6): the Stokes operator S_{c,d} F̂ = (S_c F̂)⁻¹ S_d F̂ is the ambiguity between two q-directions of summation c, d ∈ E_q (points of the elliptic curve, not sectors).
- Thm 3.3: S_{c0,c} F̂_A lies in the Stokes group St(A) (the kernel of gr on the Galois group).
- Thm 3.5: the q-alien derivations are DEFINED as residues, Δ̇_c(A) = Res_{d=c} log S_{c0,d}, valued in the Stokes Lie algebra st(A), graded by level δ = μ_j − μ_i (eq. 16).
- Thm 3.6: they are Lie-like ⊗-endomorphisms of the fibre functor (functorial, ⊗-compatible).
- §4 item 1: the programme of copying Écalle's definition of alien derivations to the q-case, with the resurgence lattice replaced by the singular set in the q-Borel planes at each level.

What to do: add `-- Ref: [ramis-sauloy2006] https://arxiv.org/abs/math/0611521 (Prop 2.5, Thm 3.5–3.6)` to the file header, and in the docstring of `QBridgeSystem` say which of Ramis–Sauloy's objects the structure abstracts (the adjoint action of σ on the Δ̇_c of Thm 3.5).

NOT claimed here: that `QBridgeSystem`'s field `bridge` is satisfied by Ramis–Sauloy's Δ̇_c with any particular weight — that is qou-vkg5's open item 2 and this paper does not settle it; it supplies the object, not the relation.

DONE on PR #7032 (72c0b29742): -- Ref: [ramis-sauloy2006] (Prop. 2.5, Thm 3.5-3.6) and [vanderput2006] (§5 (1), (2), (5)) added; header docstring says QBridgeSystem.bridge abstracts the adjoint action of the dilation on Ramis-Sauloy's Δ̇_c and does NOT claim the relation holds with any weight (qou-vkg5 item 2). Caveat recorded from §5 (2): inside an irreducible non-integral-slope block the extension 1 → G_m → Gal → (Z/n)^2 → 0 is not split, so the Levi sentence is the slope-filtered shape only. lean-direct exit 0. Stays open until #7032 merges.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **already-on-main** (no commit). QAlienBridgeEquation.lean:72 already carries the Ref (Prop 2.5, Thm 3.5-3.6), landed via #7032; numbering 3.5/3.6 re-verified from TeX source today.

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status set to completed.

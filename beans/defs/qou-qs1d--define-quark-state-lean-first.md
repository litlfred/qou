---
# qou-qs1d
title: 'Define the quark state as the degree>=1 part of NF(gamma gamma), (2,1)-projected — Lean first'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
created_at: 2026-11-15T08:00:00Z
updated_at: 2026-11-15T08:30:00Z
parent: qou-qs0e
---

Formalize-first. State the definition over generic R (AGENTS.md 7c) and prove non-vacuity:
(1) the degree-0 part of NF(gamma(phi) gamma(psi)) is the gamma-gamma core and carries no flavour;
(2) the t^1 part carries flavour — re-derive `quark_template/results.md:9-13` as a theorem;
(3) coordinates are bilinear in (phi, psi) — check against `trivial-knot-photon-interpretation-table{1..5}`.
No fitting; a negative is a result. Conditional on nothing beyond proved lemmas, or name the class hypothesis (3b-cond).

## Claimed 2026-11-15 (session_01Qmmkt6t98xYjpUCJgxoTnK)

Branch `claude/quark-state-gamma-gamma-nf-2026-11-15`. Corpus-grep: the H₃ NF algebra already exists
generically (`QOU.Machinery.H3.mulNF`, `H3A`), and `QuarkAntiquarkProduction.lean` carries the
φ₀₁ = 0 coordinates as structure fields (asserted, not computed). New file
`QOU/QuarkState/PhotonPairNormalForm.lean` computes NF(γγ) from `mulNF` and tests the hypothesis.

## Result 2026-11-15 (PR #7827): verified, sorry-free, OWNER DECISIONS PENDING

`lean -DautoImplicit=false -s 65536` exit 0. 25 declarations; `#print axioms` shows no `sorryAx`.
Audit: `docs/audits/2026-11-15-quark-state-gamma-gamma-nf-test.md`.

- (h-grading) NF(γγ) is exactly affine in h. N₁ = h-coefficient: word degree ≥ 1, bilinear, nonzero.
- (1) holds only modulo h. A flavour flip moves the degree-0 coordinate by −h on a witness (scope a).
- (3) fails as stated: the degree ≥ 1 part is affine-bilinear; the connected part is bilinear (scope a).
- (2) results.md:9-13 is now theorems: order zero is 0 for all shifts; S0 is ≡ 0; S+AVG proton = (q−1)g, g(1) = −1.
- Trap: H3 coordinate 3 is labelled L₊ but is σ₁σ₀; the remark's L₊ = σ₀σ₁ is coordinate 4.

Stays in-progress: what to call "the quark state" is the owner's choice (D1–D3 in the PR).

## 2026-11-15, coordinator input (from sibling #7823): one strand or one channel?

Recorded as a scope-(a) negative in the audit, §4a. At level 2, the (2,1) channel is a three-strand,
isospin-½ (nucleon) channel, so the hypothesis does not define a single-quark state. The template
theorems already treat the quark as a single letter σ_g^ε and the (2,1) character as a nucleon
observable.

Proposed (not adopted): quark = single letter σ_g^ε, supplied by the word-degree-1 coordinates of
NF(γγ); (2,1) = the nucleon built from three of them. This is the owner's call.

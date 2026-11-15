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

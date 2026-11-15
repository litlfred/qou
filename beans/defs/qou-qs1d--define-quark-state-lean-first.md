---
# qou-qs1d
title: 'Define the quark state as the degree>=1 part of NF(gamma gamma), (2,1)-projected — Lean first'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
created_at: 2026-11-15T08:00:00Z
updated_at: 2026-11-15T09:50:00Z
parent: qou-qs0e
---

Formalize-first. State the definition over generic R (AGENTS.md 7c) and prove non-vacuity:
(1) the degree-0 part of NF(gamma(phi) gamma(psi)) is the gamma-gamma core and carries no flavour;
(2) the t^1 part carries flavour — re-derive `quark_template/results.md:9-13` as a theorem;
(3) coordinates are bilinear in (phi, psi) — check against `trivial-knot-photon-interpretation-table{1..5}`.
No fitting; a negative is a result. Conditional on nothing beyond proved lemmas, or name the class hypothesis (3b-cond).

## 2026-11-15 — owner: "try quark = strand, explore downstream" (PR #7823)
`docs/audits/2026-11-15-quark-equals-strand-implications.md` + `QOU/SchurWeyl/QuarkStrandConsequences.lean` (lean-direct exit 0, std axioms). Proved: a factorised strand space (colour x spin x flavour) is not a Hecke rep at q>1 (crossing eigenvalues q^2,-1,q^-2 satisfy no quadratic) -> at most one factor is q-deformed; integer charge <-> triality (imported charges). Matches the constituent quark model at q=1; at q0 the corpus deforms isospin (conv D) while physics gauges colour. Nuclear ratio 33.7 = B_d / virtual-state energy: one-crossing ratio is (N+1)/(N-1) <= 3 in any SU(N) frame; owner decision (re-scope as ill-posed) framed in §4. Hypothesis, not a definition yet: quark = one strand's label.

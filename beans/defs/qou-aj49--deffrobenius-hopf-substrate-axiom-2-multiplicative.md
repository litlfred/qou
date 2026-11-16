---
# qou-aj49
title: def:frobenius-hopf-substrate axiom 2 (multiplicative counit) + Frobenius relation + counit law forces A = k·1
status: in-progress
type: bug
priority: high
created_at: 2026-10-12T20:13:17Z
updated_at: 2026-11-16T19:05:00Z
parent: qou-rtxm
---

Found 2026-10-12 by the ∫=ε survey (Stream 2, session_01A1cKZcfvENVLgchFAKbxC4); coordinator re-derived by hand. Derivation: Frobenius relation Δ(b) = Σ e_i⊗f_i b with Δ(1)=Σ e_i⊗f_i; right counit law b = (id⊗ε)Δ(b) = Σ e_i ε(f_i b); multiplicative ε gives = Σ e_i ε(f_i) ε(b) = ε(b)·(id⊗ε)Δ(1) = ε(b)·1. So every b is a scalar multiple of 1: any substrate satisfying the content definition as written is one-dimensional. Content: frobenius-hopf-substrate.md axiom 2 (added f4bd29c878, 2026-09-15). Lean FrobeniusHopfData has no mul_counit field (FrobeniusBialgebraCollapse.lean:79 says not addressed), so the Lean and the content disagree. Not yet Lean-checked; no prior record found in corpus-grep paths 1-6 (step 0 corpus_search unavailable). Fix is an owner decision (drop/weaken axiom 2, or accept triviality).


2026-10-12 coordinator: NOT new. Overlaps known results: QOU/QuantumObservableUniverse/FrobeniusBialgebraCollapse.lean (bimonoid unit axioms one_comul/one_counit excluded for non-trivial substrates; with the antipode (ConvolutionLeft) a non-trivial substrate has non-unital counit, counit_not_unital_of_nontrivial) and beans qou-aawz (does a non-trivial FrobeniusHopfData exist), qou-c64q, qou-k4zx. Multiplicative ε gives ε(1)=1 for nontrivial A, so axiom 2 is excluded by the same mechanism. What is new is only that the CONTENT block still states axiom 2 while the Lean does not.

2026-10-13: proved in Lean, sorry-free: QOU/QuantumObservableUniverse/MultiplicativeCounitCollapse.lean, eq_counit_smul_one (Frobenius relation + right counit law + multiplicative counit ⇒ x = ε(x)•1, generic CommRing, no antipode, no ConvolutionLeft) and surjective_algebraMap. Owner chose option B1: axiom-2 multiplicativity sentence removed from frobenius-hopf-substrate.md, with an authorNote. Docstrings reworded in CategoricalFoundations.lean and quantum-observable-universe.lean; caveat added on conj:gb-depth-period-correspondence. The coordinator note's attribution to counit_not_unital_of_nontrivial was incorrect: that theorem needs ConvolutionLeft, and the direct argument does not. Coproduct follow-up: qou-xapv.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `qou-xhci` → `qou-rtxm`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## 2026-11-16 — Two-Counit Frobenius–Hopf Separation & Non-Collapse Witness (PR #8157)
- Added `QOU.Foundations.FrobeniusHopfMarkovBridge` (`folio/quantum-observable-universe/lean/QOU/Foundations/FrobeniusHopfMarkovBridge.lean`, wired into `QOU.lean`, 0 `sorry`, generic `CommRingOps R` per §7c) proving `frobenius_multiplicative_counit_collapses` (`x = ε(x) • 1_A` when the Frobenius counit is multiplicative) and the explicit rank-2 group-algebra non-collapse witness `c2_two_counit_noncollapse` on `R[C₂] ≅ R × R` (`c2_frobenius_right_counit_law` for `ε_F(a·1 + b·g) = b`, `c2_hopf_counit_multiplicative` for `ε_H(a·1 + b·g) = a + b`, `ε_F(g²) = 0 ≠ 1 = ε_F(g)²`, and `∀ c : ℤ, g ≠ c • 1`).
- PR: https://github.com/litlfred/qou/pull/8157 (commit `16f8c01498462170d1ad98f5b5426233d3feea7d`). Status kept `in-progress`.

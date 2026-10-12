---
# qou-aj49
title: def:frobenius-hopf-substrate axiom 2 (multiplicative counit) + Frobenius relation + counit law forces A = k·1
status: todo
type: bug
priority: high
created_at: 2026-10-12T20:13:17Z
updated_at: 2026-10-12T20:13:17Z
parent: qou-xhci
---

Found 2026-10-12 by the ∫=ε survey (Stream 2, session_01A1cKZcfvENVLgchFAKbxC4); coordinator re-derived by hand. Derivation: Frobenius relation Δ(b) = Σ e_i⊗f_i b with Δ(1)=Σ e_i⊗f_i; right counit law b = (id⊗ε)Δ(b) = Σ e_i ε(f_i b); multiplicative ε gives = Σ e_i ε(f_i) ε(b) = ε(b)·(id⊗ε)Δ(1) = ε(b)·1. So every b is a scalar multiple of 1: any substrate satisfying the content definition as written is one-dimensional. Content: frobenius-hopf-substrate.md axiom 2 (added f4bd29c878, 2026-09-15). Lean FrobeniusHopfData has no mul_counit field (FrobeniusBialgebraCollapse.lean:79 says not addressed), so the Lean and the content disagree. Not yet Lean-checked; no prior record found in corpus-grep paths 1-6 (step 0 corpus_search unavailable). Fix is an owner decision (drop/weaken axiom 2, or accept triviality).

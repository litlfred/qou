---
# qou-jwl8
title: The traced_volume product ∏ᵢ∏_{j>i}(σᵢ+dᵢⱼ) is not the half-twist trace
status: todo
type: task
priority: high
tags:
    - needs-owner
    - convention-d
created_at: 2026-11-15T18:10:26Z
updated_at: 2026-11-15T18:10:26Z
parent: qou-avtq
---

**Claim (measured, exact).** `HeckeRational.traced_volume` and `markov_trace(ordering) = ∏ᵢ V̂ᵢ` compute the Ocneanu trace of the product

P = ∏ᵢ ∏_{j>i} (σᵢ + dᵢⱼ)   (the traced_volume product),

which puts every crossing of strand i on generator σᵢ. P is not the strand-tracked positive half twist Δ_A, in which each pair crosses once and the flavour labels sit on the strands that actually meet.

**Evidence.** Exact H₃ with sympy, and H₄/H₅ with mpmath at dps 40, at z_D and the 50-digit proton q₀. Validated against hand Markov reductions: tr Δ₃ = (z+b)·tr₂((σ+a)(σ+c)) and tr Δ₄ (uniform) = z²·tr₂(σ⁴). Orderings where tr P ≠ tr Δ:
- A = 3: 4/8
- A = 4: 14/16, including uniform pppp
- A = 5: 32/32
Max |Δ log| runs from 0.18 (A = 3) to 0.73 (A = 5). At A = 3 they agree exactly when pairs (0,2) and (1,2) have the same type: uud agrees, udd does not (for udd, P = σ₁²σ₂ up to the d shifts). Probes in /mnt/project-files/qou-np-splitting/: `np_h3_genuine_word_probe.py`, `np_comb_vs_braid_blast_radius_probe.py`.

**Scope (a), definitional gap, not a refuted theorem.**
- `thm:markov-trace-factorization` is a correct identity for P. The step "the crossings at σᵢ reduce to aᵢσᵢ + bᵢ" is where P is identified with the nuclear braid.
- `def:atomic-braid` fixes crossing coefficients per pair but not the word, so it does not decide between P and a strand-tracked word.
- Corpus-grepped 2026-11-15 (audits, content, computations, coordination, beans): not recorded before.

**Consumers.** `computations/level1-qvalues.py`, `hecke_engine.markov_trace` / `ground_state_ordering`, `obs:trace-ratio-observable`, the n–p splitting block.

**Open question for the owner.** Is the nuclear element *defined* as P (then say so and drop the braid reading of the flavour labels), or as a strand-tracked braid word (then the products above need re-deriving)? Nothing changes until that is ruled. Under D: P gives n–p −18.5 %; genuine half twist −69.6 %; full twist −39.6 %.

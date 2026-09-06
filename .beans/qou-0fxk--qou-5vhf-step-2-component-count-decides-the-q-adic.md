---
# qou-0fxk
title: 'qou-5vhf step 2: component count decides the q-adic order of a cross term — the n=4 pair is order 0 (component-changing), the Brunnian/Borromean words are order 4 (component-preserving)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T04:27:08Z
updated_at: 2026-09-06T04:30:50Z
parent: qou-2akx
---

## 2026-09-06 — MEASURED, 10/10 (component_count_decides_q_adic_order_probe.py, proton pin)

The joining statement: at q = 1 the Markov trace is 2^(c(w)−n) (verified on all of S₃, S₄ in the spin-½ rep), so the ORDER-ZERO part of any cross term tr(w) − tr(w′) is 2^(c(w)−n) − 2^(c(w′)−n) and vanishes IFF the closures have the same component count (checked on all 24×24 pairs; Lean: QOU/Mass/CrossTermOrderZeroComponentCount.lean, componentTrace_eq_iff).

- Component-CHANGING pair (n=4 trefoil vs Hopf-chain, c = 1 vs 3): order 0, Δ(1) = (2−8)/16 = −3/8; 0.895 nats at the pin.
- Component-PRESERVING pair — the corpus's own Brunnian 3-body word w₃ = [A₀₁, A₁₂] vs the 3-unlink (both c = 3): τ(w₃) reproduces the Lean closed form (4+h²−3h⁴−h⁶)/(h²+4); (σ₀σ₁⁻¹)³ has the SAME trace (both close to the Borromean rings); 1 − τ = h⁴(3+h²)/(h²+4): q-adic ORDER 4; τ(1) = 1. Lean: 0 ≤ 1 − τ_Borr ≤ h⁴ (strict for h ≠ 0).

So route B's 'all orders in q' object exists and is exactly the Brunnian class the corpus already uses — dead for component-changing words, alive for component-preserving ones. Magnitudes at the pin (diagnostic at the comparison boundary, not a fit): h₀ = 0.20906; Brunnian deficit 1.438e-3 (E₀·deficit = 6.02e-3 MeV with E₀ = m_e/(q₀(q₀−1)) = 4.18598 MeV); classical n=4 cross term 0.8952 nats (3.747 MeV); the quoted Δ_λ target μ₃ = 0.4708 MeV is 78× the Brunnian term and 1/8 of the classical one. The missing 3-body magnitude sits BETWEEN the two classes; neither supplies it as it stands.

Answer to 'which word class is a nucleus' (qou-5vhf): the corpus's 3-nucleon operator IS an interleaved (commutator) word class, of the component-preserving kind. Its cross term is intrinsically O(h⁴). A term of the needed size would have to be either classical (component-changing — a different link topology per nucleus, which is the fitted census route qou-5vhf closed) or a higher-n Brunnian object whose order in h is lower; the Milnor parity law (MilnorParitySignLaw: leading order 2(A−1)) says the order RISES with A, so the Brunnian class gets smaller, not larger, up the tower.

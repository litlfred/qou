---
# qou-6082
title: Explore a tower over Bring's surface (covers / levels)
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T18:48:35Z
updated_at: 2026-11-15T21:40:00Z
---

Owner 2026-10-12: explore two types of towers. Parent context: qou-jfx8 (segment collision datum, PR #7741). Prior-work grep in progress.


## 2026-10-12 — formalized (QOU/Brings/BringCoverTower.lean, lean-direct exit 0)
Σ₄ = regular map of type (2,4,5); Riemann–Hurwitz 40(g−1) = |G| (bring_rh: |S₅|=120 → g=4). Canonical tower: iterated mod-m homology covers (characteristic ⇒ normal in Δ(2,4,5) ⇒ every level is again type (2,4,5), same cone angles, so the C₅ rotation/chirality data lifts). Proved: g_{k+1}−1 = m^{2g_k}(g_k−1) is RH-consistent at every level (tower_rh), strictly increasing, g_{k+1} ≥ m^{2g_k}; g_1 = 1+3m⁸ (769 at m=2, 1 171 876 at m=5). NOT derived: the modulus m (choosing it by what it reproduces would be a fit). No identification with confinement levels claimed.


## 2026-10-12 — prior art (six-path grep, corpus_search unavailable)
Below Σ₄ the corpus is well worked: X₀(5) hauptmodul gate (BringHauptmodulGate.lean), X₀(50)/50a Hecke gate (qou-6zxq), Jac ~ E⁴, Sylow-5 genus-2 shadow (bring-z5-descent, remark). Library BDH24 (s40879-023-00706-0 §4, sec-012/013): Bring is an UNRAMIFIED degree-3 cover of a genus-2 curve C₂ (g−1 = 3·1 ✓) — a DERIVED descending step, no modulus chosen. Above Σ₄: no prior work; BringCoverTower.lean (this branch) is new and its m is a choice. Confinement levels as surfaces: 0 hits (homonyms: ℓ = Hecke-reduction count; SU(r)/Wenzl level). Asymmetry worth noting: the descending tower is forced by the S₅ subgroup lattice; the ascending one is not.


## 2026-10-12 — option 3 done: the derived descending tower (BringDescendingTower.lean, exit 0; probe bring_descending_tower_probe.py 16/16, exact sympy)
Fixed points on Bring per S₅ class: (12) 3, (12)(34) 2, (123) 0, (1234) 2, (12345) 4, (123)(45) 0. Only 3-cycles generate a free subgroup (a free subgroup has exponent 3, so it is a 3-group, and 9 ∤ 120). B/C₃ is unramified of genus 2 (= BDH24's C₂); genus 2 has no non-trivial unramified quotient. So the FORCED unramified descending tower is exactly Σ₄ →(3:1) C₂ and has length 1. Cyclic quotient genera (Riemann–Hurwitz, exact): /(12) 1, /(12)(34) 2, /(123) 2, /(1234) 1, /(12345) 0, /(123)(45) 1. Option 2 (modulus m of the ascending tower): owner says leave open.


## 2026-11-15 — Non-abelian Hurwitz `(2,4,5)` `PSL₂(𝔽_p)` / `PGL₂(𝔽_p)` cover family over `Σ₄` (owner ruling `Q-VO9T-3 = 2`, PR `litlfred/qou#7987`, commit `eb1b32fa99`)

Extended `QOU/Brings/BringCoverTower.lean` (`lean -DautoImplicit=false -s 65536`, exit 0, 0 `sorry`) and added companion probe `computations/probes/bring_hurwitz_245_psl2_tower_probe.py` (32/32 assertions pass) classifying the non-abelian congruence / Hurwitz `(2,4,5)` cover family above `Σ₄`:
- Proved the generic `[CommRing R]` Cayley–Hamilton trace criteria for projective order 4 (`t² = 2Δ ⟹ M⁴ = -Δ² I₂`, `projOrder4_cayley_hamilton`) and projective order 5 (`t⁴ - 3t²Δ + Δ² = 0 ⟹ M⁵ = -(t³ - 2tΔ)Δ I₂` with discriminant `5Δ²`, `projOrder5_cayley_hamilton`, `projOrder5_discriminant_identity`).
- At `p = 5`, `PSL₂(𝔽₅) ≅ A₅` (`|A₅| = 60`) fails Riemann–Hurwitz (`40 ∤ 60`, `psl2_five_not_rh245`), while `PGL₂(𝔽₅) ≅ S₅` (`|S₅| = 120`) yields `Σ₄` (`g = 4`, `bring_pgl2_five_rh`).
- For prime `p > 5` with `p ≡ ±1 (mod 5)`, both the direct `PSL₂(𝔽_p)` branch (`p ≡ ±1, ±9 mod 40`, e.g. `p = 31, 41`, subdirect product `G_p = S₅ × PSL₂(𝔽_p)`) and the fiber-product `PGL₂(𝔽_p)` branch (`p ≡ ±11, ±19 mod 40`, e.g. `p = 11, 19, 29`, index-2 fiber product `G_p = S₅ ×_{C₂} PGL₂(𝔽_p)` over `Δ(2,4,5)^ab ≅ C₂`) have order `120 · |PSL₂(𝔽_p)|` and yield unramified `PSL₂(𝔽_p)`-Galois covers `Σ(G_p) → Σ₄` of genus `g(p) = 3 |PSL₂(𝔽_p)| + 1` (`bringPSL2Cover_rh`, `bringPSL2CoverGenus_values`: `g(11) = 1981`, `g(19) = 10261`, `g(29) = 36541`, `g(31) = 44641`, `g(41) = 103321`).

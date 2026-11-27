---
# qou-efxy
title: 'Bring H0(K) is std⊗sgn, not std, as an S5-rep: recheck BringPrymRiemannRochGenerations (S4 pairing, Pic[3] count)'
status: todo
type: bug
priority: high
created_at: 2026-11-27T21:38:08Z
updated_at: 2026-11-27T21:38:08Z
---


Found 2026-11-27 by the q-Bessel dictionary thread, checked by the χ = −6 chain thread (session_01VQDpPbyS5NspZ1YQT2xsE6).

**Claim.** As an S₅-representation, H⁰(Bring, K) ≅ std ⊗ sgn = [2,1,1,1], not std = [4,1]. (Same thing on A₅.)

**Check (Chevalley–Weil, one line).** dim H⁰(K)^⟨τ⟩ = genus of B/⟨τ⟩. A transposition τ has 6 fixed points on Bring, so by Riemann–Hurwitz B/⟨τ⟩ has genus 1 (bean qou-qhcr, Braden & Disney-Hogg). On std, τ has eigenvalues (1, 1, 1, −1), so its fixed space is 3-dim (genus 3 ✗). On std ⊗ sgn the eigenvalues are (−1, −1, −1, 1), so the fixed space is 1-dim (genus 1 ✓).

**Affected.** `folio/quantum-observable-universe/lean/QOU/StandardModel/BringPrymRiemannRochGenerations.lean` models H⁰(K) as V_std (line ~920, "Bring's 4-dimensional canonical differential space V_std(F)"). With the sign twist, Hom_{S₄}(H⁰(K), triv) = Hom_{S₄}(std, sgn) = 0, so `s5_protects_fourth_lepton_s4_unlocks_pairing` (the "S₄ unlocks the pairing" half) and the "8 S₄-invariant 3-torsion classes" count in the F₃ Pic[3] section may not hold for H⁰(K). The Lean theorems about V_std themselves are not wrong; the identification with H⁰(K) is. Not edited: the physics reading is the owner's call.

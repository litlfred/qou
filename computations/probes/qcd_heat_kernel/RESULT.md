# RESULT — heat-kernel time as RG time: sign of the colour one-loop coefficient

Bean `qou-bwwr` (R-α3 / R-β3). Pre-registration `PREREGISTRATION-heat-kernel-beta0-sign.md`
(commit 58c6511cf52, pushed before the probe). Probe `qcd_heat_kernel_beta0_sign_probe.py`,
output `qcd_heat_kernel_beta0_sign_probe.out.json`, **43/43 checks** (39 pre-registered + 4
post-hoc identity checks, labelled as such). Exact sympy over ℚ(q); mpmath only at the proton
pin q₀ = 1.10997858275138080759…. Convention: t → ∞ is the IR; b := d log g²_eff/dt;
b > 0 antiscreening, b < 0 screening.

## Claim

**MISS on every pre-registered construction (scope (a): not found in the searched class C1–C3).**
No construction gives the antiscreening direction, and none separates gluon and quark with
opposite signs without inserting (−1)^F by hand.

| | construction | exact result | verdict |
|---|---|---|---|
| C1 | adjoint/singlet heat-weight ratio under the corpus Δ_ξ, channels (k+1,k,k−1) vs (k,k,k) in (C³)^{⊗3k} | **b_C1(k) = −[3]_q [2k−2]_q** = −(q^{2k−2}−q^{2−2k})(q³−q^{−3})/(q−q^{−1})² | k = 1 (V⊗V̄ = 1⊕8): **0 exactly** (as predicted). k ≥ 2: < 0 for q > 1 (screening). q = 1: −6(k−1). At q₀: −6.1206, −12.5087, −19.4435 (k = 2,3,4) |
| C2 | same ratio under the U_q(gl₃) ribbon Casimir | b_C2 = −C_A = −3, every k | screening; trivial (Casimir positivity), as predicted |
| C1′ | F-projection of e^{−tΔ_ξ} on (C³)^{⊗3} (side check) | ⟨F, P_λ⟩ = 0 for λ = (3), (2,1), (1³), all q | identically 0 |
| C3 | proper-time log coefficient ½Tr_R H² per field | Casimir: gluon 8·3²/2 = **36**, quark 3·(4/3)²/2 = **8/3**. Δ_ξ: gluon **4(q²+1)²/q²** (16.1748 at q₀), quark **0** (one box, content 0) | same sign for both (sum of squares), as predicted; opposite sign only via an inserted (−1)^F |

## Evidence

- Setting verified explicitly on (C³)^{⊗3} with the Jimbo R̂ of U_q(gl₃) (convention of the
  constraint file's N = 2 matrix): Hecke and braid relations hold; Δ_ξ built from the raw
  Jucys–Murphy elements L₂ = σ₁², L₃ = σ₂σ₁²σ₂ equals μ_λ = Σ[c][c+1]_q on each isotypic part, with
  ranks 10, 16, 1 summing to 27.
- C1 closed form checked at k = 1..4; the factorisation q^{2k+1}+q^{−2k−1}−q^{2k−5}−q^{5−2k} =
  (q^{2k−2}−q^{2−2k})(q³−q^{−3}) is a sympy identity in symbolic k.
- k = 1 vanishing has a structural reason: [c][c+1] is invariant under c ↦ −1−c
  (`reebStep_reflect` in `HeckeReebHolonomyLaplacian.lean`), which maps the contents {0,1,−1} of (2,1)
  onto those {0,−1,−2} of (1³).

## Implications

1. **Δ_ξ is not a colour Casimir.** The adjoint (k+1,k,k−1) is the same sl₃ irrep for every k, yet
   b_C1 depends on k: Δ_ξ sees the U(1) (determinant / baryon-number) part of gl₃. So the C1
   coefficient is not a property of the colour channel alone. The [3]_q factor comes from the
   k ↦ k−3 row shift (N = 3 rows); C_A = N for SU(N) makes that look suggestive, but it is a
   post-hoc observation, not a pre-registered prediction, and is not claimed.
2. **Why the sign is screening (structural, not a proof).** In every construction the heat weight
   is e^{−t·(positive spectrum)}; higher-Casimir channels are suppressed toward the IR, so a ratio
   "exchange channel / vacuum channel" can only fall. QCD antiscreening comes from the
   paramagnetic spin coupling of the vector gluon in a background field (the Ω²/12 + spin part of
   the heat-kernel a₂, which is ∝ T(R)). Nothing in qou's colour heat kernel carries a spin or a
   background colour curvature, so that term is absent from C1–C3. C3 as registered measures the
   ½E² (potential) coefficient, which renormalises the potential, not g.
3. **n_f** cannot enter C1 or C2 (fixed channel of fixed n); it enters C3 only as an input count.
4. **α_EM per-loop arc (shared a₀ = 1/(4π)).** Nothing here changes it. a₀ appears only as the
   d = 2 version of the C3 prefactor, and C3 is sign-only.

## Not established

- Any heat-kernel reading with a background colour field or a spin (paramagnetic) term: not built,
  because qou has no such object (bean `qou-ni4b`: no colour action on qou's own state space).
- That t is an RG scale at all (bean `qou-abzr` stays open).
- Channels other than (k+1,k,k−1)/(k,k,k), heat operators other than Δ_ξ and the ribbon Casimir,
  n ≠ 3k. The result is a scope-(a) negative, not an exclusion of a heat-kernel RG reading.
- No gluon is identified or selected (owner ruling: step 4 of def:derived-atom stays open).

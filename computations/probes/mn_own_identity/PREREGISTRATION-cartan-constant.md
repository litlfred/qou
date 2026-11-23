# Pre-registration: which term of the categorical mass formula can carry the n–p split

Date 2026-11-21, branch `claude/mn-own-identity-2026-11-21`. Written before the probe
`mn_cartan_constant_probe.py` was run. Disclosure: the two headline numbers below
(12·h·m_e and 12·(1−q⁻²)·m_e) were estimated by hand while reading the corpus, before
this file was written. Every other number comes from the probe.

## Question (owner, 2026-11-21)

"What missing terms can we fill in? They should come from the categorical mass formula."

## What the corpus already fixes

1. The categorical mass `def:mass-identity` is a function of the braid class:
   the framing-corrected trace `(1+q²)ⁿ q^{−n−2w(β)} ∫ρ(β)` is constant on each class.
2. The γγ selection gives the same element `V³` for p and n (#8636, whole-word U(1)
   neutrality ruling). So the volume term `2 m_μ F_Bor` is the same for p and n
   (`neutron_identity_forces_equal_mass`, N0).
3. On the nucleon weight spaces, every braid word has equal bare trace and quantum-trace
   ratio `q²` (`NucleonIsospinExclusions.trace_sword_eq`, `restrictedTrace_ratio`). So
   any sector-resolved (Cartan-weighted) term `T` gives `T(p) = q·t`, `T(n) = q⁻¹·t`
   for one isospin-blind `t`.
4. The production identity has exactly two terms: `+2 m_μ F_Bor` (positive) and
   `−12 m_e` (negative, not derived, issue #8809).

## Claim to be proved (Lean, generic ordered field, no measured values)

For an assembly `m_N = Σ_k c_k ω_k(N) t_k`, where each term is either bare
(`ω_k = 1`) or Cartan-weighted (`ω_k(p) = s q`, `ω_k(n) = s q⁻¹`, `s > 0`):

    m_n − m_p = −s (q − q⁻¹) Σ_{k weighted} c_k t_k.

So for q > 1 the neutron is heavier **iff the Cartan-weighted part is net negative**.
Corollary for the production identity: weighting the volume term (alone or with the
constant) gives the neutron lighter. That is the existing N1 (−19 %). Only a weighted
`−12 m_e` with a bare volume term gives the neutron heavier.

## Readings to evaluate (both are reported, neither is chosen by its residual)

- **K1, proton-normalised** (`s = q⁻¹`, so the proton identity is unchanged):
  `m_n − m_p = 12 (1 − q⁻²) m_e`. Prediction: about 1.15 MeV, neutron heavier,
  about 10 % low. m_p is unchanged (−0.244 ppm at the muon pin).
- **K2, symmetric** (`s = 1`, plain quantum-trace weight `K^{⊗3}` on the sector):
  `m_n − m_p = 12 h m_e`. Prediction: about 1.28 MeV, within about 1 %. But m_p moves by
  `−12 (q − 1) m_e`, about −0.67 MeV, so the proton round trip breaks at the muon pin by
  about −700 ppm.
- **K0 control** (volume term weighted, constant bare): the neutron is lighter by tens of
  MeV (this is N1).

## Scope, fixed in advance

- That the `−12 m_e` term carries a Cartan weight is **not derived**. The −12 itself is not
  derived (#8809; the −12 sibling reduced it to "proton Reeb weight k = 2 on a 3-dim weight
  space", `−k²·dim W`). If the term is read as a trace over the nucleon's own weight space,
  the quantum trace supplies `K^{⊗3}`, which is the K2 normalisation. K1 needs an extra `q⁻¹`.
- Choosing K1 or K2 by which residual is smaller is selection against the target and is
  not done. The robust content is the sign, and the order of magnitude `h · 12 m_e`.
- CODATA and literature values appear only in comparison columns.

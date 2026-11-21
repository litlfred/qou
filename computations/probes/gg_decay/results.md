# gg_decay — results (bean qou-a1hh; hypothesis only; nothing wired)

Pre-registration: 515ef592b8b. A(n→p; g) = τ(p⁻¹ W_g n), τ = convention-D Markov trace on H₃,
W_g = q⁻¹(2σ_g − h)/[2]_q, proton q₀.

**Precision note (deviation from pre-registration):** the shared base module
(`h2_one_rule_probe`) fixes q₀ at 40 dps, not 70. Checks D0–D2 use tolerance 1e-35 accordingly.
A first run with a 1e-50 tolerance failed D0/D1 at the 1e-42 level; that run was void.

## Checks: D0 (W² = q⁻²), D1 (τ(1) = 1), D2 (ι(W) = −W): all PASS.

## Results
- Diagonal: A(n→n; g) = τ(W) = 0.4553279084459 for every candidate and both sites. This is
  forced by cyclicity of τ, so it carries no information.
- Owner's two assignments (p = V³, n = V⁶ and the reverse):
  - g0: V⁶→V³ = 0.449030644404885, V³→V⁶ = 0.461625172486915
  - g1: V⁶→V³ = 0.461625172486915, V³→V⁶ = 0.449030644404885
  The two directions swap exactly when the site g is swapped. So within this pair the direction
  asymmetry is a site label, not an intrinsic direction: neither assignment is preferred.
- All 90 (unordered pair × site) cells have |A(n→p)| ≠ |A(p→n)|; the largest gap is 0.642
  (VBB|BVV, g0). Unlike the V³/V⁶ pair, the g0↔g1 swap is not an exact symmetry in general
  (max |A(n→p;g0) − A(p→n;g1)| = 0.326), so for mixed words the asymmetry is not only a site label.

## Reading (scope a)
E1 (no pair singled out) holds for the owner's assignments: decay with W does not pick
p = V³, n = V⁶ over the reverse. Mixed-orientation words do show direction asymmetries, but by
the pair result ι(V) = V̄ those words differ by chirality, not flavour, so this is not a
flavour decay. Calling any of these a decay rate is an interpretation.

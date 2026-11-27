# Pre-registration: a charge vertex from the braid algebra, all orders in φ, and distance (2026-11-22)

Thread "Settle the neutron-heavier sign". Owner 2026-11-22: "Do both. But it's also the notion of plank
length for distance.... Does it not enter here?" Follows `np_two_block_photon_exchange_preregistration.md`
(PR #9077). Written before any code for A–C exists. Setup, K, Ř, the V³ blocks, block charge Q and the
pair shift ΔE_X(a, b) = T_X(a, b)/T_1(a, b) are unchanged from that file.

## A. Every element of the six-strand braid image (this also settles all orders in φ at n = 6)
T_X is linear in X, so "ΔE_X = c + κ·Q_aQ_b on every sector with T_1 ≠ 0" is a linear system in the
coordinates of X and in (c, κ). X runs over the image of H_6(q) on (C²)^{⊗6} (expected dimension 132,
the Temperley–Lieb quotient). Any power series in the photon monomials is such an X, so A covers every
order in φ at n = 6.
- **A1.** Report the dimension of the image (spanned by the 720 reduced words).
- **A2.** Report whether a solution with κ ≠ 0 exists, for the Coulomb form (O1), the isospin form (O2)
  and the general affine-bilinear form (O3). Exact arithmetic at q = 111/100 and q = 7/5.
- **Guess, stated so it can fail:** no solution with κ ≠ 0 for O1. Reason offered: the braid image
  commutes with U_q(sl₂), so it cannot tell weights apart inside one irreducible piece. Then the sector
  dependence comes only from K and Π, and I do not see how that reproduces Q·Q. I am not confident in
  this guess.

## B. All orders for a single crossing (Lean)
σ² = hσ + 1 implies every power series in σ is a + bσ. So ΔE of the resummed single-crossing photon is
a + b·ΔE_σ. If b ≠ 0 it is non-Coulomb exactly when ΔE_σ is. To be proved in Lean, generically.

## C. Distance: spectator strands between the nucleons
n = 6 + d with d = 0, 1, 2, 3. Block A is on strands 0–2, block B on strands 3+d … 5+d, and the d
spectators lie between them. The trace runs over all spectator states with K, and spectators are not
projected. The exchange is the band generator joining strand 2 to strand 3 + d across the spectators:
X_d = (σ₂⋯σ_{1+d})·σ_{2+d}·(σ₂⋯σ_{1+d})⁻¹, which is σ₂ at d = 0.
- Reported, exact: I(d) = pp − pn − np + nn, pp − nn, and pn − np as functions of d.
- **Coulomb reading:** a charge-like part falling as 1/(d + 1). **Exchange-force reading:** a fall faster
  than any power, or no fall at all (a braid has no metric, so d may not act as a distance).
- No prediction. Whichever holds, no length unit is attached: "one strand = one Planck step" is not
  assumed, only tested for shape.

## What is not done
No value is compared with experiment and nothing is fitted.

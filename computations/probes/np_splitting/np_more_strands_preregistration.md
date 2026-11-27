# Pre-registration: the reachable pair terms on more than six strands

Written and committed before `np_more_strands_probe.py` is run (owner choice 2026-11-22, item 2 of
issue #9124: "more strands").

Same readout as `np_all_q_symbolic_probe.py`: ΔE_X = T_X/T_1 with
T_X(a, b) = Tr(K^{⊗N} Π_{a,b} V_A³ V_B³ X), V = σ_lo σ_{lo+1}⁻¹, Jimbo Ř, and X ranging over the
whole image of the N-strand Hecke algebra (the images of the T_w, w ∈ S_N). Block A sits on strands
0–2. The other strands are spectators: they carry no core and are summed over in Π_{a,b}.

Layouts:

- L7s: N = 7, block B on strands 4–6, one spectator between the blocks (strand 3).
- L7e: N = 7, block B on strands 3–5, one spectator at the end (strand 6).
- L8s: N = 8, block B on strands 5–7, two spectators between the blocks.

Arithmetic: exact rationals at q = 111/100 and q = 7/5 (python-flint fmpq). No float. A result at
fixed q is exact at that q only; it is not an identity in q.

Predictions (stated before running):

- P1. In the layouts symmetric under strand reversal (L7s, L8s), the reachable set of pair shifts is
  closed under (Q_A, Q_B) ↦ (1 − Q_B, 1 − Q_A). This is the symmetry of
  `QOU.QBeta.PairTermSectorSymmetry`. The flip-and-reverse map J fixes the layout, and the half twists
  act inside the blocks, so the argument carries over unchanged.
- P2. No prediction on the rank. The spectators enlarge the algebra, so the reachable affine-bilinear
  pair terms could be one ray (as at N = 6), a plane, or every pair term. The probe reports the rank
  of the system for (κ, κα, κβ). Rank 3 means no pair term with κ ≠ 0 is reachable. Rank 2 means a
  unique ray. Rank 1 or 0 means a family. Only a rank of 1 or 0 can contain the Coulomb form.
- P3. If the rank is 2 in a symmetric layout, then α + β = 1 at that q (forced by P1).
- P4. If the Coulomb form (α = β = 0, κ ≠ 0) is reachable in some layout, the probe says so. That
  would be a positive result about spectators, reported as found.

The asymmetric layout L7e carries no prediction beyond the rank being reported.

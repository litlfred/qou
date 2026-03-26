-- Ref: [manuscript] Ch. 6, §3
-- The stable neutron number as a function of proton number and
-- substrate parameter q.  The beta-stability formula gives:
--   p = A / (2 + c * A^{2/3})  where c = a_C / (2 * a_A)
-- Solving for A and setting n = A - p.
--
-- This is the smooth (shell-free) prediction.  Shell corrections
-- at stability pairs {2, 8, 20, 28, 50, 82, 126} are not included
-- in this formula.

-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
sorry

noncomputable section

/-- The Coulomb coefficient a_C = (q - q⁻¹) · λ_C -/
def coulomb_coeff (q λ_C : ℝ) : ℝ := (q - q⁻¹) * λ_C

/-- The curvature parameter c = a_C / (2 · a_A) -/
def curvature_param (q λ_C a_A : ℝ) : ℝ :=
  coulomb_coeff q λ_C / (2 * a_A)

/-- The continuous beta-stability optimum: p*(A) = A / (2 + c · A^{2/3}) -/
def beta_stability_continuous (c : ℝ) (A : ℝ) : ℝ :=
  A / (2 + c * A ^ (2/3 : ℝ))

/-- The stable neutron number: solve p = A/(2 + c·A^{2/3}) for A,
    then n = round(A) - p.  This is the integer minimiser of the
    convex quadratic E(p, A) at fixed p. -/
def stable_neutron_number (q λ_C a_A : ℝ) (p : ℕ) : ℕ :=
  sorry -- requires solving the cubic t³ = 2p(1 + ct²) for t

/-- Witness: at q = 1.10997, λ_C = 3.334, a_A = 23.29,
    the predicted stable neutron numbers for p = 1..103.
    Each entry is (p, n_pred). -/
def stable_neutron_witness : List (ℕ × ℕ) :=
  [ (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 8),
    (8, 9), (9, 10), (10, 11), (11, 12), (12, 14), (13, 15),
    (14, 16), (15, 17), (16, 19), (17, 20), (18, 21), (19, 22),
    (20, 24), (21, 25), (22, 26), (23, 28), (24, 29), (25, 30),
    (26, 32), (27, 33), (28, 35), (29, 36), (30, 37), (31, 39),
    (32, 40), (33, 42), (34, 43), (35, 45), (36, 46), (37, 48),
    (38, 49), (39, 51), (40, 52), (41, 54), (42, 55), (43, 57),
    (44, 58), (45, 60), (46, 62), (47, 63), (48, 65), (49, 66),
    (50, 68), (51, 70), (52, 71), (53, 73), (54, 75), (55, 76),
    (56, 78), (57, 80), (58, 81), (59, 83), (60, 85), (61, 86),
    (62, 88), (63, 90), (64, 92), (65, 93), (66, 95), (67, 97),
    (68, 99), (69, 101), (70, 102), (71, 104), (72, 106),
    (73, 108), (74, 110), (75, 112), (76, 114), (77, 115),
    (78, 117), (79, 119), (80, 121), (81, 123), (82, 125),
    (83, 127), (84, 129), (85, 131), (86, 133), (87, 135),
    (88, 137), (89, 139), (90, 141), (91, 143), (92, 145),
    (93, 147), (94, 149), (95, 151), (96, 153), (97, 155),
    (98, 157), (99, 159), (100, 161), (101, 163), (102, 165),
    (103, 167) ]

/-- The observed stable neutron numbers (most stable isotope, AME2020). -/
def observed_neutron_numbers : List (ℕ × ℕ) :=
  [ (1, 0), (2, 2), (3, 4), (4, 5), (5, 6), (6, 6), (7, 7),
    (8, 8), (9, 10), (10, 10), (11, 12), (12, 12), (13, 14),
    (14, 14), (15, 16), (16, 16), (17, 18), (18, 22), (19, 20),
    (20, 20), (21, 24), (22, 26), (23, 28), (24, 28), (25, 30),
    (26, 30), (27, 32), (28, 30), (29, 34), (30, 34), (31, 38),
    (32, 42), (33, 42), (34, 46), (35, 44), (36, 48), (37, 48),
    (38, 50), (39, 50), (40, 50), (41, 52), (42, 56), (43, 55),
    (44, 58), (45, 58), (46, 60), (47, 60), (48, 66), (49, 66),
    (50, 70), (51, 70), (52, 78), (53, 74), (54, 78), (55, 78),
    (56, 82), (57, 82), (58, 82), (59, 82), (60, 82), (61, 84),
    (62, 90), (63, 90), (64, 94), (65, 94), (66, 98), (67, 98),
    (68, 98), (69, 100), (70, 104), (71, 104), (72, 108),
    (73, 108), (74, 110), (75, 112), (76, 116), (77, 116),
    (78, 117), (79, 118), (80, 122), (81, 124), (82, 126),
    (83, 126), (84, 125), (85, 125), (86, 136), (87, 136),
    (88, 138), (89, 138), (90, 142), (91, 140), (92, 146),
    (93, 144), (94, 150), (95, 148), (96, 151), (97, 152),
    (98, 153), (99, 154), (100, 157), (101, 158), (102, 157),
    (103, 159) ]

/-- The maximum discrepancy |n_pred - n_obs| across all p ≤ 103
    is at most 8 (occurring at the heaviest transuranic elements). -/
theorem stable_neutron_max_error :
    ∀ entry ∈ stable_neutron_witness.zip observed_neutron_numbers,
      |Int.ofNat entry.1.2 - Int.ofNat entry.2.2| ≤ 8 := by
  sorry

end

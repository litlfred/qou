# Pre-registration: the capture as a conditional expectation, and the sign on n strands (2026-11-22)

Thread "Settle the neutron-heavier sign". Owner relay 2026-11-22: work option 2 (the capture
correction to Q_β) and option 3 (the sign for every word with the extra strands on the right).
Written before `np_capture_conditional_expectation_probe.py` is run.

## Honesty clause
Before writing this I checked one number by hand from the committed probe output: the ratio
ε(W_adj,L)/ε(V³) = 0.0704847/0.0769805 = 0.91562, against 1 + h² − h·q²/[2] = 0.91562 at the
proton q₀. P3 below is therefore not a blind prediction for that one element.

## Setup (fixed, unchanged from np_hydrogen_flavour_split_probe.py)
Ř = [[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]], h = q − q⁻¹, K = diag(q, q⁻¹), u = index 0.
E_c(W) = Tr(K^{⊗n}·(Π_c ⊗ 1)·W)/[2]^n with the nucleon on strands 0–2. ε = E_p − E_n.
E(X) := ptr_{last}((1 ⊗ K)·X)/[2], the K-weighted partial trace over the last strand,
normalised. Exact arithmetic only (sympy over Q(q), or Fraction at rational q).

## Predictions
- **P1 (option 3, n strands).** With the nucleon on strands 0–2 and the extra strands on the
  right, E_n = q⁻²·E_p for every braid word, for n = 5 and n = 6 as for n = 4 (Lean
  `left_ratio`). Test: every word of length ≤ 4 on 5 strands and ≤ 3 on 6 strands, exact at
  q = 111/100 and q = 7/5.
  Reason given in advance: E maps the braid image on n strands into the braid image on n−1
  (Markov property of the last-strand K-trace plus H_n = H_{n−1} + H_{n−1}σ_{n−1}H_{n−1}), so the
  n-strand functional is the 3-strand one on E^{n−3}(W), where the ratio is q⁻².
- **P2.** With the nucleon not at the left end (strands 1–3 or 2–4 on 5 strands), the ratio
  fails for some word. No prediction of which.
- **P3 (option 2, adjacent capture).** E(σ₂⁻²) = (1 + h² − h·q²/[2])·1, a scalar, so
  ε(V³·σ₂⁻²) = (1 + h² − h·q²/[2])·ε(V³) exactly.
- **P4 (option 2, cabled capture).** C = (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹ is the inverse of the Jucys–Murphy
  element of strand 3. E(C) is central in the braid image on 3 strands, so it is a scalar c_λ on
  each isotypic block λ ∈ {(3), (2,1)}, and ε(V³·C) = Σ_λ c_λ·ε_λ(V³). The c_λ are reported
  exactly; no value is predicted.
- **P5.** No number is compared with CODATA for selection. Q_β factors are reported for both
  captures.

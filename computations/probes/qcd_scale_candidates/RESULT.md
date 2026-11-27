# RESULT — tower index n and KZ coupling κ as the scale of a colour coupling

Bean `qou-abzr` (sibling of `qou-bwwr`, heat-kernel time t). Pre-registration
`PREREGISTRATION-n-and-kappa-scales.md` (commit 40489bd8bd5, pushed before the probe). Probe
`qcd_n_kappa_scale_probe.py`, output `qcd_n_kappa_scale_probe.out.json` (commit 2f12731a1ff),
**89/89 checks**, of which 6 are post-hoc closed-form identities and are labelled `posthoc`.
Exact sympy over ℚ(q, k); mpmath only at the proton pin q₀ = 1.109978582751380807591669.
Common definitions: g² := W_8/W_1 (adjoint over singlet), b := d log g²/ds, s increasing = IR,
b > 0 antiscreening direction.

## Claim

**MISS on both arms (scope (a): not found in the searched class N1, N2, K1–K3).** No construction
meets the pre-registered hit rule. C_A does appear, in two arms, but only as a Casimir difference.
It never comes with a T_F·n_f partner, and the running is never logarithmic.

| | construction | exact result | hit clause (i) sign | clause (ii) C_A/T_F | log running |
|---|---|---|---|---|---|
| N1 | Ocneanu isotypic weight f^λ·dim_q V_λ, n = Nk, adjoint (k+1,k^{N−2},k−1) vs singlet (k^N) | g² = (N²−1)·k/(k+N)·dim_q(adj). For N = 3: **g² = 8k/(k+3)·[2]_q[4]_q**. b = **N/(k+N)** (= N²/(n+N²)), q-free, invariant under q ↔ q⁻¹ | **definite, b > 0** (antiscreening direction) | C_A = N in the baryon count k (N² in the strand count n); **no n_f term** | **no**: 1/g² ∝ 1 + N/k, a power correction |
| N2 | last-strand Jucys–Murphy eigenvalue q^{2c}, Plancherel branching | N = 3: g² = (k q⁸ + 2k q⁴ + 5k + 3q⁸ + 2q⁴ − 5)/(8k q²); g²(k+1)/g²(k) − 1 = −(q²−1)(q²+1)(3q⁴+5)/((k+1)(…)) | **choice-dependent**: b < 0 at q₀, b > 0 at 1/q₀, every k = 2..12 and N = 2, 3, 4 (factor q²−1, bar-odd) | no n_f | no (1/k) |
| K1 | KZ collision z_ij = ℓe^{iθ}, W_R = \|z^{κω_R}\|², ω_R = (C_R − C_a − C_b)/2 | ω_8 − ω_1 = C_A/2 for **every** external pair (checked 2⊗2̄, 3⊗3̄, 4⊗4̄, 3-adj⊗adj, 2-adj⊗adj from explicit matrices); **b = Re(κ)·C_A** | **choice-dependent**: sign of Re κ. Drinfeld–Kohno q = e^{iπκ} with real q₀ > 1 gives κ imaginary, **b = 0 exactly** (scale dependence is a pure phase in θ). Wick convention q = e^{±πκ}: b = ±3 log q₀/π = ±0.099638… | C_A identified, but **quark pair and gluon pair give the same b** | **no**: power law ℓ^{Re κ·C_A} |
| K2 | resonance (only source of log ℓ in a Fuchsian system) | eigen-differences 3/2 (3⊗3̄), {1, 3/2, 5/2, 3, 4} (8⊗8); log terms iff κΔ ∈ ℤ∖{0} ⇔ \|q\| = 1 | — | — | **never at real q > 1** |
| K3 | spectator quark at z₃ | residue at z₁₂ → 0 stays κΩ₁₂ ⊗ 1 (spectrum −4/3 ×3, 1/6 ×24) | — | **no n_f in the leading exponent** | — |

## Evidence

- N1 closed form from the Frobenius formula f^λ/n! = Δ(ℓ)/Πℓᵢ!, checked against the hook formula
  at k = 1..8 for N = 2, 3, 4; dim_q(adj) → N² − 1 at q = 1.
- N2 branching probabilities sum to 1 for both channels (exact in k); sign table at q₀ and 1/q₀
  in the `.out.json`.
- K1 Ω built over ℚ as ½(Σ E_ij ⊗ E_ji − (1/N) 1⊗1) in the fundamental, antifundamental
  (−E_ji) and adjoint (ad on sl_N) — no √3 Gell-Mann entries; Casimirs C_F = (N²−1)/(2N) and C_A = N
  verified from the same matrices.

## Implications

1. **N1 is the only construction with a definite antiscreening-direction sign, and its coefficient
   is C_A** (N in units of baryon number). This is a prediction of the registration that held. It is
   the classical multiplicity effect: a channel with larger Casimir is under-represented at small n
   and saturates to its dimension as n grows. It is a finite-size effect with a 1/k law, not a loop
   coefficient: 1/g² has no log n term, and nothing in it counts quark flavours. So n behaves as a
   block-spin count, but the "running" it gives is power-law approach to a fixed ratio.
2. **κ is not a running variable at qou's q₀.** With the Drinfeld–Kohno identification and real
   q₀ > 1, the KZ exponent is purely imaginary, so the collision behaviour in log|z| is a phase and
   b = 0 exactly; logs never arise (no resonance off the unit circle). A real-κ reading gives
   b = ±C_A log q₀/π with the sign fixed only by the convention.
3. **No quark/gluon separation in K1.** The adjoint-minus-singlet exponent is C_A/2 whatever
   colour sits at the two points. KZ exponents are tree-level one-gluon-exchange Casimir differences
   (§48), so a T_F n_f vacuum-polarisation term has no place to enter.
4. **Across the three candidates (t, n, κ)**, none gives a log running with a C_A vs T_F n_f split.
   `qou-abzr` stays open: the searched class contains no RG scale in the one-loop sense.
5. α_EM per-loop a₀ = 1/(4π): not used, not changed. q₀: evaluated only; never solved for.

## Not established

- Any construction outside N1, N2, K1–K3: other channels, other tower weights (e.g. the N = 2
  convention-D trace, which cannot see C_A anyway, §48), multi-point KZ asymptotics beyond the
  two-point collision, KZ at |q| = 1.
- That n or κ is, or is not, an RG scale in some other sense. Scope (a) only; no structural
  exclusion is claimed.
- Which of k (baryon count) or n (strand count) is the natural variable: N1's coefficient reads N
  in one and N² in the other. Reported, not chosen.
- No gluon is identified or selected (step 4 of def:derived-atom stays open).

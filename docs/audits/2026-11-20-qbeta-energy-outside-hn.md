# Q_β as an energy from U_q(gl₂) structure outside H_n

Owner (Carl, 2026-11-20 ~20:15): derive Q_β as an energy, consistent with the q-dependent rate,
with nothing chosen. Bean `qou-99qc`. Pre-registration:
`computations/probes/qbeta_uq_energy/PREREGISTRATION.md` (commit `d632ed27bf`). It discloses
two cells I estimated by hand before writing it.

## 1. Result

**No candidate outside H_n derives Q_β.** The U_q(gl₂) side adds one derived fact and one
structural negative.

- **Derived.** The amplitude (q²−1)·T⁺ (#8638) is exactly Ad_K(T⁺) − T⁺. That is, it is
  e^{λΔH} − 1 with λ = ln q and ΔH = 2. So the q-dependence of the amplitude is fixed by the
  **Cartan charge 2 carried by T⁺**. It is not fixed by an energy in MeV.
- **Structural negative, scope (b).** Only the Cartan weight separates n from p. A central element
  (twist, Casimir), or anything else that commutes with T⁺, gives them the same eigenvalue.
  Include the lepton strand, and the Cartan weight becomes a conserved charge: n⊗ν and p⊗e⁻ lie
  in one K^{⊗4} weight space. So every K-weighted four-strand split is 0. Every energy linear in
  the Cartan weight with a single coefficient also gives Q_β = 0.
- **Consequence for the scored cell.** The ruled Q_β = 0.3254 MeV (#8586, D1 = A) is the
  **three-strand** (quark-only) half of a quantity that the full four-strand process conserves.
  It is non-zero only because the lepton strand is kept outside the K-grading. That is a premise,
  not a derivation. It is the subject of sibling
  `claude/beta-rate-lepton-strand-premise-2026-11-20`.

## 2. Candidates

| | construction | exact form | at proton q₀ (70 dps) | vs CODATA 0.78233341 | scope |
|---|---|---|---|---|---|
| a1 | linear K-gap h = q−q⁻¹ × scale | h·S | m_e: 0.10683 / E₀⁰: 0.87512 / E₀^tow: 0.88380 MeV | −86.3 / +11.9 / +13.0 % | (a): scale and linear-vs-log are choices |
| a2 | log K-gap 2λ × scale | 2 ln q·S | m_e: 0.10664 / E₀⁰: 0.87354 / E₀^tow: 0.88220 MeV | −86.4 / +11.7 / +12.8 % | (a): same |
| b | twist θ / Casimir, n vs p | central ⇒ equal | 0 | −100 % | (b): centrality + T⁺n ≠ 0 |
| c0 | four-strand K-weighted split, any X | n⊗ν, p⊗e⁻ in one weight space | 0 | −100 % | (b): Δ(K) grouplike, E⊗F charge 1 |
| c1 | linear Cartan energy, one coefficient | 2(b−a), a = b | 0 | −100 % | (b): charge conservation |
| c2 | lepton strand alone, #8586 functional | \|ε_ℓ\|·E₀ = m_e(q+1)/(q(q²+1)) | 0.43519 / 0.43950 MeV | (not Q_β) | equals m_e only at q = 1 |
| c3 | additive sectors (ε_q − ε_ℓ)·E₀ | ε_q from #8586, ε_ℓ = −h/[2] | 0.11295 / 0.11407 MeV | −85.6 / −85.4 % | (a); sign conflict below |
| d | E₀ = m_e/(q(q−1)) as a K-grading unit | E₀·g = m_e ⇔ g = q(q−1) | E₀·g/m_e: h 1.7126, 2λ 1.7095, q−1 0.9009, q²−1 1.9009 | — | (b) over ℚ(q): no doublet gap equals q(q−1) |
| ref | #8586 scored | \|ε_flavour(V³)\|·E₀^tow | 0.325434 MeV | −58.40 % | ruled |

**Do not read a2·E₀ (+12.8 %) as a lead.** It needs three choices: the log gap, the posited E₀,
and dropping the lepton strand. It also drops the factor tr_W(V³)/[2]³ that #8586's functional
carries. Accuracy is not evidence (§NO FITTING). The +12 % cells are within 0.3 % of each other
because h = 2 sinh λ, so h and 2λ agree to O(λ³). They are the same cell twice.

**c2/c3: the electron does not enter correctly.** Apply the #8586 functional to the lepton strand
and the electron–neutrino split is 0.435–0.440 MeV, not m_e. Under the only sign convention that
makes c3 positive (mass = +trace·E₀), both splits have the wrong ordering: m_n < m_p and
m_e < m_ν, since ε_q < 0 (#8586) and ε_ℓ < 0. With the other sign, Q_β < 0.

**d: E₀ is not derived.** E₀·q(q−1) = m_e is the definition. q(q−1) = q² − q is the gap between
the K-eigenvalues q² and q, which belong to weights H = 2 and H = 1. No single strand of the
doublet carries that gap (`h_eq_E0gap_iff`, `qsq_eq_E0gap_iff`). Interpreting E₀ as a K-grading
unit adds nothing, so it stays posited (`qou-mkm8`).

## 3. Consistency with the rate

The rate's q-dependence comes from |M|² = (q²−1)²·… (#8638, #8639). Here (q²−1) = e^{2λ} − 1
is the Ad_K factor of a charge-2 transition, and it is the **same** charge-2 that c1 shows the
lepton side returns. So the amplitude and the K-grading agree with each other. Neither carries
an energy scale. A Q_β "consistent with the rate" in this sense is any S·g(2λ), where S is not
derived. The only MeV input the corpus has is m_e (CAL-1), and m_e times either gap is 86 % low.

## 4. Lean — `QOU/QuarkState/CartanEnergyTransport.lean`

Generic `[Field R]`, Mathlib only, `lean -DautoImplicit=false -s 65536` exit 0. `#print axioms`:
propext, Classical.choice, Quot.sound.

| theorem | content |
|---|---|
| `eigen_eq_of_commute` | C commutes with E, Cv = av, C(Ev) = b·Ev, Ev ≠ 0 ⇒ a = b (twist, Casimir, H₃) |
| `eigen_mul_of_qcommute` | K E = c·E K ⇒ K(Ev) = (c·a)·Ev |
| `K_E`, `K_F`, `adK_sub_self`, `adK_E` | K E K⁻¹ − E = (q²−1)E on the doublet |
| `kron_qcommute`, `EKK_charge` | q-commutation charges multiply under ⊗; E⊗K⊗K has charge q² |
| `EF_commutes_KK`, `exchange_preserves_weight` | E⊗F commutes with K⊗K; the exchange keeps the K-weight |
| `linear_cartan_released(_zero_iff)` | released energy 2(b − a), zero iff a = b |
| `epsLepton_E0` | ε_ℓ·E₀ = −m_e(q+1)/(q(q²+1)) |
| `h_eq_E0gap_iff`, `qsq_eq_E0gap_iff` | h = q(q−1) ⇔ (q−1)(q²−q−1) = 0; q²−1 = q(q−1) ⇔ q = 1 |

The three-strand Ad_K identity, the Casimir transport and the four-strand commutation are also
checked exactly in the probe (sympy, coproduct Δ(E) = E⊗K + 1⊗E). Probe 14/14.

## 5. What remains a choice (none selected)

1. **Whether the lepton strand is in the K-grading.** In: Q_β = 0 (scope b). Out: #8586's 0.3254.
2. **The energy scale S** (m_e, posited E₀⁰ or E₀^tower). Nothing in U_q(gl₂) fixes a scale.
3. **Linear K vs log K** (h vs 2λ). These differ at O(λ³) only.
4. **Different Cartan coefficients on quark and lepton strands** (c1, a ≠ b). This is one free
   number. Fixing it by Q_β would be a fit.

Not searched: U_q(gl₂) structures beyond the Cartan, the centre and the Hopf structure. These
include R-matrix spectral parameters and affine (loop) U_q. "Found none" applies to the four
candidates above only.

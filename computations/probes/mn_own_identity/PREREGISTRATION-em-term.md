# Pre-registration: one electromagnetic term for n − p, built from α_EM (2026-11-22)

Written before the probe `mn_em_term_probe.py` was run. Context: §39 of
`LITERATURE-COMPARISON.md`. Lattice QCD+QED (Borsanyi et al. 2015) splits
m_n − m_p ≈ +2.52 MeV (quark mass) − 1.00 MeV (electromagnetic). Every braid-built term in this
model is 0 at q = 1 (§34, `FlipSymmetryAtOne.lean`), so an EM piece that is still there at q = 1
has to carry something from outside the braid algebra. Here that is the adopted quark charges.
The lattice split is printed after the numbers, for comparison only. Nothing is tuned to it.

## The α_EM element (corpus check, before computing)

Three objects carry the name α_EM in the corpus:

| object | where | status |
|---|---|---|
| **bare singlet α(q) = q⁻¹/([9]_q[10]_q)** | `predicted-spectra/em-coupling-projection` (prop), `constants.py:1019` | Lean `QOU.Archimedean.isEmCoupling_iff`: `IsEmCoupling α :↔ [9][10]α = q⁻¹`, proof `Iff.rfl`, no `sorry`. The Lean *defines* α by this relation. It does not derive the relation from upstream structure. The open-problems block labels it "Derived". At q₀, 1/α = 136.823, 0.155 % from CODATA. At q = 1, α = 1/90. |
| trace-ratio form h²/(q·δ^top(T₂,₉)·δ^top(T₃,₅)) | `alpha-em-categorical-trace-ratio` | The same element, rewritten by an exact identity. Not a separate choice. |
| dressed α (Chern–Simons tower, Form A) | `meson_em_sinh_closed_form.alpha_em_inv_derived` | Uses κ_gram, which is not proved ("κ ≈ 1.722 … was never proved", `alpha-em-derivation-open-problems`). Conditional. |
| Habiro element H = [2]_q(1 − h²α) | `braids-and-knots/alpha-em-habiro-bar-involution` (sorry-free) | Takes α as an **input**. It is not a source of α. |

**Chosen: the bare singlet α(q) = q⁻¹/([9]_q[10]_q).** It is the only form whose status is
not conditional on an unproved constant. Its own derivation status is "defined, sorry-free",
not "proved from upstream". Form A is not used, because it adds κ.

## The one candidate, EM-1 (definitions fixed before computing)

- **Charge structure.** S = QPair·hol on C²⊗³. QPair = diag(Σ_{i<j} qᵢqⱼ) and hol = V³,
  V = σ₀σ₁⁻¹. This is the same object as §31/§35 and is taken from `mn_muon_scale_probe.py`
  unchanged. The charges are the **adopted** +⅔, −⅓. That makes every number below
  **conditional on the owner ruling of 2026-11-22 that qᵢ must be derived** (§33). The derived
  operator charge Q̂ of §38 is not used for EM-1. Q̂ has equal spectra on W_p and W_n (§38 PA1), so
  every Q̂-built term is 0 at q = 1. That would make it a braid-algebra term, which this test is
  not about.
- **EM Lagrangian term and its sign.** ℒ_EM = −α(q)·S, the Coulomb-law sign: the electrostatic
  potential of charges is V = +α Σ qᵢqⱼ·(1/r), and ℒ carries −V. By the owner's degree-0 ruling,
  the term enters the energy as E_EM = −ℒ_EM = +α·S.
  **Two things about this sign must be stated.** (i) It is **imported from the Coulomb law**, not
  derived in the model. So "the EM term makes the proton heavier" is an input of the test, not a
  prediction it can confirm. (ii) It is **opposite** to the sign that §35 gave the strong-sector S
  (ℒ′ = 𝒟² + S, so V = −S). The corpus therefore puts the two S terms in with opposite signs.
  That tension is recorded here and not resolved. Under the §35 sign the result is the negative
  of EM-1's.
- **Scale: the electron map** (§31/§35 E-pot), with the derived weighting K = q^{T³⊗3}:
  E_n − E_p = m_e · α · [tr_{W_n}(K·S) − tr_{W_p}(K·S)] / tr(K·𝒟_e²). Here 𝒟_e is the electron
  word σ₀σ₁σ₀ (Hopf closure, writhe 3), exactly as in `mn_muon_scale_probe.py`. The reason for the
  electron map is §35's own conclusion that a degree-0 S must not ride the muon scale. The plain
  (unweighted) trace is reported as a labelled diagnostic.
- q₀ is the proton pin `Q_50_DIGIT_STR`. The computation is exact sympy in q, evaluated with
  mpmath at 60 dps. No float64.

## The one stated alternative, EM-2

The same +α·S on the §35 **muon map**:
E_n − E_p = 2 m_μ([3]_q!/q³)·α·(τ_n − τ_p)(S), with m_μ = m_e·Vol(4₁)/ℏ_q².

## Predictions (written before computing; how each was obtained is stated)

These are **not blind**. Each follows by arithmetic from numbers already in
`mn_muon_scale_probe.out.json`, multiplied by α(q₀) ≈ 1/136.8 and α(1) = 1/90.

1. **EM-1 sign: negative** (proton heavier). This follows from the imported Coulomb sign and
   ΣqᵢqⱼPair_n = −⅓ < 0 = ΣqᵢqⱼPair_p.
2. **EM-1 size: about −0.36 keV (K-weighted) and −0.40 keV (plain) at q₀.** That is α times the S
   part of §35 E-pot (49.07 / 54.44 keV, less a small 𝒟² part).
3. **EM-1 at q → 1: finite and nonzero, −m_e/720 ≈ −0.710 keV.** That is α(1) = 1/90 times
   §35's limit 1/8, so the term survives q = 1, as an EM term should.
4. **EM-1 against the lattice −1.00 MeV: predicted to miss by about 2500–2800×.** If |EM-1| at q₀
   falls outside [0.1, 10] MeV, then EM-1 is **refuted as the electromagnetic part of n − p**
   (scope (a): this term on this map). A result of the wrong sign would refute the construction
   itself. Prediction 4 is that EM-1 is refuted.
5. **EM-2: about −0.76 MeV at q₀** (α times the S part of §35 M2, ≈ −104.58 MeV), and it
   **diverges like h⁻²** as q → 1 through the m_μ pole.
   **Note made before computing:** I knew this number lands near the lattice −1.00 MeV when I
   listed EM-2. Its agreement therefore carries **no evidential weight**: it was foreseeable, and
   it was not tested blind. EM-2 also rides the ℏ_q⁻² pole, which §35 and §39 already established
   is the wrong place for a degree-0 term. EM-2 is **not adopted**, whatever it gives.

## What would count, and what would not

- If EM-1 lands at keV and EM-2 at about −0.76 MeV, as predicted: the result is that **α times the
  charge structure, on the scale where degree-0 terms are finite at q = 1, is about three orders of
  magnitude short.** The missing factor is the ratio between the nucleon's own length scale and the
  electron map's unit, and this test derives neither. That is a scope (a) negative for EM-1, not an
  exclusion of an EM term.
- Swapping to a different scale after seeing the numbers, such as m_p or E₀, would be selection
  against the target. It is not done here.

Comparison printed after: CODATA m_n − m_p = 1.29333 MeV; BMW 2015 lattice QED part ≈ −1.00 MeV.

# Pre-registration: hydrogen orientation, bond chirality and the corpus capture braid (2026-11-22)

Owner, 2026-11-22: *"1"* (try the other bond chirality) and *"what is the braid word for an electron
bound with the proton? There should be one coming from Breit–Wheeler pair production and γγ
processes."* Written and committed before any number for this probe is computed.

Same functionals, projectors and decision rule as `PREREGISTRATION-hydrogen-bound-orientation.md`
(§42): B1 = tr(T³·W·Π_O), B2 = tr(T³·K·W·Π_O), Π_O = proton strands carrying w = 2 (O₊) or
w = 1 (O₋) zeros; S := F(O₊) + F(O₋); fixed iff exactly one orientation is neutral, for both
placements. Exact sympy over ℚ(q), 60 dps at q₀ (`Q_50_DIGIT_STR`). No float64.

## Arm 1 — bond chirality (6 strands)
§42 with the bond G′ = (σ₂⁻¹σ₃)³ in place of G = (σ₂σ₃⁻¹)³, proton left and right.
Predictions: values ±6 at q = 1 (the q = 1 argument of §42 P1 does not depend on the bond's
chirality); no orientation neutral at q₀; S(1) = 0. Not predicted: the sign of S. **Reading fixed
in advance:** if S_B1 for G′ has the opposite sign of S_B1 for G at the same placement, the
asymmetry is set by the bond's chirality, a second convention.

## Arm 2 — the corpus capture braid (4 strands)
The corpus already has a word for an electron bound to a nucleus. In the γγ shell model
(`QOU.ShellCondensation.GammaGammaAtom`, `docs/audits/2026-11-21-magic-shells-gamma-gamma-model.md`,
step 6 of `def:derived-atom`) the nucleus is one strand and capture of electron k is
K_k = A_{0k}⁻¹, the inverse pure braid in which strand k encircles strand 0 (closure: a Hopf link,
negative nucleus–electron orientation). Hydrogen is W₁ = K₁ = σ₀⁻².
Here the nucleus is cabled to its three strands, and the electron (one strand) encircles the whole
cable: proton left, W = N · (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹, N = (σ₀σ₁⁻¹)³ on strands 0–2, electron strand 3;
proton right, W = N′ · (σ₀σ₁σ₂σ₂σ₁σ₀)⁻¹, N′ = (σ₁σ₂⁻¹)³ on strands 1–3, electron strand 0.
Cabling the one-strand nucleus is the one choice made here; it is not in the corpus model, which
quotients the nucleus to one strand (owner card D1, 2026-11-21).
Predictions: at q = 1 the capture is the identity and N = 1, so F₁ = F₂ = Σ T³_p = +3 (O₊),
−3 (O₋), the electron share is 0; no orientation neutral at q₀; S(1) = 0.

## Overall prediction
Not fixed in either arm. Honesty clause as in §42: nothing is chosen for its n − p outcome.
**Pre-registration completed: 2026-11-22T10:00:06 (UTC), before any computation for this probe.**

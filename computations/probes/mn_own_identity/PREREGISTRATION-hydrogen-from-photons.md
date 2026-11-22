# Pre-registration: hydrogen as one Hecke element built by the six steps of `def:derived-atom` (2026-11-22)

Owner request (relayed by the parent session): build hydrogen as **one** Hecke element by running the
six steps of `def:derived-atom` from photons, instead of writing the Borromean core 𝓑₃ by hand, and
test in that element whether either p ↔ n orientation is neutral, with the §42/§43 tests. Written
and committed before any number for this probe is computed.

Photon (owner ruling 2026-11-18/20): γ(φ₀, φ₁, φ₀₁) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹. Hecke
(σ − q)(σ + q⁻¹) = 0, Ř = [[q,0,0,0],[0,0,1,0],[0,1,q−q⁻¹,0],[0,0,0,q]] on C²⊗ⁿ, h = q − q⁻¹.
Convention D. Proton pin q₀ = `Q_50_DIGIT_STR`. Exact sympy over ℚ(q) (ℚ(q, φ) in arm Φ); mpmath
60 dps at q₀. No float64.

## 1. What each step is, and which corpus artefact fixes it

| step | content in the element | fixed by | status |
|---|---|---|---|
| 1 pair production | one γγ collision on the proton's three strands, γ(0,0,qh)·γ(0,0,−q⁻¹h) | Lean `borromeanV3A_eq_switched_photon_product` / `…B…`; the colour weights qh, −q⁻¹h are the only weights the corpus derives (the eigenvalues q, −q⁻¹ of σᵢ; `docs/audits/2026-11-20-qbeta-flavour-weight-split.md` §1, arm γ). Other recorded weights (φ = 0.0487, s = 0.0978) are labelled fits and are not used. | **partly built.** `def:derived-atom` says "three independent collisions per nucleon"; the corpus gives no element for three collisions, no strand count for a single q q̄ pair, and no φ beyond the eigenvalue pair. What is built is the one collision the corpus derives. |
| 2 quark selection | no letters: each selected quark is a strand (owner 2026-11-20: the up quark is an unknot strand, a component of the Borromean braid). Flavour enters only through the T³ weight of the strand, which is what the orientation test assigns. | owner ruling 2026-11-20; `quark-antiquark-production-reduction.md` | **built as "no letters"**; the quark *tail* used in `nuc11_interleaved` is a chosen census template (`isotope_record_schema.py` provenance note) and is not used. |
| 3 Borromean confinement | 𝓑₃ = V³, V = σ₀σ₁⁻¹. By the Lean identity above this **is** the step-1 product, so steps 1 and 3 coincide in the element. | Lean identity; `GammaGammaFrobeniusSelection.frobeniusSelected_borromean` | built (as the photon product, not by hand). Checked on C²⊗⁴ as a check C1. |
| 4 gluon | owner-unresolved (`gluon-stabiliser-ledger.md`: four statements, two answers; `qou-99qc`). Run as four labelled arms, all reported, none ranked: **G0** empty (γγ rule + reading 3 on the bare core: V³ is already feasible, χ_k > 0 ⇔ 3∣k, `GammaGammaSelectionTen`, so the minimal γγ gluon on a tail-less core is k = 0); **GV** V (the γγ reading-3 survivor k = 1 *with the census tail*, `gg_gluon_segment/results.md`); **Gσ₁** σ₁ (universal-ILP witness record); **GL₋** L₋ = σ₁σ₀ (proton/neutron blocks). σ₀σ₀ (`nuc11_interleaved`) is owner-rejected under reading 3 and is not run. | the four corpus statements named | **blocker**: no single gluon is fixed by the corpus. |
| 5 nuclear assembly | none: A = 1 has no inter-nucleon crossing | `def:derived-atom` step 5 | built (empty). |
| 6 electron cloud | γγ shell model, nucleus = one strand, capture K₁ = A₀₁⁻¹; hydrogen W₁ = K₁ (no interaction I_k, no emitted photon E_k: both start at k = 2). Electron = one strand. | `GammaGammaAtom.lean`, `docs/audits/2026-11-21-magic-shells-gamma-gamma-model.md` §2 | built, **with one choice**: the one-strand nucleus is cabled to its three strands. |

Choices made here, each labelled:

- **C-cable** (as §43): the electron strand encircles the whole proton cable,
  K = (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹ (proton strands 0–2, electron 3). **C-adj** (sensitivity arm): it encircles
  only the adjacent proton strand, K = σ₂⁻². Neither is in the corpus model, which quotients the
  nucleus to one strand (owner card D1).
- Order: element = (step 1·3) · (step 4) · (step 6), i.e. W = γ(0,0,qh)·γ(0,0,−q⁻¹h)·g·K, applied
  rightmost first as in the §42/§43 engine. V commutes with V³, so the GV arm has no placement
  ambiguity; Gσ₁ and GL₋ are placed after the core, per the step order.
- Placement control (as §42/§43): proton right, strands 1–3, electron strand 0, every word mirrored
  (generator i ↦ 2 − i on the proton, capture (σ₀σ₁σ₂σ₂σ₁σ₀)⁻¹ resp. σ₀⁻²).
- **Arm Φ** (no selection): the general collision γ(φ)·γ(ψ) with six symbolic weights
  (φ₀, φ₁, φ₀₁, ψ₀, ψ₁, ψ₀₁) on the proton strands, gluon G0, capture C-cable, proton left and right.
  Reported as exact polynomials; no value of φ, ψ is chosen. Its specialisation to the derived
  weights must reproduce the G0/C-cable arm (check C2).
- Not built: three collisions per nucleon (would need an unspecified 6-strand-per-pair element and
  selection map); the electron as the ruled 3-strand σ₀σ₁σ₀ (needs a bond, which §42 had to choose).

## 2. Functionals and decision rule (unchanged from §42/§43)

B1 = tr(T³·W·Π_O), B2 = tr(T³·K_U·W·Π_O) with K_U = q^{2T³}; Π_O projects onto proton strands
carrying w = 2 zeros (O₊) or w = 1 (O₋); S := F(O₊) + F(O₋); also the electron-strand share of B1.
**Orientation fixed iff exactly one of O₊/O₋ is neutral (B1 = 0 at q₀), for both placements.**
Arm Φ: fixed only if this holds identically in (φ, ψ); a region of (φ, ψ) where it holds would be
reported as a region, not adopted.

## 3. Predictions (derived before computing)

- P1 (q = 1): σ ↦ transposition, V³ ↦ id, pure-braid captures ↦ id. So G0: B1(O±) = ±3 for both
  cablings. GV and GL₋: V and L₋ are 3-cycles on the proton strands, which fix no state with
  w ∈ {1, 2}, so B1(O±)(1) = 0 for both orientations (both neutral at q = 1; trivially). Gσ₁:
  σ₁ fixes proton states with s₁ = s₂, giving B1(O±)(1) = ±1.
- P2: G0/C-cable is the same element as §43 arm 2, so S_B1 = −h²[3]_q (left) and +h²[3]_q
  (right), O₊ = +1.97252, O₋ = −2.08049 at q₀ (left). This is a consistency prediction, not new.
- P3: S(1) = 0 in every arm (q = 1 relabel symmetry, Lean `FlipSymmetryAtOne`).
- P4: no orientation is neutral at q₀ in any built arm; hence not fixed. Not predicted: signs of S
  for GV, Gσ₁, GL₋, C-adj; whether arm Φ's S vanishes identically (predicted: it does not).

## 4. Honesty clause

I know the §42/§43 results (no word fixes the orientation; S follows placement). Nothing in the
arms is chosen for its n − p or neutrality outcome; every arm is reported. The gluon is
owner-unresolved and is reported as the blocker of step 4, not settled here.

**Pre-registration completed: 2026-11-22T10:53:02Z (UTC, `date -u`), before any computation for this probe.**

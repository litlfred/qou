# Pre-registration: hydrogen on its full strand count from γγ production — where does the gluon enter? (2026-11-22)

Owner question (verbatim): *"If we work on the full stands of γγ production starting from all the
necessary photons to produce hydrogen. Where do we see the gluons come in? We should see it in the
braid somewhere working on the full Tower. Was it a knot operation that bound the quarks together so
that that knot operation corresponds to the gluon?"* Plus: *"See sibling for minimal crossing
energy"* and *"enumerate γγ words up to a cap"*. Written and committed before any number for this
probe is computed.

Fixed inputs. Photon (owner ruling 2026-11-18/20): γ(φ₀,φ₁,φ₀₁) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹.
Hecke (σ − q)(σ + q⁻¹) = 0, Ř as in §46 on C²⊗ⁿ, h = q − q⁻¹. Convention D, z = q³/(q²+1). Proton
pin q₀ = `Q_50_DIGIT_STR`. Owner ruling 2026-11-22: **the step-4 gluon stays open** — this probe
identifies and measures, it does not select. Crossing energy (sibling, `def:crossing-energy`, Lean
`BorromeanWordForcing.wordEnergy`): E(w) = n₊·q − n₋·q⁻¹; the owner accepted its minimisation as a
selection rule **for the proton's Borromean word only** (2026-11-22); here it is only measured.
Exact sympy over ℚ(q) / ℚ(q,φ,ψ) where symbolic; mpmath 60 dps at q₀ for large enumerations (signs
certified against a 1e-45 band; a value inside the band is reported "undecided"). No float64.

## 1. Strand bookkeeping (construction F, every choice labelled)

Tower: **H₈(q)**, the smallest holding one strand per particle: three selected quarks, three
antiquarks, e⁻, e⁺ (up quark = one strand, owner 2026-11-20; electron = one strand in the capture
model, as §46 and `GammaGammaAtom.lean`; the ruled 3-strand electron σ₀σ₁σ₀ is not used, as in §46).

Layout F (choice): positions 0,1,2 = q₁,q₂,q₃ (the quark kept from pair k), 3 = e⁻, 4 = e⁺,
5,6,7 = q̄₁,q̄₂,q̄₃. Kept strands are left of disposed strands so that disposal (step 2 antiquarks,
step 6 positron) is the closure of the **rightmost** strands, i.e. the convention-D conditional
expectation E₈→₄. In C²⊗ⁿ this is the partial trace with weights diag(q², 1)/(q² + 1) per closed
strand (to be checked: E(σ_last) = z_D, E(1) = 1).

Letters, by step:

| step | letters placed in layout F | source |
|---|---|---|
| 1 pair creation (q_k q̄_k), k = 1..3, and Breit–Wheeler (e⁻e⁺) | **none**: γγ on two strands is the identity (`two-photon-pair-production`); in layout F a pair's two strands are not adjacent, so no two-strand letter could be placed without moving strands (moving them is not specified anywhere) | corpus |
| 1+3 quark collision | γ(0,0,qh)·γ(0,0,−q⁻¹h) on positions 0–2 = V₀³ (Lean identity) | corpus |
| antiquarks | arm **A-ann** (annihilate: no letters, strands closed) / arm **A-bar** (antinucleon: the same collision on 5–7, V₅³) | `def:derived-atom` step 2 |
| 4 gluon | arms G0 / GV / Gσ₁ / GL₋ on positions 0–2, as §46 | open (owner) |
| 6 capture | C-cable K = (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹ on 0–3, as §46 | §43/§46 choice |

Full word W₈ = V₀³ · [V₅³] · g · K (rightmost applied first), written out letter by letter with each
crossing's strand **labels** (tracked through the permutation), and each letter classified as
intra-pair / cross-pair (quark–quark of different pairs) / quark–lepton / antiquark–antiquark.

## 2. Measurements

- **M1** the cross-pair letter list of W₈ for each arm.
- **M2** disposal: E₈→₄(W₈) against c·W₄ with W₄ the §46 element V₀³·g·K; test exact
  proportionality (all 16×16 matrix entries on C²⊗⁴, symbolic in q) and report c.
- **M3** the general collision γ(φ)γ(ψ) on three strands: its 16 braid words with coefficient
  monomials, and its NF; which of the four ledger candidates (σ₁; σ₀σ₀; L₋ = σ₁σ₀; V) occur as words
  and with which weight; and what survives at the derived weights (qh, −q⁻¹h).
- **M4** writhe test: writhe of each ledger candidate vs the writhe of γγ words (products of
  vertices, Lean `GammaGammaWord`).
- **M5** enumeration of γγ words (products of vertices σ_iσ_{i+1}⁻¹) up to the **cap of 6 crossings**
  (3 vertices), at three levels: H₃ (vertex V₀ only: 3 non-empty words), H₄ (V₀, V₁: 14), H₈
  (V₀…V₅: 258). For each word w: reading 3 (χ_λ(w) ≥ 0 for every two-row λ, the blocks with y_λ > 0
  under D), crossings, |tr_M(w)| (convention D), E(w). As gluon-on-core elements also:
  H₃ core·g, H₄ V₀³·g·K. Report what each corpus objective would pick among admissible non-identity
  words: (a) min crossings, (b) min |tr_M|, (c) min E. **Reported, not adopted.**
  Characters via quantum Schur–Weyl on C²⊗ⁿ: χ_j = Tr|_{T³=j} − Tr|_{T³=j+1}.
  Also the four ledger candidates on the bare core (H₃): reading 3, crossings, |tr_M|, E.

## 3. Predictions (derived before computing)

- P1: at derived weights the only letters joining quarks of different pairs are the six letters of
  V₀³ (plus the gluon-arm letters); pair creation and BW contribute none; the capture contributes
  quark–lepton letters only.
- P2: E₈→₄(W₈) = c·W₄ exactly, c = 1 (A-ann), c = tr_M(V³) on H₃ (A-bar) since V₅³ touches only
  closed strands.
- P3: every γγ word has writhe 0; σ₁ (1), σ₀σ₀ (2), L₋ (2) do not, so of the four ledger candidates
  only V is a γγ word.
- P4: in γ(φ)γ(ψ) the words σ₁, σ₀σ₀, L₋, V all occur, with coefficients φ₁+ψ₁, φ₀ψ₀, φ₁ψ₀,
  φ₀₁+ψ₀₁; at derived weights the product is 1 + h²V − h²V² = V³ and none of σ₁, σ₀σ₀, L₋ survives.
- P5: on H₃, V^{3+k} passes reading 3 iff 3 | k (`GammaGammaSelectionTen`), so among non-empty γγ
  gluons up to the cap only V³ passes on the bare core. Crossing energy on γγ words is
  (crossings)·h/2, so (a) and (c) coincide on γγ words.
- Not predicted: H₄ and H₈ pass counts and picks; ledger-candidate reading-3 signs at H₃ (partly in
  §46's diagnostic).

## 4. Decision rule

The hypothesis "the cross-pair binding operation is the gluon" is **supported in construction F**
only if, after disposal, the cross-pair sub-word coincides with one of σ₁, σ₀σ₀, L₋, V beyond the
core. It is **not found in construction F** if the only cross-pair binding sub-word is the core V³
itself; the identification then reported is "the binding operation is the vertex V, which is also
the γγ gluon unit" — an identification of a shared unit, not a selection of a gluon.

## 5. Honesty clause

The layout, the one-strand electron and the capture are choices, listed above. No object is chosen
for a numerical outcome; every arm and every enumerated word is reported. The gluon remains open.

**Pre-registration completed: 2026-11-22T11:51:41Z (UTC), before any computation for this probe.**

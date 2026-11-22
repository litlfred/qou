# Pre-registration: hydrogen from γγ production with each pair's strands adjacent (2026-11-22)

Follow-up to §50 (`PREREGISTRATION-hydrogen-full-strand-gammagamma.md`, probe
`mn_hydrogen_full_strand_probe.py`, layout F = q₁q₂q₃e⁻ | e⁺q̄₁q̄₂q̄₃). §50 left unbuilt: layouts in
which each created pair's two strands are adjacent, the σ₀σ₁σ₀ electron, and reading 3 on the whole
H₈ element. Written and committed before any number for this probe is computed.

Fixed inputs (unchanged from §50). Photon (owner ruling): γ(φ₀,φ₁,φ₀₁) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹.
Hecke (σ − q)(σ + q⁻¹) = 0, h = q − q⁻¹. Convention D, z = q³/(q²+1). Proton pin q₀ =
`Q_50_DIGIT_STR`. Engine: §50's C²⊗ⁿ Ř-matrix engine (copied), and a new Iwahori-basis Hecke
engine for H_n (n ≤ 9) over the exact field ℚ(q) to express residues in a faithful basis.
**Owner ruling 2026-11-22: the step-4 gluon stays open.** This probe identifies and measures
candidates; it selects nothing and names nothing "the gluon".

## 1. Construction (every choice labelled)

**Layouts** (positions 0..7, each pair's strands adjacent):

| name | layout | kept order after gathering |
|---|---|---|
| L1 | q₁ q̄₁ q₂ q̄₂ q₃ q̄₃ e⁻ e⁺ | q₁ q₂ q₃ e⁻ |
| L2 | q̄₁ q₁ q̄₂ q₂ q̄₃ q₃ e⁺ e⁻ | q₁ q₂ q₃ e⁻ |
| L3 | e⁻ e⁺ q₁ q̄₁ q₂ q̄₂ q₃ q̄₃ | e⁻ q₁ q₂ q₃ |
| F (control, §50) | q₁ q₂ q₃ e⁻ e⁺ q̄₁ q̄₂ q̄₃ | q₁ q₂ q₃ e⁻ |

**Pair creation and Breit–Wheeler**: no letters (corpus: γγ on two strands is the identity). In
the adjacent layouts a two-strand letter on a pair *could* be placed; it is not, since nothing in
the corpus places one. Stated as a choice.

**Gathering.** The collision V³ needs the three quark strands adjacent, and the capture needs e⁻
next to them; in L1–L3 they are not. The kept strands {q₁,q₂,q₃,e⁻} are moved to positions 0..3 by
the minimal shuffle that preserves the relative order of kept strands and of disposed strands
(target frame F′: kept order as in the table, then the disposed strands in their original order).
Its braid G_T is the permutation braid of that shuffle with **all letters positive (T = +) or all
negative (T = −)**. The corpus does not specify the sign; both are arms.

**Collision, gluon slot, capture** (in frame F′, the §46 element):
- L1, L2, F: Y = V₀³ · g · K, V₀ = σ₀σ₁⁻¹ (the ruled vertex itself), K = (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹.
- L3 (e⁻ at 0): Y′ = V₁³ · g′ · K′, K′ = (σ₀σ₁σ₂σ₂σ₁σ₀)⁻¹, core at positions 1..3, so the bond
  reading matters: **reading A** V₁ = σ₁σ₂⁻¹ (invert the larger letter, production), **reading B**
  V₁ = σ₁⁻¹σ₂ (reflected letter). Both reported side by side; no choice made.
- Gluon arms as §46/§50: g ∈ {G0 = 1, GV = V₀, Gσ₁ = σ₁, GL₋ = σ₁σ₀}; in L3 shifted one strand
  right: {1, V₁(reading), σ₂, σ₂σ₁}.

**Disposal** of the antiquarks and e⁺ = closure of their strands. A disposed strand that is not
rightmost is closed by an arc that runs to the right on one side (behind or in front): the
disposal on side S is E_{8→4}(G_S · Z · G_S⁻¹), E the convention-D conditional expectation (closure
of the rightmost strands, E(σ_top) = z_D, E(1) = 1), S ∈ {+, −}. The whole H₈ element in layout
coordinates is Z_L(T,S) = G_S⁻¹ · Y · G_T, so the disposed element is
  E(Y · G_T · G_S⁻¹) = Y · R_{TS},   R_{TS} := E_{8→4}(G_T G_S⁻¹) ∈ H₄
(E is an H₄-bimodule map). For T = S, R = 1 identically. For T ≠ S, G_T G_S⁻¹ is a pure braid in
which each disposed strand encircles the kept strands it passed.

## 2. Measurements

- **M1** letter bookkeeping of Z_L(T,S) for every layout/arm, each letter classified by its strand
  labels (intra-pair, cross-pair quark–quark, quark–antiquark of another pair, quark/lepton–
  antiquark, lepton pair, …). Which letters join quarks of different pairs.
- **M2** disposal: R_{TS} for every layout and T,S, in the Iwahori basis {T_w : w ∈ S₄} of H₄ over
  ℚ(q) (exact), cross-checked against the C²⊗⁸ partial-trace disposal at q = 3 and q₀ (16×16 entries,
  exact Fractions). Report: is R scalar; which letters σ₀ (q₁–q₂ in L1/L2), σ₁ (q₂–q₃), σ₂ (q₃–e⁻)
  occur in its support; is R in span{1, V, V²} (V = the vertex of the kept quark window); is R
  central in H₄. Answer to the owner-side question: does any letter other than V join quarks of
  different pairs after disposal?
- **M3** reading 3 on the **whole** H₈ element Z_L(T,S), every gluon arm and reading: two-row
  characters χ_λ (the blocks with y_λ > 0 under D) via quantum Schur–Weyl on C²⊗⁸,
  χ_j = Tr|_{T³=j} − Tr|_{T³=j+1}; pass iff all χ_λ ≥ 0. Also tr_M (convention D) and crossing
  energy E = n₊q − n₋q⁻¹ (measured only).
- **M4** enumeration: whole element Z_L(T,S)·w with g = G0, w a γγ word in layout coordinates
  (product of 1..3 vertices V_i, i = 0..5, V₀ = σ₀σ₁⁻¹, V_i (i ≥ 1) in reading A or B), **only
  freely reduced words**. Reduction rule: free reduction in the free group on the σ_i (delete any
  adjacent σ_iσ_i⁻¹ or σ_i⁻¹σ_i); a vertex product is kept iff it is already freely reduced
  (equivalently V_iV_{i+1} is never adjacent, in both readings). Layouts L1, L2, L3 (and F), arms
  (T,S) ∈ {(+,+), (+,−)}, readings A, B. Per word: reading 3, |tr_M|, crossings, E. Picks of the
  corpus objectives (min crossings, min |tr_M|, min E) reported, not adopted. Numeric at q₀ with
  mpmath 60 dps; a character within 1e-45 of 0 is "undecided".
- **M5** electron arm: e⁻ as the ruled word σ₀σ₁σ₀ on three strands (Hopf closure). Kept frame H₆ =
  q₁q₂q₃e₁e₂e₃, Y₆ = V₀³ · g · K_c · (σ₃σ₄σ₃), K_c the 3-cable of K (the electron bundle loops the
  quark bundle: inverse of the positive permutation braid of the block swap times its return).
  Layouts F₃ = q₁q₂q₃e₁e₂e₃ | q̄₁q̄₂q̄₃ and L1₃ = q₁q̄₁q₂q̄₂q₃q̄₃e₁e₂e₃ (positron, three strands with
  the mirror word, never crosses: closes to the scalar tr_D(σ₀⁻¹σ₁⁻¹σ₀⁻¹), reported). Report R_{TS}
  on H₉→H₆, reading 3 on Y₆ and on the whole H₉ element, tr_M.

## 3. Predictions (derived before computing)

- **P1** In every layout the only cross-pair quark–quark letters of Z are the 6 core letters (plus
  gluon-arm letters); gathering letters are all kept–disposed crossings. L1: 6 gathering letters,
  none intra-pair. L2: 10, of which 3 are q_k–q̄_k (intra-pair) and 1 e⁻–e⁺. L3: 6, none intra-pair.
- **P2** T = S: disposal returns exactly Y (c = 1) in every layout (R = 1 by construction; the C²⊗⁸
  check must agree).
- **P3** T ≠ S: R_{TS} is not scalar. In L1 it lies in ⟨σ₁, σ₂⟩ (q̄₁ encircles q₂q₃e⁻, q̄₂ encircles
  q₃e⁻, q̄₃ encircles e⁻ only) and contains σ₁, a letter joining q₂–q₃ that is not V. It is not in
  span{1, V, V²}. In L2, q̄₁ encircles all four kept strands; R involves σ₀, σ₁, σ₂.
- **P4** L3 reading B: characters and tr_M of Y′(B, G0) equal those of Y(G0), by strand reflection
  (`towerTr_reflect`) plus conjugation by σ₂ (which commutes with K′). Reading A: not predicted.
- **P5** Enumeration pass counts and picks: not predicted.
- **P6** Electron arm without capture would factor through tr_D(σ₀σ₁σ₀) = q³(q⁴+1)/(q²+1)²; with
  the cabled capture nothing is predicted.

## 4. Decision rule

A **candidate gluon letter** is reported for layout L iff after disposal the kept element contains,
beyond Y, a letter joining quarks of different pairs (R non-scalar with σ₀ or σ₁ in its support).
If such letters arise **only** in the T ≠ S arms, they are reported as produced by the mismatch
between the gathering side and the closure side — a convention of the construction, not a letter
the photons place — and the identification is scope (a). If no arm produces one, the result is
"not found in the searched class". Nothing is selected; the gluon stays open.

## 5. Honesty clause

The layouts, the gathering braid and its sign, the closure side, the one-strand electron in M1–M4,
the capture cable, and the gluon-slot shift in L3 are choices, all listed. Every arm and every
enumerated reduced word is reported. No object is chosen for a numerical outcome.

**Pre-registration completed: 2026-11-22T15:14:06Z (UTC), before any computation for this probe.**

## Addendum 2026-11-22 (after the first run; the text above is unchanged)

Owner ruling the same day (`docs/coordination/owner-rulings.md`, PR #9019;
`docs/audits/2026-11-22-sign-conventions-table.md` §6): **reading A plus right-hand closure is
canonical**. The vertex at strands (i, i+1) is σ_iσ_{i+1}⁻¹ (larger letter inverted); a bond's side is
set by closing on the right. Reading B is retired. Consequences for this probe:
- All results are reported in reading A. Every reading-B number already computed is moved to a section
  of the `.out.json` labelled `non_canonical_comparison (reading B retired 2026-11-22)` and is not a live
  alternative. P4 becomes a non-canonical comparison check.
- The disposal already closes on the right (E_{8→4} closes the rightmost strands). The ruling does not
  decide the **over/under sign** of the gathering braid (T) or of the closure arc (S); those stay arms.
- Nothing else in the construction, predictions or decision rule changes.

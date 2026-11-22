# PRE-REGISTRATION: a spin factor separate from colour (beans `qou-ni4b`, `qou-bwwr`; issue #9058)

Owner choice on PR #9059: *"Add a spin factor first"*. Build a spin factor that is separate from
colour, then test it. Written and pushed before any probe code exists.

## Why

- `qcd_colour_action/RESULT.md`: with colour strand-wise (classical sl₃ or U_p(gl₃)) and the
  braiding in the class Ř = s_c⊗X + a_c⊗Y (K4), a braiding that carries colour with flavour
  (q→1 limit ±P) needs (p²−1)² = (q²−1)² = 0. At generic q colour stays at its position (K0).
- `qcd_spin_background/RESULT.md`: colour-only data has no paramagnetic (2s)² piece and no
  N-independent diamagnetic −1/3 piece. The missing object is a twist acting on spin and not on
  isospin, the hypothesis `θI = 1` of `QOU/Hecke/TwistedChannelSplitting.lean`, which that file
  states is derived nowhere.
- `qcd_heat_kernel`, `qcd_scale_candidates`: screening, or power-law (N1: b = N/(k+N)) only.

## Corpus grep, 2026-11-22

- `bun scripts/corpus-search.ts "spin twist ribbon" --limit 200`: **no seeds**. Also no seeds for
  "spin statistics" and "Deligne product". "twist" and "framing" reach `def:strand-twist-datum`
  (which states that in a ribbon category the twist is fixed by the braiding, so a free per-strand
  twist is an addition), `rem:fermionic-twisted-sectors`, `prop:chirality-writhe-ribbon-derivation`,
  `prop:sl-n-color-framing`. None carries a spin tensor factor separate from colour.
- grep `spin factor|spin-only|θ_I|Deligne|chromomagnetic|helicity` over `folio/`, `docs/audits`,
  `beans/defs`: no construction of a per-strand C²_spin ⊗ C^N_colour braiding, no Deligne-product
  twist, no chromomagnetic background. `TwistedChannelSplitting.lean` remains the closest object.

## Setting (exact over ℚ(p, r, q); no float64)

Per strand W = C^N_colour ⊗ C²_spin. Colour: Jimbo Ř_c(p) of U_p(gl_N) (p = 1: the swap P_c).
Spin: Jimbo Ř_s(r) of U_r(gl₂) (r = 1: the swap P_s). Projectors
Π^c_S = (Ř_c + p⁻¹)/(p + p⁻¹), Π^c_A = (p − Ř_c)/(p + p⁻¹), and the same for spin with r.
For generic p, r the commutant of U_p(gl_N) ⊗ U_r(gl₂) on W⊗W is spanned by the four products
Π^c_a ⊗ Π^s_b (a, b ∈ {S, A}), so the class below is **every** strand-wise colour-and-spin
symmetric braiding on W⊗W.

## Constructions

**P1 (spin as the extra factor of K4; exhaustive in its class).**
Ř = Σ_{a,b} λ_ab Π^c_a ⊗ Π^s_b with each λ_ab ∈ {q, −q⁻¹} (Hecke with eigenvalues q, −q⁻¹):
16 assignments, each at (p, r) ∈ {(1,1), (1, r), (p, 1), (p, r)} with p, r symbolic.
*Transported* means λ_SS = λ_AA and λ_SA = λ_AS with opposite limits, i.e. Ř → ±P_c⊗P_s.
Compute the braid residual σ₁σ₂σ₁ − σ₂σ₁σ₂ on three strands in every irrep pair
(colour λ ⊢ 3 with ≤ N rows) × (spin μ ⊢ 3 with ≤ 2 rows) using seminormal Hecke matrices,
for N = 2, 3, 4. Take a lex Gröbner basis of the numerators in (p, r, q). Cross-check the
irrep result against the explicit 216-dimensional operator (N = 3) at rational points with
exact `Fraction` arithmetic.
**Prediction:** the K4 obstruction persists. Every transported member needs q² = 1 (with
p² = r² = 1). The members that braid at generic q keep colour fixed (λ_Sb = λ_Ab) or spin fixed
(λ_aS = λ_aA), or are the colour-flavour degenerate scalar cases. Spin is the same algebra as the
nucleon flavour C² of the sibling probe, so this is expected, and it is reported either way.

**P2 (a ribbon twist on the spin factor only, derived).**
Three per-strand braidings on C²_spin ⊗ C²_isospin, all with Hecke spin factor Ř_s(q):
(D) Deligne product Ř_s(q) ⊗ P_I (isospin classical, transported);
(F) K0-type Ř_s(q) ⊗ 1_I (isospin at fixed position);
(Y) symmetric Ř_s(q) ⊗ Ř_I(q) (one braided category on both).
For each: braid relation (n = 3, symbolic); whether Hecke holds (D is predicted **not** Hecke:
eigenvalues ±q, ±q⁻¹); the full twist Δ²_n for n = 3, 4 compared with Δ²_s ⊗ (Δ²_I or 1).
Prediction: D and F give Δ² = Δ²_s ⊗ 1_I, because the classical full twist is the identity
permutation (D) or the isospin is not braided (F); so **θ_I = 1 is derived** in D and F,
from isospin being classical or unbraided, not assumed. Y gives Δ²_s ⊗ Δ²_I, the symmetric case.
On (C²)^{⊗n}, n = 2..6, verify Δ²_s acts on two-row shape λ as q^{2c(λ)} (c = content sum) via
the minimal polynomial. Then the deuteron (spin (4,2), isospin (3,3)) minus singlet split
s·i′ − s′·i of `twisted_split` with the full twist: predicted q¹⁰ − q⁶ for D and F, 0 for Y.
Side computation (pre-declared): with the q-trace on the q-deformed spin factor and the ordinary
trace on a classical isospin factor, the *untwisted* isotypic traces already differ; predicted
deuteron − singlet = f^{(4,2)} f^{(3,3)}([3]_q − 3) = 45(q − q⁻¹)², i.e. the classical-isospin
route also breaks the equal-trace (Pauli-lock) premise of `qou-7zob`. Reported, not claimed as
a mechanism.

**P3 (does a spin factor split a β₀-type coefficient into (2s)² and −1/3?).**
Backgrounds per strand, a a traceless colour Cartan vector:
chromomagnetic h = a ⊗ σ_z (colour charge × 2s_z, the Nielsen–Hughes spin coupling);
colour charge h₀ = a ⊗ 1; Zeeman h_s = 1 ⊗ σ_z. On n strands H = Σ_i h^{(i)}.
(i) Covariance: for general symbols λ_ab, solve [H, Σ λ_ab Π^c_a ⊗ Π^s_b] = 0 on W⊗W (N = 3,
explicit, p, r symbolic and p = r = 1). Prediction: only λ_SS = λ_AA and λ_SA = λ_AS (Ř in
span{1, P_c⊗P_s}) at p = r = 1, and nothing at generic p or r, so with P1 a Hecke braiding with
chromomagnetic covariance exists only at q² = 1. h₀ and h_s are predicted to commute with every
member of the class.
(ii) At the classical point (the only one where (i) allows it) compute per-state susceptibilities,
in units of the fundamental, χ_X(B) = ([ε²] Tr(e^{εB} X)/Tr X) / ([ε²] Tr_{C^N⊗C²} e^{ε b}) / …
with B ∈ {H, H₀, H_s} for the channels X invariant under H: Sym²W, Λ²W (n = 2) and the S₃
isotypic projectors P_(3), P_(2,1), P_(1³) on W^{⊗3} (n = 3), for N = 2, 3, 4. Define the
correlation remainder κ(X, N) = χ_X(H)/χ_X(H₀) − χ_X(H_s). For n = 1, κ = 0 (factorisation).

### Acceptance test for P3 (fixed now)

HIT requires all of: (1) a channel X, invariant under the chromomagnetic background, with a
(2s)² piece: χ_X(H_s) contains the spin-1 value (2s_z)² = 4 per helicity state; (2) a
remainder κ(X, N) that does **not** depend on N (N = 2, 3, 4 give the same value) and equals
−1/3 exactly (STRONG) or lies in {−1/3, 1/3, −1/12, 1/12, −2/3, 2/3} (weak); (3) the sign is read
without choosing a convention; (4) at generic q, or at q = 1 with a stated reason why q = 1 is
the right point. **Prediction: MISS.** κ is 0 or N-dependent, because a finite strand algebra
has no orbital (Landau-ladder) factor, and the Nielsen–Hughes −1/3 is the Euler–Maclaurin term of
that ladder (4·B₂(½) = −1/3).

## Coincidences declared now (not hits)

- 2/N and 1 − 1/N both equal 2/3 at N = 3 (sibling S1/S2). Not counted.
- The full-twist exponent 2c(λ) = 2S(S+1) + n(n−4)/2 (from `four_mul_contentSum_pair`). The
  constant n(n−4)/4 is N-independent but n-dependent; it is never −1/3 for integer n. The
  Casimir S(S+1) is not (2S)²: a two-spin linear fit a·S(S+1) + b to (2S)² − 1/3 (s = ½, 1)
  gives a = 12/5, b = −17/15. Any such fit is a fit, not a hit.
- [2j+1]_q expanded in ħ = log q gives ħ² coefficients ⟨(2m)²⟩/2, e.g. 4/3 for j = 1. A 4/3 or
  1/3 obtained this way is a Zeeman average, not a diamagnetic term.

## Honesty clause

No construction is selected by its numbers. Every member of P1 is reported. q₀ is never solved
for; mpmath at the proton pin q₀ only for display. No gluon is identified or selected. A negative
is "not found in the searched class" (scope a) unless the class was enumerated exhaustively and a
Gröbner basis or a proved invariant excludes it (scope b, cite it).

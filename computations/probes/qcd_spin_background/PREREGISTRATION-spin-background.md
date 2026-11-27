# PRE-REGISTRATION — a spin / background-field object for the QCD β₀ sign

Bean `qou-bwwr` (route `qou-ni4b`). Follows `computations/probes/qcd_heat_kernel/RESULT.md`
(C1–C3 gave only screening: a positive heat kernel damps higher-Casimir channels). Owner:
*"Look for a spin or background-field object (route to qou-ni4b)"*. Written and pushed before any
probe code exists.

## Target structure (Nielsen–Hughes)

One-loop β₀ per field of spin s, per helicity state, ∝ −(−1)^{2s}[(2s_z)² − 1/3]: a
**paramagnetic** spin term (2s_z)² and a **diamagnetic** orbital term −1/3 of opposite sign. The
−1/3 is the Landau-ladder Euler–Maclaurin correction and does **not** depend on the gauge group
(it is a property of the orbital motion, not of the colour rep). Gluon (s_z = ±1): 4 − 1/3 = 11/3.

## Corpus grep (six paths + corpus_search CLI), 2026-11-22

- `corpus-search.ts`: "background field", "spin statistics", "ribbon twist spin": **no seeds**.
  "twist"/"framing" reach `def:strand-twist-datum`, `prop:sl-n-color-framing`,
  `prop:chirality-writhe-ribbon-derivation`, `rem:fermionic-twisted-sectors`.
- grep `Nielsen|Hughes|paramagnetic|diamagnetic|background field|Euler.Heisenberg` over
  docs/audits, folio, computations, docs/coordination, library (sections + ocr), beans/defs:
  only mentions are the Nielsen–Hughes formula quoted in
  `mn_own_identity/PREREGISTRATION-beta0-from-braid.md` and unrelated hits (Ito/Dehornoy
  "Nielsen", Hughes–Drever). No Nielsen–Hughes source is held in `library/`; no background-field
  or Euler–Heisenberg construction exists anywhere in the corpus.
- Closest object: `QOU/Hecke/TwistedChannelSplitting.lean` — proves the split for a twist acting
  on a *spin factor only* (`θI = 1`), and states that this asymmetry "is not derived anywhere in
  the corpus … inside a single ribbon category it is false (the natural twist acts on every
  object)". So in qou the ribbon twist is a function of the colour label, not of a separate spin.

## Setting (all exact over ℚ(q), N symbolic where possible)

V = C^N, Jimbo Ř of U_q(gl_N) (σ = q on Sym²V, −q⁻¹ on Λ²V; matrix as in
`ColourStructureConstantCommutator.lean`), σᵢ on V^{⊗n}, n ≤ 3. **Background colour holonomy**
K(ε) = diag(e^{ε a_j}), a traceless Cartan direction (a = (1,−1,0) and (1,1,−2) at N = 3;
(1,−1), (1,−1,0,0) etc. otherwise). K^{⊗n} commutes with every σᵢ (weight preservation), so
Z_X(ε) := Tr(K(ε)^{⊗n} X) is a background-field trace. Its ε² coefficient
χ(X) := [ε²] Z_X / [ε²] Tr_V K is the **background susceptibility** of X, in units of the
fundamental (2T(V) = 1). Exact: [ε²] Z_X = Σ_x X_xx (Σ_i a_{x_i})²/2.

## Constructions and predictions

**S3 (Euler–Heisenberg / background holonomy).** χ(X) for X ∈ {1, σ, σ⁻¹} (n = 2) and
{σ₀σ₁, photon σ₀σ₁⁻¹, core V³, electron σ₀σ₁σ₀, full twist Δ²₃} (n = 3), N = 3 explicit
27×27 matrices; cross-checked against the isotypic formula χ(X) = Σ_λ x_λ f^λ 2T(λ).
Prediction: at q = 1 a permutation with cycle lengths ℓᵢ gives χ = Σᵢ ℓᵢ² N^{#cycles−1}
(a strand cycle of length ℓ couples like charge ℓ — "ℓ²" not "(2s)²"); q-dependence only via h.
**No** separate diamagnetic term. Heat-kernel variant: per-state susceptibility
χ(e^{−tΔ_ξ})/Tr(e^{−tΔ_ξ}) on n = 3, N = 3, at t = 0 and t → ∞: predicted to fall
(1 → 12/17) because Δ_ξ ties (2,1) and (1³) at μ = [2]; whether "falling" is screening or
antiscreening depends on the sign convention for a real vs unitary background, and **both are
reported**.

**S2 (Hecke sign as (−1)^{2s}).** Read Sym² (eigenvalue +q) as bosonic and Λ² (−q⁻¹) as
fermionic. χ(σ) = q·2T(Sym²) − q⁻¹·2T(Λ²) = q(N+2) − q⁻¹(N−2). Prediction: the q = 1 ratio
χ(σ)/χ(1) = 2/N — **group-dependent**, so it is the swap's ℓ² = 4 over 2N, not a Nielsen–Hughes
weight. Known before computing (elementary): at N = 3 this is 2/3 = (2·½)² − 1/3. **Declared in
advance as a coincidence check, NOT a hit**; the N = 2, 4 values decide it.

**S1 (ribbon twist / framing as spin).** Full twist Δ²_n acts on λ by q^{2ct(λ)}; sl-framed by
q^{2ct(λ) − 2n²/(2N)·…} (precisely: σ^{sl} = q^{−1/N}σ, so Δ²^{sl}_n = q^{−n(n−1)/N}Δ²_n).
Expand χ(Δ²) in ħ = log q: order ħ is the "Zeeman" (linear in the twist label ct), order ħ² the
"paramagnetic" (∝ ct²). Prediction: every order is a sum over λ of [positive 2T(λ) f^λ] ×
[power of the twist exponent]; the only negative constant is the framing shift −1/N per crossing,
which is **N-dependent**. Known before computing: on Sym², σ^{sl} has exponent 1 − 1/N, which at
N = 3 is 1 − 1/3 = (2·½)² − 1/3. **Declared in advance as a coincidence, NOT a hit**, because the
Nielsen–Hughes −1/3 is N-independent.

## Hit rule (fixed now)

HIT requires all three: (i) a coefficient that splits into two terms of opposite sign, one a
square of a spin/twist label (paramagnetic) and one **N-independent** constant (diamagnetic);
(ii) a definite net sign that reads as antiscreening without choosing a sign convention;
(iii) values from the pre-listed set {11/3, −1/3, 1/3, 2/3, 4/3, 11/6, 22/3, 11/12, 4, 11}.
STRONG HIT: the 11/3 : −1/3 structure for an adjoint-channel (λ = (2,1) ⊂ V^{⊗3}) object.
Any N-dependent match (e.g. 2/N or 1 − 1/N at N = 3) is a **coincidence, reported, not a hit**.

## Honesty clause

Choosing a sign convention (real vs unitary background, t → ∞ as IR vs UV, Sym² as bosonic) to
obtain antiscreening is selection; all conventions are reported side by side. No gluon is
identified or selected (owner ruling: def:derived-atom step 4 stays open). Exact arithmetic
(sympy); mpmath only for display at the proton pin. Negatives are scope (a).

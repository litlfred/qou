# RESULT — helon twist lattice vs our gl₃ weight map (issue #9096)

- Pre-registration: `PREREG.md` (commit `9ff9770501c`, pushed before the probe existed).
- Probe: `qcd_weight_lattice_map_probe.py`. Output: `qcd_weight_lattice_map.witness.json`.
- **15/15 checks match their pre-registered prediction** (two of them, P3b and P10, were
  predicted to *fail to hold* and do fail to hold).
- Exact sympy over ℚ(√2, √3). No float, `q₀` not used.
- **Source caveat.** CAK (arXiv:2501.03260v1) is **not held in `library/`**. Its data were
  transcribed from the arXiv HTML through a summarising fetch, checked by a second targeted
  fetch. The witness lists every CAK number used. Re-check against the PDF before citing.

## Claim

1. **The CAK twist ↔ weight map is exactly the gl₃ weight map.** Their Eq. (35) matrix `M`
   (det `√3`, column sums `(0, 0, 3)`) sends `(w₁, w₂, Q)` to an integer twist vector `t`.
   Read the other way: `(w₁, w₂) = L·μ` with `μ = t − (T/3)(1,1,1)` the sl₃ part, and
   `Q = T/3` the gl₃ **centre** divided by 3. One fixed linear map serves every state.
   No per-state fix is needed (P1, P2).
2. **Q = T/3 is the corpus normalisation.** It matches CAK §6, and it matches Lambek
   Table 1 as `(aᵢ+a_j+a_k)/3` for all 16 states (P3a). Taken literally, CAK's sentence
   "the three sum up to the electric charge" is false: the e⁻ components sum to −3 and the
   u_r components to +2 (P3b). Lambek's (i,j,k) sets agree with the `M`-image sets flavour by
   flavour (P3c).
3. **The 15 helon charge configurations are the weights of `Λ•ℂ³ ⊕ Λ•(ℂ³)*`**, each with
   multiplicity 1, with centre `±k` on `Λ^k`. So `Q ∈ {0, ±1/3, ±2/3, ±1}` is `±k/3` (P4).
   The first-generation fermions use all 15. CAK prints the pattern `(±0±)` twice and omits
   `(±±0)`. Read as that typo, the count of 15 checks out.
4. **Colour multiplets are consistent.** u and d carry the same sl₃ triplet, ū and d̄ the
   conjugate one, and the leptons are singlets (P5). CAK calls d "3". In ε-coordinates it is
   the antifundamental. That is a naming choice and does not affect consistency.

## Per-state table (from the witness)

| state | t | Q = T/3 | μ (sl₃) | N₃ = t₃ | traceless N₃ = t₁+t₂−2t₃ | D-visible (t₃=0) |
|---|---|---|---|---|---|---|
| ν | (0,0,0) | 0 | 0 | 0 | 0 | yes |
| e⁻ | (−1,−1,−1) | −1 | 0 | −1 | 0 | **no** |
| e⁺ | (1,1,1) | 1 | 0 | 1 | 0 | **no** |
| d (×3) | −ε_c | −1/3 | −ε_c + ⅓ | 0 or −1 | −1, −1, 2 | 2 of 3 |
| d̄ (×3) | +ε_c | 1/3 | ε_c − ⅓ | 0 or 1 | 1, 1, −2 | 2 of 3 |
| u (×3) | (1,1,1) − ε_c | 2/3 | −ε_c + ⅓ | 1 or 0 | −1, −1, 2 | 1 of 3 |
| ū (×3) | ε_c − (1,1,1) | −2/3 | ε_c − ⅓ | −1 or 0 | 1, 1, −2 | 1 of 3 |

## Q and the convention-D U(1) = N₃

- **Q is linear in the gl₃ weight**, as `⟨λ, (1,1,1)⟩/3`. It is also linear in (sl₃ weight,
  raw N₃): `Q = N₃ − μ₃` on every state (P6a). This works only because raw `N₃ = t₃` still
  carries the centre.
- **N₃ is neither electric charge nor hypercharge** (P6b). Its traceless form, the U(1) of
  the D residual, takes different values inside one colour triplet at fixed (Q, Y), and it
  is 0 on both ν and e⁻. It is a colour Cartan component. This independently confirms the
  PR #9059 reading (`qcd_d_residual_symmetry` R2/R4) from the twist-lattice side.
- **The twist lattice is not a strand-module lattice** (P7). On `(ℂ³)^⊗n` every weight is
  non-negative with centre `n`, a constant. Twist vectors have `T ∈ {−3,…,3}` and negative
  entries. So the centre that carries Q is invisible to the Hecke strand module, which is
  consistent with "no braid word carries N₃ charge". Q has to come from the free twist label
  (`strand-twist-datum`), not from the module.
- **D sees no electron** if `t` is read as a colour weight (P8). The `N₃ = 0` sector contains
  ν, two of three d/d̄, one of three u/ū, and neither e⁻ nor e⁺, which have `t₃ = ∓1`.
  Reading-dependent; recorded as a conflict to watch, not as an exclusion.
- **Y is not a function of the twist** (P9). u_L and u_R share `t` but have Y = 1/3 vs 4/3.
  CAK put chirality in the braid. Our `Y_t = 2(Q_twist − I₃)` likewise needs the
  writhe-derived `I₃`. SM Y values are used here for comparison only.

## Conflicts with corpus rulings (reported, not resolved)

| ruling | CAK | conflict |
|---|---|---|
| electron = σ₀σ₁σ₀ ∈ B₃, Hopf closure | e_L = σ₁⁻¹σ₂ T₁₂₃⁻¹, e_R = σ₂σ₁⁻¹ T₁₂₃⁻¹ | **Braid parts differ (P10).** Ours: 2 components, writhe 3. Theirs: 1 component, writhe 0. The corpus assigns the electron no twist, so its charge −1 needs `t = (−1,−1,−1)` added as a free label. |
| up quark = one unknot strand | u = 3-ribbon braid, twists on two ribbons | **One strand cannot be a CAK quark (P11).** `Q = t/3 = 2/3` needs `t = 2`, outside CAK's {−1,0,1}. Its colour weight `2ε_c` lies in `S²ℂ³` (the **6**), not in a triplet. The single-strand d (`t = −1`, a 3̄ weight) is fine. |
| proton = Borromean of three quark strands, colour = position (K0) | p = u_r+u_g+d_b summed over three braids = (1,1,1) | **uud on three strands is not a colour singlet (P12).** Per-strand twists (2,2,−1) give Q = 1 but `μ = (1,1,−2) ≠ 0`. The singlet condition `t₁ = t₂ = t₃` forces all three quark charges to be equal. |

Rows 2 and 3 are the sharp ones. Each is exact for the map named in PREREG: colour = position,
twist = gl₃ weight coordinate, Q = T/3. They say that the corpus's three readings — up quark
as a single strand, colour as position, and charge as twist/3 — **cannot all hold together
with colour-singlet hadrons**. At least one has to give. This is a scope-(a) statement about
that map. It does not rule out other twist-to-colour assignments, for example twists that
live on the colour tube rather than on the strand. The corpus's `Q_twist` note already calls
`T/3` the "colour-tube" quantum.

## Not established

- No CAK datum was read from the PDF. The summary-transcribed Table 2 has a row labelled
  u_L with no twist and ν's vectors. That looks like a source or transcription defect, and
  this probe uses no data from that row.
- No twist value is derived for any corpus word. `strand-twist-datum` keeps `t` as a free
  label, and per the 2026-11-22 ruling ("derive the qᵢ") every Q used here is adopted, not
  derived.
- Post-hoc remark, not evidence: CAK's lepton braid σ₂σ₁⁻¹ has the shape of the photon's
  fourth term σ₀σ₁⁻¹ (index shift). Nothing was computed on it.
- No Lean.

## Verification

`python3 -u qcd_weight_lattice_map_probe.py` → `SUMMARY 15/15`, exit 0.

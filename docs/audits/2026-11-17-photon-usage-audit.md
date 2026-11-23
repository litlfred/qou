# Photon usage audit (2026-11-17)

Owner request, 2026-11-17: *"make a separate definition block so this doesn't keep happening"* and *"do a thorough pass of the paper, the compute etc. to see if there are other incorrect uses of photon"*.

The new block is [`def:photon`](../../folio/quantum-observable-universe/predicted-spectra/photon.md):

$$\gamma(\varphi) = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1 \in H_3(R,q),$$

with three colour weights. The bare photon is $\gamma(0,0,0) = \mathbf{1}$, the empty knot, not the unknot. The definition is taken from the corpus: `prop:gamma-gamma-generates-particles`, `rem:knot-basis-color-content`, `quark-antiquark-production`, `confinement-universality`, the introduction, and the Lean `KnotRegistry.PhotonHeckeElement`. No statement was changed in this PR. Every row marked **conflict** waits on an owner ruling.

## Method

- Grepped `folio/` (`.md`, `.lean`) and `computations/`, `tools/`, `qou-mass/` (`.py`) for `photon` and for `\gamma =`.
- Counts: 129 prose `.md` files, 23 table blocks, 42 `.lean` files and 75 `.py` files mention "photon".
- I read every site that **constructs** or **identifies** the photon as an element or a braid word. Most mentions are physics prose (energy $h\nu$, photon number, $\alpha_{\mathrm{EM}}$ loops), where "photon" means the gauge field and no Hecke element is involved. Those are a different object, not an error, and are not listed.
- This is a grep for spellings, so it cannot rule out a construction written without the word "photon".

## Agrees with `def:photon`

| site | form |
|---|---|
| `predicted-spectra/gamma-gamma-generates-particles` (.md + .lean) | four-term |
| `brings-surface/knot-basis-color-content`, `trivial-knot-photon-interpretation` (+ tables 1-5) | four-term; bare = $\mathbf{1}$ |
| `knots-particles-confinement/quark-antiquark-production(-reduction)`, `confinement-universality` | four-term |
| `introduction/intro-particles-as-knots`, `chapter-overview` | four-term |
| `observations/double-slit-intro`, `quantum-observable-universes/photon-wavefront-example`, `predicted-spectra/meson-formation-chain` | four-term |
| `notation/notation-collisions` §"Photon vs the unknot", `nuclear-interactions/two-photon-pair-production`, registry `principled-gb-nf` row | bare photon = identity |
| Lean `KnotRegistry.PhotonHeckeElement` / `barePhoton`, `Interactions/GammaGammaPairChannels.Photon`, `QuarkState/PhotonPairNormalForm.photon`, `ParticleInteractions/four_term_pair_nucleon` | four-term |
| `mass-theory/transfer-matrix-operator.lean` (`photonElectronCoeffs`: photon = empty knot, $J = 1$) | bare |
| `computations/probes/gamma_gamma_pair_nf_h3_probe.py` | four-term |
| `hecke-operations-table1-data`, `knot-operator-basis-table-table1-data`, `frobenius-gram-matrix-table1-data`, `mass-element-nf`, `operator-selection-lp-proof` | $\gamma$ used as the **name** of the basis vector $\mathbf{1}$ (vacuum channel); consistent with bare = $\mathbf{1}$, but see note N1 |

## Conflicts: the photon is something else

| # | site | what it says | how it differs |
|---|---|---|---|
| C1 | `predicted-spectra/breit-wheeler-pair-production.md` (a `definition`) | $\gamma = \sigma_0$ | bare photon is a single crossing, not $\mathbf{1}$ |
| C2 | `breit-wheeler-pair-production-derivation.md` §"Bare photon pair" | $\gamma\gamma = \sigma_0^2$; colour weights introduced *"to match the $2m_e$ threshold"* | same as C1. It also introduces the colour dressing in order to reproduce a measured number, which §NO FITTING counts as selection against the target |
| C3 | `breit-wheeler-pair-production-derivation.md` §"Colored photon" | treats *"3-term colored photons"* | it is a specialisation $\varphi_{01}=0$; fine if labelled as one, but the block calls it the photon |
| C4 | `breit-wheeler-pair-production.lean` `ColoredPhoton` | one weight: $\gamma_\varphi = \mathbf{1} + \varphi\sigma_0 + \varphi\sigma_1$ | one parameter instead of three, no $\sigma_0\sigma_1$ term; this is the Lean behind the C1 `definition` |
| C5 | `computations/gram-matrix-dual.py` Part C | coloured photon $\mathbf{1} + \varphi\sigma_0 + \varphi\sigma_1$, $\varphi = 0.0487$; bare pair $\sigma_0^2$ | same as C4 and C1; the numeric $\varphi$ is a fitted value |
| C6 | `computations/knot-operator-table.py` "key table" | photon channel $\sigma_0 \cdot T \cdot \sigma_0$ | photon = $\sigma_0$ |
| C7 | `computations/gamma_gamma_pair_production_decomposition.py` | photon $= \sigma_0$, anti-photon $= \sigma_1^{-1}$ | photon = single crossing, and introduces an "anti-photon" the definition does not have |
| C8 | Lean `Mass/GammaGammaWordSelection.lean` (`vertex`), `OneDim/GammaGammaForcesTheLayout.lean` | the γγ vertex $\sigma_i\sigma_{i+1}^{-1}$ = "one photon and one anti-photon", taken from C7 | **this is the $\gamma\gamma$ word grammar of bean `qou-ales`** (letter $V = \sigma_0\sigma_1^{-1}$), and every γγ-selected word, including the nucleon words of `qou-99qc`, is built on it |
| C9 | `computations/breit_wheeler_filtration_chain_probe.py`, `computations/probes/photon_electron/photon_electron_probe.py` | "one photon (a single crossing)" | photon = single crossing |
| C10 | `mass-theory/pieri-photon-shift-proof.md`, `degree-one-braid-trivial-volume.md` | photon = degree-one element $c_0\mathbf{1} + \sum_i \phi_i \sigma_i^{\pm1}$ on $n$ strands | no $\sigma_0\sigma_1$ term, and allows inverse letters; it is an $n$-strand generalisation the definition does not cover |
| C11 | `information-theory/jet-horizon.md`, `knots-particles-confinement/confined-particle-examples.md`, registry $\widehat{\mathbf{1}_{B_4}}$ row | photon = 4-strand identity $\mathbf{1}_{B_4}$ | bare photon agrees, but on 4 strands, where `def:photon` lives in $H_3$ (3 strands) |
| C12 | `nuclear-interactions/two-photon-pair-production.md` | the two-photon state $\gamma\gamma$ is $T_e$ on 2 strands | true only for two bare photons; with colour weights $\gamma\gamma$ spans all of $H_3$ |

## Notes

- **N1 (symbol collision).** In the six-element basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$, the glyph $\gamma$ names the basis vector $\mathbf{1}$, while `def:photon` uses $\gamma$ for the whole four-term element. A coefficient "on $\gamma$" therefore means the coefficient on $\mathbf{1}$. Not wrong, but easy to misread.
- **N2 ($L_\pm$ labelling).** `PhotonPairNormalForm.lean` records that `MarkovTraceOnHecke` labels coordinate 3 as $L_+$ although it is $\sigma_1\sigma_0 = L_-$. Not about the photon itself, but it sits on the same basis.
- **N3 ($L_-$ in the γγ probes).** PR #8104 and the γγ thread's stage 1 took $L_- = \sigma_0^{-1}\sigma_1^{-1}$; `def:photon` and `prop:gamma-gamma-generates-particles` give $L_- = \sigma_1\sigma_0$. Already relayed; stage 1b is re-running (bean `qou-99qc`).

## The decision this raises

C8 is the one with downstream weight. The γγ word grammar ($V = \sigma_i\sigma_{i+1}^{-1}$) was built from C7's reading "photon = a single crossing", which `def:photon` and the notation canon both reject. Whether the grammar should be re-derived from the four-term product $\gamma(\varphi)\gamma(\psi)$ is put to the owner on a decision card; nothing here changes it.

> **Update 2026-11-20 (PR #8583).** By owner ruling — chosen 2026-11-18 (bean `qou-99qc`, entry "OWNER WORKING ASSUMPTION: photon last term σ₀σ₁⁻¹ (switched)"), confirmed as a decision 2026-11-20 — `def:photon` is $\gamma(\varphi) = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1^{-1}$. The γγ grammar letter $V = \sigma_0\sigma_1^{-1}$ of C8 is therefore now **exactly the photon's last term**: the conflict between C8 and `def:photon` is resolved on the $\sigma_0\sigma_1^{-1}$ side. What C8 still records is the separate point that the grammar's justification ("one photon and one anti-photon" = two single crossings, C7) reads "photon" as a single crossing; that reading is still rejected by `def:photon`, and the grammar is now tied to the photon through its vertex term rather than through C7. The Borromean braid is $V^3 = \gamma(0,0,qh)\,\gamma(0,0,-q^{-1}h)$ (`QOU.Mass.BorromeanPhotonFactorisation.borromean_eq_photon_product`).

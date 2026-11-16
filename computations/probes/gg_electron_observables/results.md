# Results: invariants of the γγ electron candidates V⁰, V³, V⁶

Pre-registration: `preregistration.md`, commit 43188f82802, pushed before the probe was written.
Producer `gg_electron_observables_probe.py`, witness `gg-electron-observables.witness.json`, 5/5 checks.
V = σ₀σ₁⁻¹; mpmath 40 dps, convention D, proton pin; SnapPy 3.x for link type, volume and chirality.

| observable | V⁰ | V³ | V⁶ | separates |
|---|---|---|---|---|
| O1 components | 3 | 3 | 3 | no |
| O1 pairwise linking | 0 | 0 | 0 | no |
| O1 link type (SnapPy identify) | 3-component unlink | Borromean rings (6³₂, L6a4) | L12a1882 | **yes, all three** |
| O3 amphichiral | yes | yes | yes | no |
| O4 hyperbolic volume | 0 (not hyperbolic) | 7.32772475341775212043682811946 | 21.6315986791926589697402486963 | **yes, all three** |
| O5 min level character, levels 1–3 | 1 | 0.99440172663906920 | 0.98692577002215985 | **yes** (all pass) |
| O6 ρ₍₂,₁₎ eigenvalues | 1, 1 | e^{±iφ}, φ = 3θ − 2π = 0.07627 rad | e^{±2iφ} | **yes** |
| O7 equals the nucleon word | no | yes, if nucleon = V³ | yes, if nucleon = V⁶ | — |

## Structure behind O5/O6 (exact)

On the two-dimensional block (2,1), V has determinant 1 and trace −1 − h², h = q − q⁻¹ (checked to 1e-35). So V acts as a rotation e^{±iθ} with 2cos θ = −1 − h². At q = 1, θ = 2π/3 and V³ is the identity on every block: V³ is a pure braid. At q₀ the rotation overshoots, so V³ is a rotation by 3θ − 2π, and V⁶ by twice that. χ₍₂,₁₎(V^k) = 2cos kθ to 1e-30. Every candidate is a small rotation off the identity, and the size of the rotation (0, one step, two steps) is what the level characters see.

## What this does and does not settle

- **Separated:** link type, volume, the level-character profile and the (2,1) rotation all distinguish the three candidates.
- **Not separated:** components, linking numbers, chirality. **None of the three is chiral**, so none of them can carry handedness on its own. A chiral electron needs a letter outside the γγ vertex V, such as the photon twist L± = σ₀σ₁ (writhe +2) raised by the weak-vertex thread (bean qou-99qc).
- V⁰ means the electron carries no crossings at all; its closure is the unlink.
- V³ makes electron and nucleon the same word when the nucleon is V³.
- No observable here picks a candidate. Volume and every other number are not compared with any measured electron quantity. The choice is the owner's.

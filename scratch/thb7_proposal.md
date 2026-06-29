# Proposal: Resolution of Lever 3 (universal-ρ normalisation)

## Status and Investigation
The investigation of bean `thb7` (Lever 3: universal-ρ normalisation on the atomic q-Reeb object) reveals that while the relative binding ratio is derived, the absolute scale `ρ` remains gated. 

1. **Success of the ρ-free Ratio**: As established in `binding_reeb_ratio_rho_free.py`, the A=3 mirror binding ratio `B(³H)/B(³He) = S(³H)/S(³He)` cancels the normalisation `ρ`. This produces a genuine, no-fit prediction that matches the AME ratio to **+1.7%**.
2. **The Absolute Scale is Gated**: The absolute scale `ρ ≈ 18.5 MeV/rad` is currently a CAL-4-gated fit (`ρ_need = B_AME/S`).
3. **Numerology Constraints**: Deriving a per-λ `ρ_λ` from a single total binding target is exactly the underdetermined Δ_λ gate (where six ansätze have already failed). A numerical scan to force `ρ = f(substrate)` is explicitly classified as numerology in the corpus and is thus forbidden.
4. **Channel Separation and Asymmetry**: The probe `charge_slambda_reeb_phase_crack.py` showed that the atomic q-Reeb phase captures the Coulomb split to 1.7% at the ratio level, entirely in the bar-odd (sinh) channel. The spurious 5.9% cosh mirror-asymmetry was diagnosed as an artifact of incomplete sinh-removal in the braid-word construction (inter-nucleon only, missing the intra-nucleon bar-odd term).

## Required Author Assistance
A mathematical derivation of the absolute scale `ρ` cannot be implemented without risking numerology. To properly close Lever 3 and derive `ρ` structurally, we need author input on the following:

1. **Structural Anchor for ρ**: Can `ρ` be anchored structurally to an extensive bulk term (like the `2·m_e·8G` shell residue) combined with a fibre q-Askey per-λ kernel, as suggested in recent A-scaling diagnostics, rather than remaining an empirical CAL-4 parameter?
2. **Charge-Symmetry Breaking**: How should we handle the genuine charge-symmetry breaking physics (the sub-2% residual)? Should this remain a known limitation of the current q-Reeb model, or is there a planned extension to the braid-word construction to fully resolve the intra-nucleon vs inter-nucleon bar-odd terms?

Until the structural anchor for the absolute scale is mathematically defined, `ρ` must remain a gated CAL-4 parameter. Please advise on the preferred theoretical direction to replace the fitted `ρ` with a derived substrate volume or energy scale.

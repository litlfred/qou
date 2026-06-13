# GAP-A-4: Operator-Valued Generation Branching for the Muon Mass

**Date:** 2026-06-13
**Branch:** `claude/gap-a4-muon-operator-branching`
**Status:** Scoping document

## 1. The 210 ppb Substrate Floor
The bare-categorical formulation of the muon mass is:
$$ m_\mu = m_e \cdot \frac{\mathrm{Vol}(4_1)}{\hbar_q^2} $$
As confirmed by the 2026-06-13 probe, evaluated at the proton-anchor $q_0 \approx 1.109978$, this yields a prediction gap of **210 ppb** relative to CODATA. This gap is mathematically identical to the mechanical propagation of the proton-anchor shift ($\Delta q_0 = -11.53$ ppb $\times$ lever $-18.185$). 
Because fitting a scalar correction to absorb this tension violates the three-calibration discipline, the only structurally legitimate path to resolving it is to upgrade the generation tower from a scalar sequence to an **operator-valued branching tower** over Bring's surface (GAP-A-4).

## 2. Operator-Valued Branching: The $H_5(q)$ Framework
In the geometric model, the lepton generations are indexed by the vertical degree $\ell$ of the harmonic forms over the Bring's surface (which has $A_5 \cong I$ icosahedral symmetry). The framework identifies the electron as $\ell=1$ and the muon as $\ell=2$.
Under the icosahedral branching $SO(3) \downarrow I$:
- **Electron ($\ell=1$)**: Decomposes to $T_1$ (dimension 3).
- **Muon ($\ell=2$)**: Decomposes to $H$ (dimension 5).

The Bring's surface action lifts to the Hecke algebra $H_5(q)$ on 5 strands. The classical symmetric group $S_5$ has irreducible representations whose dimensions restrict to $A_5$ as follows:
- The dimension-6 irrep of $S_5$, partition **$\lambda = (3,1,1)$**, restricts to $A_5$ as $T_1 \oplus T_2$ (dimensions $3 \oplus 3$). The electron ($\ell=1$) channel $T_1$ lives exactly within this block.
- The dimension-5 irreps of $S_5$, partitions **$\lambda = (3,2)$** and **$\lambda = (2,2,1)$**, restrict directly to the icosahedral irrep $H$ (dimension 5). The muon ($\ell=2$) channel $H$ lives exactly within these blocks.

## 3. The GAP-A-4 Structural Hypothesis
The current $m_\mu$ evaluation treats the mass mapping as a purely geometric scalar $Vol(4_1) / \hbar_q^2$. The **GAP-A-4 hypothesis** posits that the mass evaluation is a trace over the 5-strand fiber space, weighted by the Wedderburn projector $E_\lambda$ corresponding to the lepton's generation degree:
- For the electron: the mass evaluation factors through the projector $E_{(3,1,1)}$.
- For the muon: the mass evaluation factors through the projector $E_{(3,2)}$ (or $E_{(2,2,1)}$).

This implies the true mass formula contains a Wedderburn-trace correction:
$$ m_\mu = m_e \cdot \frac{\mathrm{Vol}(4_1)}{\hbar_q^2} \cdot \mathcal{F}(E_{(3,2)}, q_0) $$
where $\mathcal{F}$ is a relative categorical modifier (e.g., a normalized quantum-dimension ratio or character shift) derived from the $H_5(q_0)$ projectors that bridges the 210 ppb gap without violating the rigid parameter-free substrate.

## 4. Next Steps & Proof Obligations
1. **Compute Wedderburn Action**: Evaluate the exact action of the generation selection projectors $E_{(3,2)}$ and $E_{(3,1,1)}$ on the local knot module.
2. **Derive the Functor (`conj:s5-so3-fiber-action`)**: The 5-strand $H_5(q)$ fiber must be mapped to the 3-strand $H_3(q)$ trace (where the mass scale originates). This is the exact missing cross-algebra functor identified in the 2026-06-01 audit.
3. **Analytic Closure**: Prove that the shift induced by $E_{(3,2)}$ precisely cancels the 210 ppb anchor-shift tension at the fundamental level.

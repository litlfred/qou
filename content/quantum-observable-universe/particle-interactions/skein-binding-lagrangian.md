**Definition.**
*Let $L = Z\mathfrak{p} \oplus N\mathfrak{n}$ be a multi-nucleon Hopf link with $Z$ protons, $N$ neutrons, and $A = Z + N$. The **Skein binding Lagrangian** is the categorical action $\mathfrak{S}_q$ evaluated on $L$:*
$$
  \mathcal{L}_{\mathrm{bind}}[L]
  = 
  \mathcal{L}_{\mathrm{vol}}
  - \mathcal{L}_{\mathrm{surf}}
  - \mathcal{L}_{\mathrm{Coul}}
  - \mathcal{L}_{\mathrm{Pauli}}
  + \mathcal{L}_{\mathrm{pair}}.
$$
*Each term arises from the Skein polynomial structure of $L$:*

1. ***Volume binding.** Each nearest-neighbour nucleon--nucleon Hopf junction contributes a binding energy proportional to the average Skein weight. There are roughly $A$ such junctions, yielding*
   $$
     \mathcal{L}_{\mathrm{vol}}
     =  \frac{q + q^{-1}}{2} \cdot \lambda_V \cdot A
   $$
   *where $\lambda_V$ is the per-junction energy scale.*

2. ***Surface correction.** Nucleons on the boundary of the link have fewer Hopf junctions. The boundary count scales as $A^{2/3}$:*
   $$
     \mathcal{L}_{\mathrm{surf}}
     =  \frac{q + q^{-1}}{2} \cdot \lambda_S \cdot A^{2/3}.
   $$

3. ***Coulomb repulsion.** Each proton--proton Hopf crossing takes the positive-crossing coefficient $q$ instead of the baseline $(q + q^{-1})/2$, producing a repulsive excess $\delta = \tfrac{1}{2}(q - q^{-1})$ per pair. The $\binom{p}{2}$ pairs are distributed over a link of radius $A^{1/3}$:*
   $$
     \mathcal{L}_{\mathrm{Coul}}
     =  (q - q^{-1}) \cdot \lambda_C
     \cdot \frac{p(p-1)}{A^{1/3}}.
   $$

4. ***Pauli asymmetry.** The hadron definition uses the antisymmetric product $\mathrm{Sym}^n(-)$ for fermionic constituents. When $N \neq Z$, the species asymmetry costs energy from the exclusion constraint:*
   $$
     \mathcal{L}_{\mathrm{Pauli}}
     =  \lambda_A \cdot \frac{(N - Z)^2}{4A}.
   $$

5. ***Pairing.** Two identical nucleons can form a closed Hopf loop, contributing a pairing energy $\pm \lambda_P / A^{1/2}$ (positive for even--even, negative for odd--odd).*

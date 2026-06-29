**Definition.**
*Let $L = Z\mathfrak{p} \oplus N\mathfrak{n}$ be a multi-nucleon Hopf
link with $Z$ protons and $N$ neutrons, $A = Z + N$. The **Skein binding
Lagrangian** is the categorical action $\mathfrak{S}_q$
([canonical action](#prop:qou-canonical-action)) evaluated on $L$,*

$$
  \mathcal{L}_{\mathrm{bind}}[L]
  = 
  \mathcal{L}_{\mathrm{vol}}
  - \mathcal{L}_{\mathrm{surf}}
  - \mathcal{L}_{\mathrm{Coul}}
  - \mathcal{L}_{\mathrm{Pauli}}
  + \mathcal{L}_{\mathrm{pair}},
$$

*with each term arising from the Skein polynomial structure of $L$:*

1. **Volume binding** (strong force baseline).  Each nearest-neighbour
   nucleon--nucleon Hopf junction contributes a binding energy
   proportional to the average Skein weight.  There are
   $\sim A$ such junctions (nearest-neighbour count in the link),
   giving

   $$
     \mathcal{L}_{\mathrm{vol}}
     =  \frac{q + q^{-1}}{2} \cdot \lambda_V \cdot A
   $$

   where $\lambda_V$ is the per-junction energy scale.

2. **Surface correction**.  Nucleons on the boundary of the link
   have fewer Hopf junctions (lower linking number).  The boundary
   count scales as $A^{2/3}$:

   $$
     \mathcal{L}_{\mathrm{surf}}
     =  \frac{q + q^{-1}}{2} \cdot \lambda_S \cdot A^{2/3}.
   $$

3. **Coulomb repulsion** (crossing asymmetry on $\mathfrak{p}$--$\mathfrak{p}$
   pairs).  Each proton--proton Hopf crossing picks up the
   positive-crossing coefficient $q$ instead of the baseline
   $(q + q^{-1})/2$, producing a repulsive excess
   $\delta = \tfrac{1}{2}(q - q^{-1})$ per crossing pair.
   The $\binom{p}{2}$ pairs are distributed over a link of radius
   $\sim A^{1/3}$:

   $$
     \mathcal{L}_{\mathrm{Coul}}
     =  (q - q^{-1}) \cdot \lambda_C
     \cdot \frac{p(p-1)}{A^{1/3}}.
   $$

4. **Pauli asymmetry** (antisymmetric product cost).  The hadron
   definition ([hadron](#def:hadron)) uses the antisymmetric
   product $\mathrm{Sym}^n(-)$ for fermionic constituents.  When
   $n \neq p$, the asymmetry between the two nucleon species costs
   energy from the exclusion constraint:

   $$
     \mathcal{L}_{\mathrm{Pauli}}
     =  \lambda_A \cdot \frac{(n - p)^2}{4A}.
   $$

5. **Pairing** (Cooper-like Hopf loops).  Two identical nucleons
   can form a closed Hopf loop, contributing a pairing energy
   $\pm \lambda_P / A^{1/2}$ (positive for even--even, negative for
   odd--odd).

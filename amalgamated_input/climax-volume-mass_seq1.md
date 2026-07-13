<!-- FILE_START: crossing-energy-intro.md -->
The previous section converted the $R$-matrix into a global energy for a closed strand. We now localise that energy at the points where strands cross. Each crossing carries a sign and a weight. The Hecke relation dictates these weights; we do not choose them by hand. Consequently, the per-crossing decomposition splits into a strong baseline and an electromagnetic correction.

We open with Definition: Crossing energy of a knot composite. This assigns the weights $(q, -q^{-1})$ to positive and negative crossings, tracing them back to the eigenvalues of the Hecke generator $T = P \circ R$. Example: Crossing energy and binding in the trefoil carries the definition through a familiar case. Remark: Categorical coordinate of the commutative limit records how $i = \sqrt{\lambda_-}$ provides the natural complex structure on the antisymmetric eigenspace. 

The structural pivot is Definition: Coulomb charge of a knot composite. This extracts the antisymmetric half $Q(\mathfrak{H}) = \tfrac{1}{2}(n_+ - n_-)$ of the crossing count and yields the decomposition $\mathfrak{E}_{\mathrm{cross}} = \text{strong baseline} + Q \cdot (q - q^{-1})$. Proposition: Crossing asymmetry and per-crossing Coulomb correction and Proposition: Skein relation $L_+ - L_- = (q - q^{-1})\,L_0$ is bar-antisymmetric close the loop. They show that the asymmetric piece transforms correctly under the bar involution $q \mapsto q^{-1}$. 

The next section, **Lagrange Resolvents and $q$-Deformed Kinematics**, uses the Coulomb-charge decomposition as the starting point for the discrete Fourier transform on the cyclic subgroup $C_5$, reading off the kinematic observables from the result.
<!-- FILE_END: crossing-energy-intro.md -->

<!-- FILE_START: crossing-energy.md -->
Let $\mathfrak{H} = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ be a composite of knots linked by $\mathcal{L}$, with braid word $\beta \in B_n$ representing the linking. We define the **crossing energy** of $\mathfrak{H}$ as:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \sum_{\text{crossings in } \beta}
  \begin{cases}
    q   & \text{positive crossing } (L_+), \\
    -q^{-1} & \text{negative crossing } (L_-),
  \end{cases}
$$

where $q$ is the substrate parameter ([substrate parameter](#def:substrate-parameter)). The sign convention follows the Skein relation:

$$
  q  L_+ -  q^{-1} L_-
  =  (q^{1/2} - q^{-1/2}) L_0.
$$

The crossing energy measures the net Skein weight of the composite. A positive $\mathfrak{E}_{\mathrm{cross}}$ indicates that repulsion dominates; a negative value indicates that binding dominates.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs—real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The generic categorical/$q$-deformation identities it relies upon remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: crossing-energy.md -->

<!-- FILE_START: crossing-energy-categorical-origin.md -->
**Remark (crossing weights are Hecke eigenvalues, not postulates).**

The per-crossing weights $(q, -q^{-1})$ of the [crossing energy](#def:crossing-energy) are not an energetic penalty laid on top of a topological framework. They are the **two eigenvalues of the Hecke generator** $T = P \circ R \colon V \otimes V \to V \otimes V$ acting on the symmetric/antisymmetric decomposition. The rigid monoidal structure forces them:

1. *Rigidity fixes the $R$-matrix determinant.* Dualisability of $V$ and the categorical volume constraint ([volume constraint](#def:quantum-observable-universe)) require the braiding $R = c_{V,V}$ to satisfy $\det(R|_{V \otimes V}) = 1$, with eigenvalues $(q, q^{-1})$ on $S^{2} V \oplus \Lambda^{2} V$.
2. *The Hecke generator carries the transposition sign.* The Hecke generator is $T = P \circ R$, where $P$ is the swap. Since $P|_{\Lambda^{2} V} = -\mathrm{id}$, composition flips the sign on the antisymmetric summand. This gives $T$-eigenvalues $(q, -q^{-1})$ with $\det(T) = -1$, which matches the Hecke minimal polynomial $(T - q)(T + q^{-1}) = 0$ ([eigenvalue extraction](#prop:braiding-eigenvalue-extraction)).
3. *Crossing weights are eigenvalues, not postulates.* Assigning a positive crossing $L_{+}$ the weight $q$ and a negative crossing $L_{-}$ the weight $-q^{-1}$ represents precisely the action of $T$ on a symmetric-channel input and $T^{-1}$ on an antisymmetric-channel input. The sum $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})$ is therefore a trace of $T^{\pm 1}$-eigenvalues along the braid. The categorical structure dictates this assignment.
4. *Gröbner--Shirshov resolution.* When we reduce $\mathfrak{H}$ to Gröbner--Shirshov normal form ([nuclear normal form](#prop:nuclear-groebner-reduction)), each crossing contributes its $T$-eigenvalue exactly once. The net $\mathfrak{E}_{\mathrm{cross}}$ is the resulting Laurent polynomial in $q$, read off the normal form. Removing any of these weights would violate duality and break the Hecke relation.

We compute this quantity entirely from the $R$-matrix braiding ([R-matrix](#rem:r-matrix-braiding)) of $\mathcal{U}_q(\mathfrak{su}(2))$ acting on the tensor product of constituent representations.
<!-- FILE_END: crossing-energy-categorical-origin.md -->

<!-- FILE_START: crossing-energy-trefoil.md -->
We evaluate the crossing energy ([crossing energy](#def:crossing-energy)) for the trefoil knot and then detail how binding arises in hadrons.

**Single crossing energy.**
Each crossing in a knot diagram carries Skein weight $q$ (positive crossing) or $-q^{-1}$ (negative crossing). For a positive crossing, the energy contribution is

$$
  \mathfrak{E}_{\mathrm{cross}}^{(+)} = q,
  \qquad
  \mathfrak{E}_{\mathrm{cross}}^{(-)} = -q^{-1}.
$$

The net energy of a single positive crossing minus a single negative crossing is $q - q^{-1}$. This coefficient appears in the Skein relation $T - T^{-1} = q - q^{-1}$.

**Trefoil: three positive crossings.**
The standard diagram of the trefoil $\tau(2,3)$ has three positive crossings. Its total crossing energy is

$$
  \mathfrak{E}_{\mathrm{cross}}(\tau(2,3))
  =  3q.
$$

At the substrate parameter $q \approx 1.110$:

$$
  \mathfrak{E}_{\mathrm{cross}}(\tau(2,3))
   \approx  3 \times 1.110
  =  3.330.
$$

This is positive. The trefoil is a single knot, not a composite, so there is no linking to provide negative binding energy.

**Binding in composites.**
A hadron $\mathfrak{H} = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ is a composite. Its linking $\mathcal{L}$ introduces additional crossings between constituent knots. Mutual crossings between distinct components can contribute *negative* energy (via negative crossings in the linking braid word). The total crossing energy of a composite is

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \underbrace{\sum_{i} \mathfrak{E}_{\mathrm{cross}}(K_i)}_{\text{self-crossings (positive)}}
  + 
  \underbrace{\mathfrak{E}_{\mathrm{cross}}(\mathcal{L})}_{\text{mutual crossings (can be negative)}}.
$$

The composite is *bound* when the total is negative: $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) < 0$. The mutual linking energy overcomes the individual knot crossing costs. The composite is energetically favorable relative to the separated constituents.

**Proton binding.**
The proton ([proton as Borromean hadron](#ex:hadron-proton)) consists of three quarks linked in a Borromean configuration. The Borromean linking contributes enough negative mutual crossing energy to make $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p}) < 0$. This explains why the proton is a stable bound state: disassembling it into free quarks demands adding energy equal to $|\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p})|$.
<!-- FILE_END: crossing-energy-trefoil.md -->

<!-- FILE_START: commutative-crossing-energy.md -->
**Remark (categorical coordinate of the commutative limit).**
The Hecke generator $\sigma = P \circ R$ on $V \otimes V$ has eigenvalues $(\lambda_+, \lambda_-) = (q, -q^{-1})$ on the symmetric/antisymmetric decomposition $S^2 V \oplus \Lambda^2 V$ ([def:crossing-energy](#def:crossing-energy)). At $q = 1$ ([def:commutative-qou](#def:commutative-qou)), the eigenvalues collapse to $(+1, -1) = \mathbb{Z}_2$, and the per-crossing weight $q - q^{-1}$ vanishes identically. We recover the categorical structure of the commutative limit by extracting the *square root* of the antisymmetric eigenvalue $\lambda_- = -1$:

$$
  i  =  \sqrt{\lambda_-}, \qquad i^2 + 1  =  0  \;\text{in}\; R[i].
$$

The categorical structure forces the ring extension $R[i]$ (the universal $R$-algebra containing an element $i$ with $i^2 = -1$). The element $i$ is the **categorical coordinate of $\mathbb{P}(V)$ in the commutative limit**, mirroring the role of $q$ in the non-commutative theory. The construction is intrinsic to $R$; we assume no real or complex numbers. When $R$ already contains a square root of $-1$ (e.g. the archimedean realisation where $R = \mathbb{C}$, see [archimedean realisations](#rem:archimedean-realisations)), $i \in R$ is canonical. When $R$ does not (e.g. $R = \mathbb{Z}[q, q^{-1}]$ at $q = 1$), $R[i]$ is the minimal extension realising $\lambda_-$ as a categorical square.

**Categorical-coordinate dictionary.**

See [Table 1](#tbl:commutative-crossing-energy-table1-data).

**Deformation hierarchy.** The discrete Weyl group $\mathbb{Z}_2$ embeds into the continuous maximal torus, which itself is the $q = 1$ fibre of the quantum torus:

$$
  \mathbb{Z}_2  \;\hookrightarrow\;  \mathrm{U}(1)  \;\hookrightarrow\;
   \mathrm{U}_q(1).
$$

Each inclusion identifies a different categorical coordinate on $\mathrm{End}(\mathbf{1})$. The value $-1$ generates $\mathbb{Z}_2$; $i$ generates $\mathrm{U}(1)$ at the quarter-turn $\varTheta = \pi/2$; and $q$ generates $\mathrm{U}_q(1)$ off-locus. The standard non-commutative deformation $\mathrm{SU}(2) \rightsquigarrow \mathrm{SU}_q(2)$ acts on the second inclusion. The commutative-limit *enlargement* $\mathbb{Z}_2 \hookrightarrow \mathrm{U}(1)$ acts on the first. These are the two mechanisms to escape the $q = 1$ degeneracy of $q - q^{-1}$.

**Three categorical readings of $i$ on $\mathbb{P}(V)$.**

1. *Algebraic.* $i = \sqrt{\lambda_-} \in \mathrm{End}_{R[i]}(\mathbf{1})$ is the categorical square root of the antisymmetric braiding eigenvalue. This single datum appears in three faces: Wick rotation, CR complex structure, and arrow of time. All reduce to the binary choice of braiding orientation $c_{V,V}$ vs $c_{V,V}^{-1}$ ([rem:i-as-braiding-orientation](#rem:i-as-braiding-orientation)).
2. *Geometric.* $J = i \cdot \mathrm{id}_V \in \mathrm{End}_{R[i]}(V)$ is an endomorphism with $J^2 = -\mathrm{id}_V$, descending to a complex structure on $\mathbb{P}(V) = \mathrm{Proj}(\mathrm{Sym}\, V^\vee)$ over $R[i]$. In the archimedean realisation, this recovers the standard complex structure on the exceptional divisor $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$ ([def:exceptional-divisor](#def:exceptional-divisor)).
3. *Equivariant.* The maximal torus $\mathrm{U}(1) \subset \mathrm{SU}(2)$ acts on $\mathbb{P}(V)$ with $i$ as the quarter-turn generator. The orbit space is $[0, \pi]$ with phase fibre $\varphi \in S^1$ over the interior ([prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction)).

The three readings coincide because each computes the same categorical datum: a square root of $\lambda_-$ in $\mathrm{End}_{R[i]}(V)$.

**Affine-chart origin.** Both $q$ and $i$ originate from the chart-transition data of $\mathbb{P}(V)$ ([rem:affine-chart-origin-of-i-and-q](#rem:affine-chart-origin-of-i-and-q)). The parameter $q$ constitutes the chart-transition coefficient $z\,w = q^{-1}$ on the quantum projective line $\mathbb{P}_q(V)$. The element $i$ is the square root of the chart-swap involution $\iota: z \mapsto z^{-1}$ that the transition collapses to at $q = 1$. Formally, the **categorical-coordinate ring** is the universal $R$-algebra extension $R[i, q^{\pm 1}] = R[q, q^{-1}][i]/(i^2 + 1)$ ([prop:categorical-coordinate-ring](#prop:categorical-coordinate-ring)) in which $q$ is invertible and the involution-eigenvalue $-1$ possesses a square root. The chart-transition automorphism group factors as $\langle q \rangle \rtimes \langle \iota \rangle$ over this ring.

**Half-twist and ribbon structures.** The ribbon element $v = q^{1/2}$ is *not* required for the categorical-coordinate construction. It appears only when $\mathbf{C}$ carries an additional ribbon twist $\varTheta_V = q^{1/2}\,\mathrm{id}_V$ for framed-link invariants or Reshetikhin--Turaev TQFT ([rem:sqrt-q-ribbon-structure](#rem:sqrt-q-ribbon-structure)). We extract the square root of $\lambda_-$ within $R[i]$, not from any ribbon datum. It remains independent of the eigenvalue-labelling convention $q := \lambda_+$ ([rem:braiding-unit-circle-convention](#rem:braiding-unit-circle-convention)).

**Crossing energy in the commutative limit.** Setting $q = e^{i\varTheta}$ on the unit circle of $\mathrm{End}(\mathbf{1})$ gives

$$
  q - q^{-1}  =  2i \sin\varTheta,
$$

with $\varTheta \in [0, \pi]$ tracking the orbit-space interval of [prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction). The endpoints $\varTheta = 0, \pi$ define the polar fixed points (zero weight). The interior constitutes the free $S^1$-fibre. The point $\varTheta = \pi/2$ (where $q = i$) marks the location of maximum weight $|2i \sin(\pi/2)| = 2$. The Hecke energy $q - q^{-1}$ of the non-commutative theory operates as the algebraic deformation of this commutative-limit form.
<!-- FILE_END: commutative-crossing-energy.md -->

<!-- FILE_START: branch-phase-mass-tower-witness.md -->
**Remark (branch-phase localisation and the mass-tower falsifiability witness).**

**Branch-phase localisation on $\mathcal{X}_5$.** The five finite branch points $\zeta_5^k$ of the hyperelliptic quintic ([def:hyperelliptic-quintic](#def:hyperelliptic-quintic)) lie on the unit circle. They pick out five preferred phase values $\varphi_k = 2\pi k/5$ on the $\mathrm{U}(1)$ tube ([rem:u1-phase-tube](#rem:u1-phase-tube)). At these phases, the commutative crossing weight ([crossing energy](#def:crossing-energy)) takes only two distinct magnitudes:

$$
  2\lvert\sin(2\pi/5)\rvert  \approx 1.902,
  \qquad
  2\lvert\sin(4\pi/5)\rvert  \approx 1.176.
$$

The golden-ratio identity $\sin(2\pi/5)/\sin(4\pi/5) = \varphi$ relates them, where $\varphi = (1+\sqrt{5})/2$.

**Falsifiability witness.** The computation `isospin-mass-tower-collapse` evaluates the multi-brane mass $\mathfrak{m}_{\mathrm{cat}} = \lvert\mathrm{tr}_M(\beta)\rvert + \sum_n \hbar_q^{2n} \mathrm{tower}^{(n)}$ against AME binding for the three lightest non-trivial nuclei. The derived/observed ratio overshoots by a factor of $3$ to $4$, indicating a missing scalar prefactor. After isospin (Coulomb) correction, the two distinct strong-force ratios match the two branch-phase magnitudes:

See [Table 2](#tbl:commutative-crossing-energy-table2-data).

Removing the $\approx 0.76\;\mathrm{MeV}$ Coulomb energy of ${}^3\mathrm{He}$ collapses the two $A = 3$ ratios to $3.4767$. This matches tritium ($3.4764$) to $0.014\%$, consistent with the isospin symmetry of strong-force binding (Wigner-energy convention, \cite{satula1997}).

**Caveat (updated).** We have now categorically derived the structural form of the per-nucleon scaling between $A = 2$ and $A = 3$. The **Path A pipeline** (commits `f9f25b5f`, `23e447dc`, [`per_irrep_pole_atom.py`](../../../computations/per_irrep_pole_atom.py)) verifies $\mathrm{ord}_{u=0}(\mathrm{tr}_M(\beta)) = 18Z + 21N + 1$ via symbolic Hoefsmit pole-order analysis for the proton ($Z=1, N=0$) and deuteron ($Z=N=1$). Predictions match experimental atomic masses to $\leq 0.30\%$ across $Z = 1 \dots 20$ using the single-generator $\rho_K$ formula. The probe witness [`rho-k-pair-gen-v2-wedderburn.witness.json`](../../../computations/_deprecated/rho-k-pair-gen-v2-wedderburn.witness.json) is now deprecated. We tested and **rejected** the Wedderburn pair-generator extension (it worsens the fit to $\sim 4.7\%$ MAE). The Hecke structure at $q = 1$ forces the categorical-coordinate identification $i = \sqrt{\lambda_-}$; it does not rely on this numerical confirmation.
<!-- FILE_END: branch-phase-mass-tower-witness.md -->

<!-- FILE_START: categorical-coordinate-ring-dedup.md -->
**Remark ($R[i, q^{\pm 1}]$ as the ambient deformation ring).**

**Downstream applications of $R[i, q^{\pm 1}]$.** Recognizing the categorical-coordinate ring as the ambient deformation ring ([prop:categorical-coordinate-ring](#prop:categorical-coordinate-ring)) deduplicates four ad-hoc complexification patterns:

1. *This block.* The substitution $q = e^{i\varTheta}$ used in the [commutative-limit remark](#rem:commutative-crossing-energy) is not an external complexification. The element $e^{i\varTheta} = \cos\varTheta + i\sin\varTheta$ is a unit *in* $R[i]$ via the Euler identity. We compute $q - q^{-1} = 2i\sin\varTheta$ entirely inside $R[i, q^{\pm 1}]$ without enlarging the categorical ground ring.
2. *Witness computations.* We justify the complex arithmetic in `isospin-mass-tower-collapse` and the broader mass-tower pipeline categorically as a single specialisation $R[i, q^{\pm 1}] \to \mathbb{C}$ via $q \mapsto q_0$. We apply the universal property of the categorical-coordinate ring once, rather than complexifying ad hoc per script.
3. *Wick-rotation and complex-substrate remarks.* The blocks [rem:laplace-fourier-wick-rotation](#rem:laplace-fourier-wick-rotation) and [rem:complex-substrate-interpretation](#rem:complex-substrate-interpretation) previously complexified in isolation (introducing $i$ for the half-plane swap, the CR structure, and the substrate value). Both invocations of $i$ are realisations of the single categorical coordinate of [prop:categorical-coordinate-ring](#prop:categorical-coordinate-ring), under the $\mathrm{Gal}(R[i]/R) = \mathbb{Z}_2$ orientation choice of [rem:i-as-braiding-orientation](#rem:i-as-braiding-orientation).
4. *Curves over the substrate.* We normally introduce the hyperelliptic quintic $\mathcal{X}_5: y^2 = x^5 - 1$ ([def:hyperelliptic-quintic](#def:hyperelliptic-quintic)) and the Descartes elliptic curve $\mathcal{E}_q$ ([prop:descartes-elliptic-curve](#prop:descartes-elliptic-curve)) "over $\mathbb{C}$" with $\zeta_5 = e^{2\pi i/5}$ as a complex root of unity. In the categorical-coordinate framework, these curves live over $R[i, q^{\pm 1}]$ at $q = q_0$. The fifth roots of unity $\zeta_5^k$ are the five geometric points of $\mathrm{Spec}(R[i, q^{\pm 1}])$ where the chart-transition coefficient hits $\zeta_5^k$. This recovers the branch-phase localisation of [rem:u1-phase-tube](#rem:u1-phase-tube).

In each case, the simplification supplies *categorical justification*. It does not alter the algorithmic computations and proofs. Their ambient ring simply becomes a single named object.
<!-- FILE_END: categorical-coordinate-ring-dedup.md -->

<!-- FILE_START: coulomb-charge.md -->
Let $\mathfrak{H}$ be a knot composite with braid word $\beta$. Let $n_+(\beta)$ and $n_-(\beta)$ denote the number of positive and negative crossings in $\beta$. We define the **Coulomb charge** of $\mathfrak{H}$ as:

$$
  Q(\mathfrak{H}) =  \tfrac{1}{2}\bigl(n_+(\beta) - n_-(\beta)\bigr).
$$

The crossing energy ([crossing energy](#def:crossing-energy)) decomposes into two terms:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \underbrace{\tfrac{1}{2}(n_+ + n_-)(q + q^{-1})}_{\text{baseline (strong)}}
  + 
  \underbrace{Q(\mathfrak{H}) \cdot (q - q^{-1})}_{\text{Coulomb correction}}.
$$

The first term is symmetric under $q \leftrightarrow q^{-1}$ and represents the strong binding. The second term is antisymmetric and vanishes at $q = 1$. The Coulomb charge $Q(\mathfrak{H})$ governs the magnitude and sign of the electromagnetic correction:

- $Q(\mathfrak{H}) > 0$: net positive crossings yield a repulsive Coulomb contribution.
- $Q(\mathfrak{H}) = 0$: the configuration is electromagnetically neutral.
- $Q(\mathfrak{H}) < 0$: net negative crossings yield an attractive Coulomb contribution.

The ratio of Coulomb to strong contributions evaluates to $\tanh(\ln q) \approx 0.104$ at $q = q_0$.
<!-- FILE_END: coulomb-charge.md -->

<!-- FILE_START: coulomb-strong-ratio-q-rational.md -->
*For every real $q > 0$ (the substrate-anchor regime, $\operatorname{Im}(q) = 0$ at the archimedean place), the ratio satisfies:*

$$
  \tanh(\ln q) \;=\; \frac{q - q^{-1}}{q + q^{-1}} \;=\; \frac{q^2 - 1}{q^2 + 1}.
$$

*The Coulomb/strong ratio from $\operatorname{def:coulomb-charge}$ equals the q-rational expression $(q_0^2 - 1)/(q_0^2 + 1)$ at the substrate anchor. They represent the SAME object, not two different choices.*

## Significance

`def:coulomb-charge` defines the Coulomb-to-strong ratio as $\tanh(\ln q)$. This proposition confirms that the analytic and the algebraic forms coincide identically over real $q > 0$. This removes any ambiguity regarding whether the framework employs a "classical-$\tanh$" or a "$q$-deformed $\tanh_q$" realization at the substrate anchor.

The forms match because $\exp(\ln q) = q$ for $q > 0$. Therefore,

$$
  \tanh(\ln q)
  \;=\; \frac{e^{\ln q} - e^{-\ln q}}{e^{\ln q} + e^{-\ln q}}
  \;=\; \frac{q - q^{-1}}{q + q^{-1}}
  \;=\; \frac{q^2 - 1}{q^2 + 1}
  \quad\text{(multiply numerator and denominator by $q$).}
$$
<!-- FILE_END: coulomb-strong-ratio-q-rational.md -->

<!-- FILE_START: skein-crossing-asymmetry-prop.md -->
The Skein relation assigns positive crossings a weight of $q$ and negative crossings a weight of $q^{-1}$:

$$
  q  L_+ -  q^{-1} L_-
  =  (q^{1/2} - q^{-1/2}) L_0.
$$

For $q > 1$, the per-crossing repulsive Coulomb correction relative to a mixed-charge baseline evaluates to:

$$
  \delta_{\mathrm{Coulomb}}
  =  q -  \tfrac{1}{2}(q + q^{-1})
  =  \tfrac{1}{2}(q - q^{-1})
   >  0.
$$

The ratio of the antisymmetric (Coulomb) to symmetric (strong) Skein weights is:

$$
  \frac{q - q^{-1}}{q + q^{-1}}
  =  \tanh(\ln q).
$$

At $q = 1$, the asymmetry vanishes. As $q \to \infty$, the ratio approaches $1$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs—real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The generic categorical/$q$-deformation identities it relies upon remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: skein-crossing-asymmetry-prop.md -->

<!-- FILE_START: skein-crossing-asymmetry.md -->
The $R$-matrix braiding ([R-matrix](#rem:r-matrix-braiding)) enforces a fundamental asymmetry between positive and negative crossings. The Skein relation

$$
  q  L_+ -  q^{-1} L_-
  =  (q^{1/2} - q^{-1/2}) L_0
$$

weights positive crossings by $q$ and negative crossings by $q^{-1}$. Because $q > 1$, positive crossings contribute *more* to the Skein polynomial than negative ones. This asymmetry constitutes the topological origin of electromagnetic repulsion.

**Emergent Coulomb repulsion.**
For a hadron $\mathfrak{H}$ with Coulomb charge $Q(\mathfrak{H})$ ([Coulomb charge](#def:coulomb-charge)), the crossing energy ([crossing energy](#def:crossing-energy)) decomposes into a symmetric (strong) baseline and an antisymmetric (Coulomb) correction. The per-crossing repulsive correction between composites of the same charge relative to a mixed-charge baseline is

$$
  \delta_{\mathrm{Coulomb}}
  =  q -  \tfrac{1}{2}(q + q^{-1})
  =  \tfrac{1}{2}(q - q^{-1})
  > 0.
$$

**Unification of strong and electromagnetic interactions.**
Electromagnetic repulsion does *not* operate as a separate force in the QOU framework. It is a **phase asymmetry** in the same Skein polynomial that dictates the strong binding. Both interactions stem from the $R$-matrix braiding of $\mathcal{U}_q(\mathfrak{su}(2))$. The parameter $q$ controls their relative strength:

- The strong binding scales with $\tfrac{1}{2}(q + q^{-1})$ (the baseline Skein weight).
- The electromagnetic repulsion scales with $\tfrac{1}{2}(q - q^{-1})$ (the crossing asymmetry).

Their ratio evaluates to

$$
  \frac{\text{Coulomb}}{\text{Strong}}
  =  \frac{q - q^{-1}}{q + q^{-1}}
  =  \tanh\!\left(\ln q\right).
$$

At $q = 1$ (classical limit), the asymmetry vanishes and the electromagnetic interaction disappears. At $q \to \infty$ (deep-quantum regime), the ratio approaches $1$ and the two interactions balance.

Chapter 6 details the specific assignment of Coulomb charges to protons and neutrons, and its consequences for nuclear stability, which require the Descartes universe ($\chi = -6$).
<!-- FILE_END: skein-crossing-asymmetry.md -->

<!-- FILE_START: skein-bar-antisymmetry.md -->
The Hecke--Skein relation

$$
  L_+ - L_-  =  (q - q^{-1})\,L_0
  \tag{S}
$$

in the Iwahori--Hecke algebra $H_n(q)$ is **antisymmetric** under the bar involution

$$
  \overline{\,\cdot\,} \colon
  (L_+,\,L_-,\,L_0,\,q)
  \;\longmapsto\;
  (L_-,\,L_+,\,L_0,\,q^{-1}).
$$

Applying $\overline{\,\cdot\,}$ to both sides of (S) yields $-1$ times (S):

$$
  \overline{L_+ - L_-}  =  L_- - L_+
   =  -\,(L_+ - L_-),
  \qquad
  \overline{(q - q^{-1})\,L_0}
   =  (q^{-1} - q)\,L_0
   =  -\,(q - q^{-1})\,L_0.
$$
<!-- FILE_END: skein-bar-antisymmetry.md -->


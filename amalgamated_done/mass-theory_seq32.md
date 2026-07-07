<!-- FILE_START: intro-lp-dual-jucys-murphy.md -->
The operator-selection LP admits a dual program whose variables are the shadow prices of the Frobenius positivity constraints. The Jucys-Murphy central elements of the Hecke algebra furnish a canonical basis where the dual variables have a transparent categorical interpretation. Each shadow price acts as the residue of a Jucys-Murphy operator at a Wedderburn block.

The sequence establishes the LP dual-Jucys-Murphy correspondence and proves the central-element identities required to read off the shadow prices. It verifies that the active demand channels coincide with the most receptive sub-braids. The closing blocks tabulate the Jucys-Murphy spectra for small $n$ and connect the active-set identification to the binding-energy substrate formula.
<!-- FILE_END: intro-lp-dual-jucys-murphy.md -->

<!-- FILE_START: jucys-murphy-central-elements-qou.md -->
**Proposition.**
*In the Iwahori-Hecke algebra $H_n(q)$, the Jucys-Murphy elements*

$$
  J_k \;=\; q^{1-k}\sum_{i < k} \sigma_{i,k},
  \qquad k = 1, 2, \ldots, n
$$

*generate a maximal commutative subalgebra. The elementary symmetric polynomials*

$$
  P_\ell \;:=\; e_\ell(J_1, J_2, \ldots, J_n)
  \;\in\; Z\bigl(H_n(q)\bigr)
$$

*lie in the centre and act on the Wedderburn block $V_\lambda$ as the scalar*

$$
  c_\ell(\lambda) \;=\; e_\ell\!\left(\{q^{2c(\square)} :
    \square \in \lambda\}\right)
$$

*where $c(\square) = j - i$ is the content of cell $\square = (i,j)$.*
<!-- FILE_END: jucys-murphy-central-elements-qou.md -->

<!-- FILE_START: jucys-murphy-central-elements-qou-interpretation.md -->
**Remark.**
The Jucys-Murphy elements are the Hecke-algebraic shadow of commuting Casimirs in $U_q(\mathfrak{sl}_n)$. They are the natural commuting operators that read off the highest weight of an irreducible representation. The cell content $c(\square)$ is the magnetic quantum number $m_j$ of the corresponding $\mathrm{SU}_q(2)$ weight space, making $c_\ell(\lambda)$ a $q$-deformation of the $\ell$-th Casimir eigenvalue on $V_\lambda$. The crystal limit $q \to 0$ recovers the classical content combinatorics of the Kashiwara crystal.
<!-- FILE_END: jucys-murphy-central-elements-qou-interpretation.md -->

<!-- FILE_START: spin-involution.md -->
**Definition (spin involution on a Frobenius $*$-algebra).**
*Let $(A, \tau, {}^*)$ be a Frobenius $*$-algebra over a commutative ring $R$. A spin involution on $(A, \tau, {}^*)$ is an $R$-linear map $\sigma : A \to A$ satisfying:*

1. *Involution: $\sigma \circ \sigma = \mathrm{id}_A$.*
2. *Anti-multiplicative: $\sigma(a b) = \sigma(b)\, \sigma(a)$ for all $a, b \in A$.*
3. *Trace-invariant: $\tau \circ \sigma = \tau$.*
4. *$*$-compatible: $\sigma(a^*) = \sigma(a)^*$ for all $a$.*

*The $\mathbb{Z}/2$ grading $A = A_+ \oplus A_-$ by $\sigma$-eigenvalue defines the spin grading. The space $A_+$ is the spin-singlet sector and $A_-$ is the spin-doublet sector.*

When applying the $A_\pm$ projections, assume $2 \in R^\times$. Without this hypothesis, the projections $a_\pm := \tfrac{1}{2}(a \pm \sigma(a))$ are ill-defined.

Every $a \in A$ has the canonical decomposition $a = a_+ + a_-$. The isospin third-component evaluates on $\sigma$-eigenvectors as:

$$
  T_3(a) \;=\; \tfrac{1}{2}\,\mathrm{sgn}_\sigma(a)
  \;\in\; \{-\tfrac{1}{2},\, 0,\, +\tfrac{1}{2}\}.
$$

For a general $a \in A$, read $T_3$ off the $A_\pm$-projection $a = a_+ + a_-$. The derived spin grading secures the additive homomorphism properties, the orthogonality of the sectors $A_+ \cap A_- = 0$, and the explicit mapping $2\,T_3 = \mathrm{sgn}_\sigma$.
<!-- FILE_END: spin-involution.md -->

<!-- FILE_START: spin-involution-lp-dual-invariance.md -->
**Proposition (spin-invariance of the LP-dual).**
*Let $(A, \tau)$ be a Frobenius algebra with spin involution $\sigma$. Let $c \in A$ be $\sigma$-invariant. Let $\Sigma$ be a $\sigma$-stable set of central idempotents of $A$. For any $\beta \in A$, the optimal dual variable $y_0^*$ of the operator-selection LP*

$$
  \min_{x \in A}\; \tau(c \cdot x)
  \quad \text{s.t.} \quad
  \tau(\beta^* \beta \cdot x) = n_{\mathrm{target}}(\beta), \;\;
  \tau(\pi_\lambda \cdot x) \geq 0 \;\; \forall \lambda \in \Sigma
$$

*satisfies*

$$
  y_0^*\bigl(\sigma(\beta)\bigr) \;=\; y_0^*(\beta).
$$
<!-- FILE_END: spin-involution-lp-dual-invariance.md -->

<!-- FILE_START: spin-involution-lp-dual-invariance-interpretation.md -->
**Remark.**
Isospin is not exclusive to nucleons. It is the $\mathbb{Z}/2$ grading attached to any Frobenius algebra equipped with a spin involution. When physical observables are extracted as $\tau$-traces of products of central elements and braid recipes, the spin-singlet sector and spin-doublet sector decompose canonically under the LP-dual. The Wigner energy term $\sim |Z - N|/A$ in the BW formula is the $T_3$-projection of this grading. It appears because $|Z - N|$ is the $\mathbb{Z}/2$ charge of the recipe, which the LP-dual reads off mechanically.

The proof does not invoke Lie theory or $SU(2)$ symmetries. Any quantum-algebraic system with a trace-preserving spin involution, a $\sigma$-invariant central cost, and a $\sigma$-stable channel set inherits LP-dual spin-invariance. Particle physics exhibits isospin because nucleons populate a 2-row Wedderburn stratum governed by the same algebra. The Wigner-energy phenomenology is the LP-dual shadow of the categorical $\mathbb{Z}/2$ grading.
<!-- FILE_END: spin-involution-lp-dual-invariance-interpretation.md -->

<!-- FILE_START: lp-dual-scaling-conjecture.md -->
**Remark.**
Empirical data on $y_0^*$ verifies mirror-pair invariance across the physical regime. However, the ratio $T/D$ depends strongly on $q$, ruling out the simplest separable closed form $y_0^*(A, |T_3|) = g_\ell(q) \cdot h_\ell(A, |T_3|)$.

Candidate closed forms require structural analysis. A partition-of-unity decomposition sums over the LP-dual active set. A Wedderburn-block-resolved form decomposes $y_0^*$ over per-block contributions, leveraging the Hopf antipode to secure mirror-pair invariance. The Demazure sub-crystal selector empirically picks out specific crystal-graph weights, suggesting the true scaling operates at the Demazure component level rather than as a global structural property.
<!-- FILE_END: lp-dual-scaling-conjecture.md -->

<!-- FILE_START: wigner-2-coefficient.md -->
**Proposition.**
*For any self-conjugate partition $\lambda = \lambda'$ of $k$, the per-generator trace in the Hoefsmit seminormal representation evaluates to:*

$$
  \frac{\mathrm{tr}(\sigma_g^{(\lambda)})}{\dim(\lambda)}
  = \frac{h}{2}
  = \frac{q - q^{-1}}{2}.
$$

*Consequently, the BW shadow-price coefficient for $\lambda$ is:*

$$
  C_\lambda = w_\lambda \cdot \frac{h}{2}
  = \frac{\dim_q(\lambda)^2}{[k]_q!} \cdot \frac{q - q^{-1}}{2}.
$$
<!-- FILE_END: wigner-2-coefficient.md -->

<!-- FILE_START: wigner-2-coefficient-interpretation.md -->
**Remark.**
The value $h/2$ is the arithmetic mean of the symmetric eigenvalue $q$ and the antisymmetric eigenvalue $-q^{-1}$. Self-conjugate partitions occupy the exact isospin midpoint of the Hecke spectrum.

The proton-neutron crossing is invisible to $[3,2,1]$. Its trace contribution cancels exactly. Only $pp$ and $nn$ crossings contribute, doing so with opposite signs. The BW scaling for $[3,2,1]$ is therefore proportional to the net $pp$ minus $nn$ asymmetry $(Z - N)(A - 1)$, rather than the isospin Casimir $T(T+1)$.
<!-- FILE_END: wigner-2-coefficient-interpretation.md -->

<!-- FILE_START: mass-endomorphism-tower.md -->
**Proposition.**
*The mass of a vortex $\varrho$ with braid representative $\beta \in B_n$ and $n - 1$ generators evaluates as:*

$$
  \mathfrak{m}(\varrho)
  =
  \Bigl\lvert \prod_{i=0}^{n-2} \hat{V}_i^{\mathrm{full}} \Bigr\rvert
  -
  \sum_{i=0}^{n-2}
    \mathrm{Li}_2^q\!\bigl(-\lvert\hat{V}_i^{\mathrm{full}}\rvert\bigr)
  -
  \sum_{0 \leq i < j \leq n-2}
    z^2 \cdot \mathrm{Li}_2^q\!\bigl(-\lvert\hat{V}_i^{\mathrm{full}}
      \cdot \hat{V}_j^{\mathrm{full}}\rvert\bigr),
$$

*where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov parameter and $\mathrm{Li}_2^q$ is the symmetric q-dilogarithm $\mathrm{Li}_2^q(z) = \sum_{n \geq 1} z^n / (n \cdot [n]_q)$.*

The three sums isolate the three types of blow-up centers in the brane tower. The descended term is the base-level regular-representation trace. The single-generator blow-ups and the pair blow-ups apply the $\mathrm{Li}_2^q$ functional across the generator loci. The weight $z^2$ for pairs strictly follows from the Markov-trace factorization.

The substitution of $\mathrm{Li}_2^q$ for the older $\Phi_q$ Kashaev limit is canonical. The Faddeev $\Phi_q$ form was empirically incompatible with isospin symmetry at $q_0$ and created massive mirror-nucleus pathologies. The literal integration of the $q$-deformed dilogarithm evaluates securely to $\mathrm{Li}_2^q$.
<!-- FILE_END: mass-endomorphism-tower.md -->

<!-- FILE_START: mass-endomorphism-jet-tower.md -->
**Remark.**
The tower formula limits explicitly to quadratic $\hat{V}_i \hat{V}_j$ coordinates per jet level. The Hecke relation and the $\Phi_q$ pentagon identity are intrinsically quadratic. Triple or higher interactions at level $n$ ascend to level $n+1$ as new singletons or pairs, ensuring they are captured appropriately by the level-$(n+1)$ contribution. The descended contribution carries a single holonomy contribution from the level-0 unknot core and is not summed iteratively over jet levels.
<!-- FILE_END: mass-endomorphism-jet-tower.md -->

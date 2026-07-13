<!-- FILE_START: particle-interactions-intro.md -->
This chapter develops the computational engine that derives particle interactions, nuclear structure, and atomic construction from the categorical framework of Parts I and II. We deploy two principal tools: Gröbner--Shirshov reduction in the Iwahori--Hecke algebra $H_A(q)$ (yielding unique normal forms for nuclear braid words) and linear programming duality over the Frobenius Gram matrix (selecting confinement operators by minimizing categorical action).

First, the reduction engine dictates that every nucleus $\mathcal{N}(Z,N)$ forms a braid word in $B_A$ with a unique, path-independent Gröbner--Shirshov normal form. Next, the linear programming framework recasts confinement operator selection as a linear program. Strong duality yields the Borromean link $\mathcal{B}_3$ as the unique optimum. From these mechanisms, we derive nucleon structure, nuclear binding, magic numbers, beta decay via transfer matrices, and the Wedderburn mass formula.

These derivations remain symbolic in $q$. Witness evaluations at $q_0$ provide numerical verification. This chapter isolates the *how* of particle interactions from the *what* of particle definitions and the *observed* predictions. We develop molecular extensions in Chapter 12.
<!-- FILE_END: particle-interactions-intro.md -->

<!-- FILE_START: nuclear-groebner-reduction.md -->
Every nucleus $\mathcal{N}(Z, N)$ corresponds to a braid word in $B_A$. Gröbner--Shirshov reduction in $H_A(q)$ produces a unique normal form representing the lowest-energy state.

**Convention.** $\mathcal{N}(Z, N)$ denotes the reduced normal form unless explicitly stated.

**Proposition.**
Let $R = \mathbb{Z}[q, q^{-1}]$. $q$ is a categorical invariant, not a free parameter. The Iwahori--Hecke algebra $H_A(q) = R[B_A] / I$ admits an admissible system $(B, <)$.

The Gröbner--Shirshov basis $G$ for $I$ consists of:
1. **Hecke relation**: $\sigma_i^2 - (q - q^{-1})\sigma_i - 1$
2. **Yang--Baxter relation**: $\sigma_i\sigma_{i+1}\sigma_i - \sigma_{i+1}\sigma_i\sigma_{i+1}$
3. **Far commutativity**: $\sigma_i\sigma_j - \sigma_j\sigma_i$ for $|i - j| \geq 2$

The division algorithm computes the remainder, yielding the unique normal form:

$$
  \mathcal{N}(Z, N)
   := 
  r\bigl(\mathcal{N}_{\mathrm{raw}}(Z, N), G\bigr)
   \in  H_A(q).
$$

By Gröbner--Shirshov basis theory, the remainder is path-independent.

**The nuclear braid word.**
The unreduced braid word is:

$$
  \mathcal{N}(Z, N)
  = 
  \prod_{1 \leq i < j \leq A}
  \sigma_{i}^{\epsilon(i, j)}
$$

where the crossing sign $\epsilon(i, j)$ depends on nucleon types: $+1$ (protons), $-1$ (neutrons), $0$ (mixed, resolved as $\tfrac{1}{2}(\sigma_i + \sigma_i^{-1})$).

Gröbner--Shirshov reduction collapses the exponential expansion into the normal form.

**Computational results.**
The change in total Hecke weight under beta decay is always negative, confirming that beta decay releases energy. The normal form is tractable for numerical evaluation via the Markov trace.
<!-- FILE_END: nuclear-groebner-reduction.md -->

<!-- FILE_START: nuclear-reduction-algorithm.md -->
We compute the Gröbner--Shirshov normal form of a nuclear braid word via the division algorithm, specialized to the Iwahori--Hecke algebra.

**Input:** Mass number $A = Z + N$, proton number $Z$, neutron number $N$. The algebra $H_A(q)$, admissible system $(B, <)$, and Gröbner--Shirshov basis $G$.

**Output:** The unique normal form $\mathcal{N}(Z, N) \in H_A(q)$ and its Markov trace.

The algorithm proceeds inductively.

1. Initialize with the normal form of the first nucleon.
2. For each subsequent nucleon, determine the crossing type based on nucleon pairs ($pp$, $nn$, or mixed).
3. Form the product and apply the division algorithm.
4. Return the final reduced form and its trace.

**Correctness.** The output is independent of the choice of $g \in G$ because $G$ is a Gröbner--Shirshov basis.

**Complexity.** The inductive strategy requires $O(A^2)$ multiplications and $O(A^3)$ Hecke reduction steps. Multiplying all crossings before reduction would generate $O(2^{Z \cdot N})$ terms.
<!-- FILE_END: nuclear-reduction-algorithm.md -->

<!-- FILE_START: groebner-shirshov-energy.md -->
The Gröbner--Shirshov basis theory gives a stronger result than uniqueness: the energy of the nuclear braid word is a topological invariant, computed with no path dependence.

**Theorem.**
Define the energy functional on $H_A(q)$ by

$$
  E(\xi) =  \sum_{w \in B} |c_w(q)| \cdot \ell(w)
$$

where $\xi$ is the normal form and $\ell(w)$ is the word length. Then:

1. **Only Hecke reductions change energy.** The Yang--Baxter relation and far commutativity preserve coefficients and lengths. The Hecke relation is the unique energy-changing generator.
2. **Energy is path-independent.** The total energy change is independent of the order of applied basis elements. This follows from confluence.
3. **Each Hecke step has a definite energy.** Replacing $\sigma_i^2$ with $(q - q^{-1})\sigma_i + 1$ changes energy by $|c| \cdot |q - q^{-1}|$. Every Hecke step increases the total weight.

**Archimedean specialisation (§7c).** The energy $|c|\,(q - q^{-1})$ and its positivity for $q > 1$ are stated over $\mathbb{R}$. This block sits on the archimedean side of the substrate wall.
<!-- FILE_END: groebner-shirshov-energy.md -->

<!-- FILE_START: groebner-shirshov-energy-interpretation.md -->
**Remark (physical interpretation).**
The energy functional $E(\mathcal{N}(Z, N))$ gives the Skein binding energy of the nucleus. Each Hecke step resolves a double crossing into a weighted single crossing plus a resolved identity term. The factor $(q - q^{-1})$ acts as the crossing asymmetry. The Hecke reduction algebraically expresses the physical process of resolving a double crossing into its electromagnetic and strong components.
<!-- FILE_END: groebner-shirshov-energy-interpretation.md -->

<!-- FILE_START: inductive-gb-reduction.md -->
We compute the nuclear normal form inductively by reducing intermediate words after each multiplication.

**Proposition.**
*The inductive step yields a normal form containing at most $\binom{A-1}{\lfloor(A-1)/2\rfloor}$ terms.*
<!-- FILE_END: inductive-gb-reduction.md -->

<!-- FILE_START: nucleon-ordering-factorization.md -->
The Wedderburn--Artin decomposition of $H_3(q)$, combined with jet-descended confinement, factorizes the nuclear Markov trace. This factorization renders the ground-state ordering search trivial in two of the three channels.

## Statement

**Proposition.**
*The Markov trace decomposes as:*

$$
  \mathrm{tr}_M(\mathcal{N})
  =
  W_{\mathrm{sym}} \cdot S(\pi)
  + W_{\mathrm{std}} \cdot (z \cdot a_\pi + b_\pi)
  + W_{\mathrm{alt}} \cdot A(\pi)
$$

*(i) Ordering independence of scalar channels.*
*The symmetric product $S(\pi)$ and alternating product $A(\pi)$ remain independent of the ordering $\pi$ for a fixed composition.*

*(ii) Standard-channel factorization.*
*The standard-channel state emerges from a $2 \times 2$ matrix product.*

*(iii) Jet-descended nucleon blocks.*
*Intra-nucleon crossings yield fixed $2 \times 2$ transfer matrices $T_\mathfrak{p}^{\mathrm{std}}$ and $T_\mathfrak{n}^{\mathrm{std}}$. We precompute these once.*

*(iv) Inter-nucleon crossings (transient).*
*Each inter-nucleon crossing carries a $2 \times 2$ matrix dictated by the pair type.*

## Computational consequence

Factorization reduces the ordering search cost from $\binom{A}{Z} \times O(A^2) \times O(36)$ to $\binom{A}{Z} \times O(A^2) \times O(4)$, providing a $\sim 9 \times$ reduction per ordering.

## Compact nucleon notation

The factorization suggests a natural nucleon-level alphabet. A nucleus is written:

$$
  \mathcal{N}(\pi)
  =
  \mathfrak{t}_1 \cdot \mathfrak{t}_2 \cdots \mathfrak{t}_A
$$

where $\mathfrak{t}_k \in \{\mathfrak{p}, \mathfrak{n}\}$. The six normal-form coefficients per nucleon collapse to a $2 \times 2$ matrix plus two precomputed scalars.
<!-- FILE_END: nucleon-ordering-factorization.md -->

<!-- FILE_START: box-braid-irreducibility.md -->
**Proposition.**
The process $\gamma\gamma \to \nu\nu^{\sigma}$ requires the $T_{3,5}$ torus knot topology. The crossing number $c(T_{3,5}) = 10$ is a topological invariant. Therefore:

1. The process cannot occur before Planck step $10$.
2. No simpler mediator exists.
3. The box is the minimum-crossing topology for any $\gamma$–$\nu$ interaction.

**The $T_{3,5}$ braid word.**
The torus knot $T_{3,5}$ has braid representation $(\sigma_1\sigma_2)^5 \in B_3$ with 10 crossings.
<!-- FILE_END: box-braid-irreducibility.md -->

<!-- FILE_START: box-braid-irreducibility-interpretation.md -->
**The box braid: crossing-by-crossing.**

The process $\gamma\gamma \to \nu\nu^{\sigma}$ has no tree-level realisation. The minimal topology is a box with four vertices and four internal propagators at brane tower level $A_1$.

**Vertex structure.**
- **EM vertices** ($\gamma \leftrightarrow e^-e^+$): The photon's $\dagger$-involution couples to the trefoil's antisymmetric crossing energy. This creates virtual pairs.
- **Weak vertices** ($e \to \nu$ via $T_{3,5}$): The Skein relation converts the charged trefoil to the neutral unknot.

**Corollary: neutrino stability.**
The neutrino is strictly stable. It cannot decay via any process.
1. **No beta decay.** The neutrino is an elementary knot with no internal constituents.
2. **No scattering decay.** Any decay channel must pass through the $T_{3,5}$ topology. The topological obstruction barrier scales with the invariant crossing number, strongly suppressing the channel.
3. **No simpler process.** $T_{3,5}$ is the unique cross-family mediator.

The neutrino is stable by the energetic inaccessibility of its only interaction channel.
<!-- FILE_END: box-braid-irreducibility-interpretation.md -->

<!-- FILE_START: generator-volume-decomposition.md -->
The canonical trace decomposes as a sum of generator volumes. A transfer matrix product computes each generator's volume. These terms organize as a jet expansion in the nucleon count.

**Proposition.**
At each generator $\sigma_i$, nucleon $i$ crosses with subsequent nucleons. These crossings act on $\sigma_i$ and reduce via the Hecke relation to a linear combination:

$$
  \prod_{j=i+1}^{A-1} C_{ij}(\sigma_i)
  = 
  a_i  \sigma_i + b_i
$$

The coefficients $(a_i, b_i)$ satisfy a recurrence, defining a $2 \times 2$ transfer matrix $T_j$ at each crossing.

## Jet expansion in the nucleon count

The transfer matrix product $M_i = \prod_{j=i+1}^{A-1} T_j$ admits a jet expansion. Each order corresponds to a color degree. The total step count across all generators matches the number of nucleon pairs, $\binom{A}{2}$.

## Beta decay as the 1-jet variation

Single beta decay changes one nucleon type. The trace variation represents the 1-jet of the volume functional in the nucleon-type variable.

## Double beta decay as the 2-jet variation

Double beta decay changes two nucleons simultaneously. The trace variation includes a 2-jet cross-term encoding the correlation between the converting nucleons.

For neutrinoless double beta decay, the 2-jet cross-term adopts a different structure, corresponding to a single unknot threading both crossing changes.

## The jet bundle structure

The generator volumes form a section of a jet bundle over the nuclear configuration space. The base is the space of nucleon-type assignments.

## Generator volume profile

The Markov-traced volume at generator $\sigma_i$ is $\hat{V}_i = z \cdot a_i + b_i$. The canonical trace decomposes accordingly.

## The volume of the ideal

The Gröbner--Shirshov ideal absorbs the difference between the unreduced weight and the reduced weight. The total ideal volume measures the portion of the naive crossing count absorbed by double-crossing resolutions.

## Connection to the Reeb decomposition

The color degree at each generator corresponds to the vertical degree of the Reeb flow. The jet expansion provides the Taylor series of the transfer matrix product along the Reeb flow direction.
<!-- FILE_END: generator-volume-decomposition.md -->

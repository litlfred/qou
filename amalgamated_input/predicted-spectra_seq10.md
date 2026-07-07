<!-- FILE_START: intro-integer-stability-diophantine.md -->
The integer-stability mechanism identifies stable proton and neutron counts as points in a *Diophantine valley*. This lattice of $(Z, N)$ pairs minimises the categorical mass functional under substrate flow. The following blocks state the mechanism, construct the valley, and prove its stability against perturbations of the substrate parameter.
<!-- FILE_END: intro-integer-stability-diophantine.md -->

<!-- FILE_START: integer-stability.md -->
The [beta-stability line](#prop:beta-stability) defines a continuous optimum $p^*(A)$. Physical nuclei require integer proton and neutron numbers. Stable hadrons correspond to integer solutions of a quadratic energy minimisation.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with substrate parameter $q$. At a fixed mass number $A = Z + N$, the nuclear binding energy is a strictly convex quadratic in the proton number $p$:

$$
  E(p, A) = 
  \underbrace{\left(\frac{a_C}{A^{1/3}} + \frac{a_A}{A}\right)}_{\alpha(A)} p^2
  - \underbrace{a_A}_{\gamma} p
  + \delta(A),
$$

where $a_C = (q - q^{-1}) \lambda_C$ is the Coulomb coefficient, $a_A$ is the Pauli asymmetry coefficient, and $\delta(A)$ collects terms independent of $p$.

The continuous minimum is

$$
  p^*(A) =  \frac{\gamma}{2\alpha(A)} =  \frac{a_A A}{2(a_A + a_C A^{2/3})}.
$$

Because $E$ is strictly convex in $p$, the exact integer minimiser $p_{\mathrm{stab}}(A)$ is one of the two nearest integers to the continuous minimum:

$$
  p_{\mathrm{stab}}(A) = \mathrm*{argmin}_{p \in \{0, 1, \ldots, A\}} E(p, A) \in \bigl\{\lfloor p^*(A) \rfloor, \lceil p^*(A) \rceil\bigr\}.
$$

**Even-odd selection.**
The pairing energy $\pm \lambda_P / A^{1/2}$ breaks the $p \leftrightarrow p + 1$ symmetry at the rounding boundary. The system selects the pair $(p, A - p)$ where both are even. This yields the observed even-even dominance: of the 254 stable nuclides, 166 have even $p$ and even $n$.

**Regime transitions.**
The minimiser $p_{\mathrm{stab}}(A)$ increases by $1$ when $p^*(A)$ crosses a half-integer. To leading order, the critical mass numbers for this transition are

$$
  A_k = \left( \frac{a_C (2k + 1)}{2a_A} \right)^{3/2}.
$$

These are the **beta-decay thresholds**. At $A = A_k$, the nuclei $(k, A_k - k)$ and $(k + 1, A_k - k - 1)$ have equal binding energy. Beta decay is energetically neutral.

**Archimedean specialisation (§7c).** 
The binding energy $E(p)$, its continuous optimum $p^*$, and the convex-minimisation argument are stated over $\mathbb{R}$. The integer-minimiser bound relies on the real ordering.
<!-- FILE_END: integer-stability.md -->

<!-- FILE_START: integer-stability-novelty.md -->
**Algebraic rigidification.**
This nearest-integer minimization reframes even-even dominance algebraically. The empirical observation stems from a rigid convex optimization over the quantum integers. This supplements standard liquid-drop models.
<!-- FILE_END: integer-stability-novelty.md -->

<!-- FILE_START: diophantine-valley.md -->
The nuclear stability problem is a Diophantine problem on an algebraic curve. The stable hadrons (the nuclei that exist in nature) are precisely the integer solutions to an equation derived from the Skein binding Lagrangian.

**The stability cubic.**

Substituting $t = A^{1/3}$ into the continuous stability condition $p^*(A) = a_A A / (2a_A + 2a_C A^{2/3})$ ([integer stability](#prop:integer-stability)) and clearing denominators yields the stability cubic:

$$
  t^3 =  2p(1 + ct^2),
  \qquad
  c = \frac{a_C}{2a_A}.
$$

This plane curve $\mathcal{S} \subset \mathbb{A}^2$ parametrizes the locus of beta-stable nuclei in the $(p, t)$-plane. The physical nuclei are the integer points of $\mathcal{S}$: pairs $(p, A) \in \mathbb{Z}^2$ with $t = A^{1/3}$ and $A = t^3 \in \mathbb{Z}$.

**Comparison with the color fibration.**

The color elliptic curve of Bring's surface ([color elliptic](#prop:color-elliptic)) is the cubic:

$$
  X^3 + (z + 1)X^2 + (z^2 + z + 1)X
  + (z^3 + z^2 + z + 1) = 0
$$

in the color variable $X$ at spacetime ratio $z$. The stability cubic and the color cubic are both one-variable cubics parametrized by another variable, arising from the same $\chi = -6$ surface. The [elliptic stability conjecture](#rem:elliptic-stability-locus) posits that when the pairing energy lifts the stability cubic to genus $1$, the resulting elliptic curve is isogenous to the color fiber.

**The $n/p$ ratio.**

For each proton number $p$, the stable neutron number $n^*(p)$ satisfies:

$$
  \frac{n^*(p)}{p}
  = 
  \frac{A^*(p)}{p} - 1
  = 
  1 + 2c \cdot {A^*}^{2/3} + O(1/p)
$$

where $A^*(p)$ solves $p = A/(2 + cA^{2/3})$. The ratio $n/p$ is a slowly growing function of $p$. Its integer-part transitions occur at specific elements:

See [Table](#tbl:diophantine-valley-table-data).

**Stable hadrons as integer points on an algebraic curve.**

Every stable nucleus in nature corresponds to a lattice point $(p, A) \in \mathbb{Z}^2$ on the stability cubic $\mathcal{S}$. The nuclear chart is not a phenomenological fit; it is the set of integer solutions to an algebraic equation determined by the single parameter $q$.

When the pairing correction lifts $\mathcal{S}$ from genus $0$ to genus $1$ ([elliptic stability conjecture](#rem:elliptic-stability-locus)), the stability pairs become rational points of an elliptic curve $\mathcal{E}_p$ over $\mathbb{Q}(q)$. Mordell's theorem constrains them to a finite set, potentially explaining why only finitely many stability pairs exist.

**Connection to the substrate parameter.**

The curvature parameter $c = (q - q^{-1})\lambda_C / (2a_A)$ is controlled entirely by $q$. At $q = 1$, the stability cubic degenerates to $t^3 = 2p$, a rational parametrization where all nuclei are symmetric ($n = p$). As $q$ increases from $1$, the $ct^2$ term bends the curve. The integer solutions disperse, and the structure of the nuclear chart (neutron excess, stability pairs, even-odd staggering) emerges from a single deformation parameter.
<!-- FILE_END: diophantine-valley.md -->

<!-- FILE_START: valley-stability.md -->
This visualization frames the valley of stability as a Diophantine approximation problem.

**Controls:**
- **$q$ slider**: Varies the substrate parameter from $1.0$ (classical, no Coulomb) to $2.0$ (deep quantum). Default: the substrate $q$.
- **View**: Toggle between $(p, n)$-plane and $(A, n/p)$-plane.

**Display:**
- **Blue curve**: Continuous beta-stability line $p^*(A) = A/(2 + cA^{2/3})$ from the Skein binding Lagrangian.
- **Green dots**: Integer lattice points $(p_{\mathrm{stab}}, n_{\mathrm{stab}})$ for observed stable isotopes.
- **Red segments**: Diophantine error $\varepsilon(A)$ (vertical distance from each lattice point to the curve).
- **Gold diamonds**: Stability pairs (shell closures).
- **Shaded band**: Valley width (range of $p$ values within one beta-decay half-life of the stable isotope).

As $q \to 1$, the curve straightens to $p = A/2$. All lattice points fall on this diagonal. The Diophantine problem becomes trivial. As $q$ increases, the curve bends, lattice points scatter, and the stability-pair structure emerges.
<!-- FILE_END: valley-stability.md -->


The Kashaev volume conjecture states:

$$
  \mathrm{Vol}(S^3 \setminus K)
   \;=\; 2 \pi \cdot \lim_{n \to \infty}
    \frac{\log |J_K(\zeta_n, n)|}{n}.
$$

We evaluate the $n$-th coloured Jones polynomial $J_K(q, n)$ at $\zeta_n = e^{2 \pi i / n}$. The operator $\mathrm{Vol}$ yields the hyperbolic volume. Murakami and Murakami [@murakami-murakami2001] proved this for various knots, but full generality remains open.

The conjecture presents two awkward features for QOU:

1. The left-hand side uses hyperbolic volume. This pure analytic geometry breaks under surreal replacement ([analytic obstructions](#rem:analytic-obstructions)).
2. The right-hand side takes an asymptotic-$n$ limit at a root of unity. This is a singular limit in $\mathbb{C}$.

The surreal lift provides cleaner reformulations and sharpens the gap between the sides.

## Reformulation

We set $n = \omega \in \mathbf{No}$. We interpret $\zeta_\omega = e^{2 \pi i / \omega}$ as an element of $\mathbf{No}[i]$ using Berarducci--Mantova's transseries [@berarducci-mantova2018]. The polynomial $J_K(q, n)$ is rational in $q$ and polynomial in $n$. Thus $J_K(\zeta_\omega, \omega)$ evaluates well in $\mathbf{No}[i]$.

The **surreal Kashaev statement** asserts:

$$
  \mathrm{Vol}(S^3 \setminus K)
   \;\stackrel{?}{=}\;
   \mathrm{st}\!\left(
     2 \pi \cdot \frac{\log |J_K(\zeta_\omega, \omega)|}{\omega}
   \right).
$$

We apply the standard-part map $\mathrm{st}$ to a finite surreal.

## The trade-off

This reformulation does not solve the volume conjecture. It trades:

- An analytic limit $\lim_{n \to \infty}$ of complex numbers and a hyperbolic-volume identity in $\mathbb{R}$.

For:

- A surreal evaluation of a polynomial-in-$n$ at $n = \omega$ and the standard-part identity that matches hyperbolic volume.

The right-hand side of the surreal version is manifestly well-defined via rational arithmetic in $\mathbf{No}$. The question reduces to whether the standard-part matches. We replace asymptotic-limit content with standard-part content.

## Location of the algebra-vs-analysis split

The reformulation separates the algebraic and analytic content:

| Side | Algebra-vs-analysis content |
|---|---|
| RHS, before $\mathrm{st}$ | Pure algebra: rational in $\omega$ at root of unity |
| $\mathrm{st}$ application | Asymptotic transseries reduction |
| Identification with $\mathrm{Vol}$ | Genuine hyperbolic geometry |

The first row uses no analysis. The second row uses a single transseries reduction. The third row introduces hyperbolic geometry exclusively on the LHS.

Kashaev becomes one transseries reduction and one $\mathrm{Vol}$-identity. We avoid analytic limits.

## Potential utility and its limits

**Might help:** The algebraic side $J_K(\zeta_\omega, \omega)$ is exactly computable for any specific knot. If a general formula exists for $\mathrm{st}(\log |J_K(\zeta_\omega, \omega)|/\omega)$ in terms of knot data, we gain a path to proof.

**Might not help:** The standard-part identity asserts an analytic asymptotic relationship between algebra and geometry. The surreal lift may merely relocate the difficulty.

## Discussion

The conjecture is a reformulation, not a proof. We separate computable algebraic content from geometric Kashaev content. We should re-derive the Murakami--Murakami proof for the figure-eight knot [@murakami-murakami2001] in surreal form as a sanity check.

## Connection to QOU

We use the Kashaev volume conjecture to cross-check the categorical mass formula ([Kashaev volume--density](#rem:kashaev-volume-density)). The mass formula computes a particle mass via Hoefsmit/Markov-trace data. The cross-check identifies this with a Jones-polynomial evaluation that Kashaev relates to hyperbolic volume.

Under the surreal lift:

- The Hoefsmit/Markov-trace side lifts algebraically to $\mathbf{No}$ ([algebraic core survives](#rem:algebraic-core-survives)).
- The Jones polynomial at $q = q_0 \in \mathbb{R}$ lifts by definition ($q_0 \in \mathbb{R} \subset \mathbf{No}$).
- The hyperbolic volume side stays in $\mathbb{R}$ as an external anchor.
- Kashaev's identity bridges the two as a standard-part identity.

Proving the surreal Kashaev conjecture secures an algebraic foundation for the QOU mass formula independent of hyperbolic geometry.

## Proof strategy

**Reformulation reducibility (provable now)**:

1. We show the classical Kashaev statement and the surreal Kashaev statement are equivalent.
2. Forward direction: If the classical limit yields $\mathrm{Vol}(S^3 \setminus K)$, the transfer principle aligns the standard-part evaluation.
3. Backward direction: If $\mathrm{st}(\cdots) = \mathrm{Vol}(\cdots)$, the asymptotic limit converges to $\mathrm{Vol}$ by definition.

**Verification on known cases (provable now)**:

4. We verify the volume conjecture for the figure-eight knot $4_1$ and the trefoil $3_1$. We compute $J_K(\zeta_\omega, \omega)$ directly, apply $\mathrm{st}$, and match the known volume.
5. We use `QOU.AppendixSurreals.gonshorIn` and `omegaSurreal` for surreal evaluations.

**General case (open)**:

6. The general Kashaev conjecture for hyperbolic knots remains open classically. The surreal reformulation separates algebraic content from geometric volume identity.

**Required infrastructure**:
- Coloured Jones polynomial in Lean (does not exist in mathlib).
- Berarducci–Mantova exponential/logarithm on $\mathbf{No}$ (partial in mathlib).
- Hyperbolic-volume formalization (does not exist in mathlib).

**Falsification path**: The surreal form fails if and only if the classical limit form fails.

**Provability assessment**: The equivalence of the formulations is provable via the transfer principle. We productively reorganize a long-standing open problem.

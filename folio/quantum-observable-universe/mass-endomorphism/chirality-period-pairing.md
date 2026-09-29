**Remark (chirality structure on Goncharov period classes via the bar involution).**

The bar involution $* \colon q \mapsto q^{-1}$ on $H_n(q)$ (equivalently, the Hecke algebra antipode $*(\sigma_i) = \sigma_i^{-1}$) acts on the central primitive idempotents $e_\lambda$ by partition conjugation: $*(e_\lambda) = e_{\lambda'}$, where $\lambda'$ denotes the transposed Young diagram ([`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent) Cross-check 3-4).

Under [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence) and [`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic), this categorifies the chirality structure of hyperbolic $3$-manifold volumes:

| Cell-class | Bar action on $e_\lambda$ | Knot type | Period type |
|---|---|---|---|
| **Self-conjugate** ($\lambda = \lambda'$) | $*(e_\lambda) = e_\lambda$ | amphichiral knot | $\mathrm{Vol}(K) = \mathrm{Vol}(\overline{K})$ — real period in $\mathcal{P}_2(\mathbb{R})$ |
| **Chiral pair** ($\lambda \neq \lambda'$) | $*(e_\lambda) = e_{\lambda'}$ | chiral knot $K \neq \overline{K}$ | $\mathrm{Vol}(K) = \mathrm{Vol}(\overline{K})$, $\mathrm{CS}(K) = -\mathrm{CS}(\overline{K})$ — period with a Tate twist |

## The figure-8 row

The knot $4_1$ is amphichiral: $4_1 \cong \overline{4_1}$. Its dominant cell in $H_4(q)$ is $\lambda = (2, 2)$, the unique self-conjugate $4$-partition. The bar-fixed projection $e_{(2,2)}$ yields the real period $2\,\mathrm{Cl}_2(\pi/3) \in \mathbb{R}$ without a Tate twist.

## A chiral example: trefoil

The knot $3_1$ is chiral: $3_1 \neq \overline{3_1}$. Its dominant cell $\lambda = (3)$ pairs with $\lambda' = (1, 1, 1)$ under the bar involution: $*(e_{(3)}) = e_{(1, 1, 1)}$. The volume vanishes (the trefoil is not hyperbolic), but the Chern–Simons invariant $\mathrm{CS}(3_1) = \pm \pi^2 / 6$ flips sign under the bar involution. This yields the chirality-twisted depth-$3$ period in $\mathcal{P}_3 / \mathcal{P}_2$. It manifests the same chirality structure at depth $3$. See [`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness) for a Bring-natural depth-$3$ witness.

## Compatibility with the depth filtration

The bar involution preserves the iterated-integral depth filtration: $* \colon G^{(n)}(\mathcal{H}_q) \to G^{(n)}(\mathcal{H}_q)$. Each depth $G^{(n)}$ decomposes into bar-eigenspaces:

$$
  G^{(n)}(\mathcal{H}_q) \;=\; G^{(n), +} \;\oplus\; G^{(n), -},
$$

where $G^{(n), \pm}$ are the $\pm 1$ eigenspaces of $*$. Under the archimedean completion $\tau_{\mathrm{arch}}$:

- $G^{(n), +} \to \mathcal{P}_n(\mathbb{R})$ produces real periods.
- $G^{(n), -} \to i \cdot \mathcal{P}_n(\mathbb{R})$ produces imaginary periods. Geometrically, these correspond to Chern–Simons-style invariants paired with a $(2\pi i)^n$-factor from the Tate motive.

Each Goncharov period class $\mathcal{P}_n / \mathcal{P}_{n-1}$ inherits a bar-grading. Hyperbolic volume resides in $\mathcal{P}_2^+$, Chern–Simons in $\mathcal{P}_3^-$, and multiple polylog values split according to the amphichirality of the underlying motive.

## Provenance

This categorifies the amphichirality construction introduced in the figure-$8$ block ([`rem:figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration)). We recast it as a period-theoretic structure on $\mathcal{P}_\bullet$. The bar involution's role remains structural. It organises period classes by the orientation-reversal symmetry of the motivic substrate.

## Falsifiability

We propose a test using a chiral hyperbolic knot $K$ with known $\mathrm{CS}(K) \neq 0$. The simplest such knot is $5_2$, which has $\mathrm{Vol} \approx 2.8281$ and $\mathrm{CS} \approx -0.1530\,\pi^2 \pmod{\pi^2}$. We verify three points:

1. The dominant cell of $5_2$ in $H_4(q)$ (or $H_5(q)$) forms a chiral pair, rather than a self-conjugate cell.
2. The depth-$2$ pairing produces the real $\mathrm{Vol}(5_2)$.
3. The depth-$3$ pairing on the same cell produces the chirality-twisted $\mathrm{CS}(5_2)$.

Discharge remains open. The cell identification at $H_5(q)$ presents the primary technical obstacle.

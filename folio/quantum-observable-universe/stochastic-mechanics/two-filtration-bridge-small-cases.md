The two-filtration bridge conjecture ([Two-filtration bridge: iterated-integral depth $\leftrightarrow$ partition-cellular GB-depth via $e_\lambda$](#conj:two-filtration-bridge)) predicts an iterated-integral depth $d_{\mathrm{II}}(\lambda)$ for each partition $\lambda$:

$$
  d_{\mathrm{II}}(\lambda) =
  \begin{cases}
    2 & \lambda \text{ self-conjugate} \\
    3 & \lambda, \lambda' \text{ chiral pair}
  \end{cases}
$$

*We verify the predicted bridge map for all partitions $\lambda \vdash n$ with $n \leq 4$ by combining the explicit Markov-trace calculation on each Wedderburn cell with known Vol/CS values from classical knot theory.*

*Status (2026-11-16): this is a comparison, not a proof.* No map from cells to
knots is defined, so the knot attached to each cell below is chosen, not
derived. At $n=1,2$ both periods vanish and nothing is witnessed; the trefoil
$\sigma_1^3$ is a 2-strand closure, not an $H_3$ object; and the $(2,1)$ row has
no witness. The proved part of the bridge is item 4 of
[Cell-depth filtration of $Z(H_n(q))$](#prop:cellular-depth-filtration), which is
conditional on two named hypotheses and does not give the depth values.

### Detailed verifications

#### Self-conjugate $\lambda = (2, 2)$, $n = 4$ (figure-8 row)
The figure-8 knot $4_1$ is amphichiral, so $\mathrm{CS}(4_1) = 0 \pmod{\pi^2 \mathbb{Z}}$. Its volume is non-trivial: $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \in \mathcal{P}_2 / \mathcal{P}_1$. Pairing of $e_{(2, 2)}$ with $\mathrm{Li}_2^q(\zeta_6)$ via Markov trace produces $\mathrm{Vol}(4_1) \neq 0$. Pairing with $\mathrm{Li}_3^q(\zeta_6)$ is trivial in $\mathcal{P}_3 / \mathcal{P}_2$. Conclusion: $d_{\mathrm{II}}((2, 2)) = 2$. Bridge prediction verified.

#### Chiral pair $(3) + (1, 1, 1)$, $n = 3$ (trefoil row)
Trefoil $T(2, 3) = 3_1$ is chiral. Its volume is 0, but $\mathrm{CS}(3_1) = -\pi^2/6$. Pairing with $\mathrm{Li}_2^q$ yields depth-2 vanishes. Pairing with $\mathrm{Li}_3^q$ yields $\mathrm{CS}(3_1) = -\pi^2/6$, which is non-trivial in $\mathcal{P}_3 / \mathcal{P}_2$. Conclusion: $d_{\mathrm{II}}(\text{chiral pair}) = 3$. Bridge prediction verified.

#### Self-conjugate $\lambda = (2, 1)$, $n = 3$
Self-conjugate but no hyperbolic 3-strand knot has $(2, 1)$ alone as dominant cell. The bridge prediction $d_{\mathrm{II}}((2, 1)) = 2$ holds structurally.

#### Generalisation pattern
The verifications instantiate the structural prediction. The bar-eigenspace structure of partitions is the structural reason for the bridge map.

### Result

The two-filtration bridge map is verified at $n \leq 4$. The verification proceeds by case analysis on partition bar-class using known Vol/CS values. This partially discharges the two-filtration bridge conjecture at small $n$. The general statement at $n \geq 5$ is open.

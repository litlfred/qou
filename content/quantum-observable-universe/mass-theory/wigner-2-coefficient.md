*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
*For any self-conjugate partition $\lambda = \lambda'$ of $k$,
the per-generator trace in the Hoefsmit seminormal representation
satisfies*

$$
  \frac{\mathrm{tr}(\sigma_g^{(\lambda)})}{\dim(\lambda)}
  = \frac{h}{2}
  = \frac{q - q^{-1}}{2}
$$

*for every generator $g = 1, \ldots, k{-}1$.  Consequently, the
BW coefficient ([shadow price](#prop:mass-coefficient-shadow-price))
for $\lambda$ is*

$$
  C_\lambda = w_\lambda \cdot \frac{h}{2}
  = \frac{\dim_q(\lambda)^2}{[k]_q!} \cdot \frac{q - q^{-1}}{2}
$$

*In particular, for $\lambda = [3,2,1] \vdash 6$:*

$$
  C_{[3,2,1]}
  = \frac{[2]_q\,[4]_q\,[6]_q \cdot h}
         {2\,[3]_q^2\,[5]_q}
$$

*Proof.*
The argument has three steps: a pairing identity, a counting
argument, and an algebraic simplification.

**Step 1 (Paired sum identity).**
In the [seminormal form](#prop:hoefsmit-seminormal-form), the
diagonal entry for standard tableau $T$ at generator $\sigma_g$
is $a_\rho = h/(1 - q^{-2\rho})$ where
$\rho = c(T, g{+}1) - c(T, g)$ is the axial distance (difference
of contents of the cells containing entries $g{+}1$ and $g$).

For any $\rho \neq 0$:

$$
  a_\rho + a_{-\rho}
  = \frac{h}{1 - q^{-2\rho}} + \frac{h}{1 - q^{2\rho}}
  = h \cdot \frac{(1 - q^{2\rho}) + (1 - q^{-2\rho})}
              {(1 - q^{-2\rho})(1 - q^{2\rho})}
  = h \cdot \frac{2 - q^{2\rho} - q^{-2\rho}}
              {1 - q^{2\rho} - q^{-2\rho} + 1}
  = h
$$

since numerator and denominator are both $2 - (q^{2\rho} + q^{-2\rho})$.

**Step 2 (Conjugation pairing).**
Let $\lambda = \lambda'$ be self-conjugate.  The transposition of
the Young diagram (reflecting across the main diagonal) induces an
involution $T \mapsto T^\vee$ on the set of standard Young tableaux
of shape $\lambda$.  Under this involution:

- The cell of entry $m$ in $T^\vee$ has content $-c(T, m)$
  (reflection swaps row and column).
- Therefore $\rho(T^\vee, g) = -\rho(T, g)$ for every generator $g$.
- Since $\lambda$ is self-conjugate, $T^\vee$ is again a valid SYT
  of shape $\lambda$.
- The involution is fixed-point-free on axes: $\rho(T,g) \neq 0$
  implies $T^\vee \neq T$ in the relevant entry positions.

The $\dim(\lambda)$ tableaux pair into $\dim(\lambda)/2$ conjugate
pairs $\{T, T^\vee\}$.

**Step 3 (Trace computation).**
The trace of $\sigma_g$ in the seminormal basis is the sum of all
diagonal entries:

$$
  \mathrm{tr}(\sigma_g^{(\lambda)})
  = \sum_{T} a_{\rho(T,g)}
  = \sum_{\{T, T^\vee\}} \bigl(a_{\rho(T,g)} + a_{-\rho(T,g)}\bigr)
  = \sum_{\{T, T^\vee\}} h
  = \frac{\dim(\lambda)}{2} \cdot h
$$

Dividing by $\dim(\lambda)$:

$$
  \frac{\mathrm{tr}(\sigma_g^{(\lambda)})}{\dim(\lambda)}
  = \frac{h}{2}
$$

This is independent of $g$ (since all generators are conjugate in
$S_k$, and the trace is conjugation-invariant).

**Corollary (BW coefficient).**
By the [shadow price proposition](#prop:mass-coefficient-shadow-price),
$C_\lambda = w_\lambda \cdot \mathrm{tr}(\sigma_g)/\dim$.
Substituting $\mathrm{tr}/\dim = h/2$:

$$
  C_\lambda = \frac{\dim_q(\lambda)^2}{[k]_q!} \cdot \frac{h}{2}
$$

For $\lambda = [3,2,1] \vdash 6$, the hook lengths are
$\{5, 3, 1, 3, 1, 1\}$, giving $\dim_q = [6]_q!/([5]_q [3]_q^2)
= [2]_q [4]_q [6]_q / [3]_q$.  Therefore:

$$
  C_{[3,2,1]}
  = \frac{[2]_q^2 [4]_q^2 [6]_q^2}{[3]_q^2 \cdot [6]_q!}
    \cdot \frac{h}{2}
  = \frac{[2]_q [4]_q [6]_q \cdot h}{2\,[3]_q^3\,[5]_q}
$$

$\square$

**Proposition (explicit formula for the central primitive
idempotents $e_\lambda$ via Lagrange interpolation in Murphy elements).**

*Let $H_n(q)$ be the Iwahori–Hecke algebra over $R$ at generic
$q$, with Jucys–Murphy elements
$\{J_1, \ldots, J_n\} \subset H_n(q)$ as in
[`prop:jucys-murphy-central-elements-qou`](#prop:jucys-murphy-central-elements-qou).
The JM elements pairwise commute and act diagonally on the Hoefsmit
seminormal basis: $J_k \cdot v_T = c_T(k; q) \cdot v_T$ for any
standard Young tableau $T$ of shape $\lambda \vdash n$, where*

$$
  c_T(k; q) \;=\; q^{\,2(j(k) - i(k))}
$$

*is the **$q$-content** of the box of $T$ containing $k$
($i(k), j(k)$ are its row and column indices,
[`prop:hoefsmit-seminormal-form`](#prop:hoefsmit-seminormal-form)).*

*The central primitive idempotent $e_\lambda \in Z(H_n(q))$
projecting onto the $\lambda$-Wedderburn block
([`prop:wedderburn-weight-canonical`](#prop:wedderburn-weight-canonical))
has the explicit formula:*

$$
  \boxed{\;
    e_\lambda \;=\; \sum_{T \in \mathrm{SYT}(\lambda)}
    \prod_{k=1}^{n}
    \prod_{\substack{c \in \mathrm{C}(n) \\ c \neq c(T(k); q)}}
    \frac{J_k - c}{c(T(k); q) - c},
  \;}
$$

*where $\mathrm{C}(n) := \{c(\square; q) : \square \in \mu,\; \mu \vdash n\}$
is the set of distinct $q$-contents arising across **every** partition
$\mu \vdash n$ (not only the cells of $\lambda$).  The product over $c$
ranges over $\mathrm{C}(n)$ excluding the eigenvalue $c(T(k); q)$
assigned by tableau $T$. Each factor is
a Lagrange-interpolation projector onto the eigenspace where $J_k$
has eigenvalue $c(T(k); q)$. Together with
[`prop:jucys-murphy-central-elements-qou`](#prop:jucys-murphy-central-elements-qou)
this gives a complete explicit construction of $Z(H_n(q))$.*

> **Scope correction note.** Earlier versions of this
> proposition ranged the inner Lagrange product over cells of $\lambda$
> only (i.e., $\square \in \lambda$).  With that scope, the off-block
> projection does NOT vanish: the JM eigenvalue $q^{2c(T'(k))}$ for
> $T' \in \mathrm{SYT}(\mu \neq \lambda)$ may not lie in
> $\{c(\square; q) : \square \in \lambda\}$, so the Lagrange factor
> fails to kill that direction.  The corrected scope above ranges
> over $\mathrm{C}(n)$ (the union of contents across every $\mu$),
> which is exactly the candidate set of joint JM eigenvalues across
> all Wedderburn blocks.  Numerically verified to $\sim 10^{-50}$ in
> [`explicit-central-idempotent-probe.witness.json`](../../../computations/probes/explicit-central-idempotent-probe.witness.json):
> own-block residue $0$, off-block residue $0$, completeness
> residue $0$ under the corrected scope; literal-scope off-block
> residue $\approx 32$ at $q_0$ for $n = 3$.

### Cross-checks

1. **Sum-to-identity.** $\sum_{\lambda \vdash n} e_\lambda = 1
   \in H_n(q)$ (completeness of partition decomposition).
2. **Orthogonality.** $e_\lambda e_\mu = \delta_{\lambda \mu} e_\lambda$
   (Lagrange interpolation in commuting variables).
3. **Self-adjointness for self-conjugate $\lambda$.** When
   $\lambda = \lambda'$ (transpose), every box $\square \in \lambda$
   has a partner $\square'$ with $c(\square'; q) = c(\square; q^{-1}) =
   *(c(\square; q))$, so the product is bar-fixed term-by-term:
   $* (e_\lambda) = e_\lambda$.
4. **Bar-pairing for chiral $\lambda$.** When $\lambda \neq \lambda'$,
   $* (e_\lambda) = e_{\lambda'}$, and the sum $e_\lambda + e_{\lambda'}$
   is bar-fixed.

### Examples for small $n$

| $n$ | $\lambda$ | bar-class | $e_\lambda$ structure |
|---|---|---|---|
| 2 | $(2)$ | self-conjugate | $\frac{L_2 - (-q^{-2})}{q^2 - (-q^{-2})} = \frac{q^{-1}\sigma_1 + 1}{q + q^{-1}}$ |
| 2 | $(1,1)$ | self-conjugate | $\frac{L_2 - q^2}{(-q^{-2}) - q^2} = \frac{q\sigma_1^{-1} - 1}{-q - q^{-1}}$ (sign-twisted) |
| 3 | $(3)$ | chiral pair w/ $(1,1,1)$ | symmetriser, $q$-deformed |
| 3 | $(2,1)$ | self-conjugate | standard 2D rep idempotent |
| 4 | $(2,2)$ | **self-conjugate** | bar-fixed; *witnesses Vol(4_1)* via depth-2 pairing with $\mathrm{Li}_2^q(\zeta_6)$ |

### Significance

$e_\lambda$ is the **explicit, computable, named generator** of
the period class associated with cell $\lambda$. Combined with
[`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
and [`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic):

$$
  \tau_{\mathrm{arch}}\bigl( e_\lambda \cdot \mathrm{Li}_2^q(z) \bigr)
  \;\in\;
  \mathcal{P}_2 / \mathcal{P}_1
$$

is a Bloch-regulator class, computable to arbitrary precision via
the Murphy-element formula above. For the figure-8 knot ($\lambda
= (2,2)$, $z = \zeta_6$):

$$
  \tau_{\mathrm{arch}}\bigl( e_{(2,2)} \cdot \mathrm{Li}_2^q(\zeta_6) \bigr)
  \;=\; 2\,\mathrm{Cl}_2(\pi/3)
  \;=\; \mathrm{Vol}(S^3 \setminus 4_1)
$$

(verified numerically in
[`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness)).

### Provenance

The Murphy-element diagonalisation of $Z(H_n(q))$ goes back to
Murphy 1981 (symmetric-group case) and Dipper–James 1986
(Hecke-algebra case). The $q$-content formula is standard. The
Lagrange-interpolation form is the cleanest computable expression
and is what implementations of $H_n(q)$ projectors use in practice
(e.g. SageMath's `IwahoriHeckeAlgebra`, the `pyhecke-native` module
in this repo).

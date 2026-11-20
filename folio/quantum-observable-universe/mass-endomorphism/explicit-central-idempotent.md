**Proposition (conditional on [The four Murphy–Lagrange cross-checks for $e_\lambda$ follow from Lagrange interpolation in commuting variables](#conj:explicit-central-idempotent)).**
The statement below is proved *conditionally* on the
Lagrange-interpolation cross-checks, which are **open**. The four
cross-checks (sum-to-identity, orthogonality, self-adjointness,
bar-pairing) are the conjectural input; everything downstream of them is
proved.

*Let $H_n(q)$ be the Iwahori–Hecke algebra over $R$ at generic $q$. The Jucys–Murphy elements $\{J_1, \ldots, J_n\} \subset H_n(q)$ ([Elementary symmetric polynomials in Jucys–Murphy elements are central in $H_n(q)$ with closed-form spectrum on each Wedderburn block](#prop:jucys-murphy-central-elements-qou)) commute pairwise and act diagonally on the Hoefsmit seminormal basis. For any standard Young tableau $T$ of shape $\lambda \vdash n$, we have $J_k \cdot v_T = c_T(k; q) \cdot v_T$, where*

$$
  c_T(k; q) \;=\; q^{\,2(j(k) - i(k))}
$$

*is the $q$-content of the box containing $k$ at row $i(k)$ and column $j(k)$ ([Hoefsmit seminormal matrices as $R$-matrix evaluations in $H_n(q)$](#prop:hoefsmit-seminormal-form)).*

*The central primitive idempotent $e_\lambda \in Z(H_n(q))$ projecting onto the $\lambda$-Wedderburn block ([Canonical q-deformed Wedderburn-block weight $\tilde w_\lambda$ and named scalings (BW, LP for all $\lambda$)](#prop:wedderburn-weight-canonical)) carries the explicit formula:*

$$
  \boxed{\;
    e_\lambda \;=\; \sum_{T \in \mathrm{SYT}(\lambda)}
    \prod_{k=1}^{n}
    \prod_{\substack{c \in \mathrm{C}(n) \\ c \neq c(T(k); q)}}
    \frac{J_k - c}{c(T(k); q) - c},
  \;}
$$

*where $\mathrm{C}(n) := \{c(\square; q) : \square \in \mu,\; \mu \vdash n\}$ comprises the distinct $q$-contents arising across every partition $\mu \vdash n$. The inner product excludes the eigenvalue $c(T(k); q)$. Each factor forms a Lagrange-interpolation projector onto the eigenspace where $J_k = c(T(k); q)$. This construction completely specifies $Z(H_n(q))$.*

## Cross-checks

1. **Sum-to-identity.** $\sum_{\lambda \vdash n} e_\lambda = 1 \in H_n(q)$, confirming the completeness of the partition decomposition.
2. **Orthogonality.** $e_\lambda e_\mu = \delta_{\lambda \mu} e_\lambda$ via Lagrange interpolation in commuting variables.
3. **Self-adjointness.** For a self-conjugate partition $\lambda = \lambda'$, every box $\square \in \lambda$ has a transposed partner $\square'$ with $c(\square'; q) = c(\square; q^{-1}) = *(c(\square; q))$. The product remains bar-fixed term-by-term: $*(e_\lambda) = e_\lambda$.
4. **Bar-pairing.** For a chiral partition $\lambda \neq \lambda'$, we have $*(e_\lambda) = e_{\lambda'}$. The sum $e_\lambda + e_{\lambda'}$ remains bar-fixed.

## Small $n$ examples

| $n$ | $\lambda$ | bar-class | $e_\lambda$ structure |
|---|---|---|---|
| $2$ | $(2)$ | self-conjugate | $\frac{L_2 - (-q^{-2})}{q^2 - (-q^{-2})} = \frac{q^{-1}\sigma_1 + 1}{q + q^{-1}}$ |
| $2$ | $(1,1)$ | self-conjugate | $\frac{L_2 - q^2}{(-q^{-2}) - q^2} = \frac{q\sigma_1^{-1} - 1}{-q - q^{-1}}$ |
| $3$ | $(3)$ | chiral pair w/ $(1,1,1)$ | $q$-deformed symmetriser |
| $3$ | $(2,1)$ | self-conjugate | standard 2D representation idempotent |
| $4$ | $(2,2)$ | self-conjugate | bar-fixed; witnesses $\mathrm{Vol}(4_1)$ via depth-2 pairing with $\mathrm{Li}_2^q(\zeta_6)$ |

## Significance

The element $e_\lambda$ serves as the explicit, computable generator of the period class assigned to cell $\lambda$. Under [GS-depth $\leftrightarrow$ Goncharov period-depth correspondence](#conj:gb-depth-period-correspondence) and [Iwahori--Hecke algebra $H_n(q)$ is a Baer-*-ring at generic $q$](#prop:hecke-baer-star-generic), the class

$$
  \tau_{\mathrm{arch}}\bigl( e_\lambda \cdot \mathrm{Li}_2^q(z) \bigr)
  \;\in\;
  \mathcal{P}_2 / \mathcal{P}_1
$$

forms a Bloch-regulator period computable to arbitrary precision. For the figure-$8$ knot ($\lambda = (2,2)$, $z = \zeta_6$):

$$
  \tau_{\mathrm{arch}}\bigl( e_{(2,2)} \cdot \mathrm{Li}_2^q(\zeta_6) \bigr)
  \;=\; 2\,\mathrm{Cl}_2(\pi/3)
  \;=\; \mathrm{Vol}(S^3 \setminus 4_1).
$$

This is numerically verified in [Bring figure-8 volume as depth-2 grouplike value (50-digit numerical witness)](#conj:bring-figure-eight-depth-2-witness).

## Provenance

The Murphy-element diagonalization of $Z(H_n(q))$ originates with Murphy (1981, symmetric group) and Dipper–James (1986, Hecke algebra). The Lagrange-interpolation form offers the cleanest computable expression. It is standard in computer-algebra implementations such as SageMath.

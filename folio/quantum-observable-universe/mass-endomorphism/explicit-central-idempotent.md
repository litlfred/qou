**Proposition.** *Let $H_n(q)$ be the Iwahori–Hecke algebra over a characteristic-$0$ field $K$ at generic $q \in K^\times$ (not a root of unity). The multiplicative Jucys–Murphy elements $\{J_1, \ldots, J_n\} \subset H_n(q)$ ([Jucys–Murphy central elements](#prop:jucys-murphy-central-elements-qou)) commute pairwise and act diagonally on the Hoefsmit seminormal basis: for every standard Young tableau $T$ of shape $\lambda \vdash n$, $J_k \cdot v_T = c_T(k; q) \cdot v_T$, where*

$$
  c_T(k; q) \;=\; q^{\,2(j(k) - i(k))}
$$

*is the $q$-content of the cell containing $k$ at row $i(k)$ and column $j(k)$ ([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)).*

*The central primitive idempotent $e_\lambda \in Z(H_n(q))$ projecting onto the $\lambda$-Wedderburn block ([canonical Wedderburn weight](#prop:wedderburn-weight-canonical)) is given explicitly by*

$$
  \boxed{\;
    e_\lambda \;=\; \sum_{T \in \mathrm{SYT}(\lambda)}
    \prod_{k=1}^{n}
    \prod_{\substack{c \in \mathrm{C}(n) \\ c \neq c_T(k; q)}}
    \frac{J_k - c}{c_T(k; q) - c},
  \;}
$$

*where $\mathrm{C}(n) := \{c(\square; q) : \square \in \mu,\; \mu \vdash n\}$ is the set of distinct $q$-contents occurring across all partitions $\mu \vdash n$. The family $\{e_\lambda\}_{\lambda \vdash n}$ lies in $Z(H_n(q))$ and satisfies $\sum_{\lambda \vdash n} e_\lambda = 1$ and $e_\lambda e_\mu = \delta_{\lambda\mu}\, e_\lambda$.*

*Proof.* At generic $q \in K^\times$, $q^{2d} \neq 1$ for every nonzero integer $d$, so $d \mapsto q^{2d}$ is injective on integer contents $[-n+1, n-1]$. Because the integer content tuple $(j(1) - i(1), \ldots, j(n) - i(n))$ determines both the Young diagram $\lambda$ (by diagonal cell counts) and the standard tableau $T \in \mathrm{SYT}(\lambda)$ \cite{murphy1981,ram1997}, the multiplicative $q$-content tuples $(c_T(1; q), \ldots, c_T(n; q))$ pairwise separate the union $\bigsqcup_{\mu \vdash n} \mathrm{SYT}(\mu)$. Under the Wedderburn product map $\rho = \prod_{\mu \vdash n} \rho_\mu \colon H_n(q) \xrightarrow{\sim} \prod_{\mu \vdash n} M_{f^\mu}(K)$, [the Murphy–Lagrange interpolation lemma](#lem:explicit-central-idempotent-lagrange) evaluates the $T$-summand of $\rho(e_\lambda)$ to the diagonal matrix unit $E^\lambda_{T,T}$, so summing over $T \in \mathrm{SYT}(\lambda)$ gives $\rho(e_\lambda) = (0, \ldots, I_{f^\lambda}, \ldots, 0)$ \cite{dipper-james1986}. Pulling back along the algebra isomorphism $\rho$ yields $e_\lambda x = x e_\lambda$ for all $x \in H_n(q)$, $\sum_{\lambda \vdash n} e_\lambda = 1$, and $e_\lambda e_\mu = \delta_{\lambda\mu}\, e_\lambda$. $\square$

## Cross-checks

1. **Sum-to-identity.** $\sum_{\lambda \vdash n} e_\lambda = 1 \in H_n(q)$, exhausting the Wedderburn block decomposition.
2. **Orthogonality and idempotency.** $e_\lambda e_\mu = \delta_{\lambda\mu}\, e_\lambda$, and in particular $e_\lambda^2 = e_\lambda$.
3. **Self-conjugate invariance.** Every cell $\square = (i, j)$ and its transpose $\square' = (j, i)$ satisfy $c(\square'; q) = c(\square; q^{-1}) = c(\square; q)^{-1}$. Under the transposing involution $\# \colon \sigma_i \mapsto -\sigma_i^{-1}$ (which maps $J_k \mapsto J_k^{-1}$ at fixed $q$), every self-conjugate partition $\lambda = \lambda'$ satisfies $\#(e_\lambda) = e_\lambda$; under the Kazhdan–Lusztig bar involution $\sigma_i \mapsto \sigma_i^{-1}$, $q \mapsto q^{-1}$ (which inverts both $J_k$ and $c_T(k; q)$ simultaneously), every $e_\lambda$ is bar-fixed.
4. **Transpose pairing.** For a chiral pair $\lambda \neq \lambda'$, the transposing involution satisfies $\#(e_\lambda) = e_{\lambda'}$ (matching content inversion $c_T(k; q) \mapsto c_T(k; q^{-1}) = c_{T'}(k; q)$ at fixed $J_k$), so $e_\lambda + e_{\lambda'}$ is invariant under both involutions.

## Small $n$ examples

| $n$ | $\lambda$ | transpose class | $e_\lambda$ structure |
|---|---|---|---|
| $2$ | $(2)$ | chiral pair w/ $(1,1)$ | $\frac{J_2 - q^{-2}}{q^2 - q^{-2}} = \frac{\sigma_1 + q^{-1}}{q + q^{-1}}$ |
| $2$ | $(1,1)$ | chiral pair w/ $(2)$ | $\frac{J_2 - q^2}{q^{-2} - q^2} = \frac{-\sigma_1 + q}{q + q^{-1}}$ |
| $3$ | $(3)$ | chiral pair w/ $(1,1,1)$ | $q$-deformed symmetriser |
| $3$ | $(2,1)$ | self-conjugate | standard $2$-dimensional representation idempotent |
| $4$ | $(2,2)$ | self-conjugate | transpose-fixed; witnesses $\mathrm{Vol}(4_1)$ via depth-$2$ pairing with $\mathrm{Li}_2^q(\zeta_6)$ |

## Significance

The element $e_\lambda$ serves as the explicit, computable generator of the period class assigned to cell $\lambda$. Under [the Grothendieck–Brieskorn depth–period correspondence](#conj:gb-depth-period-correspondence) and [the generic Hecke Baer $*$-structure](#prop:hecke-baer-star-generic), the class

$$
  \tau_{\mathrm{arch}}\bigl( e_\lambda \cdot \mathrm{Li}_2^q(z) \bigr)
  \;\in\;
  \mathcal{P}_2 / \mathcal{P}_1
$$

forms a Bloch-regulator period computable to arbitrary precision. For the figure-$8$ knot ($\lambda = (2,2)$, $z = \zeta_6$):

$$
  \tau_{\mathrm{arch}}\bigl( e_{(2,2)} \cdot \mathrm{Li}_2^q(\zeta_6) \bigr)
  \;=\; 2\,\mathrm{Cl}_2(\pi/3)
  \;=\; \mathrm{Vol}(S^3 \setminus 4_1),
$$

matching the numerical evaluation in [the Bring figure-eight depth-2 witness](#conj:bring-figure-eight-depth-2-witness).

## Provenance

The Murphy-element diagonalization of $Z(H_n(q))$ originates with Murphy \cite{murphy1981} for symmetric groups and Dipper–James \cite{dipper-james1986} and Ram \cite{ram1997} for Iwahori–Hecke algebras.

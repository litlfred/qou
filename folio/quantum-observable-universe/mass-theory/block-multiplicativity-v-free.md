**Conjecture (Block-Multiplicativity of $\hat V^{\text{free}}$ on the Disjoint Hecke Product).**

*Let $\mathcal{B}_K^{\mathrm{vac}} = \mathcal{B}_p^{(1)} \cdots \mathcal{B}_n^{(N)} \in H_{3A}(q)$ denote the constituent vacuum—the disjoint Hecke product of $Z$ proton braids and $N$ neutron braids on disjoint 3-strand blocks, with no interface crossings. For each generator $\sigma_g$ acting only inside the $k$-th nucleon block, the Wedderburn-weighted per-generator character ratio*

$$
  \hat V^{(3A)}_g(\mathcal{B}_K^{\mathrm{vac}})
   :=
  \sum_{\lambda \vdash 3A}
    \frac{\dim_q^2(\lambda)}{[3A]_q!} \cdot
    \frac{\chi^\lambda(W_g)}{\dim(\lambda)}
$$

*is independent of $A$. It depends only on the flavor of the $k$-th nucleon and on the local position $g \bmod 3 \in \{0, 1\}$ within the block, not on the total strand count $3A$ or the flavor content of the other blocks.*

### Empirical verification

Computed via the canonical formalism on D, T, ${}^{3}$He at $H_6, H_9, H_9$ respectively (50 dps):

| atom | proton block (gens 0, 1) | neutron block | matches D? |
|---|---|---|:-:|
| D (A=2) | $V_0 = 0.6714$, $V_1 = 1.0551$ | $V_0 = 0.5517$, $V_1 = 1.0884$ | — |
| T (A=3) | same | same | yes |
| ${}^{3}$He (A=3) | same | same | yes |

Block-multiplicativity holds exactly to 4 digits. The block factors evaluate to $v_p = 0.7084$ and $v_n = 0.6005$.

### Classical-limit proof sketch ($q \to 1$)

When $\sigma_g$ acts inside the first 3-strand block, the symmetric-group character factors via the Littlewood–Richardson restriction rule. At $q = 1$ the Wedderburn weight is the classical Plancherel measure. By the classical Plancherel duality identity, the ratio simplifies to:

$$
  \hat V^{(3A)}_g
   =
  \frac{1}{6}
  \sum_{\mu \vdash 3} \chi_\mu(\sigma_g) \dim(\mu).
$$

The right-hand side depends only on the $H_3$ character data of $\sigma_g$, proving the classical limit.

### $q$-deformation: the open structural step

For $q \ne 1$, the LR identity generalises to a $q$-Schur duality. Conjecturally, this identity yields an $A$-independent residual after factoring out $[3A]_q! / [3A-3]_q!$. A structural proof via the $q$-Schur–Weyl duality remains pending.

### Significance

Block-multiplicativity reduces the $T_1^{\text{free}}$ term of the mass-endomorphism tower from an $O(p(3A) \cdot 3A^3)$ character-sum compute to an $O(1)$ exponentiation: $T_1^{\text{free}}(K) = v_p^Z \cdot v_n^N$. Combined with structural identities for interface generators, this yields a closed-form formula computable in microseconds for any $(Z, N)$.

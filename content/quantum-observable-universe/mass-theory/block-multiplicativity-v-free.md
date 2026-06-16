**Conjecture (Block-Multiplicativity of $\hat V^{\text{free}}$ on the
Disjoint Hecke Product).**

*Let $\mathcal{B}_K^{\mathrm{vac}} = \mathcal{B}_p^{(1)} \cdots \mathcal{B}_n^{(N)} \in
H_{3A}(q)$ denote the **constituent vacuum** — the disjoint Hecke
product of $Z$ proton braids and $N$ neutron braids on disjoint
3-strand blocks, with no interface crossings
(`def:ew-interface-knot`). For each
generator $\sigma_g$ acting non-by definition only inside the $k$-th
nucleon block, the Wedderburn-weighted per-generator character ratio*

$$
  \hat V^{(3A)}_g(\mathcal{B}_K^{\mathrm{vac}})
   :=
  \sum_{\lambda \vdash 3A}
    \frac{\dim_q^2(\lambda)}{[3A]_q!} \cdot
    \frac{\chi^\lambda(W_g)}{\dim(\lambda)}
$$

*is **independent of $A$**: it depends only on the flavor of the
$k$-th nucleon (proton vs neutron) and on the local position
$g \bmod 3 \in \{0, 1\}$ within the block, not on the total strand
count $3A$ or the flavor content of the other blocks.*

### Empirical verification

Computed via [`per_generator_V_hat_3A`](https://github.com/litlfred/qou/blob/claude/log-delta-categorical-derivation/computations/mass_at_3A_proper.py)
on D, T, ${}^{3}$He at $H_6, H_9, H_9$ respectively (50 dps), as recorded in
[`binding-via-interface-knot.witness.json`](https://github.com/litlfred/qou/blob/claude/log-delta-categorical-derivation/computations/binding-via-interface-knot.witness.json):

| atom | proton block (gens 0, 1) | neutron block | matches D? |
|---|---|---|:-:|
| D (A=2) | $V_0 = 0.6714$, $V_1 = 1.0551$ | $V_0 = 0.5517$, $V_1 = 1.0884$ | — |
| T (A=3) | same | same | ✓ |
| ${}^{3}$He (A=3) | same | same | ✓ |

Block-multiplicativity holds **exactly** to 4 digits, the resolution
of the recorded witness. The block factors evaluate to

$$
  v_p := \hat V^{p}_0 \cdot \hat V^{p}_1 = 0.7084, \qquad
  v_n := \hat V^{n}_0 \cdot \hat V^{n}_1 = 0.6005.
$$

### Classical-limit proof sketch ($q \to 1$)

When $\sigma_g$ acts inside the first 3-strand block (positions $1, 2, 3$),
the symmetric-group character factors via the Littlewood–Richardson
restriction rule:

$$
  \chi_\lambda(\sigma_g)
   =
  \sum_{\mu \vdash 3, \nu \vdash 3A-3}
    c_{\mu, \nu}^{\lambda} \cdot
    \chi_\mu(\sigma_g) \cdot \dim(\nu).
$$

At $q = 1$ the Wedderburn weight $w_\lambda = \dim^2(\lambda) / (3A)!$ is
the classical Plancherel measure. Plugging in:

$$
  \hat V^{(3A)}_g
   =
  \frac{1}{(3A)!} \sum_{\mu, \nu}
    \chi_\mu(\sigma_g) \dim(\nu)
    \sum_\lambda c_{\mu, \nu}^\lambda \dim(\lambda).
$$

By the classical **Plancherel duality identity**
$\sum_\lambda c_{\mu,\nu}^\lambda \dim(\lambda)
 = \binom{3A}{3} \dim(\mu) \dim(\nu)$, this simplifies to

$$
  \hat V^{(3A)}_g
   =
  \binom{3A}{3} \frac{(3A-3)!}{(3A)!}
  \cdot
  \sum_{\mu \vdash 3} \chi_\mu(\sigma_g) \dim(\mu)
   =
  \frac{1}{6}
  \sum_{\mu \vdash 3} \chi_\mu(\sigma_g) \dim(\mu),
$$

using $\binom{3A}{3} \frac{(3A-3)!}{(3A)!} = \frac{1}{6} = \frac{1}{3!}$.
The right-hand side **depends only on the H_3 character data** of
$\sigma_g$, hence is $A$-independent. This proves the classical
limit ($q = 1$) of the conjecture.

### $q$-deformation: the open structural step

For $q \ne 1$, the q-deformed weight is $\tilde w_\lambda = \dim_q^2(\lambda)/[3A]_q!$
and the LR identity generalises to a **q-Schur duality**

$$
  \sum_\lambda c_{\mu, \nu}^\lambda \dim_q^2(\lambda) / \dim(\lambda)
   \stackrel{?}{=}
  \binom{3A}{3}_q \cdot (\text{factor depending only on } \mu, \nu),
$$

where $\binom{3A}{3}_q$ is the q-binomial. The conjecture is that this
identity yields an $A$-independent residual after factoring out
$[3A]_q! / [3A-3]_q!$. Empirically it holds to 4 digits at $q_0 \approx
1.11$ across $A \in \{2, 3\}$; structural proof via the q-Schur–Weyl
duality for $H_n(q)$ acting on tensor products of $\mathrm{U}_q(\mathfrak{sl}_n)$-
modules is pending.

### Why this matters

Block-multiplicativity reduces the $T_1^{\text{free}}$ term of the
mass-endomorphism tower
([`prop:mass-endomorphism-tower`](#prop:mass-endomorphism-tower)) from
an $O(p(3A) \cdot 3A^3)$ character-sum compute to an $O(1)$
exponentiation:

$$
  T_1^{\text{free}}(K) = v_p^Z \cdot v_n^N.
$$

Together with the structural identities
$T_1^{\text{atom}}(K) = 0$ (interface generator zeros the product)
and

$$
  T_2^{\text{diff}}(K) = (Z-1) \delta_{pp} + (N-1) \delta_{nn} + \delta_{pn},
   \quad
  \delta_{XY} = \mathrm{Li}_2^q(1) - \mathrm{Li}_2^q(|\hat V^{XY}_{\text{inter}}|),
$$

this gives a **closed-form $B^{(1)}_{\text{dim}}(Z, N)$** computable
in microseconds for any $(Z, N)$ — bypassing the $H_{3A}$ character
sum entirely beyond the one-time $H_6$ calibration of
$\{v_p, v_n, |\hat V^{pp}_{\text{inter}}|, |\hat V^{nn}_{\text{inter}}|\}$.

[`binding_block_multiplicative.py`](https://github.com/litlfred/qou/blob/claude/log-delta-categorical-derivation/computations/binding_block_multiplicative.py)
applies this to 16 atoms (D $\to$ ${}^{56}$Fe) in $< 1$ s total, all signs correct;
finer agreement awaits the $T_3$ pair-term closure (see
[`prop:mass-endomorphism-tower`](#prop:mass-endomorphism-tower)
§T_3 deferral).

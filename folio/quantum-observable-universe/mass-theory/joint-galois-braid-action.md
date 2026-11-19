**Conjecture (joint motivic-Galois $\times$ braid-group action on the
bi-filtration).**

*Let $\mathcal{H}_q^{(n, K)}$ be the knot-indexed bi-filtration
([$H_n(q)$ bi filtration definition](#def:hq-bi-filtration)). Two groups act
on it by symmetry:*

- *the **motivic Galois group** $G_{\mathrm{mot}}$ acts on the
 depth axis, permuting Goncharov period classes
 $\mathcal{P}_n / \mathcal{P}_{n-1}$ under $\tau_{\mathrm{arch}}$
 (Kontsevich–Zagier 2001, Goncharov 2001);*
- *the **braid group** $B_{n_K}$ acts on the knot axis, permuting
 Wedderburn cells $e_{\lambda_K}$ via the standard
 representation on $H_{n_K}(q)$.*

*Conjectural joint structure: these two actions extend to a joint
action of a semi-direct product $G_{\mathrm{mot}} \rtimes B_{n_K}$
on $\mathcal{H}_q^{(n, K)}$, with the action on each axis being
**equivariant** with respect to the action on the other:*

$$
  \boxed{\;
    g_{\mathrm{mot}}(\beta \cdot \alpha)
    \;=\;
    \beta \cdot g_{\mathrm{mot}}(\alpha)
    \quad\text{for } \alpha \in \mathcal{H}_q^{(n, K)},\;
    g_{\mathrm{mot}} \in G_{\mathrm{mot}},\;
    \beta \in B_{n_K}.
  \;}
$$

*Equivalently: the motivic-Galois action commutes with the braid-
group action when restricted to the bi-filtration, and the joint
group $G_{\mathrm{mot}} \times B_{n_K}$ stabilises each
$\mathcal{H}_q^{(n, K)}$ stratum.*

### Structural motivation for the prediction

Three motivations:

1. **The depth axis is Galois-equivariant by construction.** Goncharov's
 motivic-Galois group acts accordingly on the period algebra
 $\mathcal{P}_*$, preserving the depth filtration. Pulled back via
 $\tau_{\mathrm{arch}}$, this gives an action on each $G^{(n)}(\mathcal{H}_q)$.

2. **The knot axis is braid-equivariant by construction.** The braid
 group $B_n$ acts on $H_n(q)$ via the standard half-twist generators
 $\sigma_i$, permuting Wedderburn cells via the Hoefsmit
 seminormal-form action. This descends to an action on
 $\mathcal{H}_q$ via Schur–Weyl.

3. **The two actions touch different parts of the structure.** Galois
 acts on $q$-coefficients (via $q \mapsto q^{-1}$ for the bar
 involution, or via cyclotomic Galois on $\zeta_n$); braid acts on
 the Hecke-element argument. These are **a priori orthogonal**,
 so commutativity is the natural conjecture.

### Equivalent statements

- The bi-filtration $\mathcal{H}_q^{(n, K)}$ is a **bi-graded
 $(G_{\mathrm{mot}} \times B_{n_K})$-module**.
- The composition map $\tau_{\mathrm{arch}} \circ (\beta \cdot -)$
 equals $(\beta \cdot -) \circ \tau_{\mathrm{arch}}$ on each
 stratum (with $\beta$ acting on the period side via its
 monodromy representation).
- The joint orbit of any $\alpha \in \mathcal{H}_q^{(n, K)}$ under
 $G_{\mathrm{mot}} \times B_{n_K}$ stays within $\mathcal{H}_q^{(n, K)}$.

### Concrete prediction at $(n, K) = (3, \zeta_5\text{-Bring})$

For the Bring depth-3 bi-filtration cell
([Bring trilogarithm depth 3 witness conjecture](#conj:bring-trilog-depth-3-witness)):

- $G_{\mathrm{mot}}$-action: cyclotomic Galois $\sigma_a \colon
  \zeta_5 \mapsto \zeta_5^a$ for $\gcd(a, 5) = 1$. Permutes
 $\{\mathrm{Li}_3(\zeta_5^k) : k = 1, 2, 3, 4\}$ as the
 $(\mathbb{Z}/5)^\times \cong \mathbb{Z}/4$ orbit.
- $B_n$-action (here $B_5$ via $S_5$ symmetry of Bring): permutes
 the same 4 values via the regular representation of $S_5$ on
 $\mathbb{Q}(\zeta_5)$.

**The conjecture predicts**: these two permutation actions
**commute**. canonical evidence: the orbit-sum
$\sum_{k=1}^4 \mathrm{Li}_3(\zeta_5^k) = -\frac{24}{25}\zeta(3)$
is *both* Galois-invariant (= cyclotomic Galois-trace) *and*
$S_5$-invariant (= regular-representation trace), so the joint-
invariant subspace contains $\zeta(3)$. Higher invariants would
test the joint commutativity sharply.

### Concrete prediction at $(n, K) = (2, 4_1)$

For the figure-8 ($\lambda_K = (2, 2)$ self-conjugate cell):

- $G_{\mathrm{mot}}$-action: bar involution $q \mapsto q^{-1}$.
 Fixes $e_{(2, 2)}$ since $(2, 2)$ is self-conjugate. acts as the identity
 on $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \in \mathcal{P}_2^+$.
- $B_3$-action (figure-8 is a 3-strand braid): the dihedral
 $D_3 = S_3$ symmetry of the braid acts on $e_{(2, 2)}$ by definition
 (since $(2, 2)$ is the unique self-conjugate cell of
 $H_3 \subset H_4$ structure).

Joint action stabilises the entire stratum by definition —
**consistent with the prediction** that the figure-8 is the
canonical fixed point for both groups in $\mathcal{H}_q^{(2, K)}$.
### Significance

If discharged, the joint action gives:

1. **Symmetry-organised period generation.** Periods at depth $n$
 for knot $K$ generate a $G_{\mathrm{mot}} \rtimes B_{n_K}$-module;
 the irreducible decomposition predicts which periods are
 independent vs forced by $q$-rational structure.
2. **Cross-axis dictionaries.** Galois orbits on $\mathcal{P}_n$
 correspond to braid orbits on cells: each pair $(g, \beta)$
 gives a relation among period values.
3. **Sharpness of the depth correspondence via representation theory.** The correspondence's
 sharpness condition (image generates $\mathcal{P}_n / \mathcal{P}_{n-1}$
 non-by definition) reduces to non-vanishing of certain
 $G_{\mathrm{mot}} \rtimes B_n$-invariants — a representation-
 theoretic question, much more tractable than
 transcendence-theoretic ones.

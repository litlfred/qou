**Definition.**
*Let $q$ be the braiding eigenvalue of $(\mathbf{C}, A, \tau)$. The **derived atom** $\mathcal{A}(Z, N)$ is the element of $H_A(q)$ obtained by the following six steps:*

1. ***Pair production.** Three independent 4-term photon collisions produce three quark--antiquark pairs per nucleon via the Hecke relation.*
2. ***Quark selection.** Select one quark from each pair. The remaining antiquarks either annihilate or form antinucleons.*
3. ***Borromean confinement.** The minimum-action operator $\mathcal{B}_3$ confines each triple of quarks. This yields pre-gluon NF elements in $H_3(q)$.*
4. ***Gluon stabilisation.** The confined nucleon is LP-unstable. The integer LP dual selects the minimum gluon. The stabilised nucleon NF elements are $\mathfrak{N}_k \in H_3(q)$.*
5. ***Nuclear assembly.** Inter-nucleon typed crossings in $H_A(q)$ link the $A = Z + N$ nucleons.*
6. ***Electron cloud.** Electromagnetic crossings link $Z$ electrons to the nucleus via Hopf links.*

## Inductive Gröbner--Shirshov reduction

For large $A$, the unreduced braid word has exponentially many terms. The Gröbner--Shirshov normal form is computed inductively. One reduces after each multiplication step, not at the end. Each intermediate result is in normal form. The total computation is polynomial in $A$.

## NF characterization

The derived atom $\mathcal{A}(Z, N)$ is a unique element of $H_A(q)$ in Gröbner--Shirshov normal form:

$$
  \mathcal{A}(Z, N)
  \;=\;
  \sum_{w \in \mathrm{NF}(B_A)}
  c_w(q, Z, N) \cdot w
$$

where $c_w \in \mathbb{Z}[q, q^{-1}]$ are Laurent polynomial coefficients.

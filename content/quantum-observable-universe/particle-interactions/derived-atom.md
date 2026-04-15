A **derived atom** $\mathcal{A}(Z, N)$ with atomic number $Z$ and
neutron number $N$ is the endpoint of the following categorical
construction.  No component is asserted — each step is derived from
the previous one via operations in $H_A(q)$ where $A = Z + N$.

## Construction

**Definition.**
*Let $q$ be the braiding eigenvalue of $(\mathbf{C}, A, \tau)$.
The **derived atom** $\mathcal{A}(Z, N)$ is the element of $H_A(q)$
obtained by the following five-step construction:*

**(i) Pair production.**
*For each nucleon $k \in \{1, \ldots, Z + N\}$, three independent
4-term photon collisions
$\gamma_{k,i} \cdot \gamma_{k,i}' \in H_3(q)$ ($i = 1,2,3$)
produce three quark--antiquark pairs via the Hecke relation
([Breit--Wheeler](#def:breit-wheeler-pair-production)).*

**(ii) Quark selection.**
*From each triple of pairs, select one quark per pair:*
- *Proton ($k \leq Z$): select $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$*
- *Neutron ($k > Z$): select $(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$*

*The remaining antiquarks either annihilate or form antinucleons.
Baryon number is conserved: $3 \times 0 = 1 + (-1)$.*

**(iii) Borromean confinement.**
*Each triple of quarks is confined by the minimum-action operator
$\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$
([confinement selection](#prop:confinement-operator-selection)),
yielding pre-gluon NF elements in $H_3(q)$.*

**(iii-b) Gluon stabilisation.**
*The confined nucleon $\mathcal{B}_3 \times \Delta_3$ is LP
unstable ([integer LP gluon](#prop:mass-endomorphism-tower)):
the $\gamma$ Frobenius channel violates positivity.
The integer LP dual selects the minimum gluon:*
- *Proton: $\sigma_0 \to \sigma_0$ ($2$ bare crossings, $11$ total)*
- *Neutron: $L_+ \to L_-$ ($4$ Hopf link crossings, $13$ total)*

*The gluon is required by LP stability at $q_0 \approx 1.110$
(the proton is stable without gluon only for $q < 1.104$).
The stabilised nucleon NF elements are
$\mathfrak{N}_k \in H_3(q)$.*

**(iv) Nuclear assembly.**
*The $A = Z + N$ nucleons are linked by inter-nucleon typed
crossings in $H_A(q)$:*

$$
  \mathcal{N}(Z, N)
  =
  \mathrm{NF}\!\left(
    \prod_{k=1}^{A} \mathfrak{N}_k
    \cdot
    \prod_{1 \leq i < j \leq A}
    C(\mathfrak{N}_i, \mathfrak{N}_j; \sigma_{\min(i-1, A-2)})
  \right)
$$

*where $C(\mathfrak{N}_i, \mathfrak{N}_j; \sigma_g)$ is the
inter-nucleon typed crossing:*
- *$p$-$p$: $\sigma_g$ (positive, eigenvalue $+q$)*
- *$n$-$n$: $\sigma_g - H_A$ (negative, eigenvalue $-q^{-1}$)*
- *$p$-$n$: $\sigma_g - \tfrac{1}{2}H_A$ (mixed)*

**(v) Electron cloud.**
*$Z$ electrons (trefoils $T_{2,3} = \sigma_0\sigma_1\sigma_0$)
are Hopf-linked to the nucleus via electromagnetic crossings
$\sigma_{g_e}$:*

$$
  \mathcal{A}(Z, N)
  =
  \mathrm{NF}\!\left(
    \mathcal{N}(Z, N)
    \cdot
    \prod_{e=1}^{Z}
    \sigma_{g_e} \cdot T_{2,3}
  \right)
$$

*where $g_e = (e - 1) \bmod 2$ alternates the generator to
distribute electrons across crossing planes.*

## Inductive Gröbner--Shirshov reduction

For large $A$, the unreduced braid word has exponentially many
terms.  The Gröbner--Shirshov normal form is computed **inductively**
— reduce after each multiplication step, not at the end:

$$
  \mathcal{N}_{\leq k+1}
  =
  \mathrm{NF}\bigl(
    \mathcal{N}_{\leq k}
    \cdot C(\mathfrak{N}_k, \mathfrak{N}_{k+1}; \sigma_g)
    \cdot \mathfrak{N}_{k+1}
  \bigr)
$$

Each intermediate result is in NF (at most $\binom{A-1}{k}$ terms
of length $\leq A - 1$), so the total computation is polynomial
in $A$ rather than exponential
([nuclear Gröbner reduction](#prop:nuclear-groebner-reduction)).

## NF characterization

The derived atom $\mathcal{A}(Z, N)$ is a unique element of
$H_A(q)$ in Gröbner--Shirshov normal form:

$$
  \mathcal{A}(Z, N)
  =
  \sum_{w \in \mathrm{NF}(B_A)}
  c_w(q, Z, N) \cdot w
$$

where $c_w \in \mathbb{Z}[q, q^{-1}]$ are Laurent polynomial
coefficients determined entirely by $q$, $Z$, and $N$.

**Witness**: `four-term-photon-to-atoms.witness.json`.

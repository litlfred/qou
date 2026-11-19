**Inductive Gröbner--Shirshov reduction.**

For the [derived atom](#def:derived-atom) at large $A$, the unreduced braid word has exponentially many terms. The Gröbner--Shirshov normal form is computed inductively. We reduce after each multiplication step, not at the end. Each intermediate result is in normal form. The total computation is polynomial in $A$.

**NF characterization.**

The derived atom $\mathcal{A}(Z, N)$ is a unique element of $H_A(q)$ in Gröbner--Shirshov normal form:

$$
  \mathcal{A}(Z, N)
  \;=\;
  \sum_{w \in \mathrm{NF}(B_A)}
  c_w(q, Z, N) \cdot w
$$

where $c_w \in \mathbb{Z}[q, q^{-1}]$ are Laurent polynomial coefficients.

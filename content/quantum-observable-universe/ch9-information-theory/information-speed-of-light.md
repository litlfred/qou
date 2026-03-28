In the quantum observable universe $(\mathbf{C}, \theta, G, \mathcal{S})$,
the **speed of light** is the maximum rate at which the $q$-connection
$\nabla_q$ can propagate a state change between adjacent fibres of
the $1$-jet bundle $J^1 \mathcal{S}_n$.

**Definition.**
Let $\mathcal{O}_x$ be a local observable supported on the fibre
above $x$, and let $\mathcal{O}_y$ be a local observable supported
on the fibre above $y$.  The *Lieb--Robinson velocity* of the
discrete Reeb dynamics is

$$
  c \;:=\;
  \sup \Bigl\{
    \frac{d(x,y)}{n \cdot \hbar_q}
    \;\Big|\;
    \bigl\lVert
      [\,\mathcal{O}_x(n),\, \mathcal{O}_y(0)\,]
    \bigr\rVert > \varepsilon
  \Bigr\},
$$

where $\mathcal{O}_x(n) = (\nabla_q)^n \mathcal{O}_x$ denotes the
observable after $n$ discrete $f_q$-iterations, $d(x,y)$ is the
base-manifold distance, and $\varepsilon > 0$ is an arbitrary
threshold.

**Theorem (speed of light equals one).**
*In Planck units, $c = 1$.  This is not a unit convention but a
consequence of the categorical structure:*

*Proof.*
Each application of the $q$-connection $\nabla_q$ acts by correlating
one fibre with its immediate neighbour via the $R$-matrix braiding.
Three properties of the rigid monoidal category $\mathbf{C}$ ensure
that no information can propagate faster:

1. **Locality of $\nabla_q$.**  The comultiplication
   $\Delta \colon A \to A \otimes A$ of the Frobenius--Hopf object
   splits the section algebra into tensor factors indexed by fibres.
   The $q$-connection acts on the tensor product of adjacent factors
   only --- it cannot skip fibres.

2. **Unitarity of the $R$-matrix.**  The braiding
   $\sigma_{V,W} \colon V \otimes W \to W \otimes V$ in the rigid
   monoidal category $\mathbf{C}$ is unitary (norm-preserving with
   respect to the Frobenius pairing).  Therefore each $f_q$-iteration
   is a bijection on the fibre Hilbert space, and information is
   neither created nor destroyed per step.

3. **Bounded displacement per step.**  One $f_q$-iteration advances
   the Reeb phase by $\hbar_q = 1 - q^{-1}$
   ([Planck time](#def:planck-time)), displacing the base-manifold
   coordinate by $\hbar_q$.  The time duration of one step is also
   $\hbar_q$ (in continuous Reeb-flow units).  Hence the displacement
   per unit time is $\hbar_q / \hbar_q = 1$.

By properties (1)--(3), any perturbation at fibre $x$ can influence
at most one additional fibre per discrete step, propagating at speed
$1$ in Planck units.  Outside this causal cone, the commutator norm
decays exponentially:

$$
  \bigl\lVert
    [\,\mathcal{O}_x(n),\, \mathcal{O}_y(0)\,]
  \bigr\rVert
  \;\leq\;
  C \, e^{-\mu(d(x,y) - n \cdot \hbar_q)}
$$

for constants $C, \mu > 0$ depending on $q$.  This is the
**Lieb--Robinson bound** of the QOU dynamics. $\square$

**Information bandwidth.**
While the geometric speed $c = 1$ is $q$-independent, the
*information content* of the propagation depends on $q$ through the
operational entropy $\eta_q$
([operational entropy](#def:operational-entropy)).  The total
information bandwidth per Planck time across a causal contact is

$$
  \mathcal{B}(q) \;=\; n_R(q) \cdot \eta_q
  \;=\; \frac{\eta_q}{\hbar_q}
  \quad \text{(bits per Planck time)}.
$$

At $q = 1.1097$: $\mathcal{B} \approx 10 \cdot d_H(1.1097) \cdot \log 2$.

**Why $c$ is derived, not postulated.**
In standard physics, the speed of light is a dimensional constant
relating metres to seconds.  In the QOU, neither the Planck length
($\ell_P = 1$) nor the Planck time ($t_P = 1$ in Reeb units)
contains $c$ as an independent parameter.  The speed of light
emerges from the theorem above: the locality of the categorical
connection, the unitarity of the braiding, and the bounded
displacement per iteration together force $c = 1$.  The dimensional
value $c = 2.998 \times 10^8\,\mathrm{m/s}$ is recovered by
restoring SI units to the Planck length and Planck time --- it
measures the human-scale size of a Planck cell, not a property of
the categorical dynamics.

**Comparison with information-theoretic speed limits.**
The Lieb--Robinson derivation of $c = 1$ is the discrete-dynamics
analog of three classical results:

| Result | Bound | QOU analog |
|--------|-------|------------|
| Margolus--Levitin (1998) | $\leq 2E/\pi\hbar$ ops/sec | $n_R(q) = 1/\hbar_q$ operations per Planck time |
| Bremermann (1962) | $\leq mc^2/h$ bits/sec/kg | $\mathcal{B}(q) = \eta_q / \hbar_q$ bits per Planck time |
| Bekenstein (1981) | $S \leq 2\pi RE/\hbar c$ | Fibre entropy $\leq \eta_q$ per operation |

In each case, the QOU bound is *saturated* by the Reeb dynamics:
each $f_q$-iteration is one $R$-matrix evaluation at the maximum
allowed rate.

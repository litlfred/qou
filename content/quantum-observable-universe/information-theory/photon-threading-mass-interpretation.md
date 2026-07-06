**Three computations of the same quantity.**
The mass $\mathfrak{m}_{\mathfrak{H}}$ is computed by three independent methods
that yield the same result:

| Method | Domain | Computes $\mathfrak{m}_{\mathfrak{H}}$ as |
|--------|--------|------------------------------|
| Yekutieli MI | Analytic | $\lVert\mathrm{MI}\int_\Sigma(\nabla_A q, L \wedge F^+)\rVert$ |
| Ribbon trace | Algebraic | $\lVert\mathrm{tr}_{\mathrm{ribbon}}(\rho(\beta_{\mathfrak{H}}))\rVert \cdot (q-1)^2$ |
| Gröbner--Shirshov reduction | Computational | $(q-1)^2 \sum \lvert c_w\rvert \cdot \lvert q - q^{-1}\rvert$ |

The first is the definition ([mass over $\mathbb{C}$](#ex:mass-identity-su2)).
The second follows from the ribbon category structure
([mass--energy equivalence](#thm:mass-energy-equivalence)).
The third is the content of this proposition.

**Physical picture.**
The photon $\gamma$ ($\mathbf{1}_{B_4}$ 4-strand id, knot-trivial under Markov closure) approaches the
hadron $\mathfrak{H}$.  To "measure" the hadron — to determine its mass — the
photon must braid completely through $\mathfrak{H}$, moving from one side of
the braid word to the other.

1. **Start.**  The photon strand sits above the hadron braid:
   $\gamma \otimes \beta_{\mathfrak{H}} \in B_{n+1}$.

2. **Thread.**  Apply braid relations to move $\gamma$ downward
   through $\beta_{\mathfrak{H}}$.  The Yang--Baxter moves
   ($\sigma_i\sigma_{i+1}\sigma_i = \sigma_{i+1}\sigma_i\sigma_{i+1}$)
   and far-commutativity ($\sigma_i\sigma_j = \sigma_j\sigma_i$)
   are **free** — they rearrange crossings without changing the
   Skein weight
   ([Gröbner--Shirshov energy](#thm:groebner-shirshov-energy)).
   Only the **Hecke steps**
   ($\sigma_i^2 \to (q - q^{-1})\sigma_i + 1$) cost energy:
   each resolves a double crossing into a weighted single crossing
   plus a resolved identity.

3. **End.**  The photon strand is below $\beta_{\mathfrak{H}}$.  The total
   Hecke cost is the crossing energy
   $E_{\mathfrak{H}} = \sum |c_w| \cdot |q - q^{-1}|$ (in Skein
   units).  Via mass--energy equivalence, the mass is
   $\mathfrak{m}_{\mathfrak{H}} = E_{\mathfrak{H}} \cdot (q-1)^2$.

**Mechanism by which the photon measures mass.**
The photon has no crossings of its own — it is topologically
trivial ($K = \varnothing$).  But it couples to the gauge field
($F_A^+$) because it propagates as exceptional-divisor flux
([photon wavefront](#ex:photon-wavefront)).  Threading
it through $\mathfrak{H}$ forces it to traverse every crossing of $\beta_{\mathfrak{H}}$,
and each crossing it encounters contributes a Hecke reduction.

The **surface** $\Sigma$ in the Yekutieli integral
$\mathrm{MI}\int_\Sigma$ is precisely the disc swept by the photon
as it passes through the hadron: $\partial\Sigma = \varrho$ (the
vortex boundary), and the interior of $\Sigma$ is the trajectory
of $\gamma$ through $\beta_{\mathfrak{H}}$.  The multiplicative integral
accumulates the connection along this trajectory — the analytic
expression of the algebraic Gröbner--Shirshov reduction.

**The Gröbner--Shirshov energy is path-independent.**
The confluence of the Gröbner--Shirshov basis (Bergman diamond lemma)
ensures that the total Hecke cost is the same regardless of the
order in which reductions are applied.  This is the algebraic
expression of the **gauge invariance** of the mass: the
Yekutieli integral is independent of the choice of surface
$\Sigma$ (provided $\partial\Sigma = \varrho$), and the
Gröbner--Shirshov reduction is independent of the reduction path.

**Connection to the speed of light.**
The factor $(q-1)^2$ converting crossing energy to mass is
$1/c_q^2$:

$$
  \mathfrak{m}_{\mathfrak{H}} =  \frac{E_{\mathfrak{H}}}{c_q^2}
  =  (q-1)^2 \cdot E_{\mathfrak{H}}.
$$

Each Hecke step costs $|q - q^{-1}|$ in Skein units (spatial
information).  The factor $(q-1)^2 = (q\hbar_q)^2$ converts this
to mass units (temporal information) — the square of the ratio of
temporal to spatial coupling in the $q$-connection.  The photon
traverses the hadron at speed $c_q = 1/(q-1)$; the mass is the
total traversal cost divided by $c_q^2$.

The correspondence between the Feynman path integral formalism and the
QOU categorical trace is summarised in the following dictionary.  Each
row identifies a structural element of Feynman's formulation with its
QOU counterpart; the third column gives the content block where the
QOU object is defined.

See [Table](#tbl:feynman-qou-dictionary-table-data).

**Three finite computations of the path integral.**
The categorical trace admits three independent evaluation methods
--- analytic, algebraic, and computational --- each producing the
same finite answer without regularisation:

1. **Multiplicative integral** (analytic) \cite{yekutieli2015}:
   $\mathfrak{m} = \lVert\mathrm{MI}\int_\Sigma(\nabla_A q, L \wedge F^+)\rVert$.
   The surface $\Sigma$ is the disc swept by the photon threading
   through the hadron braid; the multiplicative integral accumulates
   the connection along this surface.

2. **Ribbon trace** (algebraic):
   $\mathfrak{m} = \lVert\mathrm{tr}_{\mathrm{ribbon}}(\rho(\beta))\rVert \cdot (q-1)^2$.
   The Reshetikhin--Turaev invariant evaluated in the ribbon category
   gives the crossing energy; the factor $(q-1)^2 = c_q^{-2}$ converts
   to mass.

3. **Gr\"obner--Shirshov reduction** (computational):
   $\mathfrak{m} = (q-1)^2 \sum_{\text{Hecke steps}} |c_w| \cdot |q - q^{-1}|$.
   Each Hecke step $\sigma_i^2 \to (q - q^{-1})\sigma_i + 1$ is a
   discrete contribution; the Yang--Baxter moves are free.  Confluence
   of the Gr\"obner--Shirshov basis ensures path independence (gauge
   invariance).

**Photon threading as insertion of a complete set of states.**
In the Feynman formalism, the propagator is computed by inserting a
complete set of intermediate states: $K(x_f, x_i; t) = \sum_n
\langle x_f | n \rangle \langle n | x_i \rangle e^{-iE_n t/\hbar}$.
The QOU analogue is the photon threading construction
([photon threading mass](#prop:photon-threading-mass)):
the photon strand $\gamma$ passes through the hadron braid
$\beta_{\mathfrak{H}}$, encountering each crossing in sequence.  Each
crossing contributes a Hecke step (eigenvalue insertion), and the total
threading cost is the mass.  The braid crossings play the role of
intermediate states; the Hecke relation $(T - q)(T + q^{-1}) = 0$
provides the eigenvalue decomposition at each insertion.

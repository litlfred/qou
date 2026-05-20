The correspondence between the Feynman path integral formalism and the
QOU categorical trace is summarised in the following dictionary.  Each
row identifies a structural element of Feynman's formulation with its
QOU counterpart; the third column gives the content block where the
QOU object is defined.

| Feynman formalism | QOU categorical trace | Reference |
|:---|:---|:---|
| Configuration space of paths | Braid group $B_n$ acting on $V^{\otimes n}$ | [braid action](#prop:braid-action-tensor) |
| Path measure $\mathcal{D}\phi$ | Markov trace $\mathrm{tr}_M$ on $H_n(R, q)$ | [Jones--Markov trace](#thm:jones-markov-trace) |
| Action functional $S[\phi]$ | $q$-energy $\mathfrak{E}_q(\varrho) = |\mathrm{tr}_M(\rho(\beta))|$ | [$q$-energy](#def:q-energy) |
| Transition amplitude $\langle\psi_f|\psi_i\rangle$ | Markov trace $\mathrm{tr}_M(\rho(\beta))$ | [categorical trace](#prop:feynman-categorical-trace) |
| Amplitude phase $e^{iS[\phi]/\hbar}$ | $R$-matrix eigenvalues $q$, $-q^{-1}$ of $c_{V,V}$ | [$R$-matrix braiding](#rem:r-matrix-braiding) |
| Propagator $K(x,y;t)$ | Categorical transfer matrix $\mathcal{T}(\mathfrak{H})$ | [transfer matrix](#def:categorical-transfer-matrix) |
| Hilbert space $\mathcal{H}$ | Algebraic direct limit $V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$ (no metric completion) | [knot eigenbasis](#prop:knot-eigenbasis-complete) |
| Basis states $|n\rangle$ | Irreducible summands $V_\lambda \otimes S_\lambda$ | [knot eigenbasis](#prop:knot-eigenbasis-complete) |
| Planck constant $\hbar$ | Quantum Planck constant $\hbar_q = 1 - q^{-1}$ | [$q$-energy](#def:q-energy) |
| Classical limit $\hbar \to 0$ | $q \to 1$ limit | [classical limit](#prop:feynman-classical-limit) |
| Partition function $Z$ | $\dim_q(V^{\otimes n}) = \sum_\lambda \dim_q(V_\lambda)\dim(S_\lambda)$ | [knot eigenbasis](#prop:knot-eigenbasis-complete) |
| Regularisation / renormalisation | Absent (finite sum, no divergences) | — |

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

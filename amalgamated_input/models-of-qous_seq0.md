<!-- FILE_START: framing-arc-intro.md -->
The five structural steps below map the logical arc of this paper. Every quantum observable universe realises these steps, with each developed in a dedicated chapter. The arc runs from categorical foundations to physical prediction. The sequence reads top-down to build the machinery, or bottom-up to trace predictions to their origin.

1. **Categorical step.** A rigid braided monoidal category with a Frobenius--Hopf object, parametrised by the substrate $q$.
2. **Algebraic step.** The braid group $B_n$ and its Hecke quotient $H_n(q)$, equipped with a Markov trace.
3. **Geometric step.** Knot complements realised as $q$-hyperbolic structures. The Reeb-bundle complement equals the volume invariant.
4. **Archimedean step.** Specialisation $R \to R[i] \to R[i][q, q^{-1}]$ at $q = q_0$. The non-abelian Stokes mass identity closes the arc.
5. **Physical step.** Predicted spectra and observations.

This chapter outlines each step, fixes the standard terminology, and catalogues alternative models (Calabi--Yau, ALE, $p$-adic, characteristic $p$). These models realise the common axioms across different arithmetic settings.
<!-- FILE_END: framing-arc-intro.md -->

<!-- FILE_START: step-categorical.md -->
**Categorical step.** The model begins categorically because the
substrate parameter $q$ needs a structure to deform: at $q = 1$ one has
the classical symmetric tensor category, while $q \neq 1$ resolves its
action into a braided one. Concretely, the substrate is a rigid braided
monoidal category $(\mathbf{C}, A, \tau)$ equipped with a
Frobenius--Hopf object $A$ and a fibre functor $\tau$, and $q$ records
the deformation of this categorical action. The Reeb derivation $\delta_q$ promotes $q$ to a connection
on the categorical bundle; its curvature is the Yekutieli MI tower.
The Quantum Universes and Quantum Observable Universes chapters develop
the axioms and derive the Reeb derivation. The Brane Tower chapter
develops descent, jets, and the Gröbner--Shirshov filtration --- the
categorical infrastructure consumed throughout the paper.
<!-- FILE_END: step-categorical.md -->

<!-- FILE_START: step-algebraic.md -->
**Algebraic step.** To turn the categorical action into a computable
knot invariant, one passes from braids to a trace-carrying quotient.
The braid group $B_n$ acts on $A^{\otimes n}$. Its
quotient by the Hecke relation
$(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ is the Iwahori--Hecke algebra
$H_n(q)$, which controls the combinatorics of the categorical action.
The Markov trace $\mathrm{tr}_M$ packages braid words into a class
function whose evaluation on $\beta_K$ is the Jones polynomial
$J_K(q) = \mathrm{tr}_M(\rho(\beta_K))$. The Braids, Knots, and Hecke
chapter develops braids, knot groups, the Hecke algebra, and the
Skein-relation translation. The stochastic interpretation of
$\mathrm{tr}_M$ as a transition kernel is deferred to the Stochastic
Mechanics chapter (Part IV).
<!-- FILE_END: step-algebraic.md -->

<!-- FILE_START: step-geometric.md -->
**Bring's surface — the canonical geometric object.** The geometric
step realises the mass of every knot on one fixed surface, so we fix
that surface before running the flow argument. The canonical geometric
realisation is **Bring's surface** $\Sigma_4$, the genus-4 smooth
projective curve with Euler characteristic $\chi = -6$ whose
automorphism group $\mathrm{Aut}(\Sigma_4) \cong S_5$
exchanges the five quark--lepton families. It is the vanishing locus
on $\mathbb{P}^4$ of the first three power sums:

$$
  \Sigma_4 = \mathrm{Proj}\!\left(
    R[x_0,\dots,x_4]\Big/\bigl(\textstyle\sum x_j,
    \textstyle\sum x_j^2, \textstyle\sum x_j^3\bigr)
  \right).
$$

The structural facts consumed throughout the paper are:

- $\Sigma_4$ has **genus** $g = 4$ and **Euler characteristic**
  $\chi(\Sigma_4) = 2 - 2g = -6$.
- The **automorphism group** is $\mathrm{Aut}(\Sigma_4) \cong S_5$
  (order 120), the largest for any genus-4 curve. The orientation-
  preserving subgroup $A_5 \subset S_5$ acts faithfully and supplies
  the symmetry group of the canonical particle assignment.
- $\Sigma_4$ is the **canonical archimedean model**: the substrate
  parameter $q_0$ is fixed by its $\chi = -6$ structure, and the
  Reeb derivation produces a $q$-hyperbolic structure on $\Sigma_4$
  with five $S_5$-equivalent fibres (one per particle family).
- The **cohomological defect** of $\Sigma_4$ — the discrepancy
  between its first Betti number and the rank of the natural
  three-colour bundle — supplies the structural origin of the
  three-colour SU(3) charge of QCD.

**Geometric step.** With $\Sigma_4$ in hand, the Reeb derivation lifts
a braid word $\beta_K$ to a Reeb flow whose complement $S^3 \setminus
K$ is a $q$-hyperbolic 3-manifold. By a theorem of Yekutieli, this
complement carries a tessellation by ideal $q$-tetrahedra indexed by
$k = 0, 1, 2, 3$ --- the categorical $h^{2j}$ ladder with cell
coefficients $(1, 4, 16, 64)$. The volume $\mathrm{Vol}(K)$ of the
complement is the central geometric invariant. Because this volume
realises the topological mass of the knot, evaluating it on $\Sigma_4$
assigns each knot its mass; and because the cohomological defect of
$\Sigma_4$ supplies the three-colour charge, the one surface fixes
both the mass and the colour structure.

The climax chapter (q-Hyperbolic $\to$ Volume $\to$ Mass) derives the
volume identity, the tangle-energy decomposition, and the mass-
endomorphism statement. The Bring's Surface chapter develops the
surface in full depth --- the formal definition with proofs of
smoothness, the $S_5/A_5$ action, the cohomological-defect derivation
(which yields the three quark colours), and the connection to the
Klein quartic.
<!-- FILE_END: step-geometric.md -->

<!-- FILE_START: step-archimedean.md -->
**Archimedean step.** We cross the archimedean wall because it is the
branch that gives physics: specialisation at the substrate value $q_0$
produces archimedean (real-valued, dimensional) quantities, and its
payoff is a dimensional mass. The machinery that gets there is a chain
of extensions of the generic categorical content: stated over a
commutative ring $R$, it specialises through
$R \to R[i] \to R[i][q, q^{-1}]$. The substrate value $q = q_0$ is
fixed by the $\chi = -6$ structure of Bring's surface (its numerical
value is pinned in the Introduction and in the Observations chapter).

The mass endomorphism
$\mathfrak{m}(K) = \mathrm{Vol}(K) \cdot c_q^{-2}$ ---
the non-abelian Stokes integration of the Reeb flow against the
categorical action --- is the statement that closes the first half
of the paper. The climax chapter states it; the Mass --- Theory and
Mass --- Application chapters unpack the machinery (Wedderburn
decomposition, partition channels $y_\lambda \chi^\lambda$, crystal
bases, $\Delta_\lambda$ gating) needed to evaluate it.

Alternatives to the archimedean specialisation --- $\pp$-adic
($R \to \mathbb{Q}_\pp$) and characteristic-$\pp$ ($R \to
\mathbb{F}_\pp[T]$) substrate completions --- are sketched in §7
below. They are non-archimedean and do not produce dimensional
masses.
<!-- FILE_END: step-archimedean.md -->

<!-- FILE_START: step-physical.md -->
**Physical step.** Once the archimedean specialisation at $q_0$ is
fixed on Bring's surface, the framework predicts a particle spectrum
from three calibration inputs ($m_e$, $m_\mu/m_e$, $\mathfrak{Q}_\beta$). The
Particles chapter develops the particle-generation mechanism (LP/SDP
confinement, operator-valued folding/unfolding); the Statistics &
Symmetrisation chapter derives Pauli exclusion and the fermion/boson
split from the rigid-braided structure. The Predicted Spectra chapter
catalogues these predictions (leptons, quarks, baryons, nuclei,
$\mathfrak{Q}_\beta$, magnetic moments) and compares them to CODATA in the
Observations chapter. Subsequent chapters extend the framework to
atomic, molecular, and organic chemistry.

Part IV develops dynamical and information-theoretic deepenings: fluid
dynamics of the brane, stochastic mechanics of the Markov trace,
categorical information theory, quantum measurement as fibre-functor
behaviour, and the $q$-geometric Langlands correspondence.
<!-- FILE_END: step-physical.md -->


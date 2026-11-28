The Cardona–Miranda–Peralta-Salas–Presas \cite{cardona2021} procedure bridges steady Euler flow and contact-Reeb flow through a **conformal change of metric**. Given a divergence-free, non-vanishing Euler field $X$ on $(M^3, g)$, rescaling $X \mapsto X / |X|_g^2$ and factoring the metric maps $X$ to the Reeb vector field of a contact form on $(M^3, \tilde g)$. The dynamical universality derives from the contact structure, not the initial metric.

The QOU executes exactly this operation via the aether parameter $q$. The [$q$-Navier–Stokes equation](#def:q-navier-stokes) replaces the classical Riemannian inner product with the $q$-deformed Frobenius pairing ([Frobenius–Hopf aether](#def:frobenius-hopf-aether)). This constitutes a one-parameter family of metric adjustments, smoothly modulating between:

- the **full Levi-Civita connection** (the "Euler-side" geometry representing Riemannian fluid flow), and
- its **Reeb projection** along $\xi_q$ (the "contact-side" geometry isolating pure Reeb flow).

The parameter $q$ acts as the dial. Three regimes govern the behaviour:

| Parameter limit | Geometric picture | Dynamical content |
|---|---|---|
| $q \to 1^+$ | Full Riemannian metric; $\varTheta_q$ degenerates | Inviscid Euler limit ($\nu_q \to 0$, or fixed-viscosity Navier--Stokes after $c_q$-rescaling); Reeb projection vanishes |
| $q > 1$ generic | Strict contact metric on $\mathcal{S}$ | $q$-NS conditionally regular ([global regularity](#thm:q-ns-wellposedness)); Reeb flow Turing-complete ([Reeb universal computer](#rem:reeb-contact-universal-computer)) |
| $q \to \infty$ | Pure Reeb (horizontal components vanish) | Hamiltonian first-return; bare tape-reading dynamics |

**A geometric reading of the $q$-NS obstruction.**
The [NS obstruction class](#def:ns-obstruction) gauges how the classical $q = 1$ contact form collapses at a vortex-collision locus. Through Miranda's framework, increasing $q$ past $1$ rescales the Riemannian metric to buoy the contact form against degeneracy. Because the plane field $\ker\varTheta = \xi^\perp$ on the three-dimensional flow domain has Levi datum given by the single scalar $\xi\cdot\mathrm{curl}\,\xi$ rather than an eigenvalue pair or condition number ([core Levi form](#prop:core-levi-form)), this rescaling cannot be read as [quantum pressure](#rem:madelung-fluid) bounding a Levi condition number away from zero; how the $q$-deformation acts on $\xi\cdot\mathrm{curl}\,\xi$ is not established here.

**Location in the proof strategy.**
The [q-NS research programme](#rem:q-ns-research-programme) incorporates two implications:

1. Global well-posedness for $q > 1$ ([thm:q-ns-wellposedness](#thm:q-ns-wellposedness)) versus breakdown at $q = 1$ is a feature of the smooth-vs-degenerate contact dichotomy, not an independent quantum effect.
2. The [Levi degeneracy conjecture](#conj:levi-degeneracy) asks whether vanishing of $\xi\cdot\mathrm{curl}\,\xi$ on the high-vorticity set prevents blow-up; that question is open, whereas the converse claim that preserving contact non-degeneracy forces blow-up is refuted by steady Beltrami flows. The [Biot–Savart](#rem:townsend-biot-savart-strain) and [hyperbolic overlap](#rem:hyperbolic-overlap-saturation) remarks give the core aspect ratio as the solution of ODEs; that ratio carries no Levi information.

In the Cardona–Miranda grammar: the parameter $q$ selects the contact metric, and that choice determines whether the Reeb dynamics persists.

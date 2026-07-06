**Proposition (conditional on
[`conj:hyperbolic-volume-transcendence`](#conj:hyperbolic-volume-transcendence)
and
`rem:baryon-period-ratio`).**
*The categorical volume form, evaluated on the knot complement
$S^3 \setminus K$ through the fibre functor $\tau$, yields
$\mathrm{Vol}(K)$ for hyperbolic knots and $\mathrm{CS}(K)$ for
torus knots.  This identification is universal: it is the UNIQUE
evaluation compatible with the Frobenius--Hopf structure.*

*Specifically, $\mathrm{Geom}(K)$ is the unique functional on knot
complements satisfying:*

1. *Additivity: $\mathrm{Geom}(K_1 \# K_2) = \mathrm{Geom}(K_1) +
   \mathrm{Geom}(K_2)$.*
2. *Functoriality: $\mathrm{Geom}(K) = \tau(\mathrm{tr}_M(\rho(\mathcal{B}_K)))$
   for some fibre functor $\tau$.*
3. *Normalisation: $\mathrm{Geom}(\bigcirc) = 0$ (vacuum) and
   $\mathrm{Geom}(4_1) = \mathrm{Vol}(4_1)/\hbar_q^2$ (fixes $q_0$).*

*Proof.*
The argument proceeds in three steps.

**Step 1: Existence (Neumann--Zagier, τ-image side).**
On the τ-image (geometric) side, the Neumann--Zagier theorem
\cite{neumann-zagier1985} establishes that for a hyperbolic knot
$K$, $\mathrm{Vol}(K)$ and $\mathrm{CS}(K)$ are related by:

$$
  \mathrm{Vol}(K) + i\,\mathrm{CS}(K)
  = \sum_j \bigl(L(z_j) + \arg(z_j) \log|z_j|\bigr)
$$

where $L$ is the Bloch--Wigner dilogarithm and $z_j$ are the shape
parameters of the ideal triangulation.  This is a function of the
$\mathrm{SL}(2,\mathbb{C})$ representation variety of $\pi_1(S^3
\setminus K)$.

In the categorical framework, the Frobenius--Hopf algebra $A$ at
parameter $q$ has representation variety isomorphic to $\mathrm{Spec}$
of the coordinate ring $\mathcal{O}_q(\mathrm{SL}_2)$.  The fibre
functor $\tau$ evaluates the volume form $\omega$ on this variety.
By Neumann--Zagier, the real part of this evaluation is
$\mathrm{Vol}(K)$.

**Step 2: Uniqueness (Yekutieli rigidity).**
The rigid dualizing complex $\omega_A^\bullet$
([Geom(K) alignment](#conj:geom-yekutieli-alignment)) provides a
non-degenerate Frobenius pairing
$\langle -, - \rangle_{\mathrm{Frob}}$.  Yekutieli's rigidity
theorem \cite{yekutieli2015} states that this pairing is unique up
to scalar.

The scalar is fixed by the two normalisations:
- $\mathrm{Geom}(\bigcirc) = 0$ eliminates the constant term.
- $\mathrm{Geom}(4_1) = \mathrm{Vol}(4_1)/\hbar_q^2$ fixes the
  overall scale (this is the equation that defines $q_0$).

Therefore any functional satisfying properties 1--3 must equal
$\mathrm{Geom}$.

**Step 3: The CS/Vol duality.**
For torus knots, $\mathrm{Vol} = 0$ and the representation variety
consists of a single abelian flat connection.  The evaluation of
$\omega_A^\bullet$ on this connection is the Chern--Simons functional:

$$
  \mathrm{CS}(T_{m,n})
  = \frac{\pi^2(m^2-1)(n^2-1)}{12mn}
$$

The duality $\mathrm{Vol}/\hbar_q^2 \leftrightarrow
\mathrm{CS} \cdot \hbar_q^2$ follows from the self-duality of the
rigid dualizing complex: $\omega_A^\bullet \simeq
R\mathrm{Hom}_{A^e}(A, A^e)$ provides two evaluation maps (left and
The right), and the scale factor $\hbar_q^2$ exchanges them.

Additivity (property 1) follows from the fact that connected sum
$K_1 \# K_2$ corresponds to tensor product in the Frobenius--Hopf
category, and the volume form is a trace (hence additive on tensor
products).
$\square$

**Archimedean specialisation (§7c).** This block is stated over the real field $\mathbb{R}$ — the archimedean side of the substrate wall: its constructs are real-valued (physical observables, real-analytic bounds, or numerical evaluations at the substrate parameter $q_0$) rather than generic-ring $q$-deformation data. The generic categorical / $q$-deformation machinery it draws on is stated over an abstract coefficient ring in its own blocks; only the archimedean realisation is specialised here.

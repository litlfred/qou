<!-- FILE_START: q-ns-regularity-intro.md -->
The $q$-deformed hydrodynamics of the preceding sections
delivers a closed evolution equation on $\Omega^1(A)$. We now prove
that this evolution is globally regular whenever $q > 1$, using the
spectral theory of the $q$-Laplacian and the quantum Peter--Weyl
decomposition of the brane.

The main theorem is Theorem: Global regularity of the $q$-deformed Navier--Stokes equation: for every $q > 1$, smooth
finite-energy initial data extends to a unique smooth solution for
all time. We then outline the argument in Remark: Proof strategy: three mechanisms for $q$-deformed regularity, naming the UV
damping, enstrophy bound, and uniqueness inputs. The first input
is Proposition: Spectral theory and Sobolev embedding for the $q$-Laplacian on $\Omega^1(A)$, which establishes compact resolvent and the
embedding chain on the categorical Hodge complex. The completeness
of the resulting eigenbasis is Theorem: Quantum Peter--Weyl theorem: completeness of the $\mathrm{SU}_q(2)$ eigenbasis, proved
on the categorical infrastructure already in place. The nonlinear
step is Proposition: Nonlinear estimates and uniqueness for the $q$-Navier--Stokes system, and the calculations are
collected in Remark: Proof details: nonlinear estimates, enstrophy evolution, and uniqueness. The next section, **The NS
obstruction**, takes the regularity theorem as the $q > 1$ side of
the categorical degeneration and asks what survives at $q = 1$.

_(draft.)_
<!-- FILE_END: q-ns-regularity-intro.md -->

<!-- FILE_START: q-ns-wellposedness.md -->
Let $(\mathbf{C}, A, \tau)$ be a
[QOU](#def:quantum-observable-universe) with
[substrate parameter](#def:substrate-parameter)
$q \in \mathrm{End}(\mathbf{1})$, $q > 1$.  Let
$\Delta_q = d_q\delta_q + \delta_q d_q$ be the
[$q$-Laplacian](#rem:q-laplacian-interpretation) on $\Omega^k(A)$
and let $\nu_q = \frac{1}{2}(1 - q^{-1}) > 0$ be the kinematic
viscosity.

**Categorical statement.**
Let $v_0 \in \ker(\delta_q|_{\Omega^1(A)})$ be a divergence-free
initial velocity 1-form with finite
[Frobenius norm](#def:frobenius-pairing)
$\lVert v_0 \rVert_A^2 = \int_A v_0^\dagger \wedge v_0 < \infty$.
Then the [q-deformed Navier--Stokes system](#def:q-navier-stokes)
admits a **unique global solution**

$$
  (v, p) \colon [0, \infty)
   \to 
  \ker(\delta_q|_{\Omega^1(A)}) \times A
$$

such that:

1. **Smoothness in $\mathbf{C}$**: the map
   $t \mapsto v(t) \in \Omega^1(A)$ is smooth (infinitely
   differentiable in the internal hom of $\mathbf{C}$).

2. **Energy inequality**: for all $t \geq 0$,

   $$
     \lVert v(t) \rVert_A^2
     + 2\nu_q \int_0^t
     \lVert d_qv(s) \rVert_A^2ds
      \leq 
     \lVert v_0 \rVert_A^2.
   $$

3. **Spectral decay**: the $\Delta_q$-eigencomponents
   $\hat{v}_k \in V_k \subset \Omega^1(A)$
   (where $\Delta_q|_{V_k} = [k]_q^2\mathrm{id}$) satisfy

   $$
     |\hat{v}_k(t)|  \leq 
     |\hat{v}_k(0)|e^{-\nu_q [k]_q^2 t}
   $$

   so that modes decay at exponential-in-$k$ rate.

**Archimedean realisation.**
Under the fibre functor $\tau$, the categorical solution maps to
a smooth vector field on the
[state bundle](#ex:c-quantum-observable-universe) $\mathcal{S}$:

$$
  \tau(v) \in C^\infty(\mathcal{S} \times [0,\infty); T\mathcal{S}),
  \qquad
  \nabla_A \cdot \tau(v) = 0,
$$

satisfying the coordinate form

$$
  \partial_t v + (v \cdot \nabla_A) v
  = 
  -\frac{1}{\rho}\nabla_A p
  - \nabla_A Q_q
  + \nu_q\Delta_q v,
  \qquad
  v|_{t=0} = v_0,
$$

with energy inequality

$$
  \lVert v(\cdot, t)\rVert_{L^2}^2
  + 2\nu_q \int_0^t
  \sum_{k=1}^\infty [k]_q^2|\hat{v}_k(s)|^2ds
   \leq 
  \lVert v_0\rVert_{L^2}^2
$$

for all $t \geq 0$.

<!-- FILE_END: q-ns-wellposedness.md -->

<!-- FILE_START: p1-spectral-sobolev.md -->
Let $(\mathbf{C}, A, \tau)$ be a
[QOU](#def:quantum-observable-universe) with
[substrate parameter](#def:substrate-parameter) $q > 1$. Let
$\Delta_q = d_q\delta_q + \delta_q d_q$ be the
[$q$-Laplacian](#rem:q-laplacian-interpretation) acting on
$\Omega^1(A)$, and let
$\langle \cdot, \cdot \rangle_\varTheta$ be the
[Webster inner product](#rem:hodge-laplacian-relation).

Then the following hold:

**(a) Compact resolvent and discrete spectrum.**
The operator $\Delta_q$ on $\Omega^1(A)$ has compact resolvent:
for any $\lambda \notin \mathrm{spec}(\Delta_q)$, the resolvent
$(\lambda\mathrm{id} - \Delta_q)^{-1}$ is a compact operator
on the Hilbert completion
$\overline{\Omega^1(A)}^{\langle\cdot,\cdot\rangle_\varTheta}$.
Consequently, the spectrum is discrete:
$\mathrm{spec}(\Delta_q) = \{\mu_k^{(q)}\}_{k \geq 0}$
with $0 \leq \mu_0^{(q)} \leq \mu_1^{(q)} \leq \cdots$ and
$\mu_k^{(q)} \to \infty$.

**(b) Exponential eigenvalue growth.**
The eigenvalues satisfy

$$
  \mu_k^{(q)} = [k]_q^2,
  \qquad
  [k]_q = \frac{q^k - q^{-k}}{q - q^{-1}},
$$

with the growth bound

$$
  \frac{q^{2k}}{(q - q^{-1})^2}
   \leq 
  \mu_k^{(q)}
   \leq 
  \frac{q^{2k}}{(q - q^{-1})^2}
  \left(1 + q^{-4k}\right)
$$

for all $k \geq 1$. In particular,
$\mu_k^{(q)} = \Theta(q^{2k})$ — exponential in $k$.

**(c) Categorical Sobolev embedding.**
Define the $q$-Sobolev space
$H^1_q(A) = \{v \in \Omega^1(A) :
\lVert v \rVert_A^2 + \lVert d_q v \rVert_A^2 < \infty\}$.
Then $H^1_q(A)$ embeds continuously into the space of bounded
1-forms:

$$
  \lVert v \rVert_{L^\infty}
   \leq 
  C_q\lVert v \rVert_{H^1_q},
  \qquad
  C_q = \left(\sum_{k=1}^\infty [k]_q^{-2}\right)^{1/2}.
$$

The constant $C_q$ is finite for all $q > 1$ (the series
converges because $[k]_q^{-2} = O(q^{-2k})$). As $q \to 1$,
$[k]_q \to k$ and $C_q^2 \to \sum k^{-2} = \pi^2/6$ in the
1-dimensional case. On the 3-dimensional state bundle
$\mathcal{S}$, eigenvalue multiplicities $(2j+1)^2$ cause
$C_q$ to diverge — the embedding fails in the classical limit.
<!-- FILE_END: p1-spectral-sobolev.md -->

<!-- FILE_START: quantum-peter-weyl.md -->
**Statement.**
Let $(\mathbf{C}, A, \tau)$ be a
[QOU](#def:quantum-observable-universe) with
[substrate parameter](#def:substrate-parameter) $q > 1$.  Let
$\{V_j\}_{j \in \frac{1}{2}\mathbb{Z}_{\geq 0}}$ be the simple
objects of $\mathbf{C}$ indexed by spin $j$, with categorical
dimension $\dim(V_j) = 2j + 1$.  For each $j, m, n$ with
$-j \leq m, n \leq j$, define the **matrix coefficient**

$$
  D^j_{mn}
  = 
  (\mathrm{ev}_{V_j} \otimes \mathrm{id})
  \circ (\mathrm{id} \otimes e^j_m \otimes (e^j_n)^\vee)
  \circ \mathrm{coev}_{V_j}
   \in  A,
$$

where $\{e^j_m\}$ is an orthonormal basis of $\tau(V_j)$ and
$\mathrm{ev}, \mathrm{coev}$ are the evaluation and coevaluation
from the rigid structure.

Then:

**(a) Orthogonality.**  With respect to the
[Frobenius pairing](#def:frobenius-pairing):

$$
  \int_A (D^j_{mn})^\dagger \cdot D^{j'}_{m'n'}
  = 
  \frac{\delta_{jj'}\delta_{mm'}\delta_{nn'}}{[2j+1]_q},
$$

where $[2j+1]_q$ is the quantum dimension.

**(b) Completeness.**  The matrix coefficients
$\{[2j+1]_q^{1/2}D^j_{mn}\}$ form a complete orthonormal
system in the Hilbert completion
$L^2(A) = \overline{A}^{\int_A}$:

$$
  \sum_{j \geq 0} [2j+1]_q
  \sum_{m,n=-j}^{j} D^j_{mn} \otimes (D^j_{mn})^\dagger
  =  \mathrm{id}_A.
$$

**(c) $\Delta_q$-eigendecomposition.**  Each matrix coefficient
$D^j_{mn}$ is an eigenfunction of $\Delta_q$ with eigenvalue
$[j]_q[j+1]_q$ (the $q$-Casimir):

$$
  \Delta_qD^j_{mn} = [j]_q[j+1]_qD^j_{mn}.
$$

The eigenspace of eigenvalue $[j]_q[j+1]_q$ has dimension
$(2j+1)^2$.
<!-- FILE_END: quantum-peter-weyl.md -->

<!-- FILE_START: quantum-peter-weyl-interpretation.md -->
The [spectral-Sobolev theory](#prop:q-spectral-sobolev) identifies
a single gap: completeness of the $\Delta_q$-eigenbasis.  This
theorem closes it by proving the quantum Peter--Weyl theorem for
$\mathrm{SU}_q(2)$ using the categorical infrastructure already
available.

**Connection to the Kelvin dispersion.**
The [Kelvin dispersion derivation](#prop:kelvin-dispersion-derivation)
proved $\Delta_q(z^k) = -[k]_q^2z^k$ by explicit computation.
The Peter--Weyl theorem provides the conceptual reason: $z^k$ is
a matrix coefficient $D^{k/2}_{k/2, k/2}$ of the spin-$k/2$
representation, and its eigenvalue $[k/2]_q[k/2+1]_q$ reduces to
$[k]_q^2$ for the appropriate normalisation on the circle.

The quantum Peter--Weyl theorem is a consequence of the QOU
axioms (specifically the existence of the faithful exact monoidal
fibre functor $\tau$).  No external result (Woronowicz 1987) is
needed — the categorical infrastructure is self-sufficient.
<!-- FILE_END: quantum-peter-weyl-interpretation.md -->

<!-- FILE_START: p1-nonlinear-uniqueness.md -->
Let $(\mathbf{C}, A, \tau)$ be a
[QOU](#def:quantum-observable-universe) with substrate parameter
$q > 1$.  Let $v$ be a divergence-free solution of the
[q-NS system](#def:q-navier-stokes) with initial energy
$E_0 = \lVert v_0 \rVert_A^2$ and let
$C_q = (\sum_k [k]_q^{-2})^{1/2}$ be the
[Sobolev constant](#prop:q-spectral-sobolev).

**(a) q-Ladyzhenskaya inequality.**
The advection term $B(v) = \mu \circ (v \otimes \nabla_q v)$
satisfies

$$
  \lVert B(v) \rVert_A
   \leq 
  C_q\lVert v \rVert_A\lVert d_q v \rVert_A.
$$

**(b) Enstrophy bound.**
The enstrophy $\Omega(t) = \lVert d_q v(t) \rVert_A^2$ satisfies

$$
  \frac{d\Omega}{dt}
   \leq 
  \Lambda_q\Omega,
  \qquad
  \Lambda_q = \frac{C_q^2E_0}{\nu_q} - \nu_q  <  \infty.
$$

In particular, $\Omega(t) \leq \Omega(0)e^{\Lambda_q t}$ for
all $t \geq 0$: the enstrophy never blows up in finite time.

**(c) Uniqueness.**
If $v_1, v_2$ are two solutions with $v_1(0) = v_2(0)$, then
$v_1(t) = v_2(t)$ for all $t \geq 0$.
<!-- FILE_END: p1-nonlinear-uniqueness.md -->

<!-- FILE_START: p1-nonlinear-uniqueness-novelty.md -->
While these steps mirror the standard Ladyzhenskaya/enstrophy arguments for classical 2D fluid uniqueness, the mathematical novelty is demonstrating that this precise package of estimates lifts identically to the non-commutative algebraic $q$-deformed categorical setting without modification, anchoring the well-posedness natively in the quantum group Sobolev spaces rather than classical function spaces.
<!-- FILE_END: p1-nonlinear-uniqueness-novelty.md -->


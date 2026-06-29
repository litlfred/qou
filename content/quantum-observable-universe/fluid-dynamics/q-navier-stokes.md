The [quantum Euler equation](#rem:madelung-fluid) describes
inviscid flow in the brane fluid. To account for dissipation —
the irreversible transfer of kinetic energy from coherent vortex
motion to incoherent thermal fluctuations — we introduce the
**$q$-deformed Navier--Stokes equation**, first in categorical
language and then in coordinates.

**Categorical formulation.**
Let $(\mathbf{C}, A, \tau)$ be a
[QOU](#def:quantum-observable-universe) with
[substrate parameter](#def:substrate-parameter)
$q \in \mathrm{End}(\mathbf{1})$, $q > 1$. Let
$\Omega^k(A)$ denote the [differential forms](#def:higher-forms)
on the Frobenius--Hopf object $A$, with
[q-exterior derivative](#def:categorical-q-ext-deriv)
$d_q \colon \Omega^k(A) \to \Omega^{k+1}(A)$ and its adjoint
$\delta_q \colon \Omega^{k+1}(A) \to \Omega^k(A)$ with respect to
the [Frobenius pairing](#def:frobenius-pairing). The
[$q$-Laplacian](#rem:q-laplacian-interpretation) is
$\Delta_q = d_q\delta_q + \delta_q d_q$.

The **$q$-Navier--Stokes system** is the pair of morphisms in
$\mathbf{C}$:

$$
  \partial_t v
  + \mu \circ (v \otimes \nabla_q v)
  = 
  -\rho^{-1}d_qp
  -  d_qQ_q
  +  \tfrac{1}{2}(1 - q^{-1})\Delta_qv
  +  \rho^{-1}\delta_q\boldsymbol{\sigma}_q,
$$

$$
  \partial_t\rho + \delta_q(\rho \cdot v) = 0,
$$

where:

- $v \in \Omega^1(A)$ is the velocity 1-form,
- $\rho \in A$ is the density (a 0-form),
- $p \in A$ is the pressure,
- $\nabla_q$ is the [q-connection](#def:categorical-q-connection),
- $\mu \colon A \otimes A \to A$ is the multiplication on $A$,
- $Q_q = -\tfrac{1}{2}(1-q^{-1})^2
  \Delta_q(\rho^{1/2}) \cdot \rho^{-1/2} \in A$
 is the quantum pressure,
- $\boldsymbol{\sigma}_q = (1-q^{-1})\rho
  \bigl(d_q v + (d_q v)^\dagger
  - \tfrac{2}{3}(\delta_q v)\mathrm{id}_A\bigr)
  \in \Omega^2(A)$
 is the viscous stress,
- and the dagger $(-)^\dagger$ uses the
 [Frobenius pairing](#def:frobenius-pairing).

The kinematic viscosity $\nu_q = \frac{1}{2}(1 - q^{-1})
= \hbar_q/2$ arises from the
[substrate parameter](#def:substrate-parameter) alone — it is not
an independent physical constant.

**Incompressibility.**
The constraint $\delta_q v = 0$ (divergence-free, i.e.
$v \in \ker(\delta_q|_{\Omega^1})$) replaces the classical
$\nabla \cdot v = 0$. The [observability
condition](#def:quantum-observable-universe)
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
ensures this constraint is non-degenerate: there are no gauge
modes that could by definition satisfy it.

**Archimedean realisation.**
Under the [categorical--archimedean
bridge](#prop:categorical-archimedean-bridge), the fibre functor
$\tau$ sends the categorical system to coordinates on the
[state bundle](#ex:c-quantum-observable-universe) $\mathcal{S}$:

$$
  \partial_t v + (v \cdot \nabla_A)v
  = 
  -\frac{1}{\rho}\nabla_A p
  -  \nabla_A Q_q
  +  \nu_q\Delta_q v
  +  \frac{1}{\rho}
  \nabla_A \cdot \boldsymbol{\sigma}_q,
$$

where $\nabla_A$ is the $\mathrm{SU}(2)$ covariant derivative
(the geometric image of $\nabla_q$ under $\tau$), and the
$q$-deformed viscous stress tensor in coordinates is

$$
  (\boldsymbol{\sigma}_q)_{ij}
  = 
  \nu_q\rho
  \bigl(
    \nabla_{A,i}v_j + \nabla_{A,j}v_i
    - \tfrac{2}{3}(\nabla_A \cdot v)\delta_{ij}
  \bigr),
$$

with the continuity equation
$\partial_t\rho + \nabla_A \cdot (\rho v) = 0$.

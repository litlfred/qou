Let $(\mathbf{C}, A, \tau)$ describe a [QOU](#def:quantum-observable-universe) governed by [aether parameter](#def:substrate-parameter) $q \in \mathrm{End}(\mathbf{1})$, with $q > 1$. Let $\Delta_q = d_q\delta_q + \delta_q d_q$ act as the [$q$-Laplacian](#rem:q-laplacian-interpretation) on $\Omega^k(A)$, and set the kinematic viscosity $\nu_q = \frac{1}{2}(1 - q^{-1}) > 0$.

**Categorical statement.**
Let $v_0 \in \ker(\delta_q|_{\Omega^1(A)})$ be a divergence-free initial velocity 1-form carrying finite [Frobenius norm](#def:frobenius-pairing) $\lVert v_0 \rVert_A^2 = \int_A v_0^\dagger \wedge v_0 < \infty$. The [q-deformed Navier--Stokes system](#def:q-navier-stokes) then admits a **unique global solution**

$$
  (v, p) \colon [0, \infty)
   \to 
  \ker(\delta_q|_{\Omega^1(A)}) \times A
$$

satisfying:

1. **Smoothness in $\mathbf{C}$**: The map $t \mapsto v(t) \in \Omega^1(A)$ is smooth (infinitely differentiable within the internal hom of $\mathbf{C}$).
2. **Energy inequality**: For all $t \geq 0$,

   $$
     \lVert v(t) \rVert_A^2
     + 2\nu_q \int_0^t
     \lVert d_qv(s) \rVert_A^2ds
      \leq 
     \lVert v_0 \rVert_A^2.
   $$

3. **Spectral decay**: The $\Delta_q$-eigencomponents $\hat{v}_k \in V_k \subset \Omega^1(A)$ (where $\Delta_q|_{V_k} = [k]_q^2\mathrm{id}$) satisfy

   $$
     |\hat{v}_k(t)|  \leq 
     |\hat{v}_k(0)|e^{-\nu_q [k]_q^2 t}.
   $$

   Modes decay at a rate exponential in $k$.

**Archimedean realisation.**
Operating under the fibre functor $\tau$, the categorical solution maps directly to a smooth vector field on the [state bundle](#ex:c-quantum-observable-universe) $\mathcal{S}$:

$$
  \tau(v) \in C^\infty(\mathcal{S} \times [0,\infty); T\mathcal{S}),
  \qquad
  \nabla_A \cdot \tau(v) = 0,
$$

satisfying the coordinate equation

$$
  \partial_t v + (v \cdot \nabla_A) v
  = 
  -\frac{1}{\rho}\nabla_A p
  - \nabla_A Q_q
  + \nu_q\Delta_q v,
  \qquad
  v|_{t=0} = v_0,
$$

and bound by the continuous energy inequality

$$
  \lVert v(\cdot, t)\rVert_{L^2}^2
  + 2\nu_q \int_0^t
  \sum_{k=1}^\infty [k]_q^2|\hat{v}_k(s)|^2ds
   \leq 
  \lVert v_0\rVert_{L^2}^2
$$

for all $t \geq 0$.

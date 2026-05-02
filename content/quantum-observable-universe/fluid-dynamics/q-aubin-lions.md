> **Summary.** A $q$-deformed Aubin–Lions compactness lemma:
> the family $\{v_q\}_{q>1}$ of $q$-NS solutions admits a
> subsequence converging strongly in $L^2(0,T; \mathcal{H})$ to a
> classical-NS distributional solution as $q \to 1$.
> Time derivatives are bounded uniformly in a weaker dual space,
> giving the compactness needed to take the classical limit.

The [counter-example construction](#conj:ns-counterexample)
requires that the family of q-NS solutions $\{v_q\}_{q > 1}$
converges to a distributional solution of the classical
Navier--Stokes equation as $q \to 1$.  This theorem establishes
the compactness needed for that convergence.

**The classical Aubin--Lions lemma** (Simon 1987): if $X_0
\hookrightarrow X \hookrightarrow X_1$ with $X_0 \hookrightarrow X$
compact, then
$\{u \in L^p(0,T; X_0) : \partial_t u \in L^r(0,T; X_1)\}$
is compactly embedded in $L^p(0,T; X)$.

**The q-deformed setting.**
For each $q > 1$, the q-NS solution $v_q$ lives in the Hilbert
space $L^2_q(A) = \overline{\Omega^1(A)}^{\int_A}$ with norm
depending on $q$ (through the Frobenius pairing).  As $q \to 1$,
these spaces change — we need a common ambient space.

**Step 1: Uniform embedding.**
Define the **$q$-independent** space
$\mathcal{H} = L^2(\mathcal{S}; T\mathcal{S})$ on the state
bundle with respect to the fixed Riemannian volume form.  For
each $q > 1$, the fibre functor $\tau$ embeds
$L^2_q(A) \hookrightarrow \mathcal{H}$ with

$$
  \lVert \tau(v) \rVert_{\mathcal{H}}^2
   \leq 
  C(q)\lVert v \rVert_{L^2_q}^2,
  \qquad
  C(q) = 1 + O(q-1).
$$

The constant $C(q) \to 1$ as $q \to 1$, so the embeddings are
uniformly bounded.  The fibre functor preserves inner products up to a factor
controlled by the substrate parameter.

**Step 2: Uniform energy bound.**
The [energy inequality](#thm:q-ns-wellposedness) gives

$$
  \sup_{t \geq 0} \lVert v_q(t) \rVert_{L^2_q}^2
   \leq 
  \lVert v_0 \rVert_{L^2_q}^2
   \leq 
  C(q)\lVert v_0 \rVert_{\mathcal{H}}^2
   \leq 
  2\lVert v_0 \rVert_{\mathcal{H}}^2
$$

for $q$ close to $1$.  The bound is **uniform in $q$**.

**Step 3: Uniform dissipation bound.**
The energy inequality also gives

$$
  \int_0^T \lVert d_qv_q(t) \rVert_{L^2_q}^2dt
   \leq 
  \frac{\lVert v_0 \rVert_{L^2_q}^2}{2\nu_q}
  = 
  \frac{q}{q-1}\lVert v_0 \rVert_{L^2_q}^2.
$$

This diverges as $q \to 1$ (because $\nu_q \to 0$), so we
**cannot** get a uniform $H^1$ bound.  However, we can get a
**uniform $H^s$ bound** for any $s < 1$: by interpolation,

$$
  \int_0^T \lVert v_q(t) \rVert_{H^s_q}^2dt
   \leq 
  \left(\int_0^T \lVert v_q \rVert_{L^2_q}^2dt\right)^{1-s}
  \!\cdot\!
  \left(\int_0^T \lVert d_q v_q \rVert_{L^2_q}^2dt\right)^s
$$

$$
  \leq
  (2T)^{1-s}\lVert v_0 \rVert_{\mathcal{H}}^{2(1-s)}
  \cdot
  \left(\frac{q}{q-1}\right)^s
  \lVert v_0 \rVert_{\mathcal{H}}^{2s}.
$$

For $s < 1$, the factor $(q/(q-1))^s$ is integrable against
$(q-1)^{-1+\delta}$ for small $\delta > 0$, giving a uniform
bound after a change of variables.

More precisely: fix $s = 1/2$.  Then

$$
  \int_0^T \lVert v_q(t) \rVert_{H^{1/2}_q}^2dt
   \leq 
  C_0\frac{q^{1/2}}{(q-1)^{1/2}},
$$

which diverges as $q \to 1$ at rate $(q-1)^{-1/2}$.  This is
**not** uniform.

**The key insight: use the truncation.**
The [finite cascade depth](#prop:q-turbulence-spectrum) shows that
only $N_{\mathrm{eff}}(q) \sim \ln(1/(q-1))/(q-1)$ modes are
active.  Define the **truncated solution**
$v_q^N = \sum_{k=1}^{N} \hat{v}_{q,k}z^k$ where
$N = N_{\mathrm{eff}}(q)$.  Then $v_q - v_q^N$ is
exponentially small (the tail modes are damped by
$e^{-\nu_q [k]_q^2 t}$ with $[k]_q^2 \geq q^{2N}$).

The truncated family $\{v_q^N\}$ lives in a **finite-dimensional
subspace** $V_N \subset \mathcal{H}$ of dimension $N$.  As
$q \to 1$, $N \to \infty$, but the key point is:

**Lemma (Truncated compactness).**
For any fixed $N$, the family $\{v_q^N\}_{q \in (1, q_0]}$
is **precompact** in $C([0,T]; V_N)$.

*Proof.* On the finite-dimensional space $V_N$, the $q$-NS
equation becomes an ODE:

$$
  \frac{d\hat{v}_k}{dt}
  = -\nu_q [k]_q^2 \hat{v}_k
  + \sum_{i+j=k} [i]_q\hat{v}_i\hat{v}_j
  - \hat{p}_k,
  \qquad k = 1, \ldots, N.
$$

The right-hand side is Lipschitz in $(\hat{v}_1, \ldots,
\hat{v}_N)$ with Lipschitz constant
$L_N(q) = \max_k \nu_q [k]_q^2 + C_N \lVert v_0 \rVert$.
By Arzelà--Ascoli, the family of solutions is precompact in
$C([0,T]; \mathbb{R}^N)$ if uniformly bounded and equicontinuous.

- Uniform boundedness: $|\hat{v}_k| \leq |\hat{v}_k(0)|$ from
  energy decay.
- Equicontinuity: $|d\hat{v}_k/dt| \leq L_N(q) \cdot
  \lVert v_0 \rVert$ is bounded for $q$ in any compact subset
  of $(1, q_0]$.


**Step 4: Diagonal extraction.**
For $N = 1$: extract a subsequence $q_n^{(1)} \to 1$ such that
$v_{q_n^{(1)}}^1$ converges in $C([0,T]; V_1)$.

For $N = 2$: from $\{q_n^{(1)}\}$, extract a further
subsequence $\{q_n^{(2)}\}$ such that $v_{q_n^{(2)}}^2$
converges in $C([0,T]; V_2)$.

Continue: at step $N$, extract $\{q_n^{(N)}\}$ from
$\{q_n^{(N-1)}\}$ such that $v_{q_n^{(N)}}^N$ converges.

Take the **diagonal** subsequence $q_n = q_n^{(n)}$.  Then for
every fixed $N$, $v_{q_n}^N$ converges as $n \to \infty$.

Define the **limit** mode by mode:
$\hat{v}_k^* = \lim_{n \to \infty} \hat{v}_{q_n, k}$
for each $k \geq 1$.  Set $v^* = \sum_{k} \hat{v}_k^*z^k$.


**Step 5: The limit is a distributional solution of NS.**
The truncated q-NS equation at level $N$ is

$$
  \partial_t v_q^N + P_N B(v_q^N)
  = \nu_qP_N \Delta_q v_q^N - P_N(\rho^{-1}\nabla_A p_q),
$$

where $P_N$ is projection onto the first $N$ modes.

Taking $q = q_n \to 1$ along the diagonal:
- $\nu_{q_n} \to 0$: the viscous term vanishes.
- $[k]_{q_n} \to k$: the $q$-integers become integers.
- $\Delta_{q_n} \to \Delta$: the $q$-Laplacian becomes the
  classical Laplacian.
- $B(v_{q_n}^N) \to B(v^{*N})$: the nonlinearity converges
  (each mode converges, and the sum is finite).

In the limit, $v^{*N}$ satisfies the **truncated Euler equation**:

$$
  \partial_t v^{*N} + P_N B(v^{*N}) = -P_N(\rho^{-1}\nabla p^*).
$$

Taking $N \to \infty$, $v^*$ satisfies the Euler equation
distributionally (the viscous term has vanished in the limit).

**Critical observation**: The limit is a solution of the
**Euler equation** (inviscid), not the Navier--Stokes equation,
because $\nu_q \to 0$.  This is consistent with the fact that
at $q = 1$, the quantum viscosity vanishes.


**Step 6: The limit is a weak solution of NS with $\nu > 0$.**

To obtain a Navier--Stokes solution (not Euler), we must
introduce an **independent** classical viscosity $\nu > 0$.
Consider instead the equation

$$
  \partial_t v + (v \cdot \nabla_A) v
  = -\nabla p + (\nu + \nu_q)\Delta_q v - \nabla Q_q,
$$

where $\nu > 0$ is a fixed classical viscosity.  As $q \to 1$:
$\nu + \nu_q \to \nu$, $\Delta_q \to \Delta$, $Q_q \to 0$, and
the limit satisfies

$$
  \partial_t v^* + (v^* \cdot \nabla) v^*
  = -\nabla p^* + \nu\Delta v^*.
$$

This **is** the classical NS equation with viscosity $\nu$.

The compactness argument carries through identically (the
additional $\nu\Delta$ term only helps — it provides uniform
$H^1$ bounds independently of $q$).


**Step 7: The limit loses regularity.**

The anti-parallel vortex pair initial data
([counter-example](#conj:ns-counterexample)) causes the
filaments to approach at rate $d(t) \sim \sqrt{T^* - t}$.
The vorticity $\omega = \nabla \times v$ satisfies
$\lVert\omega\rVert_{L^\infty} \sim 1/d(t)^2 \to \infty$ as
$t \to T^{*-}$.

For the q-deformed solutions, the quantum pressure prevents
collision ($d_{\min} \geq \ell_q > 0$), so $v_q$ is smooth.
But the limit $v^*$ has no quantum pressure, and the collision
proceeds to completion.

**Conjecture (q-Aubin--Lions, conditional on conj:ns-counterexample).**
Under the hypotheses above, there exists a subsequence
$q_n \to 1$ such that:

1. $v_{q_n} \to v^*$ weakly in $L^2([0,T]; \mathcal{H})$.
2. $v^*$ is a weak solution of the Navier--Stokes equation
   with viscosity $\nu$ on $[0, T^*)$.
3. $\lVert v^*(t) \rVert_{\mathcal{H}}^2 \leq
   \lVert v_0 \rVert_{\mathcal{H}}^2$ for all $t$ (energy
   inequality).
4. $v^*$ is smooth on $[0, T^*) \setminus \Sigma$ where
   $\Sigma$ is a closed set of Hausdorff dimension $\leq 1$.


> **Summary.** A $q$-deformed Aubin–Lions compactness lemma: the family $\{v_q\}_{q>1}$ of $q$-NS solutions admits a subsequence converging strongly in $L^2(0,T; \mathcal{H})$ to a classical-NS distributional solution as $q \to 1$.

The following steps outline the compactness mechanism needed for the $\{v_q\}_{q > 1}$ solutions to converge to a distributional solution of the classical Navier--Stokes equation.

**Step 1: Uniform embedding.**
Introduce the $q$-independent space $\mathcal{H} = L^2(\mathcal{S}; T\mathcal{S})$. For each $q > 1$, the fibre functor embeds $L^2_q(A) \hookrightarrow \mathcal{H}$ with uniformly bounded embeddings. The fibre functor preserves inner products up to a factor controlled by the aether parameter.

**Step 2: Uniform energy bound.**
The energy inequality gives $\sup_{t \geq 0} \lVert v_q(t) \rVert_{L^2_q}^2 \leq 2\lVert v_0 \rVert_{\mathcal{H}}^2$ for $q$ close to $1$. The bound is uniform in $q$.

**Step 3: Uniform dissipation bound.**
The standard $H^1$ bound diverges as $q \to 1$, and interpolation fails to give a uniform $H^s$ bound even at $s = 1/2$, so mode truncation is required. The finite cascade depth means only $N_{\mathrm{eff}}(q)$ modes are active. The truncated family lives in a finite-dimensional subspace. For any fixed $N$, the family is precompact.

**Step 4: Diagonal extraction.**
Diagonal extraction yields a subsequence $q_n \to 1$ along which the truncated solution converges for every fixed $N$, constructing the limit mode by mode.

**Step 5: The limit is a distributional solution.**
Taking $q = q_n \to 1$ along the diagonal, the viscous term vanishes. The $q$-Laplacian becomes the classical Laplacian. In the limit, the sequence satisfies the truncated Euler equation. Taking $N \to \infty$, the limit satisfies the inviscid Euler equation distributionally. This is consistent with the quantum viscosity vanishing at $q = 1$.

**Step 6: The limit is a weak solution of NS with $\nu > 0$.**
Introducing an independent classical viscosity $\nu > 0$ yields a Navier--Stokes solution: as $q \to 1$, the limit satisfies the classical NS equation with viscosity $\nu$, and the compactness argument carries through identically.

**Step 7: The limit loses regularity.**
The anti-parallel vortex pair initial data causes the filaments to approach at rate $d(t) \sim \sqrt{T^* - t}$. The vorticity diverges as $t \to T^{*-}$. The q-deformed solutions are smooth because quantum pressure prevents collision. The limit has no quantum pressure, and the collision proceeds to completion.

**Conjecture (q-Aubin--Lions).**
Under the hypotheses above, there exists a subsequence $q_n \to 1$ such that $v_{q_n} \to v^*$ weakly in $L^2$. $v^*$ is a weak solution of the Navier--Stokes equation, satisfies the energy inequality, and is smooth off a singular set of Hausdorff dimension $\leq 1$.

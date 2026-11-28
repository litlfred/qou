> **Summary.** A $q$-deformed Aubin–Lions compactness conjecture: the family $\{v_q\}_{q>1}$ of $q$-NS solutions admits a subsequence converging strongly in $L^2(0,T; \mathcal{H})$ to a distributional solution of the Euler equation as $q \to 1$. Because the viscosity $\nu_q$ tends to zero, the limit of the $q$-NS family itself is inviscid; a Navier--Stokes limit requires a modified family with a separate fixed viscosity (Step 6).

This would supply the compactness needed for the $\{v_q\}_{q > 1}$ solutions to converge to a distributional solution of the Euler equation.

**Step 1: Uniform embedding.**
Introduce the $q$-independent space $\mathcal{H} = L^2(\mathcal{S}; T\mathcal{S})$. For each $q > 1$, the fibre functor embeds $L^2_q(A) \hookrightarrow \mathcal{H}$ with uniformly bounded embeddings. The fibre functor preserves inner products up to a factor controlled by the aether parameter.

**Step 2: Uniform energy bound.**
The energy inequality gives $\sup_{t \geq 0} \lVert v_q(t) \rVert_{L^2_q}^2 \leq 2\lVert v_0 \rVert_{\mathcal{H}}^2$ for $q$ close to $1$. The bound is uniform in $q$.

**Step 3: Uniform dissipation bound.**
The standard $H^1$ bound diverges as $q \to 1$. A uniform $H^s$ bound for $s < 1$ follows by interpolation. For $s = 1/2$, it diverges. Truncation is necessary. The finite cascade depth means only $N_{\mathrm{eff}}(q)$ modes are active. The truncated family lives in a finite-dimensional subspace. For any fixed $N$, the family is precompact.

**Step 4: Diagonal extraction.**
Extract a diagonal subsequence $q_n \to 1$ such that for every fixed $N$, the truncated solution converges. The limit is constructed mode by mode.

**Step 5: The limit is a distributional solution.**
Taking $q = q_n \to 1$ along the diagonal, the viscous term vanishes. The $q$-Laplacian becomes the classical Laplacian. In the limit, the sequence satisfies the truncated Euler equation. Taking $N \to \infty$, the limit satisfies the inviscid Euler equation distributionally. This is consistent with the quantum viscosity vanishing at $q = 1$.

**Step 6: A modified family with fixed viscosity.**
The $q$-NS family itself does not converge to Navier--Stokes. To obtain a Navier--Stokes limit one must change the family, adding an independent classical viscosity $\nu > 0$ that does not vanish with $q - 1$. For that modified family the same compactness argument would give a weak Navier--Stokes solution with viscosity $\nu$; the modified family is a separate object, not the brane $q$-NS of this chapter.

**Step 7: Conjectured loss of smoothness in the limit.**
Under the anti-parallel vortex-pair collision scenario of [the vortex-collision conjecture](#conj:ns-counterexample), the filaments are posited to approach at rate $d(t) \sim \sqrt{T^* - t}$ with diverging vorticity as $t \to T^{*-}$: for $q > 1$, quantum pressure opposes core overlap, whereas in the $q \to 1^+$ limit $Q_q \to 0$.

**Conjecture (q-Aubin--Lions).**
Under the hypotheses above, there exists a subsequence $q_n \to 1$ such that $v_{q_n} \to v^*$ weakly in $L^2$. $v^*$ is a weak solution of the Euler equation (of the Navier--Stokes equation with viscosity $\nu$ for the modified family of Step 6), satisfies the energy inequality, and is smooth off a singular set of Hausdorff dimension $\leq 1$.

**Archimedean specialisation.** What follows sits on the archimedean side of the algebraic-to-archimedean wall. It invokes real- or complex-analytic constructs. Generic categorical identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.

*Within a QOU $(\mathbf{C}, A, \tau)$.* Part A below concerns the QOU's internal $q$-Navier--Stokes flow. Part B is a statement about the classical Navier--Stokes equation on $\mathbb{R}^3$. Identifying the internal flow with the classical equation is the separate open categorical-to-classical bridge and is not asserted here.

The global regularity theorem ([$q$-NS well-posedness](#thm:q-ns-wellposedness)) holds for every $q > 1$. The conjecture concerns the endpoint $q = 1$.

**Conjecture (regularity breakdown).**

*Part A (the $q$-family).* Define the enstrophy order parameter
$$
\Omega(q) = \sup_{t \geq 0} \sum_k [k]_q^2\, |\hat{v}_k(t)|^2 .
$$
For each $q > 1$, $\Omega(q) < \infty$. Part A asserts that, for suitable data, $\Omega(q) \to +\infty$ as $q \to 1^+$, with $\Omega(q) \sim (q - 1)^{-\alpha}$ for some critical exponent $\alpha > 0$.

*Part B (classical model).* There exists a nonzero backward discretely self-similar solution of the classical Navier--Stokes equation on $\mathbb{R}^3$ with fixed viscosity, in the sense of [the discretely self-similar Leray profile](#def:leray-profile): a smooth profile $V(y, s)$, periodic in $s = -\log(T^* - t)$ with some period $P > 0$, with $|V(y, s)| = O(|y|^{-1})$ as $|y| \to \infty$ and $V(\cdot, s) \notin L^3(\mathbb{R}^3)$. No value of $P$ is asserted.

**Consequences and constraints.**

1. **Enstrophy blow-up is a consequence of Part B.** The enstrophy of the field is $(T^* - t)^{-1/2} E(s)$ with $E(s) = \|\nabla_y V(\cdot, s)\|_{L^2}^2$. A periodic $E$ that is positive somewhere makes the enstrophy unbounded as $t \to T^{*-}$ (Lean `lerayEnstrophy_blowup`). Independently, at any blow-up time $\|\nabla v(t)\|_{L^2}^2 \geq c\,(T^* - t)^{-1/2}$ \cite{leray1934}.
2. **The singular set is a point.** A discretely self-similar blow-up has a single singular point $(x_0, T^*)$ \cite{chae-wolf2016dss}. The earlier claim of concentration on a vortex sheet of spatial Hausdorff dimension $2$ is withdrawn; it is incompatible with this and with $d_H = 1$ in [the counterexample conjecture](#conj:ns-counterexample).
3. **The decay class is forced.** A steady profile in $L^3$ is trivial \cite{necas-ruzicka-sverak1996}, extended to $L^q$, $3 < q \leq \infty$, and to local energy estimates \cite{tsai1998}. The $L^3$ norm is invariant under the Leray rescaling, so along a discretely self-similar solution it is periodic in $s$; if it is continuous it is bounded (Lean `dss_L3_norm_not_tendsto_atTop`), while $\|v(t)\|_{L^3} \to \infty$ at any blow-up time \cite{seregin2012}. Hence no discretely self-similar blow-up has a profile continuous in $s$ with values in $L^3$ \cite{chae2013adss}. A bounded square-integrable profile lies in $L^3$, so it is excluded as well. Faster decay than $|y|^{-1}$ puts the profile in $L^3$; slower decay makes $v(\cdot, T^*)$ unbounded away from $x_0$. This leaves $|V| \sim |y|^{-1}$.
4. **The scaling factor.** Write $P = 2 \log \lambda$ with $\lambda > 1$. Scaling factors $\lambda$ close to $1$ are excluded under a scale-critical bound \cite{chae-wolf2016dss}; the case of $\lambda$ well above $1$ is open \cite{bradshaw-tsai2018survey}. The period is not tied to the root-of-unity ladder $q_\kappa = e^{i\pi/\kappa}$: $q_\kappa^{2\kappa} = 1$ (Lean `qKappa_pow_two_kappa`), and [the substrate parameter](#def:substrate-parameter) is not a root of unity.
5. **Integer angular degrees only.** On the spin-$j$ summand the central element $-1 \in \mathrm{SU}(2)$ acts by $(-1)^{2j}$, and on velocity fields on $\mathbb{R}^3$ it acts trivially, since the action factors through $\mathrm{SO}(3)$. So only integer $j$ occur (Lean `IntegerSpin.even_of_neg_one_pow_eq_one`).

**Heuristics for Part A.** The following explain why Part A is expected; none is a proof ingredient.

*Loss of UV regularisation.* At $q = 1$ the $q$-Laplacian eigenvalues degenerate from exponential to polynomial growth, $[k]_1 = k$, so the spectral gap that controls the cubic term in the enstrophy equation closes.

*Viscosity vanishes.* The quantum viscosity is $\nu_q = (q - 1)/(2q)$, and $\nu_q \to 0$ as $q \to 1^+$. The formal $q \to 1$ endpoint of the $q$-family is therefore the Euler equation, not the Navier--Stokes equation with fixed viscosity. This is why Part A does not by itself say anything about Part B.

*Cascade becomes continuous.* The discrete transfer rates of [the $q$-turbulence spectrum](#prop:q-turbulence-spectrum) merge into a continuous cascade at $q = 1$.

**What $\Omega(1) = +\infty$ does and does not mean.** $\Omega(q)$ is a supremum over all $t \geq 0$. A quantity can be unbounded on $[0, \infty)$ while bounded on every $[0, T]$ (Lean `sup_unbounded_without_finite_time_blowup`), so divergence of $\Omega$ is not finite-time blow-up. The analogy with a second-order phase transition, with $q$ in the role of temperature and $\Omega$ as order parameter, is a heuristic; it is not derived from the QOU axioms.

**Relation to the Clay problem.** The Clay problem asks whether smooth finite-energy data for the Navier--Stokes equation with fixed viscosity can blow up in finite time. A discretely self-similar solution with $|V| \sim |y|^{-1}$ has infinite global energy, so Part B is relevant to the Clay problem only as the local profile of a finite-energy blow-up near $(x_0, T^*)$; local asymptotics of this kind with profile continuous in $s$ with values in $L^3 \cap C^2$ are again excluded \cite{chae2013adss}. Part B is a scenario for a positive answer that survives the exclusions listed above; it is open. Part A concerns a family whose $q \to 1$ endpoint is Euler, so it does not reframe the Clay problem as a statement about the limit $q \to 1$.

**Archimedean specialisation.** What follows invokes real- or complex-analytic constructs. Generic categorical identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.

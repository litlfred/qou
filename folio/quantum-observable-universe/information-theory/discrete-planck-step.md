Discretizing the continuous Reeb flow $\phi_t^q$ ([$q$-Reeb flow](#ex:q-reeb-flow)) at the Big Bang—where the substrate parameter $q \to \infty$ and the quantum Planck constant $\hbar_q = 1 - q^{-1} \to 1$ ([quantum Planck constant](#def:quantum-planck-constant))—defines a **Planck step**, the minimal dynamical time unit of the QOU. Time is discrete at the origin.

**Algebraic normalization.**
The $q$-deformed Reeb flow rotates the affine coordinate $Z$ of a state ([substrate radial coordinate](#prop:substrate-radial-coordinate)):

$$
  \mathcal{L}_\xi Z = J\hbar_q Z.
$$

The naive period of this rotation is $T = 2\pi/\hbar_q$. The transcendental factor $2\pi$ obstructs finite-field and $p$-adic realisations ([finite field realisation](#ex:finite-field-realisation), [Witt vector lift](#rem:witt-lift-qou)). Normalising one full Reeb circuit as **one unit of time** eliminates this factor:

$$
  t_P(q)  :=  \frac{1}{\hbar_q}
  =  \frac{1}{1 - q^{-1}}
  =  \frac{q}{q - 1}.
$$

Because $t_P(q)$ is a rational function, it is well-defined over any field $k$ where $q \neq 1$.
- Over $\mathbb{F}_\pp$: $t_P = q/(q-1) \in \mathbb{F}_\pp$ for $q \in \mathbb{F}_\pp^\times \setminus \{1\}$.
- Over $\mathbb{Q}_\pp$: $t_P \in \mathbb{Q}_\pp$. Its $\pp$-adic valuation $v_\pp(t_P) = v_\pp(q) - v_\pp(q-1)$ encodes proximity to the classical limit.
- Over $\mathbb{C}$: It reproduces the angular period up to $2\pi$.

The Planck step acts as the polynomial iteration $f_q(z) = z^2 + c(q)$ ([Julia set of Reeb flow](#rem:julia-set-reeb)).

**Limits.**

| Regime | $q$ | $\hbar_q$ | $t_P$ | Interpretation |
|--------|-----|-----------|-------|----------------|
| Big Bang | $q \to \infty$ | $\to 1$ | $\to 1$ | Minimal step; time is fastest |
| Physical | $q = q_0$ ([local substrate $q$](#prop:local-substrate-q)) | $0.0988$ | $\approx 10.1$ | Local Planck time |
| Classical | $q \to 1$ | $\to 0$ | $\to \infty$ | No Reeb period; time freezes |

At the Big Bang, $t_P \to 1$. One Planck step exactly equals one unit. The continuous Reeb flow is merely the $\mathbb{R}$-shadow of this discrete iteration. There is no sub-step resolution.

**One Planck length of flow.**
After one Planck step, the Reeb flow displaces a state by exactly one Planck length:

$$
  \ell_P(q)
  =  \hbar_q \cdot t_P
  =  (1 - q^{-1}) \cdot \frac{q}{q-1}
  =  1.
$$

This is the **normalised total** --- one full Reeb circuit, an angular displacement carrying no length scale --- and it evaluates to $1$ over any field precisely because $\hbar_q$ is its per-step share (see [share versus total](#rem:planck-length-share-vs-total)). It is not the same object as the local $\ell_P^{\mathrm{step}} \sim \hbar_q$ of [the Planck information unit](#sec:planck-info-unit). The angular velocity $\hbar_q$ changes with $q$. At the Big Bang, the fiber is traversed at maximum speed ($\hbar_q = 1$). Near heat death, the rotation halts.

**Discrete time at the Big Bang.**
The Big Bang initial state ([bundle initial conditions](#def:bundle-initial-conditions)) is a formal sum $\mathcal{S}_0 = \sum_i (p_i, H_i)$. It specifies fiber data without horizontal transport. The **first Planck step** $\phi_1^q$ applies horizontal transport for the first time. It connects neighboring fibers, initiates the $q$-connection, and begins information propagation across the brane.

Before the first step, position is known exactly but momentum is entirely undetermined. After one step, the $q$-connection $\nabla_q$ correlates adjacent fibers. It produces the first non-trivial holonomy. The Heisenberg commutator $[\hat{X}, \hat{P}]_q = J\hbar_q \approx J$ is near-maximal. The first tick of time maximizes uncertainty.

Over $\mathbb{F}_\pp$, this first step evaluates $f_q$ once: $z_1 = z_0^2 + c(q)$. The first moment after the Big Bang is a single polynomial evaluation.

**Counting Planck steps.**
The count of Planck steps measures dynamical distance in Reeb time. From the Big Bang ($q_0 \gg 1$) to the local substrate ($q = q_0$):

$$
  N(q_0, q)
  =  \int_{q}^{q_0}
  \frac{dq'}{t_P(q')\dot{q}(q')}
$$

where $\dot{q}$ is the coordinate time derivative of the substrate parameter. Over $\mathbb{F}_\pp$, the integral becomes a finite sum.

**Information per step.**
Each Planck step propagates information across one fiber. The information content per step is bounded by the Julia-set Hausdorff dimension $d_H(q)$ ([Julia set of Reeb flow](#rem:julia-set-reeb)) over $\mathbb{C}$, or by the orbit complexity of $f_q$ over $\mathbb{F}_\pp$. At the Big Bang, the dynamics is simplest and each step carries minimal information. As $q$ approaches the golden threshold, the complexity peaks. The universe processes information faster as it cools, reaching peak capacity near the golden ratio.

**Relation to 't Hooft's ontological CA.**
't Hooft \cite{thooft2016} posits a Planck-scale tick as the elementary time unit of a deterministic cellular automaton. The Planck step $t_P(q) = q/(q-1)$ realizes this tick. It is algebraically derived from the substrate parameter $q$ rather than posited independently. It recovers the dimensional Planck time via the archimedean realisation at $q_0$.

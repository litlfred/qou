The continuous Reeb flow $\phi_t^q$
([$q$-Reeb flow](#ex:q-reeb-flow)) admits a natural discretization
at the Big Bang, where the substrate parameter $q \to \infty$ and
the quantum Planck constant $\hbar_q = 1 - q^{-1} \to 1$
([quantum Planck constant](#def:quantum-planck-constant)).  This
defines a **Planck step** — the minimal dynamical time unit of the
QOU — and makes time discrete at the origin.

**Algebraic normalization.**
The $q$-deformed Reeb flow rotates the affine coordinate $Z$ of a
state ([substrate radial coordinate](#prop:substrate-radial-coordinate)):

$$
  \mathcal{L}_\xiZ =  J\hbar_qZ.
$$

The naive period of this rotation is $T = 2\pi/\hbar_q$, but the
factor $2\pi$ is transcendental — it exists only over
$\mathbb{R}$ or $\mathbb{C}$ and obstructs the finite-field and
$p$-adic realisations
([finite field realisation](#ex:finite-field-realisation),
[Witt vector lift](#rem:witt-lift-qou)).  We normalize instead by
defining one full Reeb circuit as **one unit of time**:

$$
  t_P(q)  :=  \frac{1}{\hbar_q}
  =  \frac{1}{1 - q^{-1}}
  =  \frac{q}{q - 1}.
$$

This is a **rational function of $q$** — it makes sense over any
field $k$ in which $q \neq 1$.  In particular:

- Over $\mathbb{F}_\pp$: $t_P = q/(q-1) \in \mathbb{F}_\pp$
  whenever $q \in \mathbb{F}_\pp^\times \setminus \{1\}$.
- Over $\mathbb{Q}_\pp$: $t_P \in \mathbb{Q}_\pp$, and its
  $\pp$-adic valuation $v_\pp(t_P) = v_\pp(q) - v_\pp(q-1)$
  encodes the arithmetic proximity of $q$ to the classical limit.
- Over $\mathbb{C}$: reproduces the angular period up to the
  conventional factor $2\pi$ (which can be restored by
  $T = 2\pi \cdot t_P$ when working over $\mathbb{R}$).

The Planck step is the iteration
$f_q(z) = z^2 + c(q)$
([Julia set of Reeb flow](#rem:julia-set-reeb)) — one application
of the discrete dynamical system.  This iteration is polynomial and
works over any field.

**Limits.**

| Regime | $q$ | $\hbar_q$ | $t_P$ | Interpretation |
|--------|-----|-----------|-------|----------------|
| Big Bang | $q \to \infty$ | $\to 1$ | $\to 1$ | Minimal step; time is fastest |
| Physical | $q = q_0$ ([local substrate $q$](#prop:local-substrate-q)) | $0.0988$ | $\approx 10.1$ | Our Planck time |
| Classical | $q \to 1$ | $\to 0$ | $\to \infty$ | No Reeb period; time freezes |

At the Big Bang, $t_P \to 1$: **one Planck step equals one unit**.
Time is discrete in the strongest sense — the dynamical system is
an iterated map with step size $1$, and there is no sub-step
resolution.  The continuous Reeb flow is the $\mathbb{R}$-shadow of
this discrete algebraic iteration.

**One Planck length of flow.**
After one Planck step, the Reeb flow displaces a state by

$$
  \ell_P(q)
  =  \hbar_q \cdot t_P
  =  (1 - q^{-1}) \cdot \frac{q}{q-1}
  =  1.
$$

The Planck length is **identically $1$** over any field.  What
changes with $q$ is the angular velocity $\hbar_q$ — at the Big Bang
the fiber is traversed at maximum speed ($\hbar_q = 1$), while near
heat death the rotation slows to zero.

**Discrete time at the Big Bang.**
The Big Bang initial state
([bundle initial conditions](#def:bundle-initial-conditions)) is a
formal sum $\mathcal{S}_0 = \sum_i (p_i, H_i)$ specifying fiber
data without horizontal transport.  The **first Planck step**
$\phi_1^q$ is the first application of horizontal transport:
it connects neighboring fibers for the first time, initiating the
$q$-connection and beginning the propagation of information across
the brane.

Before this step: position is known exactly, momentum is entirely
undetermined (Big Bang complementarity).  After one step: the
$q$-connection $\nabla_q$ has acted once, correlating adjacent
fibers and producing the first non-trivial holonomy.  The
Heisenberg commutator $[\hat{X}, \hat{P}]_q = J\hbar_q \approx J$
is near-maximal — the first tick of time is also the moment of
greatest uncertainty.

Over $\mathbb{F}_\pp$, this first step is literally $f_q$ applied
once: $z_1 = z_0^2 + c(q)$.  The "first moment after the Big Bang"
is a single polynomial evaluation.

**Counting Planck steps.**
The number of Planck steps between two values of $q$ measures the
dynamical "distance" in Reeb time.  From the Big Bang ($q_0 \gg 1$)
to our universe ($q = q_0$, [local substrate $q$](#prop:local-substrate-q)):

$$
  N(q_0, q)
  =  \int_{q}^{q_0}
  \frac{dq'}{t_P(q')\dot{q}(q')}
$$

where $\dot{q}$ is the rate of change of the substrate parameter
with respect to coordinate time.  Over $\mathbb{F}_\pp$ this
integral is replaced by a sum over discrete $q$-values, and $N$ is
a finite count.

**Information per step.**
Each Planck step propagates information across one fiber's worth of
the brane.  The information content per step is bounded by the
Julia-set Hausdorff dimension $d_H(q)$
([Julia set of Reeb flow](#rem:julia-set-reeb)) over $\mathbb{C}$,
or by the orbit complexity of $f_q$ over $\mathbb{F}_\pp$.  At the
Big Bang ($q \to \infty$ over $\mathbb{C}$, or $q$ with
$v_\pp(q-1) = 0$ over $\mathbb{Q}_\pp$), the dynamics is simplest
— each step carries minimal information.  As $q$ approaches the
golden threshold, the orbit structure (finite field) or fractal
complexity (complex) peaks, and each Planck step carries more
information.  The universe's information processing rate
**increases** as it cools from the Big Bang, reaching peak capacity
near the golden ratio before the fiber degenerates.

**Relation to 't Hooft's ontological CA.**
't Hooft \cite{thooft2016} introduces a Planck-scale tick as the
elementary time unit of a deterministic cellular automaton
underlying quantum mechanics.  The Planck step $t_P(q) = q/(q-1)$
is the QOU realisation of this tick: it is algebraically
determined by the substrate parameter $q$ rather than posited
independently, and it recovers the dimensional Planck time via the
archimedean functor at $q_0$.

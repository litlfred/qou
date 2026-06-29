The discrete Planck step ([discrete Planck step](#rem:discrete-planck-step))
and the jet prolongation tower
([recursive brane tower](#def:recursive-brane-tower)) are the same
structure viewed from two directions: each Planck step $n$ reveals
the $n$-th jet of the energy function $E$ at the Big Bang, so
that the first few moments of the universe unfold as successively
higher Taylor approximations of $E$.

**Identification: Planck step $n$ = $n$-th jet.**
The brane tower
$A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$
is defined by $A_{n+1} = J^1(A_n)$
([jet prolongation](#prop:jet-prolongation)), where $J^1$ is the
first jet functor. Iterating $n$ times gives $A_n = J^n(A_0)$:
the $n$-th jet bundle of the original Frobenius--Hopf object.
This is the space of $n$-th order Taylor data of sections of
$\mathcal{S}$.

The Planck step ([discrete Planck step](#rem:discrete-planck-step))
is one application of the $q$-connection $\nabla_q$
([categorical $q$-connection](#def:categorical-q-connection)).
At the Big Bang, where $t_P = 1$, each step applies $\nabla_q$
once, and $\nabla_q$ acts on $A_n$ to produce $A_{n+1}$: the
connection promotes $n$-th order data to $(n+1)$-th order data.
**One Planck step = one jet prolongation = one additional order in
the Taylor expansion of $E$.**

**The first four Planck steps.**

Let $E$ be the energy functional on the state bundle $\mathcal{S}$.
At the Big Bang initial state
([bundle initial conditions](#def:bundle-initial-conditions)),
$E$ is concentrated at a point — the primordial vortex. Each
Planck step reveals the next derivative:

**Step 0: the value.** $J^0(E) = E(p_0)$.

The zeroth jet is the function value at the Big Bang point
$p_0$. This is the **position-only** specification: fibre data
with no transport. No derivatives, no connection, no geometry —
the raw energy at a point. Over $\mathbb{F}_\pp$: a single
element of $\mathbb{F}_\pp$.

**Step 1: the linear approximation.** $J^1(E) = E(p_0) + dE|_{p_0} \cdot \delta p$.

The first jet is the tangent — the first application of $\nabla_q$.
This is the **first horizontal transport**: the connection
correlates the fiber at $p_0$ with neighboring fibers for the first
time, producing a linear approximation of $E$ near the vortex.
The local state space is $J^1\mathcal{S}$
([local states](#rem:j1e-local-states)).

Over any field $k$: a linear polynomial $a_0 + a_1 x$, two
coefficients. The dynamics at step 1 is that of a line — no
curvature, no structure beyond slope. The Heisenberg commutator
$[\hat{X}, \hat{P}]_q = J\hbar_q$ appears here: the linear
approximation already encodes the non-commutativity of position
and momentum.

**Step 2: the quadratic approximation.**
$J^2(E) = E + dE \cdot \delta p + \tfrac{1}{2}d^2E \cdot (\delta p)^2$.

The second jet introduces **curvature**. The connection applied
twice produces the Hessian $d^2E$: the quadratic form that
determines whether the energy is at a minimum, maximum, or saddle.
This is where the **Frobenius pairing**
$\langle f, g \rangle = \int_A(\mu(f \otimes g))$ first becomes
visible — the non-degeneracy of the pairing is a condition on the
Hessian.

Over any field: $a_0 + a_1 x + a_2 x^2$, three coefficients.
The discriminant $a_1^2 - 4a_0 a_2$ determines the nature of the
critical point. Over $\mathbb{F}_\pp$: whether the quadratic has
roots is a quadratic residue condition.

**Step 3: the cubic approximation.**
$J^3(E) = E + dE \cdot \delta p + \tfrac{1}{2}d^2 E \cdot (\delta p)^2 + \tfrac{1}{6}d^3 E \cdot (\delta p)^3$.

The third jet is where the **color structure appears**. The color
elliptic curve ([color elliptic](#prop:color-elliptic))

$$
  X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1) = 0
$$

is a cubic in $X$ — it is a **third-order approximation** of the
energy landscape in the chiral direction. The three roots
$X_1, X_2, X_3$ are the three color-tube coordinates of the Bring
surface.

This is the first step at which:

- **Elliptic structure** emerges: a generic cubic in Weierstrass
 form defines a genus-1 curve.
- **The golden ratio appears**: the factor $(s^2 + s - 1)$ in the
 Weierstrass coefficient $r(q)$ exists only because the polynomial
 is cubic — it would not arise at quadratic order
 ([golden ratio degeneration](#rem:golden-ratio-degeneration)).
- **Monodromy** becomes non-trivial: a cubic has a discriminant
 whose vanishing locus defines branch points, and loops around
 branch points generate the braid group $B_3$.
- **The trefoil** enters: the holonomy around the singular fibers
 of the chiral cubic generates $\pi_1(S^3 \setminus K_{3,2})$,
 the trefoil knot group.

Over $\mathbb{F}_\pp$: the cubic $X^3 + aX + b = 0$ has 0, 1, 2,
or 3 roots depending on the Legendre symbol
$\left(\frac{-4a^3 - 27b^2}{\pp}\right)$. The golden degeneration
($r = 0$, cubic reduces to $X^3 + pX$) is visible iff
$\varphi \in \mathbb{F}_\pp$, i.e., $\pp \equiv \pm 1 \pmod 5$.

**Convergence: $n \to \infty$ and the jet shell.**
As $n \to \infty$, the tower
$A_0 \hookrightarrow A_1 \hookrightarrow \cdots$ converges to the
jet shell $J^\infty E = \varprojlim J^k E$, which encodes the full
analytic germ of $E$ at the Big Bang. Over $\mathbb{C}$, this is
the Taylor series; over $\mathbb{Q}_\pp$, it is the $\pp$-adic
expansion; over $\mathbb{F}_\pp$, the tower stabilizes (since
$\mathbb{F}_\pp$ has only finitely many elements, the formal power
series truncates). The passage from discrete (finitely many Planck
steps) to continuous (the full jet shell) is the arithmetic version
of the cosmological progression from Big Bang to classical limit.

**Cubic as the highest independent jet.**
The Bring's surface is defined by constraints $\sum x_i = \sum x_i^2 = \sum x_i^3 = 0$ in $\mathbb{CP}^4$. The power-sum conditions
use degrees 1, 2, and 3 — exactly the first three non-trivial jets.
The fourth power sum $\sum x_i^4$ is *not* independent: by Newton's
identities it is determined by the lower power sums. The chiral
cubic exhausts the independent data, and the elliptic curve at
step 3 is the complete local model. Higher jets refine the global
geometry (higher-order moduli of the elliptic fibration) but do not
introduce new algebraic structure — the genus, monodromy, and golden
ratio are all present by step 3.

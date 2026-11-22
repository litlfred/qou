*Let $L$ be a Lipschitz seminorm on an algebra of observables, let $\varphi$ and
$\psi$ be states, and let*

$$
  d(\varphi,\psi) \;=\; \sup\,\bigl\{\, |\varphi(a) - \psi(a)| \;:\; L(a) \le 1 \,\bigr\}
$$

*be the associated Connes distance. If some $k$ satisfies $L(k) = 0$ while
$\varphi(k) \ne \psi(k)$, then the supremum is unbounded: for every proposed bound
$M$ there is an admissible $b$ with $|\varphi(b) - \psi(b)| > M$.*

## The argument in one line

Homogeneity and subadditivity give $L(a + tk) \le L(a) + |t|\,L(k) = L(a)$, so the
whole line $a + tk$ stays inside the unit ball of the seminorm, while the objective

$$
  \varphi(a+tk) - \psi(a+tk)
  \;=\; \bigl(\varphi(a)-\psi(a)\bigr) \;+\; t\,\bigl(\varphi(k)-\psi(k)\bigr)
$$

grows linearly in $t$. Choosing $t$ large enough overshoots any bound. The distance is
$+\infty$ as posed, not a hard computation.

Stating the conclusion as "no upper bound exists" rather than "$d = \infty$" keeps the
statement inside an ordered field, with no top element adjoined.

## Why the framework runs into it

The natural candidate for a derived metric on the state space is the Gram form of the
Markov trace: build a Lipschitz seminorm from it, take the Connes supremum, and read
off a distance. Under convention D that route is blocked before it starts. The star
form is positive semidefinite with a one-dimensional kernel --- the block killed by
the row cap --- and a kernel of the form is a kernel of the seminorm. Any state pair
separating that direction supplies the $k$ above.

The obstruction is a fact about the *method*, and it names its own repair: quotient by
the radical, or choose a different seminorm.

Under convention C the question does not arise. Every Wedderburn weight is strictly
positive there, the star form is definite, and no kernel element exists to exploit.
The blocker is specific to the convention that imposes the row cap.

**Archimedean specialisation.** What follows sits on the archimedean side of the
substrate wall: it invokes real- or complex-analytic constructs --- real-valued
physical observables, real-analytic bounds, transcendental constants, or numerical
evaluation at the substrate parameter $q_0$. Any generic categorical or
$q$-deformation identities it draws on remain valid over an abstract coefficient ring;
only their archimedean realisation is specialised here. At $q_0$ under convention D
the star-form spectrum is $0,\, 0.752702^{\times 3},\, 4.230339$: exactly one null
direction, and it is the braid-symmetric one.

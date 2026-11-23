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

## Prior art and structural synthesis

The metric formula combines the primal--dual optimal transport duality of Leonid V.
Kantorovich \cite{kantorovich1942} and Gennady Sh. Rubinstein \cite{rubinstein1957}
with the noncommutative spectral distance of Alain Connes \cite{connes1989,connes1994},
recast in order-unit generality by Marc A. Rieffel \cite{rieffel1999,rieffel2004} and
linked to Wasserstein transport by Francesco D'Andrea and Pierre Martinetti
\cite{dandrea-martinetti2010}. On any order-unit algebra, Rieffel's Lip-norm theorem
establishes that $d(\varphi,\psi)$ defines a finite state-space metric if and only if
$\ker L$ reduces to scalar multiples of the identity \cite{rieffel1999,latremoliere2016};
Bruno Iochum, Thomas Krajewski, and Pierre Martinetti \cite{iochum-krajewski-martinetti2001}
track the resulting infinite-distance walls on finite-dimensional algebras whenever the
representation kernel is non-trivial, together with the finite shortest-path distance
recovered on the faithful quotient. Passing modulo the null ideal $\mathcal{N}_\tau$
implements the operational indiscernibility quotient of Israel M. Gelfand, Mark A.
Naimark, and Irving E. Segal \cite{gelfand-naimark1943,segal1947} (extended to physical
equivalence by Rudolf Haag and Daniel Kastler \cite{haag-kastler1964}) and mirrors
quotienting by the presymplectic gauge null radical in the formalism of Marc Henneaux
and Claudio Teitelboim \cite{henneaux-teitelboim1992}.

Two structural features distinguish how this quotient operates here from its standard
appearances in topological field theory and noncommutative geometry. First, universal
skein and categorical semisimplification quotients --- developed by Christian Blanchet,
Nathan Habegger, Gregor Masbaum, and Pierre Vogel \cite{bhmv1995} and by John W.
Barrett and Bruce W. Westbury \cite{barrett1993} --- specialise $q$ to a root of unity
$e^{i\pi/r}$ to annihilate tilting modules of zero quantum dimension; here $q > 1$ lies
on the real hyperbolic ray where $U_q(\mathfrak{sl}_2)$ is semisimple, and the Markov
trace radical arises from Michio Jimbo's two-row $\mathrm{SU}_q(2)$ Schur--Weyl rank
cap \cite{jimbo1986}, which sets the Young-diagram trace weights of Vaughan F. R. Jones
\cite{jones1987}, Hans Wenzl \cite{wenzl1988}, Rosa C. Orellana \cite{orellana1998},
and Meinolf Geck and Sofia Lambropoulou \cite{geck-lambropoulou-2004} to zero on every
partition with $\ell(\lambda) \ge 3$, leaving the planar algebra of Harold Neville
Vazeille Temperley and Elliott H. Lieb \cite{temperley-lieb1971}. Second, spectral
Standard Model geometries \cite{chamseddine-connes-1997} posit a semisimple finite
algebra $\mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$ with a faithful trace by
stipulation; here the derivation starts on $H_n(q)$ at real $q_0 > 1$, proves that
convention D forces $\det G = 0$ for $n \ge 3$, and uses Rieffel's kernel criterion so
that state-space metric finiteness dynamically forces the projection
$H_n(q) \twoheadrightarrow TL_n(q)$.

**Archimedean specialisation.** What follows sits on the archimedean side of the
substrate wall: it invokes real- or complex-analytic constructs --- real-valued
physical observables, real-analytic bounds, transcendental constants, or numerical
evaluation at the substrate parameter $q_0$. Any generic categorical or
$q$-deformation identities it draws on remain valid over an abstract coefficient ring;
only their archimedean realisation is specialised here. At $q_0$ under convention D
the star-form spectrum is $0,\, 0.752702^{\times 3},\, 4.230339$: exactly one null
direction, and it is the braid-symmetric one.

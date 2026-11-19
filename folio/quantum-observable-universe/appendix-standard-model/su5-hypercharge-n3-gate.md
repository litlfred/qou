**$\mathrm{SU}(5)$ is not derived here, and nothing below should be read as
deriving it.**  What the framework possesses is a *family of levels among
which $\mathrm{SU}(5)$ is one*, together with a proved statement about what
occupying that level would force.  It does not possess anything occupying it.
The distinction is the whole content of this block.

The family is the Ocneanu parameter as a function of the Wenzl level,

$$
  z_r \;=\; \frac{q^{r}}{[r]_q},
  \qquad [r]_q = \frac{q^{r} - q^{-r}}{q - q^{-1}},
$$

whose $r = 2$ member is $z_2 = q^3/(q^2+1)$ — the canonical trace parameter on
the rank-$2$ base fibre $V_2$ — whose $r = 3$ member $z_3 = q^3/[3]_q$ is the
HOMFLY-PT trace parameter on the Kummer-pushforward colour bundle
$W_3 = \pi_*\mathcal{L}$, and whose $r = 5$ member is
$z_5 \approx 0.32275$ at the aether parameter.  The Schur–Weyl row cap at level
$r$ is $\ell(\lambda) \le r$, so each level fixes an admissible row count: a
single base spinor sits at $r = 2$, the colour pushforward occupies $r = 3$, and
irreducible Georgi–Glashow $\mathrm{SU}(5)$ would occupy $r = 5$.

**These levels are alternatives on an irreducible fibre rather than cumulative stages.**
A single irreducible fibre of quantum dimension $[N]_q$ carries one Markov trace
parameter, fixed with nothing left to choose by $z\,[N]_q = q^N$: a two-dimensional
fibre carries $z_2$, a three-dimensional fibre carries $z_3$, and an irreducible
five-dimensional fibre would carry $z_5$.  No construction in this framework
produces an *irreducible* fibre of quantum dimension $[5]_q$, and restating the
conditional implication $\dim_q V = [5]_q \Rightarrow z = z_5$ as though its
antecedent held would mistake a value of a rational function for an object.

**The framework constructs a split $2 \oplus 3$ bundle rather than an irreducible $r = 5$ fibre.**
On a single unramified base fibre $V_2$, every summand passing the $\mathrm{Sym}^2$
gate has even dimension, so $r = 3$ cannot arise inside one base fibre alone.
Over Bring's genus-$4$ surface ($\chi_{\mathrm{eu}} = -6$), however, scalar
restriction along the degree-$3$ cyclic Kummer $\mathbb{Z}_3$-cover $\pi$ pushes
a rank-$1$ Kummer module forward to a rank-$3$ bundle $W_3 = \pi_*\mathcal{L}$
($\dim \Lambda^3 W_3 = 1$), equipped with Jimbo's $N = 3$ ($a = q^3$) braided
$R$-matrix and Markov parameter $z_3 = q^3/[3]_q$.  Assembling $V_2$ and $W_3^*$
forms the **reducible split bundle** $F = V_2 \oplus W_3^*$ rather than an irreducible
level-$5$ Wenzl fibre.

## Consequences of the split $2 \oplus 3$ bundle without $\mathrm{SU}(5)$

In the Georgi–Glashow organisation one generation and its antiparticles occupy
the exterior algebra $\Lambda \mathbb{C}^5$, with the five basis vectors labelled
$u, d, r, g, b$ \cite{baez-huerta2010}, so that
$\mathbb{C}^5 \cong \mathbb{C}^2 \oplus \mathbb{C}^3$ — isospin and colour.
On the split bundle $F = V_2 \oplus W_3^*$, **fractional hypercharge is forced
without importing the full $\mathfrak{su}(5)$ algebra.**  Inside the $5 \times 5$
matrices on $F$, the block-diagonal unimodular Lie subalgebra
$\mathfrak{su}(3)_{\mathrm{c}} \oplus \mathfrak{su}(2)_L \oplus \mathfrak{u}(1)_Y$
has exact dimension $8 + 3 + 1 = 12$ and identically vanishing $(2,3)$ and $(3,2)$
off-diagonal blocks, thereby excluding all $24 - 12 = 12$ proton-decay leptoquark
generators of Georgi–Glashow $\mathrm{SU}(5)$.  The centralizer of
$\mathfrak{gl}(V_2) \oplus \mathfrak{gl}(W_3^*)$ inside the block-diagonal
endomorphisms consists of block scalars $\mathrm{diag}(y_2 I_2, y_3 I_3)$, and
tracelessness $2y_2 + 3y_3 = 0$ holds if and only if $y_3 = -\frac{2}{3}y_2$.
Setting $y_2 = -\frac{1}{2}$ forces $y_3 = +\frac{1}{3}$ on $W_3^*$, fixes all
five chiral multiplets on $\Lambda^1 F \oplus \Lambda^2(F^*)$ ($5 + 10 = 15$
Weyl states) with global kernel $\mathbb{Z}_6$ and exact cancellation of all five
gauge and gravitational anomalies, and yields the canonical ultraviolet mixing
ratio $\sin^2\theta_W^{\mathrm{UV}} = \mathrm{Tr}(T_3^2)/(\mathrm{Tr}(T_3^2) + \mathrm{Tr}(Y^2)) = 3/8$
purely from exterior-trace additivity on $F$.

**Distinction from $r = 5$ grand unification.**  Because $F = V_2 \oplus W_3^*$
is split rather than simple, the three gauge couplings $(g_3, g_2, g_1)$ evolve
under the one-loop Standard Model Dynkin multiplicities $(7, \frac{19}{6}, -\frac{41}{10})$
without proton-decay gauge bosons, whereas Georgi–Glashow $\mathrm{SU}(5)$
at an irreducible $r = 5$ rung is excluded experimentally by proton-lifetime
bounds \cite{baez-huerta2010}.  On the knot-state side, lifting the split-bundle
hypercharge grading to canonical per-state framed braid words is the open bridge
in [the truncation conjecture](#conj:sm-gauge-truncation) and [the hypercharge conjecture](#conj:sm-hypercharge-invariant).

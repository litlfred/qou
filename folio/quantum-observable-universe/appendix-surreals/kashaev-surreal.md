The [Kashaev volume conjecture](#conj:kashaev-volume-conjecture)
\cite{kashaev1997} (open in full generality; provenance is recorded in that
block) states:

$$
  \mathrm{Vol}(S^3 \setminus K)
   \;=\; 2 \pi \cdot \lim_{n \to \infty}
    \frac{\log |J_K(\zeta_n, n)|}{n},
$$

where $J_K(q, n)$ is the $n$-th coloured Jones polynomial,
$\zeta_n = e^{2 \pi i / n}$, and $\mathrm{Vol}$ is the hyperbolic
volume.

The conjecture has two awkward features when viewed through QOU:

1. The **left-hand side** is hyperbolic volume — pure analytic
 geometry, broken under surreal replacement (see
 [analytic obstructions](#rem:analytic-obstructions)).
2. The **right-hand side** uses an asymptotic-$n$ limit at a root
 of unity — a *singular* limit in $\mathbb{C}$.

Under the surreal lift, both sides admit cleaner reformulations,
and the gap between them sharpens.

## Reformulation

Set $n = \omega \in \mathbf{No}$ (the first infinite ordinal as a
surreal). Then $\zeta_\omega = e^{2 \pi i / \omega}$ is a
specific element of $\mathbf{No}[i]$ (interpreting the exponential
via Berarducci--Mantova's transseries \cite{berarducci-mantova2018}).
The coloured Jones polynomial $J_K(q, n)$ is rational in $q$ and
*polynomial in $n$* for fixed $K$, so $J_K(\zeta_\omega, \omega)$
is well-defined as an element of $\mathbf{No}[i]$.

The **surreal Kashaev statement** is:

$$
  \mathrm{Vol}(S^3 \setminus K)
   \;\stackrel{?}{=}\;
   \mathrm{st}\!\left(
     2 \pi \cdot \frac{\log |J_K(\zeta_\omega, \omega)|}{\omega}
   \right),
$$

where $\mathrm{st}$ is the standard-part map applied to a finite
surreal.

## The trade-off

The reformulation **does not solve** the volume conjecture. It
trades:

- (classical) an analytic limit $\lim_{n \to \infty}$ of complex
 numbers, plus a hyperbolic-volume identity in $\mathbb{R}$;

for:

- (surreal) an evaluation of a polynomial-in-$n$ at $n = \omega$,
 plus the *standard-part* identity that the result agrees with
 hyperbolic volume.

The right-hand side of the surreal version is *manifestly*
well-defined (rational arithmetic in $\mathbf{No}$), so the
question reduces to whether the **standard-part** matches. The
asymptotic-limit content of Kashaev becomes the standard-part
content of the surreal version.

## Location of the algebra-vs-analysis split

The reformulation makes the algebraic and analytic content of
Kashaev separable:

| Side | Algebra-vs-analysis content |
|---|---|
| RHS, before $\mathrm{st}$ | Pure algebra: rational in $\omega$ at root of unity |
| $\mathrm{st}$ application | Asymptotic transseries reduction |
| Identification with $\mathrm{Vol}$ | Genuine hyperbolic geometry |

The first row uses no analysis. The second row uses a *single*
transseries reduction (Berarducci--Mantova) — an instance of the
$\mathrm{st}$/$\mathrm{ord}_\omega$ reduction of the
[surreal blow-up calculus](#def:surreal-blowup-calculus). The third
row is where hyperbolic geometry enters — and it enters *only* on
the LHS.

The second row admits a precise name from resurgence theory
\cite{ecalle1981}. The Berarducci--Mantova transseries invoked there
are transseries in Écalle's sense, and the evaluation sits on a
Stokes ray of the Kashaev asymptotic series, where the two lateral
Borel sums of a divergent transseries disagree. The standard-part
map applied to the finite surreal selects the unique
real-single-valued value — which is the *median resummation* of
Écalle's alien calculus. The unspecified "asymptotic transseries
reduction" is therefore a named operation: $\mathrm{st}$ acts as
median resummation of the Kashaev transseries at the root of
unity. This identifies the second row's content with a standard
resurgence construction; it does not touch the third row, which
remains the genuine geometric input.

Kashaev thus becomes one transseries reduction plus one
$\mathrm{Vol}$-identity, instead of an analytic limit plus a
$\mathrm{Vol}$-identity.

## Potential utility and its limits

**Might help:** the algebraic side $J_K(\zeta_\omega, \omega)$
is exactly computable for any specific knot (it is a rational
function evaluated at named surreals). If a *general* formula
exists for $\mathrm{st}(\log |J_K(\zeta_\omega, \omega)|/\omega)$
in terms of knot data, we have a path to a proof of Kashaev.

**Might not help:** the standard-part identity is *itself* an
analytic statement (it asserts an asymptotic relationship
between the algebraic and the geometric). The surreal lift may
just relocate the difficulty rather than dissolve it.

## Discussion

**Open in general; a theorem for the figure-eight knot** — the
conjecture is a reformulation, not a proof. Its value is in
*separating* the algebraic content (which is computable) from the
geometric content (which is the actual Kashaev). For $K = 4_1$ the
classical limit statement is a theorem \cite{murakami-murakami2001}, so
the surreal form holds with $=$ in place of $\stackrel{?}{=}$ for
$4_1$ — see the next section.

## Figure-eight discharge and quantum-modularity refinement

For the figure-eight knot the two question marks collapse:

1. **Leading order ($=$, not $\stackrel{?}{=}$).** The classical
   Kashaev limit for $4_1$ is proved \cite{murakami-murakami2001}.
   Combined with the formulation equivalence (proof-strategy items
   1--3 below, provable by transfer), the surreal statement is a
   theorem for $4_1$:

   $$
     \mathrm{st}\!\left(
       2 \pi \cdot \frac{\log |J_{4_1}(\zeta_\omega, \omega)|}{\omega}
     \right)
     \;=\; \mathrm{Vol}(S^3 \setminus 4_1)
     \;=\; 2\,\mathrm{Cl}_2(\pi/3),
   $$

   conditional only on the transfer equivalence, not on any open
   conjecture.

2. **All orders (quantum modularity).** Garoufalidis--Zagier
   \cite{garoufalidis-zagier-2024} refine the leading asymptotic to a
   matrix-valued $\mathrm{SL}_2(\mathbb{Z})$-cocycle $W_\gamma$,
   holomorphic on cut planes, whose functional equation holds
   *exactly* — the factorially divergent perturbative series
   $\Phi(\hbar)$ is the asymptotic expansion of an actual analytic
   object satisfying an equality, not merely an estimate. Read
   through [$\mathrm{st}$ as median resummation](#rem:st-is-median-resummation),
   the cocycle supplies precisely the real-single-valued function
   whose surreal evaluation $\mathrm{st}$ selects: the
   quantum-modular functional equation is the inequality-free form of
   the asymptotic statement.

3. **Stokes data as integer counts.** The resurgent structure of the
   $4_1$ Kashaev series is completely described in
   \cite{garoufalidis-gu-marino2021}: Borel singularities sit on the
   complex-volume lattice and the Stokes constants are organised as
   integer $q$-series identified with 3d-index data. Under the
   modular-resurgence template \cite{fantini-rella2024} these Stokes
   constants are coefficients of an L-function, tying the alien
   calculus of the series to a quantum modular form.

The upgrade is deliberately scoped: it discharges the $4_1$
*instance* of the surreal Kashaev statement and equips it with an
exact (rather than asymptotic) analytic backbone. The general-knot
statement remains open, exactly as for the classical volume
conjecture. The QOU relevance is concentrated at $4_1$ because the
muon anchor is $\mathfrak{m}_\mu = \mathfrak{m}_e \cdot
\mathrm{Vol}(4_1)/\hbar_q^2$: the volume entering the mass formula is
backed, at $4_1$, by a proved equality rather than a conjectural
limit.

## What $\mathrm{st}$ discards: the $\omega$-grade of the remainder

The sections above are thorough about what $\mathrm{st}$ *is* and say
nothing about what it *throws away*. For $4_1$ the discarded quantity can
be named exactly, and it is not a benign tail.

Following the surreal-equality bookkeeping of the
[blow-up calculus](#def:surreal-blowup-calculus), write the pre-standard-part
argument as $\mathrm{Vol}(4_1) + \delta$, i.e.

$$
  \delta_N \;:=\;
   \frac{2\pi}{N}\,\log \langle 4_1 \rangle_N \;-\; \mathrm{Vol}(4_1),
$$

with $\langle 4_1 \rangle_N$ the Kashaev invariant, so that the discharge
of the previous section is the statement $\mathrm{st}(\delta) = 0$ at
$N = \omega$. Here $\delta$ is the blow-up calculus's remainder symbol; it
is unrelated to the alien derivative $\Delta_\omega$ of
[Écalle--Borel resummation](#def:ecalle-borel-resummation) and to the
per-partition binding weight $\Delta_\lambda$, both of which carry the
capital.

### The grade, derived

The corpus derives the sub-leading shape of the Kashaev invariant at $4_1$
from the saddle point, rather than importing it: at the one-variable saddle
$\theta^\ast = 5\pi/6$ the Stirling factor is $2\sin\theta^\ast = 1$ and
the Hessian is $|\cot\theta^\ast| = \sqrt{3}$, giving

$$
  \langle 4_1 \rangle_N \;\sim\; 3^{-1/4}\,N^{3/2}\,
   e^{\,N\,\mathrm{Vol}(4_1)/2\pi}
$$

with both $3^{-1/4}$ and the power $3/2$ derived
([1-loop prefactor provenance](#prop:one-loop-prefactor-provenance)). Taking logarithms term by term gives the two
leading terms of the remainder:

$$
  \delta_N \;=\; \frac{3\pi \log N}{N}
   \;-\; \frac{\pi \log 3}{2N} \;+\; r_N ,
$$

since $(2\pi/N)\cdot\tfrac{3}{2}\log N = 3\pi \log N / N$ and
$(2\pi/N)\cdot(-\tfrac{1}{4}\log 3) = -\pi \log 3 / (2N)$. **The two
named terms are derived; the order of $r_N$ is not.** A relative
correction $1 + O(1/N)$ in the asymptotic above would give
$r_N = O(1/N^2)$, and check 1 of the probe below measures exactly
that — the residual after subtracting the two terms falls by a factor
$0.4928, 0.4966, 0.4983, 0.4992, 0.4996$ on successive doublings, against
$1/2$ for a clean $1/N$ relative tail. That rate is measured here, not
derived; the proposition cited above states the leading asymptotic and
records the step from its two proved analytic inputs to the saddle
hypotheses as still assumed.

At $N = \omega$ the leading monomial of $\delta$ is therefore
$(\log \omega)/\omega$, which in the Berarducci--Mantova hierarchy
\cite{berarducci-mantova2018} sits **strictly between grade $-1$ and
grade $0$**: it exceeds $c/\omega$ for every real $c$, and is exceeded by
$\omega^{-1+\varepsilon}$ for every real $\varepsilon > 0$. Two statements
follow, and both are load-bearing:

1. $\mathrm{ord}_\omega(\delta) = -1$ in the **coarse** grading. The
   remainder is a first-order infinitesimal, so $\mathrm{st}(\delta) = 0$
   and the figure-eight discharge above is correct as stated.
2. $\delta$ is **not** a grade-$(-1)$ monomial: $\omega \cdot \delta$ is
   **infinite**. A grade-$(-1)$ monomial $c/\omega$ would give the finite
   $\omega \cdot (c/\omega) = c$.

Quoting only the first — "the remainder is a first-order
infinitesimal" — is true and misleading. It is the second that records that the
underlying convergence is logarithmically slow.

### Three consequences, derived before measurement

Each consequence below was written down from the expansion above, and only
then compared against this corpus's own Kashaev sum at
$N = 50, 100, 200, 400, 800, 1600$ (exact `mpmath` at 50 dps, with
$\mathrm{Vol}(4_1)$ computed as $2\,\mathrm{Cl}_2(\pi/3)$ rather than read
from a float literal).

| | derived | measured |
|---|---|---|
| **C1.** $N\delta_N/\log N \to 3\pi$ from below, with offset $-(\pi \log 3)/(2 \log N)$ | $9.1908728$ at $N = 1600$ | $9.1911680$; the gap falls $0.0183 \to 0.000295$ across the ladder, halving on each doubling |
| **C2.** $N \delta_N \to \infty$ | diverges | $35.22 \to 67.81$, monotone, with no sign of settling |
| **C3.** a $1/N$ Richardson step on the Kashaev limit leaves $N(R_N - \mathrm{Vol}(4_1)) \to 3\pi \log 2$ | $6.53275827$ | $6.53058$ at $N = 800$ |

C2 is the measured form of statement 2 above. C3 is its operational
consequence: anyone extrapolating the Kashaev limit on a $1/N$ grid is
fitting a mis-specified ansatz, and the residual they will see is
$3\pi \log(2)/N$.

### What this prices

The algebra-versus-analysis table above assigns
the whole analytic burden of the surreal form to a single application of
$\mathrm{st}$, on the ground that the pre-$\mathrm{st}$ side is exact
rational arithmetic in $\mathbf{No}$. That accounting is unchanged, but
the second row is not free: the object $\mathrm{st}$ is applied to differs
from $\mathrm{Vol}(4_1)$ by a quantity whose $\omega$-multiple *diverges*,
so the reduction is not the truncation of a convergent tail. The surreal
form relocates the analysis into $\mathrm{st}$ faithfully; it does not
make it small.

**Scope.** This is an asymptotic statement about $4_1$ alone, resting on a
cited expansion that is not re-derived here. What is established is that
this corpus's own computed Kashaev sum reproduces that expansion, and that
the three consequences hold. It does not bear on the volume conjecture for
any other knot, does not alter $\mathrm{st}$, and does not weaken the
figure-eight discharge.

## Connection to QOU

This paper uses the Kashaev volume conjecture as a *cross-
check* on its categorical mass formula
([Kashaev volume--density](#rem:kashaev-volume-density)). The
mass formula computes a particle mass via Hoefsmit/Markov-trace
data; the cross-check identifies this with a Jones-polynomial
evaluation, which Kashaev relates to hyperbolic volume.

Under the surreal lift:

- Hoefsmit/Markov-trace side lifts to $\mathbf{No}$ exactly
 (algebraic — see [algebraic core survives](#rem:algebraic-core-survives)).
- Jones polynomial at $q = q_0 \in \mathbb{R}$ lifts by definition
 ($q_0 \in \mathbb{R} \subset \mathbf{No}$).
- Hyperbolic volume side stays in $\mathbb{R}$ (external anchor).
- Kashaev's identity, recast as a surreal standard-part
 identity, bridges the two.

If the surreal Kashaev conjecture is proved (or even just
proved for the knot class relevant to QOU), the QOU mass formula
acquires an algebraic foundation independent of hyperbolic
geometry.

## Proof strategy

**Reformulation reducibility (provable now)**:

1. Show: the classical Kashaev statement (limit form) and the
 surreal Kashaev statement (standard-part form) are
 *equivalent* — one holds iff the other does.

2. Forward direction: if $\lim_{n \to \infty} 2\pi \log
   |J_K(\zeta_n, n)|/n = \mathrm{Vol}(S^3 \setminus K)$, then by
 the transfer principle the standard-part of the surreal
 evaluation matches.

3. Backward direction: if $\mathrm{st}(\cdots) =
   \mathrm{Vol}(\cdots)$, then by definition of $\mathrm{st}$
 the asymptotic limit converges to $\mathrm{Vol}$.

**Verification on known cases (provable now)**:

4. The figure-eight knot $4_1$ (Murakami–Murakami 2001
 \cite{murakami-murakami2001}) and the trefoil $3_1$ have the volume
 conjecture proved. Compute $J_K(\zeta_\omega, \omega)$
 directly, take $\mathrm{st}$, and verify equality with the
 known volume.

5. Express the surreal evaluations through Gonshor's sign-sequence
 map and the surreal $\omega$.

**General case (open)**:

6. The general Kashaev conjecture for hyperbolic knots is open
 classically. The surreal reformulation does not provide a new
 line of attack, but it *separates* the algebraic content
 (rational-in-$\omega$ evaluations of $J_K$) from the geometric
 content (the volume identity).

**Falsification path**: identical to the classical Kashaev
conjecture; if the limit form fails for some knot, the
surreal form fails as well (and conversely).

**Provability assessment**: the *equivalence* of the two
formulations is provable (transfer principle). The
underlying conjecture is a long-standing open problem; the
reformulation does not by itself solve it but reorganises the
problem productively.

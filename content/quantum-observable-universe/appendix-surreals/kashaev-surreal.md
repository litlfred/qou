The [Kashaev volume conjecture](#conj:kashaev-volume-conjecture)
[@kashaev1997] (open in full generality; provenance and the Lean
axiomatisation live in that block) states:

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
via Berarducci--Mantova's transseries [@berarducci-mantova2018]).
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
[@ecalle1981]. The Berarducci--Mantova transseries invoked there
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
classical limit statement is a theorem [@murakami-murakami2001], so
the surreal form holds with $=$ in place of $\stackrel{?}{=}$ for
$4_1$ — see the next section.

## Figure-eight discharge and quantum-modularity refinement

For the figure-eight knot the two question marks collapse:

1. **Leading order ($=$, not $\stackrel{?}{=}$).** The classical
   Kashaev limit for $4_1$ is proved [@murakami-murakami2001].
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
   [@garoufalidis-zagier-2024] refine the leading asymptotic to a
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
   [@garoufalidis-gu-marino2021]: Borel singularities sit on the
   complex-volume lattice and the Stokes constants are organised as
   integer $q$-series identified with 3d-index data. Under the
   modular-resurgence template [@fantini-rella2024] these Stokes
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
 [@murakami-murakami2001]) and the trefoil $3_1$ have the volume
 conjecture proved. Compute $J_K(\zeta_\omega, \omega)$
 directly, take $\mathrm{st}$, and verify equality with the
 known volume.

5. Use `QOU.AppendixSurreals.gonshorIn` and
 `omegaSurreal` to express the surreal evaluations.

**General case (open)**:

6. The general Kashaev conjecture for hyperbolic knots is open
 classically. The surreal reformulation does not provide a new
 line of attack, but it *separates* the algebraic content
 (rational-in-$\omega$ evaluations of $J_K$) from the geometric
 content (the volume identity).

**Required infrastructure**:
- Coloured Jones polynomial in Lean (does not exist in mathlib).
- Berarducci–Mantova exponential/logarithm on $\mathbf{No}$
 (partial in mathlib).
- Hyperbolic-volume formalisation (does not exist in mathlib).

**Falsification path**: identical to the classical Kashaev
conjecture; if the limit form fails for some knot, the
surreal form fails as well (and conversely).

**Provability assessment**: the *equivalence* of the two
formulations is provable in Lean (transfer principle). The
underlying conjecture is a long-standing open problem; the
reformulation does not by itself solve it but reorganises the
problem productively.

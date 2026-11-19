> **Superseded.** The scalar substrate density $\rho_q = 1/\hbar_q^2$ used
> below is the structurally-wrong leading-order ansatz; the operator-valued
> form supersedes it ([`mass-endomorphism-tower`](mass-endomorphism-tower.md));
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [rho k graded expansion proposition](../mass-endomorphism/rho-k-graded-expansion.md).

**Conjecture (Algebraic-geometric dilogarithm equivalence).**
*The categorical Markov trace of the nonabelian multiplicative integral
over a lifted transient crossing
([mass identity](#def:mass-identity))
evaluates algebraically to a rational function in $\mathbb{Z}[q^{1/2},
q^{-1/2}, x]$ governed by the $q$-Pochhammer partial product
$\Phi_n(x; q) = \prod_{k=0}^{n-1}(1 - x q^k)^{-1}$
([q-Pochhammer partial product](#def:q-pochhammer-partial-product)).
Under the Archimedean realization $\tau_{\mathrm{arch}}$
([archimedean realization functor](#def:archimedean-realization-functor)):*

1. *(**Pole-to-cusp bijection.**) The roots
   $\{x = q^{-k} : k = 0, \dots, n-1\}$ of the denominator
   $(x; q)_n$ are in bijection with the $n$ ideal tetrahedra of a
   hyperbolic triangulation of the $\Phi_q$-piece $K_S$ of the lifted
   transient crossing
   ([Φ$_q$-piece](#def:phi-q-piece)), the root of index $k$ labelling
   the tetrahedron whose shape parameter it seeds.*

2. *(**Asymptotic Bloch–Wigner.**) The asymptotic of the partial
   product under Faddeev's scaling
   ([Archimedean limit](#conj:dilogarithm-archimedean-limit))
   recovers the Bloch–Wigner dilogarithm $D(z)$ at the matched shape
   parameter, so*

$$
  \tau_{\mathrm{arch}}\!\bigl(\Phi_n(x; q_0)\bigr)
  \;\xrightarrow[n \to \infty]{}\;
  D(z(x))
  \;=\;
  \mathrm{Vol}_{\mathrm{hyp}}\bigl(\Delta_{z(x)}\bigr),
$$

   *where $z(x)$ is the shape parameter of the ideal tetrahedron
   $\Delta_{z(x)}$ that triangulates $K_S$.*

3. *(**Mass formula.**) The $\tau_{\mathrm{arch}}$-image of the
   transient mass element is*

$$
  \tau_{\mathrm{arch}}\!\bigl(\mathfrak{m}^{\mathrm{trans}}(\varrho)\bigr)
  \;=\;
  \rho_q \cdot
  \!\!\sum_{S \subseteq \{0,\dots,n-2\}}\!\!
  D\bigl(z(\lvert V_S\rvert)\bigr)
  \;=\;
  \rho_q \cdot
  \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K),
$$

   *recovering the JSJ piecewise sum used in the canonical binding-
   energy pipeline (cf.
   [Φ$_q$-tower JSJ bridge](#rem:phi-q-tower-jsj-bridge)).*

**Note — what $n$ is, and it is not pinned.** Clause (1) counts $n$ ideal
tetrahedra because that is what the carrier of the bijection
([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy),
table row 4) and the compute both count: `snappy_cusp_seeding.py` takes
$n$ from `num_tetrahedra()` and emits one algebraic seed per tetrahedron, eight
for the eight-tetrahedron $\mathtt{L6a4}$. But the same symbol is the Hecke
index and GB-depth $k_\star(T_w) = n$ in that carrier's own hypothesis, a free
truncation order swept over $1, \dots, 4$ in
[q-pochhammer-seed.witness.json](../../../computations/q-pochhammer-seed.witness.json),
and unbounded in clause (2) below, which takes $n \to \infty$. For the
figure-eight $4_1$ these disagree: the triangulation has **2** tetrahedra and
**1** cusp, while the braid whose closure it is has Hecke index **3**. So
clause (1) fixes the geometric *object* the roots label without fixing the
*count*, and no clause here should be read as asserting that the Hecke depth
equals the tetrahedron count — that identification is asserted in
[thurston-relaxation](#sec:thurston-relaxation) as the "GB-PL bijection" and
is not established here.

## Relation to the structural form of Kashaev

The conjecture is the **QOU-native, partial-product** form of the
Kashaev–Murakami–Murakami theorem
([Kashaev volume conjecture](#conj:kashaev-volume-conjecture)).
Kashaev–MM pass through the colored Jones polynomial at roots of
unity; the present conjecture passes through the **explicit shared
denominator**:

| Side | Object | Pole / singularity |
|------|--------|--------------------|
| Algebraic ($R$) | $\Phi_n(x; q_0)$ | zero of $(1 - x q^k)$ at $x = q^{-k}$ |
| Archimedean ($\mathbb{C}$) | $\mathrm{Li}_2$ | logarithmic singularity at $t = 1$ |
| Geometric ($\mathbf{Hyp}_3$) | ideal tetrahedron $\Delta_{z_k}$ | complete cusp of $\Delta_{z_k}$ |

The bijection between the rows is the content of
([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)).
Under that bijection, the algebraic state sum and the hyperbolic
volume are the same regulator
$\Phi_n(x; q_0) \mapsto D(z(x))$ evaluated through two convergence
schemes.

## Conjectural standing

This result is downstream of
([Kashaev volume conjecture](#conj:kashaev-volume-conjecture)) and
([Archimedean limit](#conj:dilogarithm-archimedean-limit)), so it is
necessarily a **conjecture** — propagation of conjectural backing
forbids promotion to `proposition`/`theorem`.

The conditional formulation carries the open inputs — the matched shape
parameter $z(x)$, the volume-conjecture saddle asymptotic (a theorem for $4_1$
by Ohtsuki / Andersen–Hansen), and the matched-cusp volume identification
supplied by ([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)) —
and derives both halves: item 1 (pole side) unconditionally (each $x = q^{-k}$
is a genuine root of $(x;q)_n$), and item 2 (Bloch–Wigner asymptotic) from the
conditional hypotheses. This matches the conditional pattern used for
[Φ$_q$-tower JSJ bridge](#rem:phi-q-tower-jsj-bridge).

**The shape parameter lies in the upper half plane.** Item 2 above
states the asymptotic at $D(z(x))$, with $z(x)$ the shape of the ideal
tetrahedron. Typing the Bloch–Wigner function as $D \colon \mathbb{R} \to \mathbb{R}$
and applying it directly to the real state variable $x$ would diverge from the
statement above: $D$ is conjugation-antisymmetric, $D(\bar z) = -D(z)$, so $D$
vanishes identically on the reals and every volume would be forced to zero — a
*flat* tetrahedron, which is the negation of the conjecture rather than a weak
form of it. Keeping the shape parameter in the upper half plane $\mathfrak{H}$
excludes degenerate shapes while $x$ retains its role as the $q$-Pochhammer
state variable, matching the shape assignment in
([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)).

## The bar-odd open item: argument identification to $S$

The equivalence above is the **bar-even** face of the correspondence:
the asymptotic recovers the real volume $D(z) = \mathrm{Vol}_{\mathrm{hyp}}$,
which for the amphichiral $4_1$ supplies the $-\mathrm{Vol}(4_1)$ part of
the $Q_\beta$ coefficient $c_3$. Its **bar-odd** companion is the
anchor-dependent leak $S = c_3 + \mathrm{Vol}(4_1)$, carried not by the
compact $\Phi_q$ but by the Faddeev non-compact $\Phi_b$
(modular double). The open item is the
**argument-identification map**: the structural map $q_0 \mapsto z(q_0)$
— the substrate-to-meridian-holonomy map supplied by the same
pole-to-cusp matching as items 1–2 — such that the fibre-branch Faddeev
phase at the identified argument reproduces $S$:

$$
  \arg \Phi_{b(q_0)}\bigl(z(q_0)\bigr) \;=\; S(q_0),
  \qquad
  b(q_0) \;=\; \sqrt{\tfrac{\ln q_0}{2\pi}}.
$$

The hypothesis is parametrized by the argument map itself: a bare existence
claim ($\forall q_0\, \exists z$) would be near-vacuous by pointwise choice
against the unbounded continuous phase, so the structural map is carried as an
explicit parameter. Two consequences follow unconditionally from this hypothesis:

1. (**Unimodular readout.**) At the identified argument the $\Phi_b$
   value is the pure phase $e^{i S(q_0)}$ — the leak is the argument of
   a $\sigma$-unitary
   ([unitary phases are bar-odd](#prop:phi-b-unitary-bar-odd)).

2. (**Zero crossing — conditional on a sign flip the data does not
   establish.**) *If* $S$ changes sign between the anchors, continuity of
   $S$ on $q_0 > 1$ forces by the intermediate value theorem a substrate
   $q^{*}$ where $S(q^{*}) = 0$: there $c_3 = -\mathrm{Vol}(4_1)$ and the
   $\Phi_b$ readout is $1$.
   The premise is **not established by the data**: each anchor value
   $S(\text{muon}) \approx +0.00968$, $S(\text{proton}) \approx -0.03946$
   carries a CAL-3 propagated uncertainty of $\pm 1.26$ ($130\times$ / $32\times$ the
   value); only the swing $S(\text{muon}) - S(\text{proton})$ is resolved,
   and it is the cross-anchor $c_3$ difference with $\mathrm{Vol}(4_1)$
   cancelled. So the zero-crossing is a conditional structural statement,
   not an established prediction. (The onward identification of this
   $S$-channel with the resurgent monodromy datum $A_\omega$ has no
   literature support and is not derivable.)

## The fibre branch ($\lvert q \rvert = 1$, real $b$) and construction status

The physical regime of the bar-odd face is the **fibre branch**: real
$b$, where the modular parameter $q_b = e^{i\pi b^2}$ satisfies
$\lvert q_b \rvert = 1$ and equals the pure phase $e^{i \ln q_0 / 2}$ at
the substrate map. On
this branch the modular-double product diverges and the construction is
the real single integral $\Phi_b$, whose structural laws —
self-duality $\Phi_{b^{-1}} = \Phi_b$, unitarity
$\lvert \Phi_b \rvert = 1$, the inversion relation, and
$\sigma$-unitarity $\Phi_b \cdot \overline{\Phi_b} = 1$ — hold for the
defined object unconditionally. By the rigidity clause of
([unitary phases are bar-odd](#prop:phi-b-unitary-bar-odd)), the
fibre-branch $\Phi_b$ is an intrinsically bar-odd carrier.

Of the two analytic identifications behind the construction, the
**integrability** of the Faddeev kernel is an unconditional
theorem: the near-$0$ piece (where the
$-2z/t^2$ subtraction cancels the pole, via the two-sided cubic $\sinh$
estimates and a global $\lvert \sin y - y \rvert \le 2\lvert y \rvert^3$
bound), the exponential-domination tail on $[1, \infty)$, and hence integrability on all of
$(0, \infty)$ are all hypothesis-free, since $e^{-bt}$ and $t^{-2}$ are integrable on
$[1, \infty)$. The
**definition-to-contour identity** — that the real-integral $\Phi_b$
equals the Faddeev contour integral — remains a numerical pin
($8 \times 10^{-29}$ against the validated contour evaluator) and is
carried as an explicit fibre-extension hypothesis.

## Binding channel: conditional only

The identification of the bar-odd face with the decay observable
$\mathfrak{Q}_\beta = \mathrm{Im}\,\mathfrak{V}$ — and with it any
"decay equals binding" reading of the Gram-ghost mode — is conditional
on the complex-volume unification
([binding–$Q_\beta$ complex volume](#conj:binding-qbeta-complex-volume)).
$\Phi_b$ touches binding **only** through that unproven channel
identity. When the channel is carried explicitly via the $u(q_0)$ map,
the deformed volume, and the identity $S = \mathrm{Im}\,\mathfrak{V}(u(q_0))$,
its composition with the argument-identification map yields the equality of the
$\Phi_b$ phase with the imaginary part of the deformed volume and the
Chern–Simons phase, and any sign flip of $S$ forces a substrate point with
vanishing deformed Chern–Simons part.

## Witness

Two witnesses bracket the matching, and neither is a SnapPy cusp solve
driven from the algebraic seeds.

[q-pochhammer-seed.witness.json](../../../computations/q-pochhammer-seed.witness.json)
sweeps the partial-product order over $n = 1, \dots, 4$; at each order it
extracts the $n$ denominator zeros $q_0^{-k}$, lifts them off the real line by a
fixed imaginary perturbation, and drives Newton-Raphson from each seed onto the
**colour-tube discriminant** $\Delta(z) = 0$ — not onto the Thurston gluing
equations. Nine of its ten runs converge, in at most 11 iterations. Its own
caveat records that it *"does not yet drive a SnapPy Newton iteration"*.

[snappy-cusp-seeding.witness.json](../../../computations/snappy-cusp-seeding.witness.json)
is the SnapPy side. It compares the bare algebraic seeds against SnapPy's
converged tetrahedral shape parameters for the figure-eight $4_1$
($\mathtt{m004}$), its sister $\mathtt{m003}$, and the Borromean rings
$\mathtt{L6a4}$, and reports the pairing distance; it seeds no solve. Those
distances ($0.40$ to $0.91$) are what bound the conjecture's canonical form, as
[shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)
§*Empirical scope* records.

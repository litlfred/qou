> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

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
   $(x; q)_n$ are in bijection with the ideal vertices of a hyperbolic
   tetrahedron triangulating the $\Phi_q$-piece $K_S$ of the lifted
   transient crossing
   ([Φ$_q$-piece](#def:phi-q-piece)).*

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
| Geometric ($\mathbf{Hyp}_3$) | ideal tetrahedron $\Delta_z$ | cusp at vertex $v_k$ |

The bijection between the rows is the content of
([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)).
Under that bijection, the algebraic state sum and the hyperbolic
volume are not two competing engines: they are the same regulator
$\Phi_n(x; q_0) \mapsto D(z(x))$ evaluated through two convergence
schemes.

## Conjectural standing

This block is downstream of
([Kashaev volume conjecture](#conj:kashaev-volume-conjecture)) and
([Archimedean limit](#conj:dilogarithm-archimedean-limit)), so it is
necessarily a **conjecture** — propagation of conjectural backing
forbids promotion to `proposition`/`theorem`.

The Lean formalization follows the hypothesis-carrying conditional-class
pattern: the class `QOU.QPochhammer.AlgebraicGeometricEquivalence` carries
exactly the two open inputs — the volume-conjecture saddle asymptotic
(a theorem for $4_1$ by Ohtsuki / Andersen–Hansen) and the matched-cusp
volume identification supplied by
([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)) —
and the statement bundle `QOU.QPochhammer.algebraic_geometric_equivalence`
*derives* both halves: item 1 (pole side) unconditionally, as the sorry-free
theorem `pole_cusp_bijection_proved` (each $x = q^{-k}$ is a genuine root of
$(x;q)_n$), and item 2 (Bloch–Wigner asymptotic) from the two class fields.
The class asserts nothing provable-outright; no instance is fabricated. This
matches the conjectural-class pattern used for
[Φ$_q$-tower JSJ bridge](#rem:phi-q-tower-jsj-bridge).

## The bar-odd keystone: argument identification to $S$

The equivalence above is the **bar-even** face of the correspondence:
the asymptotic recovers the real volume $D(z) = \mathrm{Vol}_{\mathrm{hyp}}$,
which for the amphichiral $4_1$ supplies the $-\mathrm{Vol}(4_1)$ part of
the $Q_\beta$ coefficient $c_3$. Its **bar-odd** companion is the
anchor-dependent leak $S = c_3 + \mathrm{Vol}(4_1)$, carried not by the
compact $\Phi_q$ but by the Faddeev non-compact $\Phi_b$
(modular double). The keystone open item is the
**argument-identification map**: the structural map $q_0 \mapsto z(q_0)$
— the substrate-to-meridian-holonomy map supplied by the same
pole-to-cusp matching as items 1–2 — such that the fibre-branch Faddeev
phase at the identified argument reproduces $S$:

$$
  \arg \Phi_{b(q_0)}\bigl(z(q_0)\bigr) \;=\; S(q_0),
  \qquad
  b(q_0) \;=\; \sqrt{\tfrac{\ln q_0}{2\pi}}.
$$

The Lean carrier is the hypothesis class
`QOU.QBeta.PhiBSArgumentIdentification.SArgumentIdentification`,
parametrized by the argument map itself: a bare existence claim
($\forall q_0\, \exists z$) would be near-vacuous by pointwise choice
against the unbounded continuous phase, so the class carries the
structural map as a parameter and no instance is fabricated. Two
consequences are derived unconditionally from the class:

1. (**Unimodular readout.**) At the identified argument the $\Phi_b$
   value is the pure phase $e^{i S(q_0)}$ — the leak is the argument of
   a $\sigma$-unitary
   ([unitary phases are bar-odd](#prop:phi-b-unitary-bar-odd)).

2. (**Zero crossing.**) The measured sign flip
   $S(\text{muon}) \approx +0.00968 > 0 > S(\text{proton}) \approx
   -0.03946$, together with continuity of $S$ on $q_0 > 1$, forces by
   the intermediate value theorem a substrate $q^{*}$ between the
   anchors where $S(q^{*}) = 0$: there $c_3 = -\mathrm{Vol}(4_1)$
   exactly and the $\Phi_b$ readout is $1$ — the bar-odd leak switches
   off (Lean: `exists_zero_crossing`, `exists_pure_bar_even`).

## The fibre branch ($\lvert q \rvert = 1$, real $b$) and construction status

The physical regime of the bar-odd face is the **fibre branch**: real
$b$, where the modular parameter $q_b = e^{i\pi b^2}$ satisfies
$\lvert q_b \rvert = 1$ and equals the pure phase $e^{i \ln q_0 / 2}$ at
the substrate map (Lean: `norm_fibreQParam`, `fibreQParam_fibreB`). On
this branch the modular-double product diverges and the construction is
the real single integral `phiB`
(`QOU.MathlibExt.FaddeevPhiBRealIntegral`), whose structural laws —
self-duality $\Phi_{b^{-1}} = \Phi_b$, unitarity
$\lvert \Phi_b \rvert = 1$, the inversion relation, and
$\sigma$-unitarity $\Phi_b \cdot \overline{\Phi_b} = 1$ — hold for the
defined object unconditionally. By the rigidity clause of
([unitary phases are bar-odd](#prop:phi-b-unitary-bar-odd)), the
fibre-branch $\Phi_b$ is an intrinsically bar-odd carrier.

Of the two analytic identifications behind the construction, the
**integrability** of the Faddeev kernel is settled on the tail: the
exponential-domination chain on $[1, \infty)$ is proved
(`integrableOn_kernel_Ioi_one`, with the two standard majorant
integrability facts carried as explicit named hypotheses), and full
integrability on $(0, \infty)$ is reduced to the bounded near-$0$ piece
(`integrableOn_kernel_Ioi_zero`). The **definition-to-contour
identity** — that the real-integral `phiB` equals the Faddeev contour
integral — remains a numerical pin ($8 \times 10^{-29}$ against the
validated contour evaluator) and is assumed nowhere in the Lean.

## Binding channel: conditional only

The identification of the bar-odd face with the decay observable
$\mathfrak{Q}_\beta = \mathrm{Im}\,\mathfrak{V}$ — and with it any
"decay equals binding" reading of the Gram-ghost mode — is conditional
on the complex-volume unification
([binding–$Q_\beta$ complex volume](#conj:binding-qbeta-complex-volume)).
$\Phi_b$ touches binding **only** through that unproven channel
identity; no statement in this block or in the Lean carriers above
assumes it. The channel is carried explicitly as the class
`SDeformedVolumeChannel` ($u(q_0)$ map + deformed volume + the identity
$S = \mathrm{Im}\,\mathfrak{V}(u(q_0))$), and the composition with the
keystone is derived, not assumed: `phase_eq_im_deformed_volume`,
`phiB_eq_cs_phase`, and `exists_cs_vanishing` (the sign flip of $S$
forces a substrate point with vanishing deformed Chern–Simons part).

## Witness

The algebraic-geometric matching of poles to cusps for the simplest
non-trivial case (the trefoil, $n = 3$) is recorded in
[q-pochhammer-seed.witness.json](../../../computations/q-pochhammer-seed.witness.json).
The witness reports the algebraic denominator zeros, the SnapPy-
solved cusp shape parameters obtained by feeding those zeros as
Newton–Raphson seeds, and the residual after one Newton step.

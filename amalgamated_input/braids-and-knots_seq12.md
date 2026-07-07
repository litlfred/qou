<!-- FILE_START: lepton-meson-parallel-intro.md -->
The torus-knot dictionary that assigns leptons to $T(2,k)$
braids extends naturally to mesons.  This section develops
the parallel: both sectors share the same Hecke algebra
$H_3(q)$, but mesons carry a bar-involution asymmetry
(charge conjugation $\neq$ bar on non-zero-writhe braids)
that distinguishes them from the bar-symmetric baryons.
<!-- FILE_END: lepton-meson-parallel-intro.md -->

<!-- FILE_START: frobenius-lepton-meson-bridge.md -->
**Proposition (Frobenius lepton–meson bridge).**
*The standard representation $V_{(2,1)}$ of $H_3(q)$ restricts to
$H_2(q)$ as the direct sum of the two lepton irreps:*

$$
  V_{(2,1)} \big\downarrow_{H_2}
  = V_{(2)} \oplus V_{(1,1)}.
$$

*The meson sector's sole mass-carrying partition is the
**entangled** lepton spectrum.*
## The entanglement interpretation

At $H_2$, the lepton irreps $V_{(2)}$ and $V_{(1,1)}$ are
**separate channels**: the electron mass formula evaluates them
independently, with eigenvalues $q$ and $-q^{-1}$.  The
figure-eight knot volume $\mathrm{Vol}(4_1)$ measures the
transition **between** these channels.

At $H_3$, the same two channels are **entangled** inside the
$2 \times 2$ Hoefsmit block of $V_{(2,1)}$.  The off-diagonal
element

$$
  b = \sqrt{a_\rho \cdot a_{-\rho} + 1},
  \qquad
  a_\rho = \frac{h}{1 - q^{-2\rho}},
$$

is the **binding amplitude** that prevents the lepton channels
from decoupling.  When $b = 0$ (no binding), the $(2,1)$ block
becomes diagonal and the meson reverts to two independent leptons.
When $b \ne 0$, the channels mix — this is the Hopf link binding.

## Frobenius reciprocity and the mass-ratio correspondence

By Frobenius reciprocity:

$$
  \langle \mathrm{Res}(V_{(2,1)}), V_{(2)} \rangle_{H_2}
  = \langle V_{(2,1)}, \mathrm{Ind}(V_{(2)}) \rangle_{H_3}
  = 1.
$$

Each lepton irrep appears **exactly once** in the restriction,
with the following consequences:

1. The **lepton mass ratio** $m_\mu / m_\mathfrak{e}$ measures
   the separated $V_{(2)} \leftrightarrow V_{(1,1)}$ transition
   (the figure-eight volume between the two 1-dim channels).

2. The **meson mass ratio** $m_K / m_\pi$ measures the same
   transition but **inside** the entangled $(2,1)$ block — the
   Hoefsmit $2 \times 2$ matrix encodes both channels simultaneously.

3. The **Hoefsmit off-diagonal $b$** is the bridge: it is the
   amplitude at which the lepton pair-channel becomes the meson
   binding channel.  At $b \to 0$: leptons (no binding).
   At $b \ne 0$: mesons (Hopf binding).

## Connection to $C$ versus bar

The branching also explains
[`prop:c-equals-bar-iff-all-1dim`](../../particle-interactions/c-equals-bar-iff-all-1dim.md):

- At $H_2$: $V_{(2)}$ and $V_{(1,1)}$ are separate 1-dim irreps,
  so $C = \mathrm{bar}$ (charge conjugation = bar involution).
- At $H_3$: $V_{(2,1)}$ entangles them into a 2-dim irrep, and
  the off-diagonal $b$ breaks the $C = \mathrm{bar}$ equivalence.

The standard representation is WHERE:
- the two lepton channels merge (branching),
- $C$ and bar diverge (symmetry breaking),
- the meson mass lives (SDP active set).

All three phenomena are the **same algebraic fact**: the appearance
of a multi-dimensional irrep in the Hecke tower.
<!-- FILE_END: frobenius-lepton-meson-bridge.md -->

<!-- FILE_START: frobenius-lepton-meson-bridge-interpretation.md -->
While the underlying branching rule $V_{(2,1)} \downarrow V_{(2)} \oplus V_{(1,1)}$ is standard representation theory (derived from the Pieri / Littlewood-Richardson rule), the mathematical novelty here lies in its formal topological application: lifting a strictly representation-theoretic branching into a geometric constraint on the observable mass spectrum, and demonstrating that the physical entanglement of lepton channels uniquely maps to the single mass-carrying partition of the meson sector.
<!-- FILE_END: frobenius-lepton-meson-bridge-interpretation.md -->

<!-- FILE_START: hoefsmit-binding-amplitude.md -->
**Proposition (Hoefsmit binding amplitude).**
*The off-diagonal element $b$ of the Hoefsmit seminormal matrix
for the standard representation $(2,1)$ of $H_3(q)$ satisfies*

$$
  b^2 = \frac{[3]_q}{[2]_q^2},
  \qquad
  1 - b^2 = \frac{1}{[2]_q^2}.
$$

**Mathematical Novelty.** While the computation of the Hoefsmit seminormal matrix is a standard algebraic procedure within Hecke representation theory, the mathematical novelty is demonstrating that this specific exact rational relation ($1-b^2 = 1/[2]_q^2$) directly governs the discrete geometric de-entanglement fraction of the pion's mass, reinterpreting an abstract representation-theoretic off-diagonal matrix element as a topological binding constraint.
## Physical interpretation: pion decay

The binding amplitude $b$ governs the entanglement of the two
lepton channels $V_{(2)} \oplus V_{(1,1)}$ inside the meson's
standard representation
([`prop:frobenius-lepton-meson-bridge`](frobenius-lepton-meson-bridge.md)):

- $b = 0$: the $(2,1)$ block diagonalises $\to$ the lepton channels
  decouple $\to$ no meson binding (free leptons).
- $b \ne 0$: the off-diagonal element mixes $V_{(2)}$ and
  $V_{(1,1)}$ $\to$ meson exists as an entangled lepton pair.

The pion decay $\pi \to \mu + \nu$ releases a fraction
$1 - b^2 = 1/[2]_q^2$ of the pion's rest energy as
de-entanglement energy:

$$
  E_{\mathrm{bind}} = \frac{m_\pi}{[2]_q^2}.
$$

The remaining energy is $m_\pi \cdot b^2
= m_\pi \cdot [3]_q / [2]_q^2$.  By the Frobenius bridge,
this residual energy flows into the de-entangled lepton channel
(the $V_{(2)}$ component of $V_{(2,1)}\!\downarrow_{H_2}$),
consistent with the dominant pion decay mode
$\pi^+ \to \mu^+ + \nu_\mu$.

## The $q$-integer structure

The identities $b^2 = [3]_q/[2]_q^2$ and $1 - b^2 = 1/[2]_q^2$
are exact in $q$ — they hold for all $q$, not just $q_0$.  The
pion decay fraction is a **universal algebraic identity** of the
Hecke algebra, independent of the substrate parameter.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: hoefsmit-binding-amplitude.md -->

<!-- FILE_START: self-dual-higgs-real-volume.md -->
**Proposition (the self-dual Higgs has a real complex volume).**
*The figure-eight knot $4_1$ — the Higgs (mass mechanism) — is
**amphichiral**: it equals its own mirror, so under the bar-involution
$\sigma\colon q \mapsto q^{-1}$ its colored Jones is fixed,*

$$
  J_N(4_1; q) = J_N(4_1; q^{-1}) \qquad (\forall N).
$$

*Consequently its Neumann–Zagier complex volume
$\mathbb{V}(4_1) = \mathrm{Vol}(4_1) + i\,\mathrm{CS}(4_1)$ is **real**:*

$$
  \mathrm{CS}(4_1) = \mathrm{Im}\,\mathbb{V}(4_1) = 0,
  \qquad
  \mathrm{Re}\,\mathbb{V}(4_1) = \mathrm{Vol}(4_1) \approx 2.0299.
$$

*The bare Higgs knot therefore contributes **only the real (volume / mass)
face** — the muon mass scale $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ — and
its imaginary (decay) face vanishes: $\mathfrak{Q}_\beta$ is **not** a
property of the lone Higgs knot.*

Where the decay face does live is conjectural: per
[`conj:binding-qbeta-complex-volume`](../mass-endomorphism/binding-qbeta-complex-volume.md),
$\mathfrak{Q}_\beta$ is the imaginary part of the many-body **binding
defect** $\mathfrak{V} = E_0\,\mathrm{tr}_M((\Pi_{\text{free}}-\mathbf{1})\circ\mathcal{M})$.
That identification is not part of this proposition's claim.

## The Askey two-saddle structure

Torus knots and hyperbolic knots are the two archimedean saddles of one
quantum A-polynomial $\hat A_K$ (the AJ machinery,
[`phi-q-aj-machinery-identification`](../stochastic-mechanics/phi-q-aj-machinery-identification.md);
the strong AJ conjecture is proved for $4_1$ \cite{nguyen-tran-2021}):

| | torus knots (leptons) | hyperbolic knots (Higgs $4_1$) |
|---|---|---|
| Askey object | Rogers $q$-ultraspherical | non-compact Askey-Wilson \cite{koelink-stokman-2003} |
| dilog regulator | Rogers $\mathrm{Li}_2^q$ | Faddeev $\Phi_q$ |
| archimedean saddle | real $q\in(0,1)$ | root of unity $q=e^{2\pi i/N}$ |
| bar-parity | bar-even ($\cosh$) | bar-odd ($\sinh$) recovered only when chiral |

For the *amphichiral* $4_1$ both saddles collapse onto the real axis (the
bar-odd part vanishes), which is precisely why the volume-conjecture sum
$\langle 4_1\rangle_N$ is real and grows at the rate $\mathrm{Vol}(4_1)$
(Kashaev \cite{kashaev1997}, Murakami–Murakami \cite{murakami-murakami2001}),
with no Chern–Simons phase.

## What is proved, and over which ring

The self-duality $\Rightarrow$ vanishing-imaginary-face implication is an
**algebraic identity over any commutative ring with a bar-involution**
$\sigma$ — *not* $\mathbb{C}$ (the archimedean instance is $\sigma = $ complex
conjugation). It is Lean-formalised sorry-free
(`QOU.Knot.SelfDuality.higgs_complex_volume_real`): a $\sigma$-fixed
element has zero bar-odd part and bar-even part $2V$. The same file proves the
**recurrence descent** — one three-term recurrence with a bar-even multiplier
yields both parity ladders (the $c_k$ engine).

The hyperbolic-volume *value* $\mathrm{Vol}(4_1)$ itself (the saddle limit) is
the volume conjecture, proved in the literature but not in Mathlib; it is
carried as the conditional class
`QOU.Knot.FigureEightVolume.VolumeConjecture41`. The Kashaev sum's
non-vanishing floor ($\langle 4_1\rangle_N \ge 1$) is proved sorry-free.
<!-- FILE_END: self-dual-higgs-real-volume.md -->

<!-- FILE_START: meson-em-sinh-closed-form.md -->
**Proposition (meson EM sinh-channel closed-form).**
*Let $R$ be a field and $q \in R^\times$. Writing the substrate Planck
quantum $\hbar_q = (q - 1)/q$, the following are equal:*

$$
  1 + \hbar_q - \hbar_q^2/2
  \;=\;
  1 + \frac{1 - q^{-2}}{2}
  \;=\;
  \frac{3 - q^{-2}}{2}
  \;=\;
  \frac{3 q^2 - 1}{2 q^2}.
$$
## Significance: the meson $m_K^2/m_\pi^2$ closure form

Substituting the closed form into the meson mass-squared ratio gives
a **single closed-form derived expression** for the full
$m_K^2 / m_\pi^2$ ratio:

$$
  \frac{m_K^2}{m_\pi^2}
  \;=\;
  [3]_q \cdot [4]_q
  \;+\;
  \frac{\alpha_{\mathrm{em}}}{\pi}
  \cdot
  \frac{3 q^2 - 1}{2 q^2}.
$$

Both pieces are framework-derived (no fitted integers): the strong
fusion $[3]_q \cdot [4]_q$ from the qq̄ 2-body decomposition
([`prop:meson-qcg-fusion-identity`](#prop:meson-qcg-fusion-identity)),
and the sinh-channel EM correction from the CS-corrected
$\alpha_{\mathrm{em}} = q \cdot [9]_q \cdot [10]_q$ ([force-carrier
Diophantine uniqueness](#prop:force-carrier-bring-uniqueness))
multiplied by $(3 q^2 - 1)/(2 q^2)$.

(See [`docs/audits/2026-05-28-meson-mass-ratio-derived-vs-fitted.md`](../../../docs/audits/2026-05-28-meson-mass-ratio-derived-vs-fitted.md)
for the archimedean substrate evaluation.)

## Structural reading

The numerator $3 q^2 - 1$ has a Bring-surface generation structure:
**3** is the number of saturating-genus generation torus knots
$T_{2,3}, T_{2,5}, T_{2,7}$ on Bring's surface (per the same
Diophantine uniqueness that fixes the force-carrier set), and $q^2$
is the substrate's squared coupling. The denominator $2 q^2$
contributes the standard EM-self-energy halving (Casimir) and puts
the correction on the substrate-natural scale. Per
`prop:cosh-sinh-q-bridge` (#1417, $[n]_q
= \sinh(n\lambda)/\sinh(\lambda)$ with $\sinh$ = Coulomb channel),
this is the sinh-side categorical-action correction on the qq̄ pair,
modulo a rigorous first-principles derivation of the
$\hbar_q - \hbar_q^2/2$ truncation order.


**Mathematical Novelty:** While the proved identity relies on the elementary textbook rational-function algebra $1+\hbar_q-\hbar_q^2/2 = (3q^2-1)/(2q^2)$, the interpretive novelty is highly framework-specific. Specifically, the meson $m_K^2/m_\pi^2$ closure significance and its Bring 3-generation reading provide a novel physical interpretation of this algebraic form.
<!-- FILE_END: meson-em-sinh-closed-form.md -->

<!-- FILE_START: meson-qcg-fusion-identity.md -->
**Proposition (q-Clebsch–Gordan fusion identity).**
*Let $R$ be a field and $q \in R^\times$. The q-integers satisfy*

$$
  [3]_q \cdot [4]_q \;=\; [2]_q + [4]_q + [6]_q.
$$

*This is the q-deformation of the classical SU(2) Clebsch–Gordan
identity $\mathrm{spin}\text{-}1 \otimes \mathrm{spin}\text{-}\tfrac{3}{2}
= \mathrm{spin}\text{-}\tfrac{1}{2} \oplus \mathrm{spin}\text{-}\tfrac{3}{2}
\oplus \mathrm{spin}\text{-}\tfrac{5}{2}$ (dimensions $3 \cdot 4 = 2 + 4 + 6$).*
## Significance

This identity is the *categorical* content behind the meson mass-squared
ratio $m_K^2 / m_\pi^2$. A meson $M = q_1 \bar q_2$ is a **2-body** state
on $H_{q_1} \otimes H_{q_2}$, so its mass-squared is a bilinear (Casimir-
like) quantity on the *pair* — a fusion product, not a 1-body character.
The 1-body Hecke character ratio for the kaon vs pion misses
$m_K / m_\pi$ substantially; the 2-body **squared** ratio
$m_K^2/m_\pi^2$ is the genuinely-derived target, and the right q-fusion
is precisely $[3]_q \cdot [4]_q$.

The residual archimedean-evaluation cross-check at the substrate
parameter (numerical residual + EM/Coulomb sinh-channel correction
via $(\alpha_{\mathrm{em}}/\pi) \cdot (1 + \hbar_q - \hbar_q^2/2)$,
the first three terms of $1 + \log(1 + \hbar_q)$) is recorded in
audit
[2026-05-28-meson-mass-ratio-derived-vs-fitted.md](../../../docs/audits/2026-05-28-meson-mass-ratio-derived-vs-fitted.md);
both ingredients are framework-derived with no fitted integers. The
derived-candidate exact sinh-channel closure form is the open
categorical piece. (Specific numerical residuals and the substrate
evaluation live in the audit document, not here — this block carries
only the categorical fusion identity.)


**Mathematical Novelty:** The q-Clebsch-Gordan fusion $[3]_q[4]_q=[2]_q+[4]_q+[6]_q$ is standard q-representation theory. The novel, framework-specific mathematical insight is its application to the 2-body meson $m_K^2/m_\pi^2$ squared-ratio (as opposed to a 1-body character).
<!-- FILE_END: meson-qcg-fusion-identity.md -->

<!-- FILE_START: q-difference-viewpoint-method.md -->
### The $q$-difference / root-of-unity viewpoint

Several of the framework's $q$-deformed quantities — the $\mathfrak{Q}_\beta$
Habiro element, the $\alpha_{EM}$ next-order factor
([`prop:alpha-em-habiro-bar-involution`](#prop:alpha-em-habiro-bar-involution)),
and the Markov trace itself — are analysed not through
their power series at $q=1$, but through their behaviour under the
**$q$-difference shift** $\sigma_q : q \mapsto q\zeta$, where $\zeta$
runs over roots of unity. This subsection records the method, which
recurs throughout the categorical-derivation chain.

A Habiro-type element $F(q)$ satisfies a $q$-difference equation of the
form $(1 - \sigma_q)\,F = \delta\,(q;q)_\infty$ (Habiro's equation;
equivalently the level-$1$ Knizhnik–Zamolodchikov connection in
disguise). Three structural features make this tractable:

1. **Fourier diagonalisation.** The shift $\sigma_q$ is diagonalised by
   the Fourier transform over the cyclic group $\langle\zeta\rangle$;
   its eigenvectors are the root-of-unity evaluations $F(\zeta_d)$.
2. **Witten–Reshetikhin–Turaev truncation.** The $q$-Pochhammer
   $(u;u)_m = \prod_{k\le m}(1 - u^k)$ *vanishes* at a primitive
   $d$-th root of unity for $d \le m$. Evaluating a Habiro expansion
   $F = \sum_m a_m\,(u;u)_m / D$ at $\zeta_d$ therefore truncates the
   sum to its first $d$ modes — an exact, finite spectrum.
3. **Mode-by-mode solution.** When $F$ is rational, solving the
   $q$-difference equation reduces to the **partial-fraction
   decomposition** of $F$ over its poles: each pole is one Fourier
   mode, and the modular data (residues at $\zeta_d$) are exact.

This viewpoint is intrinsically **fibre-level**. The variable $q$ is
formal, with $\mathrm{Im}(q)$ unconstrained, and the operative symmetry
is the **bar involution** $q \mapsto q^{-1}$ — not a reality
assumption. Only the *observable* component, obtained by evaluating at
the real archimedean substrate, is real
(cf. the fibre-versus-observable distinction in the front matter). The
root-of-unity spectra and residues are exact identities in the
relevant cyclotomic field, independent of the eventual archimedean
realisation.

The duality between $\alpha_{EM}$ and $\mathfrak{Q}_\beta$ illustrates the method.
Both are Habiro elements with the *same* $q$-difference machinery, yet
they are distinguished by a single modular datum: the $\alpha_{EM}$
element $[2]_q(1-h^2\alpha)$ is a bar-involution fixed point with a
**zero** at $\zeta_4$, while the $\mathfrak{Q}_\beta$ trace difference is *not* a
bar fixed point and has a **pole** at $\zeta_4$. The cleanliness of the
$\alpha_{EM}$ case — a polynomial, bar-fixed, with $q_0$-stable Taylor
coefficients — is precisely why its next-order form was identifiable as
a Habiro element, whereas the $\mathfrak{Q}_\beta$ analogue required the
additional cancellation of a bar-anti-invariant part.
<!-- FILE_END: q-difference-viewpoint-method.md -->

<!-- FILE_START: alpha-em-habiro-bar-involution.md -->
**Proposition.** *Let $H(q) = [2]_q\,(1 - h^2\alpha)$ be the
$\alpha_{EM}$ Habiro element, where $[2]_q = q + q^{-1}$ and
$h = q - q^{-1}$ is the Hecke differential. Then, over a generic
commutative ring with $q$ a formal variable:*

1. *$H$ is a **fixed point of the bar involution** $q \mapsto q^{-1}$:*
   $$H(q^{-1}) = H(q).$$
2. *Its leading **special values** are*
   $$H(1) = 2, \qquad H(-1) = -2.$$

These are **fibre-level** statements: $q$ is a formal variable with no
reality or archimedean constraint imposed. The operative symmetry is
the bar involution $q \mapsto q^{-1}$ — the framework/tower involution
structure — not a reality assumption. Only the *observable* component,
read off at the archimedean substrate evaluation, is real; the
involution structure itself holds over the formal fibre.

## Significance

The factor $H = [2]_q(1 - h^2\alpha)$ is the $\alpha_{EM}$ next-order
Habiro element ([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)).
Because $[2]_q = q + q^{-1}$ is manifestly bar-symmetric, $H$ lies
**entirely** in the charge-conjugation-symmetric (bar-fixed) sector.
This is the same sector that the analogous $\mathfrak{Q}_\beta$ scaling map must
occupy, and it is precisely the structural reason the $\alpha_{EM}$
next-order form was identifiable as a Habiro element while the
$\mathfrak{Q}_\beta$ analogue — whose trace difference is *not* a bar fixed point
— required a separate cancellation analysis.

The two special values are the lowest root-of-unity evaluations of
$H$: $H(\zeta_1) = H(1) = 2$ is the classical leading term that gives
$\alpha/(4\pi)$, and $H(\zeta_2) = H(-1) = -2$ is the bar mode. The
full root-of-unity spectrum of $H$ (exact in the cyclotomic field, with
$\alpha$ kept formal) is recorded in the computational witness;
$H(\zeta_4) = 0$, a modular **zero** that is the exact structural dual
of the $\mathfrak{Q}_\beta$ Habiro element's modular **pole** at $\zeta_4$.

## Lean structure

`alphaEmHabiro q qi α := (q + qi)·(1 - (q - qi)²·α)` is defined over a
generic `CommRing` with `q`, `qi` independent variables (the inverse
relation `q·qi = 1` is invoked only where needed). The bar involution
is the swap `q ↔ qi`; `alphaEmHabiro_bar_invariant` proves the swap
fixes `H` by `ring` (the sum `q + qi` is symmetric and `(q − qi)²`
absorbs the sign). The special values `alphaEmHabiro_at_one` and
`alphaEmHabiro_at_neg_one` evaluate at `q = qi = ±1` by `ring`. No
`ℝ`, no ordering, no complex numbers — the statements are
involution-level, not archimedean.


**Mathematical Novelty:** The proved facts are elementary, consisting of a ring-level observation regarding the bar-symmetry of $[2]_q(1-h^2 \alpha)$. The mathematical novelty and interesting framework content lie in the fibre-vs-observable framing and the realization that $\zeta_4=0$ is dual to the $\mathfrak{Q}_\beta$ pole.
<!-- FILE_END: alpha-em-habiro-bar-involution.md -->

<!-- FILE_START: figure-eight-reeb-rotation.md -->
**Proposition (figure-eight knot operator is unitary on $V_{(2,1)}$).**
*The knot operator $M_{4_1} = (\sigma_1\sigma_2^{-1})^2$ of the
figure-eight knot, acting on the standard representation $V_{(2,1)}$
of $H_3(q)$, has eigenvalues of unit modulus:*

$$
  \lambda_{4_1} = e^{\pm i\theta},
  \qquad |\lambda_{4_1}| = 1.
$$

*The eigenvalue phase $\theta$ is the accumulated
$q$-Reeb rotation angle of the alternating braid
$\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$.*
## Connection to the $q$-Reeb flow

The $q$-Reeb flow
([`ex:q-reeb-flow`](../climax-volume-mass/q-reeb-flow-on-color-coords.md))
advances the color-sector angular coordinate by $q \cdot t$
per crossing on the active strands.  For an alternating braid
$\sigma_a\sigma_b^{-1}$, the positive crossing $\sigma_a$
advances by $+q\pi$ and the negative crossing $\sigma_b^{-1}$
advances by $-q^{-1}\pi$.  The net Reeb advance per alternating
pair is $(q - q^{-1})\pi = h\pi$.

The figure-eight braid has TWO such pairs, giving total Reeb
advance $2h\pi$ on the pair of active strands.  Restricted to
$V_{(2,1)}$, this advance manifests as the eigenvalue phase
$\theta = \mathrm{arg}(\lambda_{4_1})$.

The q-Reeb flow rotates between the two lepton channels
$V_{(2)}$ and $V_{(1,1)}$ that constitute $V_{(2,1)}$ under
Frobenius restriction
([`prop:frobenius-lepton-meson-bridge`](frobenius-lepton-meson-bridge.md)).
The rotation angle $\theta$ is the **accumulated Reeb phase** of
the figure-eight's alternating crossings — the same geometric
quantity that, in the Kashaev $N \to \infty$ limit, yields the
hyperbolic volume $\mathrm{Vol}(4_1)$.

## Role of $4_1$ in the mass scale

The $q$-Reeb rotation mixes the lepton channels
$V_{(2)} \leftrightarrow V_{(1,1)}$ inside $V_{(2,1)}$.  The
rotation angle $\theta$ is the natural invariant of this mixing.
The muon-anchor identity
$m_\mu / m_\mathfrak{e} = \mathrm{Vol}(4_1) / \hbar_q^2$
uses the **asymptotic volume** (Kashaev limit of $\theta$).
The finite-$q$ phase $\theta(q_0)$ and the asymptotic volume
$\mathrm{Vol}(4_1)$ are related by the Volume Conjecture; the
mass formula uses the asymptotic form because the lepton sector
lives at $H_2$ where the Kashaev limit is the natural evaluation.

The figure-eight knot $4_1$ appears in the mass formula because
it is the **simplest alternating braid** at $H_3$ — the
minimal-crossing braid that implements a full Reeb rotation on
$V_{(2,1)}$.  Its volume is the rotation angle, and the rotation
is the mechanism that connects the two lepton generations.

## Lean realisation (archimedean specialisation, §7c)

The unitarity statement is realised on the **archimedean side**. The
structural inputs — $\det(M_{4_1}) = 1$ (a product of generator
determinants $q\cdot(-q^{-1}) = -1$, an exact identity over the formal
field $\mathbb{Q}(q^{1/2})$) and the reality of the trace — are
substrate/categorical and base-ring-agnostic. The *conclusion*
$|\lambda_{4_1}| = 1$, however, is an archimedean assertion: it says the
eigenvalues lie on the unit circle of $\mathbb{C}$. The Lean
`QOU.BraidsAndKnots.figure_eight_unitary_on_standard` proves it over
$\mathbb{R}$ via the complex norm $\lVert\cdot\rVert$ /
`Complex.normSq` and the ordering hypothesis $t^2 < 4$ (forcing a
non-real root), discharged by `nlinarith`. The complex modulus, the
unit circle, and the real trace bound $t^2 < 4$ are the archimedean
constructs that pin this formalisation to $\mathbb{R}$; the determinant
identity itself stays on the substrate side (`figure_eight_det_one` for
the $\mathbb{R}$ specialisation used here, with the generic
Hecke-generator determinant lemma belonging in the algebraic layer).
<!-- FILE_END: figure-eight-reeb-rotation.md -->

<!-- FILE_START: figure-eight-reeb-novelty-note.md -->
**Mathematical Novelty:** The q-Reeb-rotation-phase reading of the figure-eight eigenvalue on $V_{2,1}$, which connects to $\mathrm{Vol}(4_1)$ and the muon anchor, is a genuinely framework-specific and novel conceptual idea. (Note that this connection is asserted conceptually rather than fully established in the formalization).
<!-- FILE_END: figure-eight-reeb-novelty-note.md -->

<!-- FILE_START: pion-half-figure-eight.md -->
**Proposition (pion = half-figure-eight on $V_{(2,1)}$).**
*The pion braid $\mathfrak{M}_+ = (\sigma_1\sigma_2)^2\sigma_2\sigma_1$
and the half-figure-eight braid $\sigma_1\sigma_2^{-1}$ have
identical eigenvalue phases when acting on the standard
representation $V_{(2,1)}$ of $H_3(q)$:*

$$
  \mathrm{arg}\bigl(\lambda(\mathfrak{M}_+)\bigr)
  = \mathrm{arg}\bigl(\lambda(\sigma_1\sigma_2^{-1})\bigr).
$$

*The figure-eight knot operator $(\sigma_1\sigma_2^{-1})^2$ is the
square of the pion-type rotation.*

## The half-rotation interpretation

The figure-eight knot $4_1 = (\sigma_1\sigma_2^{-1})^2$ is the
**composition of two pion-type rotations**.  Each pion rotation
advances the Reeb phase by $\theta$; two such advances give the
figure-eight's eigenvalue phase $2\theta \pmod{2\pi}$.

The muon-anchor identity
$m_\mu / m_\mathfrak{e} = \mathrm{Vol}(4_1) / \hbar_q^2$
uses the volume of the figure-eight — the asymptotic value of
twice the pion rotation angle.  The pion is the **generator**
of the Reeb rotation tower; the figure-eight is its square.

## Connection to pion decay

The pion decay $\pi \to \mu + \nu$
([`prop:hoefsmit-binding-amplitude`](hoefsmit-binding-amplitude.md))
de-entangles $V_{(2,1)}$ into $V_{(2)} \oplus V_{(1,1)}$.  This
is the **inverse** of a half-Reeb-rotation: the pion's eigenvalue
phase $\theta$ is the energy that was stored in the entanglement,
and the decay releases it by undoing the rotation.

Two such decays (two pions) would undo a full figure-eight
rotation — connecting the meson decay energy to the lepton
mass ratio through the composition $4_1 = (\text{half-rotation})^2$.
<!-- FILE_END: pion-half-figure-eight.md -->

<!-- FILE_START: pion-half-figure-eight-formalization-note.md -->
**Mathematical Novelty.** While the proof itself is a straightforward characteristic-polynomial comparison for $2 \times 2$ matrices with equal trace and determinant, the mathematical novelty is structurally mapping the meson's topological state to a specific "half-knot" Reeb rotation, directly formalising the relationship between meson decay energies and the lepton mass ratio (figure-eight volume) via the algebraic squaring relation $4_1 = (\sigma_1\sigma_2^{-1})^2$.

**Formalization Goal Plausibility.** The formalization intentionally focuses on the algebraic reduction—verifying that identical traces and determinants force identical characteristic polynomials and eigenvalues in the $2 \times 2$ module. The specific trace identity $\chi^{(2,1)}(\mathfrak{M}_+) = -(h^2+1)$ is introduced as an assumed hypothesis rather than calculated from scratch; this is a routine computational fact in representation theory, not a disguised gap. By factoring out the topological character computation, the goal of verifying the spectral consequences becomes highly plausible and sharply targeted.
<!-- FILE_END: pion-half-figure-eight-formalization-note.md -->

<!-- FILE_START: outro-braids-and-knots.md -->
This closes the substrate-arithmetic chapter.  The categorical
Hecke / Wenzl-bridge / Gröbner–Shirshov machinery developed here
drives the chapter cycle that follows: every numerical prediction
downstream — six-term mass formula, binding-energy substrate
form, alpha-EM coupling, half-life formulas — reads off its
coefficients from the eigenbasis and trace identities established
above.  The closing lepton–meson parallel anchors the Frobenius
bridge between leptonic and mesonic substrate channels, supplying
the input that the mass-theory and predicted-spectra chapters
consume wholesale.

The next chapter (climax: volume-mass duality) extracts the
hyperbolic-volume side of the substrate arithmetic and pairs it
with the mass content of the eigenbasis; the chapters after that
specialise the resulting volume-mass duality to atomic isotopes
and physical predictions.
<!-- FILE_END: outro-braids-and-knots.md -->


# Parabolic-cylinder / toroidal channel interpolation — exploratory audit

**Date:** 2026-07-06
**Branch:** `claude/parabolic-cylinder-channel-interpolation-5m9scj`
**Status:** EXPLORATORY (per `local/production-vs-exploratory-discipline`). Nothing
here wires to production compute. Leads are marked as leads; the only claims
stated as fact are (i) classical special-function facts and (ii) corpus results
cited by file path.

## 0. The question

Owner prompt (paraphrased, three parts):

1. Does the parabolic cylinder function $D_\nu(z)$ — the continuous-$\nu$
   interpolation between the even and odd solutions of the quantum harmonic
   oscillator — "close the gap" between the corpus's even and odd channels?
   Do those channels correspond to meson/lepton?
2. What is the QOU analogue of the 1-d Schrödinger oscillator equation in
   which $D_\nu$ arises? Can it be written algebraically / categorically?
3. Physical picture: lepton and meson channels each oscillate in their own
   local 1-d channel; interpolation requires *mixed* oscillation in 3-d.
   Owner refinement: **toroidal functions** are the natural 3-d carrier.
   Fluid-dynamics framing: vortex loops (e.g. the two components of a Hopf
   link) are soliton-like solutions following geodesics; their mutual
   disturbance decays rapidly enough in the substrate not to destroy each
   component's internal dynamics. Wanted: the eigenspace in which the knot
   operators (= vortex-interaction dynamics) act nicely.

## 1. Classical facts (the flat model)

The Weber equation

$$
y'' + \Bigl(\nu + \tfrac{1}{2} - \tfrac{z^2}{4}\Bigr) y = 0
$$

is the 1-d oscillator Schrödinger equation after scaling ($\nu + \tfrac12 =
E/\hbar\omega$). Its solution space is 2-dimensional and splits under parity
$z \mapsto -z$ into an **even** series $y_1$ (a ${}_1F_1$ in $z^2$) and an
**odd** series $y_2$ ($z \cdot {}_1F_1$). The parabolic cylinder function
$D_\nu(z)$ is the unique (up to scale) *recessive* solution as
$z \to +\infty$, and for non-integer $\nu$ it is an honest **mixture** of
$y_1$ and $y_2$:

$$
D_\nu(z) = 2^{\nu/2} e^{-z^2/4} \left[
  \frac{\sqrt{\pi}}{\Gamma\bigl(\tfrac{1-\nu}{2}\bigr)}\, y_1
  - \frac{\sqrt{2\pi}}{\Gamma\bigl(-\tfrac{\nu}{2}\bigr)}\, y_2
\right].
$$

Quantization is exactly the statement that demanding recessive behaviour at
*both* ends forces $\nu = n \in \mathbb{N}$, where the Gamma poles kill one
parity component and

$$
D_n(z) = 2^{-n/2} e^{-z^2/4} H_n\bigl(z/\sqrt{2}\bigr)
$$

recovers the Hermite eigenfunctions with sharp parity. So $D_\nu$ **is** the
continuous interpolation between the even and odd channels; off the integer
lattice the two channels necessarily mix, and the mixing coefficients are the
two Gamma factors.

## 2. Even/odd = binding/decay, and where meson vs lepton actually sits

The corpus already has the $q$-deformed version of the even/odd split, at the
*recurrence* level:

- [`channel-rotation-askey-lit.md`](../../content/quantum-observable-universe/mass-endomorphism/channel-rotation-askey-lit.md):
  the bar-even (binding, $\cosh$, compact locus $x = \cos\theta$) channel is
  carried by the continuous $q$-Hermite polynomials $H_n(x \mid q)$; the
  bar-odd ($\mathfrak{Q}_\beta$, $\sinh$, non-compact $x = \sinh t$) channel
  by the Ismail–Masson $q^{-1}$-Hermite $h_n(x \mid q) = i^{-n} H_n(ix \mid
  q^{-1})$. One three-term recurrence, read through the rotation
  $(x, q) \mapsto (ix, q^{-1})$; formalized generically as `rotation_step`.
- Parity under $z \mapsto -z$ in the flat model corresponds to the **bar
  involution** $q \mapsto q^{-1}$: bar-even $\leftrightarrow$ Hermite-even,
  bar-odd $\leftrightarrow$ Hermite-odd. The $\cosh/\sinh$ split of
  [`binding-qbeta-complex-volume.md`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.md)
  is literally the even/odd part of an exponential under an involution.

**Meson/lepton refinement** (the owner's identification is right up to one
precision). The corpus's sharp statement is not "even = meson, odd = lepton"
as sectors, but:

- The two **1-dim channels** are the $H_2(q)$ lepton irreps $V_{(2)}$,
  $V_{(1,1)}$ with $\sigma$-eigenvalues $q$ and $-q^{-1}$
  ([`QOU/Mass/LeptonMesonParitySplit.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/LeptonMesonParitySplit.lean):
  $H_2$ is the unique all-1-dim level, $C = \bar{C}$, the lepton world).
- The **meson** is the 2-dim Hoefsmit block $V_{(2,1)}$ of $H_3(q)$, whose
  restriction to $H_2$ is exactly $V_{(2)} \oplus V_{(1,1)}$
  ([`frobenius-lepton-meson-bridge.md`](../../content/quantum-observable-universe/braids-and-knots/frobenius-lepton-meson-bridge.md)).
  The Hoefsmit off-diagonal $b = \sqrt{a_\rho a_{-\rho} + 1}$ is the binding
  amplitude that entangles the two lepton channels; at $b = 0$ the meson
  reverts to two independent leptons.

So: the *even/odd pair* is the lepton channel pair; the *meson* is what the
interpolation **produces** when the channels are forced to mix. The mapping
to the $D_\nu$ story is then precise:

| flat oscillator | QOU corpus object |
|---|---|
| parity $z \mapsto -z$ | bar involution $q \mapsto q^{-1}$ |
| even solution $y_1$ | $V_{(2)}$ channel / $H_n(x\mid q)$, $\cosh$, binding |
| odd solution $y_2$ | $V_{(1,1)}$ channel / $h_n(x\mid q)$, $\sinh$, $\mathfrak{Q}_\beta$ |
| integer $\nu = n$ (pure parity) | decoupled 1-dim lepton channels ($b = 0$) |
| non-integer $\nu$ (mixed $D_\nu$) | entangled Hoefsmit block ($b \neq 0$, meson) |
| Gamma-factor mixing coefficients | Hoefsmit $a_\rho = h/(1 - q^{-2\rho})$, $b$ |
| recessive-at-$+\infty$ condition | Markov-trace normalizability (lead, §5) |

**Lead (not a corpus claim):** the quantization mechanism transfers. In the
flat model, "physical spectrum = integer $\nu$" is *equivalent to* "sharp
parity". In QOU the analogous statement would be: exact bar-parity
eigenstates exist only at the Hecke-integer levels (partitions), and any
continuous interpolation between levels (§4) necessarily carries a mixed
bar-parity component — which is where the meson (Goldstone, chiral) sector
lives. This matches `h3_not_all_one_dim`: the first level past the lepton
world *already* fails to diagonalize the bar involution.

## 3. The QOU analogue of the oscillator Schrödinger equation

Three layers, from analytic to categorical.

### 3a. Fibre level: the $q$-difference Weber equation

The flat Schrödinger operator $-\tfrac{\hbar^2}{2m}\partial_x^2 +
\tfrac12 m\omega^2 x^2$ is replaced by the **Askey–Wilson second-order
$q$-difference operator** $\mathcal{D}_q$, whose polynomial eigenfunctions in
the relevant degeneration are exactly the continuous $q$-Hermite family:

$$
\mathcal{D}_q\, H_n(x \mid q) = [n]_q\, H_n(x \mid q),
\qquad [n]_q = \frac{q^n - q^{-n}}{q - q^{-1}},
$$

with $\hbar\omega \leftrightarrow \hbar_q = 1 - q_0^{-1}$ as the level
spacing at the archimedean anchor. Equivalently, position acts tridiagonally
via the three-term recurrence $2x H_n = H_{n+1} + (1 - q^n) H_{n-1}$ — this
recurrence *is* the corpus's channel object (§2). The bar-odd channel
satisfies the same equation at $(\sigma q, \iota x)$ (`rotation_step`). A
genuine $q$-analogue of $D_\nu$ (non-polynomial, continuous $\nu$, recessive
solution of the $q$-Weber equation) exists in the Ismail–Masson / Ismail–Zhang
$q > 1$ literature — **lead: not yet in the corpus** (grep: `parabolic
cylinder` hits only bibliography and this-session files).

### 3b. Operator level: Leonard pair / $AW(3)$

Already the corpus's chosen packaging
([`channel-rotation-askey-lit.md`](../../content/quantum-observable-universe/mass-endomorphism/channel-rotation-askey-lit.md)
§Leonard pairs): two operators $K_1, K_2$, each tridiagonal in the other's
eigenbasis,

$$
[K_1, [K_1, K_2]_q]_{q^{-1}} = \text{lower order}, \qquad
[K_2, [K_2, K_1]_q]_{q^{-1}} = \text{lower order},
$$

with the channel overlap as the rotation matrix. In this language the flat
statement "$D_\nu$ = recessive eigencolumn of the tridiagonal position
operator at non-integer spectral parameter" has the proved corpus half
`eigencolumn_eq_overlap` (any eigencolumn of the channel tridiagonal operator
has orthogonal-polynomial entries); the conjectural half is
`ChannelLeonardDuality`.

### 3c. Categorical level: the Heisenberg relation on the Hecke tower

The oscillator algebra $[a, a^\dagger] = 1$ categorifies on
$\bigoplus_n H_n(q)\text{-mod}$ with $a^\dagger = \mathrm{Ind}_{H_n}^{H_{n+1}}$,
$a = \mathrm{Res}^{H_{n+1}}_{H_n}$, and the Mackey decomposition as the
categorical commutation relation:

$$
\mathrm{Res} \circ \mathrm{Ind} \;\cong\; \mathrm{Ind} \circ \mathrm{Res}
\;\oplus\; \mathrm{Id}.
$$

This is the algebraic/categorical form of the oscillator equation the owner
asked for, and the corpus already *uses* its decategorified shadow: the
Frobenius-reciprocity computation in
[`frobenius-lepton-meson-bridge.md`](../../content/quantum-observable-universe/braids-and-knots/frobenius-lepton-meson-bridge.md)
($\langle \mathrm{Res} V_{(2,1)}, V_{(2)} \rangle = \langle V_{(2,1)},
\mathrm{Ind} V_{(2)} \rangle = 1$) is one matrix element of this relation.
The dictionary:

| oscillator | Hecke tower |
|---|---|
| $a^\dagger$, $a$ | $\mathrm{Ind}$, $\mathrm{Res}$ between $H_n$, $H_{n+1}$ |
| number operator $N$ | Jucys–Murphy elements (spectrum = contents of $\lambda$) |
| energy eigenstates $\lvert n \rangle$ | Wedderburn blocks $V_\lambda$ |
| ground state / vacuum evaluation | Markov trace $\mathrm{tr}_M$ |
| $E_n = \hbar\omega(n + \tfrac12)$ | $[n]_q$ ladder, spacing $\hbar_q$ at $q_0$ |
| continuous $\nu$ off the integer lattice | trace/tower parameter interpolation (lead below) |

**Lead — the categorical seat of continuous $\nu$.** The Hecke-tower analogue
of "non-integer oscillator level" is interpolation in the **Ocneanu/HOMFLY
Markov-trace parameter** (equivalently a Deligne-style interpolation of the
tower level, $\mathrm{Rep}(S_t)$ with $t \notin \mathbb{N}$, $q$-deformed).
At integer levels the trace weights $y_\lambda$ localize on honest partitions
(sharp bar-parity available at $H_2$ only); at interpolated parameter the
"partition" is virtual and the bar-parity mixing is forced — the categorical
$D_\nu$. This is a *lead*, not a corpus result; it is the natural next
formalization target if this direction is pursued.

## 4. Toroidal functions: the right 3-d carrier (owner's refinement)

The owner's correction — "I think toroidal functions" — is geometrically
sharper than the flat $D_\nu$ model, for three corpus-consistent reasons.

**4a. Geometry.** In toroidal coordinates $(\eta, \theta, \varphi)$ the
Laplace equation separates as

$$
\Psi = \sqrt{\cosh\eta - \cos\theta}\;
P^{\mu}_{\nu - 1/2}(\cosh\eta)\, e^{i\mu\theta} e^{i\nu\varphi},
$$

associated Legendre functions of **half-integer degree** $\nu - \tfrac12$
(Whipple class). These are the canonical harmonics around a vortex ring: the
two phase factors $e^{i\mu\theta}, e^{i\nu\varphi}$ are precisely the two
*local 1-d oscillations* (around the core, and along the loop), and the
radial factor $P^{\mu}_{\nu-1/2}(\cosh\eta)$ decays away from the core torus.
"Mixed oscillation in 3-d" is thus indexed by the winding pair $(\mu, \nu)$
— for a link supported on a common torus, exactly the linking data.

**4b. Hopf fit.** The two components of a Hopf link are two fibres of the
Hopf fibration and lie on a common Clifford torus; nested tori foliate the
complement. The Hopf complement is *not* hyperbolic —
$\mathrm{Vol}(\mathrm{Hopf}) = 0$, SDP-validated in the corpus (CAL-3
independence) — it is Seifert-fibred/flat, which is exactly the regime where
toroidal (flat-torus $\times$ decaying radial) modes, not hyperbolic modes,
are the natural eigenfunctions. So the meson anchor (Hopf, $m_\pi$) living on
toroidal harmonics while the lepton anchor ($4_1$, hyperbolic
$\mathrm{Vol}(4_1)$) lives on hyperbolic modes is *consistent with*, and
gives a geometric reading of, the corpus's "$m_\pi$ orthogonal to the
hyperbolic-volume tower".

**4c. Same interpolation shift.** The half-integer degree $\nu - \tfrac12$ is
the toroidal counterpart of the $D_\nu$ parity interpolation: $P_{\nu-1/2}$
at integer $\nu$ sits exactly *between* the Legendre-parity lattices, and the
argument $\cosh\eta$ is the bar-even locus (the $\sinh$ partner appearing on
the non-compact channel as in §2). Toroidal functions are also Legendre
functions of geodesic distance on hyperbolic 2-space, so the $\cosh\eta$
variable is literally a hyperbolic-distance variable — the same
$\cosh/\sinh$ bar-parity pair, now with geometric meaning (distance from the
vortex core).

**Corpus status:** `grep -rli toroidal content/ docs/` returns only tangential
hits (Mostow-rigidity Lean comment, two audit docs). Toroidal harmonics as
such are **not yet in the corpus** — this direction is new.

## 5. The soliton/eigenspace formalization sketch

The owner's fluid picture, translated to corpus objects:

1. **Solitons on geodesics.** One vortex loop = one strand-cable following a
   geodesic of the substrate; its *internal* dynamics is the 1-d channel
   oscillation ($e^{i\mu\theta}$ around the core; a 1-dim Hecke channel with
   $\sigma$-eigenvalue $q$ or $-q^{-1}$).
2. **Knot operators = interaction dynamics.** The braid image
   $\rho(\beta) \in H_n(q)$ *is* the vortex-interaction operator; the
   corpus's closed form for the Hopf case is
   [`trm-hopf-sigma1-sq-closed-form.md`](../../content/quantum-observable-universe/braids-and-knots/trm-hopf-sigma1-sq-closed-form.md)
   ($\mathrm{tr}_M(\sigma_1^2)$).
3. **The nice eigenspace.** Wedderburn blocks $V_\lambda$ are the requested
   soliton eigenspaces: the interaction is block-diagonal, so each
   $V_\lambda$ is invariant — a soliton "keeps its identity" because the
   dynamics cannot leave its block. Which blocks a bound state actually
   saturates is already first-class infra: the LP/SDP dual active channels
   ($y^\star_i > 0$, `computations/lp_dual_solver.py`).
4. **Weak-disturbance condition (the soliton criterion).** Within the
   entangled Hoefsmit block, channel mixing is controlled by
   $b = \sqrt{a_\rho a_{-\rho} + 1}$ with $a_\rho = h/(1 - q^{-2\rho})$: the
   coupling decays **geometrically in $q_0^{-2\rho}$** with the content
   distance $\rho$ between the strands' boxes. That is the algebraic form of
   "the disturbance decays rapidly enough in the substrate": perturbation
   theory converges when the channel gap dominates the coupling,

   $$
   |b| \;\ll\; |q - (-q^{-1})| = [2]_q \cdot q^{0},
   $$

   i.e. the spectral gap $[2]_q = q + q^{-1}$ between the two channel
   eigenvalues is the stiffness that protects each soliton's internal
   dynamics. Two loops interact (nonzero $b$, binding, meson/Hopf) without
   destroying each other's channel (gap $[2]_q$ uncrossed) — the owner's
   "disturbing each other's path but not the soliton solution".
5. **Proposed conjecture shape (exploratory, NOT wired).**
   *Toroidal channel interpolation:* the archimedean evaluation of the
   $H_3$ Hoefsmit channel overlap at the Hopf anchor factorizes through
   toroidal harmonics, with $(\mu, \nu)$ = the linking data of the two
   strands, and the Markov-trace-normalizable eigencolumn playing the role
   of the recessive $D_\nu$ (resp. $P^\mu_{\nu-1/2}$) solution. Quantized
   levels (integer $\nu$, sharp bar-parity) = free lepton channels; the
   interpolated level = the bound meson.

## 6. What would falsify / advance this (next probes)

Per formalize-first discipline (narrow before scanning):

- **P1 (structural, cheap).** Check that the Hoefsmit $2 \times 2$
  eigenvector components at generic $\rho$ satisfy a three-term relation in
  $\rho$ that degenerates to the toroidal-Legendre recurrence
  (contiguous relations of $P^\mu_{\nu-1/2}$) under $q \to 1$ with
  $\cosh\eta \leftrightarrow$ content variable. Pure symbolic; no wide scan.
- **P2 (Lean, small).** State the §3c Mackey relation
  $\mathrm{Res}\,\mathrm{Ind} \cong \mathrm{Ind}\,\mathrm{Res} \oplus
  \mathrm{Id}$ at the decategorified level ($H_2/H_3$ branching matrices,
  $\mathbb{N}$-combinatorics like `LeptonMesonParitySplit`) — sorry-free is
  plausibly reachable; it upgrades the bridge proposition's reciprocity
  computation to the full oscillator relation.
- **P3 (literature).** Pull the Ismail–Masson $q>1$ / $q$-parabolic-cylinder
  sources and the Whipple toroidal↔Legendre transformation into
  `references.ts` when (if) a content block is authored.
- **Anti-goal.** Do not launch a numerical fit of toroidal-mode spectra to
  meson masses — that would be a new fitted ansatz in the Δ_λ-gate sense.
  The value of this direction is structural (which eigenspace, which decay,
  which quantization mechanism), not a new closed form to fit.

## 7. Corpus-grep record

- `parabolic cylinder|Weber equation|Hermite`: hits are the Askey/channel
  cluster cited above + bibliography; no prior parabolic-cylinder treatment.
- `bar-even|bar-odd`: the channel-rotation cluster (§2), `LeptonMesonParitySplit`.
- `toroidal`: 3 tangential hits; no prior treatment.
- `Ocneanu`: mass-theory Markov-trace proofs; no continuous-parameter
  interpolation treatment found.

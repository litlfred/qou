# Parabolic cylinder $D_\nu(z)$ as the even/odd channel interpolator — QOU analogue exploration

**Date:** 2026-07-03
**Branch:** `claude/parabolic-cylinder-channels-fh08ia`
**Status:** exploratory (no production wiring; no numerical claims). Three owner
questions answered structurally; candidate identifications + follow-ups listed.

## Owner questions

1. Does the parabolic cylinder function $D_\nu(z)$ close the gap for
   *interpolating the even and odd channels* — and do those channels
   correspond to the meson / lepton channels?
2. What is the QOU analogue of $D_\nu$'s natural home, the 1-d quantum
   harmonic oscillator Schrödinger equation
   $\bigl[-\tfrac{\hbar^2}{2m}\partial_x^2 + \tfrac12 m\omega^2 x^2\bigr]\psi = E\psi$?
3. Can the vortex-loop soliton picture (Hopf link as two mutually weak,
   rapidly-decaying soliton disturbances on geodesics) be written as
   algebraic / categorical equations, with a nice eigenspace for the knot
   dynamics?

## 1. Classical facts being transported

Weber's equation

$$
\frac{d^2 y}{dz^2} + \Bigl(\nu + \tfrac12 - \tfrac{z^2}{4}\Bigr) y = 0
$$

is the QHO Schrödinger equation after rescaling; $D_\nu(z)$ is its recessive
solution. Three facts carry all the structure:

- **Integer $\nu$ = the oscillator tower.** For $\nu = n \in \mathbb{N}$,
  $D_n(z) = 2^{-n/2} e^{-z^2/4} H_n(z/\sqrt2)$ — the Hermite bound states,
  $E = \hbar\omega(n + \tfrac12)$. Normalizability *quantizes* $\nu$.
- **Parity selection by $\Gamma$-poles.** With $y_1$ (even) and $y_2$ (odd)
  the standard parity solutions,

  $$
  D_\nu(z) \;=\; 2^{\nu/2}\sqrt{\pi}\,
  \Bigl[\frac{y_1(z)}{\Gamma\bigl(\tfrac{1-\nu}{2}\bigr)}
        \;-\; \frac{\sqrt2\, y_2(z)}{\Gamma\bigl(-\tfrac{\nu}{2}\bigr)}\Bigr].
  $$

  At $\nu$ an even integer, $1/\Gamma(-\nu/2) = 0$ kills the odd part; at
  $\nu$ odd, $1/\Gamma(\tfrac{1-\nu}{2}) = 0$ kills the even part. **At
  non-integer $\nu$, $D_\nu$ is a genuine mixture of the even and odd
  channels** — this is exactly the "interpolation" the owner is pointing at:
  one analytic family whose integer points alternate parity, with the parity
  projection implemented by pole-vanishing, not by an external projector.
- **Two sublattices, one function.** The even-$\nu$ and odd-$\nu$ sublattices
  are two separate towers *only* when read at integers; the continuous-$\nu$
  object is irreducibly one family.

## 2. Channel correspondence: yes — bar-even/meson vs bar-odd/lepton (with the corpus's precise names)

The corpus already fixes what "even channel" and "odd channel" mean, and the
correspondence the owner conjectures is exactly the standing one:

| classical | QOU channel | physics proxy | corpus home |
|---|---|---|---|
| even Hermite tower ($\cosh$-like) | **bar-even** ($q \leftrightarrow q^{-1}$-symmetric), compact locus $x = \cos\theta$ | binding / **meson scale** ($m_\pi$, CAL-3) | $H_n(x\,\vert\,q)$, [`channel-rotation-askey-lit`](../../content/quantum-observable-universe/mass-endomorphism/channel-rotation-askey-lit.md) |
| odd Hermite tower ($\sinh$-like) | **bar-odd** (antisymmetric), non-compact locus $x = \sinh t$ | $\mathfrak{Q}_\beta$ / **weak-lepton scale** (CAL-2) | Ismail–Masson $h_n(x\,\vert\,q)$, same block |

Precision on the naming: "meson/lepton" is the *proxy* labelling via the
calibration table (CAL-3 $= \mathfrak{D}_\pi$ meson width, bar-even $\cosh$;
CAL-2 $= \mathfrak{D}_\beta$ weak width, bar-odd $\sinh$ — the AGENTS.md
cheat-sheet's "$Q_\beta$ is the bar-odd $\sinh$ partner of the bar-even
$\cosh$ meson scale $m_\pi$"). The invariant statement is the bar-parity
split of the complex volume
[`conj:binding-qbeta-complex-volume`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.md):
$\mathrm{Re}\,\mathfrak{V} = $ binding (even), $\mathrm{Im}\,\mathfrak{V} =
\mathfrak{Q}_\beta$ (odd).

**What is genuinely new in the $D_\nu$ lens** (corpus-grep verified: no prior
"parabolic cylinder" / Weber occurrence in `content/`, `docs/`,
`computations/`): the corpus so far relates the two channels by a *rotation*
(the Askey rotation $x \mapsto ix$, $q \mapsto q^{-1}$, formalized as
`rotation_step`) and by *projections* ($P_{\mathrm{avg}}$ / $P_{\mathrm{skew}}$).
$D_\nu$ adds a third, stronger mechanism: a **single continuous-index family
containing both integer towers**, with parity selection by pole-vanishing.
Interpolation ≠ rotation ≠ projection; the three should be kept distinct.

## 3. The QOU analogue of the oscillator equation

The substrate has no $\partial_x^2$; the analogue of the Schrödinger
eigenproblem is a **second-order $q$-difference eigenproblem**, and its
bound-state basis is already the corpus's proved binding basis:

- **Algebraic form ($q$-oscillator).** Replace the Heisenberg pair by the
  $q$-oscillator algebra

  $$
  a\,a^{\dagger} - q\,a^{\dagger}a = 1,
  \qquad
  a^{\dagger}a = [\,N\,]_q = \frac{1 - q^{N}}{1 - q},
  $$

  so the equally-spaced spectrum $n + \tfrac12$ deforms to $q$-integers
  $[n]_q$ (Atakishiyev–Suslov $q$-oscillator). This is the "oscillation in
  its own local 1-dim channel": one ladder algebra per channel.
- **Function form.** The $x$-representation eigenfunctions are the
  continuous $q$-Hermite / Rogers–Szegő polynomials — the corpus's
  [`QOU.Mass.BindingQHermiteOscillator`](../../content/quantum-observable-universe/lean/QOU/Mass/BindingQHermiteOscillator.lean)
  (`FollowsRogersSzego`, with the $q \to 1$ collapse and the even/odd
  two-step decoupling at $t = -1$ proved sorry-free). The eigenoperator is
  the Askey–Wilson divided-difference operator (the $q$-deformation of
  $-\partial_x^2 + x^2$); the Hermite weight $e^{-x^2}$ deforms to the
  $q$-Gaussian, whose moments are the $q$-involution numbers — already
  identified with the binding period $a_D^{(n)}$
  ([2026-06-26 audit](2026-06-26-binding-period-qinvolution-qhermite-identification.md)).
- **Scale dictionary.** $\hbar \to \hbar_q = 1 - q_0^{-1}$; $\omega \to$
  per-channel level spacing; $E_n = n + \tfrac12 \to$ $q$-integer spectrum.

So the answer to Q2 is: **the oscillator equation is already in the corpus,
as the Rogers–Szegő / $q$-Hermite recurrence + the $q$-oscillator ladder
algebra; what is missing is precisely the $D_\nu$ layer — the
continuous-index solution.**

## 4. The candidate $q$-$D_\nu$: three identification levels

What object interpolates the even and odd $q$-Hermite towers at continuous
$\nu$? Three levels, increasing in depth:

1. **Recurrence level (fibre, formalizable now).** The three-term recurrence
   / $q$-difference equation makes sense at continuous degree; the
   $\Gamma$-pole parity mechanism $q$-deforms verbatim with
   $\Gamma \to \Gamma_q$ (which has the same pole lattice at non-positive
   integers). A $q$-Weber combination

   $$
   D^{q}_{\nu} \;=\; c(\nu)\,
   \Bigl[\frac{y^{q}_1}{\Gamma_q\bigl(\tfrac{1-\nu}{2}\bigr)}
     - \frac{\sqrt2\, y^{q}_2}{\Gamma_q\bigl(-\tfrac{\nu}{2}\bigr)}\Bigr]
   $$

   collapses to the pure even (resp. odd) channel at integer $\nu$ by the
   same pole-vanishing. This extends `BindingQHermiteOscillator` (whose
   $t = -1$ two-step decoupling is the parity split) by one continuous
   index; it is a §3b-class candidate, not yet a theorem.
2. **Rotation level (where it must live).** In QOU the two towers are *not*
   two solutions over one measure — the even channel is compact
   ($x \in [-1,1]$, determinate) and the odd channel non-compact
   ($x \in \mathbb{R}$, indeterminate moment problem), related by the Askey
   rotation. So the honest $q$-$D_\nu$ interpolates *across the rotation*,
   i.e. it lives where compact and non-compact are unified: the **modular
   double / Faddeev $\Phi_q$ level** (Ponsot–Teschner $b \leftrightarrow
   1/b$), consistent with the corpus's $\Phi_q$ (non-compact) vs
   $\mathrm{Li}_2^q$ (Rogers, compact) context-sorting. Prediction: the
   correct $q$-parabolic-cylinder object is a Faddeev-type non-compact
   special function / Askey–Wilson *function* (the non-polynomial,
   continuous-degree completion of the scheme), not a polynomial.
3. **Categorical level (interpolated tower level).** Continuous $\nu$ =
   non-integer tower level $n$. The categorical machine for that is
   Deligne-style interpolation (generic-parameter Temperley–Lieb /
   $\mathrm{Rep}(S_t)$): the channel category at non-integer level, in which
   the binding period $a_D^{(n)}$ ($q$-involution numbers = $q$-Hermite
   moments) acquires meaning at continuous $n$. "Closing the gap" then reads:
   **the mesonic (even) and leptonic (odd) towers are the integer points of
   one interpolated family object in the channel category.**

**"Mixed oscillation in 3d."** The owner's phrasing has a precise algebraic
home already cited in the corpus: Zhedanov's $AW(3)$ algebra — *three*
generators (two channel operators, each tridiagonal in the other's
eigenbasis, plus their commutator) closing on a quadratic algebra. The
Askey–Wilson overlap coefficients are the "rotation matrix" between the
meson and lepton eigenbases (`eigencolumn_eq_overlap`, proved;
`ChannelLeonardDuality`, conjectural). A $q$-$D_\nu$ is then an eigenvector
of the Leonard pair at *continuous* spectral parameter — the "mixed 3d
oscillation" is $AW(3)$, and the 3 is the same 3 as the three
$H^1(\mathrm{Bring})$ calibration DOF (scale + modulus + orthogonal class),
which is a suggestive count-match, flagged here as exactly that (a
count-match, not a derivation).

## 5. The soliton / vortex picture as algebra (Q3)

The owner's fluid picture maps onto standard factorized-scattering algebra,
with every ingredient already present in the corpus:

1. **Solitons on geodesics.** The corpus's
   [`geodesic-vortices`](../../content/quantum-observable-universe/fluid-dynamics/geodesic-vortices.md)
   block: vortex filaments are critical points of $\mathcal{E}_q$; at
   $q \to 1$ the gauge term reduces to Biot–Savart self-induction — the
   **Hasimoto soliton**. So "sets of soliton-like solutions following the
   geodesic path" = geodesic vortices, literally.
2. **"Weak enough not to disrupt internal dynamics" = factorization.** The
   algebraic statement that two soliton trains pass through each other with
   only a phase shift (no internal-state production) is the **Yang–Baxter
   equation** for the two-vortex scattering operator:

   $$
   (R \otimes 1)(1 \otimes R)(R \otimes 1)
   \;=\;
   (1 \otimes R)(R \otimes 1)(1 \otimes R).
   $$

   This is why "the knot operators are the dynamics of the vortex
   interaction": the braiding $R$-matrix of $\mathbf{C}$ *is* the two-soliton
   S-matrix (sine-Gordon solitons forming quantum-affine multiplets is the
   classical precedent for solitons carrying quantum-group charges).
3. **The Hopf link, exactly.** Two vortex loops, linking number 1: in the
   2-strand algebra $H_2(q)$ the interaction is $\sigma_1^2$, decomposed by
   the corpus's Wedderburn projectors
   ([`van-der-waals-hopf-channel`](../../content/quantum-observable-universe/information-theory/van-der-waals-hopf-channel.md))

   $$
   e_{+} = \frac{\sigma + q^{-1}}{q + q^{-1}},
   \qquad
   e_{-} = \frac{q - \sigma}{q + q^{-1}},
   \qquad e_+ + e_- = 1,\quad e_\pm^2 = e_\pm,
   $$

   with $\sigma$-eigenvalues $q$ (symmetric) and $-q^{-1}$ (antisymmetric).
   $\mathrm{Vol}(\text{Hopf}) = 0$: linked but not bonded — the interaction
   carries no shared volume, matching "disturbing each other's path without
   disturbing the soliton solution."
4. **"Disturbances rapidly decay in the substrate" = the eigenvalue gap.**
   Per crossing, the antisymmetric channel is suppressed relative to the
   symmetric one by $|{-q^{-1}}/q| = q^{-2}$ at $q_0 > 1$ — an algebraic
   decay rate per interaction, before any analysis. Independently, the
   geodesic-vortex second variation is gapped (longitudinal eigenvalues
   $[k]_q^2 \hbar_q / L_q^2$; ladder barrier $> 0$ for $q > 1$; Morse index
   0 for the fundamental vortex), so sub-gap perturbations cannot destabilize
   the soliton. These are the two decay mechanisms — one per-crossing
   (algebraic), one spectral (per-filament).
5. **The "nice eigenspace" for knot dynamics.** Assemble the above: the
   solution space the owner is asking for is the **channel eigenbasis**

   - per filament: the longitudinal/ladder weight-space decomposition of
     $\delta^2\mathcal{E}_q$ (discrete, gapped);
   - per channel: the Rogers–Szegő / $q$-Hermite tower (the $q$-oscillator
     bound states, §3);
   - per interaction: the Wedderburn $\lambda$-block decomposition of
     $H_n(q)$ ($e_\pm$ at $n = 2$), which simultaneously diagonalizes all
     the braidings — factorized scattering *is* this simultaneous
     diagonalizability;

   and the $D_\nu$-layer (§4) is what lets the eigenspace *index* move
   continuously between the even (binding/meson) and odd
   ($\mathfrak{Q}_\beta$/lepton) sublattices.

## 6. Discipline guards (what this does NOT claim)

- **No numerical claim.** The 2026-06-30 probe already showed the bar-even
  *projection* does not fix the ~38% binding MAE; interpolation is a
  different mechanism, but nothing here claims it closes any numerical
  residual. The "gap" closed in this note is structural (one family, two
  towers), not the binding error.
- **Scope-limited identifications.** The Faddeev-level identification of
  $q$-$D_\nu$ (§4 level 2) and the Deligne/TL interpolation reading (level 3)
  are candidate homes, not results. The $AW(3)$-vs-$H^1$ "3 = 3" is a
  count-match observation only.
- **Closed line respected.** The crossing-moment-as-binding-object direction
  is CLOSED (owner directive 2026-06-26); nothing here reopens it — the
  $q$-Hermite family is used as the *basis/recurrence* home, which is the
  part of that audit that stands.

## 7. Follow-ups (queued, not started)

1. **Lean §3b class `QWeberInterpolation`** extending
   `BindingQHermiteOscillator`: two-solution combination with continuous
   index; parity collapse at integer $\nu$ from $\Gamma_q$-pole-vanishing
   carried as hypothesis fields; the even/odd two-step decoupling already
   proved becomes the integer-point boundary case.
2. **Literature pass → `references.ts`**: Ismail–Masson $q^{-1}$-Hermite at
   continuous degree; Koelink–Stokman Askey–Wilson function transform;
   Atakishiyev–Suslov $q$-oscillator; classical Weber/parabolic-cylinder
   (Whittaker–Watson / DLMF ch. 12).
3. **Probe (cheap, decisive per formalize-first caveat):** evaluate a
   continuous-$\nu$ channel mixture on the Hopf channel and check whether
   the neutron-organized $B_{\mathrm{odd}}$ (2026-06-30 probe: 0.889 /
   2.757 MeV steps) sits at an interpolating $\nu$ between the integer
   sublattices.
4. **Categorical note:** generic-parameter TL / Deligne interpolation of the
   channel category as the meaning of continuous tower level (ties to the
   $a_D^{(n)}$ $q$-involution identification at non-integer $n$).

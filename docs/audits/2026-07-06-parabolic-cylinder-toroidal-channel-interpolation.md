# Parabolic-cylinder / toroidal channel interpolation — exploratory audit

**Date:** 2026-07-06
**Branch:** `claude/parabolic-cylinder-channel-interpolation-5m9scj`
**Status:** EXPLORATORY (per
[`local/production-vs-exploratory-discipline`](../../.claude/skills/local/production-vs-exploratory-discipline.md)). Nothing
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

## 7. Probe results (2026-07-06, owner-approved "p1 p2 p3")

**P1 — PASSED, and stronger than asked.** Probe:
[`computations/substrate/hoefsmit_toroidal_ladder_probe.py`](../../computations/substrate/hoefsmit_toroidal_ladder_probe.py)
(witness `hoefsmit-toroidal-ladder-probe.witness.json`, 8/8 assertions,
sympy exact). The audit asked whether the Hoefsmit mixing structure
*degenerates to* the toroidal-Legendre ladder; the probe shows the toroidal
locus is **forced**:

- The classical Young-orthogonal eigencolumns at axial distance $d$ are
  $(\sqrt{d+1}, \sqrt{d-1})$ (eigenvalue $+1$) and $(\sqrt{d-1}, -\sqrt{d+1})$
  ($-1$); the mixing amplitude is $\sqrt{d^2-1}/d$.
- Matching $d^2 - 1 = (n-\mu)(n+\mu+1)$ (the associated-Legendre order-ladder
  factor) **identically in $d$** has exactly the solutions
  $(n, \mu) = (d - \tfrac12, \tfrac12)$ up to the Legendre reflection
  $\mu \mapsto -\mu - 1$. The **half-integer degree shift $\nu - \tfrac12$ —
  the toroidal signature — is derived, not imposed.**
- The corpus Hoefsmit convention ($a_\rho = h/(1-q^{-2\rho})$,
  $b = \sqrt{a_\rho a_{-\rho} + 1}$, $h = q - q^{-1}$) satisfies
  $b^2 = [\rho-1]_q[\rho+1]_q/[\rho]_q^2$ exactly, and the forcing computation
  $q$-deforms verbatim ($q^{2\alpha+1} = 1 \Rightarrow \alpha = -\tfrac12$).
  The half-integer shift survives $q$-deformation.
- **Scope (a):** ladder-coefficient identification only — structural support
  for the §5 conjecture shape; not a full eigenfunction transform, nothing
  wired, no numerical claim.

**P2 — PASSED (sorry-free, `lean`-direct exit 0).**
[`QOU/Mass/HeckeTowerMackey.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/HeckeTowerMackey.lean):
the decategorified Mackey/oscillator relation
$R_{n+1\to n} R_{n+1\to n}^{\mathsf T} = R_{n\to n-1}^{\mathsf T} R_{n\to n-1} + \mathrm{Id}_n$
proved at levels 1 and 2 (`mackey_level1`, `mackey_level2`), plus
`level2_gram`: $R_{32}R_{32}^{\mathsf T} = \bigl[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr]$
— the off-diagonal $1$ is the meson bridge (inducing a lepton channel to
$H_3$ and restricting reaches the *other* lepton channel exactly once,
through the entangled $(2,1)$ block only). Dependency-free ℕ-combinatorics
(§7c clean); upgrades the bridge proposition's reciprocity element to the
full oscillator commutation relation of §3c.

**P3 — DONE.** Bibliography intake in `content/schema/references.ts`: the
$q$-oscillator cluster (`askey1989`, `ismail-masson1994`,
`atakishiyev-suslov1990`, `dlmf-ch12`, `deligne2007`, `zhedanov1991`) had
already landed 2026-07-03; this pass adds **`whipple1917`** (the Whipple
transformation — degree/order exchange at hyperbolic argument, the
structural home of $P^\mu_{\nu-1/2}(\cosh\eta)$) and **`lebedev1965`**
(standard toroidal-coordinates reference).

## 8. Follow-on tranche (owner picked options 1 + 2)

**Option 1 — P1 promoted to a content block (sorry-free Lean).**
[`prop:hoefsmit-toroidal-ladder-locus`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-toroidal-ladder-locus.md)
(+ proof block, registered in `sec:lepton-meson-parallel`): the forcing
theorem is now `QOU.BraidsAndKnots.toroidal_locus_forced`, proved over a
generic characteristic-zero field via `linear_combination` (no ℝ, no
ordering — §7c clean), with the validity direction `toroidal_locus_valid`.
Verified `lean`-direct exit 0 against the restored olean cache.

**Option 2 — eigenfunction-level probe (7/7 PASS).**
[`computations/substrate/whipple_rotation_involution_probe.py`](../../computations/substrate/whipple_rotation_involution_probe.py):

- **Bar-evenness of the ladder** (exact): $[d]_{q^{-1}} = [d]_q$ — the
  interpolating/mixing ladder lives entirely in the bar-even sector.
- **Whipple argument involution** (exact): $\coth(\mathrm{arccosh}(\coth a)) = \cosh a$
  — the $\cosh \leftrightarrow \coth$ exchange is an involution, the
  geometric seat of the $(\mu, \nu)$ winding exchange. *(Rendered here in
  prose; the probe verifies the radical-free squared form.)*
- **Quarter-period channel shift** (exact, corpus Lean-certified):
  $\cosh(t + i\pi/2) = i \sinh t$.
- **Whipple pairing discovered by scan** (50 dps, two generic $(\nu,\mu)$
  points): of 48 candidate pairings, exactly the DLMF 14.9.16 family is
  $a$-independent:
  $P^{-\mu}_{\nu-1/2}(\coth a) = C(\nu,\mu)\,\sqrt{\sinh a}\;Q^{\nu}_{\mu-1/2}(\cosh a)$,
  with Γ-shift laws $C(\nu,\mu+1)/C(\nu,\mu) = +1/(\nu+\mu+\tfrac12)$ and
  $C(\nu+1,\mu)/C(\nu,\mu) = -1/(\nu+\mu+\tfrac12)$ — a single
  $\Gamma(\nu+\mu+\tfrac12)$ with an alternating $\nu$-sign. Degree and
  order — the two windings — exchange exactly.
- The identification *"`rotation_step` archimedean shadow = Whipple
  involution"* remains a **lead** (necessary structural facts all verified;
  the intertwining statement itself is not yet formulated as a theorem).

## 9. Use toward the mass / binding computation (owner question, 2026-07-06)

Honest scoping first: nothing in this tranche moves an L2 dashboard number
today — no production script was touched, so both dashboards are unchanged
by construction. The value is *structural*, in four concrete directions,
ordered by nearness:

1. **A bar-parity selection rule for the Δ_λ search (usable now, prunes
   before any scan).** The mixing/interpolation ladder is bar-even (probe-
   exact: $[d]_{q^{-1}} = [d]_q$), and the binding amplitude is built from
   it ($b^2 = [d-1][d+1]/[d]^2$). So any candidate binding/Δ_λ closure whose
   mixing kernel is bar-odd is structurally wrong — bar-odd data enters only
   through the channel loci (the weak/$\mathfrak{Q}_\beta$ sector), matching
   the corpus's routing of the pn sign to the weak sector (PR #3448 line).
   This is a formalize-first pruning invariant in the sense of the
   compute-author discipline: apply it to the GAP-A-3/A-4 candidate lists
   before running anything.
2. **Level selection (GAP-A-3) lead.** Toroidal quantization — integer
   winding pair $(\mu, \nu)$ on the shared torus plus the *forced*
   half-integer degree — is a derived candidate for the brane-tower level
   selection rule: allowed tower levels = allowed windings. If a Hopf/²H
   structural test survives, this replaces a fitted level choice with a
   derived one. (Next formalizable step; no fit involved.)
3. **A derived zero-point offset.** The forced $-\tfrac12$ degree shift is
   the ladder's zero-point. Constant $\tfrac12$-type offsets currently
   floating in binding-tower bookkeeping are candidates for *derivation*
   from this shift — checkable against existing witnesses with no new
   parameters.
4. **A parameter-free small parameter for binding corrections.** The
   soliton criterion (§5) gives $b/[2]_q = \sqrt{[d-1][d+1]}/([d]\,[2]_q)$
   as a derived expansion parameter for channel-mixing corrections — a
   structured organizing principle for the higher-order terms in exactly
   the sector where the Q_β/m_n/Δ_pn trio share their root cause. Any
   numerical exploitation must go through the Δ_λ gate (formalize-first,
   no seventh ansatz): the path is P1-style forcing lemmas, not fits.

## 10. Tranche 3 (owner picked §9 paths 1 + 2 + conjecture formalization)

**T1 — bar-parity prune of the recorded Δ_λ ansätze (6/6, audit-only).**
[`bar_parity_delta_lambda_prune_probe.py`](../../computations/substrate/bar_parity_delta_lambda_prune_probe.py).
Grounding facts, all exact: $\mathrm{dim}_q$ is bar-even (hook brackets);
Hecke characters obey the **twisted** parity
$\chi_\lambda(w; q^{-1}) = (-1)^{\ell(w)} \chi_{\lambda'}(w; q)$ (verified
via explicit Hoefsmit representations, every irrep of $H_2$ and $H_3$,
words to length 3 — the probe also pinned the Hoefsmit diagonal-order
convention by the braid relation); content sums are conjugation-odd.
Classification of the recorded families
(per [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md)):
content-linear kernels (PR #619 `c_content_monotonic`) are **bar-odd →
pruned**; $\lambda \leftrightarrow \lambda'$-asymmetric Frobenius-cost
kernels (the LP singleton picks) are **pruned unless routed to the weak
sector**; $\mathrm{dim}_q$-built kernels (co-Casimir, Plancherel) **pass
parity** — their recorded numerical failures stand unchanged; PROBE-4's KL
prune is parity-consistent (the chirality sign is the bar-odd datum). No
ansatz re-litigated, none proposed.

**T2 — toroidal level selection on the Hopf tower (6/6; GAP-A-3 candidate).**
[`toroidal_level_selection_hopf_probe.py`](../../computations/substrate/toroidal_level_selection_hopf_probe.py).
The $(2, 2k)$ torus-link (Hopf-power) two-channel trace tower
$x_k = W_+ q^{2k} + W_- q^{-2k}$ **is exactly** the forced toroidal family:
it satisfies the $2\cosh\eta$ degree recurrence at $\eta = 2\ln q$, and

$$
x_k = \sqrt{\tfrac{\pi \sinh\eta}{2}}
\Bigl[ (W_+ + W_-)\, P^{1/2}_{k-1/2}(\cosh\eta)
+ (W_+ - W_-)\, k\, P^{-1/2}_{k-1/2}(\cosh\eta) \Bigr],
$$

with $k$-independent coefficients (solved at $k = 1,2$, verified to
$\sim 10^{-42}$ at $k = 3..5$): the bar-even channel rides $P^{+1/2}$
($\cosh$), the bar-odd channel rides $P^{-1/2}$ ($\sinh$), at exactly the
forced order $\mu = \tfrac12$ and half-integer degree $k - \tfrac12$.
**Level-selection reading:** allowed levels = integer windings $k$;
Hopf/²H = the $k = 1$ ground level; zero-point = the forced $-\tfrac12$.
Structural only — selects levels, produces no binding number.

**T3 — conjecture formalized (§3b primary class, `lean`-direct exit 0).**
[`conj:whipple-rotation-intertwining`](../../content/quantum-observable-universe/mass-endomorphism/whipple-rotation-intertwining.md)
(registered in `sec:complex-volume`): the channel rotation acts on
winding-graded ladder data as the Whipple degree–order exchange
(grading swap + involutivity as content-bearing class fields; primary — no
instance, no conjectural hypothesis; a provable `grading_square` sanity
theorem keeps the fields non-vacuous).

## 11. Tranche 4 (three strands + rule institutionalized)

**T2b — three strands add one rigid color winding (8/8).**
[`toroidal_level_selection_three_strand_probe.py`](../../computations/substrate/toroidal_level_selection_three_strand_probe.py).
On the $(2,1)$ Hoefsmit block, $\rho(\sigma_1\sigma_2)$ has trace $-1$,
det $1$, and $(\sigma_1\sigma_2)^3 = \mathrm{Id}$ **exactly and
$q$-independently** — its eigenvalues are the primitive cube roots of
unity. So the $(3,k)$ torus-link tower (three strands = the
Borromean/nucleon carrier arity) is

$$
x_k = W_+\, q^{2k} + W_-\, q^{-2k} + W_0 \cdot 2\cos\!\bigl(\tfrac{2\pi k}{3}\bigr),
$$

annihilated by the factored order-4 operator
$(E^2 + E + 1)(E^2 - (q^2 + q^{-2})E + 1)$: the T2 hyperbolic winding pair
(carrying the substrate modulus, $\eta = 2\ln q$) **plus one compact
$\zeta_3$ winding of period 3 that does not flow with $q$** — a
topological color/triality phase. The compact channel rides the *same*
forced $\mu = \tfrac12$ elementary family on the compact locus
($P^{\pm 1/2}_{\nu-1/2}(\cos\theta) \propto \cos/\sin(\nu\theta)/\sqrt{\sin\theta}$,
verified with constants at 50 dps) — one family, the two locus rows of the
§2 channel-rotation table. **Level-selection reading:** the three-strand
level lattice is the winding pair $(k,\, k \bmod 3)$ — hyperbolic
(modulus-carrying) $\times$ compact color (rigid). Structural only.

**Rule institutionalized.** The T1 bar-parity selection rule now lives in
the gating doc every future ansatz must read:
[`2026-05-18-delta-lambda-gating-context.md` §Bar-parity selection rule](2026-05-18-delta-lambda-gating-context.md)
— candidates must pass the parity screen *before* any numerical run, and
the Recommendation section points at it.

## 12. Tranche 5 (owner picked: promote + Borromean test + prepare-merge)

**T5 — winding rigidity promoted to a content block.**
[`prop:three-strand-color-winding-rigidity`](../../content/quantum-observable-universe/braids-and-knots/three-strand-color-winding-rigidity.md)
(+ proof block, `braids-and-knots`): $\mathrm{tr}\,M = -1$, $\det M = 1$,
$M^3 = \mathrm{Id}$ for the uniform three-strand rotation on the $(2,1)$
block, every $q^4 \neq 1$. Lean `threeStrand_cubes_to_one` sorry-free
(`lean`-direct exit 0) over a generic field via Cayley–Hamilton
(`M2.cube_of_trace_det`), with $\beta$ carried as a constrained variable
(no $\sqrt{\ }$, §7c clean; self-contained `M2` carrier, no Mathlib
matrix API).

**T6 — the Borromean question answered (10/10).**
[`alternating_tower_borromean_winding_probe.py`](../../computations/substrate/alternating_tower_borromean_winding_probe.py).
The alternating word $A = \sigma_1\sigma_2^{-1}$ (whose power closures are
the hyperbolic anchors: figure-eight $4_1$ at $k=2$, Borromean $\mathcal{B}_3$
at $k=3$) has, on the same block,

$$
\mathrm{tr}\,\rho_{(2,1)}(A) = 1 - q^2 - q^{-2}, \qquad \det = 1,
$$

bar-even, $q$-dependent, equal to the rigid value $-1$ at $q = 1$. Its
tower obeys the same $\mu = \tfrac12$ Chebyshev flow, **elliptic** for
$q^2 + q^{-2} < 3$ with the exact parabolic boundary at
$q = \varphi = (1+\sqrt5)/2$ ($\varphi^2 = \varphi + 1$; an exact
spectral-transition point of the trace polynomial — **not** a fitted
anchor, cf. the #3444 numerology cut). So the block carries two winding
directions: the **rigid** $\zeta_3$ color rotation (uniform word, T5) and
its **modulus-deformed** version (alternating word,
$\theta'(q) = \arccos(\tfrac{1 - q^2 - q^{-2}}{2})$, $\theta'(1) = 2\pi/3$).
**Answer to "does the nucleon sit at a lattice point": yes** — $4_1$
(lepton) and $\mathcal{B}_3$ (nucleon) are the $k = 2, 3$ windings of the
deformed rotation, the same $k$ as their torus-link shadows on the rigid
direction.

## 13. Full-derivation program, tranche 1 (owner directive: "keep exploring until we can fully derive")

Target: the ²H law $B = 5g\,E_{\text{unit}}$ (owner ruled near-match label,
PR #3451). The §2f constraint ledger requires either a genuinely new derived
energy or the conclusion that the linear law is not fundamental.

**D1 — the fusion frame (7/7 exact,
[`deuteron_tower_fusion_frame_probe.py`](../../computations/substrate/deuteron_tower_fusion_frame_probe.py)).**
The dimensionless content of the $5g$ law is canonical-tower data:

1. **The bond factor is the corpus Markov parameter.** `pyhecke.gram` sets
   $z = 1/(\sqrt{q_0} + 1/\sqrt{q_0}) = 1/[2]_v$ — the reeb-flow bond
   factor is *the* Ocneanu–Markov trace parameter of $\mathrm{tr}_M$
   (checked live against the package value).
2. **The 5 is forced by the fusion rule.** $[2]_v^2 = [3]_v + 1$
   (spin $\tfrac12 \otimes \tfrac12 = 1 \oplus 0$ in quantum dimensions), so
   $1 + [2]_v^2 = 2 + [3]_v \to 5$ at $v = 1$: the integer in $5g$ is the
   classical total quantum dimension of the two-nucleon channel
   decomposition, not a free constant.
3. **Winding bridge.** $1 + [2]_v^2 = 4 - \tau(v)$ exactly, with $\tau$ the
   §12 alternating winding trace — so $g = 1/\sqrt{4 - \tau(v)}$: the
   deuteron bond magnitude, the muon anchor ($4_1$, $k{=}2$) and the
   nucleon carrier ($\mathcal{B}_3$, $k{=}3$) are levels of one tower
   ($k{=}1$ is the unknot → the bond).
4. **Criticality = normalized channel projection**:
   $g^2(1 + [2]_v^2) = 1$ identically — the marginal-stability zero and
   the landed magnitude are the same statement.

**Sharpened open (honest):** the classical 5 admits at least two canonical
deformations ($5/\sqrt{2+[3]_v}$ vs $\sqrt{2+[3]_v}$), both ~0.4–0.6 %
near-matches with a ~1 MeV unit; the frame does not select one, and
$E_{\text{unit}}$ stays open.

**D2 — zero-point unit family pruned (4/4 negative,
[`zeropoint_unit_candidate_gate_probe.py`](../../computations/substrate/zeropoint_unit_candidate_gate_probe.py),
witness
[`zeropoint-unit-candidate-gate-probe.witness.json`](../../computations/substrate/zeropoint-unit-candidate-gate-probe.witness.json)).**
Predicted-first: if the unit were the Fock zero-point of the forced
$-\tfrac12$ (half a winding quantum × canonical anchor), the four licensed
candidates (hyperbolic/compact × $m_e$/$E_{\text{cross}}$) miss by
23–99 %. The zero-point family is excluded *as the unit* under these
anchors; the zero-point reading of the $-\tfrac12$ itself is untouched.

**D3 — next formalize-first target (note).** The reeb-flow chain's one
residual postulate (*linking amplitude = CWF unit-tangent functional on the
channel direction $(1, z)$*) reads, in the toroidal frame, as: the channel
direction is the winding slope $\tan\theta = z$ of a geodesic pair on the
shared torus, and the CWF functional is the normalized winding tangent. The
concrete discharge candidate: **prove that the Gauss linking integral of a
$(1, z)$-slope curve pair on the Clifford torus equals the normalized
exchange component $\sin\theta = g$** — classical differential geometry,
plausibly provable, and it would reduce the ²H derivation chain to the
deformation choice + unit. Queued as the program's next step;
`conj:whipple-rotation-intertwining` is the bar-involution face of the same
identification.

## 14. Corpus-grep record

- `parabolic cylinder|Weber equation|Hermite`: hits are the Askey/channel
  cluster cited above + bibliography; no prior parabolic-cylinder treatment.
- `bar-even|bar-odd`: the channel-rotation cluster (§2), `LeptonMesonParitySplit`.
- `toroidal`: 3 tangential hits; no prior treatment.
- `Ocneanu`: mass-theory Markov-trace proofs; no continuous-parameter
  interpolation treatment found.

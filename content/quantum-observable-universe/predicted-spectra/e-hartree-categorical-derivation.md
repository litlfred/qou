> **SUPERSEDED-$\rho_q$ note.** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](../braids-and-knots/mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](../braids-and-knots/rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

The molecular-binding framework uses the Hartree energy
$E_h = m_e c_q^{2}\,\alpha_{EM}^{2}$ as a conversion scale (for example in
[`hecke_core.py:198`](folio-assistant/computations/substrate/hecke_core.py)).
This block asks whether the $\alpha_{EM}^{2}$ factor arises from QOU/Hecke
structure rather than as an empirical input. The answer reached is a
**clean conditional theorem**, not a closed one.

**Conjecture (corrected headline form).** *For a covalent diatomic with
definite-parity ground state, the bound-state contribution on the EM
Wedderburn channel $(2,2)$ of the molecular Markov trace carries the
fine-structure scale exactly:*

$$
  \rho_{(2,2)}
  \;=\;
  \frac{\chi_{(2,2)}^{\mathrm{dressed}}}{\bigl(q\,[9]_q\,[10]_q\bigr)^{2}}
  \;=\;
  C(q)\,\alpha_{EM}^{2},
  \qquad
  C(q) \;=\; h\,\bigl(\dim_q V_{(2,2)}\bigr)^{2},
$$

*with $\alpha_{EM} = 1/(q\,[9]_q\,[10]_q) \in R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$
and $C(q)$ a fixed categorical coefficient (the EM-block
Plancherel-square — not a free parameter), so that
$E_h = m_e c_q^{2}\,\alpha_{EM}^{2}$ is the archimedean evaluation of
$\rho_{(2,2)}$ up to the CAL-1 energy unit $m_e c^{2}$.*

> **Historical framing.** The investigation opened from a weaker
> $J^{1}$-vanishing claim about the Markov-layer LP dual
> $y_{\mathrm{cov}} = c_2\,\alpha^{2} + O(\alpha^{4})$. That form is
> refuted: the separated-atom point is a kink, so $y_{\mathrm{cov}}$ is
> $O(\alpha)$, not $O(\alpha^{2})$ — the $\alpha^{2}$ scaling is real but
> lives in the q-dimension layer, not the Markov layer. The trace-ratio
> above is the live statement; the $y_{\mathrm{cov}}$ form is retained
> only in the investigation log.

## Standing — a conditional theorem

Every *mechanism* question is resolved: the coupling-parity routes are
refuted (below), the $\alpha_{EM}^{2}$ scaling is exact in $R$, the
archimedean functor is the known $q_0$-evaluation / Bloch–Suslin pairing,
and the $(2,2) = \mathrm{EM}$ channel is grounded in the covalent-pair
structure. The statement is **not closed**, and — by the framework's
three-calibration design — **cannot be unconditional**: the energy unit
$m_e c^{2}$ is **CAL-1** (deriving it is the owner-declined Subgoal-2). The
residual is exactly **three named items**, none a hidden gap:

1. **The $(2,2) = \mathrm{EM}$ identification** — grounded ($(2,2)$ is the
   unique self-transpose summand of
   $\mathrm{Ind}_{S_2\times S_2}^{S_4}(\mathrm{sgn}\boxtimes\mathrm{sgn})$),
   *not eliminated*; it still rests on the physical input "covalent bond
   $=$ two EM singlets."
2. **The $m_e c^{2}$ CAL-1 unit** — not provable by design (Subgoal-2,
   owner-declined).
3. **The $\alpha^{2}$ magnitude algebra** — that the squared
   force-carrier complexity normaliser sets the *physical* energy. The
   $\alpha^{2}$ *scaling* is exact; what stays conditional is the
   magnitude, resting on the covalent Pauli-2 reuse of the bare EM
   complexity (the honest successor to the refuted quadratic-form
   Mechanism B below).

## What is rigorous

1. **The bare LP/SDP framework.** The $H_2$ molecular braid and its
   primal/dual program are set up rigorously in
   [LP dual binding](#prop:h2-lp-dual-binding) and
   [ILP covalent bond](#prop:ilp-covalent-bond), with strong duality
   ([operator-selection LP](#prop:operator-selection-lp)) giving
   $y_{\mathrm{cov}}^{*}$ as the binding energy per shared electron.

2. **The bare formula.** The leading expression
   $1/\alpha_{EM} = q\,[9]_q\,[10]_q$ is rigorously derived from the
   singlet-idempotent / Bring force-carrier complexity
   ([EM coupling projection](#prop:em-coupling-projection)) and lies in
   $R$. It admits the equivalent shift-exponent form
   $1/\alpha_{EM} = q \cdot [\alpha_{\mathrm{shift}}(T_{2,9})]_q \cdot
   [\alpha_{\mathrm{shift}}(T_{3,5})]_q$
   ([multiplicative-chain form](#prop:alpha-em-shift-multiplicative-chain)),
   exposing the same combinatorial primitive — pole order at $q = 0$ of a
   seminormal Hecke trace — that controls the atomic-shift framework.

3. **The Frobenius / curvature-rank decomposition.** The Gröbner–Shirshov
   spectral sequence collapses at $E_1$
   ([spectral sequence collapse](#prop:spectral-sequence-collapse)) and the
   molecular operator decomposes by curvature rank
   ([curvature-rank GB stratification](#prop:curvature-rank-gb-stratification));
   the covalent bond — sharing two electrons through two crossings — sits
   at curvature rank $2$.

4. **Closed-form dressed characters.** All five irrep characters of the
   bare $H_2$ braid $\sigma_1\sigma_2\sigma_3 \in B_4$ are single
   $q$-monomials (See [Table 12](#tbl:e-hartree-categorical-derivation-table12-data)),
   with force-carrier sum
   $\chi_{(3,1)} + \chi_{(2,1,1)} = -q + q^{-1} = -h$. Replacing the middle
   crossing with the K-shell-dressed $T^{\mathrm{dr}}$ (eigenvalues
   $q^{5}, -q^{-5}$) activates the $(2,2)$ channel — breaking the bare
   $(2,2) = 0$ selection rule — and amplifies the force-carrier channel by
   $\approx [5]_q$
   (See [Table 13](#tbl:e-hartree-categorical-derivation-table13-data)),
   the algebraic signature of the dressing power.

## Three candidate mechanisms (all with gaps)

### Mechanism A — Pauli / two-electron combinatorial counting

A covalent bond shares **exactly two** electrons (Pauli exclusion +
singlet pairing). In the Hecke braid representation each shared electron
contributes one crossing operator, so the covalent operator
$L_{\mathrm{cov}}$ is bilinear in Hecke generators,
$L_{\mathrm{cov}} = \sigma_{i}\,\sigma_{j} + (\text{symmetrisation})$. If
each Hecke crossing entering the operator-selection LP carries weight
$\alpha_{EM}$, then $L_{\mathrm{cov}} \sim \alpha_{EM}^{2}$ and the Markov
trace inherits the $\alpha_{EM}^{2}$ leading order.

**Gap.** Showing that *each* "EM-mediating" crossing carries exactly one
factor of $\alpha_{EM}$ in the LP-dual expansion. The bare formula
$1/\alpha_{EM} = q\,[9]_q\,[10]_q$ is the operator-selection weight of a
single force-carrier knot, not a per-crossing factor; translating between
"per-knot weight" and "per-crossing factor" needs a
multiplicative-decomposition lemma that is not established.

### Mechanism B — quadratic-form structure of the Frobenius LP

The molecular SDP is a quadratic program over the Frobenius Gram matrix
([`prop:operator-selection-lp § dual program`](#prop:operator-selection-lp)).
For a quadratic primal parametrised by a single perturbation $\varepsilon$
turning on the covalent constraint, the Legendre/Schur-complement dual is
$y_{\mathrm{cov}}(\varepsilon) = \tfrac{1}{2}\varepsilon^{2}\,(G^{-1})_{\mathrm{cov,cov}} + O(\varepsilon^{4})$;
if $\varepsilon \propto \alpha_{EM}$ this gives
$y_{\mathrm{cov}} \propto \alpha_{EM}^{2}$ with no linear term.

**Gap.** The argument needs the bare separated-atom configuration to be a
smooth interior point with the covalent constraint active at
$\varepsilon = 0$ as an equality. In practice the activation is a *kink*,
$y_{\mathrm{cov}}$ jumps non-smoothly, and the linear coefficient is
generically non-zero. A rigorous version requires the bare atoms to
already saturate the Frobenius-pairing equality (live on the active
facet) — not verified, and the source of the round-21 refutation of the
$y_{\mathrm{cov}}$ form.

### Mechanism C — parity / antipode invariance of the Markov trace

The antipode $S$ of the Iwahori–Hecke algebra acts by
$S(\sigma_i) = \sigma_i^{-1}$, and the Markov trace is $S$-invariant. For a
definite-parity ground state the molecular braid is $S$-equivariant up to
Markov equivalence, which would force a parity selection rule eliminating
odd powers of $\alpha_{EM}$.

**Gap.** The antipode acts on the substrate parameter as
$S(\alpha_{EM}) = \alpha_{EM}\bigl|_{q \mapsto q^{-1}} = q^{2}\,\alpha_{EM}$
— a multiplicative scaling, **not** a sign flip — since $[n]_q$ is
palindromic but the $q^{-1}$ prefactor is not. $S$-invariance then only
imposes the functional equation $f(\alpha_{EM}) = f(q^{2}\alpha_{EM})$,
which does not force odd powers to vanish. Recovering a coupling-parity
rule would need a *different* involution flipping the sign of
$\alpha_{EM}$ — and none exists (next section).

### Mechanism D — virial / scaling (the route that survives)

The $\alpha^{2}$ scaling of $E_{\mathrm{Hartree}}$ does not come from
linear-Stark vanishing; it is dimensional analysis at the Bohr radius
$a_0 \sim 1/(m_e c \alpha)$, where both kinetic
$T \sim \hbar^{2}/(m_e a_0^{2})$ and Coulomb
$V \sim e^{2}/a_0$ scale as $m_e c^{2}\alpha^{2}$ and the virial theorem
balances them. The QOU analogue is therefore a **virial/scaling**
argument, not a parity argument: at the bound-state LP/SDP optimum the
molecular Markov trace decomposes into two contributions both scaling as
$\lambda_{\mathrm{bound}}^{-2}$, where $\lambda_{\mathrm{bound}}$ is the
characteristic eigenvalue of the molecular transfer matrix
($T_1 = T_{e_2 \mathfrak{p}_2}^{\mathrm{dressed}}$ in
[`prop:h2-lp-dual-binding`](#prop:h2-lp-dual-binding), eigenvalues
$q^{5}, -q^{-5}$) and $\lambda_{\mathrm{bound}}^{-1}$ is the categorical
analogue of $\alpha_{EM}$. The leading order is $\alpha_{EM}^{2}$ by
dimensional matching, with no linear term to suppress. Under this reading
$J^{1}$-vanishing is not a theorem to prove but a consequence of the LP/SDP
being quadratic in the bound-state scale; the conjecture sharpens to the
claim that $\lambda_{\mathrm{bound}}^{-1} \in R$ and
$\lambda_{\mathrm{bound}}^{-1}(q_0) = \alpha_{EM}(q_0)\,c_1$ for some
$c_1 \in R$ of order unity — a direct symbolic computation
(See [Table 11](#tbl:e-hartree-categorical-derivation-table11-data)). The
$H_2$ witness
([`h2-molecular-binding.witness.json`](folio-assistant/computations/h2-molecular-binding.witness.json))
gives the dimensionless ratio $E_{\mathrm{bind}}/E_{\mathrm{Hartree}} \approx 0.170$,
of order unity (matching the standard-physics $H_2$ ratio $\approx 1/6$),
consistent with Mechanism D without any $J^{1}$-vanishing miracle.

## No coupling-level involution flips $\alpha_{EM}$

A natural follow-up to Mechanism C asks whether some involution $\iota$ of
$R$ other than $q \leftrightarrow q^{-1}$ flips the sign of $\alpha_{EM}$.
Direct calculation rules out all four automorphisms generated by
$q \mapsto \pm q^{\pm 1}$
(See [Table 10](#tbl:e-hartree-categorical-derivation-table10-data)): using
$[n]_{-q^{\pm 1}} = (-1)^{n+1}[n]_q$, the sign factors from $q$ and
$[10]_q$ cancel, and none of the four maps $\alpha_{EM}$ to
$-\alpha_{EM}$. This is a structural obstruction — $\alpha_{EM}$ is a
positive scalar on the relevant component of the substrate variety, and no
positivity-preserving automorphism of $R$ flips its sign — so a
coupling-parity selection rule of the form
"$f(\alpha_{EM}) = f(-\alpha_{EM}) \Rightarrow$ odd terms vanish" cannot be
implemented by any Galois-style involution.

The viable analogue is **operator-parity, not coupling-parity**: the
standard linear-Stark vanishing $\langle\psi_0|\hat r|\psi_0\rangle = 0$
has the parity-odd object be the *operator* (the dipole), not the coupling.
The categorical version seeks a $\sigma$-antisymmetric Hecke perturbation
$\Delta_{\mathrm{cov}}$ (built from $\sigma_i - \sigma_i^{-1}$ skein
factors) with
$\Phi_1(\mathcal{M}_{\mathrm{atom}} \cdot \Delta_{\mathrm{cov}}) = 0$ by a
categorical parity rule, leaving an $\alpha_{EM}^{2}$-scaled second-order
contribution — aligning with how
[antiparticle crossing reversal](#prop:antiparticle-crossing-reversal)
realises $\sigma$ at the operator level.

## Companion remark — physical translation

In standard non-relativistic QED, $E_h \propto \alpha_{EM}^{2}$ because
both kinetic energy and Coulomb potential are quadratic in
$1/a_0 \propto \alpha_{EM}$ and the virial theorem balances them at
$E = -\tfrac{1}{2}V \propto \alpha_{EM}^{2}$; the $\alpha_{EM}^{1}$
contribution is the linear Stark shift, which vanishes in any
definite-parity state by symmetry of the electric-dipole matrix element. A
categorical proof would amount to identifying the categorical analogue of
that linear-Stark vanishing — see
[antiparticle crossing reversal](#prop:antiparticle-crossing-reversal) for
the QOU analogue of charge-conjugation parity.

## What is still missing for closure

A genuinely categorical derivation of the $\alpha_{EM}^{2}$ scaling
requires three concrete, tractable items, all beyond the present block's
scope:

1. **A Hecke-algebraic definition of $\Phi_1^{\mathrm{kin}}$ and
   $\Phi_1^{\mathrm{Coul}}$** as distinct, computable components of the
   molecular Markov trace — the current LP/SDP framework does not separate
   them.
2. **A proof that these contributions balance at a specific categorical
   length, derived from Hecke structure** — not from transported
   dimensional analysis — likely via a symbolic $q$-polynomial recompute of
   the optimal $\Phi_1^{H_2}(\pi^{*})$ tracking each crossing-type
   separately.
3. **An independent derivation of the archimedean energy unit per
   $\Phi_1$** from algebraic structure, not from "matches QED in
   $q \to 1$ limit" — the deepest layer, requiring a functorial uniqueness
   statement about $\rho_\infty$ verifiable without experimental Hartree
   values.

## What this block does not claim

- It does **not** claim a proof of $E_h \propto \alpha_{EM}^{2}$ from QOU
  principles; it claims only that this scaling is the expected leading
  behaviour and identifies the open structural step.
- It does **not** introduce $\pi$, transcendentals, or PSLQ-fitted
  constants — the coefficient $c_2$ is conjecturally in
  $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$.
- It does **not** override the existing usage of
  $E_{\mathrm{Hartree}} = m_e c^{2}\,\alpha_{EM}^{2}$ in
  [`hecke_core.py:198`](folio-assistant/computations/substrate/hecke_core.py)
  as a numerical input — that usage remains an empirical scale pending
  closure of this conjecture.

## Honest reporting

Three derivation mechanisms are recorded above, each with an explicit
identified gap; the operator-parity sharpening of Mechanism C and the
virial-scaling Mechanism D are the two surviving lines of attack. Reporting
the partial chain — rather than papering over it with post-hoc numerical
identifications — is the deliberate purpose of this block.

## Supporting data tables

The data tables that follow (Tables 1–13) collect the intermediate
symbolic computations of the investigation. Tables 10–13 support the
rigorous results and mechanisms above; Tables 1–9 record per-round
intermediate data whose narrative context is preserved in the
investigation log.

---

**Investigation record.** The full round-by-round derivation log — every
candidate mechanism, how it was ruled out or sharpened — is preserved in
[the e-Hartree investigation log](../../../docs/audits/2026-06-13-e-hartree-investigation-log.md).
That document is the historical record; this block carries the distilled
conditional theorem, the rigorous results, and the open closure programme.

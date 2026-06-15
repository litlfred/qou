A handful of common letters carry overloaded meanings in the
literature. The following conventions are enforced throughout this
paper to keep them disambiguated:

- **$c$** = color (never charm; charm is $\mathfrak{c}$).
- **$b$** = generic variable (never bottom quark; bottom is $\mathfrak{b}$).
- **$p$** = brane point (never proton number; proton number is $Z$).
- **$E$** alone = not used for an exceptional divisor, energy, or
  elliptic curve. Use $\mathcal{S}_p$, $\mathfrak{E}$, or $\mathcal{E}_q$
  respectively. $E_{\mathfrak{H}}$ (with hadron subscript) is allowed
  for crossing energy.
- **$\mathfrak{E}_0$ vs $Q_\beta(n)$** — two distinct hadronic-sector
  scalars that have been historically conflated in Python compute
  scripts (see [`folio-assistant/computations/binding_canonical.py`](../../../folio-assistant/computations/binding_canonical.py)
  history). They are **not interchangeable**:
    - $\mathfrak{E}_0$ = **hadronic energy scale**, framework-derived as
      $\mathfrak{E}_0^{(N=0)} = m_e/(q_0(q_0-1)) \approx 4.186$ MeV (CAL-1
      and CAL-2 only); the tower-summed form is
      $\mathfrak{E}_0^{\text{full}} = \mathfrak{E}_0^{(N=0)}/(1-\hbar_q^2)
      \approx 4.228$ MeV. Sets the MeV-per-dimensionless-trace-unit
      conversion for hadronic predictions.
    - $Q_\beta(n) = 0.78233341\,\text{MeV}$ — the **free-neutron
      $\beta$-decay Q-value**, derived from CAL-2 ($\mathfrak{D}_\beta$). Used as
      the binding-energy-scale multiplier in
      [`prop:categorical-mass-markov`](../braids-and-knots/categorical-mass-markov.md)'s
      explicit binding formula $B = Q_\beta(n) \cdot (|\mathrm{tr}_M(W_{\text{free}})| - |\mathrm{tr}_M(W_{\text{atom}})|)$.
  $\mathfrak{E}_0/Q_\beta(n) = 1/|\Delta(\mathrm{net})| \approx 5.31$
  (the dimensionless Hecke NF reduction). Code must name the
  parameter for the actual quantity it carries; using `E_0` for a
  $Q_\beta$-valued binding-scale variable is a registered audit flag.
- **$\gamma$** = three reserved meanings, all standard, disambiguated
  by context: (i) the **photon** (default reading in particle / QED
  contexts: pair production $\gamma\gamma \to e^+ e^-$, photonic
  channels, Breit–Wheeler vertices); (ii) the **Euler–Mascheroni
  constant** (only inside zeta-value identities, e.g.
  $\zeta'(0) = -\tfrac{1}{2}\log(2\pi)$, $\gamma = \lim(H_n - \log n)$);
  (iii) **Dirac matrices** $\gamma^\mu$ (always with an explicit
  Lorentz index). Never use $\gamma$ for a vortex or closed cycle —
  the vortex morphism is $\varrho$.
- **$\chi_q$** = Lyapunov exponent (distinct from $\chi_\zeta(c)$,
  the character).
- **$\zeta$** = three distinct uses, never bare. $\zeta_n := e^{2\pi i/n}$
  (primitive $n$-th root of unity, **always with integer subscript** —
  e.g. $\zeta_5$, $\zeta_6 = e^{i\pi/3}$); $\zeta(s)$ (Riemann
  zeta function, **always parenthesised**, e.g. $\zeta(2) = \pi^2/6$,
  $\zeta(3)$ — Apéry's constant); $\chi_\zeta(c)$ (character, **always
  with $\chi$ prefix and argument**). The bare token $\zeta$ alone is
  **not used**.
- **$\mathcal{P}_n$** = Goncharov period filtration class (weight-$n$
  periods modulo lower-weight). Distinct from $P_\ell$ = elementary
  symmetric polynomials in Jucys–Murphy elements
  ([`prop:jucys-murphy-central-elements-qou`](#prop:jucys-murphy-central-elements-qou)),
  which are non-calligraphic and indexed by symmetric-polynomial
  degree.
- **$H_q$** alone = not used. Three distinct concepts share the
  letter $H$: $\mathcal{H}_q$ (shuffle Hopf algebra), $\hat{H}_q$
  (Hamiltonian operator), $H_n(q)$ or $H_q(\lambda)$ (Hecke /
  hook-length, always with argument).
- **$\mathfrak{S}$** = categorical action (fraktur, Hamilton's $S$).
  Never the **state bundle**, which keeps calligraphic $\mathcal{S}$
  (QOU tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$). The action was
  historically written $\mathcal{S}_q$ and plain $S_q$. The plain-$S_q$
  form is now $\mathfrak{S}_q$ throughout the physics/computation
  chapters. Three other objects deliberately keep plain or calligraphic
  $S$ and are **not** the action:
    - the Hopf **antipode** $S$ (plain $S$, or $S_q$ on the $q$-shuffle
      Hopf algebra);
    - the q-**entropy** $S_q(U)$ (`quantum-temperature`, with
      $\partial S_q/\partial \mathfrak{E}_q = 1/T_q$) and the
      Bekenstein–Hawking entropy $S_{BH}$ — entropy is a distinct
      thermodynamic observable, never the action;
    - the **Skein module** $\mathcal{S}_q(\mathbf{C})$, which keeps
      calligraphic $\mathcal{S}$ (a module of knot classes, not a scalar
      functional).
  Note: the *calligraphic* action $\mathcal{S}_q = \mathrm{tr}(\mathcal{L}_q)$
  still appears in several chapters; migrating it to $\mathfrak{S}_q$ is a
  follow-up that must dodge the Skein module $\mathcal{S}_q$ above (which
  legitimately retains calligraphic $\mathcal{S}$ and still brushes the
  state bundle — a residual collision the action rename does not fix).
- **$\mathfrak{O}$** = observation / intent morphism — the section
  $(\mathfrak{O}, \epsilon)$ of $\mathrm{Ad}(J^1\mathcal{S})$ and its
  germ endomorphism $\mathfrak{O}_p$. Never an **ideal**: the
  genus-filtration ideal keeps $\mathfrak{I}$
  ($\mathfrak{I}_4 = (u^5)$). Intent moved off $\mathfrak{I}$ to
  disambiguate the two.
- **$\mathfrak{W}$** = confinement observable / $q$-Wilson loop
  $\mathfrak{W}(\mathcal{K}, \mathcal{T})$. Never the observation
  morphism (now $\mathfrak{O}$); the abstract Wilson-loop functional is
  plain $W(\gamma)$.
- **$S_n$ vs $H_n(q)$** — $q$-deformed braiding decompositions
  (eigenvalues $\{q, -q^{-1}\}$) are actions of the Iwahori–Hecke
  algebra $H_n(q)$, **not** the symmetric group $S_n$, even when the
  block dimensions match the classical $S_n$ irreps (§7a–7b). Write
  classical $S_n$ only for a genuine $\epsilon = \pm 1$ flip; never
  fraktur $\mathfrak{S}_n$ (fraktur $\mathfrak{S}$ is the action).
- **Three partition-weight families** — Markov $y_\lambda$,
  Plancherel $w_\lambda$, q-deformed Wedderburn $\tilde w_\lambda$ —
  are distinct at $q \neq 1$ and must not be conflated. They
  coincide at $q = 1$. Specifically:
    - $y_\lambda$ = Jones–Markov central coefficient ($\mathrm{tr}_M
      = \sum y_\lambda \chi_\lambda$, Wenzl hook–content closed
      form);
    - $w_\lambda = (\dim V_\lambda)^2 / n!$ = classical Plancherel
      probability measure, $\sum w_\lambda = 1$ exactly;
    - $\tilde w_\lambda = \dim_q^2(\lambda) / [n]_q!$ = q-deformed
      Wedderburn-block weight, $\sum \tilde w_\lambda$ finite but
      $\neq 1$ at $q \neq 1$ (empirically $\approx 1.51$ at $q_0$,
      $n = 12$).
  Use $w_\lambda$ unsubscripted **only** for the classical
  Plancherel measure; mark the q-deformed analogue with the tilde
  ($\tilde w_\lambda$). The Wenzl-bridge identity
  $y_\lambda = w_\lambda$ holds on the **self-conjugate stratum
  only** (where $\kappa_\lambda = \sum_{x} c(x) = 0$).

  **Plus a fourth scalar that does NOT belong to the weight family**
  but is easy to misread as one because of the symbol $\mu_\lambda$:

    - $\mu_\lambda(q)$ = $q$-Laplacian eigenvalue on $V_\lambda$ from
      [`prop:q-heat-kernel-peter-weyl`](../information-theory/q-heat-kernel-peter-weyl.md)
      — the **heat-flow decay rate** $\hbar_q^2 \sum_{x \in \lambda}
      [c(x)]_q [c(x)+1]_q$, NOT a Markov-trace ingredient. It does
      not multiply $\chi^\lambda$, does not sum to anything
      normalised, and does not appear in the Frobenius expansion.
      Symbol-similarity to $w_\lambda$ / $\tilde w_\lambda$ makes
      conflation tempting; avoid.

  **Concrete $H_3$ values at $q = 1$** (Jones-normalised
  $V / [2]_q^{c-1}$ convention of
  [`prop:borromean-markov-trace-closed-form`](../mass-theory/borromean-markov-trace-closed-form.md)
  and [`prop:h3-markov-wenzl-weights`](../mass-theory/h3-markov-wenzl-weights.md)):

  | $\lambda$ | $d_\lambda$ | $y_\lambda(1)$ | $w_\lambda(1)$ | $\mu_\lambda(1)$ |
  |---|---|---|---|---|
  | $(3)$ | $1$ | $1/2$ | $1/6$ | $0$ |
  | $(2,1)$ | $2$ | $1/4$ | $2/3$ | $2 \hbar_q^2$ |
  | $(1^3)$ | $1$ | $0$ | $1/6$ | $0$ |
  | sum identity | — | $\sum y_\lambda d_\lambda = 1$ | $\sum w_\lambda = 1$ | (no sum) |

  Note the $y_\lambda$ vector $(1/2, 1/4, 0)$ is *not* uniform and
  $y_{(1^3)} = 0$ identically (Temperley–Lieb quotient — Jones
  factors through TL); the Wenzl-bridge $y_\lambda = w_\lambda$
  fails at $\lambda = (2,1)$ here ($1/4 \neq 2/3$) because the
  bridge identity uses a *different* (non-Jones, Schur-element)
  normalisation of $y_\lambda$ — they coincide on the
  self-conjugate stratum **after** matching normalisation
  conventions. When in doubt, cite the source proposition.
- **$\check{q}$** (q-háček, meaning "little hook" in Czech)
  = spinor information rate, $\check{q} = q^{1/2}$, $\check{q}^2 = q$.
  Eigenvalue of the elementary half-twist on the spin-½ fundamental
  rep of $\mathrm{SU}_q(2)$. Reserved exclusively for this purpose.
  The háček diacritic encodes the relation $\check{q}^2 = q$ in the
  glyph — every occurrence is self-documenting. The relation to $q$
  is exactly analogous to $i$ vs $-1$: $\check{q}$ opens up the 2-D
  spinor (spin-½) representation from the 1-D adjoint (spin-1)
  representation. **Renamed from $r$ on 2026-06-04** to free $r$
  for radius / generic-real contexts (the prior reservation forced
  authors to write $\rho$ for radius in physics chapters, an
  unnecessary cost; the háček also absorbs the historical Habiro
  $u = q^{1/2}$ — see $u$ entry below). **Never** use $r$ or $t$
  for $q^{1/2}$ ($t$ clashes with the $V_K(t)$ knot variable and
  with time-like usage); $\iota$ is also reserved (involution /
  inclusion).
- **$u$** = LP shadow-price $u_\lambda, u_0$ (Schrijver convention
  for operator-selection LP dual variables, see Table 3 row 15) **or**
  the $Q_\beta$ precision-ladder step variable
  $u_{\text{ladder}} = b\,\hbar_q^2$ with
  $Q_\beta = Q_{\text{base}} \prod_k (1 + c_k\,u_{\text{ladder}}^k)$,
  $b$ the Hoefsmit coupling and $\hbar_q = (q-1)/q$. At $q_0$,
  $u_{\text{ladder}} \approx 0.00852$.
  **Habiro $u = q^{1/2}$ retired 2026-06-04**: the Habiro-ring
  expansion is now written as
  $\mathrm{tr}_M = \sum_m a_m(\check{q})\,(\check{q};\check{q})_m /
  D(\check{q})$ with $\check{q}$ the spinor rate above
  (the two were always numerically identical; the dual name was a
  literature-debt that produced a $5\times10^{38}$ error in
  [`habiro_q_difference_fourier.py`](../../../folio-assistant/computations/habiro/habiro_q_difference_fourier.py)
  by silent substitution between Habiro $u$ and ladder $u$).
  **Discipline:** when a compute script uses BOTH the ladder step
  and either the LP shadow-price $u_\lambda$ or the (retired)
  Habiro $u$, the ladder variable **must** be spelled `u_ladder`
  to keep contexts unambiguous. Single-context scripts may keep
  bare `u` when an in-script comment annotates which meaning
  applies (`u = sqrt(q)` for Habiro-facing scripts is permitted
  when accompanied by `# = \check{q}, spinor rate` annotation).
  Mixing the meanings under a single bare `u` without comments is
  the audit-flag pattern that produced the 2026-06-01 incident.
- **$\ell$** = Wenzl principal-specialisation length (number of
  points in $s_\lambda(1, q^2, \ldots, q^{2(\ell-1)})$). **Renamed
  from $r_W$** in the May 2026 notation cleanup (when $r$ was
  the spinor rate); $r$ itself was subsequently renamed to
  $\check{q}$ on 2026-06-04. Old code/docs using $r_W$ should
  migrate to $\ell$.
- **Numerical $q = 1.1097$** (or any specific value of the substrate
  parameter) should not appear outside the introduction, Chapter 8
  (Information Theory, for falsifiability computations), and
  Chapter 11 (Observations). Geometry chapters should use symbolic
  $q$.

**Approximation convention (derived / observed values).** Numerical
values derived from the substrate parameter $q_0$ or compared to
experimental data use $\approx$ (or $\simeq$), never $=$, unless an
explicit error term is present. Exact algebraic identities (e.g.\
$c_q = 1/(q-1)$) use $=$ since they hold for all $q$.

**Hecke–Skein convention.** The Hecke algebra generator is
$\sigma_i$ (never $T$, never $t$ or $A$ for the Jones polynomial
variable). The Iwahori–Hecke algebra $H_n(q)$ is presented as a
quotient of the braid group algebra of $B_n$, so the same symbol
$\sigma_i$ denotes both the braid-group generator and its image in
$H_n(q)$ — context disambiguates. The Jones polynomial is always
$J_K(q)$, not $V_K(t)$. The letter $J$ is shared with the **Hahn–Exton
q-Bessel** function $J_\nu^{(3)}(x;q)$ (substrate harmonic analysis, the
$\mathrm{SU}_q(2)\to E_q(2)$ contraction; PR #2279) and the ordinary Bessel
weights $J_n(x)$ of the Jacobi–Anger expansion. These are disambiguated by
their subscript: a **knot/link $K$** for the Jones polynomial, an **order
$\nu$/$n$** (always with an argument $x$, and the $(3)$ superscript for
Hahn–Exton) for Bessel. Never bare $J$.

**Categories vs CPT operators.** Categories are typeset bold,
$\mathbf{C}$, $\mathbf{Rep}$, etc. The calligraphic $\mathcal{C}$
is **reserved for the charge-conjugation operator** in CPT
discussions (parity $\mathcal{P}$, time-reversal $\mathcal{T}$,
combined $\mathcal{CP}$, $\mathcal{CPT}$). Calligraphic $\mathcal{C}$
must never denote a category in this paper; readers should always
parse a calligraphic $\mathcal{C}$ in context as a discrete
symmetry operator. The $\mathcal{P}$ / $\mathcal{T}$ / $\mathcal{CP}$
companions are likewise CPT operators; they do not collide with any
categorical or geometric reservation.

**Base ring convention (Lean).** In Lean source the generic ground
ring is **$R$** with the weakest typeclass that admits the
construction (`[CommRing R]`, `[Field R]`, `[GroupWithZero R]`,
etc.); the **real numbers $\mathbb{R}$** are used **only past the
archimedean wall** — specifically, when the declaration genuinely
needs `Real.sqrt`, `Real.rpow`, `Real.cos`, `Real.exp`, `Real.log`,
an ordering predicate (`0 < q`), `linarith`, or a CODATA /
experimental numerical value. Categorical content, algebraic
identities, q-deformation combinatorics, and Wenzl / Hecke /
Hoefsmit structural data all live over generic $R$. The narrative
side mirrors this in symbol use: $q \in R$ for the substrate
parameter when only the algebraic structure matters, $q \in \mathbb{R}$
only when an archimedean evaluation (numerical
$q_0 = 1.109978595554181\ldots$ (50 dps), the substrate's archimedean realisation) is
under discussion. See
[`CLAUDE.md` §7c](https://github.com/litlfred/qou/blob/main/CLAUDE.md#7c-base-ring-convention-generic-r-vs-archimedean-r-strict)
for the typeclass cheat-sheet and the archimedean-wall membership
list.

**Non-degeneracy of $q$: $\lvert q \rvert > 1$ (substrate) vs $q > 1$ (real specialization).**
The pre-Archimedean substrate's non-degeneracy condition on the
parameter is $\lvert q \rvert > 1$ — sufficient to make $q$ a unit
on any commutative ring with a norm, in particular $R = \mathbb{C}$
(see [`prop:q-zero-complex-extension`](../braids-and-knots/q-zero-complex-extension.md)).
The narrative and Lean infrastructure has historically used the
strict ordering $q > 1$ because the framework specializes to
$R = \mathbb{R}$ at the archimedean wall, where the two conditions
coincide. When writing **substrate-level** statements (pre-$\tau$,
categorical / algebraic content), prefer $\lvert q \rvert > 1$;
reserve $q > 1$ for **post-$\tau$** content that genuinely needs
the real ordering (Hoefsmit seminormal orthogonality,
`Real.sqrt`-bearing identities, CODATA comparisons). The real-axis
specialization $\mathrm{Im}(q_0) = 0$ is one valid choice; complex
$q_0$ with $\lvert q_0 \rvert > 1$ and $\mathrm{Im}(q_0) \neq 0$ is
structurally admissible but currently uninstantiated
(audit: [`-q-zero-reality-audit.md`](../../../docs/audits/-q-zero-reality-audit.md)).

**Decay width $\mathfrak{D}$ vs lifetime $\tau$ vs sheaf sections $\Gamma$.**
Three standard physics/math symbols collide in this paper:

| Symbol | Paper use | Physics use (avoided) | Resolution |
|--------|----------|----------------------|------------|
| $\tau$ | **Fibre functor** $\tau : \mathbf{C} \to \mathbf{Arch}$ | Lifetime $\tau_n, \tau_\mu$ | Use $\hbar / \mathfrak{D}$ for lifetime |
| $\Gamma$ | **Sheaf sections** $\Gamma(N)$, local cohomology $\Gamma_{\mathfrak{m}_1}$ | Decay width $\Gamma_n, \Gamma_\mu$ | Use $\mathfrak{D}$ (fraktur D) |
| $\mathfrak{D}$ | **Decay width** (NEW) | — | $\mathfrak{D}_K$ = decay width of hadron $K$ |

Convention: $\mathfrak{D}_K = \hbar / (\text{lifetime of } K)$.
Subscripts: $\mathfrak{D}_\mu$ (muon), $\mathfrak{D}_n$ (neutron),
$\mathfrak{D}_K$ (generic hadron). Fermi theory:
$\mathfrak{D}_\mu = G_F^2 \mathfrak{m}_\mu^5 / (192\pi^3)$.

**Archimedean / fibre / forgetful functors (Phase 5o disambiguation).**
Three nominally similar functors appear in the QOU framework and must
not be conflated:

| Functor | Domain → Codomain | Role |
|---|---|---|
| **Fibre functor** $\tau$ | $\mathbf{C} \to \mathbf{Arch}$ | Tannakian fibre over a brane point; selects which substrate object becomes the observation. |
| **Forgetful functor** $U$ | $\mathbf{Arch} \to \mathbf{Vec}_{\mathbb{R}}$ | Drops the archimedean enrichment, leaving the underlying real vector space. |
| **Archimedean realisation** (informal "Arch") | $\mathbf{C}(R) \to \mathbf{C}(\mathbb{R})$ | Base-ring substitution (`R ↦ ℝ`) at the archimedean wall; **not** a functor between QOU categories — it lives at the Lean / compute level (CLAUDE.md §7c). |

The category $\mathbf{Arch}$ is the target of $\tau$, not the name of
a functor; "archimedean functor" in chat or commits usually means
either the fibre functor $\tau$ (with explicit Arch codomain) or the
base-ring realisation, and the two are categorically distinct. When
authoring, **say which** — "$\tau$ specialised to $\mathbf{Arch}$"
or "the $R \mapsto \mathbb{R}$ realisation" — and never write "the
archimedean functor" without context.

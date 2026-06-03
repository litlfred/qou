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
- **$r$** = spinor information rate, $r = q^{1/2}$, $r^2 = q$.
  Eigenvalue of the elementary half-twist on the spin-½ fundamental
  rep of $\mathrm{SU}_q(2)$. Reserved exclusively for this purpose.
  **Never** use $r$ for radius (use $\rho$), recurrence rate (use
  $\nu$), or Wenzl level (use $\ell$ — see below). The relation to
  $q$ is exactly analogous to $i$ vs $-1$: $r$ opens up the 2-D
  spinor (spin-½) representation from the 1-D adjoint (spin-1)
  representation. **Never** use $t$ for $q^{1/2}$ either ($t$ is
  the standard knot-polynomial variable in $V_K(t)$, and $t$ is
  also reserved for time-like usage).
- **$u$** = **two distinct objects historically conflated in Python
  compute scripts** (registered 2026-06-01 after
  [`habiro_q_difference_fourier.py`](../../../folio-assistant/computations/habiro/habiro_q_difference_fourier.py)
  caught the collision producing a $5\times10^{38}$ error from the
  wrong substitution). They are **not interchangeable**:
    - **Habiro $u = q^{1/2}$** — the half-twist variable in the Habiro
      ring expansion $\mathrm{tr}_M = \sum_m a_m(u)\,(u;u)_m / D(u)$,
      $a_m \in \mathbb{Z}[u]$. This is *numerically equal to the
      registered spinor rate $r = q^{1/2}$* (§above); the two names
      coexist because $u$ is the established symbol in the Habiro /
      cyclotomic-completion literature (Habiro 2002) while $r$ is the
      QOU spinor-rate name. At $q_0 \approx 1.110$, $u = \sqrt{q_0}
      \approx 1.054$.
    - **Ladder $u_{\text{ladder}} = b\,\hbar_q^2$** — the $Q_\beta$
      precision-ladder step variable, $Q_\beta = Q_{\text{base}}
      \prod_k (1 + c_k\,u_{\text{ladder}}^k)$, with $b$ the Hoefsmit
      coupling and $\hbar_q = (q-1)/q$. At $q_0$, $u_{\text{ladder}}
      \approx 0.00852$ — **three orders of magnitude smaller** than the
      Habiro $u$, so silent substitution of one for the other is a
      catastrophic error, not a small drift.
  **Discipline:** any compute script using $u$ must name which one in a
  comment at definition (`u = sqrt(q)  # Habiro half-twist` vs
  `u_ladder = b*hbar**2  # Q_β ladder step`). When both appear in one
  script, the ladder variable **must** be spelled `u_ladder` (never
  bare `u`). 15 scripts use the Habiro $u$, 14 use the ladder $u$ as of
  this registration; mixing them without the explicit name is a
  registered audit flag.
- **$\ell$** = Wenzl principal-specialisation length (number of
  points in $s_\lambda(1, q^2, \ldots, q^{2(\ell-1)})$). **Renamed
  from $r_W$** to free $r$ for the spinor rate. Old code/docs
  using $r_W$ should migrate to $\ell$.
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
$J_K(q)$, not $V_K(t)$.

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

**Two bars + dagger — three distinct involutions (never share a glyph).**

| notation | name | meaning |
|---|---|---|
| $\overline{x}$ | conjugation bar | the archimedean place's involution (the QM bar, $\lvert\psi\rvert^2 = \psi\overline{\psi}$); trivial at real $q_0$ |
| $f(q^{-1})$, or $\mathrm{b}(f)$ | Hecke / KL bar | the fibre-level duality $q \mapsto q^{-1}$ (Kazhdan–Lusztig; §7b "bar-involution invariant"). Written **functionally** — it is literally substitution $q \to q^{-1}$, so for a $q$-function $f$ its bar is $f(q^{-1})$; the operator form is $\mathrm{b}(f)$, defined by $\mathrm{b}(f)(q) = f(q^{-1})$ |
| $x^{\dagger}$ | dagger / adjoint | the $\dagger$-compact adjoint (categorical inner product, $\mathrm{SU}(2)$ unitarity) — see `dagger-su2`, `adjoint-trace` |

**Functional notation for the Hecke bar (convention).** Because every
object we bar — $\mathrm{tr}_M$, $\chi^\lambda$, $J_K$ — is already a
function of $q$, the Hecke/KL bar needs **no new accent**: write it as
evaluation at $q^{-1}$. The bar-pairing is $\mathrm{tr}_M(q)\,
\mathrm{tr}_M(q^{-1})$; use the operator $\mathrm{b}(\cdot)$ only when
the involution itself must be named on an abstract Hecke-algebra
element. This keeps conjugation $\overline{\cdot}$ and the adjoint
$\dagger$ untouched.

The conjugation bar and the Hecke bar **coincide only on the unit
circle** $\lvert q\rvert = 1$ (root of unity): there $q^{-1} =
\overline{q}$, so $f(q^{-1}) = \overline{f(q)}$ and $\mathrm{tr}_M(q)\,
\mathrm{tr}_M(q^{-1}) = \lvert\mathrm{tr}_M\rvert^2$. At the **real**
substrate anchor $q_0 \approx 1.1097$ ($\lvert q_0\rvert \neq 1$) they
are different maps: the archimedean observation $\tau$ realizes the
modulus $\lvert\mathrm{tr}_M(q_0)\rvert$ (conjugation bar, trivial at
real $q_0$), whereas $\mathrm{tr}_M(q_0^{-1})$ evaluates at the mirror
point $q_0^{-1} \approx 0.9009$ — a *different* archimedean place, used
only for fibre-level identities (Habiro recursion, $\alpha_{EM}$
$[2]_q(1-\hbar^2\alpha)$), never as the observation. Rationale in
[`docs/audits/2026-06-03-bar-pairing-does-not-improve-binding.md`](../../../docs/audits/2026-06-03-bar-pairing-does-not-improve-binding.md).

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

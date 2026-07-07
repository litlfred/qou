A handful of common letters carry overloaded meanings in the literature. We enforce the following conventions throughout this paper to disambiguate them:

- **$c$** = color (never charm; charm is $\mathfrak{c}$).
- **$b$** = generic variable (never bottom quark; bottom is $\mathfrak{b}$).
- **$p$** = brane point (never proton number; proton number is $Z$).
- **$E$** alone = not used for an exceptional divisor, energy, or elliptic curve. We use $\mathcal{S}_p$, $\mathfrak{E}$, or $\mathcal{E}_q$ respectively. $E_{\mathfrak{H}}$ (with hadron subscript) is allowed for crossing energy.
- **$\mathfrak{E}_0$ vs $Q_\beta(n)$** — two distinct hadronic-sector scalars historically conflated in Python compute scripts (see [`computations/binding_canonical.py`](../../../computations/binding_canonical.py) history). They are not interchangeable:
    - $\mathfrak{E}_0$ = hadronic energy scale. We derive this as $\mathfrak{E}_0^{(N=0)} = m_e/(q_0(q_0-1)) \approx 4.186$ MeV (CAL-1 and CAL-2 only). The tower-summed form is $\mathfrak{E}_0^{\text{full}} = \mathfrak{E}_0^{(N=0)}/(1-\hbar_q^2) \approx 4.228$ MeV. It sets the MeV-per-dimensionless-trace-unit conversion for hadronic predictions.
    - $Q_\beta(n) = 0.78233341\,\text{MeV}$ = the free-neutron $\beta$-decay Q-value. We derive this from CAL-2 ($\mathfrak{D}_\beta$). We use it as the binding-energy-scale multiplier in [`prop:categorical-mass-markov`](../braids-and-knots/categorical-mass-markov.md)'s explicit binding formula $B = Q_\beta(n) \cdot (|\mathrm{tr}_M(W_{\text{free}})| - |\mathrm{tr}_M(W_{\text{atom}})|)$.
  The ratio is $\mathfrak{E}_0/Q_\beta(n) = 1/|\Delta(\mathrm{net})| \approx 5.31$ (the dimensionless Hecke NF reduction). Code must name the parameter for the actual quantity it carries. Using `E_0` for a $Q_\beta$-valued binding-scale variable raises a registered audit flag.
- **$\gamma$** = three reserved meanings, all standard, disambiguated by context: (i) the photon (default reading in particle / QED contexts: pair production $\gamma\gamma \to e^+ e^-$, photonic channels, Breit–Wheeler vertices); (ii) the Euler–Mascheroni constant (only inside zeta-value identities, e.g. $\zeta'(0) = -\tfrac{1}{2}\log(2\pi)$, $\gamma = \lim(H_n - \log n)$); (iii) Dirac matrices $\gamma^\mu$ (always with an explicit Lorentz index). We never use $\gamma$ for a vortex or closed cycle — the vortex morphism is $\varrho$.
- **$\chi_q$** = Lyapunov exponent (distinct from $\chi_\zeta(c)$, the character).
- **$\zeta$** = three distinct uses, never bare. We use $\zeta_n := e^{2\pi i/n}$ (primitive $n$-th root of unity, always with integer subscript — e.g. $\zeta_5$, $\zeta_6 = e^{i\pi/3}$); $\zeta(s)$ (Riemann zeta function, always parenthesised, e.g. $\zeta(2) = \pi^2/6$, $\zeta(3)$ — Apéry's constant); $\chi_\zeta(c)$ (character, always with $\chi$ prefix and argument). We do not use the bare token $\zeta$ alone.
- **$\mathcal{P}_n$** = Goncharov period filtration class (weight-$n$ periods modulo lower-weight). This is distinct from $P_\ell$, the elementary symmetric polynomials in Jucys–Murphy elements ([`prop:jucys-murphy-central-elements-qou`](#prop:jucys-murphy-central-elements-qou)), which are non-calligraphic and indexed by symmetric-polynomial degree.
- **$H_q$** alone = not used. Three distinct concepts share the letter $H$: $\mathcal{H}_q$ (shuffle Hopf algebra), $\hat{H}_q$ (Hamiltonian operator), $H_n(q)$ or $H_q(\lambda)$ (Hecke / hook-length, always with argument).
- **$\mathfrak{S}$** = categorical action (fraktur, Hamilton's $S$). We previously wrote the action two ways — calligraphic $\mathcal{S}_q$ and plain $S_q$. We now unify both to $\mathfrak{S}_q$ throughout the paper. This frees calligraphic $\mathcal{S}$ for the state bundle alone (QOU tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$). Three other objects deliberately keep $S$ / $\mathrm{Sk}$ and are not the action:
    - the Hopf antipode $S$ (plain $S$, or $S_q$ on the $q$-shuffle Hopf algebra);
    - the q-entropy $S_q(U)$ (`quantum-temperature`, with $\partial S_q/\partial \mathfrak{E}_q = 1/T_q$) and the Bekenstein–Hawking entropy $S_{BH}$ — entropy is a distinct thermodynamic observable, never the action;
    - the Skein module $\mathrm{Sk}_q(\mathbf{C})$ — the $\mathbb{Z}[q^{\pm 1}]$-algebra of knot classes, with mass functional $\mathcal{M}\colon \mathrm{Sk}_q \to \mathbb{R}_{\geq 0}$. We moved this off calligraphic $\mathcal{S}$ (where it collided with the state bundle) to roman $\mathrm{Sk}$, since single-letter calligraphic was blocked: $\mathcal{S}$ = state bundle, $\mathcal{K}$ = knot.
- **$\mathfrak{O}$** = observation / intent morphism — the section $(\mathfrak{O}, \epsilon)$ of $\mathrm{Ad}(J^1\mathcal{S})$ and its germ endomorphism $\mathfrak{O}_p$. We never use this for an ideal. The genus-filtration ideal keeps $\mathfrak{I}$ ($\mathfrak{I}_4 = (u^5)$). We moved intent off $\mathfrak{I}$ to disambiguate the two.
- **$\mathfrak{W}$** = confinement observable / $q$-Wilson loop $\mathfrak{W}(\mathcal{K}, \mathcal{T})$. We never use this for the observation morphism (now $\mathfrak{O}$). The abstract Wilson-loop functional is plain $W(\gamma)$. This is distinct from $\mathfrak{V}$ (below).
- **$\mathfrak{V}$** = the complex-volume observable (QOU analogue of the Neumann–Zagier complex volume $\mathbb{V}=\operatorname{Vol}+i\,\mathrm{CS}$): $\mathfrak{V}(K) = E_0\,\mathrm{tr}_M((\Pi_{\text{free}}-\mathbf{1})\circ\mathcal{M})$. Its real part is binding $\mathfrak{E}_{\mathrm{bind}} = \operatorname{Re}\mathfrak{V}$ (bar-even / $\cosh$) and its imaginary part is the $\beta$-decay Q-value $\mathfrak{Q}_\beta = \operatorname{Im}\mathfrak{V}$ (bar-odd / $\sinh$) ([`conj:binding-qbeta-complex-volume`](../mass-endomorphism/binding-qbeta-complex-volume.md)). We do not use $\mathfrak{W}$ (Wilson loop) or $\mathbb{V}$ (the literal NZ symbol, used only as the analogy reference).
- **$\Pi_{\text{free}}$** = idempotent projector onto the factorized sub-object (parabolic/Young subalgebra; constituents un-linked). The "free" trace is $\mathrm{tr}_M\circ\Pi_{\text{free}}$.
- **$\mathfrak{Q}_\beta$ (fraktur)** = the $\beta$-decay Q-value as a *trace-component* ($\operatorname{Im}\mathfrak{V}$, derived). We promoted this to fraktur (observable register) from the older roman $Q_\beta$. The measured/experimental value is $\mathfrak{Q}_\beta^{\,\mathrm{obs}}$ (CODATA).
- **$\mathfrak{D}$ (decay width) vs $\mathcal{D}$ (operator)** — visually close but register-distinct. We write $\mathfrak{D}$ (fraktur, a decay-rate observable) always carrying a decay subscript ($\mathfrak{D}_\beta$ neutron, $\mathfrak{D}_\pi$ pion) as the experimental face of a trace-component energy (not itself a $\mathrm{tr}_M$). We write $\mathcal{D}$ (calligraphic, an operator) as the categorical Dirac operator $\mathcal{D}_\nabla$ or the path measure $\mathcal{D}\phi$. The subscript / decoration disambiguates. We never write a bare $\mathfrak{D}$ or bare $\mathcal{D}$.
- **$S_n$ vs $H_n(q)$** — $q$-deformed braiding decompositions (eigenvalues $\{q, -q^{-1}\}$) are actions of the Iwahori–Hecke algebra $H_n(q)$, not the symmetric group $S_n$, even when the block dimensions match the classical $S_n$ irreps (§7a–7b). We write classical $S_n$ only for a genuine $\epsilon = \pm 1$ flip. We never write fraktur $\mathfrak{S}_n$ (fraktur $\mathfrak{S}$ is the action).
- **Three partition-weight families** — Markov $y_\lambda$, Plancherel $w_\lambda$, q-deformed Wedderburn $\tilde w_\lambda$ — are distinct at $q \neq 1$ and must not be conflated. They coincide at $q = 1$. Specifically:
    - $y_\lambda$ = Jones–Markov central coefficient ($\mathrm{tr}_M = \sum y_\lambda \chi_\lambda$, Wenzl hook–content closed form);
    - $w_\lambda = (\dim V_\lambda)^2 / n!$ = classical Plancherel probability measure, $\sum w_\lambda = 1$ exactly;
    - $\tilde w_\lambda = \dim_q^2(\lambda) / [n]_q!$ = q-deformed Wedderburn-block weight, $\sum \tilde w_\lambda$ finite but $\neq 1$ at $q \neq 1$ (empirically $\approx 1.51$ at $q_0$, $n = 12$).
  We use $w_\lambda$ unsubscripted only for the classical Plancherel measure. We mark the q-deformed analogue with the tilde ($\tilde w_\lambda$). The Wenzl-bridge identity $y_\lambda = w_\lambda$ holds on the self-conjugate stratum only (where $\kappa_\lambda = \sum_{x} c(x) = 0$).

  We have a fourth scalar that does NOT belong to the weight family but is easy to misread as one because of the symbol $\mu_\lambda$:

    - $\mu_\lambda(q)$ = $q$-Laplacian eigenvalue on $V_\lambda$ from [`prop:q-heat-kernel-peter-weyl`](../information-theory/q-heat-kernel-peter-weyl.md) — the heat-flow decay rate $\hbar_q^2 \sum_{x \in \lambda} [c(x)]_q [c(x)+1]_q$. This is NOT a Markov-trace ingredient. It does not multiply $\chi^\lambda$, does not sum to anything normalised, and does not appear in the Frobenius expansion. Symbol-similarity to $w_\lambda$ / $\tilde w_\lambda$ makes conflation tempting. We avoid it.

  **Concrete $H_3$ values at $q = 1$** (Jones-normalised $V / [2]_q^{c-1}$ convention of [`prop:borromean-markov-trace-closed-form`](../mass-theory/borromean-markov-trace-closed-form.md) and [`prop:h3-markov-wenzl-weights`](../mass-theory/h3-markov-wenzl-weights.md)):

  | $\lambda$ | $d_\lambda$ | $y_\lambda(1)$ | $w_\lambda(1)$ | $\mu_\lambda(1)$ |
  |---|---|---|---|---|
  | $(3)$ | $1$ | $1/2$ | $1/6$ | $0$ |
  | $(2,1)$ | $2$ | $1/4$ | $2/3$ | $2 \hbar_q^2$ |
  | $(1^3)$ | $1$ | $0$ | $1/6$ | $0$ |
  | sum identity | — | $\sum y_\lambda d_\lambda = 1$ | $\sum w_\lambda = 1$ | (no sum) |

  The $y_\lambda$ vector $(1/2, 1/4, 0)$ is not uniform and $y_{(1^3)} = 0$ identically (Temperley–Lieb quotient — Jones factors through TL). The Wenzl-bridge $y_\lambda = w_\lambda$ fails at $\lambda = (2,1)$ here ($1/4 \neq 2/3$) because the bridge identity uses a different (non-Jones, Schur-element) normalisation of $y_\lambda$. They coincide on the self-conjugate stratum after matching normalisation conventions. When in doubt, we cite the source proposition.
- **$\check{q}$** (q-háček, meaning "little hook" in Czech) = spinor information rate, $\check{q} = q^{1/2}$, $\check{q}^2 = q$. This is the eigenvalue of the elementary half-twist on the spin-½ fundamental rep of $\mathrm{SU}_q(2)$. We reserve it exclusively for this purpose. The háček diacritic encodes the relation $\check{q}^2 = q$ in the glyph, making every occurrence self-documenting. The relation to $q$ is exactly analogous to $i$ vs $-1$. The spinor rate $\check{q}$ opens up the 2-D spinor (spin-½) representation from the 1-D adjoint (spin-1) representation. We renamed this from $r$ on 2026-06-04 to free $r$ for radius / generic-real contexts. We never use $r$ or $t$ for $q^{1/2}$ ($t$ clashes with the $V_K(t)$ knot variable and with time-like usage). We reserve $\iota$ for involution / inclusion.
- **$u$** = LP shadow-price $u_\lambda, u_0$ (Schrijver convention for operator-selection LP dual variables, see Table 3 row 15) or the $Q_\beta$ precision-ladder step variable $u_{\text{ladder}} = b\,\hbar_q^2$ with $Q_\beta = Q_{\text{base}} \prod_k (1 + c_k\,u_{\text{ladder}}^k)$, $b$ the Hoefsmit coupling and $\hbar_q = (q-1)/q$. At $q_0$, $u_{\text{ladder}} \approx 0.00852$. We retired Habiro $u = q^{1/2}$ on 2026-06-04. We now write the Habiro-ring expansion as $\mathrm{tr}_M = \sum_m a_m(\check{q})\,(\check{q};\check{q})_m / D(\check{q})$ with $\check{q}$ the spinor rate above. When a compute script uses BOTH the ladder step and either the LP shadow-price $u_\lambda$ or the (retired) Habiro $u$, the ladder variable must be spelled `u_ladder` to keep contexts unambiguous. Single-context scripts may keep bare `u` when an in-script comment annotates which meaning applies (`u = sqrt(q)` for Habiro-facing scripts is permitted when accompanied by `# = \check{q}, spinor rate` annotation).
- **$\ell$** = Wenzl principal-specialisation length (number of points in $s_\lambda(1, q^2, \ldots, q^{2(\ell-1)})$). We renamed this from $r_W$ in the May 2026 notation cleanup. Old code/docs using $r_W$ should migrate to $\ell$.
- We do not use numerical $q \approx 1.110$ (or any specific value of the substrate parameter) outside the introduction, Chapter 8 (Information Theory, for falsifiability computations), and Chapter 11 (Observations). Geometry chapters use symbolic $q$.

**Approximation convention (derived / observed values).** Numerical values derived from the substrate parameter $q_0$ or compared to experimental data use $\approx$ (or $\simeq$), never $=$, unless an explicit error term is present. Exact algebraic identities (e.g. $c_q = 1/(q-1)$) use $=$ since they hold for all $q$.

**Hecke–Skein convention.** The Hecke algebra generator is $\sigma_i$ (never $T$, never $t$ or $A$ for the Jones polynomial variable). The Iwahori–Hecke algebra $H_n(q)$ is presented as a quotient of the braid group algebra of $B_n$. We use the same symbol $\sigma_i$ to denote both the braid-group generator and its image in $H_n(q)$. Context disambiguates. The Jones polynomial is always $J_K(q)$, not $V_K(t)$. The letter $J$ is shared with the Hahn–Exton q-Bessel function $J_\nu^{(3)}(x;q)$ (substrate harmonic analysis, the $\mathrm{SU}_q(2)\to E_q(2)$ contraction) and the ordinary Bessel weights $J_n(x)$ of the Jacobi–Anger expansion. We disambiguate these by their subscript. We use a knot/link $K$ for the Jones polynomial, and an order $\nu$/$n$ (always with an argument $x$, and the $(3)$ superscript for Hahn–Exton) for Bessel. We never write bare $J$.

**Categories vs CPT operators.** We typeset categories in bold, $\mathbf{C}$, $\mathbf{Rep}$, etc. We reserve the calligraphic $\mathcal{C}$ for the charge-conjugation operator in CPT discussions (parity $\mathcal{P}$, time-reversal $\mathcal{T}$, combined $\mathcal{CP}$, $\mathcal{CPT}$). Calligraphic $\mathcal{C}$ never denotes a category in this paper. Readers should parse a calligraphic $\mathcal{C}$ in context as a discrete symmetry operator. The $\mathcal{P}$ / $\mathcal{T}$ / $\mathcal{CP}$ companions are likewise CPT operators. They do not collide with any categorical or geometric reservation.

**Dirac bra–ket $\lvert \psi \rangle$ / $\langle \phi \vert \psi \rangle$.** The framework's states are objects and morphisms of $\mathbf{C}$ and vectors of its Hecke modules. The native scalar-valued form is the Frobenius pairing, written in comma form $\langle x, y\rangle_F$. We write matrix elements as $\langle v, \Phi v\rangle_F$, never $\langle v \vert \Phi \vert v\rangle$. We write seminormal / Young basis vectors as $v_T$ (SYT $T$) or $v_c$ (channel $c$), never kets $\lvert T \rangle$, $\lvert \psi_N \rangle$. We reserve bra–ket notation for quoted standard-QM material only. A ket carrying framework-native mathematics is an audit flag.

**Base ring convention (Lean).** In Lean source, the generic ground ring is $R$ with the weakest typeclass that admits the construction (`[CommRing R]`, `[Field R]`, `[GroupWithZero R]`, etc.). We use the real numbers $\mathbb{R}$ only past the archimedean wall — specifically, when the declaration genuinely needs `Real.sqrt`, `Real.rpow`, `Real.cos`, `Real.exp`, `Real.log`, an ordering predicate (`0 < q`), `linarith`, or a CODATA / experimental numerical value. Categorical content, algebraic identities, q-deformation combinatorics, and Wenzl / Hecke / Hoefsmit structural data all live over generic $R$. The narrative side mirrors this. We write $q \in R$ for the substrate parameter when only the algebraic structure matters, and $q \in \mathbb{R}$ only when an archimedean evaluation is under discussion. See [`AGENTS.md` §7c](https://github.com/litlfred/qou/blob/main/AGENTS.md#7c-base-ring-convention-generic-r-vs-archimedean-r-strict) for the typeclass cheat-sheet and the archimedean-wall membership list.

**Non-degeneracy of $q$.** The pre-Archimedean substrate's non-degeneracy condition on the parameter is $\lvert q \rvert > 1$. This is sufficient to make $q$ a unit on any commutative ring with a norm, in particular $R = \mathbb{C}$ (see [`prop:q-zero-complex-extension`](../braids-and-knots/q-zero-complex-extension.md)). When writing substrate-level statements (pre-$\tau$, categorical / algebraic content), we prefer $\lvert q \rvert > 1$. We reserve $q > 1$ for post-$\tau$ content that genuinely needs the real ordering (Hoefsmit seminormal orthogonality, `Real.sqrt`-bearing identities, CODATA comparisons).

**Decay width $\mathfrak{D}$ vs lifetime $\tau$ vs sheaf sections $\Gamma$.** Three standard physics/math symbols collide in this paper:

| Symbol | Paper use | Physics use (avoided) | Resolution |
|--------|----------|----------------------|------------|
| $\tau$ | **Fibre functor** $\tau : \mathbf{C} \to \mathbf{Arch}$ | Lifetime $\tau_n, \tau_\mu$ | Use $\hbar / \mathfrak{D}$ for lifetime |
| $\Gamma$ | **Sheaf sections** $\Gamma(N)$, local cohomology $\Gamma_{\mathfrak{m}_1}$ | Decay width $\Gamma_n, \Gamma_\mu$ | Use $\mathfrak{D}$ (fraktur D) |
| $\mathfrak{D}$ | **Decay width** (NEW) | — | $\mathfrak{D}_K$ = decay width of hadron $K$ |

Convention: $\mathfrak{D}_K = \hbar / (\text{lifetime of } K)$. Subscripts: $\mathfrak{D}_\mu$ (muon), $\mathfrak{D}_n$ (neutron), $\mathfrak{D}_K$ (generic hadron). Fermi theory: $\mathfrak{D}_\mu = G_F^2 \mathfrak{m}_\mu^5 / (192\pi^3)$.

**Archimedean / fibre / forgetful functors.** Three nominally similar functors appear in the QOU framework and must not be conflated:

| Functor | Domain → Codomain | Role |
|---|---|---|
| **Fibre functor** $\tau$ | $\mathbf{C} \to \mathbf{Arch}$ | Tannakian fibre over a brane point; selects which substrate object becomes the observation. |
| **Forgetful functor** $U$ | $\mathbf{Arch} \to \mathbf{Vec}_{\mathbb{R}}$ | Drops the archimedean enrichment, leaving the underlying real vector space. |
| **Archimedean realisation** (informal "Arch") | $\mathbf{C}(R) \to \mathbf{C}(\mathbb{R})$ | Base-ring substitution (`R ↦ ℝ`) at the archimedean wall; **not** a functor between QOU categories. |

The category $\mathbf{Arch}$ is the target of $\tau$, not the name of a functor. When authoring, we say which one: "$\tau$ specialised to $\mathbf{Arch}$" or "the $R \mapsto \mathbb{R}$ realisation". We never write "the archimedean functor" without context.

**Binding-energy notions $B_\bullet$.** The framework accumulates many distinct "binding energy" objects, almost all written as a bare $B$ or $B(K)$. We keep binding as plain $B$ with systematic subscripts. The kept canonical symbols (see [`2026-06-15-binding-energy-notation-catalog.md`](../../../docs/audits/2026-06-15-binding-energy-notation-catalog.md)):

| Symbol | Definition | Role | Status |
|---|---|---|---|
| $B_{\mathrm{AME}}$ | AME 2020 measurement | experimental ground truth | anchor |
| $B_{\mathrm{sym}}$ | $-\alpha \ln\lvert\mathrm{tr}_M(K)\rvert$ (log-trace) | **exact** symbolic, light $A$ | kept |
| $B_{\mathrm{qCLT}}$ | $-\alpha \sum_i \ln\lvert V_i\rvert$ | qCLT asymptotic, $A\to\infty$ | kept |
| $B_{\mathrm{lin}}$ | $Q_\beta(n)\,(\mathrm{tr}_M(W_{\text{free}}) - \mathrm{tr}_M(W_{\text{atom}}))$ | **linear-truncation** production | canonical compute |
| $B_{\mathrm{depth}}$ | $\sum_k \alpha_k \Phi_k$ | depth-stratified tower | default; empirical $\alpha_k$ |
| $B_{\mathrm{magic}}$ | $2\,m_e A\,\mathrm{Vol}(L6a4)$ (⁴He) | flat magic-$A$ | ⁴He canonical |
| $B_\lambda$ | $m_e \sum_\lambda y_\lambda \chi^\lambda \Delta_\lambda$ | per-partition | $\Delta_\lambda$-gated |

**Critical distinction — $B_{\mathrm{sym}}$ (exact) vs $B_{\mathrm{lin}}$ (linear).** $B_{\mathrm{lin}}$ is the linearization of $B_{\mathrm{sym}}$ (Kashaev $\mathrm{tr}_M \sim \exp(\mathrm{Vol})$; the scalar $\Delta\mathrm{tr}$ is the first-order term). They are NOT interchangeable. Their ratio is the binding deficit
$$ B_{\mathrm{sym}} / B_{\mathrm{lin}} \;\approx\; q_0^{\,5(2A-1)}, $$
i.e. the $\Delta_\lambda = B_{\mathrm{AME}}/B_{\mathrm{lin}}$ residual. We always subscript $B$. A bare $B$ in prose denotes the production $B_{\mathrm{lin}}$.

## Quantum dilogarithm: $\Phi_q$ (compact) vs $\Phi_b$ (Faddeev non-compact)

Two distinct functions were historically both called "Faddeev $\Phi_q$",
which is **forbidden** (terminology ruling 2026-07-06,
[`2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md`](../../../docs/audits/2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md)):

| Symbol | Definition | Correct name |
|---|---|---|
| $\Phi_q(z)$ | $\prod_{k\ge 1}(1 - q^{-k}z)^{-1}$ (reciprocal $q$-Pochhammer) | **compact quantum dilogarithm** / $q$-exponential |
| $\Phi_b(z)$ | modular-double ratio, kernel $\sinh(zb)\sinh(z/b)$, poles at $c_b + ib\mathbb{N} + i b^{-1}\mathbb{N}$ | **Faddeev** (non-compact) quantum dilogarithm |

- **"Faddeev" belongs to $\Phi_b$ only.** Never write "Faddeev $\Phi_q$" for
  the compact form; write "compact quantum dilogarithm $\Phi_q$" (or
  "$q$-Pochhammer").
- $\Phi_q$ is correct on the real-$q$ / **mass** (bar-even, Rogers) face;
  $\Phi_b$ is the **decay** ($\mathfrak{Q}_\beta$, bar-odd, root-of-unity)
  face. At the real substrate $\Phi_b \to \Phi_q$ (the modular dual
  $\tilde q$ is $\sim 10^{-165}$-suppressed).
- Canonical evaluator: [`computations/qbeta/phi_b_evaluator.py`](../../../computations/qbeta/phi_b_evaluator.py)
  ($\Phi_b$, literature-verified vs Hikami math/0604094); Lean structure
  `QOU.QBeta.FaddeevModularDouble` ($\Phi_b$). The legacy Lean class
  `QOU.Machinery.FaddeevQuantumDilogContext` names the **compact** $\Phi_q$
  (kept for `lean.ref` compatibility; its docstring flags this).
- **Residual collision — follow-up cleanup:** a few Askey-two-saddle prose
  sites use the single glyph "$\Phi_q$" where context makes clear the
  non-compact regulator is meant. Resolving that (a distinct glyph, or always
  writing $\Phi_b$) is a follow-up notation decision; until then, disambiguate
  in surrounding prose.

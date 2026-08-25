A handful of common letters carry overloaded meanings in the literature. We enforce the following conventions throughout this paper to disambiguate them:

- **$c$** = color (never charm; charm is $\mathfrak{c}$).
- **$b$** = generic variable (never bottom quark; bottom is $\mathfrak{b}$).
- **$p$** = brane point (never proton number; proton number is $Z$).
- **$E$** alone = not used for an exceptional divisor, energy, or elliptic curve. We use $\mathcal{S}_p$, $\mathfrak{E}$, or $\mathcal{E}_q$ respectively. $E_{\mathfrak{H}}$ (with hadron subscript) is allowed for crossing energy.
- **$\mathfrak{E}_0$ vs $Q_\beta(n)$** — two distinct hadronic-sector scalars historically conflated in Python compute scripts (see [`computations/binding_canonical.py`](../../../computations/binding_canonical.py) history). They are not interchangeable:
    - $\mathfrak{E}_0$ = hadronic energy scale. We derive this as $\mathfrak{E}_0^{(N=0)} = m_e/(q_0(q_0-1)) \approx 4.186$ MeV (CAL-1 and CAL-2 only). The tower-summed form is $\mathfrak{E}_0^{\text{full}} = \mathfrak{E}_0^{(N=0)}/(1-\hbar_q^2) \approx 4.228$ MeV. It sets the MeV-per-dimensionless-trace-unit conversion for hadronic predictions.
    - $Q_\beta(n) = 0.78233341\,\text{MeV}$ = the free-neutron $\beta$-decay Q-value. We derive this from CAL-2 ($\mathfrak{D}_\beta$). We use it as the binding-energy-scale multiplier in [`prop:categorical-mass-markov`](../braids-and-knots/categorical-mass-markov.md)'s explicit binding formula $B = Q_\beta(n) \cdot (|\mathrm{tr}_M(W_{\text{free}})| - |\mathrm{tr}_M(W_{\text{atom}})|)$.
  The ratio is $\mathfrak{E}_0/Q_\beta(n) = 1/|\Delta(\mathrm{net})| \approx 5.31$ (the dimensionless Hecke NF reduction). Code must name the parameter for the actual quantity it carries. Using `E_0` for a $Q_\beta$-valued binding-scale variable is a registered notation violation.
- **$\gamma$** = three reserved meanings, all standard, disambiguated by context: (i) the photon (default reading in particle / QED contexts: pair production $\gamma\gamma \to e^+ e^-$, photonic channels, Breit–Wheeler vertices); (ii) the Euler–Mascheroni constant (only inside zeta-value identities, e.g. $\zeta'(0) = -\tfrac{1}{2}\log(2\pi)$, $\gamma = \lim(H_n - \log n)$); (iii) Dirac matrices $\gamma^\mu$ (always with an explicit Lorentz index). We never use $\gamma$ for a vortex or closed cycle — the vortex morphism is $\varrho$.
- **$c_k$ vs $\mathrm{cl}_k$** — the letter $c$ carried **three** distinct coefficient families, two of them within ~12% of each other numerically, which is how they stayed conflated. We now split them:
    - $c_k$ = **Q$_\beta$ precision-ladder** coefficients only, $Q_\beta = Q_{\text{base}}\prod_k(1 + c_k u^k)$ with $u = b\hbar_q^2$ — dimensionless, $c_2 = -1$, $c_3 = -2$ a near-match. (This register fixes the *symbol*; each rung's epistemic tier and its convention scoping live in the c$_k$/d$_k$ canonical registry. The word **"proved"** previously appeared on $c_2$ here and is removed as a symbol-level claim — the Lean identity re-reads the $N{=}2$ factor rather than deriving it. **"Taylor-exact" was NOT removed for being false**, and must not be: $c_2$ genuinely is the $u^2$ coefficient of the explicit-factor product $\prod_{k\ge2}(1 + c_k u^k)$. It is $\tilde c_2 = -9/8$ only for the normalised series with the cosine factor inside — so always say *which series*. No tier is changed by this edit.)
    - $\tilde c_k$ = the **normalised-series** coefficients of the *same* ladder model: the $u^k$ coefficients of $\Phi(u)/\Phi(0)$ rather than of the explicit factors. The tilde marks a **different normalisation of the same object** — deliberately *not* justified by the old $w_\lambda$ / $\tilde w_\lambda$ pairing, which this same register retired in the entry below. The two families are **not** interchangeable: the model's cosine factor contributes at every order, and $\tilde c_2 = c_2 - 1/8$ exactly, independently of the phase $\alpha$ (Lean, sorry-free: `QOU.QBeta.normalisedQuadCoeff_eq`), so the committed $c_2 = -1$ has $\tilde c_2 = -9/8$. **Both are correct** — one model at two normalisations. The $-1/8$ is contributed entirely by the half-argument in $\cos(\alpha - u/2)$.
    - $c_k^{\mathrm{even}}$ = the **bar-even part** of the ladder data, exact in $\mathbb{Q}(\sqrt 3)$ — a third object, read as neither $c_k$ nor $\tilde c_k$.
    - $\mathrm{cl}_k$ = **cluster / Ursell coefficients** of the many-body expansion — MeV-valued. $\mathrm{cl}_3 = -\mathfrak{E}_0\,\Delta^2 g$ is the three-body cluster coefficient of the $\mu_3$ door ($\mu_3 > 0 \iff \Delta^2 g < 0$), and the Borromean H$_9$ magnitude lift is the same family.
  We never write a bare $c_k$ for a cluster coefficient, and never quote a $c_k$ value without saying which of $c_k$ / $\tilde c_k$ / $c_k^{\mathrm{even}}$ it is — the three differ at the same $k$ ($-1$, $-9/8$, $\approx -8.006$ at $k = 2$). Rationale for the roman two-letter tag rather than a new single letter: **every** single Roman letter is either register-claimed or produces a same-domain case-collision ($X_k$ vs the knot object $X_K$; $Y_k$ vs the Markov weight $y_\lambda$; $Z$ = proton number; $W_\lambda$ = geometric weight; $j$ vs the Jones polynomial $J_K(q)$). This follows the same resolution already used for $\mathrm{Sk}$ (Skein module, moved off $\mathcal{S}$) and $h_{\mathrm{A}}$ (Hecke amplitude, moved off bare $H_A$).
- **$\chi_q$** = Lyapunov exponent (distinct from $\chi_\zeta(c)$, the character).
- **Euler characteristic is $\chi_{\mathrm{eu}}$ — never a bare $\chi$.** The glyph $\chi$ is shared by three register-claimed families: the **characters** $\chi_\lambda$ (Frobenius pairing $\mathrm{tr}_M = \sum_\lambda y_\lambda \chi_\lambda$) and $\chi_\zeta(c)$; the Lyapunov exponent $\chi_q$ above; and the **Euler characteristic**, which keeps the standard glyph but always carries the roman subscript: $\chi_{\mathrm{eu}}$. A bare $\chi$ is a notation violation in all three senses. When a total and its strata both appear we subscript further rather than overload: $\chi_{\mathrm{eu}}(M)$ for the whole moduli, $\chi_{\mathrm{eu},i}$ for the $i$-th Behrend stratum. The DT setting is where this bites — a Donaldson–Thomas count is a *Behrend-weighted* Euler characteristic $\sum_i n_i\,\chi_{\mathrm{eu},i}$, whose unweighted total $\sum_i \chi_{\mathrm{eu},i} = \chi_{\mathrm{eu}}(M)$ is a different number. (Write $\chi_{\mathrm{eu}}$, not an uppercase "$\Chi$": there is no such KaTeX/LaTeX macro — uppercase Greek chi is glyph-identical to Latin X and has no control sequence, so it fails the render gate. The orbifold Euler *number* of $\Sigma(2,3,5)$ keeps its own conventional symbol $e = -1/30$.)
- **$-2$ vs $-6$ in the Stokes/DT sector** — two integers that are not the same object and must not be swapped. $\sum_{\lambda \vdash 3} \Delta_\lambda = -2$ is the QOU Wedderburn/Springer Euler characteristic (`partitionEuler3_eq`) and is the *prefactor* of the GGM sandwich $A \cdot W_{-1} \cdot B \cdot W_{-1}^{\mathsf{T}} \cdot C = -2\,S^{+}(0)$. The sandwich $(0,1)$ entry is $-6 = (-2)\cdot 3$ — the prefactor times the Stokes/DT **count** $S^{+}(0)_{01} = 3$ — and is *not* an Euler characteristic, notwithstanding the G3 directive's "Euler $= -6$" hint. Cite $-2$ for the Euler characteristic and $3$ for the count.
- **$\theta_p$ vs $\vartheta_K$** — two unrelated objects sharing a glyph. $\theta_p(w) = \sum_{n\in\mathbb{Z}} p^{-n(n+1)/2}w^{n}$ is the $q$-theta of a $q$-difference operator: a function of a complex variable, satisfying $\theta_p(pw) = w\,\theta_p(w)$, whose zero set is the orbit $-p^{\mathbb{Z}}$. $\vartheta_K$ is the **angular** deformation parameter of the volume channel $S_K = A_\omega\,\kappa\,(\ln^{2} q_0 - \vartheta_K^{2})$ — a real angle attached to a knot, not a function. Neither is a Newton-polygon slope; "theta order" in the slope register is a third, again unrelated, use of the word.
- **$\zeta$** = three distinct uses, never bare. We use $\zeta_n := e^{2\pi i/n}$ (primitive $n$-th root of unity, always with integer subscript — e.g. $\zeta_5$, $\zeta_6 = e^{i\pi/3}$); $\zeta(s)$ (Riemann zeta function, always parenthesised, e.g. $\zeta(2) = \pi^2/6$, $\zeta(3)$ — Apéry's constant); $\chi_\zeta(c)$ (character, always with $\chi$ prefix and argument). We do not use the bare token $\zeta$ alone.
- **$\mathcal{P}_n$** = Goncharov period filtration class (weight-$n$ periods modulo lower-weight). This is distinct from $P_\ell$, the elementary symmetric polynomials in Jucys–Murphy elements ([`prop:jucys-murphy-central-elements-qou`](#prop:jucys-murphy-central-elements-qou)), which are non-calligraphic and indexed by symmetric-polynomial degree.
- **$H_q$** alone = not used. Three distinct concepts share the letter $H$: $\mathcal{H}_q$ (shuffle Hopf algebra), $\hat{H}_q$ (Hamiltonian operator), $H_n(q)$ or $H_q(\lambda)$ (Hecke / hook-length, always with argument). The Hecke amplitude $q - q^{-1}$ is $h_{\mathrm{A}}$ (plain-italic scalar, roman subscript). Older text splits this between "$\mathrm{HA}$" and a bare "$H_A$"; bare $H_A$ collided with the Hecke algebra $H_A(q)$ on $A$ strands.
- **$\mathfrak{S}$** = categorical action (fraktur, Hamilton's $S$). We previously wrote the action two ways — calligraphic $\mathcal{S}_q$ and plain $S_q$. We now unify both to $\mathfrak{S}_q$ throughout the paper. This frees calligraphic $\mathcal{S}$ for the state bundle alone (QOU tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$). Three other objects deliberately keep $S$ / $\mathrm{Sk}$ and are not the action:
    - the Hopf antipode $S$ (plain $S$, or $S_q$ on the $q$-shuffle Hopf algebra);
    - the q-entropy $S_q(U)$ (`quantum-temperature`, with $\partial S_q/\partial \mathfrak{E}_q = 1/T_q$) and the Bekenstein–Hawking entropy $S_{BH}$ — entropy is a distinct thermodynamic observable, never the action;
    - the Skein module $\mathrm{Sk}_q(\mathbf{C})$ — the $\mathbb{Z}[q^{\pm 1}]$-algebra of knot classes, with mass functional $\mathfrak{m}\colon \mathrm{Sk}_q \to \mathbb{R}_{\geq 0}$ (fraktur; the calligraphic $\mathcal{M}$ is reserved for the mass *endomorphism* $\mathcal{M}(K)\in\mathrm{End}_{\mathbf{C}}(X_K)$ — see the $\mathcal{M}$ ruling below). We moved the Skein *module* off calligraphic $\mathcal{S}$ (where it collided with the state bundle) to roman $\mathrm{Sk}$, since single-letter calligraphic was blocked: $\mathcal{S}$ = state bundle, $\mathcal{K}$ = knot.
- **$\mathfrak{O}$** = observation / intent morphism — the section $(\mathfrak{O}, \epsilon)$ of $\mathrm{Ad}(J^1\mathcal{S})$ and its germ endomorphism $\mathfrak{O}_p$. We never use this for an ideal. The genus-filtration ideal keeps $\mathfrak{I}$ ($\mathfrak{I}_4 = (u^5)$). We moved intent off $\mathfrak{I}$ to disambiguate the two.
- **$\mathfrak{W}$** = confinement observable / $q$-Wilson loop $\mathfrak{W}(\mathcal{K}, \mathcal{T})$. We never use this for the observation morphism (now $\mathfrak{O}$). The abstract Wilson-loop functional is plain $W(\gamma)$. This is distinct from $\mathfrak{V}$ (below).
- **$\mathfrak{V}$** = the complex-volume observable (QOU analogue of the Neumann–Zagier complex volume $\mathbb{V}=\mathrm{Vol}+i\,\mathrm{CS}$): $\mathfrak{V}(K) = E_0\,\mathrm{tr}_M((\Pi_{\text{free}}-\mathbf{1})\circ\mathcal{M})$. Its real part is binding $\mathfrak{E}_{\mathrm{bind}} = \mathrm{Re}\mathfrak{V}$ (bar-even / $\cosh$) and its imaginary part is the $\beta$-decay Q-value $\mathfrak{Q}_\beta = \mathrm{Im}\mathfrak{V}$ (bar-odd / $\sinh$) ([`conj:binding-qbeta-complex-volume`](../mass-endomorphism/binding-qbeta-complex-volume.md)). We do not use $\mathfrak{W}$ (Wilson loop) or $\mathbb{V}$ (the literal NZ symbol, used only as the analogy reference).
- **$\Pi_{\text{free}}$** = idempotent projector onto the factorized sub-object (parabolic/Young subalgebra; constituents un-linked). The "free" trace is $\mathrm{tr}_M\circ\Pi_{\text{free}}$.
- **$\mathfrak{Q}_\beta$ (fraktur)** = the $\beta$-decay Q-value as a *trace-component* ($\mathrm{Im}\mathfrak{V}$, derived). We promoted this to fraktur (observable register) from the older roman $Q_\beta$. The measured/experimental value is $\mathfrak{Q}_\beta^{\,\mathrm{obs}}$ (CODATA).
- **$\mathfrak{D}$ (decay width) vs $\mathcal{D}$ (operator)** — visually close but register-distinct. We write $\mathfrak{D}$ (fraktur, a decay-rate observable) always carrying a decay subscript ($\mathfrak{D}_\beta$ neutron, $\mathfrak{D}_\pi$ pion) as the experimental face of a trace-component energy (not itself a $\mathrm{tr}_M$). We write $\mathcal{D}$ (calligraphic, an operator) as the categorical Dirac operator $\mathcal{D}_\nabla$ or the path measure $\mathcal{D}\phi$. The subscript / decoration disambiguates. We never write a bare $\mathfrak{D}$ or bare $\mathcal{D}$.
- **$S_n$ vs $H_n(q)$** — $q$-deformed braiding decompositions (eigenvalues $\{q, -q^{-1}\}$) are actions of the Iwahori–Hecke algebra $H_n(q)$, not the symmetric group $S_n$, even when the block dimensions match the classical $S_n$ irreps. We write classical $S_n$ only for a genuine $\epsilon = \pm 1$ flip. We never write fraktur $\mathfrak{S}_n$ (fraktur $\mathfrak{S}$ is the action).
- **Three partition-weight families** — Markov $y_\lambda$, q-deformed Wedderburn $w_\lambda(q)$, classical Plancherel $w_\lambda(1)$ — are distinct at $q \neq 1$ and must not be conflated. They coincide at $q = 1$. Specifically:
    - $y_\lambda$ = Jones–Markov central coefficient ($\mathrm{tr}_M = \sum y_\lambda \chi_\lambda$, Wenzl hook–content closed form);
    - $w_\lambda(1) = (\dim V_\lambda)^2 / n!$ = classical Plancherel probability measure, $\sum_\lambda w_\lambda(1) = 1$ exactly;
    - $w_\lambda(q) = \dim_q^2(\lambda) / [n]_q!$ = q-deformed Wedderburn-block weight, $\sum w_\lambda(q)$ finite but $\neq 1$ at $q \neq 1$ (empirically $\approx 1.51$ at $q_0$, $n = 12$).
  **Convention (owner ruling, 2026-08-16).** $w_\lambda(q)$ **is** the $q$-deformed Wedderburn-block weight, and the classical Plancherel measure is its specialisation $w_\lambda(1)$ — not a separate symbol. The two are the same function at different points: $\dim_q(\lambda) \to \dim V_\lambda$ and $[n]_q! \to n!$ as $q \to 1$, verified per-partition for $n = 3, 4, 5$ in `docs/audits/scripts/wlambda_normalisation_census.py`. Bare $w_\lambda$ means $w_\lambda(q)$ at the ambient $q$. The previous convention reserved bare $w_\lambda$ for the classical measure and marked the $q$-deformed one $\tilde w_\lambda$; that was followed by five content blocks and contradicted by eighteen, so the register moved rather than the corpus. **Never write a normalisation claim on bare $w_\lambda$** — $\sum_\lambda w_\lambda(1) = 1$ is exact, $\sum_\lambda w_\lambda(q)$ is not (0.987 at $n = 3$, 1.051 at $n = 8$). The Wenzl-bridge identity $y_\lambda = w_\lambda(q)$ holds on the self-conjugate stratum only (where $\kappa_\lambda = \sum_{x} c(x) = 0$).

  We have a fourth scalar that does NOT belong to the weight family but is easy to misread as one because of the symbol $\mu_\lambda$:

    - $\mu_\lambda(q)$ = $q$-Laplacian eigenvalue on $V_\lambda$ from [`prop:q-heat-kernel-peter-weyl`](../information-theory/q-heat-kernel-peter-weyl.md) — the heat-flow decay rate $\hbar_q^2 \sum_{x \in \lambda} [c(x)]_q [c(x)+1]_q$. This is NOT a Markov-trace ingredient. It does not multiply $\chi^\lambda$, does not sum to anything normalised, and does not appear in the Frobenius expansion. Symbol-similarity to $w_\lambda(q)$ / $w_\lambda(1)$ makes conflation tempting. We avoid it.

  **Concrete $H_3$ values at $q = 1$** (Jones-normalised $V / [2]_q^{c-1}$ convention of [`prop:borromean-markov-trace-closed-form`](../mass-theory/borromean-markov-trace-closed-form.md) and [`prop:h3-markov-wenzl-weights`](../mass-theory/h3-markov-wenzl-weights.md)):

  | $\lambda$ | $d_\lambda$ | $y_\lambda(1)$ | $w_\lambda(1)$ | $\mu_\lambda(1)$ |
  |---|---|---|---|---|
  | $(3)$ | $1$ | $1/2$ | $1/6$ | $0$ |
  | $(2,1)$ | $2$ | $1/4$ | $2/3$ | $2 \hbar_q^2$ |
  | $(1^3)$ | $1$ | $0$ | $1/6$ | $0$ |
  | sum identity | — | $\sum y_\lambda d_\lambda = 1$ | $\sum w_\lambda(1) = 1$ | (no sum) |

  The $y_\lambda$ vector $(1/2, 1/4, 0)$ is not uniform and $y_{(1^3)} = 0$ identically (Temperley–Lieb quotient — Jones factors through TL). The Wenzl-bridge $y_\lambda = w_\lambda(q)$ fails at $\lambda = (2,1)$ here ($1/4 \neq 2/3$) because the bridge identity uses a different (non-Jones, Schur-element) normalisation of $y_\lambda$. They coincide on the self-conjugate stratum after matching normalisation conventions. When in doubt, we cite the source proposition.
- **$\check{q}$** (q-háček, meaning "little hook" in Czech) = spinor information rate, $\check{q} = q^{1/2}$, $\check{q}^2 = q$. This is the eigenvalue of the elementary half-twist on the spin-½ fundamental rep of $\mathrm{SU}_q(2)$. We reserve it exclusively for this purpose. The háček diacritic encodes the relation $\check{q}^2 = q$ in the glyph, making every occurrence self-documenting. The relation to $q$ is exactly analogous to $i$ vs $-1$. The spinor rate $\check{q}$ opens up the 2-D spinor (spin-½) representation from the 1-D adjoint (spin-1) representation. Older text writes $r$ for this; we reserve $r$ for radius / generic-real contexts. We never use $r$ or $t$ for $q^{1/2}$ ($t$ clashes with the $V_K(t)$ knot variable and with time-like usage). We reserve $\iota$ for involution / inclusion.
- **$u$** = LP shadow-price $u_\lambda, u_0$ (Schrijver convention for operator-selection LP dual variables, see Table 3 row 15) or the $Q_\beta$ precision-ladder step variable $u_{\text{ladder}} = b\,\hbar_q^2$ with $Q_\beta = Q_{\text{base}} \prod_k (1 + c_k\,u_{\text{ladder}}^k)$, $b$ the Hoefsmit coupling and $\hbar_q = (q-1)/q$. At $q_0$, $u_{\text{ladder}} \approx 0.00852$. We do not use the Habiro convention $u = q^{1/2}$. We write the Habiro-ring expansion as $\mathrm{tr}_M = \sum_m a_m(\check{q})\,(\check{q};\check{q})_m / D(\check{q})$ with $\check{q}$ the spinor rate above. When a compute script uses BOTH the ladder step and either the LP shadow-price $u_\lambda$ or the older Habiro $u$, the ladder variable must be spelled `u_ladder` to keep contexts unambiguous. Single-context scripts may keep bare `u` when an in-script comment annotates which meaning applies (`u = sqrt(q)` for Habiro-facing scripts is permitted when accompanied by `# = \check{q}, spinor rate` annotation).
- **"Borel"** = three unrelated senses, never to be cross-linked: (i) the Lie-theoretic **Borel subalgebra** (Armand Borel) of the $q$-oper chapter ([`def:q-oper`](../q-geometric-langlands/q-oper.md)); (ii) the K-theoretic **Borel regulator** (Armand Borel, 1977) of [`prop:borel-partial-resolution`](../appendix-surreals/borel-partial-resolution.md) and [`conj:borel-zagier-qou-volumes`](../predicted-spectra/borel-zagier-qou-volumes.md) — the only "Borel" in the definition index before 2026-07; (iii) **Écalle–Borel resummation** (Émile Borel) — the Borel transform $\mathcal{B}$, lateral/median Laplace–Borel sums, alien derivatives $\Delta_\omega$ ([`def:ecalle-borel-resummation`](../appendix-surreals-archimedean/ecalle-borel-resummation.md)). Resummation statements bear neither on regulator transcendence (ℚ-linear independence of volumes) nor on flag/oper data; conflating the senses is a notation violation.
- **$\ell$** = Wenzl principal-specialisation length (number of points in $s_\lambda(1, q^2, \ldots, q^{2(\ell-1)})$). Older text writes $r_W$ for this quantity.
- We do not use numerical $q \approx 1.110$ (or any specific value of the substrate parameter) outside the introduction, Chapter 8 (Information Theory, for falsifiability computations), and Chapter 11 (Observations). Geometry chapters use symbolic $q$.

**Approximation convention (derived / observed values).** Numerical values derived from the substrate parameter $q_0$ or compared to experimental data use $\approx$ (or $\simeq$), never $=$, unless an explicit error term is present. Exact algebraic identities (e.g. $c_q = 1/(q-1)$) use $=$ since they hold for all $q$.

**Hecke–Skein convention.** The Hecke algebra generator is $\sigma_i$ (never $T$, never $t$ or $A$ for the Jones polynomial variable). The Iwahori–Hecke algebra $H_n(q)$ is presented as a quotient of the braid group algebra of $B_n$. We use the same symbol $\sigma_i$ to denote both the braid-group generator and its image in $H_n(q)$. Context disambiguates. The Jones polynomial is always $J_K(q)$, not $V_K(t)$. The letter $J$ is shared with the Hahn–Exton q-Bessel function $J_\nu^{(3)}(x;q)$ (substrate harmonic analysis, the $\mathrm{SU}_q(2)\to E_q(2)$ contraction) and the ordinary Bessel weights $J_n(x)$ of the Jacobi–Anger expansion. We disambiguate these by their subscript. We use a knot/link $K$ for the Jones polynomial, and an order $\nu$/$n$ (always with an argument $x$, and the $(3)$ superscript for Hahn–Exton) for Bessel. We never write bare $J$.

**Categories vs CPT operators.** We typeset categories in bold, $\mathbf{C}$, $\mathbf{Rep}$, etc. We reserve the calligraphic $\mathcal{C}$ for the charge-conjugation operator in CPT discussions (parity $\mathcal{P}$, time-reversal $\mathcal{T}$, combined $\mathcal{CP}$, $\mathcal{CPT}$). Calligraphic $\mathcal{C}$ never denotes a category in this paper. Readers should parse a calligraphic $\mathcal{C}$ in context as a discrete symmetry operator. The $\mathcal{P}$ / $\mathcal{T}$ / $\mathcal{CP}$ companions are likewise CPT operators. They do not collide with any categorical or geometric reservation.

**Dirac bra–ket $\lvert \psi \rangle$ / $\langle \phi \vert \psi \rangle$.** The framework's states are objects and morphisms of $\mathbf{C}$ and vectors of its Hecke modules. The native scalar-valued form is the Frobenius pairing, written in comma form $\langle x, y\rangle_F$. We write matrix elements as $\langle v, \Phi v\rangle_F$, never $\langle v \vert \Phi \vert v\rangle$. We write seminormal / Young basis vectors as $v_T$ (SYT $T$) or $v_c$ (channel $c$), never kets $\lvert T \rangle$, $\lvert \psi_N \rangle$. We reserve bra–ket notation for quoted standard-QM material only. A ket carrying framework-native mathematics is a notation violation.

**Base ring convention (Lean).** In Lean source, the generic ground ring is $R$ with the weakest typeclass that admits the construction (`[CommRing R]`, `[Field R]`, `[GroupWithZero R]`, etc.). We use the real numbers $\mathbb{R}$ only past the archimedean wall — specifically, when the declaration genuinely needs `Real.sqrt`, `Real.rpow`, `Real.cos`, `Real.exp`, `Real.log`, an ordering predicate (`0 < q`), `linarith`, or a CODATA / experimental numerical value. Categorical content, algebraic identities, q-deformation combinatorics, and Wenzl / Hecke / Hoefsmit structural data all live over generic $R$. The narrative side mirrors this. We write $q \in R$ for the substrate parameter when only the algebraic structure matters, and $q \in \mathbb{R}$ only when an archimedean evaluation is under discussion.

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

The category $\mathbf{Arch}$ is the target of $\tau$, not the name of a functor. When authoring, we say which one: "$\tau$ specialised to $\mathbf{Arch}$" or "the $R \mapsto \mathbb{R}$ realisation". We never write "the archimedean realisation" without context.

**Pinning $\tau$'s codomain — one functor, several de-enriched levels.** The canonical fibre functor is $\tau \colon \mathbf{C} \to \mathbf{Arch}$. Where $\tau$ is written into a *different* target, it means a **composite** with $\tau$, not a rival functor:

| Written as | Means | Level |
|---|---|---|
| $\tau \colon \mathbf{C} \to \mathbf{Arch}$ | the fibre functor itself | enriched (canonical) |
| $\tau \colon \mathbf{C} \to \mathbf{Vec}_{\mathbb{R}}$ | $U \circ \tau$ | forget archimedean enrichment |
| $\tau \colon \mathbf{C} \to \mathbf{Type}$ (Lean `C ⥤ Type*`) | underlying set-valued functor (Tannakian $\omega$) | forget linear structure |
| $\tau \colon \mathbf{C} \to \mathbf{D}$ (spatial realisation) | $\tau$ into a chosen geometric model $\mathbf{D}$ | model-specific |

These are genuine functors (they act on morphisms). What is **not** a functor is the archimedean **evaluation** $\pi_\infty \colon \mathrm{Obj}(\mathbf{Arch}) \to \mathbb{R}$ (an object-level map / place), and the *ring-level* realisations it induces: the motivic measure $\mathcal{R}_{\mathrm{top}} \colon K_0(\mathrm{Var}) \to \mathbb{R}$ (a ring homomorphism) and the standard-part map $\mathrm{st} \colon \mathbf{No}_{\mathrm{fin}} \to \mathbb{R}$ (a ring homomorphism). Reserve "functor" for $\tau$, $U$, and $\mathrm{St}$; call the maps into $\mathbb{R}$ *realisations / evaluations*.

**"Forgetful functor $\tau$" (classical usage) — a synonym, not a clash.** The core definition blocks write "the **forgetful functor** $\tau$" (e.g. *a QOU is a $(\mathbf{C}, A, \tau)$ with the forgetful functor $\tau$ **faithful***; `def:quantum-observable-universe`), and `tau-notation.md` names $\tau$ "the forgetful functor". This is the **classical Tannakian name**: for $\mathbf{C} = \mathbf{Rep}(U_q\mathfrak{sl}_2)$ the fibre functor and the forgetful functor are the *same* functor $\tau$ — the one $\mathbf{C} \to \mathbf{Mod}_R$ that forgets the coaction, keeping the underlying module. In the enriched register above that classical $\tau$ is the composite $U \circ \tau \colon \mathbf{C} \to \mathbf{Vec}_{\mathbb{R}}$ (row 2 of the previous table); the faithfulness axiom is a statement about this underlying-module level. So "**forgetful functor $\tau$**" and "**fibre functor $\tau$**" name the **same genuine functor** at different codomain levels — the only *distinct* forgetful arrow is the intermediate $U \colon \mathbf{Arch} \to \mathbf{Vec}_{\mathbb{R}}$. This is naming synonymy, **not** a functor-vs-map error: $\tau$ is a genuine functor under either name, so the core-block wording needs no change.

**Binding-energy notions $B_\bullet$.** The framework accumulates many distinct "binding energy" objects, almost all written as a bare $B$ or $B(K)$. We keep binding as plain $B$ with systematic subscripts. The kept canonical symbols:

| Symbol | Definition | Role | Status |
|---|---|---|---|
| $B_{\mathrm{AME}}$ | AME 2020 measurement | experimental ground truth | anchor |
| $B_{\mathrm{sym}}$ | $-\alpha \ln\lvert\mathrm{tr}_M(K)\rvert$ (log-trace) | **exact** symbolic, light $A$ | kept |
| $B_{\mathrm{qCLT}}$ | $-\alpha \sum_i \ln\lvert V_i\rvert$ | qCLT asymptotic, $A\to\infty$ | kept |
| $B_{\mathrm{lin}}$ | $Q_\beta(n)\,(\mathrm{tr}_M(W_{\text{free}}) - \mathrm{tr}_M(W_{\text{atom}}))$ | **linear-truncation** production | canonical compute |
| $B_{\mathrm{depth}}$ | $\sum_k \alpha_k \Phi_k$ | depth-stratified tower | default; empirical $\alpha_k$ |
| $B_{\mathrm{magic}}$ | $2\,m_e A\,\mathrm{Vol}(L6a4)$ (⁴He) | flat magic-$A$ | ⁴He canonical |
| $B_\lambda$ | $m_e \sum_\lambda y_\lambda \chi^\lambda \Delta_\lambda$ | per-partition | open (the $\Delta_\lambda$ magnitude) |

**Critical distinction — $B_{\mathrm{sym}}$ (exact) vs $B_{\mathrm{lin}}$ (linear).** $B_{\mathrm{lin}}$ is the linearization of $B_{\mathrm{sym}}$ (Kashaev $\mathrm{tr}_M \sim \exp(\mathrm{Vol})$; the scalar $\Delta\mathrm{tr}$ is the first-order term). They are NOT interchangeable. Their ratio is the binding deficit
$$ B_{\mathrm{sym}} / B_{\mathrm{lin}} \;\approx\; q_0^{\,5(2A-1)}, $$
i.e. the $\Delta_\lambda = B_{\mathrm{AME}}/B_{\mathrm{lin}}$ residual. We always subscript $B$. A bare $B$ in prose denotes the production $B_{\mathrm{lin}}$.

## Mass: endomorphism $\mathcal{M}$ vs element $\Phi_{\mathrm{mass}}$ vs functional $\mathfrak{m}$

The phrase "mass endomorphism" names **three** distinct objects across the mass
chapter. They must not be conflated: only the first is an endomorphism, only the
third is the observable.

| Symbol | Object | Type | Name to use |
|---|---|---|---|
| $\mathcal{M}(K)$ | the **endomorphism** of the knot object | $\mathrm{End}_{\mathbf{C}}(X_K)$, i.e. $X_K \to X_K$ | **mass endomorphism** |
| $\Phi_{\mathrm{mass}}(\beta)$ | the **Hecke mass element** | an element of $H_n(R, q)$ | **Hecke mass element** (never "endomorphism") |
| $\mathfrak{m}(\varrho)$ | the observable mass | a scalar $\lvert\mathrm{tr}_M(\rho(\beta))\rvert\cdot\mathrm{VolDensity} \in \mathbb{R}$ | **categorical mass functional** |

- **Reserve "mass endomorphism" for $\mathcal{M}(K)$.** It is a genuine
  endomorphism only in the Reshetikhin–Turaev **long-knot (1–1 tangle)** sense
  \cite{reshetikhin1991, turaev2010}: a long knot is $V \to V$; **closing** it
  (Markov trace) lands in $\mathrm{End}_{\mathbf{C}}(\mathbf{1}) = k$, a scalar.
- **$\Phi_{\mathrm{mass}}(\beta) \in H_n(R, q)$ is an element, not a map.** It
  *is* an endomorphism of $V^{\otimes n}$ via $q$-Schur–Weyl
  $H_n(q) \cong \mathrm{End}_{U_q\mathfrak{sl}_N}(V^{\otimes n})$
  \cite{jimbo1986}, or via the faithful left-regular map
  $a \mapsto L_a \in \mathrm{End}_R(H_n)$ \cite{kock2004} — but say which; do not
  write "$\Phi_{\mathrm{mass}}$ is the mass endomorphism" bare.
- **$\mathfrak{m}$ is a functional, not an endomorphism.** The Markov trace
  $\mathrm{tr}_M \colon H_n \to R$ is a trace functional \cite{jones1987,
  geckpfeiffer2000}; the modulus collapses $\mathcal{M}$ to a number. Note
  $\mathrm{tr}_M(a) \neq \mathrm{tr}(L_a)$: the Markov trace is the *quantum*
  trace, not the regular-representation trace.

**Convention — $\mathcal{M}$ = endomorphism; the mass functional is $\mathfrak{m}$.** The glyph $\mathcal{M}$ is overloaded **three** ways in the literature and in earlier text, which is forbidden here:

| Sense | Object | Type | Canonical glyph |
|---|---|---|---|
| **mass endomorphism** | $\mathcal{M}(K)$ (complex-volume block, $\mathfrak{V}$ entry) | $\mathrm{End}_{\mathbf{C}}(X_K)$ | **$\mathcal{M}$** (keep) |
| **mass functional** | Skein-module map $\mathrm{Sk}_q\to\mathbb{R}_{\geq0}$ (evaluates a knot class to its mass) | functional | **$\mathfrak{m}$** (migrate ← $\mathcal{M}$) |
| **scattering amplitude** | transition matrix element $\lvert\mathcal{M}_q\rvert^2$ (e.g. [`trace-ratio-observable`](../observations/trace-ratio-observable.md)) | scalar amplitude | **$\mathcal{M}_q$** (distinct; unaffected) |

Convention: reserve $\mathcal{M}$ (calligraphic operator) for the **endomorphism**; the Skein **functional** becomes $\mathfrak{m}\colon\mathrm{Sk}_q\to\mathbb{R}_{\geq0}$ (fraktur observable register, matching the mass scalar $\mathfrak{m}$ it outputs); the QFT **amplitude** $\mathcal{M}_q$ keeps its subscripted glyph. The Skein-module entry above is updated to $\mathfrak{m}$ accordingly.

> **Scope of the convention.** The rename applies to the functional sense only. The
> amplitude sense $\lvert\mathcal{M}_q\rvert^2$ and the endomorphism sense
> $\mathcal{M}(K)$ keep $\mathcal{M}$, so the two must be distinguished case by
> case rather than by a blanket substitution; some earlier text still uses
> $\mathcal{M}$ in the functional sense.

## Quantum dilogarithm: $\Phi_q$ (compact) vs $\Phi_b$ (Faddeev non-compact)

Two distinct functions were historically both called "Faddeev $\Phi_q$",
which is **forbidden**:

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
- **Residual collision.** A few Askey-two-saddle passages write the single
  glyph "$\Phi_q$" where context makes clear the non-compact regulator is
  meant. That collision is unresolved: no distinct glyph is reserved for it
  here, so disambiguate from the surrounding prose.

## Photon $\gamma$ vs the unknot $0_1$

The photon and the unknot are **different objects** and must never be
identified:

| Object | Symbol | Particle | Never write |
|--------|--------|----------|-------------|
| Empty knot / identity element (trivial Hecke representation; empty braid word, zero crossings, bar-invariant) | $\varnothing$, $\mathbf{1}$, $T_e$ | **photon** $\gamma$ | "the photon is the unknot" |
| Unknot (closed single strand, crossing number 0) | $0_1$ | **neutrino** $\nu$ | "the unknot is the photon" |

The photon is the trivial knot **representation** — the identity element of
$H_n(R, q)$, with no closed strand at all. The unknot $0_1$ is a **closed
strand** and represents the neutrino. The closure of the photon's identity
word on $n$ strands is $n$ disjoint unknots; describing that *closure* as
disjoint unknots is correct, but assigning the single unknot $0_1$ to the
photon as its knot identity is a canon violation. Authoritative statements:
[`two-photon-pair-production.md`](../particle-interactions/two-photon-pair-production.md)
("the photon $\gamma$ is the empty knot $\varnothing$ … distinct from the
unknot $0_1$ representing the neutrino") and the atlas registry
([`recursive-atom-knot-atlas-registry.md`](../appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md):
"the bare photon (identity $\mathbf{1}$, not the unknot)").

## Bar-even / bar-odd: always the coefficient half

The words **bar-even** and **bar-odd** label four different gradings in this
paper. They are not four involutions. All four descend from the single
[`def:bar-involution`](../braids-and-knots/bar-involution.md) on $H_n(q)$,

$$
  \overline{\sigma_i} = \sigma_i^{-1}, \qquad \overline{q} = q^{-1},
$$

which has **two halves that blocks apply independently**:

| Half | Acts by | Geometrically |
|---|---|---|
| **coefficient half** | $q \mapsto q^{-1}$, diagram fixed | reciprocates the weights |
| **diagram half** | $\sigma_i \mapsto \sigma_i^{-1}$, coefficients fixed | the **mirror**: exchanges positive and negative crossings, $p \leftrightarrow m$ |

**Convention.** In this paper *bar-even* and *bar-odd* always mean parity
under the **coefficient half**. A parity taken under the diagram half is
called **mirror-even** / **mirror-odd**, never "bar-". Which grading is meant:

| | Splits | Graded by | Where |
|---|---|---|---|
| **A** | the Laurent scalar $\mathfrak{E}_{\mathrm{cross}}$ into $\cosh\lambda$ / $\sinh\lambda$ | coefficient half | [`obs:crossing-energy-decomposition`](../observations/crossing-energy-decomposition.md) |
| **B** | the Hecke module into $e_+$ / $e_-$ by eigenvalue $q$ / $-q^{-1}$ | **neither** — the full involution *fixes* both idempotents | [`prop:em-coupling-projection`](../predicted-spectra/em-coupling-projection.md) |
| **C** | the knot, by the mirror; the channel totals $E_{\mathrm{sym}}$ / $E_{\mathrm{asym}}$ | diagram half | same block as A, item 2 |
| **D** | the algebra $A = A_+ \oplus A_-$ by the spin involution | coefficient half | [`def:spin-involution`](../mass-theory/spin-involution.md) |

**A and D are the same grading.** On the symmetric/alternating Hecke block the
spin involution acts as the eigenvalue swap $q^{2k} \leftrightarrow q^{-2k}$,
which is exactly the coefficient half; its sectors are $A_+ = \cosh(2k\lambda)$
and $A_- = \sinh(2k\lambda)$. So $A_+$ bar-even and $A_-$ bar-odd agrees with
$\cosh\lambda$ bar-even and $\sinh\lambda$ bar-odd, and the shared vocabulary
is consistent rather than colliding.

**C is anti-correlated with A, and this is not an error.** The weight
$\cosh\lambda$ is bar-even, while its channel total
$E_{\mathrm{sym}} = (p - m)\cosh\lambda$ is mirror-**odd**, because the mirror
flips the multiplicity $p - m$ as well as the weight. Both statements hold of
the same summand; only the half differs. Read a parity claim about a *weight*
as coefficient-half and a parity claim about a *channel total* as diagram-half
unless the text says otherwise.

**Never say "bar-even" unqualified of a channel.** Under the full involution
both crossing-energy channels are negated, and both Hecke idempotents are
fixed, so the words separate nothing there. They are informative only relative
to a named half. Proved sorry-free over a general field in
[`QOU.BraidKnot.CrossingEnergyBarParity`](../lean/QOU/BraidKnot/CrossingEnergyBarParity.lean)
(`eSym_coef`, `eSym_mirror`, `bar_neg_of_both`); the full atlas including
gradings B and D is
[`bar-parity-involution-atlas.witness.json`](../../../computations/bar-parity-involution-atlas.witness.json).

**Four different objects wear the glyph $\sigma$** — the Hecke generator
$\sigma_i$, the mirror $K \mapsto K^{\sigma}$, the spin involution
$\sigma : A \to A$, and the bar involution itself, which several blocks write
as $\sigma \colon q \mapsto q^{-1}$. A bare $\sigma$ therefore never
disambiguates a parity claim; name the half instead.

That last usage carries its own hazard: writing the bar involution as
"$\sigma \colon q \mapsto q^{-1}$" states only the **coefficient half**, and a
reader who takes it as the definition will compute the wrong parity for
anything living inside $H_n(q)$. Three corpus claims have been caught by
exactly this slip: the crossing-energy channels and the $V_\lambda
\leftrightarrow V_{\lambda'}$ intertwiner (which is the sign twist $\sigma_i
\mapsto -\sigma_i^{-1}$, not the bar involution) are corrected here, and the
argument from bar-invariance for the Markov parameter $z$ is withdrawn — its
bar-partner is $z - h$, not $z$, because M3 contains $\sigma_n$. (The $z$
*convention* is settled independently of this: convention D, $z = q^3/(q^2+1)$,
is canonical and C is excised; see
[`def:markov-axioms-primitive`](../braids-and-knots/markov-axioms-primitive.md).)
When the object being graded lies in the algebra, use both halves.

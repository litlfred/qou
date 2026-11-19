A handful of common letters carry overloaded meanings in the literature. The following conventions disambiguate them throughout this paper:

- **$c$** = color (never charm; charm is $\mathfrak{c}$).
- **$b$** = generic variable (never bottom quark; bottom is $\mathfrak{b}$).
- **$p$** = brane point (never proton number; proton number is $Z$).
- **$E$** alone = not used for an exceptional divisor, energy, or elliptic curve; those are written $\mathcal{S}_p$, $\mathfrak{E}$, or $\mathcal{E}_q$ respectively. $E_{\mathfrak{H}}$ (with hadron subscript) is allowed for crossing energy.
- **$\mathfrak{E}$** bare = the energy $\mathfrak{m}\,c_q^2$ of a braid class ([energy](#def:mass-energy)). Every other energy carries a subscript: $\mathfrak{E}_{\mathrm{cross}}$ (crossing energy, which is a different quantity), $\mathfrak{E}_0$, $\mathfrak{E}_{\mathrm{bind}}$, $\mathfrak{E}_{\gamma}$, $\mathfrak{E}_{\mathrm{pole}}$. The Euler–Lagrange operator is $\mathrm{EL}$.
- **$\mathfrak{E}_0$ vs $Q_\beta(n)$**: two distinct hadronic-sector scalars that are not interchangeable:
    - $\mathfrak{E}_0$ = hadronic energy scale, given at leading order by $\mathfrak{E}_0^{(N=0)} = m_e/(q_0(q_0-1)) \approx 4.186$ MeV (CAL-1 and CAL-2 only). The tower-summed form is $\mathfrak{E}_0^{\text{full}} = \mathfrak{E}_0^{(N=0)}/(1-\hbar_q^2) \approx 4.228$ MeV. It sets the MeV-per-dimensionless-trace-unit conversion for hadronic predictions.
    - $Q_\beta(n) = 0.78233341\,\text{MeV}$ = the free-neutron $\beta$-decay $Q$-value, determined from CAL-2 ($P_{\mathrm{skew}}^{\beta}$). It enters as the binding-energy-scale multiplier in [categorical Markov mass](#prop:categorical-mass-markov) via the explicit binding formula $B = Q_\beta(n) \cdot (|\mathrm{tr}_M(W_{\text{free}})| - |\mathrm{tr}_M(W_{\text{atom}})|)$.
  The ratio is $\mathfrak{E}_0/Q_\beta(n) = 1/|\Delta(\mathrm{net})| \approx 5.31$ (the dimensionless Hecke normal-form reduction). Using $\mathfrak{E}_0$ for a $Q_\beta$-valued binding-scale variable is a registered notation violation.
- **$\gamma$** = three reserved meanings, all standard, disambiguated by context: (i) the photon (default reading in particle / QED contexts: pair production $\gamma\gamma \to e^+ e^-$, photonic channels, Breit–Wheeler vertices); (ii) the Euler–Mascheroni constant (only inside zeta-value identities, e.g. $\zeta'(0) = -\tfrac{1}{2}\log(2\pi)$, $\gamma = \lim(H_n - \log n)$); (iii) Dirac matrices $\gamma^\mu$ (always with an explicit Lorentz index). Never write $\gamma$ for a vortex or closed cycle; the vortex morphism is $\varrho$.
- **$c_k$ vs $\mathrm{cl}_k$**: the letter $c$ distinguishes **four** related or adjacent coefficient families:
    - $c_k$ = **Q$_\beta$ precision-ladder** coefficients only, $Q_\beta = Q_{\text{base}}\prod_k(1 + c_k u^k)$ with $u = b\hbar_q^2$ (dimensionless, $c_2 = -1$, $c_3 = -2$ a near-match). (This register fixes the *symbol*; each rung's epistemic tier and convention scoping belong to the $c_k/d_k$ canonical registry. Here $c_2$ is the exact $u^2$ coefficient of the explicit-factor product $\prod_{k\ge2}(1 + c_k u^k)$, whereas $\tilde c_2 = -9/8$ is the quadratic coefficient of the normalised series with the cosine factor inside; always state *which series* is meant.)
    - $\tilde c_k$ = the **normalised-series** coefficients of the *same* ladder model: the $u^k$ coefficients of $\Phi(u)/\Phi(0)$ rather than of the explicit factors. The tilde marks a **different normalisation of the same object**. The two families are **not** interchangeable: the model's cosine factor contributes at every order, and $\tilde c_2 = c_2 - 1/8$ holds identically, independently of the phase $\alpha$, so $c_2 = -1$ corresponds to $\tilde c_2 = -9/8$. **Both are valid**: one model at two normalisations, with the $-1/8$ shift contributed entirely by the half-argument in $\cos(\alpha - u/2)$.
    - $c_k^{\mathrm{even}}$ = the **bar-even part** of the ladder data, lying in $\mathbb{Q}(\sqrt 3)$, a third object distinct from both $c_k$ and $\tilde c_k$.
    - $\mathrm{cl}_k$ = **cluster / Ursell coefficients** of the many-body expansion (MeV-valued). $\mathrm{cl}_3 = -\mathfrak{E}_0\,\Delta^2 g$ is the three-body cluster coefficient of the $\mu_3$ door ($\mu_3 > 0 \iff \Delta^2 g < 0$), and the Borromean H$_9$ magnitude lift belongs to the same family.
  Never write a bare $c_k$ for a cluster coefficient, and never quote a $c_k$ value without specifying which of $c_k$ / $\tilde c_k$ / $c_k^{\mathrm{even}}$ is meant; the three differ at the same $k$ ($-1$, $-9/8$, $\approx -7.4588$ at $k = 2$). Every single Roman letter is either register-claimed or produces a same-domain case-collision ($X_k$ vs the knot object $X_K$; $Y_k$ vs the Markov weight $y_\lambda$; $Z$ = proton number; $W_\lambda$ = geometric weight; $j$ vs the Jones polynomial $J_K(q)$). This motivates the roman two-letter tag $\mathrm{cl}_k$, analogous to $\mathrm{Sk}$ (Skein module) and $h_{\mathrm{A}}$ (Hecke amplitude).
* **$\chi_q$** = Lyapunov exponent (distinct from $\chi_\zeta(c)$, the character).
* **Euler characteristic is $\chi_{\mathrm{eu}}$, never a bare $\chi$.** The glyph $\chi$ is shared by three register-claimed families: the **characters** $\chi_\lambda$ (Frobenius pairing $\mathrm{tr}_M = \sum_\lambda y_\lambda \chi_\lambda$) and $\chi_\zeta(c)$; the Lyapunov exponent $\chi_q$ above; and the **Euler characteristic**, which keeps the standard glyph with the roman subscript: $\chi_{\mathrm{eu}}$. A bare $\chi$ is a notation violation in all three senses. When a total and its strata both appear, additional subscripts distinguish them: $\chi_{\mathrm{eu}}(M)$ for the whole moduli, $\chi_{\mathrm{eu},i}$ for the $i$-th Behrend stratum. A Donaldson–Thomas count is a *Behrend-weighted* Euler characteristic $\sum_i n_i\,\chi_{\mathrm{eu},i}$, whose unweighted total $\sum_i \chi_{\mathrm{eu},i} = \chi_{\mathrm{eu}}(M)$ is a different number. (Write $\chi_{\mathrm{eu}}$, never an uppercase `\Chi`, which is not a standard LaTeX control sequence. The orbifold Euler *number* of $\Sigma(2,3,5)$ keeps its conventional symbol $e = -1/30$.)
- **$-2$ vs $-6$ in the Stokes/DT sector**: two integers that are not the same object and must not be swapped. $\sum_{\lambda \vdash 3} \Delta_\lambda = -2$ is the Wedderburn/Springer partition Euler characteristic and serves as the *prefactor* of the GGM sandwich $A \cdot W_{-1} \cdot B \cdot W_{-1}^{\mathsf{T}} \cdot C = -2\,S^{+}(0)$. The sandwich $(0,1)$ entry is $-6 = (-2)\cdot 3$ (the prefactor times the Stokes/DT **count** $S^{+}(0)_{01} = 3$) and is *not* an Euler characteristic. Cite $-2$ for the Euler characteristic and $3$ for the count.
- **$\mathrm{tr}(\mathrm{id}_A)$ vs topological and sheaf Euler characteristics: four distinct symbols, never interchanged.** [Euler-characteristic stability](#prop:euler-char-stability) relates $\mathrm{tr}(\mathrm{id}_{A_n})$ to $\chi_{\mathrm{eu}}(\mathcal{S}_n)$, while [Bring's Euler characteristic](#lem:brings-euler-characteristic) evaluates $\chi_{\mathrm{eu}}(\Sigma_4) = -6$, [quantum characteristic classes for SU(2)](#ex:quantum-characteristic-classes-su2) evaluates $\chi_{\mathrm{eu}}(\mathbb{CP}^1) = 2$, and [knot-operator selection](#prf:knot-operator-selection) evaluates the fundamental quantum dimension $[2]_q = q + q^{-1} \approx 2.0108968667$ at $q_0$. Unlike the topological invariants summarized in [aether line bundle: base not fibre](#rem:substrate-line-bundle-base-not-fibre), the categorical trace $\mathrm{tr}(\mathrm{id}_X) = \dim_q(X)$ depends on $q$: for $A = \mathcal{O}_q(\mathrm{SU}(2)) \cong \bigoplus_n V_n \otimes V_n^{*}$, the naive sum $\sum_n [n+1]_q^2$ diverges at $q_0 > 1$ (since $[n+1]_q > 0$ grows like $q^n$), requiring $\zeta$-regularisation before $\dim_q(A)$ takes a finite scalar value. Four distinct symbols separate these concepts unambiguously. First, $\chi_{\mathrm{eu}}(M_0)$ is the topological Euler characteristic of the base curve ($-6$ on $\Sigma_4$; [three Euler characteristics](#rem:three-euler-characteristics)). Second, $\chi(M_0, V)$, always with two arguments, is the sheaf Euler characteristic $h^0 - h^1$ of a vector bundle on the base (Hirzebruch–Riemann–Roch; equal to $\chi_{\mathrm{eu}}(M_0)$ when $\mathrm{rk}\, V = 2$ and $\deg V = 0$). Third, $\dim_q(X) = \mathrm{tr}(\mathrm{id}_X)$ is the rigid trace of an object of $\mathbf{C}$, so $\dim_q(V) = [2]_q$ for the fundamental object and $\dim_q^{\zeta}(A) = 0 = \chi_{\mathrm{eu}}(\mathrm{SU}(2))$ under $\zeta$-regularisation ([regular representation](#rem:euler-characteristic-of-the-regular-representation)). Fourth, $w(A)$ is the obstruction class of the [Wigner axiom](#conj:wigner-axiom), whose archimedean image is the Euler class $e(\xi)$. Bare $\chi(A)$ is not used: Hecke characters $\chi_\lambda$ carry a partition subscript, the Lyapunov exponent $\chi_q$ carries $q$, the motivic measure is $\chi_{\mathrm{top}}$, and Euler characteristics carry roman $\mathrm{eu}$ or two arguments.
- **$\theta_p$ vs $\vartheta_K$**: two unrelated objects sharing a glyph. $\theta_p(w) = \sum_{n\in\mathbb{Z}} p^{-n(n+1)/2}w^{n}$ is the $q$-theta of a $q$-difference operator: a function of a complex variable, satisfying $\theta_p(pw) = w\,\theta_p(w)$, whose zero set is the orbit $-p^{\mathbb{Z}}$. $\vartheta_K$ is the **angular** deformation parameter of the volume channel $S_K = A_\omega\,\kappa\,(\ln^{2} q_0 - \vartheta_K^{2})$, a real angle attached to a knot rather than a function. Neither is a Newton-polygon slope; "theta order" in the slope register is a third, again unrelated, use of the word.
- **$\Omega_q$** = the **Reeb period** only. This is one object across two regimes: in the finite categorical model it is the smallest positive integer with $\xi_q^{\Omega_q} = \mathrm{id}_A$ ([categorical Reeb derivation](#def:categorical-reeb-derivation); the divisibility $6 \mid \Omega_q$ is an integer-regime statement only), and at the aether parameter it is the infinite surreal $\Omega_q \asymp \varepsilon^{-1} \asymp \omega$ ([surreal rate calculus](#prop:surreal-rate-calculus)). These are the same period lifted rather than a collision. What is **not** $\Omega_q$: the $q$-deformed **Kerov limit-shape space** (the target of the Plancherel pushforwards $\iota_n$) is $\mathcal{K}_q$ (calligraphic, per the space convention). A topological space is not a period; do not carry $6 \mid \Omega_q$ to $\mathcal{K}_q$ or to the surreal. The $q$-oper datum $\Omega^1_q$ (a differential in the $q$-geometric Langlands chapter) is a superscripted third use and unrelated; its tensor powers keep the superscript, $(\Omega^1_q)^{\otimes 2}$, never a bare $\Omega_q^{\otimes 2}$ (which reads as a power of the period). A fourth use is disambiguated by its **argument**, in the manner of $\zeta(s)$ and $H_q(\lambda)$ above: $\Omega_q(\varrho)$ is the **$q$-holonomy residue** of a loop $\varrho$, an element of $\mathrm{End}(\tau(\mathcal{L}_q))$ fixed by $\mathcal{L}_q(\varrho) = \mathrm{id} + (q-1)\Omega_q(\varrho)$ ([the $q$-local system definition](#def:q-local-system)). It is an endomorphism rather than a number: the divisibility $6 \mid \Omega_q$ does not reach it either. Never write it without its loop argument.
- **$\zeta$** = three distinct uses, never bare: $\zeta_n := e^{2\pi i/n}$ (primitive $n$-th root of unity, always with integer subscript — e.g. $\zeta_5$, $\zeta_6 = e^{i\pi/3}$); $\zeta(s)$ (Riemann zeta function, always parenthesised, e.g. $\zeta(2) = \pi^2/6$, $\zeta(3)$ — Apéry's constant); $\chi_\zeta(c)$ (character, always with $\chi$ prefix and argument). The bare token $\zeta$ is never used alone.
- **$\mathcal{P}_n$** = Goncharov period filtration class (weight-$n$ periods modulo lower-weight). This is distinct from $P_\ell$, the elementary symmetric polynomials in Jucys–Murphy elements ([central Jucys–Murphy elements](#prop:jucys-murphy-central-elements-qou)), which are non-calligraphic and indexed by symmetric-polynomial degree.
- **$H_q$** alone = not used. Three distinct concepts share the letter $H$: $\mathcal{H}_q$ (shuffle Hopf algebra), $\hat{H}_q$ (Hamiltonian operator), $H_n(q)$ or $H_q(\lambda)$ (Hecke / hook-length, always with argument). The Hecke amplitude $q - q^{-1}$ is $h_{\mathrm{A}}$ (plain-italic scalar, roman subscript), avoiding collision with the Hecke algebra $H_A(q)$ on $A$ strands.
- **$W$** alone = not used. Two unrelated objects claim the bare letter: the rank-2 Hodge plane of $H^1(\text{Bring}) = 2W$, which carries the three calibrations ([three-calibration discipline](#rem:three-calibration-discipline-discussion)), and the three-dimensional object with irreducible $\mathrm{Sym}^2$ discussed in [eightfold open problems](#rem:eightfold-open-problems). The first appears only as $2W$ or as the rank-2 $W$-plane, and the second only with its dimension stated explicitly. The decorated forms are separately claimed and are neither of these: $W_\lambda$ (geometric weight), $W(\gamma)$ (abstract Wilson-loop functional; the confinement observable is $\mathfrak{W}$), $W(A_2)$ (Weyl group, always with a root system as argument), and $W_{\text{free}}$ / $W_{\text{atom}}$ (braid words in the binding formula above).
- **$\mathrm{SU}(3)$** alone = permitted only for a representation-theoretic statement true of any $\mathrm{SU}(3)$ (e.g. "$\mathbf{3}\otimes\bar{\mathbf{3}} = \mathbf{8}\oplus\mathbf{1}$ is standard $\mathrm{SU}(3)$ representation theory"). The two physical groups in this paper are distinct and always carry roman lowercase subscripts: $\mathrm{SU}(3)_{\mathrm{c}}$ (colour — the stabiliser $\mathrm{SU}(3)_{\mathrm{c}} \subset G_2 = \mathrm{Aut}(\mathbb{O})$, the colour tubes, the gluon octet) and $\mathrm{SU}(3)_{\mathrm{f}}$ (flavour — the group organising the meson/baryon octets, the decuplet, and quark flavour). Because [the eightfold-way open-problems block](#rem:eightfold-open-problems) asks whether the two are identical, distinct, or groupoid-dual, a shared glyph would presuppose an answer; any comparison carries both subscripts.
* **$\mathfrak{S}$** = categorical action (fraktur, Hamilton's $S$), written $\mathfrak{S}_q$ throughout the paper. This reserves calligraphic $\mathcal{S}$ for the state bundle alone (QOU tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$). Three other objects deliberately keep $S$ / $\mathrm{Sk}$ and are not the action.
    * The Hopf antipode $S$ (plain $S$, or $S_q$ on the $q$-shuffle Hopf algebra).
    * The $q$-entropy $S_q(U)$ (with $\partial S_q/\partial \mathfrak{E}_q = 1/T_q$) and the Bekenstein–Hawking entropy $S_{BH}$, which is a distinct thermodynamic observable.
    * The Skein module $\mathrm{Sk}_q(\mathbf{C})$ — the $\mathbb{Z}[q^{\pm 1}]$-algebra of knot classes, with mass functional $\mathfrak{m}\colon \mathrm{Sk}_q \to \mathbb{R}_{\geq 0}$ (fraktur; calligraphic $\mathcal{M}$ is reserved for the mass *endomorphism* $\mathcal{M}(K)\in\mathrm{End}_{\mathbf{C}}(X_K)$ below), written roman $\mathrm{Sk}$ to avoid colliding with $\mathcal{S}$ (state bundle) and $\mathcal{K}$ (knot).
* **$\mathfrak{O}$** denotes the observation / intent morphism — the section $(\mathfrak{O}, \epsilon)$ of $\mathrm{Ad}(J^1\mathcal{S})$ and its germ endomorphism $\mathfrak{O}_p$, never used for an ideal. The genus-filtration ideal keeps $\mathfrak{I}$ ($\mathfrak{I}_4 = (u^5)$).
- **$\mathfrak{W}$** = confinement observable / $q$-Wilson loop $\mathfrak{W}(\mathcal{K}, \mathcal{T})$, never used for the observation morphism $\mathfrak{O}$. The abstract Wilson-loop functional is plain $W(\gamma)$, distinct from $\mathfrak{V}$ below.
- **$\mathbb{M}_{n,q}$** = the **$q$-Plancherel measure** on partitions of $n$, $\mathbb{M}_{n,q}(\lambda) = q^{n(\lambda)} f^\lambda / \prod_\square \{h(\square)\}_q$ with the *asymmetric* $q$-integers $\{k\}_q = (q^k-1)/(q-1)$ ([the $q$-Plancherel asymptotic skeleton](#prop:q-plancherel-asymptotic-skeleton)). Blackboard bold matches the source literature and avoids plain $M$ ($\chi_{\mathrm{eu}}(M)$) and calligraphic $\mathcal{M}$ (mass endomorphism). **Three distinct quantities are NOT this measure and must not be written $\mathbb{M}$:** the Wedderburn weight $w_\lambda = \dim_q^2/[n]_q!$ (which differs from $\mathbb{M}_{n,q^2}$ by a relative factor of $978$ at $n=12$ and is unnormalised), the Markov weights $y_\lambda$, and the Markov trace $\mathrm{tr}_M$. Note also that $n(\lambda) = \sum_i (i-1)\lambda_i$ is Macdonald's statistic rather than a function of the size $n$. The Molien / fake-degree weight coincides with $\mathbb{M}_{n,Q}$ at $Q = q^2$ (by the Molien–Féray–Méliot fake-degree identity), so neither transfers to $w_\lambda$.
- **$\mathfrak{V}$** = the complex-volume observable (analogue of the Neumann–Zagier complex volume $\mathbb{V}=\mathrm{Vol}+i\,\mathrm{CS}$): $\mathfrak{V}(K) = E_0\,\mathrm{tr}_M((\Pi_{\text{free}}-\mathbf{1})\circ\mathcal{M})$. Its real part is binding $\mathfrak{E}_{\mathrm{bind}} = \mathrm{Re}\mathfrak{V}$ (bar-even / $\cosh$) and its imaginary part is the $\beta$-decay $Q$-value $\mathfrak{Q}_\beta = \mathrm{Im}\mathfrak{V}$ (bar-odd / $\sinh$) ([the binding--$\mathfrak{Q}_\beta$ complex-volume conjecture](#conj:binding-qbeta-complex-volume)). Neither $\mathfrak{W}$ (Wilson loop) nor $\mathbb{V}$ (the Neumann–Zagier symbol) is used for this observable.
- **$\Pi_{\text{free}}$** = idempotent projector onto the factorized sub-object (parabolic/Young subalgebra; constituents un-linked). The "free" trace is $\mathrm{tr}_M\circ\Pi_{\text{free}}$.
- **$\mathfrak{Q}_\beta$ (fraktur)** = the $\beta$-decay $Q$-value as a *trace-component* ($\mathrm{Im}\mathfrak{V}$, derived) in the fraktur observable register; the experimental value is written $\mathfrak{Q}_\beta^{\,\mathrm{obs}}$.
- **$\mathfrak{D}$ (decay width) vs $\mathcal{D}$ (operator)**: visually close but register-distinct. Fraktur $\mathfrak{D}$ (a decay-rate observable) always carries a decay subscript ($\mathfrak{D}_n$ for neutron, $\mathfrak{D}_\mu$ for muon, $\mathfrak{D}_K$ for generic hadron) under the convention $\mathfrak{D}_K = \hbar/\tau_K$. The calibration channels $P_{\mathrm{skew}}^{\beta}$ (CAL-2) and $P_{\mathrm{avg}}^{\pi}$ (CAL-3) are bar-parity projections rather than rates, with $Q$-value and mass proxies respectively. Calligraphic $\mathcal{D}$ denotes the categorical Dirac operator $\mathcal{D}_\nabla$ or the path measure $\mathcal{D}\phi$. Bare $\mathfrak{D}$ and bare $\mathcal{D}$ are never used.
- **$S_n$ vs $H_n(q)$**: $q$-deformed braiding decompositions (eigenvalues $\{q, -q^{-1}\}$) are actions of the Iwahori–Hecke algebra $H_n(q)$, not the symmetric group $S_n$, even when the block dimensions match the classical $S_n$ irreps. Classical $S_n$ denotes only a genuine $\epsilon = \pm 1$ permutation action, and fraktur $\mathfrak{S}_n$ is never used ($\mathfrak{S}$ is the action).
* **"Depth"** covers **six** distinct filtration/cutoff indices; bare "depth" is never written, and each sense carries its own symbol and full qualifier on first use.
    * **Transcendence depth** $n$: the iterated-integral index of $\mathcal{H}_q^{(n,K)}$, where $G^{(n)}$ adjoins $\mathrm{Li}_n^q$ and $\tau_{\mathrm{arch}}(G^{(n)}) \subseteq \mathcal{P}_n$. This index is additive under the $q$-shuffle ($\mathcal{H}^{(n_1)} \ast_q \mathcal{H}^{(n_2)} \subseteq \bigoplus \mathcal{H}^{(n_1+n_2)}$) and indexes the $K$-theory period dictionary.
    * **Cell** $\lambda_K \vdash n_K$: the Hecke/knot partition cell of an atom's braid. A partition rather than an integer; write the partition, never "the depth of $K$".
    * **Curvature-rank** $k$: the Gröbner–Shirshov grading index $k = \mathrm{depth}(\lambda) - 1$ with $\mathrm{depth}(\lambda)$ the *partition* depth (maximum hook length).
    * **Cascade depth** $N_{\mathrm{eff}} = \lfloor \log_q(\mathrm{Re}_q^{3/4}) \rfloor$: the $q$-turbulence Reynolds cutoff of the fluid-dynamics chapter, unrelated to algebraic filtrations.
    * **Triangulation size** $n$: the number of ideal tetrahedra in a hyperbolic triangulation of a JSJ piece $K_S$ (for instance, **eight** ideal tetrahedra for $\mathtt{L6a4}$, and **two** ideal tetrahedra with **one** cusp for the figure-eight closure of $(\sigma_1\sigma_2^{-1})^2 \in H_3(q)$). This count is distinct a priori from both the Gröbner–Shirshov $a$-function grade $k_\star(T_w)$ and the transcendence depth $n$; any identification between them (such as the piecewise-linear correspondence referenced in [Thurston relaxation](#sec:thurston-relaxation)) is a conjectural hypothesis rather than a definitional equality. Never write a bare $n$ across these three senses.
    * **Tower depth** $N$: the brane-tower truncation index, as in $\mathfrak{E}_0^{(N)}$ and $N_v = 120\,q_0^{90}$.

  Two further phrases connect to the senses above via specific claims rather than by definition: **normal-form support depth** (equated with Lusztig's $a$-function grade, taking value $\binom{n}{2}$ on $T_{w_0}$, while conjecturally related to tower depth) and **slicing depth** (defined as Coxeter length $\ell(w)$ in the atom-knot dictionary). **"Cyclotomic depth"** and **"Bring-natural depth"** are informal synonyms for transcendence depth.

* **Three partition-weight families** — Markov $y_\lambda$, $q$-deformed Wedderburn $w_\lambda(q)$, and classical Plancherel $w_\lambda(1)$ — are distinct at $q \neq 1$ and coincide only at $q = 1$.
    * $y_\lambda$ is the Jones–Markov central coefficient ($\mathrm{tr}_M = \sum y_\lambda \chi_\lambda$, Wenzl hook–content closed form).
    * $w_\lambda(1) = (\dim V_\lambda)^2 / n!$ is the classical Plancherel probability measure, $\sum_\lambda w_\lambda(1) = 1$.
    * $w_\lambda(q) = \dim_q^2(\lambda) / [n]_q!$ is the $q$-deformed Wedderburn-block weight, $\sum w_\lambda(q)$ finite but $\neq 1$ at $q \neq 1$ ($\approx 1.51$ at $q_0$, $n = 12$).
  **Convention.** $w_\lambda(q)$ denotes the $q$-deformed Wedderburn-block weight, and the classical Plancherel measure is its specialisation $w_\lambda(1)$ ($\dim_q(\lambda) \to \dim V_\lambda$ and $[n]_q! \to n!$ as $q \to 1$). Bare $w_\lambda$ means $w_\lambda(q)$ at the ambient $q$. **Never write a unit-sum claim on bare $w_\lambda$** — $\sum_\lambda w_\lambda(1) = 1$ holds at $q = 1$, whereas $\sum_\lambda w_\lambda(q) \neq 1$ for $q \neq 1$ ($0.987$ at $n = 3$, $1.051$ at $n = 8$). The Wenzl-bridge equality $y_\lambda = w_\lambda(q)$ holds only on the self-conjugate stratum ($\kappa_\lambda = \sum_{x} c(x) = 0$) under matching Schur-element normalisations.

  A fourth partition-indexed scalar is unrelated to the weight family despite symbol similarity:

    - $\mu_\lambda(q)$ = $q$-Laplacian eigenvalue on $V_\lambda$ from [the $q$-heat-kernel Peter–Weyl proposition](#prop:q-heat-kernel-peter-weyl) — the heat-flow decay rate $\hbar_q^2 \sum_{x \in \lambda} [c(x)]_q [c(x)+1]_q$. It is not a Markov-trace weight, does not multiply $\chi^\lambda$, is not normalised, and does not enter the Frobenius expansion.

  **Concrete $H_3$ values at $q = 1$** (Jones-normalised $V / [2]_q^{c-1}$ convention of [the Borromean Markov-trace closed form](#prop:borromean-markov-trace-closed-form) and [the $H_3$ Markov–Wenzl weights](#prop:h3-markov-wenzl-weights)):

  | $\lambda$ | $d_\lambda$ | $y_\lambda(1)$ | $w_\lambda(1)$ | $\mu_\lambda(1)$ |
  |---|---|---|---|---|
  | $(3)$ | $1$ | $1/2$ | $1/6$ | $0$ |
  | $(2,1)$ | $2$ | $1/4$ | $2/3$ | $2 \hbar_q^2$ |
  | $(1^3)$ | $1$ | $0$ | $1/6$ | $0$ |
  | sum identity | — | $\sum y_\lambda d_\lambda = 1$ | $\sum w_\lambda(1) = 1$ | (no sum) |

  The $y_\lambda$ vector $(1/2, 1/4, 0)$ is non-uniform with $y_{(1^3)} = 0$ identically (Temperley–Lieb quotient). At $\lambda = (2,1)$, $y_{(2,1)}(1) = 1/4 \neq 2/3 = w_{(2,1)}(1)$ because the Jones normalisation differs from the Schur-element normalisation; the two match on the self-conjugate stratum once normalisations are aligned.
- **$\check{q}$** (q-háček, "little hook") = spinor information rate, $\check{q} = q^{1/2}$, $\check{q}^2 = q$, the eigenvalue of the elementary half-twist on the spin-$\tfrac{1}{2}$ fundamental representation of $\mathrm{SU}_q(2)$. The háček diacritic encodes $\check{q}^2 = q$ directly in the glyph, analogous to $i^2 = -1$, lifting the 1-D adjoint (spin-1) braid representation to the 2-D spinor (spin-$\tfrac{1}{2}$) representation. The letter $r$ is reserved for radius or root-of-unity order, $t$ is avoided ($V_K(t)$ knot variable and time), and $\iota$ is reserved for involutions and inclusions.
- **$u$** = LP shadow-price $u_\lambda, u_0$ (Schrijver convention for operator-selection LP dual variables, Table 3) or the $Q_\beta$ precision-ladder step variable $u_{\text{ladder}} = b\,\hbar_q^2$ in $Q_\beta = Q_{\text{base}} \prod_k (1 + c_k\,u_{\text{ladder}}^k)$, with $b$ the Hoefsmit coupling and $\hbar_q = (q-1)/q$ ($u_{\text{ladder}} \approx 0.00852$ at $q_0$). Rather than the Habiro literature's $u = q^{1/2}$, Habiro-ring expansions are written $\mathrm{tr}_M = \sum_m a_m(\check{q})\,(\check{q};\check{q})_m / D(\check{q})$ using the spinor rate $\check{q}$, and contexts combining LP shadow prices with the precision ladder write $u_{\text{ladder}}$ explicitly.
- **Borel** covers three unrelated senses that must never be cross-linked. First is the Lie-theoretic **Borel subalgebra** (Armand Borel) of the $q$-oper chapter ([the $q$-oper definition](#def:q-oper)). Second is the $K$-theoretic **Borel regulator** (Armand Borel, 1977) of [partial Borel resolution](#prop:borel-partial-resolution) and [the Borel–Zagier volume conjecture](#conj:borel-zagier-qou-volumes). Third is **Écalle–Borel resummation** (Émile Borel) — the Borel transform $\mathcal{B}$, lateral/median Laplace–Borel sums, and alien derivatives $\Delta_\omega$ ([Écalle–Borel resummation](#def:ecalle-borel-resummation)). Resummation statements bear neither on regulator transcendence ($\mathbb{Q}$-linear independence of volumes) nor on flag/oper data.
- **$\ell$** denotes the Wenzl principal-specialisation length (number of points in $s_\lambda(1, q^2, \ldots, q^{2(\ell-1)})$).
- **$\mathcal{A}$ vs $\mathcal{B}_K$ — two distinct braids on different strand counts.** $\mathcal{A} \in H_{A+Z}(q)$ is the **neutral atom**: $Z$ protons, $N$ neutrons, and $Z$ **electrons** on $A + Z$ strands, carrying all six crossing types of [the atomic braid definition](#def:atomic-braid) including the three electronic sectors ($\mathfrak{p}e$, $\mathfrak{n}e$, $ee$). $\mathcal{B}_K \in H_{3A}(q)$ is the **electron-free nuclear core** — three quark strands per nucleon, no electron strands — as recorded in Table 3 and [atomic mass normal form](#prop:atomic-mass-gb-nf). Because $A + Z < 3A$ strictly for every $Z \geq 1$, $H_{A+Z}$ cannot hold the $3A$ word at any mass number $A$. Thus $\mathcal{A}$ denotes exclusively the $A+Z$ neutral-atom braid (which reproduces all $19$ rows of the $Z = 1$–$20$ $\Phi_3$ column parameter-free), whereas every $3A$ nuclear-core element is written $\mathcal{B}_K$.
- Numerical specialisations $q \approx 1.110$ (or specific aether-parameter values) appear only in the introduction, Chapter 8 (Information Theory, for falsifiability evaluations), and Chapter 11 (Observations); geometry chapters keep $q$ symbolic.

**Approximation convention (derived / observed values).** Numerical values derived from the aether parameter $q_0$ or compared to experimental data use $\approx$ (or $\simeq$), never $=$, unless an explicit error term is present. Exact algebraic identities (e.g. $c_q = 1/(q-1)$) use $=$ since they hold for all $q$.

**Hecke–Skein convention.** The Hecke algebra generator is $\sigma_i$ (never $T$, never $t$ or $A$ for the Jones polynomial variable). The Iwahori–Hecke algebra $H_n(q)$ is presented as a quotient of the braid group algebra of $B_n$, with the same symbol $\sigma_i$ denoting both the braid-group generator and its image in $H_n(q)$ according to context. The Jones polynomial is always $J_K(q)$, not $V_K(t)$. The letter $J$ is shared with the Hahn–Exton $q$-Bessel function $J_\nu^{(3)}(x;q)$ (aether harmonic analysis, the $\mathrm{SU}_q(2)\to E_q(2)$ contraction) and the ordinary Bessel weights $J_n(x)$ of the Jacobi–Anger expansion. Subscripts and superscripts disambiguate the three: a knot/link $K$ for the Jones polynomial, and an order $\nu$ or $n$ with argument $x$ (plus superscript $(3)$ for Hahn–Exton) for Bessel functions. Bare $J$ is never written.

**Categories vs CPT operators.** Categories are typeset in bold ($\mathbf{C}$, $\mathbf{Rep}$, etc.), whereas calligraphic $\mathcal{C}$ is reserved exclusively for the charge-conjugation operator in CPT discussions (alongside parity $\mathcal{P}$, time-reversal $\mathcal{T}$, $\mathcal{CP}$, and $\mathcal{CPT}$). Calligraphic $\mathcal{C}$ never denotes a category in this paper.

**Dirac bra–ket $\lvert \psi \rangle$ / $\langle \phi \vert \psi \rangle$.** States of the framework are objects and morphisms of $\mathbf{C}$ and vectors of its Hecke modules. The native scalar-valued pairing is the Frobenius form $\langle x, y\rangle_F$: matrix elements are written $\langle v, \Phi v\rangle_F$ (never $\langle v \vert \Phi \vert v\rangle$), and seminormal or Young basis vectors are written $v_T$ (standard Young tableau $T$) or $v_c$ (channel $c$), never kets $\lvert T \rangle$ or $\lvert \psi_N \rangle$. Bra–ket notation appears only when quoting standard quantum-mechanics literature.

**Base ring convention.** Pre-boundary categorical constructions, algebraic identities, $q$-deformation combinatorics, and Wenzl / Hecke / Hoefsmit structural data are formulated over a generic ground ring $R$ carrying the minimal required algebraic structure (commutative ring, field, or group with zero). The real field $\mathbb{R}$ enters **only past the Archimedean boundary** — when a statement genuinely requires real square roots, fractional powers, trigonometric, exponential, or logarithmic functions, an archimedean order ($0 < q$), or comparison with experimental constants. Accordingly, $q \in R$ whenever only the algebraic structure is invoked, and $q \in \mathbb{R}$ only at archimedean evaluation.

**Non-degeneracy of $q$.** On any normed commutative ring (in particular $R = \mathbb{C}$; see [complex $q_0$ extension](#prop:q-zero-complex-extension)), the condition $\lvert q \rvert > 1$ suffices to make $q$ a unit. Pre-$\tau$ algebraic-aether statements use $\lvert q \rvert > 1$, whereas $q > 1$ is reserved for post-$\tau$ statements requiring real ordering (such as Hoefsmit seminormal orthogonality, real square-root identities, and experimental comparisons).

**Decay width $\mathfrak{D}$ vs lifetime $\tau$ vs sheaf sections $\Gamma$.** Three standard physics/math symbols collide in this paper:

| Symbol | Paper use | Physics use (avoided) | Resolution |
|--------|----------|----------------------|------------|
| $\tau$ | **Fibre functor** $\tau : \mathbf{C} \to \mathbf{Arch}$ | Lifetime $\tau_n, \tau_\mu$ | Use $\hbar / \mathfrak{D}$ for lifetime |
| $\Gamma$ | **Sheaf sections** $\Gamma(N)$, local cohomology $\Gamma_{\mathfrak{m}_1}$ | Decay width $\Gamma_n, \Gamma_\mu$ | Use $\mathfrak{D}$ (fraktur D) |
| $\mathfrak{D}$ | **Decay width** (NEW) | — | $\mathfrak{D}_K$ = decay width of hadron $K$ |

Convention: $\mathfrak{D}_K = \hbar / (\text{lifetime of } K)$. Subscripts: $\mathfrak{D}_\mu$ (muon), $\mathfrak{D}_n$ (neutron), $\mathfrak{D}_K$ (generic hadron). **The family contains rates only.** A bar-parity calibration channel takes $P_{\mathrm{skew}}$ / $P_{\mathrm{avg}}$, never $\mathfrak{D}$: writing CAL-2 as $\mathfrak{D}_\beta$ placed it one subscript from the genuine $\mathfrak{D}_n$ while denoting a different kind of object, and invited the relation $\mathfrak{Q}_\beta = \hbar/\mathfrak{D}_\beta$, which is dimensionally inconsistent — $\mathfrak{Q}_\beta$ is an energy and $\hbar/\mathfrak{D}_n$ is a time. Fermi theory: $\mathfrak{D}_\mu = G_F^2 \mathfrak{m}_\mu^5 / (192\pi^3)$.

**Archimedean / fibre / forgetful functors.** Three nominally similar functors appear in the QOU framework and must not be conflated:

| Functor | Domain → Codomain | Role |
|---|---|---|
| **Fibre functor** $\tau$ | $\mathbf{C} \to \mathbf{Arch}$ | Tannakian fibre over a brane point; selects which aether object becomes the observation. |
| **Forgetful functor** $U$ | $\mathbf{Arch} \to \mathbf{Vec}_{\mathbb{R}}$ | Drops the archimedean enrichment, leaving the underlying real vector space. |
| **Archimedean realisation** (informal "Arch") | $\mathbf{C}(R) \to \mathbf{C}(\mathbb{R})$ | Base-ring substitution ($R \mapsto \mathbb{R}$) at the Archimedean boundary; **not** a functor between QOU categories. |

The category $\mathbf{Arch}$ is the target of $\tau$ rather than the name of a functor: prose specifies either "$\tau$ specialised to $\mathbf{Arch}$" or "the $R \mapsto \mathbb{R}$ realisation", never "the archimedean realisation" without context.

**Pinning $\tau$'s codomain: one functor, several de-enriched levels.** The canonical fibre functor is $\tau \colon \mathbf{C} \to \mathbf{Arch}$. Where $\tau$ is written into a *different* target, it means a **composite** with $\tau$ rather than a rival functor:

| Written as | Means | Level |
|---|---|---|
| $\tau \colon \mathbf{C} \to \mathbf{Arch}$ | the fibre functor itself | enriched (canonical) |
| $\tau \colon \mathbf{C} \to \mathbf{Vec}_{\mathbb{R}}$ | $U \circ \tau$ | forget archimedean enrichment |
| $\tau \colon \mathbf{C} \to \mathbf{Set}$ | underlying set-valued functor (Tannakian $\omega$) | forget linear structure |
| $\tau \colon \mathbf{C} \to \mathbf{D}$ (spatial realisation) | $\tau$ into a chosen geometric model $\mathbf{D}$ | model-specific |

These are genuine functors (they act on morphisms). What is **not** a functor is the archimedean **evaluation** $\pi_\infty \colon \mathrm{Obj}(\mathbf{Arch}) \to \mathbb{R}$ (an object-level map / place), and the *ring-level* realisations it induces: the motivic measure $\mathcal{R}_{\mathrm{top}} \colon K_0(\mathrm{Var}) \to \mathbb{R}$ (a ring homomorphism) and the standard-part map $\mathrm{st} \colon \mathbf{No}_{\mathrm{fin}} \to \mathbb{R}$ (a ring homomorphism). Reserve "functor" for $\tau$, $U$, and $\mathrm{St}$; call the maps into $\mathbb{R}$ *realisations / evaluations*.

**"Forgetful functor $\tau$" (classical usage): a synonym rather than a clash.** Core definition blocks write "the **forgetful functor** $\tau$" (e.g. *a QOU is a $(\mathbf{C}, A, \tau)$ with the forgetful functor $\tau$ **faithful***). This is the **classical Tannakian name**: for $\mathbf{C} = \mathbf{Rep}(U_q\mathfrak{sl}_2)$ the fibre functor and the forgetful functor are the *same* functor $\tau \colon \mathbf{C} \to \mathbf{Mod}_R$ that forgets the coaction while keeping the underlying module. In the enriched register above, that classical $\tau$ is the composite $U \circ \tau \colon \mathbf{C} \to \mathbf{Vec}_{\mathbb{R}}$ (row 2 of the previous table), and the faithfulness axiom is a statement at this underlying-module level. Thus "**forgetful functor $\tau$**" and "**fibre functor $\tau$**" name the **same genuine functor** at different codomain levels; the only *distinct* forgetful arrow is $U \colon \mathbf{Arch} \to \mathbf{Vec}_{\mathbb{R}}$.

**Binding-energy notions $B_\bullet$.** Distinct binding-energy quantities are written as plain $B$ with systematic subscripts:

| Symbol | Definition | Role | Status |
|---|---|---|---|
| $B_{\mathrm{AME}}$ | AME 2020 measurement | experimental ground truth | anchor |
| $B_{\mathrm{sym}}$ | $-\alpha \ln\lvert\mathrm{tr}_M(K)\rvert$ (log-trace) | **exact** symbolic, light $A$ | kept |
| $B_{\mathrm{qCLT}}$ | $-\alpha \sum_i \ln\lvert V_i\rvert$ | qCLT asymptotic, $A\to\infty$ | kept |
| $B_{\mathrm{lin}}$ | $Q_\beta(n)\,(\mathrm{tr}_M(W_{\text{free}}) - \mathrm{tr}_M(W_{\text{atom}}))$ | **linear-truncation** production | canonical compute |
| $B_{\mathrm{depth}}$ | $\sum_k \alpha_k \Phi_k$ | depth-stratified tower | default; empirical $\alpha_k$ |
| $B_{\mathrm{magic}}$ | $2\,m_e A\,\mathrm{Vol}(L6a4)$ ($^4\mathrm{He}$) | flat magic-$A$ | $^4\mathrm{He}$ canonical |
| $B_\lambda$ | $m_e \sum_\lambda y_\lambda \chi^\lambda \Delta_\lambda$ | per-partition | open (the $\Delta_\lambda$ magnitude) |

**Critical distinction — $B_{\mathrm{sym}}$ (exact) vs $B_{\mathrm{lin}}$ (linear).** $B_{\mathrm{lin}}$ is the linearization of $B_{\mathrm{sym}}$ (Kashaev $\mathrm{tr}_M \sim \exp(\mathrm{Vol})$; the scalar $\Delta\mathrm{tr}$ is the first-order term). They are NOT interchangeable. Their ratio is the binding deficit
$$ B_{\mathrm{sym}} / B_{\mathrm{lin}} \;\approx\; q_0^{\,5(2A-1)}, $$
i.e. the $\Delta_\lambda = B_{\mathrm{AME}}/B_{\mathrm{lin}}$ residual. Binding energies always carry subscripts; a bare $B$ in prose denotes the production $B_{\mathrm{lin}}$.

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
- **$\Phi_{\mathrm{mass}}(\beta) \in H_n(R, q)$ is an element rather than a map.** It
  *maps to* an endomorphism of $V^{\otimes n}$ via $q$-Schur–Weyl
  $H_n(q) \twoheadrightarrow \mathrm{End}_{U_q\mathfrak{sl}_N}(V^{\otimes n})$
  \cite{jimbo1986}, or *is* one faithfully via the left-regular map
  $a \mapsto L_a \in \mathrm{End}_R(H_n)$ \cite{kock2004}; specify which, never
  writing "$\Phi_{\mathrm{mass}}$ is the mass endomorphism" bare.
  **The Schur–Weyl arrow is a surjection, not an isomorphism, unless $N \ge n$.**
  Below that it has kernel the blocks with more than $N$ rows, so an element of
  the kernel maps to the zero endomorphism and the identification is not
  faithful. At $N = 2$ (convention D) with $n = 3A$,
  the image is $\mathrm{TL}_n(q) = \mathrm{End}_{U_q\mathfrak{sl}_2}(V^{\otimes n})$
  of dimension $C_n$, against $\dim H_n = n!$, a kernel of dimension
  $n! - C_n$, i.e. $1, 10, 78, 588, 4611, 38890$ at $n = 3,\dots,8$. Only the
  left-regular map is faithful unconditionally.
- **$\mathfrak{m}$ is a functional rather than an endomorphism.** The Markov trace
  $\mathrm{tr}_M \colon H_n \to R$ is a trace functional \cite{jones1987,
  geckpfeiffer2000}; the modulus collapses $\mathcal{M}$ to a number. Note
  $\mathrm{tr}_M(a) \neq \mathrm{tr}(L_a)$: the Markov trace is the *quantum*
  trace rather than the regular-representation trace.

**Convention — $\mathcal{M}$ = endomorphism; the mass functional is $\mathfrak{m}$.** The glyph $\mathcal{M}$ separates into three distinct symbols:

| Sense | Object | Type | Canonical glyph |
|---|---|---|---|
| **mass endomorphism** | $\mathcal{M}(K)$ (complex-volume block, $\mathfrak{V}$ entry) | $\mathrm{End}_{\mathbf{C}}(X_K)$ | **$\mathcal{M}$** |
| **mass functional** | Skein-module map $\mathrm{Sk}_q\to\mathbb{R}_{\geq0}$ (evaluates a knot class to its mass) | functional | **$\mathfrak{m}$** |
| **scattering amplitude** | transition matrix element $\lvert\mathcal{M}_q\rvert^2$ (e.g. [trace-ratio observable](#prop:trace-ratio-observable)) | scalar amplitude | **$\mathcal{M}_q$** |

Convention: reserve $\mathcal{M}$ (calligraphic operator) for the **endomorphism**; write $\mathfrak{m}\colon\mathrm{Sk}_q\to\mathbb{R}_{\geq0}$ for the Skein **functional** (fraktur observable register, matching the mass scalar $\mathfrak{m}$ it outputs); and keep the subscripted $\mathcal{M}_q$ for the scattering **amplitude**.

## Quantum dilogarithm: $\Phi_q$ (compact) vs $\Phi_b$ (Faddeev non-compact)

Two distinct functions must never share the name "Faddeev $\Phi_q$":

| Symbol | Definition | Correct name |
|---|---|---|
| $\Phi_q(z)$ | $\prod_{k\ge 1}(1 - q^{-k}z)^{-1}$ (reciprocal $q$-Pochhammer) | **compact quantum dilogarithm** / $q$-exponential |
| $\Phi_b(z)$ | modular-double ratio, kernel $\sinh(zb)\sinh(z/b)$, poles at $c_b + ib\mathbb{N} + i b^{-1}\mathbb{N}$ | **Faddeev** (non-compact) quantum dilogarithm |

- **"Faddeev" belongs to $\Phi_b$ only.** Never write "Faddeev $\Phi_q$" for
  the compact form; write "compact quantum dilogarithm $\Phi_q$" (or
  "$q$-Pochhammer").
- $\Phi_q$ governs the real-$q$ / **mass** (bar-even, Rogers) face;
  $\Phi_b$ governs the **decay** ($\mathfrak{Q}_\beta$, bar-odd, root-of-unity)
  face, matching Hikami's modular-double conventions. At the real aether parameter $\Phi_b \to \Phi_q$ (the modular dual
  $\tilde q$ is $\sim 10^{-165}$-suppressed).
- **Askey two-saddle passages.** Where an Askey-saddle context writes $\Phi_q$ for the non-compact regulator, disambiguate from the surrounding modular-double prose.

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
disjoint unknots is accurate, whereas assigning the single unknot $0_1$ to the
photon as its knot identity violates the distinction recorded in
[two-photon pair production](#rem:two-photon-pair-production)
and the [recursive atom-knot atlas registry](#rem:recursive-atom-knot-atlas-registry).

## Bar-even / bar-odd: always the coefficient half

The words **bar-even** and **bar-odd** label four different gradings in this
paper. They are not four involutions. All four descend from the single
[bar involution](#def:bar-involution) on $H_n(q)$,

$$
  \overline{\sigma_i} = \sigma_i^{-1}, \qquad \overline{q} = q^{-1},
$$

which has **two halves that apply independently**:

| Half | Acts by | Geometrically |
|---|---|---|
| **coefficient half** | $q \mapsto q^{-1}$, diagram fixed | reciprocates the weights |
| **diagram half** | $\sigma_i \mapsto \sigma_i^{-1}$, coefficients fixed | the **mirror**: exchanges positive and negative crossings, $p \leftrightarrow m$ |

**Convention.** In this paper *bar-even* and *bar-odd* always mean parity
under the **coefficient half**. A parity taken under the diagram half is
called **mirror-even** / **mirror-odd**, never "bar-". Which grading is meant:

| | Splits | Graded by | Where |
|---|---|---|---|
| **A** | the Laurent scalar $\mathfrak{E}_{\mathrm{cross}}$ into $\cosh\lambda$ / $\sinh\lambda$ | coefficient half | [crossing-energy decomposition](#prop:crossing-energy-decomposition) |
| **B** | the Hecke module into $e_+$ / $e_-$ by eigenvalue $q$ / $-q^{-1}$ | **neither** — the full involution *fixes* both idempotents | [electromagnetic coupling projection](#prop:em-coupling-projection) |
| **C** | the knot, by the mirror; the channel totals $E_{\mathrm{sym}}$ / $E_{\mathrm{asym}}$ | diagram half | same block as A, item 2 |
| **D** | the algebra $A = A_+ \oplus A_-$ by the spin involution | coefficient half | [spin involution](#def:spin-involution) |

**A and D are the same grading.** On the symmetric/alternating Hecke block the
spin involution acts as the eigenvalue swap $q^{2k} \leftrightarrow q^{-2k}$,
which is the coefficient half; its sectors are $A_+ = \cosh(2k\lambda)$
and $A_- = \sinh(2k\lambda)$. Thus $A_+$ bar-even and $A_-$ bar-odd match
$\cosh\lambda$ bar-even and $\sinh\lambda$ bar-odd.

**C is anti-correlated with A, and this is not an error.** The weight
$\cosh\lambda$ is bar-even, while its channel total
$E_{\mathrm{sym}} = (p - m)\cosh\lambda$ is mirror-**odd**, because the mirror
flips the multiplicity $p - m$ as well as the weight. Both statements hold of
the same summand; only the half differs. Read a parity claim about a *weight*
as coefficient-half and a parity claim about a *channel total* as diagram-half
unless stated otherwise.

**Never say "bar-even" unqualified of a channel.** Under the full involution
both crossing-energy channels are negated and both Hecke idempotents are
fixed, so unqualified parity separates nothing there; parity is informative only
relative to a named half over a general ground field.

**Four different objects wear the glyph $\sigma$** — the Hecke generator
$\sigma_i$, the mirror $K \mapsto K^{\sigma}$, the spin involution
$\sigma : A \to A$, and the bar involution itself when written
$\sigma \colon q \mapsto q^{-1}$. A bare $\sigma$ therefore never
disambiguates a parity claim; name the half instead.

Writing the bar involution as "$\sigma \colon q \mapsto q^{-1}$" states only the
**coefficient half**, which yields the wrong parity if applied naively to elements
inside $H_n(q)$. Specifically, the $V_\lambda \leftrightarrow V_{\lambda'}$ intertwiner is the
sign twist $\sigma_i \mapsto -\sigma_i^{-1}$ rather than the bar involution, and
under the full involution the Markov parameter $z$ maps to $z - h$ rather than
$z$ because M3 contains $\sigma_n$ (convention D, $z = q^3/(q^2+1)$, follows
independently from [primitive Markov axioms](#rem:markov-axioms-primitive)).
When grading an element of the algebra $H_n(q)$, apply both halves.

## QCD vocabulary: five words that mean something else here

Every collision above is **internal** — two objects inside this framework
wearing one glyph. This section records a different hazard: five terms that
carry a standard meaning in QCD and a *different*, unrelated meaning in this
paper:

| Term | Standard QCD meaning | Meaning in this paper |
|------|----------------------|-----------------------|
| **saturation** | small-$x$ gluon recombination; the saturation scale $Q_s(x)$ | three distinct senses: the *genus* saturation of $T_{2,9}$; **nuclear saturation**, meaning the $B/A$ plateau; and cosmological scale saturation |
| **shadowing** | nuclear shadowing; Gribov inelastic screening | **LP-dual shadow prices** $y_0^{\star}, y^{\star}$ — the binding-energy duals of [the operator-selection linear program](#prop:operator-selection-lp); also "archimedean shadow" and the $a_1$ "parity shadow" |
| **diffraction** | Pomeron exchange; diffractive dissociation | **optical** diffraction — Fraunhofer, Airy, and the double-slit chapter |
| **S-matrix** | the scattering matrix | the **modular** $S$-matrix of a modular tensor category — the Reshetikhin–Turaev / Chern–Simons vacuum row and total quantum dimension $D = \sum_i d_i^2$ |
| **Fourier transform** | conjugate to momentum or impact parameter | the discrete transform on $C_n$ (Lagrange resolvent), the **categorical** Fourier transform, and the adelic Fourier transform (none over a transverse impact plane) |

In the nuclear and hadronic binding chapters, observables are evaluated at a
single aether parameter as knot and link invariants rather than
transverse-plane impact-parameter or Gribov-shadowing amplitudes. Resolve each term to its definition in
[the notation register](#prose:notation-register) before interpreting its domain.

## "One-dimensional": four senses, and the spatial one is the rarest.

Four distinct mathematical senses share the adjective "one-dimensional".

* **Representation dimension** — a Wedderburn block, irreducible representation, or character of
  dimension one; a one-row or one-column Young diagram.
* **Linear-algebraic dimension** — a solution space, cohomology group, or
  module of forms: *"$HH^2 \cong k$ is one-dimensional"*, *"$\Lambda^2 H^*$ is
  one-dimensional"*.
* **Seminormal channel dimension** — a seminormal channel on which a Hecke generator acts by a
  scalar.
* **Spatial dimension** — $\dim M_k = 1$: a one-dimensional descent stratum or filament.

Write the spatial sense explicitly as $\dim M_k = 1$, or qualify it in words as
*spatially one-dimensional* / *one spatial dimension*, since representation,
cohomological, and seminormal channel uses outnumber spatial uses by more than an
order of magnitude. Where a noun immediately follows (*one-dimensional block*,
*one-dimensional channel*, *one-dimensional representation*, *one-dimensional character*),
the noun already disambiguates the sense.

## Demand magnitude: always $|\mathrm{dem}|$, never $|\mathrm{def}|$

[The demand-profile definition](#def:demand-profile) defines, for a derived atom in
normal form $\mathcal{A}(Z,N) = \sum_w c_w \cdot w$,

$$
  \mathrm{dem}(\mathcal{A}) = \{(w, c_w) : c_w < 0\},
  \qquad
  |\mathrm{dem}| = \sum_{c_w < 0} |c_w| ,
$$

the sum of the negative normal-form coefficients. **That quantity has one
symbol:** always write $|\mathrm{dem}|$, never $|\mathrm{def}|$.
The English noun *deficit* (*deficit-free*, *deficit closure*, *periodic-table
deficit conjecture*) remains standard prose for the condition $|\mathrm{dem}| = 0$,
whereas the symbol $|\mathrm{def}|$ is disallowed.

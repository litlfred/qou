<!-- FILE_START: topological-mass-pl-sw-duality-intro.md -->
The categorical Markov-Frobenius residue and the Seiberg-Witten (SW) thimble decomposition act as algebro-geometric duals. Each Picard-Lefschetz (PL) reduction maps to an SW critical-point structure. Each abelianization at an algebraic pole matches a Wedderburn-orbit decomposition.

The sequence traces $D_4$ moduli symmetry, the Möbius limit, Morse-wall $q$-moduli, and delta-lambda categorical closure. A jet/Grobner/PL correspondence links Grobner reduction to PL thimbles. Denominator-zeros form SW critical points. Algebraic poles induce abelianization.

Orbital symmetry and cohomological embedding dictate consequences for fundamental particles.
<!-- FILE_END: topological-mass-pl-sw-duality-intro.md -->

<!-- FILE_START: bar-self-dual-confinement-band.md -->
**Proposition.** Let $\iota \colon \mathbb{R}_{>0} \to \mathbb{R}_{>0}$ denote the bar involution $\iota(q) = q^{-1}$. The open interval

$$
  \mathcal{B}  :=  \bigl(1/\varphi^2,\,\varphi^2\bigr) \subset  \mathbb{R}_{>0}
$$

is the maximal connected $\iota$-invariant open subinterval of $\mathbb{R}_{>0}$ excluding the golden nodes $\{1/\varphi^2,\,\varphi^2\}$ ([skew-dual golden node](#prop:golden-skew-dual-node)). Equivalently, $\mathcal{B}$ is the largest interval satisfying the deconfinement criterion $q > 1/\varphi^2$ ([deconfinement threshold](#rem:deconfinement-golden-threshold)) and its bar conjugate $q < \varphi^2$ simultaneously.
<!-- FILE_END: bar-self-dual-confinement-band.md -->

<!-- FILE_START: bar-self-dual-confinement-band-novelty.md -->
**Remark.** To define a rigid phase boundary, this formulation unifies three disjoint asymmetric phase regimes into a single bar-self-dual confinement band using standard involution bounds.
<!-- FILE_END: bar-self-dual-confinement-band-novelty.md -->

<!-- FILE_START: bar-t-duality-substrate.md -->
**Proposition.** The bar involution $\iota \colon q \mapsto q^{-1}$ on the substrate parameter line lifts to a substrate-level T-duality between elliptic curves of the Descartes family ([Descartes elliptic curve](#prop:descartes-elliptic-curve)):

$$
  \iota_*\,\mathcal{E}_q  =  \mathcal{E}_{q^{-1}}.
$$

Here $\iota_*$ is the pull-back of $\iota$ along the substrate parametrization $q \mapsto \mathcal{E}_q$. Under $\iota_*$:

1. **Discriminant locus:** The pole $\Delta(\mathcal{E}_q) = 0$ at $q = 1/\varphi^2$ pairs with $\Delta(\mathcal{E}_{1/q}) = 0$ at $q = \varphi^2$ ([skew-dual golden node](#prop:golden-skew-dual-node)).
2. **$j$-invariant:** The rational involution $j \mapsto j^*$, induced by $q \mapsto q^{-1}$ on the Weierstrass coefficients, relates $j(\mathcal{E}_q)$ and $j(\mathcal{E}_{1/q})$.
3. **Confinement band:** The curve $\mathcal{E}_q$ is non-degenerate if and only if $q \in \mathcal{B}$ ([bar-self-dual band](#prop:bar-self-dual-confinement-band)). The involution $\iota$ fixes $\mathcal{B}$ setwise.

Target-space T-duality ([self-duality of $\mathcal{E}_z$](#rem:t-duality-elliptic)) exchanges $X \leftrightarrow z$ on a single curve. Bar T-duality instead acts on the moduli parameter $q$. These commuting dualities generate a $\mathbb{Z}/2 \times \mathbb{Z}/2$-action on the moduli stack of Descartes-family curves.
<!-- FILE_END: bar-t-duality-substrate.md -->

<!-- FILE_START: bar-apply-transfer.md -->
**Proposition (Bar-transfer principle).**
Let $P \colon \mathbb{R}_{>0} \to \mathrm{Prop}$ be a bar-invariant property of the substrate parameter:

$$
  \forall\,q > 0,\quad P(q) \iff P(q^{-1}).
$$

For every $a > 0$:

1. **Lower bound transfer.**
   $\bigl(\forall q > a,\; P(q)\bigr) \iff
    \bigl(\forall q < a^{-1},\, q > 0 \Rightarrow P(q)\bigr).$

2. **Two-sided extension.**
   If $a < 1$ and $\bigl(\forall q \in (a, a^{-1}),\, P(q)\bigr)$, then
   $\bigl(\forall q \in \mathbb{R}_{>0} \setminus \{a, a^{-1}\},\, P(q)\bigr)$
   does not follow in general. If $P$ is continuous on
   $\mathbb{R}_{>0}$, bar-invariance forces $P$ to extend symmetrically
   across both endpoints.

3. **Negation transfer.**
   $\bigl(\exists q < a,\, q > 0 \land \neg P(q)\bigr) \iff
    \bigl(\exists q > a^{-1},\, \neg P(q)\bigr)$.

**Archimedean specialisation (§7c).**
This block sits on the archimedean side of the substrate wall. It invokes analytic constructs: real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at $q_0$. Categorical or $q$-deformation identities remain valid over an abstract coefficient ring. Only their archimedean realisation requires specialisation here.
<!-- FILE_END: bar-apply-transfer.md -->

<!-- FILE_START: golden-quartet-galois.md -->
**Proposition (Golden quartet as Galois $\times$ bar orbit).**
The golden quartet

$$
  Q  :=  \bigl\{\,1/\varphi,\;-\varphi,\;\varphi,\;-1/\varphi\,\bigr\}
$$

is the complete root set of the quartic polynomial

$$
  P(x)  :=  x^4 - 3x^2 + 1
   =  (x^2 - x - 1)(x^2 + x - 1)
$$

over $\mathbb{Q}$. Under the Galois action $\mathrm{Gal}(\mathbb{Q}(\sqrt{5})/\mathbb{Q}) = \langle \tau \rangle \cong \mathbb{Z}/2$, where $\tau \colon \sqrt{5} \mapsto -\sqrt{5}$, the quartet splits into two orbits:

$$
  Q_+  :=  \{\,\varphi,\;-1/\varphi\,\}
  \;=\;\mathrm{Gal\text{-orbit}\ of\ }\varphi
  \;=\;\mathrm{roots\ of\ }x^2 - x - 1,
$$

$$
  Q_-  :=  \{\,1/\varphi,\;-\varphi\,\}
  \;=\;\mathrm{Gal\text{-orbit}\ of\ }1/\varphi
  \;=\;\mathrm{roots\ of\ }x^2 + x - 1.
$$

The bar involution $\iota \colon x \mapsto x^{-1}$ on $\mathbb{R}^\times$ exchanges these orbits:

$$
  \iota(Q_+) = Q_-,\qquad \iota(Q_-) = Q_+.
$$

The joint group $G := \mathrm{Gal}(\mathbb{Q}(\sqrt{5})/\mathbb{Q}) \times \langle\iota\rangle \cong \mathbb{Z}/2 \times \mathbb{Z}/2$ acts transitively and faithfully on $Q$.
<!-- FILE_END: golden-quartet-galois.md -->

<!-- FILE_START: golden-quartet-galois-interpretation.md -->
**Remark.** Standard cyclotomic $\zeta_5$ bookkeeping introduces complex phase ambiguities. A pure real orbit $Q$ replaces this bookkeeping to strictly bound physical observables within the maximal real subfield during Bring's curve reductions. The joint group $G = \mathrm{Gal} \times \langle \iota \rangle$ acting on $Q$ structures the QOU model.
<!-- FILE_END: golden-quartet-galois-interpretation.md -->

<!-- FILE_START: moduli-symmetry-d4.md -->
**Proposition (Dihedral $D_4$-action on the moduli line).**
The two natural involutions on the substrate moduli line $\mathbb{C}^\times$,

$$
  \sigma\colon q \mapsto iq
  \qquad\text{(complex rotation by $\pi/2$)},
  \qquad
  \tau\colon q \mapsto q^{-1}
  \qquad\text{(Hecke bar involution)},
$$

generate a faithful action of the dihedral group of order 8:

$$
  D_4
   =  \langle\,\sigma,\,\tau \;\mid\; \sigma^4 = \tau^2 = (\sigma\tau)^2 = 1\,\rangle.
$$

The relation $(\sigma\tau)^2 = 1$ enforces the dihedral commutation $\tau\sigma\tau = \sigma^{-1}$. Verification:

$$
  \tau\sigma\tau(q)
   =  \tau(\sigma(q^{-1}))
   =  \tau(iq^{-1})
   =  (iq^{-1})^{-1}
   =  -iq
   =  \sigma^{-1}(q).
$$

**The golden octet.**

The $D_4$-orbit of $\varphi$ in $\mathbb{C}^\times$ forms the golden octet:

$$
  G_8
   :=  D_4 \cdot \varphi
   =  \bigl\{\,\varphi,\;i\varphi,\;-\varphi,\;-i\varphi,\;
              1/\varphi,\;i/\varphi,\;-1/\varphi,\;-i/\varphi\,\bigr\}.
$$

The eight elements partition by stabilizer into two cosets:

| Coset | Elements | Generator | Real / imaginary |
|-------|----------|-----------|------------------|
| $\sigma\langle 1\rangle$-orbit through $\varphi$ | $\{\varphi, i\varphi, -\varphi, -i\varphi\}$ | $\sigma^k \cdot \varphi$ | real (golden quartet $Q_+$) plus imaginary axis |
| $\sigma\langle 1\rangle$-orbit through $1/\varphi$ | $\{1/\varphi, i/\varphi, -1/\varphi, -i/\varphi\}$ | $\sigma^k \cdot 1/\varphi$ | bar-image of $Q_+$, by $\tau$ |

The intersection $G_8 \cap \mathbb{R}$ recovers the golden quartet
$Q = \{\,\varphi,\,-\varphi,\,1/\varphi,\,-1/\varphi\,\}$
([golden-quartet-galois](#prop:golden-quartet-galois)).
The intersection $G_8 \cap i\mathbb{R}$ recovers its $\pi/2$-rotation
$iQ = \{\,i\varphi,\,-i\varphi,\,i/\varphi,\,-i/\varphi\,\}$.

Equivalently, the octet contains the eight roots of

$$
  P_{\mathbb{C}}(z)  :=  P(z) \cdot P(z/i)
   =  (z^4 - 3z^2 + 1)(z^4 + 3z^2 + 1)
   =  z^8 - 7z^4 + 1
$$

over $\mathbb{Q}(i)$, where $P(z) = z^4 - 3z^2 + 1$ is the quartic of the golden quartet.
<!-- FILE_END: moduli-symmetry-d4.md -->

<!-- FILE_START: moduli-symmetry-d4-novelty.md -->
**Remark.** To lock the moduli line symmetries to a complex algebraic origin, $\mathbb{Z}[i]$ rather than $\mathbb{Z}$ serves as the ring of definition for the Möbius family under the $D_4$ action.
<!-- FILE_END: moduli-symmetry-d4-novelty.md -->

<!-- FILE_START: outro-predicted-spectra.md -->
Substrate-level predictions assemble into a unified surface: categorical proton uniqueness, the neutron parity-lift, $\alpha_{\mathrm{EM}}$ from the Hartree-categorical fixed point, hadron half-lives, atomic-shell binding energies, the transcendence content of the topological mass formula, and its PL/Seiberg–Witten duality.

The subsequent chapter carries these predictions to the Archimedean side. Setting $q_0 \approx 1.1097$ compares the predictions against CODATA, PDG, and SnapPy data. The per-observable 100× accuracy target defines the empirical band for testing.
<!-- FILE_END: outro-predicted-spectra.md -->

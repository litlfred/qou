The substrate parameter $q$ is a section of $\mathbb{G}_m$ ([substrate $\mathbb{G}_m$ torsion](#rem:substrate-gm-torsion)). The $q$-BSD conjecture ([$q$-BSD](#conj:q-birch-swinnerton-dyer)) describes a family of $L$-functions parametrised by $\mathbb{G}_m$. Its behavior at the boundary and torsion points of $\mathbb{P}^1$ reveals the arithmetic content.

Embed $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$ via $k^\times \hookrightarrow k \cup \{\infty\}$. The $q$-BSD data extends to a family over $\mathbb{P}^1$ with three regimes:

**(I) Generic $q \in \mathbb{G}_m^{\mathrm{nt}}$ (non-torsion locus).**
The QOU axioms hold. The representation category $\mathbf{C} \simeq \mathrm{Rep}(\mathrm{SU}_q(2))$ has infinitely many simple objects $V_j$, for $j = 0, \tfrac{1}{2}, 1, \ldots$, with positive quantum dimensions $[2j+1]_q > 0$. The $q$-BSD data is:

* $r_q = 0$ (by the rank argument).
* $L(\mathcal{E}_q, 1) \neq 0$ (computable from Frobenius eigenvalues; the Hasse--Weil bound gives $|\alpha_\mathcal{E}| = q^{1/2}$, so the Euler factors are bounded away from zero).
* The weak $q$-BSD reduces to $L(\mathcal{E}_q, 1) \neq 0$, which is an unconditional theorem at the $q$-scale.

**(II) $\mathbb{G}_m$ torsion: roots of unity $q = \zeta_n$.**
At the torsion points ([root-of-unity truncation](#prop:root-of-unity-truncation)), the representation category truncates to finitely many simple objects $V_0, V_{1/2}, \ldots, V_{(n-2)/2}$, forming a modular tensor category (Chern--Simons TQFT at level $n$). The $q$-BSD data undergoes a phase transition:

* **Rank:** The categorical rank remains zero. $V_{1/2}$ is still non-trivial in the truncated category, so $V_{1/2}^G = 0$ and $r_q = 0$ persists at all roots of unity.
* **$q$-integers:** The $q$-integers degenerate ($[n]_{\zeta_n} = 0$). The $q$-factorial $[r]_q!$ and the explicit formula have poles/zeros at the torsion points.
* **$L$-function:** The Euler product over $\mathrm{Spec}(R_q)$ reduces to a finite product (only finitely many representations contribute to the trace), giving a rational function in $\zeta_n$ rather than an infinite product.
* **Kummer obstruction:** The Kummer obstruction ([Kummer specialisation](#prop:ns-kummer-specialisation)) controls the behavior: $\kappa_0 \bmod n = 0$ if and only if $n \mid \chi(A)$. For $\chi(A) = -6$, the obstruction vanishes only at $n \in \{1, 2, 3, 6\}$ and persists for all other $n$. At levels where the obstruction persists, the $L$-function carries non-trivial arithmetic information from the Euler class.

**(III) Boundary points $q = 0$ and $q = \infty$.**
At the boundary of $\mathbb{P}^1$:

* $q = 0$: The operator $d_q = q^{-1} d + (1 - q^{-1}) \pi_V d$ has a pole. The elliptic curve $\mathcal{E}_q$ degenerates (the Weierstrass coefficients $p(q), r(q)$ diverge). The $L$-function has an essential singularity.
* $q = \infty$: Here $d_q \to \pi_V \circ d$ (pure Reeb direction). The $j$-invariant $j(\mathcal{E}_q) \to 0$: the curve approaches a CM curve with complex multiplication. The $L$-function acquires Hecke $L$-function structure (Deuring's theorem).

The Kummer exact sequence ([Kummer specialisation](#prop:ns-kummer-specialisation))

$$
1 \to \mu_n \to \mathbb{G}_m \xrightarrow{(\cdot)^n} \mathbb{G}_m \to 1
$$

controls the specialisation of $L(\mathcal{E}_q, 1)$ to the classical limit. The Euler class $\kappa_0 = e(\xi)$ with $\mathrm{tr}(\kappa_0) = \chi(A) = -6$ satisfies

$$
\kappa_0 \bmod n \neq 0 \qquad\text{for } n \nmid 6.
$$

Thus, the topological obstruction class $\kappa_0 \in H^2(\mathcal{S}, \mathbb{G}_m)$ is not $n$-divisible for $n = 5, 7, 11, 13, \ldots$ (all primes $> 3$ and their multiples). At each such level of the Kummer tower, the $q$-BSD formula carries non-trivial arithmetic content that cannot be cancelled by torsion.

*Scope.* On a closed surface $H^2(\mathcal{S}, \mathbb{G}_m) = 0$. The Kummer obstruction is the image $\chi(A) \bmod n \in H^2(\mathcal{S}, \mu_n) \cong \mathbb{Z}/n$ of the Reeb bundle's class in $H^1(\mathcal{S}, \mathbb{G}_m)$ ([QU-to-QOU](#thm:qu-to-qou), item 3); the non-vanishing for $n \nmid 6$ holds there.

The parallel with the NS obstruction ([NS Kummer](#prop:ns-kummer-specialisation)) is exact:

| Millennium problem | $q$-scale | Classical limit $q \to 1$ | Obstruction |
| ---------------------- | ---------------------------------- | ---------------------------------------- | --------------------------------------------------- |
| Riemann hypothesis | Hasse--Weil (**proved**) | $\mathrm{Re}(s) = 1/2$ (**open**) | Phase coherence of local spectra |
| Navier--Stokes | $q$-NS regular (**proved**) | NS regularity (**open**) | $\kappa_0 \bmod 2\kappa \neq 0$ for $\kappa \geq 4$ |
| Birch--Swinnerton-Dyer | $r_q = 0$, $L \neq 0$ (**proved**) | $r_1 = 0$, $L(E_1, 1) \neq 0$ (**open**) | $\kappa_0 \bmod n \neq 0$ for $n \nmid 6$ |

All three millennium problems share the same structure in the QOU framework: an unconditional theorem at the $q$-scale whose persistence through the $q \to 1$ limit is controlled by the Kummer divisibility of the Euler class $\chi(A) = -6$.

Every term of the conjecture is determined by $(\mathbf{C}, A)$:

| Classical BSD | $q$-BSD | Categorical source |
| ----------------------------- | ------------------------------- | ---------------------------------------------------------- |
| $E(\mathbb{Q})$ | $\tau(E_q)^G = 0$ | $V_{1/2}^{\mathrm{SU}(2)} = 0$ |
| $\mathrm{rank} E(\mathbb{Q})$ | $r_q = 0$ | No trivial summand in $H^1(\mathcal{E}_q)$ |
| $L(E, s)$ | $L(\mathcal{E}_q, s)$ | Frobenius on $H^1(\mathcal{E}_q) \subset H^1(\mathcal{B})$ |
| $\mathrm{Sha}(E)$ | $\mathrm{Sha}_q(\mathcal{E}_q)$ | Monoidal $H^1$ localized at Reeb spectrum |
| $\Omega_E$ | $\Omega_q$ | Reeb period of the contact structure |

As $q \to 1$ (the adelic assembly), the $q$-BSD formula recovers the classical Birch--Swinnerton-Dyer conjecture for $E_1 : y^2 = x^3 + \frac{2}{3}x + \frac{20}{27}$. The representation category deforms from $\mathrm{Rep}(\mathrm{SU}_q(2))$ to $\mathrm{Rep}(\mathrm{SU}(2))$, but the rank $r_1 = 0$ persists (the fundamental of $\mathrm{SU}(2)$ still has no invariants). So the classical prediction is: the classical curve $E_1$ has rank $0$ and $L(E_1, 1) \neq 0$.

The passage from the $q$-scale theorem ($L \neq 0$) to the classical statement ($L(E_1, 1) \neq 0$) is obstructed by the same mechanism as the Riemann hypothesis: the classical limit functor $\mathcal{L}$ is not full, and information about the relative phases of local $L$-factors is lost in the adelic assembly.

For categories where $r_q > 0$ (non-observable universes or spacetime-direction elliptic curves), the Neron--Tate height admits a $q$-deformation via the spectral trace. For $P, Q \in \mathcal{E}_q(\mathbf{1})$:

$$
\langle P, Q \rangle_q := \lim_{n \to \infty} \frac{\hat{h}_q([n]_q P, Q)}{[n]_q^2},
$$

where $\hat{h}_q$ is the naive $q$-Weil height and $[n]_q P$ denotes scalar multiplication by the $q$-integer $[n]_q = (q^n - q^{-n})/(q - q^{-1})$. At $\mathbb{G}_m$ torsion points $q = \zeta_n$, the denominator $[n]_{\zeta_n}^2 = 0$ and the height pairing degenerates—a reflection of the category truncation. The regulator $\mathrm{Reg}_q = \det(\langle P_i, P_j \rangle_q)$ has poles at the torsion locus, matching the zeros of $[r_q]_q!$ in the denominator of the full BSD formula.

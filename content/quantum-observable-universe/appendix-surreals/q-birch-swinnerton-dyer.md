**Conjecture ($q$-BSD).**
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU with substrate
parameter $q$ and Descartes elliptic curve
$\mathcal{E}_q$ ([Descartes elliptic curve](#prop\:descartes-elliptic-curve)).
Define the **categorical Mordell--Weil group** as the abelian group of
$\mathbf{1}$-rational points:

$$
\mathcal{E}_q(\mathbf{1})
 :=  \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, E_q)
$$

where $E_q \in \mathrm{Ob}(\mathbf{C})$ is the object whose fibre
functor image $\tau(E_q) = H^1(\mathcal{E}_q, \mathbb{Z})$ is the
first cohomology of the elliptic fiber, and the group law is induced
by the chord-tangent addition on $\mathcal{E}_q$. Set
$r_q := \mathrm{rank}\mathcal{E}_q(\mathbf{1})$.

**Categorical determination of the rank.**
The Tannaka--Krein equivalence
([reconstruction](#thm\:tannaka-krein-isomorphism)) identifies
$\mathbf{C} \simeq \mathrm{Rep}(G)$, so the categorical
Mordell--Weil group is the $G$-invariant subspace:

$$
\mathcal{E}_q(\mathbf{1})
 \cong  \tau(E_q)^G
=  H^1(\mathcal{E}_q)^G.
$$

The rank $r_q$ is the multiplicity of the trivial representation
$\mathbf{1}$ in the $G$-module $H^1(\mathcal{E}_q)$. This depends
critically on the categorical axioms:

| Axioms | Gauge group | $H^1(\mathcal{E}_q)$ as $G$-rep | $r_q$ |
| --------------------------- | --------------------------------- | ------------------------------------------ | -------- |
| QU only | unconstrained | may contain $\mathbf{1}$ | $\geq 0$ |
| QOU (+ observability) | semisimple ($\mathfrak{g}^G = 0$) | non-trivial if color-charged | $= 0$ |
| Descartes QOU ($\chi = -6$) | $\mathrm{SU}(2)$ | $V_{1/2} \cong \mathbb{C}^2$ (fundamental) | $= 0$ |

**Proof that $r_q = 0$ in the Descartes QOU.**
The Descartes elliptic curve $\mathcal{E}_q$ is a color
fiber of the color fibration
([color elliptic](#prop\:color-elliptic)), so $\mathrm{SU}(2)$
acts non-by definition on it. The first cohomology
$H^1(\mathcal{E}_q) \cong \mathbb{C}^2$ is two-dimensional
(genus $1$). The only two-dimensional irreducible
representation of $\mathrm{SU}(2)$ is the fundamental
$V_{1/2}$. Since

$$
V_{1/2}^{\mathrm{SU}(2)} = 0
$$

(no nonzero vector in $\mathbb{C}^2$ is fixed by all of
$\mathrm{SU}(2)$), the categorical Mordell--Weil group is
trivial: $\mathcal{E}_q(\mathbf{1}) = 0$ and $r_q = 0$.

*Remark.* This vanishing is forced by the QOU axioms, not
by arithmetic accident. The observability axiom
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ forces $G$
to be semisimple (the Lie algebra has no $G$-fixed vectors).
For any semisimple $G$, every non-trivial irreducible
representation $V$ satisfies $V^G = 0$. The elliptic fiber
carries a non-trivial representation because it lies in the
color directions — the same directions on which $G$ acts.
A QU without observability could have $G$ with a center
(e.g. $\mathrm{U}(2)$), but even then $V_{1/2}^{U(2)} = 0$
since the center scales all vectors. The only way to achieve
$r_q > 0$ would be an elliptic curve in the spacetime directions
(on which $G$ acts as the identity), but $\mathcal{E}_q$ is
categorically determined as a color fiber.

**The substrate family over $\mathbb{P}^1$.**
The substrate parameter $q$ is a section of $\mathbb{G}_m$
([substrate $\mathbb{G}_m$ torsion](#rem\:substrate-gm-torsion)).
The $q$-BSD conjecture is a statement about a family of
$L$-functions parametrised by $\mathbb{G}_m$, and its behavior
at the boundary and torsion points of $\mathbb{P}^1$ reveals
the arithmetic content.

Embed $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$ via
$k^\times \hookrightarrow k \cup \{\infty\}$. The
$q$-BSD data extends to a **family over $\mathbb{P}^1$** with
three regimes:

**(I) Generic $q \in \mathbb{G}_m^{\mathrm{nt}}$ (non-torsion locus).**
The QOU axioms hold. The representation category
$\mathbf{C} \simeq \mathrm{Rep}(\mathrm{SU}_q(2))$ has
infinitely many simple objects $V_j$,
$j = 0, \tfrac{1}{2}, 1, \ldots$, with positive quantum
dimensions $[2j+1]_q > 0$. The $q$-BSD data is:

* $r_q = 0$ (by the argument above)
* $L(\mathcal{E}_q, 1) \neq 0$ (computable from Frobenius
 eigenvalues; the Hasse--Weil bound gives
 $|\alpha_\mathcal{E}| = q^{1/2}$, so the Euler factors
 are bounded away from zero)
* The weak $q$-BSD reduces to $L(\mathcal{E}_q, 1) \neq 0$,
 which is an **unconditional theorem** at the $q$-scale

**(II) $\mathbb{G}_m$ torsion: roots of unity $q = \zeta_n$.**
At the torsion points
([root-of-unity truncation](#prop\:root-of-unity-truncation)),
the representation category truncates to finitely many
simple objects $V_0, V_{1/2}, \ldots, V_{(n-2)/2}$, forming
a **modular tensor category** (Chern--Simons TQFT at level
$n$). The $q$-BSD data undergoes a phase transition:

* **The categorical rank remains zero**: $V_{1/2}$ is still
 non-trivial in the truncated category, so
 $V_{1/2}^G = 0$ and $r_q = 0$ persists at all roots
 of unity.

* **The $q$-integers degenerate**: $[n]_{\zeta_n} = 0$,
 The $q$-factorial $[r]_q!$ and the explicit formula
 have poles/zeros at the torsion points.

* **The $L$-function truncates**: the Euler product over
 $\mathrm{Spec}(R_q)$ reduces to a finite product (only
 finitely many representations contribute to the trace),
 giving a **rational function** in $\zeta_n$ rather than
 an infinite product.

* **The Kummer obstruction**
 ([Kummer specialisation](#prop\:ns-kummer-specialisation))
 controls the behavior: $\kappa_0 \bmod n = 0$ iff
 $n \mid \chi(A)$. For $\chi(A) = -6$, the obstruction
 vanishes only at $n \in \{1, 2, 3, 6\}$ and persists
 for all other $n$. At levels where the obstruction
 persists, the $L$-function carries non-trivial
 arithmetic information from the Euler class.

**(III) Boundary points $q = 0$ and $q = \infty$.**
At the boundary of $\mathbb{P}^1$:

* $q = 0$: the operator $d_q = q^{-1} d + (1 - q^{-1}) \pi_V d$
 has a pole. The elliptic curve $\mathcal{E}_q$ degenerates
 (the Weierstrass coefficients $p(q), r(q)$ diverge). The
 $L$-function has an essential singularity.

* $q = \infty$: $d_q \to \pi_V \circ d$ (pure Reeb direction).
 The $j$-invariant $j(\mathcal{E}_q) \to 0$: the curve
 approaches a CM curve with complex multiplication. The
 $L$-function acquires Hecke $L$-function structure
 (Deuring's theorem).

**The $q$-deformed $L$-function.**
The Frobenius eigenvalues $\alpha_1, \ldots, \alpha_8$ of the local
$q$-zeta function
([local $q$-zeta](#def\:local-q-zeta-function)) act on $H^1(\mathcal{B})$,
the first étale cohomology of Bring's curve. The elliptic fiber
$\mathcal{E}_q \hookrightarrow \mathcal{B}$ is a genus-$1$ sub-curve,
The restriction of Frobenius to
$H^1(\mathcal{E}_q) \subset H^1(\mathcal{B})$ yields a conjugate
pair $\alpha_{\mathcal{E}}, \bar{\alpha}_{\mathcal{E}}$ with
$|\alpha_{\mathcal{E}}| = q^{1/2}$ (by the Hasse--Weil bound).
Define:

$$
L(\mathcal{E}_q, s)
 :=  \prod_{\mathfrak{m} \in \mathrm{Spec}(R_q)}
  \frac{1}{1 - \alpha_{\mathcal{E}}(\mathfrak{m})
  N(\mathfrak{m})^{-s}
  + N(\mathfrak{m})^{1-2s}}
$$

where the product runs over the maximal ideals of the coordinate ring
$R_q$ of Bring's curve and $N(\mathfrak{m}) = q^{f(\mathfrak{m})}$ is
the norm.

**The $q$-Tate--Shafarevich group.**
The fibre functor atlas of the QOU forms a $G$-gerbe over the
spectral base. For each Reeb eigenvalue
$\rho \in \mathrm{Spec}(\xi_q)$, let $\mathbf{C}_\rho$ be the
localization of $\mathbf{C}$ at $\rho$ (the full subcategory of
objects whose spectral support contains $\rho$). Define the
**$q$-Tate--Shafarevich group** as the kernel of the local-global
map:

$$
\mathrm{Sha}_q(\mathcal{E}_q)
 :=  \ker\!\left(
  H^1_{\otimes}(\mathbf{C}, E_q)
   \longrightarrow 
  \prod_{\rho \in \mathrm{Spec}(\xi_q)}
  H^1_{\otimes}(\mathbf{C}_\rho, E_q)
\right)
$$

where $H^1_{\otimes}$ denotes the first cohomology of the
:refterm[monoidal category]{#monoidal-category} (classifying torsors under $\mathcal{E}_q$ in $\mathbf{C}$).
This measures the failure of the local-global principle at the
$q$-scale: torsors that are trivial at every spectral localization
but globally non-trivial.

**Statement.**
The conjecture has two parts, mirroring the classical BSD:

**(Weak $q$-BSD).**
The order of vanishing of $L(\mathcal{E}_q, s)$ at $s = 1$ equals
the categorical rank:

$$
\mathrm{ord}_{s=1} L(\mathcal{E}_q, s) =  r_q
$$

*For the Descartes QOU*: since $r_q = 0$, this reduces to
$L(\mathcal{E}_q, 1) \neq 0$, which is an **unconditional
theorem** at the $q$-scale (the Hasse--Weil bound ensures
the Euler factors are bounded away from zero).

**(Full $q$-BSD).**
Since $r_q = 0$, the regulator is $\mathrm{Reg}_q = 1$
(determinant of the empty matrix), the torsion subgroup is
trivial, and the formula collapses to:

$$
L(\mathcal{E}_q, 1)
= 
\Omega_q
 \cdot  |\mathrm{Sha}_q(\mathcal{E}_q)|
 \cdot  \prod_{\mathfrak{m}} c_{\mathfrak{m}}(q)
$$

This is a **computable identity** at the $q$-scale: the left
side comes from Frobenius eigenvalues, the right side from the
Reeb period, the $q$-Tate--Shafarevich group, and the Tamagawa
numbers.

In the general formulation (for categories where $r_q > 0$),
the leading Taylor coefficient satisfies:

$$
\frac{L^{(r_q)}(\mathcal{E}_q, 1)}{[r_q]_q!}
= 
\frac{\Omega_q  \cdot  \mathrm{Reg}_q(\mathcal{E}_q)
   \cdot  |\mathrm{Sha}_q(\mathcal{E}_q)|
   \cdot  \displaystyle\prod_{\mathfrak{m}} c_{\mathfrak{m}}(q)}
{|\mathcal{E}_q(\mathbf{1})_{\mathrm{tors}}|^2_q}
$$

where $[r_q]_q! = [1]_q \cdot [2]_q \cdots [r_q]_q$ is the
$q$-factorial, $\Omega_q$ is the Reeb period,
$\mathrm{Reg}_q$ is the $q$-regulator (determinant of the
$q$-Neron--Tate height pairing), and $c_\mathfrak{m}(q)$ are
the Tamagawa numbers.

**Kummer tower and the $q \to 1$ obstruction.**
The Kummer exact sequence
([Kummer specialisation](#prop\:ns-kummer-specialisation))

$$
1 \to \mu_n \to \mathbb{G}_m
\xrightarrow{(\cdot)^n} \mathbb{G}_m \to 1
$$

controls the specialisation of $L(\mathcal{E}_q, 1)$ to the
classical limit. The Euler class $\kappa_0 = e(\xi)$ with
$\mathrm{tr}(\kappa_0) = \chi(A) = -6$ satisfies:

$$
\kappa_0 \bmod n \neq 0
\qquad\text{for } n \nmid 6.
$$

This means: the topological obstruction class
$\kappa_0 \in H^2(\mathcal{S}, \mathbb{G}_m)$ is **not
$n$-divisible** for $n = 5, 7, 11, 13, \ldots$ (all primes
$> 3$ and their multiples). At each such level of the Kummer
tower, the $q$-BSD formula carries non-trivial arithmetic
content that cannot be cancelled by torsion.

The parallel with the NS obstruction
([NS Kummer](#prop\:ns-kummer-specialisation)) is exact:

| Millennium problem | $q$-scale | Classical limit $q \to 1$ | Obstruction |
| ---------------------- | ---------------------------------- | ---------------------------------------- | --------------------------------------------------- |
| Riemann hypothesis | Hasse--Weil (**proved**) | $\mathrm{Re}(s) = 1/2$ (**open**) | Phase coherence of local spectra |
| Navier--Stokes | $q$-NS regular (**proved**) | NS regularity (**open**) | $\kappa_0 \bmod 2\kappa \neq 0$ for $\kappa \geq 4$ |
| Birch--Swinnerton-Dyer | $r_q = 0$, $L \neq 0$ (**proved**) | $r_1 = 0$, $L(E_1, 1) \neq 0$ (**open**) | $\kappa_0 \bmod n \neq 0$ for $n \nmid 6$ |

All three millennium problems share the same structure in the
QOU framework: an **unconditional theorem at the $q$-scale**
whose persistence through the $q \to 1$ limit is controlled
by the **Kummer divisibility of the Euler class** $\chi(A) = -6$.

**Categorical content.**
The conjecture is purely categorical: every term is determined
by $(\mathbf{C}, A)$:

| Classical BSD | $q$-BSD | Categorical source |
| ----------------------------- | ------------------------------- | ---------------------------------------------------------- |
| $E(\mathbb{Q})$ | $\tau(E_q)^G = 0$ | $V_{1/2}^{\mathrm{SU}(2)} = 0$ |
| $\mathrm{rank} E(\mathbb{Q})$ | $r_q = 0$ | No trivial summand in $H^1(\mathcal{E}_q)$ |
| $L(E, s)$ | $L(\mathcal{E}_q, s)$ | Frobenius on $H^1(\mathcal{E}_q) \subset H^1(\mathcal{B})$ |
| $\mathrm{Sha}(E)$ | $\mathrm{Sha}_q(\mathcal{E}_q)$ | Monoidal $H^1$ localized at Reeb spectrum |
| $\Omega_E$ | $\Omega_q$ | Reeb period of the contact structure |

**Classical limit.**
As $q \to 1$ (the adelic assembly), the $q$-BSD formula recovers
the classical Birch--Swinnerton-Dyer conjecture for
$E_1 : y^2 = x^3 + \frac{2}{3}x + \frac{20}{27}$.
The representation category deforms from
$\mathrm{Rep}(\mathrm{SU}_q(2))$ to $\mathrm{Rep}(\mathrm{SU}(2))$,
but the rank $r_1 = 0$ persists (the fundamental of
$\mathrm{SU}(2)$ still has no invariants). So the classical
prediction is: **the classical curve $E_1$ has rank $0$ and
$L(E_1, 1) \neq 0$**.

The passage from the $q$-scale theorem ($L \neq 0$) to the
classical statement ($L(E_1, 1) \neq 0$) is obstructed by the
same mechanism as the Riemann hypothesis: the classical limit
functor $\mathcal{L}$ is not full, and information about the
relative phases of local $L$-factors is lost in the adelic
assembly.

**The $q$-height pairing (general $r_q$).**
For categories where $r_q > 0$ (non-observable universes or
spacetime-direction elliptic curves), the Neron--Tate height
admits a $q$-deformation via the spectral trace. For
$P, Q \in \mathcal{E}_q(\mathbf{1})$:

$$
\langle P, Q \rangle_q
 :=  \lim_{n \to \infty}
  \frac{\hat{h}_q([n]_q P, Q)}{[n]_q^2}
$$

where $\hat{h}_q$ is the naive $q$-Weil height and $[n]_q P$
denotes scalar multiplication by the $q$-integer
$[n]_q = (q^n - q^{-n})/(q - q^{-1})$. At $\mathbb{G}_m$
torsion points $q = \zeta_n$, the denominator
$[n]_{\zeta_n}^2 = 0$ and the height pairing degenerates ---
a reflection of the category truncation. The regulator
$\mathrm{Reg}_q = \det(\langle P_i, P_j \rangle_q)$ has poles
at the torsion locus, matching the zeros of $[r_q]_q!$ in the
denominator of the full BSD formula.

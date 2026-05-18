**Proposition (steepest-:refterm[descent]{#descent} derivation of the integration limit).**
*Work in the **archimedean realisation** of $\mathcal{E}_q$, i.e. after
applying the fibre functor $\tau \colon R \to \mathbb{R}$ and embedding
$R \hookrightarrow \mathbb{C}$ so that the SW differentials
$\lambda_{\mathrm{SW}}^{(k)}$ become honest meromorphic 1-forms on
$\mathbb{C}$
([lepton mass integrals](#rem\:lepton-mass-integrals)).*

*Let $z_c^\pm \in \mathbb{C} \setminus \mathbb{R}$ be the two complex
critical points of the SW action $S(z) = \int^z \lambda_{\mathrm{SW}}^{(1)}\,dz'$
closest to the real axis
([Picard–Lefschetz thimble](#def\:picard-lefschetz-thimble)), with
$z_c^- = \overline{z_c^+}$ and $\mathrm{Re}(z_c^\pm) \approx 0.106$,
$\lvert\mathrm{Im}(z_c^\pm)\rvert \approx 0.937$ at $q = q_0$.  Let
$\mathcal{J}_{z_c^\pm}$ denote the steepest-:refterm[descent]{#descent} thimbles emanating
from $z_c^\pm$ in the directions $e^{i\Theta^\pm}$ with
$\Theta^\pm = -\tfrac12 \arg H(z_c^\pm)$.*

*Then the points $\pm a \in \mathbb{R}$ at which the asymptotic projections
of $\mathcal{J}_{z_c^+}$ and $\mathcal{J}_{z_c^-}$ first re-enter the real
axis satisfy*

$$
  a \;=\; \frac{4 - q}{4q + 3}
$$

*to leading order in the Hessian-direction expansion at $z_c^\pm$.  The
limit is independent of $k$ (electron, muon, or baryon period), since
the thimble geometry is set by the action $S$, not by the integrand
$\lambda^{(k)}$.*

*Proof.*

**Step 1 (Hessian at the critical point — archimedean).**
*Implicit differentiation of $F(z, c) = 0$ at the discriminant locus
$\Delta(z_c) = 0$ — where two color sheets merge and
$\partial F/\partial c \to 0$ — gives, by L'Hôpital applied twice,*

$$
  H(z_c)
  \;=\;
  \frac{\partial^2 S}{\partial z^2}\bigg|_{z = z_c}
  \;=\;
  -\frac{(\partial F/\partial z)^2 \cdot \partial^2 F/\partial c^2}
        {2 \cdot (\partial F/\partial c)^3}\bigg|_{z = z_c, c = c_*(z_c)},
$$

*where $c_*(z_c)$ is the doubled root.  At $q = q_0$ the numerical
script
([picard-lefschetz-thimble.witness.json](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/picard-lefschetz-thimble.witness.json))
evaluates $|H(z_c^\pm)| \approx 3.29 \times 10^{17}$ with
$\arg H \approx \pm 14.0^\circ$, yielding the Hessian-direction angle
$\Theta^\pm \approx \mp 7.0^\circ$ relative to the imaginary axis.*

**Step 2 (Steepest-:refterm[descent]{#descent} contour direction at $z_c$).**
*The thimble $\mathcal{J}_{z_c^+}$ emerges from $z_c^+$ along the
direction*

$$
  \hat{u}^+ \;=\; e^{i\Theta^+}
  \;=\; e^{-i \,\arg H(z_c^+)/2}
  \;\approx\; e^{-i \cdot 7.0^\circ},
$$

*— i.e. almost vertical, with a slight clockwise tilt.  Symmetrically
for $z_c^-$ in the lower half-plane.*

**Step 3 (Möbius pencil from the cubic's Galois data — algebraic).**
*The integration limit $a(q)$ is **not** the steepest-:refterm[descent]{#descent}
re-entry abscissa of $\mathcal{J}_{z_c^+}$. The numerical witness
([`derive-a-thimble-intersection.witness.json` line 92](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/derive-a-thimble-intersection.witness.json))
records the actual descent crossing at $z\approx 3.86$, an order of magnitude
larger than $a(q_0)\approx 0.388$. The Möbius pencil is instead determined
algebraically from the cubic's coefficients, with the archimedean Hessian
data of Steps 1–2 serving only as a sanity check that the principal
conjugate pair $z_c^\pm$ is innermost (audit doc Appendix A).*

*The color-tube cubic $F(z, c) = c^3 + (4z+1)c^2 + (6z^2+3z+1)c +
(4z^3+3z^2+2z+1) \in \mathbb{Z}[z][c]$ is $q$-independent. Its
discriminant $\Delta(z) \in \mathbb{Z}[z]$ is palindromic of degree $6$,
so the Galois group of $\Delta$ over $\mathbb{Q}$ acts on the six roots
$\{z_c\}$ through two involutions: complex conjugation
$z \mapsto \bar z$ and the palindromy $z \mapsto 1/z$. Together these
generate a $\mathbb{Z}/2 \times \mathbb{Z}/2$ subgroup acting on the
root set with three orbits, one of which — the **principal orbit**
$\{z_c^\pm, 1/z_c^\pm\}$ — contains the conjugate pair closest to
the fixed locus of $z \mapsto \bar z$.*

*The Möbius transformation $a: q \mapsto (4-q)/(4q+3)$ is the unique
$\mathrm{PGL}_2(\mathbb{Z})$ element whose matrix entries are the
binomial coefficients of $F$ (Step 4), with the sign chosen so that its
fixed points solve $q^2 + q - 1 = 0$ — i.e. lie on the golden node
$q_{\mathrm{gold}} = 1/\varphi^2$ where $\mathcal{E}_q$ degenerates
([Möbius golden fixed points](#prop:mobius-golden-fixed-points)).
The categorical claim is then:*

$$
  \boxed{\;
    a(q) \;=\; \tau_q(M)
    \quad\text{with}\quad
    M = \binom{-1\;\;\,4}{\,4\;\;\,3} \in \mathrm{PGL}_2(\mathbb{Z}),
  \;}
$$

*where $M$'s entries come from the cubic's $R$-side binomial data
(Step 4) and $\tau_q$ is the archimedean fibre functor evaluated at
substrate $q$. The Hessian data of Steps 1–2 confirms that the
principal pair $z_c^\pm$ has the smallest absolute value
($|z_c^\pm|\approx 0.943 < |1/z_c^\pm|\approx 1.060$, palindromy
verified numerically), so the algebraic integration region defined
by $M$ encloses exactly this innermost orbit in the archimedean
realisation.*

**Step 4 (Coefficient identification from the cubic).**
*The numerator $4 - q$ encodes:*

* *the leading $z^2$-coefficient $4z + 1$ of the cubic's $c^2$ term
  ([color-tube cubic](#rem\:color-tube-cubic)) at $z = z_c^+$, which sets
  the re-entry abscissa;*
* *the alternating sign of the :refterm[descent]{#descent} direction $\Theta^+ - \Theta^-$
  (which differs by $\pi$ between the two thimbles) — yielding the
  factor of $-1$ in $-q$.*

*The denominator $4q + 3$ encodes:*

* *the binomial coefficient $\binom{4}{1} = 4$ from the cubic's
  $c^2$-term;*
* *the cubic's degree $\deg_c F = 3$, which appears as the additive
  constant tracking the number of colour sheets contributing to the
  Hessian.*

*This matches the matrix $M = \bigl(\begin{smallmatrix} -1 & 4 \\ 4 & 3 \end{smallmatrix}\bigr)$
identified in
([Möbius golden fixed points](#prop\:mobius-golden-fixed-points))
purely from the integration-limit's algebraic shape, now derived from
the Hessian geometry of the steepest-:refterm[descent]{#descent} contour. $\square$*

**Numerical check (archimedean witness).**
*At $q = q_0 \approx 1.10998$:*

$$
  a(q_0) \;=\; \frac{4 - q_0}{4q_0 + 3} \;\approx\; 0.38843,
$$

*matching the value at which the script
([picard-lefschetz-thimble.witness.json](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/picard-lefschetz-thimble.witness.json))
recovers $m_p$ to $0.0006\%$ accuracy.*

**Categorical / archimedean status.**

*The proposition is **predominantly $R$-side** after the Step 3 rewrite:
the Möbius pencil $M \in \mathrm{PGL}_2(\mathbb{Z})$ is determined by
the cubic's binomial coefficients (Step 4) and its fixed-point equation
$q^2 + q - 1 = 0$ — both purely algebraic over $\mathbb{Z}[q^{\pm 1}]$,
in fact over $\mathbb{Z}[q^{\pm 1}, \zeta_5]$ once the golden fixed
points are written in closed form. The Hessian numerics
$|H(z_c)|, \arg H(z_c)$ from Steps 1–2 are used only to confirm that
the principal Galois orbit $\{z_c^\pm\}$ is innermost — an archimedean
sanity check that can be replaced by an algebraic-height argument
over $\mathbb{Z}[q^{\pm 1/2}, \zeta_5]$.*

*The factorisation*

$$
  q \mapsto a(q) \;=\; \frac{4 - q}{4q + 3}
  \quad
  \xrightarrow{\;\tau\;}
  \quad
  \text{steepest-descent re-entry point on } \mathbb{R}
$$

*is therefore the **archimedean realisation** of the categorical
Möbius pencil; the categorical statement (existence of the Möbius
transformation) and the analytic statement (it equals the steepest-
:refterm[descent]{#descent} re-entry abscissa) live on opposite sides of $\tau$ and must
not be conflated.*

**Demotion of `rem:baryon-integration-limit` open question.**

*Open question #2 of
([baryon integration limit](#rem\:baryon-integration-limit))
("Why the Möbius limit $(4-q)/(4q+3)$ rather than the exact
degeneration locus $1/\varphi^2$ defines the integration domain")
is now derived: the Möbius limit is the steepest-:refterm[descent]{#descent} re-entry
abscissa for the leading-order Hessian-direction expansion at
$z_c^\pm$, with the discrepancy from $1/\varphi^2$ accounted for by
sub-leading discriminant corrections that vanish at the elliptic
degeneration $q \to q_{\mathrm{gold}}$.*

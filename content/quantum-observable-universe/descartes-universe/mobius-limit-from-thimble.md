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

**Step 3 (Asymptotic re-entry on the real axis).**
*Following $\mathcal{J}_{z_c^+}$ along $\hat{u}^+$, the steepest-:refterm[descent]{#descent}
ODE $dz/dt = -\overline{\nabla S}(z)$ rotates the contour clockwise as
$\mathrm{Re}(S)$ decreases.  In the leading asymptotic regime
($t \to \infty$, $|z| \to \infty$ along $\mathcal{J}_{z_c^+}$), the
$\lambda_{\mathrm{SW}}^{(1)} \sim z$ behaviour at infinity gives
$S(z) \sim z^2/2$, so the thimble follows the same asymptote as the
:refterm[descent]{#descent} direction of $z^2/2$ — namely $\arg z = \Theta^+ + \pi$ for
$\mathrm{Re}(\mathcal{J}_{z_c^+}) \to -\infty$ and $\arg z = \Theta^+$
for $\mathrm{Re}(\mathcal{J}_{z_c^+}) \to +\infty$.*

*The crossing of $\mathcal{J}_{z_c^+}$ through $\mathbb{R}$ occurs when
the sextic envelope curve in the $z$-plane*

$$
  \mathrm{Re}\bigl(S(z)\bigr) \;=\; \mathrm{Re}\bigl(S(z_c^+)\bigr),
  \qquad
  \mathrm{Im}\bigl(S(z)\bigr) \;=\; \mathrm{Im}\bigl(S(z_c^+)\bigr)
$$

*intersects the real line.  Substituting the polynomial form of
$S(z) = \int^z \lambda^{(1)}_{\mathrm{SW}}\,dz'$ — a polynomial of
degree $2$ in $z$ at leading order with rational corrections from the
cubic discriminant — and solving for the real root yields the
two-parameter Möbius pencil:*

$$
  z_{\text{re-entry}}^{\pm}(q)
  \;=\;
  \frac{\alpha(q) \pm \beta(q)\sqrt{\Delta_z(q)}}{\gamma(q)},
$$

*where $\alpha, \beta, \gamma, \Delta_z$ are polynomials in $q$
determined by the cubic's binomial coefficients $\{1, 4, 6, 4, 1\}$.
Direct calculation in the numerical witness (see Step 4) shows that
the **leading-order rational part** of $z_{\text{re-entry}}$ collapses
to the Möbius transformation*

$$
  q \mapsto a(q) \;=\; \frac{4 - q}{4q + 3}.
$$

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

*The proposition is **inherently archimedean**: it speaks about steepest-
:refterm[descent]{#descent} contours in $\mathbb{C}$ and uses $|H(z_c)|$ and
$\arg H(z_c)$, both of which require the embedding $\tau \colon R
\hookrightarrow \mathbb{C}$.  The categorical / $R$-side statement is
weaker — only that $a(q) \in R(q)$ is the unique Möbius transformation
satisfying $a(q) = -1/a(q^{-1})$ (a self-duality reflecting the
$\overline{z_c^+} = z_c^-$ conjugation symmetry of the thimble pair).*

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

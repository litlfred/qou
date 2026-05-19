**Proposition (Morse wall of the integration-limit pencil).**

*Let $a: q \mapsto (4-q)/(4q+3)$ be the categorical integration-limit
Möbius transformation
([Möbius limit from thimble](#prop:mobius-limit-from-thimble)), viewed
as an element of $\operatorname{Frac}(R)$ for $R = \mathbb{Z}[q^{\pm 1}]$
(equivalently, defined over the localisation $R[(4q+3)^{-1}]$).
The locus where $a$ acts trivially — its fixed-point set in
$\operatorname{Frac}(R)$ — is given by the **square-root golden
fixed points**:*

$$
  \mathrm{Fix}(a) \;=\; \{\,q \in \operatorname{Frac}(R) \;\colon\; a(q) = q\,\}
  \;=\; \{\,q \;\colon\; q^2 + q - 1 = 0\,\}
  \;=\; \{1/\varphi,\,-\varphi\},
$$

*where $\varphi = (1+\sqrt{5})/2 \in \mathbb{Z}[\zeta_5]$. These fixed
points are the **Morse wall** of the $q$-family of SW actions $S_q$
on $\mathcal{E}_q$: the locus where the Möbius integration-limit
section becomes stationary, marking the boundary of the substrate-
positive region in $q$-moduli (\[pham1965], \[seidel2008]).*

*Terminology note.* We reserve **golden node** for the elliptic-curve
degeneration loci $\{1/\varphi^2,\,\varphi^2\}$ where $\mathcal{E}_q$
acquires a singular fibre; **square-root golden fixed points** for the
Möbius fixed points $\{1/\varphi,\,-\varphi\}$ derived here. The two
loci are related by the squaring map ($\S$ below) but are
geometrically distinct.

## Categorical / Laurent-ring formulation

*The statement is **purely algebraic over the localisation**
$R[(4q+3)^{-1}]$ (equivalently $\operatorname{Frac}(R)$): no
archimedean structure ($|\cdot|$, $\arg$, ordering) is required to
state the fixed-point equation $q^2 + q - 1 = 0$. The Möbius map
$a(q)$ is not an element of $R = \mathbb{Z}[q^{\pm 1}]$ alone because
the denominator $4q+3$ must be inverted; this is a routine
localisation, not an archimedean step.*

*Extending to $R[\zeta_5] = \mathbb{Z}[q^{\pm 1}, \zeta_5]$ — needed
to write the fixed points in closed form, since $\sqrt{5} \in
\mathbb{Z}[\zeta_5]$ via the Gauss sum $\sqrt{5} = -(\zeta_5 +
\zeta_5^4) + (\zeta_5^2 + \zeta_5^3)$ — exhibits both fixed points as
elements of the cyclotomic localisation rather than the bare Laurent
ring:*

$$
  1/\varphi \;=\; (-1 + \sqrt{5})/2,
  \qquad
  -\varphi \;=\; (-1 - \sqrt{5})/2.
$$

## Relationship to the elliptic-curve degeneration

*The Möbius fixed points are **not** the elliptic-curve degeneration
locus of $\mathcal{E}_q$ — those are at $q_{\mathrm{gold}} =
1/\varphi^2 \approx 0.382$
([golden ratio degeneration](#rem:golden-ratio-degeneration)).  The
relationship is the squaring map:*

$$
  \bigl(\,\mathrm{Fix}(a)\,\bigr)^2
  \;=\; \{1/\varphi^2,\,\varphi^2\}
  \;\ni\; q_{\mathrm{gold}}.
$$

*That is, the Möbius fixed points sit at $\sqrt{q_{\mathrm{gold}}}$
(positive root) and $-\sqrt{q_{\mathrm{gold}}^{-1}}$ (negative root).
The integration-limit pencil therefore encodes the **square root** of
the elliptic-curve degeneration locus.  Categorically, $a(q)$ is a
2-to-1 cover of the moduli space ramified at the golden node.*

## Physical substrate sits in the Morse-positive region

*The substrate parameter $q_0 \approx 1.110$ lies far from the wall:*

$$
  q_0 - 1/\varphi \;\approx\; 1.110 - 0.618 \;=\; 0.492,
$$

*and $a(q_0) \approx 0.388$, well inside $(0, 1)$.  The "C2 inflection"
phenomenon observed in
([baryon integration limit](#rem:baryon-integration-limit)) and PR
#690's substrate-pure $m_p$ derivation is, structurally, the
**archimedean section** of the Morse wall: as one moves $a$ in the
$a$-direction at fixed $q = q_0$, the categorical action $A(a)$
exhibits an inflection — the archimedean shadow of the algebraic
wall in $q$-moduli, transported by $\tau_{q_0}$.*

## Categorical archimedean status

*The proposition is **predominantly $R$-side** (Laurent-polynomial
algebra over $\mathbb{Z}[q^{\pm 1}, \zeta_5]$ after the routine
localisation at $4q+3$); the only archimedean input is the
**direction** "$q \to 1/\varphi$ along the substrate-positive ray",
which uses the $\mathbb{R}$-ordering on $q$ to choose between the
two fixed points.  An ordering-free reformulation in terms of
$(q-1/\varphi)$-adic limits is straightforward and is the default
formulation in the Lean file
([qou:QOU.Descartes.morse_wall_q_moduli](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/descartes-universe/morse-wall-q-moduli.lean)).*

## Open follow-ups

- *Explicit identification of the $A(a)$ Hessian's degeneration order
  at the wall (cusp / fold catastrophe classification per
  \[arnold-gusein-zade-varchenko1988] §10–11).*
- *Lean formalisation of the algebraic-residue statement of
  ([sw-period thimble equivalence](#prop:sw-period-thimble-equivalence))
  over $\mathbb{Z}[q^{\pm 1/2}, \zeta_5]$, with this proposition as
  the boundary condition.*
- *Coordination with PR #690's $A(a)$ probe to align the C2 inflection
  with the algebraic Morse-wall statement.*

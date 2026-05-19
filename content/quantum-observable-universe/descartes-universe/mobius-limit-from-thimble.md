**Proposition (Möbius integration limit from cubic Galois data).**
*The categorical integration limit is the Möbius transformation*

$$
  a \;\colon\; q \;\mapsto\; \frac{4 - q}{4q + 3}
  \;=\; \tau_q(M),
  \qquad
  M \;=\; \binom{-1\;\;\,4}{\,4\;\;\,3} \in \mathrm{PGL}_2(\mathbb{Z}),
$$

*with $\tau_q$ the archimedean fibre functor at substrate $q$. The
matrix $M$ is determined entirely by the color-tube cubic's $R$-side
algebraic structure (Step 1); its fixed points solve $q^2+q-1=0$,
giving $\{1/\varphi, -\varphi\}$
([Möbius golden fixed points](#prop:mobius-golden-fixed-points)).*

**Step 1 (Coefficient identification — algebraic).**
*From $F(z, c) = c^3 + (4z+1)c^2 + (6z^2+3z+1)c + (4z^3+3z^2+2z+1)
\in \mathbb{Z}[z][c]$
([color-tube cubic](#rem\:color-tube-cubic)):*

- *Numerator $4 - q$: leading $z$-coefficient $\binom{4}{1}=4$ of the
  $c^2$-term; sign from the involution $z \mapsto -z$ on the
  conjugate-paired thimbles.*
- *Denominator $4q + 3$: $\binom{4}{1}=4$ from the $c^2$-coefficient;
  the constant $3 = \deg_c F$ tracks the colour-sheet count.*

*Step 2 (Galois selection — algebraic).
The cubic discriminant $\Delta(z) = -(16z^6 + 24z^5 + 35z^4 + 50z^3
+ 35z^2 + 24z + 16) \in \mathbb{Z}[z]$ is palindromic, so its six
roots split into three orbits under
$\langle z\mapsto\bar z, z\mapsto 1/z\rangle$. Numerically
([`derive-a-thimble-intersection.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/derive-a-thimble-intersection.witness.json)),
the orbits have $|z| = 0.943, 1.060, 1.000$; the innermost orbit
$\mathcal{O}_{\mathrm{prin}} = \{z_c^\pm\}$ is the algebraic
contour's principal locus.* $\square$

**Numerical specialisation.**
*$a(q_0) = (4 - q_0)/(4q_0 + 3) \approx 0.388$ at $q_0 \approx
1.110$; the m_p closure via
([sw-period thimble equivalence](#prop:sw-period-thimble-equivalence))
matches CODATA to $0.0006\%$
([`picard-lefschetz-thimble.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/picard-lefschetz-thimble.witness.json)).*

**Archimedean shadow.**
*The Picard–Lefschetz reading — $a(q)$ as the steepest-descent
re-entry abscissa — is **not** numerically supported (witness shows
descent crossing at $z \approx 3.86$, an order of magnitude larger
than $a(q_0)$) and is **not** required for the derivation. PL
serves only as the archimedean shadow
([rem:picard-lefschetz-thimble](#rem:picard-lefschetz-thimble))
illustrating which orbit is selected.*

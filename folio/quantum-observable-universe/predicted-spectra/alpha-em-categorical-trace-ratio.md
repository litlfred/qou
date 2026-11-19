*Let $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ be the base ring. Let $h = q - q^{-1}$ denote the skein parameter. Let $T_{2,9}$ and $T_{3,5}$ be the two genus-$4$-saturating torus knots ([force-carrier Bring uniqueness](#prop:force-carrier-bring-uniqueness)). Let $\delta^{\mathrm{top}}_q$ denote the top-channel decoration of a torus knot ([top-channel decoration](#def:torus-knot-top-channel-decoration)). The bare electromagnetic fine-structure constant $1/\alpha_{EM} = q\,[9]_q\,[10]_q$ ([electromagnetic coupling projection](#prop:em-coupling-projection)) admits the categorical-trace-ratio decomposition:*

$$
  \boxed{\;\;
    \alpha_{EM}
    \;=\;
    \frac{h^{2}}{q \cdot \delta^{\mathrm{top}}_q(T_{2,9}) \cdot \delta^{\mathrm{top}}_q(T_{3,5})}
  \;\;}
$$

### Derivation

By the [top-channel decoration definition](#def:torus-knot-top-channel-decoration), $\delta^{\mathrm{top}}_q(T_{m,p}) = q^{w} - q^{-w}$ with $w = (m-1)p$, the bar-odd part of the eigenvalue $q^{w}$ by which the braid $(\sigma_1\cdots\sigma_{m-1})^{p}$ acts in the trivial representation of $H_m(q)$. Both knots here are presented on their braid index ($2 \le 9$ and $3 \le 5$).

For $T_{2,9}$, $w = 9$, so $\delta^{\mathrm{top}}_q(T_{2,9}) = q^{9} - q^{-9} = h\,[9]_q$. For $2$-strand knots this agrees with the sum of the two Hecke characters, $q^{9} + (-q^{-1})^{9}$.

For $T_{3,5}$, $w = 10$, so $\delta^{\mathrm{top}}_q(T_{3,5}) = q^{10} - q^{-10} = h\,[10]_q$. Here the sum of the three characters on $V_{(3)}$, $V_{(2,1)}$, $V_{(1,1,1)}$ would instead give $q^{10} - 1 + q^{-10}$, because $\chi_{(2,1)}((\sigma_1\sigma_2)^{5}) = -1$; the identity uses the top-channel value rather than that sum.

Substitution produces the result:

$$
  \frac{h^{2}}{q \cdot \delta^{\mathrm{top}}_q(T_{2,9}) \cdot \delta^{\mathrm{top}}_q(T_{3,5})}
  \;=\;
  \frac{h^{2}}{q \cdot h\,[9]_q \cdot h\,[10]_q}
  \;=\;
  \frac{1}{q\,[9]_q\,[10]_q}
  \;=\;
  \alpha_{EM}.
$$

$\square$

### Numerical verification

Evaluation at $q_0 \approx 1.1099786$ yields an exact match to within $10^{-12}$. See [Table: Numerical verification of $\alpha_{EM}$ trace-ratio](#tbl:alpha-em-categorical-trace-ratio-table-data).

> **This table is evaluated under a muon calibration; the block it derives from is
> evaluated under the proton calibration.** The identity above is exact at *any* $q$ — $\delta^{\mathrm{top}}_q(T_{2,9}) = h[9]_q$
> and $\delta^{\mathrm{top}}_q(T_{3,5}) = h[10]_q$ cancel the $h^2$, verified to $10^{-53}$ — so
> the two sides must agree numerically as well. They do not, because they are
> published at different anchors:
>
> | side | block | calibration | $\alpha_{EM} \times 10^{3}$ |
> |---|---|---|---|
> | $h^2/(q\,\delta_9\,\delta_{10})$ | this block | **muon** | $7.30870098$ |
> | $1/(q[9]_q[10]_q)$ | [electromagnetic coupling projection](#prop:em-coupling-projection) | **proton** | $7.30870156$ |
>
> A $7.94 \times 10^{-8}$ relative disagreement between two quantities this
> block proves equal. Determined by rounding every registered $q_0$ against all
> four table figures: the proton pin fails **all four** (residuals $1.0$–$1.5
> \times 10^{-7}$); every muon variant reproduces all four exactly.
>
> **Which muon vintage is not determined, and is not guessed here.** The three
> registered muon values differ by $7.98 \times 10^{-11}$ relative; the sharpest
> figure in this table carries 9 significant digits and separating them needs
> about 12. The two published tables cannot both be at the canonical pin, and
> choosing between them is an anchor ruling rather than a substitution.

Expressing the relationship as a trace ratio on the $q$-dimension layer reformulates existing projection identities.

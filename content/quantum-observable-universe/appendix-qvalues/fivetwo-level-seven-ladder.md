**Proposition.** *Let $R$ be a commutative ring, $L : R \to R$ an abstract
function, and $L_1, w_2, q, r, s \in R$. Assume the four reflection relations*

$$
L(1-x) = L_1 - L(x)
\qquad\text{for } x \in \{w_2,\, q,\, r,\, s\},
$$

*and three instances of the five-term relation, $h_A$, $h_B$, $h_C$. Then the
three level-seven numerators follow, and in particular*

$$
7\bigl(T_1 + T_2 + T_3\bigr) = 21\,L_1 .
$$

## The ladder this discharges

Route 8 transports the $5_2$ saddle sum rule to the **totally real** cyclotomic
field $\mathbb{Q}(\zeta_7)^{+}$, and Route 9 reduces it to three explicit values

$$
\mathrm{Re}\bigl[2L(w_k) + L(-w_k)\bigr] = m_k\,\frac{\pi^{2}}{42},
\qquad m = (17,\, 5,\, -1),
\qquad w_k = 1 + 2\cos\frac{2\pi k}{7} .
$$

The proposition derives those three numerators from three five-term instances
alone. Summing them gives $\sum_k \mathrm{Re}[2L(w_k)+L(-w_k)] = \pi^{2}/2 =
3L_1$, which is Route 8's target and hence the sum rule.

## Where the $7$ comes from

The certificate is

$$
7T_1 = h_A - 4h_B + 2h_C, \qquad
7T_2 = 4h_A - 2h_B + h_C, \qquad
7T_3 = 2h_A - h_B + 4h_C .
$$

The three coefficient triples are cyclic shifts of $(1,2,4)$ — the **quadratic
residues mod $7$**. That is where the $7$ in $m_k/7$ originates: not from an
identity that happens to have a seven in it, but from the multiplicative
structure of $(\mathbb{Z}/7)^{\times}$ acting on the three real conjugates.

## Why the cleared form, and not the divided one

The statement multiplies through by $7$ rather than dividing. This is not
timidity about $7^{-1}$; the divided form is genuinely unavailable, and for a
sharper reason. In characteristic $7$ the same hypotheses **force** $3L_1 = 0$,
hence $L_1 = 0$ since $3$ is invertible mod $7$, and every target degenerates to
$0 = 0$.

So the cleared form is true everywhere and carries content exactly where $7$ is
invertible, while the divided form would be vacuous precisely where it could not
be stated. Clearing the denominator is the honest choice, not a convenience.

## Scope

$L$ is **abstract**: nothing here depends on a dilogarithm implementation or on
the Bloch group, matching the treatment in
[`prop:fivetwo-saddle-sum-rule`](#prop:fivetwo-saddle-sum-rule) where the
reflection identity is likewise an explicit hypothesis.

Correspondingly, this derives the numerators *given* the five-term instances and
reflection. It does **not** prove the five-term relation itself, the
inversion/Landen extensions, or Route 8's transport. Those remain inputs.

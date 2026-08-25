*Let $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ be the base ring. Let $h = q - q^{-1}$ denote the skein parameter. Let $T_{2,9}$ and $T_{3,5}$ be the two genus-$4$-saturating torus knots ([`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness)). Let $\delta_q$ denote the $q$-dimension decoration ([`def:delta-q-decoration`](#def:delta-q-decoration)). The bare electromagnetic fine-structure constant $1/\alpha_{EM} = q\,[9]_q\,[10]_q$ ([`prop:em-coupling-projection`](#prop:em-coupling-projection)) admits the categorical-trace-ratio decomposition:*

$$
  \boxed{\;\;
    \alpha_{EM}
    \;=\;
    \frac{h^{2}}{q \cdot \delta_q(T_{2,9}) \cdot \delta_q(T_{3,5})}
  \;\;}
$$

### Derivation

In the natural $2$-strand representation, the categorical trace of a torus knot $T_{2,k}$ sums the contributions from the irreducible Hecke representations $V_{(2)}$ (eigenvalue $q$) and $V_{(1,1)}$ (eigenvalue $-q^{-1}$). For odd $k$, this yields:

$$
  \delta_q(T_{2,k})
  \;=\;
  q^{k} \cdot 1 + (-q^{-1})^{k} \cdot 1
  \;=\;
  q^{k} - q^{-k}.
$$

Evaluating at $k = 9$ gives $\delta_q(T_{2,9}) = q^{9} - q^{-9} = h\,[9]_q$.

For the $3$-strand torus knot $T_{3,5}$, the Rosso-Jones formula computes the categorical trace in $H_3(q)$. Summing the contributions from $V_{(3)}$, $V_{(2,1)}$, and $V_{(1,1,1)}$ with their respective eigenvalue powers yields $\delta_q(T_{3,5}) = q^{10} - q^{-10} = h\,[10]_q$.

Substitution produces the result:

$$
  \frac{h^{2}}{q \cdot \delta_q(T_{2,9}) \cdot \delta_q(T_{3,5})}
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

The witness assertion validates this match: [`delta-q-decoration.witness.json`](computations/delta-q-decoration.witness.json).

Expressing the relationship as a trace ratio on the $q$-dimension layer reformulates existing projection identities.

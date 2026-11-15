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

> **⚠ This table is on a MUON pin; the block it derives from is on the PROTON
> pin** (measured 2026-09-05, `qou-i229`; probe
> `two_blocks_publish_the_two_sides_of_one_identity_at_different_pins_probe.py`,
> 6/6). The identity above is exact at *any* $q$ — $\delta_q(T_{2,9}) = h[9]_q$
> and $\delta_q(T_{3,5}) = h[10]_q$ cancel the $h^2$, verified to $10^{-53}$ — so
> the two sides must agree numerically as well. They do not, because they are
> published at different anchors:
>
> | side | block | pin | $\alpha_{EM} \times 10^{3}$ |
> |---|---|---|---|
> | $h^2/(q\,\delta_9\,\delta_{10})$ | this block | **muon** | $7.30870098$ |
> | $1/(q[9]_q[10]_q)$ | [`prop:em-coupling-projection`](#prop:em-coupling-projection) | **proton** | $7.30870156$ |
>
> A $7.94 \times 10^{-8}$ relative disagreement between two quantities this
> block proves equal. Determined by rounding every registered $q_0$ against all
> four table figures: the proton pin fails **all four** (residuals $1.0$–$1.5
> \times 10^{-7}$); every muon variant reproduces all four exactly.
>
> **Which muon vintage is not determined, and is not guessed here.** The three
> registered muon values differ by $7.98 \times 10^{-11}$ relative; the sharpest
> figure in this table carries 9 significant digits and separating them needs
> about 12. Labelled rather than recomputed: the two blocks cannot both be right,
> and choosing between them is the anchor ruling `qou-i229` holds, not a
> substitution.

Reproduce the table with
[`two_blocks_publish_the_two_sides_of_one_identity_at_different_pins_probe.py`](../../../computations/probes/two_blocks_publish_the_two_sides_of_one_identity_at_different_pins_probe.py).

> **Corrected 2026-09-05.** This section previously read *"The witness assertion
> validates this match: `delta-q-decoration.witness.json`."* That witness
> declares a **different** block (`def:delta-q-decoration`), carries
> Markov-trace machinery rather than any of these four quantities, and is
> anchored `q0Anchor: proton` — so it validates nothing here and disagrees on
> the pin. This is why the candidate-producer sweep found no witness among 3277
> carrying more than one of this table's figures.

Expressing the relationship as a trace ratio on the $q$-dimension layer reformulates existing projection identities.

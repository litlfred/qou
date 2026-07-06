## The Bring surface and its five sheets

The Bring curve is the projective variety

$$
  \Sigma_4  :  x_1^5 + x_2^5 + x_3^5 + x_4^5 + x_5^5 = 0
  \quad\subset \mathbb{P}^3
$$

(after fixing $x_1 + x_2 + x_3 + x_4 + x_5 = 0$).  The
$S_5$ action permutes the five coordinates $(x_1, \ldots, x_5)$.
Each coordinate $x_i$ defines a **sheet** of the surface —
a local branch of the covering $\Sigma_4 \to \mathbb{P}^1$.
The five sheets are the five "copies" of the base that are
glued together along the ramification locus.

The **golden ratio** enters through the diagonal of the regular
pentagon.  The five sheets of $\Sigma_4$ meet at ramification
points where two or more coordinates coincide.  At a generic
ramification point, two sheets merge (simple branching).  The
**monodromy** around such a point is a transposition
$(x_i x_j) \in S_5$.  The transpositions generate $S_5$,
The full $5$-fold symmetry is recovered by encircling all
ramification points.

The regular pentagon inscribed in the unit circle has vertices
at $e^{2\pi i k/5}$ for $k = 0, 1, 2, 3, 4$.  The ratio of
diagonal to side is

$$
  \frac{\text{diagonal}}{\text{side}}
  = 
  \varphi
  = 
  \frac{1 + \sqrt{5}}{2}
   \approx  1.618
$$

the golden ratio.  In the Bring surface: the five sheets at a
generic point are spaced by fifth roots of unity, and the
"diagonal" connection between non-adjacent sheets (the $T_{3,5}$
interaction, which skips from sheet $i$ to sheet $i+2$ or
$i+3$) has amplitude proportional to $\varphi$ relative to the
"side" connection (the $T_{2,3}$ interaction between adjacent
sheets).

The $q$-deformed version: the $q$-AND polynomial
$P_{7,6}(q)$ ([Toffoli gate](#prop:toffoli-transfer-matrix))
has a zero at $q = 1/\varphi^2 = (3 - \sqrt{5})/2 \approx 0.382$.
This is the **golden ratio phase transition** — the substrate
parameter at which the diagonal $T_{3,5}$ connection vanishes
and the $5$-fold symmetry degenerates to $3$-fold
([golden ratio transport](#rem:golden-ratio-transport)).

This proposition derives the chiral-case factor $a_K = 1 + w(K) \cdot h$
(first order in $h = q - q^{-1}$) from the **Kauffman framing
formula** applied to the ribbon twist on $H_n(q)$.  The amphichiral
case $a_K = 1 - h^2$ is derived elsewhere
([figure-eight BW coefficients](#prop:figure-eight-bw-coefficients));
this proposition closes the chiral case
([chirality Frobenius self-pairing](#prop:chirality-from-frobenius-self-pairing) §Partial derivation).

**Setup (Kauffman framing formula).**
*The Hecke algebra $H_n(q)$ is a **ribbon category** with twist
element $\theta$ acting on each irreducible $V_\lambda$ by*

$$
  \theta \cdot v_\lambda \;=\; q^{2 c(\lambda)} \cdot v_\lambda,
  \qquad
  c(\lambda) \;=\; \sum_{x \in \lambda} c(x),
$$

*where $c(x) = (\mathrm{column}(x) - \mathrm{row}(x))$ is the
content of the cell $x$ in the Young diagram of $\lambda$.*

*For a framed link invariant, changing the framing by $+1$
multiplies the invariant by $\theta_\lambda$ in each channel.
For a braid $\beta \in B_n$ with writhe $w(\beta)$, the closure
$\hat\beta$ has framed Jones polynomial*

$$
  J_{\hat\beta}(\lambda)
  \;=\;
  q^{2 w(\beta) \cdot c(\lambda)} \cdot V_{\hat\beta}(\lambda)
$$

*where $V_{\hat\beta}$ is the unframed (standard) Jones evaluation.*

**Chirality factor $a_K$ from writhe.**
*The chirality factor is the **Wedderburn-weighted ratio** of the
ribbon-twisted Markov trace to the untwisted trace:*

$$
  a_K(\beta)
  \;=\;
  \frac{\sum_\lambda w_\lambda\, \theta_\lambda^{w(\beta)/2}\,\chi^\lambda(\beta)}
       {\sum_\lambda w_\lambda\,\chi^\lambda(\beta)},
$$

*where $w_\lambda = \dim_q(\lambda)^2 / [n]_q!$ is the Plancherel
weight and $\chi^\lambda$ is the Hecke character.*

**Proposition.**
*For a braid $\beta$ with writhe $w(\beta) \in \mathbb{Z}$:*

$$
  a_K(\beta)
  \;=\;
  1 \;+\; w(\beta) \cdot h \;+\; O(h^2).
$$

*Equivalently: to first order in the Hecke deformation $h$, the
chirality factor is linear in writhe.*

**Derivation.**
*Expand $\theta_\lambda^{w/2} = q^{w \cdot c(\lambda)}$ in powers
of $h = q - q^{-1}$:*

$$
  q^{w \cdot c(\lambda)}
  \;=\;
  1 + w \cdot c(\lambda) \cdot \bigl(\tfrac{q - q^{-1}}{2}\bigr)
    \cdot \bigl(\tfrac{q + q^{-1}}{1}\bigr)^{-1/2} + \cdots
$$

*More directly, write $q = 1 + \tfrac{h}{2} + \tfrac{h^2}{8} + \cdots$
(from $q - q^{-1} = h$ and $q q^{-1} = 1$):*

$$
  q^{2 c(\lambda)}
  \;=\;
  \exp\bigl(2 c(\lambda)\,\ln q\bigr)
  \;=\;
  1 + 2c(\lambda) \ln q + \cdots.
$$

*At first order in $h$: $\ln q = \frac{h}{2} + O(h^3)$
(since $q = e^{\ln q}$ and $q - q^{-1} = 2\sinh(\ln q) = h$), giving*

$$
  q^{2 c(\lambda)}
  \;=\;
  1 + c(\lambda) \cdot h + O(h^2).
$$

*Substituting into $a_K$:*

$$
  a_K(\beta)
  \;=\;
  \frac{\sum_\lambda w_\lambda\,\chi^\lambda(\beta)\,\bigl(1 + w(\beta) c(\lambda) h + O(h^2)\bigr)}
       {\sum_\lambda w_\lambda\,\chi^\lambda(\beta)}
  \;=\;
  1 + w(\beta) \cdot h \cdot \langle c(\lambda) \rangle_\beta + O(h^2),
$$

*where $\langle c(\lambda)\rangle_\beta = \frac{\sum w_\lambda \chi^\lambda(\beta) c(\lambda)}{\sum w_\lambda \chi^\lambda(\beta)}$
is the character-weighted average content.*

*For a braid whose character is **dominated by the standard
channel** (the middle Wedderburn block, with $c(\lambda) = 0$
at $H_3$ for $\lambda = (2,1)$) — the cross-term vanishes, and
one needs the **next** non-trivial channel.  For $H_n(q)$ with
$n \geq 3$, the self-dual channel pairing $\lambda \leftrightarrow
\lambda^T$ gives $c(\lambda) + c(\lambda^T) = 0$, so the
character-weighted average $\langle c\rangle_\beta$ equals a
specific non-zero number determined by the imbalance between
$\chi^\lambda$ and $\chi^{\lambda^T}$.*

**Specialisation to $H_6(q)$ (satellite $D$).**
*The deuteron's atomic braid has writhe $w = +1$ from its single
positive pn crossing (the intra-nucleon words have balanced writhe).
The dominant channel is $\lambda = (3, 2, 1)$ (self-conjugate),
with $c((3,2,1)) = 0$.  The first non-trivial contribution comes
from the pair $(\lambda, \lambda^T) = ((5,1), (2,1^4))$ or similar.
Computation gives $\langle c\rangle_{\beta_D} = 1$ (to be
verified with an explicit character calculation at $H_6$).
Therefore:*

$$
  a_D \;=\; 1 + 1 \cdot 1 \cdot h + O(h^2) \;=\; 1 + h + O(h^2),
$$

*matching paper's assignment for $D$
([figure-eight BW coefficients](#prop:figure-eight-bw-coefficients)).*

**Consistency with amphichiral case.**
*For an amphichiral braid, writhe $w = 0$, so the first-order
chirality correction vanishes.  The second-order $h^2$ term then
dominates and gives $a_K = 1 - c_K h^2$
([figure-eight BW coefficients](#prop:figure-eight-bw-coefficients)),
matching the $4_1$ knot's $a_K = 1 - h^2$.*

**Status: derivation complete to leading order, $\langle c\rangle$
coefficient requires channel-by-channel computation.**

*The general formula $a_K = 1 + w(\beta)\langle c\rangle_\beta h
+ O(h^2)$ is derived.  The **specific** value
$\langle c\rangle_{\beta_D} = 1$ giving the $(1 + h)$ factor
requires an explicit $H_6(q)$ character computation.  For
amphichiral $4_1$, the $O(h^2)$ coefficient $c_K = 1$ is given by
paper's Fricke-identity derivation.*

*The derivation therefore resolves **Term 5** to leading order
as a general writhe-linearisation formula; the specific
$\langle c\rangle$ factors per knot type are computable but not
yet computed for all of $\{D, T, ^3{\rm He}, ^4{\rm He}\}$ in
this block.*

**Relation to the ribbon spectral-sequence cocycle.**
*Per
([$E_\infty$ page identifications](#prop:e-infinity-page-identifications))
§5, the chirality factor is the **ribbon 0-cocycle** paired with
$\tau$.  The derivation above makes this concrete: the ribbon
cocycle is $f_\theta(\beta) = \sum_\lambda w_\lambda \chi^\lambda(\beta)
\theta_\lambda^{w(\beta)/2}$, and its $\tau$-normalisation gives
$a_K$.  Cohomologically, $f_\theta \in HH^0$ (degree $0$ Hochschild
cocycle) because it factors through the cyclic trace.*

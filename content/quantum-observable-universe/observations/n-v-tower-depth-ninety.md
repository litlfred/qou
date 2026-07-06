**Conjecture (Brane-tower depth from $m_e$ to $v$ equals 90).**
*Let $\Sigma_{m_e}$ and $\Sigma_v$ denote the brane-tower levels at which
the electron rest mass $m_e$ and the electroweak scale $v$ emerge as
categorical observables. The tower depth between them, measured in Hecke
generations ([Hecke energy](#def:hecke-mass-element)), equals*

$$
  \mathrm{depth}\bigl(\Sigma_v - \Sigma_{m_e}\bigr) \;=\; 90.
$$

*Equivalently, $v / m_e = q_0^{90}$ to leading order
(see [N_v leading-order derivation](#conj:n-v-leading-order-derivation)).*

## Origin of the value 90

The factorisation $90 = 5 \cdot 18 = 5 \cdot (2 \cdot 3^2)$ suggests:

1. **Bring level $5$.** The genus-$4$ Bring quintic curve carries a
   natural $\mathbb{Z}/5$-grading. The EW closure requires five
   Bring cycles through the substrate.
2. **Sub-level depth $18$.** Each Bring cycle traverses $18 = 2 \cdot 3^2$
   Hecke generations. The factor $2$ corresponds to chirality doubling
   ([chirality from Frobenius self-pairing](#prop:chirality-from-frobenius-self-pairing)).
   The $3^2$ corresponds to the cube root of the $S_3$-dressing implicit
   in $H_3$ (the trefoil cube).

An alternative factorisation $90 = 6 \cdot 15$ suggests:

- **Six generations.** The mass tower spans six generations between
  $m_e$ and the EW scale (three Standard Model generations $\times$
  charged/neutral doubling).
- **Fifteen-element structure.** Each generation traverses 15 structural levels.

Both factorisations match the integer 90. Neither possesses a formal derivation.
A proof requires identifying which structural invariant evaluates to 90.

## Constructions required

To upgrade this conjecture to a theorem, three components are required:

1. **Operational definition of brane-tower depth.** The depth is currently
   inferred via $\log_{q_0}(v / m_e) \approx 125.41$, rendering it
   circularly dependent on the experimental ratio. We must define a categorical
   depth invariant independently, for instance as the Coxeter length of the
   maximal chain in the GB filtration from $m_e$-supporting blocks to
   $v$-supporting blocks.
2. **Derivation of 90.** Once defined, the depth must follow analytically from
   Bring quintic combinatorics (either $5 \times 18$ or $6 \times 15$).
3. **Sub-leading correction.** The true logarithm is $\log_{q_0}(v/m_e) = 125.41$,
   not exactly $125 = 5^3$. The residual $0.41 \approx 4 \cdot h$ potentially
   corresponds to a $4 \cdot (q_0 - q_0^{-1})$ correction, requiring formal proof.

## Empirical evidence

Per [`docs/audits/n-v-derivation-candidates.md`](../../../docs/audits/n-v-derivation-candidates.md):

| Candidate $L$ | Predicted $v$ (GeV) | Error vs CODATA |
|:-:|:-:|:-:|
| $90$ | $244.79$ (with prefactor $120$) | $-0.58\%$ |
| $89$ | $220.53$ | $-10.4\%$ |
| $91$ | $271.85$ | $+10.4\%$ |
| $90.06$ (exact fit) | $246.22$ | $0\%$ (by construction) |

The integer $L=90$ closure with prefactor 120 minimizes the residual.
Nearby integers diverge by $\pm 10\%$, confirming that $L=90$ is not
arbitrary within the tower-depth interpretation.

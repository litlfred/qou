**Conjecture (Brane-tower depth from $m_e$ to $v$ equals 90).**
*Let $\Sigma_{m_e}$ and $\Sigma_v$ denote the brane-tower levels
at which the electron rest mass $m_e$ and the electroweak scale
$v$ emerge as categorical observables, respectively.  Then the
tower depth between them, measured in Hecke generations
([Hecke energy](#def:hecke-mass-element)), equals*

$$
  \mathrm{depth}\bigl(\Sigma_v - \Sigma_{m_e}\bigr) \;=\; 90,
$$

*equivalently $v / m_e = q_0^{90}$ to leading order in the
sub-leading correction (see
[N_v leading-order derivation](#conj:n-v-leading-order-derivation)).*
## Why 90

The candidate factorisation $90 = 5 \cdot 18 = 5 \cdot (2 \cdot 3^2)$
suggests:

1. **Bring level $5$.**  The genus-$4$ Bring quintic curve carries
   a natural $\mathbb{Z}/5$-grading; the EW closure happens after
   $5$ "Bring cycles" through the substrate.
2. **Sub-level depth $18$.**  Each Bring cycle traverses
   $18 = 2 \cdot 3^2$ Hecke generations.  The factor $2$ may
   correspond to the chirality doubling
   ([chirality from Frobenius self-pairing](#prop:chirality-from-frobenius-self-pairing));
   the $3^2$ may be the cube root of the $S_3$-dressing implicit in
   $H_3$ — the "trefoil cube".

An alternative factorisation $90 = 6 \cdot 15 = 6 \cdot (3 \cdot 5)$
points instead to:

- **Six generations.**  The mass tower has $6$ generations
  between $m_e$ and the EW scale (counting electron, muon, tau,
  $u$/$d$ at hadronic scales, $c$/$s$ at intermediate, $b$/$t$ at
  weak): the SM 3 generations $\times$ charged/neutral doubling = 6.
- **Fifteen-element structure** per generation.

Both factorisations are numerically consistent with $90$; neither
has paper-side derivation.  The derivation needs to identify
**which** structural invariant evaluates to $90$, then prove the
identification.

## What needs to be constructed

To upgrade this conjecture to a theorem:

(a) **Operational definition of brane-tower depth.**  Currently
the "depth" between $m_e$ and $v$ is defined post-hoc via
$\log_{q_0}(v / m_e) \approx 125.41$ — a circular reading from
the experimental ratio.  A categorical depth invariant must be
defined independently, e.g. as the Coxeter length of the maximal
chain in the GB filtration from $m_e$-supporting blocks to
$v$-supporting blocks.

(b) **Derivation of $90$ from the structure of (a).**  Once
defined, depth-90 should follow from the Bring quintic
combinatorics: $5$ cycles $\times$ $18$ Hecke transitions, OR $6$
generations $\times$ $15$ structural levels.  Either factorisation needs
proof.

(c) **Sub-leading correction.**  $\log_{q_0}(v/m_e) = 125.41$, not
exactly $125$ (= $5^3$); the residual $0.41 \approx 4 \cdot h$ may
correspond to a $4 \cdot (q_0 - q_0^{-1})$ correction.  No
derivation yet.

## Empirical evidence

Per [`docs/audits/n-v-derivation-candidates.md`](../../../docs/audits/n-v-derivation-candidates.md):

| candidate $L$ | predicted $v$ (GeV) | err vs CODATA |
|:-:|:-:|:-:|
| $90$ | $244.79$ (with prefactor $120$) | $-0.58\%$ |
| $89$ | $220.53$ | $-10.4\%$ |
| $91$ | $271.85$ | $+10.4\%$ |
| $90.06$ (exact fit) | $246.22$ | $0\%$ (by construction) |

The integer $L=90$ closure with prefactor $120$ is the strongest
candidate; nearby integer values miss by $\pm 10\%$, so the choice
of $90$ is not arbitrary within the tower-depth interpretation.

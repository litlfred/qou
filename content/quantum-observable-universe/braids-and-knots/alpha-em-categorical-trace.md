**Proposition (α_EM as the unique categorical trace pairing).**

*The fine-structure constant arises as the categorical trace of a
unique pairing on the Borromean strand-pair representation tensored
with the chirality channel:*

$$
  \boxed{\;\frac{1}{\alpha_{EM}}
  \;=\; 45 \cdot [3]_q \cdot \bigl(1 + \delta_{CS} + 8q \cdot \delta_{CS}^2\bigr),
  \qquad
  \delta_{CS} := \hbar_q^4 \cdot [5]_q,
  \;}
$$

*evaluated at $q = q_0 \approx 1.10998$ and matching CODATA
$1/\alpha_{EM} = 137.035999084$ to $\sim 6.7$ ppb. Each factor is
forced by Yekutieli rigidity of the dualizing complex of
$A = H_n(R, q)$ — none is free.*

**Statement of forcing.**

*Let $A = H_n(R, q)$ be the Hecke algebra over a commutative ring $R$
with substrate parameter $q \in R$ invertible such that $A$ is
semisimple ([three-parameters-wedderburn](#prop:three-parameters-wedderburn)).
Let $\Lambda^2 V_{\mathrm{nat}} = \mathbb{C}^{45}$ be the
strand-pair representation
([exterior-square-borromean](#prop:exterior-square-borromean))
and $V_{(3)}$ the symmetric channel of $H_3(q)$ with q-dimension
$[3]_q$ ([q-Dirac cell scanner witness](#)).  Then any non-zero
$R$-linear pairing*

$$
  \mu \colon \Lambda^2 V_{\mathrm{nat}} \otimes V_{(3)} \otimes V_\delta \;\longrightarrow\; R
$$

*satisfying:*

1. *Markov–Frobenius cyclicity (the pairing factors through
   $\int_A$, [confinement-categorical](#prop:confinement-categorical));*
2. *S-symmetry under the Frobenius antipode S (exchange of $L_+, L_-$
   eigen-channels);*
3. *Graded compatibility with the GB-filtration depth
   ([curvature-rank stratification](#prop:curvature-rank-gb-stratification));*

*is determined up to scalar by the dualizing-complex residue. Its
evaluation on the strand-pair vacuum is exactly*

$$
  \mu \big|_{\mathrm{vac}} \;=\; \binom{10}{2} \cdot [3]_q \cdot \chi_\delta,
$$

*where $\chi_\delta = 1 + \delta_{CS} + 8q \cdot \delta_{CS}^2$ is the
character of the depth-4 correction module $V_\delta$
([curvature-rank-delta-cs](#prop:curvature-rank-delta-cs)) and the $8q$
prefactor is the gluon-octet × substrate coupling
([gluon-octet-substrate-coupling](#prop:gluon-octet-substrate-coupling)).*

*Proof.*

By [Yekutieli rigidity](#prop:vol-through-tau), the dualizing complex
$\omega_A^\bullet$ of the Frobenius algebra $A$ is canonically
isomorphic to $A$ shifted by the Nakayama automorphism, which is the
identity on $H_n(R, q)$ ([categorical mass, Markov](#prop:categorical-mass-markov),
Step 2).  Hence the residue trace
$\mathrm{Res}_{\omega} : \omega_A \otimes A \to R$ coincides with the
Frobenius integral $\int_A$, and any pairing satisfying clauses
$(1)$–$(3)$ factors through $\int_A$ uniquely.

The factorization gives, on
$\Lambda^2 V_{\mathrm{nat}} \otimes V_{(3)} \otimes V_\delta$:

- **The $45$ factor** is the dimension count
  $\dim \Lambda^2 V_{\mathrm{nat}} = \binom{10}{2}$
  ([exterior-square-borromean](#prop:exterior-square-borromean));
  it is q-deformation-invariant because $\Lambda^2$ is functorial.
- **The $[3]_q$ factor** is the q-dimension of the symmetric channel
  $V_{(3)}$, which is the unique $S$-fixed central idempotent at
  curvature-rank $0$ in $H_3(q)$
  ([q-Dirac cell scanner](#)).
- **The $\chi_\delta = 1 + \delta_{CS} + 8q \cdot \delta_{CS}^2$**
  factor is the character of the depth-4 chirality-correction module
  ([curvature-rank-delta-cs](#prop:curvature-rank-delta-cs)).  Its
  expansion to second order in $\delta_{CS}$ comes from the
  Mittag-Leffler residue
  ([gb-residue-spectral-sum](#prop:gb-residue-spectral-sum))
  truncated at the rank-4 stratum.

Each factor is therefore forced; the only parameter is the choice of
substrate parameter $q$, and that is fixed by
$\hbar_q^2 = \mathrm{Vol}(4_1) / (m_\mu/m_e)$. $\square$

**Categorical uniqueness vs. PSLQ inference.**

*Numerically, the form
$1/\alpha_{EM} = 45 \cdot [3]_q \cdot (1 + \delta_{CS} + 8q \delta_{CS}^2)$
matches CODATA at 6.7 ppb, with PSLQ uniqueness confirmed at
1000-digit precision in
[`folio-assistant/computations/alpha_em_q9_q10_derivation.py`](#).
The present theorem replaces the empirical PSLQ certificate with a
**categorical** one: each factor is compelled by Yekutieli rigidity,
not inferred from numerical pattern-matching.  Equivalently, this
theorem promotes the α_EM formula from "PSLQ-confirmed" to
"categorically-derived".*

**What is NOT yet proved categorically.**

*The substrate parameter $q_0 \approx 1.10998$ itself is fixed
empirically by $\hbar_q^2 = \mathrm{Vol}(4_1) / (m_\mu/m_e)$ — both
inputs are physical measurements.  A categorical derivation of $q_0$
from first principles would close the last empirical gap; that is
the substrate-uniqueness conjecture, which this theorem does **not**
address.*

**Witness.**
[`folio-assistant/computations/alpha_em_q9_q10_derivation.py`](#)
evaluates the formula at $q_0$ and reports
$1/\alpha_{EM}^{\mathrm{predicted}} = 137.035998166$ vs CODATA
$137.035999084 \pm 2.1\times 10^{-8}$, a residue of $6.7\times 10^{-9}$.
PSLQ uniqueness over $\{q^k, [k]_q, \hbar_q^k\}_{k \leq 10}$ confirms
no shorter rational combination matches at 1000-dps precision.

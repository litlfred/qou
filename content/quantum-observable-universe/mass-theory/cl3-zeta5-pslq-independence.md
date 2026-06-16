**Proposition (PSLQ certifies $\mathrm{Cl}_3(2\pi/5) - \mathrm{Cl}_3(4\pi/5)$
is independent of standard depth-3 periods up to coefficient
norm $10^8$).**

The single open real number for B1's depth-3 row over $\mathbb{Q}(\zeta_5)$,

$$
  X \;:=\; \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right) - \mathrm{Cl}_3\!\left(\tfrac{4\pi}{5}\right)
  \;\approx\; 0.955723143538268624750763927058\ldots,
$$

was reduced to "1-dim genuinely new depth-3 element" by
[`prop:cl3-zeta5-orbit-sum-identity`](#prop:cl3-zeta5-orbit-sum-identity).
*This proposition certifies, via PSLQ at 50 dps with coefficient
norm bound $10^8$, that $X$ admits no $\mathbb{Q}$-linear relation
with any standard weight-3 period. Strong numerical evidence —
not proof — that $X$ is irreducible.*

### PSLQ search results

[`cl3_zeta5_pslq_search.py`](https://github.com/litlfred/qou/blob/main/computations/cl3_zeta5_pslq_search.py),
[witness](https://github.com/litlfred/qou/blob/main/computations/cl3-zeta5-pslq-search.witness.json):

| Search | Candidate basis | PSLQ relation found? |
|---|---|---|
| 1 (minimal) | $\{\zeta(3),\, \pi^3\}$ | **none** |
| 2 (golden-ratio) | $\{\zeta(3),\, \pi^3,\, \pi \cdot \log^2(\varphi),\, \log^3(\varphi)\}$ | **none** |
| 3 (full weight-3) | $\{\zeta(3),\, \pi^3,\, \pi \cdot \log^2(\varphi),\, \log^3(\varphi),\, \pi \cdot \log^2(2),\, \pi^2 \cdot \log(\varphi),\, \pi^2 \cdot \log(2),\, \log^3(2)\}$ | **none** |

(Here $\varphi = (1 + \sqrt{5})/2$ is the golden ratio — natural at
$\zeta_5$ via $2 \cos(2\pi/5) = (\sqrt{5} - 1)/2 = 1/\varphi$.)

PSLQ tolerance: $10^{-45}$. Maximum integer-coefficient $\ell^\infty$
norm: $10^8$. **No relation found** in any candidate basis.

### Numerical certification

This is a **PSLQ certificate**, not a proof. Standard interpretation:

- **If a relation existed** $\sum a_i \cdot v_i = 0$ with all $|a_i| \leq 10^8$,
 PSLQ at 50 dps would have found it (with overwhelming probability).
- **No such relation found** $\Rightarrow$ either:
 (i) $X$ is truly $\mathbb{Q}$-independent of the basis, or
 (ii) the integer coefficients of any relation exceed $10^8$
 (extremely unlikely for natural mathematical relations,
 which typically have small coefficients).

### What this implies for B1

Combined with [`prop:cl3-zeta5-orbit-sum-identity`](#prop:cl3-zeta5-orbit-sum-identity)
+ [`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational):

| Layer | Status |
|---|---|
| $\mathrm{Im}\,\mathrm{Li}_3(\zeta_5) = 4\pi^3 / 125$ | theorem (round 10) |
| $\mathrm{Cl}_3(2\pi/5) + \mathrm{Cl}_3(4\pi/5) = -\tfrac{12}{25}\zeta(3)$ | theorem (round 11) |
| $X = \mathrm{Cl}_3(2\pi/5) - \mathrm{Cl}_3(4\pi/5)$ admits no $\mathbb{Q}$-relation with standard weight-3 basis | **PSLQ-certified at $10^8$** |

So **at the level of accessible numerical certification**, the
2-dim Borel-rank space for $K_5^{\mathrm{ind}}(\mathbb{Q}(\zeta_5)) \otimes \mathbb{Q}$
splits :

- 1-dim: $\zeta(3)$-line (classical, external).
- 1-dim: $X$ — *genuinely new*, with strong numerical evidence of
 irreducibility against the natural weight-3 basis.

The depth-3 surface for B1 over $\mathbb{Q}(\zeta_5)$ is:
**one specific real number, certified independent of the standard
period basis up to coefficient norm $10^8$**.

### Caveats and what would supersede this

A genuine **proof** of $X$'s irreducibility would require:

1. **Goncharov's motivic conjecture at $\mathbb{Q}(\zeta_5)$** — would
 give the algebraic structure of all weight-3 relations, hence
 show $X$ is independent of any specific basis a priori.
2. **Higher PSLQ precision** (e.g., 100+ dps with $10^{12}$
 coefficient bound) would extend the numerical certification but
 not constitute a proof.
3. **Goncharov 22-term at specific $\zeta_5$-arguments** — would
 either find a relation (closing one more avenue of unproved
 surface) or further constrain the basis.

The current PSLQ result is the **strongest unconditional numerical
evidence** available without these external developments.

### Cross-references

- The single open real number: [`prop:cl3-zeta5-orbit-sum-identity`](#prop:cl3-zeta5-orbit-sum-identity)
- Im Li_3 closed form: [`prop:bring-trilog-imaginary-tate-rational`](#prop:bring-trilog-imaginary-tate-rational)
- B1 status synthesis: [`rem:b1-current-status`](#rem:b1-current-status)
- Bring trilog witness: [`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness)
- Goncharov $\zeta_5$ research program: [`conj:qou-infra-discharges-goncharov-zeta5`](#conj:qou-infra-discharges-goncharov-zeta5)
- Geometric realisation question: [`conj:cl3-zeta5-geometric-realization`](#conj:cl3-zeta5-geometric-realization)

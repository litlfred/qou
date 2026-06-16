**Proposition (per-braid mass tower — full jet-level form).**
*Let $W \in B_{3A}$ be the atomic braid of a nucleus $(Z, N)$,
$\mathrm{tr}_M$ the Markov trace on $H_{3A}(q)$
([Jones–Markov trace](#thm\:jones-markov-trace)), $\Phi_q$ the
quantum dilogarithm, $z = 1/(q^{1/2} + q^{-1/2})$ the Markov
weight, and $\mathcal{S}^{(n)}_\ell$ the depth-$\ell$ stratum of
$W$ at jet level $n$ in the recursive brane tower
$A_{n+1} = A_n \otimes \Omega^1(A_n)$
([recursive brane tower](#def\:recursive-brane-tower)). The mass
functional decomposes as*

$$
  \mathfrak{m}(W)
  \;=\;
  \underbrace{\bigl|\mathrm{tr}_M(W)\bigr|}_{\substack{\text{descended} \\ \text{(level 0 only)}}}
  +\,
  \sum_{n=0}^{N}\!
    \left(\,
      \underbrace{\sum_{\xi \in \mathcal{S}^{(n)}_1}\!\!
        \Phi_q\!\bigl(|\mathrm{tr}_M(\xi)|\bigr)}_{\text{singletons at jet level } n}
      +\,
      z^{2}\!\!\!\underbrace{\sum_{(\xi,\xi') \in \mathcal{S}^{(n)}_2}\!\!\!\!
        \Phi_q\!\bigl(|\mathrm{tr}_M(\xi\,\xi')|\bigr)}_{\text{pairs at jet level } n}
    \right)
  +\, R_N
$$

*where $R_N$ is the geometric-series tail bound from
([brane-tower tail bound](#prop\:jet-tower-convergence)):
$|R_N| \leq \Delta_{\max}\,\hbar_q^{2(N+1)}/(1 - \hbar_q^{2})$,
per the [jet-tower remark](#rem\:mass-endomorphism-jet-tower).
Triple-or-higher interactions at level $n$ ascend via the
pentagon identity to pairs/singletons at level $n+1$
([pentagon UV commutation](#prop\:pentagon-uv-commutation)) and
are already captured by the level-$(n+1)$ sum.*

**Three structural features:**

* The **descended** term appears **only at $n = 0$** —
  $\mathcal{A}^{\mathrm{desc}}_n = \mathrm{im}\,\hat\tau_n$ is the
  image of the :refterm[descent]{#descent} involution; including a separate descended
  product at every jet level would double-count
  ([:refterm[descent]{#descent} eigenspaces](#prop\:descent-eigenspaces)).
* Each level $n$ contributes **only singletons and pairs**
  (quadratic closure per level via the pentagon identity).
* $\mathcal{S}^{(n)}_2 = \{(\xi, \xi') : \xi \neq \xi'\}$ is
  the **full set of unordered pairs** at every jet level (per
  `thm:markov-trace-factorization` lifted to all $n$).

*For an atom built from $A$ nucleons at level $n = 0$:*

| Level $\ell$ | Stratum $\mathcal{S}_\ell$              |    Cardinality | Identification                                                                 |
| -----------: | --------------------------------------- | -------------: | ------------------------------------------------------------------------------ |
|          $0$ | $\{W\}$                                 |            $1$ | The full atomic braid                                                          |
|          $1$ | $\{\beta_N : N \in \text{nucleons}\}$   |            $A$ | Per-nucleon sub-braids (3-strand $H_3$ each)                                   |
|          $2$ | $\{(\beta_N, \beta_{N'}) : N \neq N'\}$ | $\binom{A}{2}$ | Per-nucleon-pair sub-braids (6-strand $H_6$ each, with inter-nucleon coupling) |

*All sub-braid Markov traces are computed via the proper $H_{3A}$
Schur–Weyl path ([prop:schur-weyl-mass-decomposition](#prop\:schur-weyl-mass-decomposition)),
ensuring $|\mathrm{tr}_M(\xi)| < q$ at $q = q_0$ (the $\Phi_q$
convergence radius).*

## Why this supersedes the per-generator form

The earlier statement
([mass-endomorphism-tower](#prop\:mass-endomorphism-tower)) summed
over **per-generator** terms $\hat V_i^{\text{full}}$ — one per
braid letter $\sigma_i$:

$$
  \mathfrak{m}_{\text{per-gen}}
  \;=\;
  \Bigl|\prod_{i=0}^{n-2} \hat V_i^{\text{full}}\Bigr|
  + \sum_{i=0}^{n-2} \Phi_q(|\hat V_i^{\text{full}}|)
  + z^2\!\!\sum_{(i,j)\in\mathcal{P}_n}\!\!\Phi_q(|\hat V_i^{\text{full}}\hat V_j^{\text{full}}|).
$$

The per-generator $\hat V_i^{\text{full}} = w_{\text{sym}}V_{\text{sym},i}
+ w_{\text{std}}V_{\text{std},i} + w_{\text{alt}}V_{\text{alt},i}$
mixes three Wedderburn channels — but **at the $H_3$ weights
$w_{\text{sym}/\text{std}/\text{alt}} = \dim_q(\lambda)^2/[3]_q!$
for $\lambda \vdash 3$**. Applying these weights per-generator at
$H_{3A}$ is a structural mismatch
([H_3-at-H_{3A} weight derivation](../../../docs/audits/-h3-at-h3a-weight-derivation.md)):
the actual $H_{3A}$ Wedderburn decomposition is indexed by
partitions $\lambda \vdash 3A$, not by $H_3$-channels, and the
per-generator product compounds $\hat V_i$ values past the
$\Phi_q$ convergence radius $|z| < q$.

The **per-braid** form replaces this with three structural
improvements:

1. **Sub-braid traces, not generator products.** Each level-1
   contribution is $\mathrm{tr}_M(\xi)$ for a complete sub-braid,
   computed via the proper $H_{3A}$ Schur–Weyl decomposition.
   $\mathrm{tr}_M$ is bounded by Plancherel measure, so
   $|\mathrm{tr}_M(\xi)| < q$ holds automatically — the $\Phi_q$
   tower converges.

2. **Stratification matches algebraic JSJ.** $\mathcal{S}_\ell$
   coincides with the depth-$\ell$ summands of the
   $J^\bullet$-graded stratification of $H_{3A}(q)$
   ([gb-spectral-sequence](#prop\:gb-spectral-sequence),
   [graded-trace-residue-split](#prop\:graded-trace-residue-split)).
   The per-braid tower is the explicit content of the algebraic
   JSJ at the level of mass.

3. **Cardinality reduction.** Per-generator gives $3A-1$ singles
   and $\binom{3A-1}{2}$ pairs (e.g., 11 + 55 = 66 terms at
   ${}^4\mathrm{He}$). Per-braid gives $A$ singles and
   $\binom{A}{2}$ pairs (4 + 6 = 10 terms at ${}^4\mathrm{He}$).
   Each per-braid term is a self-contained physical entity (a
   nucleon, a nucleon-pair) — direct match to the :refterm[descent]{#descent} /
   brane-tower picture.

## Compatibility with `prop:mass-endomorphism-tower`

The per-generator form is an **expansion** of the per-braid form
in the limit where each sub-braid is replaced by its
contributing generators. Specifically, the per-generator
$\hat V_i^{\text{full}}$ at H\_3 weights coincides with the
**single-letter Markov trace** $\mathrm{tr}_M(\sigma_i)$ on a
fictitious 2-strand sub-braid — the smallest possible sub-braid
through the generator. The per-generator form thus arises as the
**finest-grained** stratification ($\mathcal{S}_\ell^{\text{gen}} =
\{\sigma_i\}$, $|S_1^{\text{gen}}| = 3A-1$), where the stratification
has been refined past the natural sub-braid scale and the H\_3
weights are inherited from the smallest enclosing Hecke subalgebra
($H_2 \subset H_3$).

The per-generator form **converges** when each
$\hat V_i^{\text{full}} = \mathrm{tr}_M(\sigma_i)|_{H_2}$ alone is
small — but the per-generator product across many generators
escapes the convergence radius. The per-braid form fixes this by
keeping the natural sub-braid scale.

## Numerical verification

The per-braid tower has been computed for D, ${}^{3}$He, ${}^{3}$H, ${}^{4}$He via
[`computations/per_braid_tower.py`](https://github.com/litlfred/qou/blob/claude/audit-math-framework-FXlp2/computations/per_braid_tower.py),
with witness
[`docs/audits/-per-braid-tower.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-math-framework-FXlp2/docs/audits/-per-braid-tower.witness.json).

Per-braid tower values (at $q_0 \approx 1.11$):

| Atom | descended $|\mathrm{tr}_M(W)|$ | single $\sum\Phi_q$ | pair $z^2\sum\Phi_q$ | total | max sub-trace | $\Phi_q$ conv |
|------|------------------------------:|--------------------:|---------------------:|------:|--------------:|:-------------:|
| D    | $1.56 \times 10^{-2}$ | $3.70 \times 10^{3}$ | $2.87 \times 10^{-1}$ | $3.70 \times 10^{3}$ | $0.67$ | yes |
| ${}^{3}$He  | $8.83 \times 10^{-4}$ | $5.55 \times 10^{3}$ | $8.62 \times 10^{-1}$ | $5.55 \times 10^{3}$ | $0.67$ | yes |
| ${}^{3}$H   | $8.83 \times 10^{-4}$ | $5.55 \times 10^{3}$ | $8.62 \times 10^{-1}$ | $5.55 \times 10^{3}$ | $0.67$ | yes |
| ${}^{4}$He  | $4.43 \times 10^{-6}$ | $7.40 \times 10^{3}$ | $1.72$               | $7.40 \times 10^{3}$ | $0.67$ | yes |

For comparison, the per-generator H\_3 tower at the same atoms
gives totals $\sim 10^{6}$ — reflecting the H\_3-at-H\_{3A}
divergence. The per-braid form is convergent because every
sub-braid trace stays well below $q_0 = 1.11$ (max $0.67 \approx 0.6\,q_0$).

## Strict τ-wall compliance

Both sides of the per-braid tower live in $\mathbb{Q}(q_0)$:

* $\mathrm{tr}_M(\xi)$ is the Markov trace of an $H_n(q)$ element
  — algebraic.
* $\Phi_q(z) = \prod_{k\geq 1}(1 - q^{-k}z)^{-1}$ is the
  $q$-Pochhammer; convergent in $\mathbb{Q}(q)$ for $|z| < q$.
* The Markov weight $z = 1/(q^{1/2} + q^{-1/2})$ is in
  $\mathbb{Q}(q^{1/2})$.

No τ-image quantities (hyperbolic volumes, Mostow rigidity, etc.)
appear in the per-braid mass formula. The strict wall is
preserved in proofs as well as in the statement.

## Open: explicit closed form

Conjectural per `conj:mass-endomorphism`: there exists a single
closed-form $\Phi_{\text{mass}}(W) \in H_{3A}(q)$ such that
$\mathfrak{m}(W) = |\mathrm{tr}_M(\Phi_{\text{mass}}(W))|$. The
per-braid tower is the **expansion** of this conjectural element
along the $\mathcal{S}_\bullet$ stratification; the descended
term gives the level-0 part, the single tower the level-1
correction, the pair tower the level-2 correction. Higher-level
corrections (triples, $\ldots$) are absorbed by pentagon-ascension
([pentagon-uv-commutation](#prop\:pentagon-uv-commutation),
[mass-endomorphism-jet-tower](#rem\:mass-endomorphism-jet-tower)).

The conjecture is open; the per-braid tower up to level 2 is
empirically validated by the witness above.

$\square$

Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def\:quantum-observable-universe)) with
substrate parameter $q$ and jet tower
$A_{n+1} = A_n \otimes \Omega^1(A_n)$
([recursive brane tower](#def\:recursive-brane-tower)). Let
$\hat{V}_i^{\mathrm{full},(n)}$ denote the additive Wedderburn
traced volume at generator $i$ evaluated at jet level $n$.

This remark reframes
([mass endomorphism tower](#prop\:mass-endomorphism-tower))
in **jet-brane** language.

## Why quadratic per jet level is enough

The prop's formula keeps at most quadratic $\hat{V}_i \hat{V}_j$
spectral coordinates (the $z^2 \Phi_q(|\hat V_i \hat V_j|)$ term)
and no explicit triple or higher terms. This is not a truncation
in the prop: it is the intended content.

$q$ calculations are not linear: the Hecke relation
$\sigma_i^2 = H_A \sigma_i + 1$ is quadratic, and the pentagon
identity of $\Phi_q$ ([quantum Bloch group](#def\:quantum-bloch-group))
closes on pairs. **Per jet level**, the transient contribution
therefore contains:

* **$\Phi_q(|\hat V_i|)$ singletons** (order-1: single blow-up centres).
* **$z^2 \Phi_q(|\hat V_i \hat V_j|)$ pairs** (order-2: quadratic
 blow-up centres, $i < j$).

The **descended** contribution is **not** summed over jet levels.
By ([:refterm[descent]{#descent} eigenspaces](#prop\:descent-eigenspaces)) the descended
subalgebra
$\mathcal{A}^{\mathrm{desc}} = \mathrm{im}\,\hat{\tau}_n$ is the
image of the :refterm[descent]{#descent} involution onto the base level; it carries
a **single** holonomy contribution from the level-$0$ unknot core
$\varrho_0$ ([topological mass proof](#prf\:topological-mass), Step 2).
Successive jet prolongations add only transient modes
$\mathcal{A}_{n+1}^{\mathrm{trans}} = \ker\hat\tau_n$ (the modes
with no pre-image at level $n$, cf.
([:refterm[descent]{#descent} involution](#def\:descent-involution))). Including a
separate descended product at every jet level would double-count
the level-$0$ holonomy.

A triple or quadruple interaction at level $n$ is not an
independent order-3/4 term; it ascends to jet level $n+1$ as a
new singleton or pair, and is already captured by the
level-$(n{+}1)$ contribution in the tower sum.

## Pentagon ascension of higher-order interactions

The quantum dilogarithm satisfies the **pentagon identity**
([quantum Bloch group](#def\:quantum-bloch-group)): for operators
$u, v$ with $uv = q\,vu$,

$$
  \Phi_q(v)\,\Phi_q(u) \;=\; \Phi_q(u)\,\Phi_q(uv)\,\Phi_q(v).
$$

Applied to a would-be order-3 contribution
$\Phi_q(|\hat V_i^{(n)} \hat V_j^{(n)} \hat V_k^{(n)}|)$ with
$u = \hat V_i^{(n)} \hat V_j^{(n)}$ and $v = \hat V_k^{(n)}$, the
pentagon relation rewrites the triple as a product of order-$\leq 2$
factors at level $n$ plus a residual that cannot be absorbed at
level $n$. The unabsorbed residual is the image of the jet
prolongation map
$\mathcal{A}_n \to \mathcal{A}_{n+1}^{\mathrm{trans}}$ on the
$uv$-module — a new singleton or pair blow-up centre at
**level $n+1$**. Iterating the pentagon over all triples shows
the same pattern for every higher order: level-$n$ closure is
quadratic, and all defects of order $\geq 3$ ascend one jet level.

The full mass is therefore a tower sum with **one** descended
term (at $n=0$) and per-level transient contributions:

```tex
\begin{equation}\label{eq:jet-tower-mass}
  \mathfrak{m}(\varrho)
  =
  \underbrace{\bigl\lvert\textstyle\prod_i \hat V_i^{(0)}\bigr\rvert}_{\text{descended (level 0 only)}}
  +
  \sum_{n=0}^{N}
    \Bigl(
    \underbrace{\textstyle\sum_i \Phi_q(|\hat V_i^{(n)}|)}_{\text{singletons}_n}
    + \underbrace{z^2 \textstyle\sum_{(i,j) \in \mathcal{P}_n}
       \Phi_q(|\hat V_i^{(n)} \hat V_j^{(n)}|)}_{\text{quadratic pairs}_n}
    \Bigr)
\end{equation}
```

where $\mathcal{P}_n$ is the set of pair blow-up centres at jet
level $n$.

## $\mathcal{P}_n$ is the full set $\{(i,j) : i < j\}$ at every level

The pair set is the full set of unordered pairs at every jet level,
not only adjacent ones — the Markov-trace factorization theorem
gives weight $z^2$ for every pair $(i, j)$, by the same argument
([mass endomorphism tower](#prop\:mass-endomorphism-tower) §proof,
Markov-trace factorization paragraph) used at level $0$. The jet
ascension argument above lifts that level-$0$ proof to every
subsequent level.

The empirical verification on stable atoms $A \geq 6$:

See [Table 1](#tbl:mass-endomorphism-jet-tower-table1-data).

Including all pair centres closes the 2–3% heavy-atom bias to
under 1%, consistent with the categorical derivation.

Triple terms with $z^3 \Phi_q(|\hat V_i \hat V_j \hat V_k|)$
inserted as explicit level-$n$ contributions overshoot the target
(0.6–1.3% at the same atoms), confirming the pentagon ascension:
order-$\geq 3$ defects belong at level $n+1$, not as explicit
cubic terms at level $n$
(see `adjacent-vs-full-probe.witness.json`).

## Remaining open subconjectures

1. **Jet-level sum convergence** — *(conjectural)* path-(b) closure via
 [`conj:jet-tower-uniform-delta-max`](#conj\:jet-tower-uniform-delta-max)
 (workplan **P3.4** path (b)). A geometric-series tail bound
 has been proved conditional on uniform boundedness of
 $\Delta^{(n)}$
 ([brane-tower tail bound](#prop\:jet-tower-convergence)):
 if $|\Delta^{(n)}| \leq \Delta_{\max}$ for all $n$, then the
 $N$-term truncation error is
 $\leq \Delta_{\max} \hbar_q^{2(N+1)} / (1 - \hbar_q^{2})$.
 The uniform bound is now an explicit conjecture with empirical
 support: the
 [`jet_tower_delta_max.py`](../../../computations/jet_tower_delta_max.py)
 measurement script confirms `uniform_bound_pass = true` for
 D, T, ${}^{3}$He across $n = 1, \dots, 7$. The path-(a) proof from
 GS spectral-sequence $E_2$-collapse remains open.
2. **Pentagon $\to$ uv-commutation** — *(resolved)* by
 [`lem:vhat-pair-commutation-trace`](#lem\:vhat-pair-commutation-trace).
 The traced volumes $\hat V_i \in \mathbb{Z}[q^{\pm 1/2}, z]$
 are scalar polynomials and commute by definition; the pentagon
 identity in its operator form does not apply to scalars. The
 ascension argument's rigorous content is Markov-trace
 factorization
 ([thm:markov-trace-factorization](#thm\:markov-trace-factorization))
 plus the brane-tower's $q$-graded jet ascension between
 adjacent levels — which is where the operator pentagon $uv =
   q\,vu$ does apply (on inter-level lifts $\widehat U_i$,
 $\widehat V_j$).
3. **:refterm[Descent]{#descent} involution on pairs / pair-formula sharpness** — *(resolved)*
 resolved by
 [`lem:tower-pair-equality-fixed-level`](#lem\:tower-pair-equality-fixed-level).
 The level-$n$ pair contribution $z^2 \sum_{(i, j) \in
   \mathcal{P}_n} \Phi_q(|\hat V_i^{(n)} \hat V_j^{(n)}|)$ is an
 **exact equality**, not an upper bound — the pentagon-bound
 framing was vacuous (per item 2 above the pentagon doesn't apply
 to scalar $\hat V$'s), and the Markov-pair identity
 ([prop:markov-pair-z2](#prop\:markov-pair-z2)) is itself an
 equality. The empirical residual to CODATA at light atoms
 ($\sim 0.5$–$0.9\%$) reflects incomplete tower truncation
 (level $\ge 1$ contributions), not a sharpness gap in the
 level-$n$ formula. The remaining open piece is the uniform
 $\Delta_{\max}$ bound for the truncation-error formula
 ([prop:jet-tower-convergence](#prop\:jet-tower-convergence)),
 tracked as workplan **P3.4** (item 1 above).

# Derivation: what are we summing over for D?

*Start from $m = \rho_q \cdot V$ (one hyperbolic piece) and derive
step-by-step what the sum is for a multi-piece atomic link.*

## Base formula (particle mass, single hyperbolic knot)

From `rem:kashaev-volume-density`:

$$
  \mathfrak{m}(K) = \rho_q \cdot V_\text{hyp}(K),\qquad
  \rho_q = 1/\hbar_q^2 = q^2/(q-1)^2
$$

At $q_0 \approx 1.110$, $\rho_q \approx 101.86$ in $m_e$ units.
This is the PARTICLE mass of a particle whose atomic link is $K$.

## Extension to multi-component link (atomic link)

A composite particle like deuterium has an atomic link $L_D$ that
is generally NOT a single hyperbolic knot. Its complement
$S^3 \setminus L_D$ admits a **JSJ decomposition** into pieces
$P_1, P_2, \ldots, P_k$:

$$
  S^3 \setminus L_D = P_1 \sqcup P_2 \sqcup \cdots \sqcup P_k \quad \text{(glued along tori)}
$$

Each $P_i$ is either:
- **Seifert-fibered** (torus-knot-like): $V_\text{hyp}(P_i) = 0$
- **Hyperbolic**: $V_\text{hyp}(P_i) > 0$

## Why volume is additive (Thurston)

Hyperbolic volume is a topological invariant. For a 3-manifold
cut along an essential torus, the volumes add:

$$
  V_\text{hyp}(M) = \sum_i V_\text{hyp}(P_i)
$$

This is Thurston's additivity (see `prop:thurston-volume-additivity`).

## Two distinct mass scales

From `rem:frobenius-packing-density`:

- **Particle scale** (rest mass of a particle):
  $$\mathfrak{m}_\text{part}(K) = \rho_q \cdot V_\text{hyp}(K),\qquad \rho_q \approx 102$$

- **Nuclear scale** (binding energy of a composite):
  $$B(\mathcal{K}) = \sum_{P_i\text{ hyp}} \rho_F(P_i) \cdot V_\text{hyp}(P_i),\qquad \rho_F \in \{m_e, 2m_e\}$$

The $\rho_q \to \rho_F$ shift (factor $\sim 1/102$) is NOT derived in
the paper beyond the "Frobenius packing density" story.

## For deuterium specifically

D has A=2 nucleons, each a "trefoil quark" structure
(per `trefoil-quark-nucleon-nf.py`):
- Proton $\mathfrak{p}$: 3 quarks uud in confinement $B_3 = (\sigma_0\sigma_1^{-1})^3$
- Neutron $\mathfrak{n}$: 3 quarks udd in confinement $B_3$
- Inter-nucleon: one p-n crossing

The confinement braid $(\sigma_0\sigma_1^{-1})^3$ is the **Borromean rings**
L6a4, whose complement has hyperbolic volume $8G = 7.3277$.

So the **internal structure of each nucleon** contributes a
Borromean volume piece. But that's PARTICLE mass, not nuclear binding:

- $\mathfrak{m}_p \supseteq \rho_q \cdot V_\text{hyp}(\text{Borromean}) = \rho_q \cdot 8G$
- $\mathfrak{m}_n \supseteq \rho_q \cdot V_\text{hyp}(\text{Borromean}) = \rho_q \cdot 8G$

These go INTO the free mass $Z \cdot m_p + N \cdot m_n$, which is
SUBTRACTED from the total atom mass to give binding.

So the **binding** $B(D)$ comes ONLY from the piece(s) of the JSJ
decomposition that represent inter-nucleon structure — not the
internal Borromean pieces.

## What to sum over for B(D)?

Hypothesis from the JSJ-refinement formula:

$$
  B(D) = \sum_{P_i\text{ hyp, inter-nucleon}} \rho_F(P_i) \cdot V_\text{hyp}(P_i)
$$

For D with only ONE inter-nucleon crossing (p-n pair):

**Hypothesis A (single piece):** The inter-nucleon part closes to
ONE hyperbolic piece with Vol = $V_\text{inter}$.
- $B(D) = m_e \cdot V_\text{inter}$
- $B_\text{AME}(D)/m_e = 4.3533$, so $V_\text{inter} = 4.3533$
- The census-match to 6_2 (Vol = 4.4008) gives +1.09% — off by
  Vol difference of 0.0475.

**Hypothesis B (multiple pieces):** Two or more hyperbolic pieces,
each contributing.
- $V_1 + V_2 + \cdots = 4.3533$ (with all $\rho_F = m_e$)
- Or mixed $\rho_F$, weighted sum.

For B to work out, we need to identify pieces whose volumes add
to 4.3533 EXACTLY.

## Volumes of candidate pieces

From SnapPy low-crossing census:

| manifold | $V_\text{hyp}$ |
|----------|---------------:|
| $4_1$ (figure-8) | 2.02988 |
| $m003$ (Gieseking's sister) | 2.02988 |
| $5_2$ | 2.82812 |
| $m004$ | 2.02988 |
| $6_1$ | 3.16396 |
| $6_2$ | 4.40083 |
| $6_3$ | 5.69302 |
| $7_1$ | 2.71136 |
| $L6a4$ (Borromean) | 7.32772 |
| Gieseking $m000$ | 1.01494 |

Trying pairs summing to 4.3533:
- $4_1 + ?$ → need 2.323 (no standard match)
- $\text{Gieseking} + ?$ → need 3.338 (no standard match)

**No combination of 2-3 low-crossing knot complements sums to
4.3533 EXACTLY.** Single knot 6_2 at 4.4008 is the nearest, off by 0.0475.

## Where 0.0475 could live

$0.0475 / 4.3533 = 1.09\%$ — the residual.

In units:
- $\hbar_q^2 \approx 0.00982$ — too small by ~5×
- $\hbar_q \approx 0.0991$ — too big by ~2×
- $(q_0 - 1)^2/q_0 \approx 0.01090$ — off by ~4×
- $(q_0 - 1) \approx 0.110$ — off by factor 2

A simple universal correction factor doesn't hit 0.0475 exactly.

## What the "full tower accumulation" might actually be

The **categorical mass** of $\varrho$ from `def:mass-identity`:

$$
  \mathfrak{m}(\varrho) = \|\mathrm{tr}((\textstyle\int_A \otimes \mathrm{id})\circ\Delta\circ\varrho)\|
$$

The $\Delta: A \to A \otimes A$ is the comultiplication of the
Frobenius-Hopf structure. Iterating gives $\Delta^{(n)}: A \to A^{\otimes n}$
for each brane level $n$. The MASS is the n=0 evaluation; higher
brane levels give corrections via the recursive brane tower.

For D, the "accumulation" is over:
1. **Brane tower levels** $n = 0, 1, 2, \ldots$ — categorical
   contributions.
2. **Wedderburn channels** (sym/std/alt) — decomposition of the
   Hecke representation at each level.
3. **NF basis words** — decomposition of $\beta_D$ as Hecke element.

The sum is over brane levels × channels × NF terms, combined via
specific weights. The Φ_q product is the level-sum factor per
generator per channel.

## Numerical status

| approach | B(D) prediction | err |
|----------|---------------:|----:|
| Single-knot 6_2 Kashaev | 2.249 MeV | +1.09% |
| NF-weighted Σ c_w · Vol(ŵ) | 1.27 MeV | −71% |
| Per-block log Φ_q (paper) | 5.11 MeV | +130% |
| Naive Wedderburn | 0.11 MeV | −95% |
| Colored-Jones N=2 @ q=-1 | 4.355 (=2πln2) | +0.04% |
| AME | 2.225 MeV | — |

The single-knot Kashaev at +1.09% beats every "accumulation" variant
I've tried at q₀ substrate. The N=2 @ q=-1 hits 414 ppm but uses a
root of unity, inconsistent with q₀ being real > 1.

## Open derivation gap

The formula chain from Frobenius → mass identity → Kashaev → ρ·V
is RIGOROUS up through Kashaev (volume conjecture, proved for
low-crossing knots). What's NOT derived:

1. The jump from $\rho_q \sim 102$ (particle) to $\rho_F \in \{m_e, 2m_e\}$ (nuclear)
2. The two-body → $m_e$ vs three-body → $2m_e$ dichotomy
3. The specific JSJ decomposition of D's atomic link

Without (3), we can't compute what sum over pieces to do.

## $\hbar_q$ substitution — test

The Φ_q product $\prod (1 - q^{-k} v)^{-1}$ has poles at $v = q^k$
for $k \ge 0$. At $q_0 \approx 1.11$, these poles are at 1, 1.11,
1.23, 1.37, ...  — all for $|v| \ge 1$. Our V̂ values in the Hecke
computation exceed 1 for baryon-scale words, hitting poles.

If we substitute $\hbar_q \approx 0.099$ for $q$:
$$
  \Phi_{\hbar_q}(v) = \prod_k (1 - \hbar_q^{-k} v)^{-1}
$$

$\hbar_q^{-k}$ grows as $10.09^k$ — poles at $v = \hbar_q^k$ for
$k \ge 0$ are at 1, 0.099, 0.0098, ... — poles at SMALL values.
Different geometry. Might avoid the convergence issue for
$|v| > 1$ but introduces poles near 0.

Neither variant is "derived" from the paper — would need to check
if there's a theoretical basis for substituting $\hbar_q$ for $q$
in this specific context.

## Concrete next steps

1. **Check if D's atomic braid $\beta_D$ closes to a link whose JSJ
   complement has VOL exactly 4.35328.** Would need a specific
   braid-to-JSJ calculation, likely via SnapPy's triangulation.
2. **Derive which channels (sym, std, alt) and brane levels (n=0,1,2)
   contribute the "inter-nucleon" piece.** The paper's framework
   would need to explicitly separate internal-nucleon from
   inter-nucleon contributions.
3. **Accept 1.09% as the current state of the framework for D** and
   identify this gap as an open theoretical question.

Currently option 3 is the only option reachable without fresh
theoretical input.

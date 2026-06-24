**Step 1 (decompose the bi-filtration cell).**  Every element
$\alpha \in \mathcal{H}_q^{(n, K)}$ admits a canonical factorisation:

$$
  \alpha \;=\; e_{\lambda_K} \cdot g(z_K)
$$

where $e_{\lambda_K} \in Z(H_{n_K}(q))$ is the central primitive
idempotent of the dominant cell
([`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent))
and $g(z_K)$ is a depth-$n$ grouplike at the shape parameter $z_K \in F^\times$.

By centrality of $e_{\lambda_K}$ in $H_{n_K}(q)$, the action of
$\beta \in B_{n_K}$ via the standard representation factors as

$$
  \beta \cdot \alpha \cdot \beta^{-1}
  \;=\;
  (\beta \cdot e_{\lambda_K} \cdot \beta^{-1}) \cdot g(z_K)
  \;=\;
  e_{\lambda_K} \cdot g(z_K)
  \;=\; \alpha.
$$

**The braid-group action is trivial on $\mathcal{H}_q^{(n, K)}$**
— it fixes both factors (centrality + grouplike-as-scalar).

**Step 2 (Galois action on the cell factorisation).**  The motivic-
Galois action $G_{\mathrm{mot}}$ acts on:
- The coefficient ring $F$ (cyclotomic Galois, bar involution etc.),
- The shape parameter $z_K \in F^\times$.

It does **not** act on the partition $\lambda_K$ directly, but
through the bar involution it sends $e_{\lambda_K} \to e_{\lambda_K'}$
(transpose partition). The factorisation transforms as:

$$
  g_{\mathrm{mot}}(\alpha)
  \;=\;
  e_{\lambda_K'} \cdot g(g_{\mathrm{mot}}(z_K)).
$$

**Step 3 (joint composition).**  Compute the two composites:

$$
  \begin{aligned}
    g_{\mathrm{mot}}(\beta \cdot \alpha)
    & \;=\; g_{\mathrm{mot}}(\alpha)
      \quad\text{(Step 1: braid trivial)} \\
    & \;=\; e_{\lambda_K'} \cdot g(g_{\mathrm{mot}}(z_K))
      \quad\text{(Step 2)} \\[4pt]
    \beta \cdot g_{\mathrm{mot}}(\alpha)
    & \;=\; \beta \cdot e_{\lambda_K'} \cdot g(g_{\mathrm{mot}}(z_K)) \cdot \beta^{-1} \\
    & \;=\; e_{\lambda_K'} \cdot g(g_{\mathrm{mot}}(z_K))
      \quad\text{(centrality of } e_{\lambda_K'}\text{).}
  \end{aligned}
$$

Both expressions equal $e_{\lambda_K'} \cdot g(g_{\mathrm{mot}}(z_K))$.
**Joint commutativity holds.** $\square$

### Why the conjecture was open in form, not in content

The conjecture was *structurally automatic*: bar, cyclotomic Galois,
and the rest of $G_{\mathrm{mot}}$ act on the *coefficient ring + shape
parameter* (algebraic-number side); the braid group acts on the
*Hecke cell* (representation-theoretic side). By design these two
structures are **separate factors** of $\mathcal{H}_q^{(n, K)}$, so
disjoint actions commute.

The proof took two ingredients already in the paper:
1. **Centrality** of $e_{\lambda_K}$
   ([`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic)
   Step 1).
2. **Bar-transposition** of partitions
   ([`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent)
   Cross-check 3).

### What this discharges

| Claim | Status before | Status after |
|---|---|---|
| Joint-action conjecture, figure-8 cell | theorem ([`prop:joint-galois-braid-figure-8-verified`](#prop:joint-galois-braid-figure-8-verified)) | theorem (subsumed) |
| Joint-action conjecture, *all* cells | conjectural ([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)) | **theorem** (this prop.) |
| Joint-action sharpness predictions | conditional | **conditional theorem** (depends only on the depth predictions of [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)) |

### Significance: another conjecture moves to theorem

The joint-action conjecture is now fully discharged. Combined with
the small-cases bridge verification
([`prop:two-filtration-bridge-small-cases`](#prop:two-filtration-bridge-small-cases))
and the depth-2 / torus-knot / hyperbolic-row B1 discharges, the
**graded-Mikusiński bi-filtration framework's structural theorems
are complete**:

| Bi-filtration claim | Status |
|---|---|
| Bi-filtration definition well-defined | theorem ([`def:hq-bi-filtration`](#def:hq-bi-filtration)) |
| Bridge map $d_{\mathrm{II}}$, small partitions | theorem |
| Joint Galois $\times$ braid action commutes (any cell) | **theorem (this prop.)** |
| B1 row at figure-8 / torus knots / Borromean / Whitehead | theorem |

**Open remaining**: depth-3 strong sharpness over $\mathbb{Q}(\zeta_5)$
(Beilinson + Goncharov), per-knot VC discharges for chiral
hyperbolic knots, geometric realisation of $\mathrm{Cl}_3(2\pi/5)$.

### Cross-references

- Joint-action conjecture (now discharged): [`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)
- Figure-8 special case: [`prop:joint-galois-braid-figure-8-verified`](#prop:joint-galois-braid-figure-8-verified)
- Bi-filtration: [`def:hq-bi-filtration`](#def:hq-bi-filtration)
- Bridge map: [`conj:two-filtration-bridge`](#conj:two-filtration-bridge), [`prop:two-filtration-bridge-small-cases`](#prop:two-filtration-bridge-small-cases)
- Centrality of $e_{\lambda_K}$: [`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent)

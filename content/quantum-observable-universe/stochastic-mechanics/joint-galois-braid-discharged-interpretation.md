**Remark (the conjecture was open in form, not content; its discharge).**

### Open in form, not in content

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

### Content discharged

| Claim | Status before | Status after |
|---|---|---|
| Joint-action conjecture, figure-8 cell | theorem ([`prop:joint-galois-braid-figure-8-verified`](#prop:joint-galois-braid-figure-8-verified)) | theorem (subsumed) |
| Joint-action conjecture, *all* cells | conjectural ([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)) | **theorem** (this prop.) |
| Joint-action sharpness predictions | conditional | **conditional theorem** (depends only on the depth predictions of [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)) |

### Significance: a further conjecture promoted to theorem

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

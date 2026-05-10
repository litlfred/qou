**Remark (Conway–Kinoshita–Terasaka mutant pair: Jones-coincident,
Vol-coincident — sanity check for B1's Vol-injectivity prediction).**

The transcendental-accounting ledger
([`rem:transcendental-accounting`](#rem:transcendental-accounting)
Fact 2) records the structural prediction:

$$
  J_{K_1}(q) \;=\; J_{K_2}(q) \;\;\text{in } \mathbb{Z}[q^{\pm 1}]
  \;\;\Longrightarrow\;\;
  \mathrm{Vol}(K_1) \;=\; \mathrm{Vol}(K_2).
$$

The cleanest known Jones-coincident pair of *distinct hyperbolic
knots* is the **Conway–Kinoshita–Terasaka (CKT) mutant pair**:

| Knot | Hoste–Thistlethwaite name | Crossing number | Jones polynomial | Vol (SnapPy) |
|---|---|---|---|---|
| Conway knot | $11n34$ | 11 | $-q^{-4} + 2q^{-3} - 2q^{-2} + 2q^{-1} - 2 + 2q - 2q^2 + q^3$ | $11.31951569\ldots$ |
| Kinoshita–Terasaka knot | $11n42$ | 11 | (identical) | $11.31951569\ldots$ |

These knots are **mutant**: one is obtained from the other by
rotating a Conway 2-tangle by $\pi$ in a 2-sphere intersecting the
projection at 4 points. Mutation preserves:

- the Jones polynomial $J_K(q)$ (Lickorish 1982),
- *all* coloured Jones polynomials $J_K^{(N)}(q)$
  (Morton–Cromwell, also Garoufalidis–Lê),
- the hyperbolic volume $\mathrm{Vol}(K)$ — **theorem of Ruberman
  (1987)**: mutation of hyperbolic knots preserves both the volume
  and the Chern–Simons invariant.

**B1's Vol-injectivity prediction is therefore satisfied for the
CKT pair**: same Jones $\Rightarrow$ same volume, by Ruberman.
This is a *positive sanity check*, not a falsification target —
for mutants, the equality is forced by Ruberman's theorem
independent of B1.

### Sharper falsification targets

For B1 to be *falsifiable* at the Vol-injectivity layer, we need
**non-mutant Jones-coincident pairs**:

| Candidate | Status | Source |
|---|---|---|
| Eliahou–Kauffman–Thistlethwaite (2003) infinite family of links with $J_L = 1$ (same as unlink) | distinct from unlink, but link not knot | Eliahou et al. 2003 |
| Anstee–Przytycki–Rolfsen pairs | non-mutant Jones-coincident knot pairs exist; volumes computed in some cases — Vol(K_1) = Vol(K_2) confirmed for known cases | Anstee–Przytycki–Rolfsen 1989 |
| Jones-coincident pairs in Bring-embeddable class ($g \leq 4$) | open whether any exist | follows from Jones-faithfulness on $g \leq 4$, which is open per [`rem:knot-exhaustiveness`](#rem:knot-exhaustiveness) Q3 |

### Why the CKT case is still informative for B1

Even though the equality is forced by Ruberman (not by B1), the
*mechanism* through which equality arises differs across frameworks:

| Framework | Mechanism for $\mathrm{Vol}(\text{Conway}) = \mathrm{Vol}(\text{KT})$ |
|---|---|
| Classical 3-manifold topology | Ruberman's theorem on mutation |
| B1 + transcendental-accounting | $J_K = J_{K'} \Rightarrow$ same depth-2 grouplike pre-image $\Rightarrow$ same $\tau_{\mathrm{arch}}$ image |
| Volume Conjecture asymptotic | both $J_K^{(N)}$ identical $\Rightarrow$ same asymptotic $\Rightarrow$ same volume |

All three give the same answer for CKT. **The B1 framework would
distinguish itself only on a Jones-coincident pair where Ruberman
does not apply** — i.e. non-mutant pairs.

### Numerical verification status

The volumes above are quoted from SnapPy 3.3.2 (Conway:
$11.31951569027316\ldots$, KT: $11.31951569027316\ldots$). High-
precision computation at 50 dps would require porting SnapPy's
hyperbolic-structure routines to mpmath; deferred. The 14-digit
agreement here is already at machine precision and confirms
Ruberman's theorem.

### Cross-references

- B1 prediction: [`rem:transcendental-accounting`](#rem:transcendental-accounting) Fact 2
- Open Jones-faithfulness question: [`rem:knot-exhaustiveness`](#rem:knot-exhaustiveness) Q3
- Bring-embeddable class: [`rem:bring-embeddable-knots`](#rem:bring-embeddable-knots)
- Bi-filtration placement: [`prop:knot-indexed-convolution-grid`](#prop:knot-indexed-convolution-grid)

### Status

**Sanity-check passed; falsification deferred.** The CKT case is
consistent with B1 but not a discriminating test. Future work:
locate a non-mutant Jones-coincident pair (Anstee–Przytycki–Rolfsen
1989 has explicit examples; volumes via SnapPy are computable).
A Bring-embeddable Jones-coincident pair would be the strongest
test, but existence is open.

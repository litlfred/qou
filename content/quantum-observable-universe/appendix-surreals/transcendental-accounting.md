**Remark (transcendental-accounting ledger — every period in the
paper, indexed by Goncharov depth).**

The dual ledger to
[`rem:algebraic-core-survives`](#rem:algebraic-core-survives): that
block enumerates *what algebra survives* the archimedean wall; this
block enumerates *what transcendentals appear on the other side* —
which periods, where, how related, and whether their post-archimedean
relations are forced by pre-archimedean $q$-rational structure or
are archimedean accidents.

### Why this matters (the user's wall-crossing question)

A relation $R(\alpha_1, \ldots, \alpha_m) = 0$ in $\mathbb{Z}[q^{\pm 1}]$
on the algebraic side **survives** under the archimedean realization
functor $\tau_{\mathrm{arch}}$ iff it is a $q$-polynomial identity.
A relation that holds *only* among the archimedean values
$\tau_{\mathrm{arch}}(\alpha_i) \in \mathbb{R}$ but not among the
$\alpha_i \in \mathbb{Z}[q^{\pm 1}]$ is an **archimedean accident**
— typically a transcendence relation among periods (e.g. the 5-term
Bloch–Wigner relation among hyperbolic volumes).

The graded-Mikusiński keystone
([`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence))
predicts which side each relation comes from by depth. The table
below operationalises this for every period that appears in the
QOU paper.

### Master table — every transcendental at a glance

| Symbol | Depth | Algebraic input | Where it appears | $q$-rational pre-image | Archimedean accident |
|---|---|---|---|---|---|
| $\zeta_n = e^{2\pi i / n}$ | **0** | $\overline{\mathbb{Q}}^\times$ | `rem:figure-8-archimedean-illustration` ($\zeta_6$), `conj:bring-trilog-depth-3-witness` ($\zeta_5$) | itself (algebraic by def) | none — depth 0 |
| $\log\alpha$, $\alpha \in \overline{\mathbb{Q}}^\times$ | **1** | $\alpha$ algebraic | spectral / partition-function expansions, occasional in $\Phi_q$ residues | logarithmic singularity locus of $\Phi_q$ at $z = q^k$ ([`prop:quantum-dilogarithm-stratified`](#prop:quantum-dilogarithm-stratified)) | Baker's theorem on linear independence of logs of multiplicatively independent algebraics |
| $\pi$ | **2** *(Tate twist)* | — | everywhere (volumes, $\alpha_{EM}$) | period of $H^1(\mathbb{P}^1 \setminus \{0,1\})$; Tate motive denominator | none structural — $\pi$ is the Tate-motive period |
| $\zeta(2) = \pi^2/6$ | **2** | — | `rem:rh-surreal-bound` envelope | $-\mathrm{Li}_2(1)$ analytic continuation | none — pinned by Tate twist |
| $\mathrm{Cl}_2(\pi/3)$ | **2** | $\zeta_6$ | `rem:figure-8-archimedean-illustration`, `conj:bring-figure-eight-depth-2-witness` | $\mathrm{Im}\,\mathrm{Li}_2^q(\zeta_6) \in G^{(2)}(\mathcal{H}_q)$ | Bloch–Wigner 5-term relation; scissors-congruence equalities among polyhedral volumes |
| Catalan $G = \mathrm{Cl}_2(\pi/2)$ | **2** | $\zeta_4 = i$ | nuclear binding scale ${}^4$He = $A \cdot 8G$, `binding-scale-catalan` | $\mathrm{Im}\,\mathrm{Li}_2^q(i)$ | as Bloch–Wigner |
| $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ | **2** | $\zeta_6$ | `rem:figure-8-archimedean-illustration` | $2 \cdot \mathrm{Im}\,\mathrm{Li}_2^q(\zeta_6)$ on cell $e_{(2,2)}$ | scissors congruence with other 2-tetrahedra hyperbolic mfds |
| $\mathrm{Vol}(\text{Borromean}) = 8G$ | **2** | $\zeta_4$ | `rem:bring-embeddable-knots`, principled atlas | $8 \cdot \mathrm{Im}\,\mathrm{Li}_2^q(i)$ | scissors with figure-8 (forced by $\mathrm{Cl}_2(\pi/2)$ vs $\mathrm{Cl}_2(\pi/3)$ ratio — open) |
| $\mathrm{Vol}(K)$ for $K$ hyperbolic | **2** | shape param $z_K$ | `rem:bring-embeddable-knots` table, `prop:vol-through-tau` | $\mathrm{Im}\,\mathrm{Li}_2^q(z_K)$ on cell $e_{\lambda_K}$ ([`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent)) | $J_K(q) = J_{K'}(q) \Rightarrow \mathrm{Vol}(K) = \mathrm{Vol}(K')$ (Jones-faithfulness open) |
| $\zeta(3)$ Apéry's constant | **3** | — | `conj:bring-trilog-depth-3-witness` (orbit-sum cross-check) | $\mathrm{Li}_3^q(1)$ regularised; multiplicative identity $\sum_k \mathrm{Li}_3(\zeta_N^k) = (N^{1-3}-1)\zeta(3)$ | irrationality (Apéry 1978); transcendence open |
| $\mathrm{Cl}_3(2\pi/5) = \mathrm{Re}\,\mathrm{Li}_3(\zeta_5)$ | **3** | $\zeta_5$ | `conj:bring-trilog-depth-3-witness` | $\mathrm{Re}\,\mathrm{Li}_3^q(\zeta_5)$ | unknown geometric realisation (open: hyperbolic 4-mfd? CS?) |
| $S_3(2\pi/5) = \mathrm{Im}\,\mathrm{Li}_3(\zeta_5)$ | **3** | $\zeta_5$ | `conj:bring-trilog-depth-3-witness` | $\mathrm{Im}\,\mathrm{Li}_3^q(\zeta_5)$ | bar-pair partner of $\mathrm{Cl}_3$ ([`rem:chirality-period-pairing`](#rem:chirality-period-pairing)) |
| $\mathrm{CS}(K)$ for $K$ hyperbolic | **3** | shape param $z_K$ | `prop:vol-through-tau` (paired with Vol), open | depth-3 partner of $\mathrm{Vol}(K)$ in $\mathcal{H}_q$; bar-twisted under $\lambda \leftrightarrow \lambda'$ | $\mathrm{CS}(K) + i\,\mathrm{Vol}(K) \in \mathbb{C}/\pi^2\mathbb{Z}$ — complexified volume |
| $\zeta(n)$ multiple-zeta values | **$n$** | — | future / open | $\mathrm{Li}_n^q$ traces; conjecturally span $\mathcal{P}_n$ at every depth | Euler relations ($\zeta(\overline{2,3}) = ...$); MZV algebra is graded by depth $\times$ weight |

### Two structural facts the table makes visible

#### Fact 1 — depth-2 ceiling for hyperbolic 3-mfd volumes

Every hyperbolic 3-manifold volume in the paper is depth 2 — one
$\mathrm{Li}_2$ factor. This is **not** a paper-specific claim;
it is forced by the Bloch–Wigner formula $\mathrm{Vol}(M) =
\sum_i D(z_i)$ over ideal-tetrahedron triangulation. To break out
of depth 2 a different invariant is needed: $\mathrm{CS}$, hyperbolic
4-manifolds, or trilog at algebraic points (the `bring-trilog-zeta5`
route).

#### Fact 2 — pre-archimedean $q$-rational relations $\Rightarrow$ post-archimedean equalities

For any two Bring-embeddable knots $K, K'$:

$$
  J_K(q) = J_{K'}(q) \;\;\text{in } \mathbb{Z}[q^{\pm 1}]
  \;\;\;\Longrightarrow\;\;\;
  \mathrm{Vol}(K) = \mathrm{Vol}(K').
$$

Reason: $\mathrm{Vol}$ is computed from $J_K^{(N)}$ via a limit
that depends only on the polynomial. Whether the implication is
*vacuous* (no Jones-coincident pairs among Bring-embeddable knots —
i.e. Jones-faithfulness on this class) is open
([`rem:knot-exhaustiveness`](#rem:knot-exhaustiveness) Question 3).
**A single Jones-coincident pair would yield a non-trivial
post-archimedean equality forced by $q$-rational structure** —
exactly the kind of "wall-crossing" prediction the keystone
framework should make explicit.

### What does *not* survive: archimedean accidents

The 5-term Bloch–Wigner relation

$$
  D(x) + D(y) + D\!\left(\tfrac{1-x}{1-xy}\right) + D(1 - xy)
  + D\!\left(\tfrac{1-y}{1-xy}\right) \;=\; 0
$$

holds among hyperbolic volumes (after $\tau_{\mathrm{arch}}$) but is
**not** a $\mathbb{Q}(q)$-polynomial identity on the pre-archimedean
side. It's an archimedean accident at depth 2 — a relation in
$\mathcal{P}_2 / \mathcal{P}_1$ that has no $q$-polynomial witness.

Similar wall-crossing accidents at depth 3:
- Goncharov's 22-term relation for $\mathrm{Li}_3$ at 5th roots;
- $\zeta(2,1) = \zeta(3)$ (Euler 1775; an accident from the
  algebraic side, since the multiple zeta value $\zeta(2,1)$ is
  a separate iterated integral that just happens to evaluate to
  the single zeta).

### Open: post-archimedean structure forced by Bring's $S_5$

Because Bring's curve has $S_5$ symmetry, the cyclotomic field
$\mathbb{Q}(\zeta_5)$ acts on the Bring-natural depth-3 grouplikes.
Galois action $\sigma_a \colon \zeta_5 \mapsto \zeta_5^a$ for
$\gcd(a, 5) = 1$ permutes:

$$
  \{\mathrm{Li}_3(\zeta_5),\, \mathrm{Li}_3(\zeta_5^2),\, \mathrm{Li}_3(\zeta_5^3),\, \mathrm{Li}_3(\zeta_5^4)\}.
$$

The orbit-sum identity proved by the
[`bring-trilog-zeta5-depth-3.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/bring-trilog-zeta5-depth-3.witness.json)
is the **Galois-invariant trace** of this $S_5$-action. The
**Galois-non-invariant** components — individual $\mathrm{Li}_3(\zeta_5^k)$
values — give a 4-dim $\mathbb{Q}$-vector space of depth-3 periods
on which $S_5$ acts irreducibly. These are *the* depth-3
Bring-natural transcendentals; their post-archimedean structure
(linear relations over $\overline{\mathbb{Q}}$) is governed by the
motivic Galois group, not by the $q$-rational pre-image.

This is the cleanest concrete instance of "post-archimedean
structure not visible at the $q$-polynomial level": an
$S_5$-equivariant 4-dimensional period space sitting at depth 3,
generated by Bring-natural inputs.

### Cross-references

- Pre-archimedean side (what survives algebraically):
  [`rem:algebraic-core-survives`](#rem:algebraic-core-survives)
- Standard-part wall-crossing: [`conj:archimedean-stpart`](#conj:archimedean-stpart),
  [`def:standard-part-functor`](#def:standard-part-functor)
- Per-depth witnesses:
  [`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness),
  [`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness)
- Keystone: [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
- Period-class chirality: [`rem:chirality-period-pairing`](#rem:chirality-period-pairing)

### Status

**Tabulation block.** Aggregates existing paper content under a
single Goncharov-depth ledger. Adds two new structural observations:
(1) the Jones-faithfulness $\Rightarrow$ Vol-injectivity implication,
(2) the $S_5$-equivariant 4-dim depth-3 period space at $\zeta_5$.
Neither is a new theorem; both are open structural claims awaiting
a sharp formulation.

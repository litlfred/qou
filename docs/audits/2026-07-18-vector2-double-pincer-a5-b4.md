# Vector-2 double pincer on the Δ_λ magnitude scalar — A5 + B4 (2026-07-18)

**Tier:** executes ideas **A5** and **B4** of
[`2026-07-18-uploaded-papers-binding-mass-gap-ideas.md`](2026-07-18-uploaded-papers-binding-mass-gap-ideas.md),
attacking the "Vector 2" lead of
[`2026-07-18-deltalambda-attack-vector-map.md`](2026-07-18-deltalambda-attack-vector-map.md).
Audit-only; scope-(a); comparison-only; **no fit; nothing wired**. The magnitude
scalar $m \in (0, 1/\sqrt5)$ is **not** selected here. Probe + witness:
[`vector2_double_pincer_probe.py`](../../computations/probes/vector2_double_pincer_probe.py).

## What the pincer targets

The $\Delta_\lambda$ magnitude wall is one real scalar $m \in (0, 1/\sqrt5)$ (attack
map). The ceiling $1/\sqrt5$ comes from the He$^4$ $[1^4]$ complete-graph exchange
matrix $S$, whose spectrum is $\{\pm\sqrt5, \pm1\}$ so that $\det(I + mS) = (1 - 5m^2)(1 - m^2) > 0$
exactly when $m < 1/\sqrt5$
([`b4_slater_antisymmetrizer_exchange_sign.py`](../../computations/deltalambda/b4_slater_antisymmetrizer_exchange_sign.py)).
Vector 2 asks whether this $1/\sqrt5$ is the *same* $1/\sqrt5$ that appears in Bring's
$S_5$ level-5 geometry and in the icosahedral $\Sigma(2,3,5)$ modular data — i.e.
whether the ceiling is tied to level-5 structure rather than being a shared
normalization coincidence. A5 and B4 come at that $\sqrt5$ from opposite sides.

## A5 — exact spectral audit (the naive identification is refuted exactly)

All characteristic polynomials are computed exactly over $\mathbb{Q}$ (sympy):

| Object | charpoly | spectrum |
|---|---|---|
| $S$ (exchange matrix, $\mathrm{mag}=1$) | $(x-1)(x+1)(x^2-5)$ | $\{\pm\sqrt5, \pm1\}$ |
| $S^2$ | $(x-5)^2(x-1)^2$ | $\{5,5,1,1\}$ |
| $c$ (RR92 $S_5$-Gram) | $(x-5)^3(x-1)$ | $\{5,5,5,1\}$, $\det = 125$ |
| $M_S = 5I - J$ (BDH22) | $(x-5)^3(x-1)$ | $\{5,5,5,1\}$ |

Two exact facts:

1. **$c$ and $M_S$ are cospectral** (both $(x-5)^3(x-1)$), confirming the
   RR92 $m^{\mathsf T} c\, m = \mathrm{diag}(5,5,5,1)$ ↔ BDH22 $M_S$ consistency.
2. **The naive "$S$ is an $S_5$-equivariant square root of the period Gram" is
   refuted exactly.** The eigenvalue *set* $\{5,1\}$ of $S^2$ matches that of $c$, but
   the *multiplicity vector* does not: $S^2$ has $5$ with multiplicity $2$, whereas
   $c$ has it with multiplicity $3$. So $\mathrm{charpoly}(S^2) \ne \mathrm{charpoly}(c)$
   — a machine-checked non-cospectrality, not a near-match. (The attack map recorded
   this "by inspection"; here it is the exact charpoly identity.)

**Surviving A5 question (OPEN, not closed).** $S$ is odd under the $\pm$-pairing of its
spectrum, while $c$ is positive-definite. The natural Bring counterpart of the odd
$\pm\sqrt5$ structure is the **real-structure / anti-involution** action — BN12's $S'$,
or the odd part of the intersection form $C$ (both $8\times 8$). Comparing the exact
spectrum of that action restricted to the two standard-rep blocks against $\{\pm\sqrt5, \pm1\}$
would decide the surviving question. Those matrices are printed in BN12 (SIGMA 8 (2012)
065, §5.2) and RR92 §2 but are **not in the corpus**; this probe does not fabricate them
(anti-guessing rule). Open sub-item.

## B4 — exact ζ₅ Gauss sum (the origin of the 1/√5 prefactor)

Garoufalidis–Kashaev Cor 1.2 ($M=1$) evaluates the 1-dim state integral with an explicit
$1/\sqrt N$ prefactor. At $N=5$ the source of that $1/\sqrt5$ is the quadratic Gauss sum,
computed exactly as a cyclotomic integer:

$$g_5 = \sum_{k \bmod 5} \zeta_5^{k^2} = \sqrt5, \qquad g_5^2 = 5$$

(the $+$ branch since $5 \equiv 1 \pmod 4$). The icosahedral $\Sigma(2,3,5)$ vacuum row
$(2/\sqrt5)(\sin\tfrac{\pi}{5}, \sin\tfrac{2\pi}{5})$ is unit-normalized — exactly,
$\sin^2\tfrac{\pi}{5} + \sin^2\tfrac{2\pi}{5} = 5/4$ so $(2/\sqrt5)^2 \cdot 5/4 = 1$ — so its
$1/\sqrt5$ is the *same* algebraic number $\sqrt5$.

**Surviving B4 question (OPEN, not closed).** The full algebraic number multiplying
$1/\sqrt5$ in Cor 1.2's $4_1$ evaluation is $1/\sqrt5 \times (\text{root of unity}) \times (\text{Rogers exp}) \times \prod D_5(\theta, \zeta_5)$,
the cyclic-dilogarithm product over the $4_1$ angle data. The $1/\sqrt5$ is pinned
($g_5$); the $D_5$ product needs GK's explicit $4_1$ triangulation data and is left as
the open sub-item.

## Verdict — the pincer does NOT land (honest scope-(a))

- The two directions locate the **same algebraic number** $\sqrt5$ (exchange spectrum,
  quadratic Gauss sum, icosahedral S-matrix normalization).
- The naive Bring-period-Gram identification is **refuted exactly** (multiplicity
  mismatch).
- There is **no object-level derivation** that the exchange ceiling $1/\sqrt5$ *is* the
  icosahedral / Gauss-sum $1/\sqrt5$ rather than a shared normalization — many unrelated
  objects equal $\sqrt5$. The **anti-numerology gate** applies with full force (the
  audit's own B4 "Risk"): the magnitude scalar $m \in (0, 1/\sqrt5)$ remains **OPEN**,
  and nothing is wired to production.

The rigorous residue of the session: one exact falsifier (A5.4), one exact source
identification (B4.1), two named open sub-items (BN12 real-structure spectrum; the
$D_5$ $4_1$ product), and an explicit refusal to close the bridge.

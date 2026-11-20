### Proof — upper bound

**Step 1 (count starting generators).** The Galois orbit of $\zeta_K$
yields $(K - 1)/2$ complex-conjugate pairs (for prime $K \geq 3$).
Each pair gives 2 real numbers: $\mathrm{Re}\,\mathrm{Li}_n(\zeta_K^j)$
and $\mathrm{Im}\,\mathrm{Li}_n(\zeta_K^j)$. Total: $K - 1$ candidate
generators per depth.

**Step 2 (eliminate wrong-parity via Jonquière).** By
[General Jonquière Tate-rationality](#prop:jonquiere-cyclotomic-tate-rationality):

- *$n$ odd:* All $(K - 1)/2$ imaginary parts are Tate-rational
  ($\in \pi^n \mathbb{Q}$) $\to$ collapse to 0 in
  $\mathcal{P}_n / \mathrm{Tate}$. Right-parity = Re, giving
  $(K - 1)/2$ real-part candidates.
- *$n$ even:* All $(K - 1)/2$ real parts are Tate-rational $\to$ collapse
  to 0. Right-parity = Im, giving $(K - 1)/2$ imaginary-part
  candidates.

After this step: $(K - 1)/2$ candidate generators in either case.

**Step 3 (apply orbit-sum relation).** By
[General orbit-sum at every depth](#prop:cyclotomic-orbit-sum-all-depths):

- *$n$ odd:* $\sum_{k} \mathrm{Cl}_n(2\pi k/N) = (N^{1 - n} - 1)\,\zeta(n)$.
  This is **one linear relation** pulling 1 dim into the
  $\zeta(n)$-line.  For $n$ odd, $\zeta(n)$ is **not** Tate-rational
  (Apéry: $\zeta(3) \notin \pi^3 \mathbb{Q}$; conjecturally
  $\zeta(2k + 1) \notin \pi^{2k + 1} \mathbb{Q}$ for all $k \geq 1$).
  So this relation eliminates **1 dim** from the genuinely-new content.
- *$n$ even:* $\sum_{k} \mathrm{Cl}_n(2\pi k/N) = 0$. Trivial — gives
  no relation. But also no $\zeta(n)$ subtraction is needed:
  $\zeta(2k) \in \pi^{2k} \mathbb{Q}$ is **Tate-rational**, hence
  already in the Tate-line ignored at Step 2.

**Step 4 (count residual).**

- $n$ odd: $(K - 1)/2 - 1 = (K - 3)/2$ genuinely-new dimensions.
- $n$ even: $(K - 1)/2$ genuinely-new dimensions (no subtraction).

$\square$

### Lower bound — Beilinson-conditional

Borel's theorem
([Borel's theorem partially discharges the depth correspondence's sharpness target — explicit dimensions](#prop:borel-partial-resolution)):
for prime $K$, $\mathbb{Q}(\zeta_K)$ is totally complex with $r_2 =
(K - 1)/2$.

- $n$ odd: $\dim K_{2n - 1}^{\mathrm{ind}}(\mathbb{Q}(\zeta_K)) \otimes \mathbb{Q} = r_2 = (K - 1)/2$.
  Modding the $\zeta(n)$-line gives $(K - 3)/2$ predicted.
- $n$ even: $\dim K_{2n - 1}^{\mathrm{ind}}(\mathbb{Q}(\zeta_K)) \otimes \mathbb{Q} = r_1 + r_2 = (K - 1)/2$.
  No $\zeta(n)$ subtraction (it is already Tate). All $(K - 1)/2$
  predicted.

Beilinson's conjecture asserts the regulator image saturates the
Borel rank.  Combined with the upper bound: dimensions are exactly
as stated.

### Depth-2 case is theorem-level (no Beilinson)

For $n = 2$: Bloch–Suslin
([Depth-2 identification of $G^{(2)}(\mathcal{H}_q)$ with $K_3^{\mathrm{ind}}(F) \otimes \mathbb{Q}$](#prop:depth-2-identification-bloch-suslin))
proves the regulator image is precisely $K_3^{\mathrm{ind}}(F) \otimes \mathbb{Q}$
without invoking Beilinson. So:

$$
  \dim_{\mathbb{Q}} \mathcal{V}_{2, K} \;=\; (K - 1)/2
  \quad \text{(unconditional theorem for } n = 2 \text{)}.
$$

This gives concrete dimensions per prime $K$:

| $K$ | $\dim_{\mathbb{Q}} \mathcal{V}_{2, K}$ | Generators |
|---|---|---|
| 3 | 1 | $\mathrm{Cl}_2(2\pi/3)$ |
| 5 | 2 | $\mathrm{Cl}_2(2\pi/5),\, \mathrm{Cl}_2(4\pi/5)$ |
| 7 | 3 | $\mathrm{Cl}_2(2\pi/7),\, \mathrm{Cl}_2(4\pi/7),\, \mathrm{Cl}_2(6\pi/7)$ |
| 11 | 5 | 5 distinct $\mathrm{Cl}_2$ values |
| 13 | 6 | 6 distinct $\mathrm{Cl}_2$ values |

### Predictions at general $n \geq 3$

Beilinson-conditional:

| Prime $K$ | $n = 3$ (odd, $(K-3)/2$) | $n = 4$ (even, $(K-1)/2$) | $n = 5$ (odd, $(K-3)/2$) |
|---|---|---|---|
| 5 | 1 (confirmed) | 2 | 1 |
| 7 | 2 (confirmed) | 3 | 2 |
| 11 | 4 | 5 | 4 |
| 13 | 5 | 6 | 5 |

### Generalises Theorem D

Theorem D ([Cyclotomic depth-3 dimension synthesis: $(K - 3)/2$ at every prime $K \geq 5$](#prop:cyclotomic-depth3-dimension-synthesis))
gave $(K - 3)/2$ at $n = 3$.  This proposition extends to:

- All odd $n$: same $(K - 3)/2$ formula.
- All even $n$: $(K - 1)/2$ — one MORE dimension than the odd case.

The parity difference comes from $\zeta(n)$'s Tate-rationality:
$\zeta(2k) \in \pi^{2k} \mathbb{Q}$ is "free" at even depths;
$\zeta(2k + 1)$ is "costly" at odd depths (subtracts one dim).

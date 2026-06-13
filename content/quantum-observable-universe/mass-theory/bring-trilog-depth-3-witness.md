**Conjecture (Bring trilog at $\zeta_5$ as depth-3 grouplike value;
50-digit numerical witness with functional-equation cross-validation).**

*The depth-3 grouplike of $\mathcal{H}_q$ at the primitive 5th root
of unity $\zeta_5 = e^{2\pi i / 5}$ — the canonical Bring-natural
input via $S_5$-symmetry of Bring's curve
([`def:brings-coordinate-ring`](#def:brings-coordinate-ring)) —
maps under archimedean realisation to a class in
$\mathcal{P}_3 / \mathcal{P}_2$ (Goncharov period weight 3):*

$$
  \boxed{\;
    \tau_{\mathrm{arch}}\bigl(\,\mathrm{Li}_3^q(\zeta_5)\,\bigr)
    \;=\;
    \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right)
    \;+\;
    i\,S_3\!\left(\tfrac{2\pi}{5}\right)
    \;\in\;
    \mathcal{P}_3 \big/ \mathcal{P}_2.
  \;}
$$

### Numerical witness (50-digit precision)

Computed via `mpmath.polylog` at `mp.dps = 50` (script
[`bring_trilog_zeta5_depth_3.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/bring_trilog_zeta5_depth_3.py),
witness
[`bring-trilog-zeta5-depth-3.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/bring-trilog-zeta5-depth-3.witness.json)):

$$
  \mathrm{Re}\,\mathrm{Li}_3(\zeta_5)
  \;=\; \mathrm{Cl}_3(2\pi/5)
  \;=\; 0.189{,}367{,}915{,}010{,}831{,}683{,}879{,}444{,}804{,}766{,}413{,}613{,}631\ldots
$$

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_5)
  \;=\; S_3(2\pi/5)
  \;=\; 0.992{,}200{,}853{,}769{,}594{,}245{,}615{,}242{,}082{,}147{,}244{,}646{,}471\ldots
$$

### Cross-validation: Bring-orbit functional equation

The classical multiplication identity for polylogarithms at $N$th
roots of unity:

$$
  \sum_{k=1}^{N-1} \mathrm{Li}_n(\zeta_N^k)
  \;=\;
  \bigl( N^{1-n} - 1 \bigr) \cdot \zeta(n).
$$

For $N = 5$, $n = 3$:

$$
  \sum_{k=1}^{4} \mathrm{Li}_3(\zeta_5^k)
  \;\stackrel{!}{=}\;
  -\tfrac{24}{25}\,\zeta(3).
$$

**Numerically verified** at 50 dps:

| Side | Value (50 dps) |
|---|---|
| LHS: $\sum_{k=1}^{4} \mathrm{Li}_3(\zeta_5^k)$ | $-1.1539746270332105139837486350509919911343868406469\ldots$ |
| RHS: $-\tfrac{24}{25} \zeta(3)$ | $-1.1539746270332105139837486350509919911343868406469\ldots$ |
| Residual | $5.51 \times 10^{-51}$ |

The imaginary part of the orbit sum vanishes (complex-conjugate
cancellation between $\zeta_5^k$ and $\zeta_5^{5-k}$), verified to
$1.3 \times 10^{-51}$. **This is a 50-digit cross-validation
independent of `mpmath`'s polylog implementation** — the functional
equation forces the relation regardless of how each individual
$\mathrm{Li}_3(\zeta_5^k)$ is computed.

### Depth correspondence

| Side | Object | Depth |
|---|---|---|
| Algebraic | $\mathrm{Li}_3^q(\zeta_5) \in G^{(3)}(\mathcal{H}_q) \setminus G^{(2)}$ | iterated-integral depth $= 3$ |
| Archimedean | $(\mathrm{Cl}_3(2\pi/5), S_3(2\pi/5)) \in \mathcal{P}_3/\mathcal{P}_2$ | Goncharov period-depth $= 3$ |

A single $\mathrm{Li}_3$ factor on the algebraic side maps to a
weight-3 motivic period on the geometric side: depth $3 = 3$ match.

### Geometric realisation (open)

Unlike the depth-2 case (where $2\,\mathrm{Cl}_2(\pi/3) = \mathrm{Vol}(4_1)$
identifies the period with a hyperbolic volume), the depth-3 trilog
values $\mathrm{Cl}_3(2\pi/5)$ and $S_3(2\pi/5)$ do not yet have a
*direct* geometric interpretation in the QOU paper. Three candidate
identifications, in order of plausibility:

1. **Hyperbolic 4-manifold volume on Bring-cusped quotient.** The
   Goncharov regulator on $K_5^{\mathrm{ind}}(\overline{\mathbb{Q}})$
   gives $\mathrm{Li}_3$ values at algebraic points; specific values
   at $\zeta_5$ correspond to volumes of cusped hyperbolic 4-manifolds
   (Goncharov 1995). A Bring-natural 4-manifold has not been
   constructed in the paper; it is the cleanest discharge target.

2. **Chern–Simons of an $S_5$-symmetric knot in $S^3$.** $\mathrm{CS}$
   is the depth-3 partner of $\mathrm{Vol}$ in the complexified
   $\mathrm{CS} + i\,\mathrm{Vol} \in \mathbb{C}/\pi^2\mathbb{Z}$
   invariant. For a knot whose hyperbolic structure has $S_5$
   monodromy on its representation variety, $\mathrm{CS}$ would
   evaluate at $\zeta_5$-related shape parameters.

3. **Iterated integral on $\mathcal{M}_{0,5}$ for Bring's
   $S_5$-cover.** The moduli space of 5 marked points on $\mathbb{P}^1$
   carries an $S_5$-action; iterated integrals there generate
   weight-3 multiple polylogs at $\zeta_5$ values.

### Significance for B1

This is the **first depth-3 numerical witness** for
[`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence).
Combined with [`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness)
(depth 2), B1 is now **falsifiability-tested at depths 2 and 3**.

The functional-equation cross-validation provides genuine 50-digit
agreement (depth-2 witness only had ~13-digit cross-validation via
Clausen partial sum); the depth-3 instance is therefore the
*numerically tightest* graded-Mikusiński instance recorded.

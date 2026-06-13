**Conjecture (Bring figure-8 volume as depth-2 grouplike value;
50-digit numerical witness).**

*The hyperbolic volume of the figure-8 knot $4_1$ embedded in
Bring's genus-4 surface
([`rem:figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration))
equals the standard-part of $2\,\mathrm{Im}\,\mathrm{Li}_2^q$ at the
regular-ideal-tetrahedron shape parameter $z = e^{i\pi/3}$ — the
depth-2 grouplike value predicted by
[`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence):*

$$
  \mathrm{Vol}(S^3 \setminus 4_1)
  \;=\;
  \mathrm{std}\bigl( 2\,\mathrm{Im}\,\mathrm{Li}_2^q(e^{i\pi/3}) \bigr)
  \;=\;
  2\,\mathrm{Cl}_2\!\left(\tfrac{\pi}{3}\right).
$$

### Numerical witness (50-digit precision)

Computed via `mpmath.polylog` at `mp.dps = 50` (script
[`gb_depth_period_bring_fig8.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/gb_depth_period_bring_fig8.py),
witness
[`gb-depth-period-bring-fig8.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/gb-depth-period-bring-fig8.witness.json)):

$$
  2\,\mathrm{Cl}_2(\pi/3)
  \;=\;
  2.029{,}883{,}212{,}819{,}307{,}250{,}042{,}405{,}108{,}549{,}040{,}571{,}883\ldots
$$

A SnapPy-precision sanity check via independent Clausen-series
partial sum (2 million terms) agrees to $\sim 13$ digits — the
working precision of SnapPy 3.3.2's verified hyperbolic structure.
The 50-digit value is the canonical algebraic computation.

### Depth correspondence

| Side | Object | Depth |
|---|---|---|
| Algebraic | $2\,\mathrm{Li}_2^q(e^{i\pi/3}) \in G^{(2)}(\mathcal{H}_q)$ | iterated-integral depth $= 2$ |
| Archimedean | $\mathrm{Vol}(4_1) \in \mathcal{P}_2 / \mathcal{P}_1$ | Goncharov period-depth $= 2$ |

A single $\mathrm{Li}_2$ factor on the algebraic side maps to a
single Bloch-regulator class on the geometric side: depth $2 = 2$
match, by construction of the Bloch–Wigner regulator
([bloch2000], [suslin1991]).

### Bring-specific significance

The figure-8 knot is the canonical knot-theoretic witness for
Bring's surface in this paper
([`def:brings-coordinate-ring`](#def:brings-coordinate-ring)). Its
4-strand braid word $\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$
realises inside the genus-4 handlebody, and amphichirality
$4_1 \cong 4_1^{\,\mathrm{mirror}}$ pins it as a *mass invariant*
rather than a chirality invariant. Two structural facts already in
the paper are consistent with the depth-2 reading:

- The $\pi$ in $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ and the
  $\pi$ in the Bring zero-mode $\alpha_{EM}$ correction
  $2g/(4\pi(g-1))|_{g=4} = 2/(3\pi)$ share a single provenance — the
  unique archimedean shadow of pentagon-coherent substrate data on
  Bring's surface (cf.
  [`rem:figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration)).
- Both factor through the Bloch–Wigner dilogarithm at a Bring shape
  parameter — exactly the depth-2 grouplike of $\mathcal{H}_q$.
### Cross-reference: deeper-depth Bring instances (open)

The keystone predicts analogous numerical witnesses at every depth:

| Depth | Bring object | Predicted std-image |
|---|---|---|
| 2 | figure-8 in genus-4 ($4_1$) | $2\,\mathrm{Cl}_2(\pi/3) \approx 2.02988\ldots$ ✓ |
| 3 | $\mathrm{Li}_3$ at $\zeta_5$ ($S_5$-natural Bring root of unity) | $\mathrm{Im}\,\mathrm{Li}_3(\zeta_5) \in \mathcal{P}_3/\mathcal{P}_2$ |
| $n$ | $\mathrm{Li}_n^q$ at the $S_5$-orbit of $\zeta_5$ | weight-$n$ Goncharov motivic period |

**Depth-2 ceiling for hyperbolic 3-manifold volumes.** *All* hyperbolic
3-manifold volumes (figure-8, Borromean rings = $8G$, Whitehead link,
$\ldots$) are depth-2 periods — one $\mathrm{Li}_2$ factor in their
Bloch–Wigner formula. Different knots correspond to different shape
parameters at the same depth. A genuine depth-3 witness therefore
requires either (a) a trilog $\mathrm{Li}_3$ at an algebraic argument,
(b) a Chern–Simons invariant (the depth-3 part of the complexified
volume $\mathrm{CS} + i\,\mathrm{Vol} \in \mathbb{C}/\pi^2\mathbb{Z}$),
or (c) a multiple zeta value such as $\zeta(3)$. The Bring-natural
choice is (a) at the primitive 5th root of unity $\zeta_5$ — see
[`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness).

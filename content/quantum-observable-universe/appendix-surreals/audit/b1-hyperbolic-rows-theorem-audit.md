# Audit: Per-row computations for B1 hyperbolic rows

This block records the explicit cell pairing and Volume Conjecture discharge steps for the Borromean rings and Whitehead link, supporting the conditional reduction of B1 at these rows.

## Borromean rings row

**Step 1 (Bloch–Suslin depth-2 ID).**  Over $F = \mathbb{Q}(i)$:
$\dim_\mathbb{Q} K_3^{\mathrm{ind}}(\mathbb{Q}(i)) \otimes \mathbb{Q} = 1$
([`prop:borel-partial-resolution`](#prop:borel-partial-resolution),
since $\mathbb{Q}(i)$ has $r_1 = 0, r_2 = 1$). The Bloch–Suslin
regulator's image is the line spanned by $D(i) = \mathrm{Cl}_2(\pi/2) = G$
(Catalan's constant).

**Step 2 (cell pairing).**  The Borromean rings have braid
representation $(\sigma_1 \sigma_2^{-1})^3 \in B_3$ closure. Its
dominant cell in $H_3(q)$ pairs with $\mathrm{Li}_2^q(i)$ via
Markov trace, producing $8 \cdot D(i) = 8 G = \mathrm{Vol}(L_{6a4})$
(Lobachevsky decomposition of the Borromean rings complement into
8 ideal regular octahedra, each contributing $G$).

**Step 3 (VC discharge — van der Veen 2008).**  van der Veen's
asymptotic analysis of the coloured Jones polynomial of the
Borromean rings gives:

$$
  \lim_{N \to \infty} \frac{2 \pi}{N} \log\bigl|J_{L_{6a4}}^{(N)}(e^{2 \pi i / N})\bigr|
  \;=\;
  \mathrm{Vol}(L_{6a4})
  \;=\;
  8\,\mathrm{Cl}_2(\pi/2).
$$

## Whitehead link row

**Steps 1–2 (Bloch–Suslin + cell pairing).** Over $\mathbb{Q}(i)$
again. The Whitehead link complement is a **single regular ideal
octahedron** (equivalently 4 ideal tetrahedra with shapes
$\{1+i,\,(1+i)/2\}$ in the SnapPy triangulation), of volume
$4 G = 8\,\Lambda(\pi/4) = 4\,\mathrm{Cl}_2(\pi/2) \approx 3.66386$ —
exactly half the Borromean rings' two-octahedron $8G$. This Step-2
geometric input is now **Lean-supported (sorry-free)**:
`QOU.Archimedean.WhiteheadVolume.vol_L5a1_eq_half_vol_B3`
($\mathrm{Vol}(L5a1) = \mathrm{Vol}(\mathcal B_3)/2$) and
`vol_L5a1_eq_4_catalan`.

**Step 3 (VC discharge — Murakami 2002).** Murakami's analysis
generalised the figure-8 calculation to the Whitehead link's
coloured Jones, giving the asymptotic match. This published discharge
is now **corroborated in-corpus numerically**: an independent
$U_q(\mathfrak{sl}_2)$ R-matrix reconstruction reproduces the leading
rate $\mathrm{Vol}(L5a1)=4G$ **formula-free** (identifying
$\beta_W=\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}\sigma_1$ against a
torus-link control) and the refined sub-leading constant
$c_0 = -0.53 \pm 0.08$ (factor $\approx 2$) from mpmath exact-root
anchors $N=6,8,10,12$ — the fit validated against the figure-8's exact
$-\tfrac14\ln 3$. The factor-2 reading is **under the knot exponent
$p=3/2$**; whether the 2-cusp link exponent differs is the one open
sub-item. See
[`docs/audits/2026-07-26-whitehead-vc-verification-and-p-exponent.md`](../../../../docs/audits/2026-07-26-whitehead-vc-verification-and-p-exponent.md)
and witnesses `computations/whitehead-volume-identification.witness.json`,
`computations/whitehead-c0-mpmath.witness.json` (PR #4274).

# Per-row computations for the hyperbolic rows of the depth correspondence

This note records the explicit cell pairing and Volume Conjecture discharge steps for the Borromean rings and Whitehead link, supporting the conditional reduction of the depth correspondence at these rows.

## Borromean rings row

**Step 1 (Bloch–Suslin depth-2 ID).**  Over $F = \mathbb{Q}(i)$:
$\dim_\mathbb{Q} K_3^{\mathrm{ind}}(\mathbb{Q}(i)) \otimes \mathbb{Q} = 1$
([Borel partial resolution](#prop:borel-partial-resolution),
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
exactly half the Borromean rings' two-octahedron $8G$, so
$\mathrm{Vol}(L5a1) = \mathrm{Vol}(\mathcal B_3)/2 = 4G$.

**Step 3 (VC discharge — van der Veen 2008; Murakami 2002).** van der
Veen ([arXiv:math/0611181](https://arxiv.org/abs/math/0611181)) **proves**
the Volume Conjecture for the Whitehead link (as a Whitehead chain) via
a *positive-sum* colored-Jones kernel
$S_{n,k} = \prod_{j=1}^{n} 2\sin^2\!\bigl((k+j)\pi/N\bigr)/\sin(j\pi/N) > 0$;
Murakami's analysis (2002) generalised the figure-8 calculation
to the same asymptotic match. This published discharge is
**corroborated three independent ways**, formula-free:

1. **[Kas95] §3 face-index state sum** on the 2-bridge $b(8,3)$ plat
   presentation (plat word $[-2,-2,1,-2,-2]$, strands $(2,9)$), evaluated
   by tensor-network contraction to $N=31$;
2. an independent $U_q(\mathfrak{sl}_2)$ $R$-matrix reconstruction at roots of unity
   (in the Kashaev normalisation), matching the state sum on every
   root of unity ($\beta_W=\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}\sigma_1$
   identified against a torus-link control); and
3. van der Veen's positive-sum formula (arXiv:math/0611181, Lemma 1).

All three agree, and their VC growth Richardson-extrapolates to
$\mathrm{Vol}(L5a1)=4G$. The sub-leading constant is
$c_0 = -0.53 \pm 0.08$ (factor $\approx 2$) from exact-root
anchors $N=6,8,10,12$ — the fit validated against the figure-8's exact $-\tfrac14\ln 3$. The factor-2 reading is **under the knot exponent $p=3/2$** (`whitehead-volume-identification.witness.json`).

Whether the two-cusp link
exponent differs from the knot $p = 3/2$ is **settled: it does not.**
High-precision evaluation of van der Veen's exact positive sum ($N \le 3000$
at 100 decimal places) fits $p = 1.4999992$ against a figure-eight control of
$1.49999998$, i.e. $p = 3/2$ for the two-cusped L5a1 as well; apparent low-$N$
instability comes only from the $O(N^9)$ $R$-matrix's $N \le 14$ ceiling,
which the $O(N^2)$ van der Veen formula avoids. The same evaluation pins the
sub-leading constant to $2^{-3/4}$ to 20 digits (`whitehead-c-sigma-hiprec.witness.json`).

Two geometric remarks apply to that sub-leading constant. Its *geometric* derivation does **not** run through a naive adjoint-torsion determinant: that determinant is not a
triangulation invariant (producing 8 distinct values for $5_2$ under retriangulation),
and no per-cusp factor $2^{(c-1)/2}$ arises — against
the Dimofte–Garoufalidis invariant, $c_\sigma\,|\tau_{\mathrm{DG}}|^{1/2}$
takes the *same* value $2^{-1/2}$ at $c = 1$ and $c = 2$ to 17 digits. The
triangulation-invariant one-loop torsion derivation preserves the 20-digit numerical value unchanged.

**Squeeze decomposition of Step 3.** The van der Veen positive-sum kernel decomposes the asymptotic limit into three elementary steps:

1. the **saddle value** identity —
   $\int_0^{1/2}\bigl[2\log\bigl(2\sin\pi(u+\tfrac14)\bigr) - \log(2\sin\pi u)\bigr]\,\mathrm{d}u
   = 2\,\mathrm{Cl}_2(\pi/2)/\pi$, whose product with $2\pi$ is
   $4\,\mathrm{Cl}_2(\pi/2) = 4G$;
2. the **analytic limit** at the $\lfloor N/2\rfloor$ level —
   $(2\pi/N)\log\sum_k S_{\lfloor N/2\rfloor,k} \to 4G$, squeezed below by
   the explicit $k^\ast = \lfloor N/4\rfloor$ saddle term and above by the
   $k$-independent envelope $(2\pi/N)\log N + U_{\max}(N)$; and
3. the **reduction** of the asymptotic at $\lfloor N/2\rfloor$ to that single saddle-value input, together with the Catalan identity
   $G = \mathrm{Cl}_2(\pi/2)$ matching the saddle value to the octahedral volume $4G$ (`whitehead-kashaev-statesum.witness.json`, `whitehead-van-der-veen.witness.json`, `whitehead-saddle.witness.json`). The published result of van der Veen (2008) supplies the full root-of-unity coloured-Jones asymptotic.

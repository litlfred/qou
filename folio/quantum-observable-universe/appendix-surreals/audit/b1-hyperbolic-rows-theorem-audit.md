# Per-row computations for the hyperbolic rows of the depth correspondence

We record the explicit cell pairing and Volume Conjecture discharge steps for the Borromean rings and Whitehead link, supporting the conditional reduction of the depth correspondence at these rows.

## Borromean rings row

**Step 1 (Bloch–Suslin depth-2 ID).**  Over $F = \mathbb{Q}(i)$:
$\dim_\mathbb{Q} K_3^{\mathrm{ind}}(\mathbb{Q}(i)) \otimes \mathbb{Q} = 1$
([Borel's theorem partially discharges the depth correspondence's sharpness target — explicit dimensions](#prop:borel-partial-resolution),
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
geometric input is now **Lean-supported**:
`QOU.Archimedean.WhiteheadVolume.vol_L5a1_eq_half_vol_B3`
($\mathrm{Vol}(L5a1) = \mathrm{Vol}(\mathcal B_3)/2$) and
`vol_L5a1_eq_4_catalan`.

**Step 3 (VC discharge — van der Veen 2008; Murakami 2002).** van der
Veen ([arXiv:math/0611181](https://arxiv.org/abs/math/0611181)) **proves**
the Volume Conjecture for the Whitehead link (as a Whitehead chain) via
a *positive-sum* colored-Jones kernel
$S_{n,k} = \prod_{j=1}^{n} 2\sin^2\!\bigl((k+j)\pi/N\bigr)/\sin(j\pi/N) > 0$;
Murakami's earlier analysis (2002) generalised the figure-8 calculation
to the same asymptotic match. This published discharge is
**corroborated three independent ways**, formula-free:

1. **[Kas95] §3 face-index state sum** on the 2-bridge $b(8,3)$ plat
   presentation (plat word $[-2,-2,1,-2,-2]$, strands $(2,9)$), evaluated
   by tensor-network contraction to $N=31$;
2. an independent $U_q(\mathfrak{sl}_2)$ R-matrix reconstruction
   (`reduced_at_root`, Kashaev norm), matching the state sum on every
   root of unity ($\beta_W=\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}\sigma_1$
   identified against a torus-link control); and
3. van der Veen's positive-sum formula (arXiv:math/0611181, Lemma 1).

All three agree, and their VC growth Richardson-extrapolates to
$\mathrm{Vol}(L5a1)=4G$. The sub-leading constant is
$c_0 = -0.53 \pm 0.08$ (factor $\approx 2$) from mpmath exact-root
anchors $N=6,8,10,12$ — the fit validated against the figure-8's exact $-\tfrac14\ln 3$. The factor-2 reading is **under the knot exponent $p=3/2$**. The supporting computations are recorded in `computations/whitehead-volume-identification.witness.json` and `computations/whitehead-c0-mpmath.witness.json`.

The sub-item this note previously left open — whether the two-cusp link
exponent differs from the knot $p = 3/2$ — is **settled: it does not.**
`whitehead_c_sigma_hiprec.py` (van der Veen exact positive sum, $N \le 3000$
at 100 dps) fits $p = 1.4999992$ against a figure-eight control of
$1.49999998$, i.e. $p = 3/2$ for the two-cusped L5a1 as well; the earlier
instability was an artifact of the $O(N^9)$ R-matrix's $N \le 14$ ceiling,
which the $O(N^2)$ van der Veen formula does not have. The same run pins the
sub-leading constant to $2^{-3/4}$ to 20 digits. See
[`docs/audits/2026-08-02-whitehead-c-sigma-closed-form-2-pow-minus-3-4.md`](../../../../docs/audits/2026-08-02-whitehead-c-sigma-closed-form-2-pow-minus-3-4.md)
and `computations/whitehead-c-sigma-hiprec.witness.json`.

Two cautions on that constant, both recorded after the note above was
written. Its *geometric* derivation does **not** run through the adjoint
torsion route of `computations/whitehead_c_sigma_torsion.py`: the
determinant computed there is not a
triangulation invariant (8 distinct values for $5_2$ under retriangulation),
and the per-cusp factor $2^{(c-1)/2}$ it introduced does not exist — against
the corrected Dimofte–Garoufalidis invariant, $c_\sigma\,|\tau_{\mathrm{DG}}|^{1/2}$
is the *same* constant $2^{-1/2}$ at $c = 1$ and $c = 2$ to 17 digits. The
surviving derivation runs through the triangulation-invariant
`computations/one_loop_torsion.py`
([`2026-08-08-c-sigma-derivation-status.md`](../../../../docs/audits/2026-08-08-c-sigma-derivation-status.md),
[`2026-08-08-per-cusp-factor-dissolves.md`](../../../../docs/audits/2026-08-08-per-cusp-factor-dissolves.md)).
The 20-digit numerical value is untouched by either correction.

**Step 3 in Lean.** The van der Veen positive-sum kernel also underwrites
an in-repo squeeze proof of this row. Three pieces are unconditional and
sorry-free:

1. the **saddle value** identity
   ([`QOU.Knot.WhiteheadSaddle.saddle_integral`](../../lean/QOU/Knot/WhiteheadSaddleClausen.lean)) —
   $\int_0^{1/2}\bigl[2\log\bigl(2\sin\pi(u+\tfrac14)\bigr) - \log(2\sin\pi u)\bigr]\,\mathrm{d}u
   = 2\,\mathrm{Cl}_2(\pi/2)/\pi$, so $2\pi$ times it is
   $4\,\mathrm{Cl}_2(\pi/2) = 4G$;
2. the **analytic limit** at the $\lfloor N/2\rfloor$ level
   ([`whitehead_vc_innerSum_half`](../../lean/QOU/Knot/WhiteheadSaddleClausen.lean)) —
   $(2\pi/N)\log\sum_k S_{\lfloor N/2\rfloor,k} \to 4G$, squeezed below by
   the explicit $k^\ast = \lfloor N/4\rfloor$ saddle term and above by the
   $k$-independent envelope $(2\pi/N)\log N + U_{\max}(N)$; and
3. the **reduction** of the conjecture to that single saddle-value input
   ([`QOU.Knot.WhiteheadVC.whitehead_vc_of_saddle_value`](../../lean/QOU/Knot/WhiteheadVolumeConjecture.lean),
   §3b-cond), together with the Catalan bridge
   $G = \mathrm{Cl}_2(\pi/2)$ (`catalanG_eq_clausen_pi_div_two`) that
   matches the two constants.

What remains open is narrow and bookkeeping-shaped: the abstract
`kashaev`-linked statement `whitehead_volume_conjecture` is indexed at the
placeholder $(N-1)/2$ rather than $\lfloor N/2\rfloor$, and carries this
row's one honest `sorry` (`-- Ref: [vanderveen2008]`, bean qou-1gkf) until
the $\lfloor N/2\rfloor$ result above is ported to that index. The
published discharge (van der Veen 2008) supplies the unconditional
statement meanwhile. See
[`docs/audits/2026-07-26-whitehead-vc-verification-and-p-exponent.md`](../../../../docs/audits/2026-07-26-whitehead-vc-verification-and-p-exponent.md)
and witnesses `computations/whitehead-kashaev-statesum.witness.json`,
`computations/whitehead-van-der-veen.witness.json`,
`computations/whitehead-saddle.witness.json` (PRs #4274, #4394, #4532).

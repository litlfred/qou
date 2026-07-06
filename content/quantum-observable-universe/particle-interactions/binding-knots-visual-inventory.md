**Remark (visual inventory of binding knots).**

This block collects diagrams for the knots and links that appear
as binding operators across the QOU framework. Each entry shows
the knot/link's standard diagram (TikZ), its braid word in
$B_n$, and where it enters the binding pipeline. For per-particle
context see [knot-particle-dictionary](#rem:knot-particle-dictionary).

## Trivial: the unknot

The unknot $0_1 = T_{1,0}$ is a single unknotted circle —
the trivial element of every braid group. It carries
**zero crossings**, hence zero $q$-deformed crossing energy
$\mathfrak{E}_\times(q) = \frac{1}{2}(q - q^{-1}) \cdot 0 = 0$,
so its bare mass vanishes. Two disjoint roles:

1. **Neutrino $\nu$**: a single unknot in $H_1(q)$
   ([`knot-particle-dictionary`](#rem:knot-particle-dictionary)
   Table 1 row 1). Mass arises only from Reeb-divisor
   coupling, not from the knot itself.
2. **Each quark inside the Borromean baryon**: the three
   strands of $\mathcal{B}_3$ are individually unknotted —
   only their joint closure is non-trivial
   ([`def:borromean-baryon`](#def:borromean-baryon)).

```tex
\begin{tikzpicture}[scale=1, line width=1.2pt]
  \draw[->, >=Latex] (0:0.9) arc (0:355:0.9);
  \node at (0, 0) {\small $0_1$};
  \node at (1.6, 0) {$\equiv$};
  \node at (3.0, 0) {$\beta = \mathbf{1} \in B_1$};
\end{tikzpicture}
```

## Hopf link (the "bowtie")

The Hopf link $L2a1 = T(2, 2)$ is the simplest non-trivial
link: two circles linked once. Its braid word
$\sigma_0 \sigma_1 \in B_3$ closes to two interlocked
loops, giving the "bowtie" silhouette when drawn flat with
a single crossing per loop. This is the **gluon's**
categorical identity (strong-force mediator) per
[`knot-particle-dictionary`](#rem:knot-particle-dictionary)
Table 2 row 1.

```tex
\begin{tikzpicture}[scale=1, line width=1.2pt]
  % left ring
  \draw[->, >=Latex] (-0.6, 0) circle (0.6);
  % right ring (overlapping)
  \draw[white, line width=4pt]
    (0.6, 0) ++(165:0.6) arc (165:195:0.6);
  \draw[->, >=Latex] (0.6, 0) circle (0.6);
  \node at (0, -1.2) {\small $L2a1 = T(2,2)$};
  \node at (3.4, 0) {$\beta = \sigma_0 \sigma_1 \in B_3$};
\end{tikzpicture}
```

The full torus-link family $T(2, 2k)$ supplies the
electroweak bosons: $T(2,2)$ gluon, $T(2,4)$ $W$, $T(2,6)$
$Z$, $T(2,8)$ Higgs.

## Trefoil $3_1 = T(2,3)$

The trefoil knot is the simplest non-trivial knot, and the
canonical **electron** identity. Its braid word
$\sigma_0\sigma_1\sigma_0 \in B_3$ closes to a 3-cusp
shape with three over/under crossings. Crossing energy
$3 \cdot \mathfrak{E}_\times(q) = \frac{3}{2}(q - q^{-1})$
fixes the leptonic mass quantum.

```tex
\begin{tikzpicture}[scale=0.9, line width=1.2pt]
  % three-fold-symmetric trefoil schematic
  \foreach \a in {0, 120, 240} {
    \draw[rotate=\a]
      (0:1.0) .. controls (40:1.4) and (80:1.4) .. (120:1.0);
  }
  \node at (0, 0) {\small $3_1$};
  \node at (3.0, 0) {$\beta = \sigma_0\sigma_1\sigma_0$};
\end{tikzpicture}
```

The torus-knot family $T(2, 2k+1)$ extends to muon
$T(2,5)$, tau $T(2,7)$, and beyond.

## Figure-eight $4_1$ — the mass mechanism

The figure-eight $4_1$ is the smallest hyperbolic knot
($\mathrm{Vol}(4_1) \approx 2.0299$, the CAL-2 calibration
anchor; see
[`prop:three-calibration-inputs`](#prop:three-calibration-inputs)).
Braid word $\sigma_0\sigma_1^{-1}\sigma_0\sigma_1^{-1} \in B_3$
— alternating positive/negative crossings give amphichirality
$4_1 \cong 4_1^{\,\text{mirror}}$ (invariance under
$q \mapsto q^{-1}$). This is what selects $4_1$ as the
**Higgs / mass mechanism**
([`figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration)).

```tex
\begin{tikzpicture}[scale=0.9, line width=1.2pt]
  \draw (-1.2, 0)
    .. controls (-1.5, 1.0) and (-0.4, 1.4) .. (0.0, 0.6)
    .. controls (0.4, -0.2) and (-0.4, -0.2) .. (0.0, -0.6)
    .. controls (0.4, -1.4) and (1.5, -1.0) .. (1.2, 0)
    .. controls (1.0, 1.0) and (-1.0, 1.0) .. (-1.2, 0);
  \node at (-1.8, 0) {\small $4_1$};
  \node at (3.5, 0)
    {$\beta = \sigma_0\sigma_1^{-1}\sigma_0\sigma_1^{-1}$};
\end{tikzpicture}
```

## Borromean rings $\mathcal{B}_3 = 6^3_2$

The Borromean rings are three mutually linked circles such
that **removing any one frees the other two** — no two of
them are individually linked. Braid word
$\mathcal{B}_3 = \sigma_0\sigma_1\sigma_2\sigma_0\sigma_1\sigma_2 \in B_4$.
Hyperbolic volume $\mathrm{Vol}(\mathcal{B}_3) = 8G$
(twice the volume of a regular ideal octahedron; $G$ is
Catalan's constant). This is the **three-quark
confinement** identity for proton, neutron, $^4$He nucleus,
and the binding-energy scale
$\alpha = m_e \cdot 8G \approx 3.7445$ MeV
([`prop:binding-scale-catalan`](#prop:binding-scale-catalan)).

```tex
\begin{tikzpicture}[scale=0.85, line width=1.2pt]
  % three circles arranged at 120° offsets
  \def\R{0.85}
  \def\d{0.55}
  \draw[red!70!black] (0, \d) circle (\R);
  \draw[green!50!black] ({-\d*0.866}, {-\d*0.5}) circle (\R);
  \draw[blue!70!black] ({\d*0.866}, {-\d*0.5}) circle (\R);
  \node at (0, -2.0) {\small $6^3_2 = \mathcal{B}_3$};
  \node at (4.7, 0)
    {$\beta = \sigma_0\sigma_1\sigma_2\sigma_0\sigma_1\sigma_2$};
\end{tikzpicture}
```

(The schematic above shows the three rings overlapping; the
actual over/under crossing pattern alternates so that no
two rings are individually linked. See KnotInfo entry
$L6a4$ — also known as the three-component Brunnian link.)

## Cross-reference table

See [Table 1](#tbl:binding-knots-visual-inventory-table1-data).

## Higher-order links (in mass-table-ppb pipeline)

The zero-parameter Kashaev law $B = \rho_F \cdot \mathrm{Vol}_{\mathrm{hyp}}(K)$
in [`mass_table_ppb.py`](../../../computations/mass_table_ppb.py)
uses additional hyperbolic knots/links that do not yet have
visualizations here:

See [Table 2](#tbl:binding-knots-visual-inventory-table2-data).

These are flagged `census-assigned` in
[`mass-table-ppb.witness.json`](../../../computations/mass-table-ppb.witness.json),
indicating the assignment was selected by census search to
match AME binding energies rather than derived from first
principles ([Workplan 0b §4 derivation status](../../../docs/audits/-workplan-0b-script-rewire-handoff.md)).

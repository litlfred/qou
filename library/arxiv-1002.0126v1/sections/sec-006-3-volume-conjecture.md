---
doc_id: arxiv-1002.0126v1
doc_title: "An introduction to the volume conjecture"
section_id: sec-006-3-volume-conjecture
section_title: "Volume conjecture"
section_number: 3
pages: 15-22
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.947
doc_brief: "An introduction to the volume conjecture — This is an introduction to the Volume Conjecture and its gene r- alizations for nonexperts."
---
[]{#sec:Volume_Conjecture label="sec:Volume_Conjecture"}

In this section we state the Volume Conjecture and then prove it for the figure-eight knot. We also give supporting evidence for the conjecture.

## Statement of the Volume Conjecture

In [@Kashaev:MODPLA95] Kashaev introduced a link invariant $\langle L\rangle_N\in\mathbb{C}$ for an integer $N$ greater than one and a link $L$ by using the quantum dilogarithm. Then he observed in [@Kashaev:LETMP97] that the limit $2\pi\lim_{N\to\infty}\log|\langle K\rangle_N|/N$ is equal to the hyperbolic volume of the knot complement if a knot $K$ is hyperbolic. Here a knot in the three-sphere $S^3$ is called hyperbolic if its complement possesses a complete hyperbolic structure with finite volume. He also conjectured this would also hold for any hyperbolic knot.

In [@Murakami/Murakami:ACTAM12001] J. Murakami and I proved that Kashaev's invariant equals the $N$-dimensional colored Jones polynomial evaluated at the $N$-th root of unity, that is, $\langle L\rangle_N=J_N(L;\exp(2\pi\sqrt{-1}/N))$ and proposed that Kashaev's conjecture would hold for any knot by using the simplicial volume.

::: conjecture
[]{#conj:VC label="conj:VC"} The following equality would hold for any knot $K$. $$\begin{equation*}
  2\pi\lim_{N\to\infty}\frac{\log|J_N(K;\exp(2\pi\sqrt{-1}/N))|}{N}
  =\operatorname{Vol}(S^3\setminus{K}).
\end{equation*}$$
:::

To define the simplicial volume (or Gromov norm), we introduce the Jaco--Shalen--Johannson (JSJ) decomposition (or the torus decomposition) of a knot complement.

::: definition
Let $K$ be a knot. Then its complement $S^3\setminus{K}$ can be uniquely decomposed into hyperbolic pieces and Seifert fibered pieces by a system of tori: $$\begin{equation*}
  S^3\setminus{K}
  =
  \left(\bigsqcup H_i\right)\sqcup\left(\bigsqcup E_j\right)
\end{equation*}$$ with $H_i$ hyperbolic and $E_j$ Seifert-fibered.
:::

Then the simplicial volume of the knot complement is defined to be the sum of the hyperbolic volumes of the hyperbolic pieces.

::: definition
If a knot complement $S^3\setminus{K}$ is decomposed as above, then its simplicial volume $\operatorname{Vol}(S^3\setminus{K})$ is defined as $$\begin{equation*}
  \operatorname{Vol}(S^3\setminus{K})
  :=
  \sum_{H_i:\text{hyperbolic piece}}\text{Hyperbolic Volume of $H_i$}.
\end{equation*}$$
:::

::: example
Let us consider the $(2,1)$-cable of the figure-eight knot as shown in figure [1](#fig:2_1_fig_8){reference-type="ref" reference="fig:2_1_fig_8"}.

<figure id="fig:2_1_fig_8" data-latex-placement="h">
<embed src="2_1_cable_small.eps" />
<figcaption><span class="math inline">(2, 1)</span>-cable of the figure-eight knot</figcaption>
</figure>

Then its complement can be decomposed by a torus into two pieces (Figure [2](#fig:2_1_fig_8_JSJ){reference-type="ref" reference="fig:2_1_fig_8_JSJ"}), one hyperbolic and one Seifert fibered.

<figure id="fig:2_1_fig_8_JSJ" data-latex-placement="h">
<p><embed src="complement_2_1_cable_small.eps" /> <span class="math inline">$\underset{\text{\raisebox{-2mm}{hyperbolic}}}
    {\includegraphics[scale=0.3]{complement_fig8_small.eps}}$</span></p>
<figcaption>The JSJ decomposition of the <span class="math inline">(2, 1)</span>-cable of the figure-eight knot</figcaption>
</figure>

Therefore we have $$\begin{equation*}
  \operatorname{Vol}
  \left(
    \raisebox{-14mm}{\includegraphics[scale=0.3]{complement_2_1_cable_small.eps}}
  \right)
  =
  \operatorname{Vol}
  \left(
    \raisebox{-14mm}{\includegraphics[scale=0.3]{complement_fig8_small.eps}}
  \right).
\end{equation*}$$
:::

## Proof of the Volume Conjecture for the figure-eight knot {#subsec:proof_fig8}

We give a proof of the Volume Conjecture for the figure-eight knot due to T. Ekholm.

### Calculation of the limit

We use the formula [\[eq:fig8_single\]](#eq:fig8_single){reference-type="eqref" reference="eq:fig8_single"} of the colored Jones polynomial for the figure-eight knot $E$ due to Habiro and Lê. (See [@Habiro:SURIK2000; @Masbaum:ALGGT12003] for Habiro's method.) By a simple calculation using it, we have $$\begin{equation}
\label{eq:Jones_fig8}
  J_N\left(E;q\right)
  =
  \sum_{j=0}^{N-1}
  \prod_{k=1}^{j}
  \left(q^{(N-k)/2}-q^{-(N-k)/2}\right)
  \left(q^{(N+k)/2}-q^{-(N+k)/2}\right).
\end{equation}$$ Replacing $q$ with $\exp(2\pi\sqrt{-1}/N)$, we have $$\begin{equation*}
  J_N\left(E;\exp(2\pi\sqrt{-1}/N)\right)
  =
  \sum_{j=0}^{N-1}\prod_{k=1}^{j}f(N;k)
\end{equation*}$$ where we put $f(N;k):=4\sin^2(k\pi/N)$.

The graph of $f(N;k)$ is depicted in Figure [3](#fig:graph_f){reference-type="ref" reference="fig:graph_f"}.

<figure id="fig:graph_f" data-latex-placement="h">
<embed src="graph_f_small.eps" />
<figcaption>Graph of <span class="math inline"><em>f</em>(<em>N</em>; <em>k</em>)</span></figcaption>
</figure>

Put $g(N;j):=\prod_{k=1}^{j}f(N;k)$ so that $J_N\left(E;\exp(2\pi\sqrt{-1}/N)\right)=\sum_{j=0}^{N-1}g(N;j)$. Then $g(N;j)$ decreases when $0<j<N/6$ and $5N/6<j$, and increases when $N/6<j<5N/6$. Therefore $g(N;j)$ takes its maximum at $j=5N/6$. (To be precise we need to take the integer part of $5N/6$.) See Table [1](#tbl:f_g){reference-type="ref" reference="tbl:f_g"}.

::: {#tbl:f_g}
     $j$      $0$    $\cdots$    $N/6$    $\cdots$    $5N/6$     $\cdots$    $1$
  ---------- ----- ------------ ------- ------------ --------- ------------ -----
   $f(N;k)$            $<1$       $1$       $>1$        $1$        $<1$     
   $g(N;j)$   $1$   $\searrow$           $\nearrow$   maximum   $\searrow$  

  : table of $f(N;k)$ and $g(N;j)$
:::

Since there are $N$ positive terms in $J_N\left(E;\exp(2\pi\sqrt{-1}/N)\right)=\sum_{j=0}^{N-1}g(N;j)$ and $g(N;5N/6)$ is the maximum of these terms, we have $$\begin{equation*}
  g(N;5N/6)
  \le
  J_N\left(E;\exp(2\pi\sqrt{-1}/N)\right)
  \le
  N\times g(N;5N/6).
\end{equation*}$$ Noting that each side is positive, we take their logarithms and divide them by $N$. $$\begin{equation*}
  \frac{\log{g(N;5N/6)}}{N}
  \le
  \frac{\log J_N\left(E;\exp(2\pi\sqrt{-1}/N)\right)}{N}
  \le
  \frac{\log{N}}{N}+
  \frac{\log{g(N;5N/6)}}{N}.
\end{equation*}$$ Since $\log_{N\to\infty}(\log{N})/N=0$, we have $$\begin{equation*}
  \lim_{N\to\infty}\frac{\log{g(N;5N/6)}}{N}
  \le
  \lim_{N\to\infty}
  \frac{\log J_N\left(E;\exp(2\pi\sqrt{-1}/N)\right)}{N}
  \le
  \lim_{N\to\infty}\frac{\log{g(N;5N/6)}}{N}.
\end{equation*}$$ Therefore we have $$\begin{equation*}
  \lim_{N\to\infty}
  \frac{\log{J_N\left(E;\exp(2\pi\sqrt{-1}/N)\right)}}{N}
  =
  \lim_{N\to\infty}\frac{\log{g(N;5N/6)}}{N}.
\end{equation*}$$

We can calculate the limit $\lim_{N\to\infty}\bigl(\log{g(N;5N/6)}\bigr)/N$ by integration. Since $g(N;j)=\prod_{k=1}^{j}f(N;k)$, we have $$\begin{equation}
\label{eq:Jones_integral}
\begin{split}
  \lim_{N\to\infty}\frac{\log{g(N;5N/6)}}{N}
  &=
  \lim_{N\to\infty}
  \frac{1}{N}
  \sum_{k=1}^{5N/6}\log{f(N;k)}
  \\
  &=
  2
  \lim_{N\to\infty}
  \frac{1}{N}
  \sum_{k=1}^{5N/6}\log\bigl(2\sin(k\pi/N)\bigr)
  \\
  &=
  \frac{2}{\pi}
  \int_{0}^{5\pi/6}
  \log\bigl(2\sin{x}\bigr)\,dx.
\end{split}
\end{equation}$$ What does this mean? I will explain a geometric interpretation of this integral.

### Lobachevsky function

The function defined by the integral in [\[eq:Jones_integral\]](#eq:Jones_integral){reference-type="eqref" reference="eq:Jones_integral"} is known as the Lobachevsky function. More precisely, we define the Lobachevsky function $\Lambda(\theta)$ as $$\begin{equation*}
  \Lambda(\theta)
  :=
  -\int_{0}^{\theta}\log|2\sin{x}|\,dx
\end{equation*}$$ for $\theta\in\mathbb{R}$. By using this function, we can express the limit of the colored Jones polynomial as $$\begin{equation}
\label{eq:Jones_Lobachevsky}
  \lim_{N\to\infty}
  \frac{\log{J_N\left(E;\exp(2\pi\sqrt{-1}/N)\right)}}{N}
  =
  -\frac{2}{\pi}\Lambda(5\pi/6)
\end{equation}$$ We show some properties of the Lobachevsky function (see for example [@Milnor:BULAM382]).

::: lemma
The Lobachevsky function satisfies the following two properties.

1.  The Lobachevsky function is an odd function and has period $\pi$.

2.  We have $\Lambda(2\theta)=2\Lambda(\theta)+2\Lambda(\theta+\pi/2)$. In general we have $\Lambda(n\theta)=n\sum_{k=1}^{n-1}\Lambda(\theta+k\pi/n)$.
:::

::: proof
*Proof.* The first property is easily shown by the periodicity of the sine function.

To prove the second, we use the double angle formula of the sine function: $\sin(2x)=2\sin{x}\cos{x}$. We have $$\begin{equation*}
  \log|2\sin(2x)|
  =
  \log|2\sin{x}|
  +
  \log|2\cos{x}|
  =
  \log|2\sin x|
  +
  \log|2\sin(x+\pi/2)|,
\end{equation*}$$ completing the proof. ◻
:::

From (1) we have $$\begin{equation*}
  \Lambda(5\pi/6)
  =
  \Lambda(-\pi/6)
  =
  -\Lambda(\pi/6).
\end{equation*}$$ From (2) and (1) we also have $$\begin{equation*}
  \Lambda(\pi/3)
  =
  2\Lambda(\pi/6)+2\Lambda(2\pi/3)
  =
  2\Lambda(\pi/6)-2\Lambda(\pi/3).
\end{equation*}$$ Therefore we have $$\begin{equation*}
  \Lambda(5\pi/6)=-\frac{3}{2}\Lambda(\pi/3).
\end{equation*}$$

Returning to the limit of the Jones polynomial [\[eq:Jones_Lobachevsky\]](#eq:Jones_Lobachevsky){reference-type="eqref" reference="eq:Jones_Lobachevsky"}, we conclude that $$\begin{equation*}
  2\pi\lim_{N\to\infty}
  \frac{\log{J_N\left(E;\exp(2\pi\sqrt{-1}/N)\right)}}{N}
  =
  6\Lambda(\pi/3).
\end{equation*}$$

Next we show how the Lobachevsky function is related to hyperbolic geometry.

### Hyperbolic geometry {#subsubsec:geometry}

It is well known that the complement of the figure-eight knot can be decomposed into two ideal hyperbolic regular tetrahedra.

::: theorem
The complement of the figure-eight knot can be obtained by gluing two ideal hyperbolic regular tetrahedra.
:::

I will explain what is an ideal hyperbolic regular tetrahedron later. Topologically, the theorem states that the complement of the figure-eight knot can be obtained by gluing two truncated tetrahedra as in Figure [4](#fig:fig8_tetra){reference-type="ref" reference="fig:fig8_tetra"} (see also [@Murakami:FUNDM2004]). In Figure [4](#fig:fig8_tetra){reference-type="ref" reference="fig:fig8_tetra"} we identify $A$ with $A'$, $B$ with $B'$, $C$ with $C'$ and $D$ with $D'$. Note that edges with single arrows and edges with double arrows are also identified respectively.

<figure id="fig:fig8_tetra" data-latex-placement="h">
<p><embed src="complement_fig8_small.eps" /> <embed src="tetrahedron_z_small.eps" /> <embed src="tetrahedron_w_small.eps" /></p>
<figcaption>The complement of the figure-eight knot is decomposed into two ideal hyperbolic regular tetrahedra. Shadowed triangles make the boundary of the knot complement.</figcaption>
</figure>

Here I give a short introduction to hyperbolic geometry.

First consider the upper half space $\{(x,y,z)\in\mathbb{R}^3\mid z>0\}$ with hyperbolic metric $ds:=\sqrt{dx^2+dy^2+dz^2}/z$ and denote it by $\mathbb{H}^3$. It is known that a geodesic line in $\mathbb{H}^3$ is a semicircle or a straight line perpendicular to the $xy$-plane, and that a geodesic plane is a hemisphere or a flat plane perpendicular to the $xy$-plane.

An ideal hyperbolic tetrahedron is a tetrahedron in $\mathbb{H}^3$ with geodesic faces with four vertices at infinity, that is, on the $xy$-plain or at the point at infinity $\infty$. By isometry we may assume that one vertex is $\infty$ and the other three are on the $xy$-plane. So its faces consist of three perpendicular planes and a hemisphere as shown in Figure [5](#fig:tetrahedron){reference-type="ref" reference="fig:tetrahedron"}.

<figure id="fig:tetrahedron" data-latex-placement="h">
<embed src="tetrahedron_small.eps" />
<figcaption>An ideal hyperbolic tetrahedron is the part above the hemisphere surrounded by three perpendicular planes.</figcaption>
</figure>

If we see the tetrahedron from the top, it is a (Euclidean) triangle with angles $\alpha$, $\beta$, and $\gamma$.

<figure id="fig:top_view" data-latex-placement="h">
<embed src="tetrahedron_skeleton_small.eps" />
<figcaption>A top view (right) of the ideal hyperbolic tetrahedron (left)</figcaption>
</figure>

It is known that an ideal hyperbolic tetrahedron is defined (up to isometry) by the similarity class of this triangle. Therefore we can parametrize an ideal hyperbolic tetrahedron by a triple of positive numbers $(\alpha,\beta,\gamma)$ with $\alpha+\beta+\gamma=\pi$. We denote it by $\Delta(\alpha,\beta,\gamma)$.

The hyperbolic volume $\operatorname{Vol}(\Delta(\alpha,\beta,\gamma))$ can be expressed by using the Lobachevsky function $\Lambda(\theta)$. In fact it can be shown that $$\begin{equation*}
  \operatorname{Vol}(\Delta(\alpha,\beta,\gamma))
  =
  \Lambda(\alpha)+\Lambda(\beta)+\Lambda(\gamma).
\end{equation*}$$ For a proof, see for example [@Thurston:GT3M Chapter 7].

Now we return to the decomposition of the figure-eight knot complement. Figure [4](#fig:fig8_tetra){reference-type="ref" reference="fig:fig8_tetra"} shows that after identification we have two edges, edge with single arrow and edge with double arrow, each of them is obtained by identifying six edges. So if the ideal hyperbolic tetrahedra we are using are regular, that is, isometric to $\Delta(\pi/3,\pi/3,\pi/3)$ then the sum of dihedral angles around each edge becomes $2\pi$. This means that if we use two ideal hyperbolic regular tetrahedra, our gluing is geometric, that is, the complement of the figure-eight knot is isometric to the union of two copies of $\Delta(\pi/3,\pi/3,\pi/3)$. In particular its volume equals $2\operatorname{Vol}(\Delta(\pi/3,\pi/3,\pi/3))=6\Lambda(\pi/3)$.

Thus we have proved $$\begin{equation*}
  2\pi\lim_{N\to\infty}
  \frac{\log{J_N\left(E;\exp(2\pi\sqrt{-1}/N)\right)}}{N}
  =
  6\Lambda(\pi/3)
  =
  \operatorname{Vol}\left(S^3\setminus{E}\right),
\end{equation*}$$ which is the statement of the Volume Conjecture for the figure-eight knot.

## Knots and links for which the Volume Conjecture is proved

As far as I know the Volume Conjecture is proved for

1.  figure-eight knot by Ekholm,

2.  $5_2$ knot by Kashaev and Yokota,

3.  Whitehead doubles of torus knots by Zheng [@Zheng:CHIAM22007],

4.  torus knots by Kashaev and Tirkkonen [@Kashaev/Tirkkonen:ZAPNS2000],

5.  torus links of type $(2,2m)$ by Hikami [@Hikami:COMMP2004],

6.  knots and links with volume zero by van der Veen [@van_der_veen:2008],

7.  Borromean rings by Garoufalidis and Lê [@Garoufalidis/Le:2005],

8.  twisted Whitehead links by Zheng [@Zheng:CHIAM22007],

9.  Whitehead chains by van der Veen [@van_der_Veen:ACTMV2009],

10. a satellite link around the figure-eight knot with pattern the Whitehead link by Yamazaki and Yokota [@Yamazaki/Yokota].

Note that (1) and (2) are for hyperbolic knots, (3) is for a knot whose JSJ decomposition consists of a hyperbolic piece and a Seifert fibered piece, (4)--(6) are for knots and links only with Seifert pieces, (7)--(9) are for hyperbolic links, and (10) is for a link whose JSJ decomposition consists of a hyperbolic piece and a Seifert fibered piece.

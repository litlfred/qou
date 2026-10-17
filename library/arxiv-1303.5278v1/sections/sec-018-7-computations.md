---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-018-7-computations
section_title: "Computations"
section_number: 7
pages: 43-51
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.895
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
[]{#sec.computation label="sec.computation"}

## How to compute the coefficients of a $q$-series {#sub.overview.compute}

In this section we will explain a general method to compute the coefficients of a $q$-series which is given by a multi-dimensional sum of some basic $q$-series. The idea is simple, but the effective aspects of it are tricky and were explained to the first author by D. Zagier. The method is applied in forthcoming work [@GV] which computes the coefficients of the stabilization of the coloured Jones polynomial of an alternating knot [@GL2].

Fix a 1-efficient ideal triangulation $\mathcal{T}$ with $n$ tetrahedra of a 1-cusped hyperbolic manifold $M$ and an oriented multi-curve $\varpi$ on $\partial M$. The index $I_{\mathcal{T}}(\varpi)(q) \in \mathbb Z((q^{1/2}))$ is given by a convergent $(n-1)$-dimensional sum over the integers of a summand that depends on the angle structure equation matrices of $\mathcal{T}$; see Equation [\[eq.indT\]](#eq.indT){reference-type="eqref" reference="eq.indT"}. The summand of $I_{\mathcal{T}}(\varpi)$ is a product of tetrahedron indices (one per tetrahedron of $\mathcal{T}$) of linear forms in $\boldsymbol{k}=(k_1, \ldots, k_{n-1}) \in \mathbb Z^{n-1}$ and the turning number vectors $(a_{\varpi}|b_{\varpi})$ of $\varpi$.

The building block of the summand is the tetrahedron index $I_\Delta$, whose degree (i.e., minimum degree with respect to $q$) is a piecewise quadratic function on $\mathbb{R}^2$; see Section [\[sub.degI\]](#sub.degI){reference-type="ref" reference="sub.degI"}. By a *piecewise quadratic function* on $\mathbb R^m$, we mean that there exists a partition $\mathcal F$ of $\mathbb R^{m}$ into a finite number of chambers whose boundaries are rational polyhedral cones such that the restriction of the function to each chamber is given by a quadratic polynomial. It follows that for fixed $\varpi$, the degree $\delta(\varpi,\boldsymbol{k})$ of the summand in [\[eq.indT\]](#eq.indT){reference-type="eqref" reference="eq.indT"} is a piecewise quadratic function defined on a partition $\mathcal F_{\mathcal{T}}$ of $\mathbb R^{n-1}$. In a later publication, we will explain how to compute $\mathcal F_{\mathcal{T}}$ directly from $\mathcal{T}$. A priori, $\mathcal F_{\mathcal{T}}$ need not be a fan in $\mathbb R^{n-1}$ as the cones in the partition may not be convex.

Since $\mathcal{T}$ is 1-efficient, it follows that its index $I_{\mathcal{T}}(\varpi)(q)$ is a convergent series. In other words, the degree of the summand is a proper function on $\mathbb Z^{n-1}$. Thus, for fixed $\varpi$ and every half-integer $N$, the set $\{\boldsymbol{k}\in \mathbb Z^{n-1} \,: \delta(\varpi,\boldsymbol{k}) \leq N \}$ is finite. To compute the index of $\mathcal{T}$, we need to compute bounds on this finite set. Since $\delta$ is convex and piecewise quadratic, it follows that to bound $\delta(\varpi,\boldsymbol{k})$, it suffices to bound the restriction of $\delta(\varpi,\boldsymbol{k})$ to an arbitrary ray $\rho = \{ k' \rho_0: k' \in \mathbb N\}$ of $\mathcal F_T$. Now $\delta(\varpi,k' \rho_0)$ is a quadratic function of $k' \in \mathbb N$, and we obtain sharp bounds for $k_i$ typically of the form $k_i=O(\sqrt{N})$ and *exceptionally* of the form $k_i=O(N)$. The latter happens when $\delta$ has linear growth on some ray of $\mathcal F_T$. These directions of linear growth (also observed in [@GL2] in the context of stabilization of the coloured Jones function) are computationally costly. For an example, see the case of the knot $6_1$ discussed below.

The bounds for $k_i$ discussed above are rigorous and sharp, and work well for $n=2$ and $n=3$ tetrahedra. However, they quickly become inefficient when $n$ increases (e.g. $n=9$). The better way to proceed for larger $n$, as was explained to us by D. Zagier and is applied successfully in [@GV], is to use *iterated summation*. In the examples shown below for $n=2$ and $n=3$ iterated summation is not needed. For simplicity, we focus on 1-cusped manifolds and their index for $[\varpi]=0 \in H_1(\partial M;\mathbb{Z})$. The data presented below are available from [@Ga:data].

::: rmk
[]{#rem.same.index label="rem.same.index"} If two 1-cusped hyperbolic 3-manifolds $M$ and $M'$ have 1-efficient ideal triangulations $\mathcal{T}$ and $\mathcal{T}'$ with equal angle structure matrices, then $I_{\mathcal{T}}(0)(q)=I_{\mathcal{T}'}(0)(q)$. For example, $M$ and $-M$ have such triangulations, where $-M$ denotes the orientation reversed cusped hyperbolic manifold. Also, $M_{\phi}$ and $M_{-\phi}$ have such triangulations for a pseudo-Anosov homeomorphism $\phi$ of a once punctured torus, where $M_{\phi}$ denotes the mapping torus of $\phi$.
:::

## The index of the $4_1$ knot complement {#sub.index41}

The default `SnapPy` triangulation $\mathcal{T}$ of the $4_1$ knot complement uses 2 regular ideal tetrahedra and coincides with the Epstein-Penner decomposition, thus $\mathcal X_{4_1}^{\mathrm{EP}}=\{\mathcal{T}\}$. `SnapPy` gives the angle structure matrices of $\mathcal{T}$: $$\overline{\mathbf A} =
\begin{pmatrix}
2 & 2 \\
0 & 0 
\end{pmatrix} \qquad
\overline{\mathbf B} =
\begin{pmatrix}
1 & 1 \\ 
1 & 1 
\end{pmatrix} \qquad
\overline{\mathbf C} =
\begin{pmatrix}
 0 & 0 \\
 2 & 2 
\end{pmatrix}.$$ `SnapPy` also gives an additional two rows which correspond to the meridian and longitude equations; we will not use these in our examples so we omit them here. We eliminate $\overline{\mathbf B}$ to obtain $\rm A$ and $\rm B$. We choose our basic edge set $\mathcal B = \{e_1\}$ and excluded edge set $\mathcal X = \{e_2\}$. We can therefore ignore the rows of our matrices corresponding to $e_2$, and write

$$\mathbf A'= 
\left(
\begin{array}{cc}
 1 & 1 \\
\end{array}
\right)
\qquad 
\mathbf B'= 
\left(
\begin{array}{cc}
 -1 & -1 \\
\end{array}
\right)
\qquad 
\nu'=
\left(
\begin{array}{c}
 0 \\
\end{array}
\right).$$

We obtain the angle structure equations $$\mathbf A' \alpha+ \mathbf B' \gamma = \pi \nu'.$$ Equation [\[eq.indT\]](#eq.indT){reference-type="eqref" reference="eq.indT"} gives that $$I_{4_1}(0)(q)=\sum_{k \in \mathbb Z} I_{\Delta}(k,k)(q)^2 \in \mathbb Z[[q]] \, .$$ Equation [\[eq.degID\]](#eq.degID){reference-type="eqref" reference="eq.degID"} implies that the degree $\delta(k)$ of the summand is given by the piecewise quadratic polynomial $$\delta(k)=2 \delta(k,k)= 2 k^2 + |k| \, .$$ Its corresponding fan $\mathcal F_{\mathcal{T}}$ in $\mathbb R$ consists of two rays, corresponding to the columns of the matrix $$\left(
\begin{array}{cc}
 1 & -1
\end{array}
\right)\, .$$ Here, a column vector $v$ of a matrix, spans the ray $\mathbb R_+ v$. It follows that for every natural number $N$ we have $$I_{4_1}(0)(q) + O(q)^{N+1}=
\sum_{k=\lfloor 1/4 (-1 - \sqrt{1 + 8 N}) \rfloor}^{\lceil 
1/4 (-1 + \sqrt{1 + 8 N}) \rceil }
I_{\Delta}(k,k)(q)^2 + O(q)^{N+1} \, .$$ To compute $I_{\Delta}(k,k)(q) +  O(q)^{N+1}$, we use its definition [\[eq.ID\]](#eq.ID){reference-type="eqref" reference="eq.ID"} and truncate the $n$-summation as follows $$\label{eq.IDtruncated}
I_{\Delta}(k,k)(q) +  O(q)^{N+1}=
\sum_{n=\lfloor 1/2 (-1 + 2 k - \sqrt{1 - 4 k + 8 k^2 + 8 N}) \rfloor }^{
\lceil 1/4 (-1 + \sqrt{1 + 8 N}) \rceil } 
(-1)^n \frac{q^{\frac{1}{2}n(n+1)
-\left(n+\frac{1}{2}k\right)k}}{(q)_n(q)_{n+k}} + O(q)^{N+1} \, .$$ Putting everything together, the first 100 coefficients of $I_{4_1}(0)(q)$ are given by

$1-2 q-3 q^2+2 q^3+8 q^4+18 q^5+18 q^6+14 q^7-12 q^8-52 q^9-106 q^{10}-164 q^{11}-209 q^{12}-212 q^{13}-141 q^{14}+14 q^{15}+309 q^{16}+714 q^{17}+1249 q^{18}+1824 q^{19}+2401 q^{20}+2794 q^{21}+2898 q^{22}+2434 q^{23}+1256 q^{24}-918 q^{25}-4186 q^{26}-8712 q^{27}-14394 q^{28}-21046 q^{29}-28184 q^{30}-35094 q^{31}-40740 q^{32}-43732 q^{33}-42508 q^{34}-35068 q^{35}-19524 q^{36}+6288 q^{37}+43942 q^{38}+95026 q^{39}+159698 q^{40}+237774 q^{41}+326680 q^{42}+422880 q^{43}+519595 q^{44}+608636 q^{45}+677761 q^{46}+713352 q^{47}+697625 q^{48}+611956 q^{49}+434572 q^{50}+144616 q^{51}-279773 q^{52}-856288 q^{53}-1599627 q^{54}-2515906 q^{55}-3602521 q^{56}-4842516 q^{57}-6203552 q^{58}-7632646 q^{59}-9054429 q^{60}-10367858 q^{61}-11443874 q^{62}-12125534 q^{63}-12226286 q^{64}-11535062 q^{65}-9815935 q^{66}-6820480 q^{67}-2289703 q^{68}+4024698 q^{69}+12355340 q^{70}+22887604 q^{71}+35751602 q^{72}+50979996 q^{73}+68497913 q^{74}+88071340 q^{75}+109297633 q^{76}+131547294 q^{77}+153959928 q^{78}+175385202 q^{79}+194390216 q^{80}+209208210 q^{81}+217767013 q^{82}+217655122 q^{83}+206182023 q^{84}+180375446 q^{85}+137083864 q^{86}+73018494 q^{87}-15089960 q^{88}-130393760 q^{89}-275708923 q^{90}-453351590 q^{91}-664856517 q^{92}-910744842 q^{93}-1190185170 q^{94}-1500703210 q^{95}-1837805659 q^{96}-2194650672 q^{97}-2561673782 q^{98}-2926258326 q^{99}-3272416148 q^{100}$

The first 1000 coefficients are available from [@Ga:data].

## The index of the sister of the $4_1$ knot complement {#sub.index41s}

The $4_1$ knot complement and its sister are the census manifolds `m004` and `m003` respectively, and are punctured torus bundles over a circle with monodromy $+RL$ and $-RL$ respectively [@SnapPy]. The Epstein-Penner decompositions for `m004` and `m003` consist of two regular ideal tetrahedra. The edge gluing equations of $+RL$ and $-RL$ coincide. Thus, $I_{\text{{\tt m003}}}(0)=I_{\text{{\tt m004}}}(0)$.

## The index of the $5_2$ knot complement {#sub.index52}

The default `SnapPy` triangulation $\mathcal{T}$ of the $5_2$ knot complement uses 3 ideal tetrahedra. The Epstein-Penner decomposition $\mathcal{T}^{\mathrm{EP}}$ uses 4 ideal tetrahedra. Both triangulations carry geometric shape structures and thus canonical strict angle structures. One can show that $\mathcal{T}$ and $\mathcal{T}^{\mathrm{EP}}$ are related by geometric 2--3 moves hence they have equal indices. For reasons of efficiency, we will work with the triangulation $\mathcal{T}$. Its angle structure matrices are given by:

$$\overline{\mathbf A} =
\left(
\begin{array}{ccc}
 1 & 1 & 1 \\
 0 & 0 & 0 \\
 1 & 1 & 1 
\end{array}
\right)
\qquad
\overline{\mathbf B} =
\left(
\begin{array}{ccc}
 0 & 2 & 0 \\
 1 & 0 & 1 \\
 1 & 0 & 1 
\end{array}
\right)
\qquad
\overline{\mathbf C} =
\left(
\begin{array}{ccc}
 1 & 0 & 1 \\
 1 & 2 & 1 \\
 0 & 0 & 0 
\end{array}
\right) \, .$$

Eliminating $\overline{\mathbf B}$, and removing the third row (which corresponds to the third edge equation), we obtain the angle structure equations $$\mathbf A' \alpha+ \mathbf B' \gamma = \pi \nu'$$ where $$\mathbf A'=
\left(
\begin{array}{ccc}
 1 & -1 & 1 \\
 -1 & 0 & -1 \\
\end{array}
\right)
\qquad 
\mathbf B'=
\left(
\begin{array}{ccc}
 1 & -2 & 1 \\
 0 & 2 & 0 \\
\end{array}
\right)
\qquad 
\nu'=
\left(
\begin{array}{c}
 0 \\
 0 \\
\end{array}
\right) \, .$$ The index of $\mathcal{T}$ is given by $$\label{eq.ind.52}
I_{5_2}(0)(q)=\sum_{(k_1,k_2) \in \mathbb Z^2} I_{\Delta}(-k_1,k_1-k_2)^2 I_{\Delta}(2 k_1-2 k_2,-k_1)
\in \mathbb Z[[q]] \, .$$ Equation [\[eq.degID\]](#eq.degID){reference-type="eqref" reference="eq.degID"} implies that the degree $\delta(k_1,k_2)$ of the summand is a piecewise quadratic polynomial with fan $\mathcal F_{\mathcal{T}}$ given by six rays, $\rho_1, \ldots, \rho_6$, corresponding to the columns of the matrix $$\left(
\begin{array}{cccccc}
 2 & 1 & 0 & -1 & -1 & 0 \\
 1 & 1 & 1 & 0 & -1 & -1 \\
\end{array}
\right) \, .$$

<figure id="6ays">
<p><span class="math inline"><em>ρ</em><sub>5</sub></span> at -3 3 <span class="math inline"><em>ρ</em><sub>4</sub></span> at -3 18 <span class="math inline"><em>ρ</em><sub>3</sub></span> at 13 33 <span class="math inline"><em>ρ</em><sub>2</sub></span> at 38 33 <span class="math inline"><em>ρ</em><sub>1</sub></span> at 38 25 <span class="math inline"><em>ρ</em><sub>6</sub></span> at 22 3</p>
<img src="draws_eps/6rays" style="width:13.0%" />
<figcaption>The fan of the summand of <span class="math inline"><em>I</em><sub>5<sub>2</sub></sub>(0)</span>.</figcaption>
</figure>

Let $C_{ij}$ denote the two-dimensional cone with rays $\rho_i$ and $\rho_j$. Then we have: $$\delta(k_1,k_2)=
\begin{cases}
\frac{k_1}{2}+\frac{k_1^2}{2}
& \text{if} \,\, (k_1,k_2) \in C_{12} \\
-\frac{k_1}{2}-\frac{k_1^2}{2}+k_2+k_2^2
& \text{if} \,\, (k_1,k_2) \in C_{23} \\
-k_1+k_1^2+k_2-2 k_1 k_2+k_2^2
& \text{if} \,\, (k_1,k_2) \in C_{34} \\
-k_1+k_1^2
& \text{if} \,\, (k_1,k_2) \in C_{45} \\
k_1^2-k_2-2 k_1 k_2+2 k_2^2
& \text{if} \,\, (k_1,k_2) \in C_{56} \\
k_1+2 k_1^2-k_2-4 k_1 k_2+2 k_2^2
& \text{if} \,\, (k_1,k_2) \in C_{61}  \, .
\end{cases}$$ A plot of $\delta(k_1,k_2)$ for $k_1, k_2 \in [-1,1]$ is given in Figure [2](#plot.summand.52){reference-type="ref" reference="plot.summand.52"}.

![The plot of the degree of the summand of $5_2$.](draws_eps/plot_summand_52){#plot.summand.52 width="50%"}

If $\delta(k_1,k_2) \leq N$, then to bound $k_1$ from above and below we use the restriction to the rays $\rho_1$ and $\rho_5$ respectively. Likewise, to bound $k_2$ from above and below we use the restriction to the rays $\rho_2$ and $\rho_5$ respectively. The equations $$\delta(k_1,k_1)=
\begin{cases} 
(-1 + k_1) k_1 & \text{if} \,\, k_1 \leq 0 \\
\frac{1}{2} k_1 (1 + k_1) & \text{if} \,\, k_1 \geq 0
\end{cases}
\qquad
\delta(2 k_2,k_2)=
\begin{cases} 
2 k_2 (-1 + 2 k_2) k_2 & \text{if} \,\, k_2 \leq 0 \\
k_2 (1 + 2 k_2) & \text{if} \,\, k_2 \geq 0
\end{cases}$$ and the inequality $\delta(k_1,k_2) \leq N$ give the bounds $$\begin{equation} 
\label{eq.52boundsa}
\frac{1}{2} (1 - \sqrt{1 + 4 N}) \leq k_1  \leq 
\frac{1}{2} (1 + \sqrt{1 + 8 N}) 
  \end{equation} 
  \begin{equation} 
\label{eq.52boundsb}
\frac{1}{2} (1 - \sqrt{1 + 4 N}) \leq k_2  \leq 
\frac{1}{2} (1 + \sqrt{1 + 8 N}) \, .
  \end{equation}$$ With these bounds, we can compute the coefficients of $I_{5_2}(0)(q)$. The first 100 of them are given by:

$1-4 q-q^2+16 q^3+26 q^4+23 q^5-34 q^6-122 q^7-239 q^8-312 q^9-221 q^{10}+102 q^{11}+778 q^{12}+1757 q^{13}+2930 q^{14}+3825 q^{15}+4003 q^{16}+2560 q^{17}-1183 q^{18}-8033 q^{19}-18087 q^{20}-30864 q^{21}-44625 q^{22}-56225 q^{23}-60913 q^{24}-52342 q^{25}-23373 q^{26}+33675 q^{27}+124356 q^{28}+251997 q^{29}+412837 q^{30}+596153 q^{31}+778487 q^{32}+925195 q^{33}+984860 q^{34}+895092 q^{35}+579789 q^{36}-39418 q^{37}-1039055 q^{38}-2474979 q^{39}-4370844 q^{40}-6691737 q^{41}-9326308 q^{42}-12059462 q^{43}-14553043 q^{44}-16329323 q^{45}-16762776 q^{46}-15091256 q^{47}-10436174 q^{48}-1863234 q^{49}+11551967 q^{50}+30594044 q^{51}+55785006 q^{52}+87178516 q^{53}+124185931 q^{54}+165312079 q^{55}+207965719 q^{56}+248191454 q^{57}+280543349 q^{58}+297911617 q^{59}+291580973 q^{60}+251299184 q^{61}+165675668 q^{62}+22662435 q^{63}-189540512 q^{64}-481437576 q^{65}-860708203 q^{66}-1330509280 q^{67}-1887333621 q^{68}-2518748267 q^{69}-3200856694 q^{70}-3895826567 q^{71}-4549488766 q^{72}-5089337005 q^{73}-5423179738 q^{74}-5438686309 q^{75}-5004368747 q^{76}-3972096155 q^{77}-2181963773 q^{78}+530655834 q^{79}+4324768774 q^{80}+9340768927 q^{81}+15683465230 q^{82}+23402429365 q^{83}+32468254286 q^{84}+42746925974 q^{85}+53970937518 q^{86}+65710530396 q^{87}+77343886238 q^{88}+88031000047 q^{89}+96690414035 q^{90}+101984965333 q^{91}+102316085357 q^{92}+95834146866 q^{93}+80464612248 q^{94}+53958404128 q^{95}+13966121550 q^{96}-41855327561 q^{97}-115704867879 q^{98}-209460627592 q^{99}-324467541887 q^{100}$

The first 300 coefficients are available from [@Ga:data].

## The index of the $(-2,3,7)$ pretzel knot complement {#sub.index237}

The $(-2,3,7)$ pretzel knot is the 12 crossing knot `12n242` in the census. The default `SnapPy` triangulation $\mathcal{T}$ of the `12n242` complement uses 3 ideal tetrahedra. The Epstein-Penner decomposition $\mathcal{T}^{\mathrm{EP}}$ uses 3 ideal tetrahedra. However, the two triangulations $\mathcal{T}$ and $\mathcal{T}^{\mathrm{EP}}$ are combinatorially different; for instance have edge-valencies $5,6,7$ and $5,5,8$

respectively.

Nevertheless, both triangulations are geometric with canonical strict angle structure and are related by geometric 2--3 moves, which preserve the index. The angle structure equations of $\mathcal{T}$ are given by:

$$\overline{\mathbf A} =
\left(
\begin{array}{ccc}
 1 & 0 & 0 \\
 0 & 1 & 1 \\
 1 & 1 & 1
\end{array}
\right)
\qquad
\overline{\mathbf B} =
\left(
\begin{array}{ccc}
 0 & 1 & 0 \\
 1 & 1 & 0 \\
 1 & 0 & 2 
\end{array}
\right)
\qquad
\overline{\mathbf C} =
\left(
\begin{array}{ccc}
 1 & 1 & 2 \\
 1 & 0 & 0 \\
 0 & 1 & 0
\end{array}
\right) \, .$$

Apply the following operations on $(\overline{\mathbf A}|\overline{\mathbf B}|\overline{\mathbf C})$:

-   Permute the rows according to $(123) \mapsto (312)$.

-   Permute the second and third columns of $\overline{\mathbf A}$ and simultaneously, of $\overline{\mathbf B}$ and $\overline{\mathbf C}$.

-   If $\bar{\boldsymbol a}_1, \bar{\boldsymbol b}_1, \bar{\boldsymbol c}_1$ are the first columns of $\overline{\mathbf A}$, $\overline{\mathbf B}$ and $\overline{\mathbf C}$, then permute $(\bar{\boldsymbol a}_1| \bar{\boldsymbol b}_1 | \bar{\boldsymbol c}_1)\mapsto 
    (\bar{\boldsymbol b}_1| \bar{\boldsymbol c}_1 | \bar{\boldsymbol a}_1)$.

After the above permutations, the matrix $(\overline{\mathbf A}|\overline{\mathbf B}|\overline{\mathbf C})$ of the $(-2,3,7)$ pretzel knot becomes the corresponding matrix of the $5_2$ knot. Since the above permutations do not change the index, it follows that $I_{(-2,3,7)}(0)=I_{5_2}(0)$.

::: exercise
[]{#exerc.237 label="exerc.237"} Using the matrix $(\overline{\mathbf A}|\overline{\mathbf B}|\overline{\mathbf C})$ above, it follows that the index of $\mathcal{T}$ is given by $$\label{eq.ind.237}
I_{(-2,3,7)}(0)(q)=\sum_{(k_1,k_2) \in \mathbb Z^2} 
(-1)^{k_2} q^{\frac{1}{2} (k_1 - 2 k_2)}
I_{\Delta}(k_1, -k_2) I_{\Delta}(-k_1 + k_2, k_1) I_{\Delta}(-2 k_1 + 2 k_2, k_1 - 2 k_2).$$ On the other hand, the index of $5_2$ is given by Equation [\[eq.ind.52\]](#eq.ind.52){reference-type="eqref" reference="eq.ind.52"}. Using the identities of the tetrahedron index from Section [\[sec.review\]](#sec.review){reference-type="ref" reference="sec.review"}, show that $$\begin{aligned}
\sum_{(k_1,k_2) \in \mathbb Z^2} I_{\Delta}(-k_1,k_1-k_2)^2 I_{\Delta}(2 k_1-2 k_2,-k_1)
&= \\
\sum_{(k_1,k_2) \in \mathbb Z^2} 
(-1)^{k_2} q^{\frac{1}{2} (k_1 - 2 k_2)}
  I_{\Delta}(k_1, -k_2) I_{\Delta}(-k_1 + k_2, k_1) I_{\Delta}(-2 k_1 + 2 k_2, k_1 - 2 k_2). &
\end{aligned}$$
:::

## The index of the $6_1$ knot complement {#sub.index61}

In this section we discuss the index $I_{6_1}(0)$ as an example of the phenomenon of linear growth. The default `SnapPy` triangulation $\mathcal{T}$ of the $6_1$ knot complement has 4 ideal tetrahedra, and the Epstein-Penner decomposition uses 6 ideal tetrahedra. The two triangulations are related by geometric 2--3 moves and so have equal indices. The angle structure equations of $\mathcal{T}$ are given by:

$$\overline{\mathbf A} =
\left(
\begin{array}{cccc}
 1 & 1 & 0 & 0 \\
 0 & 0 & 0 & 1 \\
 0 & 1 & 1 & 0 \\
 1 & 0 & 1 & 1 
\end{array}
\right)
\qquad
\overline{\mathbf B} =
\left(
\begin{array}{cccc}
 0 & 2 & 0 & 1 \\
 1 & 0 & 1 & 0 \\
 1 & 0 & 0 & 0 \\
 0 & 0 & 1 & 1
\end{array}
\right)
\qquad
\overline{\mathbf C} =
\left(
\begin{array}{cccc}
 1 & 0 & 1 & 1 \\
 1 & 2 & 1 & 0 \\
 0 & 0 & 0 & 1 \\
 0 & 0 & 0 & 0
\end{array}
\right) \, .$$

Eliminating $\overline{\mathbf B}$, and removing the fourth row (which corresponds to the fourth edge equation), we obtain the angle structure equations $$\mathbf A' \alpha+ \mathbf B' \gamma = \pi \nu'$$ where $$\mathbf A'=
\left(
\begin{array}{cccc}
 1 & -1 & 0 & -1 \\
 -1 & 0 & -1 & 1 \\
 -1 & 1 & 1 & 0 \\
\end{array}
\right)
\qquad 
\mathbf B'=
\left(
\begin{array}{cccc}
 1 & -2 & 1 & 0 \\
 0 & 2 & 0 & 0 \\
 -1 & 0 & 0 & 1 \\
\end{array}
\right)
\qquad 
\nu'=
\left(
\begin{array}{c}
 -1 \\
 0 \\
 1 \\
\end{array}
\right) \, .$$ The index of $\mathcal{T}$ is given by $$\begin{aligned}
I_{6_1}(0)(q) &= \sum_{(k_1,k_2,k_3) \in \mathbb Z^3} 
q^{\frac{1}{2} (-k_1 + k_3)}
  I_{\Delta}(-k_1, -k_2 + k_3) I_{\Delta}(
  2 k_1 - 2 k_2, -k_1 + k_3) \\
&  I_{\Delta}(-k_3, -k_1 + k_2) I_{\Delta}(-k_1 + k_3, 
  k_1 - k_2 - k_3) \in \mathbb Z[[q]] \, .
\end{aligned}$$ $\mathcal F_{\mathcal{T}}$ in $\mathbb R^3$ has 18 rays, corresponding to the columns of the matrix $$\left(
\begin{array}{cccccccccccccccccc}
 -1 & -1 & -1 & -1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 2 & 3 \\
 -2 & -2 & -1 & 0 & 0 & 1 & -1 & -1 & -1 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 1 & 2 \\
 -3 & -1 & 0 & -1 & 0 & 0 & -2 & -1 & 0 & 1 & -1 & 0 & -1 & 1 & 0 & 1 & 1 & 1 \\
\end{array}
\right) \, .$$ If $\delta(k_1,k_2,k_3)$ denotes the degree of the summand and $N \in \mathbb N$, then $\delta(k_1,k_2,k_3) \leq N$ implies that $(k_1,k_2,k_3)$ satisfy the bounds $$\frac{1}{2} (1 - \sqrt{1 + 4 N}) \leq k_1  \leq 
\frac{1}{2} (-1 + \sqrt{1 + 12 N})$$ $$\frac{2}{3} (1 - \sqrt{1 + 3 N}) \leq k_2  \leq 
\frac{1}{2} (-1 + \sqrt{1 + 8 N})$$ $$\frac{3}{7} (1 - \sqrt{1 + 7 N}) \leq k_3  \leq 
N  \, .$$ Observe that the upper bound for $k_3$ is linear in $N$. For instance, when $N=3$, the following 17 terms (each a product of 4 truncated tetrahedron indices, as in Equation [\[eq.IDtruncated\]](#eq.IDtruncated){reference-type="eqref" reference="eq.IDtruncated"} for $N=3$) contribute to $I_{6_1}(0)+O(q)^4= 1-4 q+q^2+18 q^3+O(q)^4$:

$I_{\Delta}(-2,0)^2 I_{\Delta}(0,-2) I_{\Delta}(0,0)
-q^{-\frac{1}{2}} I_{\Delta}(-1,-1) I_{\Delta}(-1,0) I_{\Delta}(0,-1) I_{\Delta}(0,0)
+I_{\Delta}(-1,0)^2 I_{\Delta}(0,-1) I_{\Delta}(0,0)+I_{\Delta}(0,0)^4
\\ +I_{\Delta}(-2,0) I_{\Delta}(0,-1)^2 I_{\Delta}(0,1)
-q^{\frac{1}{2}} I_{\Delta}(-2,0) I_{\Delta}(-1,1) I_{\Delta}(0,1) I_{\Delta}(1,-2)
-q^{\frac{1}{2}} I_{\Delta}(-1,0) I_{\Delta}(0,1)^2 I_{\Delta}(1,-1) \\
-q^{-\frac{1}{2}} I_{\Delta}(-1,1) I_{\Delta}(0,-1)^2 I_{\Delta}(1,0)
-q^{\frac{1}{2}} I_{\Delta}(-2,1) I_{\Delta}(0,1) I_{\Delta}(1,-1) I_{\Delta}(1,0)
+I_{\Delta}(0,0) I_{\Delta}(0,1) I_{\Delta}(1,0)^2 \\
+I_{\Delta}(-2,0) I_{\Delta}(0,0) I_{\Delta}(1,-1) I_{\Delta}(1,1)
-q^{\frac{1}{2}} I_{\Delta}(0,0) I_{\Delta}(0,1) I_{\Delta}(1,0) I_{\Delta}(1,1)
+q I_{\Delta}(-2,0) I_{\Delta}(0,2)^2 I_{\Delta}(2,-2) \\
-q^{-\frac{1}{2}}I_{\Delta}(-2,0) I_{\Delta}(-1,-1) I_{\Delta}(-1,0) I_{\Delta}(2,-1)
-q^{-\frac{1}{2}}I_{\Delta}(-1,0) I_{\Delta}(-1,1) I_{\Delta}(0,-1) I_{\Delta}(2,-1) \\
-q^{-\frac{1}{2}} I_{\Delta}(-1,2) I_{\Delta}(0,0) I_{\Delta}(1,-1) I_{\Delta}(2,-1))
-q^{\frac{3}{2}} I_{\Delta}(-3,0) I_{\Delta}(0,3)^2 I_{\Delta}(3,-3)$

The first 50 coefficients of $I_{6_1}(0)$ are given by:

$1-4 q+q^2+18 q^3+22 q^4+q^5-78 q^6-178 q^7-254 q^8-188 q^9+167 q^{10}+855 q^{11}+1864 q^{12}+2892 q^{13}+3426 q^{14}+2583 q^{15}-488 q^{16}-6698 q^{17}-16273 q^{18}-28550 q^{19}-41189 q^{20}-49943 q^{21}-48554 q^{22}-28899 q^{23}+17621 q^{24}+98726 q^{25}+217819 q^{26}+371551 q^{27}+544496 q^{28}+707360 q^{29}+811832 q^{30}+792301 q^{31}+565550 q^{32}+40436 q^{33}-872995 q^{34}-2241496 q^{35}-4087180 q^{36}-6354321 q^{37}-8877834 q^{38}-11348143 q^{39}-13283739 q^{40}-14014789 q^{41}-12685231 q^{42}-8288627 q^{43}+266720 q^{44}+14032731 q^{45}+33862808 q^{46}+60173861 q^{47}+92687285 q^{48}+130092845 q^{49}+169735693 q^{50}$

## The index of the $7_2$ knot complement {#sub.index72}

The index $I_{7_2}(0)$ is another example of linear growth. The default `SnapPy` triangulation $\mathcal{T}$ of the $7_2$ knot complement has 4 ideal tetrahedra, and the Epstein-Penner decomposition has 8 ideal tetrahedra. The two triangulations are related by geometric 2--3 moves and have equal indices. The angle structure equations of $\mathcal{T}$ are given by:

$$\overline{\mathbf A} =
\left(
\begin{array}{cccc}
 1 & 2 & 1 & 0 \\
 0 & 0 & 1 & 0 \\
 1 & 0 & 0 & 1 \\
 0 & 0 & 0 & 1 
\end{array}
\right)
\qquad
\overline{\mathbf B} =
\left(
\begin{array}{cccc}
 1 & 0 & 0 & 0 \\
 1 & 0 & 0 & 0 \\
 0 & 2 & 1 & 0 \\
 0 & 0 & 1 & 2 
\end{array}
\right)
\qquad
\overline{\mathbf C} =
\left(
\begin{array}{cccc}
 0 & 0 & 1 & 0 \\
 0 & 1 & 0 & 2 \\
 1 & 1 & 1 & 0 \\
 1 & 0 & 0 & 0
\end{array}
\right) \, .$$ Eliminating $\overline{\mathbf B}$, and removing the fourth row (which corresponds to the fourth edge equation), we obtain the angle structure equations $$\mathbf A' \alpha+ \mathbf B' \gamma = \pi \nu'$$ where $$\mathbf A'=
\left(
\begin{array}{cccc}
 0 & 2 & 1 & 0 \\
 -1 & 0 & 1 & 0 \\
 1 & -2 & -1 & 1 \\
\end{array}
\right)
\qquad 
\mathbf B'=
\left(
\begin{array}{cccc}
 -1 & 0 & 1 & 0 \\
 -1 & 1 & 0 & 2 \\
 1 & -1 & 0 & 0 \\
\end{array}
\right)
\qquad 
\nu'=
\left(
\begin{array}{c}
1 \\
1 \\
-1 \\
\end{array}
\right) \, .$$ The index of $\mathcal{T}$ is given by $$\begin{aligned}
I_{7_2}(0)(q) &= \sum_{(k_1,k_2,k_3) \in \mathbb Z^3} 
(-1)^{k_1+k_2-k_3} q^{\frac{1}{2} (k_1+k_2-k_3)} 
I_{\Delta}(-k_1,k_1+k_2-k_3) I_{\Delta}(-2 k_2,k_3) \\
 & I_{\Delta}(k_1+k_2-k_3,-k_2+k_3) I_{\Delta}(-k_2+k_3,2 k_1-2 k_3)
\in \mathbb Z[[q]] \, .
\end{aligned}$$ $\mathcal F_{\mathcal{T}}$ in $\mathbb R^3$ has 14 rays, spanned by the columns of the matrix $$\left(
\begin{array}{cccccccccccccc}
 -2 & -1 & -1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 2 \\
 -1 & -1 & 0 & -1 & -1 & -1 & 0 & 1 & 1 & 0 & 0 & 0 & 1 & 1 \\
 -2 & -1 & 0 & -2 & -1 & 0 & 1 & -1 & 0 & 0 & 1 & 2 & 1 & 3 \\
\end{array}
\right) \, .$$ If $\delta(k_1,k_2,k_3)$ denotes the degree of the summand and $N \in \mathbb N$, then $\delta(k_1,k_2,k_3) \leq N$ implies that $(k_1,k_2,k_3)$ satisfy the bounds $$1 - \sqrt{1 + 2 N} \leq k_1  \leq 
\frac{1}{2} (-1 + \sqrt{1 + 8 N})$$ $$\frac{1}{2} (1 - \sqrt{1 + 4 N}) \leq k_2  \leq 
N$$ $$1 - \sqrt{1 + 2 N} \leq k_3  \leq 
\frac{1}{2} (-1 + \sqrt{1 + 12 N}) \, .$$ Observe that the upper bound for $k_3$ is linear in $N$. The first 50 coefficients of $I_{7_2}(0)$ are given by:

$1-4 q+q^2+16 q^3+20 q^4+q^5-72 q^6-156 q^7-206 q^8-98 q^9+275 q^{10}+924 q^{11}+1740 q^{12}+2370 q^{13}+2227 q^{14}+495 q^{15}-3485 q^{16}-10168 q^{17}-19045 q^{18}-28467 q^{19}-34899 q^{20}-33157 q^{21}-16460 q^{22}+22305 q^{23}+89035 q^{24}+185478 q^{25}+306146 q^{26}+434575 q^{27}+539981 q^{28}+575717 q^{29}+479148 q^{30}+176483 q^{31}-408854 q^{32}-1340316 q^{33}-2648389 q^{34}-4301970 q^{35}-6179555 q^{36}-8036073 q^{37}-9477453 q^{38}-9942897 q^{39}-8710346 q^{40}-4925980 q^{41}+2323715 q^{42}+13897628 q^{43}+30430263 q^{44}+52111135 q^{45}+78414600 q^{46}+107796294 q^{47}+137380650 q^{48}+162674912 q^{49}+177363801 q^{50}$

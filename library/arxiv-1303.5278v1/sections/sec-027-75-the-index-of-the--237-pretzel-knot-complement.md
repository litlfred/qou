---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-027-75-the-index-of-the--237-pretzel-knot-complement
section_title: "The index of the (-2,3,7) pretzel knot complement"
section_number: 7.5
pages: 47-48
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.664
latex_coverage_ratio: 0.897
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
[]{#sub.index237 label="sub.index237"}

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

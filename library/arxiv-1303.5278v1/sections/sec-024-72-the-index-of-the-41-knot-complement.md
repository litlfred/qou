---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-024-72-the-index-of-the-41-knot-complement
section_title: "The index of the 41 knot complement"
section_number: 7.2
pages: 44-45
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.938
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
[]{#sub.index41 label="sub.index41"}

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

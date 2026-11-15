---
doc_id: arxiv-1806.09450v1
doc_title: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗"
section_id: sec-003-31-the-automorphism-group-f4-of-the-exceptional
section_title: "The automorphism group F4 of the exceptional Jordan algebra and its Lie algebra f4"
section_number: 3.1
pages: 6-8
source_pdf: 1806.09450v1.pdf
source_sha256: 8556b67d97856446
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.986
doc_brief: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗ — We continue the study undertaken in [DV] of the exceptional Jordan algebra"
---
About the same time Pascual Jordan introduced his algebras Ruth Moufang studied her non-Desarguian (octonionic) projective plane $P{\mathbb O}_2$. Sixteen years later, in 1949, Jordan noticed that the points of $P{\mathbb O}_2$ are given by the one-dimensional (trace-one) idempotents of the exceptional Jordan algebra $J$ which are also the pure states of $J$.\
A glimpse on the automorphism group $F_4 = \{ g : J \to J ; g(X \circ Y) = g \, X \circ g \, Y \}$ is provided by displaying the stability subgroup of one such idempotent $$\label{eq31}
E_1 = \begin{pmatrix}
1 &0 &0 \\
0 &0 &0 \\
0 &0 &0 \end{pmatrix} \left( {\rm or} \ E_2 = \begin{pmatrix}
0 &0 &0 \\
0 &1 &0 \\
0 &0 &0 \end{pmatrix} , \ {\rm or} \ E_3 = \begin{pmatrix}
0 &0 &0 \\
0 &0 &0 \\ \, 
0 &0 &1 \end{pmatrix} \right).$$ Noting that $F_4$ should preserve the unit element ${\rm 1\mkern-4mu I}= E_1 + E_2 + E_3$ of $J$ we deduce that this stability subgroup should also preserve $E_2 + E_3$ and hence the square of any traceless element of $H_2 ({\mathbb O})$, $$\label{eq32}
X^2 = (\xi^2 + \vert x \vert^2) \begin{pmatrix}
0 &0 &0 \\
0 &1 &0 \\
0 &0 &1 \end{pmatrix} \ \mbox{for} \quad X = \begin{pmatrix}
0 &0 &0 \\
0 &\xi &x \\
0 &\bar x &-\xi \end{pmatrix}$$ and coincides with ${\rm Spin} \, (9)$ (the simply connected double covering of the orthogonal group $SO (9)$ in nine dimensions). It follows that the octonionic projective (*Moufang*) plane[^1] coincides with the homogeneous space $$\label{eq33}
{\mathbb P} {\mathbb O}_2 = F_4 / {\rm Spin} (9) \, .$$ This allows to find, in particular, the dimension of $F_4$ (over the reals): $$\label{eq34}
\dim \, (F_4) = \dim \, ({\rm Spin} (9)) + \dim \, ({\mathbb P} {\mathbb O}_2) = 36 + 16 = 52 \, .$$ With a little more work one recovers the Lie algebra ${\mathfrak f}_4$ as a direct sum of the Lie algebra $so (9)$ and its 16-dimensional spinor representation $S_9$: $$\label{eq35}
{\mathfrak f}_4 \simeq so (9) \, \dot + \, S_9 \qquad (S_9 = S_8^+ \, \dot + \, S_8^-)$$ which yields ([\[eq11\]](#eq11){reference-type="ref" reference="eq11"}) and can be interpreted in "purely octonionic" terms: $$\label{eq36}
{\mathfrak f}_4 \cong so \, ({\mathbb O} \oplus {\mathbb R}) \, \dot + \, {\mathbb O}^2 = so \, ({\mathbb O}) \, \dot + \, {\mathbb O}^3 \, .$$

Finally, we turn to a description that will also apply to higher rank exceptional Lie algebras. According to [@BS] the Lie algebra of derivations on $H_3 ({\mathbb K})$ -- the set of hermitian $3 \times 3$ matrices over any alternative composition algebra ${\mathbb K}$ -- can be presented as a sum $$\label{eq37}
{\rm Der} \, (H_3 ({\mathbb K})) \cong {\rm Der} \, ({\mathbb K}) \, \dot + \, sa_3 ({\mathbb K})$$ where $sa_3 ({\mathbb K})$ is the set of antihermitean traceless $3 \times 3$ matrices with entries in ${\mathbb K}$: $$\label{eq38}
sa_3 ({\mathbb K}) = \{ X \in {\mathbb K} \, [3] ; \ X^* = -X , \ {\rm tr} \, X = 0 \} \, .$$ Given an element $X \in sa_3 ({\mathbb K})$ there is a derivation $ad_X$ of $H_3 ({\mathbb K})$ given by $$\label{eq39}
ad_X (Y) = [X,Y] \quad \mbox{for} \quad \forall \, Y \in H_3 ({\mathbb K}) \, .$$ The subspace ${\rm Der} \, ({\mathbb K})$ in the right-hand side of ([\[eq37\]](#eq37){reference-type="ref" reference="eq37"}) is always a Lie algebra, but $sa_3 ({\mathbb K})$ is not unless ${\mathbb K}$ is commutative and associative (in which case ${\rm Der} \, ({\mathbb K})$ vanishes). Nevertheless, there is a formula for the bracket in ${\rm Der} \, [H_3({\mathbb K})]$ which applies in every case. Given $D,D' \in {\rm Der} \, [H_3({\mathbb K})]$ and $X,Y \in sa_3 ({\mathbb K})$ it reads: $$[D,D'] = DD' - D'D \, , \quad [D,ad_X] = ad_{DX} \, ,$$ $$\label{eq310}
[ad_X , ad_Y] = ad_{[X,Y]_0} + \frac13 \sum_{i,j=1}^3 D_{x_{ij} , y_{ij}}$$ where $D$ acts on $$X = \begin{pmatrix}
x_{11} &x_{12} &x_{13} \\
x_{21} &x_{22} &x_{23} \\
x_{31} &x_{32} &x_{33} 
\end{pmatrix}$$ componentwise, $[X,Y]_0$ is the trace-free part of the commutator $[X,Y]$, and $D_{x,y}$ is the derivation defined by ([\[eq24\]](#eq24){reference-type="ref" reference="eq24"}).

Summarizing, we have the following expressions for the compact form of ${\mathfrak f}_4$ (which also appears as the isometry algebra of the Riemannian manifold ${\mathbb P} {\mathbb O}^2$): $$\label{eq311}
{\mathfrak f}_4 \cong {\rm Der} \, H_3 ({\mathbb O}) \cong {\rm Der} \, ({\mathbb O}) \, \dot + \, sa_3 ({\mathbb O})$$ (a special case of ([\[eq37\]](#eq37){reference-type="ref" reference="eq37"})). Here ${\rm Der}\, ({\mathbb O})$ is the 14-dimensional exceptional Lie algebra $\mathfrak g_2$.

[^1]: The octonionic quantum mechanics in the Moufang plane is studied in [@GPR].

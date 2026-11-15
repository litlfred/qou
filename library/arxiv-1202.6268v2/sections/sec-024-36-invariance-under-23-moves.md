---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-024-36-invariance-under-23-moves
section_title: "Invariance under 2–3 moves"
section_number: 3.6
pages: 19-22
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.957
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.inv23 label="sec.inv23"}

We finally come to the proof of Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"}, *i.e.*the invariance of $\tau_{\mathcal{T}}$ under 2--3 moves. We set up the problem as in Figure [1](#fig.23){reference-type="ref" reference="fig.23"}. Namely, we suppose that $M$ has two different regular triangulations $\mathcal{T}$ and $\widetilde\mathcal{T}$, with $N$ and $N+1$ tetrahedra, respectively, which are related by a local 2--3 move. Let us denote the respective (triples of) shape parameters as

$$Z := (X_1,X_2,Z_3,...,Z_N)\,,\qquad 
\tilde Z := (W_1,W_2,W_3,Z_3,...,Z_N)\,.$$

We fix a quad type, labeling the five tetrahedra involved in the 2--3 move as in the figure. We will also assume that when calculating Neumann-Zagier matrices $\mathbf A$ and $\mathbf B$, we choose to ignore an edge that is *not* the central one of the 2--3 *bipyramid*.

![The geometry of the 2--3 move: a bipyramid split into two tetrahedra for triangulation $\bigcup_{i=1}^N\Delta_i$, and three for triangulation $\bigcup_{i=1}^{N+1} \widetilde\Delta_i$.](23){#fig.23 width="5.5in"}

There are nine linear relations among the shapes of the tetrahedra involved in the move; three come from adding dihedral angles on the equatorial edges of the bipyramid:

$$W_1'=X_1+X_2\,,\qquad W_2'=X_1'+X_2''\,,\qquad 
W_3'= X_1''+X_2'\,, \label{eqs3}$$

and six from the longitudinal edges:

$$\label{eqs6}
\begin{array}{c@{\qquad}c@{\qquad}c}
X_1=W_2+W_3''\,,& X_1'=W_3+W_1''\,,&  X_1''=W_1+W_2''\,, \\[.2cm]
X_2 = W_2''+W_3\,,& X_2'=W_1''+W_2\,,& X_2''=W_3''+W_1\,.
\end{array}$$

Moreover, due to the central edge of the bipyramid, there is an extra gluing constraint in $\widetilde\mathcal{T}$:

$$W_1'+W_2'+W_3' = 2\pi i\,. 
\label{glue3}$$

After exponentiating the relations ([\[eqs3\]](#eqs3){reference-type="ref" reference="eqs3"}--[\[glue3\]](#glue3){reference-type="ref" reference="glue3"}), and also using $z_iz_i'z_i''=-1$ and $z_i''+z_i^{-1}-1=0$ for every tetrahedron $\Delta_i$ and $\widetilde\Delta_i$, we find a birational map between the shape parameters in the two triangulations. Explicitly,

$$\begin{aligned}
\label{map23}
\Big\{w_1'=x_1x_2,\,
w_2'=\frac{1-x_2^{-1}}{1-x_1},\,
w_3'=\frac{1-x_1^{-1}}{1-x_2}\Big\}\quad\text{or}\quad 
\Big\{ x_1=\frac{1-w_2'{}^{-1}}{1-w_3'},\,x_2=\frac{1-w_3'{}^{-1}}{1-w_2'}\Big\}\,.
\end{aligned}$$

Note that the birational map is well defined and one-to-one as long as no shape parameters $(x_1,x_2,w_1,w_2,w_3)$ equal 0, 1, or $\infty$. This condition is satisfied *so long as* triangulations $\mathcal{T}$ and $\widetilde\mathcal{T}$ are both regular. (A necessary condition is that no univalent edges are created on one side or the other of the 2--3 move; this is also sufficient when considering the discrete faithful representation of $M$.)

We must also choose a flattening in the two triangulations. Let us suppose that for $\bigcup_{i=1}^{N+1}\widetilde\Delta_i$ we have a flattening with (triples of) integer parameters $\widetilde f=(d_1,d_2,d_3,f_3,...,f_N)$. This automatically determines a flattening $f= (e_1,e_2,f_3,...,f_N)$ for the $\bigcup_{i=1}^{N} \Delta_i$ triangulation, by simply setting

$$\label{flat6}
\begin{array}{c@{\qquad}c@{\qquad}c}
e_1=d_2+d_3''\,,& e_1'=d_3+d_1''\,,&  e_1''=d_1+d_2''\,, \\[.2cm]
e_2 = d_2''+d_3\,,& e_2'=d_1''+d_2\,,& e_2''=d_3''+d_1\,.
\end{array}$$

This is a discretized version of the six longitudinal relations [\[eqs6\]](#eqs6){reference-type="eqref" reference="eqs6"}. One can check that expected relations such as $e_1+e_1'+e_1''=1$ are satisfied by virtue of the discretized edge constraint $d_1'+d_2'+d_3'=2$ (*cf.* [\[glue3\]](#glue3){reference-type="eqref" reference="glue3"}).

We have all the data needed to calculate $\tau_{\mathcal{T}}$. Let us start with determinants. In the triangulation $\bigcup_{i=1}^{N} \Delta_i$, we write the matrices $\mathbf A$ and $\mathbf B$ schematically in columns as

$$\mathbf A = (a_1,\;a_2,\;a_i)\,,\quad \mathbf B = (b_1,\;b_2,\;b_i)\,,$$

with $a_i$ meaning $(a_3,a_4,...,a_N)$ and similarly for $b_i$. This leads to a determinant

$$\det\big({\mathbf A}\Delta_{z''}+{\mathbf B}\Delta_{z}^{-1}\big) 
= \det\Big(a_1x_1''+\tfrac{b_1}{x_1},\; a_2x_2''+\tfrac{b_2}{x_2},\; 
a_iz_i''+\tfrac{b_i}{z_i} \big)\,.$$

Alternatively, in the triangulation $\bigcup_{i=1}^{N+1}\widetilde\Delta_i$, the matrices $\widetilde{\mathbf A}$ and $\widetilde{\mathbf B}$ have one extra row and one extra column. The extra gluing condition [\[glue3\]](#glue3){reference-type="eqref" reference="glue3"} causes the extra row in both $\widetilde{\mathbf A}$ and $\widetilde{\mathbf B}$ to contain three $-1$'s. Altogether, the matrices take the form

$$\widetilde{\mathbf A} = \begin{pmatrix} -1 & -1 & -1  & 0 \\ 
b_1+b_2 & a_1 & a_2 & a_i \end{pmatrix}\,,\qquad \widetilde{\mathbf B} 
=\begin{pmatrix} -1 & -1 & -1 & 0 \\ 0 & a_2+b_1 & a_1+b_2 & b_i 
\end{pmatrix}\,,$$

so that

$$\begin{aligned}
\widetilde{\mathbf A}\Delta_{\tilde z''}+\widetilde{\mathbf B}\Delta_{\tilde z}^{-1} 
&= \begin{pmatrix} -w_1''-\frac{1}{w_1} & -w_2''-\frac{1}{w_2  } 
& -w_3''-\frac{1}{w_3} & 0 \\ (b_1+b_2)w_1'' & a_1w_2''+\frac{a_2+b_1}{w_2} 
& a_2 w_3''+\frac{a_1+b_2}{w_3} & a_i z_i''+\frac{b_i}{z_i} \end{pmatrix} 
\notag\\
&=  \begin{pmatrix} -1 & -1 & -1 & 0 \\ (b_1+b_2)w_1'' 
& a_1w_2''+\frac{a_2+b_1}{w_2} & a_2 w_3''+\frac{a_1+b_2}{w_3} 
& a_i z_i''+\frac{b_i}{z_i} \end{pmatrix}\,. \notag
\end{aligned}$$

It is then straightforward to check, using the map [\[map23\]](#map23){reference-type="eqref" reference="map23"}, that

$$\big(\widetilde{\mathbf A}\Delta_{\tilde z''}+\widetilde{\mathbf B}\Delta_{\tilde z}^{-1}\big) 
\begin{pmatrix} 1 & -1 & -1 & 0 \\
   0 & 1 & 0 & 0 \\
   0 & 0 & 1 & 0 \\
   0 & 0 & 0 & \mathbf{1} \end{pmatrix}
 \begin{pmatrix} 1 & 0 & 0 & 0 \\
   0 & 1 & \frac{w_3' x_2''}{x_1''} & 0 \\
   0 & \frac{w_2'x_1''}{x_2''} & 1 & 0  \\
   0 & 0 & 0 & \mathbf{1} \end{pmatrix}=
 \begin{pmatrix} -1 & 0 \\
   * & {\mathbf A}\Delta_{z''}+{\mathbf B}\Delta_{z}^{-1} \end{pmatrix}
 \,.$$

The determinant of the last matrix on the left hand side is $1-w_2'w_3'=1-w_1'{}^{-1}=w_1$. Therefore,

$$\label{det23} \det\big(\widetilde{\mathbf A}\Delta_{\tilde z''}
+\widetilde{\mathbf B}\Delta_{\tilde z}^{-1}\big) 
= -w_1^{-1}\det\big({\mathbf A}\Delta_{z''}+{\mathbf B}\Delta_{z}^{-1}\big)\,.$$

We should also consider the monomial correction. However, with flattenings related as in [\[flat6\]](#flat6){reference-type="eqref" reference="flat6"}, and with shapes related by the exponentiated version of [\[eqs6\]](#eqs6){reference-type="eqref" reference="eqs6"}, it is easy to check that

$$\widetilde z^{\tilde f''}\widetilde z''{}^{-\tilde f} 
= w_1 (-1)^{d_2''-e_1''}z^{f''}z''{}^{-f}\,. 
\label{mon23}$$

We have thus arrived at the desired result; by combining [\[det23\]](#det23){reference-type="eqref" reference="det23"} and [\[mon23\]](#mon23){reference-type="eqref" reference="mon23"}, we find

$$\det\big(\widetilde{\mathbf A}\Delta_{\tilde z''}
+\widetilde{\mathbf B}\Delta_{\tilde z}^{-1}\big)\,
\widetilde z^{\tilde f''}\widetilde z''{}^{-\tilde f} = \pm \det \big({\mathbf A}\Delta_{z''}
+{\mathbf B}\Delta_{z}^{-1}\big)z^{f''}z''{}^{-f}\,,$$

so that $\tau_{\mathcal{T}}$ is invariant under the 2--3 move. This completes the proof of Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"}. 0◻

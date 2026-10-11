---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-015-25-the-shape-solutions-to-the-gluing-equations
section_title: "The shape solutions to the gluing equations"
section_number: 2.5
pages: 14-15
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
text_source: latex
latex_prose_ratio: 0.919
latex_coverage_ratio: 0.97
---
[]{#sub.shapesol label="sub.shapesol"}

If we exponentiate the equations [\[tetP\]](#tetP){reference-type="eqref" reference="tetP"}, and set $(z_i,z_i',z_i'')=(e^{Z_i}, e^{Z_i'},e^{Z_i''})$, we obtain that $(z_i,z_i',z_i'')$ satisfy Equation [\[tetexp\]](#tetexp){reference-type="eqref" reference="tetexp"}. If we combine the exponentiated equations [\[NZlin\]](#NZlin){reference-type="eqref" reference="NZlin"} with the nonlinear relation [\[tetLag\]](#tetLag){reference-type="eqref" reference="tetLag"} for each tetrahedron, we obtain

$$z^{\mathbf A}z''^{\mathbf B} = z^{\mathbf A}(1-z^{-1})^{\mathbf B} = (-1)^\nu\,, 
\label{glueeqs}$$

where $z^{\mathbf A} := \prod_j z_j^{\mathbf A_{ij}}$. These $N$ equations in $N$ variables are just the gluing equations of Thurston [@Th] and Neumann and Zagier [@NZ], and fully capture the constraints imposed by the gluing. For hyperbolic $M$, a triangulation $\mathcal{T}$ is regular precisely when one of the solutions to [\[glueeqs\]](#glueeqs){reference-type="eqref" reference="glueeqs"} corresponds to the complete hyperbolic structure.

## Example: $\mathbf{4_1}$ {#sec.41triang}

As an example, we describe the enhanced Neumann-Zagier datum of the figure-eight knot complement $M$. It has a well known regular ideal triangulation $\mathcal{T}$ consisting of $N=2$ tetrahedra, to which we assign logarithmic shape parameters $(Z,Z',Z'')$ and $(W,W',W'')$.

![The boundary of the cusp neighborhood for the figure-eight knot.](cusp41){#fig.41cusp width="4.5in"}

A map of the boundary of the cusp neighborhood is shown in Figure [1](#fig.41cusp){reference-type="ref" reference="fig.41cusp"}. We have chosen one of $3^2$ possible cyclic labelings by $Z$'s and $W$'s (*i.e.* one of $3^2$ possible quad types). Each of the edges intersects the cusp twice, so it is easy to read off from Figure [1](#fig.41cusp){reference-type="ref" reference="fig.41cusp"} that the edge constraints [\[glue\]](#glue){reference-type="eqref" reference="glue"} are

$$\begin{aligned}
 E_1:&\quad 2Z+ Z''+2W+W'' = 2\pi i \\
 E_2:&\quad 2Z'+Z''+2W'+W'' = 2\pi i\,.
\end{aligned}$$

The sum of the left-hand sides is automatically $4\pi i$, so we can choose to ignore the second constraint. If we choose the meridian path $\mu$ as in Figure [1](#fig.41cusp){reference-type="ref" reference="fig.41cusp"}, the meridian constraint [\[merid\]](#merid){reference-type="eqref" reference="merid"} is

$$\mu:\quad -Z'+W = 0 \notag$$

Putting together the first edge constraint and the meridian into matrices, we have

$$\begin{pmatrix} 2 & 2 \\0 & 1 \end{pmatrix}\begin{pmatrix} Z
\\W\end{pmatrix}
 + \begin{pmatrix} 0 & 0 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} Z'
\\W'\end{pmatrix}
 + \begin{pmatrix} 1 & 1 \\0 & 0 \end{pmatrix}\begin{pmatrix} Z''
\\W''\end{pmatrix} = i\pi \begin{pmatrix} 2 \\ 0 \end{pmatrix} \,.
\notag$$

Using $Z+Z'+Z''=W+W'+W''=i\pi$ to eliminate $Z'$ and $W'$, we get

$$\begin{pmatrix} 2 & 2 \\1 & 1 \end{pmatrix}\begin{pmatrix} Z
\\W\end{pmatrix}
 + \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} Z''
\\W''\end{pmatrix} = i\pi \begin{pmatrix} 2 \\ 1 \end{pmatrix}\,.
\notag$$

From this last expression, we can read off

$$\label{NZ41}
\mathbf A = \begin{pmatrix} 2 & 2 \\ 1 &  1 \end{pmatrix}\,,\qquad 
\mathbf B = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}\,,\qquad \nu
= \begin{pmatrix} 2 \\  1 \end{pmatrix}\,.$$

The two gluing equations [\[glueeqs\]](#glueeqs){reference-type="eqref" reference="glueeqs"} are then $$\label{41glue}
z^2w^2z''w''=1\,, \qquad zwz'' =-1 \,,$$ with $z''=1-z^{-1}$ and $w''=1-w^{-1}$. The solution for the complete hyperbolic structure is $z=w=e^{i\pi/3}$.

Finally, a flattening $(f_z,f_z',f_z'';f_w,f_w',f_w'')\in \mathbb{Z}^{6}$, *i.e.* an integer solution to $\mathbf A f+\mathbf B f'' = \nu$ and $f+f'+f''=1$, is given by

$$\label{flat41} (f_z,f_z',f_z'';f_w,f_w',f_w'') = (0,1,0;1,0,0)$$

It is easy to see that every flattening has the form $(a, b, 1-a-b; b, a, 1 - a - b)$ for integers $a, b$.

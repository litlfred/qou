---
doc_id: arxiv-1911.04486v4
doc_title: "Knots and the Maxwell Equations"
section_id: sec-003-22-maxwell-equations-in-covariant-formulation
section_title: "Maxwell equations in covariant formulation"
section_number: 2.2
pages: 7-9
source_pdf: 1911.04486v4.pdf
source_sha256: 53a34938c0e63bad
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.995
doc_brief: "Knots and the Maxwell Equations — In this chapter, we review the Ra˜nada ﬁeld line solutions of Maxwell’s equations in the vacuum, which describe a topologically non-trivial electro- magnetic ﬁeld"
---
The geometric properties of the electromagnetic field are highlighted in the formulation of Maxwell's equations in terms of differential forms on $\mathbb{R}^3$. However, the fundamental symmetry of Maxwell's equations, which is the invariance under the Lorentz transformations, is explicitly displayed only in the Minkowski space-time $\mathbb{R}^{1,3}$. Therefore, it is important to write the Maxwell equations in terms of differential forms on $\mathbb{R}^{1,3}$. To this end, the canonical basis $\{ dx^i \}$ on $\mathbb{R}^3$ must be  extended to the corresponding basis on $\mathbb{R}^{1,3}$, denoted by $\{ d x^{\mu} \} = \{ dx^0 = dt, dx^i \}$, by including the time-like 1-form $dx^0$. Here, we are using the indices $\mu , \nu = 0, 1, 2, 3$ to denote the geometrical objects and their components in the Minkowski space-time. The electromagnetic 2-form field $F$ is defined by the following relation
\begin{equation}
F = B  + E \wedge d x^0 \, .
\label{EM-2-form}
\end{equation}
In this notation, the components of $F$ in the basis $\{ d x^{\mu} \wedge d x^{\nu} \}$ are the same as the components of the electromagnetic rank-2 antisymmetric tensor $F_{\mu \nu}$, namely
\begin{equation}
F = \frac{1}{2} F_{\mu \nu} d x^{\mu} \wedge d x^{\nu} \, .
\label{EM-tensor}
\end{equation}
The source of the electromagnetic field can also be written in terms of differential forms in four dimensions and it is expressed by the 1-form $J= J_{\mu} dx^{\mu}$ whose components are equal to the projections of the four-current $J^{\mu} = (\rho , \mathbf{J} )$ onto the space-time directions. By using these mathematical objects, one can write down the Maxwell equations in their most compact form as follows
\begin{align}
d F & = 0 \, ,
\label{Maxwell-4d-1}
\\
\star \, d \star F & = J \, .
\label{Maxwell-4d-2}
\end{align}
It is easy to show that the homogeneous equation (\refeq{Maxwell-4d-1}) corresponds to the magnetic Gauss law and to the Faraday law combined into one equation, while the inhomogeneous equation (\refeq{Maxwell-4d-2}) is the same as the electric Gauss law and the Maxwell-Amp\'{e}re law packed in to a single mathematical relation. 

The equations (\refeq{Maxwell-4d-1}) and (\refeq{Maxwell-4d-2}) fix to some extent the geometrical properties of the electromagnetic 2-form. Indeed, from the geometrical point of view, the field $F$ is a closed 2-form due to the equation (\refeq{Maxwell-4d-1}). From this property and from the nilpotency of the exterior derivative, i. e. $d^2 = 0$, we can derive the action of the differential form on the electromagnetic field which is given by the following equation
\begin{equation}
d F = d B + d E \wedge d x^0 \, .
\label{Maxwell-4d-1-a}
\end{equation}
Recall that the exterior derivative on $\mathbb{R}^{1,3}$ can be decomposed in to two terms: the exterior derivative $\mathbf{d}$ on the spatial subspace $\mathbb{R}^3 \in \mathbb{R}^{1,3}$ and the 1-form $dx^0$ along the time-like direction $\mathbb{R}$. This decomposition is given by the following equation 
\begin{equation}
d = dx^0 \wedge \partial_0 + \mathbf{d} \, . 
\label{ext-der-decomposed}
\end{equation} 
By plugging the equations (\refeq{ext-der-decomposed}) and (\refeq{Maxwell-4d-1-a}) into the equation (\refeq{Maxwell-4d-1}), one obtains the following set of equations
\begin{align}
\mathbf{d} E + \partial_0 B & = 0 \, ,
\label{Maxwell-4d-1-E}
\\
\mathbf{d} B & = 0 \, .
\label{Maxwell-4d-1-B}
\end{align}
The equations (\refeq{Maxwell-4d-1-E}) and (\refeq{Maxwell-4d-1-B}) are the homogeneous Maxwell equations written in terms of 1-forms on the Euclidean space $\mathbb{R}^3$. 

The three-dimensional inhomogeneous equations can be derived from the four-dimensional system, too. 
The outline of the derivation is the following. Firstly, note that the electromagnetic Hodge dual form $\star F$ can be obtained from $F$ by making the following replacements
\begin{equation}
E_j \to - B_j \, ,
\qquad
B_j \to E_j \, .
\label{F-dual-replacements}
\end{equation}
Secondly, decompose the form $\star F$ as follows
\begin{equation}
\star F = \boldsymbol{\star} E - \boldsymbol{\star} B \wedge d x^0 \, ,
\label{F-dual-decompose}
\end{equation}
where $\boldsymbol{\star}$ denotes the three-dimensional Hodge star operator. Thirdly, calculate the sequence of operations from the equation (\refeq{Maxwell-4d-2}). Then one obtains the following set of inhomogeneous equations
\begin{align}
\boldsymbol{\star} \, \mathbf{d} \boldsymbol{\star} E & = \rho \, ,
\label{Maxwell-4d-2-E}
\\
\boldsymbol{\star} \, \mathbf{d} \boldsymbol{\star} B 
- \partial_0 E 
& = \mathcal{J} \, .
\label{Maxwell-4d-2-B}
\end{align}
This concludes the derivation of the three-dimensional Maxwell equations in terms of differential forms from the four dimensional formulation. 

Let us make some observations about the electromagnetic fields away from their sources. In this case, the fields propagate in the vacuum. Their dynamics is still given by the equations (\refeq{Maxwell-4d-1}) and (\refeq{Maxwell-4d-2}), but with the supplementary condition $J = 0$. Due to this last relation, the symmetries of Maxwell's equations are enhanced to the group $SO(1,3) \times U(1) \times \mathcal{D}$, where $\mathcal{D}$ denotes the electromagnetic duality symmetry defined by the following transformations 
\begin{equation}
F \leftrightarrow \star F \, .
\label{duality-symmetry}
\end{equation}
The relation (\refeq{duality-symmetry}) implies that the 2-form $F$ can be written as a sum between a self-dual form $F_{+}$ and an anti self-dual form $F_{-}$. The corresponding equations are 
\begin{equation}
F = F_{+} + F_{-} \, ,
\qquad
\star F_{\pm} = \pm i F_{\pm} \, .
\label{self-dual-anti-self-dual}
\end{equation}
The last of the two equations from above is the result of the self-duality relation for 
2-forms in the Minkwoski space-time: $\star \star \, \omega = - \omega$. 

We end this section by observing that the formulation of the classical electrodynamics in terms of differential forms is completely equivalent with the formulation in terms of three-dimensional vector fields. However, each framework has its own advantages. The vector approach is useful for the visualization of the spatial distribution of fields and sources. The differential forms are interesting because they provide more economical equations, a deeper view of the symmetries and more information about the geometrical and topological properties of the electromagnetic fields.

---
doc_id: arxiv-1911.04486v4
doc_title: "Knots and the Maxwell Equations"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-7
source_pdf: 1911.04486v4.pdf
source_sha256: 53a34938c0e63bad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.95
---
The discovery of the knot solutions of Maxwell's equations in the vacuum represents one of the most exciting results obtained recently in the modern classical electrodynamics. Since their first appearance in the seminal papers \cite{Trautman:1977im,Ranada:1989wc,Ranada:1990,Ranada:1992hw}, many interesting properties, applications, and generalizations of the knot electromagnetic fields have been discovered. 

The knot solutions of Maxwell's equations can be described in terms of electric and magnetic field lines, and their topology can be given in terms of a pair of complex scalar fields that are interpreted as Hopf maps $S^3 \to S^2$ on the compactified space-like directions of the Minkowski space-time \cite{Ranada:1992hw}-\cite{Ranada:1997}. Among the properties studied up to now, one can cite: the relationship between the linked and the knotted electromagnetic fields discussed in \cite{Irvine:2008,Irvine:2010}, the dynamics of the electric charges in topologically non-trivial electromagnetic backgrounds investigated in \cite{Kleckner:2013}-\cite{Ranada:2017ore}, and the topological quantization presented in \cite{Ranada:1998vp}-\cite{Arrayas:2012eja}. In the last decade, the Ra\~{n}ada solutions were generalized in two ways. The first generalization is from knot fields to torus fields and was given in the works of Arrayas and Hoyos \cite{Arrayas:2011ia}-\cite{Hoyos:2015bxa}. The second generalization is from the electromagnetic fields in vacuum to electromagnetic fields in matter. Several authors have showed that topological fields can be found in various areas of physics such as: fluid physics \cite{Alves:2017ggb,Alves:2017zjt}, atmospheric physics \cite{Ranada:1996}, liquid crystals \cite{Irvine:2014}, plasma physics \cite{Smiet:2015}, optics \cite{Ren:2008zzf,deKlerk:2017qvq}, and superconductivity \cite{Trueba:2008sc}. (For a recent review of the knot solutions and their applications see \cite{Arrayas:2017sfq} and the references therein). More recently, new and important generalizations of the topological electromagnetic fields have been made to the non-linear electrodynamics, the fluid physics \cite{Goulart:2016orx}-\cite{Alves:2017zjt} as well as to the gravitational physics \cite{Kopinski:2017nvp} - \cite{Alves:2018wku}. A new method to obtain the electromagnetic knot solutions in Minkowski space, by completely solving the Maxwell equations first in de Sitter space and then conformally mapping to Minkowski space was presented in \cite{Lechtenfeld:2017tif,Kumar:2020xjr}. 

Due to their wide range of applications in both physics and mathematics, the topological electromagnetic fields represent an important field of science and an active line of research. 

In the present chapter, we are going to revisit the construction of the knot solutions of Maxwell's equations in Ran\~{a}da's approach. Also, we are going to briefly survey the different mathematical formulations of Maxwell's equations and to present the construction of the Hopf maps in electrodynamics. Of utmost importance for the understanding of the knot solutions is the factorization method of the 2-forms introduced by Bateman. We will review the application of Bateman's method to the topological electromagnetic fields. Finally, we are going to present the argument from \cite{Alves:2017ggb,Alves:2017zjt} where it was showed that knot solutions can also be found in the non-linear Born-Infeld electrodynamics and other non-linear generalizations of Maxwell's electrodynamics. We will focus our presentation on the electromagnetic fields in flat space-time. The generalization of the field line solutions to the gravitating electromagnetic fields is discussed in a different chapter of this volume \cite{Vancea:2019yjt}. The results reviewed here can be found in the original papers cited in the text. Other reviews are available too, most notably \cite{Arrayas:2017sfq} to which we refer for an updated list of references. In the Appendix, we collect some basic mathematical properties of the Hopf mapping. We adopt throughout this chapter the natural units in which $c = 1$.



\section{Maxwell's equations}  

In this section, we will briefly review the formulation of Maxwell's electrodynamics in terms of differential forms in the three-dimensions Euclidian space and in the four-dimensional space-time (the covariant formulation). This is a well-known material which can be found in standard textbooks on classical electrodynamics such as \cite{Jackson:1998nia,Frankel:1997ec}. 



\subsection{Maxwell's equations in the three-dimensional formulation}

The two formulations of Maxwell's equations that are our concern in this paper are: the formulation in terms of differential forms and the covariant formulation. Both formulations are  equivalent to the one in terms of three-dimensional vectors that is known from the undergraduate textbooks on electrodynamics, see e. g. \cite{Jackson:1998nia}.

Consider the following standard form of Maxwell's equations in the Heaviside units
\begin{align}
\nabla \cdot \mathbf{D} & = \rho \, ,
\label{Maxwell-Gauss-El-1}
\\
\nabla \cdot \mathbf{B} & = 0 \, ,
\label{Maxwell-Gauss-Mag-2}
\\
\nabla \times \mathbf{E} & = 
- \frac{\partial \mathbf{B}}{\partial t}
 \, ,
\label{Maxwell-Faraday-3}
\\
\nabla \times \mathbf{H} & = 
\mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}
\, .
\label{Maxwell-Ampere}
\end{align}
Here, $\mathbf{E}$ and $\mathbf{H}$ are the electric and magnetic intensities and 
$\mathbf{D}$ and $\mathbf{B}$ are the electric and magnetic flux densities, respectively. The sources of the electric and magnetic fields are the density of charge $\rho$ and the density of vector current $\mathbf{J}$. All vectors are three-dimensional and they are defined on the entire $\mathbb{R}^3$ at each instant of time if no other conditions are imposed on the system.

The set of equations (\refeq{Maxwell-Gauss-El-1}) - (\refeq{Maxwell-Ampere}) can be written in terms of differential forms from either $\Omega^{k}(\mathbb{R}^3 )$ or $\Omega^{k}(\mathbb{R}^{1,3} )$ which denote the differential forms of rank $k$ defined on the corresponding spaces. This abstract mathematical formulation is advantageous for at least two reasons - first, it provides a more economical formulation of the basic relations of the electromagnetism. Second, it provides the mathematical framework that is necessary for the generalization of the classical electromagnetism to curved space-times (see e. g. \cite{Frankel:1997ec}). The differential forms associated with the three-dimensional electromagnetic field are given in the Table
\refeq{tbl:fields}. 

\begin{table}[htbp]
  \begin{center}
   \label{table1}
   \caption{Field content of Maxwell's equations}
   \vspace{0.2cm}    
    \begin{tabular}{l|c|c|r}
      \textbf{Vector } & \textbf{Form} & \textbf{Form} & \textbf{Field}\\ 
      \textbf{notation} & \textbf{notation} & \textbf{rank} & \textbf{}\\ 
      
      \hline
      $\mathbf{E}$ & $\mathcal{E}$ & 1 - form & electric intensity\\ 
      $\mathbf{H}$ & $\mathcal{H}$ & 1 - form & magnetic intensity\\ 
      $\mathbf{D}$ & $\mathcal{D}$ & 2 - form & electric flux density\\ 
      $\mathbf{B}$ & $\mathcal{B}$ & 2 - form & magnetic flux density\\ 
      $\rho      $ & $\mathcal{Q}$ & 3 - form & charge density \\ 
      $\mathbf{J}$ & $\mathcal{J}$ & 2 - form & current density \\ 
    \end{tabular}
    \label{tbl:fields}  
  \end{center}
\end{table}

It is easy to show that the differential forms from the Table \refeq{tbl:fields} can be projected onto the orthonormal Cartesian basis of $\mathbb{R}^3$. The corresponding components are given by the following relations
\begin{align}
\mathcal{E} & = E_x dx + E_y dy + E_z dz \, ,
\nonumber
\\ 
\mathcal{H} & = H_x dx + H_y dy + H_z dz \, ,
\nonumber
\\
\mathcal{D} & = D_x dy \wedge dz + D_y dz \wedge dx + D_z dx \wedge dy \, ,
\nonumber
\\
\mathcal{B} & = B_x dy \wedge dz + B_y dz \wedge dx + B_z dx \wedge dy \, ,
\nonumber
\\
\mathcal{Q} & = \rho \, dx \wedge dy \wedge dz \, ,
\nonumber
\\
\mathcal{J} & = J_x dy \wedge dz + J_y dz \wedge dx + J_z dx \wedge dy \, .
\label{fields-components}
\end{align}
The basis $(dx, dy, dz)$ from the space $\Omega^1 (\mathbb{R}^3)$ of 1-forms is associated by the canonical procedure to the basis  $(x, y, z)$ from $\mathbb{R}^3$.  The second canonical basis  $(dx \wedge dy, dy \wedge dz, dz \wedge dx)$ in the space $\Omega^2 (\mathbb{R}^3)$ of 2-forms is constructed from the 1-forms $(dx, dy, dz)$ by taking their wedge product which is defined as follows
\begin{equation}
\wedge : \Omega^{k} \times \Omega^{s} \to \Omega^{k + s} \, ,
\qquad
(\omega , \sigma ) \to \omega \wedge \sigma \, .
\label{wedge-product}
\end{equation}
In the equation above, we have not specified which is the base space because the wedge product is defined in the same way on either $\mathbb{R}^3$ or $\mathbb{R}^{1,3}$. 

In order to write Maxwell's equations in terms of differential forms, one has to recall that the exterior derivative $d$ is defined as being the $\mathbb{R}$-linear map from $\Omega^k \to \Omega^{k+1}$ with the following properties
\begin{align}
d f & = \partial_{i} f \, d x^i \, ,
\label{exterior-derivative-1}
\\
d^2 \omega & = 0 \, , 
\label{exterior-derivative-2}
\\
d \left( \omega \wedge \sigma \right) & =
d \left( \omega  \right) \wedge \sigma
+ (-)^k \omega \wedge d \left( \sigma \right) \, .
\end{align}
Here, $f$ is an arbitrary smooth function and $\omega$ and $\sigma$ are arbitrary differential forms. Note that the exterior derivative is nilpotent, i. e. $d^2 = 0$.

The Hodge dual operation $\star$ is defined as the map from $\Omega^{n-k} \to \Omega^k $, where $n$ is the dimension of the base manifold, that satisfies the following relation 
\begin{equation}
\omega \wedge \left( \star \sigma \right) = \langle \omega , \sigma \rangle \mathrm{n} 
\, .
\label{Hodge-star}
\end{equation}
Here, $\mathrm{n}$ is an unitary vector and $\langle \cdot , \cdot \rangle$ is the scalar product. In particular, the action of the Hodge star operator on the components of an arbitrary $k$-form is given by the following equations \cite{Frankel:1997ec}
\begin{align}
\omega & = \frac {1}{k!} \omega_{i_{1},\dots ,i_{k}} 
d x^{i_{1}} \wedge \dots \wedge dx^{i_{k}}
= \sum _{i_{1}<\dots <i_{k}}
\omega_{i_{1},\dots ,i_{k}} 
dx^{i_{1}}\wedge \dots \wedge dx^{i_{k}} \, ,
\label{k-form}
\\
(\star \, \omega ) & = \frac {1}{(n-k)!} 
(\star \, \omega)_{i_{k+1},\dots , i_{n}} 
dx^{i_{k+1}} \wedge \dots \wedge dx^{i_{n}} \, .
\label{Hodge-k-form}
\end{align}
The above equations can be easily particularized to the three-dimensional case. For example, the Hodge duals to the elements of the canonical basis in the space of 1-forms are given by the following relations
\begin{equation}
\star d x  = d y \, d z \, ,
\qquad
\star d y  = d z \, d x \, ,
\qquad
\star d z  = d x \, d y \, .
\label{Hodge-3d-1-forms}
\end{equation}
Similarly, the Hodge duals of the elements of the  canonical basis in the space of 1-forms are obtained from the equation (\refeq{Hodge-k-form}) and they are given by the following relations
\begin{equation}
\star \, d y \, d z = d x  \, ,
\qquad
\star \, d z \, d x  = d y  \, ,
\qquad
\star \, d x \, d y = d z   \, .
\label{Hodge-3d-2-forms}
\end{equation}
The equations (\refeq{Hodge-3d-1-forms}) and (\refeq{Hodge-3d-2-forms})
illustrate the more general property of involution $\star \, (\star \, \omega ) = \omega$ in the three-dimensional Euclidean space. By using the equations (\refeq{Hodge-k-form}), (\refeq{Hodge-3d-1-forms}) and (\refeq{Hodge-3d-2-forms}), one can show that the exterior derivative $d$ can be decomposed in the canonical basis as follows
\begin{equation}
d = \left( \partial_x d x +  
\partial_y d y +
\partial_z d z
\right)
\wedge \, .
\label{exterior-derivative-3d}
\end{equation}
By using the exterior derivative from the equation (\refeq{exterior-derivative-3d}), one can write the Maxwell equations in terms of the three-dimensional differential forms. The result is given by the following set of equations 
\begin{align}
d \mathcal{D} & = \mathcal{Q} \, ,
\label{Maxwell-Gauss-el-3d}
\\
d \mathcal{B} & = 0 \, ,
\label{Maxwell-Gauss-mag-3d}
\\
d \mathcal{E} & = - \partial_t \mathcal{B} \, ,
\label{Maxwell-Faraday-3d}
\\
d \mathcal{H} & = \mathcal{J} + \partial_t \mathcal{D} \, .
\label{Maxwell-Ampere-3d}
\end{align}
It is easy to recognize in the equations (\refeq{Maxwell-Gauss-el-3d}) - (\refeq{Maxwell-Ampere-3d}) the familiar laws of the electromagnetism. They allow one to write the electromagnetic field in terms of potentials $\Phi$ and $\mathcal{A}$. That is made possible by the \emph{Poincaré's theorem}, that states that on a contractible manifold all closed forms ($d \omega = 0 $) are exact, i. e. for any exact form $\omega$ there exists a form $\sigma$ such that $\omega = d \sigma$ \cite{Frankel:1997ec}. By applying this mathematical result, one can show that the electric and magnetic 1-forms can be written as follows
\begin{align}
\mathcal{E} & = - d \Phi - \partial_t \mathcal{A} \, ,
\label{potentials-1}
\\
\mathcal{B} & = d \mathcal{A} \, .
\label{potentials-2}
\end{align}
It is an simple exercise to show that the equations (\refeq{Maxwell-Gauss-el-3d}) - (\refeq{Maxwell-Ampere-3d}) are invariant under the following gauge transformations
\begin{align}
\Phi & \rightarrow \Phi' = \Phi - \partial_t \Lambda \, ,
\label{gauge-1}
\\
\mathcal{A} & \rightarrow \mathcal{A}' = \mathcal{A} + d \Lambda \, ,
\label{gauge-2}
\end{align}
where $\Lambda$ is an arbitrary smooth function that plays the role of the gauge parameter.

The equations (\refeq{Maxwell-Gauss-el-3d}) - (\refeq{Maxwell-Ampere-3d}) describe the dynamics of the electromagnetic field alone. Their solutions are given in terms of charge and current densities, respectively, which are non-dynamical objects. As usual, the change of the source state is given by Newton's second law written for the Lorentz force, which has the following form
\begin{equation}
\mathcal{F}_{L} = \rho \mathcal{E} - \iota_{(\star \mathcal{J})} \mathcal{B} \, .
\label{Lorentz-force-3d}
\end{equation}
The interior product $\iota$ is defined as the contraction between a differential form from the space $\Omega^k$ and a vector field $X$. The interior product lowers the form degree by one, and its image belongs to the space $\Omega^{k-1}$. For example, if $\omega \in \Omega^2$ is a 2-form, its interior product with the vector field $X$ is the 1-form $\iota_{X} \omega$ for which the following equality holds 
\begin{equation}
\iota_{X} \omega (Y) = \omega (X, Y) \, ,  
\label{interior-product}
\end{equation}
where $Y$ is an arbitrary smooth vector field. The equation (\refeq{interior-product}) is the last equation needed to represent the dynamics of the electromagnetic field and its sources in terms of differential forms. Since in the rest of this chapter we will investigate the topological solutions of the electromagnetic field in the vacuum, that is away from its sources, we will ignore the Lorentz force as well as the charge and current densities.

---
doc_id: arxiv-1911.04486v4
doc_title: "Knots and the Maxwell Equations"
section_id: sec-008-5-knots-in-nonlinear-electrodynamics
section_title: "Knots in nonlinear electrodynamics"
section_number: 5
pages: 19-26
source_pdf: 1911.04486v4.pdf
source_sha256: 53a34938c0e63bad
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.578
doc_brief: "Knots and the Maxwell Equations — In this chapter, we review the Ra˜nada ﬁeld line solutions of Maxwell’s equations in the vacuum, which describe a topologically non-trivial electro- magnetic ﬁeld"
---
A very important application of Bateman method to non-linear electrodynamical models that generalize Maxwell's electrodynamics in the strong field regime, was given recently in \cite{Alves:2017ggb,Alves:2017zjt}.
In these works, the authors showed that there are knot solutions of the equations of motion in any non-linear extension of Maxwell's electrodynamics that satisfies strong field requirement. 

Let us see how the Bateman method can be applied to the Born-Infeld electrodynamics. The non-linear Born-Infeld action has the following form
\begin{equation}
S_{BI} = - \gamma^2 \int d^4 x \left( \sqrt{1+ F - P^2} - 1 \right) \, ,
\label{NL-Born-Infeld-action}
\end{equation}
where $\gamma$ is a constant of dimension 2 and $L$ and $P$ are the usual Lorentz invariants defined as follows
\begin{align}
L & = \gamma^{-2} \delta_{m n}\left( B^m B^n - E^m E^n \right)
\, ,
\label{lorentz-invariant-L}
\\
P & = \gamma^{-2} \delta_{m n} E^m B^n \, .
\label{Lorentz-invariant-P}
\end{align}
The scalars $L$ and $P$ are zero for all null-fields that satisfy the equations (\refeq{null-field-1}) and (\refeq{null-field-2}). 

In order to prove that the theory described by the action $S_{BI}$ has Hopfion solutions, the following argument has been developed in \cite{Alves:2017ggb,Alves:2017zjt}. Starting from the action (\refeq{NL-Born-Infeld-action}), define new vector fields $\mathbf{H}$ and $\mathbf{D}$ whose components can be written in a notation analogous to Maxwell's electrodynamics
\begin{equation}
H_m = - \frac{\partial \mathcal{L}_{BI}}{\partial B^m} \, ,
\qquad
D_m = \frac{\partial \mathcal{L}_{BI}}{\partial E^m} \, .
\label{NL-BI-fields}
\end{equation}
Here, $\mathcal{L}_{BI}$ is the Lagrangian density from the action (\refeq{NL-Born-Infeld-action}). From it, one obtains the explicit form of $H_m$ and $D_m$ as follows 
\begin{align}
H_m & = - \frac{1}{\sqrt{1+ F - P^2}} 
\left(
B_m - P E_m
\right)
\, ,
\label{NL-BI-H}
\\
D_m & = 
- \frac{1}{\sqrt{1+ F - P^2}} 
\left(
E_m - P B_m
\right)
\, .
\label{NL-BI-D}
\end{align}
By applying the variational principle to the action (\refeq{NL-Born-Infeld-action}), the following equations of motion are obtained  
\begin{align}
\partial_m D_m & = 0 \, ,
\label{NL-PB-Eq1}
\\
\partial_m B_m & = 0 \, ,
\label{NL-PB-Eq2}
\\
\varepsilon_{m n r} \partial_n E_r & = - \partial_0 B_m \, ,
\label{NL-PB-Eq3}
\\
\varepsilon_{m n r} \partial_n H_r & = \partial_0 D_m \, .
\label{NL-PB-Eq4}
\end{align}
The above equations show that the null fields from the relations (\refeq{null-field-1}) and (\refeq{null-field-2}) belong to a theory in which the equations of motion are of Maxwellian type. Therefore, by using the results presented in Section 2, one concludes that there are null field Hopfion solutions in the non-linear Born-Infeld electrodynamics. 

The same argument can be generalized to all non-linear actions that in the weak field limit can be reduced to Maxwell's electrodynamics. Another interesting generalization is based on the observation that the equations of the classicall electrodynamics are similar to the equations of the fluid mechanics. Then by using the same reasoning as before, Hopfion solutions of the fluid flow lines were showed to exist in \cite{Alves:2017ggb,Alves:2017zjt}. 


\section{Appendix - Hopf map}

In this Appendix, we briefly review the definition and some basic properties of the Hopf map that have been used in the text. A classical reference on this topic is the textbook \cite{Milnor:1997} in which Hopf's theory is presented from a geometrical point of view.

Consider a $n$-dimensional unit sphere $S^n$ defined as follows
\begin{equation}
S^n = \{ \, \mathbf{x} \in R^{n+1} : \,
\delta_{ij} x_i x_j = 1, \, i, j = 0, 1, \ldots , n \, \} \, .
\label{Sn-sphere}
\end{equation}
The \emph{Hopf fibration} is the mapping $h: S^3 \to S^2 \simeq \mathbb{CP}^1$ defined by the following \emph{Hopf map}
\begin{equation}
h(x_0, x_1, x_2, x_3 ) = 
\left(
x^{2}_{0} + x^{2}_{1} - x^{2}_{2} - x^{2}_{3} \, ,
2(x_0 x_3 + x_1 x_2) \, ,
2( x_1 x_2 - x_0 x_3 )
\right) \, .
\label{Hopf-map}
\end{equation}
Alternatively, the Hopf map can be written in terms of the following complex coordinates on the spheres $S^2$ and $S^3$
\begin{align}
S^2 & = \{ (x,z) \in \mathbb{R} \times \mathbb{C} \, : \, 
x^2 + |z|^2 = 1
\} \, ,
\label{S2-complex}
\\
S^3 & = \{ (z_1,z_2 ) \in \mathbb{C}^2 \, : \, |z_1|^2 + |z_2|^2 = 1 
\}
\, .
\label{S3-complex}
\end{align}
Then the Hopf map takes the following form 
\begin{equation}
h(z_1 , z_2) = 
\left(
2 z_1 \bar{z}_2
,
|z_1|^2 - |z_2|^2
\right) \, .
\label{Hopf-map-complex}
\end{equation}
Since the projective space is a quotient set $\mathbb{CP}^1 \simeq S^3/U(1)$, the action of $U(1)$ on $S^3$ defines the fibres over $S^3$. These are mapped into the fibres over $S^2$ as follows. Consider the equivalence class of points of $S^3$ defined by the following relation
\begin{equation}
(z'_{1}, z'_{2} ) \sim (z_1, z_2) \, : \, 
\mbox{if} \, \, \exists \, \lambda \in \mathbb{C} 
\, \, \mbox{such that} 
\, \,
(z'_{1}, z'_{2} ) = (\lambda z_1, \lambda z_2) \, .
\label{U(1)-equivalence}
\end{equation}
Then the Hopf map of $(z'_{1}, z'_{2} )$ satisfies the following relation
\begin{equation}
h(z'_{1}, z'_{2} ) = |\lambda|^2 h(z_1 , z_2) \, .
\label{Hopf-U(1)-equivalence}
\end{equation}
The points $(z'_{1}, z'_{2} )$  and $(z_1, z_2)$ of $S^3$ belong to a fibre over $S^2$ if they are mapped onto the same point of $S^2$. This represents a constraint on the parameter $\lambda$ which is satisfied by 
any $\lambda$ of the form $\lambda = \exp (i\vartheta)$, where $\vartheta \in [0, 2 \pi)$. Thus, $\lambda$ necessarily belongs to the defining representation of $U(1)$. 

From the geometrical point of view, the fibre of $S^3$ is the great circle that contains $(z_1, z_2)$. An useful parametrization of fibres is given by the following relations
\begin{equation}
z_1 = \exp \left( i\xi + \frac{\varphi}{2} \right) 
\sin \left( \frac{\vartheta}{2}\right) \, ,
\qquad
z_2 = \exp \left( i\xi - \frac{\varphi}{2} \right) 
\cos \left( \frac{\vartheta}{2}\right) \, .
\end{equation}
It is easy to see that the Hopf map $h$ takes the points from the fibres of $S^3$ to the following points on $S^2 \subset \mathbb{R}^3$
\begin{align}
x_1 & = 2 |z_1 | | z_2 | \cos(\varphi) \, ,
\label{Hopf-1}
\\
x_2 & = 2 |z_1 | | z_2 | \sin(\varphi) \, ,
\label{Hopf-2}
\\
x_3 & = |z_1 |^2 - | z_2 |^2 \, .
\label{Hopf-3}
\end{align} 
The stereographic projections can be easily determined from its definition and we find that there are several parametrizations of these projections. For example:
\begin{align}
\pi_2 (x_1, x_2, x_3 ) & = 
\left(
\frac{x_1}{1 - x_3} \, ,
\frac{x_2}{1 - x_3}
\right)
\, ,
\label{stereo-S2}
\\
\pi_3 (x_0 , x_1, x_2, x_3 ) & = 
\left(
\frac{x_1}{1 - x_0} \, ,
\frac{x_2}{1 - x_0} \, ,
\frac{x_3}{1 - x_0} 
\right) \, .
\label{stereo-S3}
\end{align}
The Hopf map inverse $\gamma = h^{-1}$ takes points $(x,z)$ from $S^2$ into loops on $S^3$. In general, if the points are different $(x,z) \neq (x', z')$, so are the corresponding loops $\gamma \neq \gamma'$. However, there is an object associated to a pair of loops called the \emph{Hopf invariant} of $h$ that is the linking number of the pair of loops, also called the \emph{Hopf index} of $(\gamma, \gamma')$, and which has the following general form
\begin{equation}
H(h) = l(\gamma , \gamma' ) \, .
\label{Hopf-index}
\end{equation}
$H(h)$ is an homotopy invariant that characterizes the Hopf map.
It is useful to write the Hopf invariant in terms of the Chern-Simons integral \cite{Whitehead:1947} of some vector fields. This can be done as follows. Consider an unit vector field $\mathbf{U}(\mathbf{x})$ with the following properties
\begin{equation}
\delta_{ij} U_i(\mathbf{x})  U_j(\mathbf{x})  = 1 \, ,
\qquad |\mathbf{U} (\mathbf{x})| \to \mathbf{u} \, 
\, \mbox{if} \, \, |\mathbf{x}| \to \infty \, ,
\label{unit-vector-field}
\end{equation}
where $\mathbf{u}$ is a constant unit vector. Then define the vector field  $\mathbf{F}(\mathbf{x})$ with the following components
\begin{equation}
F_j (\mathbf{x}) = \varepsilon_{jmn} \varepsilon_{prs}
U_p (\mathbf{x}) \partial_m U_r (\mathbf{x}) 
\partial_n  U_s (\mathbf{x}) \, .
\label{F-field-from-U}
\end{equation}
The field  $\mathbf{F}(\mathbf{x})$ can be written in terms of a potential vector field 
$\mathbf{A}(\mathbf{x})$ as follows
\begin{equation}
F_j (\mathbf{x}) = \varepsilon_{jmn}\partial_m A_n (\mathbf{x}) \, .
\label{F-field-potential}
\end{equation}
Then the Hopf index of the field $\mathbf{U}(\mathbf{x})$ is given by the following equalities
\begin{equation}
H(\mathbf{U}) = \int d^3 x \delta_{ij} F_i (\mathbf{x})  A_j (\mathbf{x}) 
= \int d^3 x  \varepsilon_{jmn} A_j (\mathbf{x}) \partial_m A_n (\mathbf{x}) 
\, .
\label{Hopf-index-integral}
\end{equation}
We recognize in the last equality above the explicit form of the Chern-Simons integral for the potential $\mathbf{A}(\mathbf{x})$.

\newpage

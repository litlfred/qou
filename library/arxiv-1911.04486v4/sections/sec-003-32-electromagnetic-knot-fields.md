---
doc_id: arxiv-1911.04486v4
doc_title: "Knots and the Maxwell Equations"
section_id: sec-003-32-electromagnetic-knot-fields
section_title: "Electromagnetic knot fields"
section_number: 3.2
pages: 12-19
source_pdf: 1911.04486v4.pdf
source_sha256: 53a34938c0e63bad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.943
---
As we have seen above, the electromagnetic field characterized by the equations (\refeq{Ranada-magnetic-solution}) and (\refeq{Ranada-electric-solution}) is parametrized by $g$ and $f$. In particular, by choosing these functions as in the equations (\refeq{Ranada-E}) and (\refeq{Ranada-B}), the field line solutions display non-trivial topological properties. In order to see that, we note that $\phi$ and $\theta$ should be chosen such that the electromagnetic field and the observables constructed from it, e. g. energy, linear momentum, and angular momentum, be finite. Therefore, if the field is defined in the full $\mathbb{R}^3$, the regularity conditions to be imposed on the complex functions are the following 
\begin{equation}
|\phi(x)| \to 0 \, 
\,
\mbox{and}
\, \, 
|\theta(x)| \to 0 \, \,
\mbox{if}
\, \, 
|\mathbf{x}| \to \infty \, .
\label{regularity}
\end{equation}
The boundary conditions (\refeq{regularity}) imply that the defining domain of $\phi$ and $\theta$ is the compactification $\mathbb{R}^3 \cup \{ \infty \} = S^3$ at any given value of $t$. Since $\phi$ and $\theta$ take values in the compactification $\mathbb{C} \cup \{ \infty \} = S^2$, they can be viewed as two families of one-parameter maps $\phi(x) = \{ \phi_t (\mathbf{x}) \}_{t \in \mathbb{R}}$ and $\theta(x) = 
\{ \theta_t (\mathbf{x}) \}_{t \in \mathbb{R}}$ from $S^3$ to $S^2$. Here, it is convenient to use the vector notation to discuss separately the electric and the magnetic field lines, respectively. 

The fields $\mathbf{E}$ and $\mathbf{B}$ can be written in terms of electromagnetic potentials $\mathbf{C}$ and $\mathbf{A}$ in a symmetric way
\begin{equation}
E_j = \varepsilon_{jkl} \partial_k C_l \, ,
\qquad
B_j = \varepsilon_{jkl} \partial_k A_l \, .
\label{C-A-potentials}
\end{equation}
Note that $\mathbf{C}$ is dependent on $\mathbf{A}$, as they are related by the following equation
\begin{equation}
\varepsilon_{jmn} \partial_m C_n = - \partial_0 A_j \, .
\label{C-A-relation}
\end{equation}
However, it is convenient to keep $\mathbf{C}$ explicit, as it makes the electric-magnetic duality more symmetric. The Chern-Simons integrals associated to the electric and magnetic fields and their potentials can be used to define the helicities of the electromagnetic field as follows
\begin{align}
H_{ee} & = \int d^3 x \, \delta_{ij} E_i C_j = 
\int d^3 x \, \varepsilon_{jkl} C_j \partial_k C_l \, , 
\label{helicity-Hee}
\\
H_{mm} & = \int d^3 x \, \delta_{ij} B_i A_j = 
\int d^3 x \, \varepsilon_{jkl} A_j \partial_k A_l \, , 
\label{helicity-Hmm}
\\
H_{em} & = \int d^3 x \, \delta_{ij} B_i C_j = 
\int d^3 x \, \varepsilon_{jkl} C_j \partial_k A_l \, , 
\label{helicity-Hem}
\\
H_{mm} & = \int d^3 x \, \delta_{ij} E_i A_j = 
\int d^3 x \, \varepsilon_{jkl} A_j \partial_k C_l \, . 
\label{helicity-Hme}
\end{align}
The pure electric and magnetic helicites given above are the Hopf indexes of the corresponding electric and magnetic field lines (see the Appendix). If one substitutes the equations (\refeq{C-A-potentials}) into Maxwell's equations (\refeq{Maxwell-Gauss-El-1}) - (\refeq{Maxwell-Ampere}) in the vacuum, one obtains the following set of equations
\begin{align}
\varepsilon_{jmn} \partial_m 
\left( 
\frac{\partial A_{n}}{\partial x^0}
+ \varepsilon_{nrs} \partial_r C_s
 \right) & = 0 \, ,
\label{Maxwel-CA-1}
\\
\varepsilon_{jmn} \partial_m 
\left( 
\frac{\partial C_{n}}{\partial x^0}
- \varepsilon_{nrs} \partial_r A_s
 \right) & = 0 \, .
\label{Maxwel-CA-2}
\end{align}
From the vector calculus, we conclude that there are two scalar functions $\kappa_1$ and $\kappa_2$ such that
\begin{align}
\frac{\partial A_{j}}{\partial x^0}
+ \varepsilon_{jmn} \partial_m C_n
& = \partial_j \kappa_1 \, ,
\label{Maxwel-CA-1-sol}
\\
\frac{\partial C_{j}}{\partial x^0}
- \varepsilon_{jmn} \partial_m A_n
& = \partial_j \kappa_2 \, .
\label{Maxwel-CA-2-sol}
\end{align}
By using the equations (\refeq{Maxwel-CA-1}) - (\refeq{Maxwel-CA-2-sol}), the following equations are obtained
\begin{align}
\delta_{mn} \frac{\partial (A_m B_n)}{\partial x^0} 
+ 2 \delta_{mn} E_m B_n 
- \partial_k \left( \varepsilon_{krs} A_k E_s 
-\kappa_1 B_k
\right) & = 0 \, .
\label{identity-1}
\\
\delta_{mn} \frac{\partial (C_m E_n)}{\partial x^0} 
+ 2 \delta_{mn} E_m B_n 
+\partial_k \left( \varepsilon_{krs} C_k B_s 
+\kappa_2 E_k
\right) & = 0 \, .
\label{identity-2}
\end{align}
From these, it follows that
\begin{align}
\frac{\partial (H_{mm} - H_{ee} )}{\partial x^0} + 4 \int d^3 x
\delta_{mn} E_m B_n & = 0 \, ,
\label{H-conservation-1}
\\
\frac{\partial (H_{mm} + H_{ee} )}{\partial x^0} & = 0 \, .
\label{H-conservation-2}
\end{align}
The equations (\refeq{H-conservation-1}) and (\refeq{H-conservation-2}) show that the pure electric and magnetic helicities are conserved if the fields satisfy the first null field condition (\refeq{null-field-1}).

Let us quote here the explicit Hopfion solution obtained in \cite{Ranada:1997}. The fields $\phi$ and $\theta$ have the following form
\begin{align}
\phi & = \frac{(ax_1 - x_0 x_3) + i(ax_2 + x_0 (a-1)}{(ax_3 + x_0 x_1) + i[a(a-1) - x_0 x_1]}  \, ,
\label{hopfion-1-phi}
\\
\theta & = \frac{[ax_2 + x_0 (a-1)] + i(ax_3 + x_0 x_1)}{(ax_1 - x_0 x_3) + i[a(a-1) - x_0 x_2]}  \, , 
\label{hopfion-1-theta}
\end{align}
where $x_{\mu}$'s are dimensionless coordinates and 
\begin{equation}
a = \frac{r^2-x^{2}_{0} + 1}{2} \, ,
\qquad
r = \sqrt{\delta_{mn} x_{m}^{2} x_{n}^{2} } \, .
\label{hopfion-1-constants}
\end{equation}
The electric and magnetic fields derived from the scalars given by the equations (\refeq{hopfion-1-phi}) and (\refeq{hopfion-1-theta}) have the following form
\begin{align}
\mathbf{E} & = \frac{1}{\pi} \frac{q \mathbf{H}_1 - p \mathbf{H}_2}{(a^2 + x^{2}_{0} )^3} \, ,
\label{Hopfion-1-E}
\\
\mathbf{B} & = \frac{1}{\pi} \frac{q \mathbf{H}_1 + p \mathbf{H}_2}{(a^2 + x^{2}_{0} )^3} \, ,
\label{Hopfion-1-B}
\end{align}
where
\begin{align}
\mathbf{H}_1 & = 
\left( x_2 + x_0 - x_1 x_3 \right)\mathbf{e}_1
-\left[ x_1 + \left( x_2 + x_0 \right) x_3 \right] \mathbf{e}_2
\nonumber
\\
& + \frac{1}{2}
\left[
-1 - x^{2}_{3} + x^{2}_{1} + \left( x_2 + x_0 \right)^2
\right]\mathbf{e}_3
\label{Hopfion-1-H1}
\\
\mathbf{H}_2 & = + \frac{1}{2}
\left[
1 + x^{2}_{1} - x^{2}_{3} - \left( x_2 + x_0 \right)^2
\right]\mathbf{e}_1
+
\left[ - x_3 + \left( x_2 + x_0 \right) x_1 \right] \mathbf{e}_2
\nonumber
\\
& + \left( x_2 + x_0 + x_1 x_3 \right)\mathbf{e}_3 \, ,
\label{Hopfion-1-H2}
\end{align}
and
\begin{equation}
p = x_0 \left( x^{2}_{0} - 3 a^2 \right) \, ,
\qquad
q = a \left( a^2  - 3 x^{2}_{0} \right) \, .
\label{Hopfion-1-constants-1}
\end{equation}
Here, we have denoted by $\{ \mathbf{e}_l \}$ the unit vectors of the Cartesian basis in the spatial directions. The Hopf indices of the above Hopfion solution are
$H(\phi) = H(\theta) = 1$ \cite{Arrayas:2017sfq}. 

Another example of Hopfion is given by the Hopf map defined by the following scalar fields
\begin{align}
\phi & = \frac{2(x_1 + i x_2)}{2x^{2}_{3} + i (\delta_{mn}x^m x^n  - 1 )} \, ,
\label{Ranada-Hopf-1-phi}
\\
\theta & = \bar{\phi} \, .
\label{Ranada-Hopf-1-theta}
\end{align}
The electromagnetic field corresponding to these scalars has the following components
\begin{align}
E_m & = \frac{1}{\sqrt{(2 \pi)^3}} \int d^3 k 
\left[
P_m (k_j) \cos \left( \eta_{\mu \nu} k^{\mu} x^{\nu} \right)
-
Q_m (k_j) \sin \left( \eta_{\mu \nu} k^{\mu} x^{\nu} \right)
\right] \, ,
\label{Ranada-Hopf-1-E}
\\
B_m & = \frac{1}{\sqrt{(2 \pi)^3}} \int d^3 k 
\left[
P_m (k_j) \cos \left( \eta_{\mu \nu} k^{\mu} x^{\nu} \right)
+
Q_m (k_j) \sin \left( \eta_{\mu \nu} k^{\mu} x^{\nu} \right)
\right] \, ,
\label{Ranada-Hopf-1-B}
\end{align}
where
\begin{align}
\mathbf{P} & = 
\frac{e^{-k_0}}{\sqrt{2 \pi}}
\left(
- \frac{k_1 k_3}{k_0}
,
\frac{k_0 k_2 + k^{2}_{2} + k^{2}_{3} }{k_0}
,
- \frac{k_0 k_1 + k_1 k_2 }{k_0}
\right) \, ,
\label{Ranada-Hopf-1-P}
\\
\mathbf{Q} & = 
\frac{e^{-k_0}}{\sqrt{2 \pi}}
\left(
- \frac{k_0 k_2 + k^{2}_{1} + k^{2}_{2} }{k_0}
,
\frac{k_1 k_3}{k_0}
,
\frac{k_0 k_3 + k_2 k_3 }{k_0}
\right) \, .
\label{Ranada-Hopf-1-Q}
\end{align}
The fields given by the equations (\refeq{Ranada-Hopf-1-E}) and (\refeq{Ranada-Hopf-1-B}) describe a particular wave packet that travels along the $x_3$ axis and has the following energy, linear momentum, and angular momentum densities
\begin{equation}
\mathit{E} = 2 \, ,
\qquad \mathbf{p} = \left( 0, 0, 1 \right) \, ,
\qquad \mathbf{L} = \left( 0, 0, 1 \right) \, .
\label{Ranada-Hopf-1-E-p-L}
\end{equation} 
The exact values of $\mathit{E}$, $\mathbf{p}$ and $\mathbf{L}$ are calculated in a dimensionless parametrization of the space-time coordinates. From the equations (\refeq{Ranada-Hopf-1-E-p-L}), it follows that the mass of the wave packet is finite and it has the value $m^2 = 3$.


\section{Electric and magnetic knots in Bateman parametrization}

In the previous section, we have discussed several parametrizations of the field line solutions. In this section, we present the factorized parametrization of the self-dual electromagnetic fields in terms of 1-forms given by Bateman in \cite{Bateman:2016}. This representation is useful for the generalization of the field line solutions to the gravitating electromagnetic fields \cite{Vancea:2017tmx} as well as to the non-linear electromagnetism \cite{Alves:2017ggb,Alves:2017zjt}. For extensive reviews of the properties of the Hopfions in the Bateman representation see  \cite{Hoyos:2015bxa,Arrayas:2017sfq,Thompson:2014owa}.

Let us recall the covariant form of Maxwell's equation in the vacuum given by the equations (\refeq{Maxwell-4d-1}) and (\refeq{Maxwell-4d-2}), namely
\begin{align}
d F & = 0 \, ,
\label{Maxwell-4d-1-vacuum}
\\
d \star F & = 0 \, .
\label{Maxwell-4d-2-vacuum}
\end{align}
The equation (\refeq{Maxwell-4d-1-vacuum}) states that the electromagnetic 2-form field is closed. Then $F$ can be written in terms of two scalar complex functions
\begin{equation}
\alpha : \mathbb{R}^3 \rightarrow \mathbb{C} \, , 
\qquad
\beta : \mathbb{R}^3 \rightarrow \mathbb{C} \, ,
\label{Bateman-complex-fields}
\end{equation}
as follows
\begin{equation}
F = d\alpha \wedge d\beta \, .
\label{F-field-Bateman}
\end{equation}
It is relevant to write the above equation in terms of the electric and magnetic fields. To this end, we use the components of the electromagnetic 2-form $F$ which are the same as the components of the electromagnetic tensor $F_{\mu \nu}$. It follows from the equation (\refeq{F-field-Bateman}) that $F_{\mu \nu}$ satisfies the following relation
\begin{equation}
i \varepsilon^{\mu \nu \rho \sigma} F_{\rho \sigma}
- 2 F^{\mu \nu}  = 2 \varepsilon^{\mu \nu \rho \sigma} 
\partial_{\rho} \alpha \partial_{\sigma} \beta \, .
\label{F-field-covariant}
\end{equation}
By definition, the electric and magnetic fields are given by the following equations
\begin{equation}
- E^{m} = F^{0m} \, ,
\qquad
B^{m} = \frac{1}{2} \varepsilon^{mnp} F_{np} \, .
\label{F-E-B-components}
\end{equation}
Some algebraic manipulations of the equation (\refeq{F-field-covariant}) lead to the following relation between the complex scalars
\begin{equation}
B_m - i E_m 
=
 i 
\left(
\partial_0 \alpha \partial_m \beta 
- \partial_0 \beta \partial_m \alpha
\right) \, .
\label{alpha-beta-constraint-0}
\end{equation}
We know from the equation (\refeq{self-dual-anti-self-dual}) that the electromagnetic field in the vacuum is either self-dual or anti self-dual according to the eigenvalues of the $\star$ operation. That implies that the functions $\alpha$ and $\beta$ must obey the following constraint
\begin{equation}
\nabla \alpha \times \nabla \beta
=
\pm i 
\left(
\partial_0 \alpha \nabla \beta - \partial_0 \beta \nabla \alpha
\right) \, .
\label{alpha-beta-constraint}
\end{equation}
In order to understand the geometry of the electric and magnetic fields on $\mathbf{R}^3$, it is useful to introduce the Riemann-Silberstein vector
\begin{equation}
\mathbf{F} = \mathbf{B} \pm i \mathbf{E} \, , 
\label{F-vector-field-Bateman}
\end{equation}  
where $\mathbf{E}$ and $\mathbf{B}$ can be complex. Also, it is required that $\mathbf{F}$ be a solution of Bateman's equation
\begin{equation}
\delta_{mn} F_m F_n  = 0 \, .
\label{Bateman-equation}
\end{equation}
Note that in general the norm of the field $\mathbf{F}$ is non-zero
\begin{equation}
\delta_{mn} \bar{F}_m F_n  \neq 0 \, ,
\label{Bateman-equation-norm}
\end{equation}
where the bar stands for the complex conjugate. 
One can easily write the equations (\refeq{Bateman-equation}) and (\refeq{Bateman-equation-norm}) on components. The result is the following
\begin{align}
\delta_{mn} \left( B_m B_n -  E_m E_n \right)
\pm 2 i \delta_{mn} E_m B_n & = 0 \, , 
\label{Bateman-equation-1}
\\
\delta_{mn} \left( \bar{B}_m B_n +  \bar{E}_m E_n \right)
& = 0 \, .
\label{Bateman-equation-norm-1}
\end{align}
If the vector fields $\mathbf{E}$ and $\mathbf{B}$ are real, the left-hand side of the equation (\refeq{Bateman-equation-1}) is an invariant of the electromagnetic field and the left-hand side of the equation (\refeq{Bateman-equation-norm-1}) is the energy density of the electromagnetic field. The equations (\refeq{Bateman-equation-1}) and (\refeq{Bateman-equation-norm-1}) define the so called \emph{null fields} \cite{Kedia:2013bw}. 

It is easy to verify that the Bateman solutions conserve the energy, momentum and the angular momentum of the electromagnetic field. These conservation laws follow from the Lorentz symmetry. Also, the $U(1)$ symmetry of Maxwell's equations implies that there is a conserved four-current whose components are given by the following relations
\begin{align}
\rho & = \frac{1}{2} \delta_{mn}
\left(
E_m E_n + B_m B_n
\right) \, ,
\label{Bateman-conserved-rho}
\\
J_k & = \varepsilon_{kmn} E_m B_n \, .
\label{Bateman-conserved-J}
\end{align}
Beside the conserved quantities discussed above, there are new topologically conserved charges, the helicities from the equations (\refeq{helicity-Hee})-(\refeq{helicity-Hmm}).
The Bateman equations admit solution with knot as well as toric topologies. In the Bateman parametrization, different solutions can be related to each other, or derived from each other, due to the following important theorem \cite{deKlerk:2017qvq}:

{\it
Let $\alpha$ and $\beta$ be two smooth complex scalar fields on $M$ that satisfy the Bateman relation (\refeq{alpha-beta-constraint}). Then for any two arbitrary smooth complex functions $f$ and $g$ defined on $\mathbb{C}^2$, the following 2-form exists
\begin{equation}
\mathcal{F} : = d f(\alpha, \beta ) \wedge d g (\alpha , \beta ) \, ,
\label{Bateman-F-general}
\end{equation} 
and $\mathcal{F}$ has the following properties:
\begin{align}
d \mathcal{F} & = 0 \, ,
\label{Bateman-F-general-closed}
\\
\star \mathcal{F} & = \pm i \mathcal{F} \, .
\label{Bateman-F-general-self-dual} 
\end{align}}
There are several known solutions in the literature constructed with the Bateman method. Let us cite here the Hopfion obtained in \cite{Kedia:2013bw} whose complex functions are given by the following relations
\begin{align}
\alpha & = \frac{- x^{2}_{0} + \delta_{mn}x^m x^n - 1 + 2ix_3}{- x^{2}_{0} + \delta_{mn}x^m x^n +1 +2ix_0} \, ,
\label{Bateman-Hopfion-1-alpha}
\\
\beta & = \frac{x_1 - i x_2}{- x^{2}_{0} + \delta_{mn}x^m x^n +1 +2ix_0} \, .
\label{Bateman-Hopfion-1-beta}
\end{align}
The functions $\alpha$ and $\beta$ given above satisfy the following relation
\begin{equation}
|\alpha|^2 + |\beta|^2 = 1 \, .
\label{Bateman-alpha-beta-constraint}
\end{equation}
The electromagnetic vector $\mathbf{F}$ that is obtained from $\alpha$ and $\beta$ 
has the following form
\begin{align}
\mathbf{F} & =\frac{4}{(- x^{2}_{0} + \delta_{mn}x^m x^n + 1 + 2 i x_0)^3}
\nonumber
\\
& \times 
\left[
\begin{array}{c}
\left(x_0 - x_1 - x_3 + i \left(x_2-1 \right) \right) 
\left( x_0 + x_1 - x_3 - i \left( x_2 + 1 \right) \right) \\
-i \left(x_0 - x_2 - x_3 - i \left( x_1 + 1 \right) \right)
\left( x_0 + x_2 - x_3 + i \left( x_1-1 \right) \right) \\
2 \left(x_1 - i x_2 \right) \left( x_0 - x_3 -i \right)  \\
\end{array}
\right] \, ,
\label{Bateman-Hopfion-1-F}
\end{align}
where $\mathbf{F}$ is in a column vector notation. The general properties of the field (\refeq{Bateman-Hopfion-1-F}) are discussed in \cite{Kedia:2013bw,Hoyos:2015bxa}.

New Hopfions can be obtained from a given solution by performing infinitesimal conformal transformations, or a subgroup of them, on the functions $\alpha$ and $\beta$. In order to see that, recall that the scalar functions change under the infinitesimal coordinate trasformations as follows \cite{Hoyos:2015bxa}
\begin{align}
x^{\mu} & \rightarrow x^{'\mu} = x^{\mu} + \xi^{\mu}
\label{Bateman-deformations-coordinates}
\\
\alpha(x) & \rightarrow \alpha'(x') = \alpha (x) + \xi^{\nu} \partial_{\nu} \alpha (x) \, ,
\label{Bateman-deformations-alpha}
\\
\beta(x) & \rightarrow \beta'(x') = \beta (x) + \xi^{\nu} \partial_{\nu} \beta (x) \, ,
\label{Bateman-deformations-beta}
\end{align}
where $\xi = \xi^{\mu} \partial_{\mu}$ is an arbitrary infinitesimal smooth vector field on $\mathbb{R}^{1,3}$. The equation (\refeq{alpha-beta-constraint}) is invariant under the transformations (\refeq{Bateman-deformations-coordinates}) - (\refeq{Bateman-deformations-beta}) if the following condition is satisfied \cite{Hoyos:2015bxa}
\begin{equation}
\epsilon_{rmn}
\left[ 
\delta_{jr}
\left(
\partial_0 \xi_0 - \partial_s \xi_s
\right)
+ i
\epsilon_{jrs}
\left( 
- \partial_0 \xi_s + \partial_s \xi_0
\right)
+
\partial_j \xi_r + 
\partial_r \xi_j
\right]
\, 
\partial_m \alpha \partial_n \beta =
0 \, .
\label{Bateman-transformations-condition}
\end{equation}
The generators of the special conformal transformations are the vector fields 
\begin{equation}
\xi_{\mu} = a_{\mu} \eta_{\mu \nu} x^{\mu \nu} 
- 2 a_{\nu} x^{\nu} x^\mu \, .
\label{Bateman-special-conformal-transformations}
\end{equation}
It is easy to show that any vector field of the form (\refeq{Bateman-special-conformal-transformations}) is a solution of the equation (\refeq{Bateman-transformations-condition}). 
By using this property of the special conformal transformations, the authors of \cite{Hoyos:2015bxa} obtained new Bateman solutions characterized by integer powers $p$ and $q$ of the scalar functions $\alpha$ and $\beta$. The plane wave solution is one example of electromagnetic field from which new solutions can be generated by conformal deformations. The plane waves are characterized by the following scalar functions 
\begin{equation}
\alpha = e^{\imath (x_3-x_0)} \, ,
\qquad 
\beta = x_1 + i x_2 . 
\label{Bateman-Hopfion-plane-wave}
\end{equation}
The new functions that can be obtained from the equation (\refeq{Bateman-Hopfion-plane-wave}) by conformal deformations have the following form
\begin{align}
\alpha' & = \exp
\left[
-1 + 
\frac{i \left( x_0 + x_3 - i \right)}
{ 1 - x^{2}_{0} 
+ \delta_{mn} x^m x^n + 2 i x_0}
\right],
\label{Bateman-Hopfion-plane-wave-conformal-1}
\\
\beta' & = \frac{ x_1 + i x_2}{1 - x^{2}_{0} 
+ \delta_{mn} x^m x^n + 2 i x_0} 
\, .
\label{Bateman-Hopfion-plane-wave-conformal-2}
\end{align}
The electric and magnetic fields built from $\alpha'$ and $\beta'$ have \emph{toric topology}. A generalization of this method to more complex knotted electromagnetic fields was given in \cite{Kedia:2016nwk}. The conformal deformations method was applied to the study of the physical properties of the optical vorticies in \cite{Dennis:2010,deKlerk:2017qvq}.

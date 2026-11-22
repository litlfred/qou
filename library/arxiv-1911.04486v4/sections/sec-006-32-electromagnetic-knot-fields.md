---
doc_id: arxiv-1911.04486v4
doc_title: "Knots and the Maxwell Equations"
section_id: sec-006-32-electromagnetic-knot-fields
section_title: "Electromagnetic knot fields"
section_number: 3.2
pages: 12-16
source_pdf: 1911.04486v4.pdf
source_sha256: 53a34938c0e63bad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.92
doc_brief: "Knots and the Maxwell Equations — In this chapter, we review the Ra˜nada ﬁeld line solutions of Maxwell’s equations in the vacuum, which describe a topologically non-trivial electro- magnetic ﬁeld"
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

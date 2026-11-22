---
doc_id: arxiv-1911.04486v4
doc_title: "Knots and the Maxwell Equations"
section_id: sec-005-31-ranãda-solutions
section_title: "Ranãda solutions"
section_number: 3.1
pages: 10-12
source_pdf: 1911.04486v4.pdf
source_sha256: 53a34938c0e63bad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.964
doc_brief: "Knots and the Maxwell Equations — In this chapter, we review the Ra˜nada ﬁeld line solutions of Maxwell’s equations in the vacuum, which describe a topologically non-trivial electro- magnetic ﬁeld"
---
The Ran\~{a}da solutions form a particular class of \emph{field line solutions} whose main feature is that the field lines completly characterize the electromagnetic field. In general, one can associate a field line to any smooth vector field through its integral flow. The path formed by the field line is tangent in each of its points to the vector obtained by taking the value of the vector field at that point. The picture of all field lines at a given instant of time can be used to visualize the state of the vector field at that instant.

As we can see from the equations (\refeq{Maxwell-4d-1}) and (\refeq{Maxwell-4d-2}), the properties of the sources determine the physical and geometrical properties of the electromagnetic field. In particular, the field lines of the electromagnetic field can have a very complex structure for non-trivial sources and can take a simple form in the vacuum.

In order to construct an electromagnetic field in terms of its field lines, we need a formal description of the latter. That can be given in terms of two smooth scalar complex fields on $\mathbb{R}^3$, namely
\begin{equation}
\phi : \mathbb{R}^3 \rightarrow \mathbb{C} \, , 
\qquad
\theta : \mathbb{R}^3 \rightarrow \mathbb{C} \, . 
\label{Ranada-complex-fields}
\end{equation}
By introducing the above functions, one can interpret the electric and the magnetic field lines as level lines of $\theta$ and $\phi$. In the covariant formulation, the corresponding electromagnetic fields take the following form \cite{Arrayas:2017sfq}
\begin{align}
F_{\mu \nu} & = g(\bar{\phi} , \phi ) 
\left( 
\partial_{\mu} \bar{\phi} \, \partial_{\nu} \phi
-
\partial_{\nu} \bar{\phi} \, \partial_{\mu} \phi
\right) \, ,
\label{Ranada-magnetic-solution}
\\
\star F_{\mu \nu} & = f(\bar{\theta} , \theta ) 
\left( 
\partial_{\mu} \bar{\theta} \, \partial_{\nu} \theta
-
\partial_{\nu} \bar{\theta} \, \partial_{\mu} \theta
\right) \, ,
\label{Ranada-electric-solution}
\end{align}
where $g$ and $f$ are smooth functions on $\theta$ and $\phi$, and the dual electromagnetic field has the following form
\begin{equation}
\star F_{\mu \nu} = \frac{1}{2} \epsilon_{\mu \nu \rho \sigma} F^{\rho \sigma} \, .
\label{dual-em}
\end{equation}
The components of the electromagnetic tensor $F_{\mu \nu}$ contain the electric and magnetic vector fields $\mathbf{E}$ and $\mathbf{B}$. These can be obtained from the following relations
\begin{align}
F & = \frac{1}{2} F_{ \mu \nu} dx^{\mu} \wedge dx^{\nu} = 
-\varepsilon_{j k l} B_{j} dx^{k} \wedge dx^{l} 
+ E_{j} dx^{j} \wedge d x^{0} \, , 
\label{F-field-components}
\\
\star F & = \frac{1}{2} \star F_{ \mu \nu} dx^{\mu} \wedge dx^{\nu} =
\varepsilon_{j k l} E_{j} dx^{k} \wedge dx^{l} 
+ B_{j} dx^{j} \wedge d x^{0} \, . 
\label{star-F-field-components}
\end{align} 
Note that the field line solutions (\refeq{Ranada-magnetic-solution}) and (\refeq{Ranada-electric-solution}) are given in the covariant formulation. Although they are explicitly Lorentz covariant and electromagnetically dual to each other, it is almost impossible to visualize the geometry of the electromagnetic field from the equations (\refeq{Ranada-magnetic-solution}) and (\refeq{Ranada-electric-solution}). This problem can be solved by invoking the equations (\refeq{F-field-components}) and (\refeq{star-F-field-components}) 
and by giving concrete values to the arbitrary functions $g$ and $f$. The first solution with the knot topology obtained in this way is the Ran\~{a}da solution
from \cite{Ranada:1989wc,Ranada:1990}. It has the following electric and magnetic decomposition
\begin{align}
E_{j} & = 
\frac{\sqrt{a} }{2 \pi i} \left( 1 + |\theta|^2 \right)^{-2} 
\varepsilon_{jkl} \, \partial_{k} \bar{\theta} \, \partial_{l} \theta \, ,
\label{Ranada-E}
\\
B_{j} & = 
\frac{\sqrt{a}}{2 \pi i} \left( 1 + |\phi|^2 \right)^{-2} 
\varepsilon_{jkl} \, \partial_{k} \bar{\phi} \, \partial_{l} \phi \, .
\label{Ranada-B}
\end{align}
The electromagnetic duality imposes some constraints on the fields $\theta$ and $\phi$. These constraints can be easily found by substituting the functions $g(\bar{\phi},\phi )$ and $f(\bar{\theta}, \theta)$ from the equations (\refeq{Ranada-E}) and (\refeq{Ranada-B}) into the equation (\refeq{duality-symmetry}), which leads to the following equations
\cite{Arrayas:2017sfq}
\begin{align}
\left( 1 + |\phi|^2 \right)^{-2} \varepsilon_{jmn} 
\partial_m \phi \partial_n \bar{\phi}
& = \left( 1 + |\theta|^2 \right)^{-2} 
\left(
\partial_0 \bar{\theta} \partial_j \theta
-
\partial_0 \theta \partial_j \bar{\theta}
\right)
\, ,
\label{fi-teta-1}
\\
\left( 1 + |\theta|^2 \right)^{-2} \varepsilon_{jmn} 
\partial_m \bar{\theta} \partial_n \theta
& = \left( 1 + |\phi|^2 \right)^{-2}
\left(
\partial_0 \bar{\phi} \partial_j \phi
-
\partial_0 \phi \partial_j \bar{\phi}
\right)
\, .
\label{fi-teta-2}
\end{align}
The equations (\refeq{fi-teta-1}) and (\refeq{fi-teta-2}) form a set of independent non-linear partial differential equations. The electric and magnetic field lines are the level curves of the solutions of the equations (\refeq{fi-teta-1}) and (\refeq{fi-teta-2}).

As one can see from the equations (\refeq{Ranada-E}) and (\refeq{Ranada-B}), the Ran\~{a}da fields correspond to particular functions $g$ and $f$. Recall that the \emph{null field} solutions of Maxwell's equations in vacuum are defined by the following equations
\begin{align}
E_j B_k \delta_{j k} = 0 \, ,
\label{null-field-1}
\\
\delta_{j k} \left( E^j E^k - B^j B^k \right) = 0 \, .
\label{null-field-2}
\end{align}
Then it is easy to verify that Ran\~{a}da fields $\mathbf{E}$ and $\mathbf{B}$ satisfy the first null field equation (\refeq{null-field-1}), but do not satisfy the second one. From that, we can conclude that the electric and magnetic fields are orthogonal to each other and so are their field lines. 

The parametrization of the electromagnetic 2-forms $F$ and $\star F$ in terms of $\phi$ and $\theta$ is not unique according to the equations (\refeq{Ranada-E}) and (\refeq{Ranada-B}). Other possibility is to use the so called \emph{Clebsch parametrization}. The main mathematical tool to construct it is the Darboux theorem \cite{Frankel:1997ec} that is satisfied by both $F$ and $\star F$. By using the Darboux theorem, we can write $F$ and $\star F$ in terms of four canonical 1-forms $d \sigma^a$, $ d \xi^a $, $d \rho^a$ and $d \zeta^a$
\cite{Arrayas:2017sfq} as follows
\begin{align}
F & = \delta_{ab} \, d \sigma^a \wedge d \xi^b \, ,
\, \, 
\label{Clebsch-F}
\\
\star F & = \delta_{ab} \, d \rho^a \wedge d \zeta^b \, ,
\, \, 
\label{Clebsch-star-F}
\\
d \sigma^a \wedge d \xi^a & = d \rho^a \wedge d \zeta^a = - i \tau_2 \, ,
\label{symplectic-form}
\end{align}
where the indices $a, b = 1, 2$ enumerate the 1-forms and $\tau_2$ is the Pauli matrix. The Clebsch representation of the electromagnetic field takes a simpler form for fields that satisfy the equation (\refeq{null-field-1}), namely
\begin{align}
F & = d \sigma \wedge d \xi\, ,
\, \, 
\label{Clebsch-F-1}
\\
\star F & = d \rho \wedge d \zeta \, .
\, \, 
\label{Clebsch-star-F-1}
\end{align}
Another important parametrization of the electromagnetic field is given in terms of 
\emph{Euler potentials} which are smooth scalar real fields on the Minkowski space-time \cite{Arrayas:2017sfq}

\begin{equation}
\alpha_a : \mathbb{R}^3 \rightarrow \mathbb{C} \, , 
\qquad
\beta_a : \mathbb{R}^3 \rightarrow \mathbb{C} \, , 
\label{Ranada-complex-fields-1}
\end{equation}
where $a = 1, 2$. The electric and magnetic fields have the following form
\begin{align}
E_{j} & = 
\varepsilon_{jkl} \, \partial_{k} \beta_2 \, \partial_{l} \beta_1 \, ,
\label{Euler-E}
\\
B_{j} & = 
\varepsilon_{jkl} \, \partial_{k} \alpha_2 \, \partial_{l} \alpha_1 \, .
\label{Euler-B}
\end{align}
By comparying the two sets of equations (\refeq{Ranada-E})-(\refeq{Ranada-B}) and (\refeq{Euler-E})-(\refeq{Euler-B}) with each other, one can easily find the following relation among the parameters of the Ran\~{a}da and Euler parametrizations, respectively,
\begin{align}
\beta_1 & = \left( 1+ |\theta|^2 \right)^{-1} \, ,
\qquad
\beta_2  = \frac{1}{2 \pi} \arg (\theta) \, ,
\label{beta-theta}
\\
\alpha_1 & = \left( 1+ |\phi|^2 \right)^{-1} \, ,
\qquad
\alpha_2  = \frac{1}{2 \pi} \arg (\phi) \, .
\label{alpha-beta}
\end{align} 
These representations are useful to express different properties of the field line solutions. Other representations can be found for more general topological electromagnetic fields. But before discussing this case, let us take a closer look at the Ran\~{a}da fields.

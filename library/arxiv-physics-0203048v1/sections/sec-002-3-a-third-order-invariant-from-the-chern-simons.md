---
doc_id: arxiv-physics-0203048v1
doc_title: "Towards a third-order topological invariant for magnetic fields"
section_id: sec-002-3-a-third-order-invariant-from-the-chern-simons
section_title: "A third-order invariant from the Chern-Simons three-form"
section_number: 3
pages: 4-6
source_pdf: 0203048v1.pdf
source_sha256: 47204f32280e91a3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.991
doc_brief: "Towards a third-order topological invariant for magnetic fields — An expression for a third-order link integral of three magnetic ﬁelds is presented."
---
[]{#section-third-order-invariant label="section-third-order-invariant"} In this section we construct a third-order invariant which, under conditions specified below, yields an invariant for three magnetic fields. The derivation is based on some basic knowledge in differential geometry found e.g. in Frankel (1997).

We have noted before that ([\[helicity-density\]](#helicity-density){reference-type="ref" reference="helicity-density"}) can be derived purely from the homogeneous Maxwell equations. Written in differential forms it reads $$\d(A \wedge \d A)=  F\wedge F  \label{FwedgeF},$$ where $A$ is the one-form potential of the field $F$. The right-hand side of this equation is one of two (pseudo-) scalar Lorentz invariants that can be constructed from the field tensor. We can interpret this equation as a special case of a general result in the theory of Chern forms, namely the exactness of the second Chern form $$\d\,tr(A\wedge \d A - i q \frac{2}{3}A \wedge A \wedge A) = tr(F\wedge F).
\label{Chern-Simons}$$ In this equation $A$ and $F$ are a matrix valued one- and two-form. To be more precise they take their values in the Lie-Algebra ${\frak g}$ of the structure group. In Yang-Mills theory this is the symmetry group of the interaction under consideration, with coupling constant $q$. On the vector space ${\frak g}$ the trace defines a natural scalar product. For $\omega$, $\theta \in {\frak g}$, $\tr(\omega\wedge\theta)= \omega_{ij}\wedge \theta_{ji}$, where the indices denote matrix components.

Equation ([\[Chern-Simons\]](#Chern-Simons){reference-type="ref" reference="Chern-Simons"}) holds for an arbitrary, not necessarily Abelian, field strength $F = \d A - i q A \wedge A$. The three-form on the left-hand side is known as the Chern-Simons three-form. For the case of electrodynamics, i.e. for the Abelian structure group $U(1)$, $F$ is given by $F=\d\, A$, since $A \wedge A$ vanishes and ([\[Chern-Simons\]](#Chern-Simons){reference-type="ref" reference="Chern-Simons"}) reduces to ([\[FwedgeF\]](#FwedgeF){reference-type="ref" reference="FwedgeF"}). In the non-Abelian case ([\[Chern-Simons\]](#Chern-Simons){reference-type="ref" reference="Chern-Simons"}) splits into a real and imaginary part $$\begin{aligned}
   \tr(\d A \wedge \d A) = \d\tr(A\wedge \d A), \label{identity-cs-real}\\
   2\tr(A \wedge A \wedge \d A ) 
   = \d\tr(\frac{2}{3}A \wedge A \wedge A) .\label{identity-cs-imaginary}
\end{aligned}$$ As we will see in the following a third-order invariant can be derived from identity ([\[identity-cs-imaginary\]](#identity-cs-imaginary){reference-type="ref" reference="identity-cs-imaginary"}) for the special case of the structure group $SU(2)$.

Working with an $SU(2)$ structure group it is appropriate to choose the Pauli matrices $\sigma_i$, $i$=$1,2,3$, as a basis for the Lie Algebra $su(2)$. All results, however, are independent of this choice. The gauge potential $A$ and field strength $F$ now have three components $$\begin{aligned}
   A = \sigma_\indi A^\indi, \qquad\qquad   F = \sigma_\indi F^\indi, 
                             \label{SU-two-AandF} 
\end{aligned}$$ where the summation convention over repeated indices is assumed. Let us note that in the following we will refer to these fields as Yang-Mills fields, although they do not necessarily satisfy the Yang-Mills equation. Using the identities for Pauli matrices $$\begin{aligned}
    \sigma_j\sigma_k = i\;\epsilon_{jkl}\;\sigma_l + \delta_{jk}
    \mathbf{1}
    \qquad \text{and} \qquad
    \sigma_j\,\sigma_k\,\sigma_l = i\,\epsilon_{jkl} \mathbf{1},  
  \label{Pauli-matrices-identities}
\end{aligned}$$ equations ([\[identity-cs-real\]](#identity-cs-real){reference-type="ref" reference="identity-cs-real"}) and ([\[identity-cs-imaginary\]](#identity-cs-imaginary){reference-type="ref" reference="identity-cs-imaginary"}) read $$\begin{aligned}
  \d A^\indi \wedge \d A^\indi
               = \d (A^\indi \wedge \d A^\indi),\\ 
 \epsilon_{\indi \indj\indk }\, \d A^\indi \wedge A^\indj \wedge A^\indk = 
 \frac{1}{3}\, \d (\epsilon_{\indi \indj\indk }
                      A^\indi \wedge A^\indj \wedge A^\indk ).
\end{aligned}$$ If we now interpret the three components of the Yang-Mills potential $A$ as three independent potentials of three electromagnetic fields $F_{EM}^\indi = \d A^\indi$, the first identity states the helicity conservation (in IMHD) for the sum of the self-helicities of the three individual fields $F_{EM}^\indi$, similar to the electrodynamic case. The second identity is new. For convenience we introduce the two-form $G^1 = A^2 \wedge A^3$, here on $\Minkowski^4$, and cyclic permutations of it. Then we can write the second identity as $$\frac{1}{3}\d(A^i\wedge G^i) = F_{EM}^i \wedge G^i.\label{Second-identity}$$ To complete the analogy of this equation with ([\[helicity-density\]](#helicity-density){reference-type="ref" reference="helicity-density"}) we have to rewrite it in the language of three-vectors. Therefore we represent the one-form $A^i$ by the time component $A_0^i$ and the three-vector $\bA^i$ of the corresponding four-vector. The two-form $G^1$ is identified with the vector pair $(\bG_E^1,\bG_B^1) = (A_0^3\bA^2-A_0^2\bA^3, \bA^2\times\bA^3)$, equivalent to the identification of $F_{EM}$ with the three-vector pair ($\bE$,-$\bB$). Cyclic permutations immediately lead to corresponding pairs for $G^2$ and $G^3$. Using these conventions, the left- and right-hand side of ([\[Second-identity\]](#Second-identity){reference-type="ref" reference="Second-identity"}) read respectively $$\begin{aligned}
   \frac{1}{3}\d(A^i\wedge G^i)
         &= -\frac{1}{3}\left(\p_t(\bA^i\cdot\bG_B^i)
                     +\nabla\cdot(A_0^i\bG_B^i+\bA^i\times\bG_E^i)\right)
                                        {\text{vol}^{4}}\nonumber\\
      &= -\left(\p_t(\bA^1\cdot\bG_B^1)
                      +  \nabla\cdot(A_0^i\bG_B^i)\right){\text{vol}^{4}}
                    \nonumber
\end{aligned}$$ and $$F_{EM}^i \wedge G^i = (\bE^i\cdot \bG_B^i-\bB^i\cdot\bG_E^i) {\text{vol}^{4}}    
               = (\bE^i\cdot \bG_B^i-A_0^i\nabla\cdot\bG_B^i){\text{vol}^{4}}.$$ Thus, identity ([\[Second-identity\]](#Second-identity){reference-type="ref" reference="Second-identity"}) is equivalent to $$\p_t(\bA^1\cdot\bG_B^1)+\nabla\cdot(A_0^i\bG_B^i)
    = -\bE^i\cdot \bG_B^i+A_0^i\nabla\cdot\bG_B^i,
    \label{third-order-density-evolution}$$ which shows a similar structure as ([\[helicity-density\]](#helicity-density){reference-type="ref" reference="helicity-density"}) in the case of helicity. It describes the time evolution of the density $\bA^1\cdot\bA^2\times\bA^3$ with its current $A_0^i\bG_B^i$ and source term $-\bE^i\cdot \bG_B^i+A_0^i\nabla\cdot\bG_B^i$. This is the basis for the following theorem.\
**Theorem:** *Let $\bB^1$, $\bB^2$ and $\bB^3$ be three magnetic fields with potentials $\bA^i$ satisfying $\bE^i+\bv \times\bB^i=0$. The integral over a volume $V\subset\reals^3$* $$H^{(3)}(\bB^1,\bB^2,\bB^3) := \int_{V} \bA^1\cdot\bA^2\times\bA^3\dxxx
   \label{H-3-continuous-integral}$$

*is a gauge invariant, conserved quantity, if*

1.  the potentials obey $\nabla\cdot(\bA^i\times\bA^j)=0$ for all $i,j=1,2,3$, []{#H-3-condition-1 label="H-3-condition-1"}

2.  the potentials obey the boundary condition $\bA^i\times\bn|_{\p V}=0$ for $\bn$ being the normal vector to the boundary of the integration volume $V$. []{#H-3-condition-2 label="H-3-condition-2"}

*Proof*: Let us first remark that condition ([\[H-3-condition-2\]](#H-3-condition-2){reference-type="ref" reference="H-3-condition-2"}) of the theorem implies $\bB^i\cdot\bn|_{\p V}=0$ as shown in [\[Equivboundaryconditions\]](#Equivboundaryconditions){reference-type="ref" reference="Equivboundaryconditions"}. It is therefore consistent with condition ([\[H-3-condition-1\]](#H-3-condition-1){reference-type="ref" reference="H-3-condition-1"}) since $0 = (\bB^i\cdot\bA^j-\bA^i\cdot\bB^j)|_{\p V} 
   = \nabla\cdot(\bA^i\times\bA^j)|_{\p V}$. Moreover, we show in [\[Equivboundaryconditions\]](#Equivboundaryconditions){reference-type="ref" reference="Equivboundaryconditions"} that for a simply connected volume with $\bB^i\cdot\bn|_{\p V}=0$ condition ([\[H-3-condition-2\]](#H-3-condition-2){reference-type="ref" reference="H-3-condition-2"}) can always be satisfied. In order to prove the invariance of $H^{(3)}$ we observe that in an ideal dynamics ([\[third-order-density-evolution\]](#third-order-density-evolution){reference-type="ref" reference="third-order-density-evolution"}) can be written as $$\begin{aligned}
  \fl\nonumber
   \p_t(\bA^1\cdot\bA^2\times\bA^3)
     \,+\, &\nabla\cdot\left( \bv(\bA^1\cdot\bA^2\times\bA^3) \right) =\\ 
       &\nabla\cdot\left( \frac{1}{3}\bv(\bA^i\cdot\bG_B^i)-A_0^i\bG_B^i\right)
       + (A_0^i-\bA^i\cdot\bv)\nabla\cdot\bG_B^i ,\nonumber
\end{aligned}$$ where the last term vanishes due to condition ([\[H-3-condition-1\]](#H-3-condition-1){reference-type="ref" reference="H-3-condition-1"}).

Integrating over the volume $V$ yields the total time derivative of $H^{(3)}$ on the left-hand side, while the right-hand side can be converted into a surface integral, analogous to ([\[helicity-conservation-proof\]](#helicity-conservation-proof){reference-type="ref" reference="helicity-conservation-proof"}) in the case of helicity. The surface integral vanishes since condition ([\[H-3-condition-2\]](#H-3-condition-2){reference-type="ref" reference="H-3-condition-2"}) of the theorem implies $\bG_B^i=0$ on the boundary of the volume $V$. This, together with the gauge invariance of $H^{(3)}$ shown in [\[appendix-H-3-gauge-invariance\]](#appendix-H-3-gauge-invariance){reference-type="ref" reference="appendix-H-3-gauge-invariance"}, completes the proof.

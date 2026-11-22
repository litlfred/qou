---
doc_id: arxiv-physics-0203048v1
doc_title: "Towards a third-order topological invariant for magnetic fields"
section_id: sec-001-2-magnetic-helicity
section_title: "Magnetic helicity"
section_number: 2
pages: 3-4
source_pdf: 0203048v1.pdf
source_sha256: 47204f32280e91a3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.987
doc_brief: "Towards a third-order topological invariant for magnetic fields — An expression for a third-order link integral of three magnetic ﬁelds is presented."
---
Magnetic helicity of a field $\bB$ with arbitrary vector potential $\bA$ is defined as $$H(\bB) = \int_V \bA \cdot \bB \dxxx\,,  \quad\quad\quad 
  \bB \cdot \bn|_{\partial V} =0,                  \label{heldef}$$ which can readily be shown to be gauge invariant if no magnetic flux crosses the boundary of the volume. Since it is quadratic in magnetic flux it is often referred to as a second-order topological invariant. Magnetic helicity measures the total mutual linkage of magnetic flux. This interpretation can be motivated if we envisage a simple system of two isolated and closed flux tubes $U_1$ and $U_2$ with vanishingly small cross-section. The latter condition ensures that the (self-)helicities of the flux tubes vanish. Moffatt (1969) has shown that for this configuration the helicity integral yields $H(\bB) = 2\,\phi_1\phi_2\,\text{lk}(U_1,U_2)$, where $\text{lk}(U_1,U_2)$ is the Gauß  linking number (Gauß 1867) of the two tubes and where $\phi_i$ is the magnetic flux in the tube $U_i$. Introducing an asymptotic linking number, Arnol'd (1974) was able to extend this interpretation to the generic case where field lines are not necessarily closed (see also Arnol'd & Khesin 1998, Part III, §4).

Similar to *helicity* we can introduce the more general *cross-helicity* of two magnetic fields $\bB_1$ and $\bB_2$. For a simply connected volume $V$ and provided that $\bB_1 \cdot \bn|_{\partial V} =\bB_2 \cdot \bn|_{\partial V} = 0$ we define $$H(\bB_1,\bB_2) := \int_V \bA_1\cdot\bB_2 \dxxx
                  = \int_V \bB_1\cdot\bA_2 \dxxx . \label{crosshelicity}$$ The boundary conditions ensure that this is again a gauge invariant quantity. To see that the two integrals on the right-hand side are equivalent, note that they differ only by a surface integral $\int
(\bA_1 \times \bA_2)\cdot {\bf n}  \dxx$. This can be shown to vanish using the equivalence of $\bB_i \cdot \bn|_{\partial V}=0$ with $\bA_i \times \bn|_{\partial V}=0$ in a certain gauge and for a simply connected volume $V$, as proved in [\[Equivboundaryconditions\]](#Equivboundaryconditions){reference-type="ref" reference="Equivboundaryconditions"}. Since both integrals are gauge invariant this proves the equality for any gauge.

$H(\bB_1,\bB_2)$ measures purely the cross linkage of flux among the two fields. Applied to our system of two isolated closed flux tubes with fields $\bB_1 + \bB_2 = \bB$ in the corresponding tubes this invariant yields $$H(\bB_1,\bB_2) = 2\,\phi_1\phi_2\,\text{lk}(U_1,U_2),$$ which is now valid without the assumption of vanishingly small tube cross-sections.

The significance of magnetic helicity arises from the fact that it is invariant in IMHD. Using merely the homogeneous Maxwell equations we obtain $$\p_t(\bA\cdot\bB)+\nabla\cdot\left(A_0\bB+\bE\times\bA\right) 
       \,=\, -2 \bE\cdot\bB,
\label{helicity-density}$$ which describes the time evolution of helicity density $\bA\cdot\bB$. Here $A_0$ is the electric potential and $\bE$ the electric field. The term $A_0\bB+\bE\times\bA$ is to be interpreted as a *helicity current*, and $-2\bE\cdot\bB$ as a *source term*. In an ideal plasma, i.e. with $\bE + \bv\times\bB=0$, the source term vanishes and the helicity current can be written as $$A_0\bB+\bE\times\bA = 
           A_0\bB+\bv\left(\bA\cdot\bB\right)-\bB\left(\bA\cdot\bv\right).$$ Therefore ([\[helicity-density\]](#helicity-density){reference-type="ref" reference="helicity-density"}) takes the form: $$\p_t \left(\bA\cdot\bB\right)
       +\nabla\cdot\left(\bv\left(\bA\cdot\bB\right)\right) 
                        = \nabla\cdot\left(\chi\bB\right),
                        \label{helicity-conservation-equation}$$ with $\chi=-A_0+\bA\cdot\bv$. Elsasser (1956) already noticed that a particular gauge can be found such that $\chi=0$. Using either this gauge or an arbitrary gauge together with the boundary condition $\bB\cdot\bn\big|_{\p V} = 0$ this last equation implies the conservation of helicity in a comoving volume for an ideal plasma, since $$\fl
   \frac{\d}{\d t}\int\limits_V \bA\cdot\bB \dxxx = 
   \int\limits_V \p_t \left(\bA\cdot\bB\right)
       +\nabla\cdot\left(\bv\left(\bA\cdot\bB\right)\right) \dxxx =
    \int\limits_{\p V} \chi\bB\cdot\bn \dxx \,= \,0.
    \label{helicity-conservation-proof}$$ The invariance of integral ([\[heldef\]](#heldef){reference-type="ref" reference="heldef"}) was first stated by Woltjer (1958).

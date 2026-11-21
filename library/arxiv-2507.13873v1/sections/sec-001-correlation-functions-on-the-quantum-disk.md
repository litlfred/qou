---
doc_id: arxiv-2507.13873v1
doc_title: "Probing the singularity at the holographic screen via q-holography"
section_id: sec-001-correlation-functions-on-the-quantum-disk
section_title: "Correlation functions on the quantum disk"
section_number: null
pages: 4-5
source_pdf: 2507.13873v1.pdf
source_sha256: fa1d38d08dc4976a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.971
doc_brief: "Probing the singularity at the holographic screen via q-holography — We study the emergence of q-deformed spacetime in a lower-dimensional gravitational system whose asymptotic region geometrizes the"
---
[]{#s:qward label="s:qward"} We first remind the reader of the conventional CFT story. Correlation functions of primary operators in a conformal field theory are strongly constrained by the Ward identities of the corresponding global conformal subgroup. For a 2d CFT, holomorphic (quasi)primary operators with weight $\Delta$ transform under a global conformal PSL$(2)$ Möbius transformation $$z\rightarrow \frac{az+c}{bz+d},$$ as $$\begin{aligned}
\label{eq:quasiprimarytransf}
    \mathcal{O}(z)\rightarrow \left(bz+d\right)^{-2\Delta} \;\mathcal{O}\left(\frac{az+c}{bz+d}\right),
\end{aligned}$$ where $\Delta$ is the conformal scaling dimension of the quasi-primary operator. The corresponding infinitesimal transformations generate an $\mathfrak{sl}_2$ algebra $[L_0,L_{\pm1}]=\pm L_{\pm1}, \;[L_{+1},L_{-1}]=-2L_0$ with $$\begin{aligned}
\label{eq:infgenerators}
    L_{-1}=\partial_z, \qquad L_{0}=z\partial_z+\Delta , \qquad L_{+1}=z^2\partial_z+2\Delta z.
\end{aligned}$$ The trivial *coproduct* $\Delta(L_n)=L_n\otimes \mathbf{1}+\mathbf{1}\otimes L_n$ for $n=-1,0,1$ distributes the action of the differential generators on the different operators in a correlation function, leading to the three Ward identities, which demand the correlation functions to remain invariant under the action by the global conformal subgroup: $$\begin{aligned}
\label{eq:distribute}
     L_n\braket{\mathcal{O}(z_1)\mathcal{O}(z_2)}=m\circ\braket{\Delta(L_n)[\mathcal{O}(z_1)\otimes\mathcal{O}(z_2)]}\equiv 0, 
\end{aligned}$$ where $m$ is a linear multiplication map which multiplies the entries of the tensor product. Solving these three equations consistently leads to the correlation functions of gravitational theories for which the holographic boundary theory is a standard CFT.

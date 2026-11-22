---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-021-54-the-multiplicative-unitary-and-modular-maps
section_title: "The multiplicative unitary and modular maps"
section_number: 5.4
pages: 46-47
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.979
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:Dual:multi}
Under the transformation $\xi$, we can now express all the operators defined earlier on $\hat{\cH}$ to $\cH$. We have
\begin{Prop}
The action $\pi: \hat{\cA}\to \cH$ is given by
\begin{eqnarray}
\pi(\hat{A}) &=& e^{-2\pi bs},\\
\pi(\hat{B}) &=& G_b(-it) \circ e^{2\pi b(p_t-p_s)} \circ G_b(-it)\inv.
\end{eqnarray}
\end{Prop}

Hence in particular $W$ is indeed a genuine element in $M(\cA\ox \hat{\cA})$.

We also note that by general theory, the multiplicative unitary for $\hat{\cA}$ is given by
\Eq{\hat{W}=\S W^* \S,}
where $\S$ is the permutation operator on the tensor product. The coproduct induces by $\hat{W}$ is precisely the one we defined earlier, that $\hat{A}$ and $\hat{B}$ transformed as how $A$ and $B$ do.

\begin{Prop} The modular maps act on $\cH$ by:
\begin{eqnarray}
\hat{T}(f) &=& \over[f](s+t-iQ,-t)e^{-\pi Qt}e^{-\pi it^2}\\
\hat{T^*}(f)&=&\over[f](s+t,-t)e^{-\pi Qt}e^{-\pi it^2}\\
\hat{\DD}(f)&=&f(s+iQ,t)\\
\hat{J}(f)&=&\over[f](s+t-\frac{iQ}{2},-t)e^{-\pi Qt}e^{-\pi it^2}.
\end{eqnarray}
\end{Prop}

From these actions, we can verify all the well-known properties between these maps on $\cH$ (see \cite{KV2} Prop 2.1, 2.11,2.12):
\begin{Prop} \label{RJ} For $x\in \cA, y\in\hat{\cA}$, we have the properties:
\begin{eqnarray}
\hat{J}\L_R(x)&=&\L(R(x)^*),\\
\hat{\DD}^{-\frac{1}{2}}\L(x) &=& \L_R(\t_{i/2}(x)),\\
\hat{T}^*\L(x)&=&\L(S\inv(x)^*),\\
\label{nu}\hat{J}J&=&\nu^{i/4}J\hat{J},\\
\label{R1}R(x)&=&\hat{J}x^*\hat{J},\\
\label{R2}\hat{R}(y)&=&Jy^*J.
\end{eqnarray}
Furthermore, if we define on $\cH$ the operator $G$ (\cite{KV1} Prop 3.22):
\Eq{G \L((h_R\ox 1)(\D(x^*)(y\ox 1)))= \L((h_R\ox 1)(\D(y^*)(x\ox1)))}
and its polar decomposition $G=IN^{1/2}$, then we have
$\hat{T}^*=G, \hat{J}=I$ and $\hat{\DD}=N\inv$.
\end{Prop}

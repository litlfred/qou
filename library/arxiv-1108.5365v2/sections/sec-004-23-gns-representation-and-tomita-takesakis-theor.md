---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-004-23-gns-representation-and-tomita-takesakis-theor
section_title: "GNS representation and Tomita-Takesaki's theory"
section_number: 2.3
pages: 11-13
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.965
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:pre:GNS}
Let us recall the main objects in the study of GNS representation of a $C^*$-algebra (see e.g. \cite{KV1}).

\begin{Def} A Gelfand-Naimark-Segal (GNS) representation of a $C^*$-algebra $\cA$ with a weight $\phi$ is a triple
$$(\cH, \pi, \L),$$
where $\cH$ is a Hilbert space, $\L:\cA\to\cH$ is a linear map, and $\pi:\cA\to\cB(\cH)$ is a representation of $\cA$ on $\cH$ such that $\L(\cN)$ is dense in $\cH$, and
\begin{eqnarray}
\pi(a)\L(b)&=&\L(ab) \tab\forall a\in\cA,b\in \cN,\\
\<\L(a),\L(b)\>&=&\phi(b^*a)\tab\forall a,b\in\cN,
\end{eqnarray}
where $\cN=\{a\in\cA: \phi(a^*a)<\oo\}$.
\end{Def}

The Tomita-Takesaki's Theory \cite{Ta,T} provides a detailed description of the GNS-construction in the von Neumann algebraic setting:
\begin{Def} Giving a weight $\phi$ that determines the Hilbert space structure by the GNS construction, the operator
\Eq{\label{T}T: x\to x^*} is closable and has a polar decomposition as 
\Eq{T=J\DD^{\frac{1}{2}},}
where $J$ is called the modular conjugation, and $\DD$ is called the modular operator.
\end{Def}

A very important property of $J$ is the following
\begin{Thm}[Murray-von Neumann]\label{MvN} Let $M$ be the completion of $\cA\sub \cB(\cH)$ in the weak operator topology as a von Neumann algebra. Then considering $M\sub \cB(\cH)$, we have
\Eq{JM J=M',}
where $M'$ is the commutant of $M$.
\end{Thm}

\begin{Def} For $x\in\cA$, the operator
\Eq{\s_t^{\phi}(x) := \DD^{it}x\DD^{-it}} is called the modular automorphism group.

We have $\phi(a^*b) = \phi(b\s_0^\phi(a^*))$

\end{Def}

On the Hopf * algebra level, we have the following properties:

\begin{Prop}
The antipode $S$ has a polar decomposition \Eq{S=\t_{-i/2}\circ R,}
where $\t_{-i/2}$ denotes the analytic generator of $(\t_t)_{t\in\R}$, called the \emph{scaling group}, which is a group of automorphisms of $M$, and $R$, called the \emph{unitary antipode}, is an anti-automorphism of $M$. 

We have $R^2=1$ and $S^2=\t_{-i}$.

\end{Prop}

Finally some properties concerning the left and right invariant Haar functional:
\begin{Prop}
The left invariant Haar functional $\phi$ and right invariant Haar functional $\psi$ are related by $\psi=\phi \circ R$.

We have \Eq{\phi\circ\t_t=\nu^{-t}\phi,\tab \psi\circ\s_t^{\phi}=\nu^{-t}\psi,}where $\nu>0$ is called the scaling constant.

Furthermore there exists an element $\d\in \cA$ such that $$\s_t^\phi(\d)=\nu^t\d,$$ where $\d\in \cA$ is called the modular element.
\end{Prop}

\begin{Prop} \label{GNSright}The map $\L_R: \cA\to \cH$ defined by
\Eq{\L_R(a):=\L_L(a\d^{-\frac{1}{2}}),} gives the GNS representation of $\cA$ with the right Haar functional on the same space $\cH$, where $\d$ is the modular element defined above.
\end{Prop}

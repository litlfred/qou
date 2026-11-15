---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-024-62-the-representation-space
section_title: "The representation space"
section_number: 6.2
pages: 48-51
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.942
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:Trans:rep}
We introduce the transformations such that $\cA$ acts on $\cH$ canonically, and $\hat{\cA}$ acts on $\hat{\cH}$ canonically. We will use capital letter to denote the transformed function. All the new Hilbert spaces are $L^2(\R\x\R)$.

\begin{Def} We define $\cT: \cH \to \cH_{rep}$ by
\Eq{\cT: f(s,t)\mapsto \int_\R f(\a, t-s+\frac{iQ}{2})e^{2\pi i\a s} d\a,}
\Eq{\cT\inv: F(s,t)\mapsto \int_\R F(\a, t+\a-\frac{iQ}{2})e^{-2\pi i\a s}d\a,}
or simply $\cT = (t\mapsto t-s)\circ \cF_s\inv\circ (t\mapsto t+\frac{iQ}{2})$.

Similarly we define $\hat{\cT}:\hat{\cH}\to\hat{\cH}_{rep}$ by
\Eq{\hat{\cT}: \hat{f}(s,t)\mapsto \int \hat{f}(\a, t-s+\frac{iQ}{2})e^{-2\pi i\a t}e^{\pi Q\a}d\a,}
\Eq{\hat{\cT}\inv: \hat{F}(s,t)\mapsto \int \hat{F}(\a,t+\a-\frac{iQ}{2})e^{2\pi is(\a+t)}d\a,}
or simply $\hat{\cT}=(t\mapsto t-s)\circ \cF_s \circ (t\mapsto t+\frac{iQ}{2})\circ e^{-2\pi is t}$.
\end{Def}

\begin{Prop} Under the transformations, both the spaces $\cH_{rep}$ and $\hat{\cH}_{rep}$ carry the usual inner product with respect to the standard Lebesgue measure:
\Eq{\<F(s,t), G(s,t)\> = \int_\R \int_\R \over[G(s,t)]F(s,t) dsdt.}
\end{Prop}

\begin{Prop} Under the transformations, the action of $\cA$ on $\cH_{rep}$ is given by
\Eq{A=e^{2\pi bs},\tab B= e^{2\pi bp_s},}
and the action of $\hat{\cA}$ on $\hat{\cH}_{rep}$ is given by
\Eq{\hat{A}=e^{-2\pi bs},\tab \hat{B}=e^{2\pi bp_s}.}
\end{Prop}
\begin{proof} Let us demonstrate the use of transformation rule for say, the operator $B$. The rest is similar.
Recall that $B$ acts on $\cH$ as $e^{2\pi b s}e^{-2\pi bp_t}$. Hence under the transformation it becomes
\begin{eqnarray*}
e^{2\pi b s}e^{-2\pi bp_t}&\mapsto_{t\mapsto t+\frac{iQ}{2}}& e^{2\pi b s}e^{-2\pi bp_t}\\
&\mapsto_{\cF_s\inv}& e^{2\pi b p_s}e^{-2\pi bp_t}\\
&\mapsto_{t\mapsto t-s}& e^{2\pi b p_s}.
\end{eqnarray*}
\end{proof}

As a corollary, we have
\begin{Cor} As a representation of $\cA$ we have
\Eq{\cH\simeq \cH_{irr} \ox L^2(\R),}
where $\cH_{irr}$ is the canonical irreducible representation \eqref{Hirr} of $\cA$ on $L^2(\R)$.
\end{Cor}

Let us also note that 
\begin{Prop} The product of two elements in $\cA$ induces a twisted product on $\cH$ by
\Eq{F\cdot G = \cT(\cT\inv(F)\cdot \cT\inv(G)) = \int_\R F(s,\t)G(\t,t) d\t.}
\end{Prop}

We can do the same analysis to the dual space:
\begin{Prop} Under the transformations, the action of $\hat{\cA}$ on $\cH_{rep}$ is given by
\Eq{\hat{A}=e^{2\pi b(p_s+p_t)},\tab \hat{B}=G_b(\frac{Q}{2}+is-it)\circ e^{2\pi b(p_t+s)}\circ G_b(\frac{Q}{2}+is-it)\inv,}
and the action of $\cA$ on $\hat{\cH}_{rep}$ is given by
\Eq{A=e^{2\pi b(p_s+p_t)}, B=G_b(\frac{Q}{2}-is+it)\inv\circ e^{2\pi b(p_t-s)}\circ G_b(\frac{Q}{2}-is+it).}
\end{Prop}
\begin{Rem} Note that the action of $\cA$ on $\hat{\cH}$ is obtained by the $\xi$ transformation. Moreover, recall that $G_b(\frac{Q}{2}+is)$ is unitary, hence the action above is still positive.
\end{Rem}

Finally we will need to describe the action of the modular conjugation $J$ and $\hat{J}$ that are crucial in the construction of the multiplicative unitary for the quantum double.

\begin{Prop} The action of $J$ and $\hat{J}$ on $\cH_{rep}$ is given by
\Eq{J: F(s,t)\mapsto \over[F](t,s),}
\Eq{\hat{J}:F(s,t)\mapsto \over[F](-s,-t)e^{\pi is^2-\pi it^2}\nu^{i/8},}
where $\nu=e^{-2\pi Q^2}$.

Similarly, the action of $\hat{J}$ on $\hat{\cH}_{rep}$ is also given by
\Eq{\hat{J}: \hat{F}(s,t)\mapsto \overline{\hat{F}}(t,s),}
while the action of $J$ on $\hat{\cH}_{rep}$ is given by
\Eq{J:\hat{F}(s,t)\mapsto \overline{\hat{F}}(-s,-t)e^{\pi it^2-\pi is^2}\nu^{-i/8}.}
\end{Prop}

\begin{Prop} \label{AdJ} The action of $Ad J$ on $\cA$ is given by:
\Eq{J(x)J=\hat{R}_*(x^*),}
where $\hat{R}_*$ is an anti-homomorphism given by
\Eq{\hat{R}_*(A)=\hat{A}_*,\tab \hat{R}_*(B)=\hat{B}_*,}
where \Eq{\hat{A}_* =e^{2\pi bt},\tab \hat{B}_*=e^{-2\pi bp_t}.}
The action of $Ad \hat{J}$ on $\hat{\cA}$ is given by:
\Eq{\hat{J}(y)\hat{J}=R_*(y^*),}
where $R_*$ is an anti-homomorphism given by
\Eq{R_*(\hat{A})=A_*,\tab R_*(\hat{B})=B_*,}
where \Eq{A_* =e^{-2\pi bt}, \tab B_*=e^{-2\pi bp_t}.}
\end{Prop}

\begin{Cor}\label{Jcom} $J\circ \cA\circ J$ commutes with $\cA$  as operators on $\cH_{rep}$, and similarly $\hat{J}\circ \hat{\cA}\circ \hat{J}$ commutes with $\hat{\cA}$ as operators on  $\hat{\cH}_{rep}$, which verifies Theorem \ref{MvN}.
\end{Cor}

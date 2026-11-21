---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-038-86-the-modular-double
section_title: "The modular double"
section_number: 8.6
pages: 87-88
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.987
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:regular:MD}
It is known that the representation space $\cP_{\l,t}$ is actually a nontrivial representation for the modular double $U_q(\gl(2,\R))\ox U_{\til[q]}(\gl(2,\R))$. In this section we describe its action using the same multiplicative unitary $\bW_m$.

The modular double counterpart $U_{\til[q]}(\gl(2,\R))$ is defined in the same way with $q$ replaced by $\til[q]$ throughout.  In particular we can define the pairing between $\til[E],\til[F],\til[K],\til[K_0]$ with $\til[A],\til[B],\hat{\til[A]},\hat{\til[B]}$ as before. Recall that $\til[A]=A^{1/b^2}$ and similarly for the other quantum plane variables. Hence by the $b\longleftrightarrow b\inv$ duality of $\bW_m$, we can pair it with $U_{\til[q]}(\gl(2,\R))$, and obtain:

\begin{Prop} The left regular action of $U_{\til[q]}(\gl(2,\R))$ on $L^2(GL_q^+(2,\R))$ is given by replacing $b$ with $b\inv$, i.e.
\begin{eqnarray*}
\til[K_0] &=& e^{\frac{\pi b\inv}{2}s_2},\\
\til[K]&=& e^{-\pi b\inv s_1},\\
\til[E]&=&\frac{i}{\til[q]-\til[q]\inv}(\til[q]^{1/2}e^{\pi b\inv (s_1-\l)}+\til[q]^{-1/2}e^{-\pi b\inv(s_1-\l)})e^{-2\pi b\inv p_{s_1}},\\
\til[F]&=&\frac{i}{\til[q]-\til[q]\inv}(\til[q]^{-1/2}e^{\pi b\inv (s_1+\l)}+\til[q]^{1/2}e^{-\pi b\inv(s_1+\l)})e^{2\pi b\inv p_{s_1}}.\\
\end{eqnarray*}
We note that $\til[E]$ and $\til[F]$ are positive operators only when $\frac{1}{2n+1}<b^2<\frac{1}{2n}$ for $n\in \N$, and they are not necessarily essentially self-adjoint on the natural domain $\cW$ \cite{Ru}. To obtain essential self-adjointness, we have to apply Proposition \ref{x+p} and define the operators on the respective transformed domain $g_b\cdot \cW$.
\end{Prop}
Ignoring the factors, we note from Theorem \ref{ThmLeft} that the summand of $E$ and $F$ are $q$-commuting, hence we immediately obtain using Corollary \ref{u+v} (see also \cite[Cor 1]{BT}).
\begin{Prop}
As positive self-adjoint operators we have
\begin{eqnarray*}
K_0^{1/b^2}&=&\til[K_0],\\
K^{1/b^2}&=&\til[K],\\
2\sin(\pi b^{-2})\til[E] &=& (2\sin(\pi b^{2})E)^{1/b^2},\\
2\sin(\pi b^{-2})\til[F] &=& (2\sin(\pi b^{2})F)^{1/b^2}.
\end{eqnarray*}
\end{Prop}

Similar analysis works as well for the right regular representation, hence Theorem \ref{main} is actually an equivalence as a representation of the modular double $$U_{q\til[q]}(\gl(2,\R))_L\ox U_{q\til[q]}(\gl(2,\R))_R,$$ 
where $U_{q\til[q]}(\gl(2,\R)):=U_q(\gl(2,\R))\ox U_{\til[q]}(\gl(2,\R))$ denotes the modular double.

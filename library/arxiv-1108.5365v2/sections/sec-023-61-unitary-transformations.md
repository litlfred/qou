---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-023-61-unitary-transformations
section_title: "Unitary transformations"
section_number: 6.1
pages: 47-48
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.971
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:Trans:unit}
In this section, we list the transformations that will be used. They are all unitary transformations on $L^2(\R\x\R)$ equipped with the standard Lebesgue measure. For an operator $P$, its action under any transformation $\cT$ is given by
\Eq{P\mapsto \cT\circ P \circ \cT\inv.}

\begin{Prop} The following lists the transformations and their effects on the multiplication and differential operators $s$ and $p_s$.
$$f(s,t)\longmapsto:$$
\begin{eqnarray}
f(-s,t)&:& s\to -s,\tab p_s\to -p_s,\\
f(s,-t)&:& t\to -t,\tab p_t\to -p_t,\\
f(t,s)&:& s\corr t,\tab p_s\corr p_t,\\
f(s,t)e^{\pm2\pi ist}&:& p_s\to p_s\mp t,\tab p_t \to p_t\mp s,\\
f(s,t)e^{\pm \pi is^2}&:& p_s\to p_s\mp s,\\
f(s,t)e^{\pm \pi it^2}&:& p_t\to p_t\mp t,\\
f(s\pm t,t)&:& s\to s\pm t,\tab p_t\to p_t\mp p_s,\\
f(s,t\pm s)&:& t\to t\pm s,\tab p_s\to p_s\mp p_t,\\
\cF(f)=\int f(\t)e^{-2\pi i\t x}d\t &:&x\to -p_x,\tab p_x\to x,\\
\cF\inv(f)=\int f(\t)e^{2\pi i\t x}d\t &:& x\to p_x,\tab p_x\to -x,
\end{eqnarray}
where $\cF$ is the Fourier transform with
$$\cF^2 = -Id.$$
All the transformations above preserve the dense subspace $\cW\hat{\ox}\cW$ (cf. \eqref{WxW}).
\end{Prop}

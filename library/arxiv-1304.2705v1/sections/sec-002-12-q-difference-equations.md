---
doc_id: arxiv-1304.2705v1
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-002-12-q-difference-equations
section_title: "q-difference equations"
section_number: 1.2
pages: 4-4
source_pdf: 1304.2705v1.pdf
source_sha256: cb07e66e418e11f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.868
latex_coverage_ratio: 0.943
doc_brief: "FROM STATE INTEGRALS TO q-SERIES — It is well-known to the experts that multi-dimensional state integrals of prod- ucts of Faddeev’s quantum dilogarithm which arise in Quantum Topology can be written"
---
\lbl{sub.qstructure}

Next we describe a linear $q$-difference equation of $F_{A,B}(q,x)$.
Consider the operators $\hat x$ and $\hat E$ which act on 
$f(x) \in \BQ(q)[[x]]$ by:
$$
(\hat E f)(x)=f(qx), \qquad (\hat x f)(x)=x f(x) \,.
$$ 
Observe that $\hat E \hat x = q \hat x \hat E$.

\begin{lemma}
\lbl{lem.thm2}
\rm{(a)} We have:
\begin{equation}
\lbl{eq.Ftau}
F_{A,B}(q^{-1},x)=\ti F_{A,B}(q,x) \,.
\end{equation}
\rm{(b)} $F_{A,B}$ satisfies the linear $q$-difference equation

\begin{equation}
\lbl{eq.FABrec}
\left((1-\hat E)^B -(-1)^A q^A x \hat E^A \right) F_{A,B}(q,x)=0 \,.
\end{equation}
\end{lemma}

\begin{corollary}
\lbl{cor.omega}
\rm{(a)} If we define $\omega(q,x)=F_{A,B}(q,qx)/F_{A,B}(q,x)$ 
and $\omega(q,x)_n=
\prod_{j=1}^n \omega(q,q^jx)$, then $\omega$ satisfies the
nonlinear equation 
$$
\sum_{j=0}^B (-1)^j \binom{B}{j} \omega(q,x)_j -(-1)^A q^A x \omega(q,x)_A=0
\,.
$$
\rm{(b)} $F$ is an admissible power series in the sense of 
Kontsevich-Soibelman \cite[Sec.6]{KS}, the limit 
$\lim_{q\to 1} \omega(q,x)=\omega(x) \in \overline\BQ[[x]]$ 
exists and satisfies the 
algebraic equation (also known as the Nahm equation or the gluing equation) 
\begin{equation}
\lbl{eq.FABnahm}
(1-\omega(x))^B = (-1)^A x \omega(x)^A \,.
\end{equation}
\end{corollary}
The Nahm equation has been studied by several authors including
\cite[Sec.3]{Za:DL}, \cite{Vlasenko,VZ}, \cite[Sec.4]{R-V}.

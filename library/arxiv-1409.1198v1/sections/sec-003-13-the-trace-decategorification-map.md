---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-003-13-the-trace-decategorification-map
section_title: "The trace decategorification map"
section_number: 1.3
pages: 3-3
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.986
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
The trace, or zeroth  Hochschild homology, is another procedure for turning a linear category $\C$ into an abelian group.  It is defined by
 \begin{gather*}
  \Tr(\C ):=
\bigoplus_{x\in \Ob(\modC )}\modC (x,x)/\Span\{fg-gf\}
\end{gather*}
where $f$ and $g$ run through all pairs of morphisms $f:x\to y$ and $g:y\to x$ with $x,y\in \Ob(\C)$.
We write $[f]$ for the class of an endomorphism $f \maps x \to x$ in $\Tr(\C)$.
In section \ref{sec_trace_lincat} we show that the trace satisfies the property that $[f \oplus g] = [f] + [g]$.


In the category $\cat{Vect}_{\k}$, the class $[\phi]$ of an endomorphism $\phi \maps V \to V$ is
equal to the class $\tr(\phi)[1_{\k}]$, where $\tr(\phi)$ is the usual trace of the linear endomorphism $\phi$ (see exercise \ref{ex-1}).    Hence, the categorical trace of $\cat{Vect}_{\k}$ is closely connected to the usual trace map sending a vector space to an element of the ground field $\k$.


Note that $\dim_V=\tr(1_V)$ so that the trace can be seen as a generalization of the dimension decategorification map.   In Section~\ref{sec_trace_lincat} we show that
the trace $\Tr(\cat{Vect}_{\k})$ of the category of vector spaces can be identified with the ground field $\k$ and that the trace $\Tr(\cat{gVect}_{\k})$ of
the category of graded vector spaces is isomorphic to $\k[q,q^{-1}]$.





\subsubsection{Traced Euler characteristics}




The Euler characteristic in  $\cat{Vect}_{\k}$ can be recast in the language of traces by observing that $\dim_V=\tr(1_V)$, which allows to define so called traced  Euler characteristic
$$\chi_{\tr}(C^\bullet)=\sum_i (-1)^i\;\; \tr (1_{C^i}) \, .$$
This notion can be extended to any linear category $\C$ as follows. Given a complex
$C^{\bullet}\in   \Kom(\C)$,
\[
 \xy
  (-20,0)*+{\Tr(\C)}="1";
  (20,0)*+{\Kom(\C)}="2";
  {\ar_-{ \chi_{tr}} "2";"1" };
 \endxy
 \]
is defined by setting  $\chi_{tr}(C^{\bullet})=\sum_i (-1)^i [1_{C^i}]$, where $[f]$ denotes the class of the endomorphism $f$ in $\Tr(\C)$.
In general, $\chi_{\tr}$ does not need to coincide with the usual Euler characteristic.

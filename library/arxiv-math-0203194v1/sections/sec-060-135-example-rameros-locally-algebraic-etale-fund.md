---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-060-135-example-rameros-locally-algebraic-etale-fund
section_title: "Example: Ramero's locally algebraic 'etale fundamental group."
section_number: 13.5
pages: 129-130
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.965
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::1.5}

\begin{para}\label{para::1.5.1}
 When $S$ is countable at infinity, L. Ramero has introduced an
 interesting category $\Cov^{\mathrm{loc.alg}}_S$ of \'etale coverings, called
 `locally algebraic', which generalize the logarithmic covering of
 $\A^1$, and which are intimately connected with the local study of
 meromorphic differential equations around singularities \cite[4]{ramero98}.

 An \'etale covering is locally algebraic if the preimage of every {\it
 compact subdomain} $W\subset S$ is a disjoint union $\coprod W_i$ of
 subdomains $W_i$ which are finite \'etale over $W$. Since $S$ is (by
 assumption) a union of an increasing countable family of compact
 subdomains $S_j,\; j\geq 1$, it suffices to check the condition for 
 $W=S_j,\forall j.$ 

 \noindent This category is stable under taking connected components,
 fiber products (over $S$) and quotients. Moreover, it is stable by
 disjoint union and `composition'. Assuming that
 $s\in S_1$, one has a natural homomorphism  
 \begin{equation*}
 \liminj\pi_1^{\mathrm{loc.alg}}(S_j,\,\ovl{s}) = \liminj
  \pi_1^{\mathrm{alg}}(S_j,\,\ovl{s})\to \pi_1^{\mathrm{loc.alg}}(S,\,\ovl{s}).
 \end{equation*}
\end{para}

\begin{pro}\label{pro::1.5.2} This is an isomorphism:
 $\pi_1^{\mathrm{loc.alg}}(S,\,\ovl{s})\cong \liminj
 \pi_1^{\mathrm{alg}}(S_j,\,\ovl{s})$.
\end{pro}
   
\begin{proof}
 It is clear that an automorphism of $F^{\mathrm{loc.alg}}_{S,\ovl{s}}$
 amounts to a compatible family of automorphisms of
 $F^{\mathrm{alg}}_{S_j,\ovl{s}}$, hence the homomorphism is
 bijective. Moreover, the induced map $ \liminj
 \pi_1^{\mathrm{alg}}(S_j,\,\ovl{s})$-sets $\to
 \pi_1^{\mathrm{loc.alg}}(S,\,\ovl{s})$-sets is an equivalence: both
 sides are equivalent to $\Cov^{\mathrm{loc.alg}}_S$, \cf \ref{thm::1.4.5} and
 \cite[4.1.6]{ramero98}. Therefore open subgroups correspond to stabilizers as
 usual, and the bijection $\pi_1^{\mathrm{loc.alg}}(S,\,\ovl{s})\cong
 \liminj \pi_1^{\mathrm{alg}}(S_j,\,\ovl{s})$ is bicontinuous.
\end{proof}

\medskip\noindent It is not known whether
$\pi_1^{\mathrm{loc.alg}}(S,\,\ovl{s})$ is a pro-discrete group (\cf in
this direction {\it loc.~cit.} 4.3). 

\medskip\noindent {\it Example.} The logarithm of any Lubin-Tate formal
group over a $p$-adic field gives rise to a locally algebraic 
\'etale covering of the analytic affine line, \cf {\it loc.~cit.} 6.1.1.

On the other hand, the Gross-Hopkins covering of $\P^1$ is not locally
algebraic, although there is a finite affinoid 
cover $(V_i)$ of $\P^1$ such that the restriction of the covering to any
$V_i$ is a disjoint union of finite \'etale coverings.

\newpage

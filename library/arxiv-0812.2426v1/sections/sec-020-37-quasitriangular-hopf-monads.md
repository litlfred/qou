---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-020-37-quasitriangular-hopf-monads
section_title: "Quasitriangular Hopf monads"
section_number: 3.7
pages: 13-13
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 1.0
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
Let $T$ be a Hopf monad on an autonomous category $\mathcal{C}$. An *$\mathrm{R}$-matrix* for $T$ is a natural transformation $R_X,Y\colon
X \otimes Y \to T(Y) \otimes T(X)$ satisfying: $$\begin{aligned}
& (\mu_Y \otimes \mu_X)R_{T(X),T(Y)}T_2(X,Y)=(\mu_Y \otimes \mu_X)T_2(T(Y),T(X))T(R_{X,Y}); \\
\begin{split}
& (\mathrm{id}_{T(Z)}  \otimes T_2(X,Y))R_{X \otimes Y,Z} \\
& \phantom{XXXXXX}=(\mu_Z \otimes \mathrm{id}_{T(X) \otimes T(Y)}) (R_{X,T(Z)} \otimes \mathrm{id}_{T(Y)} )(\mathrm{id}_X \otimes R_{Y,Z}) ;
\end{split}\\
\begin{split}
& (T_2(Y,Z) \otimes \mathrm{id}_{T(X)})R_{X,Y \otimes Z} \\
& \phantom{XXXXXX}=( \mathrm{id}_{T(Y) \otimes T(Z)} \otimes \mu_X) ( \mathrm{id}_{T(Y)} \otimes R_{T(X),Z} ) (R_{X,Y} \otimes \mathrm{id}_Z).
\end{split}
\end{aligned}$$

Note that an $\mathrm{R}$-matrix satisfies some QYB equation and is $*$-invertible (where $*$ is some convolution product), see [@BV2 corollary 8.7].

A *quasitriangular Hopf monad* is a Hopf monad equipped with an $\mathrm{R}$-matrix.

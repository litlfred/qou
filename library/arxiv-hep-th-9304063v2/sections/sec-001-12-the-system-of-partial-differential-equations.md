---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: sec-001-12-the-system-of-partial-differential-equations
section_title: "The System of Partial Differential Equations"
section_number: 1.2
pages: 3-3
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.935
doc_brief: "arXiv:hep-th/9304063v2 29 Jan 1999 — 10 sections: Front matter; Introduction and Statement of Resu; The System of Partial Differential"
---
We set J:= \_j=1\^m(a\_2j-1,a\_2j) (a\_j) []{#Jform label="Jform"} and write $D(J;\la)$ for the Fredholm determinant of $K$ (the operator with kernel $K(x,y)$) acting on $J$. If we think of this as a function of $a=(a_{1},\ldots,a_{2m})$ then d D(J;) = -\_j=1\^2m(-1)\^j R(a\_j,a\_j) da\_j[]{#diff label="diff"} where $R(x,y)$ is the kernel of $K(I-K)^{-1}$. We introduce the notations (x):=  J\_(~~x~~), (x):= x '(x)[]{#phidef label="phidef"} and the quantities $$\begin{aligned}
q_{j}:&=&\,(I-K)^{-1}\phi\,(a_{j}),~~p_{j}:=\,(I-K)^{-1}\psi\,(a_{j}),
\;\;\;\;(j=1,\ldots ,2m)\label{pqdef} \\
u:&=&\,(\phi,(I-K)^{-1}\phi),~~v:=\,(\phi,(I-K)^{-1}\psi),\label{uvdef} 
\end{aligned}$$ where the inner products refer to the domain $J$. The differential equations are $$\begin{aligned}
\frac{\partial q_{j}}{\partial a_{k}}&=&(-1)^{k}\,
\frac{q_{j}p_{k}-p_{j}q_{k}}{a_{j}-a_{k}}  \,q_{k} \hspace{2em} (j\neq k)\label{qjk}\\
\noalign{\vskip3pt}
\frac{\partial p_{j}}{\partial a_{k}}&=&(-1)^{k}\,
\frac{q_{j}p_{k}-p_{j}q_{k}}{a_{j}-a_{k}}  \,p_{k} \hspace{2em} (j\neq k)\label{pjk}\\
\noalign{\vskip3pt}
a_{j}\frac{\pl q_{j}}{\pl a_{j}}&=&p_{j}\,+\,\frac{1}{4}\,q_{j}\,u\,
-\,\sum_{k\neq j}(-1)^{k}\,a_{k}\,\frac{q_{j}p_{k}-p_{j}q_{k}}{a_{j}-a_{k}}\,q_{k}
\label{qj} \\ \noalign{\vskip3pt}
a_{j}\,\frac{\pl p_{j}}{\pl a_{j}}&=&\frac{1}{4}(\al^{2}-a_{j}+2v)\,q_{j}
-\frac{1}{4}p_{j}\,u\,-\sum_{k\neq j}(-1)^{k}\,a_{k}\,\frac{q_{j}p_{k}-p_{j}q_{k}}
{a_{j}-a_{k}}\,p_{k} \label{pj}\\ \noalign{\vskip3pt}
\frac{\pl u}{\pl a_{j}}&=&(-1)^{j}\,q_{j}^{2} \label{uj}\\ \noalign{\vskip3pt} 
\frac{\pl v}{\pl a_{j}}&=&(-1)^{j}\,p_{j}\,q_{j}. \label{vj}
\end{aligned}$$ Moreover the quantities $R(a_{j},a_{j})$ appearing in ([\[diff\]](#diff){reference-type="ref" reference="diff"}) are given by a\_j R(a\_j,a\_j)=\_kj(-1)\^k a\_k  +p\_j\^2 -  (\^2-a\_j+2v) q\_j\^2+ p\_j q\_j u. []{#Rjj label="Rjj"} These equations are quite similar to eqs. (1.4)--(1.9) of [@tw2], as is their derivation.

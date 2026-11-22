---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-011-relation-of-sum-formulas-to-ramanujan-sums
section_title: "Relation of sum formulas to Ramanujan sums"
section_number: null
pages: 11-12
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 1.0
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
Another amusing fact about the two nice cases ([\[0powerdR\]](#0powerdR){reference-type="ref" reference="0powerdR"}) and ([\[1powerdR\]](#1powerdR){reference-type="ref" reference="1powerdR"}) is their possible relation to the celebrated Ramanujan sums [@Ram] $$\begin{aligned}
c_{m,k}:= \sum_{(a,m)=1}^k e^{\frac{2\pi i ak}{m}}
\end{aligned}$$ where the sum goes over $a$, which are coprime with $m$, and it is always a positive integer. Counterparts of ([\[0powerdR\]](#0powerdR){reference-type="ref" reference="0powerdR"}) and ([\[1powerdR\]](#1powerdR){reference-type="ref" reference="1powerdR"}), not literal, still surprisingly similar appear in two ways: with plethystic and ordinary exponentials.

Defining the plethystic exponential of a function $f(x)$ as $$\begin{aligned}
P.E.\Big(f(q)\Big):=\exp\left(\sum_{k=1}^\infty{f(q^k)\over k}\right)
\end{aligned}$$ one obtains $$\begin{aligned}
 P.E.\left({q\over 1-q}\right) = \xi_0(q) \nonumber\\
 P.E.\left(\sum_{k=1}^\infty {c_{2,k}q^k\over k}\right) = e^{q^2+q} = \sqrt{\xi_1(2q)}   \nonumber\\
P.E.\left(\sum_{k=1}^\infty {c_{1,k}q^k\over k}\right) = e^q = \xi_2(q)
\end{aligned}$$ where $$\begin{aligned}
\xi_m(q):=\sum_Rq^{|R|}d_R^m
\end{aligned}$$ is the quantity ([\[dimrep\]](#dimrep){reference-type="ref" reference="dimrep"}). In terms of ordinary exponentials, one gets $$\begin{aligned}
\xi_0(q)=\exp\left(\sum_{k=1}^\infty{q^k\over k(1-q^k)}\right)\nonumber\\
\xi_1(q)=\exp\left(\sum_{k=1}^\infty{c_{2,k}q^k\over 1-q^k}\right)=e^{2q^2+q}\nonumber\\
\xi_2(q)=\exp\left(\sum_{k=1}^\infty{c_{1,k}q^k\over 1-q^k}\right)=e^q
\end{aligned}$$

In fact, $$\begin{aligned}
P.E.\left(\sum_{k=1}^\infty {c_{0,k}q^k\over k}\right) =\exp\left({q\over 1-q}\right)
\nonumber\\
\exp\left(\sum_{k=1}^\infty{c_{0,k}q^k\over 1-q^k}\right)=\exp\left({q\over (1-q)^2}\right)
\end{aligned}$$ and $$\begin{aligned}
P.E.\left(\sum_{k=1}^\infty {c_{m,k}q^k\over k}\right) = \exp\left(\sum_{d|m} q^d\right),\ \ \ \ \ m>0 \nonumber\\
\exp\left(\sum_{k=1}^\infty{c_{m,k}q^k\over 1-q^k}\right)= \exp\left(\sum_{d|m} d\cdot q^d\right),\ \ \ \ \ m>0
\end{aligned}$$ are always expressed through the exponentiated finite sum over divisors of $m$. Thus, these are simple formulas, which, unfortunately, have nothing to do with our $\xi_m$ at $m>2$.

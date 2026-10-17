---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-015-52-a-family-of-pretzel-knots
section_title: "A family of pretzel knots"
section_number: 5.2
pages: 25-25
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.98
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polynomial and the boundary slopes of knots under the operation of cabling."
---
Consider the pretzel knot $K_p=(-2,3,p)$, where $p$ is an odd integer. It is known that $K_p$ is $A$-adequate if $p>0$, and $B$-adequate if $p<0$. Moreover, $K_p$ is a torus knot if $p \in \{1,3,5\}$. 

 
Suppose now that  $p \ge 5$. Then $K_p$ is $A$-adequate and  by above discussion Conjecture  \ref{slopeaug} 
holds  for
the mirror image $K_p^{*}$.


By \cite[Section 4.7]{Ga-slope} and Example 6.3 below we have $$4a_{K_p}(n) = 2(p^2-p-5)/(p-3) \quad \text{and} \quad 2b_{K_p}(n) = 
-(p-5)/(p-3).$$

Since $4a_{K_p}(n)$ is not an integer, in fact it is easily checked that $ \gcd ( 2(p^2-p-5), p-3)=1$, $K_p$ is not $B$-adequate.
Thus we can't apply Theorem  \ref{slopeadequate}. Note moreover that $\gcd(p-5, p-3)=2$.
By  \cite[Theorem 3.3]{callahan}, $K_p$ has an essential surface with boundary slope $2(p^2-p-5)/(p-3)$, with two boundary components, and Euler characteristic $-(p-5)$, which is equal to $(p-3)(2b_{K_p}(n))$.   
Note that for $p=5$ we get $b_{K_p}(n)=0$. The knot $K=(2,-3,5)$ is known to be a torus knot, which is in agreement with Conjecture \ref{conj}.


Suppose now that $p \le -1$. Then $K$ is $B$-adequate. By \cite[Section 4.7]{Ga-slope} and Example 6.3
we have $4a^*_{K_p}(n) = 2(p+1)^2/p$ and $$2b^*_{K_p}(n) = 
\begin{cases}
1 &\mbox{if } n \not\equiv 0 \pmod{p} \\ 
1 - 2/p & \mbox{if } n \equiv 0 \pmod{p}.
\end{cases}$$

Again since $4a^*_{K_p}(n)$ is not an integer, $K_p$ is not $A$-adequate and Theorem  \ref{slopeadequate} doesn't apply to $K_p^*$.
According to \cite[Theorem 3.3]{callahan}, 
 $K_p$ has an essential surface with boundary slope $2(p+1)^2/p$ and Euler characteristic $p$, which is equal to $p(2b_{K_p}(n))$ when $n \not\equiv 0 \pmod{p}$. Thus we have:
 
\begin{corollary} For an odd integer $p$,  the pretzel knots  $K_p=(-2,3,p)$ and $K^{*}_p$
satisfy Conjectures \ref{conj} and \ref{slopeaug}. 
\end{corollary}

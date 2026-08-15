---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-009-2e-the-asai-l-function
section_title: "2E. The Asai L-function"
section_number: null
pages: 11-12
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
of a Bianchi eigenform.
The space Sk,k(UF,1(n)) has an action of diamond operators ⟨d⟩, for all d∈(OF/n)×; and on any
Hecke eigenform9 these act via a character ε9:(OF/n)×→ C×. Let ε9,Q denote the restriction of this
character to(Z/N Z)×.
Deﬁnition 2.10. Let 9 be a normalised eigenform in Sk,k(UF,1(n)), and χ a Dirichlet character of
conductor m. Deﬁne the Asai L-function of9 by
LAs(9,χ, s):= L(m N)(χ 2ε9,Q, 2s− 2k− 2)·
∑
n>1
(m,n)=1
c(nOF,9)χ( n)n−s,
where N= n∩ Z and L(m N)(−, s) is the Dirichlet L-function with its Euler factors at primes dividing
m N removed. Ifχ is trivial we write simply LAs(9, s).
This Dirichlet series is absolutely convergent for ℜ(s) sufﬁciently large, 1 and has meromorphic
continuation to all s∈ C. (This is proved in [Flicker 1988] or [Ghate 1999] for χ trivial, and the result
for generalχ can be proved similarly.) For s in the half-plane of convergence, it can be written as an
Euler product
LAs(9,χ, s)=
∏
𝓁 prime
LAs
𝓁 (9,χ, s),
where LAs
𝓁 (9,χ, s) depends only onχ(𝓁) and the Hecke and diamond eigenvalues of9 at the primes
above𝓁. If 𝓁| m then LAs
𝓁 (9,χ, s)= 1; if𝓁 ∤ m, then a case-by-case check shows that LAs
𝓁 (9,χ, s) has
the form P𝓁(9,𝓁−sχ(𝓁))−1, where P𝓁(9,−) is a polynomial of degree⩽ 4.
If9 is a new eigenform, and χ is trivial, then LAs(9,χ, s) coincides with the function denoted by
G(s, f) in [Ghate 1999].
Lemma 2.11. Suppose9 is a normalised eigenform of level n coprime to p, n′= n∏
p|p p, and9α
is a normalised eigenform of level n′ such that c(m,9α)= c(m,9) for all m coprime to p. Let α=
c(pOF,9α). Then we have
LAs(9α, s)=(1−αp−s)−1LAs,(p)(9, s),
and L As(9α,χ, s)= LAs(9,χ, s) for every nontrivialχ of p-power conductor. □
1Since the eigenvalues c(l,9) for l prime satisfy|c(l,9)|⩽ 2NF/Q(l)k/2+1 [Jacquet and Langlands 1970, §11], it sufﬁces
to takeℜ(s)> k+ 3. This bound is not optimal, but it sufﬁces for our purposes.
1678 David Loeﬄer and Chris Williams

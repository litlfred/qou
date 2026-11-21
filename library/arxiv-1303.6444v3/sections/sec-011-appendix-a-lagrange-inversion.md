---
doc_id: arxiv-1303.6444v3
doc_title: "VIRIAL EXPANSION BOUNDS"
section_id: sec-011-appendix-a-lagrange-inversion
section_title: "Appendix A. Lagrange Inversion"
section_number: null
pages: 13-14
source_pdf: 1303.6444v3.pdf
source_sha256: 4f12ace2197f70ca
toc_source: outline
doc_brief: "VIRIAL EXPANSION BOUNDS — In the 1960s, the technique of using cluster expansion bounds in order to achieve bounds on the virial expansion was developed by Lebowitz and Penrose (1964) and Ruelle"
---
To ﬁnd the inverse of the function se−s as a power series, we can use the one-dimensional
Lagrange inversion form from [Mer06]. We want to ﬁnd a power series of s in terms of
y = se−s, which amounts to ﬁnding the inverse. We write the equation in the convenient
form:
s = yes
(A.1)
For a formal power series s(y), implicitly deﬁned by s = yφ(s), the Lagrange Inversion
Formula can be stated as:
[yn]s = 1
n[sn−1]φ(s)n
(A.2)
where the notation [yn]f(y) is used to denote the coeﬃcient of yn in the expression f(y).
The function φ on which we wish to perform Lagrange Inversion is φ(s) = es and the
formula for the nth coeﬃcient in the desired power series is:
[yn]s = 1
n[sn−1]ens
= 1
n
nn−1
(n −1)! = nn−1
n!
(A.3)
The power series we obtain is s = P
n≥1
nn−1
n! yn as required.
Acknowledgements. I would like to thank my supervisor Dr. Daniel Ueltschi and Dr.
Sabine Jansen for helpful comments during the preparation of this paper. I would also like
to thank the referees for helpful comments in the ﬁnal editing of the paper.
14
S. J. TATE

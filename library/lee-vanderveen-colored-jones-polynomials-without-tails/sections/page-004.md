---
doc_id: lee-vanderveen-colored-jones-polynomials-without-tails
doc_title: "COLORED JONES POLYNOMIALS WITHOUT TAILS"
section_id: page-004
section_title: "Page 4"
section_number: null
pages: 4-4
source_pdf: lee-vanderveen-colored-jones-polynomials-without-tails.pdf
source_sha256: fcc45aebd34e25dc
toc_source: undetermined
doc_brief: "COLORED JONES POLYNOMIALS WITHOUT TAILS — We exhibit an inﬁnite family of knots with the property that the ﬁrst coeﬃcient of the n-colored Jones polynomial grows linearly with n."
---
C. LEE AND R. VAN DER VEEN
Here the writhe is given by Wr(r, s, t, u) = r −s + t −u and
P = {(a, b, c, d) ∈[0, 1]4 : |a −b| ≤c ≤a + b}.
3. The lack of tail
Using the formulas for the building blocks we may determine the degree δ(a, b, c, d) of each term in
the state sum. It is an explicit piecewise quadratic function on the polytope nP. From our assumptions
it follows that:
δ(a + 1, b, c, d) < δ(a, b, c, d) and δ(a, b, c + 1, d) < δ(a, b, c, d) < δ(a, b, c, d −1).
Therefore all terms of highest degree satisfy b = a + c and d = 0 with 0 ≤a, c ≤a + c ≤n. Explicitly
the degree is δ(a, a + c, c, 0) =
b(r + 2c(1 + r) + s −1) −2(b2(1 + r + s) + c(r + t −2) + c2(r + t)) −2n(−2r −u) −2n2(−r −u)
Setting r, s, t = 5, −3, 5 we ﬁnd δ(a, b, c, d) = −4(a −c)2 + 2n(18 + 10n −(2 + n)u) It follows that
the maxima are on the line a = c and there are ⌊n/2⌋such maxima.
Looking at the building
blocks, each of the corresponding maximal terms in the state sum has the same leading coeﬃcient
(−1)8a+2n(−11+u) = 1. This completes the proof of our main theorem:
Theorem 3.1. If u ≤−3 then C(5, −3, 5, u) is a Manx knot.
More precisely, the leading coeﬃcient of JC(5,−3,5,u),n+1(v) is ⌊n/2⌋.
The same techniques will also show that the pretzel knot P(5, −3, 5) is Manx but this appears to
be the only Manx pretzel knot [9]. We expect that many more Manx knots exist but not in the family
C(r, s, t, u) we considered. All Montesinos Manx knots seem to derive from the unique Manx pretzel
P(5, −3, 5).
Although our Manx knots do not stabilize in the ordinary sense they may still be c-stable. This
more general notion of stability was introduced in Garoufalidis-Vuong [7] and allows growing leading
coeﬃcients. Brieﬂy, a sequence of Laurent power series fn(v) with v-degree δ(n) is c-stable if there
exists a series F(n, x, v) = P∞
k=0 Φk(n, v)xk. Here Φk(n, v) are formal Laurent power series in v with
coeﬃcients that are integer-valued quasi-polynomials in n. We require that for all k ∈N we have
lim
n→∞v−k(n+1)

v−δ(n)fn(v) −
k
X
j=0
Φj(n, v)vj(n+1)

= 0
In their paper they conjecture that c-stability holds for all Reshetikhin-Turaev knot invariants as
one scales a dominant weight.
Acknowledgement. We thank Stavros Garoufalidis for informing us about the notion of c-stability
and the organisers of the 2018 Banﬀworkshop on Modular forms and Quantum invariants for pro-
viding the right atmosphere for writing this paper. We thank Abhijit Champanerkar for interesting
conversations about tails.
References
[1] Cody Armond. The head and tail conjecture for alternating knots. Algebr. Geom. Topol., 13(5):2809–2826, 2013.
[2] Cody Armond and Oliver T. Dasbach. The head and tail of the colored Jones polynomial for adequate knots. Proc.
Amer. Math. Soc., 145(3):1357–1367, 2017.
[3] Cody Armond and Oliver T. Dasbach. Rogers-Ramanujan type identities and the head and tail of the colored Jones
polynomial. Preprint, ArXiv:1106.3948, 2018.
[4] A. Champanerkar and I. Kofman. On the tail of Jones polynomials of closed braids with a full twist. Proceedings of
the American Mathematical Society, 141:2257–2567, 2013.
[5] Francesco Costantino. Integrality of Kauﬀman brackets of trivalent graphs. Quantum topology, 5(2):143–184, 2014.
[6] O. Dasbach and X.S. Lin. On the head and the tail of the colored Jones polynomial. Compos. Math., 142:13321342,
2006.
[7] S. Garoufalidis and T. Vuong. A stability conjecture for the colored Jones polynomial. Topology Proceedings,
(49):211–249, 2017.
[8] Stavros Garoufalidis and Thang T. Q. Lˆe. Nahm sums, stability and the colored Jones polynomial. Research in
Mathematical Sciences, 2:1–55, 2015.
[9] Stavros Garoufalidis, Christine Ruey Shan Lee, and Roland van der Veen. The slope conjecture for Montesinos
knots. Preprint, 2018.
[10] Mustafa Hajij. The colored Kauﬀman skein relation and the head and tail of the colored Jones polynomial. J. Knot
Theory Ramiﬁcations, 26(3):1741002, 14, 2017.

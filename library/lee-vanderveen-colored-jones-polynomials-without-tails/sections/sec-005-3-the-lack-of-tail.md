---
doc_id: lee-vanderveen-colored-jones-polynomials-without-tails
doc_title: "COLORED JONES POLYNOMIALS WITHOUT TAILS"
section_id: sec-005-3-the-lack-of-tail
section_title: "The lack of tail"
section_number: 3
pages: 4-4
source_pdf: lee-vanderveen-colored-jones-polynomials-without-tails.pdf
source_sha256: fcc45aebd34e25dc
doc_brief: "COLORED JONES POLYNOMIALS WITHOUT TAILS — We exhibit an in nite family of knots with the property that the rst coecient of the n-colored Jones polynomial grows linearly with n."
---
Using the formulas for the building blocks we may determine the degree (a;b;c;d ) of each term in
the state sum. It is an explicit piecewise quadratic function on the polytopenP . From our assumptions
it follows that:
(a + 1;b;c;d )< (a;b;c;d ) and (a;b;c + 1;d )< (a;b;c;d )< (a;b;c;d −1):
Therefore all terms of highest degree satisfy b =a +c andd = 0 with 0≤a;c≤a +c≤n. Explicitly
the degree is (a;a +c;c; 0) =
b(r + 2c(1 +r) +s−1)−2(b2(1 +r +s) +c(r +t−2) +c2(r +t))−2n(−2r−u)−2n2(−r−u)
Setting r;s;t = 5;−3; 5 we ﬁnd (a;b;c;d ) = −4(a−c)2 + 2n(18 + 10n−(2 +n)u) It follows that
the maxima are on the line a = c and there are ⌊n=2⌋such maxima. Looking at the building
blocks, each of the corresponding maximal terms in the state sum has the same leading coeﬃcient
(−1)8a+2n(−11+u) = 1. This completes the proof of our main theorem:
Theorem 3.1. If u≤−3 then C(5;−3; 5;u ) is a Manx knot.
More precisely, the leading coecient of JC(5;−3;5;u);n+1(v) is⌊n=2⌋.
The same techniques will also show that the pretzel knot P (5;−3; 5) is Manx but this appears to
be the only Manx pretzel knot [9]. We expect that many more Manx knots exist but not in the family
C(r;s;t;u ) we considered. All Montesinos Manx knots seem to derive from the unique Manx pretzel
P (5;−3; 5).
Although our Manx knots do not stabilize in the ordinary sense they may still be c-stable. This
more general notion of stability was introduced in Garoufalidis-Vuong [7] and allows growing leading
coeﬃcients. Brieﬂy, a sequence of Laurent power series fn(v) with v-degree (n) is c-stable if there
exists a series F (n;x;v ) =P∞
k=0 Φk(n;v )xk. Here Φ k(n;v ) are formal Laurent power series in v with
coeﬃcients that are integer-valued quasi-polynomials in n. We require that for all k∈N we have
lim
n→∞
v−k(n+1)
0
@v−(n)fn(v)−
kX
j=0
Φj(n;v )vj(n+1)
1
A = 0
In their paper they conjecture that c-stability holds for all Reshetikhin-Turaev knot invariants as
one scales a dominant weight.
Acknowledgement. We thank Stavros Garoufalidis for informing us about the notion ofc-stability
and the organisers of the 2018 Banﬀ workshop on Modular forms and Quantum invariants for pro-
viding the right atmosphere for writing this paper. We thank Abhijit Champanerkar for interesting
conversations about tails.

---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-086-1-introduction
section_title: "Introduction"
section_number: 1
pages: 125-127
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
Let K be a totally real number ﬁeld and let E be an elliptic curve over K with conductor N . It is
conjectured that such a curve E is modular in the following sense: there is a level N Hilbert newform
f over K of parallel weight 2 and rational Hecke eigenvalues such that L(E, s)= L(f, s), where the
L-function on the left is the Hasse–Weil L-function of E, and the L-function on the right is the Hecke
L-function of f. This modularity conjecture is the natural generalization to totally real ﬁelds of the
Shimura–Taniyama conjecture for elliptic curves over the rationals. The latter is a celebrated theorem
due to Wiles [1995] and Breuil, Conrad, Diamond and Taylor [Breuil et al. 2001]. The earliest results
towards the modularity conjecture for elliptic curves going beyond the rationals were due to Jarvis
and Manoharmayum [2008], and established modularity of semistable elliptic curves over Q(
√
2) and
Q(
√
17). In the last 10 years there has been a dramatic strengthening of modularity lifting theorems
due to, for example, Breuil and Diamond [2014], Kisin [2009], Gee [2011], and Barnet-Lamb, Gee and
Geraghty [Barnet-Lamb et al. 2012, 2013].
By the aforementioned modularity lifting theorems and by now standard modularity switching arguments
due to Wiles and to Manoharmayum [2001], a hypothetical nonmodular E/K would therefore necessarily
have small mod p image for p= 3, 5, 7 and would give rise to a K -point on one of a number of modular
curves — we make this precise later. In [Freitas et al. 2015], the real quadratic points of these modular
curves are shown to be either cuspidal, or to correspond to elliptic curves that have complex multiplication,
or rational j-invariants, or that are Q-curves. The authors deduce the following.
Theorem 1 (Freitas, Le Hung and Siksek). Elliptic curves over real quadratic ﬁelds are modular.
Derickx is supported by Simons Foundation grant 550033. Najman is supported by the QuantiXLie Centre of Excellence, a
project coﬁnanced by the Croatian Government and European Union through the European Regional Development Fund - the
Competitiveness and Cohesion Operational Programme (Grant KK.01.1.1.01.0004) and by the Croatian Science Foundation
under the project no. IP-2018-01-1313.. Siksek is supported by EPSRC LMF: L-Functions and Modular Forms Programme
Grant EP/K034383/1.
MSC2010: primary 11F80; secondary 11G05.
Keywords: modularity, elliptic curves, totally real ﬁelds.
1791
1792 Maarten Derickx, Filip Najman and Samir Siksek
Recently these modularity lifting results have been substantially strengthened in the cases p= 5 and
p= 7, respectively by Thorne [2016] and Kalyanswamy [2018]. This means that several difﬁcult steps in
the proof of Theorem 1 can now be eliminated. In this paper we build on these theorems of Thorne and
Kalyanswamy to prove the following.
Theorem 2. Let K be a totally real cubic number ﬁeld. Let E be an elliptic curve over K . Then E is
modular.
The computations in this paper were carried out in the computer algebra system Magma [Bosma et al.
1997]. The reader can ﬁnd the Magma scripts for verifying these computations in the online supplement.
We heartily thank the referee for many excellent suggestions that have improved the exposition of this
paper.
2. Images mod 3, 5, 7 and modularity
Let p≥ 3 be a prime. Write B(p) for a Borel subgroup of GL2(Fp), and Cs(p) and Cns(p) respectively
for a split and nonsplit Cartan subgroup. Let C+
s (p) and C+
ns(p) respectively be their normalizers.
The proof of Theorem 2 is based on the fact that a putative nonmodular curve must have small mod p
images for p= 3, 5 and 7 simultaneously. We now make the conditions for each prime precise.
Theorem 3. Let K be a totally real ﬁeld and E an elliptic curve over K . Suppose thatρ E,3(G K) is not
conjugate to a subgroup of B(3) or C+
s (3). Then E is modular.
Proof. By the aforementioned modularity lifting results, if ρ E,3(G K(ζ3)) is absolutely irreducible, then E
is modular; a proof is given in [Freitas et al. 2015, Theorem 3] but the arguments are well-known.
By [Rubin 1997, Proposition 6], if ρ E,3(G K(ζ3)) is absolutely reducible, then it is conjugate to a
subgroup of B(3) or C+
s (3). □
For p= 5 we use the following result due to Thorne [2016].
Theorem 4 (Thorne). Let K be a totally real ﬁeld and E an elliptic curve over K . Suppose 5 is not a
square in K , andρ E,5 is irreducible. Then E is modular.
For p= 7 we use the following result of Kalyanswamy [2018, Proposition 4.3 and Theorem 4.4].
Theorem 5 (Kalyanswamy). Let K be a totally real ﬁeld and E an elliptic curve over K . Suppose :
• K∩ Q(ζ7)= Q.
• ρ E,7 is irreducible.
• ρ E,7(G K) is not conjugate to a subgroup of C+
ns(7).
Then E is modular.
Kalyanswamy’s theorem is somewhat more precise, but we shall not need its full strength. We note
that Q(ζ7)+ is the only totally real cubic ﬁeld for which Kalyanswamy’s theorem is inapplicable. It is for
this reason that we consider elliptic curves deﬁned over that ﬁeld separately in Section 4.
Elliptic curves over totally real cubic ﬁelds are modular 1793

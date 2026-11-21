---
doc_id: ant-v14-n7-s-p04
doc_title: "Elliptic curves over totally real cubic fields are modular"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: ant-v14-n7-s-p04.pdf
source_sha256: 6abd838a4c933311
toc_source: inferred
doc_brief: "Elliptic curves over totally real cubic fields are modular — 7 sections: Front matter; Introduction; Images mod 3, 5, 7 and modularity"
---
Let K be a totally real number ﬁeld and let E be an elliptic curve over K with conductor N. It is
conjectured that such a curve E is modular in the following sense: there is a level N Hilbert newform
f over K of parallel weight 2 and rational Hecke eigenvalues such that L(E, s) = L(f, s), where the
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
have small mod p image for p = 3, 5, 7 and would give rise to a K-point on one of a number of modular
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
1792
Maarten Derickx, Filip Najman and Samir Siksek
Recently these modularity lifting results have been substantially strengthened in the cases p = 5 and
p = 7, respectively by Thorne [2016] and Kalyanswamy [2018]. This means that several difﬁcult steps in
the proof of Theorem 1 can now be eliminated. In this paper we build on these theorems of Thorne and
Kalyanswamy to prove the following.
Theorem 2. Let K be a totally real cubic number ﬁeld. Let E be an elliptic curve over K. Then E is
modular.
The computations in this paper were carried out in the computer algebra system Magma [Bosma et al.
1997]. The reader can ﬁnd the Magma scripts for verifying these computations in the online supplement.
We heartily thank the referee for many excellent suggestions that have improved the exposition of this
paper.

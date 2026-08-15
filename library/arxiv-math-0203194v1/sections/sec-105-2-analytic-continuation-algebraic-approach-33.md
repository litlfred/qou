---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-105-2-analytic-continuation-algebraic-approach-33
section_title: "ANALYTIC CONTINUATION; ALGEBRAIC APPROACH. 33"
section_number: 2
pages: 37-39
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki) — 606 sections: Analytic continuation"
---
2.6.6. The right hand side of the Gross-Koblitz formula is a special case of
an exponential sum, i.e. an expression of the form
Sr(f,g,h) =
∑
x1,... ,xd∈Fpr , h(x)⁄=0
χ
(
NFpr /Fpg(x)
)
exp
(2πi
p TrFpr /Fpf (x)
)
where h is a polynomial with coeﬃcients in Fpr , f and g are rational func-
tions with coeﬃcients in Fpr with no pole where h vanishes, and where χ is
a character of F×
p . This includes Gauss, Jacobi and Kloosterman sums as
special cases. In fact, it is known, after the classical work s of Gauss, Artin,
Weil, that counting solutions of systems of polynomial equa tions in ﬁnite
ﬁelds amounts to the computation of exponential sums Sr(
f,g,h). They
are studied via their generating series, the so-called L-series:
L(f,g,h;t) = exp
(∑
r≥1
Sr(f,g,h)tr
r
)
.
Dwork’s methods, reﬁned by P. Robba and others, allow to tack le the ques-
tions of the rationality of L, its degree, and of the functional equation relat-
ing L(f,g,h;t) to L(f,g,h; 1
prt ). In the one-dimensional case, the solution
is elementary and follows the pattern sketched in 2.6.4. Nam ely [ CR94]:
(i) One considers liftings f,g,h of f,g,h in characteristic zero, and one
introduces the aﬃnoid set S deﬁned by |h| = 1. One sets F =
g(z)1/p−1 exp(πf (z)). Then F′/F is a rational function, and one
shows that the diﬀerential operator d
dz + F′
F has an index in H†(S)
(in a slightly generalized sense, and which can be computed t hanks to
the work of Robba). This is the crucial point. Hence the cohom ology
spaces of the de Rham complex: Ω 0 = FH†(S)→ Ω 1 = FH†(S)dz
are ﬁnite-dimensional over Cp.
(ii) One observes that E :=F φ−id (i.e. E(z) = F (zp)/F (z)) is an element
ofH†(S). This allows to deﬁne two endomorphisms of the de Rham
complex by setting:
φ0(F.g) = FEg φ, φ1(Fgdz ) = FEφ′gφdz (with φ′(z) = pzp−1);
ψ0(F.g)(z) = F (z)
∑
φ(t)=z
g(t)
E(t) , ψ 1(Fgdz ) =
∑
φ(t)=z
g(t)
E(t)φ′(t).
One has ψ∗◦φ∗ =p· id. In particular, the operators H i(ψ∗), i= 0, 1,
are invertible on the cohomology spaces. The same argument a s in
2.6.4 shows that ψi is nuclear on Ω i. In particular, it has a trace.
(iii) Polynomial approximation allows to prove the trace fo rmula:
tr(ψ1)− tr(ψ0) = tr(H 1(ψ∗))− tr(H0(ψ∗)) = Sr(f,g,h).
34 I. ANALYTIC ASPECTS OF p-ADIC PERIODS.
It follows that
L(f,g,h;t) = det(id−tH1(ψ∗))
det(id−tH0(ψ∗)).
This is a rational function since the cohomology is ﬁnite-di mensional.
Moreover, since the H i(ψ∗) are invertible, the computation of its de-
gree amounts to the computation of the index of d
dz + F′
F (the com-
putation of the dimension of H 0, 0 or 1, being essentially trivial).
(iv) The functional equation follows from a topological “du al theory” in
which the transpose of φ andψ play the roles of ψ andφ respectively.
Let us remark at last that this method has an archimedean analogue in
the so-called thermodynamic formalism —in dimension one. T he analogy
is especially striking in the presentation of D. Mayer [ May91]: exponen-
tial sums correspond to “partition functions”, L to the Ruelle zeta-function,
Frobenius to the “shift”, Dwork’s operator φ∗ to the “transfer operator” (or
Ising-Perron-Frobenius-Ruelle operator) and is given by a “composition op-
erator” (loc. cit. 7.2.2), its nuclearity is established by the same argument,
and the trace formula has the same form (loc. cit. 7.17).
In view of this close analogy, one could dream of an archimede an proof
of the rationality of Weil zeta functions, parallel to Dwork ’sp-adic proof...

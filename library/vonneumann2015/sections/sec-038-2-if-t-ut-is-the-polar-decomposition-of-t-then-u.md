---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-038-2-if-t-ut-is-the-polar-decomposition-of-t-then-u
section_title: "If T = u|T| is the polar decomposition of T then u ∈M and f(|T|) ∈M for any bounded Borel function of |T|."
section_number: 2
pages: 91-94
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
for any bounded Borel function of |T|.
Proof.
1.
is obvious from the characterisation of aﬃliation given in the
proof of the previous lemma.
2. follows from uniqueness of the polar decomposition and the bicommutant
theorem.
91
92
Chapter 13
Tomita-Takesaki theory.
In chapter 9 we showed that the GNS construction on M using a faithful
normal trace produces a perfectly symmetric Hilbert space Htr with respect
to M and its commutant. This is because the map J, which is the extension
to Htr of the * operation on M, is an isometry. So x 7→JxJ is the extension
to Htr of right multiplication by x∗.
Unfortunately if we use a (normal)
non-tracial state φ the * operation is no longer an isometry and there is
no reason to expect either it or right multiplication by elements of M to
have bounded extensions to Hφ.
But as we shall see, the * operation is
actually preclosed in the sense of unbounded operators and if S = J∆1/2
is the polar decomposition of its closure S, we will show that JMJ = M ′.
Quite remarkably, the operator ∆1/2 will satisfy ∆itM∆−it = M so that
a state actually gives rise to a dynamics – a one parameter automorphism
group of M (and M ′).
We will prove these results using a method of van Daele for which we
have followed some notes of Haagerup ([],[]). But before getting started on
this diﬃcult theory it is essential to do some elementary calculations to see
how it all works out in the 2 × 2 matrices.
Exercise 13.0.4. Let M be M2(C). Show that any state φ on M is of the
form φ(x) = Trace(hx) for some positive h of trace 1. And that φ is faithful
iﬀh is invertible. Thus with respect to the right basis,
φ(x) = Trace(x

1
1+λ
0
0
λ
1+λ

)
for some λ, 0 ≤λ ≤1.
Exercise 13.0.5. With notation as in the previous exercise, suppose φ is
faithful and let S be the * operation on the GNS Hilbert space Hφ. Calculate
93
the polar decomposition S = J∆1/2 and show that SMS = JMJ = M ′.
Show that ∆zM∆−z = M for z ∈C so that σφ
z (x) = ∆zx∆−z = M deﬁnes a
representation of C as automorphisms of M which are ∗-automorphisms iﬀ
z ∈iR.
Exercise 13.0.6. Generalize the above to the n×n matrices and in fact any
ﬁnite dimensional von Neumann algebra.

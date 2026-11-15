---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-023-63-deriving-the-complex-borceabrändén-characteri
section_title: "Deriving the complex Borcea–Brändén characterization"
section_number: 6.3
pages: 25-27
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
As mentioned above, we hope to obtain the Borcea–Brändén characterization from our strong
stability characterization given in Theorem 6.2. To this end, we state two corollaries to The-
orem 6.2, which look (naively) as close to the Borcea–Brändén characterization as possible.
Let Cc denote the complement of C in CP1.
Corollary 6.9 Fix λ, α ∈Nm
0 , a linear operator T ∈Hom(V (λ), V (α)), and a Grace pair of
the form (C1 × · · · × Cm, Cc
1 × · · · × Cc
m). The following are equivalent.
(i) T preserves strong (C1 × · · · × Cm)-stability.
(ii) Symb(T ) is (Cc
1 × · · · × Cc
m) × (C1 × · · · × Cm)-stable.
Corollary 6.10 Fix λ, α ∈Nm
0 and a linear operator T ∈Hom(V (λ), V (α)). T preserves
strong stability iff Symb(T ) is (H−
m × Hm
+)-stable.
In Theorem 1.1, the analogous “if” direction of the previous corollary is paraphrased as
follows: T preserves weak stability if the Borcea–Brändén symbol of T is stable. To see how
this statement relates, we restate the deﬁnition of the Borcea–Brändén symbol:
SymbBB(T ) := T

(z + x)λ

=

μ≤λ
λ
μ

zλ−μT (xμ)
Notice that by applying z →−z and homogenizing, we obtain (up to scalar) the universal
symbol Symb(T ) deﬁned in this paper. The crucial difference then is the fact that the Borcea–
Brändén “if” direction deals only with open upper half-planes, whereas the previous corollary
requires closed half-plane stability of Symb(T ) in the ﬁrst m pairs of variables. That is, the
required premises of the “if” direction of the previous corollary are strictly stronger than that
of the Borcea–Brändén result.
These two results can be reconciled, however, which we now demonstrate. The following
result provides the main link to the Borcea–Brändén characterization, and it can be intuitively
described as follows: with the exception of having a one-dimensional range, a linear operator
which maps (C1×· · ·×Cm)-stable polynomials to weak (B1×· · ·× Bm)-stable polynomials
can only have zeros on the boundary of the set of (C1 × · · · × Cm)-stable polynomials.
1384
J. Leake
Lemma 6.11 Fix λ, α ∈Nm
0 , a linear operator T ∈Hom(V (λ), V (α)), and any open circu-
lar regions C1, . . . , Cm, B1, . . . , Bm ⊆CP1. The following are equivalent.
(i) T maps (C1×· · ·×Cm)-stable polynomials to weakly (B1×· · ·×Bm)-stable polynomials.
(ii) One of the following holds:
(a) T maps (C1 × · · · × Cm)-stable polynomials to nonzero (B1 × · · · × Bm)-stable
polynomials.
(b) T ≡p0 · ψ for some weakly (B1 × · · · × Bm)-stable polynomial p0 ∈V (α) and
some linear functional ψ.
Proof By appropriate SL2(C) action, we can assume WLOG that Ck = Bk = D, the unit
disc, for all k ∈[m].
(i) ⇒(ii). We show that if (a) is not the case, then (b) must hold. It follows from (i) that
T maps D
m-stable polynomials to (possibly identically zero) Dm-stable polynomials. So, if
(a) is not the case, we have that T (p) ≡0 for some D
m-stable polynomial p ∈V (λ).
The rest of the argument is essentially the proof of necessity found in [1] for Theorem 1.1.
Since the set of nonzero D
m-stable polynomials is open in V (λ), there is some ball B(p) ⊂
V (λ) centered at p such that B(p) contains only D
m-stable polynomials. So, T [B(p)] is an
open set in the image of T containing 0 and otherwise consisting of Dm-stable polynomials.
Therefore, the image of T is a vector space consisting of Dm-stable polynomials. Lemma
4.12 (and appropriate SL2(C) action) then implies the image of T is of dimension ≤1, and
(b) follows.
(ii) ⇒(i). If (b) holds, then (i) is immediate. Otherwise, ﬁx p ∈V (λ) such that p is
Dm-stable. For all n ∈N, deﬁne:
pn := p((1 −n−1)x1, y1, (1 −n−1)x2, y2, . . . , (1 −n−1)xm, ym)
So, pn is D
m-stable for all n, and limn→∞pn = p coefﬁcient-wise. By (ii), T (pn) is Dm-
stable for all n, and by continuity, T (p) = limn→∞T (pn). Hurwitz’s theorem then implies
T (p) is either identically zero or Dm-stable.
⊓⊔
This lemma then yields the following corollaries to Theorem 6.2. Applying the necessary
maps to convert Symb to SymbBB as discussed above, these results give precisely the Borcea–
Brändén characterization proven in Theorem 1.1 and more generally in Theorem 6.3 of [1].
In particular, Corollary 6.12 can be seen as a uniﬁcation of the complex characterization
results of [1].
Corollary 6.12 Fix λ, α ∈Nm
0 , a linear operator T ∈Hom(V (λ), V (α)), and any open
circular regions C1, . . . , Cm. The following are equivalent.
(i) T preserves weak (C1 × · · · × Cm)-stability.
(ii) One of the following holds:
(a) Symb(T ) is (C1
c × · · · × Cm
c) × (C1 × · · · × Cm)-stable.
(b) T ≡p0 · ψ for some weakly (C1 × · · · × Cm)-stable polynomial p0 ∈V (α) and
some linear functional ψ.
Proof The result follows from the Lemma 6.11 and Theorem 6.2 applied to an operator
T which maps (C1 × · · · × Cm)-stable polynomials to nonzero (C1 × · · · × Cm)-stable
polynomials.
⊓⊔
Corollary 6.13 Fix λ, α ∈Nm
0 and a linear operator T ∈Hom(V (λ), V (α)). T preserves
weak stability iff one of the following holds:
A representation theoretic explanation...
1385
(a) Symb(T ) is (Hm
−× Hm
+)-stable.
(b) T ≡p0 · ψ for some weakly stable polynomial p0 ∈V (α) and some linear functional
ψ.
Notice that our naive guess at strong stability results which emulate the Borcea–Brändén
characterization (Corollaries 6.9 and 6.10) was incorrect. We actually needed to consider
closed circular stability regions Ck, so that their complements in CP1 would be open (i.e.,
to ensure Grace pair disjointness, which is required to apply Theorem 6.2). We see this play
out in condition (ii)(a) of Corollary 6.12.

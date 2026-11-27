---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-026-113-the-type-of-the-crossed-product
section_title: "The type of the crossed product."
section_number: 11.3
pages: 76-79
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
The type of the crossed product.
We adopt the notations and conventions of the previous section. The map
Em : M ⋊α Γ →M which assigns aid to the element P
γ∈Γ is destined to play
76
a big role in the theory. It is called the conditional expectation onto M and
obviously satisﬁes the following contitions:
(i) E2
M = EM.
(ii) EM(x)∗= EM(x∗), EM(1) = 1, EM(x∗x) = 0iffx = 0.
(iii) EM(x∗x) ≥EM(x∗)EM(x), ||E(x)|| ≤||x||.
(iv) EM(axb) = aEM(x)b for a, b ∈M.
(v) EM is ultraweakly continuous.
So EM is a projection of norm one in the Banach space sense.
The
condition (iv) says that EM is an M −M-bimodule map.
Theorem 11.3.1. If Γ acts non-transitively, freely and ergodically, preserv-
ing the ﬁnite measure µ then L∞(X, µ) ⋊Γ is a II1 factor. If Γ preserves the
inﬁnite σ-ﬁnite measure µ then L∞(X, µ) ⋊Γ is a II∞factor unless Γ acts
transitively in which case L∞(X, µ) ⋊Γ is type I.
Proof. (i) It is clearer to prove a more general statement (in the case where
Γ preserves µ and µ(X) = 1). So suppose Γ preserves the faithful positive
ultraweakly continuous trace tr on the von Neumann algebra A and that its
action is free and ergodic. Then we claim M = A ⋊Γ is a type II1 factor
(or a ﬁnite dimensional factor). By previous results we need only show that
it has an ultraweakly continous positive trace. So deﬁne Tr = tr ◦EA on
M. Ultraweak continuity and positivity are obvious so by continuity and
linearity it suﬃces to prove Tr(auγbuη) = Tr(buηauγ). For either side of
the equation to be non-zero means η = γ−1 amd then the left hand side is
tr(aαγ(b)) = tr(α−1
γ (aαγ(b))) = tr(bα−1(a)) which is equal to Tr(buηauγ).
(ii) If µ is inﬁnite and Γ does not act transitively then there are no
atoms hence there are subsets Y of X of arbitrary positive measure. Let
Y have ﬁnite non-zero measure and let ξ be the function ξ(γ) = δγ,id χY .
Then ⟨auγξ, ξ⟩= ωξ(auγ) = δid,γ
R
Y a(x)dµ(x).
One easily checks that
ωξ((pauγp)(pbuηp)) = ωξ((pbuηp)(pauγp)) so by 3.4.6 ωξ deﬁnes a positive
ultraweakly continuous trace on p(A ⋊Γ)p which is a type II1 factor. But
A ⋊Γ is not itself a type II1 factor since A contains an inﬁnite family of
equivalent mutually orthogonal projections. By 9.1.8 we are done.
(iii) If Γ acts transitively then (X, µ) = (Γ, counting measure) and the
characteristic function of a set with one element is a minimal projection in
L∞(X, µ) ⋊Γ.
Exercise 11.3.2. If Γ acts ergodically on (X, µ) preserving the σ-ﬁnite mea-
sure µ then any other invariant equivalent measure is proportional to µ.
We now want to show that there are factors that are neither of type I nor
type II. Suppose that M = L∞(X, µ)⋊Γ is a type I or II factor. Then it has
77
a trace tr : M+ →[0, ∞]. We would like to deﬁne an invariant measure on X,
absolutely continous with respect to µ, by reversing the procedure of theorem
11.3.1 and deﬁning the measure σ(A) to be tr(ξA) (ξA ∈L∞(X, µ) ⊆M).
Invariance of the measure σ is no problem. The snag is that tr(χA) could be
inﬁnite for every non-null set A. We will show that this is not the case. To
this end the concept of lower semicontinuity will be useful.
Deﬁnition 11.3.3. If X is a topological space we say that f : X →R is
lower semicontinous if for every x ∈X and ϵ > 0 there is an open set U ⊆X
such that f(u) > f(x) −ϵ for all u ∈U.
Exercise 11.3.4. Prove that if f is lower semicontinous then
(a)f −1((−∞, K])) is closed for every K ∈R.
(b)f attains its minimum on any compact subset of X.
Exercise 11.3.5. If H is a Hilbert space and ξ ∈H, the function a 7→||aξ||
from B(H) to R is weakly lower semicontinuous.
Exercise 11.3.6. If fα are lower semicontinous then ∨αfα is lower semi-
continous if it exists.
Lemma 11.3.7. Let M be a type I or II factor and tr : M + →[0, ∞] be
Trace in type I, as in 9.1.9 in type II∞and the trace in type II1. Then for
each K ≥0, M1,K = {x : tr(x∗x) ≤K} is weakly compact.
Proof. Clear in the II1 case. In a decomposition M ∼= N ⊗B(ℓ2(N)) on H
with N a type II1 factor or C we may assume by 10.2.5 that there is a vector
ξ ∈e11H with ωξ a trace on e11Me11. So if ξi = ei1ξ we have, up to a scalar,
that
tr(x) =
∞
X
i=1
⟨xξi, ξi⟩.
By the previous exercises and weak compactness of the unit ball, we are
done.
Proposition 11.3.8. With notation as above, for x ∈M1,K let W(x) be the
weak closure of the convex set of ﬁnite sums {P
i λiuixu∗
i : P
i λi = 1, λi >
0, ui unitary in L∞(X, µ)}. Then W(x) ⊆M1,K and if φ(y) = tr(y∗y) for
y ∈W(x) then φ attains its minimum at a unique point E(x) of W(x).
Proof. Note ﬁrst that {z ∈M : tr(z∗z) < ∞} is a vector space on which
||z|| = tr(z∗z) deﬁnes a prehilbert space structure. (Since (a + b)∗(a + b) ≤
2(a∗a+b∗b) as operators, and the parallelogram identity passes to the poten-
tially inﬁnite sum deﬁning tr.) Moreover W(x) is a weakly compact subset
of M so by lower semicontinuity φ attains its minimum at a point which is
unique by two dimensional Euclidean geometry as in 2.1.2.
78
Proposition 11.3.9. Suppose that M = L∞(X, µ)⋊Γ is a type I or II factor
for a free ergodic action of Γ on L∞(X, µ). Let tr be as above and p be a
projection in M with tr(p) < ∞. Then
E(p) = EL∞(X,µ)(p)
and 0 < tr(E(p)2) ≤tr(p).
Proof. Let E = EL∞(X,µ). By the uniqueness of E(p) it commutes with every
unitary in L∞so it is in L∞by 11.2.11. On the other hand E(y) = E(p)
for all y ∈W(p) by the bimodule linearity of the conditional expectation
and its ultraweak continuity. So E(E(p)) = E(p) = E(p). But φ(E(p) ≤
φ(p) = tr(p)∞.
Finally E(p) = E(p2) which is a positive non-zero self-
adjoint operator and hence has non-zero trace.
Theorem 11.3.10. Let Γ act freely and ergodically on the countably sepa-
rated σ-ﬁnite measure space (X, µ) so that there is no σ-ﬁnite Γ-invariant
measure on X absolutely continuous with respect to µ. Then L∞(X, µ) ⋊Γ
is a factor not of type I or II.
Proof. If the crossed product were of type I or II, deﬁne the measure ρ on
X by ρ(A) = tr(χA). By the previous result ρ(A) would have to be ﬁnite
and non-zero for some A since the L∞functionf = E(p)2 must dominate a
multiple of χA for some A (e.g. let A be those x with f(x) suﬃciently close
to ||f||). But then by ergodicity X = ∪γ∈Γγ(A) (up to null sets) so that ρ
is σ-ﬁnite. It is automatically absolutely continuous wrt µ. Invariance of ρ
under Γ follows from tr(uγxu−1
γ ) = tr(x) for x ≥0.
Deﬁnition 11.3.11. A factor not of type I or II is called a type III factor.
Example 11.2.22 provides a type III factor since the subgroup Q acts
ergodically so the only possible invariant measure is a multiple of dx by
exercise 11.3.2 and this is not invariant under multiplication!
Note that the above technique works in somewhat greater generality than
actions of groups on measure spaces.
Exercise 11.3.12. Adapt the proofs of the results just obtained to show that
M ⋊α Z is a type III factor if the action α is generated by a single automor-
phism of the II∞factor scaling the trace by a factor λ̸ = 1.

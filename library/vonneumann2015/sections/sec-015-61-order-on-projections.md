---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-015-61-order-on-projections
section_title: "Order on projections"
section_number: 6.1
pages: 35-40
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Order on projections
Deﬁnition 6.1.1. If p and q are projections in a von Neumann algebra M
we say that p ⪯q if there is a partial isometry u ∈M with uu∗= p and
u∗u ≤q. We say that p and q are equivalent, p ≈q if there is a partial
isometry u ∈M with uu∗= p and u∗u = q.
Observe that ≈is an equivalence relation.
Theorem 6.1.2. The relation ⪯is a partial order on the equivalence classes
of projections in a von Neumann algebra.
Proof. Transitivity follows by composing partial isometries. The issue is to
show that e ⪯f and f ⪯e imply e ≈f. Compare this situation with sets
and their cardinalities.
Let u and v satisfy uu∗= e, u∗u ≤f and vv∗= f, v∗v ≤e. Note the
picture:
We deﬁne the two decreasing sequences of projections e0 = e, en+1 =
v∗fnv and f0 = f, fn+1 = u∗enu. The decreasing property follows by induc-
tion since p →v∗pv gives an order preserving map from projections in M less
than f to projections in M less than e and similarly interchanging the roles of
e and f, v and u. Let e∞=
∞
^
i=0
ei and f∞=
∞
^
i=0
fi. Note that v∗f∞v = e∞and
f∞vv∗f∞= f∞so that e∞≈f∞. Also e = (e −e1) + (e1 −e2) + · · · + e∞and
f = (f −f0)+(f1−f2)+· · ·+f∞are sums of mutually orthogonal projections.
But for each even i, u∗(ei −ei+1)u = fi+1 −fi+2 so ei −ei+1 ≈fi+1 −fi+2, and
35
v∗(fi −fi+1)v = ei+1 −ei+2 so one may add up, in the strong topology, all
the relevant partial isometries to obtain an equivalence between e and f.
Note that if we had been dealing with vN(Γ) this argument would have
been unnecessary as we could have used the trace:
tr(v∗v) ≤tr(e) = tr(uu∗) = tr(u∗u) ≤tr(f) = tr(vv∗) = tr(v∗v)
so that tr(e −v∗v) = 0 which implies e = v∗v. However in general it is
certainly possible to get a projection equivalent to a proper subprojection of
itself. Just take the unilateral shift on B(ℓ2(N)) which exhibits an equivalence
between 1 and the projection onto the orthogonal complement of the ﬁrst
basis vector. This is analogous to the notion of an inﬁnite set—one which is
in bijection with a proper subset of itself.
Deﬁnition 6.1.3. A projection p in a von Neumann algebra M is called
inﬁnite if p ≈q for some q < p, p̸ = q. Otherwise p is called ﬁnite. A von
Neumann algebra is called ﬁnite if its identity is ﬁnite, and it is called purely
inﬁnite if it has no ﬁnite projections other than 0. A factor is called inﬁnite
if its identity is inﬁnite.
We will show that purely inﬁnite von Neumann algebras exist though it
will not be easy.
Remark 6.1.4. If dim H = ∞then B(H) is inﬁnite.
Remark 6.1.5. A factor with a trace like vN(Γ) is ﬁnite.
Remark 6.1.6. Every projection in a ﬁnite von Neumann algebra is ﬁnite.
Or, more strongly, if p ≤q and q is ﬁnite then p is ﬁnite.
For if p ≈p′,
p′ < p,
p̸ = p′ then p + (q −p) ≈p′ + (q −p)̸ = q.
Remark 6.1.7. If M is any von Neumann algebra, 1 is an inﬁnite projection
in M ⊗B(H) if dim H = ∞.
Theorem 6.1.8. If M is a factor and p, q are projections in M, either p ⪯q
or q ⪯p.
Proof. Consider the family of partial isometries u with uu∗≤p, u∗u ≤q.
This set is partially ordered by u ≤v if u∗u ≤v∗v and v = u on the initial
domain u∗uH of u. This partially ordered set satisﬁes the requirements for
Zorn’s lemma so let u be a maximal element in it. If u∗u = q or uu∗= p we
are done so suppose q −u∗u and p −uu∗are both non-zero. Then by 4.1.1
there is a v̸ = 0 with v∗v ≤q −u∗u and vv∗≤p −uu∗. But then u + v is
larger than u which was supposed maximal.
36
Exercise 6.1.9. Show that two equivalent projections p and q in a ﬁnite
factor M are unitarily equivalent, i.e. there is a unitary u ∈M with upu∗=
q.
We see that the equivalence classes of projections in a factor form a totally
ordered set. It is known that, on a separable Hilbert space, the possible
isomorphism types for this set are:
1)
{0, 1, 2, ..., n} where n = ∞is allowed.
“type In”
2)
[0, 1]
“type II1”
3)
[0, ∞]
“type II∞”
4)
{0, ∞}
“type III”
Strictly speaking this is nonsense as type III is the same as type I1 and
II1 is the same as II∞. We mean not only the order type but whether 1 is
inﬁnite or not.
Observe that the type II1 case certainly exists. We saw that vN(F2) has
projections of any trace between 0 and 1. By the previous theorem it is clear
that the trace gives an isomorphism between the ordered set of equivalence
classes of projections and the unit interval.
We will proceed to prove a
statement generalising this considerably.
Deﬁnition 6.1.10. A type II1 factor is an inﬁnite dimensional factor M on
H admitting a non-zero linear function tr : M →C satisfying
(i) tr(ab) = tr(ba)
(ii) tr(a∗a) ≥0
(iii) tr is ultraweakly continuous.
The trace is said to be normalised if tr(1) = 1.
Deﬁnition 6.1.11. In general a linear functional φ on a *-algebra A is called
positive if φ(a∗a) ≥0 (and φ(a∗) = φ(a) though this is redundant if A is a
C∗-algebra), and faithful if φ(a∗a) = 0 ⇒a = 0. A positive φ is called a
state if 1 ∈A and φ(1) = 1. A linear functional φ is called tracial (or a
trace) if φ(ab) = φ(ba).
It is our job now to show that a II1 factor has a unique ultraweakly
continuous tracial state, which is faithful. First a preliminary result on ideals.
Theorem 6.1.12. Let M be an ultraweakly closed left ideal in a von Neu-
mann algebra M.
Then there is a unique projection e ∈M such that
M = Me. If M is 2-sided, e is in Z(M).
Proof. M ∩M∗is an ultraweakly closed *-subalgebra so it has a largest
projection e. Since e ∈M, Me ⊆M. On the other hand if x ∈M let
37
x = u|x| be its polar decomposition. Since u∗x = |x|, |x| ∈M ∩M∗. Hence
|x|e = |x| and x = u|x| = u|x|e ∈Me. So M = Me.
Uniqueness follows easily since f = xe ⇒f ≤e.
Moreover if M is 2-sided, for any unitary u ∈M, uM = M = uMu∗=
Me = Mueu∗so ueu∗= e by uniqueness. Hence e ∈Z(M).
Corollary 6.1.13. An ultraweakly continuous positive non-zero trace Tr on
a II1 factor is faithful.
Proof. Let M = {x ∈M : Tr(x∗x) = 0}. Then since x∗a∗ax ≤||a||2x∗x, M
is a left ideal and since Tr(ab) = Tr(ba), M is a 2-sided ideal. Moreover by
the Cauchy Schwarz inequality Tr(x∗x) = 0 iﬀTr(xy) = 0
∀y ∈M. Thus
M is ultraweakly closed, being the intersection of the kernels of ultraweakly
continuous functionals. Thus M = Me for some central projection. And e
must be zero since M is a factor.
Corollary 6.1.14. If M is a type II1 factor on H and p ∈M is a non-zero
projection, pMp is a type II1 factor on pH.
Proof. This is clear—a trace on M restricts to a trace on pMp which is
non-zero by faithfulness and all the other properties are immediate. Since a
minimal projection in pMp would be minimal in M, pMp is inﬁnite dimen-
sional.
The uniqueness of tr will follow easily once we have gathered some facts
about projections in a II1 factor.
Theorem 6.1.15. There are non-zero projections in a type II1 factor of
arbitrarily small trace.
Proof. Let d = inf{tr(p) : p ∈M, p2 = p∗= p̸ = 0}. Suppose d > 0. Let
p be a projection with tr(p) −d < d. Then p is not minimal since we have
seen that M is not isomorphic to B(H). So there is a non-zero projection
q < p. But then we have tr(p −q) = tr(p) −tr(q) ≤tr(p) −d < d. This is a
contradiction. So d = 0.
Theorem 6.1.16. Let M be a type II1 factor with an ultraweakly continuous
positive non-zero trace tr. Then {tr(p) : p ∈M, p2 = p∗= p} = [0, tr(1)].
Proof. For r ∈[0, tr(1)] consider S = {p : p a projection in M and tr(p) ≤
r}. Then S is a partially ordered set and if pα is a chain in S, p = W
α pα ∈M
and p is in the strong closure of the pα so p is in S. So by Zorn, S has a
maximal element, say q. If tr(q) were less than r, then by 6.1.8, q ≺p. So
choose q′ ∼= q,
q′ < p. Applying 6.1.14 to p−q′ we ﬁnd a projection strictly
between q′ and p.
38
Corollary 6.1.17. The map tr gives an isomorphism between the totally
ordered set of equivalence classes of projections on a type II1 factor and the
interval [0, tr(1)].
Proof. By 6.1.16 it suﬃces to show that the equivalence class of a projection
is determined by its trace. This is immediate from 6.1.8.
Exercise 6.1.18. Let M be a type II1 factor. Then for each n ∈N there is
a subfactor N ⊆M with N ∼= Mn(C).
Corollary 6.1.19. Any two non-zero ultraweakly continuous normalised traces
on a type II1 factor are equal.
Proof. By the elementary facts it suﬃces to prove that two such traces Tr
and tr agree on projections. We may assume one of them, say tr, is positive.
By the previous exercise, 6.1.17, and the uniqueness of the trace on a matrix
algebra, tr and Tr are equal on projections for which tr is rational. Given
a projection for which tr(p) is irrational build an increasing sequence ei of
subprojections as follows:
Suppose we have already constructed ei with tr(ei) = Tr(ei) and tr(p) −
tr(ei) < 1/i. Then (p −ei)M(p −ei) is a type II1 factor so tr and Tr agree
on projections in it whose tr is arbitrarily close to tr(p −ei). So choose in
it a projection ei+1 between ei and p, on which tr and Tr agree and with
tr(p) −tr(ei+1) <
1
i+1. Then tr and Tr agree on W
i ei which is equal to p by
the faithfulness of tr.
We shall see that a positive trace on a type II1 factor is norm-continuous
and a self-adjoint operator is actually a norm-limit of linear combinations
of its spectral projections so in fact an apparently weaker property than
ultraweak continuity is all we used in the previous corollary—namely that
the trace of the supremum of an increasing net of projections is the supremum
of the traces.
Corollary 6.1.20. Let M be a von Neumann algebra with a positive ultra-
weakly continuous faithful normalised trace tr. Then M is a type II1 factor
iﬀTr = tr for all ultraweakly continuous normalised traces Tr.
Proof. We just have to show that Z(M) is trivial. But if it were not, choose
by faithfulness a projection p ∈Z(M) with 0 < tr(p) < 1. Deﬁne Tr(x) =
(
1
tr(p))tr(xp). Then Tr is an ultraweakly continuous normalized trace diﬀerent
from tr on 1 −p.
Exercise 6.1.21. Let a be a non-zero positive self adjoint operator. Show
that there is a bounded piecewise smooth function f : R+ →R+ such that
af(a) is a non-zero projection.
39
Exercise 6.1.22. A type II1 factor is algebraically simple. (Hint—use the
previous exercise to show that a 2-sided ideal contains a projection, then add
projections to obtain the identity.)

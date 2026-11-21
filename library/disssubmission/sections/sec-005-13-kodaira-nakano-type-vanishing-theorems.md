---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-005-13-kodaira-nakano-type-vanishing-theorems
section_title: "Kodaira-Nakano-type vanishing theorems"
section_number: 1.3
pages: 20-23
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
From theorem 1.1 one easily recovers stronger versions of the generic
vanishing theorems of Green and Lazarsfeld as follows. Let Y be a compact
connected K¨ahler manifold of dimension d whose Albanese variety Alb(Y)
is algebraic, and denote by
f : Y −→X = Alb(Y)
the Albanese morphism. To pass from coherent to constructible sheaves,
recall that every line bundle L ∈Pic0(X) admits a ﬂat connection; the
horizontal sections with respect to such a connection form a local system
corresponding to a character χ ∈Π(X) such that L ∼= Lχ ⊗C OX.
1.3. Kodaira-Nakano-type vanishing theorems
13
For a given line bundle L ∈Pic0(X), the set of all characters χ with the
above property is a torsor under the group H0(X,Ω1
X). Indeed, this follows
from the truncated exact cohomology sequence
0 −→H0(X,Ω1
X) −→H1(X,C∗) −→Pic0(X) −→0
attached to the exact sequence 0 →C∗
X →O∗
X →Ω1
X,cl →0 where Ω1
X,cl
denotes the sheaf of closed holomorphic 1-forms. On the other hand, from
the point of view of Hodge theory it is better to restrict our attention to
unitary characters χ : π1(X,0) →U(1) = {z ∈C∗| |z| = 1}, which has the
extra beneﬁt of making the passage from coherent to constructible sheaves
unique: Comparing the exponential sequences 0 →ZX →RX →U(1)X →0
and 0 →ZX →OX →O∗
X →0 one sees that the morphism
H1(X,U(1))
∼=
−→Pic0(X)
is an isomorphism, so for every line bundle L ∈Pic0(X) there is a unique
unitary character χ with L ∼= Lχ ⊗C OX. Concerning the applicability of
theorem 3.1 in this unitary context, we remark that the intersection of any
thin subset of Π(X) with the set of unitary characters is mapped via the
above isomorphism to a thin subset of Pic0(X).
In what follows, for n ∈N0 we put Xn = {x ∈X | dim(f −1(x)) = n} and
consider the number
w(Y) = min

2d −(dim(Xn)+2n) | n ∈N0, Xn̸ = ∅
	
.
Notice that w(Y) ≤d (indeed, for some n the preimage f −1(Xn) is dense
in Y so that d = dim(f −1(Xn)) = dim(Xn)+n, hence 2d −(dim(Xn)+2n)
is equal to 2d −(d + n) = d −n ≤d). Furthermore, by base change one
checks that for any local systems E of complex vector spaces on Y the
direct image
Rf∗E[2d −w(Y)]
is semi-perverse,
because for x ∈Xn(C) the ﬁbre F = f −1(x) ⊆Y satisﬁes Hi(F,E|F) = 0 for
all i > 2n. This being said, theorem 1.1 implies the following version of the
vanishing theorem given in [47, th. 2].
THEOREM 1.4. Let E be a unitary local system on Y. Then for most L
in Pic0(Y) we have
H p(Y,Ωq
Y(E ⊗C L )) = 0
if
p+q < w(Y).
Proof. The morphism f ∗: Pic0(X) −→Pic0(Y) is an isomorphism by
construction of the Albanese variety [48, p. 553], so every coherent line
bundle L ∈Pic0(Y) arises as the pull-back of some M ∈Pic0(X). As
explained above, there is a unitary character χ such that
M ∼= OX ⊗C Lχ.
14
Chapter 1 – Vanishing theorems on abelian varieties
Then L ∼= f ∗(M ) ∼= OY ⊗C f ∗(Lχ). Since all the occuring local systems
are unitary, Hodge theory says that
M
p+q=k
H p(Y,Ωq
Y(E ⊗C L )) ∼= Hk(Y,E ⊗C f ∗(Lχ)).
Putting K = Rf∗E[2d −w(Y)] we can identify the cohomology group on the
right hand side with the group Hk−2d+w(Y)(X,Kχ). Since the direct image
complex Kχ is semi-perverse, theorem 1.1 shows that for k > 2d −w(Y)
and most characters χ the above group vanishes. The theorem now follows
by an application of Serre duality.
□
For a similar result in this direction, consider for n ∈N0 the closed
analytic subsets
Xn = {x ∈X | dim(f −1(x)) ≥n}
and
Y n = f −1(Xn),
and put dn = dim(Y n) with the convention that dn = −∞for Y n = /0. Then
our vanishing theorem implies the following
THEOREM 1.5. Suppose that p + q = d −n for some n ≥1. Then for
most line bundles L ∈Pic0(Y),
H p(Y,Ωq
Y(L )) = 0
unless
d −dn ≤p,q ≤dn −n.
Proof. By Serre duality the claim is equivalent to the statement that
if p+q = d +n for some n ≥1, then H p(Y,Ωq
Y(L )) = 0 for most L unless
the Hodge types satisfy the estimates
d +n−dn ≤p,q ≤dn.
In fact it will sufﬁce to establish the upper estimate p,q ≤dn, the lower
estimate is then automatic since p+q = d +n by assumption.
The decomposition theorem for compact K¨ahler manifolds [90, th. 0.6]
says that Rf∗CY[d] ∼=
L
m Mm[−m] where each Mm is a pure Hodge module
on X of weight m + d in the sense of [89]. Furthermore, for any unitary
character χ with complex conjugate ¯χ the local system Lχ ⊕L ¯χ of rank two
has an underlying real structure and hence can be viewed as a real Hodge
module of weight zero in a natural way. So for any real Hodge module M
on X also Mχ, ¯χ = Mχ ⊕M ¯χ is a real Hodge module. This being said, by
theorem 1.1 we have
Hd+n(Y, f ∗(Lχ ⊕L ¯χ)) ∼= Hn(X,(Rf∗CY[d])χ, ¯χ) ∼= H0(X,(Mn)χ, ¯χ)
for most unitary characters χ. The formalism of Hodge modules equips the
cohomology group on the right hand side with a pure R-Hodge structure of
weight n+d compatible with the natural one on the left hand side. We are
looking for bounds on the types (p,q) in this Hodge structure.

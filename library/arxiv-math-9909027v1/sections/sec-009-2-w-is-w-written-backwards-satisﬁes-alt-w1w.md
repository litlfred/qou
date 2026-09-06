---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California"
section_id: sec-009-2-w-is-w-written-backwards-satisﬁes-alt-w1w
section_title: "(w∗ is w written backwards) satisﬁes alt( w1w∗"
section_number: 2
pages: 44-47
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
doc_brief: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California — We introduce a notion of planar algebra, the simplest exampl e of which is a vector space of tensors, closed"
---
2) =
alt(w1)alt(w2)−1, thus alt( w1w∗
2) ∈ ker µ which is the normal closure of e.
The length of w1w∗
2 can be reduced (if necessary) by eliminating consecutive
letters two at a time to obtain another word w, of even length, with ℓ(w) =
ℓ(alt w) ( ℓ = length). By the uniqueness of reduced words in a free group,
w must be a product of words of the form x e y , which map to conjugates of
e±1 in F (∆). But the last letter of x and the ﬁrst letter of y must then be
the same, and alt will send both these letters to the same free group element.
Thus in the process of reducing w1w∗
2, all occurrences of e must disappear
and alt( w1) = alt( w2).
A consequence of this observation is that, if T is a basic tensor with
φ(alt(∂T )) = 1 in Γ so that µ(alt(∂T )) is in the normal closure of {ri} in
F (∆ \{e}), then alt( ∂T ) is the normal closure of {alt(∂( ri ))} in F (∆).
Thus it suﬃces to show that, if T1 and T2 are basic tensors with alt( ∂T1) =
alt(∂T2) ∈ F (∆), then T1 = cT2 for some c in A(∅) (since for any x ∈ S(∆)
with φ|µ(alt(x)) = 1 we have shown there is a T in the planar algebra R with
alt(∂T ) = alt( x)). But this is rather easy — we may suppose without loss
of generality that no cancellation happens going from ∂T1 to alt( ∂T1) and
then use induction on ℓ(∂T2). If ℓ(∂T2) = ℓ(∂T1) then ∂T2 = ∂T1. Otherwise
there must be a sequence . . . δδ . . . in ∂T2 for some δ ∈ ∆. Connecting δ to
δ in the tangle reduces the length of ∂T2 by 2, and the remaining region is a
disc.
□
44
A.Casson has pointed out the connection between P Γ ,∆ and van Kampen
diagrams.
If e ∈ ∆, the dimension of P Γ ,∆
n is the number of ways of writing 1 ∈ Γ
as a product of elements ˜δ, δ ∈ ∆, with alternating signs. In particular,
dim(P Γ ,∆
1 ) = |∆ |2 iﬀ Γ is trivial. Since the problem of the triviality of a
group with given presentation is undecidable, we conclude t he following.
Corollary 2.7.10 The calculation of the dimension of a planar subalgebra
of P ⊗ is undecidable.
Since there are groups which are ﬁnitely generated but not ﬁn itely pre-
sented we have
Corollary 2.7.11 There are ﬁnite dimensional planar ∗-algebras which are
not ﬁnitely generated as planar algebras.
Proof. If ﬁnitely many linear combinations of basic tensors gener ated a
planar algebra, then certainly the basic tensors involved w ould also. But by
2.7.6, the group would then be ﬁnitely presented. □
Example 2.8 Spin models. We give a general planar algebra that
is not a planar algebra, although it is the planar algebras as sociated with it
that will be of most interest. In some sense it is a “square roo t” of the planar
algebra P ⊗ of §2.6.
Let V be a vector space of dimension Q with a basis indexed by “spin
states” {1, 2, . . . Q}. For each odd n let P σ
n be the subalgebra of End( V ⊗ n+1
2 )
given by End( V ⊗ n−1
2 ) ⊗ ∆ where ∆ is the subalgebra of End( V ) consisting
of linear maps diagonal with respect to the basis. For n = 0, P0 is the ﬁeld
K and for n even, P σ
n = End( V ⊗ n
2 ). Elements of P σ
n will be identiﬁed with
functions from {1, 2, . . . , Q}n to K, the value of the function on ( i1, i2, . . . , in)
being the coeﬃcient of the basic tensor i1 i2 . . . . . . im−1 im
in in−1 . . . .im+2 im+1
for n = 2m, and the coeﬃcient of i1 i2 . . . . . . im−1 im
in in−1 . . . .im+2 im
45
for n = 2m − 1. (See §2.6 for notation.) We shall make P σ into a general
planar algebra in two slightly diﬀerent ways. In both cases t he labelling set
will be P σ itself.
First planar structure on P σ. Take a tangle T in Pk(L). We will
deﬁne Φ 0(T ) ∈ P σ
k as follows.
First, shade the connected components of Bk\T (called regions) black
and white so that the region containing a neighborhood of (0, 0) is white,
and so that regions whose closures intersect (i.e. which sha re an edge) have
diﬀerent colours. In other words, regions whose boundary in duces the pos-
itive orientation of R2 are coloured white and negatively oriented ones are
black. Observe that the top and bottom of Bk consists of segments of length
one forming parts of the boundaries of regions alternately c oloured white
and black. If k is odd, the right-hand boundary of Bk can be joined with
the rightmost top and bottom segments to form part of the boun dary of a
black region. This way the boundary of Bk always has k segments attached
to black regions whose closure meets the boundary. Number th ese segments
cyclically 1, 2, . . . , k starting form the top left and going clockwise. To deﬁne
an element of P σ
k from T we must give a function Φ 0(T ) : {1, 2, . . . Q}k → K.
It is
Φ 0(T )(i1, i2, . . . ik) =
∑
σ
∏
B∈
{ labelled boxes
of T
}
σ(B)
where σ runs over all functions from the black regions of T to {1, 2, . . . , Q}
which take the value ij on the black region whose closure contains the jth
boundary segment, for all j = 1 , 2, . . . , k. Given a labeled box B of T , and
such a σ, the boundary segments of B which meet closures of black regions
are numbered 1 to kB so σ deﬁnes an element of {1, 2, . . . , Q}kB, and thus
the label of B gives a scalar σ(B) in K. As usual empty sums are zero and
empty products are 1. This completes the deﬁnition of Φ 0 and it is easily
checked that Φ 0 presents P σ as a planar algebra. The induced representation
of P(φ) gives a representation of TL with δ1 = Q, δ2 = 1. It is precisely the
representation associated with the Potts model used by Temp erley and Lieb
in [TL].
To be sure of relevance to subfactors, we now show how to adjus t these
46
parameters so that δ1 = δ2 = √Q.
Second planar structure on P σ. If T is a labeled tangle in Pk(L), we
deﬁne a tangle ˜T in Pk(φ) by “smoothing” all the boxes of ˜T , i.e. replacing
R by ↑ ↓ ↑, and shrinking all non-through-strings to semicircles nea r the top
or bottom of Bk. Put f (T ) = Q
1

---
doc_id: arxiv-0807.2679v1
doc_title: "A cabling formula for the colored Jones polynomial Roland van der Veen"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-4
source_pdf: 0807.2679v1.pdf
source_sha256: 69ef10f8e70fc6f6
doc_brief: "A cabling formula for the colored Jones polynomial Roland van der Veen — We prove an explicit cabling formula for the colored Jones po lynomial."
---
In this note we study how the unnormalized colored Jones polynomial or quan-
tum sl2 invariant of a link changes under the operation of cabling. We work
with a banded link or ribbon link L so that every component is an embedded
annulus. Given a diagram D of a banded link inside an annulus we can construct
a satellite of L by embedding D into a component Li of L. The ( r, s )-cabling
operation is the special case where we take D to be the closure of the ( r, s )-torus
braid Br
s = (σ1 · · · σs−1)r, where r ∈ Z, s ∈ N. To turn Br
s into a banded tangle
we use the blackboard framing and add a positive curl to every over passing arc,
see ﬁgure 1 below. The banded link obtained by ( r, s )-cabling the component Li
of a banded link L will be denoted by Lr
i;s, we will also call it the ( i; r, s )-cabling
of L.
In order to state our cabling formula we need to introduce the follow ing
generalizations of the trinomial (not multinomial) coeﬃcients deﬁned in [1].
For a vector N = ( n0, . . . , n g−1) deﬁne
( g
w
)
N to be the coeﬃcient of xw in the
expansion of the product ∏ g−1
k=0(x
Nk − 1
2 + x
Nk − 1
2 −1 + . . . + x− Nk − 1
2 ).
Theorem 1. Let g = gcd(r, s ), p = s/g and N = (N0, · · · , N g−1). The unnor-
malized colored Jones polynomial of the (i; r, s )-cabling of a banded link L with
c components can be expressed as follows: JM1,...,M i− 1, N,...,M c(Lr
i;s)(q) =
|N|− g
2∑
w=− |N|− g
2
( g
w
)
N
q
rw(wp+1)
g JM1,...,M i− 1, 2wp+1,...,M c (L)(q)
1
Figure 1: We have drawn the link L4
1;3, the (1; 3 , 4)-cabling of L = ( L1, L 2),
where L1 is the ﬁgure eight knot and L2 is an unknot. We have indicated the
torus braid B4
3 and the opened tangle T1;3 mentioned in section 2.
In the statement of the theorem we have used the notation |N| = N0+. . . +Ng−1
and the convention that JM1,...,M i− 1, −j,...,M c(L)(q) = −JM1,...,M i− 1,j,...,M c(L)(q).
In the case where g = 1 and L is the unknot the above cabling formula agrees
with Morton’s formula for the ( r, s )-torus knot [14], where his variables are
related to ours as s2 = q, m = r, p = s. The case of a ( r, 2)-cabling is also
known [20]. In all other cases our formula seems to be new.
Our main motivation for proving such a formula is to verify the volume
conjecture [10],[16] in the cases where cabling is involved. The volume c onjecture
states that the normalized colored Jones polynomial J ′(L) of a link L determines
the simplicial volume of the link complement as follows:
lim
N →∞
2π
N |J ′
N,N,...,N (L)(e
2πi
N )| = Vol(S3 − L)
As an immediate corollary to our cabling formula we will ﬁnd a proof of th e
volume conjecture for all knots and links whose complement has zer o simplicial
volume. This is because it is shown in [5] that all such links can be obtain ed
from the unknot by repeated cabling and connected sum. Using the cabling
formula we can therefore in principle write down the colored Jones po lynomial
of any such link. A simple estimate is enough to prove that there cann ot be
exponential growth, see also section 3.
2
Corollary 1. The volume conjecture is true for all zero volume knots and li nks.
So far the only zero volume and links for which the volume conjecture has been
proven are the torus knots [11] and the (2 , s )-torus links [20], [7].
The cabling formula of Theorem 1 makes it possible to conduct a detaile d
study of cabled knots and iterated cabling. In the context of the v olume con-
jecture some natural questions would be the following:
Question 1. Is the volume conjecture stable under cabling?
Since cabling does not contribute to the simplical volume this would mea n that
the existing exponential growth is unchanged under cabling.
Question 2. What is the exact asymptotic expansion for a zero volume link ?
In [11] and [2] explicit asymptotic expansions are given in the case tor us knots
at the N -th root of unity. Away from the root of unity the asymptotics of t orus
knots has also been studied in the context of the generalized volume conjecture
[15]. It would be especially interesting to see whether the polynomial g rowth
related to the roots of the Alexander polynomial predicted and stu died in [8]
persists.
Question 3. How is the colored Jones polynomial of a zero volume link rela ted
to q-series identities?
In the case of torus knots and and some special torus links K. Hikam i has shown
many interesting relations between colored Jones polynomials, modu lar forms
and q-series [6], [7].
Question 4. What is the behavior of the non-commutative A-polynomial of a
knot under cabling?
It is known [4] that the colored Jones polynomial satisﬁes a linear rec ursion
relation. This relation can be encoded in a two variable polynomial with q -
coeﬃcients called the non-commutative A-polynomial and it is conjec tured [3]
to be related to the character variety of the knot group. The kno t group be-
haves well under cabling and according to our cabling formula so does the colored
Jones polynomial. It would be interesting to see how these two relate . As before
the zero volume knots provide many cases where explicit computatio ns can be
made. So far these have only been done for torus knots [6].
An investigation of these questions will be postponed to a subseque nt publica-
tion.
Acknowledgment I would like to thank the organizers of the International
Conference on Quantum topology 2007 in Hanoi for providing the at mosphere
that got this paper started and Stavros Garoufalidis and Hitoshi M urakami for
stimulating conversations.
3

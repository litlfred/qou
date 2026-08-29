---
doc_id: arxiv-2601.07042v1
doc_title: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE"
section_id: sec-013-34-reduction-to-newton-centralizers
section_title: "Reduction to Newton centralizers"
section_number: 3.4
pages: 20-22
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
doc_brief: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE — We construct, for ap-adic fieldF, an explicit semisimple Tannakian categoryRigIsoc F whose category of fiber functors recovers Kaletha’s Galois"
---
Lemma 3.4.The categoryRigIsoc F is semisimple.
Proof.We work with the category ReppE Kalqinstead, which we showed in §2.7 can be identified with
RigIsocF . By [DM82, Proposition 2.23], it suffices to show thatE Kal is pro-reductive (in this proof by
“reductive” we mean that the connected component of the identity is reductive). This follows from the fact
that it can be written as a projective limit of groups of the form
1Ñr ResE{Fpµnq
µn
spFqÑE E{F,nÑΓ KE{F Ñ1,
whereKE{E{Fare finite Galois extensions, cf. [Kal16a, §3.1], which are all finite.□
The previous lemma implies that, in order to construct all objects inRigIsoc F , the important task is to
construct its simple objects. To facilitate this, we recall some standard facts about twisted Levi subgroups
ofGLn.
Recall that for a reductive groupGdefined overF, a subgroupMĂGis a twisted Levi subgroup if it is
defined overFandM F ĂG F is a Levi subgroup. We say that a twisted LeviMĂGsubgroup iselliptic
if theF-split rank ofZpMqequals that ofZpGq. We denote the maximal split sub-torus ofZpMqbyA M.
Suppose thatMĂGis a non-elliptic twisted Levi subgroup. ThenL“Z GpAMqis a proper Levi subgroup
ofGcontainingM. In particular, the elliptic twisted Levi subgroups ofGare precisely those that are not
contained in a proper Levi subgroup.
Lemma 3.5.The twisted Levi subgroups ofGL n overFare isomorphic to
kź
i“1
ResEi{F GLni,
whereEi{Fis a field extension of degreem i and
kř
i“1
mini“n.
Proof.This statement is well-known. See the proof given in [FS25, Lemma 4.3.4]□
Suppose thatXPobjpRigIsoc Fq, which maps via (2) to an algebraic1-cocyclez X :E KalÑGL n with
νX the associated algebraic homomorphism of the band.
2We warn the reader that the first functor is not a tensor functor, but when composed with the second functor it is.
20
Lemma 3.6.We continue withG“GL n. One can conjugatez X byGpFqsuch thatν X has trivial Galois
action (i.e., it gives anF-rational homomorphismuÑGL n).
Proof.We first argue that for all twisted Levis subgroupsM, the map
H1pF,NGpMqqÑH 1pF,NGpMq{Mq
is surjective. Note that forMa maximal torus, this surjectivity is a corollary of Raghunathan’s theorem.
ForG“GL n we can prove the result for a general twisted Levi. First, we assumeMis a Levi subgroup,
and thenN GpMq ÑN GpMq{Mhas a naturalΓ F{F -equivariant splitting coming from the permutation
matrices. This implies the surjectivity forM, and then we prove the general case by twisting.
LetM“Z GpνXq. SinceG“GL n, we have thatMis a twisted Levi ofG E, whereEis the field
of definition ofν X. Notice that the action onz X by coboundaries induces a conjugation action onν X and
henceM. The groupMmight not beΓ F{F -invariant, but sinceG“GL n is split, every Levi subgroup over
Fis conjugate to the base-change of anF-rational Levi subgroup and we can thus conjugateν X (and twist
zX by the corresponding coboundary) such thatMis the base-change to Fof such a subgroupLofG.
Thus we may as well assumeM“L F isΓF{F -stable. Now,zX gives a cocycle inZ 1pF,NGpLq{Lqvia
the function
σÞÑ¯σÞÑz Xp¯σqmodLpFq,
where¯σis any lift ofσPΓ F{F toE Kal (the cocycle is independent of the lift). By our above argument, we
may modifyzX by a coboundary such that this cocycle comes via projection from somezPZ 1pF,NGpLqq.
Now, suppose there exists somehPGp Fqsuch thathν Xh´1 isΓ F{F -fixed. Then we compute this is
equivalent toh ´1γphqz´1
γ PLp Fqfor eachγPΓ F{F . This would certainly follow if we knew thatz γ
came from a class inH 1pF,NGpLqqthat is trivial inH 1pF,Gq. But this latter group is trivial again because
G“GL n. □
From now on, we assumeνX is fixed byΓF{F .
Remark 3.7.The cohomology setH 1
algpEKal,Gqfor a connected reductive groupGis studied in detail in
[DS24], which excusively works with so-called “regular” classes, which are those arising as the image of
H1
algpEKal,Tqfor a maximal torusTofG. Lemma 3.6 implies that every class inrzsPH 1
algpEKal,GLnqis
regular, as follows: One combines [DS24, Lemma 2.8] which says, whenz| u is defined overF, we have
thatzPZ 1
baspEKal,ZGpz|uqqwith the fact ([Kal16a, Corollary 3.7]) thatH 1
algpEKal,TqÑH 1
baspEKal,Mq
is surjective for any connected reductive groupMwith elliptic maximal torusT.
Lemma 3.8.Under the assumption above, supposeMĂGL n is a minimal twisted Levi subgroup through
whichz X factors. IfXis simple, thenz X is basic inM(in other words,ν X factors throughZpMq) and
Mis elliptic. On the other hand,Xis simple if and only ifz X factors through only elliptic twisted Levi
subgroups ofGLn.
Proof.Supposez X is not basic inM. Then letM 1ĂMbe the centralizer ofν X inM. SinceG“GL n, we
claim thatM 1 is a twisted Levi subgroup ofMand henceG. Indeed,M 1 is the intersection of centralizers
of commuting semisimple elements ofGLn, each of which is a twisted Levi subgroup. Moreover,M1ĂM
is proper sinceνX is not basic. The cocyclezX factors throughM 1 sincexPE Kal liftingσPΓ F{F satisfies
IntpxqpνXq“Intpxqpσpν Xqq“ν X, henceMis not minimal.
IfXis simple, thenz X cannot factor through any non-elliptic twisted Levi subgroup, since by the above
discussion this would implyzX factors through a Levi subgroup ofGand hence is not simple.
For the second part, observe thatXis simple if and only ifz X does not factor through a proper Levi
subgroup ofGand by the discussion before Lemma 3.5, this is equivalent toz X not factoring through any
non-elliptic twisted twisted Levi subgroup.□
21

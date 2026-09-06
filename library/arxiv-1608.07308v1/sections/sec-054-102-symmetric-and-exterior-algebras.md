---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-054-102-symmetric-and-exterior-algebras
section_title: "Symmetric and exterior algebras"
section_number: 10.2
pages: 72-74
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
both associated to a vector spaceV . The ﬁrst is the symmetric algebra:
(10.5) SV =
∞⨁
d=0
SdV
concentrated in degree 0 and with trivial differential, and the exterior algebra:
(10.6) ∧V =
∞⨁
d=0
∧dV
situated in degrees ...,−2,−1, 0 and with trivial differential. By deﬁnition, the spaces (10.5)
and (10.6) are quotients of the tensor algebra ofV by the relationsv⊗v′∓v′⊗v. Therefore,
they are both particular cases of the symmetric algebra of a dg vector space:
(10.7) SV• :=
( ∞⨁
n=0
V•⊗...⊗V•
)/(
v⊗v′− (−1)(degv)(degv′)v′⊗v
)
which inherits the differential fromV•:
d(v1⊗...⊗vk) =
k∑
i=1
(−1)degv1+...+degvi−1·v1⊗...⊗vi−1⊗d(vi)⊗vi+1⊗...⊗vk
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 73
By the very deﬁnition, (10.7) is a commutative dg algebra, which is concentrated in non-
positive degrees as long as the original dg vector spaceV• is. In particular, when the dg vector
space is concentrated in degree 0 (respectively -1), we obtain (10.5) (respectively (10.6).
Example 10.3. A particularly important case of the construction (10.7) is when:
V• =
[
M
s
−→N
]
is concentrated in degrees−1 and 0. Then we have:
SV• =
[
...
ds
−→∧ 2M⊗SN
ds
−→M⊗SN
ds
−→SN
]
in degrees...,−2,−1, 0, with differential given by:
(10.8) ds(m1∧...∧mk⊗n) = (−1)k−1
k∑
i=0
m1∧...∧mi−1∧mi+1∧...∧mk⊗s(mi)n
for allm1,...,m k∈M andn∈SN .
More generally, suppose thatA is a dg algebra andM is a dg module forA. Deﬁne:
SAM• =SM•
/
(am⊗m′−m⊗am′)
which will also be a dg module forA. The formalism above, as well as Example 10.3, apply.
10.3. Afﬁne dg schemes. Dg schemes can be deﬁned as spectra of dg algebras with respect to
the ´etale topology, as detailed in [8]. We will not need the full theory, and instead follow the
original deﬁnition of Kontsevich.
Deﬁnition 10.4. IfX is an scheme with structure sheafOX, an afﬁne dg scheme supported on
X is a sheafA of dg algebras, concentrated in non-positive degrees, such thatOX =H0(A).
We will write SpecA for the afﬁne dg scheme associated toA, to match this situation with
that of usual schemes. Philosophically, the approach of Deﬁnition 10.4 can be summarized by
saying that we ignore topological subtleties of dg schemes, and simply endow them with the
topology coming fromOX. The natural deﬁnition of quasi-coherent sheaves is:
QCoh(SpecA) =A–Mod =
{
P∈ QCoh(X) endowed with a dg module structure forA
}
quasi–isomorphism
All of the dg schemes in this paper will be of ﬁnite type, meaning that A is ﬁnitely generated
overOX = H0(A). Since this is the case, it is natural to deﬁne coherent-sheaves as the full
subcategory:
A–mod = Coh(SpecA)⊂ QCoh(SpecA)
consisting of dg modules whose cohomology groups are coherent sheaves overOX =H0(A).
Example 10.5. Suppose thatA =SX[N
s
→O X] is the Koszul complex associated to a coherent
sheafN and a co-sections. Explicitly, we have:
A =
[
...
ds
−→∧ 2N
ds
−→N
ds
−→OX
]
The structure sheafOX situated in degree 0, as in Example 10.3, upgraded to the situation of
modules. If the co-sections is regular, then it is well-known that the Koszul complex is acyclic,
and the dg algebraA becomes isomorphic to the usual commutative algebraOX/s. In this case,
the dg scheme is simply the subscheme ofX cut out by the sections.
74 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
However, in general it may be that the sections is not regular (for example,s could be 0). In
this case, the dg algebraA =∧•N has 0 differential but non-trivial grading. Explicitly:
A–mod =
{
graded coherentOX ↷P• together withN⊗P • λ
→P •−1 such thatλ◦λ = 0
}
quasi–isomorphism
In particular, ifN∼=O⊕n
X is a free module, the choice of the datum λ corresponds to n com-
muting degree−1 endomorphisms ofP.
Example 10.6. In general, the afﬁne dg schemes we will encounter will combine the previous
example with the case of polynomial rings over ordinary algebras. Speciﬁcally, we will have:
A =SX[M
s
−→N ] =
[
...
ds
−→∧ 2M⊗ SXN
ds
−→M⊗ SXN
ds
−→SXN
]
whereM
s
→N is a map of coherent sheaves ofX. The differential ds is given by (10.8), and
the grading has∧iM⊗ SN sitting in degree−i. But note that there is an extra grading on the
algebraA, given by placing∧iM⊗ SjN in degreei +j. We will write this as:
A•,∗ =
⨁
i,j≥0
A−i,i+j =
⨁
i,j≥0
∧iM⊗ SjN
Since the∗ = i +j grading is preserved by the differential ds, it descends to a grading on
the cohomology groups. For example, when the morphism s is regular (i.e. when the Koszul
complexA is acyclic in negative degrees), the• grading collapses, and the∗ grading matches
the usual polynomial grading on the symmetric powerS∗
X(N/M).

---
doc_id: arxiv-2601.07042v1
doc_title: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE"
section_id: sec-011-31-the-newton-map
section_title: "The Newton map"
section_number: 3.1
pages: 17-18
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
doc_brief: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE — We construct, for ap-adic fieldF, an explicit semisimple Tannakian categoryRigIsoc F whose category of fiber functors recovers Kaletha’s Galois"
---
HomFpuF,GLpωkpXqqas follows: The groupRes Ek{FpµnkqpFqis canonically identified with the group of
automorphisms of theF-fiber functor described in the previous subsection, which we will denote byωk, and
thenfX is defined by sendingxPRes Ek{Fpµnkqto the F-linear automorphism ofω kpXqcorresponding to
x.
Lemma 3.1.The dimension ofω kpXqis ř
paσ{nkqPś
ΓEk{F
r0,1q dimLEk
pVpaσ{nkqq.
Proof.This follows immediately from the explicit description in (1) of the functorω RIk, noting that all the
internal summands in (1) are identified upon taking the quotient byIR Ek{F .□
It is straightforward to verify that the homomorphismsf X are compatible with the transition maps
RIk ÑRI l, and we thus can associate to an objectXinRigIsoc F in the image ofRI k a morphism
fXPHom FpuF,GLpωkpXqqq.
We say that an objectXofRigIsoc F isbasicif the homomorphismf X is valued inZpGLpω kpXqqq.
One can classify the basic objects as follows:
Proposition 3.2.An objectXofRigIsoc F is basic if and only if all of the indices inQrΓ F{Fsof all its
nonzero graded pieces have the same image inQ{ZrΓF{Fs.
Proof.It suffices to prove this for the finite-level Tannakian categoryRI k.
An elementx“ px σq Pś
ΓEk{F
µnkpFq “Res Ek{FpµnkqpFqacts on the fiber functor by sending
Vpaσ{nkq to itself via multiplication by ś
σxaσ
σ . This gives for each graded pieceV paσ{nkq a morphism from
uF toZpGL Vpaσ{nkqq“ F
ˆ
, and the resulting map lies inZpGLpω kpXqqqif and only if these maps agree
for allpa σ{nkqσ. This last condition holds precisely when all tuplespa σ{nkqσ withV paσ{nkq ‰0are the
same moduloś
ΓEk{F
Z.□
Denote byRigIsoc F,n the full subcategory of objects whose image under the canonical fiber functor,
temporarily denoted byω, given above (and thus any fiber functor) isn-dimensional; we can also consider
17
the full subcategoryRigIsoc F,n,basic of basic objects. Recall that ifE Kal is the gerbe of fiber functors for
RigIsocF , then we have an equivalence of categories
(2)RigIsoc F,n
„Ý ÑZ1
algpEKal,GLnq,
and we observe that this functor is compatible with the maps from both objects to HomFpuF,GLn,Fq. More
explicitly, recall from [Tai25, Proposition 7.1] that there is an equivalence of categories from the category of
pairspR,tq, whereR:E KalÑBGL n is a morphism of fibered categories overFandtis a trivialization of
Rpωq, to the categoryZ 1
algpEKal,GLnq. The claimed equivalence (2) is given by composing this equivalence
with the functor sendingXPobjpRigIsoc F,nqto the pair consisting of the functorFÞÑIsom pFpXq,ωpXqq
and the trivialization of IsompωpXq,ωpXqqinduced by our distinguished basis for the underlying vector
space ofX“pV,D,Φq.
Note that (2) induces an equivalence of categories
RigIsocF,n,basic
„Ý ÑZ1
baspEKal,GLnq.
Corollary 3.3.WhenXPobjpRigIsoc Fqis basic, the morphismf X PHom FpuF,GLpωkpXqqqdescends
to a morphism inHomFpu,GLpωkpXqqq.
This result can also be verified directly using the explicit description offX given above.

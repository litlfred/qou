---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-310-222-we-assume-thatk-is-algebraically-closed-of-c
section_title: "We assume thatK is algebraically closed of characteristic 0. Let S be"
section_number: 2.2.2
pages: 137-138
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry Yves André (with appendices by F. Kato and N. Tsuzuki) — 580 sections: INTRODUCTION; INTRODUCTI"
---
a K-manifold of dimension one, and let S be the complement of a classical
point 0 in S (so that 0 has a basis of open neighborhoods consisting in dis ks
centered at 0). As above, it follows from 2.1.12 that the restriction of any
temperate covering of S to a punctured disk around 0 of suﬃciently small
radius splits into a disjoint union of Kummer coverings of bo unded degree. If
we replace S by the its tangent space at 0 and 0 by the zero tangent vector,
the same construction yields an equivalence of categories, with an obvious
inverse given by ‘extension’. We thus get a specialization functor:
Covtemp
S → Covtemp
T 0
S, 0
.
Any geometric point ⃗t of T 0
S,0, e.g. any non-zero tangent vector at 0, then
gives rise by composition to a ﬁber functor
F temp
⃗t : Cov temp
S → Sets.
Proposition 2.2.3. This ﬁber functor is isomorphic to F temp
t for any geo-
metric point t.
Proof. We follow the line of proof of 1.3.3. We may assume that S is
aﬃnoid (hence compact). Let us consider ﬁnite open covers U = (U i)i≥1 of
S such that U 1 is a disk centered at 0 and 0 /∈U i for i> 1.
Let us denote by U = ( Ui) its trace on S, and by Cov temp
S,U the full
subcategory of Cov temp
S of temperate coveringsf :S′→S such thatf−1Ui =∐ Vij and Vij is ´ etale ﬁnite over Ui via f .
(6)for instance in the study of Galois actions on fundamental gr oups.
134 III. p-ADIC ORBIFOLDS AND MONODROMY.
The point is that by 2.1.11 (or 2.2.2) , we have Cov temp
S = lim−→
U
Covtemp
S,U ,
whereU runs among the open covers of S satisfying the above properties.
Also
Isom(F temp
⃗t ,F temp
t ) = lim←−
U
Isom(F temp
⃗t,U ,F temp
t,U )
whereF temp
⃗t,U ,F temp
t,U denote the restrictions of F temp
⃗t ,F temp
t to Cov temp
S,U .
To show that Isom(F temp
⃗t ,F temp
t )⁄=∅, we construct non-empty compact
subsets KU of Isom(F temp
⃗t,U ,F temp
t,U ) (topologized as before) such that if U′
reﬁnes U, KU ′ maps to KU under the natural map Isom( F temp
⃗t,U ′ ,F temp
t,U ′ )→
Isom(F temp
⃗t,U ,F temp
t,U ); it will follow that Isom( F temp
⃗t ,F temp
t )⊃ lim
←−UKU⁄=∅.
In fact, it suﬃces to do so for a coﬁnal system of U’s. We now use a
continuous embedding I = [0, 1]֒→
S with 0↦→0∈S, 1↦→t. We consider
open coversU = (U1,... ,U n) as above, and such that
U1∩I = 0,r 1[, ... ,Ui∩I =]ri,t i[, ... ,Um∩I =]rm, 1], Um+1∩I =∅,...
for some points ri < ti−1 < ri+1 < ti in I (i = 2,... ,m − 1) and some
m≤n.
GivenU, one chooses si inUi∩Ui+1∩I (which amounts to a real number
betweenri+1 and ti), and a geometric point si abovesi (i = 1,... ,m − 1);
one completes this collection by setting s0 =⃗t, sm =t.
Let us look at the diagram
Covtemp
S,U
σi
−→Ind Covalg
Ui+1
F alg
si,U i+1
−−−−−→
F alg
si+1,U i+1
−−−−−−−→
−→ Sets.
One has F alg
sj,Ui+1◦σi =F temp
si,U , j =i,i + 1, whence continuous maps
Isom(F alg
si,Ui+1,F alg
si+1,Ui+1)→ Isom(F temp
si,U ,F temp
si+1,U ).
But Isom(F alg
si,Ui+1,F alg
si+1,Ui+1) is a non-empty compact set for anyi = 0,... ,m :
for i = 0 ( s0 =⃗t), one uses the analogue of 2.2.3 for the category of ﬁnite
´ etale coverings, which follows from Deligne’s discussion, loc. cit (or even di-
rectly from [SGA 1 , V], interpreting F alg
⃗t,Ui+1
as a ﬁber functor at a geometric
generic point). The rest of the proof goes exactly as in 1.3.3 .

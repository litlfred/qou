---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-248-132-it-follows-from-sga-1-exp-v-that-algebraic-p
section_title: "It follows from [SGA 1 , exp. V] that algebraic paths exist. Using the"
section_number: 1.3.2
pages: 121-123
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp — 580 sections: INTRODUCTION; INTRODUCTION; INTRODUCTION"
---
nice topology of Berkovich spaces, A.J. De Jong was able to pr ove [dJ95b,
2.9]:
Key lemma 1.3.3. Etale paths exist. More precisely, any Berkovich path
γ (up to homotopy) between s and t lifts to an ´ etale path
γ betweens and t.
Proof. Up to introducing intermediate geometric points, we may ass ume
that S is aﬃnoid (hence compact). For any ﬁnite open cover U = (Ui) of
S, let us denote by Cov et
S,U the full subcategory of Cov et
S of ´ etale coverings
118 III. p-ADIC ORBIFOLDS AND MONODROMY.
f : S′→S such that f−1(Ui) = ∐ Vij and Vij is ´ etale ﬁnite over Ui via f .
We thus have
Covet
S = lim−→
U
Covet
S,U, and Isom(F et
s ,F et
t ) = lim←−
U
Isom(F et
s,U,F et
t,U )
whereF et
s,U,F et
t,U denote the restrictions of F et
s ,F et
t to Cov et
S,U .
We have to show that Isom( F et
s ,F et
t )⁄=∅. The idea is to construct non-
empty compact subsets KU of Isom(F et
s,U,F et
t,U ) (topologized as above) such
that ifU′ reﬁnesU,KU ′ maps toKU under the natural map Isom(F et
s,U ′,F et
t,U ′)→
Isom(F et
s,U,F et
t,U ); it will follow that Isom( F et
s ,F et
t )⊃ lim
←−
U
KU⁄=∅.
In fact, it suﬃces to do so for a coﬁnal system of U’s, which are chosen
as follows. Since S is arcwise connected, there is a continuous embedding
I = [0, 1]֒→S with 0 ↦→s, 1↦→t. One considers ﬁnite open coverings
U = (U1,... ,U n) such that
U1∩I = [0,r 1[, ... ,Ui∩I =]ri,t i[, ... ,Um∩I =]rm, 1], Um+1∩I =∅,...
for some points ri < ti−1 < ri+1 < ti in I (i = 2,... ,m − 1) and some
m≤n.
GivenU, one chooses si inUi∩Ui+1∩I (which amounts to a real number
betweenri+1 and ti), and a geometric point
si abovesi (i = 1,... ,m − 1);
one completes this collection of geometric points by settin g s0 =s, sm =t.
Let us look at the diagram
Covet
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
Sets.
One has F alg
sj,Ui+1◦σi =F et
si,U, j =i,i + 1, whence continuous maps
Isom(F alg
si,Ui+1,F alg
si+1,Ui+1)→ Isom(F et
si,U,F et
si+1,U ).
Since algebraic paths exist, Isom(F alg
si,Ui+1,F alg
si+1,Ui+1) is a non-empty compact
set for any i = 0,... ,m . On composing such isomorphisms for i = 0,... ,m ,
one gets a continuous map
σU ,(si) :
m∏
i=0
Isom(F alg
si,Ui+1,F alg
si+1,Ui+1)→ Isom(F et
s,U,F et
t,U )
whose image is a non-empty compact set KU .
In fact, while the map σU ,(si) depends on the choice of the geometric
points si, its image KU does not. Indeed, for any other choice s′
i, there is
an algebraic path
γi : F alg
si,Ui+1∩Ui
∼− →F alg
s′
i,Ui+1∩Ui
, γ0 = id, γm = id.
1. ´ETALE COVERINGS AND FUNDAMENTAL GROUPS. 119
We denote by the same letter the induced algebraic paths on Ui and on
Ui+1. Then σU ,(si)(α0,... ,α m) = σU ,(s′
i)(γ1α0γ−1
0 ,... ,γ mαmγ−1
m−1), whence
the independence.
From this observation, it is straightforward to conclude th at ifU′ reﬁnes
U,KU ′ maps toKU under the natural map Isom(F et
s,U ′,F et
t,U ′)→ Isom(F et
s,U,F et
t,U ).
This establishes the ﬁrst assertion.
For the second one (the surjectivity of Isom(F et
s ),F et
t )→ Isom(F top
s ,F top
t )),
one may argue as follows: let ˜s be a lifting of s to the universal topological
covering π : ˜S→ S. Then γ.¯˜s is a lifting of t to the universal topological
covering. Let α be an ´ etale path between ¯˜s and γ.¯˜s. Then γ := π∗(α) is
an ´ etale path between s and t which maps to the ordinary path γ up to
homotopy, viewed as an isomorphism F top
s →F top
t .
1.4. The formalism of fundamental groups.

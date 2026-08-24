---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-015-23-a-vanishing-theorem
section_title: "A vanishing theorem"
section_number: 2.3
pages: 32-36
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
Let L be a framed exact Lagrangian sphere in an exact symplectic ma nifold
M . According to Proposition 1.11 one can associate to it a stan dard ﬁbration
(EL,πL) over ¯D(r) for some r > 0. Each ﬁbre EL
z , z ⁄= 0, contains a dis-
tinguished Lagrangian sphere Σ L
z , described by Lemma 1.12(i); for z = r, the
isomorphism φL : EL
r → M takes Σ L
r to L. Deﬁne the standard Lagrangian
boundary condition for ( EL,πL) to be
QL = ⋃
z∈∂ ¯D(r) Σ L
z,
κQL =dc(− 1
4|z|)|∂ ¯D(r), K QL = 0.
(2.16)
This is indeed a Lagrangian boundary condition, as one can se e from (1.20). Our
aim here is to prove the following result about the invariant Φ 1(EL,πL,QL)∈
H∗(Σ L
r ; Z/2)∼=H∗(L; Z/2):
Proposition 2.13. Φ 1(EL,πL,QL) = 0 for all M and L.
The ﬁrst part of the proof is a degeneration argument, in whic h one restricts
the base to successively smaller discs. For 0 <s ≤r setQL,s = ⋃
z∈∂ ¯D(s) Σ L
z ; to-
gether withκQL,s andKQL,s as before, it is a Lagrangian boundary condition for
(EL,s,πL,s) = (EL,πL)| ¯D(s). This constitutes a deformation of ( EL,πL,QL)
in a suitable sense; which means that if one identiﬁes Σ L
r with Σ L
s using parallel
transport along [s;r], then
Φ 1(EL,πL,QL) = Φ 1(EL,s,πL,s,QL,s) (2.17)
for all s. Now ﬁx some J ∈ Jh(EL,πL,j ), where j is the standard complex
structure on ¯D(r). Let ML,s be the space of sections ¯D(s)→ EL,s which are
32
holomorphic with respect to j| ¯D(s) and J|EL,s, and have boundary in QL,s. As
s→ 0, QL,s shrinks to the single critical point Σ L
0 ={x0} of πL, and we would
like to apply a compactness argument to elements of ML,s in the limit. This
looks a bit unpleasant as it stands, but one can modify the sit uation to make the
degeneration of the QL,s less singular, and then standard Gromov compactness
is suﬃcient.
Lemma 2.14. For some 0<r ′≤r, there is a compact almost complex mani-
fold with corners ( ˆEL, ˆJ), together with pseudo-holomorphic maps
ˆEL
ηL
/d47/d47
ˆπL
/d15/d15
EL
πL
/d15/d15
¯D(r′)× ¯D(1)
m /d47/d47 ¯D(r)
where m(w,z ) = wz is multiplication, such that the following properties are
satisﬁed.
(i) Away from ZL = (ηL)−1(x0)∩(ˆπL)−1(0, 0), the map ηL identiﬁes ( ˆEL, ˆπL)
with the pullback of (EL,πL) by m. In particular, restricting to any w =
s> 0 gives a pseudo-holomorphic diﬀeomorphism
ˆEL,s = (ˆπL)−1({s}× ¯D(1))−→EL,s.
(ii) ˆEL carries a symplectic form ˆΩ L which tames its almost complex structure,
and which is of the form
ˆΩ L = (ηL)∗Ω L + (ˆπL)∗(i
2dw∧d ¯w + i
2dz∧d¯z +dγ) +δ,
with γ = 1
4 im((r′−w)¯zdz ), and where δ is supported in a small neigh-
bourhood of ZL.
(iii) ( ˆEL, ˆΩ L) contains a Lagrangian submanifold with boundary ˆQL which
projects to [0;r′]×S1⊂ ¯D(r′)× ¯D(1) and satisﬁes
ηL( ˆQL∩ (ˆπL)−1({s}× S1)) =
{
QL,s s> 0,
{x0} s = 0.
It is convenient to begin with the local model for the constru ction. Choose
some r′ > 0 and set
E ={x∈ Cn+1 : ||x||≤ 2
√
r′,|q(x)|≤ r′}, Ω = ωCn+1|E,
π =q :E−→ ¯D(r′), Q = ⋃
z∈∂ ¯D(r′) Σ z
(2.18)
where q is our standard quadratic function, and Σ z is as in (1.11). In parallel
with the reasoning above, one can also introduce ( Es,πs) = ( E,π )| ¯D(s) and
33
Qs = ⋃
z∈∂ ¯D(s) Σ z for s∈ (0;r′]. Take the pullback of ( E,π ) by the multiplica-
tion map, m∗E ={(w,z,x )∈ ¯D(r′)× ¯D(1)×E : q(x) = wz}⊂ Cn+3. This
has one singular point (0 , 0, 0), which can be resolved by blowing it up inside
Cn+3 and taking the proper transform of m∗E. The outcome, which we denote
by ˆE, comes with maps
ˆE
η /d47/d47
ˆπ
/d15/d15
E
π
/d15/d15
¯D(r′)× ¯D(1)
m /d47/d47 ¯D(r′).
(i’) η is a pullback map away from Z =η−1(0)∩ ˆπ−1(0, 0).
That is obvious from the deﬁnition. Consider the two-form
Ω + i
2dw∧d ¯w + i
2dz∧d¯z +dγ =ωCn+3 +dγ (2.19)
on ¯D(r′)× ¯D(1)×E, where γ is as in Lemma 2.14(ii). We claim that this is
symplectic and tames the obvious complex structure. All one needs to verify is
that (dγ)(·,i·) is nonnegative, which one can do by decomposing dγ = (dγ)1,1 +
(dγ)0,2 + (dγ)2,0; then (dγ)1,1 = re(r′−w)i
4dz∧d¯z is nonnegative since re( r′−
w)≥ 0, while (dγ)0,2(·,i·) vanishes because it is a two-form of type (0 , 2), and
similarly for (dγ)2,0. Now pull back (2.19) to the blowup, make it symplectic by
adding a two-form δ supported near the exceptional divisor, and restrict that
to ˆE. The outcome is:
(ii’) There is a symplectic form ˆΩ on ˆE which tames the complex structure,
and which is of the form η∗Ω + (ˆπ)∗(i
2dw∧d ¯w + i
2dz∧d¯z +dγ) +δ, with
δ supported in a small neighbourhood of Z.
The subset
{(w,z,x ) : w∈ [0;r′],|z| = 1, x∈ Σ wz}⊂ m∗E (2.20)
is a submanifold, since it is the image of the embedding S1×Z/2 ¯Bn+1(1)→
Cn+3, (z,y )↦→(|y|2,z 2,zy ). It is also Lagrangian with respect to (2.19); which is
in fact the reason for our choice of symplectic form. Deﬁne ˆQ to be the preimage
of (2.20) in ˆE; provided that the support of δ has been chosen suﬃciently small,
this is again a Lagrangian submanifold. By construction one has
(iii’) ˆπ( ˆQ) = [0;r]×S1, and
η( ˆQ∩ ˆπ−1({s}× S1)) =
{
Qs s> 0,
{0} s = 0.
34
Proof of Lemma 2.14. Take a holomorphic Morse chart ( ξ, Ξ) around x0∈EL
0
as provided by Lemma 1.12(ii). After restricting the domain s, we may assume
that ξ is the inclusion ¯D(r′)֒→¯D(r) for some 0 < r′≤ r, that Ξ is deﬁned
on the set E⊂ Cn+1 from (2.18), and that QL,s = Ξ( Qs) for all 0 < s≤ r′.
Construct a diagram
ˆE
/d15/d15
/d47/d47
ηL
/d42/d42m∗E
m∗Ξ
/d15/d15
/d47/d47E
Ξ
/d15/d15
ˆEL
ˆπL
/d37/d37/d75/d75/d75/d75/d75/d75/d75/d75/d75/d75 /d47/d47m∗EL /d47/d47
/d15/d15
EL,r′
πL,r ′
/d15/d15
¯D(r′)× ¯D(1)
m /d47/d47 ¯D(r′)
as follows: pull back EL by multiplication m; the map m∗Ξ induced by Ξ
identiﬁes neighbourhoods of the singular points (0 , 0, 0)∈m∗E and (0, 0,x 0)∈
m∗EL; which means that there is a resolution
ˆEL−→m∗EL
modelled locally on ˆE→m∗E. The given almost complex structure J induces
one on m∗E, for which m∗Ξ is holomorphic; this and the complex structure on
ˆE deﬁne the almost complex structure ˆJ. Part (i) of the lemma now follows
from the corresponding statement (i’) in the local model. Ne xt, take the two-
form Ω L + i
2dw∧d ¯w + i
2dz∧d¯z +dγ onm∗EL; due to the nonnegative curvature
of standard ﬁbrations, see Lemma 1.12(iii), and to the fact t hatJ is horizontal,
this will tame the almost complex structure away from the sin gular point. One
gets ˆΩ L by gluing this together with the symplectic form ˆΩ from the local model,
and that proves (ii). Similarly, the deﬁnition of ˆQL follows that of ˆQ, and (iii’)
implies (iii).
Returning to the moduli spaces ML,s of pseudo-holomorphic sections, we can
now carry out the compactness argument mentioned above:
Lemma 2.15. Choose some neighbourhood of the critical point x0∈ EL. For
suﬃciently small s, the image of all u∈ ML,s will lie in that neighbourhood.
Proof. Let (sk) be a sequence in (0; r′] converging to zero, and uk∈ ML,sk a
corresponding sequence of sections. By Lemma 2.14(i), ther e is for each k a
unique pseudo-holomorphic map
ˆuk : ¯D(1)−→ ˆEL
with ηL(ˆuk(z)) = uk(skz) and ˆπL(ˆuk(z)) = ( sk,z ). By part (iii) of the same
35
lemma, this maps S1 to ˆQL. Moreover, its energy is independent of k, since
∫
¯D(1)
ˆu∗
k ˆΩ L =
∫
¯D(sk)
u∗
kΩ L +
∫
¯D(1)
i
2dz∧d¯z +
∫
¯D(1)
i

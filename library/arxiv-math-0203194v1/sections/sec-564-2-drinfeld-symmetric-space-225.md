---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-564-2-drinfeld-symmetric-space-225
section_title: "DRINFELD SYMMETRIC SPACE. 225"
section_number: 2
pages: 229-231
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry Yves André (with appendices by F. Kato and N. Tsuzuki) — 580 sections: INTRODUCTION; INTRODUCTI"
---
Two normsα andα′ overK is said to be similar ifα′ =λα for someλ∈ R>0.
The set of all similarity classes of norms on V overK forms in an obvious
way a topological space. The following fact is well-known ([ GI63]):
Proposition 2.4. The topological space of similarlity classes of norms on V
over K is PGL(n + 1,K )-equivaliantly homeomorphic to the topological
realization|∆ | of the Bruhat-Tits building ∆.
The homeomorphism is given as follows: To any lattice M we need to
associate a norm αM . For a non-zero x∈V , the set {a∈K| ax∈M} is a
fractional ideal of R, and hence is of form ( πm). We then deﬁne αM (x) = qm
for non-zero x∈V , and αM (0) = 0. It is easily veriﬁed that αM is a norm.
The similarity class of αM depends only on the similarity class of M . Thus
we get a mapping from ∆ 0 to the set of similarity classes of norms. Let
Λ 0 and Λ 1 be vertices adjacent with each other. We can choose a basis
e0,... ,e n ofV such that M0 =⨁ n
i=0Rei andM1 =⨁ n−1
i=0 Rei⊕Rπen give
representatives of Λ 0 and Λ 1, respectively. Then the norms αM0 and αM1
are given by
αM0(
n∑
i=0
aiei) = max {|a0|,... ,|an|},
αM1(
n∑
i=0
aiei) = max {|a0|,... ,|an−1|,|π|−1|an|},
respectively. For 0 <t< 1, the class of the norm
αt(
n∑
i=0
aiei) = max{|a0|,... ,|an−1|,|π|−t|an|}
corresponds to the point tΛ 0 + (1−t)Λ 1 on the edge connecting Λ 0 and Λ 1.
Now, to any point z = (z0 : ··· : zn)∈ P(V ) (subject to some K-basis
{e0,... ,e n}of V ) we associate, up to invertible factor, a non-negative real
valued function
αz(
n∑
i=0
aiei) =
⏐
⏐
⏐
⏐
n∑
i=0
aizi
⏐
⏐
⏐
⏐
onV . Note that this determines a class of norm if and only if z is not lying
in any K-rational hyperplane. Thus we get a mapping
ρ : Ω −→| ∆ |.
The admissible covering in question is actually given by the collection of
subsets of Ω consisting of pull-backs of each simplices of |∆ | by ρ. For
example, notation being as above,
ρ−1(Λ 0) ={|z0| =··· =|zn| = 1}\
⋃
H
{(z0 : ··· : zn) mod π∈H},
whereH runs through all hyperplanes in Pn
k , and
ρ−1(tΛ 0 + (1−t)Λ 1) ={|z0| =··· =|zn−1| = 1,|zn| =|π|−t}
226 B. OVER VIEW OF THEORY OF p-ADIC UNIFORMIZATION.
for 0 <t< 1.
3. Uniformization.
Recall that, once we ﬁx a K-basis of V , the group PGL(n + 1,K ) canon-
ically acts on the Bruhat-Tits building ∆ and the Drinfeld sy mmetric space
Ω. We shall consider discrete groups in PGL( n + 1,K ) and the quotients of
∆ and Ω by them. A subgroup Γ ∈ PGL(n + 1,K ) is said to be hyperbolic
if it acts on ∆ discretely and freely.
To a hyperbolic subgroup Γ we associate a convex subcomplex ∆ Γ of
∆ by the following recipe: In general, a convex subcomplex ge nerated by
vertices of form [n∑
i=0
R·πσiYi
]
, σ i∈ Z, 0≤i≤n,
subject to a basis Y0,... , Yn of V , is said to be an apartment. The geo-
metrical realization of each apartment is a triangulation o f Rn of A n-type,
and ∆ is the union of all apartments. There exists an obvious b ijection
between the set of all apartments and the set of all K-split maximal tori in
PGL(n + 1,K ). For any K-split maximal tori T the untersection Γ ∩T is a
commutative discrete group of rank at most n. If this rank is n we call the
apartment corresponding to T a Γ -apartment, and we deﬁne ∆ Γ to be the
union of all Γ-apartments. Clearly the group Γ acts on ∆ Γ ; if the quotient
∆ Γ/Γ is a ﬁnite simplicial complex, we say Γ is normal hyperbolic.
Now let us be given a normal hyperbolic subgroup Γ. For each γ∈ Γ
and each ﬁnite subcomplex S of ∆ Γ , γS is again a ﬁnite subcomplex of
∆ Γ , and then, γ induces an R-isomorphism P(S)∼
= P(γS) which induces on
generic ﬁbers (= Pn
K) exactly the linear automorphism γ. Considering all S,
gluing, and taking Raynaud generic ﬁber give a rigid analyti c automorphism
of Ω(∆ Γ ) which we denote again by γ. Thus we get an homomorphism
Γ −→ AutK-rig.Ω(∆ Γ ).
Theorem 3.1 (Mustaﬁn [ Mus78], Kurihara [ Kur80]). Let Γ be a normal
hyperbolic subgroup of PGL( n + 1,K ) and ∆ Γ as above. Then there exists,
unique up to isomorphisms, a rigid analytic space XΓ , smooth, proper and
of ﬁnite type over K, and a topological covering map p : Ω(∆ Γ )→XΓ such
that
(i) p◦γ = p for any γ∈ Γ,
(ii) for x,y∈ Ω(∆ Γ ), p(x) = p(y) if and only if x =γ(y) for some γ∈ Γ.
In the references, this theorem has been stated in terms of fo rmal schemes;
viz. they took quotients of ˆΩ(∆ Γ ) to get a formal scheme ˆXΓ ﬂat and for-
mally of ﬁnite type over R. We have an admissible covering of XΓ induced
from that of Ω(∆ Γ ); in terms of formal scheme, the closed ﬁber of ˆXΓ is a
divisor of normal crossings with rational components havin g the dual group
isomorphic to ∆ Γ/Γ.

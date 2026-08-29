---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com"
section_id: sec-008-4-group-bundles-as-global-gauge-symmetries
section_title: "Group bundles as global gauge symmetries."
section_number: 4
pages: 20-23
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
doc_brief: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com — We show that superselection structures on curved spacetime s, that are expected to describe"
---
In the previous section we proved that the superselection struct ure Z 1,•(R) can be described by a
presheaf and, as a consequence of [39], as the dual of a group (ne t) bundle G when an embedding is
given. To illustrate the way in which G should behave like a gauge group, we give a class of examples
in which an action of the type (2.11) is implemented and representatio ns of the type deﬁned in §2.2
appear. The procedure that we use is based on geometric argumen ts and can be applied in a very
general setting (the input is a ﬁeld algebra carrying an action by a ga uge group), thus it yields a
new approach to construct superselection sectors with nontrivia l holonomy, diﬀerent from the one
used in [4] in the case of massive boson ﬁelds on the Einstein spacetime (S1 × R).
4.1 Twisted ﬁeld nets.
Let F = (F, )∆ be a net of C∗ -algebras. We say that F is Z2 -graded whenever there is a period 2
automorphism
βa :Fa →Fa : βa′ ◦a′a =a′a ◦βa , β 2
a =idFa , ∀a ⊆a′ ∈ ∆ .
In this case we set
F ±
a := {t ∈Fa :βa(t) = ±t} , ∀a ∈ ∆ ,
so we have the usual projections
Fa →F ±
a , t ↦→t± := 1/2(t ±βa(t)) , ∀a ∈ ∆ .
The following deﬁnition of normal commutation relations is a variant of [9, Eq.3.6] taking account,
diﬀerently from the above-cited reference, of the net structur e of the involved representation. At
any rate, it is trivially veriﬁed that the following results remain valid with the older deﬁnition. We
say that a representation ( π,U ) of F is normal whenever for any a,o ∈ ∆ with a ⊥ o, t1 ∈ Fa ,
t2 ∈Fo , it turns out
{
[πa(t+
1 ), πo(t+
2 )]net = [πa(t+
1 ), πo(t−
2 )]net = [πa(t−
1 ), πo(t+
2 )]net = 0 ,[
πa(t−
1 ), πo(t−
2 )
] net
+ = 0 , (4.1)
where the (anti)commutators are in the sense of (2.10) (with the c onvention [ ·, ·]net
− ≡ [·, ·]net ).
20
Let now H∗ denote a Hilbert space. A Z2 -graded group on H∗ is given by a group G∗ of
unitary operators on H∗ , metrizable and compact under the strong topology, and a centra l element
γ ∈ZG ∗ , γ2 = 1 , where 1 ∈G∗ is the identity. A ( G∗,γ )-net of von Neumann algebras is a net
F∗ = (F∗, ∗)∆ ⊂BH∗
represented on the Hilbert space H∗ (that is, ∗ is given by inclusion maps), such that
αg
a(t) := gtg ∗ ∈F∗,a , ∀g ∈G∗ , t ∈F∗,a , a ∈ ∆ . (4.2)
We denote the ﬁxed-point net by R∗ = (R∗, ∗)∆ , where
R∗,a :=F∗,a ∩G′
∗ , ∀a ∈ ∆ .
Note that γ induces a Z2 -grading on F∗ . We say that F∗ is normal whenever the deﬁning Hilbert
space representation ( idF∗, 1) is normal in the sense of the previous lines. By (2.10), this agrees
with the classical deﬁnition used, for example, in [17]. Finally, we deﬁne the normalizer group
NγG∗ ⊂UH ∗ : V ∈NγG∗
·
⇔



VF ∗,aV ∗ =F∗,a , ∀a ∈ ∆ ,
VgV ∗ ∈G∗ , ∀g ∈G∗ ,
Vγ =γV .
(4.3)
Lemma 4.1 (Twists of ﬁeld nets) . Let (G∗,γ ) be a Z2 -graded group on the Hilbert space H∗ and
F∗ a normal (G∗,γ )-net of von Neumann algebras on H∗ . Then for any morphism
χ :π1(M ) →NγG∗ ⊂UH ∗
there are:
1. A group net bundle G = (G, ˆı)∆ with ﬁbre G∗ ;
2. A Z2 -graded net of C*-algebras F = (F, )∆ ;
3. A gauge action G ×∆ F → F with ﬁxed point net R = (R, )∆ ;
4. A Hilbert net bundle H = (H,U )∆ with holonomy χ and a normal representation π : F → BH;
5. A causal 6 representation (π|R,U |R) of R.
Proof. Point 1. Given ω ∈ ∆ and a path frame Pω as in (2.2) we deﬁne
ıa′a :=χ(pωa′ ∗ (a′,a ;a′) ∗paω) , ∀a ⊆a′ .
By homotopy invariance the family ı fulﬁls ıa′′a′ıa′a = ıa′′a , ∀a ⊆ a′ ⊆ a′′ (see [35, §2.2]). We
deﬁne
Ga ≡G∗ , ˆıa′a(g) := ıa′agı ∗
a′a , ∀g ∈G∗ , a ⊆a′ ∈ ∆ .
Point 2. We deﬁne Fa :=F∗,a , ∀a ∈ ∆, and
a′a :Fa →Fa′ , a′a(t) := ia′ati ∗
a′a , ∀a ⊆a′ , t ∈Fa .
Since ıa′′a′ıa′a =ıa′′a , ∀a ⊆a′ ⊆a′′ , we conclude that F = (F, )∆ is a net. Moreover, since
ıa′aγ = γıa′a , ∀a ⊆a′ ,
6That is [ πa(Ra),π o(Ro)]net = 0 for any o ⊥a , in the sense of (2.10).
21
we have a Z2 -grading on F given by the adjoint action of γ . Point 3. Taking into account that
Ga ≡ G∗ and Fa = F∗,a for any a ∈ ∆ we deﬁne αg
a ∈ autFa as in (4.2). To check that α is a
gauge action (2.11) must be fulﬁlled, so we compute, for any a ∈ ∆, g ∈Ga , t ∈Fa ,
α
ˆia′ a(g)
a′ ◦a′a(t) = ıa′agı ∗
a′a ·ıa′atı ∗
a′a ·ıa′ag∗ı∗
a′a = ıa′agtg ∗ı∗
a′a = a′a ◦αg
a(t) ,
and this yields the desired equalities. Note that Ra =R∗,a for any a ∈ ∆, because G∗ ≡Ga . Point
4. We set Ha :=H∗ , πa(t) := t, and Ua′a :=ıa′a for any a ⊆a′ ∈ ∆, t ∈Fa . The pair ( π,U ) is
clearly a representation, that is normal since, for any o ⊥a, t ∈Fa , t′ ∈Fo ,
πa(t) ·Upπo(t′)Up = t ·ıpt′ı∗
p , ∀p :o →a ,
and by construction ıpt′ı∗
p ∈ F∗,o . Finally, by construction ( H,U )∆ has holonomy χ. Point 5.
Since F is graded by γ ∈G∗ we have Ra ⊆F +
a , ∀a ∈ ∆, so π|R is causal by applying (4.1).
The following notion is a natural generalization of [17, Def.3.4]. Let F = (F, )∆ be a Z2 -
graded net with a faithful normal representation ( π,U ) on the Hilbert net bundle H = (H,U )∆ ,
H = {Ha} . We assume that there is a net bundle of Z2 -graded compact groups acting on H, that
is, we have a family G = {Ga ⊂ UHa} , and central, period 2 elements γa ∈ Ga , a ∈ ∆, such
that adUa′a(Ga) = Ga′ , adUa′a(γa) = γa′ , a ⊆ a′ ∈ ∆, in such a way that the group net bundle
G = (G, adU )∆ is deﬁned. We assume that G deﬁnes, by adjoint action, a gauge action on π(F).
In this case, we call the quadruple ( F,π,U, G) a ﬁeld system .
Deﬁnition 4.2. We say that ﬁeld systems (F1,π 1,U 1, G1), (F2,π 2,U 2, G2) are equivalent when-
ever there is a unitary family ν = {νa :H1,a →H2,a} such that
νa′U1,a′a =U2,a′aνa , adνa′ ◦1,a′a =2,a′a ◦ adνa , νagν ∗
a ∈G2,a , νaγ1,a =γ2,aνa , (4.4)
for any a ⊆a′ , g ∈Ga .
Note that if χk , k = 1, 2 , are the holonomies of ( Hk,Uk)∆ , then the ﬁrst of (4.4) implies
χ2(p) = νa ·χ1(p) ·ν∗
a , ∀p :a →a . (4.5)
Corollary 4.3. If the morphism χ of the previous Lemma takes values in G∗ ⊆NγG∗ then R is
isomorphic to R∗ . Moreover, when χ is non-trivial R∗ is the ﬁxed-point net of inequivalent ﬁeld
systems, namely (F∗,idF∗, 1,G ∗) and (F,π,U, G).
Proof. Since χ takes values in G∗ we have ıa′a(t) = t for any a ⊆ a′ and t ∈ Ra , so R = R∗ .
To prove that the above ﬁeld systems are inequivalent it suﬃces to s how that U has a nontrivial
holonomy, in fact the immersion idF∗ : F∗ →BH has trivial holonomy and (4.5) implies that the
holonomy of U should be trivial too. But this is not the case, as the holonomy of U , by construction,
coincides with χ (see the proof of Point 4 of the previous Lemma).
One could argue that the only ﬁeld net having a physical meaning is F∗ . But, as a matter of
fact, the twisted ﬁeld net F has the same local algebras and causal properties as F∗ , and it can be
constructed in such a way to support the Klein-Gordon and Dirac eq uations (see §A). Note that F
lives in a representation, π , having a nontrivial holonomy in the sense of [9], whose restriction to
R is equivalent to the (topologically trivial) representation of R∗ in the initial Hilbert space H∗ ;
thus the diﬀerence between F and F∗ can be detected only in charged states which, in π , carry
topological eﬀects given by the action of the fundamental group.
22
As a further remark, we observe that the technical ingredient un derlying the construction of
twisted ﬁeld nets is that we allow a′a , a ⊆ a′ , to be actual *-monomorphisms and not simply
inclusion maps. This is justiﬁed by the fact that the same happens fo r images πz(R∗) of the
observable net under the action of sectors πz , z ∈ obj Z 1(R∗), see (3.2).
At the conceptual level, the question in which we are interested in is w hether R∗ and the
superselection structure Z 1(R∗) encode enough informations to select a unique ﬁeld system. On
the grounds of [39] and the previous corollary we conclude that, to this end, further informations
must be extracted from Z 1(R∗). A complete discussion on twisted ﬁeld nets is beyond the purposes
of the present paper, and we postpone it to a future work (see §5).

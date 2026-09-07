---
doc_id: arxiv-1909.06744v1
doc_title: "Springer correspondence for symmetric spaces"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-18
source_pdf: 1909.06744v1.pdf
source_sha256: 82e3980da78c07da
doc_brief: "Springer correspondence for symmetric spaces — This is a survey on the Springer correspondence for symmetric spa ces."
---
arXiv:1909.06744v1  [math.RT]  15 Sep 2019
Springer correspondence for symmetric spaces
Toshiaki Shoji
Abstract. This is a survey on the Springer correspondence for symmetric spa ces.
We discuss various generalization of the theory of the Springer cor respondence for
reductive groups to symmetric spaces and exotic symmetric space s associated to
classical groups.
§1. Introduction
The Springer correspondence is the canonical correspondence b etween the unipo-
tent classes of a connected reductive group G and irreducible representations of the
Weyl group W of G, established by Springer [Sp] in 1976. In 1981, Lusztig [L2]
found a way to reformulate the Springer’s theory by means of the t heory of per-
verse sheaves. In the same paper, he gave a geometric interpret ation of Koskta
polynomials in terms of the intersection cohomology associated to un ipotent classes
of GLn. The theory of Springer correspondence was generalized by Lusz tig [L3] in
1984 to the theory of generalized Springer correspondence, whic h became a basis of
his theory of character sheaves [L4].
It is an interesting problem to extend the theory of character she aves to a more
general setting, such as a variety on which G acts. Already in 1989, Ginzburg [Gi]
introduced the character sheaves on the symmetric space G/H, and Grojnowski [Gr]
and Henderson [H] studied the case where G/H =GL2n/Sp2n extensively. Recently,
by Achar-Henderson [AH], Finkelberg-Ginzburg-Travkin [FGT], Kato [K1], Shoji-
Sorlin [SS], Shoji [S3], diﬀerent types of examples, such as the enhan ced variety and
the exotic symmetric spaces associated to symplectic groups, are found. Those ex-
amples enjoy the satisﬁed theory of the Springer correspondenc e, as an analogue of
the Springer correspondence for GLn. In turn, in Chen-Vilonen-Xue [CVX], Shoji-
Yang [SY], the case of the symmetric spaces associated to orthogo nal groups were
studied. In this case, an analogue of the generalized Springer corr espondence ap-
pears, rather than the Springer correspondence. We note that the theory of perverse
sheaves associated to (Lie algebra version of) the symmetric spac es of general type
was studied by Lusztig-Yun [LY]. But in this case, the Springer corre spondence does
not hold in general, in the strict sense.
This paper is a survey on the (generalized) Springer corresponden ce for sym-
metric spaces (mainly associated to classical groups), based on th e talks at the
conference ALTReT2019 in Ito, Japan.
Contents
§1. Introduction
§2. Springer correspondene for GLn
§3. Springer correspondence for reductive groups
§4. The interpretation via perverse sheaves
1
2
§5. The generalized Springer correspondence
§6. Geometric realization of Kostka polynomials
§7. The enhanced variety GL(V )×V
§8. Springer correspondence for the enhanced variety
§9. Double Kostka polynomials
§10. Symmetric spaces in algebraic setting
§11. Symmetric spaces associated to classical groups
§12. Unipotent orbits in H and in Gιθ
uni
§13. Exotic symmetric space associated to symplectic groups
§14. Springer correspondence for Gιθ
uni, the case H =SpN
§15. Springer correspondence for Gιθ
uni, the case H =SO2n+1
§16. Generalized Springer correspondence for Gιθ
uni, the case H =SO2n+1
§17. Exotic symmetric spaces of higher level, the case H =SpN
§18. Exotic symmetric spaces, the case H =SO2n+1
§19. Symmetric spaces in characteristic 2
§2. Springer correspondence for GLn
Throughout the paper, we assume that k is an algebraically closed ﬁeld of char-
acteristicp≥ 0, and we consider ¯Ql-sheaves, where ¯Ql is an algebraic closure of the
l-adic number ﬁeld Ql withl⁄=p. Note that if p = 0, one can replace k by the com-
plex number ﬁeld C, and ¯Ql-sheaves by ordinary C-sheaves. All the representations
of ﬁnite groups are considered over ¯Ql≃ C. For a ﬁnite group Γ , we denote by Γ ∧
the set of isomorphism classes of irreducible representations of Γ .
We will start from the simplest example. Let G =GLn(k),B a Borel subgroup
of G containing a maximal torus T . Let W = NG(T )/T be the Weyl group of G.
Hence W is isomorphic to the symmetric group Sn of degree n. Let Pn be the set
of partitions λ = (λ1,...,λ k) such that ∑
iλi =n. It is well-known that there is a
bijection
(2.1) S∧
n≃ Pn, (Vλ↔λ)
where we normalize this so that Vλ is the identity (resp. the sign) representation if
λ = (n) (resp. λ = (1n)).
On the other hand, let Guni be set of unipotent elements in G, called the unipo-
tent variety ofG. G acts on Guni by the conjugation, and Guni is a union of unipo-
tent classes of G. We denote by Guni/∼G the set of unipotent classes in G. It is also
well-known, via the Jordan normal form, that
(2.2) Guni/∼G≃ Pn, (Oλ↔λ).
It follows from (2.1) and (2.2) that there exists a bijection S∧
n ≃ Guni/∼G by
Vλ↔ Oλ . But this is nothing more than the parametrization of two sets, S∧
n and
Guni/∼G, coincides each other, by accident. It would be more interesting, f orm a
mathematical point of view, to show that there exists a “canonical” bijection between
S∧
n and Guni/∼G, independent from the parametrization. Actually, this assertion
was achieved by the discovery of the Springer correspondence, a s explained below.
Let B =G/B be the ﬂag variety of G. Consider the variety
3
(2.3) ~Guni ={(x,gB )∈Guni× B|g−1xg∈B}
and a map π : ~Guni→ Guni, (x,gB )↦→x. Then ~Guni is smooth, irreducible, and
π is proper. In fact, π gives a resolution of singularities of Guni, and is called the
Springer resolution of Guni. For x∈Guni, we deﬁne a closed set Bx of B by
(2.4) π−1(x)≃ Bx ={gB∈ B|g−1xg∈B}.
Bx is called the Springer ﬁbre of x. Bx is not smooth, nor irreducible, but
it is an interesting variety. We consider the cohomology group Hi(Bx, ¯Ql). Then
Hi(Bx, ¯Ql) = 0 if i > 2dx, where dx = dim Bx. Thus H 2dx(Bx, ¯Ql) is the top
cohomology. The following result holds.
Theorem 2.1 (Springer). Letx∈Guni.
(i) Hi(Bx, ¯Ql) has a structure of Sn-module, called the Springer representa-
tion of Sn.
(ii) H 2dx(Bx, ¯Ql) is an irreducible Sn-module.
(iii) The map x↦→H 2dx(Bx, ¯Ql) induces a “canonical” bijection
Guni/∼G ∼− →S∧
n.
(iv) Forx∈ Oλ , H 2dx(Bx, ¯Ql)≃Vλ as Sn-modules. Hence we obtain the corre-
spondence Oλ↔Vλ .
The bijective correspondence in (iii) is called the Springer correspondence .
§3. Springer correspondence for reductive groups
The Springer correspondence for G = GLn gives a bijective correspondence
between unipotent classes of G and irreducible representations of the Weyl group
W of G. But this does not hold for reductive groups in general, and needs s ome
modiﬁcation. Let G be a connected reductive group. B,T,W,G uni, etc. are deﬁned
similarly as in Section 2. The Springer resolution π : ~Guni→Guni is deﬁned similarly.
(Note in the case where p >0, we need to assume that G is simply connected for
obtaining the resolution of singularities. But we ignore this point, and use the
“Springer resolution” for reductive groups in general.) The Springe r ﬁbre Bx is
deﬁned similarly, and the representation of W on Hi(Bx, ¯Ql), namely the Springer
representation of W , was constructed by Springer [Sp]. But the top cohomology
H 2dx(Bx, ¯Ql) is not necessarily irreducible.
Forx∈Guni, put AG(x) = ZG(x)/Z0
G(x). Then AG(x) is a ﬁnite group. ZG(x)
acts on Bx by z : gB ↦→zgB , which induces an action of ZG(x) on Hi(Bx, ¯Ql).
SinceZ 0
G(x) acts trivially on Hi(Bx, ¯Ql), we have an action of AG(x) onHi(Bx, ¯Ql).
It is proved that the action of W onHi(Bx, ¯Ql) commutes with AG(x), thus we have
an action of W×AG(x) on Hi(Bx, ¯Ql).
Remark 3.1. In the case whereG =GLn,ZG(x) is connected, henceAG(x) ={1}.
ForG =SpN,SO N , AG(x)≃ (Z/2Z)c for some c. In turn, for G of type G2,F 4,E 8,
4
there exist a unique class O in G such that AG(x)≃ S3,S 4 and S5 for x∈ O,
respectively.
The following theorem is the original form of the Springer correspon dence due
to Springer.
Theorem 3.2 (Springer [Sp]) . LetG be reductive, and x∈Guni.
(i) Consider the decomposition of H 2dx(Bx, ¯Ql) by AG(x)×W -modules,
H 2dx(Bx, ¯Ql)≃
⨁
τ∈AG(x)∧
τ⊗V(x,τ ).
Then V(x,τ ) is an irreducible W -module if it is non-zero.
(ii) All the irreducible W -modules are realized in this way uniquely. In particular,
we have an injective map
W ∧֒→NG :={(x,τ )|x∈Guni/∼G,τ ∈AG(x)∧}.
Remarks 3.3. (i) Except the case where G =GLn, the above map in (ii) is not
surjective. In fact, the diﬀerence δ =|NG|−| W ∧| = 1 if G is of type G2,F 4 or E8,
while δ = 0 if G is of type E6 or E7. In the former case, the missing one is the pair
(x,τ ), where x is the unique class such that AG(x)≃ S3,S 4,S 5 (see Remark 3.1)
and τ is the sign representation of S3,S 4,S 5, respectively.
(ii) In the case of classical groups, such as G = SpN or SON , δ tends to ∞ if
N→∞ .
§4. The interpretation via perverse sheaves
In [L2] Lusztig reconstructed Springer representations of W on Hi(Bx, ¯Ql) in
terms of the intersection cohomology. Based on Lusztig’s constru ction, Borho-
MacPherson [BM] reformulated Springer’s theorem (Theorem 3.2) in the framework
of the theory of perverse sheaves, which I will explain below.
Let NG be the set of pairs ( O, E ), where O is a unipotent class in Guni and
E is a G-equivariant simple local system on O. If we choose x∈ O, the stalk
Ex of E at x has a structure of a simple AG(x)-module, say τ ∈ AG(x)∧, and τ
characterizes a G-equivariant simple local system E , which we denote by Eτ. Then
by the correspondence ( O, E )↔ (x,τ ), our set NG can be identiﬁed with the set NG
appeared in Theorem 3.2 (ii). For each ( O, E )∈ NG, we consider the intersection
cohomology complex IC( O, E )[dim O], which gives a G-equivariant simple perverse
sheaf on Guni. It is known by [L1] that the number of unipotent classes in Guni is
ﬁnite. Thus by a general theory, we have
(4.1) The set {IC(O, E )[dim O]| (O, E )∈ NG} gives a complete set of isomorphism
classes of G-equivariant simple local systems on Guni.
Theorem 4.1 (Borho-MacPherson [BM]) . Let π : ~Guni→Guni be as in Section 3,
and consider the constant sheaf ¯Ql on ~Guni. Then π∗ ¯Ql[dimGuni] is a semisimple
perverse sheaf on Guni, equipped with W -action, and is decomposed as
5
π∗ ¯Ql[dimGuni]≃
⨁
(O, E )∈NG
V(O, E )⊗ IC(O, E )[dim O],
whereV(O, E ) is an irreducible W -module if it is non-zero.
Note that if K =π∗ ¯Ql[dimGuni] is a G-equivariant semisimple perverse sheaf on
Guni, it is a direct sum of various IC( O, E )[dim O] by (4.1). If K is equipped with
W -action, the multiplicity space V(O, E ) has a structure of W -module. The theorem
asserts that this W -module is irreducible. Also note that the stalk H i
xK of the
cohomology sheaf H iK at x∈ Guni is isomorphic to Hi−dimGuni(Bx, ¯Ql). Thus
Theorem 3.2 is obtained as a corollary of Theorem 4.1.
§5. The generalized Springer correspondence
The map W ∧֒→NG is not necessarily surjective. It is an interesting problem to
understand the pair ( O, E ) which is not contained in the image of W ∧ (for example,
the unique missing pair ( O, E ) in the case of type G2,F 4 or E8 in Remarks 3.3).
As an analogue of the Harish-Chandra theory of the representat ions of reductive
groups, Lusztig extended this map to a bijection to NG. His ingredients are as
follows;
• The notion of a cuspidal pair for ( O, E )∈ NG,
• The notion of an induction ind G
P for a parabolic subgroup P of G and its
Levi subgroup L,
indG
P :{ L-equiv. perverse sheaves on L}→{ semisimple complexes on G}.
Note that K is called a semisimple complex if it is a direct sum of various A[i],
whereA[i] is a degree shift of a semisimple perverse sheaf A. The induction functor
indG
P is deﬁned as follows. We consider the diagram
L
α
←−−−ˆXP
ψ
−−−→~XP
π
−−−→G,
where
ˆXP ={(x,g )∈G×G|g−1xg∈P},
~XP ={(x,gP )∈G×G/P|g−1xg∈P},
and the maps are deﬁned by
α : (x,g )↦→ηP (g−1xg), ψ : (x,g )↦→(x,gP ), π : (x,gP )↦→x.
(η :P→L≃P/UP is the natural projection.) Here α is a smooth morphism with
connected ﬁbre, and ψ is a principal P -bundle. Let K be an L-equivariant perverse
sheaf on L. Then α∗K[a] is a P -equivariant perverse sheaf on ˆX (a is the dimension
of the ﬁbre of α), and there exists a unique perverse sheaf ~K on ~X such that
α∗K[a]≃ψ∗ ~K[b]
6
withb = dimP . Since ~XP is smooth, irreducible, and π is proper, π∗ ~K is a semisim-
ple complex on G by the decomposition theorem of Deligne-Gabber. We deﬁne
indG
PK =π∗ ~K. Note that unless P =B, the map ~XP→L is not deﬁned directly,
so we need to consider ˆXP for deﬁning ~K.
Let SG be the set of triples ( L, O1, E1), up to the natural action of G, where L
is a Levi subgroup of a parabolic subgroup of G, and ( O, E )∈ NL is a cuspidal pair.
Put WL = NG(L)/L. In general, WL is not a Coxeter group, but in a very special
situation that NL has a cuspidal pair, it turns out that WL is a Coxeter group. For
ξ = (L, O1, E1)∈ SG, put Kξ = IC( O 1, E1)[dim O1]. Then Kξ is an L-equivariant
perverse sheaf on L, and one can consider the complex ind G
PKξ onG. The following
result was proved by Lusztig.
Theorem 5.1 (Lusztig [L3]) . (i) Forξ = (L, O1, E1)∈ SG,Kξ is a semisimple
perverse sheaf on G, equipped with WL-action, and is decomposed as
indG
PKξ≃
⨁
(O, E )∈NG
Vξ
(O, E )⊗ IC(O, E )[dim O],
whereVξ
(O, E ) is an irreducible WL-module if it is non-zero.
(ii) For any ξ∈ SG, we have a bijection
N (ξ)
G :={(O, E )∈ NG|Vξ
(O, E )⁄= 0}∼− →W ∧
L.
(iii) We have a partition NG = ∐
ξ∈SG
N (ξ)
G . In particular, there exists a natural
bijection
NG∼− →
∐
ξ∈SG
W ∧
L,
which is called the generalized Springer correspondence.
Remarks 5.2. (i) In general, cuspidal pairs occur very rarely. Let G = SpN or
SON , and δN the number of cuspidal pairs in G. Then we have
• G =SpN : δN =
{
1 if N =d(d− 1) for some d∈ Z ,
0 otherwise.
• G =SON : δN =
{
1 if N =d2 for some d∈ Z ,
0 otherwise.
For example, the occurrence of the cuspidal pairs are given as
N = 2, 6, 12, 20, 30,... (G :SpN ),
N = 1, 4, 9, 16, 25,... (G :SON ).
(ii) If ξ0 = (L, O1, E1), where L = T is a maximal torus, O1 ={1} is the
identity class, and E1 is the constant sheaf ¯Ql, then ind G
PKξ0 gives the original
Springer correspondence in Theorem 3.2 and Theorem 4.1. In this ca se,
• 1W↔ IC(O 1, ¯Ql) : O1 : the regular unipotent class in Guni.
• εW↔ IC(O 0, ¯Ql) : O0 ={1} ; the identity class.
7
§6. Geometric realization of Kostka polynomials
In this section, we will discuss the relationship between Kostka polyn omials and
the theory of the Springer correspondence in the case of GLn. In [L2], Lusztig gave a
geometric realization of Kostka polynomials in terms of the intersect ion cohomology
associated to unipotent classes in GLn. First we review the deﬁnition of Kostka
polynomials.
Consider x = (x1,x 2,..., ) inﬁnitely many variables, and t another parameter.
Let Λ(x) = Λ = ⨁
n≥0Λn be the ring of symmetric functions, where Λn is the n-th
homogeneous part, and consider Λ[t] = Λ⊗Z Z[t], the ring over Z[t]. For λ∈ Pn,
one can consider the Schur function sλ (x)∈ Λn and the Hall-Littlewood function
Pλ (x;t)∈ Λn[t] = Λn⊗Z Z[t]. {sλ (x)| λ∈ Pn} and{Pλ (x;t)| λ∈ Pn} give
Z[t]-bases of Λn[t]. Thus one can deﬁne the Kostka polynomial Kλ,µ (t)∈ Z[t] by
the condition that
(6.1) sλ (x) =
∑
µ ∈Pn
Kλ,µ (t)Pµ (x;t).
Here we introduce two combinatorial objects. For λ,µ ∈ Pn, write them as
λ = (λ1,...,λ k),µ = (µ1,··· ,µk) with λi,µi≥ 0. We deﬁne a partial order λ≤µ
on Pn, called the dominance order, by the condition that, for any 1 ≤j≤k,
(6.2)
j∑
i=1
λi≤
j∑
i=1
µi.
On the other hand, for λ∈ Pn, we deﬁne an n-function n : Pn→ Z≥0 by
(6.3) n(λ) =
k∑
i=1
(i− 1)λi.
Then it is known that Kλ,µ (t) is a monic polynomial with deg Kλ,µ (t) = n(µ)−n(λ).
It follows that one can deﬁne a modiﬁed Kostka polynomial ~Kλ,µ (t)∈ Z[t] by
(6.4) ~Kλ,µ (t) = tn(µ )Kλ,µ (t−1).
Let Oλ be the unipotent class in Guni corresponding to λ∈ Pn for G = GLn
as in Section 2. The following result shows that the closure relations o f unipotent
classes in GLn can be described in terms of the dominance order on Pn.
(6.5.) Oλ =
∐
µ ≤λ
Oµ
The following result gives a geometric realization of Kostka polynomials .
Theorem 6.1 (Lusztig [L2]) . Forλ∈ Pn, put Aλ = IC(Oλ, ¯Ql). Then
(i) H iAλ = 0 for odd i.
8
(ii) Forx∈ Oµ⊂ Oλ , we have
(6.6) ~Kλ,µ (t) = tn(λ ) ∑
i≥0
(dim H 2i
x Aλ )ti.
In particular, Kλ,µ (t)∈ Z≥0[t].
In the case of GLn, Borho-MacPherson’s theorem gives a decomposition
(6.7) π∗ ¯Ql[dimGuni]≃
⨁
λ ∈Pn
Vλ⊗Aλ [dim Oλ ].
By taking the stalk of the i-th cohomology on both sides of (6.7), and by comparing
them with Theorem 6.1 (ii), we obtain the interpretation of Ksotka po lynomials in
terms of the Springer representations of Sn.
Corollary 6.2. Forx∈ Oµ , we have
~Kλ,µ (t) = tn(λ ) ∑
i≥0
⟨H 2i(Bx, ¯Ql),Vλ⟩Snti,
where⟨,⟩Sn is the inner product of characters of Sn.
Remark 6.3. In the case of the Springer correspondence, only Springer repre sen-
tations of the top cohomology H 2dx(Bx, ¯Ql) are involved. While, for the description
of the Kostka polynomials, all the Springer representations H 2i(Bx, ¯Ql) are used.
§7. The enhanced variety GL(V )×V
Later we discuss the theory of the Springer correspondence for the exotic sym-
metric space associated to symplectic groups. The enhanced varie ty is an extension
ofGLn, and is also regarded as a degenerate form of the exotic symmetric space, and
was studied extensively by Achar-Henderson [AH] and Finkelberg-G inzburg-Travkin
[FGT]. So we will start from the exposition on the enhanced variety.
Let G = GL(V ) ≃ GLn with dim V = n. We consider the direct product
X = G×V , on which G acts as g : (x,v )↦→(gxg −1,gv ), where gv is the natural
action ofG onV . The role of Guni is played byXuni =Guni×V , which is aG-invariant
closed subset of X. The varieties X,Xuni are called the enhanced varieties .
Let Pn, 2 be the set of double partitions λ = (λ′,λ ′′) such that|λ| =|λ′| +|λ′′| =
n. The following result is known by Achar-Henderson and Travkin. The ﬁniteness
of the G-orbits is crucial for later discussion.
Lemma 7.1. LetXuni/∼G be the set of G-orbits in Xuni. Then we have
Xuni/∼G≃ Pn, 2.
The correspondence is given as follows; take z = (x,v )∈ Guni×V . Put Ex =
{y∈ End(v)| xy = yx}. Then Ex is a subalgebra of End( V ), and x∈ Ex. Put
Vx = Exv ⊂ V . Then Vx is an x-stable subspace of V . Let λ′ be the Jordan
type of x|Vx and λ′′ the Jordan type of x|V/V x. Then λ = (λ′,λ ′′)∈ Pn, 2, and the
correspondence z↦→λ gives a bijection Xuni/∼G ∼− →Pn, 2.
9
We shall deﬁne an analogue of the dominance order on Pn, 2 as follows; for
λ = (λ′,λ ′′)∈ Pn, 2, write it as λ′ = (λ′
1,...,λ ′
m),λ ′′ = (λ′′
1,...,λ ′′
m) with common
m, and deﬁne c(λ )∈ Z2m
≥0 by
(7.1) c(λ ) = (λ′
1,λ ′′
1,λ ′
2,λ ′′
2,...,λ ′
m,λ ′′
m).
Now deﬁne a dominance order λ≤ µ on Pn, 2 by the condition that c(λ )≤c(µ ) in
Z2m
≥0 . Note that the deﬁnition of the dominance order on Pn makes sense even for
Z2m
≥0 . The following is known by [AH].
Lemma 7.2. For each λ∈ Pn, 2, we have O λ = ∐
µ ≤λ Oµ .
Remark 7.3. Forz = (x,v )∈ Guni×V , the stabilizer ZG(z) in G is connected.
Hence the G-equivariant simple local system on a G-orbit O in Xuni is a constant
sheaf ¯Ql, and we are in a quite similar situation as in the case of GLn.
§8. Springer correspondence for the enhanced variety
We ﬁx a B-stable ﬂag M1⊂ M2⊂···⊂ Mn = V , with dim Mi = i. For an
integer 0≤m≤n, we deﬁne varieties
~Xm ={(x,v,gB )∈Guni×V× B|g−1xg∈B,g −1v∈Mm},(8.1)
Xm =
⋃
g∈G
g(U×Mm),
where U is the unipotent radical of B, and deﬁne a map πm : ~Xm → Xm by
(x,v,gB )↦→(x,v ). Then ~Xm is smooth, irreducible, and π is proper.
For 0≤m≤n, put m = (m,n−m) and Sm =Sm×Sn−m. Then Sm is a Weyl
subgroup of Sn. Put
(8.2) P(m) ={λ = (λ′,λ ′′)∈ Pn, 2||λ′| =m,|λ′′| =n−m}.
Then it is known that
(8.3) S∧
m≃ P(m), V λ =Vλ ′ ⊠Vλ ′′ ↔ λ = (λ′,λ ′′).
The following result is an analogue of Borho-MacPherson’s theorem t o the case
of the enhanced variety.
Theorem 8.1 ([SS]). Put dm = dimXm.
(i) (πm)∗ ¯Ql[dm] is a semisimple perverse sheaf on Xm, equipped with Sm-action,
and is decomposed as
(πm)∗ ¯Ql[dm]≃
⨁
λ ∈P(m)
Vλ⊗ IC(O λ, ¯Ql)[dim Oλ ].
10
(ii) The Springer correspondence is given by
∐
0≤m≤n
(Sm×Sn−m)∧≃
∐
0≤m≤n
{Oλ| λ∈ P(m)} =Xuni/∼G .
§9. Double Kostka polynomials
Kostka polynomials Kλ,µ (t) (λ,µ∈ Pn) was generalized to double Kostka poly-
nomials Kλ, µ (t) ( λ, µ ∈ Pn, 2). (See [S1, S2], where they are deﬁned for any r-
partitions. Here we only consider the special case where r = 2). Recall the dis-
cussion in Section 6. Here we prepare two types of variables x′ = (x′
1,x ′
2,... ),
x′′ = (x′′
1,x ′′
2,... ) and consider Ξ = ⨁
n≥0Λ(x′)⊗Λ(x′′), the ring of symmetric func-
tions with respect to x = (x′,x ′′). Put Ξ[ t] = Ξ ⊗Z Z[t]. For λ = (λ′,λ ′′)∈ Pn, 2,
one can deﬁne the Schur function sλ (x) = sλ ′(x′)sλ ′′(x′′) and Hall-Littlewood func-
tions Pλ (x;t). (Note that the deﬁnition of Pλ (x;t) is rather complicated.) Then
{sλ (x)| λ∈ Pn, 2},{Pλ (x;t)| λ∈ Pn, 2} give two Z[t]-bases of Ξ n[t] = Ξ n⊗Z Z[t].
We deﬁne the double Kostka polynomial Pλ, µ (t)∈ Z[t] by
(9.1) sλ (x) =
∑
µ ∈Pn, 2
Kλ, µ (t)Pµ (x;t).
For λ = (λ′,λ ′′)∈ Pn, 2, deﬁne an a-function a : Pn, 2→ Z≥0 by
(9.2) a(λ ) = 2(n(λ′) +n(λ′′)) +|λ′′|.
Thea-function has a role of n-function in the case of Pn, 2. It is known that Kλ, µ (t)
is a monic of degree a(µ )−a(λ ). As an analogue of (6.4), we deﬁne a modiﬁed
double Kostka polynomial ~Kλ, µ (t) by
(9.3) ~Kλ, µ (t) = ta(µ )Kλ, µ (t−1).
The following result was proved by [AH], which is an analogue of Theorem 6.1,
and gives a geometric realization of double Kostka polynomials.
Theorem 9.1 ([AH]). For λ∈ Pn, 2, put Aλ = IC(O λ, ¯Ql). Then we have
(i) H iAλ = 0 for odd i.
(ii) Take λ, µ∈ Pn, 2 such that µ≤ λ . For z∈ Oµ⊂ O λ , we have
(9.4) ~Kλ, µ (t) = ta(λ ) ∑
i≥0
(dim H 2i
z Aλ )t2i.
Remark 9.2 If we compare the formula (9.4) with the formula (6.6) in Theorem
6.1, we notice the discrepancy of the relations between ti and cohomology sheaves.
11
In fact, in (6.6) ti corresponds to H 2i
x Aλ , while in (9.4) t2i corresponds to H 2i
z Aλ .
Later, we also consider the geometric realization of double Kostka p olynomials by
means of exotic symmetric space. In that case, this discrepancy is removed (see
Theorem 13.4).
§10. Symmetric spaces in algebraic setting
Historically, the symmetric space G/K, where G is a connected Lie group and K
is a compact subgroup such that ( Gθ)0⊂K⊂Gθ for an involutive automorphism θ
ofG, has been studied extensively from a point of view of the Riemannian g eometry.
However, here we are interested in its algebraic structure, namely , we consider G,K
as algebraic groups and G/K as an algebraic variety over k of any characteristic.
The basis of the algebraic study of symmetric spaces was achieved b y Vust [V] and
Richardson [R], which will be summarized below.
Let G be a connected reductive group over k with ch k≥ 0, and θ :G→G an
automorphism such that θ2 = 1. Consider the ﬁxed point subgroup Gθ ={g∈G|
θ(g) = g} of G, and put H = (Gθ)0. (Here we use the notation H rather than K,
since we often use K as complexes of sheaves.) Put
Gιθ ={g∈G|θ(g) = g−1},
where ι :G→G,g↦→g−1 is an anti-automorphism, so we regard Gιθ as the subset
of G consisting of ιθ-ﬁxed elements. Put Gιθ
0 ={gθ(g)−1|g∈G}. It is known that
Gιθ
0 is a connected component of Gιθ, and there exists an isomorphism
Gιθ
0 ∼− →G/Gθ, gθ (g)−1↔gGθ.
Gθ acts on Gιθ andGιθ
0 by the conjugation action, which corresponds to the left
multiplication of Gθ onG/Gθ via the above isomorphism. Thus one can identify Gιθ
0
with the symmetric space G/Gθ, and from now on, we consider Gιθ
0 as a symmetric
space in an algebraic setting.
Remark 10.1 Assume that p⁄= 2. Let θ : G→G be as above. Let g be the Lie
algebra of G. Then θ induces an involutive automorphism on g, which we denote
by the same symbol as θ : g→ g. We have the decomposition
g≃ gθ⊕ g−θ,
where g±θ are±1 eigenspaces of θ. We note that gθ≃ LieGθ and g−θ is a Gθ-stable
subspace of g such that g−θ≃ Te(Gιθ). g−θ is usually referred as the symmetric
space with respect to Gθ. Thus Gιθ is regarded as a global analogue of g−θ.
LetGιθ
uni =Gιθ
0∩Guni be the set of unipotent elements in Gιθ
0 . Then Gιθ
uni is anH-
stable closed subset of Gιθ, which has a role of the unipotent variety Guni in the case
of symmetric spaces. The following important result was proved by R ichardson [R].
In fact, Richadson reduced the problem to a similar problem for redu ctive groups,
which certainly holds by Lusztig [L1].
Proposition 10.2. Assume that p⁄= 2 . Then the number of H-orbits in Gιθ
0 is
ﬁnite.
12
Remark 10.3. In the Lie algebra case, put g−θ
nil = g−θ∩ gnil, where gnil is the set of
nilpotent elements in g. Then g−θ
nil is an H-stable closed subset of g−θ. The ﬁniteness
property also holds in the Lie algebra case. But this does not hold for Gιθ
uni ifp = 2.
§11. Symmetric spaces associated to classical groups
From now on, we concentrate ourselves to the special type of sym metric spaces,
namely the symmetric spaces associated to classical groups.
Let V be an N-dimensional vector space over k with ch k⁄= 2, and put G =
GLN ≃ GL(V ). We deﬁne an involutive automorphism θ : G→ G by θ(g) =
J −1(tg−1)J, where J =J1 or J2,
J1 =


1 0 0
0 0 1 n
0 1 n 0

 if N = 2n + 1, J1 =
(
0 1 n
1n 0
)
if N = 2n,
J2 =
(
0 1 n
−1n 0
)
for N = 2n.
If J =J1, then Gθ =ON and H =SON . While if J =J2, then Gθ =H =SpN . In
both cases, the following identity holds.
(11.1) Gιθ
0 =Gιθ.
For later applications, we consider a generalization of the symmetric space Gιθ
of the following type; for an integer r≥ 1, consider the direct product Gιθ
uni×Vr−1,
on which H acts diagonally. Gιθ
uni×Vr−1 is called the exotic symmetric space of
levelr. In the following discussion, we are interested in extending the theo ry of the
Springer correspondence to the case of exotic symmetric spaces .
LetT⊂B be the pair of θ-stable maximal torus and θ-stable Borel subgroup of
G. Then the unipotent radical U ofB isθ-stable. Put BH = (Bθ)0 andTH = (Tθ)0.
ThenBH is a Borel subgroup of H andTH is a maximal torus of H contained in BH.
We consider the ﬂag variety BH =H/BH ofH. Let M1⊂···⊂ Mn be the isotropic
ﬂag in V such that the stabilizer of ( Mi)i in H is BH . Consider the varieties
~X ={(x, v,gBH)∈Gιθ
uni×Vr−1× BH|g−1xg∈Bιθ,g −1v∈Mr−1
n },
X =
⋃
g∈H
g(Uιθ×Mr−1
n ).
and deﬁne a map π : ~X → X by (x, v,gBH)↦→(x, v).
The map π : ~X → X is an analogue of the Springer resolution π : ~Guni→Guni,
and we want to consider an analogue of the Borho-MacPherson’s th eorem. But in
order to apply the previous discussion, we need to verify two crucia l properties,
namely (i) the map π gives a resolution of singularities, (ii) the number of H-orbits
is ﬁnite. (Actually, (i) is too strong. For the theory of the Springer correspondence,
13
enough to show that π is “semi-small”, which implies that (i ′) dim ~X = dim X ).
Thus we will verify those two properties (i ′) and (ii). Put δ = dim ~X − dim X .
The following holds.
• H =SpN r r = 1 r = 2 r≥ 3
δ δ >0 δ = 0 δ = 0
number of orbits <∞ <∞ ∞
• H =SON r r = 1 r≥ 2
δ δ = 0 δ = 0
number of orbits <∞ ∞
From those tables, we see that the most suitable situation for the S pringer
correspondence is that X =Gιθ
uni×V for the case H =SpN , and X =Gιθ
uni for the
case H = SON . This gives a reason why considering the exotic symmetric space,
rather then the symmetric space itself, is important. In the case w hereH =SpN , it
is more natural to consider Gιθ
uni×V thanGιθ
uni. In the following sections, we consider
those standard cases, separately. However, we consider the ot her cases also, since
some modiﬁed theory of the Springer correspondence holds in thos e cases, and they
have own interests.
§12. Unipotent orbits in H and in Gιθ
uni
For later applications, in this section we describe the H-orbits in Gιθ
uni in con-
nection with the unipotent classes in Gθ
uni.
In the following discussion, we only consider H =SON (N : odd) or H =SpN ,
namelyH is of type Bn orCn. Similar results hold in the case where H is of type Dn,
but since the description becomes more complicated, we omit this, fo r simplicity.
Let λ = (1m1, 2m2,... )∈ PN be a partition of N. Let Oλ be the unipotent
class in G =GLN corresponding to λ. The following result is well-known.
Proposition 12.1 (group case). Under the notation above, we have
(i) Oλ∩H⁄=∅⇐⇒ mi is even for odd i ( resp. for even i )
if H =SpN ( resp. H =SON ).
(ii) If Oλ∩H⁄=∅, then Oλ = Oλ∩H is a single class in H.
(iii) Forx∈ Oλ ,
ZGθ (x)≃
{ (∏
i:oddSpmi× ∏
i:evenOmi
)
⋉U1 ( SpN -case ),(∏
i:evenSpmi× ∏
i:oddOmi
)
⋉U1 ( SON -case ),
whereU1 : connected unipotent normal group of ZGθ (x).
The case of H-orbits in Gιθ
uni is given as follows.
Proposition 12.2 (symmetric space case). LetH =SpN .
(i) Oλ∩Gιθ⁄=∅⇐⇒ mi is even for all i.
(ii) If Oλ∩Gιθ⁄=∅, then Oλ = Oλ∩Gιθ is a single H-orbit.
(iii) Forx∈ Oλ ,
ZGθ (x)≃
∏
i
Spmi ⋉U1.
14
Proposition 12.3 (symmetric space case). LetH =SON ( N : odd ).
(i) Oλ∩Gιθ is always non-empty.
(ii) Oλ = Oλ∩Gιθ is a single H-orbit.
(iii) Forx∈ Oλ ,
ZGθ (x)≃
∏
i
Omi ⋉U1,
Remark 12.4 By comparing Proposition 12.2 and Propositions 12.3, 12.4, we ﬁnd
very interesting phenomena. In the group case, ZGθ (x) involves the subgroups of
type Sp and SO. Hence in the study of unipotent classes in H, the case of Sp and
of SO cannot be separated. While in the case of symmetric spaces, the st ructure
ofZGθ (x) is completely separated, namely in the case of H =SpN , ZGθ (x) involves
only subgroups of type Sp, and similarly for H =SON . All the properties of ZGθ (x)
in the case of symmetric spaces are inherited from similar properties in the group
case, but they produce two extreme phenomena to the opposite d irections.
As corollaries of above results, we can determine the structure of the component
group AH (x) as follows.
Corollary 12.5 (group case). Assumex∈ Oλ⊂Huni. Put AH(x) = ZH(x)/Z0
H(x).
Then
AH(x)≃ (Z/2Z)a(λ ),
where
a(λ) =
{
♯{i|i : even, mi⁄= 0} if H =SpN ,
♯{i|i : odd,mi⁄= 0}− 1 ( or 0) if H =SON .
Corollary 12.6 (symmetric space case). Assume x∈ Oλ⊂Gιθ
uni. Put AH(x) =
ZH(x)/Z0
H(x). Then
AH (x)≃ (Z/2Z)b(λ ),
where
b(λ) =
{
0 if H =SpN ,
♯{i|mi⁄= 0}− 1 ( or 0) if H =SON .
§13. Exotic symmetric space associated to symplectic groups
We now consider the case of exotic symmetric space associated to s ymplectic
groups. So assume that H = SpN and X = Gιθ
uni×V . The fact that the set of
H-orbits in X is parametrized by Pn, 2 was ﬁrst proved by Kato [K1]. The following
is a reformulation of Kato’s result due to [AH].
Let Mn be the maximal isotropic subspace in V , stable by BH. There exists a
θ-stable Levi subgroup L⊂G such that Lθ≃GL(Mn). Then we have embeddings
(13.1) Lιθ
uni×Mn⊂Gιθ
uni×V ⊂Guni×V.
Note that the left hand side and the right hand side of (13.1) are enh anced varieties
discussed in Section 7; GL(Mn) acts on Lιθ
uni×Mn diagonally, and their orbits are
15
parametrized by Pn by Lemma 7.1. In turn, G acts on Guni×V diagonally, and
their orbits are parametrized by P2n by Lemma 7.1. We have
Lemma 13.1 ([K1], [AH]) . Let λ ∈ Pn, 2, and λ∪ λ ∈ P2n, 2. Let OL
λ be the
GL(Mn)-orbit corresponding to λ , and Oλ ∪λ the G-orbit corresponding to λ∪ λ .
Then Oλ is the unique H-orbit in X such that
OL
λ ⊂ Oλ⊂ Oλ ∪λ.
The analogue of Lemma 7.2 and Remark 7.3 also hold for Gιθ
uni×V .
Proposition 13.2. Let Oλ be an H-orbit in Gιθ
uni×V corresponding to λ∈ Pn, 2.
(i) Forz = (x,v )∈Gιθ
uni×V , ZH(z) is connected.
(ii) O λ = ∐
µ ≤λ Oµ , namely the closure relations are described by the dominanc e
order on Pn, 2.
In this case, the map π : ~X → X in Section 11 is given as follows;
~X ={(x,v,gB H)∈Gιθ
uni×V× BH|g−1xg∈Bιθ,g −1v∈Mn},
X =
⋃
g∈H
g(Uιθ×V ) = Gιθ
uni×V,
and π : (x,v,gB H)↦→(x,v ).
Let Wn be the Weyl group of H =SpN , namely the Weyl group of type Cn. It
is known that W ∧
n ≃ Pn, 2, we denote by ~Vλ irreducible representation of Wn cor-
responding to λ∈ Pn, 2. (Note the diﬀerence from Vλ , which was deﬁned in (8.3).)
The following theorem was ﬁrst proved by Kato [K1] by applying the Gin zburg the-
ory of Hecke algebras, and then reproved by [SS, I] in the framewo rk of Lusztig’s
theory of the generalized Springer correspondence.
Theorem 13.3. π∗ ¯Ql[dim X ] is a semisimple perverse sheaf on X , equipped with
Wn-action, and is decomposed as
π∗ ¯Ql[dim X ]≃
⨁
λ ∈Pn, 2
~Vλ⊗ IC(O λ, ¯Ql)[dim Oλ ].
The geometric realization of double Kostka polynomials in terms of Gιθ
uni×V
was conjectured in [AH], and was proved by [K3], [SS, II], independent ly. In [SS,II],
it is proved by making use of the discussion on character sheaves du e to Lusztig
[L4].
Theorem 13.4. For λ∈ Pn, 2, put Aλ = IC(O λ, ¯Ql). Then we have
(i) H iAλ = 0 unless i≡ 0 (mod 4) .
(ii) Forz∈ Oµ⊂ O λ ,
(13.2) ~Kλ, µ (t) = ta(λ )
∑
i≥0
(dim H 4i
z Aλ )t2i.
16
Compare the formula (13.2) with the formula (9.4) in the enhanced ca se. The
correspondence H 4i↔t2i in (13.2) is more natural than the correspondence H 2i↔
t2i in (9.4). Note that the modulo 4 vanishing of the cohomology of Aλ was ﬁrst
noticed by Grojnowski [Gr].
Forz = (x,v )∈Gιθ
uni×V , consider the Springer ﬁbre
π−1(z)≃ BH
z ={gBH∈ BH|g−1xg∈Bιθ,g −1v∈Mn}.
ThenHi(BH
z , ¯Ql) has a structure ofWn-module, which is an analogue of the Springer
representations. By using the Springer representation of Wn, we obtain an expression
of double Kostka polynomials, which is an analogue of Corollary 6.2.
Corollary 13.5. Assume that z∈ Oµ . Then Hi(BH
z , ¯Ql) = 0 unlessi≡ 0 (mod 4) ,
and we have
~Kλ, µ (t) = ta(λ )
∑
i≥0
⟨H 4i(BH
z , ¯Ql), ~Vλ⟩Wnt2i.
§14. Springer correspondence for Gιθ
uni, the case H =SpN
As pointed out in Section 11, Gιθ
uni for H =SpN does not satisfy the condition
explained there, so the Springer correspondence does not hold in t he strict sense.
However some modiﬁed theory of the Springer correspondence st ill holds for Gιθ
uni,
as discussed in Henderson [H], which I will explain below.
First we prepare some notation which is common for H = SpN and SON .
Assume that H =SpN or SON (N : odd), and consider Gιθ
uni. Let NGιθ be the set
of pairs ( O, E ), where O is an H-orbit in Gιθ
uni, and E is an H-equivariant simple
local system on O. Thus as in Section 4, NGιθ can be expressed as follows;
(14.1) NGιθ≃{ (x,τ )|x∈Gιθ
uni/∼H,τ ∈AH (x)∧}.
We consider the variety
(14.2) ~Gιθ
uni ={(x,gBH)∈Gιθ
uni× BH|g−1xg∈Bιθ}
and deﬁne a map π : ~Gιθ
uni→Gιθ
uni by (x,gBH)↦→x. Then π is proper, surjective, and
~Gιθ
uni is smooth, irreducible. If we put δ = dim ~Gιθ
uni− dimGιθ
uni, δ = 0 for H =SON ,
while δ >0 for H =SpN . In fact, in the latter case, π gives rise to a ( P1)n-bundle
on its open dense part, and δ =n. Let Wn =NH(TH )/TH be the Weyl group of H,
thus Wn is of type Cn or Bn according to the case where H = SpN or SON . We
consider Sn as a subgroup of Wn.
Now assume thatH =SpN . By Proposition 12.2, the set Gιθ
uni/∼H is parametrized
by Pn, under the correspondence
(14.3) O2λ = O2λ∩Gιθ
uni↔λ∈ Pn,
and by Corollary 12.6, ZH(x) is always connected for x∈ Gιθ
uni. Hence the local
system E on O is the constant sheaf ¯Ql, and we have
17
(14.4) NGιθ ={(O, ¯Ql)}≃ Pn.
The following result was ﬁrst proved by [H] for g−θ
nil , without the explicit corre-
spondence, and was proved for Gιθ
uni in [SS, I] in the following form.
Theorem 14.1. Let H = SpN . Then π∗ ¯Ql[dimGιθ
uni] is a semisimple complex,
equipped with Sn-action, and is decomposed as
π∗ ¯Ql[dimGιθ
uni]≃H •(Pn
1 )⊗
⨁
λ ∈Pn
Vλ⊗ IC(O 2λ, ¯Ql)[dim O2λ ],
where H •(Pn
1 ) = ⨁
i≥0H 2i(Pn
1, ¯Ql) is a complex of vector spaces, and Vλ is the
irreducibleSn-module corresponding to λ∈ Pn.
Note that the occurrence of the factor H •(Pn
1 ) depends on the fact that π is
generically a Pn
1 -bundle.
Remark 14.2. If we consider the symmetric space Gιθ
uni of general type, one can
expect that a similar phenomenon as in the case of H = SpN occurs. The case
where H =SON seems to be rather special, and we could not ﬁnd other examples
such that the Springer correspondence holds in the strict sense. Thus in order to
discuss the (generalized) Springer correspondence for the gene ral case, we nned to
consider a correction factor such as H •(Pn
1 ) in the case of SpN . In the Lie algebra
case, Lusztig-Yun [LY] discusses a related problem.
§15. Springer correspondence for Gιθ
uni, the case H =SO2n+1
We now assume thatH =SO2n+1. Then by Proposition 12.3, the set of H-orbits
in Gιθ
uni is parametrized by P2n+1;
(15.1) Oλ = Oλ∩Gιθ
uni↔λ∈ P2n+1.
We deﬁne a map Γ : Pn→ P2n+1 by
(15.2) Γ :µ = (µ1,...,µ k)↦→(2µ1 + 1, 2µ2,..., 2µk).
The following result gives the Springer correspondence for Gιθ
uni. It was ﬁrst proved
by Chen-Vilonen-Xue [CVX] for g−θ
nil with k = C. The group case Gιθ
uni is due to
[SY].
Theorem 15.2. Assume that H = SO2n+1. Then π∗ ¯Ql[dimGιθ
uni] is a semisimple
perverse sheaf on Gιθ
uni, equipped with Sn-action, and is decomposed as
(15.3) π∗ ¯Ql[dimGιθ
uni]≃
⨁
µ ∈Pn
Vµ⊗ IC(OΓ (µ ), ¯Ql)[dim OΓ (µ )],
whereVµ is the irreducible Sn-module corresponding to µ∈ Pn.
18
Remarks 15.2. (i) The formula (15.3) looks very similar to the formula in the
case of GLn. But the pattern of the Springer correspondence is quite diﬀeren t from
that of GLn (see Remarks 5.2 (ii)). In fact, the Springer correspondence for Gιθ
uni is
given as follows;
• 1Sn =Vµ with µ = (n)↔ IC(OΓ (µ ), ¯Ql), where Γ (µ) = (2n + 1)∈ P2n+1,
• εSn =Vµ with µ = (1n)↔ IC(OΓ (µ ), ¯Ql), where Γ (µ) = (3, 2n−1)∈ P2n+1.
If λ = (2n + 1), Oλ is the open dense orbit in Gιθ
uni, hence it is similar to O1 in
Remarks 5.2 (ii). However if λ = (3, 2n−1), the orbit Oλ is not like O0 in [loc. cit.],
Oλ is much bigger than the unit orbit Oλ ′ with λ′ = (1 2n+1).
(ii) By Corollary 12.6, NGιθ contains lots of pairs ( O, E ) such that E is not the
constant sheaf ¯Ql. The formula (15.3) only involves the pairs such that E = ¯Ql,
the constant sheaf. Thus the Springer correspondence is not en ough to cover all the
pairs in NGιθ , and we need to consider the generalized Springer correspondenc e.
§16. Generalized Springer correspondence for Gιθ
uni, the case H =SO2n+1
In this section, we consider the generalized Springer corresponde nce for Gιθ
uni
with H =SON (N = 2n + 1).

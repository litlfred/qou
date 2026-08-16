---
doc_id: invariant-eigendistributions-2
doc_title: "REPRESENTATIONS OF WEYL GROUPS 1 Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups W. ROSSMAN"
section_id: sec-012-1-supported-bya-grant-from-nserc-canada
section_title: "Supported bya grant from NSERC Canada"
section_number: 1
pages: 1-4
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
doc_brief: "REPRESENTATIONSOFWEYL GROUPS 1 Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups W. ROSSMANN1 — 25 sections: Intr"
---
REPRESENTATIONS OF WEYL GROUPS 2
mistake in myproof of that theorem. The table of contents mayserve as a further guide to the topics
treated.
Some related papers, which have appeared or come to my attention since this paper was written, are cited in the supple-
mentary references. In particular, the recent work of Joseph [1989] and Vergne [1989] provides an interesting alternative
approach to some of the questions discussed in sections 7 and 10.
2. Construction of Weyl group representations
We keep the notation introduced in part I, except that (until further notice)g can be anycomplex,
semisimple Lie algebra (not necessarily≈ go ×go), b1 anyBorel subalgebra of g containing the Cartan
subalgebra h. For any (not necessarilyregular) λ∈h∗ we set
Ωλ ={ξ ∈g∗ :p(ξ)= p(λ) for allG-invariant polynomialsp on g∗}.
The map
pλ =pb1,λ :B∗ → Ωλ,u ·(b1,ν)→u·(λ+ν).
with u∈U (compact form ofG),ν ∈b1
⊥ is then well-deﬁned and surjective forall λ∈h∗.
Assume nowλ regular. Then pλ is bijective and for anyw ∈ W we maydeﬁne a transformation
aλ(w)= ab1,λ(w)o fB∗ by
aλ(w)= pwλ−1 ◦pλ :B∗ →B ∗.
It is evident that
aλ(wy)= ayλ(w)aλ(y). (1)
If one could setλ = 0 in this equation, one would get an action ofW on B∗, which would leave the
map po : B∗ → Ω0 invariant, so thatW would permute the ﬁbers of this map. This is of course only
triviallypossible, as the ﬁbers are genericallysingle points: the mapp0 is the Springer map,w h i c hi sa
desingularization π : B∗ →N of the nilpotent cone Ωo = N in g∗ [Steinberg 1976]. Borrowing an idea
of Kazhdan and Lusztig [1980] we look for what one might call a (proper)homotopy action of W on B∗,
meaning a homomorphism ofW into the group of proper homotopyequivalences ofB∗, rather than a
genuine action. But we shall not use the Kazhdan-Lusztig construction (which in fact theycould not
prove to give a homotopyaction); instead we use thea
λ(w). (We shall prove in an appendix that our
constructionagreeswith Kazhdan-Lusztig’s,provingincidentallythattheir constructiongivesa homotopy
action after all. Of course, what we are ultimatelyinterested in is a representation ofW in homology, and
that theydid obtain -at least for the top-dimensional homology . Several other constructions of (variants
of) this representation ofW are known, ﬁrst of all Springer’s original construction [Springer 1976,1978],
another construction of Lusztig [1981], and others.)
We write out explicitlythe deﬁnition ofa
λ(w):
aλ(w)(u·(b1,ν)) =u′·(b1,ν ′)w h e r eu′·(wλ+ν′)= u(λ+ν).
Thus
u′·ν′−u·ν =−u′·wλ+u·λ
REPRESENTATIONS OF WEYL GROUPS 3
hence
|u′·ν′−u·ν|≤ const.|λ|.
Thus for λ close to 0 (but regular) the transformationsaλ(w) leave the Springer mapπ : B∗ →N
approximatelyinvariant in the sense that
|π(aλ(w)(b,ν))−π(b,ν))|≤ const.|λ|. (2)
For anysubset V of N let
B∗(V)= {(b,ν)∈B ∗ :ν ∈V},
the inverse image ofV in B∗. We wish to constuct a proper homotopyaction of W on B∗(V). This
requires a regularitycondition onV. Namely, for ﬁxedϵ>0, letU the be theϵ-neighbourhood ofV inN,
U ={ν ∈N :|ν−ν′|<ϵfor someν′∈V},
and
B∗(U)= {(b,ν)∈B ∗ :|ν−ν′|<ϵfor someν′∈V} (3)
its inverse image inB∗. We require that
for suﬃcientlysmall ϵ>0, the inclusion i :B∗(V) →B ∗(U) should admit a proper homotopy
inversep : B∗(U) →B ∗(V), i.e.
p◦i ∼ 1o nB∗(V), and i◦p ∼ 1o nB∗(U)( 4 )
with “∼” meaning “properlyhomotopic”.
We observe that this condition is satisﬁed in either the following two cases:
(a) V is a ﬁnite subpolyhedron of a triangulation ofN,( 5 )
(b) V is a constructible subset ofN, stable under scalar multiplications. (6)
The ﬁrst condition maybe explained as follows. Let ¯g∗ =P(g∗ ⊕ C) be the projective completion ofg∗,
¯N the closure ofN in ¯g∗, ¯B∗ the closure ofB∗ ⊂B×N in B× ¯N. As a projective algebraic variety,¯N
admits a triangulation [Hironaka 1975], hence (5) makes sense.
That (5) implies (4) is seen as follows. Assume (5). ThenB∗(V) is also a ﬁnite subpolyhedron of a
triangulation ofB∗. It is an elementaryfact that a ﬁnite subpoly hedron has a retractable neighbourhood
[Alexandroﬀ-Hopf, 1935, sections 6.1-2]. In particularB∗(V) has a retractible neighbourhoodW in B∗.
Since π is a proper map, there is a neighbourhoodU of V in N so thatπ−1(U)⊂W, which gives (4).
That the condition (6) also implies (4) is seen as follows. One maysuppose thatV excludes 0, as
a neighbourhood of 0 maybe treated separately . Because of the assumption thatV is stable under scalar
multiplications and excludes 0, one maythen replaceV by V ∩{|ν| =1 } in order to prove (4). SinceV
is also constructible, one mayapply(5).
From now on we shall assume that all setsV under consideration satisfyeither (5) or (6), so that
(4) applies. (This maywell be unnecessarilyrestrictive, but is suﬃcient for the applications we have in
mind.) It is clear from (2) and (3) that
a
λ(w)B∗(V)⊂B ∗(U)
for λ∈h∗ suﬃcientlyclose to 0. Thus the transformation
aλ,V (w)= p◦aλ(w)◦i (7)
REPRESENTATIONS OF WEYL GROUPS 4
of B∗(V) is deﬁned for all regularλ in a small ball about 0 inh∗. Since theseλ form a connected set, the
proper homotopyclass aV (w)o faλ,V (w) is independent ofλ, and the equation (1) implies that
aV (wy)= aV (w)aV (y)
so that the aV (w) give a proper homotopy action of W on B∗(V).
As a consequence we havea representationofW in the homologywith integralcoeﬃcients, denoted
H∗(B∗(V), Z). As inKazhdan-Lusztig[1980],“homology”mayherebe understoodeither as“Borel-Moore
homology” or as relative homologyH∗(¯B∗(V),∂B∗(V); Z) of the ﬁnite polyhedron¯B∗(V) with respect to
its ﬁnite subpolyhedron∂B∗(V) (see the explanations in connection with (5)). The coeﬃcient ringZ will
be omitted from the notation when understood or unimportant.
For the further analysis of the representations ofW in theseH∗(B∗(V)) we follow Kazhdan-Lusztig
[1980]. SupposeX ⊂Y are closed subvarieties ofN, and putU =Y −X. There is a long exact sequence
···→ Hi+1(B∗(U))→Hi(B∗(X))→Hi(B∗(Y))→Hi(B∗(U))→Hi−1(B∗(X))→··· (8)
In top degree, wheni =2 m, m =d i mCB∗(Y),H 2m+1(B∗(U)) = 0, trivially, and the boundary map
H2m(B∗(U)) → H2m−1(B∗(X)) is = 0 because the topological boundaryof a complex varietyhas real
codimension at least 2. So (8) leads to the short exact sequence
0→H2m(B∗(X))→H2m(B∗(Y))→H2m(B∗(U))→ 0( 9 )
The maps (7) and (9) areW-maps.
3. Specialization
In the above construction, chooseV ={ν}, a single point. Then
B∗(ν)= {(b,ν)|ν ∈b⊥},
which maybe identiﬁed with
Bν ={b∈B| ν ∈b⊥}.
This is the ﬁxed point set of (the one parameter group generated by)ν, when g∗ is identiﬁed withg. We
thus have a representation ofW in H∗(Bν).
The component groupA(ν) of the stabilizer ofν in G acts onH∗(Bν). This action commutes with
the action ofW, because the elements ofA(ν) have representatives inU (the compact form ofG)a n dt h e
operators aλ(w)= pwλ−1 ◦pλ commute with the action ofU on B∗,t h epλ being U-equivariant.
The Weyl groupW acts on the ﬂag-manifoldB≈ U/T by
a(w)·u·b1 =u·w−1b1(u∈U).
InthecontextofSpringer’sconstruction,theanalogueofthefollowinglemmaisthe Specialization Theorem
of Hotta-Springer [1977].

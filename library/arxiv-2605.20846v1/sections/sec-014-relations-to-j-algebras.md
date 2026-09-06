---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li"
section_id: sec-014-relations-to-j-algebras
section_title: "Relations to J-Algebras"
section_number: null
pages: 74-90
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li — We give two presentations for bordisms ofS 2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
Definition 5.2.1.(Trace of Surgery) LetMbe an orientedn-manifold and 0≤k≤n.
Letϕ:S k−1×Dn−k ,→Mbe an embedding along which ak-handle is attached. The
resulting manifold is
M′ =M∪ ϕ (Dk×Dn−k).
Thetraceof this handle attachment is the (n+ 1)-dimensional cobordismWfromM
toM ′ obtained by attaching ak-handle toM×[0,1] alongM×{1}:
W= (M×[0,1])∪ ϕ (Dk×Dn−k+1).
Its incoming boundary isM×{0}and the outgoing boundary is the manifoldM ′.
Recall [Juh18]’s assignment of aJ-algebra associated to a 3-dimensional oriented
TFTZ: Cob(3)→Vect k 2 is denotedJ(Z) which consists of the following data
1.A g =Z(Σ g) is the vector space associated to the genusgsurface Σ g underZ, for
allg≥0
2. linear mapsα g :A g→A g−1, which we call “genus reduction maps.”
This is theZ-image of trace of the attachment of a 2-handle around a hole, which
eliminates it.
3. linear mapsδ j,g−j :A g→A j⊗Ag−j, which we call “splitting maps.”
This is theZ-image of the trace of the splitting of Σ g into Σj⨿Σg−j.
4. linear mapsµ i,j :A i⊗Aj→A i+j, which we call “merging maps.”
This is theZ-image of the trace of the merging of Σ i⨿Σj into Σi+j.
2Note Juhasz’s original paper the unusual convention is to denote by Cob(n) the category ofn-manifolds
and bordisms. We will not adopt this convention.
74
5. linear mapsω g :A g→A g+1, which we call “genus creation maps.”
This is theZ-image of the trace of the attachment of a 1-handle.
6. The linear maptr:A 0→k, which we call the “trace map.”
This isZ(D 3), whereD 3 :S 2→∅.
7. The linear map 1 :k→A 0, which we call the “unit map.”
This isZ(D 3), whereD 3 :∅→S 2
8. involutions∗ g :A g→A g
9. representationsρ g :MCG(Σ g)→Aut(A g).
8 and 9 come from the following construction: First note thatMCG(Σ g) here
means Diff +(Σg)/Diff +
0 (Σg), namely isotopy classes of orientation preserving diffeo-
morphisms. The representations send a particular orientation-preserving diffeomor-
phismd∈Diff +(Σg) toZ(Cyl(d)) whereCyl(d) is the mapping cylinder. In particu-
lar, there is a specific order 2 diffeomorphism giving rise to the involutions∗ g– this is
defined to be the diffeomorphism which sends the Σ g in its standard embedding inR 3
to itself after performing aπ-rotation about thez-axis.
The genus creation/reduction maps, and the splitting/merging maps are the images
of the trace of elementary surgeries on surfaces.
These data, along with appropriate compatibility conditions, fit into an algebraic
structure named “J-Algebras.” A theorem by [Juh18] is that these data completely
determine the 3-dimensional TFTZ. In fact, the statement is stronger:
Theorem 5.2.2.[Juhasz] The assignmentZ7→J(Z)is an equivalence between the
symmetric monoidal category of 3-dimensional TFTs andJ-Alg.
Here the categoryJ-Algis the category whose objects areJ-algebras and whose
morphisms areJ-algebra homomorphisms. We refer the reader to the original article
for the precise definition of such morphisms.
Our goal for this section is to briefly analyse wherePandLalgebras fit inside a
J-algebra.
The following data of theJ-algebra associated with a TFTZthat directly involves
the genus 0 piece:
1.A 0 =Z(S 2) is the vector space associated to the two-sphere.
2. linear mapsα 1 :A 1→A 0,
3. linear mapsδ 0,g :A g→A 0⊗Ag,
4. linear mapsµ g,0 :A g⊗A 0→A g,
5. linear mapsω 0 :A 0→A 1,
6. The linear maptr:A 0→k,
7. The linear map 1 :k→A 0,
8. involutions∗ 0 :A 0→A 0
9. representationsρ 0 :MCG(S 2)→Aut(A 0).
Note that 8 and 9 are actually both trivial for the following reason:MCGhere
means isotopy classes of orientation preserving diffeomorphisms, soMCG(S2) ={[id S2]}
75
is the group of one element. Thereforeρ 0 maps [idS2] trivially to the identity ofA 0.
The diffeomorphism ofS 2 defined by rotation about thez-axis byπis therefore also
isotopic to the identity, hence passing throughZgives the identity onA 0. By definition
this is the involution∗ g. Therefore we see that 8 and 9 contains no information.
Furthermore, we see that 6 and 7 agree with the unit and trace maps ofA 0 as a
commutative Frobenius algebra. In the caseg= 0,δ 0,g =m∨ andµ g,0 =mrecovers
the co/multiplication maps.
Therefore, the non-trivial information associated to the commutative Frobenius
algebraA 0 is the following:
2. the genus reduction mapα 1 :A 1→A 0
3. the splitting mapsδ 0,g :A g→A 0⊗Ag,g >0
4. the merging mapsµ g,0 :A g⊗A 0→A g,g >0
5. the genus creation mapω 0 :A 0→A 1.
Even though the four classes of maps above are the only maps in the data ofJ-
algebras that directly involvesA 0, they do not generate all relevant maps. For example,
they do not generate prime endomorphismse p :A 0→A 0 wherepis irreducible.
Theorem 5.2.3.The degree0part of everyJ-algebra is aP/L-algebra. Namely, every
J-algebra induces aP/L-algebra.
Proof.By theorem 5.2.2, for anyJ-algebraJthere exists a 3-dimensional oriented
TFTZ: Cob(3)→Vect k such thatJ(Z) =J, whereJ(Z) consists of the data 1-9
along with compatibility conditions. By theorem 5.1.10, every 3-dimensional TFTZ
determines aP/LalgebraZ(S 2).
This is an extremely unsatisfying proof. We will present a more geometric construc-
tion that illustrates preciselyhowthe data of aJ-algebra determines, for example, the
prime units. For this, we will need Heegaard Splitting.
Theorem 5.2.4.[Heegaard] LetMbe a connected closed oriented3-manifold. Then
there exists two handle bodiesM 1,M 2 of genusgand an orientation-reversing diffeo-
morphismf:∂M 1→∂M 2 such that
M∼=M1∪f M2.
Remark5.2.5.The Heegaard genusg(M) is defined as the minimal genus of all possible
Heegaard splitting ofM. In fact [Mar16], onlyS 3 (and thoseMdiffeomorphic to it)
hasg= 0, and only lens spaces (other thanS 3) orS 2×S 1 hasg= 1. All other
3-manifolds haveg≥2.
SinceM 1 is evidently diffeomorphic toM 1∪∂M1∂M1×[0,1], we may write
M∼=M1∪∂M1∂M1×[0,1]∪ f M2.
and after factoring through diffeomorphismsϕ 1,2 : Σg→∂M 1,2,
M∼=M1∪ϕ−1
1
Cyl(h)∪ ϕ2M2.
whereh=ϕ −1
2 ◦f◦ϕ 1 : Σg→Σ g is orientation preserving.
Therefore we have the following variant of the Heegaard splitting:
76
Theorem 5.2.6.LetMbe a connected closed oriented3-manifold. Then there exists
two handle bodiesM 1,M 2 of genusgandh∈Diff +(Σg)such that
M∼=M1∪ϕ−1
1
Cyl(h)∪ ϕ2M2.
whereCyl(h) = (Σ g×[0,1]⨿Σ g)/(x,1)∼h(x)is the mapping cylinder ofh,ϕ 1 :
Σg →∂M 1 is an orientation-preserving diffeomorphism, andϕ 2 : Σg →∂M 2 is an
orientation-reversing diffeomorphism.
and the boundary variant:
Theorem 5.2.7.LetMbe a connected closed oriented3-manifold with boundary
∂M ∼=⨿a+bS2. Then there exists two connected oriented 3-manifoldsM 1,M 2 with
boundaries∂M 1 =⨿ aS2⨿Σ 1 and∂M 2 =⨿ bS2⨿Σ 2, whereΣ 1,2 are of of genusg,
andh∈Diff +(Σg)such that
M∼=M1∪ϕ−1
1
Cyl(h)∪ ϕ2M2.
whereCyl(h) = (Σ g×[0,1]⨿Σ g)/(x,1)∼h(x)is the mapping cylinder ofh,ϕ 1 : Σg→
Σ1 is an orientation-preserving diffeomorphism, andϕ 2 : Σg→Σ 2 is an orientation-
reversing diffeomorphism.
Proposition 5.2.8.Given anyA=⊕ i≥0Ai anJ-algebra overk, and any irreducible
oriented3-manifoldP, let1 P :k→A 0 ande P :A 0→A 0 be a prime unit and a prime
endomorphism of theL-algebraA 0. Then there existsh∈MCG(Σ g)for somegsuch
that
1P =α 1◦α 2···◦α g◦ρg(h)◦ω g−1◦ωg−2◦···◦ω 0◦1.
and that
eP =α 1◦α 2···◦α g◦ρg(h)◦ω g−1◦ωg−2◦···◦ω 0.
Namely,1 P :k→A 0 is the composition
k 1→A 0
ω0
→A 1
ω1
→...
ωg−1
→A g
ρg(h)
→A g
αg
→A g−1
αg−1
→... α2
→A 1
α1
→A 0.
ande P :A 0→A 0 is the composition
A0
ω0
→A 1
ω1
→...
ωg−1
→A g
ρg(h)
→A g
αg
→A g−1
αg−1
→... α2
→A 1
α1
→A 0.
Proof.Applying theorem 5.2.7 toP\D 3 in the case (a,b) = (0,1), there exists a genusg
handle bodyM 1 and a connected closed oriented 3-manifoldM 2 with boundaryS 2⨿Σg
andh∈Diff +(Σg) such that
P\D 3∼=M1∪Cyl(h)∪M 2.
Recall that any handle body of genusgcan be obtained, by definition, by attaching
g-many 1-handles to a 0-handle. Hence in the case (a,b) = (0,1), we learn thatPis
built by first attachingg-many 1-handles to a 0-handle, which results inM 1. Then
we glue on a mapping cylinderCyl(h). Then we attachg-many 2-handles, which form
M2. We stop short of attaching the final 3-handle, which would had result in a closed
manifold.
Passing through the TFTZcorresponding to theJ-algebraA, and noting thatω i
is the image of the trace of 1-handle attachments whileα i is the image of the trace of
2-handle attachments, we obtain the desired composition for 1 P .
Doing the same toP\(D 3⊔D 3) in the case (a,b) = (1,1), we obtain the desired
composition fore P .
77
5.3 The∞-operadL ⊗
We now shift gears to the (∞,1)-categorical setting. In this exploratory section, we
aim to define an∞-operadL ⊗ and conjecture it as equivalent to the connected part
of the∞-endomorphism operad End ⊗
Ω2Bordfr
3
(S2). There is also an oriented version of
the proposal.
We will do this in steps: first we will briefly review the constructions of the∞-
littlen-cube operadE ⊗
n , then we will define the∞-operadL ⊗ and End⊗
Ω2Bord3
(S2),
and lastly we will give two precise conjectures which state that there exists a map of
∞-operads which is an equivalence.
Comment5.3.1.When we sayCis an∞-category we mean eitherCis a complete Segal
space or a quasi-category. Although it is usually clear from context which model we
are referring, we will default to using quasi-categories unless specified otherwise.
Many influential work on the bordism categories were done in the model of (n-fold)
complete Segal spaces such as[Lur08; CS19; Sch14], while∞-operads were explored by
[Lur17a] in the model of quasi-categories.
Both complete Segal spaces and quasi categories are valid models of (∞,1)-categories,
due to the fact that the homotopy theory of complete Segal spaces is the same as the
homotopy theory of Quasi-categories, hence one loses nothing by choosing a model. In
fact, one may move from one model to the other via [JT07] style constructions, such
as theorem A.2.3 in the appendix.
The following category will show up repeatedly in the section
Definition 5.3.2.(Fin ∗) Let⟨n⟩={∗,1,...,n}. The Segal category of finite pointed
setFin ∗ is defined to have
1. objects are⟨n⟩for eachn≥1.
2. a morphismα:⟨m⟩→⟨n⟩is a map such thatα(∗) =∗.
A morphismα:⟨m⟩→⟨n⟩isinertif for eachi∈1,...,n, the inverseα −1(i) has
only one element; it isactiveifα −1(∗) ={∗}.
Recall that an∞-operad as defined in [Lur17b] is a morphism of∞-categories
p:O ⊗→N(Fin ∗).
such that every inert morphism hasp-coCartesian lifts, the inert morphismsρ i⟨n⟩→
⟨1⟩sendingito 1 and everything else to∗induce “projection maps,” and there is
equivalence of∞-categoriesO ⊗
⟨n⟩→O n whereO ⊗
⟨n⟩≡p−1(⟨n⟩),O≡O ⊗
⟨1⟩. A precise
definition is recorded in A.2.13.
First let’s recall the standard construction of the∞-little k-cube operadE ⊗
k .
Let□ k = (−1,1)k be thek-dimensional open cube. We say an embeddingf:□ k→
□k is rectilinear if it is given by
f(x 1,...,x k) = (a1x1 +b 1,...,a kxk +bk).
for some constantsa i >0 andb i. For any finite setS, we say an open embedding
□k×S→□ k is rectilinear if it is rectilinear on each connected component. Denote
all such rectilinear embeddings as Rect(□ k×S,□ k) and equip it with the subspace
topology ofR 2k|S|. Note that the images of the|S|-many□ k are disjoint by definition.
78
Definition 5.3.3.Let tE⊗
k be the topological category defined as follows
1. The objects are⟨n⟩, the same as those ofFin ∗
2. An arrowf:⟨m⟩→⟨n⟩consists of the following data:
(a) a morphismα:⟨m⟩→⟨n⟩inFin ∗.
(b) for each 1≤j≤n, a rectilinear embedding in
Rect(□k×α−1(j),□k).
3. The topology on the mapping spaces Map tE⊗
3
(⟨m⟩,⟨n⟩) is induced by the presen-
tation
MaptE⊗
3
(⟨m⟩,⟨n⟩) =
a
α:⟨m⟩→⟨n⟩
Y
1≤j≤n
Rect(□k×α−1(j),□k).
4. The composition
MaptE⊗
3
(⟨n⟩,⟨n′⟩)×Map tE⊗
3
(⟨n′⟩,⟨n′′⟩)→Map tE⊗
3
(⟨n⟩,⟨n′′⟩).
sendsα:⟨n⟩,⟨n ′⟩,β:⟨n ′⟩→⟨n ′′⟩toβ◦α:⟨n⟩→⟨n ′′⟩, and the rectilinear
embeddings
fj :□ k×α−1(j)→□ k, f ′
j′ :□ k×β−1(j′)→□ k.
are sent to
f′
j′◦(
a
j∈α−1(β−1(j′))
fj) :□ k×(β◦α) −1(j′)→□ k.
We call tE⊗
k the topological littlek-cube operad.
Define the∞-categoryE ⊗
k as the topological nerve of tE⊗
k .
Proposition 5.3.4.E ⊗
k is an∞-operad.
Definition 5.3.5.We callE ⊗
k the∞-littlek-cube operad.
Remark5.3.6.There are many variations to definition 5.3.3 by replacing the spaces
Rect(□k×α−1(j),□k) by some other ones. There are two important variants:
1. One may replace□ k withD k, and define a rectilinear embeddingD k→D k as
one which extends toR k→R k asv7→λv+v 0 for someλ>0 andv 0∈R k. That
is, a uniform radial scaling and a translation. The resulting topological category
is referred to as the “littlek-disk operad” and its topological nerve is once again
an∞-operad, rightfully called the “∞-littlek-disk operad.”
By [May97] and [LV14], for any finite setSthere is a canonical homotopy equiva-
lence between Rect(□k×S,□ k), Rect(Dk×S,D k) and Conf|S|(Rk) the configura-
tion space of|S|-many distinct points inR k. Hence the topological littlek-cube
operad is homotopy equivalent to the topological littlek-disk operad. Passing
through the homotopy coherent nerve gives an equivalence between the∞-little
k-cube operad and the∞-littlek-disk operad.
79
2. One may replace□ k withD k, and define a “projective isometry”f:D k→D k
as one which extends toR k→R k asv7→λRv+v 0 for someR∈SO(k),λ >0
andv 0 ∈R k. That is, a rotation followed by a uniform radial scaling, then
a translation. The resulting topological category tE⊗
SO(k) is referred to as the
“framed littlek-disk operad” and its topological nerveE ⊗
SO(k) is once again an
∞-operad, rightfully called the “∞-framed littlek-disk operad.”
This operad (both the topological and the∞-version) is not equivalent to the
ordinary littlek-disk/cube operad fork≥2. Heuristically speaking, theSO(k)
rotational information assigned to the embedded disks is the classifying space
BSO(k). Whenk≥2 this space is no longer contractible, hence the homotopy
theory of projective isometries is different from the homotopy theory of rectilinear
embeddings.
3. Similar to variation 2, one may further allowR∈O(k) to include orientation
reversal. The resulting topological category is denoted tE⊗
O(k) and the topological
nerveE⊗
O(k) is an∞-operad.
Example 11.It is widely understood thatS k−1 is anE ⊗
k -algebra object in Bord fr
k .
Precisely, this means that there is a map of∞-operads
E⊗
k →Ω k−1 Bordfr,⊗
k .
sending⟨1⟩to the objectS 2.
Additionally,Sk−1 is understood to be anE⊗
SO(k)-algebra object in Ωk−1 BordSO(k),⊗
k ,
and anE⊗
O(k)-algebra object in Ωk−1 BordO(k),⊗
k . 3 Though, at the time of this writing,
we are not aware of a thorough treatment in existing literature.
Recall [Hat08]’s construction of the space of connect sum configurations:
Notations 5.3.7.LetGbe a graph andvbe a vertex. LetHE(v) =DE(v)∪E(v)
be the set of half edges ofv, written as a union of unpaired half edgesDE(v) and the
paired half edgesE(v). We sayvhas valency|E(v)|and deficiency|DE(v)|.
Definition 5.3.8.(C(M)) LetM=P 1#...#P m#(S2×S 1)g be a closed oriented
3-manifold, whereP i are oriented irreducible 3-manifolds. LetGbe a finite connected
graph withmof its vertices labelled 1,...,mand such that all unlabelled vertices have
valence≥3 and the fundamental group is free of rankg. Let
CG(M) =

(re,le,D 3
e ,→Pi,D 3
e ,→S 3
v)
	
over all edgeseand all unlabelled verticesvofG, wherer e>0,l e>0 and embeddings
D3
e ,→Pi andD 3
e ,→S 3
v, the latter being an isometry on its boundary. Let CG(M)
be the same asC G(M) except now allowl e to go to 0. LetG/edenote the graph by
contracting the edgee. Then define
C(M) =
a
G
CG(M)/∼.
where a configuration withl e = 0 is identified with the same one after contracting the
edgee.
3Note the infamous trap in naming conventions: associated to theframedlittlek-disk operad isS k−1 as
anorientedmanifold.
80
The spaceC(M) is best thought of as all the possible ways to “build ”MfromP i
factors. To incorporate spherical boundaries, we need to introduce unpaired half edges
corresponding toS 2 boundaries, one of which is distinguished and corresponds to the
outgoing boundary.
Definition 5.3.9.(C ∂,n
SO (M)) LetM=P 1#...#P m#(S2×S 1)g be a closed oriented
3-manifold, whereP i are oriented irreducible 3-manifolds. LetGbe a finite connected
graph withmof its vertices labelled 1,...,mand such that all unlabelled vertices
have valence≥3 and the fundamental group is free of rankg, and such that it has
n+ 1-many unpaired half edges, one of which is distinguished. Let
C∂,n
SO,G(M) =

(re,le,D 3
e ,→Pi,D 3,→S 3
v,D 3
ϵ ,→Pi,D 3
ϵ ,→S 3
v)
	
over all edgeseand all unpaired half edgesϵand all unlabelled verticesvofG, where
re>0,l e>0 and embeddingsD 3
e ,→Pi andD 3
e ,→S 3
v, the latter being an isometry on
its boundary. The half-edge embeddingsD 3
ϵ ,→Pi,D 3
ϵ ,→S 3
v are orientation-preserving
and have disjoint images. Let C∂,n
SO,G(M) be the same asC ∂,n
SO,G(M) except now allow
le to go to 0. LetG/edenote the graph by contracting the edgee. Then define
C∂,n
SO (M) =
a
G
C∂,n
SO (M)/∼.
The spaceC ∂,n
SO (M) isC(M) but now one remembers incoming and outgoing spheri-
cal boundary data. This is the oriented version– all the irreducible factors are oriented,
and all edge embeddingsD 3
e ,→S 3
v,D 3
e ,→Pi oriented, and the boundary embeddings
D3
ϵ ,→S 3
v,D 3
ϵ ,→Pi (those corresponding to half edges) are also oriented.
VariationThere exists an obvious variation, one where we upgrade the orientation
to the more restrictive framed setting. Call the spaceC ∂,n
fr (M), whereMis now a
framed closed 3-manifold, and theP i factors are also framed. All embeddings are
framing-preserving embeddings. 4
Remark5.3.10.The definition for the configuration space of the un-oriented case is less
straightforward, so we won’t attempt to present it here. However, we can make some
suggestions. Call this configuration spaceC ∂,n
O (M), whereM=P 1#...#P m#(S2×
S1)g#(S2∼
×S 1)g′
. In the unoriented case there exists a reducible primeS 2e×S1 which
is aS 2 bundle overS 1, defined as
S2e×S1 =S 2×[0,1]/(x,0)∼(r(x),1).
wherer:S 2→S 2 is the antipodal map, in particular orientation reversing. 5 Hence
we need the underlying graphs to have fundamental groups free of rankg+g ′.
We would need the attaching tubesD 3
e×I e as well as the orientation-reversing
version of these tubes, defined as
 
D3
e×Ie
a
D3/(x,1)∼r(x).
wherer:D 3×D 3 is again the antipodal map.
4We will be intentionally vague about this, since this is only a sketch definition.
5UnlikeS 2×S 1 where the identification can be made as (x,0)∼(x,1).
81
Setting aside the issue of the unoriented configuration space, we define an operad
which captures the information in the oriented configuration space:
Definition 5.3.11.( tL⊗) is a topological category defined as follows
1. The objects are⟨n⟩, the same asFin ∗.
2. A morphism from⟨m⟩to⟨n⟩consists of the following data:
(a) a morphismα:⟨m⟩→⟨n⟩inFin ∗
(b) for everyj= 1,...,n, a non-negative integerg j≥0 and an elementh j∈
BDiff(‘
i∈IjPi), whereP i are framed irreducible 3-manifolds.
(c) for everyj= 1,...,n, a framed connect sum configurationf j∈C ∂,|α−1(j)|
fr (M)
whereM=
 
#i∈IjPi

#(S2×S 1)gj.
3. Composition is given by
(a) sendα:⟨m⟩→⟨n⟩andβ:⟨n⟩→⟨n ′⟩to the compositionβ◦α:⟨m⟩→⟨n ′⟩.
(b) Ifg j≥0,h j∈BDiff(‘
i∈IjPi) forj= 1,...,n ′ andgk≥0,h k∈BDiff(‘
i∈IkPi)
fork= 1,...,n ′′ are the data to be composed, their composition is given by
gk =g k +P
j∈α−1(k)gj and hk is the image of (h j,hk)j∈α−1(k) under the
natural map

 Y
j∈α−1(k)
BDiff

a
i∈Ij
Pi



×BDiff

a
i∈Ik
Pi

→BDiff(
a
i∈∪j∈α−1(k)Ij∪Ik
Pi).
(c) Iff j forj= 1,...,n ′ andf k fork= 1,...,n ′′ are the framed connect sum
configurations over the graphsG j andG k respectively, their composition
fk is a configuration over the graph Gk obtained by connecting the incom-
ing half-edges ofG k with the outgoing half-edges of

Gj,j∈α −1(k)
	
. The
configurationfk itself is the union of the configurations{f j}j∈α−1(k) andf k.
Remark5.3.12.The natural map in item 3.b requires some explaining. There is a
natural map
BDiff(X)×BDiff(Y)→BDiff(X
a
Y).
which is induced by the natural map Diff(X)×Diff(Y)→Diff(X ‘Y). IfXis not
diffeomorphic toY, the target is just Diff(X)×Diff(Y) and this map is the identity.
IfXis diffeomorphic toY, however, the target now must include the diffeomorphism
swapping the two, which is a separate path component from the identity component.
In our model of BDiff(X) = Emb(X,R ∞)/Diff(X), we can give a geometric con-
struction. Fix two embeddings
i0,i 1 :R∞→R∞.
with disjoint images. Then send [e X]∈BDiff(X) = Emb(X,R ∞)/Diff(X) and [e Y ]∈
BDiff(Y) = Emb(Y,R ∞)/Diff(Y) to the class of embeddingX ‘Y→R ∞ given by
x7→i 0(eX(x)), y7→i 1(eY (y)).
This is well defined because precomposinge X ande Y by diffeomorphisms corresponds
to precomposing the union embedding by an element of Diff(X ‘Y).
82
VariationDefine tL⊗
SO similarly, except now 2.b theP i are oriented irreducible
3-manifolds, and 2.c the configurationf j∈C ∂,|α−1(j)|
SO (M) is an oriented connect sum
configuration.
Definition 5.3.13.Denote byL ⊗ the topological nerve of tL⊗, and byL⊗
SO the topo-
logical nerve of tL⊗
SO.
Proposition 5.3.14.The∞-categoriesL ⊗ andL⊗
SO are∞-operads.
Proof.We show that Sing(tL⊗) is canonically isomorphic to the simplicial categoryO⊗,
constructed via [Lur17b, Notation 2.1.1.22], of a fibrant simplicial coloured operadO.
ThereforeL⊗ =N(Sing( tL⊗)) =N(O ⊗) =N ⊗(O) is the operadic nerve ofO, which
by [Lur17b, Proposition 2.1.1.27] is an∞-operad.
LetObe the simplicial coloured operad with a single objectD 3, with
MulO(

D3	
i∈I,D 3) = Sing(MaptL⊗(⟨n⟩,⟨1⟩)a)
wherea:⟨n⟩→⟨1⟩is the unique active map, sending∗to∗and everything else to 1,
and MaptL⊗(⟨n⟩,⟨1⟩)a is the subspace of morphisms with dataaas the map inFin ∗.
The singular complex of any topological space is Kan. SoOis a fibrant simplicial one-
coloured operad. By construction, there is a canonical isomorphism between Sing(tL⊗)
andO⊗. HenceL ⊗ is an∞-operad.
The proof for the oriented version is analogous.
The∞-operadL ⊗ has a few notable sub-operads, induced by sub-categories of tL⊗.
Same goes for the oriented versionL⊗
SO. We shall introduce them below and show that
one of them is equivalent toE ⊗
3 .
Definition 5.3.15.( tL∗,⊗) Consider the subcategory tL∗,⊗ of the topological category
tL⊗ defined by
1. The objects are⟨n⟩, the same as before and as those ofFin ∗.
2. A morphism from⟨m⟩to⟨n⟩consists of the following data:
(a) a morphismα:⟨m⟩→⟨n⟩inFin ∗.
(b) for everyj= 1,...,n, a framed connect sum configurationf j∈C ∂
fr,G(S3)⊂
C∂
fr (S3), whereGis the graph with a single vertexvandd≥1 unpaired
half-edges.
3. The composition is the same as those of tL⊗.
Remark5.3.16.This is a subcategory of tL⊗ because we have chosen allg j to be 0,
and allh j∈BDiff(∅) to be the unique point. 6 ThenM,which is supposed to appear
in the configurationC ∂
fr (M), is now the unit under connect sum, which isS 3.
Definition 5.3.17.LetL ∗,⊗ be the topological nerve of tL∗,⊗. It is an∞-operad.
Moreover, it is an∞-sub-operad ofL ⊗.
6There is a unique functionf:∅→∅which is vacuously smooth and vacuously its own inverse. Hence
Diff(∅) ={f}. Recall that our model for the classifying spaces is BDiff(M) ∼= Emb(M,R∞)/Diff(M). There
is only one map from the empty set to any (possibly empty) set:e:∅→S, which is vacuously a smooth
embedding whenS=R ∞. Hence BDiff((∅)) ∼=∗the one-point space in our model.
83
Proposition 5.3.18.There is a canonical isomorphism between tL∗,⊗ and tE⊗
3 .
Proof.The two topological categories have the same objects. So we only need to show
that they agree on morphisms. Fix aj= 1,...,n. A framed connect sum configuration
fj∈C ∂
fr,G(S3) whereGis the single vertexvgraph withd≥1 unpaired half edges is
a tuple
fj = (D3
ϵ ,→S 3)ϵ∈DE(v).
where the embeddings are rectilinear and whose images are disjoint. HereDE(v) is
the set of half-edges at the only vertexv. We may delete the interior of the image of
the rectilinear embeddingD 3
ϵ! ,→S 3 corresponding to the one distinguished half-edge
ϵ!∈DE(v). After which we are left with a collection of rectilinear disjoint embeddings
D3
ϵ ,→(S 3\int(im(D 3
ϵ!)))∼=D3, ϵ∈DE(v)−ϵ !.
We may identify this with the morphisms of tE⊗
3
Rect(D3×α−1(j),D 3).
whered=|α −1(j)|+ 1.
Corollary 5.3.19.There is a canonical isomorphism of∞-operads betweenL ∗,⊗ and
E⊗
3 . Moreover,E ⊗
3 is an∞-sub-operad ofL ⊗.
Another sub-operad of interest is the “spike ball” operad, defined below.
Definition 5.3.20.(Spike Ball Operad) The “spike ball” operad tL⋆,⊗ is the subcat-
egory of the topological category tL⊗ defined by
1. The objects are⟨n⟩, the same as before and as those ofFin ∗.
2. A morphism from⟨m⟩to⟨n⟩consists of the following data:
(a) a morphismα:⟨m⟩→⟨n⟩inFin ∗.
(b) for everyj= 1,...,n, an elementh j∈BDiff(‘
i∈IjPi), whereP i are framed
irreducible 3-manifolds.
(c) for everyj= 1,...,n, a framed connect sum configurationf j∈C ∂,|α−1(j)|
fr,G (M)⊂
C∂,|α−1(j)|
fr (M), whereM= # i∈IjPi, andGis a graph with an unlabelled
vertexvand|α −1(j)|unpaired half edges atv, and connected tovare
Ij-labelled vertices. SoGis the star graph with one central vertexvand
|Ij|-many leaves, wherevalso has|α −1(j)|unpaired half-edges.
3. The composition is the same as those of tL⊗.
An example of the type of star graphGcan be found in figure 5.1-(a). LetL ⋆,⊗ be
the topological nerve of tL⋆,⊗. It is an∞-category and moreover an∞-operad. Call
it the “∞-spike-ball operad.”
Remark5.3.21.This is a subcategory of tL⊗ because we have chosen allg j to be 0.
Also note that tL∗,⊗ is a subcategory of tL⋆,⊗, where for anyj= 1,...,n,I j =∅so
there are no irreducible factors in BDiff( ‘
i∈IjPi).
Corollary 5.3.22.E ⊗
3 is an∞-sub-operad ofL ⋆,⊗.
84
1 2
P1 P2
(a) (b)
Figure 5.1: (a) An example of the star graphGin the spike ball operad. In this particular
case,Ghas|α −1(j)|+1 = 3 half edges, andI j ={1,2}labelled vertices. (b) illustrate the
particular bordism [M]∈BDiff(M)represented byGand the connect sum configurationf.
The two dashed spheres are considered incoming, and the distinguished half edge is the big
sphere, considered outgoing.
Lastly, we need to define the∞-endomorphism operad ofS 2. This is most easily
done using complete Segal spaces as there is previous work by Calaque and Scheim-
bauer.
Definition 5.3.23.LetVbe a finite dimensional real vector space. Define
 
PΩn−1BordV
n

k
to be the set of tuples
(M,t 0,...,t k).
such that
1.t 0≤t 1≤···≤t k an ordered tuple ofk+ 1 real numbers.
2.Mis a closedn-dimensional submanifold ofV×Rand the compositionπ:M ,→
V×R↠Ris proper.
3. For each 0≤i≤k, and eachx∈π −1(ti), the mapπis submersive atx.
Viewing
 
PΩn−1BordV
n

k as a subspace of
Sub(V×R)×R k+1,Sub(V×R) =
a
[M]
Emb(M,V×R)/Diff(M).
we equip it with the subspace topology.
Note that
 
PΩn−1BordV
n

• is a simplicial space. The simplicial face maps are given
by forgetting at, and the simplicial degeneracy maps are given by duplicating at.
LetPΩ n−1Bordn = lim−→V⊆R∞PΩn−1BordV
n . At thek-th level, we may think of it
to consist of tuples
(M,t 0,...,t k).
whereMis now a closedn-dimensional submanifold ofR ∞ (technicallyR∞×R).
Claim 5.3.24.PΩ n−1Bordn is a Segal space.
85
Definition 5.3.25.We define the (∞,1) category ofn−1 manifolds and bordisms
as the completion of the Segal spacePΩ n−1Bordn. Loosely speaking this category
consists of the following data:
•The objects are closedn−1 manifolds, corresponding to then−1 dimensional
preimageπ−1(t0)⊂MwhereMis ann-manifold.
•The 1-morphisms are compact bordisms, corresponding to then-dimensional
preimageπ−1([t0,t 1])⊂M.
•The 2-morphisms are diffeomorphisms between bordisms.
•The 3-morphisms are isotopes of diffeomorphisms
•...
VariationsBy demanding the manifolds ofPΩ n−1 Bordn be framed or oriented, we
obtain the standard framed or oriented variations of Ωn−1 Bordn, denoted as Ωn−1 Bordfr
n
or Ωn−1 BordSO
n .
Comment5.3.26.There are a few versions ofPBord V floating in the literature. They
differ mostly on condition 3. The original sketch was proposed by [Lur08], which was
later corrected by [CS19] . Our definition most closely resembles that of [Jor16], which
was adapted from [CS19].
Remark5.3.27.IfCis a symmetric monoidal (∞,n)-category with unit1, then ΩC=
EndC(1) = HomC(1,1) is a symmetric monoidal (∞,n−1)-category. As the notation
suggests, Ωk−1Bordk has an alternative construction as thek−1 looping of the (∞,k)-
categoryBord k. In fact, this construction is more precise than the one we presented
above– see [CS19] if our presentation is insufficient.
Remark5.3.28.The (∞,1)-category Ω n−1Bordn inherits a symmetric monoidal struc-
ture fromBord n. We shall be intentionally vague about what we mean by “symmetric
monoidal structure.” Beyond the heuristics of disjoint union, a precise definition can
be found in [Scheimbauer]. The symmetric monoidal category Ω n−1Bordn determines
7 an∞-operadp: Ω n−1Bord⊗
n →N(Fin ∗). Roughly speaking, the fibre ofpover
⟨m⟩consists ofm-tuples ofn−1 dimensional closed manifolds, and a morphism over
α:⟨m⟩→⟨m ′⟩is a bordism.
Definition 5.3.29.(Endomorphism operad) Givenp:C ⊗ →N(Fin ∗) be an∞-
operad, and letX∈ Cbe an object. By definition there is an equivalenceC ⊗
⟨n⟩
∼=
Cn induced by the inert mapsρ i :⟨n⟩ → ⟨1⟩. LetX n denote the object ofC ⊗
⟨n⟩
corresponding to then-tuple (X,...,X)∈C n. The∞-endomorphism operad ofXis
defined as the full∞-suboperad
End⊗
C (X)⊆C ⊗.
spanned by the objectsX n in each fiberC ⊗
⟨n⟩.
Notations 5.3.30.Let Mul C({X}1≤i≤n,Y) denote the union of the components of
MapC⊗(Xn,X) over the unique (active) map⟨n⟩→⟨1⟩sending∗to∗and everything
else to 1.
7More precisely, one extracts a quasi-category via [Joyal Tierney]. This quasi-category is the∞-category
which is symmetric monoidal in the sense of Lurie HA, and it is the underlying∞-category of the∞-operad
Ωn−1Bord⊗
n .
86
Heuristically, the∞-endomorphism operad ofXis the one-coloured∞-operad
whose multimorphisms are given by those ofC:
MapEnd⊗
C (X)(Xn,X) = MulC({X,...,X},X).
Definition 5.3.31.Let Ω n−1Bordn be the symmetric monoidal∞-category ofn-
dimensional bordisms. The∞-endomorphism operad ofS n−1 is End⊗
Ωn−1Bordn
(Sn−1).
The connected∞-endomorphism operad ofS n−1 is the sub-operad
End⊗,conn
Ωn−1Bordn
(Sn−1),→End ⊗
Ωn−1Bordn
(Sn−1)
consisting of connected bordisms.
Similarly, we define the framed∞-endomorphism operad End ⊗
Ωn−1Bordfr
n
(Sn−1), its
connected sub-operad End⊗,conn
Ωn−1Bordfr
n
(Sn−1) and the oriented∞-endomorphism operad
End⊗
Ωn−1BordSOn
(Sn−1), along with its connected sub-operad End⊗,conn
Ωn−1BordSOn
(Sn−1).
Conjecture 5.3.32.There is a map of∞-operadsf:L ⊗→End⊗
Ω2 Bordfr
3
(S2), whose
image is End ⊗,conn
Ω2 Bordfr
3
(S2). Furthermore,fis an equivalence of∞-operadsL ⊗ ∼→
End⊗,conn
Ω2 Bordfr
3
(S2).
Conjecture 5.3.33.There is a map of∞-operadsf SO :L ⊗
SO →End ⊗
Ω2 BordSO
3
(S2),
whose image is End ⊗,conn
Ω2 BordSO
3
(S2). Furthermore,f SO is an equivalence of∞-operads
L⊗
SO
∼→End⊗,conn
Ω2 BordSO
3
(S2).
Remark5.3.34.The reason behind the proposal is this: by Hatcher’s unfinished draft
[Hat08], which was proven by [BBS26], for every oriented 3 manifoldMwhose irre-
ducible factors areP 1,...,P m, with possibly finitely many irreducible prime factors
S2×S 1, then there exists a homotopy fibre sequence
C(M)→BDiff(M)→BDiff(
a
1≤i≤m
Pi).
whereC(M) is the space of connect sum configurations, and the second map is roughly
the splitting ofM ,→R∞ along splitting spheres, resulting in a collection of irreducible
factors withD 3 removed and embedded inR ∞. We then cap the missing balls, which
give the boundary-less irreducible factors ‘
iPi,→R∞.
A multimorphism in any of the above∞-endomorphism operads is a bordism from
copies ofS 2 to a single outgoingS 2. Such a bordism is an element (M,t 0,t 1) of
BDiff(M)×R 2∼= Emb(M,R∞)/Diff(M)×R 2.
Hence in order to model the multimorphisms by an operad, we need the operad to
essentially have BDiff(M) built in, as well as ways to specify its boundaries. The space
of connect sum configurationsC(M) in the homotopy fibration, over a base point, is our
intended carrier of this information. To specify the boundaries, we modified he space of
connect sum configurations to include embeddingsB 3,→S 3,Pi corresponding to newly
introduced half edges. Hence the operadL ⊗ and the oriented cousinL ⊗
SO has exactly
87
enough information to start from a collection of irreducible 3-manifolds ‘
iPi ,→R∞
and form a connect sum through a connect sum configurationf∈C ∂
fr (M) orC ∂
SO(M).
The configurationfalso specifies where along the bounding 3-balls are, so one could
remove their interior.
Example 12.Recall thatL ⊗ has an∞-suboperadL ⋆,⊗, the “spike-ball”∞-operad.
Consider a subset of morphism of⟨1⟩→⟨1⟩given by the following data
1. the morphismα:⟨1⟩→⟨1⟩is the identity inFin ∗.
2. an elementh∈BDiff(P) wherePis any fixed framed irreducible 3-manifold.
3. A configurationf∈C ∂,1
fr,G(P), whereGis the graph with a single unlabelled
vertexvconnected via the edgeeto a single labelled vertexp, where there are
two additional unpaired half edges{ϵ 1,ϵ 2}at the unlabelled vertexv: figure 5.2
1
P1
(a)
(b)
Figure 5.2: A simple spike ball example. (a) gives the graphG. (b) provides a visualization
for the bordism represented byGand a connect sum configurationf.
The configurationfis equal to the following data
(re,le,D 3
e ,→S 3
v,D 3
e ,→P,D 3
ϵ1 ,→S 3
v,D 3
ϵ2 ,→S 3
v).
where all the embeddings inS 3
v are rectilinear and have disjoint images. We may delete
the interior of the image of one of the half-edges, sayD 3
ϵ2, so what remains ofS 3
v is
diffeomorphic to a ballD 3. Then the configurationfcontains the following data
(re,le,D 3
e ,→D 3,D 3
e ,→P,D 3
ϵ1 ,→D 3).
Note that there exists a map
Conf2(D3)×BDiff(P)→L ⋆,⊗.
Sending a configuration of 2 points inD3 to the centre of the embeddingsD3
e,D 3
ϵ1 ,→D 3
and an elementh∈BDiff(P) to the chosen element as part of the data of⟨1⟩→⟨1⟩.
Taking the inclusion into the operadL ⊗, passing through the endomorphism operad,
and finally through a TFTZ, we get a map
Conf2(D3)×BDiff(P)→L ⋆,⊗,→L⊗→End⊗
Ω Bordfr
3
(S2)→End ⊗
C (Z(S 2)).
88
whose image is over the 1-ary operations. Therefore there is a map
Conf2(D3)×BDiff(P)→Map C(Z(S 2),Z(S 2)).
for any TFTZ: Ω 2 Bordfr
3 →Cand for any framed irreducible 3-manifoldP.
89
Appendix A
Appendix: Definitions and
Common Results

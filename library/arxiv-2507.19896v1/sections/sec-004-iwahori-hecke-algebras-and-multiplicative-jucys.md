---
doc_id: arxiv-2507.19896v1
doc_title: "Generalized Markov traces and Jucys-Murphy elements"
section_id: sec-004-iwahori-hecke-algebras-and-multiplicative-jucys
section_title: "Iwahori-Hecke algebras and multiplicative Jucys-Murphy elements."
section_number: null
pages: 2-4
source_pdf: 2507.19896v1.pdf
source_sha256: a3f23d5a08b397ee
doc_brief: "Generalized Markov traces and Jucys-Murphy elements — WegiveasimpleconstructionofMarkovtracesforIwahori-Heckealgebrasassociated with infinite series of crystallographic Coxeter groups."
---
2.1 Coxeter groups. Let (W,S ),S ={s1,...,s n}, be a Coxeter system. Thus,W
is a group with a presentation(s0,...,s n|(sisj)mij =e), wheremij∈ Z+∪{∞}, with
mii = 1,mji =mij≥ 2 if i̸=j, andmij =∞ means that there is no relation included
for the pairsi,sj. Such a presentation is read off the Coxeter diagram of(W,S ) in a
standard way: such a diagram is a non-oriented graph withS as a set of vertices, and
mij− 2 edges between the verticessi and sj. Let l : W→ Z≥0 be the Bruhat length
function with respect toS.
We will be primarily interested in Coxeter groups that are Weyl groups of classical
types A,B = C,D. To fix the numeration of the generators, their Coxeter diagrams
are presented below, with a vertex corresponding tosi∈S marked byi. The Coxeter
diagram of typeAn is
nn− 121
,
of typeBn =Cn is
n− 110
,
and of typeDn is
n− 12
1
1′
.
Whenn is small, these are interpreted in a standard way as follows: the Coxeter system
A1 = B1 = D1 has a single vertex,D2 = A1×A1, D3 = A3. We also adopt the
conventionA0 = B0 = D0 corresponding to the empty Coxeter graph and the trivial
Coxeter group.
2
Many of the results and definitions in this paper are valid in types all typesA,B,D ,
with definitions for typeAn−1 naturally fitting with definitions in typesBn,Dn. In this
case, we will write “typeXn, whereX isA−1,B orD” (or something in a similar vein).
2.2 Iwahori-Heckealgebras. LetA = Q(v). TheIwahori-Heckealgebra Hv(W,S ) =
H(W,S ) associated to a Coxeter system(W,S ) is a unitalA-algebra with generators
ts,s∈S, subject to the relations
(i). ⟨tsi,tsj⟩mij =⟨tsj,tsi⟩mij, where⟨x,y⟩m is an alternating productxyx... of x
and y with m factors.
(ii). (ts−v)(ts +v−1) = 0.
When (W,S ) is of type Bn we will also be interested in the Iwahori-Hecke algebra
Hv,v0(W,S ) with unequal parametersv,v 0∈A . This is a unital algebra over the ring
A, with the relation (ii) replaced by the relations
(ii'). (tsi−v)(tsi +v−1) = 0 for i> 1,
(ii''). (tsi−v0)(tsi +v−1
0 ) = 0.
When (W,S ) is of typeXn with X ∈{ A,B = C,D}, we will writeW (Xn) and
H(Xn) for W andH(W,S ), orHv,v0(Bn) if we need to emphasize that we use unequal
parameters. In each of these cases, we will writeti for tsi.
Let w = si1...s ir,w ∈ W,sik ∈ S be a reduced expression. Then the element
tw = tsi1...t sir inH(W,S ) is independent of the choice of a reduced expression, and
H(W,S ) is a freeA-module with a basistw,w ∈ W. The elements tw are invertible,
and the collectiont−1
w ,w∈W, gives another basis ofH(W,S ) overA.
2.3 Trace functional and a pairing on H(W,S ). Let x7→ x be the Kazhdan-
Lusztig involution onH(W,S ). It is aQ-algebra involution, defined by the assignments
v = v−1,tw = t−1
w−1. Let i :H(W,S ) stand for theA-linear algebra anti-involution
defined byi(tw) =tw−1.
Forh∈H (W,S ),x ∈ W, let hx stand for thet−1
x -coefficient ofh in the basist−1
w ,
where w runs throughW. Let τ :H(W,S )→A be a functional defined byτ(h) = he,
where e∈W is the unit. Forh,h′∈H (W,S ), define a pairing⟨h,h′⟩ =τ(i(h)h′). We
have the following standard proposition, see, for example, [GP00, Chapter 8].
Proposition 2.3.1. The functionalτ and the pairing⟨,⟩ satisfies the following prop-
erties.
(a). The functionalτ is anA-linear trace onH(W,S ), that isτ(hh′) =τ(h′h).
(b). The pairing⟨,⟩ isA-antilinear in the first argument,A-linear in the second ar-
gument and satisfies the orthogonality relation⟨tw1,t−1
w2⟩ =δw1,w−1
2
.
(c). We have⟨h1h2,h 3⟩ =⟨h1,h 3i(h2)⟩ =⟨h2,i (h1)h3⟩ for anyh1,h 2,h 3∈H (W,S ).
We will use the following straightforward corollary of this proposition repeatedly.
Corollary 2.3.2. Let (W′,S′) be a parabolic subgroup ofW. Assume that x,y ∈
H(W′,S′) ⊂ H(W,S ), and assume that z ∈ spanA⟨tw,w ∈ W\W′⟩ (resp. z ∈
spanA⟨t−1
w ,w∈W\W′⟩). Then⟨xz,y⟩ =⟨zx,y⟩ = 0 (resp.⟨x,yz⟩ =⟨x,zy⟩ = 0).
3
2.4 “Full twist” and Jucys-Murphy elements. Assume that (W,S ) is of finite
type. Letw0 stand for the longest element inW with respect to the Bruhat length. Let
S(W,S ) =t−2
w0∈H (W,S ). In classical types, we will writeS(Xn)∈H (Xn), whenX is
A,B or D, or simplyS when the type is clear from the context.
The following proposition is also standard:
Proposition 2.4.1. The element S(W,S ) is central inH(W,S ).
We will need the following “Serre property” of the operator of multiplication by
S(W,S ).
Proposition 2.4.2. For anyh1,h 2∈H (W,S ) we have the identity
⟨h1, S(W,S )h2⟩ =⟨h2,h 1⟩.
Proof. Itisenoughtoprovethepropositionfor h1 =t−1
w1,h 2 =tw2 forarbitrary w1,w 2∈
W. We have, by Proposition 2.3.1 (c),
⟨t−1
w1, S(W,S )tw2⟩ =⟨tw0t−1
w1,t−1
w0tw2⟩ =⟨tw0w−1
1
,t−1
w−1
2 w0
⟩ =
=δw0w−1
1 ,w0w2
=δw1,w−1
2
=⟨tw2,t−1w1⟩.
This completes the proof.
We have the natural embeddingιn :H(Xn)→H (Xn+1), where X is A,B or D,
induced by the embedding of the sets of labels of the Coxeter diagram. Using these
embeddings, an element ofH(Xn) can be considered as an element ofH(Xm) form>n .
Definition 2.4.3. Forn≥ 2, letJX
n = S(Xn)−1· S(Xn−1) when X is A−1,B or D.
We letJA
1 = 1,JB
1 = t2
0, JD
1 = 1. We call these elementsJucys-Murphy elements of
finite Hecke algebras in classical types.
We have the following corollary of Proposition 2.4.1.
Corollary 2.4.4. ForX equal toA−1,B or D, elementsJX
k commute with each other
when considered lying in the same Iwahori-Hecke algebra via the embedding described
above. The elementJX
n lies in the centralizer ofH(Xn−1) inH(Xn).
Remark 2.4.5. The elementsJA
k are sometimes called multiplicative Jucys-Murphy
elements in the Iwahori-Hecke algebra of typeA. There seem to be no agreement in
the literature on which elements to call the Jucys-Murphy elements in other types. We
chose our convention because under it the definition of the Jucys-Murphy element is
uniform in all types, but elementsjX
k forX =B,D defined below arguably also deserve
the name.

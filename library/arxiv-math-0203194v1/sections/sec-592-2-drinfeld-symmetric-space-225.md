---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-592-2-drinfeld-symmetric-space-225
section_title: "DRINFELD SYMMETRIC SPACE. 225"
section_number: 2
pages: 229-233
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
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
4. EXAMPLES. 227
Algebraicity. In n = 1 case the rigid analytic curve XΓ is algebraizable
for any Γ ([ Mu72b]). In higher dimensions, we know the following suﬃcient
condition: Let Γ be a torsion-free uniform lattice in PGL(n + 1,K ), viz. a
discrete co-compact subgroup of ﬁnite co-volume without el ements of ﬁnite
order. Then, since it is ﬁnite co-volume, we have ∆ Γ = ∆. Hence in this
case, we are going to take a quotient of the Drinfeld symmetri c space Ω.
Theorem 3.2 (loc. cit.) . If Γ is a torsion-free uniform lattice, then the quo-
tient rigid analytic variety XΓ can be algebraizable to a non-singular pro-
jective variety having the ample canonical class.
In terms of formal scheme, this means that the relative canon ical sheaf
of ˆXΓ/SpfR is ample.
4. Examples.
Tate curve. LetT be the maxial torus consisting of all invertible diagonal
matrices. We take n elements qi∈ K× (1≤ i≤ n) with |qi| < 1 and set
q0 = 1. Deﬁne Γ ⊂T to be the set of all diagonal matrices with ( i,i )-entry
an integer power of qi for 0≤i≤n. Then Γ is a normal hyperbolic subgroup
of PGL(n + 1,K ) with ∆ Γ the apartment corresponding to T . If n = 1, the
curve Ω(∆ Γ )/Γ is known to be the so-called Tate curve; in this case Ω(∆ Γ )
is simply P1
K minus two points.
Mumford curve. Consider again the n = 1 case. The rigid analytic curve
XΓ with Γ generated by at least two elements is called a Mumford curve. A
Mumford curve is, in fact, algebraized to a non-singular pro jective curve of
genus greater than 1. Moreover, the formal model provided by the admissible
covering inhereted from Ω(∆ Γ ) gives a stable k-split multiplicative reduction
of that curve. The converse is also known:
Theorem 4.1 (Mumford [ Mu72b]). Let X be a smooth and proper rigid
analytic curve over K, and suppose X admits a formal model with k-split
multiplicative reduction. Then X is isomorphic to XΓ for a unique Γ.
Surface case. In higher dimension it becomes extremely diﬃcult to ﬁnd
normal hyperbolic groups; but there are several known examp les of torsion-
free uniform lattices. Let Γ is a torsion-free uniform latti ce, and N the
number of Γ-orbits in the vertex set ∆ 0. Mumford [ Mu79] calculated the
several numerical invariants of the quotient surface XΓ :
(i) χ(OXΓ ) = N (q− 1)2(q + 1)/3.
(ii) ( c1,XΓ )2 = 3c2,XΓ = 3N (q− 1)2(q + 1).
(iii) q(XΓ ) = 0,
where q denotes the irregularity. It is very interesting that the Mu mford-
Kurihara-Mustaﬁn uniformization in two dimension always p roduces the
surfaces which satisﬁes the equality in Miyaoka-Yau inequa lity. Mumford
[Mu79] constructed one example of Γ in q = 2 such that N = 1; the
resulting surface is one of the so-called “fake projective p lanes”. Recently,
228 B. OVER VIEW OF THEORY OF p-ADIC UNIFORMIZATION.
Cartwright, Mantero, Steger, and Zappa constructed severa l examples of
lattices in q = 2 and q = 3. Making use of this groups, in [ IK98], Ishida
and the author discussed other possible fake projective pla nes, and showed
that there are at least three fake projective planes (incl. M umford’s one)
which are not isomorphic to among others. We will see in more d etail the
construction of Mumford’s fake projective plane in the next section.
Shimura variety case. LetD be a quaternion algebra over a totally real
ﬁeld F . We assume that D ramiﬁes at every inﬁnite place except one ∞0.
Let Γ ∞ be a subgroup of D×/F× deﬁned by some congruence condition;
we shall assume that it is “suﬃciently small”. Then it is clas sically known
that Γ∞ acts discontinuously on the upper 1
2 plane H such that the quotient
H/Γ∞ is a projective curve (Shimura curve of PEL-type). The canonical
model Sh is deﬁned over some ray-class ﬁeld of F .
There must be a ﬁnite place ν at which B ramiﬁes. Let p be the residue
characteristic of ν. We assume that Γ ∞ is maximal at ν. Then the Shimura
curve Sh has a bad reduction at ν, and due to Cherednik [ ˇCer76] and
Drinfeld [ Dri76], the associated rigid analytic space over F ur
ν has a p-adic
uniformization, where F ur
ν is the maximal unramiﬁed extension of Fν. Let
D be the quaternion algebra which has local invariants obtain ed precisely
by switching those of D at ν and∞0 Then there exists a subgroup Γ ν in
D
×
/F× deﬁned basically by the same congruence relation as that of Γ ∞
such that Ω ⊗F ur/Γ ν is isomorphic to the assocaied analytic space of Sh at
ν. (This isomorphism actually decends to some ﬁnite unramiﬁe d extension
of Fν , depending on the data of connected components of Sh.)
This story has been generalized to higher dimension by Rapop ort-Zink
[RZ96] and Boutot-Zink [ BZ95]. The next section is devoted to explain
one special example of the p-adic uniformization of a Shimura surface.
5. Mumford’s fake projective plane.
Our example of p-adically uniformizable Shimura surface is constructed
by means of some division algebra D. Th following construction is inspired
by the Mumford’s oroginal paper [ Mu79].
Let ζ =ζ7 be a primitive 7th-root of unity, and set L : = Q(ζ); L is a
cyclic extension of Q of degree 6 having an intermediate quadratic extension
K : = Q(λ) (∼
= Q(√
−7)), where λ =ζ +ζ 2 +ζ 4. The Galois group of L/K
is generated by the Frobenius map σ : ζ↦→ζ 2, and that of K/Q is generated
by the complex conjugation z↦→z. Note that the prime 2 decomposes on
K, more explicitly, 2 = λλ gives the prime factorization, and the prime 7
ramiﬁes. We ﬁx an inﬁnite place ε :֒→C byλ↦→−1+√−7
2 .
We set µ : = λ/λ, and deﬁne the central division algebra D overK of
dimension 9 by
D : =
2⨁
i=0
LΠ i

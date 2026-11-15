---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-031-51-intersections-of-theta-divisors
section_title: "Intersections of theta divisors"
section_number: 5.1
pages: 103-110
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
95
THEOREM 5.2. If C is a general curve of genus g = 2n, then G(dn) is
either the alternating group AN or the full symmetric group SN.
The proof of this in section 5.8 again uses a degeneration, this time
from a general curve into a hyperelliptic one. We also remark that if the
Galois group G(dn) in the above theorem is the full symmetric group SN,
then also the monodromy group G in the previous theorem has to be the
full Weyl group W(E6) because it then contains a reﬂection. However, at
present we do not know how to decide whether this is indeed the case.
5.1. Intersections of theta divisors
Consider a complex ppav X of dimension g ≥2 with a symmetric theta
divisor Θ ⊂X as above. In this section we will always assume that Θ is
smooth or has at most isolated singularities, a situation in which we have
the following Bertini-type result.
LEMMA 5.3. If the theta divisor Θ is smooth or has at most isolated
singularities, then over some Zariski-open dense subset U ⊂X there exists
a smooth proper family
fU :
YU −→U
whose ﬁbre over any point x ∈U(C) is isomorphic to Yx = Θ∩Θx.
Proof. Recall the general fact [55, cor. III.10.7] that if f : V −→W is a
morphism of complex algebraic varieties and if V is smooth, then over some
Zariski-open dense U ⊆W the restriction fU = f|f −1(U) : f −1(U) −→U is
a smooth morphism. Since we can replace W by any Zariski-open dense
subset, this remains true if the smoothness assumption on V is replaced
by the weaker assumption that the singular locus Sing(V) is mapped via f
into a proper closed subset of W. In the case at hand, we apply this to the
composite morphism
f :
V = Θ×Θ  
/ X ×X
a
/ X = W
where a : X × X −→X denotes the group law. If the theta divisor has at
most isolated singularities, then Sing(V) = (Sing(Θ)×Θ)∪(Θ×Sing(Θ))
has dimension g−1 or is empty. In both cases the general fact from above
shows that over some Zariski-open dense subset U ⊂X the restriction fU
is smooth of relative dimension g −2. This being said, our claim follows
from the observation that the projection onto the ﬁrst factor Θ × Θ −→Θ
induces an isomorphism f −1(x) ∼= Θ∩Θx for x ∈X(C).
□
We want to study the ﬁbres Yx of the above family. In this context an
important role is played by the involution σx : X −→X,y 7→x −y. Notice
that the intersection Yx = Θ ∩Θx is mapped onto itself by this involution
96
Chapter 5 – A family of surfaces
because we assumed the theta divisor to be symmetric. The above Bertini
argument yields the following
COROLLARY 5.4. If the theta divisor is smooth or has only isolated
singularities, then there exists a Zariski-open dense subset U ⊂X such that
for all x ∈U(C) the quotient morphism
Yx −→Y +
x
= Yx/σx
is an ´etale double covering between smooth varieties of dimension g−2.
Proof. From lemma 5.3 we get a Zariski-open dense subset U ⊂X such
that Yx is smooth of dimension g−2 for all x ∈U(C). Shrinking this open
dense subset we can furthermore assume that it does not contain points of
the form x = 2y with y ∈Θ(C). Then the involution σx : Yx −→Yx is ´etale
for all points x ∈U(C), and our claim follows.
□
For the rest of this section we always ﬁx a point x with the properties in
the above corollary, and we put
Y = Yx,
Y + = Y +
x
and
σ = σx
for brevity. Like for any ´etale double cover of smooth complex varieties,
the rational cohomology of the quotient Y + coincides with the eigenspace
for the eigenvalue +1 in
H•(Y,Q) = H•(Y,Q)+ ⊕H•(Y,Q)−
where the upper index ± indicates that the involution σ acts by ±1 on the
respective two eigenspaces. Now recall the following version of the weak
Lefschetz theorem [71, rem. 3.1.29]: If W is a smooth complex projective
variety of dimension d, then for all ample effective divisors D1,...,Dr the
restriction map Hn(W,Z) −→Hn(D1 ∩··· ∩Dr,Z) is an isomorphism in
degrees n < d −r and a monomorphism in degree n = d −r. Note that
the intersecting divisors are not required to be smooth or transverse to each
other. In our case, since Y is the intersection of two ample divisors on X it
follows that the restriction morphism
Hn(X,Q) −→Hn(Y,Q)
is an isomorphism for n < g −2 and a monomorphism for n = g −2. So
the interesting part of the cohomology of Y sits in the middle cohomology
degree n = g−2 and can be deﬁned as the orthocomplement
V = Hg−2(X,Q)⊥⊆Hg−2(Y,Q)
with respect to the intersection form. The involution σ acts by ε = (−1)g
on Hg−2(X,Q), hence
Hg−2(X,Q) ⊆Hg−2(Y,Q)ε =
(
Hg−2(Y,Q)+
for g even,
Hg−2(Y,Q)−
for g odd.
5.1. Intersections of theta divisors
97
So the orthocomplement from above admits a decomposition V = V+ ⊕V−
into the eigenspaces
V−ε = Hg−2(Y,Q)−ε
and
Vε = Hg−2(X,Q)⊥⊆Hg−2(Y,Q)ε
where now ⊥denotes the orthocomplement inside the ε-eigenspace. Since
the restriction morphism in the weak Lefschetz theorem is a morphism of
Hodge structures, V−and V+ are Hodge substructures of Hg−2(Y,Q). To
compute their Hodge numbers one can use the Hirzebruch-Riemann-Roch
theorem together with the following result, where [Θ] ∈H2(X,Q) denotes
the fundamental class of the theta divisor.
LEMMA 5.5. In terms of the restriction θ = [Θ]|Y ∈H2(Y,Q), the Chern
classes of Y are given by
ci(Y) = (−1)i ·(i+1)·θ i ∈H2i(Y,Q).
In particular, the variety Y is of general type with canonical class KY = 2θ.
Proof. By deﬁnition we have Y = Θ∩Θx for some point x ∈X(C). The
embedding Y ,→Θ gives an adjunction sequence
0 −→TY −→TΘ|Y −→OX(Θx)|Y −→0
where TY and TΘ are the tangent bundles to Y resp. Θ (note that this makes
sense also if the theta divisor has isolated singularities, provided that x is
chosen in such a way that Y does not meet the singularities). By restriction
of the adjunction sequence for the embedding Θ ,→X we also get an exact
sequence
0 −→TΘ|Y −→TX|Y −→OX(Θ)|Y −→0.
Since the tangent bundle TX is trivial, it follows from these two adjunction
sequences that the Chern polynomial ct(Y) = 1+c1(Y)·t +c2(Y)·t2 +···
satisﬁes
1 = ct(Y)·(1+θt)2
since the Chern polynomial is multiplicative in short exact sequences. From
this identity our claim about the Chern classes follows by a comparison of
coefﬁcients. By deﬁnition the canonical sheaf ωY is the top exterior power
of the cotangent bundle T ∗
Y , so for the canonical class we get
KY = c1(ωY) = c1(Λg−2(T ∗
Y )) = c1(T ∗
Y ) = −c1(Y) = 2θ
where in the third equality we have used that by the splitting principle the
ﬁrst Chern class of a bundle coincides with the ﬁrst Chern class of any of
its exterior powers [40, rem. 3.2.3(c)]. In particular, the canonical class KY
is ample and therefore also big in the sense of [71, sect. 2.2], so the smooth
variety Y is of general type.
□
With notations as in the above lemma, to compute intersection numbers
between powers of Chern classes we only need to determine the image of
98
Chapter 5 – A family of surfaces
the top power θ g−2 under the degree map degY : Hg−2(Y,Q) −→Q. To
achieve this recall that Y is the intersection of two general translates of the
theta divisor. Since the intersection of cycles corresponds to the cup product
on cohomology, it follows that the fundamental class of Y is the cup product
square [Y] = [Θ]2 ∈H4(X,Q). Hence
degY(θ g−2) = degX([Θ]g−2 ·[Y]) = degX([Θ]g) = g!
where the last equality holds by the Poincar´e formula [13, sect. 11.2.1]. As
a direct application we have the following
COROLLARY 5.6. For g ≥2 the topological Euler characteristic of Y is
given by the formula
χ(Y) = (−1)g ·(g−1)·g!.
Proof. By the Gauss-Bonnet theorem [48, p. 416] the topological Euler
characteristic of any compact complex manifold is equal to the degree of its
top Chern class. Hence χ(Y) = degY(cg−2(Y)), and the claim follows from
lemma 5.5 and from the above formula for the degree degY(θ g−2).
□
To get a feeling for the geometry involved in the above constructions,
let us take a more explicit look at the situation for some small values of the
dimension g = dim(X) of the underlying ppav.
The case g = 2. Here Y consists of two points which are interchanged
by the involution σ so that we have the following picture.
s
s
p
q
A
AU
K
Θ
Θx
The fundamental classes p,q of the two interchanged points of Y form a
basis of H0(Y,Q), and the eigenspace
H0(Y,Q)+ = Q·(p+q) = H0(X,Q)
equals the image of the weak Lefschetz embedding. Thus V+ = 0, and the
Hodge structure V−= Q·(p−q) of weight zero has rank one.
The case g = 3. In this case the morphism Y −→Y + is an ´etale double
covering of smooth projective curves. To any such covering one can attach
its Prym variety [79] [13, ch. 12]. Before we come to the speciﬁc example
5.1. Intersections of theta divisors
99
at hand, let us brieﬂy recall the deﬁnition and some basic features of Prym
varieties in general, referring to loc. cit. for more details.
For any covering ˜C −→C of smooth projective curves we have a norm
homomorphism
N ˜C/C :
J ˜C −→JC
between the corresponding Jacobian varieties, induced by the pushforward
morphism on divisors. This norm homomorphism is always surjective. For
an ´etale double covering its kernel has precisely two connected components,
and one deﬁnes the Prym variety
P = Prym( ˜C/C) = (ker(N ˜C/C))0 ⊂J ˜C
to be the connected component which contains the origin. By construction
this is an abelian subvariety of J ˜C. The special thing about ´etale double
covers of curves is that this Prym variety also comes along with a principal
polarization, indeed by loc. cit. the principal polarization on J ˜C restricts
on the Prym variety P to twice a principal polarization. Prym varieties are
useful in the study of ppav’s since they are more general than Jacobian
varieties but nevertheless still accessible in terms of algebraic curves. Note
that if the curve C has genus g+1 (say), then ˜C has genus 2g+1 due to the
Riemann-Hurwitz formula [55, cor. IV.2.4], and then the Prym variety has
dimension
dim(P) = (2g+1)−(g+1) = g.
Hence if we denote by Mg+1 the coarse moduli space of smooth projective
curves of genus g + 1 and deﬁne Rg+1 to be the coarse moduli space of
´etale double covers of such curves, then we have a diagram
Rg+1
ϕ
{vvvvvvvvv
π
"D
D
D
D
D
D
D
D
Mg+1
Ag
where ϕ is the forgetful morphism and where π is the morphism that assigns
to a double covering its Prym variety. Here the morphism ϕ is generically
ﬁnite of degree 2g+1 −1 because the ´etale double covers of a given curve
correspond bijectively to the non-trivial two-torsion points on its Jacobian
variety. The Prym morphism π plays an important role for the moduli of
abelian varieties and has been studied a lot in the literature; as the most
important results, we only mention that for g ≥6 it is generically ﬁnite of
degree one [39] but never injective [34]. In dimensions g < 6 the Prym
morphism π is no longer generically ﬁnite but its ﬁbres have a surprisingly
rich geometric structure which is discussed in loc. cit.
100
Chapter 5 – A family of surfaces
This brings us back to the ´etale double covering Y −→Y + deﬁned by
the intersection of two general translates of the theta divisor on a complex
ppav X of dimension g = 3. Here the curve Y has genus 7 by corollary 5.6,
hence the Prym variety P = Prym(Y/Y +) is a complex ppav of dimension 3
as well. The following result has been obtained in [84] and [66].
THEOREM 5.7. For a general complex ppav X of dimension g = 3 the
following properties are satisﬁed.
(a) For general x ∈X(C) the Prym variety P of the cover Yx −→Y +
x
is isomorphic to the ppav X.
(b) Every ´etale double covering of smooth curves with Prym variety
isomorphic to X arises as above for some point x ∈X(C), and the
coverings for two points x1,x2 are isomorphic iff x1 = ±x2.
In other words, the above construction identiﬁes the ﬁbre of the Prym
morphism π : R4 −→A3 over a general ppav X ∈A4(C) with an open
dense subset of the Kummer variety
KX = X/⟨±idX⟩.
Fixing a general point x ∈X(C), we now again use the notation Y = Yx
etc. The deﬁnition of the Prym variety P as a component of the kernel of
the norm epimorphism N : JY ↠JY + shows that the Jacobian variety JY is
isogenous to P × JY +, which together with the identiﬁcation in part (a) of
the above theorem implies
H1(Y,Q) = H1(X,Q)⊕H1(Y +,Q).
Hence in this case we have V−= 0, and V+ = H1(Y +,Q) is a pure Hodge
structure of weight one and rank eight.
The case g = 4. Here Y −→Y + is an ´etale double covering of smooth
projective surfaces that will occupy us for the rest of this chapter. We claim
that V−has Hodge numbers h2,0 = h0,2 = 11 and h1,1 = 30 whereas V+ is
of pure Hodge type (1,1) and rank six. Indeed, bearing in mind the natural
identiﬁcations
H2(Y +,Q) = H2(Y,Q)+ = H2(X,Q)⊕V+
this is a direct consequence of the numerical data in the following table.
LEMMA 5.8. For a complex ppav X of dimension g = 4 we have the
following Hodge numbers.
h2,0 = h0,2
h1,1
h1,0 = h0,1
Y
17
52
4
Y +
6
22
0
X
6
16
4
5.1. Intersections of theta divisors
101
Proof. The last row follows from the Hodge decomposition for a ppav
of dimension g = 4 and has only been included for reference. Similarly,
the last column is clear because H1(Y,Q) = H1(Y,Q)−= H1(X,Q) by the
weak Lefschetz theorem. It remains to compute the Hodge numbers of the
smooth surfaces Y and Y + in cohomology degree two. Corollary 5.6 gives
the topological Euler characteristic χ(Y) = 72, which implies h2(Y) = 86
because h0(Y) = h4(Y) = 1 and h1(Y) = h3(Y) = 8. In the same way, via
lemma 5.5 the Hirzebruch-Riemann-Roch theorem gives the holomorphic
Euler characteristic
χ(OY) = degY(c2
1(Y)+c2(Y))/12 = degY((−2θ)2 +3θ 2)/12 = 14.
Plugging in the values h0,0(Y) = 1 and h0,1(Y) = 4 we get h0,2(Y) = 17, and
then h1,1(Y) = 52 because the Hodge numbers in degree two must sum up
to the second Betti number h2(Y) = 86.
To obtain from these numbers also the Hodge numbers of the quotient
surface Y + =Y/σ we use that the quotient morphism q :Y →Y + is an ´etale
double covering. In particular we have a commutative diagram
H2(Y +,Q)×H2(Y +,Q)
∪
/
q∗

H4(Y +,Q)
degY+
/
q∗

Q
2·

H2(Y,Q)×H2(Y,Q)
∪
/ H4(Y,Q)
degY
/ Q
where the vertical arrow on the right hand side is multiplication with the
degree deg(q) = 2, and the Chern classes satisfy ci(Y) = q∗(ci(Y +)) for
all i. This being said, the Gauss-Bonnet and Hirzebruch-Riemann-Roch
theorem show
χ(Y +) = χ(Y)/2 = 36
and
χ(OY +) = χ(OY)/2 = 7.
Hence it follows that h2(Y +) = 36 −1 −1 = 34 and h0,2(Y +) = 7 −1 = 6
by similar computations as above, and we are done.
□
As an immediate corollary we obtain that the intersection form has the
following signatures on the various occuring subspaces of H2(Y,Q), where
we denote by s+ and s−the dimension of maximal subspaces on which the
form is positive resp. negative deﬁnite.
COROLLARY 5.9. For g = 4 the intersection form has the following
signatures on the various subspaces of H2(Y,Q).
H2(Y,Q)
H2(Y +,Q)
H2(X,Q)
V−
V+
s+
35
13
13
22
0
s−
51
21
15
30
6
102
Chapter 5 – A family of surfaces
Proof. The Hodge index theorem [103, th. 6.33] says that for a smooth
compact K¨ahler surface S with K¨ahler class ω ∈H1,1(X) ∩H2(X,R) the
intersection form is
• positive deﬁnite on the subspace (H2,0(S) ⊕H0,2(S)) ∩H2(S,R)
and also on the line R·ω,
• negative deﬁnite on the orthocomplement of the K¨ahler class ω
inside H1,1(S)∩H2(S,R).
In our case, taking S = Y and using the Hodge numbers in lemma 5.8 one
sees that on H2(Y,Q) = H2(Y,Q)+ ⊕V−and H2(Y,Q)+ = H2(X,Q)⊕V+
the intersection form has the given signatures.
□
In particular, it follows that on the subspace V+ the intersection form is
negative deﬁnite. In sections 5.3 and 5.4, working on the level of integral
cohomology we will determine the structure of the lattices whose signatures
have been listed above. But let us ﬁrst say a few words about the variations
of Hodge structures deﬁned by the above subspaces.

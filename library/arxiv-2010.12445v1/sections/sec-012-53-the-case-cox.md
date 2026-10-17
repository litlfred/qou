---
doc_id: arxiv-2010.12445v1
doc_title: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION"
section_id: sec-012-53-the-case-cox
section_title: "The case C={OX}"
section_number: 5.3
pages: 25-27
source_pdf: 2010.12445v1.pdf
source_sha256: 16e9ca22ecc1f296
toc_source: outline
doc_brief: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION — Given a quasi-compact category ﬁbered in groupoids X and a monoidal subcat- egory C of its category of locally free sheaves Vect(X), we are"
---
Symn OX ≃OX so the hypothesis of 5.1 are satisﬁed.
Proposition 5.20. Let X be a quasi-compact ﬁbered category over R. Then FibX ,{OX} is the
intersection of all quasi-compact open subsets of Spec H0(OX ) containing the image of X →
Spec H0(OX ).
If X is quasi-compact and quasi-separated then Vect(FibX ,{OX }) →Vect(X) is fully faithful,
or, equivalently, OFibX,{OX } →P{OX }∗OX is an isomorphism.
Moreover X →FibX ,{OX } is
universal among maps from X to pseudo-aﬃne sheaves.
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
26
Proof. We can assume R = H0(OX ). Set C = {OX }. If A is an R-algebra, there is a unique
R-linear and strong monoidal functor ΓA : C →Vect(A), namely ΓA = H0(−) ⊗R A. This means
that FibX ,C is a subfunctor of Spec R. We have that ΓA ∈FibX ,C(A) if and only if, given a test
sequence T∗for C, ΓA is exact on it. As
ΓA(T∗) = H0(T∗) ⊗R A
we can conclude that FibX ,C is the locus where all complex of free R-modules H0(T∗) are exact.
By 4.1, this is an intersection of quasi-compact open subsets of Spec R containing the image
of X →Spec R. Conversely if X →U ⊆Spec R and U is a quasi-compact open subset, say
U = Spec R −V (a1, . . . , an), then U is the locus where (a1, . . . , an): Rn →R is surjective and,
in particular,
On
X
(a1,...,an)
−−−−−−→OX →0
is a test sequence. Therefore FibX ,C ⊆U as required.
Now assume that X (and therefore PC : X →FibX ,C) is quasi-compact and quasi-separated.
Set π: X →Spec R. By construction π∗OX = OSpec R. From the Cartesian diagram
X
X
FibX ,C
Spec R
id
PC
π
u
the ﬂatness of u and [Ton20, Prop 1.15] we can conclude that
OFibX,C ≃u∗OSpec R ≃u∗(π∗OX ) ≃PC∗OX
By 5.14 this is equivalent to the fully faithfulness of Vect(FibX ,C) →Vect(X).
For the last claim, if X →U is a map to a quasi-aﬃne scheme consider the diagram
X
FibX ,C
V
Spec R
U
Spec H0(OU)
where the square one is Cartesian. The dashed arrow exists thanks to the description of FibX ,C
as intersection. From the same diagram we can see that FibX ,C →U is uniquely determined.
The general case of a pseudo-aﬃne sheaf follows easily from 4.2.
□
Proposition 5.21. Let X be a quasi-compact ﬁbered category. If X →Spec H0(OX ) has open
image then FibX ,{OX} coincides with this image. Conversely if FibX ,{OX} is an algebraic stack,
X →Spec R is a ﬁnitely presented algebraic stack and H0(OX ) is a Noetherian Jacobson ring
then X →Spec H0(OX ) has open image.
Proof. Set C = {OX }. The ﬁrst claim follows from 5.20, so let us focus on the converse.
We can assume R = H0(OX ). By 2.8 and 5.20, the fact that FibX ,C is algebraic means that
it is quasi-aﬃne. Moreover, since H0(OFibX,C) = R, it follows that V = FibX ,C is open inside
Spec R. By Chevalley’s theorem [Aut19, Tag 054K] the image U of X →Spec R is constructible.
In conclusion, from 5.20, we can conclude that V is the smallest open of Spec R containing U.
Assume by contradiction U̸ = V . As V −U is constructible, we need to show that a constructible
subset Q of Spec R contains a closed subset. We can easily reduce to the case that Q is open.
As R is a Jacobson ring, Q contains a closed point of Spec R as required.
□
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
27
Example 5.22. We show an example of an integral scheme X of ﬁnite type over a ﬁeld k such
that
• the stack FibX,{OX} is not algebraic.
• the map X →FibX,{OX} is not surjective, which shows that not all ﬁber functors (locally)
comes from a section of X.
By 5.21, the idea is to look for an X such that the image of X →Spec H0(OX ) is not open. Let
A = k[x, y, z] and B = k[x/y, y, z/y] and notice that
A ⊆B ⊆Ay ⊆Axy = Bx
We deﬁne X as the scheme obtained by gluing Spec Ax and Spec B along Spec Axy. By con-
struction there are maps
Spec A −V (x, y) = Spec Ax ∪Spec Ay →X
f−→Spec A
As the ﬁrst map is dominant because Spec Ax ⊆X is open, we obtain that H0(OX ) = A.
Moreover
f −1(V (x, y)) = Spec(B/(x, y)) = Spec(k[x/y, z/y]) →Spec A
is given by A →k[x/y, z/y], x, y, z →0. It follows that the image of X →Spec A is Im =
Spec A −V (x, y) ⊔{(x, y, z)}.
By 5.21 the stack FibX,{OX} cannot be algebraic because Im is not open. Moreover we claim
that P = (x, y) ∈FibX,{OX} −Im. By 5.20 we have to show that if Im ⊆U ⊆Spec A is open
then P ∈U. This is true because otherwise we would have the contradiction
P ∈(Spec A −U) ⊆Spec A −Im = V (P) −{(x, y, z)} ⊆V (P) = {P}

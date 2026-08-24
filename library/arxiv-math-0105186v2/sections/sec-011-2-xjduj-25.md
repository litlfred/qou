---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-011-2-xjduj-25
section_title: "(∇XJ)◦Du◦j, (2.5)"
section_number: 2
pages: 24-28
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
in which ¯∂J,u∗∇ = (u∗∇)0,1 is the ¯∂-operator associated to the pullback con-
nection u∗∇ on u∗(TEv,J|TEv). The derivative of ¯∂univ, Duniv
u,J : T Bu×
T J(E,π,j )J−→ Eu,J , is obviously
Duniv
u,J (X,Y ) = Du,J (X) + 1
2Y◦Du◦j. (2.6)
From this point onwards, we pass to a more realistic situatio n, and assume
that S is compact with ∂S ⁄= ∅. Our ﬁrst observation is a consequence of
(iv). Informally speaking, it says that for the purposes of p seudo-holomorphic
sections, the boundary ∂hE of the ﬁbres can be ignored.
Lemma 2.2. For every J∈ J(E,π,j ) there is a compact subset K⊂E\∂hE
such that all u∈ MJ satisfy u(S)⊂K.
Proof. Let W⊂ E be a closed neighbourhood of ∂hE which, under the collar
embedding provided by the Liouville vector ﬁelds on the ﬁbre s, corresponds to
[−ǫ; 0]×∂hE for some ǫ > 0. By deﬁnition σ(W ) = [ −ǫ; 0]. After possibly
makingW andǫ smaller, we may assume that W∩Q =∅, that Ω |TEh vanishes
24
on W , and that (iv) holds there. From Ω |TEh
x = 0 and J(TEh
x ) = TEh
x it
follows that Ω( X,JX )≥ 0 for all X∈TEx,x∈W . Take u∈ MJ and consider
the function h = eσ◦u on U = u−1(W ). This satisﬁes h|∂U ≡ e−ǫ and is
subharmonic, because d(dh◦j) = d(Θ ◦J◦Du◦j) = −u∗Ω ≤ 0. It follows
that h≤ e−ǫ everywhere, which shows that K = E\int(W ) has the required
property.
The action of u∈ B is deﬁned to be A(u) =
∫
Su∗Ω. This is actually the
same for all u, since
∫
S
u∗Ω =
∫
∂S
u∗Θ =
∫
∂S
κQ. (2.7)
Therefore, if one equips E with a symplectic form Ω + π∗β taming J, all the
u∈ MJ become pseudo-holomorphic curves with the same energy 1
2
∫
S||Du||2 =
A(u) +
∫
Sβ.
Lemma 2.3. MJ is compact in any Cr-topology.
Proof. We apply the Gromov compactness theorem for ( j,J )-holomorphic maps
S→E with boundary inQ. The bubble components in the Gromov limit appear
through a reparametrization which “magniﬁes” successivel y smaller parts of the
domain. Since in our case all maps are sections, the bubbles a re either noncon-
stant J-holomorphic spheres in some ﬁbre Ez, or nonconstant J-holomorphic
discs in Ez, z∈ ∂S , with boundary on Qz. But both are excluded by our as-
sumptions, since Ω is exact and Qz⊂Ez an exact Lagrangian submanifold.
A less formal version of the inﬁnite-dimensional framework introduced above
involves spaces of W 1,p-sections, p > 2. We omit the construction itself, and
only mention its main consequence. For ( u,J )∈ Muniv, the diﬀerential operator
Du,J extends to a Fredholm operator W1
u→ W0
u,J from the W 1,p-completion
W1
u ofT Bu to theLp-completion W0
u,J of Eu,J . We denote this extension equally
byDu,J . If it is onto (in which case one says that u is regular), MJ is a smooth
ﬁnite-dimensional manifold near u. If that holds for all u∈ MJ ,J itself is called
regular, and the space of such J is denoted by Jreg (E,π,Q,j )⊂ J(E,π,j ).
Lemma 2.4. Jreg (E,π,Q,j ) is C∞-dense in J(E,π,j ). In fact the following
stronger statement holds: take some nonempty open subset U⊂ S and a J∈
J(E,π,j ). Then there are J ′∈ Jreg (E,π,Q,j ) arbitrarily close to J, such that
J =J ′ outside π−1(U ).
Proof. Even though this is a well-known argument, we recall part of i t as a
preparation for subsequent more reﬁned versions. Fix U andJ. By Lemmas 2.2
and 2.3 there is an open subset V ⊂ E with V∩ (∂hE∪Ecrit) =∅, such that
im(u)⊂V for each u∈ MJ . A modiﬁed version of the compactness argument
shows that this property, with the same V , remains true for all almost complex
structures in J(E,π,j ) which are suﬃciently close to J. We want to make J
25
regular by perturbing it on V∩π−1(U ). Take T⊂T J(E,π,j )J to be the subset
of those Y which vanish outside V∩π−1(U ), and consider the operator
Duniv
u,J : W1
u× T−→ W0
u,J (2.8)
given by the same formula as in (2.6). By a standard arguments surjectivity
of this operator implies the desired result (strictly speak ing, what comes up in
this argument is a dense subspace of those Y which have “ﬁnite C∞
ǫ -norm”, but
since the ﬁrst component Du,J is Fredholm, this makes no diﬀerence as far as
surjectivity is concerned). Let F → S be the bundle dual to Λ 0,1(u∗TEv), so
that ( W0
u,J )∗∼= Lq(F ), p−1 +q−1 = 1. Suppose that η∈ Lq(F ) is orthogonal
to the image of (2.8). It then satisﬁes
D∗
u,Jη = 0 on S\∂S , and
∫
S
⟨η,Y ◦Du◦j⟩= 0 for Y ∈ T. (2.9)
The ﬁrst equation implies that η is smooth away from the boundary. Suppose
that z∈U\∂S is a point where ηz⁄= 0, and set x =u(z)∈V∩π−1(U ). Take
a (j,J )-antilinear map Z :TSz→TEv
x such that⟨ηz,Z◦j⟩⁄= 0. One can see
from (2.4) that there is a Y ∈ T J(E,π,j )J with Yvh
x = Z, Yvv
x = 0, and this
will satisfy ⟨ηz, (Y ◦Du◦j)z⟩⁄= 0. By multiplying Y with a bump function
supported near x, one can achieve that it lies in T and that
∫
S⟨η,Y ◦Du◦j⟩⁄= 0,
a contradiction. This means that η| (U\∂S ) = 0. By unique continuation
η| (S\∂S ) = 0, which proves that η = 0.
Take some ζ∈∂S and consider the map evζ : B→Qζ, evζ(u) = u(ζ). The
next result belongs to a type called “transversality of eval uation”.
Lemma 2.5. Let g be a smooth map from some arbitrary manifold G to Qζ.
Then, for any J andU as in the previous lemma, there are J ′∈ Jreg (E,π,Q,j )
arbitrarily close to J, with J ′ =J outside π−1(U ), such that evζ|MJ ′ is trans-
verse to g.
Proof. In the same setup as before, one now has to prove that for u∈ MJ and
x =u(ζ)∈Qζ, the operator
W1
u× T−→ W0
u,J×T (Qζ)x, (X,Y )↦−→(Duniv
u,J (X,Y ),Xζ)
is onto. Take ( η,ξ ) orthogonal to the image, with ξ∈ T (Qζ)∨
x . One still has
(2.9) and as before it follows that η = 0. Then ⟨ξ,Xζ⟩= 0 for all X∈ W1
u, so
that ξ = 0 as well.
For a given ( E,π,Q ) and ζ, one now proceeds as follows. After choosing
some j and a J∈ Jreg (E,π,Q,j ), one obtains a smooth compact moduli space
MJ ; and then one sets
Φ 1(E,π,Q ) = (evζ )∗[MJ ]∈H∗(Qζ; Z/2).
This is independent of the choice of j,J by a standard argument using parame-
trized moduli spaces. The same reasoning shows that it remai ns invariant under
26
any “smooth deformation” of the geometric objects involved , that is to say of
Q, Ω , Θ or of the ﬁbration π : E → S itself, as long as one remains within
the class of exact Lefschetz ﬁbrations with Lagrangian boun dary conditions. It
seems pointless to formalize this notion of deformation, be cause the necessary
conditions will be quite obviously satisﬁed in all our appli cations.
Remark 2.6. Since the regular spaces MJ are actual manifolds, one can re-
ﬁne Φ 1(E,π,Q ) by regarding it as an element of the unoriented bordism group
MO ∗(Qζ). But even with this reﬁnement, it is far from capturing all th e infor-
mation contained in MJ . To get more sophisticated invariants one can use eval-
uation at several points, allowing those to move; we will now explain the simplest
version of this. Given ζ∈∂S , choose a positively oriented path c : [0; 1]→∂S ,
c(0) = c(1) = ζ, parametrizing the boundary component on which ζ lies. Let
φt :Qc(t)→Qζ be the diﬀeomorphisms obtained from symplectic parallel tr ans-
port along c|[t; 1]. Denote by ∆ , Γ ⊂ Q2
ζ the diagonal and the graph of φ0,
respectively. For regular J, the parametrized evaluation map
~evζ : [0; 1]× MJ→ [0; 1]×Q2
ζ, ~evζ(t,u ) = (t,u (ζ),φt(u(c(t))))
represents a class ˜Φ 2(E,π,Q )∈ H∗([0; 1]×Q2
ζ,{0}× Γ ∪{ 1}× ∆; Z/2), and
this (as well as its cobordism version) is an invariant of (E,π,Q ). An example
of this invariant will be computed in Remark 2.17(iii).
LetS1,S 2 be two compact surfaces with marked points ζk∈∂Sk, and denote
by S = S1#ζ1∼ζ2S2 their boundary connected sum (Figure 2). To be precise,
one should choose oriented embeddings ψk : ¯D+(1)→ Sk of the closed half-
disc ¯D+(1) = {z ∈ C : |z| ≤1, imz ≥ 0} into Sk, such that ψk(0) =
ζk and (ψk)−1(∂Sk) = [ −1; 1]. Then, writing D+(ρ) for the open half-disc
of some radius 0 < ρ < 1, one forms S by taking the two Sk\ψk(D+(ρ))
and identifying ψ1(z) with ψ2(−ρ−1z). Suppose that we have exact Lefschetz
ﬁbrations (Ek,πk) overSk, such that their symplectic connections are trivial on
im(ψk); together with Lagrangian boundary conditions Qk⊂Ek, such that the
one-formsκQk vanish on ψk([−1; 1]); and ﬁnally, an exact syplectic manifold M
with an exact Lagrangian submanifold L, and isomorphisms φk :M→ (Ek)ζk
satisfying φk(L) = ( Qk)ζk . One can then glue the ( Ek,πk) and Qk to an
exact Lefschetz ﬁbration over S. To do that, one ﬁrst uses symplectic parallel
transport to construct embeddings
¯D+(1)×M
Ψ k
/d47/d47
/d15/d15
Ek
πk
/d15/d15¯D+(1)
ψk
/d47/d47Sk
such that Ψ k|{0}× M =φk. These will satisfy
(Ψ k)∗Ω k =ω, (Ψ k)∗Θ k =θ +dRk, (Ψ k)−1(Qk) = [−1; 1]×L
27
for some functions Rk. As in the pasting construction described in Section
1.1, one needs to introduce modiﬁed forms ˜Θ k such that (Ψ k)∗ ˜Θ k = θ near
{0}× M . The functions KQk need to be modiﬁed accordingly, but that is
rather straightforward, so we will not write it down explici tly. Now take the Ek\
Ψ k(D+(ρ)×M ) and identify Ψ 1(z,x ) with Ψ 2(−ρz−1,x ). This yields a manifold
E with a map π : E→ S, and the remaining data matches up, producing the
structure of an exact Lefschetz ﬁbration together with a Lag rangian boundary
condition Q.
1ζ
S
S
S 2 1ζ2
Figure 2:
Assume that one has chosen complex structures jk on Sk such that the ψk
are holomorphic; these determine a complex structure j on S. Take Jk ∈
J(Ek,πk,jk) such that (Ψ k)∗(Jk) is the product of the standard complex struc-
ture on ¯D+(1) and of some ﬁxed ω-compatible almost complex structure on M
(the same for both k). Then there is a canonical induced J∈ J(E,π,j ). Note
that even though we have restricted the behaviour of Jk over im(Ψ k), it is still
possible to choose them regular, by using the more precise st atement in Lemma

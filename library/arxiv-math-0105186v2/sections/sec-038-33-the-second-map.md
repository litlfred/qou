---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-038-33-the-second-map
section_title: "The second map"
section_number: 3.3
pages: 60-63
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
From this point onwards, we add one more assumption to those i n Section 3.1:
(VI) R is the function Rr which appears in the construction of exact Lefschetz
ﬁbrations in Lemma 1.10, with the given λ and some 0 < r <1/2 which
we are free to choose; see more speciﬁcally (1.19) for this fu nction.
Since that severely restricts the choice of R, one needs to worry about possible
conﬂicts with the other conditions, or that it might restric t the ultimate scope
60
of the exact sequence. An inspection of Remark 3.1 shows that the only issue
is whether, using R = Rr, one can satisfy (V) with arbitrarily small δ and ǫ.
That is taken care of by Lemma 1.12(iv), which shows that it su ﬃces to choose
r small.
τL /0/0/0
/0/0/0
/0/0/0
/0/0/0
/0/0/0
/0/0/0
/1/1/1
/1/1/1
/1/1/1
/1/1/1
/1/1/1
/1/1/1
Figure 6:
The obvious reason for introducing (VI) is that there is a sta ndard ﬁbration
(EL,πL) over a disc ¯D(r), with r small, whose monodromy around ∂ ¯D(r) is τL.
Following Remark 1.4, we want to modify this by a pullback. Ta keSp = ¯D(1/2)
and a map p :Sp→ ¯D(r) of the form p(z) = g(|z|)(z/|z|), where g is a function
with g(t) = t for small t,g(t) = r for t≥r, and g′(t)≥ 0 everywhere. Then
(Ep,πp) = p∗(EL,πL)
is again an exact Lefschetz ﬁbration. It has nonnegative cur vature; this follows
from Lemma 1.12(iii) and the fact that det(Dp)≥ 0. Moreover, it is ﬂat on
the annulus Sp\D(r); and using the isomorphism φp : (Ep)1/2→M inherited
from φL : (EL)r→ M , one can identify its monodromy around ∂Sp with τL.
To represent this property, we draw ( Ep,πp) as in Figure 6.
τL
Figure 7:
Now take the surface Sf = ( R× [−1; 1])\D(1/2)⊂ R2, with coordinates
(s,t ), and divide it into two parts Sf,± =Sf∩{t∈ R±}, so that Sf,+∩Sf,− =
((−∞;−1/2]∪ [1/2;∞))×{ 0}. Consider trivial ﬁbrations πf,± :Ef,± =Sf,±×
M → Sf,± over the two parts, and equip them with diﬀerential forms Ω f,±,
Θ f,± as follows. Ω f,± is the pullback of ω ∈ Ω 2(M ), and similarly Θ f,+ is
the pullback of θ; ﬁnally Θ f,− = θ−d(β(s)KτL ), where β is a function with
61
β(s) = 0 for s≥ 1/4, β(s) = 1 for s≤− 1/4. Deﬁne a ﬁbration ( Ef,πf ) over
Sf by identifying the ﬁbres
Ef,+
(s,0)−→Ef,−
(s,0)
via idM for s≥ 1/2, respectively via τL for s≤− 1/2. Ω f,± and Θ f,± match
up to forms Ω f , Θ f ; the ﬁrst because τL is symplectic, and the second as a
consequence of our choice of Θ f,−. This makes ( Ef,πf ) into a (ﬂat) exact
symplectic ﬁbration; it is represented in Figure 7.
τL
/0/0/0/0
/0/0/0/0
/0/0/0/0
/0/0/0/0
/0/0/0/0
/0/0/0/0
/1/1/1/1
/1/1/1/1
/1/1/1/1
/1/1/1/1
/1/1/1/1
/1/1/1/1
Figure 8:
We now carry out a pasting construction of the kind discussed in Section 1.1.
If one identiﬁes the ﬁbres of Ep andEf at the point 1/2 by using φp : (Ep)1/2→
M = (Ef )1/2, then the monodromies around the circle |z| = 1/2 coincide, being
both equal to τL. Since the two ﬁbrations are ﬂat close to this circle, one can
paste them together to an exact Lefschetz ﬁbration, denoted by (E,π ), over
S = Sp∪Sf = R× [−1; 1]; this is drawn in Figure 8. Equip ( E,π ) with the
Lagrangian boundary condition Q which is the union of R×{ 1}× L1⊂ Ef,+
and R×{− 1}× τL(L0)⊂Ef,−, with κQ = 0, and with a function KQ which is
KL1 on R×{ 1}×L1 andKτL(L0)−β(s)KτL|τL(L0) on R×{− 1}×τL(L0). This
is clearly modelled on ( τL(L0),L 1) over the positive end of S; over the negative
end it is modelled on ( L0,L 1), as one sees using the trivialization
(−∞;−1]× [−1; 1]×M Γ /d47/d47
/d15/d15
E
π
/d15/d15
(−∞;−1]× [−1; 1]
γ /d47/d47S
γ = inclusion, Γ(s,t,x ) =
{
(s,t,x )∈Ef,+ t≥ 0,
(s,t,τ L(x))∈Ef,− t≤ 0.
We now get a relative invariant Φ rel
0 (E,π,Q ) : HF (τL(L0),L 1)→HF (L0,L 1).
Following the same pattern as in the previous section (but wi th considerably
less technical diﬃculties), we need to determine partially the underlying cochain
map.
62
Lemma 3.8. (E,π,Q ) together with U = (−1; 1)× [−1; 1]⊂ S satisﬁes the
conditions of Proposition 2.28(i). Moreover, given w∈ τL(L0)∩L1 and x∈
L0∩L1, the space Mh(x,w ) contains precisely one horizontal section if w =q(x),
and is empty otherwise.
Proof. Because the two parts from which it is assembled have nonnega tive cur-
vature, so does ( E,π ). To any point x∈L0∩L1 one can associate a horizontal
section uf :Sf→Ef satisfying uf (∂S )⊂Q, which is deﬁned by
uf (s,t ) =
{
(s,t,x )∈Ef,+ t≥ 0,
(s,t,τ L(x))∈Ef,− t≤ 0.
Condition (I) and (IV) imply that x /∈ im(ι). By construction EL contains a
trivial part ¯D(r)× (M\ im(ι)), see Proposition 1.11. The pullback Ep has a
corresponding property, which means that there is a horizon tal sectionup ofEp,
matching up with uf to form a u∈ Mh(x,x )⊂ Mh.
∫
Sf (uf )∗Ω f = 0 by deﬁnition of Ω f , and similarly
∫
Sp(up)∗Ω p = 0 because
the image of up lies in the trivial part of Ep. It follows that the section we
have constructed satisﬁes A(u) = 0. The connection ∇u on u∗TEv is trivial;
in fact, by inspecting the details of the construction, one c an see that ( E,π ) is
symplectically trivial in a neighbourhood of im( u). By linearization of basic fact
that symplectic parallel transport preserves any Lagrangi an boundary condition,
one ﬁnds that the subbundle u∗(TQ∩TEv)⊂ u∗TEv|∂S is preserved under
∇u; hence it is trivial. To summarize, we have found that one can identify
u∗(TEv)∼=S× Cn symplectically, in such a way that ∇u becomes trivial, and
thatu∗(TQ∩TEv) is mapped to the subbundle ( R×{−1}× Λ −1)∪(R×{1}× Λ 1)
for some Lagrangian subspaces Λ ±1⊂ Cn; by looking at the positive end, one
sees that Λ −1 and Λ 1 are transverse. Then the index formula in terms of the
Maslov index for paths [20] shows that ind Du,J = 0.
Next, suppose that u ∈ Mh is an arbitrary horizontal section satisfying
u(∂S )⊂ Q. When restricted to Sf,±, this is of the form uf,±(z) = ( z,x ±)
for points x+∈ L1, x−∈ τL(L0). The condition for the two parts to match
along Sf,+∩Sf,− is that x− = x+ = τL(x+). In particular x± ∈ L0∩L1.
Because of the strong unique continuation property of horiz ontal sections, it
follows that the construction above yields all of Mh. By the same argument,
any partial horizontal section U→ E|U with boundary in Q can be extended
to some element of Mh.
Letj be some complex structure on S, standard over the ends. Take the same
J (3)∈ Jreg(M,τL(L0),L 1) as in the previous section, and choose an additional
J (5)∈ Jreg (L0,L 1). By Lemma 3.8 and Proposition 2.28, one can ﬁnd a J (6)∈
J(E,π,Q,j,J (3),J (5)) which is both horizontal and regular. Write
c =CΦ rel

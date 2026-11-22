---
doc_id: arxiv-math-0105186v2
doc_title: "A long exact sequence for symplectic Floer cohomology"
section_id: sec-008-23-a-vanishing-theorem
section_title: "A vanishing theorem"
section_number: 2.3
pages: 32-38
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
toc_source: inferred
doc_brief: "A long exact sequence for symplectic Floer cohomology — 17 sections: Front matter; Introduction; Dehn twists, and all that"
---
A vanishing theorem
Let L be a framed exact Lagrangian sphere in an exact symplectic manifold
M. According to Proposition 1.11 one can associate to it a standard ﬁbration
(EL, πL) over ¯D(r) for some r > 0.
Each ﬁbre EL
z , z̸ = 0, contains a dis-
tinguished Lagrangian sphere ΣL
z , described by Lemma 1.12(i); for z = r, the
isomorphism φL : EL
r →M takes ΣL
r to L. Deﬁne the standard Lagrangian
boundary condition for (EL, πL) to be
QL = S
z∈∂¯
D(r) ΣL
z ,
κQL = dc(−1
4|z|) | ∂¯D(r),
KQL = 0.
(2.16)
This is indeed a Lagrangian boundary condition, as one can see from (1.20). Our
aim here is to prove the following result about the invariant Φ1(EL, πL, QL) ∈
H∗(ΣL
r ; Z/2) ∼= H∗(L; Z/2):
Proposition 2.13. Φ1(EL, πL, QL) = 0 for all M and L.
The ﬁrst part of the proof is a degeneration argument, in which one restricts
the base to successively smaller discs. For 0 < s ≤r set QL,s = S
z∈∂¯
D(s) ΣL
z ; to-
gether with κQL,s and KQL,s as before, it is a Lagrangian boundary condition for
(EL,s, πL,s) = (EL, πL) | ¯D(s). This constitutes a deformation of (EL, πL, QL)
in a suitable sense; which means that if one identiﬁes ΣL
r with ΣL
s using parallel
transport along [s; r], then
Φ1(EL, πL, QL) = Φ1(EL,s, πL,s, QL,s)
(2.17)
for all s. Now ﬁx some J ∈Jh(EL, πL, j), where j is the standard complex
structure on ¯D(r). Let ML,s be the space of sections ¯D(s) →EL,s which are
32
holomorphic with respect to j| ¯D(s) and J|EL,s, and have boundary in QL,s. As
s →0, QL,s shrinks to the single critical point ΣL
0 = {x0} of πL, and we would
like to apply a compactness argument to elements of ML,s in the limit. This
looks a bit unpleasant as it stands, but one can modify the situation to make the
degeneration of the QL,s less singular, and then standard Gromov compactness
is suﬃcient.
Lemma 2.14. For some 0 < r′ ≤r, there is a compact almost complex mani-
fold with corners ( bEL, bJ), together with pseudo-holomorphic maps
bEL
ηL
/
ˆπL

EL
πL

¯D(r′) × ¯D(1)
m
/ ¯D(r)
where m(w, z) = wz is multiplication, such that the following properties are
satisﬁed.
(i) Away from ZL = (ηL)−1(x0)∩(ˆπL)−1(0, 0), the map ηL identiﬁes ( bEL, ˆπL)
with the pullback of (EL, πL) by m. In particular, restricting to any w =
s > 0 gives a pseudo-holomorphic diﬀeomorphism
bEL,s = (ˆπL)−1({s} × ¯D(1)) −→EL,s.
(ii) bEL carries a symplectic form bΩL which tames its almost complex structure,
and which is of the form
bΩL = (ηL)∗ΩL + (ˆπL)∗( i
2dw ∧d ¯w + i
2dz ∧d¯z + dγ) + δ,
with γ = 1
4im((r′ −w)¯zdz), and where δ is supported in a small neigh-
bourhood of ZL.
(iii) ( bEL, bΩL) contains a Lagrangian submanifold with boundary bQL which
projects to [0; r′] × S1 ⊂¯D(r′) × ¯D(1) and satisﬁes
ηL( bQL ∩(ˆπL)−1({s} × S1)) =
(
QL,s
s > 0,
{x0}
s = 0.
It is convenient to begin with the local model for the construction. Choose
some r′ > 0 and set
E = {x ∈Cn+1 : ||x|| ≤2
√
r′, |q(x)| ≤r′},
Ω= ωCn+1|E,
π = q : E −→¯D(r′),
Q = S
z∈∂¯
D(r′) Σz
(2.18)
where q is our standard quadratic function, and Σz is as in (1.11). In parallel
with the reasoning above, one can also introduce (Es, πs) = (E, π)| ¯D(s) and
33
Qs = S
z∈∂¯
D(s) Σz for s ∈(0; r′]. Take the pullback of (E, π) by the multiplica-
tion map, m∗E = {(w, z, x) ∈¯D(r′) × ¯D(1) × E : q(x) = wz} ⊂Cn+3. This
has one singular point (0, 0, 0), which can be resolved by blowing it up inside
Cn+3 and taking the proper transform of m∗E. The outcome, which we denote
by bE, comes with maps
bE
η
/
ˆπ

E
π

¯D(r′) × ¯D(1)
m
/ ¯D(r′).
(i’) η is a pullback map away from Z = η−1(0) ∩ˆπ−1(0, 0).
That is obvious from the deﬁnition. Consider the two-form
Ω+ i
2dw ∧d ¯w + i
2dz ∧d¯z + dγ = ωCn+3 + dγ
(2.19)
on ¯D(r′) × ¯D(1) × E, where γ is as in Lemma 2.14(ii). We claim that this is
symplectic and tames the obvious complex structure. All one needs to verify is
that (dγ)(·, i·) is nonnegative, which one can do by decomposing dγ = (dγ)1,1 +
(dγ)0,2 + (dγ)2,0; then (dγ)1,1 = re(r′ −w) i
4dz ∧d¯z is nonnegative since re(r′ −
w) ≥0, while (dγ)0,2(·, i·) vanishes because it is a two-form of type (0, 2), and
similarly for (dγ)2,0. Now pull back (2.19) to the blowup, make it symplectic by
adding a two-form δ supported near the exceptional divisor, and restrict that
to bE. The outcome is:
(ii’) There is a symplectic form bΩon bE which tames the complex structure,
and which is of the form η∗Ω+ (ˆπ)∗( i
2dw ∧d ¯w + i
2dz ∧d¯z + dγ) + δ, with
δ supported in a small neighbourhood of Z.
The subset
{(w, z, x) : w ∈[0; r′], |z| = 1, x ∈Σwz} ⊂m∗E
(2.20)
is a submanifold, since it is the image of the embedding S1 ×Z/2 ¯Bn+1(1) →
Cn+3, (z, y) 7→(|y|2, z2, zy). It is also Lagrangian with respect to (2.19); which is
in fact the reason for our choice of symplectic form. Deﬁne bQ to be the preimage
of (2.20) in bE; provided that the support of δ has been chosen suﬃciently small,
this is again a Lagrangian submanifold. By construction one has
(iii’) ˆπ( bQ) = [0; r] × S1, and
η( bQ ∩ˆπ−1({s} × S1)) =
(
Qs
s > 0,
{0}
s = 0.
34
Proof of Lemma 2.14. Take a holomorphic Morse chart (ξ, Ξ) around x0 ∈EL
0
as provided by Lemma 1.12(ii). After restricting the domains, we may assume
that ξ is the inclusion ¯D(r′)֒ →¯D(r) for some 0 < r′ ≤r, that Ξ is deﬁned
on the set E ⊂Cn+1 from (2.18), and that QL,s = Ξ(Qs) for all 0 < s ≤r′.
Construct a diagram
bE

/
ηL
*
m∗E
m∗Ξ

/ E
Ξ

bEL
ˆπL
%K
K
K
K
K
K
K
K
K
K
/ m∗EL
/

EL,r′
πL,r′

¯D(r′) × ¯D(1)
m
/ ¯D(r′)
as follows: pull back EL by multiplication m; the map m∗Ξ induced by Ξ
identiﬁes neighbourhoods of the singular points (0, 0, 0) ∈m∗E and (0, 0, x0) ∈
m∗EL; which means that there is a resolution
bEL −→m∗EL
modelled locally on bE →m∗E. The given almost complex structure J induces
one on m∗E, for which m∗Ξ is holomorphic; this and the complex structure on
bE deﬁne the almost complex structure bJ. Part (i) of the lemma now follows
from the corresponding statement (i’) in the local model. Next, take the two-
form ΩL+ i
2dw∧d ¯w+ i
2dz∧d¯z+dγ on m∗EL; due to the nonnegative curvature
of standard ﬁbrations, see Lemma 1.12(iii), and to the fact that J is horizontal,
this will tame the almost complex structure away from the singular point. One
gets bΩL by gluing this together with the symplectic form bΩfrom the local model,
and that proves (ii). Similarly, the deﬁnition of bQL follows that of bQ, and (iii’)
implies (iii).
Returning to the moduli spaces ML,s of pseudo-holomorphic sections, we can
now carry out the compactness argument mentioned above:
Lemma 2.15. Choose some neighbourhood of the critical point x0 ∈EL. For
suﬃciently small s, the image of all u ∈ML,s will lie in that neighbourhood.
Proof. Let (sk) be a sequence in (0; r′] converging to zero, and uk ∈ML,sk a
corresponding sequence of sections. By Lemma 2.14(i), there is for each k a
unique pseudo-holomorphic map
ˆuk : ¯D(1) −→bEL
with ηL(ˆuk(z)) = uk(skz) and ˆπL(ˆuk(z)) = (sk, z). By part (iii) of the same
35
lemma, this maps S1 to bQL. Moreover, its energy is independent of k, since
Z
¯
D(1)
ˆu∗
kbΩL =
Z
¯
D(sk)
u∗
kΩL +
Z
¯
D(1)
i
2dz ∧d¯z +
Z
¯
D(1)
i
4(r′ −sk)im(d¯z ∧dz) +
+
Z
¯
D(1)
ˆu∗
kδ = π
2 sk + π + π
2 (r′ −sk) + 0 = π(1 + r′
2 ).
Here we have used (1.20) for the ﬁrst term; and the last term is zero because,
without changing its cohomology class, one can modify δ to make its support ar-
bitrarily close to Z, in which case, since uk avoids the critical point x0, ˆuk would
not meet the support of δ. One can apply Gromov compactness to the sequence
ˆuk : ( ¯D(1), S1) →( bEL, bQL); the limit of some subsequence will be a pseudo-
holomorphic “cusp disc” or “stable disc” ˆu∞. Since im(ˆuk) ⊂(ˆπL)−1({sk} ×
¯D(1)), we have im(ˆu∞) ⊂(ˆπL)−1({0} × ¯D(1)). Composing with ηL yields a
“cusp disc” u∞in E whose boundary lies in ηL( bQL ∩(ˆπL)−1({0}×S1)) = {x0}.
Because ΩL is exact, u∞is necessarily constant equal to x0. On the other hand,
the image of uk, for k large and in our subsequence, lies in an arbitrarily small
neighbourhood of the image of u∞. The rest is straightforward.
The second part of the proof of Proposition 2.13 is an explicit computation in
the local model (E, π) from (2.18). Note that while this is not an exact Lefschetz
ﬁbration, it still makes sense to consider the spaces Ms of holomorphic sections
w : ¯D(s) →Es with boundary in Qs. In fact Qs is a Lagrangian submanifold
of Cn+1, as one can see from (1.12), and the maximum principle ensures that
any holomorphic disc in Cn+1 with boundary in Qs is actually contained in Es.
Lemma 2.16. Ms consists of maps w(z) = s−1/2az + s1/2¯a, where a ∈Cn+1
satisﬁes q(a) = 0 and ||a||2 = 1/2. All these maps are regular, in the sense that
the associated Fredholm operators are surjective.
Proof. The holomorphic functions v : ¯D(s) →C which satisfy v(z) ∈z1/2R
for all z ∈∂¯D(s) are v(z) = s−1/2cz + s1/2¯c, for c ∈C. All components of
w ∈Ms must be of this form, and the conditions on a come from q(w(z)) = z.
As for regularity, since we are dealing with the standard complex structure
J0 on Cn+1, Dw,J0 is an actual ¯∂-operator, see (2.5).
Its kernel consists of
holomorphic maps X : ¯D(s) →Cn+1 such that X(z) ∈√zRn for z ∈∂¯D(s), and
Dq(w(z))X(z) = 2 P
k wk(z)Xk(z) = 0 for all z. The same argument as before
determines all such X explicitly, the outcome being that ker Dw,J0 ∼= R2n−1.
Using the Riemann-Roch formula for surfaces with boundary one computes
that ind Dw,J0 = 2n −1, which shows that the cokernel is zero.
The condition on a can be written as
||re a||2 = ||im a||2 = 1/4,
⟨re a, im a⟩= 0
so that Ms can be identiﬁed with the sphere bundle S(T ∗Sn) by mapping a to
(u, v) = (−2 im a, 2 rea). With this and the diﬀeomorphism Sn →Σs, x 7→√sx,
36
one can identify the evaluation evs : Ms →Σs with the projection to the base
S(T ∗Sn) →Sn. This clearly represents the zero cycle in H∗(Sn; Z/2). Hence,
if one deﬁned an invariant Φ1(Es, πs, Qs) in this local model, it would vanish.
Proof of Proposition 2.13. As in the proof of Lemma 2.15, we consider a holo-
morphic Morse chart (ξ, Ξ) with Ξ deﬁned on E ⊂Cn+1 for some r′ > 0. We
know that for some suﬃciently small s > 0, all u ∈ML,s lie in im(Ξ). Recall
that Ξ is holomorphic with respect to the standard complex structure J0 on E
and to J on EL; and that it takes Qs to QL,s. This implies that composition
with Ξ yields a diﬀeomorphism
Ms
∼
= /
evs

ML,s
evs

Σs
Ξ
/ ΣL
s .
It is easy to see that, for w ∈Ms and u = Ξ ◦w ∈ML,s, the kernels and
cokernels of the associated operators Dw,J0, Du,J coincide. This shows that
J|EL,s is regular, and that the evaluation cycle ML,s →ΣL
s can be identiﬁed
with projection S(T ∗Sn) →Sn, which as observed before is zero in homology;
together with (2.17) this completes the argument.
Remarks 2.17. (i) As pointed out in Remark 2.6, Φ1 can be reﬁned to an
invariant taking values in unoriented bordism. Proposition 2.13 also applies to
this reﬁnement, since (2.17) comes from a cobordism of moduli spaces and the
projection S(T ∗Sn) →Sn is obviously cobordant to zero.
(ii) Suppose that (E1, π1, Q1) is a standard ﬁbration with its standard bound-
ary condition, and that we have another exact Lefschetz ﬁbration (E2, π2, Q2),
such that the two can be glued together to (E, π, Q) as in Section 2.1. Proposi-
tion 2.13 together with Proposition 2.7 implies that Φ1(E, π, Q) will then be zero.
By pushing this reasoning a little further, one arrives at the following result: let
(E, π) be an arbitrary exact Lefschetz ﬁbration over a compact base S, with La-
grangian boundary condition Q. Assume that there is a path c : [a; b] →S with
c(a) ∈∂S, c−1(Scrit) = {b}, and c′(b)̸ = 0, whose vanishing cycle Vc(a) is isotopic
to Qc(a) as an exact Lagrangian submanifold in Ec(a); then Φ1(E, π, Q) = 0.
(iii) Despite the vanishing of their Φ1-invariant, the moduli spaces of pseudo-
holomorphic sections of a standard ﬁbration are never empty. To see this, one
has to use the invariant ˜Φ2 mentioned in Remark 2.6. The computation of this
can be reduced to the local model in the same way as before, using Lemma 2.15.
The relevant parametrized evaluation map then becomes
[0; 1] × Ms −→[0; 1] × Σs × Σs,
(t, w) 7−→(t, w(s), eπi(1−t)w(se2πit)).
(2.21)
37
Here Σse2πit →Σs, x 7→eπi(1−t)x arises as parallel transport along ∂¯D(s) in
positive direction. Using Lemma 2.16 one can make (2.21) even more concrete,
identifying it with
[0; 1] × S(T ∗Sn) −→[0; 1] × Sn × Sn,
(t, u, v) 7−→(t, v, −cos(πt)v −sin(πt)u).
It is now easy to see that ˜Φ2(EL, πL, QL) is nonzero: it is the image of the
fundamental class [Sn × Sn] under the map
H∗(Sn × Sn; Z/2) →H∗(Sn × Sn, ∆∪∆; Z/2) ∼=
∼= H∗([0; 1] × Sn × Sn, {0} × ∆∪{1} × ∆; Z/2)
where ∆, ∆are the diagonal and antidiagonal, respectively.

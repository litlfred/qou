---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-014-46-summarising
section_title: "Summarising"
section_number: 4.6
pages: 27-30
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
doc_brief: "European Journal of Mathematics (2024) 10:3 RESEARCH ARTICLE — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
following diagram. Solid arrows represent a covering map coming from a quotient, whereas
‘squiggly’ arrows indicate isomorphisms that are unexplained by group theory alone.
B
E5τ0 C2 C1
E15τ0 P1 P1 Eτ0 Eτ0 E5τ0
P1 P1 E3τ0
P1
Figure 3. Quotient structure of Bring’s curve.
This corresponds to the quotients by the following groups, where an arrow now indicates
that a source group is normal in the target, whereas a dashed line just indicates that a
group is a subgroup. The label used corresponds to the list in §4.2, except where that label
is ambiguous and the exact group must be speciﬁed.
28 H. W. BRADEN AND LINDEN DISNEY-HOGG
{e}
⟨(12)⟩ C3 ⟨(12)(34)⟩
C6 S3 ⟨(12), (34)⟩ S′
3 ⟨(12)(34), (13)(24)⟩ C4
D12 D8 A4
S4
Figure 4. Subgroup structre of S5 corresponding to the quotients of
Bring’s curve.
Finally, we recall from a Riemann-Hurwitz argument that each elliptic curves that comes
a quotient from a genus-2 curve withV4 symmetry has 2 marked points which are the branch
points of the covering map, equivalently the images of the ﬁxed points of the involution being
quotiented by. We have shown that the preimages of these on Bring’s curve are geometric
points. In Figure 5 we illustrate the quotient structure highlighting these points. (We do
not decorate the curveB/A4∼=E3τ0, but include it so as to show every quotient with genus
greater than 0.) Note the nodes of this diagram do not correspond directly to the placements
of those above.
6×, 4⊗, 2#, 4□
6×
 2×, 2#
 2#, 2□
2×
 2#
 2□
 2#
Figure 5. Quotient structure including marked points. The points ×
correspond to the Weierstrass points [1 : 1 : α : β : γ] (and permuta-
tions of α,β,γ ), the points ⊗ to the vertices [1 : −1 : 0 : ±i :∓i] and
[1 : −1 : ±i : 0 : ∓i], the points # to the vertices [1 : −1 : ±i :∓i : 0],
and the points □ correspond to the vertices [1 : ±i :∓i :−1 : 0] and
[1 :±i :−1 :∓ : 0].
BRING’S CUR VE: OLD AND NEW 29
With the information of the quotients, we can now discuss the isogeny class and isomor-
phism class of the Jacobian of Bring’s curve with the following results.
Proposition 4.4 ([RR92], §4, [Web05], Corollary 5.5). The C-isogeny class of the Jacobian
of Bring’s curve is E 4
3 .
Proof. As we will later want to strengthen this result, we will use methods which relate
subvarieties of the Jacobian to idempotents, and thus to subgroups of the automorphism
group. Namely we will use [LR04, §4.2], which gives the isogeny decomposition in terms of
Prym varieties of the Jacobian of a curve with A5 action. Note, because of comments made
before, Bring’s curve is the unique genus-4 curve for which we could apply this argument.
The result follows as, using the notation of Lange, XA4 =E3, XD5 =XZ5 =Y = P1.
This proof also follows from [LR04, Proposition 5.1], which uses only the action of S4
on the curve. Moreover, one could use [KR89, Theorem C] taking the subgroups to be
⟨(12)⟩,⟨(34)⟩,C4 andA4. Alternatively, using the isomorphismA5∼=PSL 2(F5) and [KR89,
Example 2] on can ﬁnd JacB∼ JacC1×JacC2 and proceed from there. These proof strategies
all follow the same approach of looking for idempotents.
One may also obtain the result following the same method as R&R. We use that fact that
isogenies act on the period matrix by right multiplication by matrices R∈ M4(Z), and so
we have the required isogeny by taking λ = 1 in the identity
(λ−1 Id)( 1 τM)(λ Id 0
0 M′
)
=
(
Id 5
λτ Id
)
,
where
M′ := 5M−1 =


2 −1 1 −1
−1 2 −1 1
1 −1 2 −1
−1 1 −1 2

.
□
Note that we are able to construct the quotient B/A4 directly from the P4-model using
transformations with coeﬃcients in Q, and the resulting curve is deﬁned overQ, so by [KR89,
Remark 6] the above proposition can be strengthened to a statement about the Q-isogeny
class of the Jacobian of Bring’s curve. Calculating using Sage we ﬁnd that the Q-isogeny
class ofB/A4 is 50a using the Cremona labels for elliptic curve Q-isogeny classes. Hence the
following result holds.
Proposition 4.5 ([Ser08], Exercise 8.3.2(b)) . The Q-isogeny class of the Jacobian of the
P4-model of Bring’s curve is (50a)4.
Note in the above proposition we had to be careful to specify the Jacobian of theP4-model
of Bring’s curve, as we have seen that HC-model is not birationally equivalent over a ﬁeld
that doesn’t contain Q[ζ]. The Q-isogeny class of the elliptic curve B/⟨(12)(34), (13)(24)⟩
calculated via the HC-model is 50b. Similarly, the Q-isogeny class of the two elliptic curves
covered byC2 is 450b, and the computation of the quotient required the coeﬃcient ﬁeld to
be Q[ρ]. In order to not have a contradiction with Proposition 4.5, we must have that the
Q-isogeny classes 50b and 50a merge over Q[
√
5], and that the isogeny classes 450b and 50a
merge over Q[ρ], which is indeed the case. 24
24The isogeny classes 450b and 50b merge over Q[√−15].
30 H. W. BRADEN AND LINDEN DISNEY-HOGG
One could use computational tools such as those in [BSS +16, Lom19] 25 to numerically
ﬁnd the Q-isogeny class of the Jacobian of the HC-model of Bring’s curve, as we did in the
notebooks. Such computational results using idempotents can be helpful for developing our
understanding, for example one can use computer algebra to search for relations between
the characters IndS5
H (1H), that is the characters ofS5 induced from the trivial representation
of H≤ S5. Doing so gives relations between subvarieties of the Jacobian of Bring’s curve
following [KR89, Theorem 3], for example
(18)
J⟨(12)⟩×J⟨(12)(34),(13)(24)⟩∼J⟨(12)(34)⟩×J⟨(12),(34)⟩,
J⟨(12)(34),(13)(24)⟩×JS3∼J⟨(12),(34)⟩×JS′
3.
Using Riemann-Hurwitz arguments these would let us say that B/⟨(12)⟩ ∼ B/C4 and
B/⟨(12)(34), (13)(24)⟩∼B /S′
3 without having to do any calculation, entirely from group
theory. The reason why these isogenies are actually isomorphisms is not clear.
Proposition 4.4 can also be strengthened in a diﬀerent direction.
Proposition 4.6 ([GAR00]). The Jacobian of Bring’s curve is isomorphic as a complex
torus toE 3
2×E 1.
Proof. The proof in [GAR00] is very general, considering Jacobians whose period matrix is
invariant underSn for any n. The isomorphism from the period matrix given in [RR92] is
C
(1 τM)(D 0
0 E
)
=
(1,τ diag(5, 5, 5, 1))
where
C =


−1 1 −1 2
1 0 0 1
0 −1 0 1
0 0 0 1

,D =


0 1 0 −1
0 0 −1 1
−1 −1 −1 4
0 0 0 1

,E =


−1 1 0 0
1 0 −1 0
−2 −1 −1 1
1 0 0 0

.
□
Note it would not be possible that the Jacobian is isomorphic to the product of the elliptic
curves as a principally polarised abelian variety, as it is well know that the Jacobian of any
smooth compact Riemann surface with canonical principal polarisation is irreducible. In
particular this means the matrix
(
D 0
0 E
)
of the proposition is not symplectic.

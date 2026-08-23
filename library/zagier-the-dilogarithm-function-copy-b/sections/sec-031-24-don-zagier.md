---
doc_id: zagier-the-dilogarithm-function-copy-b
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-031-24-don-zagier
section_title: "Don Zagier"
section_number: 24
pages: 22-24
source_pdf: zagier-the-dilogarithm-function-copy-b.pdf
source_sha256: c584944a501ef0c5
doc_brief: "The dilogarithm function — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
duplicate_of: "zagier-the-dilogarithm-function"
---
has simply L(1/2) = π2/12, L((3 −
√
5)/2) = π2/15 instead of the previous
expressions involving log 2(2) and log 2((1 +
√
5)/2)) and the same holds also
for more complicated identities involving several values of the dilogar ithm
at algebraic arguments. Such identities, of which several will be dis cussed
in §2, reﬂect the fact that the corresponding linear combination of arguments
represents a torsion element in the Bloch group of Q. They play a role in
quantum ﬁeld theory, where the constants appearing on the right-hand s ides
of the identities, renormalized by dividing by L(1), occur as central charges
of certain rational conformal ﬁeld theories.
B. The enhanced dilogarithm. The Bloch-Wigner dilogarithm is the imag-
inary part of Li 2(z) (corrected by a multiple of log |z| Li1(z) to make its ana-
lytic properties better) and hence vanishes on P1(R), while the Rogers dilog-
arithm is the restriction of Li 2(z) (corrected by a multiple of log |z| Li1(z)t o
make its analytic properties better) to P1(R) and takes its values most nat-
urally in the circle group R/(π2/2)Z. It is reasonable to ask whether there
is then a function ˆD(z) with values in C/(π2/2)Z or at least C/π2Q whose
imaginary part is D(z) and whose restriction to P1(R)i s L(z). In fact such a
function does not exist if we demand that the argument belongs to P1(C), but
it does exist if we either pass to a suitable inﬁnite covering of P1(C)/integerdivide{0, 1, ∞}
or else consider only combinations ∑ njˆD(zj) where∑ nj[zj] belongs to the
Bloch group BC deﬁned in §4 of Chapter I. This extended function, which
following [47] we call the “enhanced dilogarithm,” plays an important role in
W. Nahm’s article in this volume and is discussed in some detail there , so we
will be relatively brief here.
We begin with the extension of Li 2 and D to covers of punctured projective
space. Let X = P1(C) /integerdivide{0, 1, ∞}. Its fundamental group is the free group
on two generators and its universal cover ~X is isomorphic to the complex
upper half-plane H (with covering map given by the classical Legendre mod-
ular function λ : H/Γ (2) → X), and naturally Li 2 becomes a single-valued
holomorphic function on this universal cover, but we do not have to go t his
far if we only want the values of Li 2(z) modulo π2Q. Instead, it suﬃces to
take the universal abelian cover ˆX : the abelianization of π1(X)i s Z ⊕ Z, with
generators corresponding to the monodromy around 0 and 1 and hence to the
multi-valuedness of log( z) and log(1 − z), so ˆX is given by choosing branches
of these two logarithms, i.e.,
ˆX =
{
(u, v) ∈ C2 | eu + ev =1
}
,
with covering map π : ˆX → X given by ( u, v) ↦→z = eu =1 − ev.I ti so n
this space that we will deﬁne ˆD.
Actually, to get a C/4π2Z-valued version of Li 2, we do not even need to
pass to ˆX, but only to the smaller abelian cover corresponding to choosing a
branch of log(1 − z) only, i.e., the cover X ′ = C − 2πiZ, with covering map
The Dilogarithm Function 25
X ′ → X given by v ↦→1 − ev. Indeed, from the formula Li ′
2(z)= 1
z log 1
1−z we
see that the function
F (v)=L i 2(1 − ev)( v ∈ X ′)
has derivative given by F ′(v)= −v
1 − e−v , which is a one-valued meromorphic
function on C with simple poles at v ∈ 2πiZ whose residues all belong to
2πiZ. It follows that F itself is a single-valued function on X ′ with values in
C/(2πi)2Z. This function satisﬁes F (v +2 πis)= F (v) − 2πis log(1 − ev). We
now deﬁne ˆD on ˆX by
ˆD(ˆz)= F (v)+ uv
2 for ˆz =( u, v) ∈ ˆX .
This is a holomorphic function from ˆX to C/(2πi)2Z whose behavior under
the covering transformations of ˆX → X is given by
ˆD((u +2 πir, v +2 πis)) = ˆD((u, v)) + πi(rv − su)+2 π2rs (r, s ∈ Z)
and whose relation to the Bloch-Wigner function D(z) is given by
ℑ(ˆD(ˆz)) = D(z)+ 1
2 ℑ(¯uv)( ˆ z =( u, v),π (ˆz)= z). (1)
(For more details, see [47], pp. 578–579, where the deﬁnition of ˆD is given
somewhat diﬀerently.)
Now let ξ =∑ nj[zj] be an element of the Bloch group BC. This means,
ﬁrst of all, that the numbers zj ∈ X and nj ∈ Z satisfy∑ nj(zj) ∧ (1 − zj)=0
in Λ2(C∗) and, secondly, that ξ is considered only up to the addition of ﬁve-
term relations [ x]+[ y]+
[ 1−x
1−xy
]
+[1 −xy]+
[ 1−y
1−xy
]
with x, y ∈ X, xy ⁄=1 .I fw e
lift each zj to some ˆzj =( uj,v j)i n ˆX, then the relation∑ nj(zj)∧(1−zj)=0
in Λ2(C∗) says that the sum ∑ nj (uj) ∧ (vj) ∈ Λ2(C) has the form 2 πi ∧ A
for some A ∈ C depending on the liftings ˆzj =( uj,v j). If we change these lifts
to ˆz′
j =( u′
j,v ′
j) with u′
j = uj +2 πirj, v′
j = vj +2 πisj with rj and sj in Z,
then A changes to A′ = A +∑ nj(rjvj − sjuj +2 πirjsj), so the formula given
above for the behavior of ˆD under covering transformations of ˆX implies that
the expression (“enhanced dilogarithm”)
Denh(ξ)=
∑
j
njˆD(ˆzj) − πiA ∈ C/π2Q
is independent of the choice of lifts ˆzj. (This independence is true only modulo
π2Q, and not in general modulo 2 π2Z, as asserted in [47], because the group
generated by the zj and 1 − zj may contain torsion of arbitrary order.) Any 5-
term relation is in the kernel of Denh,s o Denh does indeed give a well-deﬁned
map from the Bloch group BC to C/π2Q. (The treatment in [30] is more

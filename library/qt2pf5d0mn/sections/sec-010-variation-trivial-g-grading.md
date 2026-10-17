---
doc_id: qt2pf5d0mn
doc_title: "UC Santa Barbara"
section_id: sec-010-variation-trivial-g-grading
section_title: "Variation: Trivial G-grading"
section_number: null
pages: 59-62
source_pdf: qt2pf5d0mn.pdf
source_sha256: 4c8581c3b46398e3
toc_source: outline
doc_brief: "UC Santa Barbara — 19 sections: Front matter; Abstract; Introduction"
---
Proof:
By Equation 3.3 and the argument above,
ZD(M; T ) =
X
ˆF=(g,f,t)
(D2/|G|)|T 0|( Q
α∈T 2 df(α))( Q
σ∈T 4
ˆZϵ(σ)
ˆF
(σ))
(D2)|T 1|( Q
τ∈T 3 dt(τ))
=
X
g
1
|G||T 0|
X
f,t
(D2)|T 0|( Q
α∈T 2 df(α))( Q
σ∈T 4
ˆZϵ(σ)(σ))
(D2)|T 1|( Q
τ∈T 3 dt(τ))
=
X
g
1
|G||T 0|CYC(M)
= DWG(M)CYC(M),
where ˆZϵ(σ)(σ) is the partition function of σ for which we have hidden the dependence
on the coloring.
In Section 3.4, we will give some variations of the construction of the the partition
function, in which the twisted Dijkgraaf-Witten invariant will appear as a special case.
3.4
Variation: Trivial G-grading
In this section, we study a variation of the partition function.
Let C be a ribbon fusion category, and let D = L
g∈G
Cg be a G-BSFC with a trivial
G-grading, namely, Ce = C, and Cg = 0 for g̸ = e. Thus D is a ribbon fusion category with
a G-action. In this case, we show that we can introduce a 4-cocycle ω ∈H4(G, U(1)) in
the construction of the partition function, and this results in a new invariant.
Since the G-grading is trivial, the colors g on 1-simplices must satisfy the condition
¯g02g01g12 = e for each 2-simplex (012). The colors on 2- and 3-simplices run through
a complete set of representatives in C. For each ﬁxed coloring, we will introduce an ω
50
Section 3.4
Variation: Trivial G-grading
factor to the partition function. Explicitly, using the notations in 3.1, the new invariant
can be deﬁned as follows:
Deﬁnition 3.4.1 Given a G-BSFC D with a trivial G-grading, a 4-cocycle ω ∈H4(G, U(1)),
and an ordered triangulation T of a closed oriented 4-manifold M, the partition function
ZD,ω(M; T ) of the pair (M, T ) is deﬁned by:
ZD,ω(M; T ) =
X
F=(g,f)
(D2/|G|)|T 0|( Q
β∈T 2 df(β)) Tr( N
σ∈T 4 Zϵ(σ)
F
(σ))
(D2)|T 1|
ω(g01, g12, g23, g34), (3.9)
or written in state sum model by:
ZD,ω(M; T ) =
X
ˆF=(g,f,t)
(D2/|G|)|T 0|( Q
α∈T 2 df(α))( Q
σ∈T 4
ˆZϵ(σ)
ˆF
(σ))
(D2)|T 1|( Q
τ∈T 3 dt(τ))
ω(g01, g12, g23, g34). (3.10)
The invariance proof of ZD,ω(M; T ) can be processed in a similar way as that of
ZD(M; T ) with slight modiﬁcations, so we will omit the details. For instance, to show it
is invariant under the 3-3 pachner move, Equation 4.26 is replaced by Equation 3.11:
X
I2,
I3
{
d024
d0124d0234d0245
ˆZ+(01234) ˆZ+(01245) ˆZ+(02345)
· ω(01, 12, 23, 34)ω(01, 12, 24, 45)ω(02, 23, 34, 45)}
=
X
I′
2,
I′
3
{
d135
d0135d1235d1345
ˆZ+(01235) ˆZ+(01345) ˆZ+(12345)
· ω(01, 12, 23, 35)ω(01, 13, 34, 45)ω(12, 23, 34, 45)}
(3.11)
51
Section 3.4
Variation: Trivial G-grading
In Equation 3.11, the product of the three ω factors on the left hand side is equal
to the product of the three factors on the right hand side, and this is precisely because
ω is a 4-cocycle and the colors on 1-simplices satisfy ¯g02g01g12 for each 2-simplex (012).
Cancelling the ω factors on both sides, we get back to Equation 4.26.
Proposition 3.4.2 If D is a G-BSFC with a trivial G-grading and a trivial G-action,
and ω ∈H4(G, U(1)), then
ZD,ω(M; T ) = DW ω
G(M)CYC(M),
(3.12)
where DW ω
G(M) is the twisted Dijkgraaf-Witten invariant [20]. In particular, If D =
Vect, then ZD,ω = DW ω
G(M).
Proof:
A similar argument as that in Section 3.3.3 shows that ZD,ω can be written
as follows:
ZD,ω(M; T ) =
X
ˆF=(g,f,t)
(D2/|G|)|T 0|( Q
α∈T 2 df(α))( Q
σ∈T 4
ˆZϵ(σ)
ˆF
(σ))
(D2)|T 1|( Q
τ∈T 3 dt(τ))
ω(g01, g12, g23, g34)
=
X
g
1
|G||T 0|ω(g01, g12, g23, g34)
X
f,t
(D2)|T 0|( Q
α∈T 2 df(α))( Q
σ∈T 4
ˆZϵ(σ)(σ))
(D2)|T 1|( Q
τ∈T 3 dt(τ))
=
X
g
1
|G||T 0|ω(g01, g12, g23, g34)CYC(M)
= DW ω
G(M)CYC(M).
52
Chapter 4

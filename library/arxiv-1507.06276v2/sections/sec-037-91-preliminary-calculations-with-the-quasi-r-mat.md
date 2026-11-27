---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-037-91-preliminary-calculations-with-the-quasi-r-mat
section_title: "Preliminary calculations with the quasi R-matrix"
section_number: 9.1
pages: 46-47
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
quasi-R-matrix corresponding to the semisimple Lie subalgebra gX of g. Recall
that w0 and wX denote the longest elements of W and WX , respectively. Choose
a reduced expression w0 =si1...s it such that wX =si1...s is for some s <t. As
in Remark 3.6 the quasi-R-matrices R and RX can then be written as
R =R[t] ·R[t−1] · · ·R[1], R X =R[s] ·R[s−1] · · ·R[1].
In view of relation (3.6) one obtains that
RRX =RR−1
X =R[t] ·R[t−1] · · ·R[s+1].(9.1)
Deﬁne
R(τ,X ) = (Ad(ξ)T −1
w0T −1
wXττ 0 ⊗ 1)(RRX ) ∈ U (2)
0 .(9.2)
We will see in Theorem 9.4 that the element R(τ,X ) is a major building block of
the coproduct ∆(X).
Lemma 9.1. The following relation holds
R(τ,X ) ∈
∏
µ∈wXQ+∩Q+
U +
−Θ( µ)Kµ ⊗U +
µ.
Proof. For any j = 1,...,t let γj denote the corresponding root as in Remark 3.6.
If s + 1 ≤j ≤t then the factor R[j] deﬁned by (3.8) satisﬁes
R[j] ∈
∏
n≥0
(TwX (U −) ∩U −
−nγj ) ⊗U +
nγj.
Using (9.1) we get that
RRX ∈
∏
µ∈wXQ+∩Q+
(TwX (U −) ∩U −
−µ) ⊗U +
µ.
This implies that
(T −1
wXτ ⊗ 1)(RRX ) ∈
∏
µ∈wXQ+∩Q+
U −
−wX (τ (µ)) ⊗U +
µ.
Using (7.2) we get
(T −1
w0τ0T −1
wXτ ⊗ 1)(RRX ) ∈
∏
µ∈wXQ+∩Q+
U +
wX (τ (µ))KwX (τ (µ)) ⊗U +
µ.
Asτ0 and TwX commute, relation (8.7) gives
(Ad(ξ)T −1
w0T −1
wXτ0τ ⊗ 1)(RRX) ∈
∏
µ∈wXQ+∩Q+
U +
wX (τ (µ))Kµ ⊗U +
µ
which completes the proof of the lemma. □
Lemma 9.2. For any i ∈I the following relation holds
(1 ⊗ri)R(τ,X ) =ρi(qi−q−1
i ) ·R(τ,X ) ·RX · (T −1
wX (Eτ (i)) ⊗ 1) ·RX · (Ki ⊗ 1)
in U (2)
0 whereρi =cτ (i)s(i)q−(αi,Θ( αi)), in particular ρi = 0 if i ∈X.
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 47
Proof. It follows from the intertwining property (3.5) of the quasi R-matr ix for
u =Fj and from relation (2.15) that
(1 ⊗rj)R = −(qj −q−1
j ) ·R · (Fj ⊗ 1) for all j ∈I.(9.3)
and that (1 ⊗ri)(RRX ) = 0 for i ∈ X. This proves the lemma for i ∈ X. Now
assume that i ∈ I \ X. In view of property (2.13) for U + and the fact that
(1 ⊗ri)RX = 0 for i ∈I \X, relation (9.3) implies that
(1 ⊗ri)(RRX ) = −(qi −q−1
i )R · (FiK −1
i ⊗ 1) ·RX · (Ki ⊗ 1).
Hence one gets
(1 ⊗ri)(Ad(ξ)T −1
w0T −1
wXττ 0 ⊗ 1)(RRX) =
= −(qi −q−1
i )(Ad(ξ)T −1
w0T −1
wXττ 0 ⊗ 1)
(
R · (FiK −1
i ⊗ 1) ·RX · (Ki ⊗ 1)
)
= −(qi −q−1
i )(Ad(ξ)T −1
w0T −1
wXττ 0 ⊗ 1)(RRX )·
· (Ad(ξ)T −1
w0T −1
wXττ 0 ⊗ 1)
(
RX · (FiK −1
i ⊗ 1) ·RX · (Ki ⊗ 1)
)
.(9.4)
Applying Lemma 8.6 to the second factor in the above expression we g et
(Ad(ξ)T −1
w0T −1
wXττ 0 ⊗ 1)
(
RX · (FiK −1
i ⊗ 1) ·RX · (Ki ⊗ 1)
)
=
=RX · (Ad(ξ)T −1
w0T −1
wXττ 0(Fi) ⊗ 1) · (K −1
i ⊗ 1) ·RX · (Ki ⊗ 1)
= −RX ·
(
Ad(ξ)(T −1
wX (Eτ (i)))KwX (ατ (i))−αi ⊗ 1
)
·RX · (Ki ⊗ 1).(9.5)
AsT −1
wX (Eτ (i)) ∈U +
−Θ( αi) relation (8.7) gives
Ad(ξ)(T −1
wX (Eτ (i))) = γ(τ (i))q−(αi,Θ( αi))T −1
wX (Eτ (i))Kαi+Θ( αi).
Inserting this expression into (9.5) gives
(Ad(ξ)T −1
w0T −1
wXττ 0 ⊗ 1)
(
RX · (FiK −1
i ⊗ 1) ·RX · (Ki ⊗ 1)
)
=
= −γ(τ (i))q−(αi,Θ( αi))RX ·
(
T −1
wX (Eτ (i)) ⊗ 1
)
·RX · (Ki ⊗ 1).
Finally, inserting the above formula into (9.4) produces the desired r esult. □

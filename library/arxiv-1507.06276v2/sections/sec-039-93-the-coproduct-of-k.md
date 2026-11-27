---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-039-93-the-coproduct-of-k
section_title: "The coproduct of K"
section_number: 9.3
pages: 49-51
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
ττ 0 :P →P and obtain elements κττ 0,κ −ττ 0 ∈ U (2)
0 . To simplify notation deﬁne
Rττ 0 =
∑
µ∈Q+
(ττ 0 ⊗ 1)(Rµ) =
∑
µ∈Q+
(1 ⊗ττ 0)(Rµ) ∈ U (2)
0
and
ˆRττ 0 =Rττ 0 ·κ−ττ 0 · ﬂip ∈ U (2).
Recall from Corollary 7.7 that K = XξT −1
wXT −1
w0 .
50 MARTINA BALAGOVI ´C AND STEF AN KOLB
Theorem 9.5. The coproduct of K in U (2) is given by
∆(K) = ( K ⊗ 1) · ˆRττ 0 · (K ⊗ 1) · ˆR.(9.14)
Proof. Using 6.1.(4) one veriﬁes that in U (2)
0 one has
(TwXTw0 ⊗ 1) · XK2 · (TwXTw0 ⊗ 1)−1 =κ−ττ 0 · (1 ⊗ X) ·κττ 0.(9.15)
Moreover, the following relation holds
κττ 0 · (Tw0TwX ⊗ 1) = (Tw0TwX ⊗ 1) ·κΘ.(9.16)
Combining the above two formulas with all our previous preparations we calculate
∆(K) = ∆(X) ·∆(ξ) ·∆(T −1
wX ) ·∆(T −1
w0 )
(9.10)
= ( X ⊗ 1) ·R(τ,X ) · XK2 ·∆(ξ) ·∆(T −1
wX ) ·∆(T −1
w0 )
(9.2)
= ( K ⊗ 1) ·Rττ 0 · (TwXTw0ξ−1 ⊗ 1) ·RX · XK2 ·∆(ξ) ·∆(T −1
wX ) ·∆(T −1
w0 )
(9.9)
= ( K ⊗ 1) ·Rττ 0 · (TwXTw0ξ−1 ⊗ 1) · XK2 ·∆(ξ) ·RX ·∆(T −1
wX ) ·∆(T −1
w0 )
(3.14)
= ( K ⊗ 1) ·Rττ 0 · (TwXTw0ξ−1 ⊗ 1) · XK2 ·∆(ξ) ·T −1
wX ⊗T −1
wX ·∆(T −1
w0 )
(9.15)
= ( K ⊗ 1) ·Rττ 0 ·κ−ττ 0 · (1 ⊗ X) ·κττ 0 · (TwXTw0ξ−1 ⊗ 1) ·∆(ξ)
·T −1
wX ⊗T −1
wX ·∆(T −1
w0 )
(9.16)
= ( K ⊗ 1) ·Rττ 0 ·κ−ττ 0 · (1 ⊗ X) · (TwXTw0ξ−1 ⊗ 1) ·κΘ ·∆(ξ)
·T −1
wX ⊗T −1
wX ·∆(T −1
w0 )
(8.5)
= ( K ⊗ 1) ·Rττ 0 ·κ−ττ 0 · (1 ⊗ Xξ) · (TwXTw0 ⊗ 1) ·κ−1
·T −1
wX ⊗T −1
wX ·∆(T −1
w0 )
(3.15)
= ( K ⊗ 1) ·Rττ 0 ·κ−ττ 0 · (1 ⊗ Xξ) · (TwXTw0 ⊗ 1) ·T −1
wX ⊗T −1
wX
·T −1
w0 ⊗T −1
w0 ·R21 ·κ−1
= ( K ⊗ 1) ·Rττ 0 ·κ−ττ 0 · (1 ⊗ XξT −1
w0T −1
wX ) ·R21 ·κ−1
= ( K ⊗ 1) · ˆRττ 0 · (K ⊗ 1) · ˆR
which gives the desired formula. □
Recall Deﬁnition 4.12 of a ϕ-universal K-matrix. Combining Corollary 7.7 with
Theorem 9.5 we obtain the ﬁrst statement of the following corollary.
Corollary 9.6. The element K = XξT −1
wXT −1
w0 ∈ U is a ττ 0-universal K-matrix
for the quantum symmetric pair coideal subalgebra Bc,s of Uq(g). In particular, K
satisﬁes the reﬂection equation
(K ⊗ 1) · ˆRττ 0 · (K ⊗ 1) · ˆR = ˆR · (K ⊗ 1) · ˆRττ 0 · (K ⊗ 1).(9.17)
in U (2).
Proof. The second statement follows from Remark 4.13 and Equation (4.8). Here
one needs to observe that ˆRN τ τ 0,M τ τ 0 = ˆRN,M considered as a map N ⊗M →M ⊗N
for all M,N ∈ Oint. □
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 51
Remark 9.7. The approach to quantum symmetric pairs in the papers [Nou96],
[NS95], [NDS97], [Dij96] is based on explicit solutions of the reﬂection equation. In
[Nou96] Noumi ﬁrst found a reﬂection equation for the symmetric pair s of type
AI : (slN, soN ), AII : (sl2N +1, sp2N ).
For the symmetric pairs of type
AIII : (slM+N, s(glM × glN ))
a diﬀerent reﬂection equation appeared in [NDS97]. The diﬀering reﬂection equa-
tions are uniﬁed by Equation (9.17). Indeed, the diagram automorphism ττ 0 is
non-trivial in types AI and AII, while ττ 0 is the identity in type AIII .

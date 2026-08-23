---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-014-appendix-a-complements-on-the-fourier-transform
section_title: "Appendix A. Complements on the Fourier transform"
section_number: null
pages: 41-43
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
doc_brief: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangu lated cusped hyperbolic 3-manifold (together with some further choices)"
---
In this appendix, we give the omitted details in the last step of the pro of of Theorem 3.4.
They are an aﬃne change of coordinates, followed by the correspo nding computation of the
formal Gaussian integration.
The proof requires a version of formal Gaussian integration where the symmetric matrix
Λ ℏ ∈ GLN ( /C9 (z)[x]/llbracketℏ1/2/rrbracket) depends on ℏ, such that Λ 0 is invertible. In this case, for an
integrable function fℏ(x,z ) ∈ /C9 (z)[x]/llbracketℏ1/2/rrbracket, we deﬁne
⟨ ⟨fℏ(x,z )⟩ ⟩x,Λ ℏ
:=
√
det(Λ ℏ)
det(Λ 0)
⟨
exp
(
− 1
2xt(Λ ℏ − Λ 0)x
)
fℏ(x,z )
⟩
x,Λ 0
=
∫
e− 1
2xtΛ( ℏ)xfℏ(x,z )dx∫
e− 1
2xtΛ( ℏ)xdx
∈ /C9 (z)/llbracketℏ/rrbracket.
(159)
This version of formal Gaussian integration satisﬁes the propertie s of Lemmas 3.1 and 3.2.
We use Equations ( 34) and Equation ( 37) to obtain that
ψℏ(x,z ) = e− ℏ
24Cℏ(x,z )
⟨⟨
exp
(y
2 ℏ
1
2
)
ψℏ
(
y, 1
1 −zexℏ1/2
)⟩⟩
y,1−z−1e−xℏ 1/2. (160)
Lemma 3.2 implies that
ψℏ(x,z ) = Cℏ(x,z ) exp
(
− ℏ
24 − ℏ1/2
2 (a +x)
)
×
⟨
exp
(y
2 ℏ
1
2 +
( 1
zexℏ1/2 − 1
z
) y2
2
)
ψℏ
(
y, 1
1 −zexℏ1/2
)⟩
y,1−z−1
,
(161)
where a =aℏ(x,z ) ∈ /C9 (z)[x]/llbracketℏ1/2/rrbracketis given by
a := 1
ℏ1/2 log
( 1 −z
1 −zexℏ1/2
)
∈ /C9 (z)[x]/llbracketℏ1/2/rrbracket. (162)
Similar to Equation ( 34) we write
ψℏ
(
y, 1
1 −zexℏ1/2
)
= exp
(
A0 − (a(1 −z−1) +x)y −
( 1
zexℏ1/2 − 1
z
) y2
2
)
ψℏ
(
y +a, 1
1 −z
)
(163)
42 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
where A0 =A0,ℏ(x,z ) ∈ 1
ℏ
/C9 (z)[x]/llbracketℏ1/2/rrbracketis given by
A0 = 1
2
(
log
( −zexℏ1/2
1 −zexℏ1/2
)
− log
( −z
1 −z
))
+ 1
ℏ
(
Li2
( 1
1 −zexℏ1/2
)
− Li2
( 1
1 −z
))
+ a2
2z + a
ℏ1/2 log
( −z
1 −z
)
= 1
2aℏ
1
2 + 1
2xℏ
1
2 + 1
ℏ
(
Li2
( 1
1 −zexℏ1/2
)
− Li2
( 1
1 −z
))
+ a2
2z + a
ℏ1/2 log
( −z
1 −z
)
.
(164)
Then Equation ( 161) can be written as
ψℏ(x,z ) = Cℏ(x,z ) exp
(
− ℏ
24 − ℏ1/2
2 (a +x) +A0
)
×
⟨
exp
(y
2 ℏ
1
2 − (a(1 −z−1 +x)y)
)
ψℏ
(
y +a, 1
1 −z
)⟩
y,1−z−1
.
(165)
We make the change of variables
w ↦→w −a + xz
1 −z (166)
and using Equation ( 23) of Lemma 3.1, we obtain that
ψℏ(x,z ) = Cℏ(x,z ) exp
(
− ℏ
24 − ℏ1/2
2 (a +x) +A0 + a2
2 − a2
2z +ax + x2
2(1 −z−1) − ℏ1/2
2 a
)
×
⟨
exp
(ℏ1/2
2
(
y + xz
1 −z
))
ψℏ
(
y + xz
1 −z, 1
1 −z
)⟩
y,1−z−1
.
(167)
Hence, it remains to show that
1 = Cℏ(x,z ) exp
(
− ℏ1/2
2 (a +x) +A0 + a2
2 − a2
2z +ax + x2
2(1 −z−1) − ℏ1/2
2 a
)
. (168)
In other words, using the deﬁnitions of Cℏ(x,z ) from Equation ( 34) and A0 from Equa-
tion ( 164) it suﬃces to prove that
0 = 1
ℏ
(
Li2
( 1
1 −zexℏ1/2
)
− Li2
( 1
1 −z
))
+ 1
ℏ
(
Li2(z) − Li2
(
zexℏ1/2))
+ a
ℏ1/2 log
( −z
1 −z
)
− x
ℏ1/2 log(1 −z) + a2
2 +ax.
(169)
With the transformation formula of the dilogarithm
Li2
( 1
1 −z
)
= Li 2(z) − π2
3 + log(z) log(1 −z) − 1
2 log2(z − 1) (170)
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 43
the right hand side of the previous equation is given by
1
ℏ
(
log
(
zexℏ1/2)
log
(
1 −zexℏ1/2)
− 1
2 log2(
zexℏ1/2
− 1
)
− log(z) log(1 −z) + 1
2 log2(z − 1)
)
+ a
ℏ1/2 log
( −z
1 −z
)
− x
ℏ1/2 log(1 −z) + a2
2 +ax.
(171)
With xℏ1/2 = log
(
exℏ1/2)
we compute
1
ℏ log
(
zexℏ1/2)
log
(
1 −zexℏ1/2)
− 1
ℏ log(z) log(1 −z) − x
ℏ1/2 log(1 −z) +ax
= 1
ℏ log
(
zexℏ1/2)
log
(
1 −zexℏ1/2)
− 1
ℏ log(z) log(1 −z) − 1
ℏ log(exℏ1/2
) log(1 −z) + a
ℏ1/2 log
(
exℏ1/2)
= 1
ℏ log
(
zexℏ1/2) (
log
(
1 −zexℏ1/2)
− log(1 −z)
)
+ a
ℏ1/2 log
(
exℏ1/2)
= − a
ℏ1/2 log
(
zexℏ1/2)
+ a
ℏ1/2 log
(
exℏ1/2)
= − a
ℏ1/2 log(z)
(172)
so that Equation ( 171) becomes
− 1
2ℏ log2(
zexℏ1/2
− 1
)
+ 1
2ℏ log2(z − 1) + a
ℏ1/2 log
( −z
1 −z
)
+ a2
2 − a
ℏ1/2 log(z)
= − 1
2ℏ log2(
zexℏ1/2
− 1
)
+ 1
2ℏ log2(z − 1) − a
ℏ1/2 log(z − 1) + a2
2
= − 1
2ℏ log2(
zexℏ1/2
− 1
)
+ 1
2
( 1
ℏ1/2 log(z − 1) −a
) 2
= − 1
2ℏ log2(
zexℏ1/2
− 1
)
+ 1
2ℏ log2(zexℏ1/2
− 1)
= 0,
(173)
which completes the proof of the last step of Theorem 3.4.

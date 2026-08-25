---
doc_id: arxiv-1112.0030v2
doc_title: "Homological algebra of knots and BPS states"
section_id: sec-005-appendix-d-computation-of-the-unreduced-homology
section_title: "Appendix D. Computation of the unreduced homology of the unknot"
section_number: null
pages: 42-44
source_pdf: 1112.0030v2.pdf
source_sha256: 745f143c2df4734b
doc_brief: "Homological algebra of knots and BPS states — It is known that knot homologies admit a physical descriptio n as spaces of open BPS states. W e study operators and algebras acting on these spaces."
---
For a nonnegative integer N we deﬁne the quantum dimension [ N ] to be
[N ] = qN− q−N
q− q−1 .
Also
[N ]! = [ N ][N− 1] . . .[1] ,
and [ N
k
]
= [N ][N− 1] . . .[N− k + 1]
[k]! .
For a partition λ = (λ1, λ2, . . .), we set:
|λ| =
∑
i
λi,
n(λ) =
∑
i
(i− 1)λi,
m(λ) =
∑
i
iλi,
||λ||2 =
∑
i
λ2
i .
By λt, we denote the dual (conjugate) partition of λ. We have
m(λ) = n(λ) +|λ|,
2m(λ) = ||λt||2 +|λ|.
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 43
We also deﬁne
κ(λ) := 2(||λ||2−|| λt||2) = 2( n(λt)− n(λ)).
We identify a partition and its corresponding Young diagram.
For a box x = (i, j)∈ λ, we deﬁne its content and the hook length by:
c(x) = j− i,
h(x) = λi + λt
j− i− j + 1.
For a partition λ and positive integer N , we set:
[ N
λ
]
:=
∏
x∈λ
[N− c(x)]
[h(x)] .
Then we have
(D.1) sλ (q1−N , q3−N , . . . , qN−3, qN−1) =
[
N
λt
]
.
Of course, the following holds
sλ (1, q2, q4, . . . , q2(N−2), q2(N−1)) = q(N−1)|λ|sλ (q1−N , q3−N , . . . , qN−3, qN−1).
D.1. Colored HOMFL Y polynomial of the unknot. We compute the
specialization of the superpolynomial of the unknot at q1 = q2 (i.e. at t =−1)
from the equation (6.1). According to (6.3), this gives the value of t he polynomial
of the Hopf link as well. We denote this specialization by
P
λ
( ), i.e.
P
λ
( ) := P
λ
( )|q1=q2 = P
λ
( )|t=−1 .
We also denote Z′
λ := Zλ|q1=q2 , and so
P
λ
( ) = ( −1)|λ|(Q−1)
|λ |
2 × Z′
λ
Z′
∅
,
with
Z′
λ =
∑
ν
(−Q)|ν|sν (q−ρ
2 )sν t (q−ρ
2 )sλ (q−ρ−ν t
2 ).
By using the following identity for the Schur functions
(D.2) sλ (q−ρ−ν t
2 )sν t (q−ρ
2 ) = q
− κ (λ )
2
2
∑
η
sν t/ η (q−ρ
2 )sλ t/ η (q−ρ
2 )
44 SERGEI GUKOV AND MARKO STO ˇSI ´C
in the expression for Z′
λ , we get
Z′
λ =
∑
ν
(−Q)|ν|sν (q−ρ
2 )q
− κ (λ )
2
2
∑
η
sν t/ η
(q−ρ
2 )sλ t/ η
(q−ρ
2 ) =
= q
− κ (λ )
2
2
∑
η
sλ t/ η
(q−ρ
2 )
∑
ν
(−Q)|ν|sν (q−ρ
2 )sν t/ η
(q−ρ
2 ) =
= q
− κ (λ )
2
2
∑
η
sλ t/ η
(q−ρ
2 )
∑
ν
(−Q)|ν|sν (q−ρ
2 )
∑
ϕ
cν t
η,ϕ sϕ (q−ρ
2 ) =
= q
− κ (λ )
2
2
∑
η
sλ t/ η (q−ρ
2 )
∑
ϕ
sϕ (q−ρ
2 )
∑
ν
(−Q)|η|+|ϕ|cν t
η,ϕ sν (q−ρ
2 ) =
= q
− κ (λ )
2
2
∑
η
sλ t/ η
(q−ρ
2 )(−Q)|η| ∑
ϕ
(−Q)|ϕ|sϕ (q−ρ
2 )sϕ t (q−ρ
2 )sη t (q−ρ
2 ) =
= q
− κ (λ )
2
2
∑
η
(−Q)|η|sλ t/ η
(q−ρ
2 )sη t (q−ρ
2 )× Z′
∅.
Hence, the value of the colored HOMFLY polynomial invariant of the u nknot
labeled by λ is given by:
(D.3) P
λ
( ) = q
− κ (λ )
2
2 · (−1)|λ|(Q−1)
|λ |
2
∑
η
(−Q)|η|sλ t/ η (q−ρ
2 )sη t (q−ρ
2 ) .
In particular, the last formula tells us that (up to an overall factor ) Pλ is a poly-
nomial in Q of degree|λ|. Also, at Q = 1 one ﬁnds that P λ|Q=1 = 0 for λ⁄= 0.
Written in terms of the knot-theoretical variables ( a, q) the polynomial becomes:
(D.4) P
λ
( )(a, q) = q−κ (λ )· (−1)|λ|aλ ∑
η
(−1)|η|a−2|η|sλ t/ η (q−2ρ )sη t (q−2ρ ) .
Finally, when a = qN one can show that the above expression without the
factor q−κ (λ ) is equal to
[ N
λt
]
.

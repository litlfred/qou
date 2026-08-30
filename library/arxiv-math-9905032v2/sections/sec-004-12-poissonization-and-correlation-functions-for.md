---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-004-12-poissonization-and-correlation-functions-for
section_title: "Poissonization and correlation functions. For θ > 0, con-"
section_number: 1.2
pages: 4-6
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
sider the poissonization M θ of the measures Mn
M θ (λ) = e−θ∑
n
θn
n! Mn(λ) = e−θ θ|λ |
(dim λ
|λ|!
)2
.
This is a probability measure on the set of all partitions. Ou r ﬁrst
result is the computation of the correlation functions of th e measures
M θ .
By correlation functions we mean the following. By deﬁnitio n, set
D(λ) = {λi − i} ⊂ Z .
Also, following [37], deﬁne the modiﬁed Frobenius coordinates Fr(λ) of
a partition λ by
(1.2) Fr( λ) =
(
D(λ) + 1
2
)
△
(
Z≤0 − 1
2
)
=
{
p1 + 1
2 , . . . , pd + 1
2, −q1 − 1
2 , . . . ,−qd − 1
2
}
⊂ Z + 1
2 ,
where △ stands for the symmetric diﬀerence of two sets, d is the number
of squares on the diagonal of λ, and pi’s and qi’s are the usual Frobenius
coordinates of λ. Recall that pi is the number of squares in the ith
row to the right of the diagonal, and qi is number of squares in the
ith column below the diagonal. The equality (1.2) is a well kno wn
combinatorial fact discovered by Frobenius, see Ex. I.1.15 (a) in [22].
Note that, in contrast to Fr( λ), the set D(λ) is inﬁnite and, moreover,
it contains all but ﬁnitely many negative integers.
The sets D(λ) and Fr( λ) have the following nice geometric interpre-
tation. Let the diagram λ be ﬂipped and rotated 135 ◦ as in Figure 1,
but not scaled. Denote by ωλ a piecewise linear function with ω′
λ = ±1
whose graph if given by the upper boundary of λ completed by the
lines
v = |u| , u / ∈ [−λ′
1, λ1] .
Then
k ∈ D(λ) ⇔ ω′
λ
⏐
⏐
⏐
[k,k +1]
= −1 .
In other words, if we consider ωλ as a history of a walk on Z then D(λ)
are those moments when a step is made in the negative directio n. It
is therefore natural to call D(λ) the descent set of λ. As we shall see,
the correspondence λ ↦→D(λ) is a very convenient way to encode the
local structure of the boundary of λ.
The halves in the deﬁnition of Fr( λ) have the following interpreta-
tion: one splits the diagonal squares in half and gives half t o the rows
and half to the columns.
ASYMPTOTICS OF PLANCHEREL MEASURES 5
Deﬁnition 1.1. The correlation functions of M θ are the probabilities
that the sets Fr( λ) or, similarly, D(λ) contain a ﬁxed subset X. More
precisely, we set
ρθ (X) = M θ ({λ | X ⊂ Fr(λ)}) , X ∈ Z + 1
2 ,(1.3)
̺θ (X) = M θ ({λ | X ⊂ D(λ)}) , X ∈ Z .(1.4)
Theorem 1. For any X = {x1, . . . , xs} ⊂ Z + 1
2 we have
ρθ (X) = det
[
K(xi, xj)
]
1≤i,j ≤s
,
where the kernel K is given by the following formula
K(x, y) =







√
θ k+(|x|, |y|)
|x| − |y| , xy > 0 ,
√
θ k−(|x|, |y|)
x − y , xy < 0 .
(1.5)
The functions k± are deﬁned by
k+(x, y) = Jx− 1
2
Jy+ 1
2
− Jx+ 1
2
Jy− 1
2
,(1.6)
k−(x, y) = Jx− 1
2
Jy− 1
2
+ Jx+ 1
2
Jy+ 1
2
,(1.7)
where Jx = Jx(2
√
θ) is the Bessel function of order x and argument
2
√
θ.
This theorem is established in Section 2.1, see also Remark 1 .2 below.
By the complementation principle, see Sections A.3 and 2.2, Theorem
1 is equivalent to the following
Theorem 2. For any X = {x1, . . . , xs} ⊂ Z we have
̺θ (X) = det
[
J(xi, xj)
]
1≤i,j ≤s
,(1.8)
Here the kernel J is given by the following formula
J(x, y) = J(x, y; θ) =
√
θ Jx Jy+1 − Jx+1 Jy
x − y ,(1.9)
where Jx = Jx(2
√
θ).
Remark 1.2. Theorem 1 is a limit case of Theorem 3.3 of [6]. For the
reader’s convenience a direct proof of it is given in Section 2. Another
proof of the results of [6] will appear in [7]. Various limit c ases of the
results of [6] are discussed in [8]. By diﬀerent methods, the formula
(1.8) was obtained by K. Johansson [15].
A representation–theoretic proof of a more general formula than The-
orem 3.3 of [6] has been subsequently given in [24].

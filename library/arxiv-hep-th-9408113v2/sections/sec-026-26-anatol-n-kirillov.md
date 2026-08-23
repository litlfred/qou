---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-026-26-anatol-n-kirillov
section_title: "Anatol N. Kirillov"
section_number: 26
pages: 26-28
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
Remark. One can show that the ﬁve-term relation (1.4) follows from th e nine-term
relation (1.30). Namely, let us take x := a = b and y := bc in (1.30) ( a,b,c ∈ R). Then
(1.30) is reduced to the relation
L(xy) = L(x) +L(y) +L
(
−x 1−y
1−x
)
+L
(
−y 1−x
1−y
)
,
which is a form of the ﬁve-term relation due to C. Hill (see e.g . [Le1]).
Hint: using the Landen result Re
(
L(x) +L
( −x
1−x
))
= 0, replace the terms L(a)
and L(b) in RHS of (1.6) on −L
( −a
1−a
)
and−L
( −b
1−b
)
correspondently. It is easy to
check that −a
1−a =−x 1−y
1−x and −b
1−b =−y 1−x
1−y .
1.4. Kuniba-Nakanishi’s dilogarithm conjecture.
Recall that the dilogarithm function is deﬁned by
Li2(z) =
∞∑
n=1
zn
n2, (|z|< 1).
By using the integral representation
Li2(z) =−
∫ z
0
log(1−t)
t dt, (1.32)
Li2(z) can be analytically continued as a multivalued complex fun ction to the complex
plane cut along the real axis from 1 to + ∞. In the sequel the principal branch of diloga-
rithm which can be deﬁned by taking the principal branch of lo garithm function
−π <Im(log(z)) = arg(z)≤π
in the previous integral is used. The integration contour in (1.32) does not pass through
the branch cut of log z. Let us consider also the principal branch of Rogers’ diloga rithm
using the integral representation
L(z) =− 1
2
∫ z
0
(log(1−x)
x + logx
1−x
)
dx, (1.33)
where the principal branch of logarithm function is taken. T he integration contour in
(1.33) is assumed to be located in the branch of log x.
Let us set
Qm(ϕ) = sin(m + 1)ϕ
sinϕ , f m(ϕ) = 1− Qm+1(ϕ)Qm−1(ϕ)
Q2
m(ϕ) = 1
Q2
m(ϕ),
Dilogarithm identities 27
where ϕ = π(j + 1)
r + 2 , 1≤j≤r and g.c,d. ( j + 1,r + 2) = 1.
Following [KN] and [KNS], let us deﬁne c0(ϕ), dm(ϕ), and y(ϕ) as
π2
6 c0(ϕ) =
r−1∑
m=1
(
L(fm(ϕ))− πi
2 dm(ϕ) log(1−fm(ϕ))
)
,
πidm(ϕ) = log fm(ϕ)− 2
r−1∑
k=1
Amk log(1−fk(ϕ)), where
Amk = min(k,m )− km
r , 1≤m,k≤r− 1,
y(ϕ) = 1
πi
{ r−1∑
k=1
k log(1−fk(ϕ)) +r logQr−1(ϕ)− (r− 1) logQr(ϕ)
}
.
1.4.1. Kuniba-Nakanishi’s conjecture for sl(2).
N (j,r ) := 1
24
{ 3r
r + 2− 1− 6j(j + 2)
(r + 2) + 6y2
r −c0(ϕ)
}
∈ Z.
Remarks. 1) One can show that y :=y(ϕ) is an integer for any ϕ, whereas dm(ϕ) is
an integer if ϕ = π(j + 1)
r + 2 . Namely, it follows from deﬁnition that ( fm :=fm(ϕ), Q m :=
Qm(ϕ))
1−fm = Qm+1Qm−1
Q2
m
.
Consequently,
r−1∏
k=1
(1−fk)kQr
r−1Q−(r−1)
r = 1,
that is equivalent to exp(2 πiy(ϕ)) = 1. Now, if ϕ = π(j + 1)
r + 2 , then Qr =fr = 1 and
(1−fm)2 = f 2
m
fm−1fm+1
.
Using the fact that the matrix A := (Amk) appears to be the inverse to the Cartan matrix
Cr−1 = (2δi,j−δi+1,j−δi,j+1), 1≤i,j ≤r− 1, one can check
fm =
r−1∏
k=1
(1−fk)2Amk.
Consequently, log(2πidm(ϕ)) = 1, as it was claimed.

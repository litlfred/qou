---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-011-33-comparing-the-cyclotomic-and-the-loop-expansi
section_title: "Comparing the cyclotomic and the loop expansion"
section_number: 3.3
pages: 10-10
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
cyclotomic expansion, one should treat qn and q (where n is the color) as two independent variables. Con-
sider two independent variables z (standing for α) and y (standing for α/n). Let us deﬁne the following
biholomorphic functions
ck(z, y) =
k∏
j=1
(ez + e−z − ejy − e−jy ),
hK,k (z, y) = ck(z, y)HK,k (ey).
The cyclotomic expansion says that for every n we have:
(14) fK,n (α) =
∞∑
k=0
hK,k (α, α/n) ∈ Q[[α]].
The loop expansion is a Taylor expansion in α/n, so we will consider the Taylor expansion in y (around
0) of hK,k (z, y):
hK,k (z, y) =
∞∑
p=0
dk,p (z) yp,
where dk,p (z) (which depends on K) is holomorphic for z ∈ C.
Comparing the loop and the cyclotomic expansion (Equations (
10) and ( 14)), we obtain that:
Lemma 3.2. For every knot K and every p ∈ N we have
(15) RK,p (x) =
∞∑
k=0
dk,p (x) ∈ Q[[x]].
as formal power series in x.

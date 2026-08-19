---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-013-41-uniform-bounds-of-the-colored-jones-function
section_title: "Uniform bounds of the colored Jones function"
section_number: 4.1
pages: 10-11
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
estimates of the degree and the coeﬃcients of the cyclotomic expa nsion of the knot. These estimates will be
established in Section 6. By deﬁnition fK,n (α) = JK,n (eα/n ), hence equation ( 12) gives that
fK,n (α) =
n−1∑
k=0
Cn,k (eα/n )HK,k (eα/n ).(16)
To have upper bounds for |fK,n (α)| we will need bounds for HK,k (eα/n ) and the “kernel” Cn,k (eα/n ) (the
kernel does not depend on the knot K).
Deﬁnition 4.1. For a Laurent polynomial f (q) =∑
k akqk, we deﬁne its l1-norm by
||f ||1 =
∑
k
|ak|.
The proof of the following Theorem, which gives bounds for the degr ees and the l1-norm of HK,n , will be
given in Section 7.
ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT 11
Theorem 4.2. (Proof in Section 7) For every knot K, there are positive constants A0, A1 (depending on
K) such that for all n ∈ N we have
(a) HK,n (q) =
A0n2
∑
j=−A0n2
bj,n qj.
and
(b) ||HK,n ||1 ≤ An
1 .
The next lemma follows from Theorem
4.2 and an elementary estimate.
Lemma 4.3. Suppose |α| < 1.
(a) For every knot K there is a constant A2 such that for every 0 ≤ k ≤ n, we have
|HK,k (eα/n )| ≤ (A2)k.
(b) There is a constant A3 > 0 such that every 0 ≤ k ≤ n we have:
|Cn,k (eα/n )| ≤ (A3)k|α|k.
Proof. (a) By Theorem 4.2(a),
HK,k (eα/n ) =
A0k2
∑
j=−A0k2
bj,k ejα/n .
From the bounds for j and k ≤ n one has that |j/n| ≤ A0k, hence |ejα/n | ≤ exp(A0 k |ℜ(α)|) ≤ exp(k A0).
From the above equation one has
⏐
⏐
⏐HK,k (eα/n )
⏐
⏐
⏐ ≤ ||HK,k ||1 (exp A0)k.
Using Theorem
4.2, it is enough to take A2 = A1 exp(A0).
(b) By deﬁnition,
Cn,k (eα/n ) =
k∏
j=1
(eα + e−α − ejα/n − e−jα/n ) =
k∏
j=1
(g(α) − g(jα/n)) ,
where g(z) = ez + e−z. One has g′(z) = ez − e−z, hence for z on the interval connecting α and jα/n, with
0 ≤ j ≤ n, one has |g′(z)| ≤ 2 exp(|α|) ≤ 2e. By the mean value theorem, we have, for 0 ≤ j ≤ k ≤ n,
|g(α) − g(jα/n)| ≤ 2e|α − jα/n| ≤ 2e|α|.
It follows that
|Cn,k (eα/n )| ≤ (2e)k|α|k.
It is enough to take A3 = 2e. □

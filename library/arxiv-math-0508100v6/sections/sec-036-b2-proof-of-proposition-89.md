---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-036-b2-proof-of-proposition-89
section_title: "B.2. Proof of Proposition 8.9"
section_number: null
pages: 28-30
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
achieves maximum when k satisﬁes the condition in Lemma B.4(b), b = ⌊(n − 1)/4⌋, and a = b + k. The
value of k satisfying the condition in Lemma B.4(b) can be calculated easily:
ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT 29
k =









n/2 + 1 n = 0 mod 4
(n − 1)/2 n = 1 mod 4
n/2 n = 2 mod 4
(n + 1)/2 n = 3 mod 4
From there one can calculate a = k + b. It is easy to check that the values of a, b, k are exactly the ones
given in Proposition
8.9.
Now turn to R−(n; a, b, k). By ( 51),
|R−(n; a, b, k)| = |R+(n; b, a, k)|.
Hence |R−(n; a, b, k)| and |R+(n; b, a, k)| have the same maximum, and |R−(n; a, b, k)| achieves maximum
when |R+(n; b, a, k)| achieves maximum.
This completes the proof of Proposition 8.9, modulo the following lemma.
Lemma B.5. For 1 ≤ j ≤ n−1
4 , with n ≥ 7, one has x2j−1 > x 2
j .
Proof. With xj = 2 sin(jπ/n), the statement is equivalent to
sin((2j − 1)π/n) > 2 sin2(jπ/n),
which, using 2 sin 2(x) = 1 − cos(2x), is equivalent to
(58) sin((2 j − 1)π/n) + cos(2jπ/n) > 1 for 1 ≤ j ≤ n − 1
4 .
We will prove ( 58) not only for integer j, but for all real j ∈ [1, n−1
4 ].
The function f (j) = sin((2 j − 1)π/n) + cos(2jπ/n) has the second derivative
f ′′(j) = −(2π/n)2 (sin((2j − 1)π/n) + cos(2jπ/n))
which is strictly negative on the interval [1 , n−1
4 ]. Hence f (j) achieves absolute minimum at one of the end
points 1 and n−1
4 . It is enough to show that the values of f at these two end points are bigger than 1.
End point 1. The inequality f (1) > 1 is
(59) sin( π/n) + cos(2π/n) > 1.
The function f1(x) = sin x + cos(2x) has the second derivative
f ′′
1 (x) = − sin x − 4 cos(2x)
which is strictly negative on the interval (0 , π/6). Hence on the closed interval [0 , π/6] the function f1(x)
achieves the absolute minimum at one of the end points. But f1(0) = f1(π/6) = 1. If n ≥ 7, then
π/n ∈ (0, π/6). Hence f1(π/n) > 1, which is ( 59).
End point n−1
4 . One has
f
(n − 1
4
)
= sin
(π
2 − 3π
2n
)
+ cos
(π
2 − π
2n
)
= cos(3 π/2n) + sin(π/2n) because sin( π/2 − x) = cos x.
Hence f ((n − 1)/4) > 1 is equivalent to
(60) sin( π/2n) + cos(3π/2n) > 1.
Look at the function f2(x) = sin x + cos(3x) on the interval [0 , π/14]. The second derivative
f ′′
2 (x) = − sin x − 9 cos(3x)
is strictly negative on the interval (0 , π/14), and f2(0) = 1 and f2(π/14) = 1 .004... > 1. It follows that
f2(x) > 1 for x ∈ (0, π/14]. If n ≥ 7, then π/2n ∈ (0, π/14]. Hence f2(π/2n) > 1, which is ( 60). □
30 STA VROS GAROUF ALIDIS AND THANG TQ L ˆE

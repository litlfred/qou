---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-006-24-the-euler-maclaurin-formula
section_title: "The Euler-Maclaurin Formula"
section_number: 2.4
pages: 34-36
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
---
The Euler-Maclaurin formula is a formula which enables us to make a connection
between a sum and its corresponding integral, provided the function is suﬃciently
smooth. Before we can state the formula, we need a few preliminary deﬁnitions
and notation. Let ⌊x⌋ denote the greatest integer function, so that ⌊x⌋ returns the
greatest integer less than or equal to x. For s = 1, 2,... , let Bs(x) denote the
Bernoulli polynomials. The generating function for the Bernoulli polynomials is as
follows:
text
et− 1 =
∞∑
s=0
Bs(x)ts
s!
Fors≥ 1, we will let Bs :=Bs(0). These Bs are called the Bernoulli numbers. The
ﬁrst few Bernouli numbers are given byB1 =−12, B2 = 16, B3 = 0, B4 = 130, B5 =
26
0,B 6 = 142. See [Andrews et al., 1999] for more details and alternative deﬁnitions.
We now have everything that we need to state the Euler-Maclaurin formula.
Theorem 2.4.1. Supposef has continuous derivatives up to order s. Then
n∑
m+1
f(x) =
∫ n
m
f(x)dx +
s∑
i=1
(−1)iBi
i! (f (i−1)(n)−f (i−1)(m))
+ (−1)i−1
i!
∫ n
m
Bs(x−⌊x⌋)f (i)(x)dx (2.11)
Notice that this formula allows a sum to be estimated by its corresponding in-
tegral (or an integral by its sum), and gives an exact formula for the error in using
this estimation. In many applications, this error term can at least be bounded, if not
computed exactly. The proof of the formula involves successively performing integra-
tion by parts, which gives a sequence of periodic functions relating to the Bernoulli
polynomials. For a proof, see [Andrews et al., 1999]. We will use a similar method of
proof to prove a q-deformed version of Stirling’s formula in a later section.
27
3 Random Operator
Compressions

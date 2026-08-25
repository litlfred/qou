---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic dilogarithm identities"
section_id: sec-028-3-li2z2-6-li2z-ln2zz2-6-lnz-lnz-1-π2
section_title: "Li2(z2) + 6 Li2(z) =− ln2(z−z2)− 6 ln(z) ln(z + 1) +π2"
section_number: 3
pages: 22-23
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
doc_brief: "Analytic dilogarithm identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
Note that z = 1/p where p is the so-called Plastic Constant or ratio, given as the real root
of p3−p− 1 = 0. It also obeys the following identities: p− 1 = p−4,p−5 = 1− 1/p,p 3 =
p + 1,p 2 = 1 + 1/p. Thus we have the following relations:
Li2(p−2) + 2Li2(p−1) =−8 ln2(p) +π2
3
Li2(p−1) + Li2(p−5) = π2
6 − 5 ln2(p)
Li2(p−2)− 2Li2(p−5) = 2 ln2(p)
Li2(p2) + Li2(p3) =−1
2 ln2(p) +π2
2
Li2(−p−4)− Li2(p−1) =−π2
6 + 9
2 ln2(p)
This also leads to various ladder expressions:
5
2Li2(p−2) + Li2(p−1)− 4Li2(p−5) = π2
6
Li2
 1
p14

− 4Li2
 1
p7

+ 6Li2
 1
p5

= π2
6 − 8 ln2(p)
Example 11. Settingu = 1/2+iµ, it is possible to derive additional single-term dilogarithms
by combining the first identity in Theorem 4 with (37). Define µ as an algebraic number
given by the expression below. This is derived by setting solving for real µ for u = 1/2 +iµ
, which has four possible solutions:
1
2 =ℜ
 
4
±
p
12µ2 + 4iµ + 5− 2iµ + 3
!
The solutions are the real roots of −256c8 + 96c4 + 544c2− 125 = 0, or:
µ1≈± 1.1441...µ2≈± 0.4714...
Plugging u = 1/2 +µ2i into the first identity in Theorem 4 thus produces a single-term
dilogarithm identity, and the same holds for u = 1/2 +µ1i. Moreover, we have that µ1,µ 2
admit closed forms, with
µ2
1 = 1
32
r
k1 + 192
3 + 1
2
s
− k1
768 + 1
2 + 68
r
3
k1 + 192
22
and
µ2
2 = 1
32
r
k1 + 192
3 − 1
2
s
− k1
768 + 1
2 + 68
r
3
k1 + 192,
writing
k1 = 128· 22/3· 31/3

(45−
√
1929)1/3 + (45 +
√
1929)1/3

.
Using the two-term identity in Example 3, these are obtained by solving a system of equa-
tions, where θ = 1 corresponds to µ1 and θ =−1 corresponds to µ2.
3
4 +θ
q
12µ2 + 5 +
p
144µ4 + 136µ2 + 25
4
√
2 = 2
4k2 + 1
−µ
2 +θ
q
−12µ2− 5 +
p
144µ4 + 136µ2 + 25
4
√
2 = −4k
4k2 + 1
This allows us to produce the explicit identity such that
− 3ℜ Li2
 24k2− 2 + 4i(4k2µ− 4k +µ)
4k2(4µ2 + 9)− 32kµ + 4µ2 + 1

=−1
8 ln2(k2 + 1
4)+
ln2
4kµ + 6ik− 2iµ− 1
4kµ + 2ik− 2iµ− 3

− 5
2 arctan2(2k)− arctan2(2µ) +π arctan(2µ).

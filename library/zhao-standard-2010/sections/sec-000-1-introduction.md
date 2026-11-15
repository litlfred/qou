---
doc_id: zhao-standard-2010
doc_title: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: Zhao_standard_2010.pdf
source_sha256: 94a70847c2937ba7
toc_source: inferred
doc_brief: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity — Let N be a positive integer."
---
Introduction
2
1.1
Multiple polylog values at roots of unity . . . . . . . . . . . . .
3
1.2
Standard relations of MPVs . . . . . . . . . . . . . . . . . . . .
4
1.3
Main results . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
1.4
Acknowledgment . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2
The double shuffle relations and the algebra A
6
3
Weight one relations
10
4
Regularized distribution relations
10
5
Lifted relations from lower weights
14
6
Some conjectures of FDS and RDS
16
7
The structure of MPVs and some examples
17
7.1
Weight one
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
7.2
Weight two
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
7.3
Weight three
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
7.4
Upper bound of d(w, N) by Deligne and Goncharov
. . . . . .
21
8
Computational results in weight two
21
9
Computational results in weight three, four and five
29
1
Introduction
In recent years, there is a revival of interest in multi-valued classical polyloga-
rithms (polylogs) and their generalizations. For any positive integers s1, . . . , sℓ,
multiple polylogs of complex variables are deﬁned as follows (note that our in-
dex order is opposite to that of [19]):
Lis1,...,sℓ(x1, . . . , xℓ) =
X
k1>···>kℓ>0
xk1
1 · · · xkℓ
ℓ
ks1
1 · · · ksℓ
ℓ
,
(1)
where |x1 · · · xj| < 1 for j = 1, . . . , ℓ. It can be analytically continued to a
multi-valued meromorhpic function on Cℓ(see [29]). Conventionally ℓis called
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm Values
3
the depth (or length) and s1 + · · · + sℓthe weight. When the depth ℓ= 1 the
function is nothing but the classical polylog. When the weight is also 1 one
gets the MacLaurin series of −log(1 −x). Moreover, setting x1 = · · · = xℓ= 1
and s1 > 1 one obtains the well-known multiple zeta values (MZVs). If one
allows xj’s to be ±1 then one gets the so-called alternating Euler sums.

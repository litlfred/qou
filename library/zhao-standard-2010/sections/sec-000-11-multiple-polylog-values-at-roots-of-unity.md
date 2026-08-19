---
doc_id: zhao-standard-2010
doc_title: "Documenta Math. 1 Standard Relations of Multiple Polylogarithm V alues at Roots of Unity Dedicated to Prof. Keqin Feng on his 70th birthday Jianqiang Zhao"
section_id: sec-000-11-multiple-polylog-values-at-roots-of-unity
section_title: "Multiple polylog values at roots of unity"
section_number: 1.1
pages: 2-4
source_pdf: Zhao_standard_2010.pdf
source_sha256: 94a70847c2937ba7
doc_brief: "Documenta Math. 1 Standard Relations of Multiple Polylogarithm Values at Roots of Unity Dedicated to Prof. Keqin Feng on his 70th birthday Jianqiang Zhao — Let N be a positive integer."
---
1.2 Standard relations of MPVs . . . . . . . . . . . . . . . . . . . . 4
1.3 Main results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.4 Acknowledgment . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2 The double shuffle relations and the algebra A 6
3 Weight one relations 10
4 Regularized distribution relations 10
5 Lifted relations from lower weights 14
6 Some conjectures of FDS and RDS 16
7 The structure of MPVs and some examples 17
7.1 Weight one . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
7.2 Weight two . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
7.3 Weight three . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
7.4 Upper bound of d(w, N) by Deligne and Goncharov . . . . . . 21
8 Computational results in weight two 21
9 Computational results in weight three, four and five 29
1 Introduction
In recent years, there is a revival of interest in multi-valu ed classical polyloga-
rithms (polylogs) and their generalizations. For any posit ive integers s1, . . . , sℓ,
multiple polylogs of complex variables are deﬁned as follow s (note that our in-
dex order is opposite to that of [19]):
Lis1,...,sℓ(x1, . . . , xℓ) =
∑
k1>···>kℓ>0
xk1
1 · · ·xkℓ
ℓ
ks1
1 · · ·ksℓ
ℓ
, (1)
where |x1 · · ·xj| < 1 for j = 1 , . . . , ℓ. It can be analytically continued to a
multi-valued meromorhpic function on Cℓ (see [29]). Conventionally ℓ is called
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm V alues 3
the depth (or length) and s1 + · · ·+ sℓ the weight. When the depth ℓ = 1 the
function is nothing but the classical polylog. When the weig ht is also 1 one
gets the MacLaurin series of − log(1 − x). Moreover, setting x1 = · · ·= xℓ = 1
and s1 > 1 one obtains the well-known multiple zeta values (MZVs). If one
allows xj ’s to be ±1 then one gets the so-called alternating Euler sums.
1.1 Multiple polylog values at roots of unity
In this paper, the primary objects of study are the multiple p olylog values at
roots of unity (MPVs). These special values, MZVs and the alt ernating Euler
sums in particular, have attracted a lot attention in recent years after they were
found to be connected to many branches of mathematics and phy sics (see, for
e.g., [7, 8, 10, 11, 15, 19, 28]). Results up to around year 200 0 can be found in
the comprehensive survey paper [6].
Starting from early 1990s Hoﬀman [21, 22] has constructed so me quasi-shuﬄe
(called stuﬄe in [6]) algebras reﬂecting the essential combinatorial pro perties of
MZVs. Later he [23] extends this to incorporate MPVs althoug h his deﬁnition
of ∗-product is diﬀerent from ours. This approach was then impro ved in [24] and
[26] to study MZVs and MPVs in general, respectively, where t he regularized
double shuﬄe relations play prominent roles. One derives th ese relations by
comparing (1) with another expression of the multiple polyl ogs given by the
following iterated integral:
Lis1,...,sℓ(x1, . . . , xℓ) =
(−1)ℓ
∫ 1
0
(dt
t
) ◦(s1−1)
◦ dt
t − a1
◦ · · · ◦
(dt
t
) ◦(sℓ−1)
◦ dt
t − aℓ
, (2)
where ai = 1 /(x1 . . . xi) for 1 ≤ i ≤ ℓ. Here, one deﬁnes the iterated integrals
recursively by
∫ b
a f (t) ◦ w(t) =
∫ b
a (
∫ x
a w(t))f (x) for any 1-form w(t) and con-
catenation of 1-forms f (t). One may think the path lies in C; however, it is
more revealing to use iterated integrals in Cℓ to ﬁnd the analytic continuation
of this function (see [29]).
The main feature of this paper is a quantitative comparison b etween the results
obtained by Racinet [26] who considers MPVs from the motivic viewpoint of
Drinfeld associators, and those by Deligne and Goncharov [1 7] who study the
motivic fundamental groups of P1 − ({0, ∞} ∪µ N ) by using the theory of mixed
Tate motives over S-integers of number ﬁelds, where µ N is the group of N th
roots of unity.
Fix an N th root of unity µ = µ N := exp(2π√
−1/N). An MPV of level N is a
number of the form
LN (s1, . . . , sℓ|i1, . . . , iℓ) := Lis1,...,sℓ(µ i1 , . . . , µ iℓ). (3)
We will always identify ( i1, . . . , iℓ) with ( i1, . . . , iℓ) (mod N ). It is easy to see
from (1) that an MPV converges if and only if ( s1, µ i1 ) ⁄= (1 , 1). Clearly, all
Documenta Mathematica 15 (2010) 1–34

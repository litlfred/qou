---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Steklov Mathematical Institute"
section_id: sec-027-28-anatol-n-kirillov
section_title: "Anatol N. Kirillov"
section_number: 28
pages: 28-30
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "DILOGARITHM IDENTITIES ANATOL N. KIRILLOV — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
2) If ϕ = π(j + 1)
r + 2 , 0≤j≤r, and g.c.d.(j + 1,r + 2) = 1, it can be shown that
y(ϕ) = r min(j,r−j + (−1)j).
3) It follows from the deﬁnitions that ( x∈ R)
L(x) = π2
3 − L(x−1)− πi
2 logx, if x≥ 1, (1.34)
L(x) =−π2
6 + L
( 1
1−x
)
+ πi
2 log(1−x), if x≤ 0.
Thus (see (1.5)), the single-valued dilogarithm is the real part of L(x), if x∈ R.
Before stating our main results of this section, let us consi der an explanatory example.
Example. Assume r = 3 and j = 1, then we have ϕ = 2π
5 and
f1 =f2 =
(
2 sec 2π
5
)2
=ρ−2 = 3 +
√
5
2 ; 1 −f1 =−ρ−1.
First of all, πid1 = logf1− 2 log(1−f1) =−2πi. Thus, d1 =d2 =−2. Further, using the
fact Q2 = 1−Q2
1 = 1
f1− 1 , one can ﬁnd
y = 1
πi{log(1−f1) + 2 log(1−f2) + 3 logQ2} = 3
πi (log(1−f1)− log(f1− 1)) = 3.
Consequently,
π2
6 c0(ϕ) = 2(L(f1) +πi log(1−f1)) = 2(π2
3 −L(ρ2)− πi
2 logf1 +πi log(f1− 1)−π2)
= 2π2
(1
3− 1
15− 1
)
=− 44
5 L(1).
Here we used (1.34) and Landen’s result L(ρ2) = π2
15 . Finally,
N (1, 3) = 1
24
{ 9
5− 1− 18
5 + 18 + 44
5
}
= 1.
Even more, using the result (1.16) with j = 0, 1,r− 1,r andr≡ 1 (mod2), it can be shown
that N (1,r ) = r− 1
2 , N (r− 1,r ) = r and N (0,r ) = N (r,r ) = 0.
Dilogarithm identities 29
Theorem 3. Let r be an odd positive integer and j be an integer such that
0≤ 2j + (−1)j+1≤r. Then
N (r−j,r ) = N (j,r ) +j(−1)j−1r + (−1)j+1
2 .
To obtain an additional information about the numbers N (j,r ) let us introduce a
function
bj(r) := j2(r− 1)
2 − j3−j
6
[ r
j + 1
]
−N (j,r ),
where [x] is the integer part of a real number x.
Note that according to Theorem 3, it is suﬃcient to consider a behavior of the function
bj(r) only in the ”stable region”, namely when r≥ 2j + (−1)j+1.
Theorem 4. Let r and j be the positive integers such that r≥ 2j + (−1)j+1 and
r≡ 1(mod 2) . Then bj(r) is an integer depending only on the residue of r moduloj + 1.
If r≡ s(mod j + 1) and 0 ≤ s≤ j, let us denote by ~bj(s) the ”stable value” of the
functionbj(r). Thus for a given positive integer j we reduced a problem of computing the
inﬁnite family of numbers N (j,r ), r≥ 2j + 1, to that for ﬁnite collection of quantities
~bj(s), 0≤s≤j, only.
Theorem 5. i) (Duality) If 0 ≤s≤j− 3, then ~bj(s) +~bj(j− 3−s) =
(
j
3
)
−
(
j
2
)
,
ii)~bj(j) =~bj(j− 2) =
(
j
3
)
.
In principle, using the identity (1.16) it is possible to com pute the functions ~bj(s) ex-
actly (and consequently, to ﬁnd the remainder term N (j,r ) in Kuniba-Nakanishi’s dilog-
arithm sum c0(ϕ)). We give here only partial results concerning the computa tion of the
numbers~bj(s).
Theorem 6. i)~bj(0) =−
[ (j− 1
2
)2]
,
ii)~bj(1) =
[ 2j
3
][ 2j + 2
3
]
− j(j− 1)
2 ,
iii)~bj(2) = 2
[ j
4
][ 3j + 3
4
]
−
[ (j− 1
2
)2]
.
On the other hand ( r≡ 1(mod 2) ),
iv) b1(r) = 0,
v) b2(r) = 0, if r≥ 3,
vi) b3(r) = 1, if r≥ 7.
Corollary 2 (of Theorem 4). If r is an odd positive integer, then N (j,r ) is an integer
for any admissible value of j (i.e. g.c.d. (j + 1,r + 2) = 1 ).

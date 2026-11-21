---
doc_id: lin-wang-1999-on-ohtsukis-invariants-of-integral-homology-3
doc_title: "On Ohtsuki's invariants of integral homology 3-spheres"
section_id: sec-002-dkr
section_title: "Dk(r)-- (~=~)!"
section_number: null
pages: 4-7
source_pdf: lin-wang-1999-on-ohtsukis-invariants-of-integral-homology-3-spheres.pdf
source_sha256: 3fb38d4cfd20d4fb
toc_source: inferred
doc_brief: "On Ohtsuki's invariants of integral homology 3-spheres — We provide some more explicit formulae to facilitate the computation of Ohtsuki's rational invariants ,k,~ of integral homology 3-spheres"
---
is a Fermat function whose residue is given by 
1 
1 
1 
{ 
(-~)(-~ 
- 11...(- 
5 - (k- 
11) 
Res(Dk) = 
1 
1 
E Z(3 ) 
for k > 0, 
fork=0, 
for k < 0. 
(2.2) 
Example 2.2 
We denote by aj(Xl,...,x, 0 (1 <: j < n) the j-th elementary symmetric 
polynomial in the indeterminates xl,..., xn, with a0(xl,..., x, 0 = 1. And we will also need 
8j(Xl,''',~n) 
= ~-'~,i=1 aTi" 
Lemma 2.3 
sj (1, 2,..., n- 1) is a polynomial in n with coefficients in Z(j+2), and sj (1, 2,..., 
n- 1) - 0 mod n. 
Proof By the Euler-Maclaurin formula for sj [16], we have 
J 
i=oJ+ 1-i 
where /30 = 1,/~1 -- -1/2, and •=i = (-1)i-XBi, fl2i+1 = 0 for i _> 1 (Bi is the Bernoulli 
number). We also have yon Staudt's theorem which determines the fractional part of Bi [16]. 
It follows that f~i E Z(i+2). This implies the lemma. 
For a pair of non-negative integers l, m, we define 
,'-iv 
( 
2 J" 
(-1) m+l'am 
1,2,... 
= 
_ l + m)! 
r- 1 
l§ m- 
1). 
(2.3) 
' 
2 
Lemma 
2.4 
Hl,m is a Fermat function. Moreover, let g~,m -- Res(Hl,,0. Then g~,m E 
Z 
1 
Remark 
The proof of Lemma 2.4 will also provide us with a recursive formula to calculate 
g~,m" See Formula (2.5). 
Proof We first derive a formula for aj(1,2,...,n - 1), using a trick of Lagrange. We will use 
abbreviation aj = crj(1, 2,..., n- 1). 
On Ohtsuki's lnvariants 
297 
We have 
(x - 1)(x - 2)... (x - (n - 1)) = x n-i - o1 xn-2 ~.-...-I- (--1)n-lo'n-1 

9 
If we multiply both sides by x and change x into x - 1, we obtain 
(x -- 1)n--O'l(X -- 1) n-1 +""-t- (--1)n-l(Tn-l(X -- 1) 
= (X -- 1)(X -- 2)"" (X -- n) 
= (x- n)(x ~-I - aix '~-2 +'-" + (-1)~-ian-i). 
Equating the coefficients, we obtain 
(3) 
(n-l) 
2~r2(1,2 ,...,n- 
1) = 
+ 
2 
al, 
.,n-- 
--~ ('Q.'~ (n-- 1) 0"1-~ (n-- 2) 0"2, 
) 
jo.j(1,2,...,n_ 
l) = E 
n- 
i 
i=o 
j+l-i 
ai, 
r~--2 
(n- 1)~_1(1,2, 
,n- 
1) = ~i. 
i=0 
Therefore, we see inductively that c~j(1, 2,..., n - 1) is a polynomial of n with coefficients 
in g(j+~) and divisible by n(n - 1)-.. (n - j). Using these formulae for crj, we have 
jcrj(1,2,...,n 
- 1) _ 
1 
~ 
n -i 
cri(1,2 ,. .. ,n - 1) 
n(n-1)...(n-j) 
(j + 
1)~ 
+ 
j+l-i 
~(n---1)----(n-----j) 
(2.4) 
1 
j-1 
(n - i) 
1 iai(1, 2,..., n - 1) 
- 
(j + 1)! + ~= (j + 1 - i)! i ~(n - 1)---(~ - i)" 
Suggested by (2.4), we define a series of rational numbers @m E Z(m+2)[89 for i _> 1 
recursively as follows: 
1 
@m_ 
(-j-~ 1)!1 + "- (-89 - / + m - i) 
(J UI-- 122 ~) "v 
@m~ 
for j > 2._ 
r--1 
It is clear that we may identify a~ '~ with the residue of j~(1,2 ....... 1) with n = 
- l + m. 
n(n--1)...(n--j) 
2 
Then we have 
g0,o = -1, 
i 
1 
gl,o=(-1)(- 
)...(-~-l+l), 
ill> 
1, 
(2.5) 
' 
=(--1)m+1 
~ 
(--2 
l,m 
gl,m 
(--) . . . . 
l) Cr'~ , 
ifm>l. 
m 
298 
Xiaosong Lin et al. 
Obviously, Formula (2.5) for g~,0 and g' 
follows from the formula of Res(Dk) in Example 
1,0 
2.1. To see Formula (2.5) for m > 1, we only need to notice that 
(-89 
9 (-89 -l) 
(-} - l + 
(-} -l) 
= Res(D/_m). 
This finishes the proof of Lemma 2.4. 
3 
Fermat Limits and Ohtsuki's Invariants 
We fix some notation about the "quantum 
parameter" first: 

9 We will use r to denote an odd prime, and q = e 27r'/'E-i-/r. The quantum integer [k] = 
k 
k 
q~ -q __~. Note that [2] = q89 + q-89 
q2 --q 
2 

9 For R = Z or Z(r), O((q - 1)k;R) stands for a complex number of the form u(q - 1) k 
for some u E R[q]. 

9 If f(x) is a C a function, we use Coeff~(f; x - a) to denote the coefficient of (x - a) '~ in 
the Taylor expansion of f at x = a. 

9 The Gauss sum is Go(q) 
r-1 
r--1 k2~qk2 
= ~-~-k=0 q k2. The weighted Gauss sum is G2l(q) = ~-~k=0 
To define Ohtsuki's invariants, we need the following definition. 
Let l(r) be an integer valued function ofr with lim~++~ l(r) = +c~ and l(r) <_ r-2. Given 
a sequence of complex numbers sr(q) E Z(r)[q]. Fix a non-negative integer n; for sufficiently 
large r, we write 
s~(q) = a~,o + a~,l(q - 1) +..-+ 
a~,n(q - 1) '~ +"" + a~,z(~)(q - 1) ~(r) + O((q 
- 1)l(r)+l, Z(r)) 
for some a~,n E Z(~). 
Definition 3.1 
The sequence of complex numbers sr(q) has a Fermat limit, denoted by 
f-limsr(q), if each a .... thought of as a function of r, is a Fermat function. Let A,~ = Res(a~,n). 
We write 
f-Sms~(q) = EA~(t 
- 1) '~ e Q[[t - 1]]. 
n~--0 
Lemma 3.1 
The Fermat limit of s~(q) is well-defined and if it exists, it is unique. 
Proof 
Notice that although the expansion st(q) is not unique as q is not a free variable, 
a~,~ E Z/rZ is well defined for 0 <_ n <_ l(r). This is because of r = O((q- 
1)~-1; Z), which 
X "~r-1 i 
follows from the only relation in Z(r)[q]: z-,i=o q = 0. Therefore, each residue A,~ is well-defined 
regardless of the choice of a .... 
The uniqueness of a Fermat limit now comes from the uniqueness of residues of Fermat 
functions (Lemma 2.1). 
Remark 
Notice that An is an integer if and only if the congruence class ~ 
E Z/rZ, which 
is well-defined, stabilizes as a fixed integer for all sufficiently large r. 
On Ohtsuki's Invariants 
299 
With all the above being understood, we summarize the main results of [4] and [1] into the 
following theorem. 
Theorem 3.1 
Let M be an oriented homology 3-sphere, and Tr(M) be the quantum SU(2) 
invariant of Reshetikhin and Turaev [2] at the r-th root of unity normalized as in [17]. Then 
1 
(H. Murakami) Tr(M) e Z[q]; 
2 
(T. Ohtsuki) f-limTr(M) = ~--~,~--0 An(t- 1) n, and/~n E ~(2n+2)~"

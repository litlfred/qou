---
doc_id: 1-s2-0-0097316595900136-main
doc_title: "A q-Rational Murnaghan-Nakayama Rule"
section_id: sec-000-3-the-q-rational-murnaghan-nakayama-rule
section_title: "THE q-RATIONAL MURNAGHAN-NAKAYAMA RULE"
section_number: 3
pages: 8-18
source_pdf: 1-s2.0-0097316595900136-main.pdf
source_sha256: c92d3e85b3dec20a
toc_source: inferred
doc_brief: "A q-Rational Murnaghan-Nakayama Rule — 2 sections: Front matter; THE q-RATIONAL MURNAGHAN-NAKAYAMA"
---
(1) 
(2) 
(3) 
The dots 
hook. In 
hook. 
Here we produce the algorithm for computing Z~r (() and Z~r ((). 
Given an r-staircase 7, the boundary of y + is the ~ei of edges i~i" the 
diagram of ~ + at the right end of its rows and the bottom of its columns. 
The boundary of y- is the set of edges at the left end of its rows and the 
top of its columns. The boundary of ~ is the union of the boundaries of ? + 
and 7 
together with the vertical edge that represents the empty rows. The 
possible locations of boxes in a diagram, whether or not a box is drawn 
there, are called cells. We remove a cell from ~ by either deleting the box 
if the cell contains a box or by adding a box if the cell is empty. 
Let k e 77. If k >~ 0 (respectively, k < 0), then a k-rim hook in ~ in ~ is a 
sequence of [k] cells along the left (respectively, right) side of the boundary 
of 7 such that 
any two consecutive cells in ~ share an edge, 
contains no 2 x 2 blocks of cells, and 
the removal of the cells of ~ results in another r-staircase. 
in Figure 1 illustrate, respectively, a 7-rim hook and a (-5)-rim 
each case, the second staircase is the result of removing the rim 
If k > 0 and y is a partition, then a k-rim hook is the same as a rim hook 
(or skew hook) for partitions (see [Mac]). 
For i= 1, ..., d, let kis77 be a sequence of integers that are either all 
positive or all negative, and let k=Z~=l kl. A sequence 0 = (~1, ..., ~a) of 
rim hooks (starting from the bottom) in ?:, where ~ is a k~-rim hook, is a 
-N 
FIG. 1. Removal of rim hooks. 
A q-RATIONAL MURNAGHAN--NAKAYAMA RULE 
k-broken rim hook if for 1 ~< i,j <~ d the rim hooks ~i and ~j do not share 
a common edge. Let n(~) = d denote the number of rim hooks in ~. The 
next example illustrates the (-8)-broken rim hook ~ where n(~)= 3 and 
kl = -3, k2= -2, and k3 = -3. 
Note that ~ is a k-rim hook if and only if n(~ k) = 1. 
Let r(~) and c(~) denote the number of rows and columns in the k-rim 
hook ~, respectively. The weight of a k-broken rim hook ff = (~1, ..-, ~a) is 
n(4,) 
wt(~/; q) = (q~-- 1) n(~0)-I F[ (--1) r(~i)-I qe(C(~i)--l) 
(3.1) 
i=I 
where e = 1 if k > 0, and e = - 1 if k < 0. By convention, the weight of the 
0-broken rim hook, Z;, is wt(~; q) = 1. Note that when q = 1 the weight of 
is zero unless ~ is a rim hook, i.e., it is unbroken. The weight of the 
(-8)-broken rim hook shown above is (q 1 
1)2 (-1) q-lq-lq-2. 
If 7 and 6 are r-staircases and if 7 is obtained from fi by removing a 
k-broken rim hook ~/, then we write fi/? = ~/and say that 6/y is a k-broken 
rim hook. In the case where ~ = fi, we have ~/7 = ~- Observe that if ~/7 is 
a k-broken rim hook, then 
(c~+j)/(7+j)=fi/7 
for all j~Z. 
(3.2) 
In particular wt((~ +J)/(7 +J); q) = wt(~/~/). 
The proof of the Murnaghan-Nakayama rule requires the following 
important result of Ram [R1] (see also [HR]). 
THEOREM 3.3. 
Let v be a partition with l(v) <, r, and let k e Z +. Then 
fik (xr; q) Sv(Xr ) = ~ wt(2/v; q) s;o (x r ) 
2 
where the sum is over all partitions 2 such that 2/v is a k-broken rim hook. 
Theorem 3.3 extends to r-staircases as follows. 
COROLLARY 3.4. 
Let 7 be an r-staircase, and let k ~ Z, then 
fik(x~; q) sz(xr) = ~ wt(fi/7; q) s~(x~), 
where the sum is over all r-staircases fi such that 0/7 is a k-broken rim hook. 
TOM HALVERSON 
Proof 
When k = 0, the result holds vacuously with ~ = ~, so assume 
first of all that k > 0. Then 
/~k(Xr; q) Sy(X~) = (Xl''' Xr)erfik(X~; q) ST_?)r(Xl,... , Xr) 
by (2.4) 
=(xl...xr)'~wt(2/(7--7~);q)s)o(x~) 
by (3.3) 
2 
=~ wt((2+7~)/~; q)s;~+y~(x~), 
by (3.2) and (2.4), 
2 
where the sum is over partitions 2 with l(2)~< r, such that (2 +7~)/7 is a 
k-broken rim hook. This is equivalent to summing over all r-staircases 
such that ~/7 is a k-broken rim hook, so the result holds whenever k ~> 0. 
Now assume k<0. Then, recalling from (2.4) that 7* is the partition 
obtained by rotating 7- 7~ by 180 degrees, we have 
fik(x~; q) s~(x~) = (Xl... Xr) yl A~ k(xrl; q-l) Sy. (X71 ) 
= (Xl...x~)~Y~ wt(~/7,; q-~) s~(x;-1), 
2 
by (2.4) 
by (3.3) 
where the sum is over partitions 2, with l(2) ~< r, such that 2/7, is a ( -k)- 
broken rim hook. Upon rotating this picture by 180 degrees, we see that 
this is equivalent to summing over all r-staircases fi such that fi/7 is a 
k-broken rim hook. The result follows as above, since wt(2/7,;q-~)= 
wt(~/7; q) and (xl...x~) yl sx(x; -~) =sa(xr). 
| 
Let ~, 7 ~ Am'n with ~+ [-m and ~- ~-n. Inductively define sequences me 
and niby mr--m and nr=n, me l=me-(e and ni_l=neif(e>~O, and 
me 1 = me and n i_ 1 = ni + (e if (e < 0. Then a (-broken rim hook tableau F 
of shape ?~ is a sequence of r-staircases 
F= (~(~ = 7, ~('-1~, ..., 7(1~, 7(o~= Z) 
such that 7(i)EA m''ni and 7(i)/7 (;-~) is a ~i-broken rim hook for each 
1 ~< i ~< t. The weight of F is given by 
wt(F; q) = ~I wt(7(~)/7 (e- 1~; q). 
e=l 
For example, if ~= (5, 3, -3, -4) and 7--(4, -1, -l, -1), then Fig. 2 
illustrates a l-broken rim hook tableau F of shape 7 with wt(F; q)-- 
((- 1) q3). ((q__ 1) q). ((- 1) q 1). (q3). In each staircase, the dots repre- 
sent the broken rim hook that is removed to obtain the previous staircase. 
A q-RATIONAL MURNAGHAN--NAKAYAMA RULE 
7 (0) E A °'° 
FIG. 2. A (5, 3, -3, -4)-broken rim hook tableau of shape (4, -1, -1, -1). 
THEOREM 3.5. 
Let r >~m + n, and let ~ e A m'" with ~.+ ~-m and ~- [-n. 
Then the H~,,(q)-character Z~;,, (~) is given by 
z'.r,,..( 
= Y, wt( r; q), 
F 
where the sum is over all l-broken rim hook tableaux I" of shape 7. 
Proof 
Let k be the maximal index with ~k ¢ 0 (thus, k = r if n ~ 0). Let 
be the r-staircase obtained from ~ by removing (k and adding another 
zero row between (+ and (-. If ~k < 0, let m'= m and n'= n + (k, and if 
~k ~> 0, let m'= m- ~k and n'= n. Then we have 
2 
ZYHrr, n(q)(~) ST(Xr) =fi~(Xr; q) 
?~Ar m,n 
by (2.6) 
=fi~(xr; q)fick(x~; q) 
= 
.~Hr, n,(~) SS(Xr) J~k(Xr; q) 
= 
F, wt(7/5; q) s,(xr), 
SEA'S"" 
by Corollary 3.4 
by (2.6) 
where the last sum is over all r-staircases 7 such that 7/6 is a ~k-broken rim 
hook. Since the s~ are linearly independent (see [Koi]), we can compare 
coefficients of %(xr) on both sides to obtain 
, 
q) ZH~., .,(~), 
(3.6) 
~eAm', ; 
where the sum is over all r-staircases 6 e A m''" such that 7/6 is a ~k-broken 
rim hook. if ~ = ~, then m' = 0 and n' = 0, since we started with ~ + [- m 
and ~- [- n. In this case, we have X~, (~) = 1. If ~¢ ~, then we repeat 
the process on X~; 
(C) with the bott°6~n-most non-empty row of C. Note 
that at any stage, if there does not exist a 6 such that 7/6 is a 6k-broken 
staircase, then the contribution from this summand is zero. 
| 
TOM HALVERSON 
? 
(q-l_ 1) • 
(q-l_ 1) • 
q-lm~ 
l 
i 
1 
(-1) 
• 
(q) 
• 
• 
(1,0, 
FIG. 3. Computing X~32-1)((2, 0, -2)). 
To calculate Y 
XH;,, ,(q)(() we remove all possible G-broken rim hooks from 
7, and from the resulting r-staircases, strip away all possible (r-1-broken 
rim hooks, and so on. At some point it will either be impossible to remove 
a broken rim hook of the right size (in which case, the contribution of the 
summand is zero) or we will have reaced 
z 
XHE0(~)=I. To compute 
X~;,, ((), we let q= 1 in Theorem 3.5, and therefore sum over all (-rim 
hook tableau (unbroken) of shape 7. Figure 3 illustrates the procedure with 
.(1, 0, 
the computation of X/_/32-1)((2, 0,-2)). 
In the example, we stop the 
process whenever the number of boxes in 7 (o is greater than the number of 
boxes in ( yet to be removed from 7- 
Remark 3.7. 
If r >~ m + n and 7 and ( are as in Theorem 3.5, then it is 
not difficult to see that removing a k-rim hook from 7 is done by either 
removing a k-rim hook from 7 + or by removing a k-rim hook from 7-. 
Therefore the values X~;., (() and Z~;., 
(()~ 
are independent of r, whenever 
r>~m+n. 
4. TABLES 
The author has written a Maple program that uses (3.6) to inductively 
r 
r 
compute Hm,,(q)-characte s. The following are the character tables for the 
algebras H r l(q), gr 
1, 
2,1(q), Hr3, o(q), H~,2(q), where we assume r>.m+n. 
Setting q = 1 gives the corresponding N~, n-character table. When denoting 
partitions, we abbreviate repeated parts k, k ..... k with i factors by U. 
A q-RATIONAL MURNAGHAN-NAKAYAMA RULE 
TABLE I 
Character Table for H~, ~(q) 
7\P 
[(1),(1)] r 
[~,.~5]r 
[(1), (1)]~ 
1 
0 
[~, ~]~ 
1 
~r L 
TABLE II 
Character Table for H~, 1 (q) 
y\p 
[(2), (1)] r [(12), (1)] r [(1), ~]~ 
[(2),(1)It 
q 
1 
0 
[(12),(1)]r 
--1 
1 
0 
[(1),.~]~ 
q-1 
2 
~r~q 
TABLE III 
Character Table for H~, l(q) 
7\P 
[(3), (1)]r 
[(2, 1), (1)]r 
[(13), (1)]r 
[(2), .~53r 
[(12), .@]r 
[(3), (1)]r 
q2 
q 
1 
0 
0 
[(2, 1), (1)] r 
--q 
q--1 
2 
0 
0 
[(13), (1)Jr 
1 
--1 
1 
0 
0 
[(2), ~]r 
q2 _ q 
2q-- 1 
3 
Er~q 
-- ~r~q 
[(12), .~]r 
1 --q 
q--2 
3 
Er~q 
qEr~q 
Z 
© 
rT1 
© 
M 
~ 
rm~ 
~ 
~ 
rmml 
~ 
~ 
LmJ Li~ 
L1q~ 
LmJ LIR~ 
v 
j~ 
rul 
I 
I 
I 
L~ 
r~ 
v 
II~ 
i~ 
~ 
~ 
~d~ 
~J~ 
t~ 
~I~ 
~J ~ 
L~ 
Ft 
F~ 
F~ 
~ 
~l 
~ 
d~ 
TABLE VI 
Character Table for H ~. 3 (q) 
y\p 
[(3),(3)]~ 
[(3),(2,1)]~ 
[(3),(13)]~ 
[(2,1),(3)]~ 
[(2,1),(2, 1)]~ 
[(3),(3)]r 
[(3),(2, 1)]r 
[(3),(V)],. 
[(2, 1),(3)It 
[(2, 1),(2, 1)],. 
[(2, 1),(13)]r 
[(13),(3)3r 
[(13),(2, 1)1,. 
[(13),(13)]r 
[(2),(2)],. 
[(2),(12)]r 
[(12),(2)],. 
[(12),(12 ) 
[(I),(I)]~ 
[~,~],, 
1 
q 
q2 
q 
1 
1 
_ q 
q _ qe 
2q2 
-- 1 
1 - q 
q2 
_ q2 
q2 
q 
_ q 
_q-i 
--1 
_q 
q-2+q 
i 
_q 
1+1 
1 
-l+q 
--2q 
q 1--1 
--q t+2-q 
--q 
q 
-q 
-l+q 
1-q 
q-2 
q t 
] 
__q--2 
_q-~ 
q 1 
q.-l_l 
2 
q-1 
q l+l 
1 
--1 
1 
--1 
1 
--q-l+2--q 
--2+3q--q 2 
--3q+3q 2 
--q 2+3q 1--2 
--2q-t+5--2q 
1 --2q+q 2 
3q--2q 2- 1 
--3q+3q 2 
q-1 --3+2q 
4--4q--q 
I 
q-2--2q-l+l 
2q-l--3+q 
3--3q 
_2q-2+3q I 
1 
--4q 1+4--q 
--q 1+2--q 
q-l--3+2q 
3--3q 
2q 1--3+q 
--2q l+5--2q 
--2q I +4--2q 
q-1 
5+5q 
q2 
3_6q + 3q2 
5q-15_q-2+q 
_4q-1 + lO_4q 
3 
--2+2q 
1--2q+q 2 
2q-1--2 
4 
q-l 
q 
Table continued 
> 
<, 
> 
z> 
> 
> 
> 
> 
> 
TABLE VI--Continued 
?\p 
[(2, 1), (13)]~ 
[(13), (3)]r 
[(13), (2, 1)]~ 
[(13), (13)]~ 
[(2), (2)] r 
[(3), (3)]r 
q 
q-2 
q : 
1 
0 
[(3), (2, 1)]r 
2q 
_q-1 
q-~ - 1 
2 
0 
[(3), (13)It 
q 
1 
-1 
1 
0 
[(2, 1 ), (3)It 
- 1 + q 
2q -2 
2q-~ 
2 
0 
[(2,1), (2,1)]r 
-2+2q 
--2q ~ 
2q 1--2 
4 
0 
[(2, 1),(13)]r 
--1 +q 
2 
-2 
2 
0 
[(13), (3)] r 
-- 1 
q-2 
q-1 
1 
0 
[(13), (2,1)]~ 
-2 
-q-~ 
q ~--1 
2 
0 
[(13), (13)It 
-1 
1 
--1 
1 
0 
[(2),(2)]r 
-3+6q 
3q Z--3q ' 
6q -1-3 
9 
~r~q 
[(2), (12)It 
-3 + 6q 
-3q -1 + 3 
-6 + 3q-: 
9 
--q~r~q 
[(12),(2)]~ 
--6+3q 
3q-2 
3q 1 
6q-~_3 
9 
--q l~r~q 
[(12), (12) 
--6 + 3q 
--3q -1 + 3 
--6 + 3q -1 
9 
~r~]q 
[~(1), (1)]~ 
--9+9q 
--6q--: +3 +3q -2 
9q ~--9 
18 
(2--q -1 --q)~r~q 
[~, ~]~ 
-3 + 3q 
_q-2--2q-' 
+ 1 
3q -~ --3 
6 
2~r~q 
Table continued 
© 
=> 
Z 
TABLE Vl--Continued 
7\P 
[(2), (12)],. 
[(12), (2)],. 
[(lZ), (12)It 
[(1), (1)]~ 
[25, 5ZS]r 
>. 
<, 
[(3), (3)]r 
0 
0 
0 
0 
0 
[(3), (2, 1)]~ 
0 
0 
0 
0 
0 
O 
[(3),(1~)L 
o 
o 
o 
o 
o 
[(2, 1), (3)]r 
0 
0 
0 
0 
0 
[(2, 1), (2, 1)] r 
0 
0 
0 
0 
0 
Z 
[(2, 1), (13)]r 
0 
0 
0 
0 
0 
[(l~),(3)L 
o 
o 
o 
o 
o 
Z 
[(13), (2, 1)]~ 
0 
0 
0 
0 
0 
[(13), (13)Jr 
0 
0 
0 
0 
0 
> 
[(2), (2)3,. 
q~r~q 
q ~{r~q 
~r~q 
0 
0 
f~ 
[(2), (lZ)], 
q[r~q 
-- ~r~q 
[r~q 
0 
0 
[(12), (2)]~ 
--~r~q 
q-l~r~q 
~r~q 
0 
0 
[(1), (1)],. 
2(q- 1)~r~q 
2(q-' -- 1)[r~q 
4~r~q 
~r~ 2 
0 
[ 2J, ~25]~ 
(q-- 1)~r~q 
(q-1 _ l)~r~q 
2~r~q 
~r~ 
~r~3q 
----I 
18 
TOM HALVERSON 
ACKNOWLEDGMENTS 
I thank my thesis advisor Georgia Benkart for her generous help throughout this research. 
I thank Arun Ram for teaching me about symmetric functions and for many enlightening 
conversations. 
[BCHLLS] 
[BR] 
[Ha] 
[HR] 
[Ki] 
[Koi] 
[Kos] 
[L] 
[M] 
[R1] 
[R2] 
[ Scl ] 
[Sc2] 
[St] 
REFERENCES 
G. M. BENKART, M. CHAKRABARTI, T. HALVERSON, C. LEE, R. LEDUC, AND 
J. STROOMER, Tensor product representations of general linear groups and their 
connections with Brauer algebras, J. Algebra 166 (1994), 529-567. 
R. BRAUER, On algebras which are connected with semisimple Lie groups, Ann. 
of Math. 38 (1937), 857-872. 
T. HALVERSON, Characters of the centralizer algebras of mixed tensor representa- 
tions of GL(r,C) and the quantum group ~(gl(r, C), Pacific 3". Math., 
to appear. 
T. HALVERSON AND A. RAM, Characters of algebras containing a Jones basic 
construction: The Birman-Wenzl algebra, the Brauer algebra, the Okada 
algebra, and the Temperley-Lieb algebra, Adv. in Math., to appear. 
R. C. KING, Modification rules and products of irreducible representations of the 
unitary, orthogonal, and symplectic groups, J. Math. Phys. 12 (1971), 1588 1598. 
K. KOIKE, On the decomposition of tensor products of the representations of the 
classical groups: By means of universal characters, Adv. in Math. 74 (1989), 
57-86. 
M. KOSUDA, Centralizer algebras of the mixed tensor representations of quantum 
algebra, Uq(gl(m, C), preprint. 
R. LEDUC, A two-parameter version of the centralizer algebra of mixed tensor 
representations of quantum GL(r), preprint. 
I. a. MACDONALD, "Symmetric Functions and Hall Polynomials," Oxford Univ. 
Press, Oxford, 1979. 
A. RAM, A Frobenius formula for the characters of the Hecke algebras, Invent. 
Math. 106 (1991), 461-468. 
A. RAM, Characters of Brauer's centralizer algebras, Pacific. J. Math., to appear. 
I. SCmYR, "Ober eine Klasse yon Matrixen die sich einer gegebenen Matrix 
zuordnen lassen," Thesis, Univ. of Berlin, 1901; reprinted in "Gesammelte 
Abhandlungen I" (I. Schur, Ed.), pp. 1-70, Springer, Berlin, 1973. 
I. SCHUR, "Ober die rationalen Darstellungen der allgemeinen linearen Gruppe," 
1927; reprinted, in "Gesammelte Abhandlungen III" (L Schur, Ed.), pp. 68-85, 
Springer, Berlin, 1973. 
J. R. STEMBRIDGE, Rational tableaux and the tensor algebra of gin, J. Combin. 
Theory Ser. A 46 (1987), 79-120.

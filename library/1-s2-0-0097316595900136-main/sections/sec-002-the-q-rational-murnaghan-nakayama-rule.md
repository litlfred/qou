---
doc_id: 1-s2-0-0097316595900136-main
doc_title: "A q-Rational Murnaghan-Nakayama Rule"
section_id: sec-002-the-q-rational-murnaghan-nakayama-rule
section_title: "THE q-RATIONAL MURNAGHAN-NAKAYAMA RULE"
section_number: 3
pages: 8-11
source_pdf: 1-s2.0-0097316595900136-main.pdf
source_sha256: c92d3e85b3dec20a
doc_brief: "A q-Rational Murnaghan-Nakayama Rule — 5 sections: INTRODUCTION; The Murnaghan-Nakayama rule (see [; THE q-RATIONAL MURNAGHAN-NAKAYAMA"
---
Here we produce the algorithm for computing Z~r (() and Z~r (().
Given an r-staircase 7, the boundary of y + is the ~ei of edges i~i"the
diagram of ~ + at the right end of its rows and the bottom of its columns.
The boundary of y - is the set of edges at the left end of its rows and the
top of its columns. The boundary of ~ is the union of the boundaries of ? +
and 7 together with the vertical edge that represents the empty rows. The
possible locations of boxes in a diagram, whether or not a box is drawn
there, are called cells. We remove a cell from ~ by either deleting the box
if the cell contains a box or by adding a box if the cell is empty.
Let k e 77. If k >~0 (respectively, k < 0), then a k - r i m h o o k in ~ in ~ is a
sequence of [k] cells along the left (respectively, right) side of the boundary
of 7 such that

(1) any two consecutive cells in ~ share an edge,
(2)
(3)

contains no 2 x 2 blocks of cells, and
the removal of the cells of ~ results in another r-staircase.

The dots in Figure 1 illustrate, respectively, a 7-rim hook and a ( - 5 ) - r i m
hook. In each case, the second staircase is the result of removing the rim
hook.
If k > 0 and y is a partition, then a k-rim hook is the same as a rim hook
(or skew hook) for partitions (see [ M a c ] ) .
For i = 1, ..., d, let kis77 be a sequence of integers that are either all
positive or all negative, and let k = Z ~ = l kl. A sequence 0 = (~1, ..., ~a) of
rim hooks (starting from the bottom) in ?:, where ~ is a k~-rim hook, is a

-N

FIG. 1. Removal of rim hooks.


9

A q-RATIONAL MURNAGHAN--NAKAYAMA RULE

k-broken rim hook if for 1 ~< i,j <~d the rim hooks ~i and ~j do not share
a common edge. Let n(~) = d denote the number of rim hooks in ~. The
next example illustrates the ( - 8 ) - b r o k e n rim hook ~ where n ( ~ ) = 3 and
kl = - 3 , k 2 = - 2 , and k3 = - 3 .

Note that ~ is a k-rim hook if and only if n(~ k) = 1.
Let r(~) and c(~) denote the number of rows and columns in the k-rim
hook ~, respectively. The weight of a k-broken rim hook ff = (~1, ..-, ~a) is
n(4,)

wt(~/; q) = (q~-- 1) n(~0)-I F[ (--1) r(~i)-I qe(C(~i)--l)

(3.1)

i=I

where e = 1 if k > 0, and e = - 1 if k < 0. By convention, the weight of the
0-broken rim hook, Z;, is w t ( ~ ; q) = 1. Note that when q = 1 the weight of
is zero unless ~ is a rim hook, i.e., it is unbroken. The weight of the
( - 8 ) - b r o k e n rim hook shown above is (q 1 1)2 ( - 1 ) q - l q - l q - 2 .
If 7 and 6 are r-staircases and if 7 is obtained from fi by removing a
k-broken rim hook ~/, then we write fi/? = ~/and say that 6/y is a k-broken
rim hook. In the case where ~ = fi, we have ~/7 = ~ - Observe that if ~/7 is
a k-broken rim hook, then
for all j ~ Z .

(c~+j)/(7+j)=fi/7

(3.2)

In particular wt((~ +J)/(7 +J); q) = wt(~/~/).
The proof of the Murnaghan-Nakayama rule requires the following
important result of Ram [R1] (see also [ H R ] ) .
THEOREM 3.3.

Let v be a partition with l(v) <, r, and let k e Z +. Then

fik (xr; q) Sv(Xr ) = ~ wt(2/v; q) s;o(x r )
2

where the sum is over all partitions 2 such that 2/v is a k-broken rim hook.

Theorem 3.3 extends to r-staircases as follows.
COROLLARY 3.4.

Let 7 be an r-staircase, and let k ~ Z, then

fik(x~; q) sz(xr) = ~ wt(fi/7; q) s~(x~),
where the sum is over all r-staircases fi such that 0/7 is a k-broken rim hook.


10

TOM HALVERSON

Proof When k = 0, the result holds vacuously with ~ = ~, so assume
first of all that k > 0. Then
/~k(Xr; q) Sy(X~)= (Xl''' Xr)erfik(X~; q) ST_?)r(Xl,... , Xr)

by (2.4)

=(xl...xr)'~wt(2/(7--7~);q)s)o(x~)
2

by (3.3)

= ~ wt((2+7~)/~; q)s;~+y~(x~),
2

by (3.2) and (2.4),

where the sum is over partitions 2 with l(2)~< r, such that (2 +7~)/7 is a
k-broken rim hook. This is equivalent to summing over all r-staircases
such that ~/7 is a k-broken rim hook, so the result holds whenever k ~>0.
Now assume k < 0 . Then, recalling from (2.4) that 7* is the partition
obtained by rotating 7 - 7~ by 180 degrees, we have
fik(x~; q) s~(x~) = (Xl... Xr) yl A~ k(xrl; q - l ) Sy. (X71 )

by (2.4)

= (Xl...x~)~Y~ wt(~/7,; q-~) s~(x;-1),
2

by (3.3)

where the sum is over partitions 2, with l(2) ~<r, such that 2/7, is a ( - k ) broken rim hook. Upon rotating this picture by 180 degrees, we see that
this is equivalent to summing over all r-staircases fi such that fi/7 is a
k-broken rim hook. The result follows as above, since w t ( 2 / 7 , ; q - ~ ) =
wt(~/7; q) and ( x l . . . x ~ ) yl sx(x; -~) =sa(xr). |
Let ~, 7 ~ Am'n with ~+ [ - m and ~- ~-n. Inductively define sequences me
and n i b y m r - - m and nr=n, me l = m e - ( e and ni_l=neif(e>~O, and
me 1 = me and n i_ 1 = ni + (e if (e < 0. Then a (-broken rim hook tableau F
of shape ?~is a sequence of r-staircases
F = (~(~ = 7, ~('-1~, ..., 7(1~, 7(o~= Z )
such that 7(i)EA m''ni and 7(i)/7 (;-~) is a ~i-broken rim hook for each
1 ~<i ~<t. The weight of F is given by

wt(F; q) = ~I wt(7(~)/7 (e- 1~;q).
e=l
For example, if ~ = (5, 3, - 3 , - 4 ) and 7--(4, - 1 , - l , - 1 ) , then Fig. 2
illustrates a l-broken rim hook tableau F of shape 7 with wt(F; q)-( ( - 1) q3). ((q__ 1) q). ( ( - 1) q 1). (q3). In each staircase, the dots represent the broken rim hook that is removed to obtain the previous staircase.


11

A q-RATIONAL MURNAGHAN--NAKAYAMA RULE

7 (0) E A°'°

FIG. 2. A (5, 3, -3, -4)-broken rim hook tableau of shape (4, -1, -1, -1).
THEOREM 3.5. Let r >~m + n, and let ~ e A m'" with ~.+ ~-m and ~- [-n.
Then the H~,,(q)-character Z~;,, (~) is given by

z'.r,,..(

= Y,

F

wt( r; q),

where the sum is over all l-broken rim hook tableaux I" of shape 7.
Proof Let k be the maximal index with ~k ¢ 0 (thus, k = r if n ~ 0). Let
be the r-staircase obtained from ~ by removing (k and adding another
zero row between (+ and ( - . If ~k < 0, let m ' = m and n ' = n + (k, and if
~k ~>0, let m ' = m - ~k and n ' = n. Then we have

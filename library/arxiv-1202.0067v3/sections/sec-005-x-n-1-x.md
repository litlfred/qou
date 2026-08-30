---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN\u2013NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON"
section_id: sec-005-x-n-1-x
section_title: "X (n \u2212 1)! X"
section_number: 1
pages: 19-22
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON — 8 sections: Introduction; Deflation by averaging; Skew characters"
---
(mn )
λ
(DefresSn χλ )(xh)
φ
,χ =
n!
(n − `)!
`=1

h∈Sn−`

where x is the `-cycle (1 2 . . . `). We now apply Proposition 4.5 to see that
n
D
E 1X
X X
1
n
φ(m ) , χλ =
(DefresS` χλ/µ )(x)(DefresSn−` χµ )(h),
n
(n − `)!
µ
`=1

h∈Sn−`

where the sum is over partitions µ ⊆ λ with |λ/µ| = m`. Since x is an `cycle, Proposition 4.3 shows that (DefresS` χλ/µ )(x) is ε` (λ/µ) if there exists
an m-border strip tableau of shape λ/µ and type (`) and is zero otherwise.
Thus
n
E
D
X
1 XX
1
n
=
φ(m ) , χλ
ε` (λ/µ)
(DefresSn−` χµ )(h)
n
(n
−
`)!
µ
`=1

h∈Sn−`

n

=

=

1 XX
ε` (λ/µ) DefresSn−` χµ , 1Sn−`
n
µ
1
n

`=1
n X
X

D

ε` (λ/µ) φ

(mn−` )

µ

,χ

E

`=1 µ

where, in each case, the second sum is over all partitions µ ⊆ λ for which
there exists an m-border strip tableau of shape λ/µ and type (`).

Proposition 5.1 gives an algorithm for testing Foulkes’ Conjecture for a
single character χλ of Smn that is far faster than more direct methods, such
n
m
as those requiring the character values of φ(m ) and φ(n ) to be calculated
on all partitions of mn. Timings suggest that it can be significantly faster
than the algorithm used by symmetrica [9], although some of this gain
comes at the expense of increased use of memory. For example, to calculate
11
all the multiplicities hφ(6 ) , χλ i for λ a partition of 66 takes 34 minutes
using the Haskell [17] implementation of Proposition 5.1 available from the
third author’s website1, compared to 350 minutes for symmetrica using the
function COMPLETE_COMPLETE_PLET, both running on the same machine.
The graphs in Figures 3 and 4 show a number of intriguing features of
the character multiplicities appearing in Foulkes’ Conjecture. In particular,
1See www.ma.rhul.ac.uk/ uvah099/.

~


20

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

16

16

14

14

12

12

10

10

8

8

6

6

4

4

2

2

0

0

D 8
E
Figure 3. The left-hand graph shows log2 φ(7 ) , χλ for all partitions of
56 with at most 8 parts. Partitions are ordered lexicographically, with the
smallest partition (78 ) at the far right. If the multiplicity is zero then the
point is placed below the x axis. Vertical lines separate partitions with
equal largest parts. The right-hand graph shows an enlarged view of the
multiplicities for partitions with first part 19; the range of these partitions
is indicated by the arrow in the left-hand graph.

it seems plausible that if Foulkes’ Conjecture is false, then a counterexample occurs when m is near to n and the relevant partition is either very
large or very small in the lexicographic order on partitions of mn with at
most n parts.
Using symmetrica, Foulkes’ Conjecture has been checked for all m and n
with m + n ≤ 17 in [14]. Using Proposition 5.1 and the software already
mentioned, we have extended this range. The relevant data is available from
the third author’s website.
Corollary 5.2. If m ≤ n and m + n ≤ 19 then
D
E D m
E
n
φ(m ) , χλ ≥ φ(n ) , χλ
for all partitions λ of mn.




CHARACTER DEFLATIONS

21

7

6

5

4

3

2

1

0
7

6

5

4

3

2

1

0

8

7

Figure 4. The top graph shows log2 φ(7 ) , χλ − log2 φ(8 ) , χλ for the
partitions of 56 with at most 7 parts for which the smaller multiplicity
is non-zero. To increase their visibility a small number of points have
been enlarged. Partitions are ordered lexicographically, with the smallest
8
partition (87 ) at the far right. The lower graph shows log2 φ(7 ) , χλ for
7
8
those partitions for which φ(8 ) , χλ = 0; if φ(7 ) , χλ = 0 then the point
is drawn below the axis.


22

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

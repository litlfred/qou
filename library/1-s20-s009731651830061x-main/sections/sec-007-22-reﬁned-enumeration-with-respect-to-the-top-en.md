---
doc_id: 1-s20-s009731651830061x-main
doc_title: "Constant term formulas for refined enumerations of Gog and Magog trapezoids"
section_id: sec-007-22-reﬁned-enumeration-with-respect-to-the-top-en
section_title: "Reﬁned enumeration with respect to the top entry"
section_number: 2.2
pages: 10-11
source_pdf: 1-s2.0-S009731651830061X-main.pdf
source_sha256: 8d591fe7f1673c52
toc_source: outline
doc_brief: "Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids (JCTA 158, 2018, 560–604) — alternating sign matrices, plane partitions, constant-term methods."
---
For a positive integer n, non-negative integers min ≤a ≤max and x = (x1, . . . , xn), 
we deﬁne
GTn,a,min,max(x) =
max −min

b=0
(−1)a+min +b

b
a −min

det
1≤i,j≤n
xi + i −min −1
j −1 + b[j = n]

.
Suppose min ≤b1
≤b2
≤. . . ≤bn
≤max is a sequence of integers, then 
GTn,a,min,max(b1, . . . , bn) is the number of Gelfand–Tsetlin patterns with bottom row 
b1, . . . , bn and top row a. This follows, for instance, from a result in [13, Theorem 3, 
S = ∅, P = Q = 1], as

min≤i≤max,i̸=a
x −i
a −i =
max −min

b=0
(−1)a+min +b

b
a −min
x −min
b

.
Further, we deﬁne
Mn,a,min,max(u, v, x) =

1≤p<q≤n
Strictxq,xp GTn,a,min,max(x),
then it follows from [13, Theorem 3] and the ideas above that the evaluation of 
Mn,a,min,max(u, v, x) at x = (b1, . . . , bn) is the generating function of monotone trian-
gles with bottom row b1, . . . , bn and top row a, provided that min ≤b1 < b2 < . . . <
bn ≤max. The reﬁned version of Corollary 3 is then the following.
Theorem 4. Suppose b = (b1, . . . , bn) is a strictly increasing sequence of integers and 
min ≤a ≤max are integers with min ≤b1 and bn ≤max. Then the generating function 
of monotone triangles with bottom row b1, . . . , bn and top row a is the constant term of 
the rational function one obtains by multiplifying the Laurent polynomial in Corollary 3
with
570
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
Fig. 1. Shape of an (s, t)-tree.
max −min

b=0
(−1)a+min +b

b
a −min

n

i=1
(1 + xi)−min⟨zb⟩
n

i=1
1
1 −x−1
i z ,
where ⟨zb⟩means that we take the coeﬃcient of zb and 
1
1−x−1
i
z =
∞

k=0
zkx−k
i
. Again, 
when considering the special case u = v = 1, it suﬃces to require that b = (b1, . . . , bn)
is weakly increasing.

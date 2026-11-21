---
doc_id: 0309214v3
doc_title: "The colored Jones function is q –holonomic"
section_id: sec-019-61-recursion-relations-for-the-cyclotomic-functi
section_title: "Recursion relations for the cyclotomic function of twist knots"
section_number: 6.1
pages: 20-22
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
toc_source: outline
doc_brief: "The colored Jones function is q –holonomic — A function of several variables is called holonomic if, roughly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many linear"
---
Recursion relations for the cyclotomic function of twist
knots
The twist knots Kp for integer p are shown in Figure 2. Their planar projec-
tions have 2|p| + 2 crossings, 2|p| of which come from the full twists, and 2
come from the negative clasp.
...
full twists
p
Figure 2: The twist knot Kp, for integers p. For p = −1, it is the Figure 8, for p = 0
it is the unknot, for p = 1 it is the left trefoil and for p = 2 it is the Stevedore’s ribbon
knot.
Masbaum, [25], following Habiro and Le gives the following formula for the
cyclotomic function of a twist knot. Let c(p, ·) denote the cyclotomic function
of the twist knot Kp. Rearranging a bit Masbaum’s formula [25, Eqn.(35)], we
obtain that:
c(p, n) = (−1)n+1qn(n+3)/2
∞
X
k=0
(−1)kqk(k+1)p+k(k−1)/2(q2k+1 −1)
(q; q)n
(q; q)n+k+1(q; q)n−k
(2)
The above sum has compact support for each n. Now, in computer talk, we
have:
Mathematica 4.2 for Sun Solaris
Copyright 1988-2000 Wolfram Research, Inc.
-- Motif graphics initialized --
In[1]:=<< qZeil.m
q-Zeilberger Package by Axel Riese -- c⃝RISC Linz -- V 2.35 (04/29/03)
For p = −1 (which corresponds to the Figure 8 knot) the program gives:
In[2]:= qZeil[q^(n(n + 3)/2) (-1)^(n + k + 1) q^(-k(k + 1))(q^(2k + 1)
- 1)qfac[q, q, n]/(qfac[q, q, n + k + 1] qfac[q, q, n - k])
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q–holonomic
1273
q^(k(k - 1)/2), {k, 0, Infinity}, n, 1]
Out[2]= SUM[n] == SUM[-1 + n]
which means that c(−1, n) = c(−1, n −1) in accordance to the discussion after
[25, Thm.5.1] which states c(−1, n) = 1 for all n.
For p = 1 (which corresponds to the left hand trefoil) the program gives:
In[3]:= qZeil[q^(n(n + 3)/2) (-1)^(n + k + 1) q^(k(k + 1))(q^(2k + 1)
- 1)qfac[q, q, n]/(qfac[q, q, n + k + 1] qfac[q, q, n - k])
q^(k(k - 1)/2), {k, 0, Infinity}, n, 1]
1 + n
Out[3]= SUM[n] == -(q
SUM[-1 + n])
which means that c(1, n) = −qn+1c(1, n −1) in accordance to the discussion
after [25, Thm.5.1] which states c(1, n) = (−1)nqn(n+3)/2 for all n.
Similarly, for p = 2 (which corresponds to Stevedore’s ribbon knot) the program
gives:
In[4]:= qZeil[q^(n(n + 3)/2) (-1)^(n + k + 1) q^(2k(k + 1))(q^(2k + 1)
- 1)qfac[q, q, n]/(qfac[q, q, n + k + 1] qfac[q, q, n - k])
q^(k(k - 1)/2), {k, 0, Infinity}, n, 1]
Out[4]:= No solution: Increase order by 1
which proves that c(2, n) satisﬁes no ﬁrst order recursion relation.
It does
satisfy a second order recursion relation, as we ﬁnd by:
In[5]:= qZeil[q^(n(n + 3)/2) (-1)^(n + k + 1) q^(2k(k + 1))(q^(2k + 1)
- 1) qfac[q, q, n]/(qfac[q, q, n + k + 1] qfac[q, q, n - k])
q^(k(k - 1)/2), {k, 0, Infinity}, n, 2]
2 + 2 n
-1 + n
Out[4]= SUM[n] == -(q
(1 - q
) SUM[-2 + n]) -
1 + n
n
2 n
>
q
(1 + q - q
+ q
) SUM[-1 + n]
Thus, the program computes not only a recursion relation, but also the order
of a minimal one. Experimentally, it follows that c(p, n) satisﬁes a recursion
relation of order |p|, for all p. Perhaps one can guess the form of a minimal
order recursion relation for all twist knots.
Actually, more is true. Namely, the formula for c(p, n) shows that it is a q–
holonomic function in both variables (p, n). Thus, we are guaranteed to ﬁnd
Geometry & Topology, Volume 9 (2005)
1274
Stavros Garoufalidis and Thang T Q Lˆe
recursion relations with respect to n and with respect to p. Usually, recursion
relations with respect to p for ﬁxed n are called skein theory for the nth colored
Jones function, because the knot is changing, and the color is ﬁxed.
Thus, q–holonomicity implies skein relations (with respect to the number of
twists) for the nth colored Jones polynomial of twist knots, for every ﬁxed n.
For computations of recursion relations of the cyclotomic function of twist knots,
we refer the reader to [12].

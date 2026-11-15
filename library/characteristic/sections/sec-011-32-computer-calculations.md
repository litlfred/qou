---
doc_id: characteristic
doc_title: "ON THE CHARACTERISTIC AND DEFORMATION VARIETIES OF A KNOT"
section_id: sec-011-32-computer-calculations
section_title: "Computer calculations"
section_number: 3.2
pages: 6-11
source_pdf: characteristic.pdf
source_sha256: 42bd31da2754488f
toc_source: inferred
doc_brief: "ON THE CHARACTERISTIC AND DEFORMATION VARIETIES OF A KNOT — The colored Jones function of a knot is a sequence of Laurent polynomials in one variable, whose nth term is the Jones polynomial of the"
---
and (5) has no closed form. However, it is guaranteed to obey nontrivial recursion relations. Moreover, these
relations can be found by computer. There are various programs that can compute the recursion relations
for multisums. In maple, one may use qEKHAD developed by Zeilberger [PWZ]. In Mathematica, one may use
qZeil.m developed by Paule and Riese [PR1, PR2]. We will give explicit examples in Mathematica, using
Paule and Riese’s qZeil.m package.
We start in computer talk by loading the packages:
Mathematica 5.0 for Sun Solaris
Copyright 1988-2000 Wolfram Research, Inc.
-- Motif graphics initialized --
In[1]:=<< qZeil.m
q-Zeilberger Package by Axel Riese -- c⃝RISC Linz -- V 2.35 (04/29/03)
In[2]:= << qMultiSum.m
qMultiSum Package by Axel Riese -- c⃝RISC Linz -- V 2.45 (04/02/03)
Let us type the colored Jones function J31 from Equation (4):
In[3]:= summandtrefoil = (-1)^k q^(k(k + 3)/2) q^(n
k) qfac[q^(-n - 1), q^(-1),
k] qfac[q^(-n + 1), q, k]
6
k
(k (3 + k))/2 + k n
-1 - n
1
Out[3]= (-1)
q
qPochhammer[q
, -, k]
q
1 - n
>
qPochhammer[q
, q, k]
We now ask for a recursion relation for J31:
In[4]:= qZeil[summandtrefoil, {k, 0, Infinity}, n, 1]
qZeil::natbounds: Assuming appropriate convergence.
-2 + n
2 n
-1 + 3 n
-1 + n
q
(-q + q
)
q
(1 - q
) SUM[-1 + n]
Out[4]= SUM[n] == ------------------- - -----------------------------------
n
n
-1 + q
1 - q
In other words, for J(n) = J31(n) we have:
J(n) = q−2+n −q + q2n
−1 + qn −q−1+3n 1 −q−1+n
1 −qn
J(n −1),
The above relation is a ﬁrst order inhomogeneous recursion relation. We may convert it into a second order
homogeneous recursion relation as follows:
In[5]:= rec31 = MakeHomRec[%, SUM[n]]
-1 + 2 n
2
n
q
(q
- q ) SUM[-2 + n]
Out[5]= ------------------------------- +
3
2 n
q
- q
n
n
4
4 n
3 + n
2 + 2 n
3 + 2 n
>
((q - q ) (q + q ) (q
+ q
- q
+ q
- q
-
1 + 3 n
n
2 n
3
2 n
>
q
) SUM[-1 + n]) / (q
(q - q
) (q
- q
)) +
2 - n
n
q
(-1 + q ) SUM[n]
>
----------------------- == 0
2 n
q - q
Perhaps the reader is displeased to see the above recursion relation written in backwards shifts, i.e.,
SUM[-k+n] where k ≥0. This can be converted into a recursion relation using forward shifts by:
In[6]:= ForwardShifts[% ]
3 + 2 n
2
2 + n
q
(q
- q
) SUM[n]
Out[6]= ----------------------------- +
3
4 + 2 n
q
- q
-2 - n
2 + n
2 + n
>
(q
(q - q
) (q + q
)
4
5 + n
6 + 2 n
7 + 2 n
7 + 3 n
8 + 4 n
>
(q
- q
+ q
- q
- q
+ q
) SUM[1 + n])
7
2 + n
4 + 2 n
3
4 + 2 n
(-1 + q
) SUM[2 + n]
>
/ ((q - q
) (q
- q
)) + ------------------------ == 0
n
4 + 2 n
q
(q - q
)
The next command converts the recursion relation rec31 into an operator, where (due to Mathematica
annoyance), we use the symbol X to denote the shift E:
In[7]:= ToqHyper[rec31[[1]] - rec31[[2]]] /. {SUM[N] -> 1, SUM[N q^c_.] :> X^c} /.
N -> Q
2
2
2
q
(-1 + Q)
(q
- Q) Q
Out[7]= ----------- + -------------- +
2
3
2
2
Q (q - Q )
q (q
- Q ) X
4
3
2
2
3
2
3
4
(q - Q) (q + Q) (q
- q
Q + q
Q
- q
Q
- q Q
+ Q )
>
-------------------------------------------------------
2
3
2
Q (q - Q ) (q
- Q ) X
This operator right divides the Aq polynomial of the 31 knot. Let us assume for now that it equals to the
Aq polynomial, after clearing denominators. Setting q = 1, and replacing X by L and Q by M 2, and obtain:
In[8]:= Factor[ToqHyper[rec31[[1]] - rec31[[2]]] /. {SUM[N] -> 1,
SUM[N q^c_.] :> X^c} /. {N -> Q, q -> 1}] /. {Q -> M^2, X -> L}
6
(-1 + L) (L + M )
Out[8]= -(-----------------)
2
2
2
L
M
(1 + M )
The result agrees, up to multiplication by a rational function of M and a power of E, with the A-polynomial
of 31 from (6).
It remains to prove that rec31:=Out[7] coincides with Aq(31), after clearing denominators. Notice that
rec31 = PAq(31) for some operator P and ordE(rec31) = 2, where ordE(P) denotes the E-order of an
operator E. Thus ordE(Aq(31)) is 1 or 2. If ordE(Aq(31)) = 1, then J31 would have a closed form. This
problem can be decided by computer using qHyper (see [PWZ]), which indeed conﬁrms that J31 does not
have closed form. Thus ordE(Aq(31)) = 2 = ordE(rec31). It follows that (up to left multiplication by units),
Aq(31) equals to rec31. This completes the proof in the case of the trefoil.
Now, let us repeat the process for the colored Jones function of the ﬁgure 8 knot, given in Equation (5).
In[9]:= summandfigure8 = q^(n
k) qfac[q^(-n - 1), q^(-1), k] qfac[q^(-n + 1), q, k]
k n
-1 - n
1
1 - n
Out[9]= q
qPochhammer[q
, -, k] qPochhammer[q
, q, k]
q
In[10]:= qZeil[summandfigure8, {k, 0, Infinity}, n, 2]
qZeil::natbounds: Assuming appropriate convergence.
-1 - n
n
2 n
q
(q + q ) (-q + q
)
Out[10]= SUM[n] == ---------------------------- -
n
8
-1 + q
-2 + n
-1 + 2 n
(1 - q
) (1 - q
) SUM[-2 + n]
>
----------------------------------------- +
n
-3 + 2 n
(1 - q ) (1 - q
)
-2 - 2 n
-1 + n 2
-1 + n
>
(q
(1 - q
)
(1 + q
)
4
4 n
3 + n
1 + 2 n
3 + 2 n
1 + 3 n
>
(q
+ q
- q
- q
- q
- q
) SUM[-1 + n]) /
n
-3 + 2 n
>
((1 - q ) (1 - q
))
gives a second-order inhomogeneous recursion relation, which we convert into a third-order homogeneous
recursion relation:
In[11]:= rec41 = MakeHomRec[%, SUM[n]]
2 + n
3
n
q
(-q
+ q ) SUM[-3 + n]
Out[11]= ----------------------------- -
2
n
5
2 n
(q
+ q ) (-q
+ q
)
-2 - n
2
n
8
4 n
6 + n
7 + n
3 + 2 n
>
(q
(q
- q ) (q
+ q
- 2 q
+ q
- q
+
4 + 2 n
5 + 2 n
1 + 3 n
2 + 3 n
>
q
- q
+ q
- 2 q
) SUM[-2 + n]) /
n
5
2 n
>
((q + q ) (q
- q
)) +
-1 - n
n
4
4 n
2 + n
3 + n
1 + 2 n
>
(q
(-q + q ) (q
+ q
+ q
- 2 q
- q
+
2 + 2 n
3 + 2 n
1 + 3 n
2 + 3 n
>
q
- q
- 2 q
+ q
) SUM[-1 + n]) /
1 + n
n
2
n
2 n
q
(-1 + q ) SUM[n]
>
((q
+ q ) (-q + q
)) + ----------------------- == 0
n
2 n
(q + q ) (q - q
)
In forward shifts, we have:
In[12]:= ForwardShifts[%]
5 + n
3
3 + n
q
(-q
+ q
) SUM[n]
Out[12]= ------------------------------ -
2
3 + n
5
6 + 2 n
(q
+ q
) (-q
+ q
)
-5 - n
2
3 + n
8
9 + n
10 + n
9 + 2 n
>
(q
(q
- q
) (q
- 2 q
+ q
- q
+
9
10 + 2 n
11 + 2 n
10 + 3 n
11 + 3 n
12 + 4 n
>
q
- q
+ q
- 2 q
+ q
)
3 + n
5
6 + 2 n
>
SUM[1 + n]) / ((q + q
) (q
- q
)) +
-4 - n
3 + n
4
5 + n
6 + n
7 + 2 n
8 + 2 n
>
(q
(-q + q
) (q
+ q
- 2 q
- q
+ q
-
9 + 2 n
10 + 3 n
11 + 3 n
12 + 4 n
>
q
- 2 q
+ q
+ q
) SUM[2 + n]) /
4 + n
3 + n
2
3 + n
6 + 2 n
q
(-1 + q
) SUM[3 + n]
>
((q
+ q
) (-q + q
)) + ------------------------------- == 0
3 + n
6 + 2 n
(q + q
) (q - q
)
In operator form, rec41 becomes:
In[13]:= ToqHyper[rec41[[1]] - rec41[[2]]] /. {SUM[N] -> 1, SUM[N q^c_.] :> X^c} /.
N -> Q
2
3
q (-1 + Q) Q
q
Q (-q
+ Q)
Out[13]= ---------------- + ---------------------- -
2
2
5
2
3
(q + Q) (q - Q )
(q
+ Q) (-q
+ Q ) X
2
8
6
7
3
2
4
2
5
2
3
2
3
>
((q
- Q) (q
- 2 q
Q + q
Q - q
Q
+ q
Q
- q
Q
+ q Q
- 2 q
Q
+
4
2
5
2
2
>
Q )) / (q
Q (q + Q) (q
- Q ) X ) +
4
2
3
2
2
2
3
2
3
2
3
>
((-q + Q) (q
+ q
Q - 2 q
Q - q Q
+ q
Q
- q
Q
- 2 q Q
+ q
Q
+
4
2
2
>
Q )) / (q Q (q
+ Q) (-q + Q ) X)
where X = E. Let us assume that this coincides with Aq(41), after we clear denominators. Setting q = 1,
and replacing X by L and Q by M 2, and obtain:
In[14]:= Factor[ToqHyper[rec41[[1]] - rec41[[2]]] /. {SUM[N] -> 1,
SUM[N q^c_.] :> X^c} /. {N -> Q , q -> 1}] /. {Q -> M^2, X -> L}
2
4
4
2
4
6
8
(-1 + L) (L - L M
- M
- 2 L M
- L
M
- L M
+ L M )
Out[14]= -------------------------------------------------------
3
2
2 2
L
M
(1 + M )
The result agrees, up to multiplication by a rational function of M and a power of E, with the A-polynomial
of 41 from (7).
It remains to prove that rec41:=Out[13] equals, up to units, to Aq(41). Notice that rec41 = PAq(41) for
some operator P and ordE(rec41) = 3. Thus ordE(Aq(41)) is 1 or 2 or 3.
If ordE(Aq(41)) = 1, then J41 would have a closed form. This problem can be decided by computer using
qHyper (see [PWZ]), which indeed conﬁrms that J31 does not have closed form.
10
If ordE(Aq(41)) = 2, recall the map ϵ which evaluates at q = 1. We have: ϵrec41 = ϵP ϵAq(41). Since
ordE(ϵrec41) = 3, it follows that we must have ordE(ϵAq(41)) = 2.
Furthermore, the computer calculation above shows that ϵAq(41) divides A(41). The latter, given by
Equation (7) can be factored as a product of two irreducible polynomials of E-degree 1 and 2.
On the other hand, Lemma 3.1 below implies that E −1 divides (ϵAq(41))|Q=1. Combining these facts, it
follows that ϵAq(41) = A(41) (and therefore, also Aq(41)) is of E-degree 3, a contradiction to our hypothesis.
Thus, it follows that ordE(Aq(41)) = 3 = ordE(rec41). This implies that, up to left multiplication by
units, Aq(41) coincides with rec41. This concludes the proof in the case of the ﬁgure 8 knot.
Lemma 3.1. For every knot K, ϵAq(K)(1, 1) = 0.
Proof. Recall that the colored Jones function of a knot K is given by a multisum formula of a q-proper
hypergeometric function. Consider the evaluation of the colored Jones function ϵJK at q = 1. This is a
discrete function which is given by a multisum of a proper hypergeometric function.
Applying the WZ
algorithm, it follows that ϵQϵAq(K) annihilates ϵJK, where ϵQ is the evaluation at Q = 1.
However,
ϵJK(n) = 1 for all n; see [GL]. Thus E −1 divides ϵQϵAq(K). The result follows.
□

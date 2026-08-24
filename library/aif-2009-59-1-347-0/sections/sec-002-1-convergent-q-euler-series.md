---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-002-1-convergent-q-euler-series
section_title: "Convergent q-Euler series"
section_number: 1
pages: 8-9
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
doc_brief: "On q-summation and confluence — 18 sections: Introduction; Part 1. Convergent q-Borel and q-L; Convergent q-Euler series"
---
The series
Eq(x) =
∑
n/greaterorequalslant0
(−1)n[n]!
qxn+1,
where [0]q = 1 , [n]q = qn−1
q−1 and [n]!
q = [n]q[n − 1]q · · ·[1]q, represents a
germ of analytic function at 0. If one considers the q-derivation:
dqy = y(qx) −y(x)
(q − 1)x
and observes that dqxn = [n]qxn−1 for any n ∈ Z, n /greaterorequalslant1, then one easily
sees that Eq(x) veriﬁes the functional equation :
x2dqy +y =x,
that can be rewritten in the form:
y(x) = x
x + 1 −qy(qx) − (q − 1)x
x + 1 −q.
By substitution of x byqnx, we deduce that
y(qnx) = qnx
qnx + 1 −qy(qn+1x) − (q − 1)qnx
qnx + 1 −q,
which implies that Eq(x) can be continued to an analytic function on C /integerdivide
{(q − 1)qn : n ∈ Z, n⩽ 0}. The discrete spiral of poles {(q − 1)qn : n ∈
Z, n⩽ 0} of Eq turns out to be a spiral of simple poles, as the following
lemma shows:
Lemma 1.1. — The analytic function Eq admits the following expansion
(1.1) Eq(x) = (1 −q)
∑
n/greaterorequalslant0
(qn+1;q)∞
1 + 1−q
qnx
,
where (a;q)∞ =∏∞
i=0(1 −qia).
TOME 59 (2009), F ASCICULE 1
354 Lucia DI VIZIO & Changgui ZHANG
In particular for any k ∈ Z, k ⩽ 0, the function Eq(x) has a simple pole
at (q − 1)qk. The residue of the diﬀerential form Eq(x)dx at (q − 1)qk is
equal to
Resx=(q−1)qk Eq(x)dx = −(1 −q)2qk(q1−k;q)∞.
We recall some standard notations for basic hypergeometric functions



2φ1 (a,b ;c;q,x ) =
∑
n/greaterorequalslant0
(a;q)n(b;q)n
(c;q)n(q;q)n
xn,
where (a;q)0 = 1 and (a;q)n =∏n
k=1(1 −aqk−1)) for 1 ⩽n ⩽ ∞,
and the Heine’s basic transformation ( cf. [8, §1.4]):
(1.2)
2φ1 (a,b ;c;q,x ) = (a;q)∞(bx;q)∞
(c;q; )∞(x;q)∞
2φ1 (c/a,x ;bx;q,a ) ( |q|< 1, |a|< 1).
Proof. — The lemma above is a straightforward application of ( 1.2), in
fact:
(1.3) Eq(x) = x 2φ1
(
q,q ; 0;q, − x
1 −q
)
.
The calculation of the residues of Eq(x) follows at once. □

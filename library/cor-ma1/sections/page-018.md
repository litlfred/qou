---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-018
section_title: "Page 18"
section_number: null
pages: 18-18
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDENTITIES
17
Now we have all the ingredients to prove Proposition 5.1. We remark that Bk,k+1(N) = Bk,k(N) and we
set Γk,i(N) = Gk,i(N) + aBk,i+1(N −1) if i > 0 and 0 otherwise. Then
Bk,i(N)
=
qN(Bk,i+1(N) + Γk,i−1(N)), if i < k;
Bk,k(N)
=
Γk,k−1(N)/(1 −qN);
Γk,i(N)
=
(a + qN−1)Bk,i+1(N −1) + qNΓk,i−1(N), if i > 0;
Bk,i(0)
=
1;
Γk,0(N)
=
0.
These are the recurrences proven in Proposition 3.1. Therefore Bk,i(N) = Ek,i(N) and Proposition 5.1 is
proved.
6. Paths and successive Durfee squares
We prove in this section that
(6.1)
Ek,i(a, q) =
X
n1≥...≥nk−1≥0
q(
n1+1
2 )+n2
2+···+n2
k−1+ni+···+nk−1(−1/a)n1an1
(q)n1−n2 · · · (q)nk−2−nk−1(q)nk−1
.
This gives the case Ek,i(n, j) = Dk,i(n, j) of Theorem 1.4 as the right hand side of Equation (6.1) is the
generating function for the overpartitions counted by Dk,i(n, j) (see Equation (2.1)). We give an analytical
and a combinatorial proof.
6.1. An analytical proof. We use the Bailey lattice structure from [1] to transform (6.1) into (1.1). Recall
that a pair of sequences (αn, βn) form a Bailey pair with respect to a if for all n ≥0 we have
βn =
n
X
r=0
αr
(q)n−r(aq)n+r
.
We need the following lemma which is a special case of (3.8) in [1].:
Lemma 6.1. If (αn, βn) is a Bailey pair with respect to q, then for all 0 ≤i ≤k we have
1
(q, −aq)∞
×
X
n1≥···≥nk≥0
q(
n1+1
2 )+n2
2+···n2
k+ni+1+···nk(−1/a)n1an1
(q)n1−n2 · · · (q)nk−1−nk
βnk
=
α0
(q)2∞
+
1
(q)2∞
X
n≥1
(−1/a)nanq(n2−n)(i−1/2)+in(1 −q)
(−aq)n
×
 
q(n2+n)(k−i)
(1 −q2n+1) αn −q((n−1)2+(n−1))(k−i)+2n−1
(1 −q2n−1)
αn−1
!
(6.2)
Proof. We set a = q, ρ1 = −1/a, and then let n as well as all remaining ρi and σi tend to ∞in (3.8) of [1]
to obtain (6.2).
□
Proof of (6.1). We use the Bailey pair with respect to q [37, p.468, (B3)],
βn =
1
(q)∞
and
αn = (−1)nqn(3n+1)/2(1 −q2n+1)
(1 −q)
.

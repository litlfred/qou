---
doc_id: s0894-0347-00-00337-4
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4"
section_id: sec-018-a4-convergence-of-trace-class-operators
section_title: "A.4. Convergence of trace class operators"
section_number: null
pages: 32-33
source_pdf: S0894-0347-00-00337-4.pdf
source_sha256: 1c6848281fc2804c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4 — 22 sections: Front matter; Plancherel measures; Introduction"
---
ian nonnegative operators in L1(H). The following proposition is a special case of
Theorem 2.20 in the book [34] (we are grateful to P. Deift for this reference). For
the reader’s convenience we give a proof here.
Proposition A.9. The following conditions are equivalent:
(i) ∥Kn −K∥1 →0;
(ii) tr Kn →tr K and Kn →K in the weak operator topology.
First, we prove a lemma:
Lemma A.10. Let X =
 A
B
B∗
D

be a nonnegative operator 2 × 2 matrix. Then
∥B∥1 ≤
√
tr A · tr D.
Proof of Lemma A.10. Without loss of generality one can assume that the block B
is a nonnegative diagonal matrix, B = diag(b1, b2, . . . ). Write the blocks A and D
as matrices, too, and let ai and di be their diagonal entries. Since X ≥0, we have
b2
i ≤aidi and therefore
∥B∥1 =
X
bi ≤
X p
aidi ≤
qX
ai ·
X
di ≤
√
tr A · tr D.
Proof of Proposition A.9. Clearly, (i) implies (ii).
To check the converse claim,
write K in block form,
K =

A
B
B∗
D

,
where A is of ﬁnite size and tr D is small. Write all the Kn’s in block form with
respect to the same decomposition of the Hilbert space,
Kn =

An
Bn
B∗
n
Dn

.
Since Kn →K weakly, we have convergence of ﬁnite blocks, An →A, which implies
tr An →tr A. Since tr Kn →tr K, we get tr Dn →tr D, so that all the traces tr Dn
are small together with tr D provided that n is large enough.
ASYMPTOTICS OF PLANCHEREL MEASURES
513
Write
K′ =
A
0
0
0

and similarly for Kn. Then
∥Kn −K∥1 ≤∥Kn −K′
n∥1 + ∥K′
n −K′∥1 + ∥K′ −K∥1.
In the right-hand side, the ﬁrst and the third summands are small because of the
lemma, while the second summand is small because it is equal to ∥An −A∥1.
Proposition A.11. The map (A1, . . . , An) 7→det(I + λ1A1 + · · · + λnAn) deﬁnes
a continuous map from (L1(H))n to the algebra of entire functions in n variables
with the topology of uniform convergence on compact sets.
Proof. The fact that det(I + λ1A1 + · · · + λnAn) is holomorphic in {λi} for any
trace class operators A1, . . . , An is proved in [33]. The continuity of the map follows
from the inequality
| det(I + B) −det(I + C)| ≤∥B −C∥1 exp(∥B∥1 + ∥C∥1 + 1)
which holds for any B, C ∈L1(H); see [30, 34].

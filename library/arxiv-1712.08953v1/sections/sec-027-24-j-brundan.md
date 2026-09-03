---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-027-24-j-brundan
section_title: "J. BRUNDAN"
section_number: 24
pages: 24-25
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
doc_brief: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY — The oriented skein category OS(z, t ) is a ribbon category which un- derpins the deﬁnition of the HOMFLY-PT invariant of an orien ted link, in the"
---
We can use (4.9) to obtain a recursive formula: ﬁrst X(↑) := 1↑, X(↓) := t−21↓; then
for any b∈⟨↑,↓⟩ we have that
X(↑↑b) := X(↑b)
b
b
, X (↑↓b) := X(↑b)
b
b
, (4.11)
X(↓↓b) := X(↓b)
b
b
, X (↓↑b) := X(↓b)
b
b
. (4.12)
The following lemma will not be needed in this article. It suggests End AOS (z,t)(∅ )
consists of two copies of the ring of symmetric functions. Deﬁne th e positive and
negative bubbles with n dots by
+ n• :=



n• if n> 0,
tz−11∅ if n = 0,
0 if n< 0;
− n• :=



0 if n> 0,
−t−1z−11∅ if n = 0,
n• if n< 0;
(4.13)
+n• :=



n• if n> 0,
−t−1z−11∅ if n = 0,
0 if n< 0;
−n• :=



0 if n> 0,
tz−11∅ if n = 0,
n• if n< 0.
(4.14)
Note that n• = + n• + − n• and n• = +n• + −n• due to the relation (D).
Lemma 4.4. For any n∈ Z, we have that
∑
r,s≥0
r+s=n
+ r• +s• =
∑
r,s≤0
r+s=n
− r• −s• =−δn,0z−2.
Proof. Consider the relation involving positive bubbles. It is immediate in case n≤ 0.
If n >0, we need the following relation which may be proved by induction using the
relations (A) and (S):
•n =
•n
+z
∑
r,s>0
r+s=n
•s•r . (4.15)
Then we calculate:
− + n• + =t−1z−1 n• =z−1
n• =z−1
n•
+
∑
r,s>0
r+s=n
r• s•
=tz−1 n• +
∑
r,s>0
r+s=n
r• s• =
∑
r≥0,s>0
r+s=n
+ r• +s• .
The relation involving for negative bubbles may now be deduced by app lying the auto-
morphism ρ :AOS (z,t )→AOS (z,t ) which is deﬁned on generators in the same way
as (2.8) plus it maps • ↦→•−1 . □
The category AOS (z,t ) is studied further in [B]: it is the k = 0 case of the q-
Heisenberg categoryHk(z,t ) introduced there.
ORIENTED SKEIN CATEGORY 25

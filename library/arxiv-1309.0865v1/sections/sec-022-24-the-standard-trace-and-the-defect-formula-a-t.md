---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-022-24-the-standard-trace-and-the-defect-formula-a-t
section_title: "The standard trace and the defect formula. A trace on H is a Z[v±1]-linear map"
section_number: 2.4
pages: 16-18
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
ε : H → Z[v±1] satisfyingε(hh′) = ε(h′h) for allh,h ′ ∈ H. A straightforward calcula-
tion shows that the map ε(∑ cwHw) = ce is a trace, called the standard trace. There is
a nice combinatorial formula for the standard trace of a prod uctH w, known as the
defect formula, which we now discuss.
A subsequence ofw = s1s2...s m is a sequence π1π2...π m such that πi ∈ {e,s i} for
all 1 ≤i ≤m. Instead of working with subsequences, we work with the equi valent
datum of a sequence e = e1e2... em of 1’s and 0’s giving the indicator function of a
subsequence, which we refer to as a 01-sequence.
We can also think of e as a roadmap for a gentle stroll through the Bruhat graph
(with much pausing to admire the scenery). This Bruhat stroll is the sequence x0 =
e,x 1,...,x m deﬁned by
xi
def= se1
1 se2
2 ...s ei
i
for 0 ≤ i ≤ m. We call xm the end-point of the Bruhat stroll, and denote it by we.
Alternatively , we will say that a subsequence e ofw expresses the end-point we. The
Bruhat stroll allows us to decorate each index of e with an additional token, either
U(p) or D(own). If ei = 1 so that xi = xi−1si, then we assign U to i ifxi > xi−1 (so
that we moved up in the Bruhat order at time i) or D if xi < xi−1 (so that we moved
down at time i). If ei = 0 so that xi = xi−1, we glance longingly in the direction of
xi−1si but remain unmoved: we assign U or D to the index i according to whether
xi−1si > xi−1 orxi−1si < xi−1. The defect of a 01-sequence e, denoted d(e), is deﬁned
to be the number of U0’s minus the number of D0’s. It measures t he defect between
where we longed to go and where we actually went.
Example 2.9. Here are some examples of subexpressions, end-points and de fects:
SOERGEL CALCULUS 17
• Suppose thatw =sss. There are four subsequences with end-pointe: (U1,D 1,U 0)
and (U0,U 1,D 1) with defect 1, (U1,D 0,D 1) with defect −1, and (U0,U 0,U 0)
with defect 3. There are four subsequences with end-point s: (U1,D 1,U 1)
and (U0,U 1,D 0) with defect 1, (U1,D 0,D 0) with defect −2, and (U0,U 0,U 1)
with defect 2.
• Suppose thatw =sts and thatmst = 3. There are unique subexpressions with
endpoints sts,ts,st and t with defects 0, 1, 1 and 2 respectively . There are
two subexpressions (U1,U 0,D 0) and (U0,U 0,U 1) with end-points of defects
0 and 2 respectively , and two subexpressions (U1,U 0,D 1) and (U0,U 0,U 0)
with end-pointe with defects 1 and 3 respectively .
The defect is useful because of the following lemma of Deodha r [Deo90]:
Lemma 2.10. For any expression w we have
H w =
∑
vd(e)Hwe
where the sum runs over all 01-sequences of length ℓ(w).
Proof. (Sketch) It is an straightforward consequence of (2.5) that in H we have the
relation
HxH s =
{
Hxs +vHx ifxs>x ,
Hxs +v−1Hx ifxs<x .
We conclude that if the lemma is true for w =x it is also true for w =xs. The result
now follows by induction. □
We now come to the defect formula for the trace:
Corollary 2.11. For any expression w we have
ε(H w) =
∑
vd(e)
where the sum is over all 01-sequences expressing the identi ty element.
Example 2.12. We continue Example 2.9 and check Lemma 2.10:
• Using relation (2.7) we see that
H 3
s = (v +v−1)2H s = (v−2 + 2 +v2)Hs + (v−1 + 2v +v3)He.
• Using direct calculation, or smoothness and (2.8), or Lemma 2.10 we obtain
H sH tH s =Hsts +vHts +vHst +v2Ht + (1 +v2)Hs + (v +v3)He.
It will be important later that the set of subsequences e of a ﬁxed expression w
is equipped with a partial order, the path dominance order . Let e and f be two 01-
sequences and let their corresponding Bruhat strolls bex0,x 1,...,x m andy0,y 1,...,y m.
We say that e ≥ f ifxi ≥ yi for all 0 ≤ i ≤ m. Clearly if e ≥ f then the end-point of
e is greater than the end-point of f. The path dominance order restricts to a partial
order on the set of subsequences with ﬁxed end-point.

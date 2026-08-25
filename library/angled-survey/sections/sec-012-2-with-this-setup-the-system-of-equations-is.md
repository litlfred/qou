---
doc_id: angled-survey
doc_title: "From angled triangulations to hyperbolic structures"
section_id: sec-012-2-with-this-setup-the-system-of-equations-is
section_title: "With this setup, the system of equations is"
section_number: 2
pages: 8-10
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
doc_brief: "From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on a 3–manifoldM with"
---
Av =[ π,...,π,2π,...,2π ]T,
where v ∈ R3n is the vector of angles. Then dimA(τ)=3 n−rank(A).
Lemma 3.3. rank(A)=2 n−|∂M|.
This result is due to Neumann [21]. Our proof is adapted from Choi [2,T h e o -
rem 3.7].
Proof. Since the matrixA has 2nrows, it suﬃces to show that the row null
space has dimension|∂M|. We will do this by constructing an explicit basis for the
row null space, with basis vectors in 1−1 correspondence with the cusps ofM.
Let c be a cusp ofM. Associated to c, we construct a row vectorrc ∈ R2n.
For 1≤ i ≤ n,t h eith entry of rc is minus the number of ideal vertices that the
ith tetrahedron has at cuspc.F o rn+1 ≤ i ≤ 2n,t h eith entry ofrc is plus the
number of endpoints that theith edge has at cuspc.T h u src records incidence,
with tetrahedra counted negatively and edges counted positively.
Claim: For every cuspc, rc A =0 .
166
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES 9
Let vj be a column ofA, and recall thatvj corresponds to one pair of opposite
edges in one tetrahedron. Then the dot productrc ·vj counts minus the number
of times that one of these edges has an endpoint atc, plus the number of times
that one of these edges is identiﬁed to an edge ofM that has an endpoint atc.
Naturally the sum is 0.
Claim: The collection of vectorsrc is linearly independent.
Suppose that ∑λcrc = 0, and letei be the ith edge in M.T h eith entry of
rc will be 0, except when c is one of the endpoints ofei. Thus, if the edge ei
has endpoints at cuspsa and b,a n dt h eith entry of ∑λcrc is 0, we must have
λa +λb =0 .
Now, let Δ be an ideal triangle ofτ, whose ideal vertices are at cuspsa, b,a n d
c. The argument above, applied to the three edges of Δ, gives
λa +λb =0 ,λ a +λc =0 ,λ b +λc =0 .
The only way that these three equalities can hold simultaneously is ifλa = λb =
λc = 0. Thus all coeﬃcientsλc must vanish.
Claim: The collection of vectorsrc spans the row null space ofA.
Let q =[ q1,...,q 2n] be a vector such thatqA = 0. Our goal is to show that
q = ∑λkrk. To that end, letTi,( 1≤ i ≤ n), be one tetrahedron ofτ.L e ta,b,c,d
be the cusps ofM corresponding to the four ideal vertices ofTi.( S o m eo ft h e s e
cusps may coincide.) A pair of letters from the collection{a,b,c,d } determines
an edge ofTi, which is identiﬁed to some edge ofM. For notational convenience,
suppose that edgeab from tetrahedronTi is identiﬁed to the edgei(ab)i nM,a n d
similarly for the other letters.
Now, letvj be the jth column vector ofA. This column ofA corresponds to
a pair of opposite edges in one tetrahedron, which will be tetrahedronTi if and
only if 3i−2 ≤ j ≤ 3i. After relabeling{a,b,c,d }, we may assume thatj =3 i−2
corresponds to opposite edgesi(ab)a n di(cd), j =3 i−1 corresponds toi(ac)a n d
i(bd), and j =3 i corresponds toi(ad)a n di(bc). By the deﬁnition of the matrix
A, the only non-zero entries ofv3i−2 are in rowi (corresponding to the tetrahedron
Ti)a n dr o w si(ab),i (cd) (corresponding to edges ofM). The analogous statement
holds forj =3 i−1a n dj =3 i.
Since qA =0 ,w em u s th a v eq·vj =0f o re v e r yj. Applying this to 3i−2 ≤
j ≤ 3i gives
q·v3i−2 = qi +qi(ab) +qi(cd) =0 ,
q·v3i−1 = qi +qi(ac) +qi(bd) =0 ,
q·v3i = qi +qi(ad) +qi(bc) =0 ,
which implies
(3.2) qi(ab) +qi(cd) = qi(ac) +qi(bd) = qi(ad) +qi(bc) = −qi.
We are now ready to ﬁnd coeﬃcientsλk such thatq = ∑λkrk.L e tΔb ea n
ideal triangle inTi, whose ideal vertices are at cuspsa,b,c and whose sides are at
edges i(ab),i (ac),i (bc). Deﬁne
(3.3)
λa = qi(ab)+qi(ac)−qi(bc)
2 ,λ b = qi(ab)+qi(bc)−qi(ac)
2 ,λ c = qi(ac)+qi(bc)−qi(ab)
2 .
A priori, this deﬁnition depends on the ideal triangle Δ. To check this is well-
deﬁned, let Δ′be another ideal triangle ofTi, for example the triangle with ideal
167
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms

---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3–manifolds"
section_id: sec-005-covers-and-branched-covers
section_title: "Covers and branched covers"
section_number: null
pages: 6-7
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
It is straightforward to see that hyperbolic volume is multiplicative under finite-sheeted covers.
The following example shows that the analogous fact is not true for topological volume in general.
Example 2.7We show in Section 4Section 4 thatm009 (Snappy notation) is the unique minimiser
ofRP 3,and hence volt(RP 3) = vol H(m009)≈2.66674. One sees this by noting thatRP 3 is
obtained as a Dehn filling ofm009 in a unique way, but it is not obtained by filling a cusped
hyperbolic 3–manifold of smaller volume. As we saw in Proposition 2.1Proposition 2.1, we have volt(S 3)≈
2.02988, so
volt(S3)<2 volt(RP 3).
This shows that the topological volume is not multiplicative under finite covers in general.
A surgery description ofm009 is given by performing a 2-surgery on one component of the
Whitehead linkL5a1 (using notation from the Thistlethwaite link table). The complement
of the other link component in this surgery yieldsm009. From this surgery description one
can see that the lift toS 3 of the minimiser inRP 3 is the complement ofL6a1 with volume
2·volt(RP 3)≈5.33.
Nonetheless we have the following behaviour of topological volume under finite-sheeted covers.
Lemma 2.8LetXandYbe closed, orientable 3–manifolds. If there is ad–fold coverX→Y,
then
volt(X)≤d·volt(Y).(2.4)
ProofSupposeXandYare closed, orientable 3–manifolds withp:X→Yad–fold cover.
SupposeLinYis a hyperbolic link. ThenX\p −1(L)→Y\Lis ad–fold cover and in particular
p−1(L)⊂Xis a hyperbolic link, with vol H(X\p −1(L)) =d·vol H(Y\L). A minimiserL⊂Y
hence gives volt(X)≤vol H(X\p −1(L)) =d·vol H(Y\L) =d·volt(Y).
Example 2.9For eachd >0,choosepandqsuch thatd·pandqare coprime. Then we
have ad–fold covering of lens spacesL(p,q)→L(d·p,q).We show in Proposition 1.3Proposition 1.3 that
forpsufficiently large, volt(L(d·p,q)) and volt(L(p,q)) are arbitrarily close to the volume of
the Whitehead link complement. Hence the gap in Equation (2.4)Equation (2.4) can be arbitrarily large, asd
varies.
Question 2.10IfX→Yis ad–fold cover of non-hyperbolic closed, orientable 3–manifolds,
is volt(X)<d·volt(Y), that is, is Inequality ( 2.42.4) always strict?
As an application of Proposition 2.8Proposition 2.8 we observe that knowledge about the topological volume
can be leveraged to give bounds on degrees of covers. Recall that a linkL⊂S 3 is calleduniversal
if every closed, orientable 3–manifold arises as a cover ofS 3 branched alongL. The existence
of universal links was first shown by Thurston in unpublished work. By work of Hilden, Lozano,
and Montesinos [HLM83HLM83,HLM85aHLM85a,HLM85bHLM85b], we know that there are numerous universal links,
including the figure eight knot, the Whitehead link, and the Borromean rings.
Corollary 2.11LetLbe a hyperbolic universal link inS 3 and letd L(M)denote the minimal
degree of a coverM→S 3 branched alongL. Then
volt(M)≤d L(M) volH(L).
For example, we have
volt(M)≤d K4a1(M) volH(K4a1) =d K4a1(M) volt(S3).
6
In particular, we obtain general lower bounds ond L(M) from the the topological volumes ofS 3
andM. On the other hand, we remark thatd L(M) is algorithmically computable, since the
homeomorphism problem for 3-manifolds is decidable: there exists a deterministic algorithm
to decide if two given 3-manifolds are homeomorphic or not [ Kup19Kup19]. Thus we can enumerate
all branched covers ofLordered by the degree of the covering and check when the first such
manifold is homeomorphic toM.

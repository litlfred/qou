---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-014-54-the-general-case
section_title: "The general case"
section_number: 5.4
pages: 13-15
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
---
since it involves edge paths between multiple cusps.
Lemma 5.5. If ε is a self edge from cusp i to itself, micε∈kρ
Proof. The proof is identical to that of Lemma 5.4. □
14 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
Lemma 5.6. If two (distinct) cusps i and j are joined by an edge ε in G, we have
(5.5) mimj∈kρ.
Proof. Consider the loop εj ¯Mj ¯εjMi shown in Figure 13. A simple computation shows that
(5.6) Tr( α(cε)β(−mj)α(−cε)β(mi)) = 2 +mimjc2
ε.
Since ε∈T , cε = 1, and the result follows. □
More generally, the following holds.
Lemma 5.7. We havemi∈kρ for all cusps i.
Proof. IfG is a tree with 1-cycle, thenc1 = 1, so Lemma 5.5 implies thatm1∈kρ. Inductively
applying Lemma 5.6 for the edge εj connecting cusp i = j− 1 and j implies the result. If
G is a tree with 3-cycle, the Ptolemy coordinates c1,c 2 andc3 are 1, so the edges of the face
are labeled by α(1) and β(−1) only (see Figure 3). Inserting the peripheral loops Mi as in
Figure 14, we obtain
(5.7) Tr
(
β(−1)β(m1)α(1)β(−1)β(m2)α(1)β(−1)β(m3)α(1)
)
∈kρ
By an elementary computation, the trace equals
(5.8) m1m2m3−m1m2−m2m3−m3m1 + 2∈kρ.
By Lemma 5.6, mimj∈ kρ, so m1∈ kρ. The result now follows as above by inductively
applying Lemma 5.6. □
Let ε be an arbitrary 1-cell. If ε is a self edge, Lemmas 5.5 and 5.7 imply that cε∈ kρ.
Otherwise, there exists an edge path p in the maximal tree G\ε1, such thatp∗ε is a loop in
ˆM. By relabeling the cusps and edges if necessary, we may assume that p =εi+1∗εi+2∗···∗ εj,
where εk goes from cusp k− 1 to cusp k. Pick peripheral paths Xk on cusp k connecting
the ends (in M, not ˆM) of edges εk and εk+1 (see Figure 15). We obtain a loop that can
be composed with arbitrary powers of the peripheral loops Mi,...,M j. We thus obtain the
following traces (where bk∈ Z)
(5.9) Tr( β(xi +bimi)α(ci+1)β(xi+1 +bi+1mi+1)α(ci+2)··· β(xj +bjmj)α(cε))∈kρ.
It will be convenient to regard Tr(β(xi)α(ci+1)β(xi+1)α(ci+2)··· β(xj)α(cε)) as a function
of variables xi (disregarding that the xi’s are ﬁxed expressions of the Ptolemy coordinates).
Deﬁnition 5.8. Given a function f(x1,...,x r), let ∆if be the function given by
(5.10) ∆ if(h) =f(x1,...,x i +h,...,x r)−f(x1,...,x i,...,x r).
The following is elementary.
Lemma 5.9. If f(x1,...,x r) is a polynomial where the exponents of all variables xi are 0
or 1, and where the highest degree term is ax1x2··· xr, we have
(5.11) ∆ r
(
··· ∆2
(
∆1f(h1)
)
(h2)···
)
=ah1h2...h r,
and is thus independent of the xi’s. □
THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS 15
α(1)
α(1)
α(1)
β(−1)
β(−1)
β(−1)
β(m1)
β(m2)
β(m3)
X3
X1
X2ε1
ε2
ε3
M3
M1
M2
α(ci+1)
β(xi)
β(mi)
Xi εi+1
Mi
α(cε)
ε
α(ci+2)
β(xi+1)
β(mi+1)
Xi+1 εi+2
Mi+1
β(xj)
β(mj)
Xj
Mj
Cusp j
εj
α(cj)
Figure 14. 3-cycle case. Figure 15. Arbitrary edge ε.
If, e.g., f(x1,x 2) =x1x2, we have
(5.12)
∆1f(h1) = (x1 +h1)x2−x1x2 =h1x2, ∆2
(
∆1f(h1)
)
(h2) =h1(x2 +h2)−h1x2 =h1h2.
Lemma 5.10. Let x1,...,x r be variables and y1,...,y r be constants. The expression
(5.13) Tr
(
β(x1)α(y1)··· β(xr)α(yr)
)
is a polynomial in the xi’s whose unique highest degree term is ∏r
i=1yi
∏r
i=1xi. Moreover,
for each monomial term, the exponent of each variable is either 1 or 0.
Proof. This follows by induction on r. □
Applying Lemmas 5.10 and 5.9 to the function
(5.14) f(xi,...,x j) = Tr
(
β(xi)α(ci+1)β(xi+1)α(ci+2)··· β(xj)α(cε)
)
,
we obtain
(5.15) ( mimi+1··· mjcici+1··· cj)cε∈kρ.
Since all mi’s are in kρ by Lemma 5.7, and all ci’s are 1 (since εi∈T ), it follows that cε is
in kρ. This concludes the proof.

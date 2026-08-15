---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-002-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
All graphs considered in this paper are finite and undirected with no loops or parallel edges.
The order of a graph is meant to be its number of vertices. Denote byA(Γ) the adjacency
matrix of a graph Γ, and call its eigenvalues theeigenvaluesof Γ. SinceA(Γ) is a real
symmetric matrix, the eigenvalues of Γ are real numbers, and we order them asλ 1(Γ)≥
λ2(Γ)≥···≥λ n(Γ), wherenis the order of Γ. Similarly, for a real symmetric matrixM,
we writeλ i(M) for itsi-th largest eigenvalue. Thespectrumof Γ, denoted by Spec(Γ), is the
multiset of eigenvalues of Γ. The differenceλ 1(Γ)−λ 2(Γ) is called thespectral gapof Γ. If
λ1(Γ) has multiplicityt, then we callλ t+1(Γ) thestrictly second largest eigenvalueof Γ. In
the case when Γ isd-regular, we haveλ 1(Γ) =dwith multiplicity the number of components
of Γ, and the spectral gapd−λ 2(Γ) equals the second smallest Laplacian eigenvalue of Γ.
LetGbe a finite group with identity elemente, and letSbe an inverse-closed subset of
G\{e}. TheCayley graphonGwith respect to theconnection setS, denoted by Cay(G,S),
is the|S|-regular graph with vertex setGand edge set{{g,gs}:g∈G,s∈S}. It is readily
seen that Cay(G,S) hast= [G:⟨S⟩] connected components, so its strictly second largest
eigenvalue isλt+1(Cay(G,S)), where [G:⟨S⟩] is the index inGof the subgroup⟨S⟩generated
byS. We call Cay(G,S)normalifSis closed under conjugation (that is,Sis the union of
some conjugacy classes ofG) andnonnormalotherwise.
1.1 Aldous’ spectral gap conjecture
Given a graph Γ on [n] ={1,2,...,n}, we may identify each edge{i,j}of Γ with the trans-
position (i j) of the symmetric groupS n on [n]. LetT(Γ) be the set of such transpositions
ofS n. Then Cay(S n,T(Γ)) is a Cayley graph onS n associated with Γ. It is readily seen
that Cay(Sn,T(Γ)) is connected whenever Γ is connected. Around 1992, Aldous [1] formu-
lated a stunning conjecture, which is widely known asAldous’ spectral gap conjecture. It
asserts that any connected graph Γ and its associated Cayley graph Cay(S n,T(Γ)) have the
same spectral gap. In other words, the random walk and the interchange process on any
connected graph have the same spectral gap. When Γ is a complete graph [11] or a star [12],
this was proved before Aldous made his conjecture, and when Γ is a complete multipartite
graph the conjecture was proved in [6]. After a series of partial successes (see [8] and the
references therein), Aldous’ spectral gap conjecture was finally proved by Caputo, Liggett
and Richthammer [4] in 2010. In fact, what they proved is a more general version of Aldous’
spectral gap conjecture, namely when each edge of Γ has a positive weight which carries for-
ward to corresponding edges of Cay(S n,T(Γ)). See [4, 7, 8] and [25, Section 8.1] for details.
In this paper we confine ourselves to the unweighted case.
Aldous’ spectral gap conjecture can be stated in terms of representations of symmetric
groups. LetGbe a group, and let ˆG={ρ 1,ρ 2,...,ρ k}denote a complete set of inequivalent
complex irreducible matrix representations ofG, with the assumption thatρ 1 is the trivial
representation. For eachρ i∈ ˆG, letχ i be the character ofρ i, and let ˜χi(g) :=χ i(g)/χi(e)
2
be the normalized character ofρ i atg∈G, whereχ i(e) = dimρ i is the dimension of
ρi. It is known [21] that the adjacency matrix of any Cayley graph Cay(G,S) onGis
equal to ∑
s∈SRreg(s), whereR reg is the right regular representation ofGandR reg(s) is the
permutation matrix representing right multiplication bysonG. Setρ i(S) := ∑
s∈Sρi(s),
and denote by⊕the direct sum of matrices. The adjacency matrix of Cay(G,S) is similar to
d1ρ1(S)⊕d 2ρ2(S)⊕···⊕d kρk(S) (see [21, Proposition 7.1]), whered i = dimρi andd iρi(S)
denotes the direct sum ofd i copies ofρ i(S). This implies that the spectrum of Cay(G,S)
is the union ofd i copies of the multiset of eigenvalues ofρ i(S), for 1≤i≤k. We say that
an eigenvalueµof Cay(G,S) isattained[22] by the representationρ i ofGifµ=λ 1(ρi(S)).
In particular, the strictly second largest eigenvalueλ t+1(Cay(G,S)) of Cay(G,S) (where
t= [G:⟨S⟩]) isattainedbyρ i ifλ t+1(Cay(G,S)) =λ 1(ρi(S)). If Cay(G,S) is normal, then
Schur’s lemma implies that eachρ i(S) is a scalar matrix, and the eigenvalues of Cay(G,S)
are given by ([11, 33])
µj = 1
χj(e)
∑
s∈S
χj(s) =
∑
s∈S
˜χj(s), j= 1,2,...,k.(1)
Moreover, the multiplicity ofµj is equal to∑
1≤i≤k,µ i=µjχi(e)2. Thus, if Cay(G,S) is normal,
then an eigenvalueµof Cay(G,S) is attained byρ i if and only ifµ= ∑
s∈S ˜χi(s), and in
particular the strictly second largest eigenvalue of Cay(G,S) is attained byρ i if and only if
λt+1(Cay(G,S)) = ∑
s∈S ˜χi(s).
It is known [28] that each partition ofngives rise to an irreducible representation ofS n,
known as a Specht module, and such Specht modules form a complete list ˆSn of inequiva-
lent irreducible representations ofS n. The Specht modules corresponding to the partitions
(n−1,1) and (1 n) ofnare called thestandard representationandsign representationof
Sn and are denoted byρ (n−1,1) andρ (1n), respectively. As explained in [6, 7, 27], Aldous’
spectral gap conjecture is equivalent to saying that for any connected graph Γ with ver-
tex set [n] the second largest eigenvalue of Cay(S n,T(Γ)) is attained byρ (n−1,1); that is,
λ2(Cay(Sn,T(Γ))) =λ 1(ρ(n−1,1)(T(Γ))), orλ 2(Cay(Sn,T(Γ))) = ∑
σ∈T(Γ) ˜χ(n−1,1)(σ) when
Cay(Sn,T(Γ)) is normal. This version of Aldous’ spectral gap conjecture motivated the fol-
lowing notion for generalizing the conjecture (see [2, 8, 20, 27] for other attempts to generalize
Aldous’ spectral gap conjecture).
Definition 1.1([22, Definition 1.1]).A Cayley graph Cay(S n,S) onS n is said to have the
Aldous propertyif its strictly second largest eigenvalue is attained by the standard represen-
tation ofS n, that is,λ t+1(Cay(Sn,S)) =λ 1(ρ(n−1,1)(S)), wheret= [S n :⟨S⟩].
In particular, if Cay(S n,S) is normal, then it has the Aldous property if and only if
λt+1(Cay(Sn,S)) =
∑
σ∈S ˜χ(n−1,1)(σ).
It would be natural to study the following problem.
Problem 1.1.Determine all Cayley graphs onS n that have the Aldous property.
3
In this paper we study this problem with a focus on normal Cayley graphs onS n. Before
discussing our results, let us give a brief account of recent progress on Problem 1.1. As
usual, for a permutationσ∈S n, let supp(σ) ={i∈[n] :σ(i)̸=i}be thesupportofσand
fix(σ) ={i∈[n] :σ(i) =i}the set offixed pointsofσ. ForI⊆{2,3,...,n}and 2≤k≤n,
set
Suppn(I) ={σ∈S n :|supp(σ)|∈I}
and
Suppn(k) ={σ∈S n :|supp(σ)|=k}.
For 1≤r <k <nandI⊆{2,3,...,n}, letC(n,k) be the set of allk-cycles inS n,C(n,k;r)
the set of allk-cyclesσinS n with fix(σ)⊆{r+ 1,...,n}, andC(n,I) = ⋃
k∈IC(n,k). In
[22], Li, Xia and Zhou proved the following results for sufficiently largenwith the help of
[27, Proposition 2.3]: ifSis a single conjugacy class ofS n, then Cay(Sn,S) has the Aldous
property if and only if 2≤|supp(σ)|≤n−2 for eachσ∈S; for∅̸=I⊆{2,3,...,n}with
|I∩{n−1,n}|̸= 1, Cay(S n,Suppn(I)) has the Aldous property if and only ifI∩{n−1,n}=∅;
for any 2≤k≤n, Cay(S n,Suppn(I)) whereI={2,...,k}has the Aldous property. In
[23], the same authors proved that the strictly second largest eigenvalue of Cay(S n,C(n,I))
can be attained by at most four distinct irreducible representations ofS n, and for some
specialI⊆{2,3,...,n}they further determined the exact value of this eigenvalue and its
multiplicity. As a corollary, they gave a necessary and sufficient condition for Cay(Sn,C(n,I))
to have the Aldous property whenI∩{n−1,n}=∅, and showed that this graph does not

---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-008-51-normal-cayley-graphs-ons-n-that-are-line-grap
section_title: "Normal Cayley graphs onS n that are line graphs"
section_number: 5.1
pages: 12-17
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
Theline graphof a graph Γ is the graph whose vertices correspond to the edges of Γ, where
two vertices are adjacent if and only if the corresponding edges in Γ share exactly one end-
vertex. A graph is called aline graphif it is isomorphic to the line graph of some graph. The
following result gives a classification of normal Cayley graphs onS n that are line graphs.
12
Theorem 5.1.Letn≥2, and letSbe a nonempty normal set inS n. ThenCay(S n,S)is a
line graph if and only if one of the following holds:
(a)S=S n\{e}, and henceCay(S n,S) ∼=Kn!;
(b)S=A n\{e}, and henceCay(S n,S) ∼= 2Kn!/2;
(c)n= 4andS={(1 2)(3 4),(1 3)(2 4),(1 4)(2 3)}, and henceCay(S n,S) ∼= 6K4.
Our proof of Theorem 5.1 is based on Beineke’s characterization of line graphs. In 1970,
he proved [3] that a graph is a line graph if and only if it does not contain any one of the
nine forbidden graphs as an induced subgraph. For our purposes, we only show two of these
nine forbidden subgraphs, denoted byH 1 andH 2, in Figure 1.
δ
τ1
τ2
τ3
ω
H1
δ
τ1
τ2
τ3
H2
Figure 1: Two forbidden subgraphs for line graphs
The following lemma deals with the case when the connection set contains all transposi-
tions. In its proof we writex∼yto denote thatxandyare adjacent in the Cayley graph
Cay(Sn,S) under consideration.
Lemma 5.2.Letn≥2, and letSbe a nonempty normal set inS n which contains the
conjugacy class of all transpositions. ThenCay(S n,S)is a line graph if and only ifS=
Sn\{e}, or equivalently,Cay(S n,S) ∼=Kn!.
Proof.The sufficiency is obvious. It remains to prove the necessity.
Suppose that Cay(S n,S) is a line graph. Then by Beineke’s characterization it does
not containH 1 orH 2 (see Figure 1) as an induced subgraph. We aim to prove that every
permutationσ∈S n with|supp(σ)|≥2 belongs toS. We prove this statement by induction
on|supp(σ)|. If|supp(σ)|= 2, then the statement follows from the assumption thatS
contains all transpositions. If|supp(σ)|= 3, thenσ∈S, for otherwise an induced subgraph
of Cay(Sn,S) isomorphic toH 2 can be easily found by takingδ=e,τ 1 = (1 2),τ 2 = (2 3),
andτ 3 = (1 3) in Figure 1.
Assume inductively that for somek≥4 every permutation inS n with support size at
mostk−1 belongs toS. We now show that for an arbitrary permutationσ∈S n with
|supp(σ)|=kwe must haveσ∈S. Suppose first that the cycle decomposition ofσcontains
13
a cycle of length at least 3. Then we may write without loss of generality thatσ= (1 2···t)σ ′
for somet≥3 andσ ′∈S n. Set
δ=e, τ 1 = (2 3···t)σ ′, τ 2 = (1 3···t)σ ′, τ 3 = (3···t)σ ′, ω=σ.
By the induction hypothesis,e∼τ i for 1≤i≤3. Moreover, a direct computation shows
thatτ −1
i τj for 1≤i < j≤3 andτ −1
i σfor 1≤i≤3 are 2-cycles or 3-cycles. Since by our
induction hypothesis all 2-cycles and 3-cycles belong toS, we haveτ i∼σfor 1≤i≤3
andτ i∼τ j for all 1≤i < j≤3. Since Cay(S n,S) does not contain an induced subgraph
isomorphic toH 1, we must havee∼σand thereforeσ∈S.
It remains to consider the case when the cycle decomposition ofσcontains only cycles
of lengths 1 and 2. Since|supp(σ)|=k≥4, we may assume without loss of generality that
σ= (1 2)(3 4)σ′ for someσ ′∈S n. Let
δ=e, τ 1 = (1 2 3)σ′, τ 2 = (1 2 3 4)σ′, τ 3 = (1 2 4 3)σ′, ω=σ.
By what we proved in the previous paragraph, we havee∼τ i for 1≤i≤3. Moreover, a
direct computation shows thatτ −1
i τj for 1≤i<j≤3 andτ −1
i σfor 1≤i≤3 have supports
of size at most 3. Since by our induction hypothesis all 2-cycles and 3-cycles belong toS,
we haveτ i∼σfor 1≤i≤3 andτ i∼τ j for all 1≤i < j≤3. Since Cay(S n,S) does not
contain an induced subgraph isomorphic toH 1, we must havee∼σand henceσ∈S.
So, by mathematical induction, we have proved thatScontains every permutation inS n
with support size at least 2. Therefore,S=S n\{e},or equivalently, Cay(S n,S) ∼=Kn!.
The next lemma deals with the case when the connection set does not contain the conju-
gacy class of transpositions but contains the conjugacy class of 3-cycles.
Lemma 5.3.Letn≥3, and letSbe a nonempty normal set inS n which contains the
conjugacy class of3-cycles but not the conjugacy class of transpositions. ThenCay(S n,S)is
a line graph if and only ifS=A n\{e}, in which caseCay(S n,S) ∼= 2Kn!/2.
Proof.The sufficiency is obvious. We prove the necessity.
Suppose that Cay(Sn,S) is a line graph. Then by Beineke’s characterization it does not
containH 1 orH 2 (see Figure 1) as an induced subgraph. We first show thatAn\{e}⊆S,that
is, every permutationσ∈A n with|supp(σ)|≥3 belongs toS. We prove this statement by
induction on|supp(σ)|. Clearly, if|supp(σ)|= 3, the statement follows from our assumption
thatScontains all 3-cycles.
Letσ∈A n be such that|supp(σ)|= 4. Sinceσis an even permutation, without loss
of generality we may assume thatσ= (1 2)(3 4).Suppose, for a contradiction, thatσ /∈S.
SinceSis a union of conjugacy classes, this assumption implies that no permutation with
cycle type (2,2,1,...,1) belongs toS. Let
δ=e, τ 1 = (1 2 3), τ 2 = (1 3 4), τ 3 = (2 4 3).
14
Then, by our assumption,e∼τ i for 1≤i≤3. A direct calculation leads to
τ−1
1 τ2 = (1 4)(2 3), τ −1
1 τ3 = (1 2)(3 4), τ −1
2 τ3 = (1 3)(2 4).
Therefore,τ 1,τ 2, andτ 3 are mutually nonadjacent in Cay(S n,S). Consequently, the sub-
graph induced by{e,τ 1,τ 2,τ 3}is isomorphic to the forbidden subgraphH 2 in Figure 1, a
contradiction. Henceσ∈S.
Assume inductively that for somek≥5 every even permutation with support size at most
k−1 belongs toS. Letσ∈A n be such that|supp(σ)|=k. We aim to show thatσ∈S. If
the cycle decomposition ofσcontains an odd cycle of length at least 5, then we may assume
without loss of generality thatσ= (1 2 3···t)σ ′ for some oddt≥5 andσ ′∈A n. Note that
t≤k. Let
δ=e, τ 1 = (1 2 3)σ′, τ 2 = (2 3 4)σ′, τ 3 = (1 3 4)σ′, ω=σ.
Then eachτ i is an even permutation with support size at mostk−2, and hencee∼τ i for
1≤i≤3 by the induction hypothesis. Moreover, eachτ −1
i ωis an even permutation with
support size at mostt−1 (≤k−1), and soτ i∼σfor 1≤i≤3. Also, eachτ −1
i τj is an
even permutation with support size at most 4, and henceτ i∼τ j for 1≤i < j≤3 by the
induction hypothesis. Since Cay(Sn,S) is a line graph, it does not containH 1 as an induced
subgraph. Thus, we must havee∼σ, that is,σ∈S.
If the cycle decomposition ofσcontains an even cycle of length at least 4, then we may
assume without loss of generality thatσ= (1 2 3···t)σ ′ for some event≥4 andσ ′∈S n,
and we set
δ=e, τ 1 = (1 2)σ′, τ 2 = (2 3)σ′, τ 3 = (1 3)σ′, ω=σ.
If the cycle decomposition ofσcontains both a 2-cycle and a 3-cycle, then we may assume
without loss of generality thatσ= (1 2 3)(4 5)σ ′ for someσ ′∈S n, and we set
δ=e, τ 1 = (1 2)σ′, τ 2 = (2 3)σ′, τ 3 = (1 3)σ′, ω=σ.
If the cycle decomposition ofσcontains only 3-cycles, then since|supp(σ)|=k≥5 we may
assume without loss of generality thatσ= (1 2 3)(4 5 6)σ ′ for someσ ′∈A n, and we set
δ=e, τ 1 = (1 2)(4 5)σ′, τ 2 = (2 3)(4 5)σ′, τ 3 = (1 3)(4 5)σ′, ω=σ.
Finally, if the cycle decomposition ofσcontains only 2-cycles, then since|supp(σ)|=k≥5
we may assume without loss of generality thatσ= (1 2)(3 4)(5 6)σ ′ forσ ′∈S n, and we set
δ=e, τ 1 = (1 2)σ′, τ 2 = (3 4)σ′, τ 3 = (5 6)σ′, ω=σ.
In each case, arguing exactly as in the previous paragraph, we obtain thatσ∈S.
So, by mathematical induction, we have proved thatAn\{e}⊆S.To proveS=A n\{e},
it suffices to show that no odd permutationσ∈S n with|supp(σ)|≥4 belongs toS. Assume
15
for a contradiction thatσ∈Sis odd and|supp(σ)|≥4. Since|supp(σ)|≥4, we can find
two distinct permutationsσ 1 andσ 2 in the conjugacy classC(S n,σ), both different fromσ.
Sinceσ∈SandSis a normal set, we haveσ 1,σ 2∈S. Let
δ=e, τ 1 =σ, τ 2 =σ 1, τ 3 =σ 2, ω= (1 2).
Thenδ∼τ i for 1≤i≤3. Moreover, eachτ −1
i ωis an even permutation, and henceτ i∼ω
for 1≤i≤3. Also, eachτ −1
i τj is an even permutation, and henceτ i∼τ j for 1≤i<j≤3.
On the other hand, since by our assumption the transposition (1 2) does not belong toS,
δandωare not adjacent in Cay(S n,S). Therefore, the subgraph of Cay(S n,S) induced by
{δ,τ 1,τ 2,τ 3,ω}is isomorphic toH 1, a contradiction. Therefore,S=A n\{e}and consequently
Cay(Sn,S) ∼= 2Kn!/2.
We are now ready to prove Theorem 5.1.
Proof of Theorem 5.1.The sufficiency is obvious, so it remains to prove the necessity.
Suppose thatSis a nonempty normal set inS n such that Cay(Sn,S) is a line graph. IfS
contains the conjugacy class of transpositions, then by Lemma 5.2,S=S n\{e}, and hence
Cay(Sn,S) ∼=Kn!. IfSdoes not contain the conjugacy class of transpositions but contains the
conjugacy class of 3-cycles, then by Lemma 5.3,S=A n\{e}, and hence Cay(Sn,S) ∼= 2Kn!/2.
Therefore, we may assume in the sequel that|supp(σ)|≥4 for everyσ∈S.
IfScontains an elementσwhose cycle decomposition contains a cycle of length at least
4, then we may assume without loss of generality thatσ= (1 2 3 4···t)σ ′ for somet≥4
andσ ′∈S n. Let
δ=e, τ 1 = (1 2 3 4···t)σ ′, τ 2 = (1 3 4···t2)σ ′, τ 3 = (1 3 2 4···t)σ ′.
Sinceτ 1,τ 2, andτ 3 all lie in the conjugacy class ofσ, we haveτ i∈Sfor 1≤i≤3, and
henceδ∼τ i for 1≤i≤3. Moreover, eachτ −1
i τj is a 3-cycle, and hence by our assumption
τi andτ j are not adjacent in Cay(Sn,S) for 1≤i<j≤3. Therefore, the subgraph induced
by{δ,τ 1,τ 2,τ 3}is isomorphic toH 2 in Figure 1, but this contradicts our assumption that
Cay(Sn,S) is a line graph.
IfScontains an elementσwhose cycle decomposition contains both a 2-cycle and a 3-
cycle, then we may assume without loss of generality thatσ= (1 2)(3 4 5)σ′ for someσ′∈S n.
Let
δ=e, τ 1 = (1 2)(3 4 5)σ′, τ 2 = (1 2)(3 5 4)σ′, τ 3 = (3 5)(1 4 2)σ′.
Arguing as above, we haveδ∼τ i for 1≤i≤3 andτ i andτ j are not adjacent in Cay(Sn,S) for
1≤i<j≤3. Therefore, the subgraph of Cay(S n,S) induced by{δ,τ 1,τ 2,τ 3}is isomorphic
toH 2 in Figure 1, contradicting the assumption that Cay(S n,S) is a line graph.
IfScontains an elementσwhose cycle decomposition contains only 3-cycles, then, since
|supp(σ)|≥4, we may assume without loss of generality thatσ= (1 2 3)(4 5 6)σ ′ for some
σ′∈S n. Let
δ=e, τ 1 = (1 2 3)(4 5 6)σ′, τ 2 = (1 6 2)(3 4 5)σ′, τ 3 = (1 4 2)(3 5 6)σ′.
16
Thenδ∼τ i for 1≤i≤3. Moreover, eachτ −1
i τj is a 5-cycle. Since we have already
shown that no 5-cycle lies inS, it follows thatτ i andτ j are not adjacent in Cay(S n,S) for
1≤i<j≤3. Therefore, the subgraph of Cay(S n,S) induced by{δ,τ 1,τ 2,τ 3}is isomorphic
toH 2 in Figure 1, a contradiction.
Ifn≥5 andScontains an elementσwith at least one fixed point whose cycle decom-
position contains only 2-cycles, then, since|supp(σ)|≥4, we may assume without loss of
generality that 5/∈supp(σ) andσ= (1 2)(3 4)σ ′ for someσ ′∈S n. Let
δ=e, τ 1 = (1 2)(3 4)σ′, τ 2 = (1 5)(3 4)σ′, τ 3 = (2 5)(3 4)σ′.
Arguing as above, we haveδ∼τ i for 1≤i≤3 andτ i andτ j are not adjacent in Cay(Sn,S) for
1≤i<j≤3. Therefore, the subgraph of Cay(S n,S) induced by{δ,τ 1,τ 2,τ 3}is isomorphic
toH 2 in Figure 1, and hence Cay(S n,S) cannot be a line graph, a contradiction.
Ifn≥5 andScontains an elementσwith no fixed point whose cycle decomposition
consists only of 2-cycles, then, sincen≥5, we may assume without loss of generality that
σ= (1 2)(3 4)(5 6)σ′ for someσ ′∈S n. Let
δ=e, τ 1 = (1 2)(3 4)(5 6)σ′, τ 2 = (1 3)(2 5)(4 6)σ′, τ 3 = (1 4)(2 6)(3 5)σ′.
Thenδ∼τ i for 1≤i≤3. Moreover, the cycle decomposition of eachτ −1
i τj consists of two
3-cycles for 1≤i < j≤3. Since we have already shown that no element ofScontains a
3-cycle, it follows thatτ i andτ j are not adjacent in Cay(Sn,S) for 1≤i<j≤3. Therefore,
the subgraph of Cay(S n,S) induced by{δ,τ 1,τ 2,τ 3}is isomorphic toH 2 in Figure 1, and
hence Cay(Sn,S) cannot be a line graph, a contradiction.
Summing up, the only remaining case is thatn= 4 andScontains an elementσwhose
cycle decomposition contains only 2-cycles. In this case, we haveS={(1 2)(3 4),(1 3)(2 4),
(1 4)(2 3)}, and hence Cay(Sn,S) ∼= 6K4. This completes the proof.

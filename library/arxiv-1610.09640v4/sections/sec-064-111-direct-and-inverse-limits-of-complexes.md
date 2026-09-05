---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-064-111-direct-and-inverse-limits-of-complexes
section_title: "Direct and Inverse Limits of Complexes"
section_number: 11.1
pages: 185-187
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
limits in this section. Limits in abstract abelian and DG categories (not to mention
triangulated categories) are a very delicate issue. We will try to be as concrete as
possible, in order to avoid pitfalls and confusion. The notation we use for direct
and inverse limits of systems indexed byN was presented in Subsection 1.8.
Proposition 11.1.1.
(1) Let{Mk}k∈N be a direct system inCstr(A, M). Assume that for everyi the
direct limit limk→Mi
k exists in M. Then the direct limitM = limk→Mk
exists in Cstr(A, M), and in degreei it isMi = limk→Mi
k.
(2) Let{Mk}k∈N be an inverse system inCstr(A, M). Assume that for every
i the inverse limit lim←kMi
k exists in M. Then the inverse limit M =
lim←kMk exists in Cstr(A, M), and in degreei it isMi = lim←kMi
k.
Proof. We will only prove item (1); the proof of item (2) is similar. For each integer
i deﬁneMi := limk→Mi
k∈M. By the universal property of the direct limit, the
diﬀerentialsd :Mi
k→Mi+1
k induce diﬀerentialsd :Mi→Mi+1, and in this way we
obtain a complexM :={Mi}i∈Z∈C(M). Similarly, every elementa∈Aj induces
morphismsa :Mi→Mi+j in M, and thusM becomes an object ofC(A, M). There
are morphismsMk→M in Cstr(A, M), and it is easy to see that these makeM
into a direct limit of the system{Mk}k∈N. □
Since limits exist inM = ModK, the proposition above says that they exist in
Cstr(A). Likewise they exist in the categoryGstr(K) of gradedK-modules.
We say that a direct system{Mk}k∈N in M is eventually stationaryifµk :Mk→
Mk+1 are isomorphisms for large k. Similarly we can talk about an eventually
stationary inverse system. The limit of an eventually stationary system (direct or
inverse) always exists: it isMk for large enoughk.
Proposition 11.1.2.
(1) Let{Mk}k∈N be a direct system inCstr(A, M). Assume that for eachi the
direct system{Mi
k}k∈N in M is eventually stationary. Then the direct limit
M = limk→Mk exists in Cstr(A, M), the direct limitlimk→H(Mk) exists in
Gstr(M), and the canonical morphismlimk→H(Mk)→H(M) in Gstr(M)
is an isomorphism.
(2) Let{Mk}k∈N be an inverse system inCstr(A, M). Assume that for eachi the
inverse system{Mi
k}k∈N in M is eventually stationary. Then the inverse
limit M = lim←kMk exists in Cstr(A, M), the inverse limitlim←k H(Mk)
exists in Gstr(M), and the canonical morphismH(M)→lim←k H(Mk) in
Gstr(M) is an isomorphism.
Proof. Again, we only prove item (1). As mentioned above, for eachi the limit
Mi = limk→Mi
k exists inM. By Proposition 11.1.1 the limitM = limk→Mk exists
in Cstr(A, M).
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
185
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Regarding the cohomology: ﬁx an integeri. Take k large enough such that
Mi′
k →Mi′
k′are isomorphisms for allk≤k′andi−1≤i′≤i+1. ThenMi′
k′→Mi′
are isomorphisms in this range, and thereforeHi(Mk′)→Hi(M) are isomorphisms
for allk≤k′. We see that the direct system{Hi(Mk)}k∈N is eventually stationary,
and its direct limit isHi(M). □
When we drop the abstract abelian categoryM, i.e. when we work withM =
ModK = M(K) and Cstr(A, M) = Cstr(A), there is no problem of existence of limits.
The next proposition says that furthermore “direct limits are exact” inCstr(A).
Proposition 11.1.3. Let{Mk}k∈N be a direct system inCstr(A), with limitM =
limk→Mk. Then the canonical homomorphismlimk→H(Mk)→H(M) in Gstr(K)
is bijective.
Exercise 11.1.4. Prove Proposition 11.1.3. (Hint: forget the action of A, and
work with complexes ofK-modules.)
Exactness of inverse limits tends to be much more complicated than that of
direct limits, even forK-modules. We always have to impose some condition on the
inverse system to have exactness in the limit.
Let
(
{Mk}k∈N,{µk}k∈N
{
be an inverse system in M(K). For every k≤l let
Mk,l⊆Mk be the image of the homomorphismµk,l : Ml→Mk. Note that there
are inclusionsMk,l+1⊆Mk,l, so for ﬁxedk we have an inverse system{Mk,l}l≥k
of submodules ofMk.
Deﬁnition 11.1.5.We say that an inverse system{Mk}k∈N in M(K) has the
Mittag-Leﬄer propertyif for every indexk, the inverse system{Mk,l}l≥k is even-
tually stationary.
Example 11.1.6. If the inverse system
(
{Mk}k∈N,{µk}k∈N
{
in M(K) satisﬁes at
least one of the following conditions, then it has the Mittag-Leﬄer property:
(a) The system has surjective transitions.
(b) The system is eventually stationary.
(c) For everyk∈N there exists somel≥k such thatMk,l = 0. This is called
the trivial Mittag-Leﬄer property, and one says that the system ispro-zero.
Theorem 11.1.7 (Mittag-Leﬄer Argument). Let{Mk}k∈N be an inverse system
in Cstr(A), with inverse limitM = lim←kMk. Assume the system satisﬁes these
two conditions:
(a) For everyi∈Z the inverse system{Mi
k}k∈N in M(K) has the Mittag-Leﬄer
property.
(b) For everyi∈Z the inverse system{Hi(Mk)}k∈N in M(K) has the Mittag-
Leﬄer property.
Then the canonical homomorphismsHi(M)→lim←k Hi(Mk) are bijective for alli.
Proof. We can forget all about the gradedA-module structure, and just view this
as an inverse system in Cstr(Z), i.e. an inverse system of complexes of abelian
groups. Now this is a special case of [75, Proposition 1.12.4] or [56, Chapitre0III,
Proposition 13.2.3]. □
The most useful instance of the ML argument is this:
Corollary 11.1.8. Let{Mk}k∈N be an inverse system in Cstr(A), with inverse
limit M = lim←kMk. Assume the system satisﬁes these two conditions:
(a) For everyi∈Z the inverse system{Mi
k}k∈N has surjective transitions.
(b) For everyk the DG moduleMk is acyclic.
Then M is acyclic.
186
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. Conditions (a) and (b) here imply conditions (a) and (b) of Theorem 11.1.7,
respectively. □
Exercise 11.1.9. Prove Corollary 11.1.8 directly, without resorting to Theorem
11.1.7.
By generalized integerswe mean elements of the ordered setZ∪{±∞}. Recall
that for a subsetS⊆Z, its inﬁmum isinf(S)∈Z∪{±∞}, where inf(S) = +∞
iﬀS =∅. Likewise the supremum is sup(S)∈Z∪{±∞}, where sup(S) =−∞
iﬀS = ∅. For i∈Z∪{±∞}the expression−i has a value inZ∪{±∞}. If
i0,i 1 ∈Z∪{±∞}satisfy i0 ≤i1, then−i1 ≤−i0. For i0,i 1 ∈Z∪{∞}, the
expressions i0 +i1 and−i0−i1 have values inZ∪{±∞}. A generalized integeri
is calledﬁniteif i< ∞, i.e. ifi∈Z∪{−∞}.
Deﬁnition 11.1.10.Given i0∈Z∪{−∞}and i1∈Z∪{∞}, withi0≤i1, the
integer intervalwith these endpoints is the set
[i0,i 1] :={i∈Z|i0≤i≤i1}⊆Z.
There is also the empty integer interval∅. When the elements of an integer interval
represent degrees, we sometimes call it adegree interval.
We exclude the possibilitiesi0 = i1 =∞and i0 = i1 =−∞for endpoints of
intervals. In calculus notation we have[i0,∞] = [i0,∞)∩Z, etc.; but we avoid the
open interval notation on purpose. Whenever we refer to an integer interval[i0,i 1],
it is always assumed that the generalized integersi0 and i1 satisfy the conditions
in Deﬁnition 11.1.10. Further properties of integer intervals will be studied in
Subsection 12.1.
Deﬁnition 11.1.11.LetM ={Mi}i∈Z be a graded object inM, and letS :={i∈
Z|Mi⁄= 0}⊆Z.
(1) The supremum of M is sup(M) := sup(S)∈Z∪{±∞}.
(2) The inﬁmumof M is inf(M) := inf(S)∈Z∪{±∞}.
(3) The amplitude of M is amp(M) := sup(M)−inf(M)∈N∪{±∞}.
Note that for M = 0 this reads S = ∅, inf(M) = ∞, sup(M) = −∞and
amp(M) =−∞. ThusM is bounded (resp. bounded above, resp. bounded below)
iﬀamp(M)<∞(resp. sup(M)<∞, resp. inf(M)>−∞).

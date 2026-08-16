---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-003-3-specht-modules
section_title: "Specht modules"
section_number: 3
pages: 3-4
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 46 sections: MATTHIAS K ¨UNZER AND ANDREW MATHA; Introduction and statement of main; The Hecke algebra and permutation"
---
We will need two dualities on the category of right H –modules. Both of them
come from involutions on H . The ﬁrst duality comes from the involution ∗ deﬁned
above. The second is induced from the automorphism # : H − →H which is the
R–linear map on H determined by T #
w = ( −q)l(w)T −1
w−1, for all w ∈ Sn. It is
straightforward to check that # preserves the relations in H and, hence, that it is
anR-algebra automorphism of order 2. Note that the involutions # and ∗ commute.
If V is an H -module let V ∗ be its R-linear dual. Then V ∗ becomes an H –
module by letting ( φ ·ξ)(v) := φ(vξ ∗), where φ ∈V ∗,v ∈V and ξ ∈ H . With the
according operation on morphisms, this deﬁnes a contravariant se lf–equivalence on
the category of H -modules.
If V is an H -module let V # the H -module with underlying R-module V and
operationv ·#ξ :=v ·ξ#, where v ∈V andξ ∈ H . With the identical operation on
morphisms, this deﬁnes a covariant self–equivalence on the catego ry of H -modules.
3. Specht modules
We recall some well-known facts due to Dipper and James [ 2].
Let λ = (λ1,λ 2,... ) be a composition of n. The diagram of λ is the set [ λ] =
{ (i,j ) ∈ N2 | 1 ≤j ≤λi }. We identify the diagram of λ with an array of boxes in
the plane. For example, if λ = (4, 3, 2) then
[λ] = .
The conjugate ofλ is the partition λ′ = (λ′
1,λ ′
2,... ), where λ′
j = # {i ≥ 1 |λi ≥j }
for all j; that is, λ′ is the partition of n whose diagram is obtained by interchanging
the rows and columns of the diagram of λ.
Formally, aλ–tableau is a bijection t : [λ] − → {1, 2,...,n }; however, we will think
of a λ–tableau as a labelling of the diagram of λ by the numbers 1 , 2,...,n . Ac-
cordingly, we will speak of the rows and columns of a tableau. For exa mple,
1 2 3
4 5 , 1 3 5
2 4 , 1 4 5
2 3 and 2 3 4
1 5
are all (3, 2)–tableaux.
A tableau is row standard if in each row its entries increase from left to right.
A tableau is standard if it is row standard and in each column its entries increase
from top to bottom. Let Std( λ) be the set of standard λ-tableaux.
All of the tableaux above are row standard; however, only the ﬁrs t two tableaux
are standard.
The initialλ–tableau tλ is the standardλ–tableau which has the numbers 1, 2,...,n
entered in order from left to right, and then top to bottom, along it s rows. The
terminal λ–tableau tλ is the standard λ–tableau which has the numbers 1 , 2,...,n
entered in order from top to bottom, and then left to right, along it s columns. Of
the (3, 2)–tableaux above, the ﬁrst is t(3,2) and the second is t(3,2).
The symmetric group Sn acts from the right on the set of λ–tableaux by per-
muting their entries. If t is a λ–tableau let d(t) be the unique permutation such
that t = tλd(t). In particular, we set wλ =d(tλ).
We remark that Dµ = {d(t) | t is a row standard µ–tableau }.
Suppose that λ is a partition of n and let zλ =xλTwλyλ′ . The Specht module is
the submodule S(λ) = zλH of M (λ).

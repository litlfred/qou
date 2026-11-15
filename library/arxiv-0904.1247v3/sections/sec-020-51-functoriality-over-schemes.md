---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-020-51-functoriality-over-schemes
section_title: "Functoriality over schemes"
section_number: 5.1
pages: 31-32
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
ﬁt into the theme of the paper and are likely useful elsewhere.
Theorem 5.1. For a diagram X1 →Y ←X2 where X1, X2 are stacks and Y a scheme, the
canonical map induced by !-pullbacks is an equivalence
D(X1) ⊗D(Y ) D(X2)
∼
/ D(X1 ×Y X2).
Proof. The tensor product of D(Y )-modules can be calculated as the geometric realization of the
two-sided bar construction ([L2, 4.3.4]), the simplicial category with k-simplices
D(X1) ⊗D(Y ) ⊗· · · ⊗D(Y ) ⊗D(X2),
where the factor D(Y ) appears k times and the maps are given by the D(Y )-module structures in
the usual pattern. This is canonically equivalent to the simplicial category with k-simplices
D(X1 × Y × · · · × Y × X2)
where the factor Y appears k times and the maps are given by !-pullbacks in the usual pattern.
This extends to an augmented simplicial category with augmentation given by the pullback
j!
−1 : D(X1 × X2)
/ D(X1 ×Y X2)
along the relative diagonal
j−1 : X1 ×Y X2
/ X1 × X2
The map j−1 is a base change of the diagonal map of Y , and since Y is a separated scheme, j−1 is
a closed embedding.
Similarly, the analogous diagonal maps
jk : X1 × Y × · · · × Y × X2
/ X1 × Y × · · · × Y × Y × X2
where the factor Y appears k times in the domain and k + 1 times in the codomain are closed
embeddings.
Now let us consider pushforwards along the above closed embeddings and apply Kashiwara’s
lemma: for a closed embedding j and a D-module M, the natural adjunction map M →j!j∗M is
an equivalence. Thus by base change, the pushforward
j−1∗: D(X1 ×Y X2)
/ D(X1 × X2)
and its higher analogues
jk∗: D(X1 × Y × · · · × Y × X2)
/ D(X1 × Y × · · · × Y × Y × X2)
provide a lift to a split augmented simplicial category.
Finally, by [L1, Lemma 6.1.3.16], in any ∞-category, split augmented simplicial diagrams are
colimit diagrams.
□
Theorem 5.2. Let X be a stack, Y a scheme, and f : X →Y a safe morphism (for example, a
relative Deligne-Mumford stack). Then D(X) is a self-dual module over D(Y ).
Proof. By Theorem 5.1, we have a canonical equivalence
D(X) ⊗D(Y ) D(X) ≃D(X ×Y X).
Thus we can deﬁne a unit and counit by the correspondences
u = ∆∗f ! : D(Y )
/ D(X ×Y X) ≃D(X) ⊗D(Y ) D(X)
c = f∗∆! : D(X) ⊗D(Y ) D(X) ≃D(X ×Y X)
/ D(Y )
31
where ∆: X →X ×Y X is the diagonal. Here we assume f : X →Y is safe to ensure the continuity
of the functor f∗.
We must check that the following composition is the identity
D(X)
u⊗id / D(X) ⊗D(Y ) D(X) ⊗D(Y ) D(X)
id ⊗c / D(X).
Consider the following commutative diagram with Cartesian square:
X
∆

∆
/ X ×Y X
π1
/
id1×∆23

X
X
X ×Y X
π2
o
∆12×id3
/ X ×Y X ×Y X
Using standard identities for composition and base change, we calculate
(id ⊗c) ◦(u ⊗id)
=
π1∗(id1 × ∆23)!(∆12 × id3)∗π!
2
≃
π1∗∆∗∆!π!
2
≃
idD(X).
□
If X1 →Y is safe as in the previous theorem, and X2 →Y is arbitrary, then the integral
transform construction gives linear functors
D(X1 ×Y X2)
/ FunL
D(Y )(D(X1), D(X2))
M ✤
/ π2∗(π!
1(−) ⊗M)
Its evident compatibility with the self-duality of Theorem 5.2 and the identiﬁcation of Theorem 5.1
immediately implies the following.
Corollary 5.3. Let X1, X2 be stacks, Y a scheme, X1 →Y a safe morphism, and X2 →Y an
arbitrary morphism. Then the natural maps are equivalences
D(X1) ⊗D(Y ) D(X2)
∼
/ D(X1 ×Y X2)
∼
/ FunL
D(Y )(D(X1), D(X2))
factoring the self-duality of D(X1) over D(Y ).

---
doc_id: arxiv-math-0104104v3
doc_title: "Geometry of Four-vector Fields on Quaternionic Flag Manifolds"
section_id: sec-009-0-id
section_title: "Id"
section_number: 0
pages: 8-10
source_pdf: 0104104v3.pdf
source_sha256: e2154399f783aa9b
doc_brief: "Geometry of Four-vector Fields on Quaternionic Flag Manifolds — The purpose of this paper is to describe certain natural 4-ve ctor ﬁelds on quaternionic ﬂag manifolds, which geometrically determ ine"
---
κ = Λ L− ΛR.
Unlike the Sp(2) case, when n> 2, one can readily check that κ will not be a
quatrisson structure on Sp(n) by making use of the Leibniz rule and commutator
relations similar to those as above and noting that there will be some t erms that
will not cancel. However, we still have:
Proposition 5.1 The 4-vector ﬁeld κ descends to Σ\Sp(n), inducing a Σ -
invariant quatrisson structure, ℵ, called the Bruhat quatrisson structure .
Proof. Forκ to descend and be invariant we need to show that both the left
and right translations by elements of the Spheroid leave κ invariant, meaning
that the adjoint action by the Spheroid on Λ is trivial. This can be chec ked
similarly to the n = 2 case of Proposition 4.1. One can also directly check that
[ℵ,ℵ] = 0 on Σ \Sp(n), which will also follow from Proposition 5.6. ✷
We recall:
Deﬁnition 5.2 Let H be a Lie group equipped with a multiplicative 4-vector
ﬁeld µ, which acts on a quatrisson manifold (P,ξ ):
β :H×P→P.
We say that H acts multiplicatively if, denoting the corresponding translation
maps:
βh :P→P β y :H→P
y↦→h·y h ↦→h·y
we have:
ξ(h·x) = βh∗ξ(x) +βx∗µ(h).
We sometimes say that the actions is multiplicative with res pect to the direct
sum 4-vector ﬁeld µ⊕ξ on H×P .
and notice the following fact (cf. [11], [8]):
Quatrisson structures and H-ﬂags 9
Lemma 5.3 The 4-vector ﬁeld κ on Sp(n) is multiplicative.
Proposition 5.4 Letℵ be the Bruhat quatrisson structure on Σ\Sp(n). The
action map:
Sp(n)× Σ\Sp(n)→ Σ\Sp(n) : (g,h )↦→g·h
is multiplicative with respect to the four-vector ﬁeld κ⊕ℵ on Sp(n)×(Σ\Sp(n)).
Proof. Straightforward. ✷
We will also make use of the following embeddings:
fr,r +1 : Sp(2)֒→Sp(n)
A ↦→ Ar,r +1
where 1≤r<n and for A =
( a b
c d
)
the matrix Ar,r +1 is given by:




Id 0
a b
c d
0 Id




←rth row
Lemma 5.5 The embeddings fr,r +1 : Sp(2)֒→Sp(n) respect the multiplicative
4-vector ﬁelds κ.
Proof. Straightforward. ✷
Proposition 5.6 Every tetraplectic leaf L of Sp(n) lies entirely in some Zw.
If Lw is a tetraplectic leaf containing the permutation matrix Pw corresponding
to some w∈ Sn, and we write w = ∏ m
i=1τi as a minimal product of adjacent
transpositions, we have a tetraplectomorphism:
Fw : Lτ1×... ×Lτm → Lw
(l1,...,l m) ↦→ l1l2...l m
Moreover, for σ∈ Σ , the tetraplectic leaf through σPw equalsσLw.
Proof. (cf. [12], [15].) Immediately follows from the discussion above. ✷
More explicitly, one can follow [12] to identify Lw with the Vw - orbit of Pw,
and in the next section, we will deﬁne and exploit the analogues of the dressing
action [14] to get clearer picture of the tetraplectic leaves. In any case, we have
the following:
Theorem 5.7 The tetraplectic leaf decomposition of the quaternionic ﬂa g man-
ifold Fn≃B\ GLn(H) arising from the Bruhat quatrisson structure coincides
with the Bruhat cell decomposition.
Proof. The important point is that any tetraplectic leaf in Sp(n) under the
quotient map Sp(n)→ Σ\Sp(n) maps tetraplectomorphically onto a Bruhat
cell as follows from the results in this section. ✷

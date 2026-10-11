---
doc_id: arxiv-2401.00636v2
doc_title: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS"
section_id: sec-017-48-pseudo-pencils
section_title: "Pseudo-pencils"
section_number: 4.8
pages: 17-18
source_pdf: 2401.00636v2.pdf
source_sha256: 35e372d04cedf234
toc_source: outline
doc_brief: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS — We introduce a new notion of a periodic pencil of ﬂat connections on a smooth algebraic variety X."
---
(i.e., linearity in s) is satisﬁed in many interesting examples listed in the next section, it is still
quite restrictive and unfortunately rules out many other important examples, for instance
most motivic families. On the other hand, we have used this condition only in one place -
to argue that the monodromy representation of ∇(s) is exponentially bounded. It turns out
that the pencil condition can be relaxed to include many more examples while retaining this
property. Namely, this is accomplished by the following notion of a pseudo-pencil, which
we ﬁrst deﬁne in the 1-parameter case.
Deﬁnition 4.29. Let ∇(s) be a 1-parameter polynomial family of ﬂat connections on a
smooth irreducible variety X. We say that ∇(s) is a pseudo-pencil if after a gauge trans-
formation over k(s)(X), ∇(s) takes the form d −sB(s) where B is regular at s = ∞.
It is clear that any pencil of ﬂat connections is a pseudo-pencil.
On the other hand,
pseudo-pencils are much more general. For instance, using the results of Mochizuki ([Mo]),
one can prove the following proposition (see e.g. [Sa], Theorem 2 and Example 3):
Proposition 4.30. 3 Let π : Y →X be a smooth morphism between smooth complex varieties
of relative dimension m and Φ a nonvanishing regular function on Y such that the map
(π, Φ) : Y →X × Gm is proper. Suppose that the critical points of Φ on a generic ﬁber
π−1(x) are isolated. Then the motivic family Hm(π∗L(Φ, s)) (over some open subset of X)
is a pseudo-pencil.
There are also other similar situations where one can conclude that Hm(π∗L(Φ, s)) is a
pseudopencil, see e.g. [Sa], Example 4.
Yet it is clear that the monodromy of any pseudo-pencil (for k = C) is exponentially
bounded (indeed, we may compute the monodromy in the gauge where ∇(s) ∼d −sB(s),
where it is obviously exponentially bounded, but this condition does not depend on the
gauge).
This can be generalized to the multiparameter case as follows.
Deﬁnition 4.31. Let ∇(s), s = (s1, ..., sn) be an n-parameter polynomial family of ﬂat
connections on X. We say that ∇(s) is a pseudo-pencil if it is so with respect to each si
when the other coordinates sj, j̸ = i are ﬁxed.
Again, it is easy to see that any pencil is a pseudo-pencil, but pseudo-pencils are much
more general. Yet the above results can be generalized to them.
To make this generalization, note that, as shown by the proof of Lemma 2.3, the exponen-
tial boundedness assumption in this Lemma and hence in Theorem 2.5 can be relaxed to the
assumption of coordinatewise exponential boundedness: we say that f : Cn →V is
coordinatewise exponentially bounded for all i, f(s) is exponentially bounded with respect
to si when sj for j̸ = i are ﬁxed.
3We thank V. Vologodsky for explanations regarding this proposition
18
PAVEL ETINGOF AND ALEXANDER VARCHENKO
It remains to note that the monodromy of any pseudo-pencil is coordinatewise exponen-
tially bounded, which enables the desired generalizations.
Finally, we remark that this discussion extends straightforwardly to the case when ∇(s)
is a rational (rather than polynomial) function of s.

---
doc_id: arxiv-math-0405508v1
doc_title: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B"
section_id: sec-018-16-gecklambropoulou
section_title: "Geck–Lambropoulou"
section_number: 16
pages: 16-18
source_pdf: 0405508v1.pdf
source_sha256: ef2e41cf67f3a411
doc_brief: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B — 30 sections: Introductory remarks on knots, bra; Geck–Lambropoulou; Geck–Lambropoulou"
---
Note that S2, S 3 ∈ H(≤ N − 1) so that we can use our inductive hypotheses
in the evaluation of τ on these elements. Let us ﬁrst consider S2. At ﬁrst, we
note that gn · · · gi+1 commutes with t′
i−1, 0. So we obtain that
τ(S2) = τ(ht′
i−1, 0(gn · · ·gi+1gig−1
i+1 · · · g−1
n )dn+2 · · · dn+m)
= τ(ht′
i−1, 0(g−1
i · · · g−1
n−1gngn−1 · · · gi)dn+2 · · · dn+m).
Now gn−1 · · · gi commutes with all terms to the right of it, by Lemma 2.3(a).
Hence we conclude that
τ(S2) = τ((gn−1 · · · gi)ht′
i−1, 0(g−1
i · · · g−1
n−1)gndn+2 · · · dn+m).
We write the argument of τ as h′gndn+2 · · · dn+m with h′ ∈ Hn. Since this
element lies in H(≤ N − 1) we can use induction to deduce that
τ(S2) = τ(h′gndn+2 · · · dn+m) = zτ(h′dn+2 · · · dn+m).
Now we observe that h′ is a conjugate of ht′
i−1, 0 and the conjugating element
gn−1 · · · gi commutes with dn+2 · · · dn+m, again using Lemma 2.3(a). Thus, we
ﬁnally compute that
τ(S2) = zτ(ht′
i−1, 0dn+2 · · · dn+m).
Now we follow the same procedure with S3 and ﬁnd that
τ(S3) = τ(h(gn · · · gi+1gig−1
i+1 · · ·g−1
n )t′
i−1, 0dn+2 · · · dn+m)
= τ(h(g−1
i · · · g−1
n−1gngn−1 · · · gi)t′
i−1, 0dn+2 · · · dn+m).
Now we would like to interchange t′
i−1, 0 and dn+2 · · · dn+m but this is not
necessarily possible on the algebra level. However, it still works modu lo
the kernel of τ, as the following argument shows. We write t′
i−1, 0 = x−1tx
where x = g±1
1 · · · g±1
i−1. By Lemma 2.3(a), the element x will commute with
dn+2 · · · dn+m. The next factor, t, only commutes with dn+2 · · · dn+m up to
(possibly) changing some inverses. Thus, the term on the right han d side of
the above equality is equal to
τ(txh(g−1
i · · · g−1
n−1gngn−1 · · · gi)x−1d′
n+2 · · · d′
n+m),
for some d′
n+2 ∈ D ′
n+2, 0, . . . , d ′
n+m ∈ D ′
n+m, 0. Now we can apply our inductive
hypothesis to conclude that this equals
τ(txh(g−1
i · · · g−1
n−1gngn−1 · · · gi)x−1dn+2 · · · dn+m).
Markov traces and knot invariants 17
Now, again by Lemma 2.3(a), the element x−1 will commute with the terms
to the right of it. So, ﬁnally, we obtain that
τ(S3) = τ(t′
i−1, 0h(g−1
i · · ·g−1
n−1gngn−1 · · · gi)dn+2 · · ·dn+m).
Once more, we use Lemma 2.3(a) to conclude that gn−1 · · · gi commutes with
all terms to the right of it. So we arrive at the equality
τ(S3) = τ((gn−1 · · · gi)t′
i−1, 0h(g−1
i · · · g−1
n−1)gndn+2 · · · dn+m).
In this situation, we can argue similarly as in the evaluation of τ(S2). This
evaluation will result in an analogous expression as before, but with t he terms
h and t′
i−1, 0 interchanged. Thus, we conclude that
τ(S3) = zτ(t′
i−1, 0hdn+2 · · ·dn+m).
Arguing as above, we see that t′
i−1, 0 and dn+2 · · · dn+m can be interchanged
modulo the kernel of τ. So, eventually, we ﬁnd that τ(S2) = τ(S3) and,
hence, that τ(hTn+1,i dn+2 · · · dn+m) = τ(hTn+1,i −1dn+2 · · · dn+m), as required.
The proof of the assertion of Step 1 is now completed by repeating t he whole
process with Tn+1,i −1 and so on, until all inverses are ﬁxed.
Step 2. Now we consider the case where h = d∗
1 . . . d ∗
n, for some d∗
i ∈ D ′
i, 0.
As before, let di be the element of D′
i corresponding to d∗
i where all inverses (if
any) are in the right position. Using Step 1, we ﬁrst see that τ(d∗
1 · · · d∗
n+m) =
τ(d1 · · ·dn+m). Now, we will prove that
τ(d∗
1 · · · d∗
n+m) = zayb,
where a = a(d1 · · · dn+m) and b = b(d1 · · · dn+m). (Note that, in the deﬁnition
of a, b in Lemma 4.2(b), it does not matter whether we take d∗
i or di.) As ex-
plained in (2.4), (3.3), the element d1 · · · dn+m can be regarded as a product of
positive and negative blocks. If this element is equal to gC for some conjugacy
class C then we are done by the deﬁning equation for τ. If this is not the case,
then some positive block is followed by a negative block or some negativ e block
is followed by a strictly shorter negative block. We can then use Lemm a 2.5
to conjugate our element to d′
1 · · · d′
n+m ∈ Hn(≤ N − 1) with d′
i ∈ D ′
i, 0 and
with the same signed block structure as before, that is, the values of a and b
haven’t changed after this conjugation. Thus, we conclude that
τ(d∗
1 · · · d∗
n+m) = τ(d1 · · · dn+m) = τ(d′
1 · · · d′
n+m) = zayb,
where the last equality is by induction on N. Our claim is proved.

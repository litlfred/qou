---
doc_id: arxiv-math-0108011v1
doc_title: "The Homfly polynomial of the decorated Hopf link"
section_id: sec-005-15-the-hopf-link
section_title: "The Hopf link"
section_number: 1.5
pages: 6-7
source_pdf: 0108011v1.pdf
source_sha256: e4af4b5d3c5ff6cd
toc_source: inferred
doc_brief: "The Homfly polynomial of the decorated Hopf link — The main goal is to ﬁnd the Homﬂy polynomial of a link formed by decorating each component of the Hopf link with the closure of a directly oriented"
---
The Hopf link
We consider the Hopf link with linking number 1 as shown here.
Let X and Y be any elements of the skein C of the annulus. We write
⟨X, Y ⟩for the framed Homﬂy polynomial of the Hopf link with decorations
X and Y on its components, giving
⟨X, Y ⟩= χ





X
Y




=
*
X
Y
+
= ⟨ϕ(Y )(X)⟩.
Clearly ⟨Y, X⟩= ⟨X, Y ⟩. Our aim is to determine ⟨X, Y ⟩for any X, Y ∈C+.
Since C+ is spanned by {Qλ} it is enough to ﬁnd ⟨Qλ, Qµ⟩for all λ, µ. We
make use of the homomorphism tλ of the previous section.
6
Lemma 1.1 We can write
tλ(Y ) = ⟨Qλ, Y ⟩/ ⟨Qλ⟩.
Proof :
Suppose that λ has n cells.
Then ψn(Y )eλ = tλ(Y )eλ.
Apply
the closure map ˆ : Hn →C to both sides.
The left-hand side becomes
ϕ(Y )(ˆeλ). Now apply the evaluation map ⟨⟩to both sides, using the fact
that ˆeλ = αλQλ, to get
⟨αλQλ, Y ⟩= tλ(Y ) ⟨αλQλ⟩.
This gives the expression for tλ(Y ), since αλ̸ = 0.
✷
Corollary 1.2 For any elements X and Y of C and any Young diagram λ
we have
⟨Qλ, X⟩⟨Qλ, Y ⟩= ⟨Qλ⟩⟨Qλ, XY ⟩.
Proof :
Use the formula of lemma 1.1 and the fact that tλ is a homomor-
phism.
✷
Since any Y ∈C+ can be written as a polynomial in the skein elements
{ci} we only need to know the values of ⟨Qλ, ci⟩for integers i ≥0 in order
to compute ⟨Qλ, Y ⟩for all Y ∈C+. In particular we can then compute all
invariants ⟨Qλ, Qµ⟩. Hence, it is useful to deﬁne a formal power series
Eλ(t) =
X
i≥0
tλ(ci)ti =
1
⟨Qλ⟩
X
i≥0
⟨Qλ, ci⟩ti
(1)
for any Young diagram λ, which we study further in the next section.
2

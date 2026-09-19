---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-015-the-chern-character
section_title: "The Chern character"
section_number: null
pages: 21-22
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
In this section we deﬁne the Chern character map ch : K0(X)→ HH0(X). We
discuss the relationship between our construction and the o ne of Markar-
ian [10, Deﬁnition 2]. Then we show that the Chern character m aps the Euler
pairing to the Mukai pairing: we call this the Semi-Hirzebru ch-Riemann-
Roch Theorem.
21
6.1 Deﬁnition of the Chern character.
Suppose X is a space, and E is an object in D(X). Consider E as an object
of D(pt × X), i.e., as a kernel pt→ X, so there is an induced linear map
E∗ : HH•(pt)→ HH•(X).
Now, because the Serre functor on a point is trivial, HH0(pt) is canonically
identiﬁable with Hompt×pt(Opt, Opt) so there is a distinguished class 1 ∈
HH0(pt) corresponding to the identity map. Deﬁne the Chern characte r of
E as
ch(E ) := E∗(1) ∈ HH0(X).
Graphically this has the following description:
ch(E ) := E .
Naturality of push-forward leads to the next theorem.
Theorem 10. If X and Y are spaces and Φ : X→ Y is a kernel then the
diagram below commutes.
D(X)
Φ ◦− ✲ D(Y)
HH0(X)
ch
❄ Φ ∗✲ HH0(Y).
ch
❄
Proof. Let E be an object of D(X). We will regard it either as an object in
D(X), or as a kernel pt→ X, and similarly we will regard Φ ◦ E either as an
object in D(Y) or as a kernel pt→ Y. By Theorem 6 we have
Φ∗ ch(E ) = Φ∗ (E∗(1)) = ( Φ ◦ E )∗1 = ch(Φ ◦ E ).

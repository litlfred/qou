---
doc_id: arxiv-math-0209324v1
doc_title: "CYCLOTOMIC COMPLETIONS OF POL YNOMIAL RINGS KAZUO HABIRO"
section_id: sec-007-32-injectivity-of-the-homomorphism-ρr
section_title: "Injectivity of the homomorphism ρR"
section_number: 3.2
pages: 7-8
source_pdf: 0209324v1.pdf
source_sha256: ae2ea5024a0a45e8
doc_brief: "CYCLOTOMIC COMPLETIONS OF POLYNOMIAL RINGS KAZUO HABIRO — The main object of study in this paper is the completion Z[q]N = lim←− n Z[q]/ ((1− q)(1− q2)···(1− qn)) of the polynomial ring Z[q], which"
---
M,M ′. Let R be a ring, I⊂ R
an ideal, and f, g ∈M R. Let
√
I denote the radical of I. We write f I⇒R g,
or simply f I⇒ g, if f∈
√
(g) + I[q], i.e., if f m∈ (g) + I[q] for some m≥ 0.
For f, g ∈M R, we write f⇒R g, or simply f⇒ g, if we have f I⇒R g for
some ideal I⊂ R with ⋂
j≥0 I j = (0). Then ⇒R deﬁnes a relation on the
setMR. Obviously, g|f implies f⇒ g. Note also that if f⇒ g, f|f ′, and
g′|g, then f ′⇒ g′.
Proposition 3.2. Let R be a ring, and f, g ∈M R with f⇒R g. Then the
homomorphism ρR
(f g), (f ) : R[q](f g)→ R[q](f ) is injective.
Proof. We ﬁrst show that if f I⇒ g and R is I-adically complete, then ρR
(f g), (f )
is an isomorphism. Since R≃ RI and f is monic, we have
R[q](f )≃ RI[q](f ) = lim←−i
(lim←−j
R/I j)[q]/ (f i)
≃ lim
←−i
(lim←−j
R[q]/ ((f i) + I j[q]))≃ R[q](f )+I[q].
Similarly, R[q](f g)≃ R[q](f g)+I[q]. Since f I⇒ g, we have (( f ) + I[q])m⊂
(f m) + I[q]⊂ (f g) + I[q] for some m≥ 1, while we obviously have ( f g) +
I[q]⊂ (f ) + I[q]. Hence the (( f ) + I[q])-adic topology and the (( f g) +
I[q])-adic topology of R[q] are the same. Hence ρR
(f g)+I[q], (f )+I[q], which is
identiﬁed with ρR
(f g), (f ), is an isomorphism.
Now consider the general case, where we have f I⇒R g and R is I-adically
separated. We have a commutative diagram
R[q](f g) ρR
(f g), (f )
−−−−−→R[q](f )


↓


↓
RI[q](f g) −−−−−→
ρRI
(f g), (f )
RI [q](f )

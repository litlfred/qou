---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-004-2-preliminaries-and-a-stochastic-construction
section_title: "Preliminaries and a stochastic construction"
section_number: 2
pages: 6-7
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
---
Throughout this section, we ﬁx a probability measure ν on Cn and a Lipschitz test function
ϕ : Cn → R.
2.1 Some preliminary deﬁnitions
For a vector w ∈ Rn, deﬁne the tilt of the measure ν as
dτwν(x)
dν(x) := Zν(w)−1e⟨w,x⟩
where
Zν(w) :=
∫
Cn
e⟨w,x⟩dν.
Also deﬁne the functions
aν(w) :=
∫
Cn
xdτwν(x), A ν(w) :=
∫
Cn
(x − aν(w))⊗2 dτwν(x) = Cov( τwν).
A well-known calculation gives,
aν(w) = ∇L[ν](w), A ν(w) = ∇2L[ν](w) (8)
(this is the fact that the Log-Laplace transform is the cumul ant-generating function). Thus, if ν
is β -log-concave, we have
∇aν(w) = ∇2L[ν](w) ≼ β In. (9)
6

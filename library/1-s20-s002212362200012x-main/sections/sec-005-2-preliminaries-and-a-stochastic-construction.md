---
doc_id: 1-s20-s002212362200012x-main
doc_title: "www.elsevier.com/locate/jfa"
section_id: sec-005-2-preliminaries-and-a-stochastic-construction
section_title: "Preliminaries and a stochastic construction"
section_number: 2
pages: 8-9
source_pdf: 1-s2.0-S002212362200012X-main.pdf
source_sha256: 6fc7d28c8d40bf42
doc_brief: "www.elsevier.com/locate/jfa — 13 sections: Log concavity and concentration of; Introduction; A lower bound on the entropy"
---
Throughout this section, we ﬁx a probability measure ν on Cn and a Lipschitz test 
function ϕ : Cn → R.
2.1. Some preliminary deﬁnitions
For a vector w ∈ Rn, deﬁne the tilt of the measure ν as
dτwν(x)
dν(x) := Zν(w)−1e⟨w,x⟩
where
Zν(w): =
∫
Cn
e⟨w,x⟩dν.
In other words, τwν is the measure obtained by adding an external ﬁeld, w, to the measure 
ν. Also deﬁne the functions
aν(w): =
∫
Cn
xdτwν(x),A ν(w): =
∫
Cn
(x − aν(w))⊗2 dτwν(x)=C o v (τwν),
the center of mass and the covariance matrix of the tilt τwν.
A well-known calculation gives,
aν(w)= ∇L[ν](w),A ν(w)= ∇2L[ν](w)( 8 )
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392 9
(this is the fact that the Log-Laplace transform is the cumulant-generating function). 
Thus, if ν is β-log-concave, we have
∇aν(w)= ∇2L[ν](w) ≼ βIn. (9)

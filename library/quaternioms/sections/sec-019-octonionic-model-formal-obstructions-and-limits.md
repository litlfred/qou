---
doc_id: quaternioms
doc_title: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations"
section_id: sec-019-octonionic-model-formal-obstructions-and-limits
section_title: "Octonionic Model: Formal Obstructions and Limits"
section_number: null
pages: 17-18
source_pdf: quaternioms.pdf
source_sha256: becedcbc858611dd
toc_source: outline
doc_brief: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations — 45 sections: Front matter; Introduction; Extended Related Work"
---
We now switch to O, where the loss of associativity reverses the previous narrative.
The next results make precise how ordering and parenthesization cease to be benign choices.
In contrast to the measurement-only scheme of Freedman, Shokrian-Zini and Wang [9],
which already realizes universal quantum computation using octonionic equiangular pro-
jections, the results in this subsection are, to the best of our knowledge, new: they identify
structural obstructions to a gate-based O-model and organize possible workarounds into
the mitigation strategies (M1)–(M4).
Lemma 2 (Intrinsic path dependence via associators). For time-dependent H(t) ∈O, the prop-
agator U(t) = P exp

−i
¯h
R t
0 H(τ) dτ

admits a Magnus-like expansion with explicit associator
contributions. If the sampled triples have [x, y, z]̸ = 0, different control slicings/time orderings yield
distinct U(t). Proof idea: Appendix B. Signiﬁcance: Control order matters intrinsically outside
associative sectors.
This path dependence already disrupts standard conservation arguments, signaling
deeper structural failures.
Proposition 3 (Energy-balance breakdown outside associative sectors). For time-independent
H ∈O, the usual identity d
dt⟨ψ(t), Hψ(t)⟩= 0 need not hold when adjoints/inner products cannot
be deﬁned associatively on the full space. Proof idea: Appendix B. Signiﬁcance: Even basic
conservation proofs rely on associativity.
The culmination is a failure of canonical multipartite composition, which contrasts
sharply with Theorem 1.
Theorem 3 (No canonical multipartite tensor product in O). For right O-modules HA, HB, HC,
there is no parenthesization-independent canonical isomorphism (HA ⊗HB) ⊗HC ∼= HA ⊗
(HB ⊗HC) unless one restricts to an associative subalgebra. Proof idea: Appendix B. Signiﬁ-
cance: Large-scale circuit composition is ill-deﬁned in the fully octonionic setting.
Accordingly, wiring rules that were automatic over H become conditional on explicit
associative scaffolding.
Corollary 2 (No native, parenthesis-free wiring rule). Absent conﬁnement to associative
subalgebras, there is no parenthesis-free, platform-independent notion of “tensoring subsystems”
over O. Consequence: Universal, scalable octonionic circuit families require associative scaffolding.

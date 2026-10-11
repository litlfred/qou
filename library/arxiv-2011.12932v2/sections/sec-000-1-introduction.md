---
doc_id: arxiv-2011.12932v2
doc_title: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2011.12932v2.pdf
source_sha256: 23709542c5652a29
doc_brief: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY — Vladimir Turaev discovered in the early years of quantum topol- ogythatthenotionofmodularcategorywasanappropriatestructureforbuild- ing"
text_source: latex
latex_prose_ratio: 0.702
latex_coverage_ratio: 1.0
---
After the work of Vaughan Jones \cite{J85} and Edward Witten \cite{W88,W89}, Vladimir Turaev played a key role in the foundation of quantum topology. Together with Nikolai Reshetikhin \cite{RT91}, they were the first to obtain a mathematically rigorous construction of Witten's invariants of 3-dimensional manifolds. Turaev showed that the relevant algebraic structure underlying their approach was that of a \textit{modular category}, a notion he himself identified and introduced for this purpose \cite{T94}. Starting from a modular category, one can build a Topological Quantum Field Theory (TQFT for short) and, in particular, invariants of links in 3-manifolds, and representations of mapping class groups of surfaces. The famous Witten--Reshetikhin--Turaev invariants can be derived from a family of modular categories arising as semisimple quotients of representation categories of the restricted quantum group of $\fsl_2$ at roots of unity. Around the same time, equivalent modular categories were obtained from the Kauffman bracket skein theory \cite{BHMV95}. On the one hand, the quantum group construction generalizes to other families of modular categories, corresponding to arbitrary simple Lie algebras $\frakg$. On the other hand, the skein construction produces families of modular categories associated with the structure of Hecke algebras of type A \cite{B98} and of Birman--Murakami--Wenzl algebras of type B,C, and D \cite{BB00}. The abundance of examples shows the relevance of Turaev's definition. However, in all these instances, only simple representations, which cover just a small part of the corresponding representation theory, are used.

Already within the first decade since the birth of quantum topology, constructions of invariants and mapping class group representations beyond the scope of semisimple modular categories emerged, thanks to the work of Mark Hennings \cite{H96} and Volodymyr Lyubashenko \cite{L94}. More recently, the algebraic theory of \textit{modified traces}, whose germs can be found in an early collaboration of Nathan Geer and Bertrand Patureau with Turaev \cite{GPT07}, served as a huge propeller for a new wave of non-semisimple quantum constructions. Through this technology, TQFTs and HQFTs\footnote{Acronym for Homotopy Quantum Field Theory, a notion introduced by Turaev.} were built for the first time out of non necessarily semisimple generalizations of modular categories. Our purpose here is to review the original construction, and to relate it to the latest achievements in the field.


\section{Historical overview}\label{S:history}


\subsection{Definition of TQFT}

A popular axiomatization of the notion of TQFT was proposed by Micheal Atiyah \cite{A88}, who was inspired by a similar definition of Graeme Segal \cite{S88} for the concept of a Conformal Field Theory (CFT for short). Paraphrasing Atiyah, a TQFT in dimension 3 can be defined as a symmetric monoidal functor from a category of 3-dimensional cobordisms to the category of vector spaces. In this definition, cobordism categories are naturally equipped with the symmetric monoidal structure induced by disjoint union. In other words, a TQFT $V$ associates with every closed oriented surface $\Sigma$ a vector space $V(\Sigma)$ called the \textit{state space} of $\Sigma$, and it associates with every cobordism $M$ from $\Sigma$ to $\Sigma'$ a linear map $V(M) : V(\Sigma) \to V(\Sigma')$. At the same time, a TQFT translates the topological operations of gluing and disjoint union into the algebraic operations of composition and tensor product, respectively. The use of an indefinite article in this definition, when we talk about \textit{a} category of cobordisms, as opposed to \textit{the} category of cobordisms, is due to the fact that cobordisms are typically allowed to carry additional structure, which may vary according to the different constructions we might want to consider. All the resulting notions are gathered under the umbrella term ``TQFT''.

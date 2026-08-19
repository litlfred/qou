---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-011-26-categorical-aspects
section_title: "Categorical aspects"
section_number: 2.6
pages: 23-24
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
ules over the q-Weyl algebra and give a proof of Lemma 1.3.
To begin with, a gauge transformation X = P −1Y changes ( 3) to σY = BY where
B = σP AP −1, changes a fundamental solution U of ( 3) to P −1U, and consequently changes
Ω γ to ( P |κγ)−1Ω P . Hence, if P ∈ GLr( /C9 (t, q)), then modularity is a property of the gauge
equivalence class of a linear q-diﬀerence equation, i.e., a property of a q-holonomic module,
independent of a choice of a cyclic vector. This concludes part (a) o f Lemma 1.3.
For part (b), we use the convariant function M ↦→Sol(M) := Ker( σ, F ⊗
/C9 (t,q) M) where
F denotes a universal q-diﬀerence ﬁeld; see for example [ 61, Sec.2.2] for the case of modules
over the Weyl algebra and [ 38] for its extension for the q-Weyl algebra W. This functor by
deﬁnition satisﬁes [ 61, Lem.2.16]
Sol(M) ∼= {y ∈ F r | σy = Ay} (105)
where A is the matrix obtained by a choice of a cyclic vector of M. Moreover, if
0 → M ′ → M → M ′′ → 0
is a short exact sequence of ﬁnitely generated W-modules, then
0 → Sol(M ′) → Sol(M) → Sol(M ′′) → 0 (106)
is a short exact sequence of vector spaces over /C9 (t, q); see [ 61, Sec.2.2]. In addition, M
has a canonical ﬁltration at t = 0 (and also at t = ∞) independent of the choice of cyclic
vector [ 60] compatible with submodules and quotient modules. Converting the a bove into
matrices, it follows that the ﬁltration preserving fundamental mat rices U, U ′ and U ′′ of M,
M ′ and M ′′ (and likewise, V , V ′ and V ′′) and their corresponding cocycles are related by
U =
(
U ′ ∗
0 U ′′
)
, Ω U =
(
Ω U ′ ∗
0 Ω U ′′
)
. (107)
It follows that if Ω U extends to the cut plane, so does Ω U ′ and Ω U ′′, concluding part (b). It
is unlikely that the converse to part (b) holds, namely if extensions o f modular q-holonomic
modules are q-holonomic, but not necessarily modular.
For part (c), observe that if U is a fundamental matrix for M, then U ∧(t, q) := U(t, q−1)
and U ∨ = (U −1)t are fundamental matrices for M ∧ and M ∨. It follows that if Ω is a cocycle
24 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
of M then Ω ∧(z, τ ) := Ω( z, −τ ) and Ω ∨ = (Ω −1)t are cocycles for M ∧ and M ∨. Part (c)
follows. This concludes the proof of Lemma
1.3. □
3. Heine’s q-hypergeometric functions
This section is devoted to the proof of Theorem 1.4.

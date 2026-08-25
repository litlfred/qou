---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-011-26-categorical-aspects
section_title: "Categorical aspects"
section_number: 2.6
pages: 23-24
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
ules over the q-Weyl algebra and give a proof of Lemma 1.3.
To begin with, a gauge transformation X = P−1Y changes (3) to σY = BY where
B =σPAP−1, changes a fundamental solution U of (3) to P−1U, and consequently changes
Ωγ to (P|κγ)−1ΩP . Hence, if P∈ GLr(Q (t,q )), then modularity is a property of the gauge
equivalence class of a linear q-diﬀerence equation, i.e., a property of a q-holonomic module,
independent of a choice of a cyclic vector. This concludes part (a) of Lemma 1.3.
For part (b), we use the convariant function M↦→ Sol(M) := Ker(σ,F⊗ Q (t,q)M) where
F denotes a universal q-diﬀerence ﬁeld; see for example [67, Sec.2.2] for the case of modules
over the Weyl algebra and [42] for its extension for the q-Weyl algebraW. This functor by
deﬁnition satisﬁes [67, Lem.2.16]
Sol(M)∼={y∈F r| σy =Ay} (108)
where A is the matrix obtained by a choice of a cyclic vector of M. Moreover, if
0→M′→M→M′′→ 0
is a short exact sequence of ﬁnitely generated W-modules, then
0→ Sol(M′)→ Sol(M)→ Sol(M′′)→ 0 (109)
is a short exact sequence of vector spaces over Q (t,q ); see [67, Sec.2.2]. In addition, M
has a canonical ﬁltration at t = 0 (and also at t =∞) independent of the choice of cyclic
24 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
vector [66] compatible with submodules and quotient modules. Converting the above into
matrices, it follows that the ﬁltration preserving fundamental matrices U, U′ and U′′ of M,
M′ and M′′ (and likewise, V , V′ and V′′) and their corresponding cocycles are related by
U =
(
U′ ∗
0 U′′
)
, ΩU =
(
ΩU′ ∗
0 Ω U′′
)
. (110)
It follows that if ΩU extends to the cut plane, so does Ω U′ and ΩU′′, concluding part (b). It
is unlikely that the converse to part (b) holds, namely if extensions of modular q-holonomic
modules are q-holonomic, but not necessarily modular.
For part (c), observe that if U is a fundamental matrix for M, then U∧(t,q ) := U(t,q−1)
andU∨ = (U−1)t are fundamental matrices for M∧ andM∨. It follows that if Ω is a cocycle
of M then Ω∧(z,τ ) := Ω(z,−τ) and Ω∨ = (Ω−1)t are cocycles for M∧ and M∨. Part (c)
follows. This concludes the proof of Lemma 1.3. □
3. Heine’s q-hypergeometric functions
This section is devoted to the proof of Theorem 1.4.

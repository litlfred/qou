---
doc_id: arxiv-0801.3233v4
doc_title: "Contemporary Mathematics Twisted Deformation Quantization of Algebraic Varieties (Survey) Amnon Yekutieli"
section_id: sec-001-1-some-background-on-deformation-quantization
section_title: "Some background on Deformation Quantization"
section_number: 1
pages: 2-3
source_pdf: 0801.3233v4.pdf
source_sha256: d98f9d4a9ecb4c5e
doc_brief: "Contemporary Mathematics Twisted Deformation Quantization of Algebraic Varieties (Survey) Amnon Yekutieli — Let X be a smooth algebraic variety over a ﬁeld of characteristic 0."
---
Throughout K is a ﬁeld of characteristic0.
Let C be a commutative K-algebra. Recall that a Poisson bracketon C is a
K-bilinear function
{−,−}:C×C→C
which makesC into a Lie algebra, and is a biderivation (i.e. a derivation in each
argument). The pair
(
C,{−,−}
{
is called a Poisson algebra.
Poisson algebras arise in several ways, e.g. classical Hamiltonian mechanics, or
Lie theory.
Let K[[ℏ]] be the ring of formal power series in the variableℏ. And letC[[ℏ]]
be the set of formal power series with coeﬃcients inC, which we view only as a
K[[ℏ]]-module. A star producton C[[ℏ]] is a K[[ℏ]]-bilinear function
⋆:C[[ℏ]]×C[[ℏ]]→C[[ℏ]]
which makesC[[ℏ]] into an associative K[[ℏ]]-algebra, with unit 1∈C, and such
that
f ⋆g≡fg mod ℏ
for anyg,f ∈C.
Note that the star product⋆can be expanded into a power series as follows:
there is a sequence{ωj}j≥1 of K-bilinear functionsωj :C×C→C, such that
(1.1) f ⋆g:=fg +
∞∑
j=1
ωj(f,g )ℏj
forf,g ∈C. The conditions that⋆is associative and unital place certain constraints
on the sequence{ωj}j≥1.
TWISTED DEFORMATION QUANTIZATION 3
Example 1.2. Suppose ⋆is a star product onC[[ℏ]]. Given f,g ∈C, we know
that
f ⋆g−g⋆f≡0 mod ℏ.
Hence there is a unique element{f,g}⋆∈C such that
1
2ℏ
(
f ⋆g−g⋆f
{
≡{f,g}⋆mod ℏ.
It is quite easy to show that{−,−}⋆is a Poisson bracket onC. We call it theﬁrst
order bracketof ⋆.
Deformation quantization seeks to reverse Example 1.2.
Deﬁnition 1.3.Given a Poisson bracket{−,−}on the algebraC, adeformation
quantization of{−,−}is a star product⋆on C[[ℏ]] whose ﬁrst order bracket is
{−,−}.
In physicsℏ is thePlanck constant. For a quantum phenomenon depending on
ℏ, the limit asℏ→0 is thought of the as the classical limit of this phenomenon.
The original idea by the physicists Flato et. al. ([BFFLS], 1978) was that de-
formation quantization should model the transition from classical Hamiltonian me-
chanics to quantum mechanics. Special cases (like the Moyal product) were known.
The problem arose:does any Poisson bracket admit a deformation quantization?
For a symplectic manifoldX and C = C∞(X) the problem was solved by De
Wilde and Lecomte ([DL], 1983). A more geometric solution was discovered by
Fedosov ([Fe], 1994). The general case, i.e.C = C∞(X) for a Poisson manifoldX,
was solved by Kontsevich ([Ko1], 1997). See surveys in the book [CKTB].
Remark 1.4. The deformations considered in this paper are parameterized by
the algebra K[[ℏ]]. It is possible to replaceK[[ℏ]] with any other noetherian com-
plete local commutativeK-algebra R, with maximal idealm, such thatR/m = K.
Instead of C[[ℏ]] we take the complete tensor productRˆ⊗KC, with its obvious
augmentation toC. All results will remain valid.

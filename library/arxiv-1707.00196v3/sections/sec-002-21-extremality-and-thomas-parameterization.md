---
doc_id: arxiv-1707.00196v3
doc_title: "Yang-Baxter representations of the inﬁnite symmetric group"
section_id: sec-002-21-extremality-and-thomas-parameterization
section_title: "Extremality and Thoma's parameterization"
section_number: 2.1
pages: 6-8
source_pdf: 1707.00196v3.pdf
source_sha256: 9908b71521275b17
toc_source: outline
doc_brief: "Yang-Baxter representations of the inﬁnite symmetric group — Every unitary involutive solution of the quantum Yang-Baxter equation (R- matrix) deﬁnes an extremal character and a representation of the"
---
We now connect S∞to R-matrices by showing that any R-matrix deﬁnes an extremal
character and corresponding factor representation of S∞. We will be working with the
inﬁnite tensor product E0 := N
n≥1 End V (deﬁned only algebraically at this point),
with inclusions ﬁxed by tensoring with idV in the last factor. With the group inclusions
Sn ⊂Sn+1 ⊂S∞deﬁned by letting σ ∈Sn act on N by keeping all j > n ﬁxed, the
system of representations ρ(n)
R , R ∈R0(V ) is coherent and deﬁnes a ∗-homomorphism
ρR : C[S∞] →E0. The generators σi, i ∈N, are mapped to
Ri := ρR(σi) = 1⊗(i−1) ⊗R ⊗1 ⊗. . . ,
(2.2)
where here and hereafter, we write 1 instead of idV when the base space is clear from
the context. Note that Ri can be viewed as an element of End V ⊗n for n ≥i + 1, or
of E0.
We refrain from viewing ρR as a representation on N
n≥1 V , as the deﬁnition of
this space depends on choices. Our S∞-representations will be deﬁned by composing
ρR with the GNS representation of E0 with respect to its unique normalized trace3,
τ =
O
n≥1
TrV
d
: E0 →C .
(2.3)
Proposition 2.2. Let R ∈R0(V ). Then
χR := τ ◦ρR
(2.4)
is an extremal character of S∞. On an n-cycle cn, n ≥2, it evaluates to
χR(cn) = d−n TrV ⊗n(R1 · · · Rn−1),
d = dim V.
(2.5)
Proof. By standard properties of the trace, χR is a normalized positive class function.
To show that χR is also extremal, we have to verify that it factorizes over permutations
σ, σ′ ∈S∞with disjoint supports (Thm. 2.1).
Let σ, σ′ ∈S∞have disjoint supports. Taking into account that χR is a class
function, we may assume without loss of generality that suppσ ⊂{1, . . . , n} and
supp σ′ ⊂{n + 1, . . . , n + m} for some n, m ∈N.
Setting N := n + m, we then have ρ(N)
R (σ) = ρ(n)
R (σ) ⊗1⊗m and ρ(N)
R (σ′) =
1⊗n ⊗ρ(m)
R (σ′). Using TrV ⊗W(A ⊗B) = TrV (A) TrW (B), we arrive at
χR(σσ′) = d−N TrV ⊗N ((ρ(n)
R (σ) ⊗1⊗m)(1⊗n ⊗ρ(m)
R (σ′))
= d−n TrV ⊗n(ρ(n)
R (σ)) · d−m TrV ⊗m((ρ(m)
R (σ′))
= χR(σ)χR(σ′) ,
and the proof of extremality of χR is ﬁnished.
For the second statement, we only need to note that ρR (1.2) maps the n-cycle
σ1σ2 · · · σn−1 to R1R2 · · · Rn−1 ∈End(V )⊗n.
We will call the characters χR, R ∈R0, Yang-Baxter characters of S∞. As we
just demonstrated, every Yang-Baxter character is extremal. We will see in the next
section that the converse is not true: not every extremal character is Yang-Baxter.
3See Sec. 5.3 for diﬀerent choices of states on E0.
6
Using the representation theory of ﬁnite groups and the inductive limit deﬁnition of
S∞, it follows from Prop. 2.2 that two R-matrices R, S ∈R0 are equivalent in the sense
of Def. 1.1 if and only if they have the same character and the same dimension. (As
we work with normalized characters, the dimension is not contained in the character.)
Thus the dimension and the sequence of traces (2.5) (indirectly) characterize the
equivalence classes R0/∼.
Thoma not only found a criterion for characterizing extremal characters, but also
gave a classiﬁcation in terms of an inﬁnite dimensional simplex.
Theorem 2.3. [23] Let T denote the collection of all sequences {αi}i∈N, {βi}i∈N of
real numbers such that
i) αi ≥0 and βi ≥0,
ii) αi ≥αi+1 and βi ≥βi+1,
iii) P
i αi + P
j βj ≤1.
The pairs of sequences (α, β) ∈T are in bijection with extremal characters of S∞. On
an n-cycle, the character χ corresponding to (α, β) ∈T takes the value
χ(cn) =
X
i
αn
i + (−1)n+1 X
i
βn
i ,
n ≥2.
(2.6)
We will call the parameters (α, β) ∈T the Thoma parameters of a character.
As a consequence of these results, any R ∈R0 deﬁnes a point (α, β) ∈T. In the
following sections, we will be concerned with the problem of identifying the subset of
all Thoma parameters of Yang-Baxter characters inside T.
Another important question is how to extract the Thoma parameters (α, β) from
an involutive R-matrix. In view of (2.5) and (2.6), the parameters (α, β) ∈T corre-
sponding to R ∈R0 are uniquely ﬁxed by the system of equations
X
i
αn
i + (−1)n+1 X
i
βn
i = d−n TrV ⊗n(R1 · · · Rn−1) ,
n ≥2.
(2.7)
We will develop tools to compute (α, β) directly from R in Sections 3 and 4.1.
To conclude this section, let us mention a few simple examples of R-matrices.
Clearly, ±1 = ± idV ⊗V ∈R0(V ).
It is well known and easy to check that also
±F ∈R0(V ) is an involutive solution of (1.1), where F(v ⊗w) = w ⊗v is the tensor
ﬂip. The Thoma parameters of these R-matrices are the following.
R
non-vanishing Thoma parameters
1
α1 = 1, independent of d
−1
β1 = 1, independent of d
F
α1 = . . . = αd = d−1
−F
β1 = . . . = βd = d−1
Since the R-matrices R = 1 and R = −1 obviously give the trivial and alternating
representation of S∞, respectively, the ﬁrst two lines immediately follow from (2.7).
The claimed parameters of ±F can be veriﬁed by computing TrV ⊗n(F1 · · · Fn−1) = d.
7

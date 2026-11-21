---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-067-m-then-the-modular-group-σφ
section_title: "Then the modular group σφ"
section_number: M
pages: 157-161
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
t is the unique one parameter automorphism
group of M which satisﬁes the KMS condition for φ.
Proof. Perform the GNS construction with canonical cyclic and separating
vector Ωand modular operators S = J∆1/2. Recall that f(∆)Ω= Ωfor any
function of ∆with f(1) = 1. In particular φ(σφ
t (x) = ⟨(∆itx∆−itΩ, Ω⟩so σφ
t
preserves φ.
Now let us check the rest of the KMS condition. We have
φ(σφ
t (x)y) = ⟨∆−ityΩ, x∗Ω⟩
and
φ(yσφ
t (x))
=
⟨yσφ
t (x)Ω, Ω⟩
=
⟨J∆1/2σφ
t (x∗)Ω, J∆1/2yΩ⟩
=
⟨∆1/2yΩ, ∆1/2∆itx∗Ω⟩
=
⟨∆1/2−ityΩ, ∆1/2x∗Ω⟩
So let ξ = yΩ, η = x∗Ωand let pn be the spectral projection for ∆for
the interval [1/n, n] so that pn tends strongly to 1 and ∆±1 are bounded on
pnHφ. The functions
Fn(z) = ⟨∆−izpnξ, η⟩
are then entire and
|Fn(t) −φ(σφ
t (x)y)|
=
|⟨∆−it(1 −pn)ξ, η⟩| ≤||(1 −pn)ξ|| ||η||
|Fn(t + i) −φ(yσφ
t (x))|
=
|⟨∆1/2−it(1 −pn)ξ, ∆1/2η⟩| ≤||(1 −pn)∆1/2ξ|| ||∆1/2η||.
157
Hence the Fn are bounded and continuous on the strip {z : 0 < ℑmz < 1}
and converge uniformly on its boundary. By the Phragmen-Lindelof theorem
we are done.
Now let us prove uniqueness of the modular group with the KMS condi-
tion.
Let αt be another continous one-parameter automorphism group satisfy-
ing KMS for φ. The fact that αt preserves φ means we can deﬁne a strongly
continous one-parameter unitary group t 7→ut by utxΩ= αt(x)Ω. By Stone’s
theorem it is of the form t 7→Dit for some non-singular positive self-adjoint
operator A. The goal is to prove that D = ∆. As a ﬁrst step we construct a
dense set of analytic vectors in MΩby Fourier transform. Let A be the set
of all operators of the form
Z ∞
−∞
ˆf(t)αt(x)dx
for all C∞functions f of compact support on R. The integral converges
strongly so
f(log(D))xΩ=
Z ∞
−∞
ˆf(t)Dit(xΩ)dx
is in AΩ. Thus the spectral projections of D are in the strong closure of A
and AΩis dense. Moreover z 7→DzxΩis analytic for x ∈A since xΩis
in the spectral subspace of A for a bounded interval. Also AΩis invariant
under Dz by the functional calculus. To compare with φ deﬁne, for x and y
in A, the entire function
F1(z) = ⟨D−izyΩ, x∗Ω⟩.
Let F be the function, analytic inside the strip and continuous and bounded
on it, guaranteed for x and y by the KMS condition. Then if we deﬁne G(z)
for −1 ≤ℑmz ≤1 by
G(z) =





F(z) −F1(z)
if ℑmz ≥0;
F(z) −F1(z)
if ℑmz ≤0.
Since F and F1 agree on the real line G is analytic for −1 < ℑmz < 1, hence
check typesetting
equal to 0, and since both F and F1 are continous on the strip, φ(yσt(x)) =
F(t + i) = F1(t + i) = ⟨D1−ityΩ, x∗Ω⟩. In particular putting t = 0 we get
⟨DyΩ, x∗Ω⟩
=
φ(yx)
=
⟨xΩ, y∗Ω⟩
=
⟨J∆1/2x∗Ω, J∆1/2yΩ⟩
=
⟨∆1/2yΩ, ∆1/2x∗Ω⟩
158
So ∆1/2yΩis in the domain of ∆1/2 and ∆yΩ= DyΩ.
Thus D and ∆agree on AΩ. But multiplication by the function ez + 1 is
a linear isomorphism of C∞
c so by functional calculus (D+1)AΩ= AΩwhich
is thus dense. Since D + 1 is invertible by spectral theory, any (ξ, (D + 1)ξ)
in the graph of D+1 can be approximated by (AnΩ, (D+1)AnΩ). Thus D is
essentially self-adjoint on AΩ, and both ∆and D are self-adjoint extensions
of the restriction of D to this domain. Thus D = ∆.
159
160

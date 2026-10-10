---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-013-push-forward-and-pull-back
section_title: "Push-forward and pull-back."
section_number: null
pages: 18-20
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
For spaces X and Y and a kernel Φ : X→ Y deﬁne the push-forward on
Hochschild homology Φ∗ : HH•(X)→ HH•(Y) as follows
Φ∗

 w 

 := Φ 
w .
18
For the reader still unhappy with diagrams, for v ∈ Hom•(Σ− 1
X , IdX), deﬁne
Φ∗(v) ∈ Hom•(Σ− 1
Y , IdY) as the following composite, which is read from the
above diagram by reading upwards from the bottom:
Σ− 1
Y
γ
−→ Φ ◦ Φ∨ Id◦η◦Id
− − − −→ Φ ◦ Σ− 1
X ◦ ΣX ◦ Φ∨ Id◦v◦Id◦Id− − − − − −→ Φ ◦ ΣX ◦ Φ∨
ǫ
−→ IdY.
Similarly deﬁne the pull-back Φ∗ : HH•(Y)→ HH•(X) as follows
Φ∗

 v

 := Φ 
v .
These operations depend only on the isomorphism class of the kernel as
shown by the following.
Proposition 5. If kernels Φ and ^Φ are isomorphic then they give rise to
equal push-forwards and equal pull-backs: Φ∗ = ^Φ∗ and Φ∗ = ^Φ∗.
Proof. This follows immediately from the fact that the 2-morphisms γΦ ,
γ ^Φ , ǫ
Φ and
ǫ
^Φ of Section 3.2 are natural and thus commute with the given
kernel isomorphism Φ ∼= ^Φ.
The push-forward and pull-back operations are functorial i n the following
sense.
Theorem 6 (Functoriality). If Φ : X→ Y and Ψ : Y→ Z are kernels then
the push-forwards and pull-backs compose appropriately, n amely:
(Ψ ◦ Φ)∗ = Ψ∗ ◦ Φ∗ : HH•(X)→ HH•(Z)
and
(Ψ ◦ Φ)∗ = Φ∗ ◦ Ψ∗ : HH•(Z)→ HH•(X).
Proof. This follows from the fact that the right adjunction τR is a 2-functor.
The adjoint of Ψ ◦ Φ is canonically τR(Φ) ◦ τR(Ψ), i.e., is ΣX ◦ Φ∨ ◦ ΣY ◦ Ψ∨ .
This means that the unit of the adjunction Id⇒ Ψ ◦ Φ ◦ ΣX ◦ Φ∨ ◦ ΣY ◦ Ψ∨
is given by the composition Id⇒ Ψ ◦ ΣY ◦ Ψ∨ ⇒ Ψ ◦ Φ ◦ ΣX ◦ Φ∨ ◦ ΣY ◦ Ψ∨ .
This gives
(Ψ ◦ Φ)∗(w) =
Ψ Φ w = Ψ∗ (Φ∗(w)) .
Theorem 7. If Φ : X→ Y and Ψ : Y→ X are adjoint kernels, Φ ⊣ Ψ, then
we have
Φ∗ = Ψ∗ : HH•(X)→ HH•(Y).
19
Proof. By the uniqueness of adjoints we have a canonical isomorphis m, Ψ ∼=
τR(Φ) and by Proposition 5 Ψ∗ = ( τR(Φ))∗. It therefore suﬃces to show
that Φ∗ = (τR(Φ))∗. Observe that
τR(τR(Φ)) = τR(ΣX ◦ Φ∨ ) ∼= τR(Φ∨ ) ◦ τR(ΣX) ∼= ΣY ◦ Φ∨∨ ◦ Σ− 1
X ,
and similarly
τL(τR(Φ)) ∼= Φ ◦ Σ− 1
X ◦ ΣX.
Of course the latter is isomorphic to Φ but the Serre kernels are left in so to
make the adjunctions more transparent. We now get the unit fo r adjunction
τR(Φ) ⊣ τR(τR(Φ)) and the counit for the adjunction τL(τR(Φ)) ⊣ τR(Φ) as
follows:
Φ ; Φ .
Thus
τR(Φ)∗ (w) = Φ 
w = Φ 
w = Φ∗(w).

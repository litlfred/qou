---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-040-132-proof-of-the-main-theorem
section_title: "Proof of the main theorem."
section_number: 13.2
pages: 96-98
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Proof of the main theorem.
We begin with an easy exercise in contour integration.
Exercise 13.2.1. Let S be the strip {z ∈C : −1/2 ≤ℜ(z) ≤1/2}. Suppose
f is continuous and bounded on S and analytic on the interior of S. Then
f(0) =
Z ∞
−∞
f(1/2 + it) + f(−1/2 + it)
2 cosh πt
dt
Hint: Integrate f(z)
sin πz around rectangular contours in S tending to the
boundary of S.
96
Proposition 13.2.2. With notation as in the previous section
a =
Z ∞
−∞
λ2it ∆itJa′J∆−it
2 cosh πt
dt
Proof. Since J∆1/2J = ∆−1/2 we have J(D(S) ∩D(T)) = D(S) ∩D(T) so
after a little rearrangement the formula of 13.1.7 reads
⟨Ja′Jξ, η⟩= λ⟨a∆−1/2ξ, ∆1/2η⟩+ λ−1⟨a∆1/2ξ, ∆−1/2η⟩.
Now let H0 be the dense subspace of all vectors in H which is the union of
all ξ[a,b](∆for 0 < a < b < ∞. Certainly H0 ⊆D(S) ∩D(F), H0 is invariant
under J and ∆z for z ∈C, and moreover for ξ ∈H0, z 7→∆zξ is an entire
function of z.
For ξ, η ∈H0 deﬁne the analytic function
f(z) = λ2z⟨a∆−zξ, ∆zη⟩.
Then f is bounded in the strip S of the previous lemma and f(0) = ⟨aξ, η⟩.
Also f(1/2 + it) = ⟨∆it∆1/2ξ, η⟩so that
f(1/2 + it) + f(−1/2 + it) = λ2it⟨∆itJa′J∆−itξ, η⟩.
So by the previous lemma we are done.
Theorem 13.2.3. Let M be a von Neumann algebra on H and Ωa cyclic
and separating vector for M. Suppose S is the closure of xΩ7→x∗Ωon MΩ.
Let ∆= S∗S, and J be the antiunitary of the polar decomposition S = J∆1/2.
Then
(i) JMJ = M ′
(ii) ∆itM∆−it = M ∀t ∈R
Proof. If a′ ∈M ′ we know that
Z ∞
−∞
λ2it ∆itJa′J∆−it
2 cosh πt
dt ∈M.
Conjugating by a unitary u ∈M ′ and writing λ = e
iθ
2 we see that the
Fourier transforms of the strongly continuous rapidly decreasing functions
∆itJa′J∆−it
2 cosh πt
and u∆itJa′J∆−it
2 cosh πt
u∗are equal. Hence ∆itJa′J∆−it ∈M for
all real t since it commutes with every unitary u ∈M ′. (Take inner products
with vectors if you are not happy with Fourier transforms of operator valued
functions.)
Putting t = 0 we see JM ′J ⊆M and by symmetry JMJ ⊆M ′. Hence
JMJ = M ′ and we are done.
97
Deﬁnition 13.2.4. The operator J of the previous result is called the mod-
ular conjugation and the strongly continuous one-parameter group of auto-
morphisms of M deﬁned by σφ
t (x) = ∆itx∆−it is called the modular auto-
morphism group deﬁned by φ.

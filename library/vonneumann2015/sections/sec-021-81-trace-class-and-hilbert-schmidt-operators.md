---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-021-81-trace-class-and-hilbert-schmidt-operators
section_title: "Trace class and Hilbert Schmidt operators."
section_number: 8.1
pages: 49-54
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Trace class and Hilbert Schmidt operators.
The material in this section is standard so we will only prove results as it
suits us, otherwise referring any unproved assertions to Reed and Simon.
Lemma 8.1.1. If a ∈B(H) is positive and (ξi) and (ηi) are two orthonormal
bases of H, then
X
i
⟨aξi, ξi⟩=
X
i
⟨aηi, ηi⟩
(where ∞is a possible value for the sum).
Proof. We have
X
i
⟨aξi, ξi⟩=
X
i
||√aξi||2
=
X
i
(
X
j
|⟨√aξi, ηj⟩|2)
=
X
j
(
X
i
|⟨√aηj, ξi⟩|2)
=
X
j
||√aηj||2
49
=
X
j
⟨aηj, ηj⟩
where every number is positive so the order of the sum is immaterial.
The number P
i⟨aξi, ξi⟩of the previous theorem is called the trace of a,
written Trace(a).
Deﬁnition 8.1.2. An element a ∈B(H) is said to be of trace class if
Trace(|a|) is ﬁnite.
If a is trace class and (ξi) is an orthonormal basis, the sum
X
i
⟨aξi, ξi⟩
converges absolutely and is called the trace, Trace(a), of a.
Theorem 8.1.3. The trace class operators on H form a self-adjoint ideal
of compact operators, I1, in B(H).
The function |a|1 deﬁned by |a|1 =
Trace(|a|) deﬁnes a norm on I1 for which it is complete. Moreover ||a|| ≤
|a|1.
Proof. The only thing not proved in Reed and Simon is completeness. For
this observe that if an is a Cauchy sequence in | −|1, it is Cauchy in || −|| so
what we have to do is show that the norm limit of a | −|1-Cauchy sequence
(an) is trace class and that the sequence tends to that limit in | −|1. So
suppose ϵ > 0 is given. Then for m and n large enough
∞
X
i=1
⟨|an −am|ξi, ξi⟩< ϵ.
So for any N,
N
X
i=1
⟨|an −am|ξi, ξi⟩< ϵ.
Now if bn tends in norm to b, then |bn| tends in norm to |b| (obviously
b∗
nbn →b∗b, and approximate the square root function by polynomials on an
interval) so for each ﬁxed i,
lim
n→∞|an −am|ξi = |a −am|ξi.
So PN
i=1⟨|a −am|ξi, ξi⟩< ϵ and letting N tend to ∞we see that a ∈I1 since
I1 is a vector space, and also that an →a in | −|1.
50
The trace is independent of the orthonormal basis and if a is trace class
and b ∈B(H), Tr(ab) = Tr(ba).
We see that each h ∈I1 determines a linear functional φh on B(H) by
φh(x) = Trace(xh).
Deﬁnition 8.1.4. The trace-class matrix as above is called the density matrix
for the state φh.
Proposition 8.1.5. Each φh is ultraweakly continuous and its norm as an
element of B(H)∗is |h|1.
Proof. Since h is compact, choose an orthonormal basis (ξi) of eigenvectors
of |h| with eigenvalues λi and let h = u|h| be the polar decomposition. Then
φh(x) =
∞
X
i=1
⟨xu|h|ξi, ξi⟩
so ultraweak continuity is apparent, and
φh(x) ≤
∞
X
i=1
||x|| || |h|ξi||
= ||x||
∞
X
i=1
λi
= ||x|| |h|1.
Moreover evaluating φh on u∗gives ||φh|| = |h|1.
If H and K are Hilbert spaces, a bounded operator x : H →K is called
Hilbert-Schmidt if x∗x is trace class, i.e. P∞
i=1 ||xξi||2 < ∞for some (hence
any) orthonormal basis (ξi) of H. The set of all Hilbert-Schmidt operators
from H to K is written ℓ2(H, K) and if x is Hilbert-Schmidt, so is x∗, and x
is compact.
Theorem 8.1.6. If a ∈B(H), b ∈B(K) and x ∈ℓ2(H, K) then bxa ∈
ℓ2(H, K). If x ∈ℓ2(H, K) and y ∈ℓ2(K, H) then yx is trace class. With the
inner product ⟨x, y⟩= Trace(y∗x), ℓ2(H, K) is a Hilbert space in which the
ﬁnite rank operators are dense.
Proof. See Reed and Simon.
51
Exercise 8.1.7. Prove all the assertions made above about trace-class and
Hilbert-Schmidt operators.
Exercise 8.1.8. If H and K are Hilbert spaces construct a natural map from
K ⊗H∗to ℓ2(H, K) and show that it is unitary.
Let |x|2 be the Hilbert space norm on Hilbert-Schmidt operators.
Lemma 8.1.9. If x ∈ℓ2(H, K) and y ∈ℓ2(K, H) then Trace(xy) = Trace(yx).
Proof. First note that the result is true if we suppose that |x| is trace class.
For then let x = u|x| be the polar decomposition, choose an orthonormal
basis (ξi) of the ﬁnal domain of u and extend it to an orthonormal basis of
K. Also extend (u∗ξi) to an orthonormal basis of H by vectors in ker(|x|).
Then
Trace(xy) =
X
i
⟨u|x|yξi, ξi⟩
=
X
i
⟨|x|yuu∗ξi, u∗ξi⟩
= Trace(|x|(yu))
= Trace((yu)|x|)
= Trace(yx.)
Now suppose only that x is Hilbert-Schmidt. Let ϵ > 0 be given and choose
x′ of ﬁnite rank with |x −x′|2 < ϵ. Then
|Trace(xy) −Trace(yx)| = |Trace((x −x′)y) −Trace(y(x −x′))|
which by Cauchy-Schwartz is ≤2ϵ|y|2.
Corollary 8.1.10. If ω is an ultraweakly continuous linear functional on
B(H), there is a trace class h so that ω = φh.
Proof. By 5.1.2 there are (ξi) and (ηi) in ℓ2(N, H) so that ω(x) = P
i⟨xξi, ηi⟩.
Then if we deﬁne a and b from ℓ2(N) to H by a(f) = P
i f(i)ξi and b(f) =
P
i f(i)ηi, a and b are Hilbert Schmidt and ω(x) = Trace(b∗xa) which is
Trace(xab∗) by the previous result.
Putting everything together so far, we have identiﬁed the image of the
Banach space I1 under the map h 7→φh with the closed subspace of B(H)∗
consisting of ultraweakly continuous linear functionals. To close the loop we
only need to show that the Banach space dual of I1 is B(H).
52
Theorem 8.1.11. If α : I1 →C is linear and bounded for | −|1, there is an
x ∈B(H) so that α(a) = φa(x), and ||α|| = ||x||.
Proof. This is rather routine. Two vectors ξ and η deﬁne an element x of I1
by x(v) = ⟨v, ξ⟩η so one may deﬁne a sesquilinear form on H by (ξ, η) = α(x).
Boundedness of x follows from that of α so there is an appropriate x ∈B(H).
To show that the norm of x as an element of the dual of I1 is actually ||x||,
suppose ||x|| = 1 and choose a unit vector ξ with ||xξ|| almost equal to 1.
Then Tr(hx) is almost 1 if h is the partial isometry which sends v ∈H to
⟨v, xξ⟩
ξ
||xξ||.
Exercise 8.1.12. Fill in the missing details in the previous proof.
Now we pass to von Neumann algebras though in fact these results work
for any ultraweakly closed subspace of B(H).
Theorem 8.1.13. If V is an ultraweakly closed subspace of B(H) then V =
V ⊥⊥in the sense that if φ(x) = 0 for every ultraweakly continuous φ for
which φ(V ) = 0 then x ∈V .
Proof. This is a simple application of the Hahn-Banach theorem—if x /∈V
construct an ultraweakly continuous functional which is zero on V and non-
zero on x.
‘
Exercise 8.1.14. Exhibit a non-zero trace class operator on ℓ2(Γ) which is
orthogonal to vN(Γ).
Theorem 8.1.15. If V is an ultraweakly closed subspace of B(H) then it
is canonically the dual Banach space of V∗which is deﬁned as the space
of ultraweakly continuous linear functionals on V . Moreover the ultraweak
topology on V is the weak-* topology on V as the dual of V∗.
Proof. If B is a Banach space with dual B∗and V is a weak-* closed subspace
of B∗then V is the dual of B/V ⊥(surjectivity of the natural map from V to
the dual of V/B⊥is a result of the previous theorem), so V is a dual space.
So we just have to identify the Banach space B/V ⊥with the space of weak-*
continuous (as elements of B∗∗) linear functionals on V . This is a simple
exercise. Putting B = I1 we are done.
Exercise 8.1.16. If V is an ultraweakly closed subspace of B(H), show that
V∗is a separable Banach space if H is a separable Hilbert space.
53

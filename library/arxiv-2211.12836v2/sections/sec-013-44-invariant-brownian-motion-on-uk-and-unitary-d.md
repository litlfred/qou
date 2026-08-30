---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-013-44-invariant-brownian-motion-on-uk-and-unitary-d
section_title: "Invariant Brownian motion on Uk and unitary Dyson Brownian motion"
section_number: 4.4
pages: 30-32
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
conclude this section by recalling rigorously the deﬁnition of the generalized Dyson Brownian
motion onUk and its eigenvalue process onTk, see [39] for a detailed background on this stochastic
process and [21] for most of the content of this section. The Lie group U(k) is a Riemannian
sub-manifold of Mk(C) of real dimension n2, and the tangent space of U(k) at Id is given by the
Lie algebra
uk ={M∈Mk(C), M∗ +M = 0}.
Remark that uk is not semisimple, since uk = suk⊕iRId, where suk ={M∈ uk, Tr(M) = 0} is
simple. There is, up to a scalar, a unique invariant scalar product on suk given by⟨·,·⟩ : (X,Y )↦→
kTr (Y∗X). There is trivially a unique invariant metric on iRId given by (X,Y )↦→Tr (X)Tr (Y∗).
Hence, we can deduce that for all α,β > 0, there is a invariant scalar product ⟨·,·⟩α,γ on uk given
by
⟨X,Y⟩α,γ =γ−1kTr (Y∗X) + (α−1−γ−1)Tr (Y∗)Tr (X),
and that any invariant scalar product is of this type.
For 1≤ r,s ≤ n, write Ers for the matrix with only one nonzero entry on the r-th line and
s-th column. Set Xrs = 1√
2k(Ers−Esr),Xsr = i√
2k(Ers +Esr) for 1 ≤ r < s≤ k, Xrr =
i√
2r(r−1)k
∑
1≤s<r(Ess−Err) for 2 ≤ r≤ k and X11 = 1
k
∑k
r=1Err. Then, {Xrs}1≤r,s≤k is an
orthonormal basis of uk with respect to the scalar product ⟨·,·⟩1,1. For Y ∈ uk we denote by
LY : C1(Uk)↦→ C0(Uk) the diﬀerential operator induced by the unique left-invariant vector ﬁeld
equal to Y at Id, namely for f∈C1(Uk) and U∈Uk,
LY [f](U) = lim
t→0
f(U exp(tY ))−f(U)
t .
We can then deﬁne the Brownian motion with parameters ( α,γ ) on U(k) as follows.
Deﬁnition 4.10. Letα,γ ≥ 0. There exists a unique Markov process Bα,γ(t))t≥0 with almost sure
continuous trajectories on U(k) such that
∂
∂t E(f(UBα,γ(t)))|t=0 =

γ
∑
1≤i,j≤n
L2
Xij + (α−γ)L2
X11

f(U),
for all f∈ C1(Un) and U∈ Un. Moreover, such a Markov process is invariant by left and right
translation by elements ofU(k), and any Markov process onU(k) with the same invariance property
and with almost sure continuous trajectories is equal to Bα,γ for some α,γ ≥ 0.
Forα,γ >0, the stochastic process Bα,γ is the Brownian motion with respect to the left invariant
metric whose value at Id is⟨·,·⟩α,γ. From the expression of the generator given in Deﬁnition 4.10,
it can be seen that B0,γ(t)B0,γ(t)−1∈SU (k) (resp. Bα,0(t)Bα,0(t)−1∈ T·Id) a.s for all t≥ 0.
For ⃗ u∈ Tk with uk <··· < u1, let Bα,γ
⃗ u be the eigenvalues process of U⃗ uBα,γ where U⃗ uis
uniformly sampled on the adjoint orbit {U∈U(k),p (U) =⃗ u}. Then, Bα,γ
⃗ u is a Markov process on
Tk starting at ⃗ uand whose generator is given by
(22) Lα,γ = γ
k


k∑
i=1
∂2
∂u2
i
+
∑
i<j
cotuj−ui
2
( ∂
∂uj
− ∂
∂ui
)
 + α−γ
k2
∂2
∂2(∑ui),
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 31
the proof of this fact is given in [21, Proposition 12.5.1] for the case α = γ = k and can be
generalized for arbitrary α,γ ≥ 0. If ui = ui+1 for some 1 ≤ i≤ k, one can still give a meaning
to the corresponding heat equation in a weak sense, and in any case the corresponding kernel is
C∞ for all t> 0. We call then the resulting stochastic process ( Bα,γ
⃗ u(t))t≥0 the generalized unitary
Dyson Brownian motion with parameter ( α,γ ) starting at ⃗ u(note that the subscript ⃗ uwill be
dropped when ⃗ u= (0,..., 0)).
Whenα,γ >0 and for any initial value ⃗ u∈Tk, the probability measure µt given by the unitary
Dyson Brownian motion with parameter ( α,γ ) starting at ⃗ uhas a density KU(k),α,γ
t (⃗ u,⃗ v)|V (⃗ v)|2,
where KU(k),α,γ
t (⃗ u,⃗ v) satisﬁes the parabolic diﬀerential equation



∂tKU(k),α,γ
t (⃗ u,·) =Lα,γKU(k),α,γ
t (⃗ u,·),
KU(k),α,γ
0 (⃗ u,·) = 1
|V (⃗ u)|2δ⃗ u,
where the second equality is understood in the weak sense. For general initial distribution µ0∈
M1(Tk), the time-evolving distribution (µt)t≥0 can also be characterized by its Fourier transform:
for any J∈Bk,
(23) Φ[ µt](J) = exp(−κα,γ(J)t)Φ[µ](J),
where
κα,γ(J) = γ
k
[
‖ ˜J‖2−‖~I0‖2
]
+ α
k2 (⟨J⟩−⟨ I0⟩)2,
with⟨J⟩ =∑k
i=1Ji and‖ ˜J‖2 =∑k
i=1(Ji−⟨J⟩/k)2 for J∈ Bk. By (23) and the inverse Fourier
transform on the unitary group, for α,γ >0 and t> 0 we have
(24) KU(k),α,γ
t (⃗ u,⃗ v) =
∑
J∈Bk
exp(−κα,γ(J)t)SJ(⃗ u)SJ(⃗ v).
In the case where α = 0, the stochastic process remains on the aﬃne subspace {⃗ v∈Tk,∑k
i=1vi =∑k
i=1ui} and thus has no density on Tk even for t >0. Set A ={⃗ u∈ Tk,∑k
i=0ui = 0}, which
corresponds to the set {p(U),U ∈SU (k)}. Then, B0,1 has a density KSU (k),γ
t (⃗ u,⃗ v) on A given by
(25) KSU (k),γ
t (⃗ u,⃗ v) =
∑
J∈Bk
Jk=0
exp(−κ0,γ(J)t)SJ(⃗ u)SJ(⃗ v).
By extension, when ∑k
i=1ui = ∑k
i=1vi, we also set KSU (k),γ
t (⃗ u,⃗ v) = KSU (k),γ
t (𝓁·⃗ u,𝓁·⃗ v) with
𝓁 =∑k
i=1ui.
By the diagonalization of Lα,γ on the orthonormal basis {SJ,J ∈ Bk} of the Hilbert space
L2(Tk,dp⋆(µH)), the kernel of any operator Lα,γ with γ,α > 0 consists of the vector space C1Tk,
so that the unique invariant measure of the corresponding Brownian motion is
|V (u1,...,u k)|2 =
∏
i<j
|e2iπuj−e2iπui|2,
which is the density of the measure p⋆(µH) with respect to the Lebesgue measure on Tk. Hence,
for α,γ > 0, the generalized Dyson unitary Brownian motion has a unique invariant probability
distribution on Tk which is precisely p⋆(µH). When α = 0 (resp. γ = 0), the space of invariant
measures is larger than p⋆(µH).
32 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO

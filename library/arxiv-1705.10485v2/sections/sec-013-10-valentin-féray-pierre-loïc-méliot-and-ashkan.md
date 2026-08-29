---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-013-10-valentin-féray-pierre-loïc-méliot-and-ashkan
section_title: "Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali"
section_number: 10
pages: 10-12
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
T0(R) T1(R)⊂
∂
∩
L1(R)∩ C∞
0 (R)
∩
C∞
b (R)
Fig. 2 The two spaces of test functionsT0(R) and T1(R).
(TD2) The tempered distributionˆf can be paired with the Fourier transformˆµ of a probability measure with
ﬁnite ﬁrst moment, in a way that extends the pairing betweenS′(R) and S (R) whenµ (and therefore
ˆµ) is given by a Schwartz density.
(TD3) The Parseval formula holds: iff∈ T1(R) and µ has ﬁnite expectation, then
⟨µ|f⟩ = 1
2π
⟨
ˆf
⏐⏐⏐ˆµ
⟩
.
Proof. We start by giving a better description of the tempered distributionsf and ˆf. Denoteφ =∂f; by
assumption, this tempered distribution can be represented by a functionφ∈ T0(R), which in particular
is of classC∞ and integrable. Set
~f(x) =
∫ x
y=0
φ(y)dy.
This is a function of classC∞, whose derivative isφ, and which is bounded sinceφis integrable. Therefore,
it is a tempered distribution, and for anyg∈ S (R),
⟨∂f|g⟩ =⟨φ|g⟩ =
⟨
∂~f
⏐⏐⏐g
⟩
.
We conclude that∂(f− ~f) is the zero distribution. It is then a standard result that, given a tempered
distribution ψ, one has∂ψ = 0 if and only ifψ can be represented a constant. So,
f(x) =
∫ x
y=0
φ(y)dy +f(0).
This shows in particular thatf is a smooth bounded function.
A similar description can be provided forˆf. Recall that the principal value distribution, denotedpv( 1
x),
is the tempered distribution deﬁned for anyg∈ S (R) by
⟨
pv
( 1
x
)⏐⏐⏐⏐g
⟩
= lim
ε→0
(∫
|x|≥ε
g(x)
x dx
)
.
The existence of the limit is easily proved by making a Taylor expansion ofg around 0. Denote
S [1] ={g∈ S (R)|g(x) =xh (x) with h∈ S (R)};
S[1] ={g∈ S (R)|g =∂h with h∈ S (R)};
the Fourier transform establishes an homeomorphism betweenS [1] and S[1], and the restriction ofpv( 1
x)
to S [1] is ⟨
pv
( 1
x
)⏐⏐⏐⏐g
⟩
=
∫
R
g(x)
x dx.
Mod-φ convergence, II: Estimates on the speed of convergence 11
Letˆg(ξ) be an element ofS [1], which we write asˆg(ξ) = (−iξ)ˆh(ξ) for someh∈ S (R). This is equivalent
tog(x) = (∂h)(x). Let us denoteg−(x) =g(−x),h−(x) =h(−x), andpv(iˆφ(ξ)
ξ ) the tempered distribution
deﬁned by
pv
(
iˆφ(ξ)
ξ
)
= i pv
(1
ξ
)
◦mˆφ,
withmˆφ : S (R)→ S (R) equal to the multiplication byˆφ. Then we can make the following computation:
⟨
ˆf
⏐⏐⏐ˆg
⟩
=
⟨
f
⏐⏐⏐ˆˆg
⟩
= 2π⟨f|g−⟩ =−2π⟨f|∂h−⟩ = 2π⟨φ|h−⟩ =
⟨
φ
⏐⏐⏐⏐
ˆˆh
⟩
=
⟨
ˆφ
⏐⏐⏐ˆh
⟩
=
⟨
ˆφ
⏐⏐⏐⏐
iˆg(ξ)
ξ
⟩
=
⟨
pv
(
iˆφ(ξ)
ξ
)⏐⏐⏐⏐⏐ˆg
⟩
.
Thus, the tempered distributionsˆf and pv(iˆφ(ξ)
ξ ) agree on the codimension1 subspace S [1] of S (R).
However, S [1] is also the space of functions inS (R) that vanish at0, so, ifg0 is any function inS (R)
such thatg0(0) = 1, then forg∈ S (R),
⟨
ˆf
⏐⏐⏐g
⟩
=
⟨
ˆf
⏐⏐⏐g−g(0)g0
⟩
+g(0)
⟨
ˆf
⏐⏐⏐g0
⟩
=
⟨
pv
(
iˆφ(ξ)
ξ
)⏐⏐⏐⏐⏐g−g(0)g0
⟩
+
⟨
ˆf
⏐⏐⏐g0
⟩
⟨δ0|g⟩
=
⟨
pv
(
iˆφ(ξ)
ξ
)⏐⏐⏐⏐⏐g
⟩
+
(⟨
ˆf− pv
(
iˆφ(ξ)
ξ
)⏐⏐⏐⏐⏐g0
⟩)
⟨δ0|g⟩
=
⟨
pv
(
iˆφ(ξ)
ξ
)
+Lδ 0
⏐⏐⏐⏐⏐g
⟩
where L is some constant. Thus,
ˆf(ξ) = pv
(
iˆφ(ξ)
ξ
)
+Lδ 0
and a computation against test functions shows that
L = 2πf (0)− i
⟨
pv
(1
ξ
)⏐⏐⏐⏐ˆφ
⟩
.
The three parts of the proposition are now easily proven. For (TD1), sincef(x) is smooth and bounded,
we can indeed consider the convergent integral
∫
Rf(x)µ(dx). For (TD2), assuming thatµ has a ﬁnite ﬁrst
moment,ˆµ is a function of classC 1 and with bounded derivative. The same holds forˆφˆµ, and therefore,
one can deﬁne
∫
R
ˆf(ξ)ˆµ(−ξ)dξ = i
⟨
pv
(1
ξ
)⏐⏐⏐⏐ˆφˆµ
⟩
+L
=
(
lim
ε→∞
∫
|x|≥ε
iˆφ(ξ)ˆµ(−ξ)
ξ dξ
)
+L.
Indeed, iff∈ C 1(R), then limε→∞
∫
1≥|x|≥ε
f(x)
x dx always exists, as can be seen by replacingf by its
Taylor approximation at0. Finally, let us prove the Parseval formula (TD3). The previous calculations
show that

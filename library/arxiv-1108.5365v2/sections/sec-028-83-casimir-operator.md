---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-028-83-casimir-operator
section_title: "Casimir operator"
section_number: 8.3
pages: 79-82
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual"
---
Next we will study the action induced from the pairing with the multiplica tive
unitary W. It turns out that the technical diﬃculty comes from the analysis o f the
following positive operator:
C =e2πbx +e−2πbx +e−2πbp, (8.7)
which is studied in detail in [20] in a diﬀerent context. This expression c omes from
the Casimir operator deﬁned by
C =FE + qK 2 +q−1K −2− 2
(q−q−1)2 . (8.8)
More precisely, under the pairing given in the next section, the Casim ir operator is
given by
C =
( i
q−q−1
) 2
(e2πbx +e−2πbx +e−2πbp + 2). (8.9)
Proposition 8.8. Forλ∈ R+,
Φ λ(s2) := Sb(−ix +iλ)Sb(−ix−iλ) (8.10)
is an eigenfunction for the operator C with eigenvalue e2πbλ +e−2πbλ.
Proof. We need to solve
CΦ λ(x) = (e2πbλ +e−2πbλ)Φ λ(x). (8.11)
We consider
C− (e2πbλ +e−2πbλ) = C− 2 cos(2πibλ) = 2 cos(2πibx)− 2 cos(2πibλ) +e2πbps2.
79
From the angle sum formula, we have
2 cos(2πibx)− 2 cos(2πibλ)
= −4 sin(πib(x−λ)) sin(πib(x +λ)),
and from the functional equation (3.9)
Sb(x +b) = 2 sin(πbx)Sb(x),
we immediately see that
e2πbpx·Sb(−ix +iλ)Sb(−ix−iλ)
= Sb(−ix +iλ +b)Sb(−ix−iλ +b)
= 4 sin( πib(−x +λ)) sin(πib(−x−λ))Sb(−ix +iλ)Sb(−ix−iλ)
= 4 sin( πib(x−λ)) sin(πib(x +λ))Sb(−ix +iλ)Sb(−ix−iλ).
Hence Φ λ(x) = Sb(−ix+iλ)Sb(−ix−iλ) satisﬁes the above eigenvalue equation.
Therefore we introduce the following transformation
Deﬁnition 8.9. We deﬁne the integral transformation
Φ −1 :L2(R+,dµ (λ))−→L2(R)
F (λ)↦→f (x) := lim
ǫ− →0
∫ ∞
0
Φ λ(x +iǫ)e−2πxǫF (λ)dµ(λ) (8.12)
wheredµ(λ) =|Sb(Q + 2iλ)|2dλ.
Theorem 8.10. Φ −1 is a unitary transformation that intertwines e2πbλ +e−2πbλ
and C.
Proof. We compute the inner product for f,g ∈W + whereW + is the dense sub-
space
W + :={f (x)∈C∞(R+) : F (y) := f (ey)∈W} .
Note that
Φ λ(x) = 1
Sb(Q−ix−iλ)Sb(Q−ix +iλ).
We have
⟨Φ −1f, Φ −1g⟩
= lim
ǫ− →0
∫
R
∫ ∞
0
∫ ∞
0
Sb(ǫ−ix−iλ)Sb(ǫ−ix +iλ)e−4πxǫ
Sb(Q−ǫ−ix−iβ)Sb(Q−ǫ−ix +iβ)f (λ)g(β)dµ(λ)dµ(β)dx
= lim
ǫ− →0
∫
R
∫ ∞
0
∫ ∞
0
Gb(ǫ +ix−iλ)Gb(ǫ +ix +iλ)eπiλ2−πiβ 2
e−2πx(Q−4ǫ)
Gb(Q−ǫ +ix−iβ)Gb(Q−ǫ +ix +iβ) f (λ)g(β)dµ(λ)dµ(β)dx
80
which means the contour for x separates the poles of the numerator and denomi-
nator.
Now by Corollary 3.4 the integrand has asymptotics in x
⏐
⏐
⏐
⏐
⏐
Gb(ǫ +ix−iλ)Gb(ǫ +ix +iλ)eπiλ2−πiβ 2
e−2πx(Q−4ǫ)
Gb(Q−ǫ +ix−iβ)Gb(Q−ǫ +ix +iβ)
⏐
⏐
⏐
⏐
⏐ =
{
e−2πx(Q−4ǫ) x−→∞
e2πQx x−→−∞ .
Hence the integral is absolutely convergent in x,λ,β and we can interchange the
order of integration to bring integration over x inside.
Shifting x↦→x +β, and using the 4-5 relation (Lemma 3.10), we obtain
= lim
ǫ− →0
∫ ∞
0
∫ ∞
0
Gb(Q− 4ǫ)Gb(2ǫ +iβ−iλ)Gb(2ǫ +iβ +iλ)
Gb(Q− 2ǫ +iβ−iλ)Gb(Q− 2ǫ +iβ +iλ) ·
eπiλ2−πiβ 2
e−2πQβ+8πβǫf (λ)g(β)|Sb(Q + 2iλ)|2|Sb(Q + 2iβ)|2dλdβ.
Note that the integration for β separates the poles of the numerator and denomi-
nator as well, and also since λ,β > 0, the case β =−λ can be ignored, hence we
obtain δ(λ−β) using Lemma 3.11:
=
∫ ∞
0
Gb(2iλ)e−2πQλ
Gb(Q + 2iλ) f (λ)g(λ)|Sb(Q + 2iλ)|4dλ
=
∫ ∞
0
f (λ)g(λ)|Sb(2iλ)|2|Sb(Q + 2iλ)|4dλ
=
∫ ∞
0
f (λ)g(λ)|Sb(Q + 2iλ)|2dλ.
This shows that the map is an isometry. The converse showing the eig enfunctions
are also complete is more diﬃcult, and can be found in [20]. The techniq ue involves
writing the measure
|Sb(Q + 2iλ)|2 = 4 sinh(πbλ) sinh(πb−1λ)
as linear combinations of 4 exponentials, and calculate the integral d irectly using
hints from hyperfunctions.
From the proof we therefore deduce the inverse map of the unitar y transforma-
tion to be the complex conjugate
Φ : L2(R)−→L2(R+,dµ (λ))
f (x)↦→F (λ) :=
∫
R−i0
f (x)
Sb(Q−ix−iλ)Sb(Q−ix +iλ)dx,
where the contour goes below the poles.
Since Φ λ(x) are the eigenfunctions satisfying CΦ λ(x) = (e2πbλ +e−2πbλ)Φ λ(x),
formally the integral transformation with Φ λ(x) as kernel will intertwine the action.
81

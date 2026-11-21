---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-026-55-state-integral
section_title: "State integral"
section_number: 5.5
pages: 46-47
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
toc_source: outline
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
the extension of the cocycle to the cut plane. The main idea is to use descendant state
integrals, following [27, Eqn.(41)], deﬁned by
IA,B(z, τ) =
Z
R+iε
Φb(x)B exp

−Aπix2 −2πzx
b

dx.
(249)
Using the holomorphic extension of the quantum dilogarithm Φ from Theorem 1.5, this
integral can be shown to extend to a holomorphic function in for (z, τ) ∈C × C′.
We
are interested in the integrals I1,2(z, τ) which, using the residue theorem, factorise as an
elementary function holomorphic for τ ∈C′ times the following bilinear combination, see [27,
Thm.3],
I(z, τ) = τ 1/2g(0,0)(˜t, ˜q)g(0,1)(t, q) −τ −1/2g(0,1)(˜t, ˜q)g(0,0)(t, q)
+ τ −1/2

τ θ′(t−1; q)
θ(t−1; q) −θ′(˜t−1; ˜q)
θ(˜t−1; ˜q) −1
2 + τ
2 −z

g(0,0)(˜t, ˜q)g(0,0)(t, q)
= τ 1/2g(0,0)(˜t, ˜q)g(0,1)(t, q) −τ −1/2g(0,1)(˜t, ˜q)g(0,0)(t, q) .
(250)
MODULAR q-HOLONOMIC MODULES
47
where the equality follows from Equation (52). Therefore, I(z, τ) extends to a holomorphic
function for (z, τ) ∈C × C′. Now, we see that
ΩV,S(z, τ) = (V |κS)(z, τ)V (z, τ)−1
= qt2

g(0,0)(˜t, ˜q)
g(0,1)(˜t, ˜q)
g(0,0)(˜q˜t, ˜q)
g(0,1)(˜q˜t, ˜q)
 
τ 1/2
0
0
τ −1/2
 
g(0,1)(qt, q)
−g(0,1)(t, q)
−g(0,0)(qt, q)
g(0,0)(t, q)

.
(251)
The entries of ΩV,S are then elementary functions holomorphic for τ ∈C′ times I(z + n +
mτ, τ) for some n, m ∈{−1, 0, 1}. This shows that the cocycle ΩV,S extends to a holomorphic
function for (z, τ) ∈C × C′; see [26, Thm.14] following the proof of [30, Thm.1.1]. Now
noting that
Av(
−→
M) = ∆κ,γ(Av(
−→
M)|κγ)
(252)
and ΩAv(U),T = I, part (c) of Theorem 1.2 proves part (b) of Theorem 1.7.

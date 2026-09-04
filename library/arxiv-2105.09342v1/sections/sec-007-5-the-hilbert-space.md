---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-007-5-the-hilbert-space
section_title: "The Hilbert space"
section_number: 5
pages: 17-18
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
doc_brief: "A Unitary Matrix Model for q-deformed Plancherel Growth — In this paper we construct a unitary matrix model that captures the asymptotic growth of Young diagrams under q-deformed Plancherel measure."
---
Following [1, 15] we give a Hilbert space description of the q-deformed growth process.
Using the connection between unitary matrix model and free Fermi droplet description, we
map the Young diagrams in automodel class to diﬀerent shapes of two dimensional phase
space droplets. Quantising these droplets, we further set up a correspondence between auto-
model diagrams and coherent states in the Hilbert space. Thus, growth of Young diagrams
are mapped to evolution of coherent states in the Hilbert space. The basic construction of
the Hilbert space is similar to the one considered in [1]. We brieﬂy review the construction
in Appendix D.
The Hilbert spaceH is a direct product ofH+ andH− whereH± are the Hilbert spaces
associated with the + and − sectors deﬁned in section 3.3 namely the upper and the lower
fermi surfaces. These two sectors are isomorphic. A generic state in H+ is given by
|⃗k
⟩
=
∏
n≥1
(a†
n)kn|s
⟩
(5.1)
where a†
ns are creation operators in H+ and|s
⟩
is the ground state annihilated by ans.|⃗k
⟩
satisﬁes the completeness relation (D.22). Therefore, (1 /√z⃗k)|⃗k
⟩
is the normalised excited
17
state. One can also deﬁne coherent states in the Hilbert space H+,
|τ+
⟩
= exp
( ∞∑
n=1
τ +
na†
n
nℏ
)
|s
⟩
. (5.2)
We set up a map between a state |ψ
⟩
∈H + and shape of the upper Fermi surface
|ψ
⟩
→{
⟨
ψ|¯h+(θ)|ψ
⟩
}. (5.3)
Such a mapping has been discussed in [15]. Expectation value of ¯h+ in ground state is given
by 1
2 +sℏ and has zero dispersion. Thus, the ground state |s
⟩
corresponds to an overall
shift of ¯h+ by an amount s/N over the classical value. Generic normalised excited states
correspond to O(ℏ) ripples on ¯h+. In this case, the expectation value of ¯h+ picks up a
non-zero dispersion atO(ℏ).O(1) deformations of the upper Fermi surface ¯h+ are mapped
to coherent states|τ+
⟩
inH+ as is evident from (D.28). An important thing to note here is
that the classical deformations do not disturb the quadratic proﬁle of the droplets i.e for a
givenθ, there exists unique values of h±(θ).
We ﬁrst consider the state corresponding to automodel diagrams for ordinary Plancherel
growth [1]. The automodel diagrams corresponds to
¯h±(θ) =±
(1
2 +ξ cosθ
)
. (5.4)
The set of coherent states with τ1 = ξ/2 , τn = 0 ∀n > 1 are mapped to the automodel
diagrams. In particular, the state corresponding to the limit shape is given by
|τ∗⟩ = exp
(
a†
1
2ℏ
)
|0⟩. (5.5)
Our ﬁnal goal is to ﬁnd the coherent state associated with automodel diagrams for q-
deformed Plancherel growth. For theq-deformed automodel class, the variable ¯h+(θ) is given
by
¯h(t,θ ) = 1
2− 1
2λ log(1− 2λξ cosθ +λ2ξ2) = 1
2 +
∞∑
n=1
ξnλn−1
n cosnθ. (5.6)
Therefore the coherent state associated to q-automodel class is given by
|τ +
q
⟩
= exp
( ∞∑
n=1
τ +
na†
n
nℏ
)
|s
⟩
, where τ +
n = ξnλn−1
n . (5.7)

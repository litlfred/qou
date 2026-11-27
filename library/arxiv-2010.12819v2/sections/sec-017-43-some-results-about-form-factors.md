---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-017-43-some-results-about-form-factors
section_title: "Some results about form factors"
section_number: 4.3
pages: 20-21
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
In Appendix B we give a brief recapitulation of the Quantum Inverse Scattering Method, in which local operators
such as σz
m are expressed in terms of entries of the monodromy matrix T = (A B
C D). For a general overview of
this method see [51]. The eigenstates of the XXZ Hamiltonian are given as |{λ}⟩ =∏n
k=1B(λk)|0⟩ for a set
of Bethe roots {λ}, their duals as ⟨{λ}| =⟨0|∏n
k=1C(λk) and we wish to ﬁnd matrix elements on the form
⟨{µ}|∏
iσai
mi|{λ}⟩, where ai∈{ z, +,−} and mi⁄= mj for i⁄= j. The resulting expressions for these matrix
elements in terms of functions of the Bethe roots are called form factors.
If we can ﬁnd form factors for the Koo-Saleur generators Ln, the work of looking at the action of the
Virasoro algebra in the spin chain reduces to evaluating the expressions of these form factors, rather explicitly
diagonalizing the ﬁnite Hamiltonian and then acting on the resulting eigenstates. For large system sizes N, this
is a signiﬁcant advantage: while the size of the Hamiltonian to be diagonalized grows exponentially in N, the
time needed to evaluate form factors is only polynomial. A similar form-factor program has already been carried
out in [52] for the case of the SU (2)-invariant six-vertex model and its descendants, which in the continuum
correspond to SU (2)k WZW models. However, in this case the program was carried out for the current Ja(z)
rather than the Virasoro generators.
Finding form factors for Ln boils down to ﬁnding form factors for ei and [ei,ei+1]. A priori this will involve
form factors for all six permutations of three diﬀerent neighbouring operators, namely
σz
mσ−
m+1σ+
m+2, (88a)
σz
mσ+
m+1σ−
m+2, (88b)
σ+
mσ−
m+1σz
m+2, (88c)
σ−
mσ+
m+1σz
m+2 (88d)
8Note that within (66), a charge with a twist ofeϕ =±α−/α+ can be rewritten as a charge witheϕ = 0 where the magnetization
Sz is shifted by one, which shows that these charges are on the form αr,s, r,s∈ Z leading to degenerate conformal weights. In
particular, with|e| = 1 we obtain the degenerate weight h1,1.
20
and
σ−
mσz
m+1σ+
m+2, (89a)
σ+
mσz
m+1σ−
m+2, (89b)
as well as σ−
mσ+
m+1,σ +
mσ−
m+1,σz
mσz
m+1 and σz. Luckily we can reduce the number of form factors we need to
compute by using various relations that follow from the Bethe ansatz. These relations can also give us some
general insight into how the lattice Virasoro generators Ln, ¯Ln should act on Bethe states—in particular, we
shall soon see how the duality for conjugate states appears already at ﬁnite size.

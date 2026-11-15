---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-028-46-tau-functions
section_title: "Tau functions"
section_number: 4.6
pages: 22-23
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
a complex manifold M. For the relevant deﬁnitions the reader can either consult the summary in
Section 3.3, or the full treatment in Appendix A. There is a holomorphic map
π: M →HomZ(Γ, C),
p 7→Zp,
which we call the period map. The miniversal assumption ensures that the derivative
(Dπ)p: TpM →HomZ(Γ, C)
(23)
at each point p ∈M is an isomorphism. We can therefore identify the tangent space TpM with
the vector space HomZ(Γ, C). The form ⟨−, −⟩then induces a Poisson structure on M.
More explicitly, we can choose a basis (γ1, · · · , γn) ⊂Γ and use the functions
zi(p) = Zp(γi): M →C
as co-ordinates on M. The dual of the map (23) identiﬁes γi ∈Γ with the element dzi ∈T ∗
p M,
and the Poisson structure has the Darboux form
{zi, zj} = ǫij,
ǫij = ⟨γi, γj⟩.
Let us consider a family of solutions
Yr = Yr(p, t): M × C∗→T+
to the Riemann-Hilbert problems associated to the BPS structures (Γ, Zp, Ωp). For each ray r ⊂C∗
we assume that Yr(p, t) is a piecewise holomorphic function, with discontinuities at points p ∈M
where the ray r ⊂C∗is active in the BPS structure (Γ, Zp, Ωp). Diﬀerentiating with respect to t
and translating to the identity 1 ∈T+ we get a map
Y −1
r
· dYr
dt : M × C∗→HomZ(Γ, C).
Composing with the inverse of (23), this can be viewed as a vector ﬁeld V (t) on M depending on
t ∈C∗. A τ-function for the family of solutions Yr(p, t) is a piecewise holomorphic function
τr = τr(p, t): M →C∗,
such that V (t) is the Hamiltonian vector ﬁeld of the function (2πi) · log τr. In terms of the co-
ordinates zi = Z(γi) described above, the condition is that
1
2πi · ∂log Yr,γj
∂t
=
X
i
ǫij
∂log τr
∂zi
.
(24)
By the second symmetry property of Section 4.4 it is natural to also impose the condition that
τ is invariant under simultaneous rescaling of Z and t. In the case when the form ⟨−, −⟩is non-
degenerate this is enough to determine the τ-function uniquely up to multiplication by an element
of C∗.

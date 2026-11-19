---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-046-161-generalities
section_title: "Generalities."
section_number: 16.1
pages: 113-113
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Generalities.
Deﬁnition 16.1.1. If M is a type II1 factor, a central sequence in M is a
norm bounded sequence (xn) with limn→∞||[xn, a]||2 = 0. A central sequence
is said to be trivial if limn→∞||xn −tr(xn)id||2 = 0.
M is said to have
property Γ if there is a central
The collection of all central sequences is clearly a C∗-subalgebra of ℓ∞(N, M).
If ω is a free ultraﬁlter on N, the subalgebra Iω of ℓ∞(N, M) consisting of
sequences with limn→ω ||xn||2 = 0 is a 2-sided ideal of ℓ∞(N, M). Note also
that M is embedded in ℓ∞(N, M) as constant sequences.
Deﬁnition 16.1.2. With notation as above, the ultraproduct of M along ω is
the quotient of ℓ∞(N, M) by Iω. It is written M ω. The algebra of (ω-)central
sequences is the centraliser Mω = M ′ ∩M ω of M in ℓ∞(N, M).
By compactness, the trace on M deﬁnes a trace on M ω by
tr((xn)) = lim
n→ω tr(xn)
and by deﬁnition it is faithful on M ω.
Exercise 16.1.3. Show that the unit ball (in the C∗norm) of M ω is complete
in || −||2 so that M ω and Mω are von Neumann algebras.

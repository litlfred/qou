---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-020-51-koo-saleur-generators-and-lattice-momentum
section_title: "Koo-Saleur generators and lattice momentum"
section_number: 5.1
pages: 22-23
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
Thanks to the smearing of the twist in (22) the Bethe states are invariant under the usual translation operator,
and we can sort them by their (rescaled) lattice momentum p = 0, 1,...,N − 1 deﬁned in (81). We deﬁne the
matrix Ln[N] so that (Ln[N])ab is the matrix element⟨a|Ln[N]|b⟩ of the Koo-Saleur generator Ln[N] between
two Bethe states at system size N. Ln[N] can then be written as a block-diagonal matrix, with the blocks
indexed by values of p. We now show how, thanks to the relations of the aﬃne Temperley-Lieb algebra, only a
few blocks of this matrix can have non-zero elements, namely the ones where the lattice momentum is shifted
by precisely n between|a⟩ and|b⟩.
Recall that by (9) the generator of lattice translation u, fulﬁls ueju−1 = ej+1. Meanwhile, when acting
on a Bethe state |v⟩ belonging to the sector of lattice momentum p, the result is a phase u|v⟩ = ei2πp/N|v⟩.
Together these relations determine the behaviour of Ln|v⟩ under translation. Let us inspect the ﬁrst part of
the j’th term within the expression for Ln (31):
ueinj2π/Nej|v⟩ =einj2π/Nej+1eip2π/N|v⟩ =ei(p−n)2π/Nein(j+1)2π/Nej+1|v⟩. (99)
Up to a phase this is the corresponding part of the ( j + 1)’th term, which can be turned into the j’th by a
relabelling of the indices within the sum. Applying the same procedure to the second part of the j’th term and
summing over j yields in total
u Ln|v⟩ =ei(p−n)2π/N Ln|v⟩, (100)
i.e., we ﬁnd that Ln|v⟩ is also a momentum eigenstate, and will therefore be orthogonal to any Bethe state with
lattice momentum diﬀerent than p−n. In other words: already at ﬁnite size, the conformal spin must change
by the proper integer value when we raise or lower a state using a Koo-Saleur generator.
The relations of the aﬃne Temperley-Lieb algebra can also be used to speed up the numerics by computing
only one term of the sum. Consider the blocks within which the matrix elements ( Ln[N])ab may be non-zero,
i.e., where the Bethe states fulﬁl u|b⟩ =eip2π/N|b⟩ and u|a⟩ =ei(p−n)2π/N|a⟩, respectively. Let us write Ln[N]
as∑
jf(ej,ej+1). By (99) we can shift f(ej,ej+1)|b⟩ to f(ej+1,ej+2)|b⟩ by applying u, at the price of a phase.
Considering the matrix element of a single term and inserting 1 = u−1u, we can let u−1 act to the left. The
phases cancel:
⟨a|u−1uf (ej,ej+1)|b⟩ =e−i(p−n)2π/Nei(p−n)2π/N⟨a|f(ej+1,ej+2)|b⟩. (101)
22
We thus see that all terms give the same contributions to the matrix elements within non-zero blocks of Ln[N],
and we can replace ∑
jf(ej,ej+1) by Nf (ej,ej+1) in the numerical evaluations, gaining a factor N in speed.

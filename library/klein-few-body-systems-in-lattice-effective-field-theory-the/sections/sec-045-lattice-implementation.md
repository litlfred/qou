---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Bonn, November 2018"
section_id: sec-045-lattice-implementation
section_title: "Lattice implementation"
section_number: null
pages: 78-79
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-Body Systems in Lattice Effective Field Theory Dissertation Erlangung des Doktorgrades (Dr. rer. nat.) Mathematisch-Naturwissenschaftlichen Fakultät Rheinischen Friedrich-Wilhelms-Universität Bonn"
---
We now implement our one-dimensional theory of bosons on the lattice. We use lattice units where all
quantities are multiplied by powers of the lattice spacing to form dimensionless combinations. Since
we are interested in methods that can be readily applied to many-body calculations, we work with
energy-independent interactions only. We use anO(a4)-improved free Hamiltonian lattice action,
Hfree = 1
2m
∑
n
2ω0a†(n)a(n) + 1
2m
3∑
l=1
(−1)lωl
[
a†(n + l)a(n) + a†(n)a(n + l)
]
, (6.13)
72

---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-047-64-the-tree-ts
section_title: "The tree Ts"
section_number: 6.4
pages: 41-43
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
The tree Ts
Let (W, S) be an arbitrary Coxeter system. In this section we ﬁx a sequence of
simple reﬂections s = (s1, . . . , sn) ∈Sn and construct a tree Ts.
We construct a perfect binary tree (i.e a tree in which all interior nodes have
exactly two children and all leaves have the same depth) with nodes colored
by Bott-Samelson bimodules and arrows colored by morphisms from parent to
child nodes. We construct it by induction on the depth of the nodes. In depth
zero and one we have the following tree:
41
(Bs1Bs2 · · · Bsn)
ms1⊗idn−1
~
id
"
(Bs2 · · · Bsn)
(Bs1)(Bs2 · · · Bsn)
Let k < n and t = (t1, · · · , ti) ∈Si be such that a node N of depth k −1 is
colored by the bimodule (Bt1 · · · Bti)(Bsk · · · Bsn), then we have two cases.
(1) If we have the inequality l(t1 · · · tisk) > l(t1 · · · ti), then the child nodes
(of depth k) and child edges of N are colored in the following way:
(Bt1 · · · Bti)(Bsk · · · Bsn)
idi⊗msk⊗id
x
id
'
(Bt1 · · · Bti)(Bsk+1 · · · Bsn)
(Bt1 · · · BtiBsk)(Bsk+1 · · · Bsn)
(2) If we have the opposite inequality l(t1 · · · tisk) < l(t1 · · · ti), then the
child nodes (of depth k) and child edges of N are colored in the fol-
lowing way (arrows are the composition of the corresponding pointed
arrows):
(Bt1 · · · Bti)(Bsk · · · Bsn)


F⊗id

Br1 · · · Bri−1BskBsk · · · Bsn
idi−1⊗jsk⊗id

Br1 · · · Bri−1Bsk · · · Bsn
idi−1⊗msk⊗id
w
id
'
(Br1 · · · Bri−1)(Bsk+1 · · · Bsn)
(Br1 · · · Bri−1Bsk)(Bsk+1 · · · Bsn)
The map F is any path morphism from t1 · · · ti taking sk to the right (see
42
Section 6.3). This ﬁnishes the construction of Ts.
By composing the corresponding arrows we can see every leaf of the tree Ts
colored by Bx as a morphism in the space Hom(Bs, Bx). Consider the set
Ls(id), the leaves of Ts that are colored by the bimodule R. In [Li2] the set
Ls(id) is called light leaves basis and the following theorem is proved.
Theorem 6.3
(Nicolas Libedinsky ) The set Ls(id) is a basis of Hom(Bs, R)
as a left R-module.
In the paper [Li2] the leaves colored with R were called light leaves5. Later
this notion was changed in the literature and any leaf in the tree Ts got to be
called a light leaf. We follow this new convention.

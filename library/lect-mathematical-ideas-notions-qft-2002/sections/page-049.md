---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: page-049
section_title: "Page 49"
pages: 49-49
pdf_page: 49
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
text_source: ocr
granularity: page
doc_brief: "Mathematical ideas and notions of quantum field theory — 78 sections: Page 1; Page 2; Page 3"
---
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 49

7.8. Momentum space integration. We saw that the amplitude of a Feynman
diagram is given by an integral over the space of dimension equal to the number of
internal vertices. This is sometimes inconvenient, since even for tree diagrams such
integrals can be rather complicated. However, it turns out that if one passes to
Fourier transforms then Feynman integrals simplify and in particular the number
of integrations for a connected diagram becomes equal to the number of loops (so
for tree diagrams we have no integrations at all).

Namely, we will proceed as follows. Instead of the time variable ¢ we will consider
the dual energy variable E. A function q(t) with compact support will be replaced
by its Fourier transform g(£). Then, by Plancherel formula, for real functions
M1; 42, we have

(ase) = [ aceietBae = [ a(Bae(-B)ae.
R R
This implies that the propagator is given by
1 a
-1 _ _
BA = | pea flB) (BME

The vertex tensors standing at k-valent vertices were 65,=..=s,, So they will be
replaced by 6Q,+...4@,—0, Where Q; are dual variables to s;.

Terminological remark. Physicists refer to the time variables tj,s; as po-
sition variables, and to energy variables E;,Q, as momentum variables, since in
relativistic mechanics (which is the setting we will deal with when we study field
theory) there is no distinction between time and position and between energy and
momentum (due to the action of the Lorenz group).

This shows that the Feynman rules “in momentum space” for a given connected
Feynman diagram [ with n external vertices are as follows.

1. Orient the diagram I, so that all external edges are oriented inwards.

2. Assign variables E; to external edges, and variables Q; to internal ones.
These variables are subject to the linear equations of “the first Kirchhof law”: at
every internal vertex, the sum of the variables corresponding to the incoming edges
equals the sum of those corresponding to the outgoing edges. Let Y(E) be the
space of solutions Q of these equations (it depends on T, but we will not write
the dependence explicitly). It is easy to show that this space is nonempty only if
> E; = 0, and in that case dim Y(E) equals the number of loops of I (show this!).

3. For each external edge, write win and for each internal edge, write 7)
Let ér(E, Q) be the product of all these functions.

4. Define the momentum space amplitude of T to be the distribution Fp(E) on
the hyperplane > E; = 0 defined by the formula

FB. En) = Tau) [P EVO.

J

1
rpm"

We will regard it as a distribution on the space of all n-tuples F,,..., E,, extending

it by zero. It is clear that this distribution is independent on the orientation of I.
Remark. Here we must specify the normalization of the Lebesgue measure on

the space )* E; = 0 and the space Y(E). The first one is just dE)...dE,_;. To

define the second one, let Yz(0) be the set of integer elements in Y(0). Then the

measure on Y(E) is defined in such a way that the volume of Y(E)/Yz(0) is 1.
Now we have

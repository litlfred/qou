---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: page-021
section_title: "Page 21"
pages: 21-21
pdf_page: 21
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
text_source: ocr
granularity: page
doc_brief: "Mathematical ideas and notions of quantum field theory — 78 sections: Page 1; Page 2; Page 3"
---
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 21

3.12. 1-particle irreducible graphs and the Legendre transform. Recall the
notion of Legendre transform.

Let f be a smooth function on a vector space Y, such that the map Y > Y* given
by a > df(a) is a diffeomorphism. Then one can define the Legendre transform of
f as follows. For p € Y%*, let xo(p) be the critical point of the function (p,x) — f(a)
(i.e. the unique solution of the equation df(z) = p). Then the Legenedre transform
of f is the function on Y* defined by

L(f)() = (p. 0) — f (20).

It is easy to see that the differential of L(f) is also a diffeomorphism Y* > Y (in
fact, inverse to df(x)), and that L?(f) = f.

Example. Let f(z) = az?/2. Then px — f = pa — 27/2 has a critical point at
p = 2/a, and the critical value is p?/2a. L(ax?/2) = p?/2a. Similarly, if f(z) =
B(a,x)/2 where B is a nondegenerate symmetric form, then L(f)(p) = B-!(p, p)/2.

Now let us consider Theorem 3.10 in the situation of Theorem 3.2. Thus, S(a) =
B(x, 2)/2+ O(23), and we look at

ZI) = rar [ ee da
Vv
By Theorem 3.10, one has

In(Z(J)/Zo) = —Sesr(xo, J),

where the effective action Seg(2,.J) given by summation over 1-particle irreducible
graphs.

Now, we must. have Seg (x, J) = —J-#+ Sem(a), since the only 1PI graph which
contains 1-valent internal vertices (corresponding to J) is the graph with one edge,
connecting an internal vertex with an external one (so it yields the term —J-2, and
other graphs contain no J-vertices). This shows that In(Z(J)/Zo) is the critical
value of J - « — Seg (x). Thus we have proved the following.

Proposition 3.12. We have
Sea(x) = L(n(Z(J)/Zo)), In(Z(F)/Zo) = L(Ser(x)).
Physicists formulate this result as follows: the effective action is the Legendre

transform of the logarithm of the generating function for quantum correlators (and
vice versa).

4. MATRIX INTEGRALS

Let hw be the space of Hermitian matrices of size N. The inner product on hw
is given by (A, B) = Tr(AB). In this section we will consider integrals of the form

Zy = mee | eo SABA,

where the Lebesgue measure dA is normalized by the condition f eH TA) 2 G4 = 1,
and $(A) = Tr(A?)/2 — 39 JmTr(A™)/m is the action functional.? We will be
interested the behavior of the coefficients of the expansion of Zy in g; for large
N. The study of this behavior will lead us to considering not simply Feynman
graphs, but actually fat (or ribbon) graphs, which are in fact 2-dimensional surfaces.

3Note that we divide by m and not by m!. We will see below why such normalization will be
more convenient.

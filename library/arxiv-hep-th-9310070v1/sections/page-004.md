---
doc_id: arxiv-hep-th-9310070v1
doc_title: "Quantum dilogarithm"
section_id: page-004
section_title: "Page 4"
section_number: null
pages: 4-4
source_pdf: 9310070v1.pdf
source_sha256: b979ebf2f47a4653
toc_source: undetermined
doc_brief: "Quantum dilogarithm — A quantum generalization of Rogers’ ﬁve term, or “pentagon” dilogarithm identity is suggested. It is shown that the classical limit gives usual Rogers’ identity."
---
while the corresponding decompositions of the unity are
1 =
Z +∞
−∞
|q⟩dq⟨q| =
Z +∞
−∞
|p⟩dp
2π¯h⟨p|.
(2.9)
The “q-p” symbol of any operator ˆA, acting in H, is deﬁned as follows:
( ˆA)(q, p) = ⟨q| ˆA|p⟩
⟨q|p⟩.
(2.10)
The symbol of the product of two operators ˆA and ˆB is given by
( ˆA ˆB)(q, p) =
Z +∞
−∞
Z +∞
−∞
dq′dp′
2π¯h exp(i(q −q′)(p′ −p)/¯h)( ˆA)(q, p′)( ˆB)(q′, p).
(2.11)
The symbols of the operators Ψ( ˆU), Ψ( ˆV ), and Ψ(−ˆU ˆV ), with ˆU and ˆV given by (2.6),
have the form
(Ψ( ˆU))(q, p) = Ψ(xq),
(Ψ( ˆV ))(q, p) = Ψ(yp),
(2.12a)
(Ψ(−ˆU ˆV ))(q, p) = 1/Ψ(xqyp),
(2.12b)
where
xq = x exp(αq),
yp = y exp(βp).
(2.13)
Formula (2.12b) can be proven through the use of the following power series expansions
for Ψ(x) and 1/Ψ(x):
Ψ(x) =
∞
X
n=0
θn(n+1)/2(−1)nxn/(θ)n,
1/Ψ(x) =
∞
X
n=0
θnxn/(θ)n,
(2.14)
where
(θ)0 = 1,
(θ)n = (1 −θ)(1 −θ2) . . .(1 −θn),
n ≥1.
(2.15)
Now, we can calculate the symbols of both sides of the quantum identity (2.4), using (2.10)
– (2.12). The result has the form:
Ψ(xq)Ψ(yp)
Ψ(xqyp)
=
Z +∞
−∞
Z +∞
−∞
dq′dp′
2π¯h exp(i(q −q′)(p′ −p)/¯h)Ψ(xq′)Ψ(yp′),
(2.16)
where xq and yp are deﬁned in (2.13). In the classical limit ¯h →0 we can use (1.5) with
ǫ = iαβ¯h
(2.17)
and apply the stationary phase method for evaluation of the integrals in (2.16). Then we
get in the leading order
exp(1
ǫ [L2(xq) + L2(yp) −L2(xqyp)])
= exp(1
ǫ [L2(xq −xqyp
1 −xqyp
) + L2(yp −xqyp
1 −xqyp
) + log( 1 −xq
1 −xqyp
) log( 1 −yp
1 −xqyp
)]),
(2.18)
which is (1.3b) in the exponentiated form.
3

---
doc_id: arxiv-hep-th-9310070v1
doc_title: "September, 1993 Quantum Dilogarithm"
section_id: sec-002-2-quantized-rogers-identity
section_title: "Quantized Rogers’ Identity"
section_number: 2
pages: 3-5
source_pdf: 9310070v1.pdf
source_sha256: b979ebf2f47a4653
doc_brief: "September, 1993 Quantum Dilogarithm — A quantum generalization of Rogers’ ﬁve term, or “pentagon” dilogarithm identity is suggested. It is shown that the classical limit gives usua l Rogers’ identity."
---
Let ˆU and ˆV be two operators, satisfying the Weil algebra:
ˆU ˆV = θ ˆV ˆU . (2.1)
In [6] two relations were proved for function (1.4) with the o perator arguments:
Ψ( ˆU )Ψ( ˆV ) = Ψ( ˆU + ˆV ), (2.2)
and
Ψ( ˆV )Ψ( ˆU ) = Ψ( ˆU − ˆU ˆV + ˆV ). (2.3)
By applying (2.2) twice to the right hand side of (2.3), the la tter can be rewritten as
follows:
Ψ( ˆV )Ψ( ˆU ) = Ψ( ˆU )Ψ( − ˆU ˆV )Ψ( ˆV ). (2.4)
We shall argue that (2.4) is a quantum generalization of (1.3 ) we are looking for. Namely,
we shall show that (1.3) follows from (2.4) in the appropriat e classical limit ¯h → 0. To do
it, we shall write (2.4) in terms of symbols of operators (see for example [7]).
One can realize operators ˆU , ˆV through a pair of coordinate and momentum Hermitian
operators, ˆq and ˆp, satisfying the Heisenberg commutation relations:
[ˆq, ˆp] ≡ ˆq ˆp − ˆpˆq = i¯h. (2.5)
Expressions for ˆU and ˆV have the forms:
ˆU = x exp(αˆq), ˆV = y exp(β ˆp), (2.6)
where x and y are arbitrary complex variables, while complex parameters α and β are such
that:
θ = exp(iαβ¯h). (2.7)
In Hilbert space, H, where operators ˆq and ˆp act, there are two basis sets, {|q⟩}and {|p⟩},
which diagonalize ˆq and ˆp, respectively. We have the following scalar products:
⟨q|q′⟩= δ(q − q′), ⟨q|p⟩= exp(iqp/¯h), ⟨p|p′⟩= 2π¯hδ(p − p′), (2.8)
2
while the corresponding decompositions of the unity are
1 =
∫ +∞
−∞
|q⟩dq⟨q| =
∫ +∞
−∞
|p⟩ dp
2π¯h ⟨p|. (2.9)
The “q-p” symbol of any operator ˆA, acting in H, is deﬁned as follows:
( ˆA)(q, p) = ⟨q| ˆA|p⟩
⟨q|p⟩ . (2.10)
The symbol of the product of two operators ˆA and ˆB is given by
( ˆA ˆB)(q, p) =
∫ +∞
−∞
∫ +∞
−∞
dq′dp′
2π¯h exp(i(q − q′)(p′ − p)/¯h)( ˆA)(q, p′)( ˆB)(q′, p). (2.11)
The symbols of the operators Ψ( ˆU ), Ψ( ˆV ), and Ψ( − ˆU ˆV ), with ˆU and ˆV given by (2.6),
have the form
(Ψ( ˆU))(q, p) = Ψ( xq), (Ψ( ˆV ))(q, p) = Ψ( yp), (2.12a)
(Ψ( − ˆU ˆV ))(q, p) = 1 /Ψ( xqyp), (2.12b)
where
xq = x exp(αq), y p = y exp(βp). (2.13)
Formula (2.12b) can be proven through the use of the following power series e xpansions
for Ψ( x) and 1 /Ψ( x):
Ψ( x) =
∞∑
n=0
θn(n+1)/2(−1)nxn/(θ)n, 1/Ψ( x) =
∞∑
n=0
θnxn/(θ)n, (2.14)
where
(θ)0 = 1, (θ)n = (1 − θ)(1 − θ2) . . .(1 − θn), n ≥ 1. (2.15)
Now, we can calculate the symbols of both sides of the quantum identity (2.4), using (2.10)
– (2.12). The result has the form:
Ψ( xq)Ψ( yp)
Ψ( xqyp) =
∫ +∞
−∞
∫ +∞
−∞
dq′dp′
2π¯h exp(i(q − q′)(p′ − p)/¯h)Ψ( xq′)Ψ( yp′ ), (2.16)
where xq and yp are deﬁned in (2.13). In the classical limit ¯ h → 0 we can use (1.5) with
ǫ = iαβ¯h (2.17)
and apply the stationary phase method for evaluation of the i ntegrals in (2.16). Then we
get in the leading order
exp( 1
ǫ [L2(xq) + L2(yp) − L2(xqyp)])
= exp(1
ǫ [L2( xq − xqyp
1 − xqyp
) + L2( yp − xqyp
1 − xqyp
) + log( 1 − xq
1 − xqyp
) log( 1 − yp
1 − xqyp
)]),
(2.18)
which is (1 .3b) in the exponentiated form.
3

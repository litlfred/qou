---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-015-34-resonance
section_title: "Resonance"
section_number: 3.4
pages: 29-30
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
equation (
11), i.e., the case where at least one of the ratios ai/aj (for i ⁄= j), bi/bj (for i ⁄= j)
or ai/bj (for some i and j) is an integer power of q. For simplicity, we will consider only the
case of r = 2, although our arguments remain valid for all r. When r = 2, the system of
equations ( 108) is given by
(1 − t)f (t, a, b, c, q ) − (q−1c + 1 − t(a + b))f (qt, a, b, c, q ) + (q−1c − tab)f (q2t, a, b, c, q ) = 0
f (t, q −1a, b, c, q ) − q−1af (qt, q −1a, b, c, q ) − (1 − q−1a)f (t, a, b, c, q ) = 0
f (t, a, q −1b, c, q ) − q−1bf (qt, a, q −1b, c, q ) − (1 − q−1b)f (t, a, b, c, q ) = 0
f (t, a, b, c, q ) − q−1cf (qt, a, b, c, q ) − (1 − q−1c)f (t, a, b, q −1c, q ) = 0 ,
(140)
with Equation ( 1) being one such solution. We can specialise a, b, c so that some of a, b,
c, a/b, a/c or b/c lies in q
/CI
. All of these conditions can be seen to be special points of
the monodromy matrix ( 18) and various special properties of the equations appear like, for
example, submodules.
We now present two examples of these special points in the simplest c ase or r = 2. These
can all be deduced from Theorem 1.4.
• b = c. The ﬁrst Equation ( 140) now takes the form
(1 − q−1bσt) ((1 − σt) − t(1 − aσt))
=
(
(1 − σt)(1 − q−1bσt) − t(1 − aσt)(1 − bσt)
)
f
= 0 .
(141)
This has normalised solutions
f (1)(t, a, b, q) =
∞∑
k=0
(a; q)k
(q; q)k
tk
f (qb−1)(t, a, b, q) = (a; q)∞(q2b−1; q)∞θ(q−1bt; q)(q; q)2
∞
(qab−1; q)∞θ(q−1b; q)θ(t; q)
∞∑
k=0
(qab−1; q)k
(q2b−1; q)k
tk .
(142)
Note that the ﬁrst generates a submodule and indeed satisﬁes
(
((1 − σt) − t(1 − aσt)) f (1))
(t, q) = (1 −t)f (1)(t, a, b, q) −(1 −at)f (1)(qt, a, b, q) = 0 . (143)
30 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
We note that for the value at t = 0 and the q-diﬀerence equation we see that
f (1)(t, a, b, q) = (at; q)∞
(t; q)∞
(144)
a classical result known as the q-binomial theorem. From Theorem 1.5 or even Theorem 1.4
with r = 1, we then see that this is a modular q-holonomic submodule. Now the second
solution satisﬁes the inhomogeneous equation
(1−t)f (qb−1)(t, a, b, q)−(1−at)f (qb−1 )(qt, a, b, q) = (a; q)∞(q2b−1; q)∞θ(q−1bt; q)(q; q)2
∞
(qab−1; q)∞θ(q−1b; q)θ(t; q) (145)
where we note that the RHS is of course annihilated by (1 − q−1bσt). The full module can
then be shown to be modular using elementary functions holomorphic for τ ∈ /BV
′ times the
state integral ∫
C
Φ b(x)
Φ b(x + ib−1α)
exp
(
−2π zx
b
)
1 + ˜q1/2 exp
(
−2π x
b
)
e(β/τ ) dx . (146)
Note that this state integral is of course the same as the one in Equ ation ( 134) where
β1 = γ = β + 1 = α2 + 1.
• c = q. The ﬁrst Equation ( 140) now takes the form
(1 − t)f (t, a, b, q) − (2 − t(a + b))f (qt, a, b, q) + (1 − tab)f (q2t, a, b, q) = 0 . (147)
Notice that this now has indicial polynomial (1 − ρ)2. Therefore, we expand using the
Frobenius method to ﬁnd solutions which are the coeﬃcients of ε in the expansion to order
O(ε2) of
f (1,0)(t, a, b, q) = (qeε; q)2
∞
(aeε; q)∞(beε; q)∞
∞∑
k=0
(aeε; q)k(beε; q)k
(qeε; q)2
k
tk θ(e−εt; q)
θ(t; q)
= f (1,0)(t, a, b, q) + f (1,1)(t, a, b, q)ε + O(ε2) .
(148)
Then considering the state integral
∫
C
Φ b(x)2
Φ b(x + ib−1α)Φ b(x + ib−1β) exp
(
−2π zx
b
)
dx . (149)
along with Equation ( 52) we can show that the module is modular with this special value.

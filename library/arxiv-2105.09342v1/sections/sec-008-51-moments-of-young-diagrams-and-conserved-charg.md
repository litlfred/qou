---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-008-51-moments-of-young-diagrams-and-conserved-charg
section_title: "Moments of Young diagrams and conserved charges"
section_number: 5.1
pages: 18-19
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
doc_brief: "A Unitary Matrix Model for q-deformed Plancherel Growth — In this paper we construct a unitary matrix model that captures the asymptotic growth of Young diagrams under q-deformed Plancherel measure."
---
Following [24] one can deﬁne an inﬁnite sequence of conserved commuting quantities
Hn = 1
2π
∫
dh dθ ω(h,θ ) hn. (5.8)
18
Using the Poisson bracket (D.10) one can show that
{Hm,Hn} = 0. (5.9)
Also, using the equations of motion (D.8) one can show that
dHn
dt = 0. (5.10)
Existence of inﬁnite number of conserved charges makes the system integrable. This is a
generic feature of one matrix model and indicates that the theory is exactly solvable.
These conserved charges are related to moments of Young diagrams deﬁned in [5]. The
matrix model techniques can be used to calculate the moments of automodel diagrams.
Using the deﬁnitions (3.39), one can show that
Hn =
∫
dh u(h) hn. (5.11)
One can deﬁne a generating function for these moments
H(h) =
∫
dh′ u(h′)
h−h′ =
∞∑
n=0
Hn
hn+1. (5.12)
Using the expression for the resolvent (3.22) and the relation between h and w (3.16), one
can show that
Hn =
∑
i1,···,in≥1
λi1+···+ιn−n
i1··· in
pi1+···+in (5.13)
where pns are the moments associated with H(w),
H(w) =
∞∑
n=0
pn
wn+1. (5.14)
Since we know the exact expression forH(w), one can easily ﬁnd thepns from it’s asymptotic
expansion. In the limit λ→ 0, we get
Hn =pn. (5.15)
Thus, we have an explicit formula to compute the moments of the asymptotic automodel
diagrams.

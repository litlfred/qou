---
doc_id: czechmathj-60-2010-1-4
doc_title: "Czechoslovak Mathematical Journal"
section_id: page-009
section_title: "Page 9"
section_number: null
pages: 9-9
source_pdf: CzechMathJ_60-2010-1_4.pdf
source_sha256: 7595f81d1398d0bf
toc_source: undetermined
doc_brief: "Czechoslovak Mathematical Journal — 19 sections: Page 1; Page 2; Page 3"
---
(2) We consider k⟨X⟩as a free k⟨X⟩-module having one generator e. Then (S, T )
is a Gröbner-Shirshov pair for the A-module M = A/A(T + Id(S)), where
A = k⟨X|S⟩if and only if S is a Gröbner-Shirshov basis in the algebra k⟨X⟩
with respect to the ordering < and (SX∗∪T )e is a Gröbner-Shirshov basis in
the free module modk⟨X⟩⟨e⟩with respect to the ordering ≺.
P r o o f.
(1) Suppose that S is a Gröbner-Shirshov basis in k⟨X⟩. We shall prove
that all compositions in SX∗Y are trivial modulo SX∗Y . For any f, g ∈SX∗Y ,
let f = s1a1y, g = s2a2y, s1, s2 ∈S, a1, a2 ∈X∗, y ∈Y and w = f = ag. Then
¯s1a1 = a¯s2a2. Since S is a Gröbner-Shirshov basis in k⟨X⟩, we have
(f, g)w = f −ag = s1a1y −as2a2y = (s1a1 −as2a2)y =
X
(αiuirivi)y,
where ui, vi ∈X∗, ri ∈S and ui¯riviy ≺w. Thus, every composition is trivial modulo
SX∗Y and hence, SX∗Y is a Gröbner-Shirshov basis in modk⟨X⟩⟨Y ⟩. Conversely,
assume that SX∗Y is a Gröbner-Shirshov basis in the module modk⟨X⟩⟨Y ⟩. For any
f, g ∈S and w = fa = bg, we have w1 = fay = bgy and
(fay, bgy)w1 = (fa −bg)y =
X
αi(airi)y,
where αi ∈k, ri = sibi, ai, bi ∈X∗, si ∈S and ai¯riy ≺w1. Then
(f, g)w = fa −bg =
X
αiaisibi
with ai¯sibi < w. This shows that each composition of intersection in S is trivial mod-
ulo S. Similarly, every composition of inclusion in S is trivial modulo S. Therefore,
S is indeed a Gröbner-Shirshov basis in k⟨X⟩.
(2) The results follow directly from Deﬁnitions 2.6 and 3.1.
□
Remark. By Theorem 3.4 it is clear that Theorem 2.7 follows from Lemma 3.2.
4. Highest weight modules over sl2
In this section we give a Gröbner-Shirshov basis for the highest weight module over
sl2. By using this result and Lemma 3.2, we re-prove that the highest weight module
over sl2 is irreducible (see [13]) and show that any ﬁnite dimensional irreducible
sl2-module has the presentation (∗∗) given below.
Let X = {x, y, h} and let sl2 = Lie(X|S) be a Lie algebra over a ﬁeld k with
chk = 0, where
x =
 0
1
0
0

, y =
 0
0
1
0

, h =
 1
0
0
−1

and S = {[hx]−2x, [hy]+2y, [xy]−h}.
66

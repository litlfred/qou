---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-018-431-properties-under-conjugation-and-parity-impl
section_title: "Properties under conjugation and parity, implications for the modules"
section_number: 4.3.1
pages: 21-22
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
The site dependence of the form factors does not depend on the choice of operators and can be factorized in
the expressions. Following the notation in Appendix B we let FO1···Oj denote the site-independent part of the
form factor for j neighboring operators O1··· Oj. We wish to ﬁnd relations between the site-independent part
of the form factors of interest.
The ﬁrst type of relations between the site-independent part of the form factors of interest is due to conju-
gation. The dual states of on-shell Bethe states are, up to a possible phase 9, their conjugates,
⟨{λ}| = (phase)
(
|{λ}⟩
)†
. (90)
Combining this relation with
(σ+)† =σ−, (σz)† =σz (91)
we obtain
⟨{µ}|σ+
mσz
m+1σ−
m+2|{λ}⟩ = (phase)
(
⟨{λ}|σ−
mσz
m+1σ+
m+2|{µ}⟩
)∗
, (92a)
⟨{µ}|σz
mσ+
m+1σ−
m+2|{λ}⟩ = (phase)
(
⟨{λ}|σz
mσ−
m+1σ+
m+2|{µ}⟩
)∗
, (92b)
which relate Fσ+σzσ− to Fσ−σzσ+ and Fσzσ+σ− to Fσzσ−σ+ through the conjugation of each of the operators.
Similarly we can relate Fσ+σ− to Fσ−σ+.
The second type of relations between the site-independent part of the form factors of interest is due to parity.
Following [53] we denote by Π the parity operator. It acts on a local operator Xm as
ΠXmΠ−1 =XN+1−m (93)
and on the B-operators as
ΠB(λ)Π−1 = (−1)N−1B(−λ). (94)
Thus, parity will act on Bethe states by taking|{λ}⟩ into|{−λ}⟩ (up to a possible sign) and act onj neighboring
operators by reversing their order and the sites they act on. We obtain
⟨{µ}|σ−
mσ+
m+1σz
m+2|{λ}⟩ = (sign) ⟨{−µ}|σz
N−m−1σ+
N−mσ−
N−m+1|{−λ}⟩, (95a)
⟨{µ}|σ+
mσ−
m+1σz
m+2|{λ}⟩ = (sign) ⟨{−µ}|σz
N−m−1σ−
N−mσ+
N−m+1|{−λ}⟩, (95b)
which relate Fσ−σ+σz toFσzσ+σ− andFσ+σ−σz toFσzσ−σ+ through reversing the order of the operators. Alto-
gether, the combined actions of conjugation and parity relate the four form factors (88) among themselves, and
similarly for the remaining two (89). Thus, the only form factors involving three operators that we shall need
to compute in Appendix B will be one of each group, here chosen to be Fσzσ−σ+ and Fσ−σzσ+.
Combining the expression for the Koo-Saleur generators (31) with the parity relations for the form factors
yields relations for the matrix elements of Ln in the basis of Bethe states. In particular, we note that the term
[ej,ej+1] in (31) will pick up a sign when the order of all operators is reversed, changing Ln into ¯L−n. Thus
we have
⟨{µ}|Ln|{λ}⟩ =⟨{−λ}| ¯L−n|{−µ}⟩. (96)
Meanwhile, the pairs of conjugate states in a given sector of Sz are, as discussed in Section 4.2, related through
a change of signs for all the Bethe roots, which is precisely the action of parity on states as seen in (94). Taken
9In the numerics below, the phase is found for a given scaling state at smallN, by explicitly comparing its dual with its conjugate,
and stays the same as N is increased.
21
together, we ﬁnd in particular that (86a) and (86b) can be turned into a much stronger statement:
Strong duality: Let Vα,¯α,V ¯αc,αc and W,W c be a pair of conjugate primary states and their respective
null states, as deﬁned in connection to (86a)–(86b), and Ar,s the corresponding combination of Virasoro
generators. We here denote the corresponding scaling states and lattice operators by calligraphic letters,
e.g. V[N]α,¯α. At each ﬁnite size N—large enough to accommodate the states of interest—we have the
following equality of the matrix elements:
⟨W[N]|Ar,s[N]|Vα,¯α[N]⟩ = (phase)⟨V¯αc,αc[N]| ¯A‡
r,s[N]|Wc[N]⟩. (97a)
The same type of duality holds when Vα,¯α has a degenerate anti-chiral charge ¯α =αr,s or ¯α =αc
r,s:
⟨W[N]| ¯Ar,s[N]|Vα,¯α[N]⟩ = (phase)⟨V¯αc,αc[N]|A‡
r,s[N]|W
c
[N]⟩. (97b)
Examples of this situation are seen in the numerical results, in Tables 3 and 10.
The considerations above hold for the matrix elements of single Temperley-Lieb generators as well, because
of translational invariance (to be discussed in the next section):
⟨{µ}|ej|{λ}⟩ = (phase)⟨{−λ}|ej|{−µ}⟩. (98)
This is in agreement with the result for the modules W0,q−2 and W0,q2 discussed in the end of Section 4.2. Of
the previous examples mentioned, Table 10 has exact results at ﬁnite size coming from the Temperley-Lieb
structure.

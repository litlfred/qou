---
doc_id: arxiv-1203.4538v1
doc_title: "The exponential-logarithmic equivalence classes of surreal numbers"
section_id: sec-001-2-preliminaries-on-surreal-numbers
section_title: "Preliminaries on surreal numbers."
section_number: 2
pages: 2-6
source_pdf: 1203.4538v1.pdf
source_sha256: 5e44909e355c78d6
doc_brief: "The exponential-logarithmic equivalence classes of surreal numbers — 7 sections: Introduction.; Preliminaries on surreal numbers.; Sign sequences."
---
2.1 Inductive deﬁnitions.
This section is dedicated to ﬁx the notations and recall some of the deﬁnitions and
results obtained in [
Con01] and [ Gon86]. We will also use results from [ Ehr01] and
[vdDE01].
We denote by On the proper class of ordinal numbers. A surreal number is any
map a : α → {⊖ , ⊕} where α ∈ On. Any surreal may be canonically represented as a
sequence of pluses and minuses called its sign sequence. The ordinal α on which the
surreal number a is deﬁned is called its length. Set l(a) := α. The proper class of all
surreal numbers is denoted by No.
It is totally ordered as follows. Let a and b be any two surreal numbers with l(a) ≤
l(b). Consider the sign sequence of a completed with 0’s so that the two sign sequences
have same length. Then consider the lexicographical order between them, denoted by
≤, based on the following relation:
⊖ < 0 < ⊕.
A subset of No is said to be initial if it is made of surreals whose lengths are less
than or equal to a given ordinal. As in [ Ehr01], No is endowed with a partial ordering
called the simplicity :
a is simpler than b, write a <s b ⇔ a is a proper initial segment of b.
Given a surreal a ∈ No, any surreal number a′ <s a is called a truncation of a.
The construction of surreal numbers makes heavy use of the ke y idea of "cuts be-
tween sets" in the classical construction of real numbers. T ake two pairs ( L, R) (as
"Left" and "Right") and ( L′, R′) of subsets of No with L < R and L′ < R′. ( L′, R′) is
said to be coﬁnal in (L, R) if for any (a, b) ∈ L × R, there is (a′, b′) ∈ L′ × R′, such that
a < a′ < b′ < b. Note that coﬁnality is a transitive relation. The followin g results are
fundamental. In particular, given a surreal a ∈ No, we will considere the pair ( La, Ra)
where La = {b ∈ No ; b < a and b <s a} and Ra = {b ∈ No ; b > a and b <s a}.
2
Theorem 2.1 (Existence and coﬁnality) 1. [ Gon86, Theorem 2.1] For any pair
(L, R) with L < R, there exists a unique surreal a ∈ No of minimal length such
that L < a < R. We set ⟨L|R⟩:= a ∈ No, and call it the cut between L and R.
2. [ Gon86, Theorem 2.6] Suppose that ⟨L | R⟩= a ∈ No, L′ < a < R′ for some pair
(L′, R′) coﬁnal in (L, R), then ⟨L′ | R′⟩= a.
3. [ Gon86, Theorems 2.8 and 2.9] One always has a = ⟨La | Ra⟩and, for any cut
⟨L′ | R′⟩= a, then (L′, R′) is coﬁnal in (La, Ra).
Deﬁnition 2.2 This representation a = ⟨La | Ra⟩of a is called its canonical cut. By
abuse of notation, we also denote the canonical cut by a = ⟨aL | aR⟩where aL and aR
are general elements of the canonical sets La and Ra (e.g. aL = n if La = N).
The preceding results allow to deﬁne maps and operations on s urreal numbers re-
cursively, that is by induction on the length of the surreals considere d since aL and aR
are simpler than a. Concerning the algebraic structure of No, we have:
Theorem 2.3 1. [ Gon86, Theorems 3.3, 3.6, 3.7 and Ch. 5, Sect. D] The proper
class No endowed with its lexicographical ordering ≤ and the following opera-
tions, is a real closed ﬁeld (in the sense of proper classes): for any a, b ∈ No,
addition: a + b := ⟨aL + b, a + bL | aR + b, a + bR⟩
neutral element : 0 = ⟨∅ | ∅⟩;
multiplication: a.b := ⟨aL.b + a.bL − aL.bL, aR.b + a.bR − aR.bR |
aL.b + a.bR − aL.bR, aR.b + a.bL − aR.bL⟩
neutral element : 1 = ⊕ = ⟨0 | ∅⟩.
2. [ Ehr01, Theorems 9 and 19] Any divisible ordered abelian group, res pectively
any real closed ﬁeld, is isomorphic to an initial subgroup of(No, +), respectively
an initial subﬁeld of (No, +, .).
Note that Gonshor proves also, for the cited operations as we ll as for the following
maps, the so-called uniformity properties [Gon86, Theorems 3.2, 3.5 etc.]. For ex-
ample in the case of the addition, this means that a + b may be obtained by taking any
cuts a = ⟨L | R⟩and b = ⟨L′ | R′⟩instead of taking their canonical cuts, and applying
the same formula as above. In other words, the formulas do not depend on the cuts for
which aL, aR, bL, bR are general elements.
Any real number is identiﬁed to the sign sequence corresponding to its binar y
expansion. Thus they are the sequences of length ﬁnite or equ al to ω, the later being
non ultimately constant. These sequences form a subﬁeld of t he surreals having the
least upper bound property, i.e. a copy of the ordered set of the reals: R ⊂ No.
Surreal numbers a ∈ No such that a > R or a < R are called inﬁnitely large: we
denote by No≫1 their proper class. Those that verify 0 < a < R>0 or 0 > a > R<0 are
called inﬁnitesimals: we denote by No≪1 their proper class.
Any ordinal number α ∈ On is identiﬁed to the surreal number whose sign se-
quence is a sequence of ⊕’s of length α. The operations precedingly deﬁned on the
3
surreal numbers correspond to the natural sum and product (see e.g. [ Hau44]). So
we consider On ⊂ No.
In the following theorem, we sum up the main results about the so-called Conway
normal form of a surreal number:
Theorem 2.4 (Conway normal form) 1. [ Gon86, Theorems 5.1 to 5.4] The re-
cursive formula:
∀a ∈ No, ωa := ⟨0, n.ωaL
| ωaR
/2n}
(where it is understood that n ∈ N), deﬁnes a map:
Ω: No → No
a ↦→Ω(a) := ωa
with values in No>0 and that extends the exponentiation with base ω of the ordi-
nals. Moreover, for any a ∈ No, ωa is the representative of minimal length of its
Archimedean equivalence class (∀x, y ∈ No>0, x ∼arch y ⇔ ∃n ∈ N, n.x ≥ y ≥
x/n).
2. [ Gon86, Theorems 5.5 to 5.8] The ﬁeld of surreals is a ﬁeld ofgeneralized series
[KM12, Deﬁnition 2.5] in the following sense: any surreal number a ∈ No can
be written uniquely as a =
∑
i<λ
ωairi where the transﬁnite sequence (ai)i<λ is
strictly decreasing and, for any i, r i ∈ R \ {0}. In particular, ωNo is seen as the
group of (generalized) monomials:
No = R((ωNo)).
In particular, the proper class ωNo is a complete system of representatives of the
Archimedean equivalence classes of No>0, each of its elements being the reprensenta-
tive of minimal length in its class.
Moreover, note that the map denoted by Ind in [Gon86], which sends any surreal
a to the exponent a0 of the leading monomial of its normal form, is a valuation. It is
the natural valuation of the real closed ﬁeld No [Kuh00]. In particular, Ind(ωa) = a for
any a ∈ No.
We deduce immediately that No is a Hahn ﬁeld of series [Hah07] in the following
sense:
Proposition 2.5 1. For any a ∈ No, ωωa
is the representative of minimal length
in its equivalence class of comparability (∀x, y ∈ No≫1
>0 , x ∼comp y ⇔ (∃n ∈
N, xn ≥ y ≥ x1/n, and we set 1/x ∼comp x).
2. Any surreal a ∈ No can be written uniquely a =
∑
i<λ








∏
j<λi
(
ωωbi, j
) si, j







 ri where,
for any i, we identify
∏
j<λi
(
ωωbi, j
) si, j
= ωai where ai =
∑
j∈λi
ωbi, j (so the tranﬁnite
4
sequences (ai)i<λ and for any i, (bi, j) j<λi, are strictly decreasing, and for any i, j,
si, j, ri ∈ R\{0}). In particular, we callωωNo
the chain offundamental monomials
of No [KM12, Deﬁnition 2.2]:
No = R
(( (
ωωNo ) R))
.
The proper class ωωNo
is a complete set of representatives of the comparability
classes of No≫1
>0 , each of its elements being the one of minimal length in its class.
Following the ideas of Conway, Gonshor described also a proper class of general-
ized epsilon numbers [Con01, p.35]:
Theorem 2.6 The recursive formula:
∀a ∈ No, ǫa := ⟨Ωn(1), Ωn(ǫaL + 1) | Ωn(ǫaR − 1)}
(where it is understood that n ∈ N), deﬁnes a map:
ǫ : No → No
a ↦→ ǫ(a) := ǫa
with values in No≫1
>0 bigger than Ωn(1) for any n, and which extends the classical
epsilon numbers map on ordinals [ Sie65]. Moreover, ǫ(No) is the proper class of all
the ﬁxed points of the map Ω:
∀a ∈ No, ω ǫa = ǫa.
Gonshor deﬁnes inductively in [ Gon86] an exponential map exp : ( No, +) →
(No>0, .) which is surjective (and consequently its inverse, the logarithmic map log :
(No>0, .) → (No, +)) using the Taylor expansion of the real exponential map. Here we
give only the results we will need in this article:
Theorem 2.7 The exponential map exp : No → No>0 and its inverse log : No>0 →
No, coincide on the real numbers with the usual real exponential and logarithmic maps,
and are such that:
1. for any a ∈ No, exp(
∑
i<λ
ωairi) = ω
∑
i<λ ωg(ai)ri
where g (a) : = ⟨Ind(a), g(aL) | g(aR)⟩;
2. for any b ∈ No, log(
∏
j<λ
(
ωωb j
) s j
) =
∑
j<λ
ωh(b j)
where h (b) : = ⟨0, h(bL) | h(bR), ω b/2n⟩.
We have exp = log−1 and h = g−1 on No.
Note that g is not deﬁned at 0.
5

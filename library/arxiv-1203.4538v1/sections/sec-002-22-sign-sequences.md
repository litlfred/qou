---
doc_id: arxiv-1203.4538v1
doc_title: "The exponential-logarithmic equivalence classes of surreal numbers"
section_id: sec-002-22-sign-sequences
section_title: "Sign sequences."
section_number: 2.2
pages: 6-7
source_pdf: 1203.4538v1.pdf
source_sha256: 5e44909e355c78d6
doc_brief: "The exponential-logarithmic equivalence classes of surreal numbers — 7 sections: Introduction.; Preliminaries on surreal numbers.; Sign sequences."
---
Gonshor obtains in [
Gon86] detailed results on the sign sequences of the surreals under
the various operations and maps. We will use repeatedly his r esults. Moreover, we
introduce in this section some new operations on the sign sequences.
Deﬁnition 2.8 •Given two surreal numbers a, b ∈ No, we deﬁne their concate-
nation a/binampersandb as the juxtaposition of their sign sequences. We note that l(a/binampersandb) =
l(a) + l(b), the ordinal sum of l(a) and l(b).
•As in [ Gon86, Theorem 9.5], for any surreal number a ∈ No, we can write its
sign sequence as the following transﬁnite concatenation:
a = α0 ⊕ /binampersandβ0 ⊖ /binampersandα1 ⊕ /binampersandβ1 ⊖ /binampersand· · ·
where for any µ ∈ On used in this writing of a, we have αµ, β µ ∈ On with in
particular αµ possibly 0 for µ = 0 or for any limit ordinal µ.
•Given a surreal number a ∈ No, we denote by a+ the total number of pluses in
the sign sequence of a (a+ ∈ No). Therefore is the ordinal sum of the packages
of ⊕’s:
a+ =
∑
µ
αµ = /binampersandµ(αµ⊕).
•Given a positive surreal number a ∈ No>0, we derive from it the surreal number
♭a obtained by suppressing the ﬁrst ⊕ in the sign sequence of a.
Given a negative surreal number a ∈ No<0, we derive from it the surreal number
♯a obtained by suppressing the ﬁrst ⊖ in the sign sequence of a.
•Given a surreal number in normal form
∑
i<λ
ωai .ri, we deﬁne its corresponding
reduced sequence (a0
i )i<λ as follows. For any i < λ , a0
i is derived from ai by
suppressing in its sign sequence the following ⊖’s:
– given an ordinal number ν ∈ On, if ai(ν) = ⊖ and if there exists j < i such
that a j(ξ) = ai(ξ) for any ξ ≤ ν, then suppress the νth ⊖;
– if i is a successor ordinal, ai−1/binampersand⊖ is a truncation of ai and if ri−1 is not
a dyadic rationnal number, then suppress the ⊖ coming after ai−1 in the
writing of ai.
Concerning the exponentiation with base ω, we recall [
Gon86, Theorem 5.12 and
Corollary 5.1]:
Theorem 2.9 •Given a surreal number a = α0 ⊕ /binampersandβ0 ⊖ /binampersandα1 ⊕ /binampersandβ1 ⊖ /binampersand· · ·, for
any ordinal µ ∈ On intervening in the writing of a, we set γµ :=
∑
λ≤µ
αλ (ordinal
sum). Then the sign sequence of ωa is:
ωa = ωγ0 ⊕ /binampersandωγ0+1β0 ⊖ /binampersandωγ1 ⊕ /binampersandωγ1+1β1 ⊖ /binampersand· · ·
6
•Given a positive real number r = ρ0 ⊕ /binampersandσ0 ⊖ /binampersand· · ·, the sign sequence of ωa.r is
ωa.r = ωa/binampersandωa+
♭ρ0 ⊕ /binampersandωa+
σ0 ⊖ /binampersandωa+
ρ1 ⊕ /binampersandωa+
σ1/binampersand· · ·
(ordinal multiplication). If r is negative, reverse all the signs in the preceding
sequence.
•Given a surreal number in normal form
∑
i<λ
ωai .ri, its sign sequence is:
/binampersandi<λωa0
i .ri
where (a0
i )i<λ is the corresponding reduced sequence.

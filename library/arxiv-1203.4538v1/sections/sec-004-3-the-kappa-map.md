---
doc_id: arxiv-1203.4538v1
doc_title: "The exponential-logarithmic equivalence classes of surreal numbers"
section_id: sec-004-3-the-kappa-map
section_title: "The kappa map."
section_number: 3
pages: 7-9
source_pdf: 1203.4538v1.pdf
source_sha256: 5e44909e355c78d6
doc_brief: "The exponential-logarithmic equivalence classes of surreal numbers — 7 sections: Introduction.; Preliminaries on surreal numbers.; Sign sequences."
---
In this section we deﬁne and describe a new mapκ, which takes naturally place between
the Conway-Gonshor maps Ωand ǫ (see Remark
4.5). As in [ Kuh00, Remark 3.20],
we introduce the notion of exponential equivalence relation for surreal numbers. Set
expn and logn for the nth iterate of the corresponding maps.
Deﬁnition 3.1 We set :
•the exponential equivalence relation to be:
∀x, y ∈ NO≫1, x ∼exp y ⇔ ∃n ∈ N, logn(|x|) ≤ |y| ≤ expn(|x|);
•the exponential comparison relation to be:
∀x, y ∈ NO≫1, x ≫exp y ⇔ ∀n, logn(|x|) > |y|.
7
Theorem 3.2 The recursive formula
∀a ∈ No, κ (a) = κa := ⟨expn(0), expn(κaL) | logn(κaR)⟩
(where it is understood that n ∈ N) deﬁnes a map
κ : No → No
a ↦→κ(a) := κa
with values in No≫1
>0 and such that:
(i) for any a, b ∈ No, a < b ⇒ κa ≪exp κb;
(ii) there is a uniformity property for this formula (i.e. the recursive formula does not
depend on the choice of the cut for a).
Proof. We proceed by transﬁnite induction on the length of the surre als considered.
For l(a) = 0, i.e. a = 0 = ⟨∅|∅⟩, we have:
κ0 := ⟨expn(0) | ∅⟩
= ⟨n | ∅⟩by coﬁnality
= ω.
We consider a ∈ No with l(a) > 0, and suppose that the theorem holds for any
b ∈ No with l(b) < l(a). Consider a canonical representation a = ⟨aL | aR⟩of a. By
the induction hypothesis, since κaL > R and κaL ≪exp κaR, for any n ∈ N we have
expn(0) < expn(κaL) < logn(κaR). Thus the recursive formula for κa is well deﬁned.
Moreover, since exp n(0) for n ∈ N is coﬁnal in R and is always part of the lower
elements in the recursive formula, we have κa > R, meaning that κa ∈ No≫1
>0 for any
a ∈ No.
(i) To show the property a < b ⇒ κa ≪exp κb, we proceed as in [Gon86, Theorems
3.1, 3.4 et 5.2] by induction on the natural sum ofl(a) and l(b). So we consider a < b in
No. We denote byc the common initial segment ofa and b. There are two cases. Either
c = a or b: in this case, the property follows directly from the recursive deﬁnition of κ,
since a = bL or b = aR respectively. Or we have a < c < b with c <s a and c <s b.
Then the natural sum of a and c, and of b and c, is less than the one of a and b. By the
induction hypothesis, we obtain that κa ≪exp κc and κc <exp κb, so κa ≪exp κb.
(ii) Concerning the uniformity property, we refer to [ Gon86, Theorems 3.2, 3.5,
Corollary to Theorem 5.2 etc]. Let a = ⟨L | R⟩ ∈No. By Theorem 2.1 (3.), ( L, R)
is coﬁnal in the canonical cut ( La, Ra) of a. By the preceding property, it implies that
(κ(L), κ(R)) and (κ(La), κ(Ra)) are coﬁnals, and that κ(L) ≪exp κa ≪exp κ(R) ⇒ κ(L) <
κa < κ (R) (these inequalities concern elements in No≫1
>0 ). So we can apply Theorem
2.1 (2.) to obtain κa = ⟨κ(La) | κ(Ra)⟩= ⟨κ(L) | κ(R)⟩. □
Example 3.3 We compute some particular values:
κ1 := ⟨expn(0), expn(ω) | ∅⟩
= ⟨Ωn(ω) | ∅⟩by coﬁnality
= ǫ0 ;
κ−1 := ⟨expn(0), | logn(ω)⟩
= ⟨n | ωω−n
⟩by coﬁnality
= ωω−ω
;
8
Theorem 3.4 A surreal number b ∈ No is of the form κa for some a ∈ No if and only if
b is the representative of minimal length in an exponential equivalence class.
Proof. We got inspired by [Gon86, Theorem 5.3].
Consider a, b ∈ No such that b ∼exp κa ⇔ ∃n ∈ N, logn(x) ≤ y ≤ expn(x). So we have
expn(0) ≪exp b and expn(κaL) ≪exp b ≪exp logn(κaR) for any n ∈ N. So κa is an initial
part of b.
Conversely, we show by transﬁnite induction onl(b) ∈ On that for any b ∈ No≫1
>0 , there
exists a ∈ No such that b ∼exp κa. First, by (ii) of Theorem 3.2, we note that a is unique
whenever it exists.
One has ω = κ0.
Consider b = ⟨Lb | Rb⟩ ∈No≫1
>0 with l(b) > ω and suppose that for any c ∈ No with
l(c) < l(b) the desired property holds. So, for any c ∈ Lb ∪ Rb, we have c ∼exp κd
for some d ∈ No. Let L := {d ∈ No | ∃c ∈ Lb, c ∼exp κd} and R := {d ∈ No | ∃c ∈
Rb, c ∼exp κd}. Suppose that L ∩ R /nequal∅. We consider d ∈ L ∩ R. So there exist c1 ∈ Lb
and c2 ∈ Rb such that c1 ∼exp κd and c2 ∼exp κd. Since c1 < c < c2, it follows that
c ∼exp κd.
Suppose now that L ∩R = ∅. We have L < R (if not we would haved1 > d2 ⇒ κd1 ≫exp
κd2 ⇒ c1 > c2 with c1 ∈ Lb and c2 ∈ Rb). Note that, by deﬁnition, κ(L), respectively
κ(R), is a complete set of representatives of the exponential-l ogarithmic equivalence
classes containing the elements of Lb \ {0}, respectively of Rb. There are 3 di ﬀerent
cases:
• either there are a ∈ L and n ∈ N such that expn(κa) ≥ b. Consider c1 ∈ Lb such that
c1 ∼exp κa. Thus c1 < b ≤ expn(κa) and c1 ∼exp κa ∼exp expn(κd). So b ∼exp κa;
• either there are a ∈ R and n ∈ N such that logn(κa) ≤ b. Simingly, we obtain b ∼exp κa
;
• or for any d1 ∈ L, d2 ∈ R and n ∈ N, we have exp n(κd1) < b < logn(κd2). Consider
c1 ∈ Lb \ {0}. There is d1 ∈ L such that c1 ∼exp κd1. In particular, c1 ≤ expn(κd1)
for some n. As before, for any c2 ∈ Rb, there exists d2 ∈ R such that c2 ≥ logm(κd2).
Theorem
2.1 (2.) applies, so b = ⟨expn(0), expn(κd1) | logn(κd2)⟩= κa where we set
a := ⟨L | R⟩. □

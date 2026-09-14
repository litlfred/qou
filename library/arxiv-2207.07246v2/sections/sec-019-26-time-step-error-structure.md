---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-019-26-time-step-error-structure
section_title: "Time Step Error Structure"
section_number: 2.6
pages: 45-47
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
For the AV6’ interaction, there are only the ﬁrst 6 operators in Eq.(2.19), so G
is 1, and Eq.(2.61) becomes the high-accuracy Trotter formula 6 (Feynman (1948);
Schmidt and Lee (1995)) which has O(∆τ)3 accuracy and can be denoted as US(∆τ),
US(∆τ)≡e−V†
2 ∆τe−T ∆τe−V
2 ∆τ =e−H∆τ− ∆τ3
24 [2T +V,[T,V]]+... =e−H∆τ +O(∆τ)3, (2.74)
where the subscript letter S means symmetric because US(∆τ) =U†
S(∆τ). Note that
although the approximation ofe−V
2 ∆τ which is Eq.(2.63) alone hasO(∆τ 2) error, when
written the form of Eq.(2.74), the O(∆τ 2) cancels and one is left with only O(∆τ 3)
error. Furthermore, we ﬁnd
US(∆τ)US(−∆τ) = 1, (2.75)
this ensures the error in the exponential of US(∆τ) only contains odd orders of ∆τ,
US(∆τ) =e−H∆τ+ ˆf3∆τ3+ ˆf5∆τ5+ ˆf7∆τ7+..., (2.76)
where ˆfi are functions of operators which do not depend on ∆ τ.
For the AV6’ interaction, in the PIMC calculation, we useN short-time propagator
[US(∆τ)]N instead of (e−H∆τ)N in calculating Eq.(2.11), and the total imaginary time
τ =N∆τ, so NO(∆τn) =τO(∆τn−1). Considering Eq.(2.76), this means that for a
givenτ, the error of [US(∆τ)]N only contain the even orders of ∆τ,
[US(∆τ)]N =
(
e−H∆τ+ ˆf3∆τ3+ ˆf5∆τ5+...
)N
=e−Hτ +O(∆τ 2) +O(∆τ 4) +..., (2.77)
6All the error structures of the propagator can be found by repeatedly using Campbell-Baker-
Hausdorﬀ (CBH) formula (Reinsch (2000)),
eAeB =eA+B+ 1
2 [A,B]+ 1
12 [A−B,[A,B]]+ 1
24 [B,[A,[B,A]]]+..., (2.72)
where A and B are operators or matrices. From Eq.(2.72) we can further ﬁnd that,
e
B
2eAe
B
2 =eA+B+ 1
24 [2A+B,[A,B]]+.... (2.73)
and that is how we can write down (Apaja (2009)) Eq.(2.74).
35
and this means⟨ ˆO(∆τ)⟩ in Eq.(2.15) and the true expectation value ⟨ ˆO⟩ of Eq.(2.11)
are related by the following equation,
⟨ ˆO(∆τ)⟩ = Re⟨ΨT|[US(∆τ)]N1 ˆO[US(∆τ)]N2|ΨT⟩
Re⟨ΨT|[US(∆τ)]N|ΨT⟩
=⟨ ˆO⟩× 1 +O(∆τ 2) +O(∆τ 4) +...
1 +O(∆τ 2) +O(∆τ 4) +.... (2.78)
For small ∆τ, in order to extrapolate the expectation value ⟨ ˆO⟩, we need to use,
⟨ ˆO(∆τ)⟩ =⟨ ˆO⟩ +
nc∑
n=1
C2n(∆τ 2n), (2.79)
whereC2n are the ﬁtting parameters for even orders of ∆τ, and nc is the cutoﬀ integer
for n. The theoretical value of C2n depends on the trial wave function and the total
imaginary time τ. In principle, a general extrapolation formula which suits a wide
range of ∆τ should have the same form as Eq.(2.78).
For the local chiral N 2LO interaction, we use the U(∆τ) in Eq.(2.61) as the
short-time propagator and it has errors O(∆τ 2), so when the total imaginary time
τ =N∆τ, we multiply U(∆τ) the short-time propagator N times we have error of
NO(∆τ 2) =τO(∆τ) which isO(∆τ),
[U(∆τ)]N =e−Hτ +O(∆τ), (2.80)
this means that the error of ⟨ ˆO(∆τ)⟩ in Eq.(2.15) hasO(∆τ) error,
⟨ ˆO(∆τ)⟩ = Re⟨ΨT|[U(∆τ)]N1 ˆO[U(∆τ)]N2|ΨT⟩
Re⟨ΨT|[U(∆τ)]N|ΨT⟩
=⟨ ˆO⟩× 1 +O(∆τ) +O(∆τ 2) +O(∆τ 3) +...
1 +O(∆τ) +O(∆τ 2) +O(∆τ 3) +.... (2.81)
Similar with the Taylor expansion of 1
1+x = 1−x +... requires|x|< 1 to converge,
when the error in the denominator in Eq.(2.81) is less than one, Eq.(2.81) can be
written as,
⟨ ˆO(∆τ)⟩ =⟨ ˆO⟩ +O(∆τ) +O(∆τ 2) +.... (2.82)
36
So, usually, for a given total time τ and small ∆τ, in order to get the true expectation
value⟨ ˆO⟩ of Eq.(2.11), we need to calculate ⟨ ˆO(∆τ)⟩ for diﬀerence time step ∆τ and
error bar, and then use the following polynomial equation to extrapolate ⟨ ˆO⟩ and its
error bar,
⟨ ˆO(∆τ)⟩ =⟨ ˆO⟩ +
nc∑
n=1
Cn(∆τn), (2.83)
where Cn are ﬁtting parameters and the theoretical value of Cn depends on the trial
wave function and the total imaginary time τ. In principle a general extrapolation
expression should be Eq.(2.81).
From the error structure Eq.(2.78) or Eq.(2.81) we can see that, even if ∆τ itself
is not very small, as long as the ∆ τ errors (especially the leading order errors) in the
numerator and the denominator of Eq.(2.78) or Eq.(2.81) are comparable, ⟨ ˆO(∆τ)⟩
can still be close to the true expectation value ⟨ ˆO⟩. That is to say the results of PIMC
is robust because they may not be very sensitive to the time step ∆ τ.

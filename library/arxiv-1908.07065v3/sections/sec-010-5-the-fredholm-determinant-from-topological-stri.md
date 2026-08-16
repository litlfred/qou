---
doc_id: arxiv-1908.07065v3
doc_title: "Prepared for submission to JHEP Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-010-5-the-fredholm-determinant-from-topological-stri
section_title: "The Fredholm determinant from topological string theory"
section_number: 5
pages: 29-30
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve ofN = 2, SU (2) super Yang–Mills"
---
Let O be an operator on L2(R) such that O−1 is of trace class. Then, O has a discrete spectrum
{En}n≥0, and its Fredholm determinant
Ξ(E) = det
(
1−EO−1)
=
∏
n≥0
(
1− E
En
)
(5.1)
is an entire function of E whose zeros give the spectrum of O: Ξ(En) = 0 (see e.g. [58] for these
and other properties of Fredholm determinants).
The Fredholm determinant contains very rich information about the spectral properties of
O. For example, the spectral traces, deﬁned as
Z𝓁 =
∑
n≥0
1
E𝓁n
, (5.2)
can be computed by expanding the spectral determinant around E = 0. Indeed, we have
Ξ(E) =
∑
N≥0
(−E)NZ(N, ℏ) (5.3)
where
Z(N, ℏ) =
∑
{m𝓁}
′∏
𝓁
(−1)(𝓁−1)m𝓁Zm𝓁
𝓁
m𝓁!𝓁m𝓁
, (5.4)
and the
′
means that the sum is over the integers m𝓁 satisfying the constraint
∑
𝓁
𝓁m𝓁 =N. (5.5)
– 28 –
From the quantities Z(N, ℏ) (which were called fermionic spectral traces in [2]) one can extract
the conventional spectral traces (5.2).
Although Fredholm determinants are central objects in spectral theory, it is diﬃcult to
obtain explicit expressions for them. It is easy to show (see for instance [59]) that the inverse of
the modiﬁed Mathieu operator (2.14) is of trace class. Therefore, the Fredholm determinant is
well-deﬁned, and it is an interesting question to ﬁnd an explicit, closed form expression for this
quantity.
In recent years it was discovered [2, 3, 60–62] that, by using topological string tools, it is
possible to obtain explicitly expression for Fredholm determinants of operators arising in the
context to quantum mirror curves. We will refer to this relationship as the TS/ST correspon-
dence. As explained in section 5.1, the modiﬁed Mathieu operator (2.14) can be related, upon
a suitable limiting procedure, to the quantum mirror curve of local F0. Therefore we can study
(5.1) within the context of topological string theory and in particular, by using [2, 18], we can
deduce an explicit, closed form expression for the Fredholm determinant of the modiﬁed Mathieu
operator. We will ﬁrst state the main result and then explain how to derive it within topological
string theory. We also present several independent tests of our result, including an interesting
connection to the TBA system of [19].

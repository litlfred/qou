---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-015-5-theta-characteristics
section_title: "Theta Characteristics"
section_number: 5
pages: 30-31
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
doc_brief: "Bring's curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
We now investigate the theta characteristics of Bring’s curve, which in [Ati71] were shown
to be equivalent to spin structures, and as such we will use the terms interchangeably.
These are objects which have been studied greatly in a variety of contexts in algebraic
geometry, number theory, and even string theory, though in this paper we will not discuss
these applications and focus on calculation. Among other results we shall identify the unique
invariant spin structure of Bring’s curve.
For completeness we recall the main deﬁnition that we shall use in this paper.
Deﬁnition 5.1. A theta characteristic is a half-canonical divisor class, i.e. a divisor
class [D] such that 2[D] = [KB].
25To make the reconstruction process of Lombardo more accessible, we recreated in Sage some of the
functions implemented by Lombardo in Magma.
BRING’S CUR VE: OLD AND NEW 31
Lemma 5.2. Call a theta characteristic odd/even based on the parity of it’s index of special-
ity. Then on a Riemann surface of genus g there are 2g−1(2g− 1) odd theta characteristics
and 2g−1(2g + 1) even theta characteristics.
There are many equivalent deﬁnitions of parity for a theta characteristic, and while the
above is not computationally the easiest, it is one of the easier to state. [Far12] provides a
nice overview of these and their connections.
Example 5.3. It is a computational exercise to verify KB∼
(
−xv3v4
v2
)
= 2(3a +b−c), and
so ∆ = 3a +b−c is a theta characteristic on Bring’s curve. A simple calculation in Sage
shows that it is even.

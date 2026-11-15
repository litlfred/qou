---
doc_id: s40879-023-00706-0
doc_title: "Bring’s curve: old and new"
section_id: sec-012-42-relations-between-quotients
section_title: "Relations between quotients"
section_number: 4.2
pages: 25-26
source_pdf: s40879-023-00706-0.pdf
source_sha256: 4c5af312d2e5d6a7
toc_source: outline
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
---
We now consider the various relationships we might expect between the quotient
curves of Bring’s curve. Recall (again from Riemann–Hurwitz) that if C is a curve
of genus g ⩾2 and H ⩽Aut(C) is such that |H| > 4(g −1), a so called ‘large
automorphism group’, then the genus of the quotient curve gC/H = 0. For Bring’s
curve we are therefore interested in subgroups of S5 of order less than or equal to
12, and as we have seen the quotient by a 5-cycle leads to genus 0 we may exclude
subgroups containing such. The relevant conjugacy classes of subgroups are then17
(a) ⟨(12)(34)⟩∼= C2, ⟨(12), (34)⟩∼= V4, ⟨(1324)⟩∼= C4, ⟨(1324), (12)⟩∼= D8. Each
of these groups H has the same normaliser: NS5(H) = ⟨(1324), (12)⟩∼= D8.
17 Note that here we are using the GAP convention for the dihedral group that |Dn| = n. This is the
opposite convention to Sage which uses |Dn| = 2n.
3
Page 26 of 46
H.W. Braden, L. Disney-Hogg
(b) ⟨(12)⟩∼= C2, ⟨(345)⟩∼= C3, ⟨(345), (12)⟩∼= C6, ⟨(345), (34)⟩∼=
S3,
⟨(345), (12)(34)⟩∼= S′
3, ⟨(345), (12), (34)⟩∼= D12 ∼= S3 ×C2. Each of these
groups H has the same normaliser: NS5(H) = ⟨(345), (12), (34)⟩∼= D12.
(c) ⟨(12)(34), (13)(24)⟩∼= V4, ⟨(234), (12)(34)⟩∼= A4. Each of these groups H has
the same normaliser: NS5(⟨(234), (12)(34)⟩) = ⟨(234), (12), (34)⟩∼= S4.
The groupings here are such that if H, H′ are from the same item then they share
the same normaliser N = NS5(H) = NS5(H′). In particular each of H, H′ and
H H′ = H′H are normal in N and we have commutativity of the following diagram
of quotients:
B
B/H
B/H
B/H H
H
H
H H
H H /H
H H /H
where the arrows are labelled by the symmetry being quotiented; by an isomorphism
theorem we have of course that H H′/H ∼= H′/(H ∩H′) and H H′/H′ ∼= H/(H ∩H′).
If, say H ⩽H′, then H H′ = H′ and one side of this diagram collapses.
Now a Riemann–Hurwitz calculation shows that the each of the quotients by
⟨(12), (34)⟩, ⟨(1324), (12)⟩, ⟨(345), (34)⟩and ⟨(345), (12), (34)⟩is of genus 0 and
so not being considered. Thus from the preceding discussion we have the following
relations amongst quotients for the subgroups of (a), (b) and (c):
B
C
E
(a)
(12)(34)
(1324)
B
E′
E′′
C′
E′′′
(b)
(12)
(345)
S′
3
C6
(345)
(12)
(12)(34)
B
C
E(iv)
E(v)
(c)
V4
(12)(34)
A4
(234)
Here C, C′ are genus 2 curves and E, . . . , E(v) elliptic curves that we cannot yet specify
purely on group theoretic grounds. We turn now to their speciﬁcation and indeed we
shall ﬁnd some interesting identities between them, which will then be summarised in
Sect.4.6.

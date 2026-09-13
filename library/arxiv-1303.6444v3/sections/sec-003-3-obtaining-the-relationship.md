---
doc_id: arxiv-1303.6444v3
doc_title: "VIRIAL EXPANSION BOUNDS"
section_id: sec-003-3-obtaining-the-relationship
section_title: "Obtaining the Relationship"
section_number: 3
pages: 4-5
source_pdf: 1303.6444v3.pdf
source_sha256: 4f12ace2197f70ca
doc_brief: "VIRIAL EXPANSION BOUNDS — In the 1960s, the technique of using cluster expansion bounds in order to achieve bounds on the virial expansion was developed by Lebowitz and Penrose (1964) and Ruelle"
---
Lagrange Inversion techniques are the usual approach to obtaining the virial coeﬃcients
and this has a nice representation as a contour integral. If we want to compute the coeﬃcient
cn, we can take the contour integral (around 0) of ∂P
∂ρ divided by nρn. This gives us the
formula:
cn = 1
2πi
∮
C
∂P
∂ρ
nρn dρ (3.1)
VIRIAL EXPANSION BOUNDS 5
We can manipulate this equation to get it in terms of the z-variable, since we know about
the cluster expansion already.
cn = 1
2πi
∮
C′
∂P
∂z
nρn dz
= β−1
2nπi
∮
C′
z∂βP
∂z
zρn dz
= β−1
2nπi
∮
C′
dz
zρn−1 (3.2)
This (implicit) relationship between the virial and the cluster coeﬃcients is our starting
point. The idea is that we can bound such an integral quite easily when we consider bounds
on|ρ|, when we write it in terms of the fugacity z as in (2.4).
Indeed this method is the one used by Ruelle [Rue69] and Lebowitz and Penrose [Leb64].

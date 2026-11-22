---
doc_id: chinta-2025-j-phys-a-math-theor-58-035203
doc_title: "The discrete analogue of the Gaussian"
section_id: sec-008-71-spectral-zeta-function-of-z
section_title: "Spectral zeta function of Z"
section_number: 7.1
pages: 16-17
source_pdf: Chinta_2025_J._Phys._A__Math._Theor._58_035203.pdf
source_sha256: baba83ca76c773d4
toc_source: outline
doc_brief: "The discrete analogue of the Gaussian — 13 sections: Front matter; The discrete analogue of the Gauss; Introduction"
---
The zeta function regularization method in physics started in the 1970 s with papers by
Dowker-Critchley and by Hawking. For a survey of applications to mathematical physics of
this procedure, see [V03, El12, DEK12]. The zeta function in question is defined by a integral
transform, specifically the Mellin transform, of the heat kernel. The case of the circle essen-
tially gives rise to the Riemann zeta function. It is much less standard is to take the Mellin
integral transform of e−2tIn(2t), such as
ζZ (s) =
1
Γ(s)
ˆ ∞
0
e−2tI0 (2t)ts dt
t ,
15
J. Phys. A: Math. Theor. 58 (2025) 035203
G Chinta et al
for 0 < Re(s) < 1/2 and then extend by meromorphic continuation, as was done in [FK17].
Is this function also relevant for physics? There are some indications that this the case. First,
using the method of [CJK10] the asymptotics of the spectral zeta function of discrete tori were
determined in [FK17]. Note that in the zeta function regularization method the determinant
of the Laplacian discussed above corresponds to the special value ζ ′(0) of the corresponding
zeta function.
Second, here is a different context motivated by understanding the Casimir energy in QFT.
The paper [NP00] compared the spectral zeta functions of a circular disk, denote by ζcir(s),
and that of the solid cylinder, denote by ζcyl(s + 1), and obtained the following relationship:
ζcir (s) = 2√π Γ((s + 1)/2)
Γ(s/2)
ζcyl (s + 1).
The factor appearing here is the same independently of whether one considers Dirichlet or
Neumann boundary conditions in the circular disk and solid cylinder.
It turns out from calculations in [FK17, Du19] that
ζZ (s) =
1
√π4s
Γ(1/2 −s)
Γ(1 −s)
=

−2s
−s

,
which essentially is an extension of the Catalan numbers. Therefore, the factor appearing in
[NP00]
2√πΓ((1 + s)/2)
Γ(s/2)
equals
2s
ζZ ((1 −s)/2).
Note that, via the functional symmetry given in [FK17], ζZ((1 −s)/2) is essentially equal
to ζZ(s/2) similarly to what is the case for the Riemann zeta function. More precisely, with
ξZ(s) := 2s cos(πs/2)ζZ(s/2), it holds that
ξZ (s) = ξZ (1 −s)
for all s ∈C. Is there a spectral explanation for the appearance of ζZ(s) in [NP00] and if so,
how does it generalize?
Finally, we mention the paper [KP23] which argues that special values of ζZ(s) are related
to the volume of spheres.

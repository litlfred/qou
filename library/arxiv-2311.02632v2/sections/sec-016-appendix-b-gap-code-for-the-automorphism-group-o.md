---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE"
section_id: sec-016-appendix-b-gap-code-for-the-automorphism-group-o
section_title: "Appendix B. GAP code for the automorphism group of the Fricke-Macbeath surface"
section_number: null
pages: 37-38
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
toc_source: outline
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
Fricke-Macbeath surface
The GAP code provided below computes the order of the group G in Subsection 3.1
defined by the presentation ⟨a, b | a3 = b7 = (ab)2 = (a−1b3a−1ba−1b3)2 = 1⟩:
f := FreeGroup("a", "b");
a := f.1; b := f.2;
t := a^( -1) * b^3 * a^( -1) * b * a^(-1) * b^3;
G := f / [a^3, b^7, (a*b)^2, t^2];
Size(G);
The execution of this code yields 504.
Building on the above code, one can obtain the character table of G using the
following commands:
38
CHUL-HEE LEE
T:= CharacterTable (G);
Display(T);
To find the representatives for each of the conjugacy classes, one can use the following
commands:
conjClasses := ConjugacyClasses (T);
for i in [1.. Length(conjClasses)] do
class := conjClasses[i];
rep := Representative (class);
Print(rep , "\n");
od;

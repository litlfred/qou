---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE"
section_id: sec-015-appendix-a-word-processing-in-237
section_title: "Appendix A. Word processing in (2,3,7)"
section_number: null
pages: 37-37
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
toc_source: outline
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
The following Mathematica code defines a function named reduce.
For a given
input, the function repeatedly employs a collection of transformation rules to a list,
simplifying it according to the rules given in (3.1) and the relations s2
i = 1.
reduce [{a___ ,1,1, b___ }]:= reduce [{a,b}]
reduce [{a___ ,2,2, b___ }]:= reduce [{a,b}]
reduce [{a___ ,3,3, b___ }]:= reduce [{a,b}]
reduce [{a___ ,3,1, b___ }]:= reduce [{a,1,3,b}]
reduce [{a___ ,3,2,3, b___ }]:= reduce [{a,2,3,2,b}]
reduce [{a___ ,3,2,1,3, b___ }]:= reduce [{a,2,3,2,1,b}]
reduce [{a___ ,3,2,1,2,3,2, b___ }]:= reduce [{a,2,3,2,1,2,3,b}]
reduce [{a___ ,2,1,2,1,2,1,2, b___ }]:= reduce [{a,1,2,1,2,1,2,1,b}]
reduce [{a___ ,3,2,1,2,1,3,2,1,2,1,2,1, b___ }]:= reduce [{a
,2,3,2,1,2,1,3,2,1,2,1,2,b}]
reduce[a_] := a
To illustrate, the following command yields an empty list:
reduce [{2, 3, 2, 3, 2, 3}]
demonstrating that (s2s3)3 = 1. Refer to [vdK02] for a way to derive such rules for
Coxeter groups.

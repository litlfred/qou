---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT"
section_id: sec-010-22-presentations
section_title: "Presentations"
section_number: 2.2
pages: 10-10
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.875
latex_coverage_ratio: 1.0
doc_brief: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
Depending on the situations we will use two different presentations of the figure eight knot complement fundamental group $\Gamma_8$. 

We first use the presentation (with generators as in \cite{FKR14})
$$ 
\langle\ g_1, g_2,
g_3\ |\ g_2^{-1}g_1g_3^{-1}g_1^{-1}g_3,\ g_3^{-1}g_2g_1g_2^{-1}\ \rangle.
$$  
Observe then that
$$
g_2 = [g_1,g_3^{-1}]
\quad
\textrm{and}\quad
g_3 = g_2g_1g_2^{-1}.
$$
This presentation is the SnapPea non-simplified presentation with a change of notations.

Keeping only the generators $g_1$ and $g_3$, we get the usual parabolic presentation, used in \S \ref{ss:R_2-R_3}, with $a=g_1$ and $b=g_3$.


The simplified presentation in SnapPea, which we use in \S \ref{ss:R1}, is given (uppercase denotes inverse) by
$$ 
\langle\ a, b\ |\ \ ab^3aBA^{2}B \ \rangle
$$  
with $a=  g_3g_2$ and $b=g_2^{-1}$ (hence $g_1=ba$).

With this notation, we know \cite{Thurston} that the canonical meridian is $m=ab=g_3$ and the longitude 
$l=abABaBAb=[g_3,g_2^{-1}][g_3,g_2]$.

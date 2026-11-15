---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-023-generalizations-of-the-magnus-expansion
section_title: "Generalizations of the Magnus expansion"
section_number: null
pages: 26-27
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
In view of the attractive properties of the Magnus expansion as a tool to construct approximate solutions of non-
autonomous systems of linear ordinary differential equations, it is hardly surprising that several attempts have been made
S. Blanes et al. / Physics Reports 470 (2009) 151-238 177

along the years, either to extend the procedure to a more general setting or to manipulate the series to achieve further
improvements. In this section, we review some of these generalizations, with special emphasis on the treatment of nonlinear
differential equations.

First we reconsider an iterative method originally devised by Voslamber [92] for computing approximations 2“ (t)
in Y(t) = exp(2(t)) for the linear equation Y’ = A(t)Y. The resulting approximation may be interpreted as a re-
summation of terms in the Magnus series and possesses interesting features not shared by the corresponding truncation
of the conventional Magnus expansion. Then we adapt the Magnus expansion to the physically relevant case of a periodic
matrix A(t) with period T which incorporates, in a natural way, the structure of the solution ensured by the Floquet theorem.
Next we go one step further and generalize the Magnus expansion to the so-called nonlinear Lie equation Y’ = A(t, Y)Y.
Finally, we show how the procedure can be applied to any nonlinear explicitly time-dependent differential equation.
Although the treatment is largely formal, in Section 5 we will see that it is of paramount importance for designing new
and highly efficient numerical integration schemes for this class of differential equations. We particularize the treatment
to the important case of Hamiltonian systems, and also establish an interesting connection with the Chen-Fliess series for
nonlinear differential equations.

---
doc_id: arxiv-1806.09450v1
doc_title: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗"
section_id: sec-005-33-the-exceptional-lie-groups-e6-and-e7
section_title: "The exceptional Lie groups E6 and E7"
section_number: 3.3
pages: 10-12
source_pdf: 1806.09450v1.pdf
source_sha256: 8556b67d97856446
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.991
doc_brief: "Deducing the symmetry of the standard model from the automorphism and structure groups of the exceptional Jordan algebra ∗ — We continue the study undertaken in [DV] of the exceptional Jordan algebra"
---
A non-compact real form of the simply connected Lie group $E_6$, the (reduced) *structure group* of the exceptional Jordan algebra $J=H_3 ({\mathbb O})$, can be defined as the group of determinant preserving linear transformations of $J$ where, for $X$ given by ([\[eq26\]](#eq26){reference-type="ref" reference="eq26"}), $$\begin{aligned}
\det X &= &\frac13 \, {\rm tr} (X^3) - \frac12 \, {\rm tr} X^2 \, {\rm tr} X + \frac16 \, ({\rm tr} X)^3 \\
&= &\xi_1 \, \xi_2 \, \xi_3 - \xi_1 \vert x_1 \vert^2 - \xi_2 \vert x_2 \vert^2 - \xi_3 \vert x_3 \vert^2 + 2 {\rm Re} \, x_1 \, x_2 \, x_3 \, . \nonumber
\end{aligned}$$ Noting that the Lie algebra of this non-compact group has the form ([\[eq12\]](#eq12){reference-type="ref" reference="eq12"}) ${\rm str} \, (J) = {\mathfrak f}_4 \, \dot + \, J_0$ where ${\mathfrak f}_4$ is, in fact, its maximal compact Lie subalgebra, one finds that the signature of the Killing form of ${\rm str} \, (J)$ is[^1] $$\label{eq320}
\mbox{signature} \ [{\rm str} \, (J)] = \dim \, (J_0) - \dim \, {\mathfrak f}_4 = 26-52 = -26 \, .$$ It is demonstrated in [@BS] that this non-compact form of ${\mathfrak e}_6$ is obtained if we replace the complex numbers ${\mathbb C}$ in $L({\mathbb C} , {\mathbb O})$ by the split alternative algebra $\widetilde{\mathbb C}$: $$\label{eq321}
{\rm Str} \, J = E_{6 (-26)} \, , \quad {\mathfrak e}_{6 (-26)} = L (\widetilde{\mathbb C} , {\mathbb O})$$ where the *split form* $\widetilde{\mathbb C}$ of ${\mathbb C}$ is obtained by replacing the *imaginary unit* $i$ by $e$ such that $e^2-1 = (e+1)(e-1)=0$ ($\widetilde{\mathbb K}$ is *split* if at least one of the "imaginary units" has square $1$). (Actually, ${\mathfrak e}_{6(-26)}$ is identified with ${\rm str}' (J)$ in [@BS], the prime indicating factorization with respect to the multiples of the central operator $L_{{\rm 1\mkern-4mu I}}$ (of left multiplication by the unit element in ${\mathbb K}$).)

The asymmetrical Tits construction of the above Lie algebra gives $$\label{eq322}
{\mathfrak e}_6 \cong {\rm Der} \, (H_3 ({\mathbb O})) + sH_3 ({\mathbb O}) = {\mathfrak f}_4 + J_0$$ where $sH_3 ({\mathbb K})$ stands for the traceless hermitian $3 \times 3$ matrices with entries in ${\mathbb K}$. Eq. ([\[eq322\]](#eq322){reference-type="ref" reference="eq322"}) allows to easily calculate the dimension of ${\mathfrak e}_6$ : $$\label{eq323}
\dim {\mathfrak e}_6 = \dim \, ({\mathfrak f}_4) + \dim \, (J_0) = 52+26 = 78 \, .$$ As it is demonstrated in [@A] ${\mathfrak e}_6$ can be decomposed as a vector space into the maximal rank Lie subalgebra $so (10) \oplus u(1)$ and the 32 dimensional space $S_{10}$ of $so (10)$ spinors: $$\label{eq324}
{\mathfrak e}_6 = so (10) \oplus u(1) \, \dot + \, S_{10} \, ;$$ moreover the natural mapping $S_{10} \times S_{10} \to so (10)$ allows to reconstruct the Lie bracket in the compact form $e_6$.

In 1954 Freudenthal described a non-compact form $E_{7 (-25)}$ of $E_7$ as a group of linear transformations of the 56-dimensional space ${\mathcal P}$ of block matrices $$\label{eq325}
P = \begin{pmatrix}
\alpha &X \\
Y &\beta \end{pmatrix} \quad \mbox{where} \quad \alpha , \beta \in {\mathbb R} \, , \ X,Y \in J \quad (\alpha \equiv \alpha \, {\rm 1\mkern-4mu I}_3 \, , \ \beta \equiv \beta \, {\rm 1\mkern-4mu I}_3)$$ that preserve the symplectic form $$\label{eq325bis}
\omega \, (P_1 , P_2) = \alpha_1 \, \beta_2 - \alpha_2 \, \beta_1 + \langle X_1 , Y_2 \rangle - \langle Y_1 , X_2 \rangle$$ and a triple product ${\mathcal P}^{\times 3} \to {\mathcal P}$. The maximal compact subgroup of $E_{7(-25)}$ is $E_6 \times U(1) / {\mathbb Z}_3$, the Lie algebra $e_{7(-25)}$ having a vector space decomposition $$\label{eq325ter}
{\rm co} \, (J) = e_{7(-25)} = e_6 \oplus u(1) \, \dot + \, J \, \dot + \, J$$ of signature $$\label{eq326}
\mbox{signature} \ [{\rm co} \, (J)] = 2 \dim \, (J) - \dim \, [e_6 \oplus u(1)] = 54-79 = -25$$ justifying the above notation.

A review of the Kantor-Koecher-Tits construction of ${\rm co} (J)$ that explores the correspondence between a *Jordan triple system* and 3-graded Lie algebras is contained in [@P].

The Tits construction of the compact form of ${\mathfrak e}_7$, on the other hand, yields the elegant relation $$\begin{aligned}
\label{eq327}
{\mathfrak e}_7 = {\rm Der} \, (H_3 ({\mathbb O})) \, \dot + \, [H_3 ({\mathbb O})]^3 \Rightarrow \dim \, ({\mathfrak e}_7) &= &\dim \, ({\mathfrak f}_4) + 3 \, \dim \, (J) \nonumber \\
&= &52+81=133 \, .
\end{aligned}$$

[^1]: We are using the common notation (cf. [@B]); [@BS] write instead ${\mathfrak e}_6(26)$.

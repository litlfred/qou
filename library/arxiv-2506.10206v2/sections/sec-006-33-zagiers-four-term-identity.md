---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-006-33-zagiers-four-term-identity
section_title: "Zagier's four-term identity"
section_number: 3.3
pages: 9-12
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
Setting $u = \frac{4}{3}$ in Theorem [\[maintheorem\]](#maintheorem){reference-type="ref" reference="maintheorem"}, it is possible, as below, to derive Zagier's four-term identity such that $$\label{Zagierfour}
 3 L\left(-\frac{1}{6}\right) - L\left(\frac{1}{8}\right) + L \left(\frac{1}{9}\right) + L \left(\frac{1}{28}\right) = -\frac{\pi^2}{12}.$$ Using Theorem [\[maintheorem\]](#maintheorem){reference-type="ref" reference="maintheorem"}, we provide a sketch of a proof of the Zagier identity in [\[Zagierfour\]](#Zagierfour){reference-type="eqref" reference="Zagierfour"}. On the left-hand side, we apply the relation [\[MequalsAB\]](#MequalsAB){reference-type="eqref" reference="MequalsAB"} from Theorem [\[maintheorem\]](#maintheorem){reference-type="ref" reference="maintheorem"}, and we set $u = 
 \frac{4}{3}$, $s = 2$, $p = 3$, and $z = 
 \frac{1}{3}$ in the formula $$\label{sigmasumLi}
\sum_{m=0}^{p-1} \operatorname{Li}_s(z e^{2\pi i m/p}) = p^{1-s} \operatorname{Li}_s(z^p),$$ Plugging in $u = \frac{4}{3}$ and using the four-term relation in [\[wellknown4term\]](#wellknown4term){reference-type="eqref" reference="wellknown4term"}, we obtain $$\begin{gathered}
 - \mathrm{Li}_2\left(-\frac{1}{7}\right) + \mathrm{Li}_2\left(\frac{1}{7}\right) 
 - \mathrm{Li}_2\left(\frac{-6 - 3i\sqrt{3}}{7}\right) 
 + \mathrm{Li}_2\left(\frac{6 - 3i\sqrt{3}}{7}\right) \\ 
 - \mathrm{Li}_2\left(\frac{-6 + 3i\sqrt{3}}{7}\right) 
 + \mathrm{Li}_2\left(\frac{6 + 3i\sqrt{3}}{7}\right) 
 - \frac{\pi^2}{4} + \ln\left(\frac{4}{3}\right)\ln(7). 
\end{gathered}$$ From Abel's formula, we find that $$\begin{gathered}
 \mathrm{Li}_2\left(\frac{z}{1 - z} \cdot \frac{w}{1 - w}\right) = \\
 \mathrm{Li}_2\left(\frac{z}{1 - w}\right) 
 + \mathrm{Li}_2\left(\frac{w}{1 - z}\right) 
 - \mathrm{Li}_2(z) - \mathrm{Li}_2(w) 
 - \ln(1 - z)\ln(1 - w), 
\end{gathered}$$ writing $$w = \frac{1}{\frac{1}{7}\left(-6 - 3i\sqrt{3}\right)} \ \ \ \text{and} \ \ \ 
z = \frac{1}{\frac{1}{7}\left(-6 + 3i\sqrt{3}\right)},$$ and we omit the elementary transformations we have applied, for the sake of brevity. This yields an expression that is again amenable to [\[sigmasumLi\]](#sigmasumLi){reference-type="eqref" reference="sigmasumLi"}, so we are able to eliminate the the complex conjugate terms: $$\begin{gathered}
 \frac{\operatorname{Li}_2\left(\frac{1}{8}\right)}{3} - \operatorname{Li}_2\left(\frac{1}{4}\right) - \operatorname{Li}_2\left(\frac{7}{-6 - 3i\sqrt{3}}\right) 
 - \operatorname{Li}_2\left(\frac{7}{-6 + 3i\sqrt{3}}\right) - \frac{\pi^2}{12} + \frac{\ln^2(2)}{2}\\ 
 - \left( -\ln\left(\frac{3}{2}\right) + \frac{\ln(7)}{2} - i \cot^{-1}\left(\frac{5}{\sqrt{3}}\right) \right) \left( -\ln\left(\frac{3}{2}\right) + 
 \frac{\ln(7)}{2} + i \cot^{-1}\left(\frac{5}{\sqrt{3}}\right) \right)=0. 
\end{gathered}$$ Mimicking the above derivation with the use of Roger's formula, we obtain that $$\begin{gathered}
 \operatorname{Li}_2(z w) - \operatorname{Li}_2(w) - \operatorname{Li}_2(z) + \operatorname{Li}_2\left(\frac{w(1 - z)}{1 - w z}\right) + \operatorname{Li}_2\left(\frac{z(1 - 
 w)}{1 - w z}\right) = \\ 
 -\ln\left(\frac{1 - z}{1 - w z}\right) \ln\left(\frac{1 - w}{1 - w z}\right), 
\end{gathered}$$ writing $$w = 1 - \frac{3}{7}(2 - i\sqrt{3}) \ \ \ \text{and} \ \ \ \quad z = 1 - \frac{3}{7}(2 + i\sqrt{3}).$$ We thus have that $$\begin{aligned}
\frac{\pi^2}{4} - \frac{\ln^2(2)}{2} + \frac{(i \pi + \ln(2))^2}{2} 
+ \left( -i \cot^{-1}\left(\frac{2}{\sqrt{3}}\right) + \frac{\ln(7)}{2} \right)\left( i \cot^{-1}\left(\frac{2}{\sqrt{3}}\right) + \frac{\ln(7)}{2} \right)\\
+ \operatorname{Li}_2\left(\frac{4}{7}\right) + \frac{\operatorname{Li}_2(8)}{3} - \operatorname{Li}_2\left(\frac{1}{7} - \frac{3i}{7}\sqrt{3}\right) - \operatorname{Li}_2\left(\frac{1}{7} + \frac{3i}{7}\sqrt{3}\right)=0. 
\end{aligned}$$ We then apply the known identities $$\begin{aligned}
 \operatorname{Li}_2\left(\frac{4}{3}\right) + \operatorname{Li}_2(4) & = \frac{1}{2}\left( \pi^2 
 - \ln^2(3) \right), \nonumber \\ 
 -\operatorname{Li}_2\left(\frac{4}{7}\right) & = \operatorname{Li}_2\left(-\frac{4}{3}\right) + 
 \frac{1}{2} \ln^2\left(\frac{3}{7}\right), \nonumber \\ 
 -\frac{{\pi}^2}{18}+\frac{(\ln 3)^2}{6}. & = \operatorname{Li}_2\left(-\frac{1}{3}\right) - 
 \frac{1}{3}\operatorname{Li}_2\left(\frac{1}{9}\right), \text{and} \nonumber \\ 
 \frac{{\pi}^2}{18}+2\ln2\cdot\ln3-2(\ln 2)^2-\frac{2}{3}(\ln 3)^2 
 & = \operatorname{Li}_2\left(\frac{1}{4}\right) + 
 \frac{1}{3}\operatorname{Li}_2\left(\frac{1}{9}\right), \label{previously4p28}
\end{aligned}$$ together with $$-\operatorname{Li}_2\left(-\frac{4}{3}\right) = \operatorname{Li}_2\left(\frac{1}{7}\right) - \operatorname{Li}_2\left(-\frac{1}{7}\right) - 
 \operatorname{Li}_2\left(\frac{4}{3}\right) - \ln(3)\ln(7) + \ln(4)\ln(7) + \frac{\pi^2}{4}.$$ Converting the arguments $-\frac{1}{3}$ and $\frac{1}{9}$ to obtain the arguments $\frac{1}{4}$ and $\frac{1}{9}$ may be achieved with a classical functional equation for the dilogarithm, and similarly for the arguments $-\frac{1}{7}$ and $\frac{1}{8}$.

The associated ${}_{4}F_{3}$-series is as follows: $$\begin{aligned}
 \frac{28 \, }{27} \operatorname{Li}_2\left(\frac{1}{8}\right) - \frac{7 \pi^2}{81} + 
 \frac{14 \ln^2(2)}{3} - \frac{7 \ln^2(7)}{18} + \frac{56}{27} \pi \cot^{-1}\left(\frac{5}{\sqrt{3}}\right) - 
 \frac{14}{9} \left(\cot^{-1}\left(\frac{5}{\sqrt{3}}\right)\right)^2 \\ 
 = 2\sum_{n=0}^{\infty} \left( \frac{27}{196} \right)^{n} 
 \left[ \begin{matrix} \frac{1}{2}, \frac{1}{2}, 1 
 \vspace{1mm} \\ 
 \frac{5}{6}, \frac{7}{6}, \frac{3}{2} \end{matrix} \right]_{n}. 
\end{aligned}$$ To prove this without the Zaiger identity, we have that the left-hand side may be expressed with $$\operatorname{Li}_2\left(-\frac{1}{3}\right) + \frac{1}{3} \, \operatorname{Li}_2\left(\frac{1}{28}\right) + \operatorname{Li}_2\left(-\frac{1}{6}\right),$$ disregarding logarithmic and other non-dilogarithmic terms for the sake of brevity. Then, using the above formulation of Abel's formula, we make use of $$\operatorname{Li}_2\left(\frac{1}{28}\right) = \operatorname{Li}_2\left(\frac{1}{7}\right) + 
 \operatorname{Li}_2\left(\frac{1}{4}\right) - \operatorname{Li}_2\left(\frac{1}{9}\right) - 
 \operatorname{Li}_2\left(\frac{2}{9}\right) - \ln\left(\frac{8}{9}\right)\ln\left(\frac{7}{9}\right)$$ and $$\operatorname{Li}_2\left(\frac{2}{9}\right) = \operatorname{Li}_2\left(\frac{1}{3}\right) + 
 \operatorname{Li}_2\left(\frac{2}{3}\right) - \operatorname{Li}_2\left(\frac{4}{7}\right) - 
 \operatorname{Li}_2\left(\frac{1}{7}\right) - \ln\left(\frac{3}{7}\right)\ln\left(\frac{6}{7}\right).$$ Informally, since the bases $-\frac{1}{6}$ and $-\frac{1}{3}$ cancel with one another, we are left with a basis given by $\frac{1}{8}$.

Using [\[previously4p28\]](#previously4p28){reference-type="eqref" reference="previously4p28"} and the well-known identity $3 \operatorname{Li}_2\left(\frac{1}{2}\right) - 
 3 \operatorname{Li}_2\left(\frac{1}{4}\right) - \operatorname{Li}_2\left(\frac{1}{8}\right) + 
 \frac{1}{2} \operatorname{Li}_2\left(\frac{1}{64}\right) - \frac{\pi^2}{12} = 0$, it is possible to compress Zagier's four-term identity into a three-term identity. In this direction, we obtain that $$\frac{9}{2} \ln^2(2) - 6 \ln(2) \ln(3) + 2 \ln^2(3) + 
 \frac{1}{2} \operatorname{Li}_2\left(\frac{1}{64}\right) = 
 -\operatorname{Li}_2\left(\frac{1}{9}\right) + \operatorname{Li}_2\left(\frac{1}{8}\right)$$ Although it is always possible to derive a three-term identity with rational bases using Roger's identity, (e.g. by letting $z=1-m$ and $w=m$), there is no obvious way to prove Zagier's identity with trivial manipulations of Roger's formula and elementary transformations.

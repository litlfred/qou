---
doc_id: arxiv-2104.14491v1
doc_title: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Mos"
section_id: sec-008-32-positive-pattern-companion-decompositions
section_title: "Positive pattern-companion decompositions"
section_number: 3.2
pages: 7-7
source_pdf: 2104.14491v1.pdf
source_sha256: 1aea658f17283df1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.883
latex_coverage_ratio: 0.841
doc_brief: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Moscow 117218, Russia"
---
$\star$ The reduced Khovanov polynomial of a twisted satellite (Whitehead double) of a knot $\mathcal{K}$ has the form ($k$ in $\mathtt{Tw}_k$ is *even*, see [\[app:coltw\]](#app:coltw){reference-type="ref" reference="app:coltw"}) $$\begin{aligned}
\mathtt{Kh}^{\mathcal{S}_{\mathtt{Tw}_k}^{\mathcal{K}}}=\mathtt{Kh}^{\mathtt{Tw}_{k}}(q,t)+\left(q^2t\right)^{-k-2}\left(1+q^6t^3\right)\left(1+q^2t\right){\mathfrak{K}}^{\mathcal{K}}(q,t).
\label{ppcd-tw-sat}
\end{aligned}$$ $\star$ The reduced Khovanov polynomial of a two-strand torus satellite (two-strand cable) of a knot $\mathcal{K}$ has the form ($k$ in $\mathtt{Tor}_k$ to be *odd*, see [\[app:coltor\]](#app:coltor){reference-type="ref" reference="app:coltor"}) $$\begin{aligned}
\mathtt{Kh}^{\mathcal{S}_{\mathtt{Tor}_k}^{\mathcal{K}}}=\left(q^3t\right)^{-\mathtt{Sh}_{\mathcal{K}}}\!\cdot\!\Big(
\mathtt{Kh}^{\mathtt{Tor}_{k}}(q,t)+t^{-1}q^{k-1}\left(1+q^6t^3\right){\mathfrak{K}}^{\mathcal{K}}(q,t)\Big).
\label{ppcd-tor-sat}
\end{aligned}$$ $\star$ The unreduced Khovanov polynomials in the same case can be presented as $$\begin{aligned}
{}_u\mathtt{Kh}^{\mathcal{S}_{\mathtt{Tor}_k}^{\mathcal{K}}}=\left(q^3t\right)^{-\mathtt{Sh}_{\mathcal{K}}}\!\cdot\!\Big(
{}_u\mathtt{Kh}^{\mathtt{Tor}_{k}}(q,t)+q^{k}{_u}{\hat\mathfrak{K}}^{\mathcal{K}}(q,t)-
q^{k}\left(1+q^{-2\mathtt{sgn}_n}(-t)^{\Theta_k-\Theta_n}\right)\Big).
\label{ppcd-u-tor-sat}
\end{aligned}$$ The above formulae contain the following quantities, $$\begin{aligned}
\arraycolsep=1mm
\begin{array}{ccp{15cm}}
    \diamondsuit&k&is an integer-valued topological invariant that defines the pattern. \\
    &\diamond&The $k$-satellites of the unknot are $\mathcal{S}^{0_1}_{\mathtt{Tw}_k}=\mathtt{Tw}_k$ and $\mathcal{S}^{0_1}_{\mathtt{Tor}_k}=\mathtt{Tor}_k$;\\[2mm]
    &\diamond&We explain how to get the $k$ from a planar diagram of the satellite in sec.\ref{sec:sat}.\\[2mm]
    \diamondsuit&\mathfrak{K}^{\mathcal{K}}& is a positive polynomial invariant of the companion $\mathcal{K}$. \\
    &\diamond& The reduced invariant vanishes for the unknot, i.e., $\mathfrak{K}^{0_1}=0$.\\
    &\diamond& \textit{The same} $\mathfrak{K}^{\mathcal{K}}$ enters all formulae. \\[2mm]
    \diamondsuit&\mathtt{Sh}_{\mathcal{K}}& is an integer-valued invariant of the companion $\mathcal{K}$; \\ 
    &\diamond&in all studied cases, given in (\ref{ShKn}), $\mathtt{Sh}_{\mathcal{K}}=-3s_{\mathcal{K}}$, where $s$ is both the knot signature and the Rasmussen invariant.  
    
\end{array}
\nonumber
\end{aligned}$$ Below we recall the values of $\mathtt{Sh}^{\mathcal{K}}$ for the studied knots (up to the knot $8_9$ in [@katlas], in sec.[\[sec:AAK-rolf\]](#sec:AAK-rolf){reference-type="ref" reference="sec:AAK-rolf"}) and knot families (the two-strand torus knots, in sec.[\[sec:AAK-tor\]](#sec:AAK-tor){reference-type="ref" reference="sec:AAK-tor"}, and the twist knots, in sec.[\[sec:AAK-tw\]](#sec:AAK-tw){reference-type="ref" reference="sec:AAK-tw"}).

$$\begin{aligned}
\arraycolsep=0.5mm
\begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}
    \hline\rule{0pt}{4mm}
    \mathcal{K}&3_1&4_1&5_1&5_2&6_1&6_2&6_3&7_1&7_2&7_3&7_4&7_5&7_6&7_7&8_1
    &8_2&8_3&8_4&8_5&8_6&8_7&8_8&8_9\\
    \hline
    \simeq&\mathtt{Tor}_{3}&&\mathtt{Tor}_5&&&&&\mathtt{Tor}_7&&&&&&&&&&&&&&&\\
    \hline
    \simeq&\rule{0pt}{3mm}\overline{\rule{0pt}{3mm}\mathtt{Tw}}_{2}&\mathtt{Tw}_{-2}&&\mathtt{Tw}_3&\mathtt{Tw}_{-4}&&&&\mathtt{Tw}_5&&&&&&\mathtt{Tw}_{-6}&&&&&&&&\\
    \hline
    \mathtt{Sh}_{\mathcal{K}}&6&0&12&6&0&6&0&18&6&-12&-6&12&6&0&0&12&0&6&-12&6&-6&0&0\\
    \hline\hline
    \multicolumn{6}{|c|}{\rule{0pt}{4mm}\mathtt{Sh}_{\mathtt{Tor}_{n<0}}=3n+3}&\multicolumn{6}{c|}{\mathtt{Sh}_{\mathtt{Tor}_{n>0}}=3n-3}&
    \multicolumn{6}{c|}{\mathtt{Sh}_{\mathtt{Tw}_{n\le0}}=0}&\multicolumn{6}{c|}{\mathtt{Sh}_{\mathtt{Tw}_{n>0}}=6}\\[0.5mm]
    \hline
\end{array}
\label{ShKn}
\end{aligned}$$

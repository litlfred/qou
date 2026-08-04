The knot--particle dictionary of Chapter~\ref{chap:knots-particles}
maps each particle to a specific braid configuration: leptons to torus
knots $T(2, 2k+1)$, bosons to torus links $T(2, 2k)$, quarks to
unknot strands in the Borromean braid, and composite hadrons to
products under $\bowtie_K$.  This chapter adds the \emph{flavor layer}:
each dictionary entry now carries the $A_2$ quantum numbers $(I_3, Y)$
from the hexagonal weight lattice.

\begin{center}
\begin{tabular}{l l c c l}
\hline
Particle & Braid & $I_3$ & $Y$ & Status \\
\hline
\multicolumn{5}{c}{\textit{Quarks (unknot strands in Borromean braid)}} \\
$u$ & $\sigma_i^{+1}$ strand & $+\tfrac{1}{2}$ & $+\tfrac{1}{3}$ & conditional on $N=3$ \\
$d$ & $\sigma_i^{-1}$ strand & $-\tfrac{1}{2}$ & $+\tfrac{1}{3}$ & conditional on $N=3$ \\
$s$ & $\sigma_j^{-1}$ (2nd gen) & $0$ & $-\tfrac{2}{3}$ & conditional on $N=3$ \\
\hline
\multicolumn{5}{c}{\textit{Mesons ($q\bar{q}$ via $\bowtie_K$)}} \\
$\pi^+$ & $u \bowtie_K \bar{d}$ & $+1$ & $0$ & octet (\S\ref{sec:meson-octet}) \\
$K^+$   & $u \bowtie_K \bar{s}$ & $+\tfrac{1}{2}$ & $+1$ & octet \\
$\eta$   & $(u\bar{u}+d\bar{d}-2s\bar{s})/\sqrt{6}$ & $0$ & $0$ & octet \\
$\eta'$  & $(u\bar{u}+d\bar{d}+s\bar{s})/\sqrt{3}$ & $0$ & $0$ & singlet \\
\hline
\multicolumn{5}{c}{\textit{Baryons ($qqq$ via Borromean $\bowtie_K$)}} \\
$p$ & Borromean $(uud)$ & $+\tfrac{1}{2}$ & $+1$ & octet (\S\ref{sec:baryon-multiplets}) \\
$n$ & Borromean $(udd)$ & $-\tfrac{1}{2}$ & $+1$ & octet \\
$\Delta^{++}$ & symmetric $(uuu)$ & $+\tfrac{3}{2}$ & $+1$ & decuplet \\
$\Omega^-$    & symmetric $(sss)$ & $0$ & $-2$ & decuplet \\
\hline
\multicolumn{5}{c}{\textit{Color charge (orthogonal to flavor)}} \\
$r, g, b$ & $G_2$ stabilizer (\S\ref{sec:color-algebra}) & --- & --- & Sym$^2$ gate passed \\
\hline
\end{tabular}
\end{center}

\textbf{Epistemic tiers.}
The isospin $I_3$ column is \emph{derived} (writhe-to-isospin map,
no fitted parameters).  The hypercharge $Y$ column is \emph{open}
(candidate: ribbon twist; battery: Gell-Mann--Nishijima consistency).
The quark flavor assignments are \emph{conditional on $N = 3$}
(the central open problem of this chapter).  The color assignments
follow from the octonionic $G_2$ route but remain at the
discrete-skeleton level pending the continuous $G_2$ completion.

No entry in this table is a fit: each derives from the categorical
braid structure or is marked as open.  The table will be updated as
the open problems of \S\ref{sec:eightfold-open-problems} are resolved.

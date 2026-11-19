The knot--particle dictionary of [the knots-particles
chapter](#chap:knots-particles-confinement)
maps each particle to a specific braid configuration: leptons to torus
knots $T(2, 2k+1)$, bosons to torus links $T(2, 2k)$, quarks to
unknot strands in the Borromean braid, and composite hadrons to
products under $\bowtie_K$.  This chapter adds the *flavor layer*:
each dictionary entry now carries the $A_2$ quantum numbers $(I_3, Y)$
from the hexagonal weight lattice.

```tex
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
$r, g, b$ & $G_2$ stabilizer (\S\ref{sec:color-algebra}) & --- & --- & not excluded by the Sym$^2$ gate \\
\hline
\end{tabular}
\end{center}
```

**Epistemic tiers.**
The isospin $I_3$ column is *derived* (writhe-to-isospin map,
no fitted parameters).  The hypercharge $Y$ column is *open*
(candidate: ribbon twist; battery: Gell-Mann--Nishijima consistency).
While colour rank $N_c = 3$ arises via scalar restriction along Bring's cyclic $\mathbb{Z}_3$ cover (and via the discrete octonionic $G_2$ Fano skeleton), the three-flavour assignment $N_f = 3$ is carried as a *conditional hypothesis* throughout this chapter.

**Provenance of the $(I_3, Y)$ columns.**  With one exception they are
the standard $\mathrm{SU}(3)_{\mathrm{f}}$ flavour assignments, imported from the
eightfold-way classification and placed against the braid column to show
that the dictionary is *consistent* with it.  They are not outputs
of the braid construction.  The exception is $I_3$ on the nucleon
doublet, where the writhe difference reproduces $\Delta I_3 = 1$
scale-free --- that entry is derived.  Every $Y$ entry, and every quark
row, is either open or conditional on $N = 3$.

No entry in this table is a *fit* --- nothing here was tuned to
match data --- but neither is the table a derivation of the flavour
quantum numbers.  It is a consistency ledger, and will be updated as the
open problems of [the open-problems
section](#sec:eightfold-open-problems) are resolved.

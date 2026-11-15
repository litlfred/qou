---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-030-51-functions-near-roots-of-unity-and-the-naive-h
section_title: "Functions near roots of unity and the naive Habiro ring"
section_number: 5.1
pages: 59-64
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
text_source: latex
latex_prose_ratio: 0.734
latex_coverage_ratio: 0.976
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
\label{sec:naive}

In Habiro's original work~\cite{Habiro:completion} the Habiro rings of $\BZ$ and
$\BQ$ were defined as $\HH:=\HH_\BZ$ and $\HH_{\BQ}$, where $\HH_R$ is defined for
any ground ring $R$ by
\be
\label{eq:Hnaive}
\HH_{R} \= \varprojlim_n R[q]/(q;q)_{n}R[q]\,.
\ee
(Here we use the notation $\HH_R$, defined as an inverse limit, as opposed to
$\calH_R$, which is defined as a subset of $\calP_R$ in Definition~\ref{def.hab} of
Section~\ref{sub.hab}.)
(The two rings $\HH=\HH_\BZ$ and $\calH=\calH_\BZ$ can be identified canonically,
but in general $\HH_R$, which we will call the \emph{naive Habiro ring}, and
$\calH_R$ are different.)
Note that $\HH_\BQ\neq\HH_{\BZ}\otimes\BQ$. Indeed, the ring
$\HH_{\BZ}$ is an integral domain while $\HH_{\BQ}$ has a large number of zero
divisors~\cite[Sec. 7.5]{Habiro:completion}.

The definition of $\HH_R$ leads immediately to
expressions of the form~\eqref{eq:elts.hab} with $P_n(q)\in R[q]$.
These expressions are not unique but can be made unique by assuming
$\deg P_{n}<n$ so that $P_{n}(q)=\sum_{k=0}^{n-1}a_{n,k}q^k$ for some
$a_{n,k}\in R$.
(The example from equation~\eqref{eq:KZ} has $a_{n,k}$ given simply by $\delta_{k,0}$.)
The coefficients $a_{n,k}$ give an explicit isomorphism of $R$-modules
\be
\label{eq:hdecomp}
\begin{array}{ccccc}
  {}_{\phantom{2_{2_{2_{2_{2_{2}}}}}}}\HH_R\!
  &=&
  \!\prod_{n=1}^{\infty}
  (R\oplus qR\oplus\cdots\oplus q^{n-1}R)(q;q)_{n-1}
  
  
  &\cong&
  \prod_{n>k\geq0}R\,,\\
  \sum_{n=1}^{\infty}P_{n}(q)(q;q)_{n-1}\!
  &\mapsto&
  \!\sum_{n=1}^{\infty}\sum_{k=0}^{n-1}a_{n,k}q^k(q;q)_{n-1}
  &\mapsto&
  \{a_{n,k}\}_{n>k\geq0}\,.
\end{array}
\ee

As in Section~\ref{sub.habZ}, we have a map $\iota:\HH_R\to\calP_R$, where
$\calP_R$ was defined in equation~\eqref{PR}:
\be
\begin{array}{ccccc}
\calP_{R}
&\;:=\;&
\Big(\prod_{\z\in\mu_\infty} R[\z]
\llbracket u\rrbracket\Big)^{\mathrm{Gal}(\BQ^{\mathrm{ab}}/\BQ)}
&\;\cong\;&
\prod_{m\geq 1} R[\z_m]\llbracket u\rrbracket\,,\\







& & & &\\
f(q) & \mapsto & (f_\z(u)=F(\z(1-u)))_\z & \;\mapsto\; & (f_m(u)=f_{\z_m}(u))_m\,.
\end{array}
\ee
Here, for each $m$, we use the local variable $u$ defined by $q=\z_m(1-u)$.
(In the Introduction, we used
$q=\z_m+x$ instead, so $u$ and $x$ are related by $x=-\z_mu$
and $f_m$ differs here from that of equation~\ref{iota} by the change of variable.)
The map $\iota:\HH_R\to\calP_R$
splits as a product of maps $\iota=\prod_{m\geq1}\iota_m$, where
for $F\in\HH_R$, we define the map~$\iota_m$ by the expansion at $q=\z_m(1-u)$, i.e.
$\iota_m(F)=F(\z_m(1-u))\in R[\z_m][\![u]\!]$.

Similar to the coordinates~$a_{n,k}$ coming from the isomorphism~\eqref{eq:hdecomp},
the $R$-module $\calP_R$ has a natural basis over $R$ given by
$\{\gamma_{m,\ell,j}\}_{m,\,\ell\geq1,\,\phi(m)>j\geq0}$, where
\be
\label{eq:oht.c}
f_{m}(u) \= \sum_{\ell=1}^{\infty} C_{\ell}(\z_m)\,u^{\ell-1}\,,
\qquad C_{\ell}(\z_m)\=
  \sum_{j=0}^{\phi(m)-1}\gamma_{m,\ell,j}\,\z_m^{j}\inn \BZ[\z_m]\,.
\ee
(Again, the shift by $1$ --- making $C_{\ell}(\z_m)$ the coefficient of $u^{\ell-1}$
rather than $u^{\ell}$ --- makes later formulas more natural, because its properties
depend on the multiplicative nature of $\ell$ as opposed to $\ell-1$.)
We then have explicit isomorphisms of abelian groups,
\be
\label{eq:gamma}
\begin{array}{ccccc}
\calP_{R}
&\;\cong\;&
\prod_{n>0}\prod_{m|n}
R[\z_m]
&\;\cong\;&
\prod_{n>0}
\prod_{\underset{\phi(m)>j\geq0}{m\ell=n}}
R\,,\\
\{f_{m}(u)\}_{m>0}
&\;\mapsto\;&
\{C_{\ell}(\z_m)\}_{m,\ell>0}
&\;\mapsto\;&
\{\gamma_{m,\ell,j}\}_{\underset{\phi(m)>j\geq0}{m,\ell>0}}\,.
\end{array}
\ee

All of these $R$-modules come with natural
filtrations
and these are compatible.
From equation~\eqref{eq:hdecomp} we can naturally consider
\be
\begin{aligned}
\HH_{R,N}
&\;:=\; (q;q)_{N-1}\HH_R
\=
\bigg\{\sum_{n=N}^\infty\sum_{k=0}^{n-1}a_{n,k}q^k (q;q)_{n-1}\;
\Big|\;a_{n,k}\inn R\bigg\}\\
&\=\prod_{n=N}^{\infty}
(R\oplus qR\oplus\cdots\oplus q^{n-1}R)(q;q)_{n-1}


\;\cong\;\prod_{n\geq N,\,n>k\geq0}R\,,
\end{aligned}
\ee
i.e. $\HH_{R,N}$ consists of sums $\sum_{n=N}^{\infty}P_{n}(q)(q;q)_{n-1}$, which in
coordinates is described by a collection $\{a_{n,k}\}_{n>k\geq0}$ with $a_{n,k}=0$
for $n<N$. Denote the quotient $\HH_R/\HH_{R,N}$ by $\HH_R^{N}$.
We thus have an increasing sequence $\HH_{R,N}$ of submodules of $\HH_R$ and a
decreasing sequence $\HH_R^N$ of quotients,~i.e.
\be
\label{eq:seq.app}
0\;\subset\;\cdots\;\subset\;\HH_{R,2}\;\subset\;\HH_{R,1}\=\HH_R\;
\twoheadrightarrow\;\cdots
\;\twoheadrightarrow\;\HH_R^{2}
\;\twoheadrightarrow\;\HH_R^{1}
\=0\,.
\ee
Note that as $R$-modules,
\be\label{eq:filt.quot.HH}
\HH_R^{N}
\,\;\cong\;\,
R[q]/(q;q)_{N-1}R[q]
\,\;\cong\;\,
\bigoplus_{n=1}^{N-1}
(R\oplus qR\oplus\cdots\oplus q^{n-1}R)(q;q)_{n-1}\,,
\ee
where the first isomorphism is induced by the canonical inclusion
$R[q]\hookrightarrow\HH_R$.
It follows that $\HH_R = \varprojlim_{N} \HH_R^{N}$ (or equivalently
$\bigcap_N\HH_{R,N}=\{0\}$). Note also that the exact sequence of $R$-modules
$0\to\HH_{R,N}\to\HH_R\to\HH_R^{N}\to0$ splits so that
$\HH_R\cong\HH_{R,N}\oplus \HH_R^{N}$ as $R$-modules for every $N$.

We now look at how expansions near roots of unity interact with
the filtration $\{\HH_{R,N}\}_{N>0}$ on $\HH_R$.
If we note that $(q;q)_{N-1}$ vanishes at a primitive $m$-th root of unity $\z_m$
to order $\lceil N/m\rceil-1$, then we see that $\iota$ maps this filtration
to the filtration $\{\calP_{R,N}\}_{N>0}$ on $\calP_R$ given by
\be
\calP_{R,N} \;:=\; \big\{f\inn\calP_R\;|\;
f_m(u)\=O(u^{\lceil N/m\rceil-1})\big\}
\,\;\cong\;\,
\prod_{n=N}^{\infty}\prod_{m|n}
R[\z_m]
\,\;\cong\;\,
\prod_{n=N}^{\infty}
\prod_{\underset{\phi(m)>j\geq0}{m\ell=n}}
R\,,
\ee
where the isomorphisms are of $R$-modules.
In coordinates, $\calP_{R,N}$ consists of $\{C_{\ell}(\z_m)\}_{m,\ell>0}$ in
$\calP_R$ satisfying $C_{\ell}(\z_m)=0$ for $m\ell<N$. As before,
we denote the quotient $\calP/\calP_{R,N}$ by~$\calP_R^{N}$. We
thus have an increasing sequence~$\calP_{R,N}$ of submodules of~$\calP_R$ and a
decreasing sequence~$\calP_R^{N}$ of quotients, just as in equation~\eqref{eq:seq.app}.
Moreover, we have a splitting of $R$-modules so
that~$\calP_R\cong\calP_{R,N}\oplus \calP_R^{N}$.
Note also that we have the canonical isomorphism
\be
\calP_R^{N}
\,\;\cong\;\,
\bigoplus_{m=1}^{N}
\big(R[\z_m][u]\+\mathrm{O}(u^{\lceil N/m\rceil-1})\big)\,,
\ee
which implies that $\calP_R = \varprojlim_{N} \calP_R^{N}$ (or equivalently
$\bigcap_N\calP_{R,N}=\{0\}$), just as for $\HH$.
We see that $\iota(\HH_{R,N})\subseteq\calP_{R,N}$ and therefore
we have well-defined maps
\be
\iota^{N}:
\HH_R^{N}\to\calP_R^{N}\,,
\ee
each factoring as~$\prod_{m\geq1}\iota_m^N$.
This is an injective map between free $R$-modules of the same rank (equal
$N(N-1)/2$), invertible after tensoring with $\BQ$. This implies in turn that
$\iota$ is an injection over $R$ and an isomorphism over $R\otimes \BQ$, e.g.,
\be
\begin{array}{ccc}
\HH_{\BZ}& \hookrightarrow
& \calP_{\BZ}\\
\cap & & \cap\\
\HH_{\BQ} & \cong & \calP_{\BQ}
\end{array}
\ee
for the original Habiro rings.

To prove the last statements, we consider the associated graded groups,
\be
\begin{aligned}
\calP_{R,N}/\calP_{R,N+1}
&\;\cong\;
\bigoplus_{m\ell=N}
\big(u^{\ell-1}R[\z_m]\llbracket u\rrbracket\+\mathrm{O}(u^{\ell})\big)
\;\cong\;
\bigoplus_{m\ell=N}R[\z_m]\,,\\
\HH_{R,N}/\HH_{R,N+1}
&\;\cong\;
R[q]/(1-q^N)R[q]\,,
\end{aligned}
\ee
where the last isomorphism is induced from the first isomorphism of
equation~\eqref{eq:filt.quot.HH}. Notice that
\be
\mathrm{rk}(\calP_{R,N}/\calP_{R,N+1})
\=
\sum_{m|N} \mathrm{rk}(R[z_m])
\=
\sum_{m|N} \phi(m)
\= N \= \mathrm{rk}(\HH_{R,N}/\HH_{R,N+1})\,,
\ee
which implies the values given in the above formulas for the ranks of $\HH_{R}^N$.
The map $\iota$ descends to these graded quotients. For $P(q)\in R[q]/(1-q^{N})$,
we multiply by $(q;q)_{N-1}$ and expand at $\z_m$ for $m|N$.
For
$q=\z_m(1-u)$
\be
\label{eq:poch.dml}
(q;q)_{m\ell-1}
\=
D_{m,\ell}\,u^{\ell-1}\+ O(u^\ell),
\qquad D_{m,\ell} \;:=\;m^{2\ell-1}(\ell-1)!\,,
\ee
by a simple calculation, which is left to the reader.
Therefore, $\iota$ is represented on these quotients by the map
\be
P(q)
\;\mapsto\,
\bigoplus_{m\ell=N}\;
\big(
D_{m,\ell}\,u^{\ell-1}\,
P(\z_m)\+\mathrm{O}(u^{\ell})\big)\,.
\ee

Since $D_{m,\ell}\in\BZ_{>0}$ is a non-zero integer, it follows that
$\iota$ is an injection
on these quotients and an isomorphism after tensoring with $\BQ$.
(Indeed, here we have used that $P(q)\in(1-q^N)\BZ[q]$ if and only if $P(\z_m)=0$
for all $m|N$.)
Given that $\iota$ respects the grading and is injective on the associated graded
pieces, it is injective.
This fact implies that understanding $\HH_R$ amounts to understanding the image of
$\iota$, which was the philosophy used in Definition~\ref{def.hab} of
Section~\ref{sub.hab}.

\medskip

We now restate the above considerations in terms of
the $R$-bases $\{q^k (q;q)_{n-1}\}_{k\leq 0,\,n>0}$ and $\{\z_m^{j}u^{\ell-1}\}$ and
the corresponding coordinates $\{a_{n,k}\}$ and $\{\gamma_{m,\ell,j}\}$ for~$\HH_R$
and~$\calP_R$ as defined in equations \eqref{eq:hdecomp}~and~\eqref{eq:gamma},
respectively. These bases give rise to a square matrix~
$\bM_{N}$ representing the map~$\iota^{N}$.
This matrix has integers entries and is independent of the ring~$R$.
(This is equivalent to noticing that the choice of basis and coordinates imply
isomorphisms $\HH_R\cong\HH_{\BZ}\otimes_{\BZ} R$ and
$\calP_R\cong\calP_{\BZ}\otimes_{\BZ} R$, with $\iota_R=\iota_\BZ\otimes_\BZ 1$,
with $\bM_N$ represents $\iota_\BZ^N$.)
Also, since~$\iota^{N}$ respects the filtrations, the matrix~$\bM_{N}$ is in block
lower triangular form, as illustrated for $N=5$ by the following equation.
\be
\begin{small}
\begin{aligned}
\left(\begin{array}{c}
\gamma_{1,1,0}\\
\hline
\gamma_{2,1,0}\\
\gamma_{1,2,0}\\
\hline
\gamma_{3,1,0}\\
\gamma_{3,1,1}\\
\gamma_{1,3,0}\\
\hline
\gamma_{4,1,0}\\
\gamma_{4,1,1}\\
\gamma_{2,2,0}\\
\gamma_{1,4,0}
\end{array}
\right)
\=
\left(\begin{array}{c|cc|ccc|cccc}
1 &   &   &   &   &   &   &   &   &  \\
\hline
1 & 2 & -2 &   &   &   &   &   &   &  \\
0 & 1 & 1 &   &   &   &   &   &   &  \\
\hline
1 & 1 & 1 & 3 & 0 & -3 &   &   &   &  \\
0 & -1 & 2 & 0 & 3 & -3 &   &   &   &  \\
0 & 0 & -1 & 2 & 2 & 2 &   &   &   &  \\
\hline
1 & 1 & 1 & 2 & 2 & -2 & 4 & 0 & -4 & 0\\
0 & -1 & 1 & -2 & 2 & 2 & 0 & 4 & 0 & -4\\
0 & -1 & 3 & 4 & -4 & 4 & 8 & -8 & 8 & -8\\
0 & 0 & 0 & -1 & -3 & -5 & 6 & 6 & 6 & 6
\end{array}
\right)
\left(\begin{array}{c}
a_{1,0}\\
\hline
a_{2,0}\\
a_{2,1}\\
\hline
a_{3,0}\\
a_{3,1}\\
a_{3,2}\\
\hline
a_{4,0}\\
a_{4,1}\\
a_{4,2}\\
a_{4,3}
\end{array}
\right)\,.
\end{aligned}
\end{small}
\ee
Finally, we can give an explict formula for the absolute value of determinant
of $\bM_{N}$.

\begin{proposition}
\label{prop:det.iotaN}
The number $D(N):=|\det(\bM_{N})|$ is given by
\be
D(N)
\= \prod_{n=1}^{N} D_{1}(n)D_{2}(n)\,,
\ee
where
\be
D_{1}(n) \= \prod_{m\ell=n}D_{m,\ell}^{\phi(m)}
\=
\prod_{m\ell=n}
m^{(2\ell-1)\phi(m)}(\ell-1)!^{\phi(m)}
\ee
with $D_{m,\ell}$ defined as in equation~\eqref{eq:poch.dml} and
\be
D_{2}(n) \= n^{\frac{n}{2}}\prod_{m|n}|\mathrm{disc}(\Phi_{m})|^{-\frac{1}{2}}
\= \prod_{m|n}\Big(\frac{n}{m}\prod_{p|m\,,\,p\text{ prime}}
p^{\frac{1}{p-1}}\Big)^{\frac{\phi(m)}{2}}\,.
\ee
\end{proposition}
\noindent Note that $D_2(n)$ is an integer since if $p|m$ then $\phi(m)$ is divisible
by $2(p-1)$ except for $m=p^k,2p^k$, where $\phi(p^k)=\phi(2p^k)$, which
can be seen to be integral for both even and odd~$n$.

We have tabulated the first few of these numbers below.
One can see their extremely rapid growth.
This illustrates how small
the Habiro ring is inside the set of functions near roots of unity with integral
Taylor expansions.
\begin{small}
\begin{center}
\def\arraystretch{1.5}
\begin{tabular}{|c||c|c|c|c|c|c|c|c|c|}
\hline
$N$ & $1$ & $2$ & $3$ & $4$ & $5$ & $6$ & $7$ & $8$ & $9$ \\ \hline\hline
$D_1(N)$ & $1$ & $2$ & $18$ & $768$ & $15000$ & $2.0\times10^{8}$
 & $8.5\times10^{7}$ & $6.5\times10^{13}$ & $5.1\times10^{15}$
\\ \hline
$D_2(N)$ & $1$ & $2$ & $3$ & $8$ & $5$ & $72$ & $7$ & $128$ & $81$ \\ \hline
$D(N)$ & $1$ & $4$ & $216$ & $1327104$ & $99532800000$
& $1.4\times10^{21}$ & $8.6\times10^{29}$ & $7.1\times10^{45}$
& $3.0\times10^{63}$\\
\hline
\end{tabular}
\end{center}
\end{small}
These numbers are not only very large, but also highly factored.
Here are two bigger examples illustrating both properties for $D(N)$:
\be
\begin{aligned}
D(25)
&\=
2^{1050}\cdot
3^{469}\cdot
5^{255}\cdot
7^{118}\cdot
11^{71}\cdot
13^{25}\cdot
17^{25}\cdot
19^{25}\cdot
23^{25}\;\approx\;2.35\times10^{1016}\,,\\
D(100)
&\=
2^{26102}\cdot
3^{12800}\cdot
5^{6404}\cdot
7^{3965}\cdot
11^{2158}\cdot
13^{1514}\cdot
17^{961}\cdot
19^{983}\cdot
23^{763}\cdot
29^{497}\\
&\qquad\times
31^{503}\cdot
37^{285}\cdot
41^{289}\cdot
43^{291}\cdot
47^{295}\cdot
53^{100}\cdot
59^{100}\cdot
61^{100}\cdot
67^{100}\cdot
71^{100}\\
&\qquad\times
73^{100}\cdot
79^{100}\cdot
83^{100}\cdot
89^{100}\cdot
97^{100}\;\approx\;9.33\times 10^{34419}\,.
\end{aligned}
\ee

\medskip

Since the nuymber D(N) is the cardinality of the cokernel of $\iota_\BZ^{N}$, we
see that begin in the image of $\iota^{N}$ is equivalent to a set of congruences
on the coordinates $\gamma_{m,\ell,j}$ to a total modulus $D(N)$.
In particular, we have a well-defined map
\be
(\iota^{N})^{-1}:\calP_{R}/\calP_R^{N}\;\to\;D(N)^{-1}R[q]/(q;q)_{N-1}R[q]\,,
\ee
and the condition for a given element $H\in\calP_{R}$ to be the image of $\iota$
is that
\be
(\iota^{N})^{-1}(H)\inn R[q]/(q;q)_{N-1}R[q]
\ee
for all $N\in\BZ_{>0}$. We can express this in terms of matrices as follows:

\begin{proposition}
\label{prop:imiota}
If $H\in\calP_{R}$ with coordinates $\gamma_{m,\ell,j}\in R$
($m,\ell\geq 1,0\leq j<\phi(m)$), then $H\in\iota(\HH_{R})$
if and only if
\be
\bM_{N}^{*} \,
\Big((\gamma_{m,\ell,j})_{\underset{0\leq j<\phi(m)}{m\ell<N}}\Big)
\;\equiv\; 0\pmod{D(N)}
\ee
for all $N\in\BZ_{>0}$, where $\bM_{N}^{*}:=D(N)\,\bM_{N}^{-1}\in M_{N(N-1)/2}(\BZ)$.
\end{proposition}

Note that~$D(N)$ and~$\bM_{N}^{*}$ have many common factors, which
simplifies~$\bM_{N}^{-1}$.
This means that in practice the congruences that one constructs can be simplified.
For example, using the previous coordinates in
equation~\eqref{eq:hdecomp} and equation~\eqref{eq:gamma}, we find that for~$N=5$
these conditions become
\be
\begin{small}
\begin{aligned}
\left(\begin{array}{c|cc|ccc|cccc}
1 &   &   &   &   &   &   &   &   &  \\
\hline
-1 & 1 & 2 &   &   &   &   &   &   &  \\
1 & -1 & 2 &   &   &   &   &   &   &  \\
\hline
-7 & -9 & -6 & 16 & -8 & 12 &   &   &   &  \\
-1 & 9 & 6 & -8 & 16 & 12 &   &   &   &  \\
17 & -9 & 18 & -8 & -8 & 12 &   &   &   &  \\
\hline
-13 & 9 & -13 & -32 & 0 & 0 & 36 & 0 & 9 & 12\\
-14 & -18 & -1 & 32 & -32 & 12 & 0 & 36 & -9 & 12\\
9 & 27 & 23 & 0 & 32 & 24 & -36 & 0 & 9 & 12\\
68 & -36 & 59 & -32 & 0 & 36 & 0 & -36 & -9 & 12
\end{array}
\right)
\left(\begin{array}{c}
\gamma_{1,1,0}\\
\hline
\gamma_{2,1,0}\\
\gamma_{1,2,0}\\
\hline
\gamma_{3,1,0}\\
\gamma_{3,1,1}\\
\gamma_{1,3,0}\\
\hline
\gamma_{4,1,0}\\
\gamma_{4,1,1}\\
\gamma_{2,2,0}\\
\gamma_{1,4,0}
\end{array}
\right)
\in
\left(\begin{array}{c}
R\\
\hline
4\,R\\
4\,R\\
\hline
72\,R\\
72\,R\\
72\,R\\
\hline
288\,R\\
288\,R\\
288\,R\\
288\,R
\end{array}
\right).
\end{aligned}
\end{small}
\ee
Summarising, we have found an explicit inductive set of congruences that
the coefficients of an element of $\calP_{R}$ must satisfy to be an element of
the image of $\iota$ of the naive Habiro ring of~$R$,
the first few of these congruences (corresponding to $N=4$) being
\be
\label{eq:cong1}
\begin{small}
\begin{aligned}
\-\gamma_{1,1,0} \+ \gamma_{2,1,0} \+ 2\gamma_{1,2,0}
&\cm 0\pmod{4}\,,\\
\gamma_{1,1,0} \- \gamma_{2,1,0} \+ 2\gamma_{1,2,0}
&\cm 0\pmod{4}\,,\\
\-7\gamma_{1,1,0} \- 9\gamma_{2,1,0} \- 6\gamma_{1,2,0} \+16 \gamma_{3,1,0}
\- 8\gamma_{3,1,1} \+ 12\gamma_{1,3,0}
&\cm 0\pmod{72}\,,\\
\-\gamma_{1,1,0} \+ 9\gamma_{2,1,0} \+ 6\gamma_{1,2,0} \- 8\gamma_{3,1,0}
\+ 16\gamma_{3,1,1} \+ 12\gamma_{1,3,0}
&\cm 0\pmod{72}\,,\\
17\gamma_{1,1,0} \- 9\gamma_{2,1,0} \+ 18\gamma_{1,2,0} \- 8\gamma_{3,1,0}
\- 8\gamma_{3,1,1} \+ 12\gamma_{1,3,0}
&\cm 0\pmod{72}\,.
\end{aligned}
\end{small}
\ee
These equations are not independent and we can reduce them to
\be
\label{eq:congrd1}
\begin{small}
\begin{aligned}
\gamma_{1,1,0} \- \gamma_{2,1,0} \+2\gamma_{1,2,0} \+4\gamma_{1,3,0}
&\cm 0\pmod{8}\,,\\
\gamma_{1,1,0} \- \gamma_{3,1,0} \- \gamma_{3,1,1} \-3\gamma_{1,3,0}
&\cm 0\pmod{9}\,,\\
\gamma_{1,2,0} \+\gamma_{3,1,1}
&\cm 0\pmod{3}\,.
\end{aligned}
\end{small}
\ee
Those familiar with the Habiro ring will easily
recognise these congruences as those discovered by Ohtsuki~\cite{Ohtsuki:poly}.
Indeed, we find that they are equivalent to the beginning of the expansions
\be
\gamma_{2,1,0}
\=
\sum_{k=0}^{\infty}\gamma_{1,k,0}\,2^{k}\in R_{2}^\wedge\,,
\quad\text{and}\quad
\gamma_{3,1,0}\+\z_3\,\gamma_{3,1,1}
\=
\sum_{k=0}^{\infty}\gamma_{1,k,0}\,(1\-\z_3)^{k}\in R_{3}^\wedge[\z_3]\,.
\ee


\subsection{The Habiro ring of a number field}

In the previous subsection, although everything was done over an arbitrary ground
ring $R$, the considerations were really based on the case when $R=\BZ$ (the
original Habiro ring), because the congruences needed to recognise whether an
element of $\calP_R$ comes from the naive Habiro ring of $R$ were independent of $R$
and came from this special case.
In this subsection, we will consider more general ground rings and describe the
relation between the naive Habiro ring and the Habiro ring studied in
Sections~\hbox{\ref{sec.intro}--\ref{sec.examples}}.
We will explain that the natural definition
involves twisting the compatibility conditions by suitable
Frobenius automorphisms similar to those that appeared in Definition~\ref{def.hab}
of Section~\ref{sub.hab}.
We will focus on ground
rings given by rings of integers (or $S$-integers, meaning that we adjoin the
reciprocal of a non-zero integer) of a number field, or various completions of this.

\medskip

Let $R$ be the ring $\calO_{\BK}[1/\Delta]$, where $\calO_{\BK}$ is the ring of
integers of a number field $\BK$ and
$\Delta$ any non-zero integer divisible by the discriminant of $\BK$.
Let $p$ be a prime that does not divide $\Delta$ and is therefore unramified, so
that
\be
p \= \mathfrak{p}_{1}\cdots\mathfrak{p}_{n}\,,
\ee
with the ideals $\mathfrak{p}_{i}$ distinct. This gives rise to an isomorphism
\be
R/pR \;\cong\; R/\mathfrak{p}_{1}R\times\cdots\times R/\mathfrak{p}_{n}R\,,
\ee
where each $R/\mathfrak{p}_{i}R\cong\BF_{q_i}$ with $q_i=|R/\mathfrak{p}_{i}R|$ is a
finite field with cyclic Galois group over $\BF_{p}$ generated by the
Frobenius automorphism
\be
x\mapsto x^p\,.
\ee
The Frobenius automorphisms on each factor $R/\mathfrak{p}_{i}R$ give rise to a
Frobenius
automorphism $\fr:R/pR\cong R/pR$ given by the same formula. Hensel's lemma states
that if a polynomial factors into irreducible polynomials over $\BZ/p\BZ$, then
this factorisation lifts to a unique factorisation over $\BZ/p^n\BZ$. Therefore,
if $\xi$ is a generator of the field $\BK$ with minimal polynomial $P(x)$, then
applying
Hensel's lemma to $P(x)$ lifts the Frobenius automorphism of $R/pR$ to an
automorphism of
$\fr:R/p^nR\cong R/p^nR$ for all $n\in\BZ_{>0}$. Hensel's lemma is completely
constructive, as was explained in Section~\ref{sub.padic.compute}. These Frobenius
lifts can be used to define automorphisms for any $R/MR$ for $M\in\BZ$ prime to
the discriminant of $\BK$. To do this, we write $M=\prod_{p\text{ prime}}p^{d_p}$.
The Chinese remainder theorem gives a canonical isomorphism
\be
R/MR \;\cong\; \prod_{p\text{ prime}}R/p^{d_p}R\,.
\ee
We can define $\fr:R/MR\to R/MR$ to be the Frobenius automorphism on the $p$-th
factor and the identity on the others.
Then for $m\in\BZ_{>0}$ (or even $m\in\BQ^{\times}$) we define
\be
\varphi_{m}\=\prod_{p}\fr^{v_{p}(m)}:R/MR\rightarrow R/MR\,,
\ee
where $\fr$ on $R/MR$ is simply the identity if $p$ does not divide $M$.
This can then be used to give Frobenius automorphisms on the completion of
the integers over all unramified primes at once. Consider the completion
\be
\widehat{R} \;:=\; \varprojlim_{M} R/MR \;\cong\; \prod_{p\text{ prime}}\!\!\!
R_p\,,
\ee
where $R_p:=\varprojlim_{n}R/p^nR\cong R\otimes\BZ_p$.
Notice that if $p|\Delta$ then $R_p=\{0\}$ is the zero ring. This completion then has
Frobenius automorphisms for each $m\in\BQ^{\times}$
\be
\varphi_{m}:\widehat{R}
\rightarrow
\widehat{R}\,.
\ee
We can lift $\varphi_{m}$ uniquely to an automorphism
$\varphi_{m}:\widehat{R}[\z_n]\llbracket
x\rrbracket\to\widehat{R}[\z_n]\llbracket x\rrbracket$ acting trivially on $\z_n$
and $x$. These then combine to an automorphism
$\varphi:\calP_{\widehat{R}}\to\calP_{\widehat{R}}$ defined by
\be
(\varphi\,f)_{m}
\=
\varphi_{m}(f_{m}(x))
\inn
\widehat{R}[\z_m]\llbracket x\rrbracket\,.
\ee
We will also use $\varphi$ to denote the composite map
$\calP_R\hookrightarrow\calP_{\widehat{R}}\overset{\varphi}{\rightarrow}
\calP_{\widehat{R}}$.
We can now restate the definition of the Habiro ring (Definition~\ref{def.hab}
of Section~\ref{sub.hab}) as follows.

\begin{proposition}
The Habiro $\calH_R$ of $R=\calO_{\BK}[1/\Delta]$ is given by
\be
  \calH_R
  \=\big\{H\in\calP_R\;\big|\;\varphi(H)\in\iota(\HH_{\widehat{R}})\big\}\,,
\ee
where $\HH_{\widehat{R}}$ is defined as in~\eqref{eq:Hnaive}. Equivalently,
$\calH_R=\calP_R\cap\calH_{\widehat{R}}$ with
$\calH_{\widehat{R}}=\varphi^{-1}(\iota(\HH_{\widehat{R}}))$.
\end{proposition}

\noindent Using Proposition~\ref{prop:imiota} of Section~\ref{sec:naive}, we can
reformulate this concretely as follows:

\begin{proposition}
\label{prop:hr.cong}
Let $H\in\calP_{R}$ with coordinates $\gamma_{m,\ell,j}\in R$
($m,\ell\geq 1,0\leq j<\phi(m)$). Then $H\in\calH_R$
if and only if
\be
\bM_{N}^{*} \,
\Big((\varphi_m\gamma_{m,\ell,j})_{\underset{0\leq j<\phi(m)}{m\ell<N}}\Big)
\;\equiv\; 0\pmod{D(N)}
\ee
for all $N\in\BZ_{>0}$, where $\bM_{N}^{*}$ is the matrix defined in
Proposition~\ref{prop:imiota} of Section~\ref{sec:naive}.
\end{proposition}

\noindent This gives an easy numerical check of whether a function near roots of
unity is an element of the Habiro ring of $R$.

\begin{remark}
In this section, we have only treated the Habiro ring $\calH_R$ and not its modules
$\calH_{R,\xi}$ indexed by $\xi\in K_3(\BK)$. Given that Theorem~\ref{thm.locals}
implies the completion $\calH_{\widehat{R},\xi}$ is a free $\calH_{\widehat{R}}$-module,
we can use similar descriptions to that of Proposition~\ref{prop:hr.cong} to describe
the modules by simply dividing elements by a chosen generator of
$\calH_{\widehat{R},\xi}$.
\end{remark}

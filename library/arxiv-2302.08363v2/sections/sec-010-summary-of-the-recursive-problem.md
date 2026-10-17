---
doc_id: arxiv-2302.08363v2
doc_title: "On the structure of trans-series in quantum field theory"
section_id: sec-010-summary-of-the-recursive-problem
section_title: "Summary of the recursive problem"
section_number: null
pages: 25-29
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.635
latex_coverage_ratio: 0.989
---
\label{gn-sum}

In contrast to the bosonic models studied in the previous section, the trans-series expansion of the integral equation 
of the Gross--Neveu model can be cast into a simple recursive problem. Here, we summarize its key 
ingredients, originally presented in \cite{mmr-an}.
 
We introduce the variable $\eta$ and the coupling $v$ such that
\begin{equation}
\frac{1}{v}-2\Delta\log v = 2B, \quad \omega = \ri v\eta.
\label{v-def}
\end{equation}
For the double expansion, it is convenient to define the trans-monomial
\begin{equation}
q= \re^{-1/(\Upsilon v)}v^{2\Delta/\Upsilon}.
\end{equation}
We then organize the expansion of $u(\eta) = u(\omega=\ri v \eta)$ as
\begin{equation}
u(\eta) = \sum_{\ell\geq 0} \sum_{n\geq 0}
 \left(\re^{\mp\frac{\ri\pi\Delta}{\Upsilon}}\right)^{\ell}  q^\ell v^{n-1} u^{(n,\ell)}(\eta).
\end{equation}
It is convenient to include the phase in the non-perturbative coupling,
\begin{equation}
\left(\re^{\mp\frac{\ri\pi\Delta}{\Upsilon}}\right)^{\ell}  q^\ell = q_\pm^\ell.
\end{equation}

The trans-series solution for $u$ can be found with a ``seed solution'' and an iterated integral operator. The seed solution is
\be
\bar{u}(\eta) = \frac{1}{v\eta} +  \sum_{n\geq 1}

q^{2n-1}_\pm

\frac{\bar{\rho}_n u_n}{\xi_n+v\eta},
\label{seed-solution}
\ee
where
\begin{equation}
u_k = u\left(\omega = \ri \xi_k\right),\qquad \xi_k = \frac{2k-1}{\Upsilon},
\end{equation}
and the $\bar\rho_n$ are real numbers,
\begin{equation}
\bar\rho_n=\frac{2}{\Upsilon} \frac{(-1)^{n}}{\Gamma(n)^2} \left(\frac{2n-1}{2\re}\right)^{2n-1} \left( \frac{2n-1}{2\Upsilon\re} \right)^{-\frac{2n-1}{\Upsilon}} \frac{\Gamma\big(\frac{3}{2} + \frac{2n-1}{2\Upsilon}\big)}{\Gamma\big(\frac{3}{2} - \frac{2n-1}{2\Upsilon}\big)},
\label{polepm}
\end{equation}
derived from the residues of $\rho(\omega)$,
\begin{equation}
\text{Res}_{\omega=\ri\xi_n\pm 0}\, \rho(\omega) = \left(\re^{\mp\frac{\ri\pi\Delta}{\Upsilon}}\right)^{2n-1}\ri \bar\rho_n.
\label{rho_factor}
\end{equation}
The expansion in $v$ can be solved by iterating the integral kernel $\mathfrak{I}$,
\begin{equation}
\left[\mathfrak{I} f\right](\eta) = - \frac{1}{\pi}\int_0^\infty \frac{\re^{-\eta'}P(\eta')}{\eta+\eta'} f(\eta')\rd\eta',
\end{equation}
where the kernel $P(\eta)$ is defined from the discontinuity of $\rho$, 
\begin{equation}
\rho(\re^{-\ri 0}\omega)-\rho(\re^{+\ri 0}\omega) = -2\ri v \re^{2B\xi} \re^{-\eta}P(\eta),
\label{P-def}
\end{equation}
and can be asymptotically expanded,
\begin{equation}
 \quad P(\eta) \approx \sum_{n\geq 0} v^n \sum_{m=0}^n d_{n+1,m} \eta^{n+1} (\log\eta)^m\sim d_{1,0}\eta + \CO(v).
 \label{P-expansion}
\end{equation}
The solution to the integral equation can then be organized as
\begin{equation}
u(\eta)= \sum_{m\geq 0} v^m [\mathfrak{I}^m\bar{u}](\eta) = (1-v\mathfrak{I})^{-1}\bar{u}(\eta)  .
\end{equation}
And we can also write the auxiliary functions
\begin{equation}
\ba
\bar{u}(\eta) &= \sum_{\ell\geq 0} q_\pm^\ell \bar{u}^{(\ell)}(\eta),\\
u^{(\ell)}(\eta) &= (1-v\mathfrak{I})^{-1}\bar{u}^{(\ell)}(\eta) = \sum_{n\geq 0} v^{n-1} u^{(n,\ell)}(\eta).
\ea
\label{ueta}
\end{equation}
Note that $u^{(n,\ell)}(\eta)$ is distinct from $\mathfrak{I}^n\bar{u}^{(\ell)}$ because both $\bar{u}(\eta)$ and the integral operator $\mathfrak{I}$ produce higher corrections in $v$.

The solution is not yet fully specified, because we still need to find the values $u_k$ in \eqref{seed-solution}. 
Defining the integrals
\begin{equation}
\mathfrak{I}_{k} f = \left[\mathfrak{I} f\right]\left(\tfrac{2k-1}{v\Upsilon}\right),\quad k\in\IN,
\end{equation}
we can write $u_k$ as
\begin{equation}
u_k=\frac{\Upsilon}{2k-1}+v \mathfrak{I}_k u + \frac{\Upsilon}{2}\sum_{n\geq 1}q^{2n-1}_\pm\frac{\bar\rho_{n} u_n}{k+n-1},\quad k\in\IN.
\label{eq_uk_v2}
\end{equation}
Following the notation of \eqref{ueta}, we define the expansions
\begin{equation}

u_k = \sum_{\ell \geq 0} q_\pm^\ell  u_k^{(\ell)},\qquad
u^{(\ell)}_k = \sum_{n\geq 0} v^{n} u^{(n,\ell)}_k.

\end{equation}
This leads to a solvable recursive problem, as presented in \cite{mmr-an},
\begin{align}
u_k^{(0)}&=\frac{\Upsilon}{2k-1}+v\mathfrak{I}_k(1-v\mathfrak{I})^{-1}{\bar u^{(0)}}\label{uks-seed},\\
u_k^{(s)}&=v \mathfrak{I}_k(1-v\mathfrak{I})^{-1}{\bar u^{(s)}} + \frac{\Upsilon}{2}\sum_{\tfrac{s+1}{2}\geq r\geq 1} \frac{\bar\rho_r u_r^{(s+1-2r)}}{k+r-1}\label{uks-recurs}.
\end{align}
The r.h.s. does not contain $u^{(s)}_k$, only $u_{k'}^{(s')}$ with $s<s'$ and $k'\leq \frac{s+1}{2}$. The $u_k^{(n,m)}$ can be obtained by expanding in $v$ the operator $\mathfrak{I}_k$ as well as $\bar{u}^{(s)}$ itself.

An important intermediate ingredient is $u(\omega=\ri)$, which we denote by $u_\ri$. It can be calculated, using the above ingredients, from the equation:
\begin{equation}
u_\ri=1+v \left[\mathfrak{I} (1-v\mathfrak{I})^{-1} \bar{u}\right]\left(v^{-1}\right) + \Upsilon\sum_{n\geq 1}
q^{2n-1}_\pm
\frac{\bar\rho_{n} u_n}{\Upsilon+2n-1}.
\label{eq_ui_v2}
\end{equation}
We will need this value to compute $\CF(h)$, and it is also central to the change of variables from $v$ to $\tilde{\alpha}$.

To compute the free energy let us define the ``bare energy'',
\begin{equation}
f_v = 1 - v [\mathfrak{I}  (1-v\mathfrak{I})^{-1} \bar{u}]\left(-v^{-1}\right) - \Upsilon \sum_{n\ge 1} 
q^{2n-1}_\pm
\frac{\bar\rho_{n} u_n}{2n-1-\Upsilon}.
\end{equation}
With it, the trans-series for the free energy can be written as
\begin{equation}
\mathcal{F}(h) \sim
-\frac{h^2}{2\pi} \left\{u_\ri\times f_v + \CC_{\text{IR}}^\pm \re^{-\frac{2}{\tilde{\alpha}}}{\tilde\alpha}^\Delta \right\}.
\label{eq_freeF}
\end{equation}
As before, we define,
\begin{equation}
\ba
u_\ri &= \sum_{n\geq 0, \ell\geq 0} u_\ri^{(n,\ell)} q^\ell_\pm v^n,\\
f_v &= \sum_{n\geq 0, \ell\geq 0} f_v^{(n,\ell)} q^\ell_\pm v^n,\\
\left\{u_\ri\times f_v\right\} &= \sum_{n\geq 0, \ell\geq 0} \CF_v^{(n,\ell)} q^\ell_\pm v^n.
\ea
\end{equation}

The above procedure leads to trans-series in $v$. However, we are interested in trans-series in the more natural coupling $\tilde{\alpha}$, defined in \eqref{tilde-alpha-def}.
Using the mass gap for the Gross--Neveu model \eqref{eq_mass_gap_GN}, we can relate $v$ and $\tilde{\alpha}$ through the equation
\begin{equation}
\left(\frac{1}{2v}-\Delta\log v\right) - \log u_\ri = \left(\frac{1}{\tilde{\alpha}}-\Delta\log\tilde{\alpha}\right)+\frac{\Upsilon}{2}\log\Upsilon +\log 2.
\label{v-to-a}
\end{equation}
It is also convenient to write
\begin{equation}
y_\pm = \Upsilon  2^{2/\Upsilon } \left(u_\ri\right)^{2/\Upsilon}q_\pm,
\label{k-to-q}
\end{equation}
where
\begin{equation}
y_\pm = \left(\re^{\mp\frac{\ri\pi\Delta}{\Upsilon}}\right)\re^{- \frac{2}{\Upsilon \tilde{\alpha}}}\left(\tilde\alpha\right)^{\frac{2\Delta}{\Upsilon}}.
\end{equation}
The most convenient way of changing from $v$ to $\tilde{\alpha}$ is to treat $v$ and $q_\pm$ as independent parameters and change variables into $\tilde{\alpha}$ and $y_\pm$ using both \eqref{v-to-a} and \eqref{k-to-q}. Let us also introduce the notation

\begin{equation}
\ba



q_\pm &= \sum_{\ell\geq 1, n\geq 0} q_{n,\ell} y^\ell_\pm \tilde\alpha^n.\\
\left\{u_\ri\times f_v\right\} &= \sum_{\ell\geq 0, n\geq 0} a_{n, \ell} y^\ell_\pm \tilde\alpha^n.\\
\ea
\end{equation}

With these ingredients we can derive the real coefficients $a_{n, \ell}$, from which we construct $\CG_n(y)$ as in (\ref{CGdef}). 






Since the overall phase of the trans-series sectors factors out, it is irrelevant for considerations of convergence.


\subsubsection{Leading orders in \texorpdfstring{$\tilde{\alpha}$}{alpha}}

The leading order in $\tilde{\alpha}$ is obtained by neglecting all terms with the integral operator $\mathfrak{I}$. In this case we obtain simple recursive relations. The $u_k$ are solved by
\begin{equation}
u_k^{(0,0)}=\frac{\Upsilon}{2k-1},\qquad
u_k^{(0,s)}=\frac{\Upsilon}{2}\sum_{\tfrac{s+1}{2}\geq r\geq 1} \frac{\bar\rho_r u_r^{(0,s+1-2r)}}{k+r-1},
\end{equation}
which is simple to solve order by order, although hard to solve in closed form.
Similarly, we obtain
\begin{equation}
\ba
u_\ri^{(0,0)}&=1,\qquad
u_\ri^{(0,s)}=\Upsilon\sum_{\tfrac{s+1}{2}\geq r\geq 1} \frac{\bar\rho_r u_r^{(0,s+1-2r)}}{2r-1+\Upsilon},\\
f_v^{(0,0)}&=1,\qquad
f_v^{(0,s)}=-\Upsilon\sum_{\tfrac{s+1}{2}\geq r\geq 1} \frac{\bar\rho_r u_r^{(0,s+1-2r)}}{2r-1-\Upsilon}.
\ea
\end{equation}
From these building blocks, regular power series manipulations are sufficient to extract $a_{0, \ell}$. For example, we obtain
\begin{equation}
\ba 
a_{0, 0}&=1,
\qquad
a_{0, 1}=
\frac{2^{\frac{\Upsilon -2}{\Upsilon }} \Upsilon ^2 \bar{\rho }_1}{\Upsilon ^2-1}
,
\qquad
a_{0,2}=
\frac{2^{\frac{\Upsilon -4}{\Upsilon }} \Upsilon ^2 \bar{\rho }_1^2}{(\Upsilon +1)^2}
,\\
a_{0,3}&=
\frac{1}{3} 2^{-\frac{\Upsilon +6}{\Upsilon }} \left(\frac{3 \Upsilon ^2 (3 \Upsilon -7) \bar{\rho }_1^3}{(\Upsilon +1)^3}+\frac{4 \bar{\rho }_2}{\Upsilon ^2-9}\right)



.
\ea
\end{equation}
All the $a_{n,\ell}$ are polynomials in the residues $\bar\rho_i$, but only monomials 
$\bar\rho_{i_1}^{p_1}\bar\rho_{i_2}^{p_2}\cdots\bar\rho_{i_k}^{p_k}$ that satisfy

\begin{equation}
\sum_{j=1}^k p_j (2i_j-1) = \ell
\end{equation}

contribute to $a_{n,\ell}$. The polynomial coefficients for $a_{0,\ell}$ are rational up to an 
overall irrational power of $2$, and only at higher orders in $\tilde\alpha$ does one find 
transcendental numbers. Nevertheless, the $\bar\rho_k$ are themselves transcendental, as can be seen in \eqref{polepm}.



The next to leading order in $\tilde{\alpha}$ can be immediately obtain from the leading one. Because the perturbative part of $\bar{u}(\eta)$ is one order lower than the non-perturbative, i.e.
\be
u^{(0,0)}(\eta)= \frac{1}{\eta} , \qquad u^{(0,n)}(\eta)= 0, \qquad u^{(1,\ell)}(\eta)= \bar{u}^{(\ell)}(\eta)\big|_{v=0},
\ee
the recursive problem is the same and the solution only differs by an overall constant.
Concretely,
\begin{equation}
u_k^{(1,s)} = -\Delta u_k^{(0,s)},\quad
u_\ri^{(1,s)}=-\Delta u_\ri^{(0,s)},\quad f_v^{(1,s)}=-\Delta f_v^{(0,s)} \quad \CF_v^{(1,s)}=-2\Delta \CF_v^{(0,s)}.
\label{lo-to-nlo}
\end{equation}
For the change of variables, we find first that 
\begin{equation}
v = \frac{\tilde{\alpha}}{2}+\CO(\tilde{\alpha}^2),
\end{equation}
without any term proportional to $q_\pm$ at order $\tilde{\alpha}$ or lower. Furthermore,

\begin{equation}
q_{1, \ell} = \frac{\Delta \ell}{\Upsilon} q_{0, \ell}, 
\end{equation}

which leads to

\begin{equation}
a_{1, \ell} = \Delta\left(\frac{\ell}{\Upsilon}-1\right)a_{0, \ell}.
\label{F1-f0}
\end{equation}
Naturally, $\CG_1(y)$ has the same radius of convergence as $\CG_0(y)$.
At the next order in $\tilde\alpha$, there are no such shortcuts.


\subsubsection{Numerical analysis}

Using these recursion relations, the coefficients $a_{0,\ell}$ can be obtained analytically, order by order. However, their expressions are very intricate and a general closed formula is unreachable. 

One straightforward approach is to obtain the coefficients as exact functions of $N$. This way, one can quickly generate data for different values of $N$, but it takes significant time to compute the series. We calculated 20 exact coefficients in this form. In a similar strategy to previous cases, we estimated the radius of convergence $R$ with the 17-th coefficient of the second Richardson transform of $a_{0,\ell}/a_{0,\ell+1}$. The convergence error is below 1\%.
In Fig. \ref{rad-gn-plot}, we plot this estimate with all values of $N$ between 6 and 25, as well as from 30 to 100 with steps of 10 and then from 100 to 1000 with steps of 100.  In the large $N$ limit we seem to have $R(0)=1$, which agrees with the explicit large $N$ solution, as we explain below. Extrapolating to non-integer values of $N$, the radius seems to diverge at $\Delta=1/3$ ($N=5$). This is consistent with the fact that the trans-series vanishes at $N=5$ (there is only perturbation theory and the IR renormalon).

\begin{figure}
\centering
\includegraphics[width=0.6\textwidth]{radius.pdf}
\caption{Estimates for the radius of convergence $R$ as a function of $\Delta=(N-2)^{-1}$.}
\label{rad-gn-plot}
\end{figure}
 

\begin{table}
\centering
\arraycolsep=3mm
\begin{tabular}{llll}
\toprule
 $N$ & $R$ &  $R_h/m$ & $b_0$\\
 \midrule
 6 & $1.588595196530307661805628(3\pm 7)$ & 0.71482$\dots$ & $2.500000(0 \pm 4)$ \\
 7 & $1.0901795077562836000(83\pm 13)$ & 0.80858$\dots$ & $2.500000(2\pm 7 )$ \\
 8 & $0.969970536544952097(5\pm 4)$ & 0.85994$\dots$ & $2.5000(0\pm 5)$ \\
 9 & $0.92721010523279402(59\pm 35)$ & 0.89194$\dots$ & $2.499(99\pm 10)$ \\
 10 & $0.9101379331724643(0\pm 8)$ & 0.91349$\dots$ & $2.500(0\pm 8)$ \\
 11 & $0.903644442840670(26 \pm 11)$ & 0.92881$\dots$ & $2.50(00\pm 14)$ \\
 12 & $0.90204273932404(39\pm 22 )$ & 0.94016$\dots$ & $2.5(00\pm 22)$ \\
 1000 & $0.997821(23 \pm 14 )$ & 0.99997$\dots$ & $2.4(9\pm 2)$ \\
\bottomrule
\end{tabular}
\caption{Estimated radius as a function of $N$, using 200 numeric coefficients. $R$ is the radius in the $y$-plane, while $R_h$ is the radius in the $h$-plane. }
\label{tabrad}
\end{table}

More efficiently, one can calculate the coefficients numerically from the onset. Taking 200 digits of precision in the calculation of the  $\bar\rho_n$, one can generate 200 coefficients at fixed $\Delta$ in a few minutes.  We can obtain more precise estimates for the radius this way, see table \ref{tabrad}. We estimate the error from the convergence of successive Richardson transforms. Strikingly, the convergence is much faster than in the case of bosonic models. We do not compute the radius of convergence for the subleading series 
in this model, since we already know that it is identical to $R$ due to \eqref{F1-f0}.

It is also instructive to write the radius in terms of the variable $h$, which can be related to $y$ through \eqref{tilde-alpha-def}. The radius in the $h$-plane, $R_h$, is related to the radius in the $y$ plane by

\begin{equation}
R_h = m \frac{\Gamma (1-\Delta )}{(2 \re)^{\Delta }} R^{-\frac{1}{2} (1-2 \Delta )}.
\end{equation}
The exact solution $\CF(h)$ is expected to be singular around its zero at $h=m$, hence one could conjecture that the radius of convergence of the trans-series in the $h$-plane should be $m$. This is not the case for our radius estimate $R_h$, except at large $N$, as can be seen in table \ref{tabrad}. However, as we previously discussed, this radius is simply an approximation of the radius of convergence of the full trans-series.





Lastly, assuming the form \eqref{an-bn-R},
 we can estimate $b_0$ by evaluating the auxiliary series on the l.h.s. of (\ref{bn-seq}) for $n=0$, 
where we must plug in the estimate for the radius in table \ref{tabrad}.
Our results suggest that $b_0=5/2$ and $b_1=3/2$ independently of $\Delta$. Like in the case of bosonic models, one must account for the error both from the convergence of the sequence and from the estimate of $R$.

---
doc_id: arxiv-2302.08363v2
doc_title: "On the structure of trans-series in quantum field theory"
section_id: sec-010-summary-of-the-recursive-problem
section_title: "Summary of the recursive problem"
section_number: null
pages: 25-28
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.985
doc_brief: "On the structure of trans-series in quantum field theory — Many observables in quantum field theory can be expressed in terms of trans-series, in which one adds to the perturbative series a typically"
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

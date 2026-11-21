---
doc_id: arxiv-hep-th-9609174v2
doc_title: "arXiv:hep-th/9609174v2 23 Sep 1996"
section_id: sec-003-22-universal-correlations
section_title: "Universal correlations"
section_number: 2.2
pages: 8-11
source_pdf: 9609174v2.pdf
source_sha256: 87885f4d03661f26
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.994
doc_brief: "arXiv:hep-th/9609174v2 23 Sep 1996 — We prove the universality of correlation functions of chiral unitary and unitary ensembles of ran- dom matrices in the microscopic limit."
---
\noindent
Theorem 1 can be used to establish a remarkable universal form of
spectral correlators of the model (\ref{chUE1}).
We shall consider
the spectral density $\rho(\lambda)$, and 
higher order correlators, in the
same microscopic limit as above.

\vspace{12pt}\noindent
To begin, we recall the expression for 
the integration kernel $K_N(\lambda,\mu)$ 
associated with the eigenvalue problem
for the positive-definite hermitian
matrix $H=W^\dagger W$,
\begin{eqnarray}
K_N(\lambda,\mu)\!&\!=\!&\!
(\lambda\,\mu)^{\alpha/2}\,
\e^{-\frac{N}{2}(V(\lambda)+V(\mu))} \,
\frac1N \sum_{i=0}^{N-1} 
\frac{P^{(\alpha)}_i(\lambda)P^{(\alpha)}_i(\mu)}{h^{(\alpha)}_i}
\nonumber \\
\!&\!=\!&\!
(\lambda\,\mu)^{\alpha/2}\,
\e^{-\frac{N}{2}(V(\lambda)+V(\mu))} \,
\frac1N\,\frac{-r^{(\alpha)}_{N-1}}{h^{(\alpha)}_{N-1}}
\frac{P^{(\alpha)}_N(\lambda)P^{(\alpha)}_{N-1}(\mu)-
P^{(\alpha)}_{N-1}(\lambda)P^{(\alpha)}_{N}(\mu)}{\lambda-\mu}.
\label{kernel}
\end{eqnarray}
Here use has been made of the Christoffel-Darboux identity.
In the large-$N$ limit
we may drop the superscript $\alpha$ in 
$r^{(\alpha)}_n=-p^{(\alpha)}_n/p^{(\alpha)}_{n+1}$. This is 
because the general recursion relation 
(the counterpart of eq. (\ref{vnn-1})
for general $\alpha$)
\begin{equation}
0=
N (\hat{\lambda}V'(\hat{\lambda}))_{nn}
-2n-\alpha-1
\label{vnn-1alpha}
\end{equation}
which determines $r^{(\alpha)}(t)$
leads, in the large-$N$ limit (\ref{lim}), 
to the same (\ref{qn}) for any finite $\alpha$.

\vspace{12pt}\noindent
On the other hand, the norms of the polynomials can be evaluated 
iteratively:
\begin{eqnarray}
\tilde{h}^{(\alpha+1)}_n&=&
\int_0^\infty \d\lambda\,\lambda^{\alpha+1}\,\e^{-NV(\lambda)}
\tilde{P}_n^{(\alpha+1)}(\lambda) 
\tilde{P}_n^{(\alpha+1)}(\lambda) 
\nonumber\\
&=&\int_0^\infty \d\lambda\,\lambda^{\alpha}\,\e^{-NV(\lambda)}
\left( P^{(\alpha)}_{n+1}(\lambda)-P^{(\alpha)}_n(\lambda) \right)
\tilde{P}_n^{(\alpha+1)}(\lambda) 
\nonumber\\
&=&\int_0^\infty \d\lambda\,\lambda^{\alpha}\,\e^{-NV(\lambda)}
\left(-P^{(\alpha)}_n(\lambda) \right)
\frac{p^{(\alpha)}_{n+1}}{p^{(\alpha)}_n}{P}_n^{(\alpha)}(\lambda) 
=\frac{{h}^{(\alpha)}_n}{r_n} ~,\\
{h}^{(\alpha+1)}_n&=&
\frac{\tilde{h}^{(\alpha+1)}_n}{\tilde{P}^{(\alpha+1)}_n(0)^2}
={h}^{(\alpha)}_n
\left( \frac{\alpha+1}{N\,u(t)/2} \right)^2 .
\end{eqnarray}
We therefore obtain
\begin{equation}
{h}^{(\alpha)}_n =
\frac{1}{N^{2\alpha+1}}
(\alpha!)^2
\left(\frac{2}{u(t)}\right)^{2\alpha} h(t)
+\mbox{~higher orders in }\frac1N
\ \ \ \ \left(h(t) \equiv h^{(0)}(t) \right) ~.
\label{halpha}
\end{equation}
Using Theorem 1 and inserting eq.~(\ref{halpha}) into 
(\ref{kernel}),
we obtain a universal form of the kernel (the Bessel kernel
of order $\alpha$)
in the microscopic limit
\begin{equation}
\lim_{N\rightarrow\infty} \frac1N\, 
K_N(\frac{x}{N^2}, \frac{y}{N^2})=
\frac{u(1)}{2} 
\frac{
\sqrt{x} J_{\alpha+1} ( u(1)\sqrt{x} ) J_\alpha ( u(1)\sqrt{y} )
-
J_\alpha ( u(1)\sqrt{x} ) \sqrt{y} J_{\alpha+1} ( u(1)\sqrt{y} )
}{x-y} .
\label{Besker}
\end{equation}

\vspace{12pt}\noindent
The only way this asymptotic kernel depends on the potential
$V(\lambda)$ 
is through the parameter $u(1)$.
As we shall show now, even this dependence
is of a highly universal form. 
Let us compare eqs.~(\ref{vNN}) and (\ref{qn}) at $t=1$
with the explicit expression for the
large-$N$ spectral density $\rho(z)$ 
having  support on a single interval $[-a,a]$
\cite{BB}. 
\begin{eqnarray}
&&\rho(z)=\frac{\sqrt{a^2-z^2}}{2\pi} 
\sum_{k} g_k \sum_{n=0}^{k-1}
\left( {2n \atop n} \right) \left({a^2 \over 4}\right)^n
z^{2k-2n-2},\\
&& \frac12 \sum_{k} g_k \left({2k \atop k}\right) 
\left( {a^2 \over 4}\right)^{k}=1 ~.
\end{eqnarray}
This enables us to relate the parameters $r(1)$ and $u(1)$ to
$a$ and $\rho(0)$, respectively,
\begin{equation}
a ~=~ 2\sqrt{r(1)} ~~~,~~~~\ \ 
\rho(z\!\!=\!\!0) ~=~ \frac{u(1)}{2\pi}.
\label{rho0}
\end{equation}
The kernel (\ref{Besker}) 
therefore only depends on the potential $V(\lambda)$
in the indirect way of setting the scale $\rho(0)$. It has clearly been
the assumption throughout that $\rho(\lambda) \neq 0$. This was the
starting point of the physical motivation from field theory
(spontaneously
broken chiral symmetries, which through the Banks-Casher relation 
(\ref{BC}) entails a non-vanishing spectral density at the origin).
Moreover, it is known that the critical condition 
$\rho(0)=0$
for a transition where the intervals of support move away from the
origin is equivalent to $P_N(0)=0$ 
for the monically normalized polynomials \cite{Mor}.
If we go back to our 
proof of Theorem 1, this was precisely the condition we had to impose
in order to be able to find a smooth continuum limit of the orthogonal
polynomials in the large-$N$ limit.
Thus, under the assumption 
that the normalization (\ref{normal}) is possible,
the constants $u(1)$ and $r(1)$
are determined to be positive from
the identification (\ref{rho0}).

\vspace{12pt}\noindent
It finally remains us to relate the $s$-point correlation functions of
$\sigma_N$ ($\rho_N$) of eigenvalues of $H=W^\dagger W$ (or $M$)
to the kernel $K_N$ in eq.~(\ref{Besker}). The former is defined as
\begin{eqnarray}
&&\sigma_N(\lambda_1,\cdots,\lambda_s)=
\left\langle \prod_{a=1}^s \frac{1}{N} 
{\rm tr}\, \delta (\lambda_a-H)\right\rangle=
\det_{1\leq a,b \leq s} K_N (\lambda_a,\lambda_b),\\
&&\rho_N(z_1,\cdots,z_s)=
\left\langle \prod_{a=1}^s \frac{1}{2N} 
{\rm tr}\, \delta (z_a-M)\right\rangle=
| z_1 | \cdots | z_s |\, 
\sigma_N(z_1^2,\cdots,z_s^2),
\end{eqnarray}
respectively.
Therefore all the formulae for their 
microscopic limits ($x_a=N^2\lambda_a$, $\zeta_a=N z_a$ fixed)
\begin{eqnarray}
&&\sigma_{\rm S}(x_1,\cdots,x_s)\equiv
\lim_{N\rightarrow\infty}\frac{1}{N^s}
\sigma_N (\frac{x_1}{N^2},\cdots,\frac{x_s}{N^2}) ,\\
&&\rho_{\rm S}(\zeta_1,\cdots,\zeta_s)\equiv
\lim_{N\rightarrow\infty}
\rho_N(\frac{\zeta_1}{N},\cdots,\frac{\zeta_s}{N})=
| \zeta_1 | \cdots | \zeta_s |\, 
\sigma_{\rm S}(\zeta_1^2,\cdots,\zeta_s^2),
\end{eqnarray}
that were previously calculated for 
the Laguerre (in the $H$-picture) or 
chiral Gaussian (in the $M$-picture) 
unitary ensemble \cite{V93,NS}, hold universally.

\vspace{12pt}\noindent
In particular, 
the spectral density of the chiral unitary ensemble
\begin{equation}
\rho_N(z)=\left\langle \frac{1}{2N}
\, {\rm tr}\, \delta( z- M
)\right\rangle 
=| z | K_N (z^2, z^2)
\end{equation}
takes the universal form
\begin{equation}
\rho_{\rm S} (\zeta)=
\left( \pi \rho(0) \right)^2
|\zeta|
\left(
J_\alpha^2(2\pi\rho(0)  \zeta) -
J_{\alpha+1}(2\pi\rho(0)  \zeta)
J_{\alpha-1}(2\pi\rho(0)  \zeta)
\right)
\end{equation}
in the microscopic limit.
As expected from the Gaussian case, 
a matching condition
between the microscopic and macroscopic (ordinary large-$N$) 
spectral densities is satisfied:
\begin{equation}
\lim_{\zeta\rightarrow\infty}\rho_{\rm S}(\zeta)=
\rho(0) .
\end{equation}

\setcounter{equation}{0}

---
doc_id: arxiv-2302.08363v2
doc_title: "On the structure of trans-series in quantum field theory"
section_id: sec-007-trans-series-computation
section_title: "Trans-series computation"
section_number: null
pages: 15-20
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.987
doc_brief: "On the structure of trans-series in quantum field theory — Many observables in quantum field theory can be expressed in terms of trans-series, in which one adds to the perturbative series a typically"
---
\label{sec_bosonic_models}
In this section, we will compute the formal power series $\varphi_\ell(\tilde\alpha)$ appearing in the trans-series \eqref{eq_free_energy_transseries}. Our computation is limited to the leading and subleading corrections in $\tilde{\alpha}$, but to arbitrary order $\ell$ in the exponential corrections. This will be essential in order to extract the large order behavior of the coefficients that appear in the partial series $\mathcal{G}_n(y)$ of \eqref{phi-y}, for $n=0$, $1$.

The computation is split in two main steps. First, we determine the trans-series of the free energy $\mathcal{F}(h)$ in the small parameters $1/B$ and $\re^{-2B\xi_1}$, by working out the equations \eqref{eq_Q_integral_equation}, \eqref{eq_epsilon_0} and the boundary condition \eqref{eq_boundary_condition}. In the second step, we use \eqref{eq_alpha_tilde_def} to determine $B$ as a trans-series in $\tilde{\alpha}$ and $y = \tilde\alpha^{-2a\xi_1} \re^{-2\xi_1/\tilde{\alpha}}$. With this later result, we will be able to write the trans-series we obtained in the first step as a trans-series in the coupling $\tilde\alpha$.

From \eqref{eq_Q_integral_equation}, we have to compute $Q(\ri\xi)$ at $\xi=\xi_m$ as a trans-series in $1/B$, which we will need later for $\epsilon_+(\ri\kappa)/G_+(\ri\kappa)$ and the free energy. After evaluating \eqref{eq_Q_integral_equation} at $\omega=\ri\xi_m$, we obtain the expression
\begin{equation}
Q(\ri\xi_m)= \frac{1}{2 \pi \ri} \int_\mathbb{R} \frac{G_-(\omega) g_+(\omega)}{\omega+ \ri\xi_m} \rd \omega + \frac{1}{2 \pi \ri} \int_\mathbb{R} \frac{\re^{2 \ri B\omega} \sigma (\omega) Q(\omega)}{\omega+ \ri\xi_m} \rd \omega.
\label{eq_Qm_integral_equation}
\end{equation}
Let us compute the first integral in \eqref{eq_Qm_integral_equation}. After splitting $g_+(\omega)$ into terms proportional to $h$ and $m$, as in \eqref{eq_g}, we obtain for the terms multiplied by $h$ 
\begin{multline}
\ri h \frac{1}{2\pi\ri} \int_\mathbb{R} \frac{G_-(\omega)}{\omega + \ri\xi_m} \frac{1-\re^{2\ri B\omega}}{\omega} \rd \omega = -\frac{kh (2B)^{1/2}}{\pi \xi_m} \biggl[ 2 \sqrt{\pi} - \frac{\log(2B)}{B}a I_0\\
+ \frac{1}{B}\left( a I_1 + b I _0 - \frac{I_0}{\xi_m} \right) \biggr]
+ h \frac{G_+(\ri\xi_m)}{\xi_m} + h \sum_{n\ge 1} \frac{\ri \sigma^\pm_n G_+(\ri\xi_n)}{(\xi_n+\xi_m)\xi_n} \re^{-2B\xi_n} + \mathcal{O}\big(B^{-1}\big),
\label{eq_h_part_2}
\end{multline}
where we have defined the integrals
\begin{align}
I_0 &= -\frac{1}{2}\int_0^\infty \frac{\re^{-y}}{\sqrt{y}} \rd y = -\frac{\sqrt{\pi}}{2},\\
I_1 &= -\frac{1}{2}\int_0^\infty \frac{\re^{-y}}{\sqrt{y}}\log(y) \rd y = \frac{\sqrt{\pi}}{2}(\gamma_E+\log(4)).
\end{align}
To obtain \eqref{eq_h_part_2}, we deform the contour downwards for the integral with $1/\omega$, and upwards for the integral with $\re^{2\ri B \omega}/\omega$. The downwards contour picks the pole at $\omega = -\ri\xi_m$, which gives the term proportional to $G_+(\ri\xi_m)$ in the second line. The upwards contour picks the discontinuity of $G_-(\omega)$, which yields the first term in square brackets, and also picks the singularities of $G_-(\omega)$, which yields the sum over the exponentials in the second line. 

For the terms in $g_+(\omega)$ with $m$, we find
\begin{multline}
\frac{\ri m\re^B}{2} \frac{1}{2\pi\ri} \int_\mathbb{R} \frac{G_-(\omega)}{\omega + \ri\xi_m} \left( \frac{\re^{2\ri B\omega}}{\omega-\ri} - \frac{1}{\omega+\ri} \right) \rd \omega = -\frac{m\re^B}{2}\biggl[ \frac{G_+(\ri\xi_m)-G_+(\ri)}{\xi_m-1}\\
+ \sum_{n\ge 1} \frac{\ri\sigma^\pm_n G_+(\ri\xi_n)}{(\xi_n + \xi_m)(\xi_n -1)}\re^{-2B\xi_n} - \frac{k}{\sqrt{\pi} \xi_m}(2B)^{-1/2} \biggr] + \mathcal{O}\big( B^{-1} \big).
\label{eq_m_part_2}
\end{multline}
In this case, the first term arises from the two poles at $\omega = -\ri$ and $-\ri\xi_m$, when deforming the contour downwards for the term $-1/(\omega+\ri)$. The sum over the exponentials arises from the term $\re^{2\ri B\omega}/(\omega-\ri)$, when deforming the contour upwards and picking all the poles of $G_-(\omega)$. The last term arises from the integral over the discontinuity of $G_-(\omega)$.

Next, we consider the second integral in \eqref{eq_Qm_integral_equation}, for which we deform the contour upwards, picking both the discontinuity and the poles of $\sigma(\ri\xi)$:
\begin{equation}
\frac{1}{2 \pi \ri} \int_\mathbb{R} \frac{\re^{2 \ri B\omega} \sigma (\omega) Q(\omega)}{\omega+ \ri\xi_m} \rd \omega = \frac{1}{2\pi\ri} \int_0^\infty \frac{\re^{-2B\xi'}\delta\sigma(\ri\xi')Q(\ri\xi')}{\xi' + \xi_m} \rd\xi' - \sum_{n\ge 1} \frac{\ri\sigma^\pm_n Q(\ri\xi_n)}{\xi_n + \xi_m} \re^{-2B\xi_n},
\label{eq_sigma_part}
\end{equation}
where $\delta \sigma(\ri\xi)$ denotes the discontinuity of $\sigma(\ri\xi)$. The above equation, which we need to extract $Q(\ri\xi_m)$, involves the quantities $Q(\ri\xi_n)$, thus we will need to recursively solve for these quantities at each exponential order. Another complication is the integral over $Q(\ri\xi')$ in \eqref{eq_sigma_part}, for which we need to determine $Q(\ri\xi)$ at small $\xi$. We propose the following trans-series ansatz:
\begin{equation}
Q(\ri x /2B) = \sum_{n\ge 0} Q_{n} (x) \re^{-2B\xi_n},
\end{equation}
where each $Q_{n}(x)$ is a function of $x$ that we expand in powers of $1/B$. These functions will be 
solutions to integral equations that involve what we called in \cite{mmr-an} the Airy operator:

\begin{equation}
(\mathsf{K}f)(x) = \int_0^\infty \frac{\re^{-y}}{x+y} f(y)\mathrm{d}y.
\end{equation}

To obtain these integral equations, we need to write \eqref{eq_Q_integral_equation} at $\omega=\ri x/2B$:
\begin{equation}
Q(\ri x/2B)= \frac{1}{2 \pi \ri} \int_\mathbb{R} \frac{G_-(\omega) g_+(\omega)}{\omega+ \ri x/2B} \rd \omega + \frac{1}{2 \pi \ri} \int_\mathbb{R} \frac{\re^{2 \ri B\omega} \sigma (\omega) Q(\omega)}{\omega+ \ri x /2B} \rd \omega.
\label{eq_QB_integral_equation}
\end{equation}
Doing a similar computation to \eqref{eq_h_part_2}, we find
\begin{multline}
\ri h \frac{1}{2\pi\ri} \int_\mathbb{R} \frac{G_-(\omega)}{\omega + \ri x/2B} \frac{1-\re^{2\ri B\omega}}{\omega} \rd \omega = -kh(2B)^{1/2} \biggl[ 2B \frac{\mathsf{K}}{\pi}\frac{\re^x - 1}{x^{3/2}}\\
+ \left( 1 - \frac{\mathsf{K}}{\pi} \right) \frac{-a\log(2B) + a \log(x) + b}{x^{1/2}} \biggr]+ \mathcal{O}\big(B^0\big).
\end{multline}
The details of this computation were carried out in Appendix A of \cite{mmr-an}. In principle, in our result, we should also incorporate exponential corrections arising from the poles of $G_-(\omega)$ as we deform the contour upwards for the term $\re^{2\ri B \omega}$. However, these are of order $B^0$ and we can ignore them at the order we are working at.

By carrying out manipulation analogous to \eqref{eq_m_part_2}, we find for the terms proportional to $m$ 
\begin{multline}
\frac{\ri m\re^B}{2} \frac{1}{2\pi\ri} \int_\mathbb{R} \frac{G_-(\omega)}{\omega + \ri x/2B} \left( \frac{\re^{2\ri B\omega}}{\omega-\ri} - \frac{1}{\omega+\ri} \right) \rd \omega = -\frac{m\re^B}{2} \frac{G_+(\ri)}{\sqrt{\pi}}\times\\
\biggl[ -(2B)^{1/2}\frac{k}{G_+(\ri)}\frac{\sqrt{\pi}}{2}\left( 1 + \frac{\mathsf{K}}{\pi} \right)\frac{1}{x^{1/2}}
+ \frac{\sqrt{\pi}}{2} + \frac{\sqrt{\pi}}{G_+(\ri)}\sum_{n\ge 1} \frac{\ri\sigma^\pm_n G_+(\ri\xi_n)}{(\xi_n-1)\xi_n} \re^{-2B\xi_n} \biggr] + \mathcal{O}\big(B^0\big).
\end{multline}

We can now write \eqref{eq_QB_integral_equation} order by order in the exponential corrections $\re^{-2B\xi_n}$, which yields the following integral equations for the functions $Q_{n}(x)$:
\begin{equation}
\left( 1 + \frac{\mathsf{K}}{\pi} \right) Q_{n}(x) = -\frac{m\re^B}{2} \frac{\ri\sigma^\pm_n G_+(\ri\xi_n)}{(\xi_n-1)\xi_n} - \frac{\ri\sigma^\pm_n Q(\ri\xi_n)}{\xi_n} + \mathcal{O}\big(B^0\big), \quad n\ge 1.
\end{equation}
The solutions $Q_{n}(x)$ can be determined with the tools presented in Appendix B of \cite{mmr-an}. The case $n=0$ corresponds to the perturbative part, which is more involved, and is done in detail in Appendix A of the same reference. In particular, the function $Q_{0}(x)$ has to be split in terms proportional to the parameters $a$, $b$ appearing in \eqref{eq_G_series}:
\begin{multline}
Q_{0}(x) = -kh \Bigl[ B q_0(x) + a\log(2B)q_{2,1}^a(x) + a q_{2,0}^a(x) + b q_{2,0}^b(x) \Bigr]\\
 - \frac{m\re^B G_+(\ri)}{\sqrt{\pi}} \Bigl[ (2B)^{1/2} q_1(x) + q_2(x) \Bigr] + \mathcal{O}\bigl(B^0\bigr).
\end{multline}
We then find, for the integral involving $Q(\ri\xi')$ in \eqref{eq_sigma_part},
\begin{multline}
\frac{1}{2\pi\ri} \int_0^\infty \frac{\re^{-2B\xi'}\delta\sigma(\ri\xi')Q(\ri\xi')}{\xi' + \xi_m} \rd\xi' = \frac{kh(2B)^{1/2}}{2\pi\xi_m} \biggl[ \langle q_0 \rangle + \frac{1}{B}\biggl( a\log(2B) \langle q_{2,1}^a - xq_0\rangle\\
+ a\langle q_{2,0}^a+x\log(x)q_0 \rangle + b\langle q_{2,0}^b + xq_0 \rangle - \frac{\langle xq_0\rangle}{2\xi_m} \biggr) \biggr]\\
+ \frac{m\re^B}{\pi\xi_m} \frac{G_+(\ri)}{\sqrt{\pi}} \biggl[ \frac{\langle q_1 \rangle}{(2B)^{1/2}} + \frac{\langle q_2 \rangle}{2B} + \frac{\langle q_3 \rangle}{G_+(\ri)(2B)}\sum_{n\ge 1} \frac{\ri\sigma^\pm_n G_+(\ri\xi_n)}{(\xi_n-1)\xi_n}\re^{-2B\xi_n} \biggr]\\
+ \frac{\langle q_3 \rangle}{\pi^{3/2}B\xi_m}\sum_{n\ge 1} \frac{\ri\sigma^\pm_n Q(\ri\xi_n)}{\xi_n} \re^{-2B\xi_n} + \mathcal{O}\big(B^{-1}\big),
\label{eq_Q_integral_part}
\end{multline}
where we have defined the momenta
\begin{equation}
\langle q \rangle = \int_0^\infty \re^{-x} q(x) \rd x.
\end{equation}
The perturbative part involves different momenta that are worked out in Appendix B of \cite{mmr-an}. We have introduced the momentum of a new function $q_3(x)$, defined as
\begin{equation}
Q_{n}(x) = -\frac{2}{\sqrt{\pi}} \left( \frac{m\re^B}{2} \frac{\ri\sigma^\pm_n G_+(\ri\xi_n)}{(\xi_n-1)\xi_n} + \frac{\ri\sigma^\pm_n Q(\ri\xi_n)}{\xi_n} \right) q_3(x) + \mathcal{O}\bigl(B^0\bigr).
\end{equation}
Its momentum can be easily computed with the same tools as the perturbative part, and it is given by $\langle q_3 \rangle = \pi^{3/2}/8$.

We now have to put all pieces together [\eqref{eq_h_part_2}, \eqref{eq_m_part_2}, \eqref{eq_sigma_part}, \eqref{eq_Q_integral_part}] in \eqref{eq_Qm_integral_equation}. After evaluating the momenta and the integrals $I_0$, $I_1$, we obtain
\begin{multline}
Q(\ri\xi_m) = \frac{kh(2B)^{1/2}\sqrt{\pi}}{\xi_m} \biggl[ -\frac{1}{2} + \frac{-4 a (\log(2B)+\gamma -1+\log (4))+4 b-3/\xi_m}{16 B}  \biggr]\\
+s h\biggl[ \frac{G_+(\ri\xi_m)}{\xi_m} + \sum_{n\ge 1} \frac{\ri \sigma^\pm_n G_+(\ri\xi_n)}{(\xi_n+\xi_m)\xi_n} \re^{-2B\xi_n} \biggr]
-\frac{m\re^B}{2}\biggl[ \frac{G_+(\ri\xi_m)-G_+(\ri)}{\xi_m-1}\\
+ \sum_{n\ge 1} \frac{\ri \sigma^\pm_n G_+(\ri\xi_n)}{(\xi_n+\xi_m)(\xi_n-1)} \re^{-2B\xi_n}
- \frac{1}{8B\xi_m}\biggl( G_+(\ri) + \sum_{n\ge 1}\frac{\ri\sigma^\pm_n G_+(\ri\xi_n)}{(\xi_n-1)\xi_n} \re^{-2B\xi_n} \biggr) \biggr]\\
- \sum_{n\ge 1} \frac{\ri\sigma^\pm_n Q(\ri\xi_n)}{\xi_n+\xi_m} \re^{-2B\xi_n} + \frac{1}{8 B \xi_m} \sum_{n\ge 1} \frac{\ri \sigma^\pm_n Q(\ri\xi_n)}{\xi_n} \re^{-2B\xi_n} + \mathcal{O}\big( B^{-1} \big).
\label{eq_Qm_implicit}
\end{multline}
We introduced the parameter $s=1$ for convenience, in order to keep track of some of the terms in the above expression. In both the boundary condition and the final result for the free energy, all contributions of terms proportional to $s$ cancel each other, thus we can set $s=0$ to simplify the computation.

On the other hand, we also need to compute $\epsilon_+(\ri\kappa)/G_+(\ri\kappa)$ from \eqref{eq_epsilon_0}. The steps are mostly the same as we did for $Q(\ri\xi_m)$, but replacing $\xi_m$ by $-\kappa$. In \eqref{eq_h_part_2} and \eqref{eq_m_part_2}, contributions that arose from the pole at $-\ri\xi_m$ will be different, since the pole will now be in the positive imaginary side, at $\ri\kappa$. The final result is then given by
\begin{multline}
\frac{\epsilon_+(\ri\kappa)}{G_+(\ri\kappa)} = -\frac{kh(2B)^{1/2}\sqrt{\pi}}{\kappa} \biggl[ -\frac{1}{2} + \frac{-4 a (\log(2B)+\gamma -1+\log (4))+4 b+3/\kappa}{16 B}  \biggr]\\
+s h\biggl[ - \delta_{\kappa,1} G_-(\ri)\re^{-2B} + \sum_{n\ge 1} \frac{\ri \sigma^\pm_n G_+(\ri\xi_n)}{(\xi_n-\kappa)\xi_n} \re^{-2B\xi_n} \biggr]
-\frac{m\re^B}{2}\biggl[\frac{G_+(\ri)}{\kappa+1} - \delta_{\kappa,1} G_-'(\ri)\re^{-2B}\\
+ \sum_{n\ge 1} \frac{\ri \sigma^\pm_n G_+(\ri\xi_n)}{(\xi_n-\kappa)(\xi_n-1)} \re^{-2B\xi_n}
+ \frac{1}{8B\kappa}\biggl( G_+(\ri) + \sum_{n\ge 1}\frac{\ri\sigma^\pm_n G_+(\ri\xi_n)}{(\xi_n-1)\xi_n} \re^{-2B\xi_n} \biggr) \biggr]\\
- \sum_{n\ge 1} \frac{\ri\sigma^\pm_n Q(\ri\xi_n)}{\xi_n-\kappa} \re^{-2B\xi_n} - \frac{1}{8 B \kappa} \sum_{n\ge 1} \frac{\ri \sigma^\pm_n Q(\ri\xi_n)}{\xi_n}\re^{-2B\xi_n} + \mathcal{O}\big( B^{-1} \big).
\label{eq_epsilon_kappa}
\end{multline}
For convenience, we only wrote the terms arising from the pole at $\ri\kappa$ for the particular cases $\kappa=1, +\infty$. In the latter case, these contributions vanish, as indicated by the Kronecker delta.

We are now in position to compute the relation between $m$ and $h$, resulting from the boundary condition \eqref{eq_boundary_condition}. To this end, we propose the ansatz
\begin{equation}
\begin{aligned}
m\re^B &= kh (2B)^{1/2} \frac{\sqrt{\pi}}{G_+(\ri)} \sum_{n\ge 0} b_n (B) \re^{-2B\xi_n},\\
b_{n}(B) &= b_{(n),0} + s\frac{b_{(n),1}}{\sqrt{B}} + \frac{b_{(n),2,1} \log(2B)}{B} + \frac{b_{(n),2,0}}{B} + \mathcal{O}\big(B^{-2}\big).
\end{aligned}
\label{eq_boundary_condition_ansatz}
\end{equation}
We will see later that the $1/\sqrt{B}$ correction will be 0 to all exponential orders, so one can effectively set $s=0$ in the expression for $b_n(B)$. To find the parameters in the ansatz of $b_n(B)$, we first have to plug \eqref{eq_boundary_condition_ansatz} in \eqref{eq_Qm_implicit} and solve the resulting equation for the quantities $Q(\ri\xi_m)$, order by order in the exponential corrections. We finally evaluate \eqref{eq_epsilon_kappa} at $\kappa\rightarrow +\infty$, using our result for $Q(\ri\xi_m)$, and  impose the boundary condition \eqref{eq_boundary_condition} to solve for the parameters $b_{(n),0}$, $b_{(n),2,1}$, $b_{(n),2,0}$. As an example, for $n=1$, we obtain
\begin{equation}
b_1(B) = \frac{\ri \sigma^\pm_1}{(\xi_1 -1)\xi_1} + \frac{\ri \sigma^\pm_1 a \log(2B)}{2(\xi_1 - 1)\xi_1 B} +
\frac{\ri \sigma^\pm_1 (4 a (\gamma_E -1+\log (4))\xi_1 -4 b \xi_1-5 \xi_1+2)}{8 (\xi_1-1) \xi_1^2 B}.
\end{equation}

The free energy can be obtained by evaluating \eqref{eq_epsilon_kappa} at $\kappa=1$ and putting the result in \eqref{eq_free_energy_fourier}. In addition, we write instances of $m$ in terms of $h$, by using \eqref{eq_boundary_condition_ansatz} with the parameters obtained when we imposed the boundary condition. The final result for the free energy can be written as
\begin{equation}
\mathcal{F}(h) = - \frac{m^2}{4\pi}\ri G_-'(\ri)G_+(\ri) - \frac{k^2 h^2 B}{4} \sum_{n\ge 0} f_n(B) \re^{-2B\xi_n},
\label{eq_free_energy_transseries_B}
\end{equation}
where the coefficients $f_n(B)$ are series in $1/B$ and $\log(2B)$. In particular, for the first exponential correction, we find
\begin{multline}
f_1(B) = -\frac{2\ri \sigma^\pm_1}{(\xi_1-1)^2 \xi_1} - \frac{2\ri\sigma^\pm_1 a \log(2B)}{(\xi_1-1)^2 \xi_1 B}\\
-\frac{\ri \sigma^\pm_1 \left(4 a (\gamma_E -1+\log (4))\xi_1 -4 b \xi_1+2 \xi_1^2-4 \xi_1+1\right)}{2 (\xi_1-1)^2 \xi_1^2 B}.
\end{multline}

In the next step, we will write the trans-series in \eqref{eq_free_energy_transseries_B} as a trans-series in the $\tilde\alpha$ coupling of \eqref{eq_alpha_tilde_def}. A relation between $\tilde{\alpha}$ and the paramter $B$ can be extracted from the boundary condition derived in \eqref{eq_boundary_condition_ansatz}. We propose the following trans-series ansatz
\begin{equation}
\begin{aligned}
B &= \frac{1}{\tilde{\alpha}} + \sum_{n\ge 0} d_n(\tilde{\alpha}) \tilde{\alpha}^{-2a\xi_n} \re^{-2\xi_n/\tilde{\alpha}},\\
d_n(\tilde{\alpha}) &= d_{(n),0} + d_{(n),2,1} \tilde{\alpha} \log\tilde{\alpha} + d_{(n),1}\tilde{\alpha} + \mathcal{O}\big(\tilde{\alpha}^2\big).
\end{aligned}
\label{eq_B_to_alpha_tilde}
\end{equation}
The coefficients can then be obtained by combining \eqref{eq_alpha_tilde_def} with \eqref{eq_boundary_condition_ansatz}:
\begin{equation}
\frac{1}{\tilde{\alpha}} + \left( a + \frac{1}{2} \right)\log\tilde{\alpha} = B - \frac{1}{2}\log(B) + \frac{1}{2}\log\left( \frac{G_+(\ri)^2}{2\pi k^2} \frac{m^2}{\Lambda^2} \right) - \log\Biggl( \sum_{n\ge 0} b_n(B) \re^{-2B\xi_n} \Biggr).
\label{eq_alpha_def_mod}
\end{equation}
Replacing $B$ with the expression \eqref{eq_B_to_alpha_tilde}, one obtains an equation for $d_k(\tilde{\alpha})$ that can be recursively solved for:
\begin{multline}
d_k(\tilde{\alpha}) = \coeff_k \Biggl\{ \frac{1}{2} \log\Biggl[ 1 + \tilde{\alpha} \sum_{i=0}^{k-1} d_i(\tilde{\alpha}) \tilde{\alpha}^{-2a\xi_i} \re^{-2\xi_i/\tilde{\alpha}}\Biggr] \\
+ \log\Biggl[ \sum_{i=0}^{k-1} \left( \frac{G_+(\ri)^2}{2\pi k^2} \frac{m^2}{\Lambda^2} \right)^{\xi_i} b_i(\tilde{\alpha})\exp\Biggl( -2\xi_i \sum_{j=0}^{k-1} b_j(\tilde{\alpha}) \tilde{\alpha}^{-2a\xi_j} \re^{-2\xi_j/\tilde{\alpha}} \Biggr)   \Biggr] \Biggr\},
\end{multline}
where $\coeff_k(f)$ denotes the $k$-th coefficient of $f$ as an expansion in powers of $y=\tilde{\alpha}^{-2a\xi_1} \re^{-2\xi_1/\tilde{\alpha}}$, and $b_j(\tilde{\alpha})$ are the coefficients $b_j(B)$ evaluated at $B=1/\tilde{\alpha}$.\footnote{This replacement is only valid at the order we are working.} The initial condition can also be extracted from \eqref{eq_alpha_def_mod}, with the result
\begin{multline}
d_0(\tilde{\alpha}) =  a \log \tilde{\alpha} - \frac{1}{2}\log\left( \frac{G_+(\ri)^2}{2\pi k^2} \frac{m^2}{\Lambda^2} \right)\\
+ \frac{4 a (\gamma_E -1+\log (8))-4 b-2 \log\left( \frac{G_+(\ri)^2}{2\pi k^2} \frac{m^2}{\Lambda^2} \right)-1}{8} \tilde{\alpha} + \mathcal{O}\big(\tilde{\alpha}^2\big).
\end{multline}

We can now write the free energy $\mathcal{F}(h)$ that we determined in \eqref{eq_free_energy_transseries_B} as a trans-series in $\tilde{\alpha}$, which yields the result of \eqref{eq_free_energy_transseries}. All contributions of $\log \tilde\alpha$ cancel in this step and the $\varphi_\ell(\tilde{\alpha})$ are simply power series in $\tilde{\alpha}$.

The coefficient $\mathcal{C}_\text{IR}^\pm$ in \eqref{eq_free_energy_transseries} can be extracted by rewriting the $m^2$ term of \eqref{eq_free_energy_transseries_B} in terms of $h^2$, directly using the coupling definition \eqref{eq_alpha_tilde_def}. One obtains
\begin{equation}
\mathcal{C}_\text{IR}^\pm = \frac{\ri G_-'(\ri) G_+(\ri)}{\pi k^2} \frac{m^2}{\Lambda^2}.
\end{equation}
The ambiguity in this coefficient arises from the factor $G_-'(\ri)$.

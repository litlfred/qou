---
doc_id: arxiv-2302.08363v2
doc_title: "On the structure of trans-series in quantum field theory"
section_id: sec-008-numerical-analysis
section_title: "Numerical analysis"
section_number: null
pages: 20-24
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.988
doc_brief: "On the structure of trans-series in quantum field theory — Many observables in quantum field theory can be expressed in terms of trans-series, in which one adds to the perturbative series a typically"
---
Using the method discussed in the previous section, we can now generate the first two coefficients of the series
\begin{equation}
\varphi_\ell(\tilde\alpha) = a_{0,\ell} + a_{1,\ell} \tilde\alpha + \mathcal{O}\big(\tilde\alpha^2\big)
\end{equation}
appearing in the trans-series \eqref{eq_free_energy_transseries}, up to very large order in $\ell$. To the very first values of $\ell$, we find the following analytic results, valid for generic bosonic models:
\begin{multline}
\varphi_1(\tilde{\alpha}) = \left( \frac{G_+(\ri)^2}{2\pi k^2} \frac{m^2}{\Lambda^2} \right)^{\xi_1} \biggl[ -\frac{2 \ri \sigma_1^\pm}{(\xi_1-1)^2 \xi_1}\\
+\frac{\ri \sigma_1^\pm (4 a (\gamma_E -1+\log (8))\xi_1 -2\xi_1 ( 4 b +\log\left( \frac{G_+(\ri)^2}{2\pi k^2} \frac{m^2}{\Lambda^2} \right)) -\xi_1 +1)}{2 (\xi_1-1) \xi_1^2} \tilde{\alpha} + \mathcal{O}\big(\tilde{\alpha}^2\big) \biggr].
\label{eq_coeff_bosonic_1}
\end{multline}
\begin{multline}
\varphi_2(\tilde\alpha) = \left( \frac{G_+(\ri)^2}{2\pi k^2} \frac{m^2}{\Lambda^2} \right)^{2\xi_1} \biggl[ \frac{2 (\ri\sigma_1^\pm)^2}{(\xi_1-1)^2 \xi_1^2}-\frac{\ri \sigma_2^\pm}{(2 \xi_1-1)^2 \xi_1}\\
+ \biggl(- \frac{(\ri\sigma_1^\pm)^2 (2 \xi_1 (2 a (2 \xi_1-1) (\gamma_E -1+\log (8)) - (2\xi_1-1)(4 b+\log\left( \frac{G_+(\ri)^2}{2\pi k^2} \frac{m^2}{\Lambda^2} \right) ) - \xi_1 + 1)-1)}{2(\xi_1-1)^2\xi_1^3}\\
+ \frac{\ri \sigma_2^\pm (2 \xi_1 (4 a (\gamma_E -1+\log (8))-8 b-2 \log\left( \frac{G_+(\ri)^2}{2\pi k^2} \frac{m^2}{\Lambda^2} \right)-1)+1)}{8 (2\xi_1-1)\xi_1^2}\biggr) \tilde\alpha   + \mathcal{O}\big(\tilde\alpha ^2\big) \biggl].
\label{eq_coeff_bosonic_2}
\end{multline}
\begin{multline}
\varphi_3(\tilde\alpha) = \left( \frac{G_+(\ri)^2}{2\pi k^2} \frac{m^2}{\Lambda^2} \right)^{3\xi_1} \biggl[ -\frac{(7 \xi_1-3) (\ri\sigma_1^\pm)^3}{2(\xi_1-1)^3\xi_1^3} + \frac{2 (\ri\sigma_1^\pm) (\ri\sigma_1^\pm)}{(\xi_1-1)(2\xi_1-1)\xi_1^2} - \frac{2 \ri \sigma_3^\pm}{3(3 \xi_1-1)^2\xi_1}\\
+ \biggl( -\frac{ (\ri\sigma_1^\pm)^3 (4b + \log\left( \frac{G_+(\ri)^2}{2\pi k^2} \frac{m^2}{\Lambda^2} \right) ) (3 \xi_1-1) (7 \xi_1-3)}{4(\xi_1-1)^3 \xi_1^3}\\
+\frac{ (\ri\sigma_1^\pm)^3 \left(\xi_1 \left(12 a (3 \xi_1-1) (7 \xi_1-3) (\gamma_E -1+\log (8))-63 \xi_1^2+69 \xi_1-49\right)+3\right)}{24 (\xi_1-1)^3 \xi_1^4}\\
-\frac{(\ri\sigma_1^\pm) (\ri\sigma_2^\pm) (4 b + \log\left( \frac{G_+(\ri)^2}{2\pi k^2} \frac{m^2}{\Lambda^2} \right) ) (1-3 \xi_1)}{(\xi_1-1)(2 \xi_1-1) \xi_1^2 }\\
- \frac{(\ri\sigma_1^\pm) (\ri\sigma_2^\pm) \left(18 \xi_1^2 (4 a (\gamma_E -1+\log (8))-1)+12 \xi_1 (1-2 a (\gamma_E -1+\log (8)))-5\right)}{12 (\xi_1-1) (2 \xi_1-1) \xi_1^3}\\
+ \frac{\ri \sigma_3^\pm (3 \xi_1 (4 a (\gamma_E -1+\log (8))-8 b - 2 \log\left( \frac{G_+(\ri)^2}{2\pi k^2} \frac{m^2}{\Lambda^2} \right) -1)+1)}{18 \xi_1^2 (3 \xi_1-1)} \biggr) \alpha + \mathcal{O}\big(\alpha^2\big)
\biggr].
\label{eq_coeff_bosonic_3}
\end{multline}


To extract the large order behavior of the coefficients $a_{n,\ell}$, at large $\ell$, we will do a numerical compiutation, focusing on the $O(N)$ non-linear sigma model and the $SU(N)$ PCF. In the following, we summarize all the relevant parameters that we need for each of the two models.

(i) \textit{Non-linear $O(N)$ sigma model.} With the choice of charges $\mathsf{Q}$ made in \cite{hmn,hn}, the function $G_+(\omega)$ that one obtains from the Wiener--Hopf decomposition of the kernel is given by
\begin{equation}
G_+(\omega) = \frac{\re^{-{1 \over 2} \ri \omega [(1-2\Delta)(\log(-\frac{1}{2}\ri \omega)-1)-2\Delta\log(2\Delta)]}}{\sqrt{-\ri \Delta \omega}}\frac{\Gamma(1-\ri \Delta \omega)}{\Gamma\big(\tfrac{1}{2}-\tfrac{1}{2}\ri\omega\big)}, \qquad \Delta = \frac{1}{N-2}.
\end{equation}
The parameters of the expansion \eqref{eq_G_series} can be easily extracted from the above expression, obtaining
\begin{equation}
k = \frac{1}{\sqrt{\pi\Delta}}, \qquad a = -\frac{1}{2} (1-2 \Delta), \qquad b=\frac{(\gamma_E -1) (2 \Delta -1)+2 \Delta  \log (\Delta )-\log (2)}{2}.
\end{equation}
The singularities and residues of $\sigma(\omega)$, defined in \eqref{eq_sigma_def}, are\footnote{When $N$ is odd, there are singularities only for even $\ell$ in \eqref{eq_ON_singularities}. We can still treat all values of $N$ with the same formulas, with the observation that $\ri\sigma_\ell^\pm = 0$ when there is no actual singularity.}
\begin{equation}
\xi_\ell = \frac{\ell}{\Delta}, \qquad \ri\sigma_\ell^\pm = \pm \ri \frac{ \left( \frac{\ell}{\re}\right)^{2 \ell} \left(\frac{\ell}{2\ri\re\Delta }\right)^{-\frac{\ell}{\Delta }} }{\Delta  (\ell-1)!\, \ell! } \frac{\Gamma \left(\frac{1}{2} + \frac{\ell}{2 \Delta }\right)}{\Gamma \left(\frac{1}{2} - \frac{\ell}{2 \Delta }\right)}.
\label{eq_ON_singularities}
\end{equation}
The relation between the mass gap and the dynamically generated scale in the $\overline{\text{MS}}$ scheme is given by \cite{hmn,hn}
\begin{equation}
\frac{m}{\Lambda} = \left(\frac{8}{\re}\right)^{\Delta } \frac{1}{\Gamma (\Delta +1)}.
\end{equation}

(ii) \textit{Principal chiral field}. With the charges chosen in \cite{pcf}, we have
\begin{equation}
G_+(\omega)=\frac{\re^{- \ri \omega  [-(1-\Delta) \log (1-\Delta)-\Delta  \log (\Delta )]}}{\sqrt{-2 \pi\ri (1-\Delta ) \Delta \omega } }\frac{\Gamma (1-\ri (1-\Delta ) \omega ) \Gamma (1-\ri \Delta  \omega ) }{\Gamma (1-\ri \omega )}, \qquad \Delta = \frac{1}{N}.
\end{equation}
The parameters of the expansion \eqref{eq_G_series} are
\begin{equation}
k = \frac{1}{\sqrt{2\pi (1-\Delta)\Delta}}, \qquad a = 0, \qquad b = (1-\Delta ) \log (1-\Delta )+\Delta  \log (\Delta ).
\end{equation}
The singularities and residues of $\sigma(\omega)$ are
\begin{equation}
\xi_\ell = \frac{\ell}{1-\Delta}, \qquad \ri\sigma_\ell^\pm = \pm\ri \frac{(-1)^{\ell+1} (1-\Delta )^{2 \ell} \Delta ^{\frac{2 \Delta  \ell}{1-\Delta}} }{\ell!^2} \frac{\Gamma \bigl(1+\frac{\ell}{1-\Delta }\bigr) \Gamma \bigl(1+\frac{\ell \Delta }{\Delta -1}\bigr)}{\Gamma \bigl(-\frac{\ell}{1-\Delta}\bigr) \Gamma \bigl(1+\frac{\ell \Delta }{1-\Delta }\bigr)}.
\end{equation}
The mass gap is given by \cite{pcf}
\begin{equation}
\frac{m}{\Lambda} = \sqrt{\frac{8 \pi }{\re}} \frac{\sin (\pi  \Delta )}{\pi  \Delta }.
\end{equation}

We will check, up to numerical error, and for each of the two models discussed above, that the coefficients $a_{n,\ell}$ appearing in the trans-series have the asymptotics \eqref{an-bn-R}. To this end, we construct the quantity

\begin{equation}
\left| \frac{a_{n,\ell}}{a_{n,\ell+1}} \right| = R \left( 1 + \frac{b_n}{\ell} + \mathcal{O}(1/\ell^2) \right).
\label{eq_anl_quotient}
\end{equation}

The coefficients $a_{n,\ell}$ are ambiguous, due to the two choices in the residues $\ri\sigma_\ell^\pm$. These two choices differ by complex conjugation: $\left( \ri\sigma_\ell^+ \right)^ *=\ri \sigma_\ell^-$. On the other hand, as seen explicitly in the expressions of \eqref{eq_coeff_bosonic_1}, \eqref{eq_coeff_bosonic_2}, \eqref{eq_coeff_bosonic_3}, the $a_{n,\ell}$s are multinomials of $\ri\sigma_\ell^\pm$, with real coefficients. Therefore, 
the two choices gives the same coefficients $a_{n, \ell}$, up to complex conjugation. This implies that $|a_{n,\ell}|$ is not ambiguous and, thus, neither are the parameters $R$ and $b_n$ appearing in \eqref{eq_anl_quotient}.

Using Richardson transforms, one can accelerate the convergence of the sequence when $\ell$ is large, extracting the radius of convergence $R$. In Fig. \ref{fig_radius_ON}, we show the result for the $O(8)$ non-linear sigma model and $n=0$.

\begin{figure}
\centering
\includegraphics[width=0.6\textwidth]{plot_radius_O8.pdf}
\caption{Sequence $| a_{0,\ell}/a_{0,\ell+1} |$ for the free energy of the $O(8)$ non-linear sigma model (black), together with the 1st (red) and 2nd (orange) Richardson transforms. The dashed line is the value $R$ to which the sequences converge.}
\label{fig_radius_ON}
\end{figure}
Further, we can extract the value of $b_n$ by considering the sequence

\begin{equation}
\label{bn-seq}
\ell \log\left( \frac{| a_{n,\ell} |}{R | a_{n,\ell+1} |}\right) = b_n + \mathcal{O}(1/\ell).
\end{equation}

In figure \ref{fig_b_ON}, we show the result for the $O(8)$ non-linear sigma model and $n=0$.

In table \ref{tab_ON}, we display the value of the parameters $R$ and $b_n$ that we 
obtained for the $O(N)$ non-linear sigma model, at different values of $N$ and for the leading 
$n=0$ and subleading $n=1$ coefficients in the trans-series. In table \ref{tab_PCF}, we show the same 
results for the $SU(N)$ PCF model. We find numerical evidence that the radius of convergence 
$R$ does not depend on $n$. On the other hand, the numeric results seem to indicate that $b_1 = b_0 - 1$. We also note 
that, for the $O(N)$ sigma model, when $N$ is even, the result for $b_0$ is compatible with the exact result $b_0=5/2$, which is also the value found in the 
Gross--Neveu model. Our numerical analysis uses 600 coefficients $a_{n,\ell}$, for both $n=0$ and $n=1$. The 
numerical errors of $R$ are estimated from the difference between two successive 
Richardson transforms, and we perform a number of Richardson transforms so that the 
error estimate is minimized. In the case of $b_n$, the error estimate is the error propagating from 
$R$ plus the error estimated from two successive Richardson transforms, with both errors added in quadrature.
\begin{figure}
\centering
\includegraphics[width=0.6\textwidth]{plot_b_O8.pdf}
\caption{Sequence $\ell \log\left( \frac{| a_{0,\ell} |}{R | a_{0,\ell+1} |}\right)$ for the free energy of the $O(8)$ non-linear sigma model (black), together with the 1st Richardson transform (red). The dashed line is the value $b_0$ to which the sequences converge.}
\label{fig_b_ON}
\end{figure}
\begin{table}
\begin{equation*}
\arraycolsep=3mm
\begin{array}{lllll}
\toprule
N & R \text{ leading} & R \text{ subleading} & b_0  & b_1 \\
\midrule
4 & 0.25294249(91\pm 15) & 0.25294250(04\pm 26) & 2.5(00\pm 12) & 1.5(00\pm 15) \\
5 & 2.10247819(7\pm 7) & 2.10247819(7\pm 6) & 2.8(28\pm 12) & 1.8(28\pm 10) \\
6 & 9.30450(59\pm 13) & 9.30450(60\pm 13) & 2.(46\pm 11) & 1.(46\pm 11)\\
7 & 89.848306(72\pm 19) & 89.848306(72\pm 18) & 2.8(29\pm 11) & 1.82(9\pm 9) \\
8 & 505.12143(7\pm 9) & 505.12143(8\pm 8) & 2.4(7\pm 9) & 1.4(7\pm 9)\\
9 & 5427.95182(8\pm 5) & 5427.95182(8\pm 5) & 2.8(30\pm 10) & 1.83(0\pm 9) \\
10 & 34063.91(7\pm 4) & 34063.91(7\pm 4) & 2.(48\pm 11) & 1.(48\pm 11) \\
11 & 388517.904(71\pm 13) & 388517.904(71\pm 12) & 2.8(30\pm 10) & 1.83(0\pm 8) \\
\bottomrule
\end{array}
\end{equation*}
\caption{Parameters $R$ and $b_n$ of the asymptotics \eqref{an-bn-R}, for the free energy of the $O(N)$ non-linear sigma model at different values of $N$. We extract the parameters from the leading $n=0$ and subleading $n=1$ corrections in $\tilde\alpha$. For the radius $R$, we find numerical evidence that this parameter does not depend on $n$.}
\label{tab_ON}
\end{table}
\begin{table}
\begin{equation*}
\arraycolsep=3mm
\begin{array}{lllll}
\toprule
N & R \text{ leading} & R \text{ subleading} & b_0  & b_1 \\
\midrule
2 & 0.25294249(91\pm 15) & 0.25294250(04\pm 26) & 2.4(96\pm 18) & 1.50(0\pm 8) \\
3 & 0.17492(41\pm 29) & 0.17492(73\pm 10) & 2.5(80\pm 29) & 1.4(99\pm 32) \\
4 & 0.16537769(3\pm 6) & 0.16537769(4\pm 6) & 2.8(57\pm 30) & 1.8(57\pm 15)\\
5 & 0.1489842(2\pm 7) & 0.1489842(2\pm 8) & 2.8(80\pm 32) & 1.8(80\pm 33) \\
6 & 0.149513(8\pm 8) & 0.149513(6\pm 9) & 2.8(84\pm 35) & 1.8(83\pm 21)\\
7 & 0.15488(63\pm 30) & 0.15488(64\pm 31) & 2.8(4\pm 4) & 1.8(33\pm 22) \\
8 & 0.15(78\pm 23) & 0.15(81\pm 18) & 6\pm 11 & 4\pm 8 \\
9 & 0.15671(89\pm 14) & 0.15671(44\pm 11) & 2.9(1\pm 5) & 1.92(9\pm 6) \\
\bottomrule
\end{array}
\end{equation*}
\caption{Parameters $R$ and $b_n$ of the asymptotics \eqref{an-bn-R}, for the free energy of the $SU(N)$ PCF model at different values of $N$.}
\label{tab_PCF}
\end{table}

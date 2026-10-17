---
doc_id: arxiv-1409.0435v2
doc_title: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap"
section_id: sec-004-2-differential-identities-for-toeplitz-determina
section_title: "Differential identities for Toeplitz determinants"
section_number: 2
pages: 6-10
source_pdf: 1409.0435v2.pdf
source_sha256: 0c6abbb9c5a720d9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.979
---
\label{section: diff id}

In this section, we derive an identity for $\frac{d}{ds}\ln D_n(s,\theta_0,W)$ in terms of orthogonal polynomials on the unit circle.
Define $\phi_{j}, \widehat{\phi_j}$, $j=0,1,2,\ldots$ as the family of orthogonal polynomials on the unit circle characterized by
\begin{equation} \label{Orthogonality_condition}
\frac{1}{2\pi} \int_{0}^{2\pi} \phi_{k}(e^{i\theta}) \widehat{\phi_{m}}(e^{-i\theta})f(e^{i\theta})d\theta = \delta_{km}, \hspace{1cm} \forall k,m \in \mathbb{N},
\end{equation}
where the degree of $\phi_{j}, \widehat{\phi_j}$ is $j$, and their leading coefficients $\chi_j$ are equal and positive. 


For general weight functions $f(e^{i\theta})$, it is a standard fact that $\phi_n,\widehat\phi_n$ exist and are unique if $D_n(f), D_{n+1}(f)\neq 0$ and that they are given by the determinantal formulas \cite{Simon}
\begin{equation} \label{explicit OP}
\phi_{n}(z) = \frac{1}{\sqrt{D_{n}D_{n+1}}} \left| \begin{array}{c c c c c}
f_0 & f_{-1} & f_{-2} & \cdots & f_{-n} \\
f_{1} & f_{0} & f_{-1} & \cdots & f_{-n+1} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
f_{n-1} & f_{n-2} & f_{n-3} & \cdots & f_{-1} \\
1 & z & z^2 & \cdots & z^n
\end{array} \right|,
\end{equation}
and
\begin{equation} \label{explicit OP2}
\widehat\phi_{n}(z) = \frac{1}{\sqrt{D_{n}D_{n+1}}} \left| \begin{array}{c c c c c c}
f_0 & f_{-1} & f_{-2} & \cdots & f_{-n+1} &1\\
f_{1} & f_{0} & f_{-1} & \cdots & f_{-n+2}& z\\
\vdots & \vdots & \vdots & \ddots & \vdots& \vdots\\
f_{n} & f_{n-1} & f_{n-2} & \cdots & f_{1}& z^{n}
\end{array} \right|,
\end{equation}
where $D_n=D_n(f)$ is the Toeplitz determinant defined in (\ref{Toeplitz}), and where $f_k$ is, as before, the $k$-th Fourier coefficient of $f$.
If $f(e^{i\theta})$ is  positive, $D_n(f)>0$ for all $n\in\mathbb N$ and the OPs are well-defined. 
For complex $f$, existence and uniqueness of the orthogonal polynomials is not guaranteed for any $n$.
For $f$ given in (\ref{symbol}), it will follow from our analysis that they are well-defined for $n$ sufficiently large and $0\leq s\leq e^{-x_cn}$.
If $W=0$, the symbol $f$ is even in $\theta$ and positive, which implies that $\widehat\phi_k=\phi_{k} = \overline{\phi_{k}}$.





From (\ref{explicit OP}), we see that the leading coefficient $\chi_n$ of $\phi_n$ is equal to
\begin{equation*}
\chi_n = \chi_n(s,\theta_0,W) = \sqrt{\frac{D_{n}(s,\theta_0,W)}{D_{n+1}(s,\theta_0,W)}}.
\end{equation*}
We can thus express $D_n(s,\theta_0,W)$ in terms of the leading coefficients of the OPs if $D_0, D_1, \ldots, D_n\neq 0$:
\begin{equation}\label{Toeplit_express_by_chi_n}
D_{n}(s,\theta_0,W) = \prod_{j=0}^{n-1} \chi_{j}^{-2}.
\end{equation}

To obtain an asymptotic formula for $D_{n}(s,\theta_0,W)$ from this formula, we would need information about all OPs of degree $0$ up to $n-1$. To circumvent this problem, we derive differential identities for $\ln D_{n}(s,\theta_0,W)$.


\subsection{Differential identity for general $W$}

For general sufficiently smooth symbols $f(z;s)$ depending on a parameter $s$, there exists an identity for the logarithmic derivative of $D_n(f)$ with respect to $s$: if $D_{n-1}, D_n, D_{n+1}\neq 0$, we have \cite[Proposition 3.3]{DeiftItsKrasovsky}
\begin{equation*}
\partial_{s} \ln D_{n} (s,\theta_{0},W) = \frac{1}{2\pi i} \int_{S_{1}} z^{-n} \left[ Y^{-1}(z) Y^{\prime}(z) \right]_{21} \partial_s f(z,s) dz,
\end{equation*}
where $S_1$ is the unit circle in the complex plane, $\mbox{ }^{\prime} = \frac{d}{dz}$, $ \partial_s = \frac{d}{ds}$, and
\begin{equation}\label{sol_Y}
Y(z) = \begin{pmatrix} \chi_{n}^{-1} \phi_{n}(z) & \displaystyle \chi_{n}^{-1} \int_{S_{1}} \frac{\phi_{n}(w)}{w-z} \frac{f(w)}{2\pi i w^{n}} dw \\
\displaystyle -\chi_{n-1} z^{n-1} \widehat{\phi}_{n-1}(z^{-1}) & \displaystyle -\chi_{n-1} \int_{S_{1}} \frac{\widehat{\phi}_{n-1}(w^{-1})}{w-z} \frac{f(w)}{2\pi i w} dw
\end{pmatrix}.
\end{equation}
For our symbol given by (\ref{symbol}), this formula reduces to
\begin{equation}\label{diffid1general}
\partial_{s} \ln D_{n} (s,\theta_{0},W) = \frac{1}{2\pi i} \int_{\gamma^{c}} z^{-n} \left[ Y^{-1}(z)Y^{\prime}(z) \right]_{21} e^{W(z)}dz,
\end{equation}
where $\gamma^{c} = S_{1}\setminus \gamma$.


\subsection{Differential identity for $W = 0$}

If $W=0$, the integral at the right hand side of (\ref{diffid1general}) can be simplified. Although (\ref{diffid1general}) will be sufficient for the proof of Theorem \ref{theorem: extensionWidom}, we will show here how to simplify the differential identity if $W=0$. This will allow us to give a more elegant proof of Theorem \ref{theorem: extensionWidom} in this case.


\begin{proposition}
\label{proposition: diff id}
Let $D_n(s,\theta_0,0)$ be the Toeplitz determinant with symbol (\ref{symbol}) in the case where $W(e^{i\theta})= 0$.
We have the following differential identity for $\ln D_{n}$:
\begin{equation}\label{Differential_identity_for_D_n}
\partial_{s} \ln D_n(s,\theta_{0},0) = -2n \frac{\partial_{s} \chi_n}{\chi_n} + \frac{2(1-s)}{\pi} \mbox{\rm Im}\left( \overline{\phi_{n}(e^{i\theta_{0}})} \partial_{s}\phi_{n}(e^{i\theta_{0}}) \right).
\end{equation}
\end{proposition}
\begin{proof}
Taking the logarithm of both sides in (\ref{Toeplit_express_by_chi_n}), and then differentiating with respect to $s$, we get
\begin{equation*}
\partial_{s} \ln D_n(s,\theta_{0},0) = -2 \sum_{j=0}^{n-1} \frac{\partial_{s}\chi_{j}}{\chi_{j}}.
\end{equation*}
On the other hand, by \eqref{Orthogonality_condition},
\begin{equation*}
\frac{1}{2\pi} \int_{0}^{2\pi} \partial_{s} \left( \phi_{j}(e^{i\theta}) \overline{\phi_{j}(e^{i\theta})} \right) f(e^{i\theta})d\theta = 2\frac{\partial_{s}\chi_{j}}{\chi_{j}},
\end{equation*}
and this gives
\begin{equation}\label{diffid1}
\partial_{s} \ln D_n(s,\theta_{0},0) = - \frac{1}{2\pi} \int_{0}^{2\pi} \partial_{s} \left[ \sum_{j=0}^{n-1} \phi_{j}(e^{i\theta}) \overline{\phi_{j}(e^{i\theta})} \right] f(e^{i\theta})d\theta.
\end{equation}
Here we can use the Christoffel-Darboux formula (see e.g.\ \cite{Simon, Deift2} for a proof of it):
\begin{equation*}
\sum_{j=0}^{n-1} \phi_{j}(z) \overline{\phi_{j}}(z^{-1}) = -n\phi_{n}(z) \overline{\phi_{n}}(z^{-1}) + z\left( \overline{\phi_{n}} (z^{-1}) \phi_{n}^{\prime}(z) - \left( \overline{\phi_{n}}(z^{-1}) \right)^{\prime} \phi_{n}(z) \right).
\end{equation*}
Substituting this into (\ref{diffid1}), we obtain
\begin{align} 
&\partial_{s}\ln D_{n}(s,\theta_{0},0)  =  2n \frac{\partial_{s} \chi_{n}}{\chi_{n}}\nonumber \\ &- \frac{1}{2\pi} \int_{0}^{2\pi} \partial_{s} \left[ e^{i\theta}\left( \overline{\phi_{n}} (e^{-i\theta}) \phi_{n}^{\prime}(e^{i\theta}) - \left. \left( \overline{\phi_{n}}(z^{-1}) \right)^{\prime}\right|_{z=e^{i\theta}} \phi_{n}(e^{i\theta}) \right) \right] f(e^{i\theta})d\theta \nonumber\\
& \qquad =  2n \frac{\partial_{s} \chi_{n}}{\chi_{n}} + I_{1} + I_{2} + I_{3} + I_{4},
\label{diffid2}\end{align}
where
\begin{align}
&I_{1}  =  - \frac{1}{2\pi} \int_{0}^{2\pi} e^{i\theta} \partial_{s} \left( \overline{\phi_{n}} (e^{-i\theta}) \right) \phi_{n}^{\prime} (e^{i\theta}) f(e^{i\theta})d\theta,\\
&I_{2} = -\frac{1}{2\pi} \int_{0}^{2\pi} e^{i\theta} \overline{\phi_{n}}(e^{-i\theta})  \partial_{s} \left( \phi_{n}^{\prime}(e^{i\theta}) \right) f(e^{i\theta})d\theta,\\
&I_{3} = \frac{1}{2\pi} \int_{0}^{2\pi} e^{i\theta} \partial_{s} \left( \left. \left( \overline{\phi_{n}}(z^{-1}) \right)^{\prime} \right|_{z=e^{i\theta}} \right) \phi_{n}(e^{i\theta}) f(e^{i\theta})d\theta,\\
&I_4=\frac{1}{2\pi} \int_{0}^{2\pi} e^{i\theta} \left. \left( \overline{\phi_{n}}(z^{-1}) \right)^{\prime} \right|_{z=e^{i\theta}} \partial_{s} \phi_{n}(e^{i\theta}) f(e^{i\theta})d\theta.
\end{align}
From the orthogonality relation (\ref{Orthogonality_condition}), we easily get
\begin{equation}
I_2=I_3=-n \frac{\partial_s\chi_{n}}{\chi_{n}}.\label{I23}
\end{equation}
The computation of $I_1$ and $I_4$ is slightly more involved. Using (\ref{symbol}), we have
\begin{multline} 
I_{1}  =  - \frac{1}{2\pi i} \int_{0}^{2\pi} \partial_{s} \left( \overline{\phi_{n}} (e^{-i\theta}) \right) \frac{d}{d\theta} \left( \phi_{n} (e^{i\theta}) \right) d\theta \\
+ \frac{1-s}{2\pi i} \int_{\theta_0}^{2\pi-\theta_0} \partial_{s} \left( \overline{\phi_{n}} (e^{-i\theta}) \right) \frac{d}{d\theta} \left( \phi_{n} (e^{i\theta}) \right) d\theta.
\end{multline}
Integrating by parts and then using orthogonality, we obtain
\begin{eqnarray}
I_1&=&\frac{1-s}{2\pi i} \left[ \partial_{s} \left( \overline{\phi_{n}}(e^{-i\theta}) \right) \phi_{n}(e^{i\theta}) \right]_{\theta_{0}}^{2\pi -\theta_{0}} + \frac{1}{2\pi i} \int_{0}^{2\pi} \phi_{n}(e^{i\theta}) \partial_{s}\frac{d}{d\theta} \left( \overline{\phi_{n}} (e^{-i\theta}) \right) f(e^{i\theta}) d\theta\nonumber \\&=& \frac{1-s}{2\pi i} \left[ \partial_{s} \left( \overline{\phi_{n}}(e^{-i\theta}) \right) \phi_{n}(e^{i\theta}) \right]_{\theta_{0}}^{2\pi -\theta_{0}} - n \frac{\partial_s \chi_{n}}{\chi_{n}}.\label{I1}
\end{eqnarray}
In the same way, we show that
\begin{eqnarray}
\begin{array}{r c l}
\displaystyle I_{4} & = & \displaystyle  \frac{1}{2\pi} \int_{0}^{2\pi} e^{i\theta} \left. \left( \overline{\phi_{n}}(z^{-1}) \right)^{\prime} \right|_{z=e^{i\theta}} \partial_{s} \phi_{n}(e^{i\theta}) f(e^{i\theta})d\theta \\
& = &  \displaystyle -\frac{1-s}{2\pi i} \left[ \overline{\phi_{n}}(e^{-i\theta}) \partial_{s} \phi_{n}(e^{i\theta}) \right]_{\theta_{0}}^{2\pi -\theta_{0}} - n \frac{\partial_s \chi_{n}}{\chi_{n}}.\label{I4}
\end{array}
\end{eqnarray}
Summing up (\ref{I23}), (\ref{I1}), and (\ref{I4}), and using the fact that $\overline{\phi_{n}} =  \phi_{n}$ if $W=0$, we get the result.
\end{proof}




As a consequence of Proposition \ref{proposition: diff id} and (\ref{sol_Y}), we can express the right hand side of (\ref{Differential_identity_for_D_n}) in terms of $Y=Y^{(n)}$ given by (\ref{sol_Y}):

\begin{corollary}\label{cor}We have
\begin{equation} \label{D_n_in_term_of_Y}
\partial_{s} \ln D_{n}(s,\theta_{0},0) = n \partial_{s}\ln Y_{12}(0) + \frac{2(1-s)}{\pi} \Im \left( \frac{\overline{Y_{11}(e^{i\theta_{0}})}}{\sqrt{Y_{12}(0)}} \partial_{s} \left( \frac{Y_{11}(e^{i\theta_{0}})}{\sqrt{Y_{12}(0)}} \right) \right).
\end{equation}
\end{corollary}
\begin{proof}
By \eqref{sol_Y}, we have
\begin{equation*}
Y_{12}(0) = \chi_{n}^{-2},\qquad Y_{11}(e^{i\theta_{0}}) = \chi_{n}^{-1}\phi_{n}(e^{i\theta_{0}}).
\end{equation*}
Substituting this into \eqref{Differential_identity_for_D_n}, we get \eqref{D_n_in_term_of_Y}.
\end{proof}

Integrating both sides from $0$ to $s_0$ in (\ref{diffid1general}) or (\ref{Differential_identity_for_D_n}), we obtain
\begin{equation}\label{integration_diff_identity}
\ln D_n(s_0,\theta_0,W) - \ln D_n(0,\theta_0,W) = \int_{0}^{s_0} \left[ \partial_s \ln D_n (s,\theta_0,W)\right]ds.
\end{equation}

In order to obtain asymptotics for $\ln D_n(s_0,\theta_0,W)$, we need large $n$ asymptotics for the right-hand side of (\ref{diffid1general}) and \eqref{Differential_identity_for_D_n} uniformly for $0 \leq s \leq s_0$. 



To obtain large $n$ asymptotics for $Y$, we will use the following RH characterization \cite{FIK}:
$Y(z) = Y^{(n)}(z)$ is the unique $2 \times 2$ matrix-valued function  which satisfies the following properties. 

\subsubsection{RH problem for $Y$}
\begin{itemize}
\item[(a)] $Y : \mathbb{C}\setminus S_{1} \to \mathbb{C}^{2\times 2}$ is analytic.
\item[(b)] $Y$ has the following jumps:
\begin{equation*}
Y_{+}(z) = Y_{-}(z) \begin{pmatrix}
1 & z^{-n}f(z) \\ 0 & 1
\end{pmatrix}, \hspace{0.5cm} \mbox{ for } z \in S_{1}\setminus \left\{z_{0}=e^{i\theta_0} ,\overline{z_{0}}=e^{-i\theta_0}\right\},
\end{equation*}
where $Y_+(z)$ ($Y_-(z)$) denotes the limit as $z$ is approached from the inside (outside) of the unit circle.
\item[(c)] $Y(z) = \left(I + \bigO(z^{-1})\right)  \begin{pmatrix}
z^{n} & 0 \\ 0 & z^{-n}
\end{pmatrix}$ as $z \to \infty$.
\item[(d)] As $z$ tends to $z_0$ or $z$ tends to $\overline{z_0}$, $Y$ behaves as
\begin{equation*}
\begin{array}{l l}
Y(z) = \begin{pmatrix}
\bigO(1) & \bigO(\ln |z-z_0|) \\ \bigO(1) & \bigO(\ln |z-z_0|)


\end{pmatrix} &  \mbox{ as } z \to z_0, \\ [0.8cm]
Y(z) = \begin{pmatrix}
\bigO(1) & \bigO(\ln |z-\overline{z_0}|) \\ \bigO(1) & \bigO(\ln |z-\overline{z_0}|)
\end{pmatrix} &  \mbox{ as } z \to \overline{z_0}.
\end{array}
\end{equation*}
\end{itemize}

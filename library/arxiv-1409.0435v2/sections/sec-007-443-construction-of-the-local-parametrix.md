---
doc_id: arxiv-1409.0435v2
doc_title: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap"
section_id: sec-007-443-construction-of-the-local-parametrix
section_title: "Construction of the local parametrix"
section_number: 4.4.3
pages: 20-26
source_pdf: 1409.0435v2.pdf
source_sha256: 0c6abbb9c5a720d9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.996
---
We construct $P$ as follows,
\begin{equation}\label{Explicit_P}
P(z)=E(z)\widehat\Psi(n^2\zeta(z))e^{-\frac{n}{2}\phi(z)\sigma_3}e^{-\frac{1}{2}W(z)\sigma_{3}},
\end{equation}
where $E$ is an analytic function in $D(z_0,r)$, and where
$\zeta(z) = \frac{1}{16} \phi(z)^{2}$. By (\ref{phi int}), we have that $\zeta(z)$ is a conformal map near $z_0$, and that $\zeta(z_0)=0$. Moreover, $\zeta$ maps $\gamma\cap D(z_0,r)$ to part of the real line. We now fix the lens-shaped contours $\gamma_-$ and $\gamma_+$ by requiring that $\zeta(\gamma_-\cup\gamma_+)\subset \Sigma_{\widehat\Psi}$.

For any analytic function $E$, we have that $P$ defined in \eqref{Explicit_P} satisfies conditions (a), (b), and (d) of the RH problem for $P$. Indeed, $P$ is analytic in $D(z_0,r)\setminus(\gamma\cup\gamma_+\cup\gamma_-\cup\gamma^c)$ by construction, and 
by (\ref{Explicit_P}) and (\ref{jumps hatPsi}), it is straightforward to verify that the jump condition
(\ref{jumps P}) holds. The logarithmic behavior (\ref{P local}) of $P$ near $z_0$ follows from the logarithmic behavior (\ref{Psi local}) together with the definition (\ref{def hatPsi})-(\ref{def A}) of $\widehat\Psi$.
If we define $E(z)$ by 
\begin{equation*}
E(z) = P^{(\infty)}(z)e^{\frac{1}{2}W(z)\sigma_{3}}  \frac{1}{\sqrt{2}} \begin{pmatrix}
1 & -i \\ -i & 1
\end{pmatrix} \left( \frac{1}{2} n\pi \phi(z) \right)^{\frac{\sigma_{3}}{2}},
\end{equation*}
we have in addition the matching condition (\ref{matching P z0}) for $P$.  Using the jump relation for $P^{(\infty)}$, it is easily verified that $E$ is analytic near $z_0$.
This completes the construction of the local parametrix near $z_0$.


\subsection{Local parametrix near $\overline{z_0}$}

Once the local parametrix near $z_0$ constructed, the local parametrix near $\overline{z_0}$ is easy to construct. Define for $z \in D(\overline{z_{0}},r)$,  $P(z)=\overline{P(\overline{z})}$, where $\overline{P(\overline{z})}$ refers to the local parametrix constructed near $z_{0}$. Then, $P$ satisfies the following RH conditions.


\subsubsection{RH problem for $P$}

\begin{itemize}
\item[(a)] $P : D(\overline{z_{0}},r) \setminus (S_{1} \cup \gamma_{+} \cup \gamma_{-}) \to \mathbb{C}^{2\times 2}$ is analytic.
\item[(b)] For $z\in D(\overline{z_{0}},r)$ and $z$ on the jump contour, $P$ satisfies the jump conditions
\begin{equation*}
\begin{array}{l l}
P_{+}(z) = P_{-}(z) \begin{pmatrix}
0 & e^{W(z)} \\ -e^{-W(z)} & 0
\end{pmatrix}, & \mbox{ on } \gamma\setminus\{z_{0},\overline{z_{0}}\}, \\

P_{+}(z) = P_{-}(z) \begin{pmatrix}
 1 & e^{n(\phi(z)-x)}e^{W(z)} \\
 0 & 1
\end{pmatrix}, & \mbox{ on } \gamma^{c}, \\

P_{+}(z) = P_{-}(z) \begin{pmatrix}
 1 & 0  \\ e^{-n\phi(z)}e^{-W(z)} & 1
\end{pmatrix}, & \mbox{ on } \gamma_{-} \cup \gamma_{+}. \\
\end{array}
\end{equation*}
\item[(c)] For $ z \in \partial D (\overline{z_{0}},r)$, we have
\begin{equation}\label{matching P z0bar} P(z) = \left(I + \bigO(n^{-1})\right) P^{(\infty)}(z),\qquad\mbox{ as $n \to \infty$.}
\end{equation}
\item[(d)] As $z$ tend to $\overline{z_{0}}$, the behaviour of $P$ is
\begin{equation*}
\begin{array}{l l}
P(z) = \bigO(\ln|z-\overline{z_0}|).
\end{array}
\end{equation*}
\end{itemize}






\subsection{Local parametrix near $-1$}
For $x>x_c+\delta$, the jump matrix for $S$ converges exponentially fast to the identity matrix as $n\to\infty$ near  $-1$. However, as $x$ approaches $x_c$, the convergence becomes slower, and for $x=x_c$, the jump matrix for $S$ does not converge to $I$ any longer. Therefore, we need to construct a local parametrix near $-1$. This construction can be done for any $x\geq x_c$ but is only necessary when $x$ is close to $x_c$. The local parametrix should satisfy the following conditions.

\subsubsection{RH problem for $P$}
\begin{itemize}
\item[(a)] $P : D(-1,r)\setminus S_{1} \to \mathbb{C}^{2\times 2}$ is analytic.
\item[(b)] $P$ has the jump
\begin{equation}
P_+(z)=P_-(z)\begin{pmatrix}1 & e^{n(\phi(z)-x)}e^{W(z)}\\0 &1
\end{pmatrix}, \qquad z\in S_{1}\cap D(-1,r).
\end{equation}
\item[(c)] For $z\in\partial D(-1,r)$, we have
\begin{equation}
\label{matching P -1}P(z) = (I + o(1))P^{(\infty)}(z),\qquad \mbox{ as $n \to \infty$.}
\end{equation}
\end{itemize}

The solution of this RHP is given by

\begin{equation}\label{P-1}
P(z) = P^{(\infty)}(z) \begin{pmatrix}
1 & \tilde{h}(z) \\ 0 & 1
\end{pmatrix},
\end{equation}
with $\displaystyle \tilde{h}(z) = \frac{1}{2\pi i} \int_{S_{1}\cap D(-1,r)} \frac{e^{n(\phi(s)-x)}e^{W(s)}}{s-z}ds$.
Using the fact that $\phi(s)-x_c$ has a double zero at $s=1$, it is straightforward to verify that
\begin{equation}
\tilde{h}(z)=\bigO(n^{-1/2}e^{n(x_c-x)}),\qquad\mbox{for $z\in \partial D(-1,r)$, as $n\to\infty$,}
\end{equation}
and this implies the matching condition (\ref{matching P -1}).


Note that we use the same notation $P$ for the different local parametrices defined in $D(z_0,r)$, $D(\overline{z_0,r})$, and $D(-1,r)$.



\subsection{Final transformation $S\mapsto R$}


Define
\begin{equation}\label{R}
R(z)=\begin{cases}
S(z)P^{(\infty)}(z)^{-1},&z\in\mathbb C\setminus(\overline{D(z_0,r)}\cup\overline{D(\overline{z_0},r)}\cup\overline{D(-1,r)}),\\
S(z)P(z)^{-1}, & z\in D(z_0,r)\cup D(\overline{z_0},r)\cup D(-1,r).
\end{cases}
\end{equation}
$P$ was constructed in such a way that it has exactly the same jump relations as $S$ in $D(z_0,r)\cup D(\overline{z_0},r)\cup D(-1,r)$, and as a consequence $R$ has no jumps at all inside those disks. Moreover, from the local behaviour of $S$ and $P$ near $z_0$, $\overline{z_0}$ and $-1$, it follows that $R$ is analytic at these three points.
We have the following RH problem for $R$:

\subsubsection{RH problem for $R$}









\begin{figure}[t]
    \begin{center}
    \setlength{\unitlength}{1truemm}
    \begin{picture}(100,55)(-5,10)
        \cCircle(65,60){7.5}[f]
        \cCircle(65,20){7.5}[f]
        \cCircle(25,40){7.5}[f]
        \qbezier(69.5,54)(75,40)(69.5,26)
        \qbezier(72.3861,58.6976)(100,40)(72.3861,21.3024)


        \qbezier(26.125,47.415)(35.9673,69.0665)(58.3936,63.5488)
        \qbezier(26.125,32.585)(35.9673,10.9335)(58.3936,16.4512)
        
        \put(67,67.3){\thicklines\vector(1,0){.0001}}
        \put(63.8,12.6){\thicklines\vector(-1,0){.0001}}
        \put(17.5,41.5){\thicklines\vector(0,1){.0001}}
        \put(72.3,41){\thicklines\vector(0,1){.0001}}
        \put(86.2,42){\thicklines\vector(0,1){.0001}}
        \put(50,64.5){\thicklines\vector(-1,0){.0001}}
        \put(51,15.3){\thicklines\vector(1,0){.0001}}
        
        
        
        
        
        \put(64,59){$z_{0}$} 
        \put(64,19){$\overline{z_{0}}$}
        \put(22.5,38.8){$-1$}
        
        \put(48,68){$\Sigma_{R}$}
    \end{picture}
    \caption{The jump contour for $R$.}
    \label{figure: contour R}
\end{center}
\end{figure}


\begin{itemize}
\item[(a)] $R : \mathbb{C} \setminus \Sigma_{R} \to \mathbb{C}^{2\times 2}$ is analytic, with $\Sigma_R$ as in Figure \ref{figure: contour R}.
\item[(b)] $R$ satisfies the jump conditions:
\begin{equation*}
\begin{array}{l l}
\displaystyle R_{+}(z) = R_{-}(z) \left(I + \bigO(n^{-1})\right), & \mbox{ for } z \in \partial D(z_{0},r) \cup \partial D(\overline{z_{0}},r), \\[0.2cm]

\displaystyle R_{+}(z) = R_{-}(z) \left(I + \bigO(n^{-\frac{1}{2}}e^{n(x_c-x)})\right), & \mbox{ for } z \in \partial D(-1,r), \\[0.2cm]

\displaystyle R_{+}(z) = R_{-}(z) (I+\bigO(e^{-cn})), c>0 & \mbox{ for } z \mbox{ elsewhere on } \Sigma_{R}.

\end{array}
\end{equation*}
\item[(c)] $R(z) = I + \bigO(z^{-1})$ as $z \to \infty$.
\end{itemize}
As $n\to\infty$ with $s\leq e^{-x_cn}$, it follows from the standard theory for small-norm RH problems that \begin{equation}R(z) = I + \bigO(n^{-\frac{1}{2}}e^{n(x_c-x)})+\bigO(n^{-1}),\qquad R^{\prime}(z) = \bigO(n^{-\frac{1}{2}}e^{n(x_c-x)})+\bigO(n^{-1}),\label{as R}
\end{equation}
uniformly for $z \in \mathbb{C}\setminus \Sigma_{R}$.
By a more detailed analysis of Cauchy operators associated to the RH problem for $R$, one obtains in addition that
\begin{equation}\label{dxR}
\partial_x R(z)=\bigO(n^{1/2}e^{n(x_c-x)}).
\end{equation}
The latter estimate is not really needed for the proof of Theorem \ref{theorem: extensionWidom}, but will be needed in our alternative proof if $W=0$, see Section \ref{section: proof W0}.
Since $s=e^{-xn}$, it follows that 
\begin{equation}\label{dsR}
\partial_s R(z)=-\frac{e^{xn}}{n}\partial_x R(z)=\bigO(n^{-1/2}e^{nx_c}).
\end{equation}



\section{Asymptotics for $D_n(s,\theta_0,W)$}\label{section: int}

We will now complete the proof of Theorem \ref{theorem: extensionWidom} using the results from the previous sections. We first do this for general analytic $W$ in the case where $\epsilon<\theta_0<\pi-\epsilon$ for some $\epsilon>0$. Afterwards we will explain how the proof can be somewhat simplified if $W=0$, and we will show how it can be extended to the case where $\theta_0$ approaches $\pi$ at a sufficiently slow rate.




\subsection{Proof of Theorem \ref{theorem: extensionWidom} for $\epsilon<\theta_0<\pi-\epsilon$}

By inverting the transformations $Y\mapsto T\mapsto S\mapsto R$, we obtain an expression for $R$ in terms of $Y$, involving the parametrices $P$ and $P^{(\infty)}$.
For $z\in \gamma^c\cap (D(z_0,r)\cup D(\overline{z_0},r)\cup D(-1,r))$, we have
\begin{equation}\label{YinRin}
Y_\pm(z) = e^{-\frac{n\pi i}{2}\sigma_{3}}e^{-\frac{n\ell}{2}\sigma_3 } R(z) P_\pm(z) e^{ng(z)\sigma_3}e^{\frac{n\ell}{2} \sigma_{3}}e^{\frac{n\pi i}{2}\sigma_{3}},
\end{equation}
and for $z\in\gamma^c\setminus (D(z_0,r)\cup D(\overline{z_0},r)\cup D(-1,r))$,
\begin{equation}\label{YinR out}
Y_\pm(z) = e^{-\frac{n\pi i}{2}\sigma_{3}}e^{-\frac{n\ell}{2} \sigma_3} R_\pm(z) P^{(\infty)}(z) e^{ng(z)\sigma_3}e^{\frac{n\ell}{2} \sigma_{3}}e^{\frac{n\pi i}{2}\sigma_{3}}.
\end{equation}
It follows that
\begin{equation}\label{Yindiffid}
\left[Y^{-1}(z)Y'(z)\right]_{21}=\begin{cases} (-1)^{n}e^{2ng(z)}e^{n\ell}A_1(z),& z\in \gamma^c\cap (D(z_0,r)\cup D(\overline{z_0},r)\cup D(-1,r)),\\ (-1)^{n}e^{2ng(z)}e^{n\ell}A_2(z),&z\in\gamma^c\setminus (D(z_0,r)\cup D(\overline{z_0},r)\cup D(-1,r)),
\end{cases}
\end{equation}
where
\begin{align}
&A_{1}(z) = \left[ P^{-1}(z) R^{-1}(z) R^{\prime}(z) P(z) + P^{-1}(z)P^{\prime}(z) \right]_{21}, \\
&A_{2}(z) = \left[ {P^{(\infty )}}^{-1}(z) R^{-1}(z) R^{\prime}(z) P^{(\infty )}(z) + {P^{(\infty )}}^{-1}(z){P^{(\infty )}}^{\prime}(z) \right]_{21}.
\end{align}
Note that the boundary values of $A_1(z)$ and $A_2(z)$ as $z$ is approached from the inside and the outside of the unit circle are the same.
For $z\in D(-1,r)$, the local parametrix $P$ is given by (\ref{P-1}), and one verifies that the formulas for $A_1$ and $A_2$ coincide in this case.

 Substituting (\ref{Yindiffid}) in the differential identity \eqref{diffid1general}, we find 
\begin{equation} \label{diff_identity_W}
\partial_{s} \ln D_{n} (s,\theta_{0},W) = I_{1} + I_{2},
\end{equation}
where
\begin{equation*}
\begin{array}{l}
\displaystyle I_{1} = \frac{1}{2\pi i} \int_{\gamma_{1}^{c}} z^{-n} e^{2ng(z)}e^{n\ell} A_{1}(z) e^{W(z)}dz, \\[0.4cm]
\displaystyle I_{2} = \frac{1}{2\pi i} \int_{\gamma_{2}^{c}} z^{-n} e^{2ng(z)} e^{n\ell} A_{2}(z) e^{W(z)}dz, 
\end{array}
\end{equation*}
with $\gamma_{1}^{c} = \gamma^{c} \cap (D(z_{0},r) \cup D(\overline{z_{0}},r))$ and $\gamma_{2}^{c} = \gamma^{c}\setminus (D(z_{0},r) \cup D(\overline{z_{0}},r))$.

Now we need to know how $I_1$ and $I_2$ behave for large $n$ and $s\leq e^{-x_cn}$. For $A_2$, we note that $P^{(\infty)}$ does not depend on $n$, and that $R$ and $R'$ are uniformly bounded by (\ref{as R}). This implies that $A_{2}(z)$ is uniformly bounded on $\gamma_2^c$ for large $n$. For $A_1$, we need to take a closer look at the construction of $P$ near $z_0$ and $\overline{z_0}$, but it is straightforward to show that $P(z)=\bigO(n)$, $P^{-1}(z)=\bigO(n)$, and $P'(z)=\bigO(n^2)$ for $z\in\gamma_1^c$.
We get
\begin{equation*}
\begin{array}{r c l}
\displaystyle |I_{1}| & = & \displaystyle \bigO \left(n^3 \int_{[\theta_{0},\theta_{0}+r] \cup [2\pi - \theta_{0}-r,2\pi - \theta_{0}]} \left| e^{2ng(e^{i\alpha})+n\ell} \right| d\alpha \right), \\[0.4cm]
\displaystyle |I_{2}| & = & \displaystyle \bigO \left( \int_{\theta_{0}+r}^{2\pi -\theta_{0}-r} \left| e^{2ng(e^{i\alpha})+n\ell} \right| d\alpha \right),
\end{array}
\end{equation*}
as $n\to\infty$ with $s\leq e^{-x_c n}$.
The function $2g(z)+\ell-x_{c}$ is always negative on $\gamma^{c}$ except that it has a zero of order two at $z=-1$. 
Therefore we obtain after a straightforward analysis that
\begin{align}
&|I_{1}| = \bigO\left(e^{n(x_{c}-C)} \right),\qquad C>0, \label{Estimate1}\\
&|I_{2}| = \bigO (n^{-1/2}e^{nx_{c}}), \label{Estimate2}
\end{align}
as $n\to\infty$, $s\leq e^{-x_c n}$.

If we integrate \eqref{diff_identity_W} from $0$ up to $s=e^{-xn} \leq e^{-x_{c}n}$, we finally obtain the desired estimate
\begin{equation*}
\ln D_{n} (s,\theta_{0},W) - \ln D_{n}(0,\theta_{0},W) = \int_{0}^{s} (I_{1} + I_{2}) ds^{\prime} =\bigO(n^{-1/2}e^{-n(x-x_c)}).
\end{equation*}








\subsection{Alternative proof of Theorem \ref{theorem: extensionWidom} if $W=0$, $s=o(n^{1/2}e^{-nx_c})$}\label{section: proof W0}
In the case where $W=0$, there is an alternative approach to prove Theorem \ref{theorem: extensionWidom}: we can use the differential identity (\ref{D_n_in_term_of_Y}) instead of (\ref{diffid1general}). This does not make the proof much shorter, but it has the advantage that no integrals have to be estimated, and that we only need information about $Y$ at the points $0$ and $z_0$, instead of on the entire curve $\gamma_c$. The objects in the differential identity can be computed more explicitly in this case by the following result.


\begin{proposition}\label{Y11 and Y12}
Let $W=0$. As $n\to\infty$ with $x>x_c$, we have
\begin{align} \label{Asymptotics_Y12_Y11}
& Y_{12}(0)=  e^{-n\ell}\left[ \sin \frac{\theta_{0}}{2}+\bigO (n^{-1/2} )\right],\\
&\label{dsY} \partial_s \ln Y_{12}(0)= \bigO (n^{-1/2}e^{nx_c} ),\\
&Y_{11}(z_0)=e^{-\frac{n\ell}{2}}\bigO (n^{1/2}).
\end{align}
\end{proposition}
\begin{proof}
Using (\ref{YinR out}) and the expressions $g(0) = \pi i$ and $P_{12}^{(\infty)}(0) = \sin \frac{\theta_{0}}{2}$ (if $W=0$), we get the result for $Y_{12}(0)$.

For $\partial_s \ln Y_{12}(0)$, we have
\begin{equation}
\partial_s \ln Y_{12}(0)=\frac{\partial_s\left(R_{11}(0)P_{12}^{(\infty)}(0)+R_{12}(0)P^{(\infty)}_{22}(0)\right)}{R_{11}(0)P_{12}^{(\infty)}(0)+R_{12}(0)P^{(\infty)}_{22}(0)}.
\end{equation}
By (\ref{dsR}), this yields (\ref{dsY}).


For the rest of this proof, we assume that $|z|<1$ and that $z$ lies outside of the lenses and in $D(z_0,r)$. Then we have by (\ref{YinRin}),
\begin{equation}\label{Y11}
Y_{11}(z) = e^{ng(z)} \left[ R_{11}(z)P_{11}(z) + R_{12}(z)P_{21}(z) \right].
\end{equation}
By (\ref{g}) and (\ref{g1}), we can show that








\begin{equation*}
g(z_{0}) = -\frac{\ell}{2} + i \frac{\theta_{0}+\pi}{2}.
\end{equation*}
On the other hand, by (\ref{Psi explicit}), as $z \to z_{0}$ for fixed $n$, we have
\begin{equation*}
\Psi_{11}(n^{2}\zeta(z)) = 1+ \bigO(z-z_{0}), \quad \Psi_{21}(n^{2}\zeta(z)) = \bigO(z-z_{0}).
\end{equation*}
This implies, by (\ref{def hatPsi}), that
\begin{equation*}
P_{j1}(z_{0}) = E_{j1}(z_{0})(1+\bigO(e^{-nx}))e^{-\frac{n}{2}\phi(z_{0})},\qquad\mbox{ as $n\to\infty$}.
\end{equation*}
Since $\phi(z_{0}) = 0$, we have $P_{j1}(z_{0}) = \bigO(\sqrt{n})$, $j=1,2$, and
\begin{equation*}
Y_{11}(z_{0}) = e^{n \left( -\frac{\ell}{2} +i \frac{\theta_{0}+\pi}{2} \right)}  \left( P_{11}(z_{0}) + \bigO \left( 1 \right) \right)=e^{-\frac{n\ell}{2}}\bigO (n^{1/2}),
\end{equation*}
as $n\to\infty$.
\end{proof}


By Proposition \ref{Y11 and Y12} and (\ref{D_n_in_term_of_Y}), we have
\begin{align}
&n \partial_{s}\ln Y_{12}(0) = \bigO(n^{1/2}e^{nx_c}),\\
& \frac{2(1-s)}{\pi} \Im \left( \frac{\overline{Y_{11}(e^{i\theta_{0}})}}{\sqrt{Y_{12}(0)}} \partial_{s} \left( \frac{Y_{11}(e^{i\theta_{0}})}{\sqrt{Y_{12}(0)}} \right) \right) = \bigO(n),
\end{align}
as $n\to\infty$.
Therefore, using \eqref{integration_diff_identity}, we get
\begin{equation*}
\begin{array}{r c l}
\displaystyle \ln D_{n}(s,\theta_{0},0) & = & \displaystyle \ln D_{n}(0,\theta_{0},0) + \int_{0}^{s} \bigO(n^{1/2}e^{nx_c}) ds^{\prime} \\
& = & \displaystyle \ln D_{n}(0,\theta_{0},0) + \bigO(n^{1/2}e^{-n(x-x_{c})}),
\end{array}
\end{equation*} and we rederive Theorem \ref{theorem: extensionWidom} with a slightly worse error term which is only small if $s=o(n^{1/2}e^{-nx_c})$.








\subsection{Extension to the case where $\theta_0$ depends on $n$}
The RH analysis done in the previous section is valid as $n\to\infty$ with $\epsilon<\theta_0<\pi-\epsilon$ and $\epsilon>0$ independent of $n$. If $\theta_0=\theta_0(n)$ depends on $n$ and approaches $\pi$ as $n\to\infty$, the arc $\gamma$ grows and the {\em gap} $(e^{i\theta_0},e^{i(2\pi-\theta_0)})$ closes. 
Similarly to \cite{Krasovsky}, we will show here that the RH analysis carried out before remains valid as long as $n(\pi-\theta_0)$ is large.

A first problem in the RH analysis is that we need to allow the radius $r=r(n)$ of the disks $D(z_0,r)$, $D(-1,r)$, and $D(\overline{z_0},r)$ to depend on $n$ (or on $\theta_0$) in order to prevent the disks to overlap.
For instance, we can keep the disks separated from each other if we let $r(\theta_0)=\delta(\pi-\theta_0)$, with $\delta>0$ a sufficiently small but fixed number.
Then the local parametrices near $z_0, \overline{z_0}, -1$ can be constructed in exactly the same way as before. However, in order to make the asymptotic analysis work, it is crucial that the jump matrix for $R$ tend to $I$ uniformly as $n\to\infty$ on the $n$-dependent jump contour. Recall that the jump matrix for $R$ is given by
\begin{equation}
J_R(z)=\begin{cases}P(z)P^{(\infty)}(z)^{-1},&z\in\partial D(z_0,r)\cup \partial D(\overline{z_0},r)\cup \partial D(-1,r),\\
P^{(\infty)}(z)J_S(z) P^{(\infty)}(z)^{-1},&z\in\Sigma_R\setminus\left(\partial D(z_0,r)\cup \partial D(\overline{z_0},r)\cup \partial D(-1,r)\right),
\end{cases}
\end{equation}
where $J_S$ denotes the jump matrix for $S$ given in (\ref{JS}).




The first thing to notice is that  $h(z)$, defined in \eqref{h}, and $\beta(z)$, defined right before (\ref{h}), are uniformly bounded on the jump contour $\Sigma_{R}$. This implies that $P^{(\infty)}(z)$ is uniformly bounded for $z\in\Sigma_R$. 
Next, by (\ref{phi int}), we have \begin{equation}|\phi(z)| \geq C \sin(\pi-\theta_{0}),\qquad z\in\Sigma_R,
\end{equation} 
for a constant $C > 0$ independent of $z$ and $\theta_{0}$. 
By (\ref{JS}), this already implies that the jump matrix $J_R$ is $I+\bigO(n^{-1}(\pi-\theta_0)^{-1})$ on $\Sigma_R$, except on the three circles around $z_0, \overline{z_0}$, and $-1$.
On $\partial D(z_0,r)$ and $\partial D(\overline{z_0},r)$, we have
\begin{eqnarray}
J_R(z)&=&P(z)P^{(\infty)}(z)^{-1}=P^{(\infty)}(z)\left(I+\bigO(n^{-1}\phi(z)^{-1})\right)P^{(\infty)}(z)^{-1}\\&=&I+\bigO(n^{-1}(\pi-\theta)^{-1}).
\end{eqnarray}
Finally, on $\partial D(-1,r)$, by (\ref{P-1}), we have
\begin{equation}
J_R(z)=P(z)P^{(\infty)}(z)^{-1}=I+\bigO(\widetilde{h}(z))=I+\bigO(n^{-1/2}e^{-n(x-x_c)}).
\end{equation}
It follows from these considerations that \[J_{R}(z) - I = \bigO(n^{-1}(\pi-\theta_0)^{-1}) + \bigO(n^{-1/2}e^{-n(x-x_c)}),\qquad\mbox{ as $n\to\infty$},\] with $\theta_0$ approaching $\pi$ sufficiently slowly such that $n (\pi-\theta_{0}) \to + \infty$. By the small-norm theory for RH problems, it follows that \begin{equation}
R(z) = I+\bigO \left( n^{-1}(\pi-\theta_{0})^{-1}\right) + \bigO(n^{-1/2}e^{-n(x-x_c)}),
\end{equation} and \begin{equation}
\qquad R^{\prime}(z) = \bigO \left( n^{-1}(\pi-\theta_{0})^{-1}\right) + \bigO(n^{-1/2}e^{-n(x-x_c)}),
\end{equation}
as $n\to\infty$, $n (\pi-\theta_{0}) \to + \infty$.
The proof of Theorem \ref{theorem: extensionWidom} can now be completed in the same way as before, where the estimate \eqref{Estimate1} remains valid, \eqref{Estimate2} becomes
\begin{equation*}
|I_{2}| =\bigO((\pi-\theta_0)^{1/2}n^{-1/2}e^{nx_c}),
\end{equation*}
and we obtain the error term (\ref{error large y}).

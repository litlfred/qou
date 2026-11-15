---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-016-52-examples
section_title: "Examples"
section_number: 5.2
pages: 25-26
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.837
latex_coverage_ratio: 0.976
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
\label{Sexamples}

As an illustration of our main Theorem~\ref{theorem_J(2,2m)}, we explicitly compute ${\mathbb T}^{K}_{\lambda}$ on the character variety $X^{\mathrm{irr}}_\lambda(\Pi(K))$ for the following four examples: the trefoil knot $3_1 = J(2,2)$, $5_2 = J(2,4)$, the figure eight knot $4_1 = J(2,-2)$, and $6_1 = J(2,-4)$ respectively. The computer program for the computation is written on the free computer algebra system Maxima~\cite{Max}.


\begin{itemize}
\item[(1)]
    For the trefoil knot $3_1 = J(2, 2)$, the Riley polynomial is given by 
    $$\phi_{J(2, 2)}(s, u) = -1 + s+s^{-1} - u.$$
    The computation of the non--abelian Reidemeister torsion for $J(2, 2)$ is expressed as follows.
    \begin{align*}
        {\mathbb T}^{J(2, 2)}_{\lambda}(\rho_{\sqrt{s}, u}) 
            &= \frac{\tau_0}{s + s^{-1} -2} \left(-3(s+s^{-1}-2)\right) \\
            &= -3 \tau_0.
    \end{align*}
    This coincides with the inverse of the result~\cite[Subsection~6.1]{JDFibre} (see Remark~\ref{rmkinv}).
\item[(2)]
    For $5_2 = J(2, 4)$, the Riley polynomial is given by 
    \begin{align*}
    \phi_{J(2, 4)}(s, u) =-3+2(s+s^{-1}) &+\left(-4+3(s+s^{-1})-(s+s^{-1})^2\right)u \\ &+ \left(-3+2(s+s^{-1})\right) u^2 - u^3.
    \end{align*}
    The non--abelian Reidemeister torsion for $5_2 = J(2, 4)$ is expressed as follows.
    \begin{align*}
        {\mathbb T}^{J(2, 4)}_{\lambda}(\rho_{\sqrt{s}, u}) 
            &= \frac{\tau_0}{s + s^{-1} -2}  
                   [ -2 + 21(s+s^{-1})-10(s+s^{-1})^2 \\
            &\quad
                    +\{-2+15(s+s^{-1})-17(s+s^{-1})^2+5(s+s^{-1})^3\}u \\
            &\quad
                    +\{6+7(s+s^{-1})-5(s+s^{-1})^2\}u^2 ]\\
            &=\tau_0
              \left(-10(s+s^{-1})+1
                +\left(5(s+s^{-1})^2-7(s+s^{-1})+1\right)u \right.\\
            &\qquad\qquad
               \left.+\left(-5(s+s^{-1})-3\right)u^2
               \right).
    \end{align*}
\item[(3)]
    For the figure eight knot $4_1 = J(2, -2)$, the Riley polynomial is given by  $$\phi_{J(2, -2)}(s, u)=(3-s-s^{-1})(u+1)+u^2.
    $$
    The computation of the non--abelian Reidemeister torsion for $J(2, -2)$ is expressed as follows.
    \begin{align*}
        {\mathbb T}^{J(2, -2)}_{\lambda}(\rho_{\sqrt{s}, u}) 
            &= \frac{\tau_0}{s+s^{-1}-2} \left(-2(s+s^{-1})+1\right)\left(s+s^{-1} -2\right) \\
            &= \tau_0 \left(-2(s+s^{-1})+1\right).
    \end{align*}
    This coincides with the inverse of the result~\cite[Subsection 6.3]{JDFibre} (see Remark~\ref{rmkinv}) in which the torsion is expressed as $\pm \sqrt{17 + 4I_{\lambda}} $. 
    
    Since the longitude $\lambda$ is equal to $[y,x^{-1}][x, y^{-1}]$, one has  
    $$I_{\lambda} = -2 - (s+s^{-1}) + s^2+s^{-2}.$$
 Thus, up to sign, we have 
$$\sqrt{17 + 4I_{\lambda}}= 2(s+s^{-1})-1.$$
\item[(4)]
    For $6_1 = J(2, -4)$, the Riley polynomial is given by 
\[
\begin{split}
\phi_{J(2, -4)}(s, u)= 5 &- 2(s+s^{-1})+\left(12+(s+s^{-1})^2 -7(s+s^{-1})\right)u + \\ & \left(11+(s+s^{-1})^2-6(s+s^{-1})\right)u^2+\left(5-2(s+s^{-1})\right)u^3+u^4.
\end{split}
\]
    The non--abelian Reidemeister torsion for $J(2, -4)$ is expressed as follows.
    \begin{align*}
    \lefteqn{
        {\mathbb T}^{J(2, -4)}_{\lambda}(\rho_{\sqrt{s}, u})} &\\
            &= \frac{\tau_0}{s + s^{-1} -2}  
                   [-14 - 13(s+s^{-1}) +26(s+s^{-1})^2 -8(s+s^{-1})^3\\
            &\quad
                    +\{-8 - 34(s+s^{-1}) +49(s+s^{-1})^2 - 23(s+s^{-1})^3 + 4(s+s^{-1})^4\}u \\
            &\quad
                    +\{-2 - 31(s+s^{-1}) + 32(s+s^{-1})^2 - 8(s+s^{-1})^3\}u^2 \\
            &\quad 
                    +\{2 -9(s+s^{-1}) +4(s+s^{-1})^2\}u^3 ]\\
            &=\tau_0\left[ \left(-8(s+s^{-1})^2+10(s+s^{-1})+7\right) \right.\\
            &\qquad +\left(4(s+s^{-1})^3-15(s+s^{-1})^2+19(s+s^{-1})+4\right)u\\
            &\qquad \left.+\left(-8(s+s^{-1})^2+16(s+s^{-1})+1\right)u^2
                   +\left(4(s+s^{-1})-1\right)u^3 \right].
    \end{align*}
\end{itemize}

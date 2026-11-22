---
doc_id: arxiv-2208.12678v4
doc_title: "STATIONARY CURVES UNDER THE MÖBIUS-PLATEAU ENERGY"
section_id: sec-005-4-necessary-conditions-of-möbius-plateau-critica
section_title: "Necessary Conditions of Möbius-Plateau Critical Helix Pairs"
section_number: 4
pages: 6-11
source_pdf: 2208.12678v4.pdf
source_sha256: 406d36ff4968091d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.914
latex_coverage_ratio: 0.993
doc_brief: "STATIONARY CURVES UNDER THE MÖBIUS-PLATEAU ENERGY — Plateau problems with elastic boundary energies have been of recent theoretical and applied interest."
---
\label{sec:stationary-helix-pairs}

In this section, we alter the problem slightly to consider the M\"obius energy of links, where $\gamma_1, \gamma_2: \R \to \R^3$ are disjoint locally rectifiable curves. The M\"obius energy of the link is defined as 
\begin{align}
\label{mobiuslink}
E_M(\gamma_1, \gamma_2) = \int_{\R \times \R} \frac{ |\dot{\gamma_1}(u)| | \dot{\gamma_2}(v) | dudv}{|\gamma_1(u) - \gamma_2(v)|^2}.
\end{align}
In the link case, we do not subtract an intrinsic distance term in the integrand, as it is not needed for the integral to converge. At a given point $\gamma_1(u)$, the $L^2$ gradient of the M\"obius energy is given by the vector-valued integral
\begin{align}
\label{mobiusvar}
    G_{\gamma_1, \gamma_2}(u) = 2 \int_\R \left[ \frac{2 P_{\dot{\gamma_1}(u)^\perp}(\gamma_2(v) - \gamma_1(u))}{|\gamma_2(v) - \gamma_1(u)|^2} - \textbf{N}_{\gamma_1(u)} \right] \frac{|\dot{\gamma_2}(v)|dv}{|\gamma_2(v) - \gamma_1(u)|^2}.
\end{align}
The derivation of the variational equation for the M\"obius energy of knots is given in \cite{freedman1994mobius}, and He \cite{he02} showed the equation also holds in the case of links. Here, $P_{\dot{\gamma_1}(u)^\perp}$ refers to the projection onto the plane normal to the tangent vector at $\gamma_1(u)$, and $\textbf{N}_{\gamma_1(u)}$ refers to the normal vector in the Frenet frame along $\gamma_1$. The gradient is defined similarly along $\gamma_2$ by switching $u$ and $v$.  

A rough heuristic for interpreting \eqref{mobiusvar} is that curves with large M\"obius gradient are those in which many rescaled pairwise difference vectors are close to Frenet binormals. The integral projects a rescaled difference vector onto the curve's normal plane, and subtracts the Frenet normal, leaving only the binormal. The rescaling obeys an inverse quartic law, so difference vectors between nearby points of the curve which approximate the binormal well will contribute greatly to the gradient integral. The binormal of a helix points roughly in the direction of its axis, hinting that helices provide a fruitful set of examples in studying the dynamics of the M\"obius energy. Using explicit helix parametrizations turns \eqref{mobiusvar} into an improper trigonometric integral, which we analyze with power series and elementary estimates. In a forthcoming paper, the first author analyzes the M\"obius variations for helix pairs using complex variable techniques distinct from the methods in this section.

Whilst both energies are infinite, the variational equation describing critical parametrizations remains well-defined. Let $\boldsymbol\nu$ be the oriented unit surface normal to $\Sigma$. Now, the direction of the $L^2$ gradient of the Plateau energy at $\gamma_1(u)$ (resp. $\gamma_2(v)$) is the unit conormal $\textbf{n} = -\textbf{T} \times \boldsymbol\nu$ (resp. $\textbf{T} \times \boldsymbol\nu$). This unit vector is oriented so that it is pointing away from the surface at each of the boundary components, which in turn defines the orientation of $\boldsymbol\nu$. The derivation of the gradient for the Plateau energy is a standard calculation which can be found in Prop. 1 of \cite{gruber21}. Thus, the variational equation for the M\"obius-Plateau energy is
\begin{align}
\label{mobiusplateauvar}
    \alpha G_{\gamma_1,\gamma_2} = - \beta \bf{n}.
\end{align}

A general helicoid $\Sigma = \Sigma(\omega)$ has parametrization 
\begin{align}
\label{helicoid}
    \begin{bmatrix}
    x(s,t) \\
    y(s,t) \\
    z(s,t)
    \end{bmatrix} &=
    \begin{bmatrix}
    s \cos(\omega t) \\
    s \sin(\omega t) \\
    t
    \end{bmatrix}.
\end{align}

\begin{definition}
A \textbf{helicoidal strip} is the parametrized surface in \eqref{helicoid} with $A \leq s \leq B, t \in \R$, for prescribed $A < B$. A \textbf{helicoidal screw} corresponds to the case where $A$ and $B$ have opposite signs, and a \textbf{helicoidal ribbon} corresponds to the case where $A$ and $B$ have the same signs.
\end{definition}
The two boundary curves $\gamma_1$ and $\gamma_2$ of a helicoidal strip are found by setting $s = A$ and $s = B$. We will parametrize the curves with $u$ and $v$ respectively. 

\begin{remark}
    In the prior sections, we were careful in considering the possibility of sudden transitions in the Plateau solutions induced by small variations of the boundary curve. As the frequency parameter of a helix changes, there can be a so-called ``Courant headphone transition" where the area-minimizing surface jumps from a helicoid to a surface between the vertical layers resembling a telephone cord. In Courant's time, headphone cords probably looked like this, hence the name. The transition parameters are discussed in \cite{courant40} and \cite{machon16}. As this section is concerned with necessary conditions for critical helix pairs, we do not take these transitions into account. As we will see later, numerical searches for critical helix pairs bounding a ribbon show their widths are orders of magnitude smaller than the frequency, precluding the possibility of a headphone transition. In other words, the Plateau solution for the critical helix pair is their common helicoid.
\end{remark}

The space of helicoidal screws and ribbons are given by the three parameters $A,B,$ and $\omega$. A helicoidal strip is a screw if and only if it contains the helical axis, and otherwise it is a ribbon. For given $\alpha$ and $\beta$, we seek to find the values of $A,B,$ and $\omega$ which satisfy the variational equation of the M\"obius-Plateau energy. The variational equations for stationary helix pairs differs in the case of screws and ribbons, because of the differing orientations of $\mathbf{N}$, which we will see results in two trigonometric integrals that nominally look similar, but greatly vary in how the signs of their evaluations depend on their parameters.

For fixed $\omega$, the boundary helices are invariant under ``screw" transformations which rotate the $xy$-plane by angle $\omega t$ whilst translating in the $z$ direction by $t$. As the screw transformations are a subgroup of Euclidean isometries (and also of the larger M\"obius group of $\R^3$), the gradient flow of the M\"obius energy starting at a helix preserves symmetries under the screw transformations (cf. p.42 of \cite{freedman1994mobius}). Therefore, $G_{\gamma_1,\gamma_2}$ is tangent to $\Sigma(\omega)$, and to calculate the entire M\"obius gradient vector fields along $\gamma_1$ and $\gamma_2$, it suffices to compute them at two particular points along the boundary curves and then apply screw transformations. The same symmetry rule also holds for computing the Plateau gradient vector fields along the helices, as the Plateau energy is invariant under Euclidean isometries.

Observe that 
\begin{align*}
    \dot{\gamma_1}(u) &= 
    \begin{bmatrix}
    -\omega A \sin(\omega u) \\
    \omega A \cos(\omega u) \\
    1
    \end{bmatrix},
\end{align*} and that $|\dot{\gamma_1}(u)| = \sqrt{\omega^2 A^2 + 1}$ for all $u$. We also have $|\dot{\gamma_2}(u)| = \sqrt{\omega^2 B^2 + 1}$ for all $v$. Furthermore,
\begin{align*}
    \Ddot{\gamma_1}(u) = \begin{bmatrix}
    -\omega^2 A \cos(\omega u) \\
    -\omega^2 A \sin(\omega u) \\
    0
    \end{bmatrix}.
\end{align*}

Next, for given surface parameters $s$ and $t$, the tangent plane to $\Sigma$ is given by 
\begin{align*}
    T\Sigma &= \text{span} \Biggl\{ \partial_s \begin{bmatrix}
    x \\
    y \\
    z
    \end{bmatrix}, \partial_t \begin{bmatrix}
    x \\ 
    y \\ 
    z 
    \end{bmatrix} \Biggr\} \\
    &= \text{span} \Biggl\{ \begin{bmatrix}
    \cos(\omega t) \\
    \sin(\omega t) \\ 
    0
    \end{bmatrix}, \begin{bmatrix}
    -\omega s \sin(\omega t) \\
    \omega s \cos(\omega t) \\
    1
    \end{bmatrix} \Biggr\}.
\end{align*}

So at $u = 0$, we have the following:
\begin{center}
    $\gamma_1(0) = \begin{bmatrix}
    A\\
    0\\
    0
    \end{bmatrix}, \dot{\gamma_1}(0) = \begin{bmatrix}
    0\\
    \omega A \\
    1
    \end{bmatrix}, \Ddot{\gamma_1}(0) = \begin{bmatrix}
    -\omega^2 A\\
    0\\
    0
    \end{bmatrix}$.
\end{center}

From this, we can see that $\textbf{N}_{\gamma_1(0)} = (\pm 1, 0, 0)$, depending on the sign of $A$. We can also see that $T_{\gamma_1(0)} \Sigma = \text{span} \{ (1, 0, 0), (0, \omega A, 1) \}$, and thus $\boldsymbol\nu = \frac{1}{\sqrt{\omega^2A^2 + 1}}(0, \omega A , 1)$. Hence, $\textbf{n} = (-1,0,0)$.

Next, observe
\begin{align*}
    P_{\dot{\gamma}_1(0)^\perp} \big(\gamma_2(v) - \gamma_1(0)\big) &= \big(\gamma_2(v) - \gamma_1(0)\big) - \langle \gamma_2(v) - \gamma_1(0), \dot{\gamma_1}(0) \rangle \frac{\dot{\gamma_1}(0)}{|\dot{\gamma_1}(0)|^2} \\
    &=  \begin{bmatrix}
    B \cos(\omega v) - A \\
    B \sin(\omega v) \\
    v
    \end{bmatrix} -  \frac{ \omega AB\sin(\omega v) + v}{\omega^2A^2 + 1} \begin{bmatrix}
    0\\
    \omega A \\
    1
    \end{bmatrix}\\
    &= \begin{bmatrix}
    B\cos(\omega v) - A\\
    \frac{B \sin(\omega v) - A \omega v}{\omega^2 A^2 + 1} \\
    v - \frac{v + \omega AB \sin(\omega v)}{\omega^2A^2 + 1}
    \end{bmatrix}.
\end{align*}
Finally, it is straightforward to see that $|\gamma_2(v) - \gamma_1(0)|^2 = A^2 - 2AB\cos(\omega v) + B^2 + v^2$. For now, we will make the assumption that $A < 0 < B$, which means $\textbf{N} = (1,0,0)$. Putting all of this together, the variational equation becomes the system:
\begin{align}
    2 \alpha \int_{-\infty}^\infty \left[ \frac{2 \left( B \cos(\omega v) - A \right)}{A^2 - 2AB\cos(\omega v) + B^2 + v^2} - 1 \right] \frac{\sqrt{\omega^2 B^2 + 1}}{A^2 - 2AB\cos(\omega v) + B^2 + v^2} dv &= \beta \label{gamma1var}\\
    \int_{-\infty}^\infty \frac{B \sin(\omega v) - \frac{v + \omega^2 A^2 B \sin(\omega v)}{\omega^2 A^2 + 1}}{(A^2 - 2AB\cos(\omega v) + B^2 + v^2)^2}dv &= 0 \nonumber\\
    \int_{-\infty}^\infty \frac{ v - \frac{\omega A B \sin(\omega v) + v}{\omega^2 A^2 + 1}}{\left( A^2 - 2AB\cos(\omega v) + B^2 + v^2 \right)^2} dv &= 0.\nonumber
\end{align}
The last two integrands are odd functions in $v$, which means the integrals are always going to be zero, so only equation \eqref{gamma1var} relevant to us. Through identical computations by taking $v = 0$, noting that in this case we have $\textbf{N}_{\gamma_2(0)} = (-1,0,0)$ and $\textbf{n} = (1, 0, 0)$, we see the first component of the variational equation at $\gamma_2(0)$ is
\begin{align}
     2 \alpha \int_{-\infty}^\infty \left[ \frac{2 \left( A \cos(\omega u) - B \right)}{A^2 - 2AB\cos(\omega u) + B^2 + u^2} + 1 \right] \frac{\sqrt{\omega^2 A^2 + 1}}{A^2 - 2AB\cos(\omega u) + B^2 + u^2} du &= -\beta. \label{gamma2var}
\end{align}
Relabelling the variable of integration and adding \eqref{gamma1var} and \eqref{gamma2var} yields
\begin{equation}
\label{screwvar}
    4 \alpha \int_{-\infty}^\infty \frac{(A + B)(\cos(\omega v) - 1)}{\left(A^2 - 2AB \cos(\omega v) + B^2 + v^2 \right)^2}dv = \beta \left( \frac{1}{\sqrt{\omega^2 B^2 + 1}} - \frac{1}{\sqrt{\omega^2 A^2 + 1}}\right).
\end{equation}
This single equation leaves us with a two parameter family of stationary helicoids controlled by the constants $\alpha$ and $\beta$. From direct inspection, it is clear that $A = -B$ is a solution, which we call the symmetric stationary helicoidal screw. It is straightforward to numerically search for other solutions of \eqref{screwvar}. For instance, setting $\alpha = 2, \beta = 1, A = -1, \omega = 2$, and solving for $B$ gives solutions $B = 1$ and $B \approx 6.15375$. The two helicoidal screws are pictured in \ref{stablescrews}. In the numerical searches we ran, we generally found that under most choices of parameters, the symmetric solution had a larger basin of attraction than the asymmetric solution. An analysis of the attraction properties of the solutions is yet to be done.
\begin{figure}
    \centering
    \begin{subfigure}{0.5\textwidth}
    \centering
    \includegraphics[width=4in]{asymmetrichelicoid.jpg}
    \caption{A stationary asymmetric helicoidal screw.}
    \end{subfigure}
    \begin{subfigure}{0.5\textwidth}
    \centering
    \includegraphics[width=1in]{symmetrichelicoid.jpg}
    \caption{A stationary symmetric helicoidal screw.}
    \end{subfigure}
    \caption{Two stationary helicoidal screws with identical parameters $A = -1, \omega = 2$, except $B \approx 6.15375$ in the figure on the left, whilst $B = 1$ in the figure on the right. In these examples, we set $\alpha = 2, \beta = 1$ }
    \label{stablescrews}
\end{figure}

The full description of this family, especially with respect to its singularities, is not fully known. When we tried to find solutions to the variational equation for helicoidal ribbons, derived below, we had difficulties finding solutions, and we suspected at first that no solutions existed. During our attempt to prove this lack of solutions, we had difficulty in bounding the negative contribution to the variational integral, and we later found that solutions do indeed exist, but only under comparatively strict conditions. Furthermore, the solutions we did manage to find have parameters which differ in orders of magnitude, which contributed to the difficulty in the numerical search.

\begin{theorem}
A stationary helicoidal ribbon must have high frequency (equivalently, low pitch), very small width in comparison to the frequency, and remain close to the axis. That is, the following conditions on the parameters must hold:
\begin{enumerate}
    \item $\omega > 1$
    \item $|B - A|^2 < C(\alpha,\beta) \omega$
    \item $|A + B| < 2$.
\end{enumerate}
\end{theorem}
\begin{remark}
    We only prove the case when $\alpha = \beta = 1$. In the general case, the bounds \eqref{ba4w} and \eqref{cosneg} are scaled by powers of $\alpha$ and $\beta$, though \eqref{tail} is unchanged. One may verify these bounds still sum to a positive number as required in the last step of the proof, but this only further complicates the algebra without fundamentally altering our reasoning. Our numerical search suggests the second condition could be considerably strengthened to the form $|B-A|^{k_1} < C \frac{\beta^{k_2}}{\alpha^{k_3}} \omega$, with the optimal exponents $k_i$ yet to be determined. Modifying the bound in \eqref{cosneg} is more difficult since we could get a family of rational functions in $\omega$ controlled by $\alpha$ and $\beta$, and so a numerical approximation does not rigorously justify a lower bound. When applying the M\"obius-Plateau energy to mainstream Euler-Plateau problems, it is likely necessary to vary the coefficients $\alpha$ and $\beta$, so understanding their precise scaling effects is imperative.
\end{remark}
\begin{proof}
Without loss of generality assume $0 < A < B$. We may also assume $\omega > 0$ because the cosine function is even. This is tantamount to fixing the chirality of the helicoids under consideration to being right-handed. Observe $\textbf{N}_{\gamma_1(0)} = (-1,0,0)$, so the $-1$ term in \eqref{gamma1var} corresponding to $-\textbf{N}$ becomes a $+1$ whilst \eqref{gamma2var} remains unchanged. Adding these two nontrivial variational equations at $\gamma_1(0)$ and $\gamma_2(0)$ yields
\begin{align}
\label{ribbonvar}
    4 \int_{-\infty}^\infty \frac{A^2 - A + B^2 - B + (A + B - 2AB)\cos(\omega v) + v^2}{\left(A^2 - 2AB \cos(\omega v) + B^2 + v^2 \right)^2}dv &= \left( \frac{1}{\sqrt{\omega^2 B^2 + 1}} - \frac{1}{\sqrt{\omega^2 A^2 + 1}}\right).
\end{align}
We will show that except in a very limited circumstance, the integrand on the lefthand side of \eqref{ribbonvar} is always positive. When the integrand can take negative values, we will then show that unless all of the conditions listed are met, then the integral is positive. The righthand side of \eqref{ribbonvar} is negative, as $B > A$, so we will get our desired result.

The denominator is obviously positive. As for the numerator, we break down into cases. Suppose $A + B  -2AB \leq 0$. Then
\begin{align*}
    A^2 - A + B^2 - B + (A + B - 2AB)\cos(\omega v) + v^2 &\geq A^2 - A + B^2 + A + B - 2AB + v^2\\
    &= (B - A)^2 + v^2 > 0. 
\end{align*}
For the remainder of the proof, assume $A + B - 2AB > 0$ and we will break down into further cases. Assume $A + B \geq 2$. Then
\begin{align*}
  A^2 - A + B^2 - B + (A + B - 2AB)\cos(\omega v) + v^2 &\geq A^2 - A + B^2 - B -(A + B - 2AB) + v^2\\
    &= (A + B)(A + B - 2) + v^2 > 0. 
\end{align*}
Next, assume $ A + B < 2$ with $\omega \leq 1$. From the Taylor formula, $\cos(\omega v) \geq 1 - \frac{\omega^2v^2}{2} \geq 1 - \frac{v^2}{2}$. Now see that
\begin{align*}
    A^2 - A + B^2 - B + (A + B - 2AB)\cos(\omega v) + v^2 &\geq A^2 - A + B^2 - B + (A + B - 2AB)\left(1 - \frac{v^2}{2}\right) + v^2 \\
    &= (B - A)^2 + \frac{v^2}{2}(2AB - A - B + 2) \\
    &> \frac{v^2}{2}(2AB - A - B + 2)\\
    &\geq \frac{v^2}{2}(2AB) \geq 0.
\end{align*}
So in all of the cases we have considered for $A, B$, and $\omega$ so far, the integrand in \eqref{ribbonvar} is positive and so the variational equation will have no solutions.

\begin{figure}
\begin{center}
\includegraphics[width=4in]{ribleftint.jpg}
\caption{A graph of the integrand in \eqref{ribbonvar} with $A = 0.1, B = 1,$ and $\omega = 10$, as a function of $v$.}
\label{ribleftgraph}
\end{center}
\end{figure}

Now, assume $A + B < 2$ with $\omega > 1$. It is only in this scenario that the numerator could take negative values and possibly lead to the integral in \eqref{ribbonvar} being negative. For instance, when $A = 0.1, B = 1, \omega = 10$, the integrand takes negative values as shown in Figure~\ref{ribleftgraph}.

As the integrand is an even function in $v$, it suffices to prove 
\begin{align*}
    \int_0^\infty \frac{A^2 - A + B^2 - B + (A + B - 2AB)\cos(\omega v) + v^2}{(A^2 - 2AB\cos(\omega v) + B^2 + v^2)^2}dv > 0,
\end{align*}
when the second condition in our theorem is negated. Our method will be to overestimate the magnitude of the contribution of the negative part of the integrand whilst underestimating the contribution of the positive part of the integrand, and show that the positive contribution still outweighs the negative contribution. To estimate the negative contribution, we integrate the quadratic Maclaurin series over $[0,\frac{1}{4}]$, and then compute a lower Riemann sum over  $\{\cos(\omega v) < 0\} \cap [0,1]$. When $(B-A)^2 > c\omega$, where $c$ is some constant independent of the parameters, we get \eqref{ba4w} and \eqref{cosneg}. The computation is detailed in an appendix. 


\iffalse
Next, we consider the positive contributions of the integrand. As we saw, when $v \geq \frac{1}{4} >$, $\cos(\omega v) \geq 0$ implies the integrand is positive. The intervals where $\cos(\omega v) \geq 0$ are $\left[0, \frac{\pi}{2\omega}\right]$ and $\left[\frac{n \pi}{\omega} - \frac{\pi}{2\omega}, \frac{n\pi}{\omega} + \frac{\pi}{2\omega}\right]$, with $n$ a positive even integer. For this estimate, we will only consider intervals bounded above by $1$, and consider the tail of the integral separately. Furthermore, we cannot consider the positive contributions the integrand in any interval overlapping with the limits of integration in \eqref{ba4w}, as this would result in overcounting the positive part's contribution. The total number of intervals under consideration is the number of positive even integers $n$ such that $\left(\frac{n\pi}{\omega} - \frac{\pi}{2\omega}\right) \geq \frac{1}{2}$ and $\left( \frac{n\pi}{\omega} + \frac{\pi}{2\omega} \right) < 1$. Equivalently, this is the number of positive even $n$ such that $\frac{\omega}{4\pi} + \frac{\pi}{2} < n < \frac{1}{2} + \frac{\omega}{\pi}$. Therefore, there are at least $\frac{1}{2} \left[ \left( \frac{\omega}{\pi} - \frac{1}{2} \right) - \left( \frac{\omega}{4\pi} \right) \right] = \frac{3\omega}{8\pi}$ intervals with positive contribution before the tail.

In the region of our estimate, we are assuming $v \leq 1$. To bound the denominator from above, we square both sides of the inequality
\begin{align*}
    A^2 -2AB\cos(\omega v) + B^2 + v^2 &\leq (B - A)^2 + 1 \\
    \leq 4 + 1 = 5.
\end{align*},
where we have used the fact that
\begin{align*}
    \sup_{\substack{A + B < 2 \\ 0 < A < B}} (B - A)^2 = 4.
\end{align*}
Next, on the $(2n)^{\text{th}}$ interval, the numerator is bounded below by 
\begin{align*}
    A^2 - A + B^2 - B + (A + B - 2AB)\cos(\omega v) + \left( \frac{2n\pi}{\omega} - \frac{\pi}{2\omega} \right)^2 &\leq A^2 - A + B^2 - B + \left( \frac{2n\pi}{\omega} - \frac{\pi}{2\omega} \right)^2 \\
    & \leq -\frac{1}{2} + \left( \frac{2n\pi}{\omega} - \frac{\pi}{2\omega} \right)^2.
\end{align*}
The last inequality uses \eqref{infminusonehalf}. Now to estimate the positive contribution of the integral in the region between $v = \frac{1}{4}$ and $v = 1$, we have the Riemann sum
\begin{align}
    \left(\frac{\pi}{\omega}\right) \sum\limits_{n = 0}^{\lceil \frac{3\omega}{8\pi} \rceil} \frac{ - \frac{1}{2} + \left( \frac{2n\pi}{\omega} - \frac{\pi}{2\omega} \right)^2}{25} &= \left(\frac{\pi}{\omega} \right) \left(\frac{1}{25}\right)\sum\limits_{n = 0}^{\lceil \frac{3\omega}{8\pi} \rceil} \left[-\frac{1}{2} +  \frac{4\pi^2}{\omega^2}n^2 - \frac{2 \pi^2}{\omega^2}n  + \frac{\pi^2}{4\omega^2} \right] \nonumber \\
    &\geq \left(\frac{\pi}{\omega} \right) \left(\frac{1}{25}\right) \left( \frac{3 \omega}{8\pi} \right)\left( \frac{\pi^2}{4\omega^2} - \frac{1}{2} \right) + \left(\frac{\pi}{\omega} \right) \left(\frac{1}{25}\right) \sum\limits_{n = 0}^{\lceil \frac{3\omega}{8\pi} \rceil}\left[ \frac{4\pi^2}{\omega^2}n^2 - \frac{2 \pi^2}{\omega^2}n \right] \nonumber \\
    &\geq \left(\frac{1}{25}\right) \left( \frac{3 }{8} \right)\left( \frac{\pi^2}{4\omega^2} - \frac{1}{2} \right) \nonumber\\
    &\hspace{0.5in}+ \left(\frac{\pi}{\omega} \right) \left(\frac{1}{25}\right) \Biggl[ \frac{1}{6} \left(\frac{4 \pi^2}{\omega^2} \right) \left( \frac{3 \omega}{8\pi}\right)\left(\frac{3 \omega}{8\pi} + 1 \right)\left(\frac{3\omega}{4\pi} + 1 \right) \nonumber \\
    &\hspace{0.5in}+ \frac{1}{2} \left( -\frac{2\pi^2}{\omega^2} \right)\left( \frac{3 \omega}{8\pi}\right)\left(\frac{3 \omega}{8\pi} + 1 \right) \Biggr] \nonumber \\
    &= \frac{\pi^2}{800 \omega^2} - \frac{9\pi}{1600\omega} + \frac{3}{640}. \label{finitepos}
\end{align}
\fi



As we saw, for $v \geq 1$, the integrand is strictly positive. So consider the contribution of the tail
\begin{align*}
    \int_1^\infty \frac{A^2 - A + B^2 - B + (A + B - 2AB)\cos(\omega v) + v^2}{(A^2 - 2AB\cos(\omega v) + B^2 + v^2)^2}dv &> 0.
\end{align*}
We see that $A^2 - 2AB\cos(\omega v) + B^2 + v^2 \geq (A + B)^2 + v^2$. Combining this with \eqref{supab4}, we can conclude that the denominator is bounded above by $(4 + v^2)^2$. Likewise, we again observe by \eqref{numbound} that the numerator is bounded below by $(A + B)(A + B - 2) + v^2$. Therefore, the numerator is bounded below by $v^2 - 1$. Putting all this together, we have
\begin{align}
    \int_1^\infty \frac{A^2 - A + B^2 - B + (A + B - 2AB)\cos(\omega v) + v^2}{(A^2 - 2AB\cos(\omega v) + B^2 + v^2)^2}dv &\geq \int_1^\infty \frac{v^2 - 1}{(4 + v^2)^2}dv \nonumber \\
    &= \frac{1}{32} \left(4 + 3\pi - 6\text{arccot}(2) \right) \nonumber\\
    &\geq \frac{3}{10} \label{tail}.
\end{align}
By adding our bounds from \eqref{ba4w},\eqref{cosneg}, and \eqref{tail}, we can conclude the integral is positive.
\end{proof}

\begin{figure}
    \centering
    \includegraphics[width=3in]{ribboncontourplot.jpg}
    \caption{Contours in the $AB$-plane for \eqref{ribbonvar} and \eqref{ribbondiff}, with $\alpha = \beta = 1, \omega = 10$, and approximate region of integration $[-10000,10000]$. The intersection of the contour curves is $(A,B) \approx (0.810515,0.818991)$ which is in the valid parameter space $\{(A,B): 0 < A < B, A + B < 2 \}$.}
    \label{ribboncontours}
\end{figure}

Negating the second condition was crucial in our proof, as we otherwise would not be able to obtain the bound in \eqref{ba4w}, as the coefficient $-\frac{1}{(B-A)^4}$ tends to $-\infty$ as $(B-A) \to 0^+$, which makes the bound useless in limiting the contribution of the negative parts of the integrand. We also used this assumption in \eqref{cosnegden} in order to force the Riemann sum approximation to be of order $O(\omega^{-4})$. Were we to na\"ively the use the inequality $A^2 + B^2 + v^2 \geq 0 + \left(\frac{\pi}{2\omega}\right)^2$, our Riemann sum approximation would be of order $O(\omega^4)$ with a leading negative coefficient, which tends to $-\infty$ as $\omega \to \infty$, again preventing a bound for the negative contribution.

With the restrictions on the parameters in mind, we found approximate numerical solutions to the variational equations for stationary helicoidal ribbons. Our analysis so far has only dealt with the sum of the variational equations for $\gamma_1$ and $\gamma_2$, so to solve the full variational system, we included the difference of the two variational equations, which is
\begin{align}
    4 \alpha \int_{-\infty}^\infty \frac{(B - A) \cos^2\left( \frac{\omega v}{2} \right)}{\left(A^2 - 2AB\cos(\omega v) + B^2 + v^2 \right)^2}dv &= \beta \left( \frac{1}{\sqrt{\omega^2 A^2 + 1}} + \frac{1}{\sqrt{\omega^2 B^2 + 1}} \right).
    \label{ribbondiff}
\end{align}
Both sides of this equation are clearly positive for $B > A$, and hence there are no further obvious restrictions on the parameters for $A$ and $B$, which is why we opted to study \eqref{ribbonvar} in order to characterize the stationary ribbons.

In our numerical search, we evaluated the integrals corresponding to \eqref{ribbonvar} and \eqref{ribbondiff} on the finite interval $[-10000,10000]$ via a Gaussian quadrature with precision set to $10^{-6}$. With $\alpha = \beta = 1$ and $\omega = 10$, we obtained the contour plot depicted in \ref{ribboncontours}. The intersection of the contour lines for \eqref{ribbonvar} and \eqref{ribbondiff} was found to be $(A,B) \approx (0.810515,0.818991)$, which corresponds to a width of $B - A \approx 0.008476$. The effects of this intersection point under bifurcations of $\alpha, \beta$, and $\omega$ is yet to be investigated.

\iffalse
As we saw in the proof, for $|v| > 1$, the integrand in \eqref{ribbonvar} is positive and bounded above by $\frac{4 + v^2}{v^4}$. Likewise the integrand in \eqref{ribbondiff} is also positive and bounded above by $\frac{2}{v^4}$ everywhere. So by integrating these bounds on the region $\{|v| \geq 10000\}$, we get error upper bounds of $0.0002$ and $10^{-12}$ respectively. After adding these error bounds of differing orders, we get an upper bound on the maximum error of $\vep < 0.0003$. 

Now, by plotting contours of \eqref{ribbonvar} and \eqref{ribbondiff} using our integral approximations, with fixed $\alpha, \beta > 0$ and $\omega > 1$, we can get a numerical solution by finding their intersection. By verifying that perturbing this solution by its maximum error bound still places it in the region of valid parameters of $0 < A < B$ and $A + B < 2$, we will verify the existence of a stationary helicoidal ribbon.

\fi

---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-017-53-twisted-reidemeister-torsion-at-the-holonomy
section_title: "Twisted Reidemeister torsion at the holonomy representation."
section_number: 5.3
pages: 26-28
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.911
latex_coverage_ratio: 1.0
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
\label{subsection:results_holonomy}

In this section, we consider the non--abelian Reidemeister torsion for hyperbolic twist knots at holonomy representations.
Formulas of the non--abelian Reidemeister torsion associated to twist knots are complicated.
But we see here that formulas for the non--abelian Reidemeister torsion at holonomy representations are simpler.

Every twist knots except the trefoil knot are hyperbolic. 
It is well known that 
an exterior of a hyperbolic knot admits at most a complete hyperbolic structure and 
this hyperbolic structure determines the holonomy representation of the knot group (see Section~\ref{sechyp}). With Fact~\ref{holonomy} in mind, we know that such lifts are $\lambda$-regular representations.



\begin{remark}
If we substitute $s=1$ into Riley's polynomial $\phi_{J(2, 2m)} (s, u)$ given in Eq.~(\ref{eqn:Riley_poly}), then
\[
\phi_{J(2, 2m)} (1, u)= (1-u) t_m - t_{m-1} = 
(1-u) \frac{\xi_{+}^m - \xi_{-}^m}{\xi_{+} - \xi_{-}} - \frac{\xi_{+}^{m-1}-\xi_{-}^{m-1}}{\xi_{+} - \xi_{-}}.
\] 
\end{remark}









The $\SL$-representations which lifts the holonomy representation correspond 
to roots of Riley's equation $\phi_{J(2, 2m)}(1,u)=0$. We let $\rho_u$ denote such representations.

We are now ready to give a formula for the non--abelian Reidemeister torsion of $J(2,2m)$ at the holonomy representation in terms of $u$, which is an algebraic number, defined to be the root of  a computable algebraic equation. 


\begin{theorem}\label{R-torsionTK}
Let $m>0$ and $u$ denote one of the two complex conjugate roots of Riley's equation $\phi_{J(2, 2m)}(1,u) = 0$ (resp. $\phi_{J(2, -2m)}(1,u) = 0$) corresponding to holonomy representations, 
then 
\begin{enumerate}
\item the non--abelian Reidemeister torsion ${\mathbb T}^{J(2, 2m)}_{\lambda}(\rho_u)$ satisfies the following
{formula}:
\begin{align*}
{\mathbb T}^{J(2, 2m)}_{\lambda}(\rho_u)
&= 
  \frac{-\tau_0}{u^2+4}
  \left[
    \left(4+m(u^2-4u+8)\right) t_m (\xi_{+}^m + \xi_{-}^m) 
    \right. \nonumber \\
& \quad + 
    \left(t_m(\xi_{+}^{m-1}+\xi_{-}^{m-1})-1\right)(u^2-4)m \nonumber\\
& \left.\quad+
    (-5u^2-8u+4)t_m^2
  \right],
\end{align*}
\item similarly
the Reidemeister torsion ${\mathbb T}^{J(2, -2m)}_{\lambda}(\rho_u)$ satisfies the following
formula:
\begin{align*}
{\mathbb T}^{J(2, -2m)}_{\lambda}(\rho_u)
&= 
  \frac{-\tau_0}{u^2+4}
  \left[
    \left(-4+m(u^2-4u+8)\right) t_m (\xi_{+}^m + \xi_{-}^m) 
    \right. \nonumber \\
& \quad + 
    \left(t_m(\xi_{+}^{m+1}+\xi_{-}^{m+1}) +1\right)(u^2-4)m \nonumber\\
& \left.\quad+
    (-5u^2-8u+4)t_m^2
 \right].
\end{align*}
\end{enumerate}
\end{theorem}

\begin{remark}
Combining results of Theorem~\ref{R-torsionTK} with Eq.~(\ref{cuspshape}), the non--abelian Reidemeister torsion of a (hyperbolic) twist knot at the holonomy is expressed in terms of the cusp shape of the knot.
\end{remark}


\begin{proof}
First we make the computations in the case of $J(2, 2m)$, where $m > 0$. If we substitute $s = 1$ in Eq.~(\ref{Tlim}), then we obtain:
\begin{align}
{\mathbb T}^{J(2, 2m)}_{\lambda} (\rho)
&=
-\tau_0
\lim_{t \to 1}
\frac{\det(\I + Z_m)}{(t-1)^4} \nonumber \\
&=
\frac{-\tau_0}{24} \left.\frac{d^4}{dt^4}\det(\I+Z_m)\right|_{t=1}. \nonumber
\end{align}
Next, using the splitting of $\det(\I+Z_m)$ given in Eq.~(\ref{split}), we get:
\begin{equation}\label{diff_hol}
{\mathbb T}^{J(2, 2m)}_{\lambda} (\rho)
 = \frac{-\tau_0}{24} \left.\frac{d^4}{dt^4}\left[ 1^{} + \sigma_1(Z_m) + \sigma_2(Z_m) + \sigma_3(Z_m) \right]\right|_{t=1}. 
 \end{equation}
It follows from Eq.~(\ref{sigma_3}) that $(t-1)^6$ divides $\sigma_3(Z_m)$ in the case of $s = 1$.
Hence the term $\left.\frac{d^4}{dt^4} \sigma_3(Z_m)\right|_{t=1}$ in Eq.~(\ref{diff_hol}) vanishes.
By degrees of $t$ in $\sigma_1(Z_m)$ and $\sigma_2(Z_m)$, 
we obtain the following equation from direct computations of the above differentials:
\begin{align}
{\mathbb T}^{J(2, 2m)}_{\lambda} (\rho)
&=
-\tau_0[
\trace(X^{-1}S_m(W^{-1}))+5\sigma_2(X^{-1}S_m(W^{-1})) \label{tor_hol_matrix_pos}\\
& \quad
-\trace(X^{-1}S_m(W^{-1})) \trace((\I+X^{-1}Y)S_m(W^{-1})) \nonumber \\
&\quad
+\trace(X^{-1}S_m(W^{-1})(\I+X^{-1}Y)S_m(W^{-1})) ] \nonumber.
\end{align}
Note that $\xi_{+}  + \xi_{-} = u^2+2$ and $(\xi_{+} - \xi_{-})^2 = u^2(u^2+4)$.
By Claims \ref{trace_X^{-1}S_m}, \ref{sigma_2_result} \& \ref{trAB-trAtrB} 
we have

\begin{align*}
\trace(X^{-1}S_m(W^{-1})) 
&=
\frac{1}{u^2+4}
\left[
4(\xi_{+}^m + \xi_{-}^m)t_m - (u^2-4)m
\right] \\
\sigma_2(X^{-1}S_m(W^{-1})) 
&=
\frac{1}{u^2+4}
\left[
4m(\xi_{+}^m + \xi_{-}^m)t_m - (u^2 - 4)t^2_m
\right]
\end{align*}
and 
\begin{align*}
\lefteqn{
-\trace(X^{-1}S_m(W^{-1}))\trace((\I+X^{-1}Y)S_m(W^{-1}))
+ \trace(X^{-1}S_m(W^{-1})(\I+X^{-1}Y)S_m(W^{-1}))
}
& \\
&=
-\frac{1}{u^2+4}
\left[
8(u+2)t^2_m 
-m(u+2)(u-6)(\xi_{+}^m + \xi_{-}^m)t_m
-m(u^2-4)(\xi_{+}^{m-1}+\xi_{-}^{m-1})t_m
\right].
\end{align*}
If we substitute these results into Eq.~(\ref{tor_hol_matrix_pos}), then
we obtain the wanted formula for $J(2, 2m)$.



Similarly, in the case of twist knots $J(2, -2m)$, $m>0$, from computations of differentials we have 
\begin{align}
{\mathbb T}^{J(2, -2m)}_{\lambda}(\rho_u)
&=
-\tau_0[
-\trace(X^{-1}S_m(W)W)+5\sigma_2(X^{-1}S_m(W)W) \label{tor_hol_matrix_neg}\\
& \quad
-\trace(X^{-1}S_m(W)W) \trace((\I+X^{-1}Y)S_m(W)W) \nonumber \\
&\quad
+\trace(X^{-1}S_m(W)W(\I+X^{-1}Y)S_m(W)W) ] \nonumber.
\end{align}
It follows from Claims \ref{trace_X^{-1}S_m}, \ref{sigma_2_result} \& \ref{trAB-trAtrB} that

\begin{align*}
\trace(X^{-1}S_m(W)W)
&=
\frac{1}{u^2+4}
\left[
4(\xi_{+}^m + \xi_{-}^m)t_m - (u^2-4)m
\right] \\
\sigma_2(X^{-1}S_m(W)W) 
&=
\frac{1}{u^2+4}
\left[
4m(\xi_{+}^m + \xi_{-}^m)t_m - (u^2 - 4)t^2_m
\right]
\end{align*}
and 
\begin{align*}
\lefteqn{
-\trace(X^{-1}S_m(W)W)\trace((\I+X^{-1}Y)S_m(W)W)
+\trace(X^{-1}S_m(W)W(\I+X^{-1}YS_m(W)W))
}& \\
&=
-\frac{1}{u^2+4}
\left[
8(u+2)t^2_m 
-m(u+2)(u-6)(\xi_{+}^m + \xi_{-}^m)t_m
-m(u^2-4)(\xi_{+}^{m+1} + \xi_{-}^{m+1})t_m
\right].
\end{align*}
If we substitute these results into Eq. (\ref{tor_hol_matrix_neg}) , then
we obtain the wanted formula for $J(2, -2m)$.
\end{proof}

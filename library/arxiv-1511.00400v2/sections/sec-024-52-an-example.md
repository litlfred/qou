---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-024-52-an-example
section_title: "An example"
section_number: 5.2
pages: 41-44
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.963
---
\label{subsection:eight}
Let me use Proposition~\ref{prop:bundleadj} to compute $\T_{M,\gamma}$ for the figure eight knot
for $\PSL_2(\CC)$ and $\PSL_3(\CC)$. 
 For  $\PSL_2(\CC)$ this is done in \cite{Memoirs}, but I recall it here for completeness.
 
 
Let $\Gamma=\pi_1 M$ denote the fundamental group of the figure eight knot 
exterior. The presentation
$$
 \Gamma=\langle   a,b, m \mid m\, a\, m^{-1}= a\, b,\,  m\, b\, m^{-1}= b\, a\, 
b
 \rangle
$$
corresponds to the fact  that it is fibered over the circle, 
with fibre a punctured torus, whose fundamental group is the free group 
$F_2=\langle a, b\mid\rangle$. The element $m$ is also a meridian curve of the knot.
The monodromy $\phi\colon F_2\to F_2$ satisfies 
$$\phi(a)=a\, b \qquad \textrm{ and } \qquad 
\phi(b)=b\, a\, b.
$$

Since $F_ 2$ is the derived subgroup of $\Gamma$, every representation of $\Gamma$ in $\PSL_{n+1}(\CC)$
restricts to a representation of $F_2$ in $\SL_{n+1}(\CC) $  that is fixed by the monodromy $\phi^*$.
The set of fixed characters is denoted by 
$$
X(F_2,\SL_{n+1}(\CC))^{\phi^*}.
$$
The following lemma is  proved in \cite{Memoirs, HMP15} (using that $F_2$ is the commutator of $\Gamma$):

\begin{lemma}
 For $n=1,2$, the restriction map induces an isomorphism
 $$
 \overline{X_{irr}(\Gamma,\PSL_{n+1}(\CC))} \cong 
\overline{X_{irr}(F_2,\SL_{n+1}(\CC))^{\phi^*}},
 $$
 where the subindex $_{irr}$ stands for irreducible characters.
\end{lemma}



\subsubsection{Computations for $X(M^3,\PSL_{2}(\CC))$ }
 
 By Fricke-Klein theorem, the variety of characters $X(F^2,\SL_2(\CC))$ is isomorphic to $\CC^3$. More precisely, defining
 $$
 \begin{array}{ll}
     & \alpha_1(\rho)=\tr(\rho(a)) \, ,\\
     & \alpha_2(\rho)=\tr(\rho(b)) \, , \\
     & \alpha_3(\rho)=\tr(\rho(a\,b))  \, .
 \end{array}
$$ 
Fricke-Klein theorem asserts that  $(\alpha_1,\alpha_2,\alpha_3)$ are global coordinates of $X(F^2,\SL_2(\CC))$.
Using the relations of traces, $\forall  A,B\in\SL_2(\CC)$:
\[
 \begin{array}{ll}
\tr(A^{-1})&=  \tr(A),   \\
\tr(A B)&= \tr(A B^{-1})- \tr(A)\tr(B),
\end{array}
\]
we may deduce:
$$
 \begin{array}{ll}
       \phi^*(\alpha_1)&=\alpha_3 \, ,\\
       \phi^*(\alpha_2)&=\alpha_2 \alpha_3-\alpha_1  \, ,\\
      \phi^*(\alpha_3)&=\alpha_3^2 \alpha_2-\alpha_1 \alpha_3-\alpha_2  \, .
  \end{array}
$$
Thus $  \phi^*(\alpha_i)=\alpha_i$ is equivalent to 
$$
\alpha_3=\alpha_1,\qquad \alpha_1+\alpha_2=\alpha_1\alpha_2 \, .
$$
Then, the torsion polynomial is
\begin{equation}
 \label{eqn:tor82t}
{\det ( d \phi_* - t \operatorname{Id})}= (t-1)(t^2+(1-2 \alpha_1 \alpha_2) t+1).
 \end{equation}
Removing the factor $(t-1)$ and evaluation at $t=1$ yields
\begin{equation}
 \label{eqn:tor82}
\T_{M,l}= 3-2\alpha_1\alpha_2 = 3-2\alpha_1-2\alpha_2
 \end{equation}
Using that the trace of the longitude $l=[a,b]$ satisfies  
$\theta_l=\alpha_1^2+\alpha_2^2-\alpha_1-\alpha_2-2$
\cite{Memoirs},
we get
$\T_{M,l}^2=17+4\theta_l$. If $\theta_m$ denotes the trace of the meridian,
the distinguished component $X_0(\Gamma,\SL_2(\CC))$ is the curve
\begin{equation}
 \label{eqn:X0fig8}
\alpha_1^2+\alpha_1-1= \theta_m ^2\,(\alpha_1-1). 
\end{equation}
(Let me emphasize that $\theta_l$  and $\theta_m$ denote traces and not  
angles,
I made this choice because $\tau$ is already used for torsion.)
To get the variety $\PSL_2(\CC)$ characters instead of $\SL_2(\CC)$ just replace $\theta_m^2$ by a new variable.
From \eqref{eqn:X0fig8} and $x_1+x_2=x_1x_2$ we deduce:
\begin{equation}
 \label{eqn:x1+x2}
\alpha_1+\alpha_2= \theta_m^2-1  \qquad \textrm{ and } 
\qquad \alpha_1-\alpha_2= \pm\sqrt{(\theta_m ^2-5) (\theta_m-1)} \, .
\end{equation}
Thus 
\begin{equation}
 \label{eqn:T2l}
 \T_{M,l}=  \TT_{M,l}^2= 5-2\theta^2_m.
\end{equation}
Proposition~\ref{prop:change}  can be worked out \cite{Memoirs} to yield:
\begin{equation}
  \label{eqn:T2m}
\T_{M,m}=   \TT_{M,m}^2= \pm \frac{\alpha_1-\alpha_2}{2}=\pm \left( \alpha_1+\frac{1-\theta_m^2}{2} \right)=\pm \frac{1}{2}
\sqrt{(\theta_m^2-5)(\theta_m^2-1)}.
\end{equation}


\subsubsection{Computations for $X(M^3,\PSL_{3}(\CC))$ }

By a theorem of Lawton \cite{Lawton0} and Will \cite{Will}:
$X(F_2,\SL_3(\CC))$
is a double branched covering of $\CC^8$ with coordinates
 $$
 \begin{array}{ll}
     & \beta_1(\rho)=\tr(\rho(a))  \\
     & \beta_2(\rho)=\tr(\rho(a^{-1}))  \\
     & \beta_3(\rho)=\tr(\rho(b))  \\
     & \beta_4(\rho)=\tr(\rho(b^{-1}))  \\
     & \beta_5(\rho)=\tr(\rho(a\,b))  \\
     & \beta_6(\rho)=\tr(\rho(b^{-1}a^{-1}))  \\
     & \beta_7(\rho)=\tr(\rho(a^{-1}b))  \\
     & \beta_8(\rho)=\tr(\rho(a\,b^{-1}))  
 \end{array}
$$
and the  trace of  $l= [a,b]$ and its inverse, $\vartheta_{l^{\pm 1}}$, are a degree
two extension of the coordinates $\beta_1,\ldots,\beta_8$, and 
 $\vartheta_{l }$ and  $\vartheta_{l^{- 1}}$ are Galois conjugate.
 
As $\phi(l)=l$, we may work in $\CC^8$.
Following \cite{HMP15}, $\phi^*$ can be computed as
$$
 \begin{array}{ll}
   &  \phi^*(\beta_1)= \beta_5 \\
   &  \phi^*(\beta_2)= \beta_{{6}} \\
   &  \phi^*(\beta_3)=  -\beta_{{1}}\beta_{{4}}+\beta_{{3}}\beta_{{5}}+\beta_{{8}}          \\
   &  \phi^*(\beta_4)=  -\beta_{{2}}\beta_{{3}}+\beta_{{4}}\beta_{{6}}+\beta_{{7}}          \\
   &  \phi^*(\beta_5)=  -\beta_{{1}}\beta_{{4}}\beta_{{5}}+\beta_{{3}}{\beta_{{5}}}^{2}-\beta_{{3}}\beta_{{6}}+\beta_{{5}}\beta_{{8}}+\beta_{{2}}          \\
   &  \phi^*(\beta_6)=  -\beta_{{2}}\beta_{{3}}\beta_{{6}}+\beta_{{4}}{\beta_{{6}}}^{2}-\beta_{{4}}\beta_{{5}}+\beta_{{6}}\beta_{{7}}+\beta_{{1}}          \\
   &  \phi^*(\beta_7)=  \beta_{{3}}          \\
   &  \phi^*(\beta_8)=  \beta_{{4}}.
 \end{array}
$$
Now, setting $\beta_i=\phi^*(\beta_i)$, we get rid of four variables (we are left with 
$\beta_1$, $\beta_2$, $\beta_3$, and $\beta_4$), and we deduce that 
$X(F^2,\SL_3(\CC))^{\phi^*}$ has three components:
\begin{enumerate}[(a)]
 \item $V_0$, with equations  $\beta_1=\beta_2$, $\beta_3=\beta_4$.
 \item $V_1$, with equations $\beta_1=\beta_2=1$,
 \item $V_2$, with equations $\beta_3=\beta_4=1$.
\end{enumerate}
The component $V_0$ is the restriction of the distinguished component
$X_0(M^3,\PSL_{3}(\CC) )$. On this component,
the torsion polynomial is 
\begin{multline}
{\det ( d \phi_* - t \operatorname{Id})} =
{(t-1)^2} \left( t^2 + (2-\beta_{{1}}\beta_{{3}}) t +1 \right)  \\ \times
 \left( 
 t^4 + (  -\beta_{{1}}\beta_{{3}}-2\,\beta_{{1}}-2\,\beta_{{3}} ) t^3  +  
 ( 6\,\beta_{{1}}\beta_{{3}}+2  ) t^2+ (  -\beta_{{1}}\beta_{{3}}-2\,\beta_{{1}}-2\,\beta_{{3}} ) t + 1
\right) \, .
\end{multline}
After getting rid of $(t-1)^2$ and evaluating at $t=1$, we get
\begin{equation}
\label{eqn:TMl}
\T_{M,l}=( 4-\beta_1\beta_3) 4(1-\beta_1)(1-\beta_3) \, .
\end{equation}

Next Corollary~\ref{cor:difrentdims} is used to compute $\TT^4_{M,l}$.
The relation between traces in $\SL_2(\CC)$ and their image in $\SL_3(\CC)$
via $\operatorname{Sym}$ yields
$$
\begin{array}{l}
\beta_1= \beta_2 =\alpha_1^2-1\, ,\\
\beta_3=\beta_4  =\alpha_2^2-1 \, .
\end{array}
$$
Using these identities in \eqref{eqn:TMl} we get
$$
\T_{M,l}\circ\operatorname{Sym}= (3-2\alpha_1\alpha_2) 4 (2-\alpha_1^2)(2-\alpha_2^2).
$$
Thus by applying Corollary~\ref{cor:difrentdims} and \eqref{eqn:tor82}, one gets
\begin{equation}
 \label{eqn:t84}
 \TT^4_{M,l}= 4 (2-\alpha_1^2)(2-\alpha_2^2)=8(1-\alpha_1\alpha_2)=8(2-\theta_m^2).
\end{equation}




\begin{appendices}

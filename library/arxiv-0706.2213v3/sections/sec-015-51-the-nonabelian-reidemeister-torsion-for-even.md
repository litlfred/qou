---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-015-51-the-nonabelian-reidemeister-torsion-for-even
section_title: "The non–abelian Reidemeister torsion for even twist knots"
section_number: 5.1
pages: 17-25
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.984
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
We calculate the non--abelian Reidemeister torsion for  even twist knots $J(2, 2m)$ where $m$ is an integer.


\subsubsection{Preliminaries}
Following Section \ref{ReviewCharK} and using Riley's method, we can parametrize a non--abelian $\SL$-representation $\rho$ by two parameters $u$ and $s$  as follows:
\[
\rho(x) = 
\left(
\begin{array}{cc}
\sqrt{s} & 1/\sqrt{s} \\
0 & 1/\sqrt{s}
\end{array}
\right),\,
\rho(y) = 
\left(
\begin{array}{cc}
\sqrt{s} & 0 \\
-\sqrt{s} u & 1/\sqrt{s}
\end{array}
\right),
\]
where $s$ and $u$ satisfy Riley's equation $\phi_{J(2, 2m)}(s, u) = 0$. Besides, the Riley polynomial for twist knots is such that: 
\begin{equation}\label{eqn:Riley_poly}
\phi_{J(2, 2m)} (s,u)
=
\frac{(s+s^{-1}-1-u)(\xi_{+}^m - \xi_{-}^m) -(\xi_{+}^{m-1} - \xi_{-}^{m-1})}{\xi_{+} - \xi_{-}},
\end{equation}
where $\xi_{\pm}$ are the \emph{eigenvalues}  of the matrix $\rho(w) = \rho([y, x^{-1}])$ given by 
\begin{equation}\label{ev}
\xi_{\pm}   = \frac{1}{2} \left[ {u^2+(2-s-s^{-1})u+2 \pm \sqrt{(u^2+(2-s-s^{-1})u+4)(u^2+(2-s-s^{-1})u)}}\right].
\end{equation}










\subsubsection{Statement of the result}
\label{statement}

\begin{notation*}
Let $\alpha_1$, $\alpha_2$, $\beta_1$, $\beta_2$, $c$ and  $t_m$ be as follows:








\begin{itemize}
\item[] $c = c(s,u) = u+1-s^{-1}$; 
\item[] $\alpha_1 = (\xi_{-} - 1)(\xi_{+} + s) + (s-1)^2 u-su^2$; 
\item[] $\alpha_2 =  (1-su-\xi_{+})\left(1+ (\xi_{+} - s)/c\right)$; 
\item[] $\beta_1  = (\xi_{+}-1)(\xi_{-} + s) + (s-1)^2 u-su^2$;
\item[] $\beta_2  =  (1-su-\xi_{-})\left(1+(\xi_{-} - s)/c \right)$;
\item[] $t_m  = (\xi_{+}^m -\xi_{-}^m)/(\xi_{+} -\xi_{-})$.
\end{itemize}
\end{notation*}

\begin{remark}
Using such notation, the Riley polynomial of the twist knot $J(2, 2m)$ becomes:
\[
\phi_{J(2, 2m)} (s,u)
=
(s-c)t_m - t_{m-1}.
\]
\end{remark}

With this notation in mind we can write down the general formula for the non--abelian Reidemeister torsion for twist knots.

\begin{theorem}\label{theorem_J(2,2m)}
Let $m$ be a positive integer.
\begin{enumerate}
  \item  The Reidemeister torsion ${\mathbb T}^{J(2, 2m)}_{\lambda}(\rho)$ satisfies the following formula:
\begin{equation}\label{m_pos}
{\mathbb T}^{J(2, 2m)}_{\lambda}(\rho)
=
\frac{\tau_0}{s+s^{-1} - 2} 
\left[
    C_1(m) \xi_{+}^{m-1} t_m + C_2(m) \xi_{-}^{m-1} t_m + C_3(m)
\right].
\end{equation}
\item  Similarly, we have
\begin{equation}\label{m_neg}
{\mathbb T}^{J(2, -2m)}_{\lambda}(\rho)
=
\frac{\tau_0}{s+s^{-1} - 2} 
\left[
    -C_1(-m) \xi_{+}^{-m-1} t_m - C_2(-m) \xi_{-}^{-m-1} t_m + C_3(-m)
\right].
\end{equation}
In that two formulas we have:
\begin{align*}
C_1(m)
&= 
\frac{1}{(\xi_{+} - \xi_{-})^2} 
\left\{
\frac{1}{s} \alpha_1^2 (3m+1) + \frac{m}{s}\beta_1^2 (\xi_{+}^2+1) - m(\xi_{+}-\xi_{-})^2(s+\frac{1}{s}+1) 
\right\}\\
& \quad 
    -\frac{m}{(\xi_{+}-\xi_{-})^4}
    \left\{
    \left( c(1-\xi_{+}) + \frac{\alpha_1}{s}\right)^2  
    \left( (\xi_{+}-\xi_{-})^2(s+\frac{1}{s}+1) - \frac{\alpha_1^2+\beta_1^2}{s}\right)
    \right.\\
& \left. \qquad \qquad \qquad
     +\frac{2\alpha_1\beta_2}{s}\left(c(1-\xi_{+})+\frac{\alpha_1}{s}\right)\left(c(1-\xi_{+})+\frac{\alpha_2}{s}\right) \right\} \\
& \quad
    -\frac{m}{(\xi_{+}-\xi_{-})^4}
    \left\{
       \frac{\alpha_1^2}{s}
        \left( 
        (\xi_{+} - \xi_{-})^2(u^2+4u+3) - \left( c(1-\xi_{+}) + \frac{\alpha_1}{s}\right)^2 
        \right.
    \right.\\
&        \qquad \qquad \qquad \qquad \qquad
    \left.
        \left.
        -\left(c(1-\xi_{-}) + \frac{\beta_1}{s}\right)^2
        \right)
        \right. \\
& \qquad \qquad \qquad \left. 
        + \frac{2\alpha_1\alpha_2}{s}
        \left(
        c(1-\xi_{+}) +\frac{\alpha_1}{s}
        \right)
        \left(
        c(1-\xi_{-}) +\frac{\beta_2}{s}
        \right) 
        \right\},
\end{align*}
\begin{align*}
C_2(m)
&=
\frac{1}{(\xi_{+} -\xi_{-})^2}
\left\{
\frac{1}{s} \beta_1^2 (3m+1) + \frac{m}{s}\alpha_1^2 (\xi_{-}^2+1) - m(\xi_{+}-\xi_{-})^2(s+\frac{1}{s}+1) 
\right\} \\
& \quad
-\frac{m}{(\xi_{+}-\xi_{-})^4}
    \left\{
    \left(
    c(1-\xi_{-})+\frac{\beta_1}{s}
    \right)^2
    \left(
    (\xi_{+}-\xi_{-})^2(s+\frac{1}{s}+1)-\frac{\alpha_1^2 + \beta_1^2}{s}
    \right)
    \right.\\
& \qquad \qquad \qquad \left. 
    +\frac{2\alpha_2 \beta_1}{s}
    \left(
    c(1-\xi_{-})+\frac{\beta_1}{s}
    \right)
    \left(
    c(1-\xi_{-})+\frac{\beta_2}{s}
    \right)
    \right\}\\
& \quad
-\frac{m}{(\xi_{+}-\xi_{-})^4}
    \left\{
    \frac{\beta_1^2}{s} 
      \left( 
      (\xi_{+} - \xi_{-})^2(u^2+4u+3) - \left(c(1-\xi_{+}) + \frac{\alpha_1 }{s}\right)^2 
      \right.
    \right.\\
& \qquad \qquad \qquad \qquad \qquad
    \left.
      \left.
         - \left(c(1-\xi_{-}) + \frac{\beta_1}{s}\right)^2 
      \right) 
    \right. \\
& \qquad \qquad \qquad 
        \left.
        +\frac{2\beta_1\beta_2}{s}
        \left(c(1-\xi_{-})+\frac{\beta_1}{s}\right)\left(c(1-\xi_{+})+\frac{\alpha_2}{s}\right)
        \right\},
\end{align*}
\begin{align*}
C_3(m)
&=
\frac{m}{(\xi_{+} -\xi_{-})^2}
\left\{
(\xi_{+}-\xi_{-})^2(s+\frac{1}{s}+1)-\frac{\alpha_1^2 + \beta_1^2}{s}
\right\} \\
&\quad+
\frac{t_m^2}{(\xi_{+} -\xi_{-})^2}
\left\{
4(\xi_{+}-\xi_{-})^2(s+\frac{1}{s}+1)-\frac{5(\alpha_1^2+\beta_1^2)}{s}
\right\} \\
&\quad -
 \frac{t_m^2}{(\xi_{+}-\xi_{-})^4}
\left\{
    \frac{1}{s}
    \left( 
    c(1-\xi_{+})\beta_1+\frac{\alpha_1 \beta_1}{s}
    \right)^2
    -\frac{1}{s}
    \left(
    c(1-\xi_{+})\beta_2+\frac{\alpha_2 \beta_2}{s}
    \right)^2
\right.\\
& \left.\qquad \qquad \qquad
    +\frac{1}{s}
    \left(
    c(1-\xi_{-})\alpha_1+\frac{\alpha_1 \beta_1}{s}
    \right)^2
    -\frac{1}{s}
    \left(
    c(1-\xi_{-})\alpha_2 +\frac{\alpha_2 \beta_2}{s}
    \right)^2
\right\} \\
&\quad +m(s+\frac{1}{s}-2)^2 t_m^2.
\end{align*}
\end{enumerate}
\end{theorem}

\begin{remark}
One can observe that 
${\mathbb T}^{J(2, 2m)}_{\lambda}$ is symmetric in $\xi_{\pm}$.
Together with the fact that $\xi_{+} \cdot \xi_{-} = 1$, 
we can see that ${\mathbb T}^{J(2, 2m)}_{\lambda}$ is in fact a function of $\xi_{+} + \xi_{-} = u^2 + (2-s-s^{-1})u+2$.
\end{remark}


\subsubsection{Proof of Theorem~\ref{theorem_J(2,2m)}}
We make the detailed proof in the case of  $J(2, 2m)$ for $m>0$.

First, recall that the group of $J(2, 2m)$ admits the following presentation (see Fact~\ref{Fact1}): 
\[
\langle x, y \,|\, w^m x  = y w^m \rangle.
\]
Here $w$ is the word $[y, x^{-1}] = yx^{-1}y^{-1}x$.

Before computations, we give an elementary and useful {linear algebra} lemma about trace of matrices in $M_3(\C)$.

\begin{lemma} \label{lemma_sigma_2}
The two following items hold:
\begin{enumerate}
\item
    Let $A$ be in $M_3(\C)$.  Set
\[
\sigma_1(A) = \trace(A), 
\sigma_2(A) = \frac{1}{2} \left( \trace^2(A)-\trace(A^2)\right) \text{ and } \sigma_3(A) = \det (A).
\] 
    We have 
\[
\det(\I + A) = 1 + \sigma_1(A) + \sigma_2(A) + \sigma_3(A)
\]  
    and if $A \in {\rm GL}(3, \C)$,
$$
\sigma_2(A) = \sigma_1(A^{-1})\cdot \det(A).
$$
\item
    If $A = {(a_{i, j})}_{1 \leq i, j \leq 3}$ and $B = {(b_{i, j})}_{1 \leq i, j \leq 3}$ are two matrices in $M_3(\C)$,
    then we have 
    \begin{align*}
\trace(A)\trace(B) - \trace(AB) 
&=
    \left|
    \begin{array}{cc}
    a_{1, 1} & a_{1, 3} \\
    b_{3, 1} & b_{3, 3}
    \end{array}
    \right|
    +
    \left|
    \begin{array}{cc}
    b_{1, 1} & b_{1, 3} \\
    a_{3, 1} & a_{3, 3}
    \end{array}
    \right|\\
& \quad +
    \left|
    \begin{array}{cc}
    a_{2, 2} & a_{2, 3} \\
    b_{3, 2} & b_{3, 3}
    \end{array}
    \right|
    +
    \left|
    \begin{array}{cc}
    b_{2, 2} & b_{2, 3} \\
    a_{3, 2} & a_{3, 3}
    \end{array}
    \right|\\
&\quad +
    \left|
    \begin{array}{cc}
    a_{1, 1} & a_{1, 2} \\
    b_{2, 1} & b_{2, 2}
    \end{array}
    \right|
    +
    \left|
    \begin{array}{cc}
    b_{1, 1} & b_{1, 2} \\
    a_{2, 1} & a_{2, 2}
    \end{array}
    \right|.
    \end{align*}
\end{enumerate}
\end{lemma}
{\begin{remark}
Observe that $\sigma_2(A)$ is the trace of the matrix of cofactors of $A$.
\end{remark}}

\begin{proof}
\phantom{}\hfill
\begin{enumerate}
  \item The first Eq. of item 1 is well-known. From the Cayley--Hamilton identity, we have
\[
A^3 - \sigma_1(A) A^2 + \sigma_2(A) A - \det(A) \I= 0.
\]

Multiplying this equation by $A^{-1}$ then taking traces of both sides, we obtain the second Eq. of our first claim.
  \item Second item follows from direct calculations.
\end{enumerate}
\end{proof}



\noindent{\it Fox--differential calculus for $2m$-twist knots.}

Since $J(2, 2m)$ is a two--bridge knot,
the non--abelian Reidemeister torsion polynomial
$\T^K_\lambda(\rho)$ associated to $J(2, 2m)$
is expressed as (see Eq.~(\ref{torsionK})):

\begin{equation}\label{torsionJ}
\T^K_\lambda(\rho) = \tau_0
\frac{\det \Phi(\frac{\partial}{\partial x}w^m x w^{-m} y^{-1} )  }
{\det \Phi(y-1)}
\end{equation}
where $\Phi=Ad\circ \rho \otimes \alpha: \Z [\Pi(J(2, 2m))] \to M_3(\C[t, t^{-1}])$.

The following claim gives us the Fox--differential part in the numerator of Eq.~(\ref{torsionJ}).

\begin{claim}\label{ClaimFox}
For $m > 0$, we have:
\begin{equation}\label{EqClaimFox}
\frac{\partial}{\partial x} \left( w^m x w^{-m} y^{-1} \right)  = w^m\left(1 + (1-x)(1 + w^{-1} + \cdots + w^{-m+1})(x^{-1}-x^{-1}y) \right).
\end{equation}
\end{claim}

\begin{proof}[Proof of Claim~\ref{ClaimFox}]
We have:
\begin{align*}
\frac{\partial}{\partial x} \left( w^m x w^{-m} y^{-1} \right) 
&=
\frac{\partial w^m}{\partial x}
+ w^m
+ w^m x (-w^{-m})\frac{\partial w^m}{\partial x} \nonumber \\
&=
w^m
\left(1+(1-x)w^{-m}\frac{\partial w^m}{\partial x}\right). 
\end{align*}
It is easy to see that
\[
\frac{\partial w}{\partial x} = \frac{\partial}{\partial x}\left(yx^{-1}y^{-1}x\right) = yx^{-1}y^{-1} - yx^{-1}.
\] 
Thus
\begin{align*}
w^{-m}\frac{\partial w^m}{\partial x}
&=
(1+ w^{-1} +\cdots + w^{-m+1})w^{-1}\frac{\partial w}{\partial x}
\nonumber\\
&=
(1 + w^{-1} + \cdots + w^{-m+1})(x^{-1}-x^{-1}y),
\end{align*}
which gives us Eq.~(\ref{EqClaimFox}).
\end{proof}

Let $\{E, H, F\}$ be the following usual $\CC$-basis of the Lie algebra $\sll$: 
\[
E=
\left(
\begin{array}{cc}
0 & 1 \\
0 & 0
\end{array}
\right),
H=
\left(
\begin{array}{cc}
1 & 0 \\
0 & -1
\end{array}
\right),
F=
\left(
\begin{array}{cc}
0 & 0 \\
1 & 0
\end{array}
\right).
\]
It is easy to see that the adjoint actions of $x$ and $y$ in the basis $\{ E, H, F \}$ of $\sll$ are given by the following matrices:
\[
X = Ad_{\rho(x)} =
\left(
\begin{array}{ccc}
 s & -2 & -s^{-1} \\
 0 & 1 & s^{-1} \\
 0 & 0 & s^{-1}
\end{array}
\right),\quad
Y = Ad_{\rho(y)} =
\left(
\begin{array}{ccc}
 s & 0 & 0 \\
 su & 1 & 0 \\
 -su^2 & -2u & s^{-1}
\end{array}
\right).
\]

If $W = Ad_{\rho(w)}$, then $\Phi(\frac{\partial}{\partial x}w^m  x w^{-m} y^{-1})$ is given by (see Claim~\ref{ClaimFox}):
\[
W^m 
\left(\I + (\I - tX)(\I+ W^{-1} +\cdots +W^{-m+1})(t^{-1}X^{-1}-X^{-1}Y)\right).
\]

Set $S_m(A) = \I  + A + \cdots + A^{m-1}$, for $A \in \SL$, we finally obtain: 
\begin{equation}\label{PHI}
\Phi(\frac{\partial}{\partial x}w^m  x w^{-m} y^{-1}) = W^m
\left(
\I +(\I -tX)S_m(W^{-1})(t^{-1}X^{-1} - X^{-1}Y)
\right).
\end{equation}


\noindent {\it Observation about the \lq\lq second differential" of a determinant.}

We can compute 
the non--abelian Reidemeister torsion for $J(2, 2m)$ 
combining Eqs.~(\ref{eqn:torsion_eqn}) \&~(\ref{PHI}) as follows: 
\begin{equation*}
{\mathbb T}^{J(2, 2m)}_{\lambda}(\rho)
=
-\tau_0
\lim_{t \to 1}
\frac{\det ( \Phi(\frac{\partial}{\partial x}w^m  x w^{-m} y^{-1})) }
            {(t-1)\det ( \Phi(y-1))}.
\end{equation*}

Using the fact that $\det W =1$, Eq.~(\ref{PHI}) gives:
\begin{equation}
\det \Phi(\frac{\partial}{\partial x}w^m  x w^{-m} y^{-1})
=
\det \left(\I +(\I -tX)S_m(W^{-1})(t^{-1} X^{-1} - X^{-1}Y) \right).
\label{content_Z_m}
\end{equation}
If we write $\det(\I + Z_m)$ for
the right hand side of Eq.~(\ref{content_Z_m}),
then 
\begin{equation}\label{Tlim}
{\mathbb T}^{J(2, 2m)}_{\lambda}(\rho) = 
-\tau_0
\lim_{t \to 1}
\frac{\det(\I+Z_m)}{(t-1)^2(t^2 - (s+s^{-1})t+1)}
\end{equation}
thus
\[{\mathbb T}^{J(2, 2m)}_{\lambda}(\rho)  =
\frac{\tau_0}{s+s^{-1} - 2}
\lim_{t \to 1}
\frac{\det(\I+Z_m)}{(t-1)^2}.
\] 
{Moreover, using the first item of Lemma~\ref{lemma_sigma_2}}  we can split $\det(\I+Z_m)$ as follows: 
\begin{equation}\label{split}
\det(\I + Z_m)
=1 + \sigma_1(Z_m) + \sigma_2(Z_m) + \sigma_3(Z_m),
\end{equation}
where we repeat
\[
\sigma_1(Z_m) = \trace(Z_m), \quad
\sigma_2(Z_m) = \frac{1}{2} \left( \trace^2(Z_m)-\trace(Z_m^2)\right),\quad
\sigma_3(Z_m) = \det(Z_m).
\]


Thus
\begin{equation}\label{torsion_2m_twist}
{\mathbb T}^{J(2, 2m)}_{\lambda}(\rho)
=
\frac{\tau_0}{s+s^{-1}-2}
\left.{
    \frac{1}{2} 
    \frac{d^2}{dt^2}
        \left( 
            1 + \sigma_1(Z_m) + \sigma_2(Z_m) + \sigma_3(Z_m)
        \right)
    }\right|_{t=1}.
\end{equation}

With the \lq\lq splitting\rq\rq\, of  ${\mathbb T}^{J(2, 2m)}_{\lambda}(\rho)$ given in Eq.~(\ref{torsion_2m_twist}) in mind, we compute separately each \lq\lq second differential" of the $\sigma_i(Z_m)\,(i=1,2,3)$ to obtain the non--abelian Reidemeister torsion of $J(2, 2m)$.
\medskip

\noindent {\it The \lq\lq second differential" of $\sigma_3(Z_m)$.}
We concentrate first on  the $\sigma_3(Z_m)$-part of Eq.~(\ref{torsion_2m_twist}), which is the easier term to compute and correspond to the \lq\lq second differential" of $\sigma_3(Z_m)$.
\begin{claim}\label{claim:second_diff_sigma_3}
We have: 
\[
\frac{1}{2} \left.\frac{d^2}{dt^2} (\sigma_3(Z_m))\right|_{t=1} = \lim_{t \to 1}\frac{\sigma_3(Z_m)}{(t-1)^2}
=(2-s-s^{-1})^2 \cdot m t_m^2.
\]
\end{claim}
\begin{proof}[Proof of Claim \ref{claim:second_diff_sigma_3}]
By definition $\sigma_3(Z_m)=\det(Z_m)$, thus
\begin{align}
\sigma_3(Z_m)
    &=
    \det(
        (\I-tX)S_m(W^{-1})(t^{-1}X^{-1} - X^{-1}Y)
            ) \nonumber \\
    &=
    \det(\I-tX)
    \det(S_m(W^{-1}))
    \det(t^{-1}X^{-1}Y)
    \det(Y^{-1}-t\I) \nonumber \\
    &=
    t^{-3}(t-1)^2(1-ts)(1-ts^{-1})(t-s)(t-s^{-1})
    \det(S_m(W^{-1})). \label{sigma_3}
\end{align}
{Dividing Eq.~(\ref{sigma_3}) by $(t-1)^2$ and taking the limit} when $t$ goes to $1$, we thus obtain: 
\begin{equation*}\label{sigma_31}
\lim_{t \to 1}
\frac{\sigma_3(Z_m)}{(t-1)^2}
=
(2-s-s^{-1})^2\det(S_m(W^{-1})).
\end{equation*}
Note, with Eq.~(\ref{ev}) in mind, that $\xi_{\pm}^2$ and $1$ are the eigenvalues of $W^{-1} = Ad_{\rho(w)^{-1}}$. It thus follows that 











\begin{align*}
\det(S_m(W^{-1}))
&=
m
\frac{(1-\xi_{+}^{2m})(1-\xi_{-}^{2m})}{(1-\xi_{+}^2)(1-\xi_{-}^2)} \\
&=
m
\frac{(\xi_{-}^m - \xi_{+}^m)(\xi_{+}^m - \xi_{-}^m)}{(\xi_{-} - \xi_{+})(\xi_{+} - \xi_{-})} \\
&=
mt_m^2. 
\end{align*}
\end{proof}


If we substitute the result of Claim \ref{claim:second_diff_sigma_3} into Eq.~(\ref{torsion_2m_twist}), 
we obtain











\begin{equation}\label{sec_dif}
{\mathbb T}^{J(2, 2m)}_{\lambda}(\rho) = \frac{\tau_0}{s+s^{-1}-2}
\left[
    \left.
    \frac{1}{2} 
    \frac{d^2}{dt^2}
        \left( 
            \sigma_1(Z_m) + \sigma_2(Z_m)
        \right)
    \right|_{t=1}
+ (s+s^{-1} - 2)^2 \cdot mt_m^2
\right]. 
\end{equation}



\medskip


\noindent{\it The \lq\lq second differentials" of $\sigma_1(Z_m)$ and $\sigma_2(Z_m)$.}
We now focus on 
the \lq\lq second differentials" of  $\sigma_1(Z_m)$ and $\sigma_2(Z_m)$.
If we let 
$$\tilde Z_m = (t^{-1}X^{-1}-X^{-1}Y)(\I-tX)S_m(W^{-1}),$$
 then it follows from the definitions of $\sigma_1$ and $\sigma_2$ that 
\[
\sigma_1(Z_m) = \sigma_1(\tilde Z_m), \quad \sigma_2(Z_m) = \sigma_2(\tilde Z_m).
\]
We use $\sigma_1(\tilde Z_m)$ and $\sigma_2(\tilde Z_m)$ instead of 
$\sigma_1(Z_m)$ and $\sigma_2(Z_m)$ for our calculations.

\begin{claim}\label{claim:sec_diffs}
We have:

\begin{align}
\frac{1}{2} \left. \frac{d^2}{dt^2}\sigma_1(\tilde Z_m) \right|_{t=1}
&= 
\trace(X^{-1}S_m(W^{-1})),  \label{sec_dif_sigma_1}\\

\left.\frac{1}{2}\frac{d^2}{dt^2} \sigma_2(\tilde Z_m) \right|_{t=1} 
&= 3\sigma_2(X^{-1}S_m(W^{-1})) + \sigma_2(YS_m(W^{-1})W^{-1}) \label{sec_dif_sigma_2}\\
&\quad -\trace\left(X^{-1}S_m(W^{-1})\right)\trace\left((\I+X^{-1}Y)S_m(W^{-1})\right) \nonumber\\
&\quad + \trace\left(X^{-1}S_m(W^{-1})(\I+X^{-1}Y)S_m(W^{-1})\right).\nonumber 
\end{align}
\end{claim}
\begin{proof}[Proof of Claim \ref{claim:sec_diffs}]
Since $\sigma_1(\tilde Z_m)$ is the trace of $\tilde Z_m$, the
only term which remains after taking the \lq\lq second differential" at $t = 1$ is $\left. \frac{d^2}{dt^2}\frac{1}{t} X^{-1} S_m(W^{-1}) \right|_{t=1}$.

Now we consider $\sigma_2(\tilde Z_m)$.
From the definition of $\sigma_2(\tilde Z_m)$,
we have 

\begin{align*}
\frac{1}{2} 
\left. \frac{d^2}{dt^2}
\sigma_2(\tilde Z_m)
\right|_{t=1} 
&=
    \frac{1}{2}
        \left. \frac{d^2}{dt^2}
        \frac{1}{2}
        \left( 
            \trace^2(\tilde Z_m) -\trace ({\tilde Z_m}^2) 
        \right)
        \right|_{t=1}\\ 
&=
    \frac{1}{4}
    \left[  
    \left. \frac{d^2}{dt^2}\trace^2(\tilde Z_m) \right|_{t=1}
     - \left.\frac{d^2}{dt^2} \trace({\tilde Z_m}^2)\right|_{t=1}
    \right].
\end{align*}

In $\trace({\tilde Z_m}^2)$, 
the following three terms
are the terms which remain after taking the second differential at $t=1$:

\begin{eqnarray*}
&\left. \frac{d^2}{dt^2}t^{-2}\trace\left( (X^{-1}S_m(W^{-1}))^2 \right)\right|_{t=1},\\
&\left. \frac{d^2}{dt^2}-2t^{-1}\trace\left( X^{-1}S_m(W^{-1}) (\I+X^{-1}Y)S_m(W^{-1}) \right)\right|_{t=1},\\
&\left. \frac{d^2}{dt^2}t^2 \trace\left( (YS_m(W^{-1})W^{-1})^2 \right)\right|_{t=1}.
\end{eqnarray*}

Hence
\begin{align*} 
\left.\frac{1}{2}\frac{d^2}{dt^2} \sigma_2(\tilde Z_m) \right|_{t=1}
&=\frac{3}{2}
    \left[
        \trace^2\left(X^{-1}S_m(W^{-1})\right) - \trace\left( (X^{-1}S_m(W^{-1}))^2 \right) 
    \right] \\
&\quad -\trace\left(X^{-1}S_m(W^{-1})\right)\trace\left((\I+X^{-1}Y)S_m(W^{-1})\right) \\
&\quad + \trace\left(X^{-1}S_m(W^{-1})(\I+X^{-1}Y)S_m(W^{-1})\right)\\
&\quad +\frac{1}{2}
    \left[
        \trace^2\left(YS_m(W^{-1})W^{-1}\right) - \trace\left((YS_m(W^{-1})W^{-1})^2\right)
    \right].
\end{align*}
\end{proof}

If we substitute Eqs.~(\ref{sec_dif_sigma_1}) \&~(\ref{sec_dif_sigma_2}) of Claim~\ref{claim:sec_diffs}
into Eq.~(\ref{sec_dif}), then we obtain the following formula for ${\mathbb T}^{J(2, 2m)}_{\lambda} (\rho)$.


\begin{claim}\label{torsionJ(2,2m)}
The non--abelian Reidemeister torsion for $J(2, 2m)$ satisfies the following formula:
\begin{align} \label{matrix_rep_torsion_J(2,2m)}
{\mathbb T}^{J(2, 2m)}_{\lambda} (\rho)
&=
\frac{\tau_0}{s+s^{-1}-2}
\left[
    \trace\left(X^{-1}S_m(W^{-1})\right)
    +3\sigma_2(X^{-1}S_m(W^{-1})) \right. \\
    &\quad + \sigma_2(YS_m(W^{-1})W^{-1}) \nonumber \\ 
    &\quad -\trace\left(X^{-1}S_m(W^{-1})\right)\trace\left( S_m(W^{-1})\right) \nonumber \\
    &\quad + \trace\left(X^{-1}S_m(W^{-1})S_m(W^{-1})\right) \nonumber \\
 &\quad- \trace\left(X^{-1}S_m(W^{-1})\right)\trace\left( X^{-1}YS_m(W^{-1}) \right) \nonumber \\
 &\quad + \trace\left(X^{-1}S_m(W^{-1}) X^{-1}YS_m(W^{-1})\right)  
 \left.+ (s+s^{-1} - 2)^2 \cdot mt_m^2 \right]. \nonumber
\end{align}
\end{claim}


\noindent{\it More explicit descriptions.}

To find more explicit expression of ${\mathbb T}^{J(2, 2m)}_{\lambda}(\rho)$,
we change our basis of $\sll$ in order to diagonalize the matrix {$\rho(w)$}.

The $\SL$-matrix $\rho(w)$ can be diagonalized by 
\[
p=
\left(
\begin{array}{cc}
u+1-s^{-1} & u+1-s^{-1} \\
1-su-\xi_{+} & 1-su- \xi_{-}
\end{array}
\right).
\]
Explicitly, $p^{-1} \rho(w) p$ is the diagonal matrix $\mathrm{diag}(\xi_+, \xi_-)$.

Set $a = 1-su-\xi_{+}$ and $b = 1-su-\xi_{-}$.
With respect to the basis $\{E, H, F\}$ of $\sll$, the matrix of the adjoint action of $p$ becomes as follows: 
\[
P = Ad_p = \frac{1}{a-b}
\left(
\begin{array}{ccc}
-c                         & 2c                       & c \\
 a                         & -(a+b)                   & -b \\
 a^2 / c                   & -2ab / c                 & - b^2 / c
\end{array}
\right)
\]
where $c = u+1-s^{-1}$ is defined in Subsection~\ref{statement}.


Note that 
the matrix $P^{-1} W P$ is the diagonal matrix 
$\mathrm{diag}(\xi_{+}^2, 1, \xi_{-}^2)$. Here we repeat that $W = Ad_{\rho(w)}$.


Set 
$$\tilde X = P^{-1}XP,\quad  \tilde Y = P^{-1}YP \text{ and } \tilde W = P^{-1}WP.$$ 
Since we have $P^{-1}S_m(W^{-1}) P = S_m( \tilde W^{-1})$, 
the matrix $P^{-1} S_m (W^{-1}) P$ is the following diagonal matrix 
$$P^{-1} S_m (W^{-1}) P = \mathrm{diag}(\xi_{-}^{m-1} t_m, m, \xi_{+}^{m-1} t_m).$$

Moreover as $\trace(X^{-1}S_m(W^{-1})) = \trace(\tilde X^{-1} S_m(\tilde W^{-1}))$, we have the following claim.

\begin{claim}\label{trace_X^{-1}S_m}
We have
\begin{align*}
\lefteqn{
\trace(X^{-1}S_m(W^{-1})) }
& \\
&=
\frac{1}{(a-b)^2}
\left(
\frac{\beta_1^2}{s} \xi_{-}^{m-1} t_m 
+ \left((a-b)^2(s+s^{-1}+1)-\frac{\beta_1^2}{s} - \frac{\alpha_1^2}{s}\right)m
+\frac{\alpha_1^2}{s} \xi_{+}^{m-1} t_m
\right).
\end{align*}
\end{claim}

\begin{proof}[Proof of Claim \ref{trace_X^{-1}S_m}]
By a direct computation, we obtain that the $(1, 1)$-component of the matrix $\tilde X^{-1}$ is equal to $\beta_1^2 / (s(a-b)^2)$ and its 
$(3, 3)$-component is equal to $\alpha_1^2 / (s(a-b)^2)$. 
We can also find the $(2,2)$-component of $\tilde X^{-1}$ from $\trace(\tilde X^{-1}) = s+s^{-1}+1$.
\end{proof}

Now, we compute $\sigma_2(XS_m(W^{-1}))$ and $\sigma_2(YS_m(W^{-1})W^{-1})$
from Lemma \ref{lemma_sigma_2} as follows.

\begin{claim}\label{sigma_2_result}
The following equalities hold: 
\begin{align*}
\lefteqn{
  (1) \quad
  \sigma_2(X^{-1}S_m(W^{-1}))
}
& \\
&\quad=
  \frac{1}{(a-b)^2}
  \left(
    \frac{\beta^2_1}{s} \xi_{-}^{m-1}m t_m 
    + \left((a-b)^2(s+s^{-1}+1) - \frac{\alpha^2_1}{s} - \frac{\beta^2_1}{s} \right) t_m^2 + \frac{\alpha^2_1}{s} \xi_{+}^{m-1} m t_m
  \right).\\
\lefteqn{
  (2) \quad
  \sigma_2(YS_m(W^{-1})W^{-1})
}
& \\
&\quad=
  \frac{1}{(a-b)^2}
  \left(
    \frac{\alpha^2_1}{s} \xi_{-}^{m+1}m t_m 
    + \left((a-b)^2(s+s^{-1}+1) - \frac{\alpha^2_1}{s} - \frac{\beta^2_1}{s} \right) t_m^2
    + \frac{\beta^2_1}{s} \xi_{+}^{m+1} m t_m
  \right).
\end{align*}
\end{claim}
\begin{proof}[Proof of Claim \ref{sigma_2_result}]
Using Lemma \ref{lemma_sigma_2} and because $\det(X)=1, \det(Y) = 1$ we have:
\[
\sigma_2(X^{-1}S_m(W^{-1})) = \trace(X S_m(W^{-1})^{-1})\cdot \det(S_m(W^{-1}))
\] 
and 
\[
\sigma_2(YS_m(W^{-1}) W^{-1}) = \trace(Y^{-1} W S_m(W^{-1})^{-1})\cdot \det(S_m(W^{-1})).
\]
We obtain the above formulas by computing the traces using $\tilde X, \tilde Y$ and $S_m(\tilde W^{-1})$ as in Claim~\ref{trace_X^{-1}S_m}.
\end{proof}

Finally we calculate the other two terms 
which are of the following form: $-\trace(A)\trace(B) + \trace(AB)$.
\begin{claim}\label{trAB-trAtrB}
We have:
\begin{align*}
(1)\quad\lefteqn{
-\trace(X^{-1}S_m(W^{-1}))\trace(S_m(W^{-1}))
+\trace(X^{-1}S_m(W^{-1})S_m(W^{-1}))
}
& \\
&=
- \frac{1}{(a-b)^2}
\left[
\left(
(a-b)^2(s+\frac{1}{s}+1) -\frac{\alpha^2_1}{s} 
\right)\xi_{-}^{m-1} m t_m
+\left(
\frac{\alpha^2_1}{s} + \frac{\beta^2_1}{s} 
\right)t^2_m \right.\\
& \left.\quad+\left(
(a-b)^2(s+\frac{1}{s}+1) -\frac{\beta^2_1}{s} 
\right)\xi_{+}^{m-1} m t_m.
\right]
\end{align*}
(2) If we set $\tilde X^{-1}={(a_{i, j})}_{1\leq i, j \leq 3},$ and  $\tilde X^{-1} \tilde Y={(b_{i, j})}_{1 \leq i, j \leq 3}$,
then we have
\begin{align*}
&
-\trace(X^{-1}S_m(W^{-1}))\trace(X^{-1} Y S_m(W^{-1}))
+\trace(X^{-1}S_m(W^{-1})X^{-1} Y S_m(W^{-1}))
\\
&=
\left(
    \left|
    \begin{array}{cc}
    a_{1, 1} & a_{1, 3} \\
    b_{3, 1} & b_{3, 3}
    \end{array}
    \right|
    +
    \left|
    \begin{array}{cc}
    b_{1, 1} & b_{1, 3} \\
    a_{3, 1} & a_{3, 3} 
    \end{array}
    \right|
\right)
t^2_m \\
& \quad -
\left(
    \left|
    \begin{array}{cc}
    a_{2, 2} & a_{2, 3} \\
    b_{3, 2} & b_{3, 3}
    \end{array}
    \right|
    +
    \left|
    \begin{array}{cc}
    b_{2, 2} & b_{2, 3} \\
    a_{3, 2} & a_{3, 3} 
    \end{array}
    \right|
\right)m 
\xi_{+}^{m-1} t_m \\
& \quad -
\left(
    \left|
    \begin{array}{cc}
    a_{1, 1} & a_{1, 2} \\
    b_{2, 1} & b_{2, 2}
    \end{array}
    \right|
    +
    \left|
    \begin{array}{cc}
    b_{1, 1} & b_{1, 2} \\
    a_{2, 1} & a_{2, 2} 
    \end{array}
    \right|
\right)
m \xi_{-}^{m-1}t_m.
\end{align*}
\end{claim}
\begin{proof}[Proof of Claim \ref{trAB-trAtrB}]
Item (1) follows from above results and Item (2) follows from Lem\-ma~\ref{lemma_sigma_2}.
\end{proof}

\begin{remark}
 The  matrices $\tilde X^{-1}$ and $\tilde X^{-1} \tilde Y$ are described explicitly as follows.
\[
\tilde X ^{-1}
=
\frac{1}{(a-b)^2}
\left(
\begin{array}{ccc}
\frac{\beta^2_1}{s}  & -\frac{2\beta_1 \beta_2}{s} & -\frac{\beta^2_2}{s} \\
\frac{\alpha_2 \beta_1}{s} & (a-b)^2(s+\frac{1}{s}+1)-\frac{\alpha^2_1+\beta^2_1}{s} & -\frac{\alpha_1 \beta_2}{s} \\
-\frac{\alpha_2^2}{s} & \frac{2\alpha_1 \alpha_2}{s} & \frac{\alpha^2_1}{s}
\end{array}
\right),
\]
\begin{align*}
\lefteqn{
(a-b)^2 \tilde X^{-1} \tilde Y
} & \\
&=
\left(
\begin{array}{lll}
(c(1-\xi_{-})+\frac{\beta_1}{s})^2 & -2(c(1-\xi_{-})+\frac{\beta_1}{s})(c(1-\xi_{-})+\frac{\beta_2}{s}) & -(c(1-\xi_{-})+\frac{\beta_2}{s})^2 \\
\begin{array}{l}
(c(1-\xi_{+})+\frac{\alpha_2}{s})\\
\quad\cdot(c(1-\xi_{-})+\frac{\beta_1}{s})
\end{array}
&
\begin{array}{l}
 (a-b)^2(u^2+4u+3) \\
 \quad - (c(1-\xi_{+})+\frac{\alpha_1}{s})^2 \\
 \quad -(c(1-\xi_{-})+\frac{\beta_1}{s})^2
\end{array}
 &
 \begin{array}{l}
-(c(1-\xi_{+})+\frac{\alpha_1}{s})\\
 \quad \cdot (c(1-\xi_{-})+\frac{\beta_2}{s})
\end{array}
\\
-(c(1-\xi_{+})+\frac{\alpha_2}{s})^2 & 2(c(1-\xi_{+})+\frac{\alpha_1}{s})(c(1-\xi_{+})+\frac{\alpha_2}{s}) &(c(1-\xi_{+})+\frac{\alpha_1}{s})^2 
\end{array}
\right).
\end{align*}
\end{remark}

One can observe that $(a-b)^2$ is equal to $(\xi_{+} - \xi_{-})^2$. Thus, 
if we substitute the results given in
Claims \ref{trace_X^{-1}S_m}, \ref{sigma_2_result} \& \ref{trAB-trAtrB}
into Eq.~(\ref{matrix_rep_torsion_J(2,2m)}), then we obtain Eq.~(\ref{m_pos}) of Theorem~\ref{theorem_J(2,2m)}. This achieves the first part of the proof of Theorem~\ref{theorem_J(2,2m)}. 

The computation of ${\mathbb T}^{J(2, -2m)}_{\lambda} (\rho)$, for $m>0$, is completely similar and has the following expression:
\begin{align}
{\mathbb T}^{J(2, -2m)}_{\lambda}(\rho)
&=
-\tau_0
\lim_{t \to 1}
\frac{\det ( \Phi(\frac{\partial}{\partial x}w^{-m}  x w^m y^{-1})) }
            {(t-1)\det ( \Phi(y-1))} \nonumber \\
&=
\frac{\tau_0}{s+s^{-1} - 2}
\lim_{t \to 1}
\frac{\det(\I+Z_{-m})}{(t-1)^2}. \label{eqn:torsion_J(2,-2m)}
\end{align}
Here the matrix $Z_{-m}$ is given by 
$(\I-tX)S_m(W)(YX^{-1}- t^{-1}YX^{-1}Y^{-1})$.
The right hand side of Eq.~(\ref{eqn:torsion_J(2,-2m)}) is given by
\begin{align}\label{eqn:torsion_J(2,-2m)_tr}
&\frac{\tau_0}{s+s^{-1}-2}
\left[
  -\trace(X^{-1}S_m(W)W)
   +3\sigma_2(WX^{-1}S_m(W)) + \sigma_2(YS_m(W))
\right. \\
&\quad 
-\trace(X^{-1}S_m(W)W)\trace((\I+X^{-1}Y)S_m(W)W)  \nonumber\\
&\quad 
+ \trace(X^{-1}S_m(W)W(\I+X^{-1}Y)S_m(W)W)  \nonumber \\
&\quad \left.- (s+s^{-1} - 2)^2 \cdot mt_m^2 \right]. \nonumber
\end{align}
Each term in Eq.~(\ref{eqn:torsion_J(2,-2m)_tr}) can be computed similarly as in Claims~\ref{trace_X^{-1}S_m},~\ref{sigma_2_result} \&~\ref{trAB-trAtrB} which give the second item of Theorem~\ref{theorem_J(2,2m)}.

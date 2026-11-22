---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-008-35-the-character-varieties-of-twist-knots-a-recu
section_title: "The character varieties of twist knots: a recursive description"
section_number: 3.5
pages: 8-12
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.988
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
T. Le~\cite{Le} gives a recursive description of the $\SL$-character variety of two--bridge knots and apply it to obtain an \emph{explicit} description of the $\SL$-character variety of torus knots. 
Here we apply his method to obtain an explicit recurrent description of the $\SL$-character variety of twist knots. This is the main difference with the description given by Hoste and Shanahan~\cite{HS}.
    

Let $n = 2m$ or $2m+1$, recall that 
$\Pi(J(2,n))=\langle x,y \,|\, \Omega_m x=y \Omega_m \rangle,$
where $\Omega_m$ is a word in $x, y$ (see Facts~\ref{Fact1}--\ref{Fact2}).

\begin{notation*}
Let $\gamma \in \Pi(J(2,n))$. Following a notation introduced in~\cite{DehnSurgery}, we let 
$$I_\gamma : X(\Pi(J(2,n))) \to \CC$$ 
be the trace--function defined by $I_\gamma : \rho \mapsto \tr(\rho(\gamma))$.
\end{notation*}

Let $a=I_x$, $b=I_{xy}$ and recall the following useful formulas for $A,B,C \in \SL$:
\begin{equation}\label{Tr1}
\mathrm{tr}(A^{-1}) = \mathrm{tr}(A) \text{ and } \mathrm{tr}(AB) = \mathrm{tr}(BA),
\end{equation}
\begin{equation}\label{Tr2}
\mathrm{tr}(AB) + \mathrm{tr}(A^{-1}B) = \mathrm{tr}(A)\mathrm{tr}(B),
\end{equation}
\begin{equation}\label{Tr3}
\mathrm{tr}(ABA^{-1}B^{-1}) = -2 - \mathrm{tr}(A)\mathrm{tr}(B)\mathrm{tr}(AB) + (\mathrm{tr}(A))^2 +(\mathrm{tr}(B))^2+(\mathrm{tr}(AB))^2.
\end{equation}

As $x$ and $y$ are conjugate elements in $\Pi(J(2,n))$, we have $I_y = a = I_x$.
If $\gamma$ is a word in the letters $x$ and $y$, then $I_\gamma$ can always be expressed as a polynomial function  in $a$ and $b$. For example, combining the usual Formulas~(\ref{Tr1}),~(\ref{Tr2}) and~(\ref{Tr3}), one can easily observe that for $w=[y, x^{-1}]=yx^{-1}y^{-1}x$, we have
\begin{equation}\label{I_w}
I_w = -2 - a^2b + 2a^2+b^2.
\end{equation}

The character variety of $\Pi(J(2,n))$ is thus parametrized by $a$ and $b$. Here is a practical description of it:
\begin{enumerate}
  \item We first consider the abelian part of the character variety. It is easy to see that the equation $a^2 - b - 2 = 0$ determines the abelian part of the character variety of any knot group.
  \item Next, consider the non-abelian part of the character variety of $\Pi(J(2,n))$, suppose that the length of the word $\Omega_m$ is $2k+2$ (we know that the length of $\Omega_m$ is even). According to \cite[Theorem 3.3.1]{Le}, the non--abelian part of the character variety of $\Pi(J(2,n))$, {for} $n=2m$ or $2m+1$, is determined by the polynomial equation:
\begin{equation*}\label{EQ:CharVar}
{\mathbf\Phi}_{m}(a,b)=0,
\end{equation*}
where
$${\mathbf\Phi}_{m}(a,b)=I_{\Omega_m}-I_{\Omega_m'}+\dotsb+(-1)^{k}I_{\Omega_m^{(k)}}+(-1)^{k+1}.$$ Here we adopt the following notation: if  $\Lambda$ is a word then $\Lambda'$ denotes the word obtained from $\Lambda$ by deleting the two end letters.  
\end{enumerate}
        
    
Let us give the two simplest examples to illustrate this general result and find again some well--known facts.

\begin{example}\label{Ex1}
The trefoil knot $3_1$ is the twist knot $J(2,2)$. With the above notation, one has $\Omega_1 = x^{-1}y^{-1}$. Thus applying { Le's method}, the non--abelian part of the character variety is given by the polynomial equation:
\[
{\mathbf\Phi}_{1}(a,b)=I_{x^{-1}y^{-1}} - 1 =0,
\]
which reduces to
\begin{equation*}\label{NabTrefoil}
b = 1.
\end{equation*}
\end{example}


\begin{example}\label{Ex2}
The figure eight knot $4_1$ is the twist knot $J(2,-2)$. With the above notation, one has $\Omega_{-1} = x^{-1}yxy^{-1}$. Thus, the non--abelian part of the character variety of the group of the figure eight knot is given by the polynomial equation:
\[
{\mathbf\Phi}_{-1}(a,b)=I_{x^{-1}yxy^{-1}} - I_{yx} + 1 = 0,
\]
which reduces, using Equation~(\ref{I_w}), to:
\begin{equation*}\label{Nab8}
2a^2+b^2-a^2b - b = 1.
\end{equation*}
\end{example}

Now, we turn back to the general case and only consider the twist knot $J(2, 2m)$ (see Item (2) of Remark~\ref{remarktwist}). Recall that (see Remark~\ref{wordtwistknot}):
\begin{equation}\label{eqWOmega}
\Pi(J(2, 2m)) = \langle x, y \; |\; \Omega_m x = y \Omega_m \rangle, \text{ where } \Omega_m = \begin{cases}
     w^m & \text{ if } m < 0, \\
      x^{-1} {(\overline{w})}^{m-1} y^{-1} & \text{ if } m > 0.
      \end{cases}
\end{equation}
Here $w=[y,x^{-1}]$ and $\overline{w} = [y^{-1}, x]$ and observe that the length of the word $\Omega_m$ is $4m$, if $m < 0$, and $4m-2$, if $m>0$. 

Our method is based on the fact that the word $\Omega_m$ in the distinguished Wirtinger presentation~(\ref{eqWOmega}) of $\Pi(J(2, 2m))$ presents a particularly nice \lq\lq periodic" property. This property is discussed in the following obvious claim.

\begin{claim}\label{claimOmega}
For $m \in \ZZ^*$, we have
\[
    \Omega_{m}^{(4)} = \begin{cases}
    w^{m+2}  & \text{ if } m\leqslant -2,\\
     x^{-1} {(\overline{w})}^{m-3}y^{-1} & \text{ if } m \geqslant 3.
\end{cases}
\]
\end{claim}

Based on Claim~\ref{claimOmega}, for $m \geqslant 0$, we adopt the following notation:
$$S^+_m=I_{\Omega_{m+2}}, \; T^+_m=I_{{(\Omega_{m+2})}'},\; U^+_m=I_{{(\Omega_{m+2})}''}  \text{ and } V^+_m=I_{{(\Omega_{m+2})}'''},$$
and similarly, for $m\leqslant 0$,
$$S^-_{m}=I_{\Omega_{m-2}}, \; T^-_{m}=I_{{(\Omega_{m-2})}'},\; U^-_{m}=I_{{(\Omega_{m-2})}''}  \text{ and } V^-_{m}=I_{{(\Omega_{m-2})}'''}.$$

The Cayley--Hamilton identity applied to the matrix $A^2 \in \SL$ gives$$A^m \left(A^{4}-(\tr A^2)A^{2}+\I\right)=0.$$ 
Write $c(a,b)=I_{\Omega_2}$; thus for $m\geqslant 0$, we have
$$S^+_{m+4} - c(a,b) S^+_{m+2} + S^+_m =0$$ and same relations for $T^+_m$, $U^+_m$ and $V^+_m$ hold. Similarly, we have
$$S^-_{m-4} - c(a,b) S^-_{m-2} + S^-_m =0$$ and same relations for $T^-_m$, $U^-_m$ and $V^-_m$ also hold.


If we write $R^{\pm}_m=S^{\pm}_m-T^{\pm}_m+U^{\pm}_m-V^{\pm}_m$ for $m \in \ZZ$, then above computations can be summarized in the following claim which give us a recursive relation for ${(R^{\pm}_m)}_{m \in \ZZ}$.

\begin{claim} \label{R}
The sequence of polynomials $\left( {R^{\pm}_m(a,b)} \right)_{m \in \ZZ}$  satisfies the following recursive relation:
\begin{equation}\label{R+-}
R^{\pm}_{m\pm 4} - c(a,b) R^{\pm}_{m \pm 2} + R^{\pm}_m =0.
\end{equation}










\end{claim}

In Equation~(\ref{R+-}),  using Formula~(\ref{Tr2}) and Equation~(\ref{I_w}), we have:
\[
c(a,b) = I_{w^2} = ({I_w})^2 - 2 = 2+4a^2b-8a^2-4b^2+a^4b^2-4a^4b-2a^2b^3+4a^4+4a^2b^2+b^4.
\]

Let $v$ be such that:
\begin{equation}\label{u/c}
v + v^{-1}=c(a,b).
\end{equation}

For $m \in \ZZ^*$, we distinguish four cases to derive helpful formulas for ${\mathbf\Phi}_m$ in the case of twist knots. 
\begin{itemize}
  \item {\it Case 1:} $m > 0$ is even. 

Let $m=2l$, with $l > 0$, and set $r_i=R_{2i}$. Then 
$$r_{i+2}=c(a,b)r_{i+1}-r_i, \text{ for } i\geqslant 0.$$
 As we have supposed that $v+v^{-1}=c(a,b)$ and following a standard argument in combinatorics (see e.g. \cite[p. 322]{Merris:2003}), we have the general formula (which can also be proved by induction) $r_i=Mv^i+Nv^{-i}$, where $M$ and $N$ are determined by the initial conditions:
\[
\begin{cases}
      r_0=R^+_0=M^+_0+N^+_0  \\
      r_1=R^+_2=M^+_0v+N^+_0v^{-1} 
\end{cases}
\] 
Further observe that:
\[
r_0 = I_{\Omega_2} - I_{\Omega'_2} + I_{\Omega''_2}- I_{\Omega'''_2} = I_{x^{-1}\overline{w}y^{-1}} - I_w + b - 1.
\]
So, we have
\begin{equation*}\begin{split}{\mathbf\Phi}_{m+2}&=R^+_m+R^+_{m-2}+\dotsb+R^+_0\\
&= r_l + \dotsb + r_0\\
&=\sum_{i=0}^l (M^+_0v^i+N^+_0v^{-i})\\&=M^+_0\frac{v^{l+1}-1}{v-1}+N^+_0\frac{v^{-l-1}-1}{v^{-1}-1}.
\end{split}\end{equation*}


  \item {\it Case 2:} $m < 0$ is even. 

Let $m= - 2l$, with $l > 0$, and set $r_i=R^-_{-2i},\ i\geqslant 0$. Similar to the first case, 
$$r_{i+2}=c(a,b)r_{i+1}-r_i, \text{ for } i\geqslant 0.$$ 
The initial conditions are
\[
\begin{cases}
      r_0=R^-_0=M^-_0+N^-_0  \\
      r_1=R^-_{-2}=M^-_0v+N^-_0v^{-1}
\end{cases}
\] 
Further observe that:
\[
r_0 = I_{\Omega_{-2}} - I_{\Omega'_{-2}} + I_{\Omega''_{-2}}- I_{\Omega'''_{-2}} = I_{w^{2}} - I_{y (\overline{w})^{-1}x} + I_w - b.
\]


Thus, we have
\begin{equation*}\begin{split}{\mathbf\Phi}_{m-2}&=R^-_m+R^-_{m+2}+\dotsb+R^-_{0}+1\\
&= r_l + \dotsb + r_0+1\\
&=\sum_{i=0}^l (M^-_0v^i+N^-_0v^{-i})+1\\&=M^-_0\frac{v^{l+1}-1}{v-1}+N^-_0\frac{v^{-l-1}-1}{v^{-1}-1}+1.
\end{split}\end{equation*}


  \item {\it Case 3:} $m > 0$ is odd. 

Let $m=2l+1$, with $l>0$, and set $r_i=R^+_{2i+1},\ i\geqslant 0$. Similar to the first case, 
$$r_{i+2}=c(a,b)r_{i+1}-r_i, \text{ for } i\geqslant 0.$$ 
The initial conditions are
\[
\begin{cases}
      r_0=R^+_1=M^+_1+N^+_1  \\
      r_1=R^+_3=M^+_1v+N^+_1v^{-1}
\end{cases}
\] 
Further observe that:
\[
r_0 = I_{\Omega_3} - I_{\Omega'_3} + I_{\Omega''_3}- I_{\Omega'''_3} = I_{x^{-1}(\overline{w})^{2}y^{-1}} - I_{(\overline{w})^{2}} + I_{xwy} - I_w.
\]
Thus, 
\begin{equation*}\begin{split}{\mathbf\Phi}_{m+2}&=R^+_m+R^+_{m-2}+\dotsb+R^+_1+b-1\\ 
&= r_l + \dotsb + r_0 + b - 1\\
&=\sum_{i=0}^l (M^+_1v^i+N^+_1v^{-i})+b-1\\
&=M^+_1\frac{v^{l+1}-1}{v-1}+N^+_1\frac{v^{-l-1}-1}{v^{-1}-1}+b-1.
\end{split}\end{equation*}

\item {\it Case 4:} $m < 0$ is odd. 

Let $m=-2l-1$, with $l>0$, and set $r_i=R^-_{-2i-1},\ i\geqslant 0$. Similar to the first case, 
$$r_{i+2}=c(a,b)r_{i+1}-r_i, \text{ for } i\geqslant 0.$$ 
The initial conditions are
\[
\begin{cases}
      r_0=R^-_{-1}=M^-_1+N^-_1  \\
      r_1=R^-_{-3}=M^-_1v+N^-_1v^{-1}
\end{cases}
\] 
Further observe that:
\[
r_0 = I_{\Omega_{-3}} - I_{\Omega'_{-3}} + I_{\Omega''_{-3}} - I_{\Omega'''_{-3}} = I_{w^3} - I_{y(\overline{w})^{-2}x} + I_{w^2} - I_{y^{-1}w^{-1}x^{-1}}.
\]


Similarly to the previous case, we have:
\begin{equation*}\begin{split}{\mathbf\Phi}_{m-2}&=R^-_m+R^-_{m+2}+\dotsb +R^-_{-1} + I_{w} - b + 1\\ 
&= r_l + \dotsb + r_0 +I_{w} - b + 1\\
&=\sum_{i=0}^l (M^-_1v^i+N^-_1v^{-i}) +I_{w} - b + 1\\
&=M^-_1\frac{v^{l+1}-1}{v-1}+N^-_1\frac{v^{-l-1}-1}{v^{-1}-1} - a^2b + 2a^2 + b^2 - b - 1.
\end{split}\end{equation*}
\end{itemize}


If we adopt the following notation:
\begin{equation}
\label{MuNu}
M^\pm_j(v, l) = M^\pm_j\frac{v^{l+1}-1}{v-1} \text{ and } N^\pm_j(v, l) = N^\pm_j\frac{v^{-l-1}-1}{v^{-1}-1}, \quad j = 0, 1,
\end{equation}
then we summarize our computations in the following proposition.
\begin{proposition}
The polynomial equation which describes the character variety of the group of the twist knot $J(2,n)$, {for} $n = 2m$ or $2m+1$, is given by  ${\mathbf\Phi}_{m}(a,b) = 0$ where the sequence ${\left( {\mathbf\Phi}_{m}(a,b) \right)}_{m \in \ZZ}$ is recursively defined as follows:
$${\mathbf\Phi}_0(a,b) = 1, \quad {\mathbf\Phi}_{1}(a,b) = b-1, \quad {\mathbf\Phi}_{-1}(a,b) = - a^2b + 2a^2 + b^2 - b - 1,$$ and for $m>1$
\begin{equation}\label{CharVarTK}
{\mathbf\Phi}_{m + 2}(a,b) = \begin{cases}
     M^+_0(v, l) + N^+_0(v, l) & \text{ if } m = 2l \text{ is even}, \\
     M^+_1(v, l) + N^+_1(v, l)+ b - 1 & \text{ if } m=2l+1 \text{ is odd},
\end{cases}
\end{equation}
and
\begin{equation}\label{CharVarTK'}
{\mathbf\Phi}_{-m - 2}(a,b) = \begin{cases}
     M^-_0(v, l) + N^-_0(v, l) + 1 & \text{ if } m = 2l \text{ is even}, \\
     M^-_1(v, l) + N^-_1(v, l) - a^2b + 2a^2 + b^2 - b - 1& \text{ if } m=2l+1 \text{ is odd}.
\end{cases}
\end{equation}
Here $v$ is defined in Equation~(\ref{u/c}) and $M^\pm_k(v, l), N^\pm_k(v, l)$ in Equation~(\ref{MuNu}).
\end{proposition}

\begin{remark}
Observe that in Equations~(\ref{CharVarTK}) and~(\ref{CharVarTK'}), the part $M^\pm_k(v, l) + N^\pm_k(v, l)$ is the \lq\lq recursive" part. In Equation~(\ref{CharVarTK}) the part $b-1$ corresponds to ${\mathbf\Phi}_{1}(a,b)$, and in Equation~(\ref{CharVarTK'}) the part $- a^2b + 2a^2 + b^2 - b - 1$ corresponds to ${\mathbf\Phi}_{-1}(a,b)$, see Examples~\ref{Ex1} and~\ref{Ex2}.
\end{remark}

---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-032-102-x-coordinates
section_title: "X-coordinates"
section_number: 10.2
pages: 33-39
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
text_source: latex
latex_prose_ratio: 0.862
latex_coverage_ratio: 0.885
---
We define $X$-coordinates for Ptolemy assignments and shape assignments. These are defined for face points and agree with the $X$-coordinates of Fock and Goncharov~\cite[p.~133]{FockGoncharov}.

The natural $A_4$ action on vertices of $\dtruncsimp$ has two orbits. Let $\varepsilon_\circlearrowleft^{v_0v_1v_2}$ be a sign, which is positive if and only if $v_0v_1v_2$ is in the orbit of $012$.
\begin{definition} Let $c$ be a Ptolemy assignment and let $t\in\Delta_n^3(\Z)$ be a face point. 
The \emph{$X$-coordinate} at $t$ is given by
\begin{equation}
X_t=\prod_{t\in \mathrm{face}(v_0v_1v_2)}c^{\varepsilon_\circlearrowleft^{v_0v_1v_2}}_{t+v_0-v_1}
\end{equation} 
where the product is taken over the six ordered triples of vertices $v_0, v_1, v_2$ spanning the face containing $t$.
\end{definition}
As an example, the $X$-coodinate of $t=(t_0,t_1,t_2,0)$ is given by
\begin{equation}\label{eq:XExample}
X_{(t_0,t_1,t_2,0)}=\frac{c_{t+e_0-e_1}c_{t+e_1-e_2}c_{t+e_2-e_0}}{c_{t+e_0-e_2}c_{t+e_1-e_0}c_{t+e_2-e_1}}.
\end{equation}






\begin{definition} 
Let $z$ be a shape assignment on $\Delta^3_n$ and let $t$ be a face point spanned by $v_0$, $v_1$ and $v_2$. The \emph{$X$-coordinate} at $t$ is given by
\begin{equation}\label{eq:XandProducts}
X_t=-\prod_{s+e=t}z^e_s.
\end{equation}
\end{definition} 

\begin{remark}\label{rm:HalfofFaceEq}
Note that the product~\eqref{eq:XandProducts} consists of half of the terms involved in a face equation. More precisely, if $v_0v_1v_2\in\overline{\overline{\Delta_0}}$ is glued to $w_0w_1w_2\in\overline{\overline{\Delta_1}}$, the face equations are given by 
\begin{equation}
X_{t_0v_0+t_1v_1+t_2v_2}^{\varepsilon_\circlearrowleft^{v_0v_1v_2}}=X_{t_0w_0+t_1w_1+t_2w_2}^{\varepsilon_\circlearrowleft^{w_0w_1w_2}}.
\end{equation}
 Note that $\varepsilon_\circlearrowleft^{v_0v_1v_2}$ and $\varepsilon_\circlearrowleft^{w_0w_1w_2}$ are equal if and only if the face pairing preserves orientation. For oriented triangulations the signs are always opposite.
\end{remark}

\begin{lemma} The $X$-coordinates transform as the shapes under reordering, i.e.~we have
\begin{equation}
X(\sigma^*(c))_t=X(c)^{\sgn(\sigma)}_{\sigma(t)},\qquad X(\sigma^*(z))_t=X(z)^{\sgn(\sigma)}_{\sigma(t)}.
\end{equation}
\end{lemma}
\begin{proof}
Unwinding the definitions, we have
\begin{multline}
X(\sigma^*c)_t=
\prod_{t\in \mathrm{face}(v_0v_1v_2)}(\sigma^* c)^{\varepsilon_\circlearrowleft^{v_0v_1v_2}}_{t+v_0-v_1} =
\prod_{t\in\mathrm{face}(v_0v_1v_2)} \det(I_{\sigma,\sigma(t+v_0-v_1)}) c^{\varepsilon_\circlearrowleft^{v_0v_1v_2}}_{\sigma(t)+\sigma(v_0)-\sigma(v_1)}=\\
\left(\prod_{t\in \mathrm{face}(v_0v_1v_2)} \det(I_{\sigma,\sigma(t+v_0-v_1)})\right) X(c)_{\sigma(t)}^{\sgn(\sigma)} =
 X(c)_{\sigma(t)}^{\sgn(\sigma)}.
\end{multline}
The fact that the product of determinants equals $1$ follows from Remark~\ref{rm:ShuffleOdd}, which implies that $\det(I_{\sigma,\sigma(t+v_0-v_1)})=\det(I_{\sigma,\sigma(t+v_1-v_0)})$. Since both are $\pm 1$, their product is $1$. The second equation is obvious.
\end{proof}

\begin{lemma} The $X$-coordinates of a Ptolemy assignment $c$ agree with the $X$-coordinates of the corresponding shape assignment $\mu(c)$.
\end{lemma}
\begin{proof}
We must prove that
\begin{equation}
-\prod_{s+e=t}\mu(c)^e_s=\prod_{t\in \mathrm{face}(v_0v_1v_2)}c^{\varepsilon_\circlearrowleft^{v_0v_1v_2}}_{t+v_0-v_1}.
\end{equation}
By compatibility under reordering, it is enough to prove this for $t=(t_0,t_1,t_2,0)=t_0e_0+t_1e_1+t_2e_2$.
Let $t=\alpha+(1110)$. By \eqref{eq:Xcoordinate},
\begin{equation}
\begin{aligned}
-\prod_{s+e=t}\mu(c)^e_s&=z^{1100}_{\alpha+0010}z^{0110}_{\alpha+1000}z^{1010}_{\alpha+0010}\\
&=\frac{c_{\alpha+2010,0}c_{\alpha+1200,0}c_{\alpha+0120,0}}{c_{\alpha+2100,0} c_{\alpha+0210,0} c_{\alpha+1020,0}}\\
&=\frac{c_{t+e_0-e_1}c_{t+e_1-e_2}c_{t+e_2-e_0}}{c_{t+e_0-e_2}c_{t+e_1-e_0}c_{t+e_2-e_1}}\\
&=\prod_{t\in \mathrm{face}(v_0v_1v_2)}c^{\varepsilon_\circlearrowleft^{v_0v_1v_2}}_{t+v_0-v_1},
\end{aligned}
\end{equation}
where the last equality follows from~\eqref{eq:XExample}.
\end{proof}



\begin{lemma}\label{lemma:XandDiamonds} One can express the $X$-coordinates in terms of diamond coordinates: 
\begin{equation}
X_t=\left(\frac{d^{v_0v_1v_2}_{t-v_0-v_1}}{d^{v_0v_1v_2}_{t-v_0-v_2}}\right)^{\varepsilon_\circlearrowleft^{v_0v_1v_2}}
\end{equation}
Here $t$ is a face point spanned by $v_0$, $v_1$ and $v_2$. 
\end{lemma}
\begin{proof}
It is enough to prove this for $t=(t_0,t_1,t_2,0)$. Since
\begin{equation}
d^{012}_{t-e_0-e_1}=-\frac{c_{t+e_0-e_1}c_{t+e_2-e_0}}{c_tc_{t+e_2-e_1}},\qquad d^{012}_{t-e_0-e_2}=-\frac{c_{t+e_0-e_2}c_{t+e_1-e_0}}{c_{t+e_1-e_2}c_t},
\end{equation}
the result follows from~\eqref{eq:XExample}.
\end{proof}


\begin{figure}[htb]
\begin{center}
\begin{minipage}[b]{0.45\textwidth}
\begin{center}
\scalebox{0.7}{
\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(208.12001,210.18179)
 \put(0,0){\includegraphics{figures_gen/XCoords_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(102.24712,110.4214){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.68264pt}
\textcolor{inkcol1}{\Large{$t$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\end{center}
\end{minipage}
\hfill
\begin{minipage}[b]{0.45\textwidth}
\begin{center}
\scalebox{0.7}{
\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(208.12001,210.18179)
 \put(0,0){\includegraphics{figures_gen/diamondCoordinatesCancellationXCoords_included}}
 \end{picture}
\endgroup
}
\end{center}
\end{minipage}\\
\begin{minipage}[t]{0.45\textwidth}
\caption{Exponents of the Ptolemy coordinates involved in the $X$-coordinate at $t$.}
\end{minipage}
\begin{minipage}[t]{0.45\textwidth}
\begin{center}
\caption{An $X$-coordinate as a quotient of two diamond coordinates.}
\end{center}
\end{minipage}
\end{center}
\end{figure}



\subsection{From natural $(\SL(n,\C),N)$-cocycles to natural $(\PGL(n,\C),B,H)$-cocycles.}

The natural map $\pi\colon\SL(n,\C)\to\PGL(n,\C)$ induces a map from decorations by $N$-cosets to decorations by $B$-cosets. Given a generic $\SL(n,\C)/N$-decoration $D$ on $\Delta_n^3$, we show how the natural $(\PGL(n,\C),B,H)$-cocycle $\mathcal L_{\alpha\beta\gamma}(\pi(D))$ can be obtained from the natural cocycle $\mathcal L_{\alpha\beta}(D)$ by the coboundary action \eqref{eq:CoboundaryAction} of an explicit coboundary given in terms of the diamond coordinates. This defines the map $\tau$ in diagram~\eqref{eqn:DiagramIntro} and gives rise to an explicit formula for $\mathcal L_{\alpha\beta\gamma}(\pi(D))$ in terms of the shapes.




Given an $\SL(n,\C)/N$-decoration $D$ with diamond coordinates $d^{v_0,v_1,v_2}_{1,i}$ consider the $0$-cochain on $\overline{\overline{\Delta^3_n}}$ given by
\begin{equation}
\tau^{v_0v_1v_2}(D) = \begin{pmatrix}\prod_{i=1}^{n-1} d^{v_0v_1v_2}_{1,i} \\ & \prod_{i=2}^{n-1} d^{v_0v_1v_2}_{1,i} \\ & & \ddots \\ & & & d^{v_0v_1v_2}_{1,n-i} \\ & & & & 1\end{pmatrix}=\prod_{i=1}^{n-1}H_i(d^{v_0v_1v_2}_{1,i}).
\end{equation}
We shall make use of the abbreviations
\begin{equation}
X_{k,i}=X_{kv_2+iv_0+(n-k-i)v_1}^{v_0v_1v_2},\qquad z_i=z_{(i-1)v_0+(n-1-i)v_1}^{v_0+v_1}.
\end{equation}

\begin{theorem}\label{thm:NaturalCocycleShapes}
Let $D$ be a generic $\PGL(n,\C)/B$-decoration of $\Delta^3_n$. The natural cocycle $\mathcal L_{\alpha\beta\gamma}(D)$ is given by
\begin{equation}\label{eq:NaturalCocycleFormula}
\begin{gathered}
\alpha^{v_0v_1v_2}=q_1,\qquad \beta^{v_0v_1v_2}=\prod_{k=1}^{n-1}\left(\prod_{i=1}^{n-k}x_i(1)\prod_{i=1}^{n-k-1}H_i(X_{k,i}^{\varepsilon^{v_0v_1v_2}_\circlearrowleft})\right)d_{\pm 1}\\
\gamma^{v_0v_1v_2}=\prod_{i=1}^{n-1}H_i(z_{i}^{-\varepsilon_\circlearrowleft^{v_0v_1v_2}}).
\end{gathered}
\end{equation}
Moreover, if $\widetilde D$ is any $\SL(n,\C)/N$-decoration lifting $D$, $\mathcal L(D)=\tau \mathcal L_{\alpha\beta}(\widetilde D)$.\qed
\end{theorem}

Before embarking on the proof, we give some examples.

\begin{example}For $n=2$,
\begin{equation}
\beta^{012}=x_1(1)d_{\pm 1}=\begin{pmatrix}-1&1\\&1\end{pmatrix},\qquad \gamma^{012}=H_1(z_1^{-1})=\begin{pmatrix}z_1^{-1}&\\&1\end{pmatrix}.
\end{equation}
For $n=3$, we have
\begin{equation}
\begin{gathered}
\beta^{012}=x_1(1)x_2(1)H_1(X_{1,1})x_1(1)d_{\pm 1}=
\begin{pmatrix}X_{1,1}&-X_{1,1}&1\\&-1&1\\&&1\end{pmatrix},
\\\gamma^{012}=
H_1(z_1^{-1})H_2(z_2^{-1})=\begin{pmatrix}z_1^{-1}z_2^{-1}&&\\&z_2^{-1}&\\&&1\end{pmatrix}.
\end{gathered}
\end{equation}
For $n=4$,
\begin{equation}
\begin{gathered}
\beta^{012}=x_1(1)x_2(1)x_3(1)H_1(X_{1,1})H_2(X_{1,2})x_1(1)x_2(1)H_1(X_{2,1})x_1(1)d_{\pm 1}\\ \gamma^{012}=d(z_1^{-1}z_2^{-1}z_3^{-1},z_2^{-1}z_3^{-1},z_3^{-1},1).
\end{gathered}
\end{equation}
\end{example}

\begin{remark}
The formula for $\beta^{v_0v_1v_2}$ is inspired by \cite[(9.14)]{FockGoncharov}.
\end{remark}

\begin{remark}\label{rm:DiagonalEntries}
Note that the diagonal entries of $\beta^{v_0v_1v_2}$ and $\gamma^{v_0v_1v_2}$ are given by
\begin{equation}
\beta^{v_0v_1v_2}_{ll}=(-1)^{n-l}\prod_{i=l}^{n-2}\prod_{k=1}^{n-1-i}X_{k,i}^{\varepsilon_\circlearrowleft^{v_0v_1v_2}},\quad \gamma_{ll}^{v_0v_1v_2}=\prod_{i=l}^{n-1}z_i^{-\varepsilon_\circlearrowleft^{v_0v_1v_2}}.
\end{equation}
\end{remark}

\begin{proof}[Proof of Theorem~\ref{thm:NaturalCocycleShapes}]
We prove that $\tau(\widetilde D)\mathcal L_{\alpha\beta}(\widetilde D)$ is given by~\eqref{eq:NaturalCocycleFormula}.
Since the last column of $\prod_{i=1}^{n-1}x_i(1)$ consists of $1$'s and since none of the other terms affect the last column, the middle edges are thus normalized, so by Lemma~\ref{lemma:UniversalProperty}, the cocycle is indeed the natural cocycle of $D$. 

Let $\widetilde \alpha$, $\widetilde \beta$ (and $\widetilde \gamma=\id$) be the labelings, of long, middle and short edges given by $L_{\alpha\beta}(\widetilde D)$. By Proposition~\ref{prop:NaturalCocycleLongShort} these are given by \eqref{eq:betaTrunc}. Let $\tau=\tau(\widetilde D)$.

\textit{Long edges:}
We must prove that $(\tau^{v_0v_1v_2})^{-1}\widetilde\alpha^{v_0v_1v_2}\tau^{v_1v_0v_2}=q_1$.
Letting 
\begin{equation}
l_k=\prod_{i=k}^{n-1}d^{v_0v_1v_2}_{1,i},\quad m_k=(-1)^{k-1}e^{v_0v_1}_{(n-k)v_0+(k-1)v_1},\quad r_k=\prod_{i=k}^{n-1}d^{v_1v_0v_2}_{1,i},
\end{equation}
this is equivalent to proving that
\begin{equation}
d(l_1,\dots,l_n)^{-1}q(m_1,\dots,m_n)d(r_1,\dots,r_n)=q_1\in\PGL(n,\C).
\end{equation}


Hence, we must prove that $l_{n-k+1}^{-1}m_kr_k$ is independent of $k$. From Figure~\ref{fig:Cancellations} it follows that
\begin{equation}
\prod_{i=k}^{n-1}d^{v_0v_1v_2}_{1,i}=\varepsilon^{n-k}\frac{c_{nv_0}c_{(k-1)v_0+(n-k)v_1+v_2}}{c_{(n-1)v_0+v_2}c_{kv_0+(n-k)v_1}},\quad \prod_{i=k}^{n-1}d^{v_1v_0v_2}_{1,i}=(-\varepsilon)^{n-k}\frac{c_{nv_1}c_{(k-1)v_1+(n-k)v_0+v_2}}{c_{(n-1)v_1+v_2}c_{kv_1+(n-k)v_1}}
\end{equation}
where $\varepsilon=-\varepsilon_<^{v_0,v_1,v_2}$. Hence, we have
\begin{equation}
\begin{gathered}
l_{n-k+1}=\varepsilon^{k-1}\frac{c_{(n-k)v_0+(k-1)v_1+v_2}}{c_{(n-k+1)v_0+(k-1)v_1}c_{(n-1)v_0+v_2}},\quad m_k=(-1)^{k-1}\frac{c_{(n-k)v_0+kv_1}}{c_{(n-k+1)v_0+(k-1)v_1}}\\
r_k=(-\varepsilon)^{n-k}\frac{c_{(k-1)v_1+(n-k)v_0+v_2}}{c_{(n-1)v_1+v_2}c_{kv_1+(n-k)v_0}},
\end{gathered}
\end{equation}
from which it follows that
\begin{equation}
l_{n-k+1}^{-1}m_kr_k=(-\varepsilon)^{n-1}\frac{c_{(n-1)v_0+v_2}}{c_{(n-1)v_1+v_2}},
\end{equation}
which is independent of $k$. This proves the result.


\begin{figure}[htb]
\begin{center}
\scalebox{0.75}{
\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(214.43935,222.36778)
 \put(0,0){\includegraphics{figures_gen/diamondCoordinatesCancellation_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(50.41531,48.36835){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.68264pt}
\textcolor{inkcol1}{\normalsize{$d_{1,n-1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(-0.861329,21.30677){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{97.813064pt}
\textcolor{inkcol1}{\LARGE{$v_0$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(196.480221,21.33484){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{97.813064pt}
\textcolor{inkcol1}{\LARGE{$v_2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(99.003791,226.86986){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{97.813064pt}
\textcolor{inkcol1}{\LARGE{$v_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(83.9728,108.44327){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.68264pt}
\textcolor{inkcol1}{\normalsize{$d_{1,k+1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(98.5222,134.96072){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{129.68264pt}
\textcolor{inkcol1}{\normalsize{$d_{1,k}$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\end{center}
\caption{Cancellations.}\label{fig:Cancellations}
\end{figure}


\textit{Middle edges:} We must prove that $\tau^{-1}_{v_0v_1v_2}\widetilde\beta_{v_0v_1v_2}\tau_{v_0v_2v_1}=\beta_{v_0v_1v_2}$.
Using the basic commutator relations
\begin{equation}\label{eq:CommutatorRelations}
H_i(x)x_j(y)=x_j(y)H_i(x) \text{ if } i\neq j, \quad x_i(y)=H_i(y)x_i(1)H_i(y)^{-1}
\end{equation}
the expression
\begin{equation}
\widetilde\beta^{v_0v_1v_2}=\prod_{k=1}^{n-1}\prod_{i=1}^{n-k}x_i(d_{k,i})=\prod_{k=1}^{n-1}\prod_{i=1}^{n-k}H_i(d_{k,i})x_i(1)H_i(d_{k,i})^{-1}
\end{equation}
expands to
\begin{equation}\label{eq:AuxMiddle1}

\widetilde\beta^{v_0v_1v_2}=\prod_{k=1}^{n-1}\left(\prod_{i=1}^{n-k}H_i(d_{k,i})\prod_{i=1}^{n-k}x_i(1)\left(\prod_{i=1}^{n-k-1}H_i(d_{k,i})^{-1}\right) H_{n-k}(d_{k,n-k})^{-1}\right).
\end{equation}
We have for brevity omitted the superscript $v_0v_1v_2$ of the diamond coordinates. Letting $$\mathcal H_k=\prod_{i=1}^{n-k}H_i(d_{k,i})\quad\mbox{and}\quad \mathcal H'_k=\prod_{i=1}^{n-k-1}H_i(d_{k,i}),$$
and moving the terms $H_{n-k}(d_{k,n-k})^{-1}$ to the right, we have
\begin{equation}
\widetilde\beta^{v_0v_1v_2}=\prod_{k=1}^{n-1}\left(\mathcal H_k\left(\prod_{i=1}^{n-k}x_i(1)\right)\mathcal H'^{-1}_k\right) \prod_{k=1}^{n-1}  H_{n-k}(d_{k,n-k})^{-1}.
\end{equation}
Since $\mathcal H_n=1$, the product $(\mathcal H_1\cdots \mathcal H'^{-1}_1)(\mathcal H_2 \cdots \mathcal H'^{-1}_2)\cdots$ equals $\mathcal H_1 (\cdots \mathcal H'^{-1}_1 \mathcal H_2)(\cdots \mathcal H'^{-1}_2 \mathcal H_3)\cdots$, and we obtain 
\begin{equation}
\widetilde\beta_{v_0v_1v_2}=\mathcal{H}_1\prod_{k=1}^{n-1}\left(\left(\prod_{i=1}^{n-k}x_i(1)\right)\mathcal H'^{-1}_k \mathcal H_{k+1}\right) \prod_{k=1}^{n-1}  H_{n-k}(d_{k,n-k})^{-1}.
\end{equation}
Using \eqref{eq:DiamondDef}, we have
\begin{equation}\label{eq:AuxMiddle2}
d_{1,i}^{v_0v_2v_1}=d_{(i-1)v_0+(n-1-i)v_2}^{v_0v_2v_1}=-d_{(i-1)v_0+(n-1-i)v_2}^{v_0v_1v_2}=-d_{n-i,i}^{v_0v_1v_2},
\end{equation}
and since (last equality follows from~\eqref{eq:AuxMiddle2})
\begin{equation}
\tau^{v_0v_1v_2}=\prod_{i=1}^{n-1}H_i(d^{v_0v_1v_2}_{1,i})=\mathcal H_1,\qquad \tau^{v_0v_2v_1}=\prod_{i=1}^{n-1}H_i(d^{v_0v_2v_1}_{1,i})=\prod_{k=1}^{n-1}H_{n-k}(-d_{k,n-k}).
\end{equation}
we have
\begin{equation}
\beta_{v_0v_1v_2}=\tau^{-1}_{v_0v_1v_2}\widetilde\beta_{v_0v_1v_2}\tau_{v_0v_2v_1} = \prod_{k=1}^{n-1}\left(\left(\prod_{i=1}^{n-k}x_i(1)\right)\mathcal H'^{-1}_k \mathcal H_{k+1}\right)d_{\pm 1}.
\end{equation}
By Lemma~\ref{lemma:XandDiamonds}, $\frac{d_{k+1,i}}{d_{k,i}}=X_{k,i}^{\varepsilon_\circlearrowleft(v_0v_1v_2)}$, so that
\begin{equation}
\mathcal H'^{-1}_k \mathcal H_{k+1} = \prod_{i=1}^{n-k} H_i(d_{k,i})^{-1} H_i(d_{k+1,i}) = \prod_{i=1}^{n-k} H_i(X_{k,i}^{\varepsilon_\circlearrowleft(v_0v_1v_2)}).
\end{equation}
This proves the result.



\textit{Short edges:} We must prove that $(\tau^{v_0v_1v_2})^{-1}\tau^{v_0v_1v_3}=\gamma^{v_0v_1v_2}$. We have
\begin{equation}
(\tau^{v_0v_1v_2})^{-1}\tau^{v_0v_1v_3}=\left(\prod_{i=1}^{n-1}H_i(d^{v_0v_1v_2}_{1,i})\right)^{-1}\prod_{i=1}^{n-1}H_i(d^{v_0v_1v_3}_{1,i})=\prod_{i=1}^{n-1}H_i(\frac{d^{v_0v_1v_3}_{1,i}}{d^{v_0v_1v_2}_{1,i}}).
\end{equation}
The result now follows from Lemma~\ref{ShapesandDiamonds} below.

\begin{lemma}\label{ShapesandDiamonds}
The shape parameters in \eqref{eq:NaturalCocycleFormula} are given in terms of diamond coordinates:
\begin{equation}
z_{i}^{-\varepsilon^{v_0v_1v_2}_\circlearrowleft}=\frac{d^{v_0v_1v_3}_{1,i}}{d^{v_0v_1v_2}_{1,i}}
\end{equation}
\end{lemma}

\begin{proof}
Let $\alpha=(i-1)v_0+(n-1-i)v_1$, so that $z_i=z^{v_0+v_1}_{\alpha}$ and $d^{v_0v_1v_k}_{1,i}=d^{v_0v_1v_k}_\alpha$, $k=2,3$. By compatibility under reordering, it is enough to prove the result for $v_i=i$. We have
\begin{equation}
z^{1100}_{\alpha}=\frac{c_{\alpha+e_0+e_3}c_{\alpha+e_1+e_2}}{c_{\alpha+e_0+e_2}c_{\alpha+e_1+e_3}},\qquad d^{01k}_\alpha=-\frac{c_{\alpha+2e_0}c_{\alpha+e_1+e_k}}{c_{\alpha+e_0+e_1}c_{\alpha+e_0+e_k}}.
\end{equation}
Hence, $z_i^{-1}=d^{013}_{1,i}/d^{012}_{1,i}$ proving the result.
\end{proof}
This concludes the proof of Theorem~\ref{thm:NaturalCocycleShapes}.
\end{proof}

\begin{remark}\label{rm:NaturalLift}
Theorem~\ref{thm:NaturalCocycleShapes} implies that for a generic $\PGL(n,\C)/B$-decoration on $(M,\T)$, the restriction of the natural cocycle to $\partial M$ has a canonical lift to a cocycle with values in $B\subset\GL(n,\C)$ (not just in $\PGL(n,\C)$).
\end{remark}

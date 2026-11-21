---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-019-52-the-non-degenerate-pairing
section_title: "The non-degenerate pairing"
section_number: 5.2
pages: 41-44
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.731
latex_coverage_ratio: 0.934
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:Dual:pairing}
Recall that a Hopf pairing between two Hopf algebras $\cA$ and $\cA^*$ is a non-degenerate pairing such that
\Eq{\label{pairingdef}\<a, xy\> = \<\D(a),x\ox y\>,\tab \<ab,x\>=\< a\ox b, \D(x)\>.}
for $a,b\in\cA, x,y\in\cA^*$. (In this paper we will not consider counit and antipode in the pairing.)

In the current setting, we have the pairing between $\cA_q$ and $\cA_q^*$ from the compact case:
$$\<A,X\>=q^{-2},\tab \<B,X\>=0,$$
$$\<A,Y\>=0,\tab \<B,Y\>=c\in\C,$$
where $c$ is any complex number.

The pairings between $A,B$ and $\hat{A}=X\inv,\hat{B}=q\inv YX\inv$ are given by
$$\<A,\hat{A}\>=q^{2},\tab \<B,\hat{A}\>=0,$$
$$\<A,\hat{B}\>=0,\tab \<B,\hat{B}\>=cq:=c'.$$
We will choose $c'=1$.
From this it is extended to
$$\< B^mA^n,\hat{A}\>=q^{2n}\d_{m0},\tab\<B^mA^n ,\hat{B}\>=\d_{m1},$$
and then to
$$\<B^mA^n ,\hat{B}^{m'}\hat{A}^{n'}\>=q^{2n'(n+m)}[m]_q! \d_{mm'},$$
where $[m]_q!:=[m]_q[m-1]_q...[1]_q$ is the $q$-factorial, and $[m]_q=\frac{q^{m}-q^{-m}}{q-q\inv}$ is the $q$-number.

From the analogy between the quantum dilogarithm $G_b$ and the $\G_q$ function established in \cite{Ip}, we prove the following theorem:

\begin{Thm} The Hopf pairing between $\cA$ and $\cA^*\simeq \hat{\cA}^{cop}$ is given by
\begin{eqnarray}
&&\label{pairing1}\<\iint g(s,t) B^{ib\inv t}A^{ib\inv s}dsdt, \iint \hat{f}(s,t)\hat{B}^{ib\inv t}\hat{A}^{ib\inv s}dsdt\>\nonumber\\
&=&\iiint g(s,t)\hat{f}(s',t)G_b(Q+it)e^{-2\pi is'(s+t)} ds'dsdt\\
&&\<\iint g(s,t) A^{ib\inv s}B^{ib\inv t}dsdt, \iint \hat{f}(s,t)\hat{B}^{ib\inv t}\hat{A}^{ib\inv s}dsdt\>\nonumber\\
&=&\label{pairing}\iiint g(s,t)\hat{f}(s',t)G_b(Q+it)e^{-2\pi is'(s+t)}e^{-2\pi ist}ds'dsdt,
\end{eqnarray}
or using the Mellin transformed picture (see Remark \ref{MellinQ}):
\begin{eqnarray}
&&\<\int f(t) B^{ib\inv t}g(\log A)dt, \iint \hat{f}(s,t)\hat{B}^{ib\inv t}\hat{A}^{ib\inv s}dsdt\>\nonumber\\
&=&\label{pairing2}\iint g(-2\pi bs')\hat{f}(s',t)f(t)G_b(Q+it)e^{-2\pi its'}ds'dt\\
&&\<\int g(\log A)f(t) B^{ib\inv t}dt, \iint \hat{f}(s,t)\hat{B}^{ib\inv t}\hat{A}^{ib\inv s}dsdt\>\nonumber\\
&=&\iint g(-2\pi b(s'+t))\hat{f}(s',t)f(t)G_b(Q+it)e^{-2\pi its'}ds'dt.
\end{eqnarray}
Here the Hopf pairing between two $C^*$-algebra are defined by naturally extending the pairing in the defining relations \eqref{pairingdef} to a pairing between the multiplier algebras $M(\cA\ox\cA)$ and $M(\cA^*\ox\cA^*)$.
\end{Thm}

\begin{proof} It suffices to show that 
\Eq{\< f, \hat{g}\hat{h}\> = \<\D(f),\hat{g}\ox\hat{h}\>.}
The other relations are similar by duality.
We will prove the first form \eqref{pairing}. For simplicity we omit all the integrations after the pairing. Every variable is to be integrated.
\begin{eqnarray*} 
LHS&=&\<f(s,t), \iint \hat{g}(s-s',t-t')\hat{h}(s',t')e^{2\pi i(s-s')t'} ds'dt'\>\\
&=& f(s,t)\hat{g}(s''-s',t-t')\hat{h}(s',t')e^{2\pi i(s''-s')t'}G_b(Q+it)e^{-2\pi is'' (s+t)}e^{-2\pi ist}\\
&=& f(s,t)\hat{g}(s''-s',t-t')\hat{h}(s',t')G_b(Q+it)e^{2\pi i(s''-s')t'}e^{-2\pi is'' (s+t)}e^{-2\pi ist},\\
RHS&=&\<f(s_1,t_1+t_2)\frac{G_b(-it_1)G_b(-it_2)}{G_b(-it_1-it_2))}\d(s_2,s_1+t_1),\hat{g}(s_1,t_1)\hat{h}(s_2,t_2)\>\\
&=&f(s_1,t_1+t_2)\frac{G_b(-it_1)G_b(-it_2)}{G_b(-it_1-it_2)}G_b(Q+it_1)G_b(Q+it_2) \d(s_2,s_1+t_1)\\
&&\hat{g}(s_1',t_1)\hat{h}(s_2',t_2)e^{-2\pi is_1'(s_1+t_1)}e^{-2\pi is_2'(s_2+t_2)}e^{-2\pi is_1t_1}e^{-2\pi is_2t_2}\\
&=&f(s_1,t_1+t_2)\hat{g}(s_1',t_1)\hat{h}(s_2',t_2)G_b(Q+it_1+it_2)e^{-2\pi is_2't_2}e^{-2\pi is_1(t_1+t_2)}e^{-2\pi i(s_1+t_1)(s_1'+s_2')},\\
\end{eqnarray*}
where we used the reflection properties \eqref{reflection} of the $G_b$ function: 
\Eq{\frac{G_b(-is)G_b(-it)}{G_b(-is-it)}=\frac{G_b(Q+is+it)e^{2\pi ist}}{G_b(Q+is)G_b(Q+it)}.}
Now shifting $t_1\mapsto t_1-t_2,s_1'\mapsto s_1'-s_2'$, we obtain
\begin{eqnarray*}
&=&f(s_1,t_1)\hat{g}(s_1'-s_2',t_1-t_2)\hat{h}(s_2',t_2)G_b(Q+it_1)e^{-2\pi is_2't_2}e^{-2\pi is_1t_1}e^{-2\pi is_1'(s_1+t_1-t_2)}\\
&=&f(s_1,t_1)\hat{g}(s_1'-s_2',t_1-t_2)\hat{h}(s_2',t_2)G_b(Q+it_1)e^{2\pi i(s_1'-s_2')t_2}e^{-2\pi is_1'(s_1+t_1)}e^{-2\pi is_1t_1}.\\
\end{eqnarray*}
Hence we see that the expression is equal on renaming $s_1=s,t_1=t,s_1'=s'', s_2'=s'$ and $t_2=t'$.
\end{proof}
With the pairing established, we can prove the density condition needed in order for $\cA$ to be a locally compact quantum group.

\begin{Thm}\label{density} We have
\begin{eqnarray}
\cA&=&span\{(\w\ox1)\D(a)|\w\in\cA^*,a\in\cA\}^{closure}\\
&=&span\{(1\ox\w)\D(a)|\w\in\cA^*,a\in\cA\}^{closure}.
\end{eqnarray}
\end{Thm}
\begin{proof}
We will prove that $(\w\ox 1)\D(a)$ is dense in $1\ox\cA$, while the other statement is similar. Let us write
\begin{eqnarray*}
\w&=&\iint \hat{f}(s,t)\hat{B}^{ib\inv t}\hat{A}^{ib\inv s}dsdt\in\cA^*\\
a&=&\iint g(s,t) A^{ib\inv s}B^{ib\inv t}dsdt\in\cA.
\end{eqnarray*}
Using Proposition \ref{coprod}, the required pairing is (here we understood that it is an element in $1\ox\cA$ with coordinates $s_2,t_2$, and that all integrations converge absolutely with the appropriate contours):
\begin{flalign*}
&\<g(s_1,t_1+t_2)\frac{G_b(-it_1)G_b(-it_2)}{G_b(-i(t_1+t_2))}\d(s_2,s_1+t_1), \hat{f}(s,t)\>&\\
&=\iiint \hat{f}(s',t_1)g(s_1,t_1+t_2)\frac{G_b(-it_1)G_b(-it_2)}{G_b(-i(t_1+t_2))}G_b(Q+it_1)\d(s_2,s_1+t_1)e^{-2\pi is'(s_1+t_1)}ds'ds_1dt_1&\\
&=\iint \hat{f}(s',t_1)g(s_2-t_1,t_1+t_2)\frac{G_b(-it_2)}{G_b(-i(t_1+t_2))}e^{-2\pi is's_2}e^{\pi it_1^2-\pi t_1Q}ds'dt_1.&
\end{flalign*}
Now if we choose $\hat{f}(s',t_1)=\hat{f_1}(s')\hat{f_2}(t_1)$, the integration over $s'$ is just the Fourier transform $\hat{\cF}_1(s_2)$ of $\hat{f_1}(s')$, and we get
\begin{flalign*}
&=\int \hat{\cF}_1(s_2)\hat{f_2}(t_1)g(s_2-t_1,t_1+t_2)\frac{G_b(-it_2)}{G_b(-i(t_1+t_2))}e^{\pi it_1^2-\pi t_1Q}dt_1.&
\end{flalign*}
Finally we can choose any nice approximation of identity for $\hat{f_2}(t_1)\to\d(t_1)$, then in the limit we obtain simply
\begin{flalign*}
&\to\hat{\cF}_1(s_2)g(s_2,t_2),&
\end{flalign*}
which is then obviously all of $1\ox\cA$ for different choices of $\hat{\cF}$ and $g$.
\end{proof}
\begin{Cor} $\cA$ is a locally compact quantum group in the sense of \cite{KV1,KV2}.
\end{Cor}


\subsection{The GNS description}\label{sec:Dual:GNS}
Given our multiplicative unitary 
\Eq{W=e^{\frac{i}{2\pi b^2}\log A\inv\ox \log \hat{A}}g_b(B \ox q\hat{B}\hat{A}\inv)\in M(\cA \ox \cB(\cH)),} 
the space $\hat{\cA}\sub \cB(\cH)$ is originally defined to be
\Eq{ \hat{\cA}=\{ (\w\ox 1)W: \w\in \cA^*\}^{\mbox{norm closure}}.}
In order to find the GNS representation $\hat{\L}$ of $\hat{\cA}$ on the original space $\cH_L$, we introduce the contraction map $\l$ \cite[(8.2)]{KV1} which relates $\cA^*$ to the definition of $\hat{\cA}$ above using the multiplicative unitary, and the $\xi$ map \cite[Notation 8.4]{KV1}, which relates $\cA^*$ to the original GNS representation space $\cH_L$ of $\cA$ by the Riesz's theorem for Hilbert spaces. Then $\hat{\L}$ is just the composition of the two maps, which is naturally compatible with the previous GNS construction for $\cA$.
\begin{Def}
For $\w\in \cA^*, x\in\cA$, we define
\begin{eqnarray}
\l&:&\cA^*\to \hat{\cA}\nonumber\\
\l(\w)&=&(\w\ox 1)W.
\end{eqnarray}
and
\begin{eqnarray}
\xi&:&\cA^*\to \cH_L\nonumber\\
\w(x^*)&=&\<\xi(\w),\L(x)\>_L
\end{eqnarray}
Then the GNS map $\hat{\L}$ is given by
\begin{eqnarray}
\hat{\L}&:&\hat{\cA}\to \cH_L\nonumber\\
\hat{\L}(\l(\w))&=&\xi(\w).
\end{eqnarray}
\end{Def}


\begin{Prop}\label{lamda} $\l$ is the identity map from $\cA^*$ to $\hat{\cA}$ as elements in $\cB(\cH)$.
\end{Prop}
\begin{proof} Using the second form \eqref{W2} for $W$, and the integral form \eqref{gb2} for $g_b$, we get
$$W=\left(\int_{\R+i0} \frac{B^{ib\inv\t}A^{-ib\inv\t}\ox \hat{B}^{ib\inv\t}}{G_b(Q+i\t)}d\t\right)e^{\frac{i}{2\pi b^2}\log A\inv\ox\log \hat{A}}.$$
By the pairing \eqref{pairing} we have
\begin{eqnarray*}
\l(\w)&=&\left(\iint \hat{f}(s,t)\hat{B}^{ib\inv t}\hat{A}^{ib\inv s}dsdt\ox 1\right) (W)\\
&=&  \iint \hat{f}(s,t) \frac{(q^{2ib\inv s})^{-ib\inv t}}{G_b(Q+it)} G_b(Q+it)e^{-2\pi ist}\hat{B}^{ib\inv t}  \hat{A}^{\frac{i}{2\pi b^2} (2\pi bs)}dsdt\\
&=& \iint \hat{f}(s,t)\hat{B}^{ib\inv t} \hat{A}^{ib\inv s}dsdt.
\end{eqnarray*}
\end{proof}

\begin{Prop}
The map $\xi:\cA^*\sub\hat{\cH}\to \cH$ is given by:
\Eq{\xi:\hat{f}(s,t)\mapsto F(s,t):=\int_\R \hat{f}(s',iQ-t)G_b(-it)e^{2\pi i s'(s+t-iQ)}ds',}
it naturally extends to an invertible map $\xi:\hat{\cH}\to\cH$ with the inverse given by
\Eq{\xi\inv:F(s,t)\mapsto \hat{f}(s,t):=\int_\R \frac{F(s',iQ-t)}{G_b(Q+it)}e^{2\pi is(t-s')}ds'.}
\end{Prop}
\begin{proof}
Let $\w=\iint \hat{f}(s,t)\hat{B}^{ib\inv t}\hat{A}^{ib\inv s}dsdt, x= \iint g(s,t)A^{ib\inv s}B^{ib\inv t}dsdt$. Then
\begin{eqnarray*}
\w(x^*)&=&\<\xi(\w),\L(x)\>_L\\
LHS&=& \iiint \over[g](-s,-t)e^{2\pi ist}F(s',t)G_b(Q+it)e^{-2\pi is's-2\pi is't-2\pi ist}ds'dsdt\\
&=& \iiint \over[g](-s,-t)F(s',t)G_b(Q+it)e^{-2\pi is's-2\pi is't}ds'dsdt\\
RHS&=&\iint \overline{g(\over[s],\over[t]+\frac{iQ}{2})}\xi(\w)(s,t+\frac{iQ}{2})dsdt\\
&=&\iint \over[g](s,t-\frac{iQ}{2})\xi(\w)(s,t+\frac{iQ}{2})dsdt\\
&=&\iint \over[g](-s,-t)\xi(\w)(-s,-t+iQ)dsdt.
\end{eqnarray*}
Hence
\begin{eqnarray*}
\xi(\w)(s,t)&=&\int F(s',iQ-t)G_b(Q+i(iQ-t))e^{2\pi is's-2\pi is'(iQ-t)}ds'\\
&=&\int F(s',iQ-t)G_b(-it)e^{2\pi i s'(s+t-iQ)}ds'.
\end{eqnarray*}
We observe that $\xi$ can be realized as
$$\xi=\cF_s\circ P_t\circ G_b(Q+it)e^{-2\pi ist},$$
where $\cF_s$ is Fourier transform on $s$, $P_t f(t):=f(iQ-t)$ and $G_b(Q+it)e^{-2\pi ist}$ is just multiplication by this function. Hence we have
$$\xi\inv=G_b(Q+it)\inv e^{2\pi ist}\circ P_t\inv\circ \cF_s\inv,$$
or the formula desired.
\end{proof}

\begin{Prop} $\xi$ is an isometry, $\xi:\hat{\cH}\to \cH$.
\end{Prop}
\begin{proof} We have
\begin{eqnarray*}
&&\<\xi(\hat{f}),\xi(\hat{g})\>_L\\
&=&\int_\R\int_\R \overline{\hat{g}(s'',iQ-(t+\frac{iQ}{2}))G_b(-i(t+\frac{iQ}{2}))e^{2\pi is''(s+(t+\frac{iQ}{2})-iQ)}}\\
&& \hat{f}(s',iQ-(t+\frac{iQ}{2}))G_b(-i(t+\frac{iQ}{2}))e^{2\pi is'(s+(t+\frac{iQ}{2})-iQ)}ds'ds''dsdt\\
&=&\int_\R\int_\R \overline{\hat{g}(s'',-t+\frac{iQ}{2})G_b(\frac{Q}{2}-it)}e^{-2\pi is''(s+t+\frac{iQ}{2})}\\
&& \hat{f}(s',-t+\frac{iQ}{2})G_b(\frac{Q}{2}-it)e^{2\pi is'(s+t-\frac{iQ}{2})}ds'ds''dsdt\\
&=&\int_\R\int_\R \overline{\hat{g}(s'',t+\frac{iQ}{2})}\hat{f}(s',t+\frac{iQ}{2})e^{-2\pi is''(s-t+\frac{iQ}{2})}e^{2\pi is'(s-t-\frac{iQ}{2})}ds'ds''dsdt\\
&=&\int_\R\int_\R \overline{\hat{g}(s'',t+\frac{iQ}{2})}\hat{f}(s',t+\frac{iQ}{2})e^{-2\pi is''(-t+\frac{iQ}{2})}e^{2\pi is'(-t-\frac{iQ}{2})}e^{2\pi is(-s''+s')}ds'ds''dsdt\\
&=&\int_\R\int_\R \overline{\hat{g}(s,t+\frac{iQ}{2})}\hat{f}(s,t+\frac{iQ}{2})e^{-2\pi is(-t+\frac{iQ}{2})}e^{2\pi is(-t-\frac{iQ}{2})}dsdt\\
&=&\int_\R\int_\R\overline{\hat{g}(s,t+\frac{iQ}{2})}\hat{f}(s,t+\frac{iQ}{2})e^{2\pi Qs}dsdt\\
&=&\int_\R\int_\R \overline{\hat{g}(s,t+\frac{iQ}{2})}\hat{f}(s,t+\frac{iQ}{2})e^{2\pi Qs}dsdt\\
&=&\<\hat{f},\hat{g}\>_{\hat{L}}.
\end{eqnarray*}
\end{proof}

Hence we conclude that
\begin{Cor} $\hat{\L}(\w):=\xi(\w)$ gives the GNS representation for $\hat{\cA}$ on $\cH$ as desired.
\end{Cor}

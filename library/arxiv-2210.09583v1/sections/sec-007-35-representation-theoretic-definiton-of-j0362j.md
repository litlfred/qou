---
doc_id: arxiv-2210.09583v1
doc_title: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT"
section_id: sec-007-35-representation-theoretic-definiton-of-j0362j
section_title: "Representation theoretic definiton of J'0362J"
section_number: 3.5
pages: 9-12
source_pdf: 2210.09583v1.pdf
source_sha256: 38fc6fa465a06a7b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.701
latex_coverage_ratio: 0.948
doc_brief: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT — There is a known connection between the osp(1|2n) polynomial knot invariant Jn K and the so(2n + 1) knot invariant soJn K studied by"
---
\label{Sec:Our-method}

For the purposes of categorification, we want to define the invariant $\hat{J}$ defined in section 1 using $U_{q,\pi}$-module homomorphisms.
To do this, we need to define $U_{q,\pi}$-module homomorphisms $u: \Q(q,t)^\tau \to V \otimes V$ and $n: V \otimes V \to \Q(q,t)^\tau$ satisfying the relation $\tau R_{1,1}=\tau \Id -q un$.
Then this gives the $\mf{sl}_2$ invariant in the variable $\tau^{-1}q$ as desired.




\begin{comment}
\begin{definition}
  Let $n:V\otimes V \to Q(q,t)^{\tau}$ be the odd $U_{q,\pi}$-module map given by $n:=\tau qtr \circ (1\otimes f)$
  \[
  V\otimes V \overset{1\otimes f}{\rightarrow} V\otimes V^* \overset{\tau qtr}{\to} Q(q,t)^\tau
  \]
  n is given by the matrix  $\begin{pmatrix}
                              0 & -\tau^3 & \tau^3q & 0
                            \end{pmatrix}$
\end{definition}
\end{comment}


\begin{definition}
 Let $n:V\otimes V \to \Q(q,t)^{\tau}$ be the odd $\Q(q,t)^\tau$-linear map defined on basis elements by
  \begin{align*}
    v_+\otimes v_+ \to 0 & \qquad v_+ \otimes v_- \to -\tau^3 \\
    v_- \otimes v_- \to 0 & \qquad v_- \otimes v_+ \to \tau^3 q
  \end{align*}
\end{definition}

\begin{theorem}
  $n$ is a odd weight $U_{q,\pi}$-module homomorphism.
\end{theorem}
\begin{proof}
  We need to show that $n(\Delta(E)v\otimes w)=n(\Delta(F)v\otimes w)=0$.
  We know that $\Delta(E)(v_+ \otimes v_+)=\Delta(F)(v_i \otimes v_-)=0$, so it holds in these cases.
  It is also trivial to see that $\Delta(E)(v_{\pm}\otimes v_{\mp}) \in span\{v_+ \otimes v_+\}$, which is sent to $0$ by $n$.
  Likewise, $\Delta(F)(v_{\pm}\otimes v_{\mp})\in span\{v_-\otimes v_-\}$, which is sent to $0$ by $n$.
  Thus, all that remains to check is that $\Delta(F)(v_+ \otimes v_+)$ and $\Delta(E)(v_-\otimes v_-)$ are sent to $0$ by $n$.

  \begin{align*}
    n((E\otimes 1 + JK \otimes E)(v_- \otimes v_-)) &= n(v_+ \otimes v_- +\pi JKv_-\otimes Ev_-)= n(v_+\otimes v_- + q^{-1}v_-\otimes v_+)=0 \\
    n((F\otimes K^{-1} + 1\otimes F)(v_+ \otimes v_+))&=n(q^{-1}v_- \otimes v_+ + v_+ \otimes v_-)=0\\
  \end{align*}
  Therefore, $n(\Delta(x)(v\otimes w))=x\cdot n(v\otimes w) = 0$ for all $x\in \{E,F\}$ and $v,w \in V$, which implies $n$ is a module homomorphism.
\end{proof}

We associate a blue cap with no orientation to this map
\begin{align}\label{n-draw}
  \hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue, -] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);

\end{tikzpicture}} & = n =
\begin{pmatrix}
     0 & -\tau^3 & \tau^3q & 0
  \end{pmatrix}
\end{align}

\begin{comment}
\begin{definition}
  Define $u:\Q(q,t)^{\tau}\to V\otimes V$ by the odd map $u=(1\otimes f^{-1})\circ coqtr$
  \begin{align}\label{blue-cup}
    u =(1 \otimes f^{-1})\circ coqtr \qquad 1 \to -\pi q^{-1}v_+ \otimes v_{-} + v_{-}\otimes v_{+}
  \end{align}
\end{definition}
\end{comment}

\begin{definition}
  Let $u:\Q(q,t)^\tau \to V \otimes V$ be the odd $\Q(q,t)^\tau$-linear map defined by
  \[
  1\to -\pi q^{-1}v_+ \otimes v_{-} + v_{-}\otimes v_{+}
  \]
\end{definition}

\begin{theorem}
  $u$ is a an odd weight $U_{q,\pi}$-module homomorphism.
\end{theorem}
\begin{proof}
  We need to show that $\Delta(x)u(1)=0$ for $x\in \{E,F\}$.
  \begin{align*}
    \Delta(E)u(1)&=(E\otimes 1)(v_{-}\otimes v_{+})+(JK \otimes E)(-\pi q^{-1}v_+ \otimes v_{-})=v_+\otimes v_+ -\pi q^{-1} JKv_+ \otimes Ev_-\\
    &=v_+\otimes v_+ -v_+\otimes v_+=0
  \end{align*}
  \begin{align*}
    \Delta(F)u(1)&=(F\otimes K^{-1})(-\pi q^{-1}v_+ \otimes v_{-})+(1\otimes F)(v_-\otimes v_+)=-\pi q^{-1}v_-\otimes K^{-1}v_-+\pi v_-\otimes v_- \\
    &=-\pi v_-\otimes v_- +\pi v_- \otimes v_-=0
  \end{align*}
\end{proof}

We associate a cup without orientation to the map $u$

\begin{align}\label{blue-cup-draw}
  \hackcenter{ \begin{tikzpicture} [scale=.75]

\draw[thick,   blue, -] (0,1).. controls ++(.25,-.5) and ++(-.25,-.5).. (1,1);
\end{tikzpicture}} & = u =
\begin{pmatrix}
     0\\
     -\pi q^{-1}\\
     1 \\
     0
  \end{pmatrix}
\end{align}

Then $nu=\tau q^{-1}+\tau^3 q$.

Define $E'= un: V\otimes V\to V\otimes V$. $E'$ is the even map
\begin{align*}
  \hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);
\draw[thick,   blue] (0,1).. controls ++(.25,-.5) and ++(-.25,-.5).. (1,1);
\end{tikzpicture}} &= E'= un =
\begin{pmatrix}
     0\\
     -\pi q^{-1}\\
     1 \\
     0
  \end{pmatrix}
\begin{pmatrix}
     0 & -\tau^3 & \tau^3q & 0
  \end{pmatrix}
=
\begin{pmatrix}
  0 & 0 & 0 & 0 \\
  0 & \tau q^{-1} & -\tau & 0 \\
  0 & -\tau^3 & \tau^3 q  & 0 \\
  0 & 0 & 0 & 0
\end{pmatrix}
\end{align*}

We can derive all the relations in \eqref{bracket-poly2-1}, \eqref{bracket-poly2-2}, and \eqref{bracket-poly2-3} with this understanding of the cap and cup as $U_{q,\pi}$-module homomorphisms.

\begin{align*}
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick, red, -] (0,0) to (1,1);
\draw[thick, red, -] (1,0) to (.6,.4);
\draw[thick, red, -] (0,1) to (.4,.6);
\end{tikzpicture}} \;=
 \begin{pmatrix}
\tau & 0 & 0 & 0 \\
0 & 0 & \tau q & 0 \\
0 & \tau^3q & \tau-\tau^3q^2 & 0 \\
0 & 0 & 0 & \tau
\end{pmatrix}&=
\tau Id-q
\begin{pmatrix}
  0 & 0 & 0 & 0 \\
  0 & \tau q^{-1} & -\tau & 0 \\
  0 & -\tau^3 & \tau^3 q  & 0 \\
  0 & 0 & 0 & 0
\end{pmatrix}=
\tau\;\;
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue] (0,0) to (0,1);
\draw[thick,   blue] (1,0) to (1,1);
\end{tikzpicture}}
-q\;\;
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);
\draw[thick,   blue] (0,1).. controls ++(.25,-.5) and ++(-.25,-.5).. (1,1);
\end{tikzpicture}}
\end{align*}



\begin{align*}
\hackcenter{ \begin{tikzpicture} [xscale=-1,scale=.75]
\draw[thick, red, -] (0,0) to (1,1);
\draw[thick, red, -] (1,0) to (.6,.4);
\draw[thick, red, -] (0,1) to (.4,.6);
\end{tikzpicture}} \;=
  \begin{pmatrix}
\tau^3 & 0 & 0 & 0 \\
0 & \tau^3-\tau q^{-2} & \tau q^{-1} & 0 \\
0 & \tau^3q^{-1} & 0 & 0 \\
0 & 0 & 0 & \tau^3
\end{pmatrix}&=
\tau^3 Id- q^{-1}
\begin{pmatrix}
  0 & 0 & 0 & 0 \\
  0 & \tau q^{-1} & -\tau & 0 \\
  0 & -\tau^3 & \tau^3 q  & 0 \\
  0 & 0 & 0 & 0
\end{pmatrix}
=
\tau^3\;\;
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue] (0,0) to (0,1);
\draw[thick,   blue] (1,0) to (1,1);
\end{tikzpicture}}
-q^{-1}\;\;
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);
\draw[thick,   blue] (0,1).. controls ++(.25,-.5) and ++(-.25,-.5).. (1,1);
\end{tikzpicture}}
\end{align*}
\begin{align*}
   \hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);
\draw[thick,   blue] (0,0).. controls ++(.25,-.5) and ++(-.25,-.5).. (1,0);
\end{tikzpicture}} &=nu=
\begin{pmatrix}
     0 & -\tau^3 & \tau^3q & 0
  \end{pmatrix}
\begin{pmatrix}
     0\\
     -\pi q^{-1}\\
     1 \\
     0
  \end{pmatrix}=\tau q^{-1}+\tau^3 q
\end{align*}


\begin{align*}
    \hackcenter{ \begin{tikzpicture} [xscale=-1, scale=.75]



\draw[thick,   blue] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);
\draw[thick,   blue] (1,0).. controls ++(.25,-.5) and ++(-.25,-.5).. (2,0);

\draw[thick, blue] (2,0) to (2,1);

\draw[thick, blue] (0,0) to (0,-1);

\end{tikzpicture}}&=(1\otimes n)\circ (u\otimes 1):V\to V
\end{align*}
This is the map sending
\begin{align*}
  v_{\pm} &\overset{u\otimes 1}{\rightarrow}-\pi q^{-1}v_+\otimes v_- \otimes v_{\pm}+ v_-\otimes v_+\otimes v_{\pm} \overset{1\otimes n}{\rightarrow} -\pi q^{-1}v_+\otimes n(v_- \otimes v_{\pm})+\pi  v_-\otimes n(v_+\otimes v_{\pm})=-\tau v_{\pm}.
\end{align*}
Hence,
\begin{align*}
    \hackcenter{ \begin{tikzpicture} [xscale=-1, scale=.75]



\draw[thick,   blue] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);
\draw[thick,   blue] (1,0).. controls ++(.25,-.5) and ++(-.25,-.5).. (2,0);

\draw[thick, blue] (2,0) to (2,1);

\draw[thick, blue] (0,0) to (0,-1);

\end{tikzpicture}}&=-\tau \;\;
\hackcenter{ \begin{tikzpicture} [xscale=-1, scale=.75]
\draw[thick, blue] (1,1) to (1,-1);
\end{tikzpicture}}
\end{align*}

The other zig-zag straightens up to a different power of $\tau$.
\begin{align*}
   \hackcenter{ \begin{tikzpicture} [ scale=.75]



\draw[thick,   blue] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);
\draw[thick,   blue] (1,0).. controls ++(.25,-.5) and ++(-.25,-.5).. (2,0);

\draw[thick, blue] (2,0) to (2,1);

\draw[thick, blue] (0,0) to (0,-1);

\end{tikzpicture}} & =(n\otimes 1)\circ (1\otimes u):V \to V
\end{align*}
Note that $(1\otimes u):V \to V\otimes V\otimes V$ is the map sending
\[v_{\pm} =v_{\pm}\otimes 1 \to \pi^{p(v_{\pm})}v_{\pm}\otimes u(1)=\pi^{p(v_{\pm})}(-\pi q^{-1}  v_{\pm}\otimes  v_+\otimes v_- + v_{\pm}\otimes  v_-\otimes v_+).\]
Thus, $(n\otimes 1)\circ (1\otimes u)$ is the map sending
\begin{align*}
  v_+ &\overset{1\otimes u}{\rightarrow} (-\pi q^{-1}  v_{+}\otimes  v_+\otimes v_- + v_{+}\otimes  v_-\otimes v_+)\overset{n\otimes 1}{\rightarrow} -\tau^3 v_+  \\
  v_- &\overset{1\otimes u}{\rightarrow}  \pi(-\pi q^{-1}  v_{-}\otimes  v_+\otimes v_- + v_{-}\otimes  v_-\otimes v_+)\overset{n\otimes 1}{\rightarrow} -\tau^3 v_-.
\end{align*}
Hence,
\begin{align*}
    \hackcenter{ \begin{tikzpicture} [xscale=1, scale=.75]



\draw[thick,   blue] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);
\draw[thick,   blue] (1,0).. controls ++(.25,-.5) and ++(-.25,-.5).. (2,0);

\draw[thick, blue] (2,0) to (2,1);

\draw[thick, blue] (0,0) to (0,-1);

\end{tikzpicture}}&=-\tau^3 \;\;
\hackcenter{ \begin{tikzpicture} [xscale=1, scale=.75]
\draw[thick, blue] (1,1) to (1,-1);
\end{tikzpicture}}
\end{align*}

Therefore, we also have the relation
\begin{align*}
    \hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue] (0,1).. controls ++(.25,-.5) and ++(-.25,-.5).. (1,1);
\draw[thick,   blue] (1,1).. controls ++(.25,.5) and ++(-.25,.5).. (2,1);

\draw[thick,   blue] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);
\draw[thick,   blue] (1,0).. controls ++(.25,-.5) and ++(-.25,-.5).. (2,0);

\draw[thick, blue] (2,0) to (2,1);
\draw[thick, blue] (0,0) to (0,-1);
\draw[thick, blue] (0,1) to (0,2);
\end{tikzpicture}}
\;\;=\;\;
  \hackcenter{ \begin{tikzpicture} [xscale=-1, scale=.75]
\draw[thick,   blue] (0,1).. controls ++(.25,-.5) and ++(-.25,-.5).. (1,1);
\draw[thick,   blue] (1,1).. controls ++(.25,.5) and ++(-.25,.5).. (2,1);

\draw[thick,   blue] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);
\draw[thick,   blue] (1,0).. controls ++(.25,-.5) and ++(-.25,-.5).. (2,0);

\draw[thick, blue] (2,0) to (2,1);
\draw[thick, blue] (0,0) to (0,-1);
\draw[thick, blue] (0,1) to (0,2);
\end{tikzpicture}}
\;\;=\;\;
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue] (0,-1) to (0,2);
\end{tikzpicture}}
\end{align*}


Therefore, $\hat{J}$ can be understood using representation theory of $U_{q,\pi}$.

\begin{comment}
We also can connect this with the odd Tempereley Lieb algebra
\ME{I'm not actually sure we can do this, but it doesn't really matter for this paper.} since we have the relations
\begin{align*}
\pi \;
  \hackcenter{ \begin{tikzpicture} [ scale=.75]



\draw[thick,   blue] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);
\draw[thick,   blue] (1,0).. controls ++(.25,-.5) and ++(-.25,-.5).. (2,0);

\draw[thick, blue] (2,0) to (2,1);

\draw[thick, blue] (0,0) to (0,-1);

\end{tikzpicture}}
\;\;=\;\;
-\tau \;
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue] (0,-1) to (0,2);
\end{tikzpicture}}
\;\;=\;\;
  \hackcenter{ \begin{tikzpicture} [xscale=-1, scale=.75]



\draw[thick,   blue] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);
\draw[thick,   blue] (1,0).. controls ++(.25,-.5) and ++(-.25,-.5).. (2,0);

\draw[thick, blue] (2,0) to (2,1);

\draw[thick, blue] (0,0) to (0,-1);

\end{tikzpicture}}
\end{align*}
\end{comment}

\begin{definition}
  Let $d:=\tau^3 q+\tau q^{-1}$. Define $\sigma_i\in B_n$ using the positive crossing involving strands $i$ and $i+1$.
  Then define $\rho_{q,\tau}:B_n \to TL_n(d)$ given by
  \[
  \rho_{q,\tau}(\sigma_i)=(\tau Id -q E_i).
  \]
\end{definition}
\begin{theorem}
  $\rho_{q,\tau}:B_n \to TL_n(d)$ defines a $B_n$-representation inside $TL_n(d)$, namely a group homomorphism from $B_n$ to the group of invertible elements of $TL_n(d)$.
\end{theorem}

\begin{comment}
Note that we have $E_iE_j=E_jE_i$ in $TL_n$, so we have $(E\otimes 1\otimes 1)\circ (1\otimes 1 \otimes E)= (1\otimes 1 \otimes E)\circ (E\otimes 1\otimes 1)$

Loose diagrammatic description:

We treat each capcup $E$ as a unit, so if we move a cup above a morphism $f$, we also move the cap it comes with above $f$. The cap and cup are each odd, so if we move both of them past $f$, we get no change in sign. We can do this as we think of the capcup as an element in the algebra $TL_n$.
\end{comment}

---
doc_id: arxiv-2210.09583v1
doc_title: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT"
section_id: sec-006-32-quantum-covering-group
section_title: "Quantum covering group"
section_number: 3.2
pages: 7-9
source_pdf: 2210.09583v1.pdf
source_sha256: 38fc6fa465a06a7b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.958
doc_brief: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT — There is a known connection between the osp(1|2n) polynomial knot invariant Jn K and the so(2n + 1) knot invariant soJn K studied by"
---
\label{sec:covering-group}

\begin{definition}{\cite{CHW}}
  The quantum covering group $U_{q,\pi}:=U_{q,\pi}(\mf{sl}_2)$ is the $\Q(q,t)^\tau$-algebra with generators $E,F,K^{\pm 1},J$, subject to the relations
  \begin{align}\label{quantum-covering-group}
    J^2&=1 & JK&=KJ \\
    JE&=EJ & JF&=FJ \\
    KE&=q^2EK & KF&=q^{-2}FK \\
    EF-\pi FE &= \frac{JK-K^{-1}}{\pi q-q^{-1}}
  \end{align}
\end{definition}

It has structure of a Hopf superalgebra\cite{CHW,CHW2, C} but with braiding replaced by $x\otimes y \to \pi^{p(x)p(y)}y\otimes x$.
The coproduct $\Delta:U_{q,\pi} \to U_{q,\pi}\otimes U_{q,\pi} $ is

\begin{align*}
  \Delta(E)&=E\otimes 1+ JK\otimes E & \Delta(F)&=F\otimes K^{-1}+1\otimes F & \Delta(K)&=K\otimes K & \Delta(J)&=J\otimes J
\end{align*}

The antipode $S:U_{q,\pi}\to U_{q,\pi}$ is
\begin{align*}
  S(E)&=-J^{-1}K^{-1}E & S(F)&=-FK  & S(K)&=K^{-1} & S(J)&=J
\end{align*}

The counit $\varepsilon:U \to \Q(q,t)^{\tau}$
\begin{align*}
  \varepsilon(E)=\varepsilon(F)=0 \qquad \varepsilon(J)=\varepsilon(K)=1
\end{align*}


\subsection{$U_{q,\pi}$-modules}\label{sec:U-modules}

\begin{definition}{\cite[Section 2.4]{C}}
  A weight $U_{q,\pi}$-module $M$ is a $\Z\times \Z_2 $ graded $U$-module, whose grading is compatible with the grading on $U$ such that
  \begin{align*}
    M=\bigoplus_{\lambda \in \Z} M_{\lambda,0}\oplus M_{\lambda,1} &\qquad M_{\lambda,s}=\{ m\in M \mid p(m)=s, \; Jm=\pi^\lambda m, \;Km=q^\lambda m \}
  \end{align*}
\end{definition}

The simple weight $U$-module of highest weight $m$ with highest weight vector $v_m$ of even parity ($||v_m||=(m,0)$) is denoted $V(m)$.
It has basis $\{v_{m-2k}:=F^{(k)}v_m\}_{0\leq k\leq m}$. By convention we have $p(v_{m-2k})\equiv k (mod\; 2)$. The action of $U_{q,\pi}$ on $V(m)$ is given by
\begin{align*}
  Ev_{m-2k}&=\pi^{k-1}[m+1-k]v_{m-2(k-1)}  &\qquad Kv_{m-2k}&=q^{m-2k}v_{m-2k}\\
  Fv_{m-2k}&=[k+1]v_{m-2(k+1)} & \qquad Jv_{m-2k}&=\pi^{m-2k}v_{m-2k}
\end{align*}

Define the parity reversed module $\Pi M$ to be $M$ as a vector space equipped with the same action of $U_{q,\pi}$, but with $(\Pi M)_{\lambda, s}=M_{\lambda,1-s}$.

In particular, the identity map induces an odd $U$-module isomorphism $\gamma_{V(m)}:V(m) \to \Pi V(m)$.

For the purposes of this paper, it is enough to consider the case where $m=1$.
As a superspace, the $U_{q,\pi}$-module $V:=V(1)$ is given by the span of elements $\{v_+, v_-\}$ with $\Z\times \Z_2$ degrees $||v_+||=(1,0)$ and $||v_-||=(-1,1)$.
The action of $U_{q,\pi}$ on $V$ is given by
\begin{align*}
  Ev_{-}&=v_+  & Ev_+&=0 &\qquad Kv_{\pm}&=q^{\pm 1}v_{\pm}\\
  Fv_{+}&=v_{-} & Fv_-&=0 & \qquad Jv_{\pm}&=\pi^{\pm 1}v_{\pm}
\end{align*}

Then $\Pi V=\text{span} \{v_+', v_-'\}$ as a superspace where the $\Z\times \Z_2$ degrees of the basis elements are $||v_+'||=(1,1)$ and $||v_-'||=(-1,0)$.
By definition, the action of $U_{q,\pi}$ on $\Pi V$ is the same as the action on $V$.
\begin{align*}
  Ev_{-}'&=v_+'  & Ev_+'&=0 &\qquad Kv_{\pm}'&=q^{\pm 1}v_{\pm}'\\
  Fv_{+}'&=v_{-}' & Fv_-'&=0 & \qquad Jv_{\pm}'&=\pi^{\pm 1}v_{\pm}'
\end{align*}

Thus, the identity map induces an odd $U$-module isomorphism $\gamma_V: V \to \Pi V$ which sends $v_\pm \to v_\pm'$.
The dual module $M^*$ is defined to be
\begin{align*}
  M^*=\bigoplus_{\lambda \in \Z} (M_{\lambda,0})^*\oplus (M_{\lambda,1})^* &\qquad (M_{\lambda,s})^*=\Hom_{Q(q,t)^\tau}(M_{\lambda,s},Q(q,t)^\tau)
\end{align*}
The action on $M^*$ is induced by the Hopf superalgebra structure of $U_{q,\pi}$: For $x\in U_{q,\pi}$,
\begin{align*}
  xf(v)=\pi^{p(f)p(x)}f(S(x)v).
\end{align*}


Let us consider $M=V(m)$.
Then $V(m)^*$ has a dual basis $\{v_{m-2k}^*\}_{0 \leq k\leq m}$ with $||v_{m-2k}^*||=(2k-m,k)$.

\begin{align*}
  Ev_{m-2k}^* &= -(\pi q^{-1})^{m-2k}[m-k]v_{m-2(k+1)}^* \\
  Fv_{m-2k}^* &= -\pi^k q^{m-2k+2}[k]v_{m-2(k-1)}^*
\end{align*}

We prove the action of $F$ is correct.
\begin{align*}
  F v_{m-2k}^*(v_\alpha) &= \pi^k v_{m-2k}^*(S(F)v_{\alpha}) = \pi^k v_{m-2k}^*(-FKv_{\alpha}) \\
  &=-\pi^k\delta_{\alpha-2, m-2k}q^\alpha v_{m-2k}^*(Fv_{\alpha})= -\delta_{\alpha-2, m-2k} \pi^k q^{m-2k+2} v_{m-2k}^*(Fv_{m-2(k-1)}) \\
  &=-\delta_{\alpha-2, m-2k} \pi^k q^{m-2k+2} [k]v_{m-2k}^*(v_{\alpha-2})=-\pi^kq^{m-2k+2}[k] v_{m-2(k-1)}^*(v_\alpha)
\end{align*}


$V(m)^*$ is a weight module with highest weight vector $v_{-m}^*$. This has degree $||v_{-m}^*||=(m,m)$, so there is an even $U_{q,\pi}$-module isomorphism $\Pi^m V(m) \to V(m)^*$.

\begin{comment}
Explicitly, for $m=1$, there is an even $U_{q,\pi}$-module isomorphism $g_V: \Pi V \to V^*$ defined by $g(v_+')=v_-^*$.
This implies that $g(v_-')=-\pi q v_{+}^*$
\begin{definition}
  We define an odd $U$-module isomorphism $f:V \to V^*$ by the composition $f=g\circ \gamma_V$
  \begin{align*}
  f(v_+)&=v_-^* & \qquad f^{-1}(v_-^*)&=v_+ \\
  f(v_{-})&=-\pi q v_+^* &\qquad f^{-1}(v_+^*)&=-\pi q^{-1}v_-
\end{align*}
\ME{We don't actually use this $f:V\to V^*$ anymore, but I think it is a good thing to keep around}
\end{definition}
\end{comment}

\subsection{Clark's $\mf{osp}(1|2)$ invariant}\label{Sec:Clark-method}
In this subsection, we review how Clark obtains the uncolored $\mf{osp}(1|2)$ link invariant in simplest case done in \cite[Example 3.10]{C}.
Clark actually defines a colored $\mf{osp}(1|2n)$-invariant, but we only consider the uncolored case with $n=1$.
All of the material in this subsection comes from \cite[Section 2, Section 3]{C}.

\begin{notation}
  We use the ordered basis
  \begin{align*}
    \{v_{+}\otimes v_{+}, v_{+}\otimes v_{-}, v_{-}\otimes v_{+}, v_{-}\otimes v_{-}\} &\qquad \text{for} \; V\otimes V \\
    \{v_{+}^*\otimes v_{+}, v_{+}^*\otimes v_{-}, v_{-}^*\otimes v_{+}, v_{-}^*\otimes v_{-}\} &\qquad \text{for} \; V^*\otimes V  \\
    \{v_{+}\otimes v_{+}^*, v_{+}\otimes v_{-}^*, v_{-}\otimes v_{+}^*, v_{-}\otimes v_{-}^*\} &\qquad \text{for} \; V\otimes V^*
  \end{align*}
\end{notation}

Recall the $\Q(q,t)^{\tau}$-linear maps from \cite[Lemma 2.7]{C}.
\begin{itemize}
  \item $\text{ev}:V(1)^* \otimes V(1) \to \Q(q,t)^{\tau}$ is the map $v^*\otimes w \to v^*(w)$. It is given by the matrix
  $\begin{pmatrix}
    1 & 0 & 0 & 1
  \end{pmatrix}$
  \item $\text{qtr}:V(1) \otimes V(1)^* \to \Q(q,t)^{\tau}$ is the map $v\otimes w^* \to \pi^{p(v)p(w)}q^{-|v|}w^*(v)$. It is given by the matrix
  $\begin{pmatrix}
    q^{-1} & 0 & 0 & \pi q
  \end{pmatrix}$
  \item $\text{coev}:\Q(q,t)^{\tau} \to V(1)^* \otimes V(1) $ given by $1\to qv_{+}\otimes v_{+} + \pi q^{-1} v_{-}\otimes v_{-}$ It is given by the matrix
  $\begin{pmatrix}
     q \\
     0 \\
     0 \\
     \pi q^{-1}
   \end{pmatrix}$
  \item $\text{coqtr}:\Q(q,t)^{\tau} \to V(1) \otimes V(1)^* $ is map $1\to v_{+}\otimes v_{+}+ v_{-}\otimes v_{-}$. It is given by the matrix
  $\begin{pmatrix}
     1 \\
     0 \\
     0 \\
     1
   \end{pmatrix}$
\end{itemize}
as well as the quasi $R$-matrix

$R_{1,1}:V(1)\otimes V(1) \to V(1)\otimes V(1)$ given by the matrix
$\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 0 &  q & 0 \\
0 & \pi q & 1-\pi q^2 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$

and its inverse $R_{1,1}^{-1}$ given by the matrix
$\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1-\pi q^{-2} & \pi q^{-1} & 0 \\
0 & q^{-1} & 0 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$.

So far, we can do everything in this section in the subring $\Q(q)^\pi\subset \Q(q,t)^\tau$, but need to renormalize the maps using $\pi=\tau^2$ to get a link invariant.
In particular, the maps $qtr$ and $R_{1,1}$ pick up a factor of $\tau$, while $coev$ and $R_{1,1}^{-1}$ pick up a factor of $\tau^3$.
The renormalized maps have a diagrammatic interpretation using red strands that can be used to obtain the $U_q({\mf{osp}(1|2)})$ link invariant.

\begin{align}\label{eq:red-maps}
  \hackcenter{ \begin{tikzpicture} [scale=.75]

\draw[thick,   red, ->] (0,1).. controls ++(.25,-.5) and ++(-.25,-.5).. (1,1);
\end{tikzpicture}} & = \tau^3 coev =
\begin{pmatrix}
     \tau^3q \\
     0 \\
     0 \\
     \tau q^{-1}
   \end{pmatrix}  & \qquad \hackcenter{ \begin{tikzpicture} [scale=.75]

\draw[thick,   red, <-] (0,1).. controls ++(.25,-.5) and ++(-.25,-.5).. (1,1);
\end{tikzpicture}} & = coqtr =
\begin{pmatrix}
     1 \\
     0 \\
     0 \\
     1
   \end{pmatrix} \\
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   red, ->] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);

\end{tikzpicture}} & = \tau qtr =
\begin{pmatrix}
    \tau q^{-1} & 0 & 0 & \tau^3 q
  \end{pmatrix} & \qquad \hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   red, <-] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);

\end{tikzpicture}} & = ev =
\begin{pmatrix}
    1 & 0 & 0 & 1
  \end{pmatrix} \\
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick, red, ->] (0,0) to (1,1);
\draw[thick, red, -] (1,0) to (.6,.4);
\draw[thick, red, <-] (0,1) to (.4,.6);
\end{tikzpicture}} &= \tau R_{1,1} =
\begin{pmatrix}
\tau & 0 & 0 & 0 \\
0 & 0 & \tau q & 0 \\
0 & \tau^3q & \tau-\tau^3q^2 & 0 \\
0 & 0 & 0 & \tau
\end{pmatrix}
& \qquad
\hackcenter{ \begin{tikzpicture} [xscale=-1,scale=.75]
\draw[thick,   red, ->] (0,0) to (1,1);
\draw[thick,   red, -] (1,0) to (.6,.4);
\draw[thick,   red, <-] (0,1) to (.4,.6);
\end{tikzpicture}} &= \tau^3 R_{1,1}^{-1} =
\begin{pmatrix}
\tau^3 & 0 & 0 & 0 \\
0 & \tau^3-\tau q^{-2} & \tau q^{-1} & 0 \\
0 & \tau^3q^{-1} & 0 & 0 \\
0 & 0 & 0 & \tau^3
\end{pmatrix}
\end{align}

\begin{theorem}{\cite[Theorem 3.8, Corollary 3.9]{C}}
There is a covariant functor $J$ from the category of oriented tangles to the category of finite dimensional $U_{q,\pi}$-modules that sends a tangle $T$ to the associated $U_{q,\pi}$-module homomorphism defined using \ref{eq:red-maps} and multiplying the resulting homomorphism by $(\pi q)^{wr(T)}$.
In particular, $L$ is an oriented link, then $J_L^1=J(L)$ is Clark's $\mf{osp}(1|2)$-link invariant \cite[Example 3.10]{C}.
\end{theorem}

In \cite[Example 3.10]{C}, Clark showed that the red maps \ref{eq:red-maps} satisfy
\begin{align*}
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick, red, ->] (0,0) to (1,1);
\draw[thick, red, -] (1,0) to (.6,.4);
\draw[thick, red, <-] (0,1) to (.4,.6);
\end{tikzpicture}}
- q^2\;\;
\hackcenter{ \begin{tikzpicture} [xscale=-1,scale=.75]
\draw[thick, red, ->] (0,0) to (1,1);
\draw[thick, red, -] (1,0) to (.6,.4);
\draw[thick, red, <-] (0,1) to (.4,.6);
\end{tikzpicture}}
\;\;=\;\;
(\tau-\tau^3 q^2)\;\;
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   red,->] (0,0) to (0,1);
\draw[thick,   red,->] (1,0) to (1,1);
\end{tikzpicture}}
\end{align*}
This shows that $J_L^1$ satisfies the skein relation \ref{osp-Skein}.
Then taking the specialization $\tau=t$, which correpsonds to $\pi=-1$, he concludes that the uncolored $U_q(\mf{osp}(1|2))$ link invariant is equal to the $U_{\tau^{-1}q}(\mf{sl}_2)$ link invariant.

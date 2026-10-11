---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-007-2-borel-resummation-and-stokes-automorphisms
section_title: "Borel resummation and Stokes automorphisms"
section_number: 2
pages: 9-24
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.886
---
\label{sec.borel}


\subsection{Borel resummation}
\label{sub.borel}


In this section we briefly review the process of Borel resummation of
a factorially divergent series, its Laplace integral along rays and
the corresponding Stokes automorphism across a Stokes ray. The
material in this section is classical and well-known and is explained
in detail in the books~\cite{Costin:asymptotics,Miller:applied,msauzin},
and in the references therein. We will be following the physics convention
of Borel resummation as found for example in~\cite[Sec. 3.2]{mmbook}
and~\cite[Sec.42.5]{Zinn-Zustin:QFT}, which differs by a factor of
$\tau$ from the Borel resummation found in the math literature.

Borel resummation is a 2-step process to pass from a factorially
divergent series $F(\tau)$ to the analytic function $s(F)(\tau)$
defined in the right half-plane $\Re(\tau)>0$ summarized in the
following diagram
\begin{equation}
  \label{borel-sum}
  F(\tau) \leadsto 
  \wh{F}(\zeta) \leadsto 
  s(F)(\tau) \,.
\end{equation}
Here one starts with a Gevrey-1 a formal power series $F(\tau)$
\begin{equation}
  F(\tau) = \sum_{n=0}^\infty f_n \tau^{n} ,\quad f_n = O(C^n \, n!)
\end{equation}
and defines its Borel stransform $\wh{F}(\zeta)$ by
\begin{equation}
  \wh{F}(\zeta) = \sum_{n=0}^\infty \frac{f_n}{n!} \zeta^n \,.
\end{equation}
It follows that $\wh{F}$ is the germ of an analytic function at
$\zeta=0$. If it analytically continues to an $L^1$-analytic function
along the ray $\rho_\theta:=\re^{\ri\theta}\IR_+$ where
$\theta = \arg \tau$, we define its Laplace transform by 
\begin{equation}
  s_{\theta}(F)(\tau)=
  \int_0^\infty \wh{F}(\tau\zeta) \re^{-\zeta} \rd \zeta=
  \frac{1}{\tau} \int_{\rho_\theta}
  \wh{F}(\zeta)\re^{-\zeta/\tau} \rd \zeta
  \label{eq:brlsum}
\end{equation}






The function $s(F)(\tau)$ is often called the Borel resummation of the
formal power series $F$, and we often suppress the subscript $\theta=0$
when $\tau$ is real and positive.













If we vary $\theta = \arg \tau$ and we do not encounter singularities
of $\wh{F}$, the function $s_\th(F)(\tau)$ is locally analytic. Thus,
the problem is to understand the analytic continuation of $\wh{F}$ and
to analyze what happens to the Borel resummation $s_\theta(F)(\tau)$
when $\theta =\arg(\tau)$ crosses a Stokes ray, i.e., a ray in Borel
plane that contains one or more singularities of $\wh{F}$. This is
described by a Stokes automorphism.


\subsection{Stokes automorphism}
\label{sub.stokes}

We will specialize our discussion to the series of interest, namely to
the Borel transform $\wh{\Phi}(x;\zeta)$ of the vector of series
$\Phi(x;\tau)$. The singularities of $\Phi(x;\tau)$ are conjectured to
be in the set~\eqref{Phising} that generates a set of Stokes rays
whose complement is a countable union of open cones in Borel plane.
When $\th$ is in a fixed such cone $C$, the Laplace transform
$s_\th(\Phi)(x;\tau)$ depends on $C$ but not on $\th$.  To compare two
adjacent such cones, let $\iota_{\s,\s'}^{(\ell,k)}$ denote one of the
singularities of $\Phi_\s(x;\tau)$, $\theta$ denote its argument and
$\rho=\re^{\ri\theta}\BR_+$ denote the corresponding Stokes ray.  When
$x$ is generic, a Stokes ray contains a single singularity and the
Laplace integrals to the right and the left of $\rho$ are related by
\begin{equation}
  s_{\theta^+}(\Phi_\s)(x;\tau) =  s_{\theta^-}(\Phi_\s)(x;\tau) +
  \mc{S}_{\s,\s'}^{(\ell,k)}\tx^\ell \tq^k
  s_{\theta^-}(\Phi_{\s'})(x;\tau),
  \label{eq:Sauto}
\end{equation}
where $\mc{S}_{\s,\s'}^{(\ell,k)}$ is the Stokes constant. In matrix
form, the above formula reads
\begin{equation}
\label{lap2}
  s_{\theta^+}(\Phi)(x;\tau) =
  \mfS_{\theta}(\tx;\tq) s_{\theta^-}(\Phi)(x;\tau) 
\end{equation}
where
\begin{equation}
\label{Grho}
\mfS_\th(\tx;\tq)=
I + \mc{S}_{\s,\s'}^{(\ell,k)}\, \tx^\ell \, \tq^k \, E_{\s,\s'}
\end{equation}
where $E_{\s,\s'}$ is the elementary matrix with $(\s,\s')$-entry $1$
and all other entries zero.

More generally, consider two non-Stokes rays $\rho_{\th^+}$ and
$\rho_{\th^-}$ whose arguments satisfy $0 \leq \th^+-\th^- \leq
\pi$. Then, the Laplace integrals are related by
\begin{equation}
\label{lap3}
  s_{\theta^+}(\Phi)(x;\tau) =
  \mfS_{\theta^- \rightarrow \theta^+}(\tx;\tq) s_{\theta^-}(\Phi)(x;\tau) 
\end{equation}
where the Stokes matrices satisfy the factorization property
\begin{equation}
  \mfS_{\theta^- \rightarrow \theta^+ }(\tx,\tq) =
  \prod_{\th^- < \th < \th^+}^{\longleftarrow} \mfS_{\th}(\tx,\tq).
  \label{eq:SRR-fac}
\end{equation}
where the ordered product is taken over the Stokes rays in the cone
genarated by $\rho_{\th^-}$ and $\rho_{\th^+}$. This factorization is
well-known in the classical litetature on WKB (see for instance
Voros~\cite[p.228]{voros} who called it the ``radar method''  for
obvious visual reasons). In our case, there are four
special non-Stokes rays denoted by 
\begin{equation}
\label{4I}
I=\re^{\ri \epsilon}\BR_+,
\qquad II=\re^{\ri (\pi-\epsilon)}\BR_+,
\qquad III=\re^{\ri (\pi+\epsilon)}\BR_+,
\qquad IV=\re^{\ri (2\pi-\epsilon)}\BR_+
\end{equation}
(for $\epsilon>0$ and sufficently small) that belong to the four
distinguished cones (labeled $I,II,III,IV$) adjacent to the real axis
and free of Stokes lines. The corresponding Stokes matrices
\begin{equation}
  \label{SG}
  \ms{S}^+(\tx;\tq) =
  \mf{S}_{I\rightarrow II}(\tx;\tq)\, \mf{S}_{IV\rightarrow I}(\tx;\tq),
  \qquad
  \ms{S}^-(\tx;\tq) =
  \mf{S}_{III\rightarrow IV}(\tx;\tq)\, \mf{S}_{II\rightarrow III}(\tx;\tq)
\end{equation}
that swap two complementary and nearly horizontal half-planes
separated by a line $L$ are the ones that appear in
Conjecture~\ref{conj.asy}. They are related to the matrices
$M_\rho$ in the second part of that conjecture by
\begin{align}
  \mfS_{I\rightarrow II}(\tx;\tq)
  &= (M_{II}(\tx;\tq))^{-1}\cdot M_{I}(\tx;\tq),\quad |\tq|<1\nn
    \mfS_{III\rightarrow IV}(\tx;\tq)
  &= (M_{IV}(\tx;\tq^{-1}))^{-1}\cdot M_{III}(\tx;\tq^{-1}),\quad |\tq|<1\nn
    \mfS_{IV\rightarrow I}(\tx;\tq)
  &= (M_{I}(\tx;\tq))^{-1}\cdot M_{IV}(\tx;\tq),\nn
    \mfS_{II\rightarrow III}(\tx;\tq)
  &= (M_{III}(\tx;\tq))^{-1}\cdot M_{II}(\tx;\tq) \,.
    \label{4G}
\end{align}

We now come to an important feature of our resurgent series,
a unique factorization property for the Stokes matrices reminiscent
of the ``stability data'' description of DT-invariants in
Kontsevich-Soibelman~\cite{KS,KS:stability, KS:wall-crossing}), and
of the properties of BPS spectrum generators in
Gaiotto-Moore-Neitzke~\cite{gmn, gmn2, gmn3}. 

\begin{lemma}
  \label{lem.fac}
  $\ms{S}$
  uniquely determines $\mfS_{\th}$ for all $\th$. 
\end{lemma}

\begin{proof}
  Without loss of generality, we will show that $\ms{S}^+$ uniquely
  determines the Stokes matrices $\mfS_\th$ for all $\th$ such that
  $-\varepsilon < \th < \pi - \varepsilon$ for $\varepsilon>0$ and
  sufficiently small. We have
  \begin{equation}
    \label{SScal}
    \ms{S}^+(\tx;\tq) = \prod_{\s,\s',k,\ell}^{\longleftarrow}
    (I + \calS_{\s,\s'}^{(\ell,k)} \tx^\ell \, \tq^k E_{\s,\s'})
  \end{equation}
  where the product is over all the singularities above the line $L$.
  The entries of the above matrices are in the ring
  $\BZ[\tx^\pm][[\tq]]$.  For each fixed natural number $N$, there are
  only finitely many horizontal lines of singularities in Borel plane,
  of height at most $N$ and within those, there are finitely many
  $\tx$-dots. It follows by induction on $k$ that the finite
  collection $\{\calS_{\s,\s'}^{(\ell,k)}\}_\ell$ is uniquely
  determined from $\ms{S}^+(\tx;\tq)$.
\end{proof}

It follows that we can repackage the information of the Stokes
constants in two matrices $\calS^+$ and $\calS^-$ defined by

\begin{equation}
  \label{calS}
  \calS^\pm(\tx;\tq) = \sum_{\ell,k} \calS_{\s,\s'}^{(\ell,k)}
  \tx^\ell \, \tq^k E_{\s,\s'}
\end{equation}
where the sum in $\calS^+$ (resp. $\calS^-$) is over the singularities
above (resp., below) $L$. The matrices $\calS^\pm(\tx;\tq)$ appear to
have some positivity properties; see Sections~\ref{sub.41stokes}
and~\ref{sub.52stokes} below for the $\knot{4}_1$ and the $\knot{5}_2$
knots.
    




\section{A summary of the story when $u=0$}
\label{sec.summary}

In this section we recall briefly the results
from~\cite{GGM:resurgent} for our two sample hyperbolic knots, the
$\knot{4}_1$ and the $\knot{5}_2$ knot.


\subsection{The $\knot{4}_1$ knot when $u=0$}
\label{sub.41x=1}

The state integral of the $\knot{4}_1$ at $u=0$ is given by
\begin{equation}
  \label{Z410}
  Z_{\knot{4}_1}(0;\tau) = 
  \int_{\BR+\ri 0} \Phi_\bb(v)^2 \, \re^{-\pi \ri v^2} \rd v \,.
\end{equation}
The critical points of the integrand are the logarithms of the
solutions $\xi_1= {\rm e}^{2 \pi \ri/6}$ and
$\xi_2= \re^{-2 \pi \ri/6}$ of the polynomial equation
\begin{equation}
  \label{41xi}
  (1-y)(1-y^{-1})=1 \,.
\end{equation}
The labeling set $\calP=\{\s_1,\s_2\}$, where $\s_1$ corresponds to
the geometric representation of the $\knot{4}_1$ and $\s_2$ to the
complex conjugate of the geometric representation. Observe that
$\xi_1$ (resp., $\xi_2$) lie in the trace field $\BQ(\sqrt{-3})$
(resp., its complex conjugate) of the $\knot{4}_1$ knot, where
$\BQ(\sqrt{-3})$ is a subfield of the complex numbers with $\sqrt{-3}$
taken to have positive imaginary part.

The first ingredient is a vector of formal power series 

\be
\Phi(\tau)=
\begin{pmatrix} \Phi_{\s_1}(\tau)\\ \Phi_{\s_2}(\tau) \end{pmatrix} 
\ee

defined by the asymptotic expansion of the state-integral~\eqref{Z410}
at each of the two critical points, and which has the form

\be
\Phi_{\s}(\tau) = \exp\left( { V(\s) \over 2\pi \ri \tau} \right)
\varphi_\s(\tau),
\ee

satisfies the symmetry
$\Phi_{\s_2}(\tau) = {\rm \ri} \Phi_{\s_1}(-\tau)$, where 

\begin{equation}
  \label{volume-41}
  V(\s_1)= \ri \text{Vol}(\knot{4}_1)
  = \ri\, 2 {\rm Im}\, {\rm Li}_2(\re^{\ri \pi/3})
  = \ri\, 2.029883\dots \,.
\end{equation}

with $\text{Vol}(\knot{4}_1)$ being the hyperbolic volume of
$\knot{4}_1$ and the first few terms of
$\varphi_{\s_1}(\tau/(2\pi \ri)) \in 3^{-1/4} \BQ(\sqrt{-3})[[\tau]]$
are given by
\begin{equation}
  \label{varphi41}
  \varphi_{\s_1}\left(\frac{\tau}{2\pi \ri}\right) =
  \frac{1}{\sqrt[4]3}\, 
  \Bigl(1 \+ \frac{11\tau}{72\sqrt{-3}}
  \+ \frac{697\tau^2}{2\,(72\sqrt{-3})^2}
  \+ \frac{724351\tau^3}{30\,(72\sqrt{-3})^3} \+\cdots\Bigr)\,. 
\end{equation}


The second ingredient is a vector
$G(q)=\begin{psmall} G^0(q) \\ G^1(q)
\end{psmall}$ of $q$-series defined for $|q|<1$ by
\begin{subequations}
\begin{align}
\label{gm0}
G^0(q) &=\sum_{n=0}^\infty (-1)^n \frac{q^{n(n+1)/2}}{(q;q)_n^2}
\\
\label{Gm0}
G^1(q) &=\sum_{n=0}^\infty (-1)^n \frac{q^{n(n+1)/2}}{(q;q)_n^2}
\left(E_1(q) + 2 \sum_{j=1}^n \frac{1+q^j}{1-q^j} \right) \,,
\end{align}
\end{subequations}
where $E_1(q)=1-4\sum_{n=1}^\infty q^n/(1-q^n)$ is the Eisenstein
series, and extended to $|q|>1$ by $G^0(q^{-1})=G^0(q)$ and
$G^1(q^{-1})=-G^1(q)$.  These series are motivated by, and appear in,
the factorization of the state-integral of the $\knot{4}_1$ knot given
in~\cite[Cor.1.7]{GK:qseries}
\begin{equation}
  \label{Z410-fac}
  Z_{\knot{4}_1}(0;\tau) =
  - \frac{\ri}{2} \left(\frac{q}{\tq}\right)^{\frac{1}{24}} 
  \left(
    \sqrt{\tau} G^0(\tq) G^1(q) - \frac{1}{\sqrt{\tau}} G^0(q) G^1(\tq) 
  \right), \qquad (\tau \in \BC\setminus\BR)
\end{equation}
where 
\begin{equation}
\label{qqt}
q=\re^{2 \pi \ri \tau}, \qquad \tq=\re^{-2\pi \ri/\tau} \,.
\end{equation}
The above factorization follows by applying the residue theorem to the
integrand of~\eqref{Z410}, a meromorphic function of $v$ with
prescribed zeros and poles. In particular, the integrand
of~\eqref{Z410} determines the $q$-hypergeometric formula for the
vector $G(q)$ of $q$-series.  Below, given a $q$-series $H(q)$ defined
on $|q| \neq 1$, we denote by $h(\tau)= H(\re^{2\pi \ri\tau})$ the
corresponding holomorphic function in $\BC\setminus\BR$.

The vector $G(q)$ of $q$-series and the vector of asymptotic
series $\Phi(\tau)$ come together when we consider the asymptotics
of $\diag(\frac{1}{\sqrt{\tau}},\sqrt{\tau}) g(\tau)$


in the $\tau$-plane (as was studied in~\cite{GZ:qseries}) and compare
them with the Borel summed vector $\Phi$.

Recall that when the Borel transform of an asymptotic series has
singular points $\iota_i$ in the Borel plane, the rays (Stokes rays)
emanating from the origin with angle $\theta = \arg \iota_i$

divide the complex plane into different sectors.  When one crosses
into neighboring sectors, the Borel sum of the asymptotic series
undergoes Stokes automorphism.

In the case of the vector of asymptotic series $\Phi(\tau)$, the
singularities of the Borel transforms of its two component asymptotic
series are located at
\begin{equation}
  \iota_{i,j} = \frac{V(\s_i) - V(\s_j)}{2\pi\ri}\,,\quad i,j=1,2,\;i\neq j,
\end{equation}
as well as
\begin{equation}
  2\pi\ri k,\; \iota_{i,j}+2\pi\ri k\,,
  \quad k\in \IZ_{\neq 0},
\end{equation}
forming vertical towers as illustrated in
Figure~\ref{fig:sings-u0-41}. In particular, the two singularities
$\iota_{1,2}, \iota_{2,1}$ are on the positive and the negative real
axis. We pick out four sectors which separate 
the two singularities on the real axis and all the others, and label
them by $I,II,III,IV$, as illustrated in Figure~\ref{fig:secs-u0-41}.
The relation between the vector $G(q)$ and the Borel summed vector
$\Phi(\tau)$ depend on the sector $R$.
In~\cite{GGM:resurgent}, we found out
that we do not get an agreement, but rather both sides agree up to
powers of the exponentially small quantity $\tq$, and what is more,
several coefficients of those powers were numerically recognized to be
integers. In other words, we found that

\begin{equation}
\label{MR}
\diag(\frac{1}{\sqrt{\tau}},\sqrt{\tau}) g(\tau)



= M_R (\tq) \, s_R(\Phi)(\tau) \,.
\end{equation}

where $\diag(v)$ denotes the diagonal matrix with diagonal given by
$v$ and $M_R(q)$ is a matrix of $q$-series with integer coefficients.

\begin{figure}[htpb!]
\leavevmode
\begin{center}

  \includegraphics[height=7cm]{fig8_borelplane_s1u0} \hspace{5ex}
  \includegraphics[height=7cm]{fig8_borelplane_s2u0}
\end{center}
\caption{The singularities in the Borel plane for the series
  $\varphi_{\sigma_{j}} (0;\tau)$ for $j=1,2$ of knot $\knot{4}_1$.}
\label{fig:sings-u0-41}
\end{figure}

\begin{figure}[htpb!]
\leavevmode
\begin{center}

\includegraphics[height=7cm]{fig8_regions_u0}
\end{center}
\caption{Four different sectors in the $\tau$-plane for $\Phi(0;\tau)$
  of knot $\knot{4}_1$.}
\label{fig:secs-u0-41}
\end{figure} 

To identify the matrices $M_R$, we used the third ingredient,
namely the linear $q$-difference equation
\begin{equation}
\label{41qdiff}
y_{m+1}(q) -(2-q^m) y_m(q) + y_{m-1}(q)=0 \qquad (m \in \BZ) \,.
\end{equation}
It has a fundamental solution set given by the columns of the following
matrix 
\begin{equation}
\label{Gfund}
W_m(q) =
\begin{pmatrix} G^0_m(q) & G^1_m(q) \\ G^0_{m+1}(q) & G^1_{m+1}(q)
\end{pmatrix}, \qquad (|q| \neq 1)
\end{equation} 
where $G_m(q)=\begin{psmall} G^0_m(q) \\ G^1_m(q) \end{psmall}$,
and $G^0_m(q)$ and $G^1_m(q)$ are defined by 
\begin{subequations}
\begin{align}
\label{gm}
G^0_m(q) &=\sum_{n=0}^\infty (-1)^n \frac{q^{n(n+1)/2+m n}}{(q;q)_n^2}
\\
\label{Gm}
G^1_m(q) &=\sum_{n=0}^\infty (-1)^n \frac{q^{n(n+1)/2+m n}}{(q;q)_n^2}
\left(2m+ E_1(q) + 2 \sum_{j=1}^n \frac{1+q^j}{1-q^j} \right) \,,
\end{align}
\end{subequations}

for $|q|<1$ and extended to $|q|>1$ by
$G^j_m(q^{-1}) = (-1)^j G^j_m(q)$.  Observe that $G_0(q)=G(q)$, the
vector that appears in the factorization~\eqref{Z410-fac} of the
state-integral $Z_{\knot{4}_1}(0;\tau)$.  The matrix $W_m(q)$
of holomorphic functions in $|q| \neq 1$ satisfies several
properties summarized in the following theorem.

\begin{theorem}
  \label{thm.410}
  $W_m(q)$ is a fundamental solution of the linear $q$-difference
  equation~\eqref{41qdiff} that has constant determinant
  \begin{equation}
\label{det41}
\det(W_m(q))=2 \,,
\end{equation}
satisfies the symmetry 
\begin{equation}
  \label{W41inv}
  W_m(q^{-1}) = W_{-m}(q)
  \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \,,
\end{equation}
the orthogonality property
\begin{equation}
\label{WWT41b}
\frac{1}{2} W_m(q)
\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
W_{m}(q)^T =
\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} 
\end{equation}








as well as
\begin{equation}
\label{WWT41}
\frac{1}{2} W_m(q)
\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
W_{\ell}(q)^T \in \SL(2,\BZ[q^\pm]) 
\end{equation}
for all integers $m, \ell$ and for $|q| \neq 1$. 
\end{theorem}

\begin{conjecture} 
\label{conj.41M0}  
Equation~\eqref{MR} holds where the matrices $M_R(q)$ are
given in terms of $W_{-1}(q)$ as follows
\begin{subequations}
\begin{align}
  \label{M41I}
  M_I(q)
  &= W_{-1}(q)^T \,
    \begin{pmatrix}
      0 & -1 \\
      1 & -1
    \end{pmatrix}, & |q|<1 \,,
  \\
  \label{M41II}
  M_{II}(q)
  &= \begin{pmatrix}
    1 & 0 \\
    0 & -1
  \end{pmatrix} \, W_{-1}(q)^T \,
        \begin{pmatrix}
          1 & 0 \\
          1 &-1
        \end{pmatrix}, & |q| <1 \,,
  \\
  \label{M41III}
  M_{III}(q)
  &=
    W_{-1}(q^{-1})^T \,
    \begin{pmatrix}
      1 & 0 \\
      1 & 1 \end{pmatrix}, & |q| >1 \,,
  \\
  \label{M41IV}
  M_{IV}(q)
  &=\begin{pmatrix}
    1 & 0 \\
    0 & -1
  \end{pmatrix} \,
        W_{-1}(q^{-1})^T \,
        \begin{pmatrix}
          0 & 1 \\
          1 & 1
        \end{pmatrix}, & |q|>1 \,.
\end{align}
\end{subequations}
\end{conjecture}

Assuming the above conjecture, we can now describe completely the
resurgent structure of $\Phi(\tau)$.  The Stokes matrices are given by
\begin{equation}
  \label{Spm1}
  \ms{S}^+(q)= 
  \mathfrak{S}_{I \rightarrow II}(q)
  \mfS_{IV\rightarrow I}, \qquad
  \ms{S}^-(q)= 
  \mathfrak{S}_{III \rightarrow IV}(q)
  \mfS_{II\rightarrow III}\,,
\end{equation}

where 
\begin{subequations}
  \begin{align}
  \label{Spm3}
    \mathfrak{S}_{I \rightarrow II}(q)
    &= M_{II}(q)^{-1} M_I(q)
    & \mathfrak{S}_{III \rightarrow IV}(q)
    &= M_{IV}(q^{-1})^{-1}
  M_{III}(q^{-1}) \\
  \label{Spm4}
    \mfS_{IV\rightarrow I}
    & = M_I(q)^{-1}M_{IV}(q)
    & \mfS_{II\rightarrow III}
    &= M_{III}(q)^{-1}M_{II}(q) \,.
\end{align}
\end{subequations}
(Compare with Equations~\eqref{SG} and~\eqref{4G} after
we set $\tx=1$ and replace $\tq$ by $q$).
Note that since $M_I(q), M_{II}(q)$ and
$M_{III}(q), M_{IV}(q)$ are given respectively as $q$-series and
$q^{-1}$-series in \eqref{M41I},\eqref{M41II} and
\eqref{M41III},\eqref{M41IV}, analytic continuation as discussed below
\eqref{Gm} is needed when one computes
$\mfS_{IV\rightarrow I},\mfS_{II\rightarrow II}$ in \eqref{Spm4}.
Using~\eqref{det41}--\eqref{WWT41} we can express the answer in terms
of $W_{-1}(q)$. Explicitly, the Stokes matrices are given by
\begin{subequations}
\begin{align}
  \label{S41p}
  \ms{S}^+(q)
  &={1\over 2} \begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix}
  W_{-1}(q) \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}W_{-1}(q)^T
  \begin{pmatrix} 0 & -1 \\ 1 & 2 \end{pmatrix}, & |q|<1\,, \\
  \label{S41m}
  \ms{S}^-(q)
  &= {1\over 2}
  \begin{pmatrix} -1 & -1 \\ 0 & 1 \end{pmatrix} W_{-1}(q)
  \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}W_{-1}(q)^T
  \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix}, & |q|<1 \,.
\end{align}
\end{subequations}
In the $q\rightarrow 0$ limit,
\begin{equation}
  \ms{S}^+(0) =
  \begin{pmatrix}
    1&3\\0&1
  \end{pmatrix},\quad
  \ms{S}^-(0) =
  \begin{pmatrix}
    1&0\\-3&1
  \end{pmatrix}
  \label{eq:S0u041}
\end{equation}
whose off-diagonal entries $-3,+3$ are Stokes constants associated to
the singularities $\iota_{2,1}$ and $\iota_{1,2}$ on the negative and
positive real axis respectively, and they agree with the matrix of
integers obtained numerically in~\cite{gh-res,GZ:kashaev}. In
addition, we can assemble the Stokes constants into
the matrix $\calS$ of Equation~\eqref{calS} (after we set $\tx=1$
and replace $\tq$ by $q$). The resulting matrix $\mc{S}^+(q)$
has entries in $q\BZ[[q]]$, and we find
\begin{align}
  \mc{S}^+_{\s_1,\s_1}(q) =
  &\ms{S}^+(q)_{1,1}-1\nn=
  &-8 q - 9 q^2 + 18 q^3 + 46 q^4 + 90 q^5 + 62 q^6+\cO(q^7),\\
  \mc{S}^+_{\s_1,\s_2}(q) =
  &\ms{S}^+(q)_{1,2}/\ms{S}^+(q)_{1,1}-\mc{S}^{(0)}_{\s_1,\s_2}\nn=
  &9 q + 75 q^2 + 642 q^3 + 5580 q^4 + 48558 q^5 + 422865 q^6+\cO(q^7),\\
  \mc{S}^+_{\s_2,\s_1}(q) =
  &\ms{S}^+(q)_{2,1}/\ms{S}^+(q)_{1,1}\nn=
  &-9 q - 75 q^2 - 642 q^3 - 5580 q^4 - 48558 q^5 - 422865 q^6+\cO(q^7),\\
  \mc{S}^+_{\s_2,\s_2}(q) =
  &\ms{S}^+(q)_{2,2} -1-
    \ms{S}^+(q)_{1,2}\ms{S}^+(q)_{2,1}/\ms{S}^+(q)_{1,1}\nn=
  &8 q + 73 q^2 + 638 q^3 + 5571 q^4 + 48538 q^5 + 422819 q^6+\cO(q^7).
\end{align}
We notice the symmetry
\begin{equation}
  \mc{S}^{(k)}_{1,2}=
  -\mc{S}^{(k)}_{2,1},\quad \text{for } k\in\IZ_{>0}\,,
\end{equation}
which is due to the reflection property
$\varphi_{\s_1}(-\tau^*)= \varphi_{\s_2}(\tau)^*$ of the asymptotic
series.  Also experimentally it appears that the entries of the matrix
$\mc{S}^+(q) = (\mc{S}^+_{\s_i,\s_j}(q))$ (except the upper-left one)
are (up to a sign) in $\IN[[q]]$.


Similarly we can extract the Stokes constants
$\mc{S}^{(-k)}_{\s_i,\s_j}$ associated to the singularities in the
lower half planes and collect them in $q^{-1}$-series
$\mc{S}^-_{\s_i,\s_j}(q^{-1})$ accordingly, and we find
\begin{equation}
  
  
  
  \mc{S}_{\s_i,\s_j}^{(-k)} = -\mc{S}^{(+k)}_{\s_j,\s_i},\;i\neq j\,,
  \quad\text{and}\quad \mc{S}_{\s_1,\s_1}^{(-k)}  =
  \mc{S}_{\s_2,\s_2}^{(+k)},\;\; \mc{S}_{\s_2,\s_2}^{(-k)}  =
  \mc{S}_{\s_1,\s_1}^{(+k)},\quad \text{for } k\in \IZ_{>0}.
\end{equation}


A nontrivial consistency check in the above calculation is that the
matrices $\mfS_{IV\rightarrow I}(q)$ and $\mfS_{II\rightarrow III}(q)$
should come out to be independent of $q$, and coincide with
$\ms{S}^-(0)$ and $\ms{S}^+(0)$. That is exactly what we find.

The fourth and last ingredient, which makes a full circle of ideas, is
the descendant state-integral of the $\knot{4}_1$ knot
\begin{equation}
\label{Z410-desc}
Z_{\knot{4}_1,m,\mu}(0;\tau) = 
\int_{\mc{D}} \Phi_\bb(v)^2 \, \re^{-\pi \ri v^2
+ 2\pi(m \bb - \mu \bb^{-1})v} \, \rd v \qquad
(m, \mu \in \BZ) \,.
\end{equation}

The integration contour $\mc{D}$ asymptotes at infinity to the horizontal line
$\text{Im}{v} = v_0$ with $v_0 >|\text{Re}(m\bb-\mu\bb^{-1})|$ but is deformed
near the origin so that all the poles of the quantum dilogarithm
located at
\begin{equation}
  c_\bb + \ri\bb r +\ri \bb^{-1}s,\quad r,s\in\IZ_{\geq 0},
\end{equation}
are above the contour.
The integral $Z_{\knot{4}_1,m,\mu}(0;\tau)$ is a holomorphic function of $\tau \in \BC'$ that coincides with
$Z_{\knot{4}_1}(0;\tau)$ when $m=\mu=0$ and can be expressed bilinearly
in $G_m(q)$ and $G_\mu(\tq)$ as follows
\begin{equation}
  \label{410-desc-fac}
  Z_{\knot{4}_1,m,\mu}(0;\tau) 
  =
  (-1)^{m-\mu+1}\ri q^{\frac{m}{2}}\tq^{\frac{\mu}{2}} 
  \left(\frac{q}{\tq}\right)^{\frac{1}{24}} \frac{1}{2}
  \left(\sqrt{\tau} \,G^0_\mu(\tq) G^1_m(q) - \frac{1}{\sqrt{\tau}}
    G^1_\mu(\tq) G^0_m(q)\right) \,.
\end{equation}
It follows that the matrix-valued function 

















\begin{align}
  \label{W410-desc}
  W_{m,\mu}(\tau) = 
    (W_\mu(\tq)^T)^{-1}
    \begin{pmatrix}
      1/\sqrt{\tau} & 0 \\ 0 & \sqrt{\tau}
    \end{pmatrix} W_m(q)^T
\end{align}
defined for $\tau=\BC\setminus\BR$, has entries given by the
descendant state-integrals (up to multiplication by a prefactor
of~\eqref{410-desc-fac})

and hence extends to a holomorphic function of $\tau \in \BC'$ for all
integers $m$ and $\mu$. Using this for $m=-1$ and $\mu=0$ and the
orthogonality relation~\eqref{WWT41b}, it follows that we can express
the Borel sums of $\Phi(\tau)$ in a region $R$ in terms of descendant
state-integrals and hence, as holomorphic functions of $\tau \in \BC'$
as follows. For instance, in the region $I$ we have
\begin{equation}
  s_I(\Phi)(\tau) = M_I(\tq)^{-1}
  \begin{pmatrix}
    \frac{1}{\sqrt{\tau}} g^0_0(\tau) \\
    \sqrt{\tau} g^1_0(\tau)
  \end{pmatrix}
  = \ri\left(\frac{q}{\tq}\right)^{-\frac{1}{24}}
  \begin{pmatrix}
    Z_{\knot{4}_1,0,0}(0;\tau) -\tq^{1/2} Z_{\knot{4}_1,0,-1}(0;\tau) \\ 
    Z_{\knot{4}_1,0,0}(0;\tau)
\end{pmatrix}
\end{equation}
  
This completes the discussion of $u=0$ for the $\knot{4}_1$ knot.


\subsection{The $\knot{5}_2$ knot when $u=0$}
\label{sub.52x=1}

The state integral of the $\knot{5}_2$ at $u=0$ is given by
\begin{equation}
  \label{Z520}
  Z_{\knot{5}_2}(0;\tau) = 
  \int_{\BR+\ri 0} \Phi_\bb(v)^3 \, \re^{-2\pi \ri v^2} \rd v \,.
\end{equation}
The critical points of the integrand are the logarithms of the
solutions $\xi_1 \approx 0.78492 + 1.30714 \ri$,
$\xi_2 \approx 0.78492 - 1.30714 \ri$ and $\xi_3 \approx 0.43016$ of
the polynomial equation
\begin{equation}
  \label{52xi}
  (1-y)^3=y^2 \,.
\end{equation}
The trace field of the $\knot{5}_2$ knot is $\BQ(\xi_1)$, the cubic
field of discriminant $-23$, which has three complex embeddings
labeled by $\s_j$ for $j=1,2,3$ corresponding to the $x_j$, and the
labeling set is $\calP=\{\s_1,\s_2,\s_3\}$, where $\s_1$ corresponds
to the geometric representation of the $\knot{5}_2$ knot, $\s_2$ to
the complex conjugate of the geometric representation and $\s_3$ for
the corresponding real representation.

The first ingredient is a vector of formal power series

\be\Phi(\tau)=
\begin{pmatrix} \Phi_{\s_1}(\tau)\\ \Phi_{\s_2}(\tau) \\
\Phi_{\s_3}(\tau) \end{pmatrix}
\ee

where 

\begin{equation}
  \label{volume-52}
  \Im\,V(\s_1) = -\Im\,V(\s_2) =\text{Vol}(\knot{5}_2)= 2.82812\ldots
\end{equation}

is the hyperbolic volume of the knot $\knot{5}_2$ and the first few
terms of
$\varphi_{\s_j}(\tau/(2\pi \ri)) \in \delta_j^{-1/2}
\BQ(\xi_j)[[\tau]]$ are given by 
{\small
\begin{align}
\label{varphi52}
  \varphi_{\s_j}\left(\frac{\tau}{2\pi \ri}\right) =
  &\left(\frac{-3\xi_j^2+3\xi_j-2}{23}\right)^{1/4}
    \left(1+\frac{-242\xi^2+209\xi-454}{2^2\cdot 23^2}\tau
    +\frac{12643\xi^2-22668\xi+25400}{2^5\cdot 23^3}\tau^2\right.
  \\
  \notag
  &\left.+\frac{-35443870\xi^2+85642761\xi-164659509}
    {2^7\cdot 3\cdot 5\cdot 23^5}\tau^3 + \dots \right) \,.    
  
  
  
  
  
  
\end{align}
}

The second ingredient is two vectors
$H^+(q)= (H^+_0(q), H^+_1(q), H^+_2(q))^T$ and
$H^-(q) = (H^-_0(q),H^-_1(q),H^-_2(q))^T$ of $q$-series defined for
$|q|<1$ by
\begin{subequations}
\begin{align}
\label{Hp0}
  H^+_0(q)
  &=\sum_{n=0}^\infty \frac{q^{n(n+1)}}{(q;q)_n^3}\,,
\\
\label{Hp1}
  H^+_1(q)
  &=\sum_{n=0}^\infty \frac{q^{n(n+1)}}{(q;q)_n^3}
    \left(1+2n-3E_1^{(n)}(q)\right) \,,
  \\
  \label{Hp2}
  H^+_2(q)
  &=\sum_{n=0}^\infty \frac{q^{n(n+1)}}{(q;q)_n^3}
    \left((1+2n-3E_1^{(n)}(q))^2-3E_2^{(n)}(q)-\frac{1}{6}E_2(q)\right) \,.
\end{align}
\end{subequations}
and
\begin{subequations}
\begin{align}
\label{Hn0}
  H^-_0(q)
  &=\sum_{n=0}^\infty (-1)^n\frac{q^{\frac{1}{2}n(n+1)}}{(q;q)_n^3}\,,
\\
\label{Hn1}
  H^-_1(q)
  &=\sum_{n=0}^\infty (-1)^n\frac{q^{\frac{1}{2}n(n+1)}}{(q;q)_n^3}
    \left(\frac{1}{2}+n-3E_1^{(n)}(q)\right) \,,
  \\
  \label{Hn2}
  H^-_2(q)
  &=\sum_{n=0}^\infty (-1)^n\frac{q^{\frac{1}{2}n(n+1)}}{(q;q)_n^3}
  \left(\big(\frac{1}{2}+n-3E_1^{(n)}(q)\big)^2
    -3E_2^{(n)}(q)-\frac{1}{12}E_2(q)\right) \,,
\end{align}
\end{subequations}
where
\begin{equation}
  E_l^{(n)}(q) = \sum_{s=1}^\infty \frac{s^{l-1}q^{s(n+1)}}{1-q^s}.
  \label{eq:Eln}
\end{equation}
The two sets of $q$-series can be extended to $|q|>1$ and are in fact
related by $H^+_k(q^{-1})=(-1)^k H^-_k(q)$, and define a $q$-series
$H_k(q)$ for $|q| \neq 1$ by
\begin{equation}
  H_k(q) = \begin{cases}
    H^+_k(q) & \qquad |q|<1 \\
    (-1)^k H^-_k(q^{-1}) & \qquad |q|>1 \,.
  \end{cases}
\end{equation}
Likewise, we define holomorphic functions $h_k(\tau)$ in $\BC\setminus\BR$ by
\begin{equation}
  h_k(\tau) =
  \begin{cases}
    H^+_k(\re^{2\pi\ri \tau}), & \quad \Im(\tau) > 0\\
    (-1)^k H^-_k(\re^{-2\pi\ri \tau}), & \quad \Im(\tau) <0
  \end{cases}, \quad k=0,1,2\,. 
\end{equation}
These series appear in the factorization of the state-integral of the
$\knot{5}_2$ knot given in~\cite[Cor.1.8]{GK:qseries}
\begin{equation}
  \label{Z520-fac}
  Z_{\knot{5}_2}(0;\tau) =
  -\frac{\re^{\frac{\pi\ri}{4}}}{2} \left(\frac{q}{\tq}\right)^{\frac{1}{8}} 
  \left(
    \tau H_0^-(\tq) H_2^+(q) -2 H^-_1(\tq) H^+_1(q)+ \tau^{-1} H^-_2(\tq) H^+_0(q) 
  \right), \qquad (\tau \in \BC\setminus\BR).
\end{equation}
The above factorization follows by applying the residue theorem to the
integrand of~\eqref{Z520}, a meromorphic function of $v$ with
prescribed zeros and poles. In particular, the integrand
of~\eqref{Z520} determines the $q$-hypergeometric formula for the
vectors $H^+(q)$, $H^-(q)$ of
$q$-series.  

As in the case of the $\knot{4}_1$ knot, multiplying the vector
$h(\tau)^T=(h_0(\tau) , h_1(\tau), h_2(\tau) )^T$ by the automorphy
factors $\diag(\tau^{-1},1,\tau)$ (dictated by~\eqref{Z520-fac}),
and looking at the asymptotics as $\tau$ approaches zero in sectors,
we found that

\begin{equation}
\label{MR52}
\re^{\frac{3\pi\ri}{4}}
\diag(\tau^{-1},1,\tau) h(\tau)
= M_R (\tq) \, s_R(\Phi)(\tau) \,,
\end{equation}
where the right hand side depends on the sectors of Borel resummation.
The Borel plane singularities of the component series of the vector
$\Phi(\tau)$ are similarly located at 
\begin{equation}
  \iota_{i,j} = \frac{V(\s_i) - V(\s_j)}{2\pi\ri},\quad i,j=1,2,3,i\neq j\,,
\end{equation}
as well as

\begin{equation}
  2\pi\ri k,\; \iota_{i,j}+2\pi\ri k,\quad k\in \IZ_{\neq 0},
\end{equation}
which form vertical towers as illustrated in Figure~\ref{fig:sings-u0-52}.

In particular, the two singularities $\iota_{1,2},\iota_{2,1}$ are on
the positive and negative real axis.  We pick out the four sectors
which separate the two singularities on the real axis and all the
others, and label them by $I,II,III,IV$, as illustrated in
Figure~\ref{fig:secs-u0-52}.





\begin{figure}[htpb!]
\leavevmode
\begin{center}
\includegraphics[height=7cm]{tw3_borelplane_s1u0}\hspace{3ex}
\includegraphics[height=7cm]{tw3_borelplane_s2u0}\hspace{3ex}
\includegraphics[height=7cm]{tw3_borelplane_s3u0}
\end{center}
\caption{The singularities in the Borel plane for the series
  $\varphi_{\sigma_{j}} (0;\tau)$ for $j=1,2,3$ of knot $\knot{5}_2$.}
\label{fig:sings-u0-52}
\end{figure}

\begin{figure}[htpb!]
\leavevmode
\begin{center}
\includegraphics[height=7cm]{tw3_regions_u0.pdf}
\end{center}
\caption{Four different sectors in the $\tau$-plane for $\Phi(0;\tau)$
  of knot $\knot{5}_2$ and the line $L$ that divides the $\tau$-plane.}
\label{fig:secs-u0-52}
\end{figure} 











To identify the matrices $M_R$, we consider the third ingredient,
the linear $q$-difference equation 
\begin{equation}
  \label{52qdiffp}
  y_{m}(q) -3y_{m+1}(q)+(3-q^{2+m}) y_{m+2}(q) - y_{m+3}(q)=0 \qquad (m \in \BZ) \,,
\end{equation}











They have fundamental solution sets given by the columns of the
following matrix 
\begin{equation}
  W_m(q) =
  \begin{cases}
    W_m^+(q), & \quad |q|<1\\
    \begin{pmatrix}
      0&0&1\\0&1&0\\1&0&0
    \end{pmatrix}
    W_{-m-2}^-(q^{-1})
    \begin{pmatrix}
      1&0&0\\0&-1&0\\0&0&1
    \end{pmatrix}
    
    , & \quad |q| >1 \,.
  \end{cases}
\end{equation}
where the matrices $W^\v_m(q)$ with $\v=\pm$ are respectively
\begin{equation}
  \label{Hfund}
  W^{\v}_m(q) =
  \begin{pmatrix}
    H^\v_{0,m}(q) & H^\v_{1,m}(q) & H^\v_{2,m}(q) \\
    H^\v_{0,m+1}(q) & H^\v_{1,m+1}(q) & H^\v_{2,m+1}(q) \\
    H^\v_{0,m+2}(q) & H^\v_{1,m+2}(q) & H^\v_{2,m+2}(q) 
  \end{pmatrix}, \qquad (|q| \neq 1)
\end{equation}
with entries the $q$-series

\begin{subequations}
\begin{align}
\label{Hp0m}
  H^+_{0,m}(q)
  &=\sum_{n=0}^\infty \frac{q^{n(n+1)+nm}}{(q;q)_n^3}\,,
\\
\label{Hp1m}
  H^+_{1,m}(q)
  &=\sum_{n=0}^\infty \frac{q^{n(n+1)+nm}}{(q;q)_n^3}
    \left(1+2n+m-3E_1^{(n)}(q)\right) \,,
  \\
  \label{Hp2m}
  H^+_{2,m}(q)
  &=\sum_{n=0}^\infty \frac{q^{n(n+1)+nm}}{(q;q)_n^3}
    \left((1+2n+m-3E_1^{(n)}(q))^2-3E_2^{(n)}(q)-\frac{1}{6}E_2(q)\right) \,,
\end{align}
\end{subequations}
and
\begin{subequations}
\begin{align}
\label{Hn0m}
  H^-_{0,m}(q)
  &=\sum_{n=0}^\infty (-1)^n\frac{q^{\frac{1}{2}n(n+1)+nm}}{(q;q)_n^3}\,,
\\
\label{Hn1m}
  H^-_{1,m}(q)
  &=\sum_{n=0}^\infty (-1)^n\frac{q^{\frac{1}{2}n(n+1)+nm}}{(q;q)_n^3}
    \left(\frac{1}{2}+n+m-3E_1^{(n)}(q)\right) \,,
  \\
  \label{Hn2m}
  H^-_{2,m}(q)
  &=\sum_{n=0}^\infty (-1)^n\frac{q^{\frac{1}{2}n(n+1)+nm}}{(q;q)_n^3}
  \left(\big(\frac{1}{2}+n+m-3E_1^{(n)}(q)\big)^2-3E_2^{(n)}(q)
    -\frac{1}{12}E_2(q)\right) \,,
\end{align}
\end{subequations}

for $|q|<1$ and extended to $|q|>1$ by the relation
$H^+_{k,m}(q^{-1}) = (-1)^k H^-_{k,-m}(q)$.  Observe that
$H^\v_{k,0}(q)=H^\v_{k}(q)$.









The matrix $W_m(q)$ of holomorphic functions in $|q| \neq 1$ satisfies
several properties summarized in the following theorem.

\begin{theorem}
  \label{thm.520}
  $W_m(q)$ is a fundamental solution of the linear $q$-difference
  equation~\eqref{52qdiffp} that has constant determinant
\begin{equation}
  \label{det52}
  \det(W_m(q))=2 \,,
\end{equation}
satisfies






the orthogonality property 
\begin{equation}
  \label{WWT52b}
  \frac{1}{2} W_{m-1}(q)
  \begin{pmatrix} 0 & 0 & 1 \\ 0&2&0\\ 1 & 0 &0  \end{pmatrix}
  W_{-m-1}(q^{-1})^T =
  \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1\\0 & 1 & 3-q^{m} \end{pmatrix} \,.
\end{equation}
as well as 
\begin{equation}
  \label{WWT52}
  \frac{1}{2} W_m(q)
  \begin{pmatrix} 0 & 0 & 1 \\ 0&2&0\\ 1 & 0 &0 \end{pmatrix}
  W_{\ell}(q^{-1})^T \in \SL(3,\BZ[q^\pm]) 
\end{equation}
for all integers $m, \ell$ and for $|q| \neq 1$.
\end{theorem}

\begin{conjecture}
  \label{conj.52M0}
  Equation~\eqref{MR52} holds where the matrices $M_R(q)$ are given in
  terms of $W_{-1}(q)$ as follows 
\begin{subequations}
\begin{align}
  \label{M52I}
  M_I(q)
  &= W_{-1}(q)^T \,
    \begin{pmatrix}
      0 & 0 & 1 \\
      -1 & 3 & 0 \\
      0 & -1 & 0
    \end{pmatrix}, & |q|<1 \,,  \\
  \label{M52II}
  M_{II}(q)
  &=\begin{pmatrix}
      1&0&0\\
      0&-1&0\\
      0&0&1
    \end{pmatrix} \,
           W_{-1}(q)^T \,
           \begin{pmatrix}
             0&0&1\\
             3&-1&0\\
             -1&0&0
           \end{pmatrix}, & |q|<1 \,, \\
  \label{M52III}
  M_{III}(q)
  &=
  
  
  
  
  
         W_{-1}(q)^T \,
         \begin{pmatrix}
           0&0&1\\
           -1&-1&0\\
           -1&0&0
         \end{pmatrix}, & |q| >1 \,, \\
  \label{M52IV}
  M_{IV}(q)
  &=\begin{pmatrix}
      1&0&0\\
      0&-1&0\\
      0&0&1
    \end{pmatrix} \,
    W_{-1}(q)^T \,
    \begin{pmatrix}
      0&0&1\\
      -1&-1&0\\
      0&-1&0
    \end{pmatrix}, & |q| >1 \,.
\end{align}
\end{subequations}
\end{conjecture}

Assuming the above conjecture, we can now describe completely the
resurgent structure of $\Phi(\tau)$, following the same computation as
in the case of the $\knot{4}_1$ knot. The Stokes matrices are given
by~\eqref{Spm1}--\eqref{Spm4}.
Note that since $M_I(q), M_{II}(q)$ and
$M_{III}(q), M_{IV}(q)$ are given respectively as $q$-series and
$q^{-1}$-series in \eqref{M52I},\eqref{M52II} and
\eqref{M52III},\eqref{M52IV}, analytic continuation as discussed below
\eqref{eq:Eln} is needed when one computes
$\mfS_{IV\rightarrow I},\mfS_{II\rightarrow II}$ in \eqref{Spm4}.
Using~\eqref{det52}--\eqref{WWT52} we
can express the answer in terms of $W_{-1}(q)$. Once again, we find
that the the Stokes matrices $\mfS_{IV\rightarrow I}(q)$ and
$\mfS_{II\rightarrow III}(q)$ are independent of $q$, consistent with
semiclassical asymptotics. The Stokes matrices are given by
\begin{subequations}
\begin{align}
  \label{S52p}
  \ms{S}^+(q)
  &={1\over 2}
    \begin{pmatrix}
      0&1&0\\
      0&1&1\\
      -1&0&0
    \end{pmatrix}W_{-1}(q^{-1})
            \begin{pmatrix}
              0&0&1\\
              0&-2&0\\
              1&0&0
            \end{pmatrix} W_{-1}(q)^T
                   \begin{pmatrix}
                     0&0&-1\\
                     1&1&0\\
                     0&1&0
                   \end{pmatrix},\quad |q|<1\\
  \label{S52m}
  \ms{S}^-(q)
  &= {1\over 2}
    \begin{pmatrix}
      0&3&-1\\
      0&-1&0\\
      1&0&0
    \end{pmatrix} W_{-1}(q)
           \begin{pmatrix}
             0&0&1\\
             0&-2&0\\
             1&0&0
           \end{pmatrix}W_{-1}(q^{-1})^T
                  \begin{pmatrix}
                    0&0&1\\
                    3&-1&0\\
                    -1&0&0
                  \end{pmatrix} \,,\quad |q|<1.
\end{align}
\end{subequations}
These Stokes matrices completely describe the resurgent structure of
$\Phi(\tau)$.  They also satisfy other statements in
Conjectures~\ref{conj.asy} and~\ref{conj.S3D} when $x=1$. The
$q\rightarrow 0$ limit of the Stokes matrices factorizes
\begin{align}
  \ms{S}^+(0) =
  &\mfS_{\s_3,\s_1}\mfS_{\s_3,\s_2}\mfS_{\s_1,\s_2}
    =
     \begin{pmatrix}
       1&0&0\\0&1&0\\-3&0&1
     \end{pmatrix}
     \begin{pmatrix}
       1&0&0\\0&1&0\\0&3&1
     \end{pmatrix}
     \begin{pmatrix}
      1&4&0\\0&1&0\\0&0&1
    \end{pmatrix},  \label{eq:S0pu052}\\
  \ms{S}^-(0) =
  &\mfS_{\s_1,\s_3}\mfS_{\s_2,\s_3}\mfS_{\s_2,\s_1}
    =
     \begin{pmatrix}
       1&0&3\\0&1&0\\0&0&1
     \end{pmatrix}
     \begin{pmatrix}
       1&0&0\\0&1&-3\\0&0&1
     \end{pmatrix}
     \begin{pmatrix}
      1&0&0\\-4&1&0\\0&0&1
    \end{pmatrix}, \label{eq:S0nu052}
\end{align}
where the non-vanishing off-diagonal entry of $\mfS_{\s_i,\s_j}$ is
the Stokes constant associated to the Borel singularity $\iota_{i,j}$.
Assembling these off-diagonal entries in a matrix, we obtain the matrix
\begin{equation}
\label{GZ52}
\begin{pmatrix}
  0 & 4 & 3 \\ -4 & 0 & -3 \\ -3 & 3 & 0
  \end{pmatrix}
\end{equation}
that was found numerically in~\cite[Sec.3.3]{GZ:kashaev}. In addition,
we can assemble the Stokes constants into the matrix $\calS$ of
Equation~\eqref{calS} (after we set $\tx=1$ and replace $\tq$ by $q$).
The resulting matrix $\mc{S}^+(q)$ has entries in $q\BZ[[q]]$, and we
find
\begin{subequations} 
\begin{align}
  \mc{S}^+_{\s_1,\s_1} =
  &\ms{S}^+(q)_{1,1}-1\nn=
  &-12 q+3 q^2+74 q^3+90 q^4+33 q^5+\cO(q^6),\\
  \mc{S}^+_{\s_1,\s_2} =
  &12 q+141 q^2+1520 q^3+17397 q^4+191970 q^5+\cO(q^6),\\
  \mc{S}^+_{\s_1,\s_3} =
  &q+3 q^2+9 q^3+30 q^4+99 q^5+\cO(q^6),\\
  \mc{S}^+_{\s_2,\s_1} =
  &-12 q-141 q^2-1520 q^3-17397 q^4-191970 q^5+\cO(q^6),\\
  \mc{S}^+_{\s_2,\s_2} =
  &12 q+141 q^2+1582 q^3+17583 q^4+194703 q^5+\cO(q^6),\\
  \mc{S}^+_{\s_2,\s_3} =
  &-21 q-235 q^2-2586 q^3-28593 q^4-316104 q^5+\cO(q^6),\\
  \mc{S}^+_{\s_3,\s_1} =
  &-q-3 q^2-9 q^3-30 q^4-99 q^5+\cO(q^6),\\
  \mc{S}^+_{\s_3,\s_2} =
  &21 q+235 q^2+2586 q^3+28593 q^4+316104 q^5+\cO(q^6),\\
  \mc{S}^+_{\s_3,\s_3} =
  &0.
\end{align}
\end{subequations}
The Stokes constants enjoy the symmetry
\begin{equation}
  \mc{S}^{(k)}_{\s_i,\s_j} =
  -\mc{S}^{(k)}_{\s_{\varphi(i)},\s_{\varphi(j)}},\;\; i\neq
  j,\quad \text{for } k\in\IZ_{>0}\,,
\end{equation}
with $\varphi(1)=2,\varphi(2)=1,\varphi(3)=3$.
We notice that the entries of the matrix $\mc{S}^+(q) =
(\mc{S}^+_{\s_i,\s_j}(q))$ (except the upper-left one) are (up to a
sign) in $\IN[[q]]$. Similarly we can extract the Stokes constants
$\mc{S}^{(-k)}_{\s_i,\s_j}$ associated to the singularities in the
lower half plane, and we find
\begin{equation}
  \mc{S}^{(-k)}_{\s_i,\s_j} = - \mc{S}^{(+k)}_{\s_j,\s_i},\;i\neq j,
  \quad\text{and}\quad
  \mc{S}^{(-k)}_{\s_i,\s_i} =
  \mc{S}^{(+k)}_{\s_{\varphi(i)},\s_{\varphi(j)}},\quad
  \text{for } k\in\IZ_{>0}\,.
\end{equation}

The fourth and last ingredient, which makes a full circle of ideas, is
the descendant state-integral of the $\knot{5}_2$ knot 
\begin{equation}
  \label{Z520-desc}
  Z_{\knot{5}_2,m,\mu}(0;\tau) = 
  \int_{\mc{D}} \Phi_\bb(v)^3 \,
  \re^{-2\pi \ri v^2 + 2\pi(m \bb - \mu \bb^{-1})v} \, \rd v \qquad
  (m, \mu \in \BZ) \,.
\end{equation}
Here the same contour $\mc{D}$ as in \eqref{Z410-desc} is used.  It is
a holomorphic function of $\tau \in \BC'$ that coincides with
$Z_{\knot{5}_2}(0;\tau)$ when $m=\mu=0$ and can be expressed
bilinearly in $H^+_{k,m}(q)$ and $H^-_{k,\mu}(\tq)$ as follows
\begin{align}
  \label{520-desc-fac}
    Z_{\knot{5}_2,m,\mu}(0;\tau) 
    =&
    (-1)^{m-\mu+1}\frac{\re^{\frac{\pi\ri}{4}}}{2}
    q^{\frac{m}{2}}\tq^{\frac{\mu}{2}} 
    \left(\frac{q}{\tq}\right)^{\frac{1}{8}} \\ \notag & 
    \left(\tau \, H^-_{0,\mu}(\tq)H^+_{2,m}(q)
      -2H^-_{1,\mu}(\tq)H^+_{1,m}(q) +
      \tau^{-1}\, H^-_{2,\mu}(\tq)H^+_{0,m}(q)\right) \,.
\end{align}
It follows that the matrix-valued function 






















\begin{align}
  \label{W520-desc}
  W_{m,\mu}(\tau) = (W_\mu(\tq)^T)^{-1}
  \begin{pmatrix} \tau^{-1} & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \tau
    \end{pmatrix}  W_m(q)^T 
\end{align}
defined for $\tau=\BC\setminus\BR$, has entries given by the
descendant state-integrals (up to multiplication by a prefactor
of~\eqref{520-desc-fac}) and hence extends to a holomorphic function
of $\tau \in \BC'$ for all integers $m$ and $\mu$. Using this for
$m=-1$ and $\mu=0$ and the orthogonality relation~\eqref{WWT52b}, it
follows that we can express the Borel sums of $\Phi(\tau)$ in a region
$R$ in terms of descendant state-integrals and hence, as holomorphic
functions of $\tau \in \BC'$ as follows. For instance, in the region
$I$ we have
\begin{equation}
  s_I(\Phi)(\tau) = \re^{\frac{3\pi\ri}{4}}M_I(\tq)^{-1}

  \begin{pmatrix}
    \tau^{-1}h_0(\tau) \\
    h_1(\tau) \\
    \tau h_2(\tau)
  \end{pmatrix}
  = \ri\left(\frac{q}{\tq}\right)^{-\frac{1}{8}}
  \begin{pmatrix}
    Z_{\knot{5}_2,0,0}(0;\tau)-\tq^{1/2}Z_{\knot{5}_2,0,-1}(0;\tau) \\
    Z_{\knot{5}_2,0,0}(0;\tau)\\
    
    \tq^{-1/2}Z_{\knot{5}_2,0,1}(0;\tau)
\end{pmatrix}
\end{equation}
  
This completes the discussion of $u=0$ for the $\knot{5}_2$ knot.

---
doc_id: arxiv-2208.14188v2
doc_title: "Resurgence in complex Chern-Simons theory at generic levels"
section_id: sec-012-43-resurgent-structure
section_title: "Resurgent structure"
section_number: 4.3
pages: 32-34
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.7
latex_coverage_ratio: 0.812
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels — In this note we study the resurgent structure of sl(2, C) Chern-Simons state integral model on knot complements S3\41, S3\52 with generic"
---
\label{sc:41.lvlk}

\begin{figure}
  \centering
  \includegraphics[height=6cm]{fig8_regions_m_peacock}
  \caption{Singular points of the Borel transform of the vector of
    trans-series of the $sl(2,\IC)$ Chern-Simons theory at level $k=1$
    on the complement of the knot $\knot{4}_1$.}
  \label{fg:sing.k1.41}
\end{figure}

We collect the trans-series associated to the geometric and conjugate
flat connections in a vector
\begin{equation}
  \Phi_{\knot{4}_1}^{(k)}(x;\tau) =
  \begin{pmatrix}
    \Phi_{\knot{4}_1}^{(k,\s_1)}\\
    \Phi_{\knot{4}_1}^{(k,\s_2)}
  \end{pmatrix}(x;\tau).
\end{equation}
The singularities of the Borel transform of each component
trans-series are located in $\Lambda_{i}^{(k)}$ given in
\eqref{eq:Lmdu}.  In the case of level $k=1$, we superimpose the Borel
singularities of the components of $\Phi_{\knot{4}_1}^{(1)}(x;\tau)$
and plot them in Fig.~\ref{fg:sing.k1.41}.





At a generic level $k\geq 1$, the
distrubtion of the Borel plane singularities is the same and their
actual locations are reduced by a factor of $1/k$ according to
\eqref{eq:Lmdu}.


As explained in Section~\ref{sc:resurg}, Stokes constants of
individual Borel plane singularities can be extracted from global
Stokes automorphisms.

The entire Borel plane is divided by Stokes rays of components of
$\Phi_{\knot{4}_1}^{(k)}(x;\tau)$ into infinitely many cones.  We
label the four cones above and below the positive and negative real
axes by $I,II,III,IV$, ordered in counter-clockwise direction, as
illustrated in Fig.~\ref{fg:sing.k1.41}.  We choose to calculate the
global Stokes automorphism
$\mf{S}_+^{(k)}(\tx;\tq) = \mf{S}^{(k)}_{IV\rightarrow II}(\tx;\tq)$
and
$\mf{S}_-^{(k)}(\tx;\tq) = \mf{S}^{(k)}_{II \rightarrow IV}(\tx;\tq)$,
both in the anti-clockwise direction, which encode all the Stokes
constants.

In order to derive the Stokes automorphisms, we first calculate the
Borel resummation of the trans-series.  Following
\cite{Garoufalidis:2020xec} and with numerical evidence presented
shortly after, We claim that they can be written as bilinear products
of holomorphic blocks in $q$ and $\tq$. Concretely,
\begin{subequations}
\begin{align}
  s_{I}(\Phi^{(k)}_{\knot{4}_1})(x;\tau) =
  &\begin{pmatrix}
    -\tx & 1 + \tx^{-1}\\
    0&1
  \end{pmatrix}W_{-1}(\tx;\tq^{-1})
       \Delta^{(k)}(\tau) B(x;q),\quad |\tq|<1,
       \label{eq:s1.41}\\
  s_{II}(\Phi^{(k)}_{\knot{4}_1})(x;\tau) =
  &\begin{pmatrix}
    0 & -\tx \\ 1 & -\tx - \tx^2
  \end{pmatrix}W_{-1}(\tx^{-1};\tq^{-1})
                    \begin{pmatrix}
                      1&0\\0&-1
                    \end{pmatrix}\Delta^{(k)}(\tau) B(x;q),\quad |\tq|<1,
                              \label{eq:s2.41}\\
  s_{III}(\Phi^{(k)}_{\knot{4}_1})(x;\tau) =
  &\begin{pmatrix}
    0&-\tx\\1&1
  \end{pmatrix} W_{-1}(\tx^{-1};\tq^{-1})
               \begin{pmatrix}
                 1&0\\0&-1
               \end{pmatrix}\Delta^{(k)}(\tau)B(x;q),\quad |\tq|>1,
  \label{eq:s3.41}\\
  s_{IV}(\Phi^{(k)}_{\knot{4}_1})(x;\tau) =
  &\begin{pmatrix}
    -\tx&-\tx\\0&1
  \end{pmatrix} W_{-1}(\tx;\tq^{-1})\Delta^{(k)}(\tau)B(x;q),\quad |\tq|<1.
                  \label{eq:s4.41}
\end{align}
\end{subequations}
Here $W_{-1}(x,q)$ is the Wronskian of holomorphic blocks defined in
\eqref{eq:W.41}, and
\begin{equation}
  B(x;q) =
  \begin{pmatrix}
    A_0(x;q)\\
    B_0(x;q)
  \end{pmatrix}
\end{equation}
$\Delta^{(k)}(\tau)$ is the diagonal matrix defined by
\begin{equation}
  \Delta^{(k)}(\tau) =
  \diag(\re^{-\frac{\pi\ri
      k}{4}-\frac{\pi\ri}{2k}-\frac{\pi\ri}{4k}(\tau+\tau^{-1})},
  \re^{\frac{\pi\ri k}{4}+\frac{\pi\ri}{2k}+\frac{\pi\ri}{4k}(\tau+\tau^{-1})}
  ).
\end{equation}
From \eqref{eq:s1.41} and \eqref{eq:s2.41}, we can derive the Stokes
automorphism $\mf{S}_{I\rightarrow II}^{(k)}(\tq)$ which encompasses all
the Stokes constants in the upper half plane.  This step involves only
multiplication of $\tq$-series.  On the other hand, from
\eqref{eq:s1.41} and \eqref{eq:s4.41} we can derive the Stokes
constants associated to the three Borel plane singularities on the
positive real axis, and this step involves analytic continuation of
the Wronskian $W_{-1}(\tx^{-1};\tq^{-1})$ from inside to outside the
unit circle with the help of \eqref{eq:Wcont.41}.  We can combine the
two results to write down the global Stokes automorphism
$\mf{S}_+^{(k)}(\tx;\tq)$ from the ray $\rho_{0_-}$ to
$\rho_{\pi+0_-}$.  Likewise, we can compute the global Stokes
automorphism $\mf{S}_-^{(k)}(\tx;\tq)$ from the ray $\rho_{\pi+0_-}$
to $\rho_{2\pi+0_-}$.  Together they encompass the Stokes constants of
all the Borel plane singularities.
\begin{align}
  \mf{S}_+^{(k)}(\tx;\tq) =
  &\begin{pmatrix}
    0&-1\\\tx^{-1}&-1-\tx
  \end{pmatrix}W_{-1}(\tx^{-1};\tq^{-1})W_{-1}(\tx;\tq)^T
                    \begin{pmatrix}
                      0&\tx\\-1&-1-\tx^{-1}
                    \end{pmatrix},\quad |\tq|<1\\
  \mf{S}_-^{(k)}(\tx;\tq) =
  &\begin{pmatrix}
    \tx&\tx\\0&-1
  \end{pmatrix}W_{-1}(\tx;\tq) W_{-1}(\tx^{-1};\tq^{-1})^T
                \begin{pmatrix}
                  \tx^{-1}&0\\\tx^{-1}&-1
                \end{pmatrix},\quad |\tq|<1.
\end{align}
In particular, we notice that the Stokes automorphisms and therefore
the Stokes constants do not depend on the level $k$.

At level $k=1$ numerical evidences for the position of Borel plane
singularities as well as
\eqref{eq:s1.41},\eqref{eq:s2.41},\eqref{eq:s3.41},\eqref{eq:s4.41}
were given in detail in \cite{Garoufalidis:2020xec}.



For higher levels, the computation is similar, although the expression
becomes more complicated.
At level $k=2$, we first 
choose $x = 6/5$, corresponding to $u=2\log(6/5)$ and $n=0$.  We
truncate the power series to $N = 100$ terms. The poles of the
Pad\'{e} approximant for $\Phi_{\knot{4}_1}^{(2)}(x,\tau)$ are shown
in Fig. \ref{fig:41level2n0all}. Notice that the accumulating poles on
the real axis hint at a branch cut on the corresponding exact Borel
plane.
\begin{figure}[h!]
  
  \subfloat[]{\includegraphics[width=0.5\textwidth]
    {41level2n0_numericalBorelplane.pdf}} \hspace{2ex}
  \subfloat[]{\includegraphics[width=0.5\textwidth]
    {41level2n0dual_numericalBorelplane.pdf}}
  \caption{The distribution of poles of the Pad\'{e} approximant for
    $(a): \varphi_{\knot{4}_1}^{(k=2,\sigma_1)}(x,\tau)$ and
    $(b): \varphi_{\knot{4}_1}^{(k=2,\sigma_2)}(x,\tau)$ with
    $x = 6/5$ and $N = 100$ terms.}
  \label{fig:41level2n0all}
\end{figure}
    
Clearly, if we consider the vector $\Phi(x,\tau)$, the Borel plane is
divided into four regions as promised.  It remains to check
\eqref{eq:s1.41},\eqref{eq:s2.41},\eqref{eq:s3.41},\eqref{eq:s4.41}.
The comparison is tabulated in Table \ref{tab:41k2n0}.

\begin{table}
  \centering
  \subfloat[Region $I$: $\tau = \frac{1}{8}\re^{\frac{\pi\ri}{4}}$]
  {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
     &|\frac{s_I(\Phi)(x;\tau)}{F_I(x;\tau)}- 1|
     &|\frac{s_I(\Phi)(x;\tau)}{s_I'(\Phi)(x;\tau)}- 1|
     &|\tq(\tau)|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
     \sigma_1& 8.6\times 10^{-16} & 3.5\times10^{-15}
     & \multirow{2}{*}{$1.9\times 10^{-8}$}
      & \multirow{2}{*}{$0.36$}\\
     \sigma_2& 3.7\times 10^{-23} & 2.4\times 10^{-22}&&\\\bottomrule
   \end{tabular}}\\
 \subfloat[Region $II$: $\tau = \frac{1}{8}\re^{\frac{3\pi\ri}{4}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{II}(\Phi)(x;\tau)}{F_{II}(x;\tau)}- 1|
    &|\frac{s_{II}(\Phi)(x;\tau)}{s_{II}'(\Phi)(x;\tau)}- 1|
    &|\tq(\tau)|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 3.7\times 10^{-23} & 2.4\times 10^{-22}
    & \multirow{2}{*}{$1.9\times 10^{-8}$}
      & \multirow{2}{*}{$0.36$}\\
     \sigma_2& 8.6\times 10^{-16} & 3.5\times 10^{-15}&&\\\bottomrule
   \end{tabular}}\\
 \subfloat[Region $III$: $\tau = \frac{1}{8}\re^{-\frac{3\pi\ri}{4}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{III}(\Phi)(x;\tau)}{F_{III}(x;\tau)}- 1|
    &|\frac{s_{III}(\Phi)(x;\tau)}{s_{III}'(\Phi)(x;\tau)}- 1|
    & |\tq(\tau)^{-1}|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 3.7\times 10^{-23} &2.4\times 10^{-22}
    & \multirow{2}{*}{$1.9\times 10^{-8}$}
      & \multirow{2}{*}{$0.36$}\\
     \sigma_2&8.6\times 10^{-16}  & 3.5\times 10^{-15}&&\\\bottomrule
  \end{tabular}}\\
 \subfloat[Region $IV$: $\tau = \frac{1}{8}\re^{-\frac{\pi\ri}{4}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{IV}(\Phi)(x;\tau)}{F_{IV}(x;\tau)}- 1|
    &|\frac{s_{IV}(\Phi)(x;\tau)}{s_{IV}'(\Phi)(x;\tau)}- 1|
    & |\tq(\tau)^{-1}|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 8.6\times 10^{-16} & 3.5\times 10^{-15}
    & \multirow{2}{*}{$1.9\times 10^{-8}$}
      & \multirow{2}{*}{$0.36$}\\
     \sigma_2& 3.7\times 10^{-23} & 2.4\times 10^{-22}&&\\\bottomrule
   \end{tabular}}
 \caption{We perform the numerical Borel resummation for
   $\Phi_{\knot{4}_1}^{(k=2)}(x;\tau)$ at $x = 6/5$
   ($u=2\log 6/5, n=0$) with 100 terms, after choosing suitable $\tau$
   in four different regions. We compare them with equations
   \eqref{eq:s1.41},\eqref{eq:s2.41},\eqref{eq:s3.41},\eqref{eq:s4.41}
   whose right hand side is denoted as $F_R(x;\tau)$. Meanwhile, we
   estimate the contribution of higher order terms by resumming
   $\Phi_{\knot{4}_1}^{(k=2)}(x;\tau)$ with 95 terms. The values of
   $|\tilde{q}(\tilde{q}^{-1})|$ and $|\tilde{x}^{\pm 1}|$ are also
   provided for comparison.}
  \label{tab:41k2n0}
\end{table}

We consider next
$x = -5/4$, corresponding to $u = 2\log(5/4)$ and $n=1$, and we
truncate the power series up to $N = 200$ terms. The positions of
poles for the Pad\'{e} approximant $\Phi_{\knot{4}_1}^{(k=2)}(x,\tau)$
are shown in Fig. \ref{fig:41level2n1all}. Again one observes the
emergent branch cut on the real axis.

We then present the numerical evidence of
\eqref{eq:s1.41},\eqref{eq:s2.41},\eqref{eq:s3.41},\eqref{eq:s4.41}
for each region in Tab.~\ref{tab:41k2n1}.  As we can see, the relative
errors between two sides of \eqref{eq:s1.41}, \eqref{eq:s2.41},
\eqref{eq:s3.41}, \eqref{eq:s4.41} (the first column) are always
within the precision of the Borel resummation (the second column), and
are always far smaller than a potential $\tq$ (or $1/\tq$ in the lower
half plane) or a $\tx^{\pm 1}$ correction (the third and the fourth
columns).

\begin{figure}[h!]
  \centering
  
         
  \subfloat[]
  {\includegraphics[width=0.5\textwidth]{41level2n1_numericalBorelplane.pdf}}
         
     

     
  \centering
  \subfloat[]
  {\includegraphics[width=0.5\textwidth]{41level2n1dual_numericalBorelplane.pdf}}
     
         
         
  \caption{The distribution of poles of the Pad\'{e} approximant for
    $(a): \varphi_{\knot{4}_1}^{(k=2,\sigma_1)}(x,\tau)$ and
    $(b): \varphi_{\knot{4}_1}^{(k=2,\sigma_2)}(x,\tau)$ with
    $x = -5/4$ and $N = 200$ terms.}
  \label{fig:41level2n1all}
\end{figure}

\begin{table}
  \centering
  \subfloat[Region $I$: $\tau = \frac{1}{10}\re^{\frac{\pi\ri}{5}}$]
  {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
     &|\frac{s_I(\Phi)(x;\tau)}{F_I(x;\tau)}- 1|
     &|\frac{s_I(\Phi)(x;\tau)}{s_I'(\Phi)(x;\tau)}- 1|
     &|\tq(\tau)|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
     \sigma_1& 8.2\times 10^{-22} & 8.6\times10^{-22}
     & \multirow{2}{*}{$9.6\times 10^{-9}$}
      & \multirow{2}{*}{$0.16$}\\
     \sigma_2& 3.9\times 10^{-36} & 5.1\times 10^{-36}&&\\\bottomrule
   \end{tabular}}\\
 \subfloat[Region $II$: $\tau = \frac{1}{10}\re^{\frac{4\pi\ri}{5}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{II}(\Phi)(x;\tau)}{F_{II}(x;\tau)}- 1|
    &|\frac{s_{II}(\Phi)(x;\tau)}{s_{II}'(\Phi)(x;\tau)}- 1|
    &|\tq(\tau)|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 3.9\times 10^{-36} & 5.1\times 10^{-36}
    & \multirow{2}{*}{$9.6\times 10^{-9}$}
      & \multirow{2}{*}{$0.16$}\\
     \sigma_2& 8.2\times 10^{-22} & 8.6\times 10^{-22}&&\\\bottomrule
   \end{tabular}}\\
 \subfloat[Region $III$: $\tau = \frac{1}{10}\re^{-\frac{4\pi\ri}{5}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{III}(\Phi)(x;\tau)}{F_{III}(x;\tau)}- 1|
    &|\frac{s_{III}(\Phi)(x;\tau)}{s_{III}'(\Phi)(x;\tau)}- 1|
    & |\tq(\tau)^{-1}|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 3.9\times 10^{-36} &5.1\times 10^{-36}
    & \multirow{2}{*}{$9.6\times 10^{-9}$}
      & \multirow{2}{*}{$0.16$}\\
     \sigma_2&8.2\times 10^{-22}  & 8.6\times 10^{-22}&&\\\bottomrule
  \end{tabular}}\\
 \subfloat[Region $IV$: $\tau = \frac{1}{10}\re^{-\frac{\pi\ri}{5}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{IV}(\Phi)(x;\tau)}{F_{IV}(x;\tau)}- 1|
    &|\frac{s_{IV}(\Phi)(x;\tau)}{s_{IV}'(\Phi)(x;\tau)}- 1|
    & |\tq(\tau)^{-1}|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 8.2\times 10^{-22} & 8.6\times 10^{-22}
    & \multirow{2}{*}{$9.6\times 10^{-9}$}
      & \multirow{2}{*}{$0.16$}\\
     \sigma_2& 3.9\times 10^{-36} & 5.1\times 10^{-36}&&\\\bottomrule
   \end{tabular}}
 \caption{We perform numerical Borel resummation for
   $\Phi_{\knot{4}_1}^{(k=2)}(x;\tau)$ at $x = -5/4$
   ($u=2\log 5/4, n=1$) with 200 terms, after choosing suitable $\tau$
   in four different regions. We compare them with equations
   \eqref{eq:s1.41},\eqref{eq:s2.41},\eqref{eq:s3.41},\eqref{eq:s4.41}
   whose right hand side is denoted as $F_R(x;\tau)$. Meanwhile, we
   estimate the contribution of higher order terms by resumming
   $\Phi_{\knot{4}_1}^{(k=2)}(x;\tau)$ with 195 terms. The values of
   $|\tilde{q}(\tilde{q}^{-1})|$ and $|\tilde{x}^{\pm 1}|$ are also
   provided for comparison.}
  \label{tab:41k2n1}
\end{table}

We also perform numerical analysis at level $k = 3$.
We choose $x = \frac{6}{5} \re^{2\pi n \ri/3}$ ($n=0,1,2$)
corresponding to $u=3\log(6/5)$ and $n=0,1,2$ respectively.
The power series are truncated up to $N=220$ terms.
The poles of the Pad\'{e} approximant have a similar structure to the
cases $k=1,2$, so we omit them here.  The numerical evidence for the
Borel resummation of the trans-series
\eqref{eq:s1.41},\eqref{eq:s2.41},\eqref{eq:s3.41},\eqref{eq:s4.41} in
each region are given in Tabs. \ref{tab:41k3n0}, \ref{tab:41k3n1} and
\ref{tab:41k3n2} respectively.

\begin{table}
  \centering
  \subfloat[Region $I$: $\tau = \frac{1}{9}\re^{\frac{\pi\ri}{5}}$]
  {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
     &|\frac{s_I(\Phi)(x;\tau)}{F_I(x;\tau)}- 1|
     &|\frac{s_I(\Phi)(x;\tau)}{s_I'(\Phi)(x;\tau)}- 1|
     &|\tq(\tau)|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
     \sigma_1& 3.1\times 10^{-15} & 1.6\times10^{-15}
     & \multirow{2}{*}{$1.5\times 10^{-5}$}
      & \multirow{2}{*}{$0.27$}\\
     \sigma_2& 4.6\times 10^{-27} & 5.2\times 10^{-26}&&\\\bottomrule
   \end{tabular}}\\
 \subfloat[Region $II$: $\tau = \frac{1}{9}\re^{\frac{4\pi\ri}{5}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{II}(\Phi)(x;\tau)}{F_{II}(x;\tau)}- 1|
    &|\frac{s_{II}(\Phi)(x;\tau)}{s_{II}'(\Phi)(x;\tau)}- 1|
    &|\tq(\tau)|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 5.8\times 10^{-27} & 1.7\times 10^{-27}
    & \multirow{2}{*}{$1.5\times 10^{-5}$}
      & \multirow{2}{*}{$0.27$}\\
     \sigma_2& 1.1\times 10^{-15} & 8.3\times 10^{-16}&&\\\bottomrule
   \end{tabular}}\\
 \subfloat[Region $III$: $\tau = \frac{1}{9}\re^{-\frac{4\pi\ri}{5}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{III}(\Phi)(x;\tau)}{F_{III}(x;\tau)}- 1|
    &|\frac{s_{III}(\Phi)(x;\tau)}{s_{III}'(\Phi)(x;\tau)}- 1|
    & |\tq(\tau)^{-1}|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 5.8\times 10^{-27} &1.7\times 10^{-27}
    & \multirow{2}{*}{$1.5\times 10^{-5}$}
      & \multirow{2}{*}{$0.27$}\\
     \sigma_2&1.1\times 10^{-15}  & 8.3\times 10^{-16}&&\\\bottomrule
  \end{tabular}}\\
 \subfloat[Region $IV$: $\tau = \frac{1}{9}\re^{-\frac{\pi\ri}{5}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{IV}(\Phi)(x;\tau)}{F_{IV}(x;\tau)}- 1|
    &|\frac{s_{IV}(\Phi)(x;\tau)}{s_{IV}'(\Phi)(x;\tau)}- 1|
    & |\tq(\tau)^{-1}|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 3.1\times 10^{-15} & 1.6\times 10^{-15}
    & \multirow{2}{*}{$1.5\times 10^{-5}$}
      & \multirow{2}{*}{$0.27$}\\
     \sigma_2& 4.6\times 10^{-27} & 5.2\times 10^{-26}&&\\\bottomrule
   \end{tabular}}
 \caption{We perform numerical Borel resummation for $\Phi_{\knot{4}_1}^{(k=3)}(x,\tau)$ at $x = 6/5$ with 220 terms, after choosing suitable $\tau$ in four different regions. We compare them with equations \eqref{eq:s1.41},\eqref{eq:s2.41},\eqref{eq:s3.41},\eqref{eq:s4.41} whose right hand side is denoted as $F_R(x,\tau)$. Meanwhile, we estimate the contribution of higher order terms by resumming $\Phi_{\knot{4}_1}^{(k=3)}(x,\tau)$ with 215 terms. The values of $|\tilde{q}(\tilde{q}^{-1})|$ and $|\tilde{x}^{\pm 1}|$ are also provided for comparison.}
  \label{tab:41k3n0}
\end{table}

\begin{table}
  \centering
  \subfloat[Region $I$: $\tau = \frac{1}{9}\re^{\frac{\pi\ri}{5}}$]
  {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
     &|\frac{s_I(\Phi)(x;\tau)}{F_I(x;\tau)}- 1|
     &|\frac{s_I(\Phi)(x;\tau)}{s_I'(\Phi)(x;\tau)}- 1|
     &|\tq(\tau)|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
     \sigma_1& 4.5\times 10^{-16} & 4.9\times10^{-16}
     & \multirow{2}{*}{$1.5\times 10^{-5}$}
      & \multirow{2}{*}{$0.27$}\\
     \sigma_2& 6.5\times 10^{-27} & 3.8\times 10^{-27}&&\\\bottomrule
   \end{tabular}}\\
 \subfloat[Region $II$: $\tau = \frac{1}{8}\re^{\frac{4\pi\ri}{5}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{II}(\Phi)(x;\tau)}{F_{II}(x;\tau)}- 1|
    &|\frac{s_{II}(\Phi)(x;\tau)}{s_{II}'(\Phi)(x;\tau)}- 1|
    &|\tq(\tau)|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 3.7\times 10^{-26} & 1.1\times 10^{-25}
    & \multirow{2}{*}{$5.3\times 10^{-5}$}
      & \multirow{2}{*}{$0.31$}\\
     \sigma_2& 6.1\times 10^{-15} & 5.7\times 10^{-15}&&\\\bottomrule
   \end{tabular}}\\
 \subfloat[Region $III$: $\tau = \frac{1}{8}\re^{-\frac{4\pi\ri}{5}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{III}(\Phi)(x;\tau)}{F_{III}(x;\tau)}- 1|
    &|\frac{s_{III}(\Phi)(x;\tau)}{s_{III}'(\Phi)(x;\tau)}- 1|
    & |\tq(\tau)^{-1}|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 3.2\times 10^{-26} &1.3\times 10^{-25}
    & \multirow{2}{*}{$5.3\times 10^{-5}$}
      & \multirow{2}{*}{$0.31$}\\
     \sigma_2&3.0\times 10^{-15}  & 9.8\times 10^{-15}&&\\\bottomrule
  \end{tabular}}\\
 \subfloat[Region $IV$: $\tau = \frac{1}{9}\re^{-\frac{\pi\ri}{5}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{IV}(\Phi)(x;\tau)}{F_{IV}(x;\tau)}- 1|
    &|\frac{s_{IV}(\Phi)(x;\tau)}{s_{IV}'(\Phi)(x;\tau)}- 1|
    & |\tq(\tau)^{-1}|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 4.5\times 10^{-16} & 4.9\times 10^{-16}
    & \multirow{2}{*}{$1.5\times 10^{-5}$}
      & \multirow{2}{*}{$0.27$}\\
     \sigma_2& 6.5\times 10^{-27} & 3.8\times 10^{-27}&&\\\bottomrule
   \end{tabular}}
 \caption{We perform numerical Borel resummation for $\Phi_{\knot{4}_1}^{(k=3)}(x,\tau)$ at $x = \frac{6}{5}\re^{4\pi\ri/3}$ with 220 terms, after choosing suitable $\tau$ in four different regions. We compare them with equations \eqref{eq:s1.41},\eqref{eq:s2.41},\eqref{eq:s3.41},\eqref{eq:s4.41} whose right hand side is denoted as $F_R(x,\tau)$. Meanwhile, we estimate the contribution of higher order terms by resumming $\Phi_{\knot{4}_1}^{(k=3)}(x,\tau)$ with 215 terms. The values of $|\tilde{q}(\tilde{q}^{-1})|$ and $|\tilde{x}^{\pm 1}|$ are also provided for comparison.}
  \label{tab:41k3n1}
\end{table}

\begin{table}
  \centering
  \subfloat[Region $I$: $\tau = \frac{1}{9}\re^{\frac{\pi\ri}{5}}$]
  {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
     &|\frac{s_I(\Phi)(x;\tau)}{F_I(x;\tau)}- 1|
     &|\frac{s_I(\Phi)(x;\tau)}{s_I'(\Phi)(x;\tau)}- 1|
     &|\tq(\tau)|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
     \sigma_1& 2.4\times 10^{-16} & 7.5\times10^{-16}
     & \multirow{2}{*}{$1.5\times 10^{-5}$}
      & \multirow{2}{*}{$0.27$}\\
     \sigma_2& 4.4\times 10^{-27} & 7.9\times 10^{-27}&&\\\bottomrule
   \end{tabular}}\\
 \subfloat[Region $II$: $\tau = \frac{1}{8}\re^{\frac{4\pi\ri}{5}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{II}(\Phi)(x;\tau)}{F_{II}(x;\tau)}- 1|
    &|\frac{s_{II}(\Phi)(x;\tau)}{s_{II}'(\Phi)(x;\tau)}- 1|
    &|\tq(\tau)|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 3.2\times 10^{-26} & 1.3\times 10^{-25}
    & \multirow{2}{*}{$5.3\times 10^{-5}$}
      & \multirow{2}{*}{$0.31$}\\
     \sigma_2& 3.0\times 10^{-15} & 9.8\times 10^{-15}&&\\\bottomrule
   \end{tabular}}\\
 \subfloat[Region $III$: $\tau = \frac{1}{8}\re^{-\frac{4\pi\ri}{5}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{III}(\Phi)(x;\tau)}{F_{III}(x;\tau)}- 1|
    &|\frac{s_{III}(\Phi)(x;\tau)}{s_{III}'(\Phi)(x;\tau)}- 1|
    & |\tq(\tau)^{-1}|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 3.7\times 10^{-26} &1.1\times 10^{-25}
    & \multirow{2}{*}{$5.3\times 10^{-5}$}
      & \multirow{2}{*}{$0.31$}\\
     \sigma_2&6.1\times 10^{-15}  & 5.7\times 10^{-15}&&\\\bottomrule
  \end{tabular}}\\
 \subfloat[Region $IV$: $\tau = \frac{1}{9}\re^{-\frac{\pi\ri}{5}}$]
 {\begin{tabular}{*{5}{>{$}c<{$}}}\toprule
    &|\frac{s_{IV}(\Phi)(x;\tau)}{F_{IV}(x;\tau)}- 1|
    &|\frac{s_{IV}(\Phi)(x;\tau)}{s_{IV}'(\Phi)(x;\tau)}- 1|
    & |\tq(\tau)^{-1}|& \text{Min}(|\tx(x,\tau)|,|\tx(x,\tau)^{-1}|)\\\midrule
    \sigma_1& 4.5\times 10^{-16} & 7.5\times 10^{-16}
    & \multirow{2}{*}{$1.5\times 10^{-5}$}
      & \multirow{2}{*}{$0.27$}\\
     \sigma_2& 4.4\times 10^{-27} & 7.9\times 10^{-27}&&\\\bottomrule
   \end{tabular}}
 \caption{We perform numerical Borel resummation for
   $\Phi_{\knot{4}_1}^{(k=3)}(x,\tau)$ at
   $x = \frac{6}{5}\re^{2\pi\ri/3}$ with 220 terms, after choosing
   suitable $\tau$ in four different regions. We compare them with
   equations
   \eqref{eq:s1.41},\eqref{eq:s2.41},\eqref{eq:s3.41},\eqref{eq:s4.41}
   whose right hand side is denoted as $F_R(x,\tau)$. Meanwhile, we
   estimate the contribution of higher order terms by resumming
   $\Phi_{\knot{4}_1}^{(k=3)}(x,\tau)$ with 215 terms. The values of
   $|\tilde{q}(\tilde{q}^{-1})|$ and $|\tilde{x}^{\pm 1}|$ are also
   provided for comparison.}
  \label{tab:41k3n2}
\end{table}

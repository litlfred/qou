---
doc_id: arxiv-2512.02998v1
doc_title: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy"
section_id: sec-008-4-isomorphisms-of-fundamental-groups
section_title: "Isomorphisms of fundamental groups"
section_number: 4
pages: 12-15
source_pdf: 2512.02998v1.pdf
source_sha256: 146ff93cd70baad4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.638
latex_coverage_ratio: 0.956
doc_brief: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy — We present sufficient criteria for the equivalence of tame knots at low regularity."
---
\label{sec:iso}
This section is devoted to the proof of Theorem~\ref{thm:isomorphic}. 
To start with, notice that  the mappings $r\mapsto\delta(M_i,r)$,
$i=1,2$, are non-decreasing, where $M_i$ are


the two non-empty,
closed and path-connected sets with path-connected complement 
$\R^n\setminus M_i$,

such that
\begin{equation}\label{eq:distortion-assumptions}
\delta(M_i,r_{M_i})< g_n\quad\Fo i=1,2, \quad\AND 
\dist_{\HH}(M_1,M_2)<\frac14
\min\{r_{M_1},r_{M_2}\},
\end{equation}
as requested in Theorem~\ref{thm:isomorphic}. 
So, we set
\begin{equation}\label{eq:r*}
r^*:=\min\{r_{M_1},r_{M_2}\},
\end{equation}
and apply Theorem~\ref{thm:dist-inc-flow} to the set $M:=M_1$
but with respect to the (possibly smaller) scale $r^*$ instead
of $r_{M_1}$, and with 
the parameter $\rho$ required in Theorem~\ref{thm:dist-inc-flow} 
chosen to satisfy
\begin{equation}\label{eq:rho-choice}
0<\rho<\frac14\cdot\Big(\,\frac14\min\{r_{M_1},r_{M_2}\}-\dist_{\HH}(M_1,M_2)\Big)=\frac14\cdot\Big(\frac14 r^*-\dist_{\HH}(M_1,M_2)\Big),
\end{equation}
to obtain the smooth function $h_1:=h_{M_1}^+:\R^n\setminus M_1\times [0,1]\to\R^n
\setminus  M_1$ with all the properties listed in that theorem.
Define the 
group homomorphism
$J:\pi_1(\R^n\setminus M_1)\to 
\pi_1(\R^n\setminus M_2) $ by means of
\begin{equation}\label{eq:def-J}
J([c]_1):=[h_1(\cdot,1)\circ c]_2,
\end{equation}
for any closed curve $c$ in $\R^n\setminus M_1$ representing the equivalence\footnote{We
choose the obvious notation $[\cdot]_i$ 
to indicate equivalence classes of closed loops 
in
the respective fundamental  group $\pi_1(\R^n\setminus M_i)$ for $i=1,2$.}
class $[c]_1\in\pi_1(\R^n\setminus M_1)$. Corollary \ref{cor:nearby-sets}
for $M:=M_1$ and $A:=M_2$ implies that
\begin{equation}\label{eq:respect-complements}
h_1(\R^n\setminus M_1,1)\subset \R^n\setminus M_2,
\end{equation}
because our assumption \eqref{eq:rho-choice} on $\rho$ clearly implies
$\dist_{\HH}(M_1,M_2)<\frac14 r^*<\frac12 r^*-\rho, $
that is, hypothesis \eqref{eq:nearby-sets} of Corollary \ref{cor:nearby-sets}
is satisfied for $r_M:=r^*$.
Inclusion \eqref{eq:respect-complements} shows that the mapping
$J$ defined in
\eqref{eq:def-J}  actually maps into $\pi_1(\R^n\setminus M_2)$, but we need to
verify that the definition does \emph{not} depend on the particular choice
of the loop $c$ in $\R^n\setminus M_1$. Indeed, for any other representative
loop $\tilde{c}$ in $\R^n\setminus M_1$ with $[\tilde{c}]_1=[c]_1$ there is,
by definition, a homotopy $\psi\in C^0(
\R/\Z\times [0,1],\R^n\setminus M_1)$ such that
$\psi(\cdot,0)=c(\cdot)$ and $\psi(\cdot,1)=\tilde{c}(\cdot)$. Then by 
\eqref{eq:respect-complements} the map $h_1(\cdot,1)\circ\psi$ is a homotopy in $\R^n\setminus
M_2$ connecting $h_1(\cdot,1)\circ\psi(\cdot,0)=h_1(c(\cdot),1)$ and
$h_1(\cdot,1)\circ\psi(\cdot,1)=h_1(\tilde{c}(\cdot),1)$, so that
$J([c]_1)=J([\tilde{c}]_1).$ Hence $J$ is well-defined.
\begin{lemma}[$J$ injective]\label{lem:injective}
The linear mapping $J:\pi_1(\R^n\setminus M_1)\to\pi_1(\R^n\setminus M_2)$
as defined in \eqref{eq:def-J} above is injective.
\end{lemma}
\begin{proof}
It suffices to show that for any null-homotopic loop in $\R^n\setminus M_2$ the 
preimage of its equivalence class under $J$ only contains null-homotopic 
loops in $\R^n\setminus M_1$. To that extent let $[c]_1\in\ker J\subset
\pi_1(\R^n\setminus M_1)$,
which means that there is a homotopy $\Psi\in C^0(
\R/\Z\times [0,1],\R^n\setminus
M_2)$ such that $\Psi(\cdot,0)=h_1(\cdot,1)\circ c(\cdot)$ and
$\Psi(\cdot,1)$ is constant. By means of Theorem~\ref{thm:dist-inc-flow}
for $M:=M_2$ (again with respect to the possibly smaller
scale $r^*$ instead of $r_{M_2}$)
we find the smooth function $h_2:=h_{M_2}^+ 
\in C^\infty((\R^n\setminus M_2)\times[0,1],\R^n\setminus M_2)$ 
with all the properties
listed there, as well as
\begin{equation}\label{eq:respect-complements2}
h_2(\R^n\setminus M_2,1)\subset \R^n\setminus M_1
\end{equation}
by means of Corollary \ref{cor:nearby-sets} applied to $M:=M_2$ and
$A:= M_1$. This corollary is applicable since our assumption \eqref{eq:rho-choice}
implies the hypothesis \eqref{eq:nearby-sets} similarly as in our
justification of \eqref{eq:respect-complements} above. Consequently,
the mapping $(s,t)\mapsto h_2(\Psi(s,t),1)$ is a homotopy in $\R^n\setminus M_1$.
By means of the monotonicity of $t\mapsto\dist(h_2(x,t),M_2)$ for any
$x\in\R^n\setminus M_2$ established in Theorem~\ref{thm:dist-inc-flow},
we infer with the help of the properties (1+) and (2+) therein, and 
\eqref{eq:rho-choice},
\begin{eqnarray*}
\dist(h_2(\cdot,t)\circ\Psi(s,0),M_1) & \ge &\dist(h_2(\cdot,t)\circ\Psi(s,0),M_2)
-\dist_{\HH}(M_1,M_2)\\
&\ge &\dist(h_2(\cdot,0)\circ\Psi(s,0),M_2)
-\dist_{\HH}(M_1,M_2)\\
&\overset{\textnormal{(1+)}}{=} &\dist(\Psi(s,0),M_2)
-\dist_{\HH}(M_1,M_2)\\
&\ge &\dist(\Psi(s,0),M_1)
-2\dist_{\HH}(M_1,M_2)\\
&=& \dist(h_1(\cdot,1)\circ c(s),M_1)-2\dist_{\HH}(M_1,M_2)\\
&\overset{\textnormal{(2+)},\eqref{eq:rho-choice}}{>} &
\textstyle\frac12 r^*-\rho-2\big(\frac14 r^*-4\rho\big)\\
& = & 7\rho >0\quad\Foa s,t\in [0,1].
\end{eqnarray*}
Therefore, the mapping $(s,t)\mapsto h_2(\Psi(s,0),t)$ is also a homotopy
in $\R^n\setminus M_1$, as well as $(s,t)\mapsto h_1(c(s),t)$ with $
c(s)=h_1(c(s),0)$ due to property (1+) in Theorem~\ref{thm:dist-inc-flow}
for $M:=M_1$. We now conclude with (1+) for $M:=M_2$:
\begin{align*}
[c]_1 & = [h_1(c,1)]_1=[\Psi(\cdot,0)]_1\overset{\textnormal{(1+)}}{=}
[h_2(\Psi(\cdot,0),0)]_1\\
& = [h_2(\Psi(\cdot,0),1)]_1=[h_2(\Psi(\cdot,1),1)]_1=[const.]_1,
\end{align*}
since $\Psi(\cdot,1)$ is constant. Here we have also used that $(s,t)\mapsto
h_2(\Psi(s,t),1)$ is a homotopy in $\R^n\setminus M_1$ by means of 
\eqref{eq:respect-complements2}. Thus, we have shown that $J$ is injective.
\end{proof}
\begin{lemma}[$J$ is surjective]\label{lem:surjective}
The injective linear mapping $J:\pi_1(\R^n\setminus M_1)\to\pi_1(\R^n\setminus M_2)$ as
defined in \eqref{eq:def-J} is also surjective.
\end{lemma}
\begin{proof}
For a given closed curve $\tilde{c}$ in $\R^n\setminus M_2$ representing
$[\tilde{c}]_2\in\pi_1(\R^n\setminus M_2)$ consider the smooth functions $h_i:=
h_{M_i}^+$ from Theorem~\ref{thm:dist-inc-flow} for $M:= M_i$, $i=1,2$, 
but with respect to the common smaller scale $r^*$ defined
in \eqref{eq:r*} instead of $r_{M_i}$,
and with $\rho$ as in \eqref{eq:rho-choice} with all the 
properties listed in that theorem, and satisfying \eqref{eq:respect-complements},
and \eqref{eq:respect-complements2}, respectively.
Then we can estimate, again using that $t\mapsto\dist(h_1(x,t),M_1)$ 
is non-decreasing, properties (1+) for  $h_1$ and (2+) for $h_2$ and
our smallness assumption \eqref{eq:rho-choice}, 
\begin{eqnarray}\label{eq:dist-h1h2}
\dist(h_1(\cdot,t)\circ h_2(\cdot,1)\circ\tilde{c},M_2) & \ge &
\dist(h_1(\cdot,t)\circ h_2(\cdot,1)\circ\tilde{c},M_1)-\dist_{\HH}(M_1,M_2)
\notag\\
&\ge &
\dist(h_1(\cdot,0)\circ h_2(\cdot,1)\circ\tilde{c},M_1)-\dist_{\HH}(M_1,M_2)\notag\\
& \overset{\textnormal{(1+)}}{=} &
\dist(h_2(\cdot,1)\circ\tilde{c},M_1)-\dist_{\HH}(M_1,M_2)\notag\\
&\ge &
\dist(h_2(\cdot,1)\circ\tilde{c},M_2)-2\dist_{\HH}(M_1,M_2)\\
&\overset{\textnormal{(2+)},\eqref{eq:rho-choice}}{>} &
\textstyle \big(\frac12 r^*-\rho\big)-2\big(\frac14 r^*-4\rho
\big) \notag\\
& = & 7\rho > 0,\notag
\end{eqnarray}
to infer that the mapping $(s,t)\mapsto h_1(h_2(\tilde{c}(s),1),t)$
is a homotopy in $\R^n\setminus M_2$. Therefore, by definition \eqref{eq:def-J}
of $J$ and property (1+) for $h_1$
$$
J\big([h_2(\cdot,1)\circ\tilde{c}]_1\big)
\overset{\eqref{eq:def-J}}{=}  [h_1(\cdot,1)\circ h_2(\cdot,1)\circ\tilde{c}]_2
 =  [h_1(\cdot,0)\circ h_2(\cdot,1)\circ\tilde{c}]_2
\overset{\textnormal{(1+)}}{=} 
[h_2(\cdot,1)\circ\tilde{c}]_2=[\tilde{c}]_2,
$$
where for the last equality we used the fact that also $(s,t)\mapsto
h_2(\tilde{c}(s),t)$ is a homotopy in $\R^n\setminus M_2$.
\end{proof}
To investigate peripheral subgroups of the fundamental groups
we first use the distance-decreasing flow of Theorem~\ref{thm:dist-dec-flow}
to derive a quantified sufficient condition for loops $c\in \R^n\setminus M$
to generate elements $[c]$ in the peripheral subgroup of $\pi_1(\R^n\setminus M)$.
\begin{proposition}[Elements of peripheral subgroups]
\label{prop:elements-peripheral}
Let $M\subset\R^n$ be a non-empty, closed and path-connected set with path-connected
complement $\R^n\setminus M$, such that $\delta(M,r_M)<g_n$ for some positive
scale $r_M$. Then the equivalence class $[c]$ of any loop $c:\R/\Z\to
B_{r_M}(M)\setminus M$ is an element of the peripheral subgroup
$P_M$ of $\pi_1(\R^n\setminus M)$.
\begin{proof}
Fix a loop $c\in C^0(\R/\Z,\R^n)$ with image $c(\R/\Z)\subset B_{r_M}(M)\setminus M$. We
need to show that for arbitrary small $\epsilon >0$, the closed curve $c$ is homotopic
to a loop $\tilde{c}$ in $B_\epsilon(M)\setminus M$. If $\epsilon> 
\delta:=\max_{x\in c(\R/\Z)}\dist(x,M)$
the curve
$c$ itself is the desired loop, so we may restrict to $\epsilon \in 
(0,\delta]\subset (0,r_M)$.
Apply Theorem~\ref{thm:dist-dec-flow} for $\rho:=\epsilon$ and
$\delta:=\max_{x\in c(\R/\Z)}\dist(x,M)<r_M$ (assuming w.l.o.g.\@ that 
$\epsilon<\delta$, otherwise increase $\delta$ slightly),
to obtain a smooth function
$h:=h_M^-:\R^n\setminus M\times [0,1]\to\R^n\setminus M$ with all the properties
listed in that theorem. Then the map $(s,t)\mapsto h(c(s),t)
=h(\cdot,t)\circ c(s)$ defines a homotopy in $\R^n\setminus M$,
connecting the curve $c(\cdot)
=h(\cdot,0)\circ c(\cdot)$ with the loop $\tilde{c}(\cdot):=h(c(\cdot),1).$ Property
(2-) of $h$ implies that $\tilde{c}(\R/\Z)\subset B_\epsilon(M).$
\end{proof}
\end{proposition}
Now we are in the position to give the full 
proof of our first main result.\\
{\it Proof of Theorem~\ref{thm:isomorphic}.}\,
The mapping $J:\pi_1(\R^n\setminus M_1)\to\pi_1(\R^n\setminus M_2)$ defined in
\eqref{eq:def-J} is an isomorphism as shown in Lemmas \ref{lem:injective} and
\ref{lem:surjective}. It remains to be checked that $J$ restricted to the
peripheral subgroup $P_{M_1}\subset\pi_1(\R^n\setminus M_1) $ maps $P_{M_1}$
isomorphically onto the peripheral subgroup $P_{M_2}$ of $\pi_1(\R^n\setminus M_2)$.
In the light of Lemma~\ref{lem:injective} is it sufficient 
to show $J(P_{M_1}) = P_{M_2}$.\par
``$\subset$'':
For $p\in P_{M_1}$ take a representative loop $c$ in $\R^n\setminus M_1$, i.e., 
$[c]_1=p$, with 
\begin{equation}\label{eq:close-loop}
\textstyle
\sup_{s\in\R/\Z}\dist\big(c(s),M_1\big)< \frac12 \min\{r_{M_1},r_{M_2}\}=\frac12 r^*,
\end{equation}
where $r^*$ was defined in \eqref{eq:r*}.
Let $h_1:=h_{M_1}^+:\R^n\setminus M_1\to\R^n\setminus M_1$
be the smooth function\footnote{This function was the one used for
the definition of the isomorphism $J$ in \eqref{eq:def-J}.}
of Theorem~\ref{thm:dist-inc-flow} for $M:=M_1,
$ but using the scale $r^*$   
instead of $r_{M_1}$ and $\rho$ as in \eqref{eq:rho-choice}.
Then, properties (2+) and (3+) of that theorem imply
\begin{equation}\label{eq:peripheral-ineq}
\textstyle
0<\frac14{r^*}<\frac12{r^*}-\rho\overset{\textnormal{(2+)}}{\le}\dist(h_1(c(s),1),M_1)\le
\frac12{r^*}\quad\Foa s\in \R/\Z,
\end{equation}
since if there were some $s\in\R/\Z$ such that $\dist (h_1(c(s),1),M_1)>
\frac12{r^*}$ then by continuity of $h_1$ we could find some $t^*\in (0,1)$
such that 
$$
\textstyle
\frac12{r^*}=\dist(h_1(c(s),t^*),M_1)\overset{\textnormal{(3+)}}{=}
\dist(h_1(c(s),1),M_1)>\frac12{r^*},
$$
contradiction. Moreover, by Corollary \ref{cor:nearby-sets} for $M:=M_1$ at scale
$r^*$ (instead of $r_{M_1}$), and $A:=M_2$, we have
\begin{equation}\label{eq:respect-complements3}
h_1(\R^n\setminus M_1,1)\subset\R^n\setminus M_2,
\end{equation}
since by means of \eqref{eq:rho-choice},
$\dist_{\HH}(M_1,M_2)<\frac14 r^*-4\rho<\frac12 r^*-\rho$,
so that hypothesis \eqref{eq:nearby-sets} of Corollary \ref{cor:nearby-sets}
is satisfied. In particular, $h_1(c(\R/\Z),1)\subset\R^n\setminus M_2$ so that
by \eqref{eq:peripheral-ineq} and hypothesis \eqref{eq:hausdorff}
\begin{eqnarray*}
0  < \dist(h_1(c(s),1),M_2) &\le &\dist(h_1(c(s),1),M_1)+\dist_{\HH}(M_1,M_2)\\
&\overset{\eqref{eq:peripheral-ineq},\eqref{eq:hausdorff}}{<} &
\textstyle
\frac12{r^*}+\frac14 \min\{r_{M_1},r_{M_2}\}
=\frac34 \min\{r_{M_1},r_{M_2}\}< r_{M_2}
\end{eqnarray*}
for all $s\in\R/\Z$.
Therefore, $h_1(c(\R/\Z),1)\subset B_{r_{M_2}}(M_2)\setminus M_2$. 

By definition \eqref{eq:def-J} of the isomorophism $J$ we find
$$
J(p)=J([c]_1)\overset{\eqref{eq:def-J}}{=}[h_1(\cdot,1)\circ c]_2\in P_{M_2}
\subset\pi_1(\R^n\setminus M_2)
$$
by means of Proposition \ref{prop:elements-peripheral} applied to
$M:=M_2$ and to the loop $h_1(\cdot,1)\circ c$.

``$\supset$'':
We finally need to show that $P_{M_2}\subset J(P_{M_1})$. For $q\in P_{M_2}$
there is a representative loop $\tilde{c}:\R/\Z\to\R^n\setminus M_2$ with
$[\tilde{c}]_2=q$ and $\sup_{s\in\R/\Z}\dist(\tilde{c}(s),M_2)<\frac12 r^*$.
According to Theorem~\ref{thm:dist-inc-flow} applied to $M:=M_2$ and
the smaller scale $r^*\le r_{M_2}$ and to 
$\rho$ as in \eqref{eq:rho-choice}, we find
the smooth function $h_2:=h_{M_2}^+:\R^n\setminus M_2\to\R^n\setminus M_2$ with 
all the properties listed in that theorem but
at scale $r^*$ (instead of $r_{M_2}$). Using properties (2+) and (3+)
in the same way as for $h_1$ above we obtain
\begin{equation}\label{eq:dist-peripheral2}
\textstyle
0<\frac14{r^*} <\frac12{r^*} -\rho\overset{\textnormal{(2+)}}{\le}
\dist\big(h_2(\tilde{c}(s),1),M_2\big)
\le\frac12{r^*}\quad\Foa s\in\R/\Z.
\end{equation}
From Corollary \ref{cor:nearby-sets} we deduce
\begin{equation}\label{eq:respect-complements4}
h_2(\R^n\setminus M_2,1)\subset\R^n\setminus M_1.
\end{equation}
Consequently,  by \eqref{eq:dist-peripheral2} and hypothesis \eqref{eq:hausdorff},
\begin{eqnarray*}
0<\dist\big(h_2(\cdot,1)\circ\tilde{c},M_1\big) & \le &
\dist\big(h_2(\cdot,1)\circ\tilde{c},M_2\big)+
\dist_{\HH}(M_1,M_2)\\
& \overset{\eqref{eq:dist-peripheral2},\eqref{eq:hausdorff}}{<} &
\textstyle
\frac12{r^*}+\frac14{r^*}=\frac34 \min\{r_{M_1},r_{M_2}\}<r_{M_1};
\end{eqnarray*}
hence $h_2(\tilde{c}(\R/\Z),1)\subset B_{r_{M_1}}(M_1)\setminus M_1$, which leads
us to set $p:=[h_2(\cdot,1)\circ\tilde{c}]_1\in P_{M_1}\subset\pi_1(\R^n\setminus M_1)$
by Proposition \ref{prop:elements-peripheral}.
Exactly\footnote{The only prerequisite for the estimate \eqref{eq:dist-h1h2} was that
$\tilde{c}$ is a loop in $\R^n\setminus M_2$ which we have in the present
context as well.}
as in \eqref{eq:dist-h1h2} in the proof of Lemma \ref{lem:surjective}
we can show that the mapping $(s,t)\mapsto h_1(h_2(\tilde{c}(s),1),t)$ defines a homotopy in 
$\R^n\setminus M_2$,  
 connecting the loop 
$$
h_2(\cdot,1)\circ\tilde{c}\overset{\textnormal{(1+)}}{=}h_1(h_2(\cdot,1)\circ\tilde{c},0)
$$
with $h_1(h_2(\cdot,1)\circ\tilde{c},1)$ so that by definition \eqref{eq:def-J} of $J$,
\begin{align*}
J(p)& = J([h_2(\cdot,1)\circ\tilde{c}]_1)\overset{\eqref{eq:def-J}}{=}
[h_1(\cdot,1)\circ h_2(\cdot,1)\circ\tilde{c}]_2\\
& = [h_2(\cdot,1)\circ\tilde{c}]_2=[\tilde{c}]_2=q,
\end{align*}
as desired. For the last equality we have used the fact that
$(s,t)\mapsto h_2(\tilde{c}(s),t)$ is a homotopy in $\R^n\setminus M_2$
connecting $\tilde{c}=h_2(\tilde{c},0)$ with $h_2(\cdot,1)\circ\tilde{c}$.
\hfill $\Box$



\section{Stability of knot equivalence}\label{sec:stability}
The equivalence of two tame knots $\g_1,\g_2\in C^0(\R/\Z,\R^3)$
with local distortion below $g_3$ (or even below
$\frac{\pi}{\sqrt{8}}$) at some positive scales, such that the knots 
are sufficiently close in 
terms of these scales, was stated in Corollary \ref{cor:equiv-knots}. This was a direct
consequence of Theorem~\ref{thm:isomorphic} applied to the knots' images $M_i:=
\g_i(\R/\Z)$, $i=1,2,$ in combination with Theorem~\ref{thm:gordon-luecke}. 
We are going to apply Corollary \ref{cor:equiv-knots} now
to a knot and a small Lipschitz perturbation of that knot to
prove the Lipschitz stability of knot equivalence, i.e., 
Corollary \ref{cor:lipschitz-stability}. For that we specify the local distortion
at some scale $r>0$ as
defined in \eqref{eq:local-distortion} in Definition \ref{def:local-distortion}
to the image $M:=\eta(\R/\Z)$ of a knot $\eta\in C^0(\R/\Z,\R^n)$ by writing
\begin{equation}\label{eq:local-distortion-knots}
\delta(\eta,r)\equiv\delta(\eta(\R/\Z),r) 
=\sup_{u,v\in\R/\Z, u\not= v\atop 0<|\eta(u)-\eta(v)|\le 2r}
\frac{d_\eta\big(\eta(u),\eta(v)\big)}{|\eta(u)-\eta(v)|},
\end{equation}
where the intrinsic distance $d_\eta(\eta(u),\eta(v))$ reduces to the periodic 
parameter distance $|u-v|_{\R/\Z}$ in case of arclength parametrized curves $\eta$.

\begin{proof}[Proof of Corollary {\ref{cor:lipschitz-stability}}]
By assumption there is a scale $r_\g\in(0,\tfrac12)$ such that $\delta(\g,r_\g)< g_3$ 
(or even
less than $\frac{\pi}{\sqrt{ 8 }}$.) Our aim is to show that for a given
function $h\in C^{0,1}(\R/\Z,\R^3)$ the perturbed
curve $\g_\epsilon=\g+\epsilon h$ has also local distortion
$\delta(\g_\epsilon,\hat{r}_{\g})<g_3 $ at
a (possibly smaller) scale $\hat{r}_\g>0$ independent of $0<|\epsilon|\ll 1$. Keeping
that scale fixed we can then take $|\epsilon| $ so small 
(depending on~$h$) that the $L^\infty$-distance
is controlled in terms of the two scales $r_\g$ and $\hat{r}_\g$.

To that extent consider $x,y\in [0,1]$ with $x<y$ 
to estimate
\begin{equation}\label{eq:euclid-eps}
|\g_\epsilon(x)-\g_\epsilon(y)|=
|\g(x)-\g(y)+\epsilon(h(x)-h(y))|\ge |\g(x)-\g(y)|-|\epsilon|\|h'\|_{L^\infty}(y-x).
\end{equation}
The intrinsic distance $d_{\g_\epsilon}(\g_\epsilon(x),\g_\epsilon(y))\equiv
d_{\g_\epsilon}(x,y)$ on $\g_\epsilon$ may be compared
to $d_\g(\g(x),\g(y))\equiv d_\g(x,y)$ on $\g$ by means of
\begin{align}\label{eq:intrinsic-eps-prep}
\textstyle
\big|\int_x^y |\g_\epsilon'(u)|du & -
\textstyle
\int_x^y |\g'(u)|du\big|=
\big|\int_x^y \big(|\g_\epsilon'(u)|-|\g'(u)|\big)du\big|\le\int_x^y
\big| |\g_\epsilon'(u)|-|\g'(u)|\big|du\notag\\
&\textstyle
\le\int_x^y |\g_\epsilon'(u)-\g'(u)|du=
\int_x^y|\epsilon h'(u)|du\le |\epsilon|\|h'\|_{L^\infty}(y-x),
\end{align}







whence
\begin{equation}\label{eq:intrinsic-eps}
\textstyle
d_{\g_\epsilon}(x,y)\le\int_x^y|\g_\epsilon'(u)|du
\overset{\eqref{eq:intrinsic-eps-prep}}{\le}
\int_x^y|\g'(u)|du+|\epsilon|\|h'\|_{L^\infty}(y-x)
\le(y-x)(1+|\epsilon|\|h'\|_{L^\infty}).
\end{equation}
Without loss of generality we may assume that 
$0< y-x\le\tfrac12$, so
$d_\g(x,y) = y-x$.
Combining \eqref{eq:euclid-eps} with \eqref{eq:intrinsic-eps} we deduce supposing
 $|\g(x)-\g(y)|<2r_\g$
\begin{align}
\begin{split}\label{eq:distortion-eps}
\textstyle\frac{d_{\g_\epsilon}(x,y)}{|\g_\epsilon(x)-\g_\epsilon(y)|}
&  \overset{\eqref{eq:intrinsic-eps},\eqref{eq:euclid-eps}}{\le}
\textstyle
\frac{d_{\g}(x,y)(1+|\epsilon|\|h'\|_{L^\infty})}{|\g(x)-\g(y)|-
|\epsilon|\|h'\|_{L^\infty}(y-x)}=
 \frac{d_{\g}(x,y)(1+|\epsilon|\|h'\|_{L^\infty})}{|\g(x)-\g(y)|
 \big(1-|\epsilon|\|h'\|_{L^\infty}\frac{d_\g(x,y)}{|\g(x)-\g(y)|}\big)} \\
 & \le \textstyle
 \delta(\g,r_\g)\cdot\frac{1+|\epsilon|\|h'\|_{L^\infty}}{
 1-|\epsilon|\|h'\|_{L^\infty}\delta(\g,r_\g)}<g_3,
\end{split}
\end{align}
if
\begin{equation}\label{eq:eps2}
\textstyle
|\epsilon|\le\epsilon_0:=\min\big\{\frac{g_3-\delta(\g,r_\g)}{\delta(\g,r_\g)(1+g_3)\|h'\|_{L^\infty}+1},\frac{r_\g}{\|h'\|_{L^\infty}+1}\big\}>0.



\end{equation}




Consequently, if $|\g_\epsilon(x)-\g_\epsilon(y)|\le2\hat r_\g$ where $\hat r_\g=\tfrac12 r_\g$
we infer
$|\g(y)-\g(x)|\le 2r_\g$, so $\delta(\g_\epsilon,\hat{r}_\g)<g_3$
for all $|\epsilon|\le\epsilon_0$
due to \eqref{eq:distortion-eps} and
\eqref{eq:eps2}.














It is important to notice that the scale
$\hat{r}_\g$ does \emph{not} depend on $\epsilon\in [-\epsilon_0,\epsilon_0]$.
With $\|\g-\g_\epsilon\|_{L^\infty}=|\epsilon|\|h\|_{L^\infty}$ this allows
us to choose
\begin{equation}\label{eq:final-epsilon-choice}
\textstyle
\epsilon_{\g,h}:=\min\Big\{\epsilon_0,\frac{\hat{r}_\g}{8\|h \|_{
L^\infty}+1}\Big\}
<\frac14 \min\{r_\g,\hat{r}_\g\}
\end{equation}
to also satisfy the hypothesis on the $L^\infty$-distance in Corollary 
\ref{cor:equiv-knots} to conclude that $\g\sim\g_\epsilon$ for all
$|\epsilon|\le\epsilon_{\g,h}.$ In addition, $\essinf_{\R/\Z}|\g_\epsilon'|
\ge\essinf_{\R/\Z}|\g'|-|\epsilon|\|h'\|_{L^\infty} > \frac12$
for all $|\epsilon|\le\epsilon_{\g,h}$, since $\epsilon_{\g,h}\le\epsilon_0\le
\tfrac12(\|h'\|_{L^\infty}+1)^{-1}$.
\end{proof}






































































































Before treating the stability of knot equivalence in the setting of
fractional Sobolev regularity let us point out that bounding  the
bilipschitz constant\footnote{\label{foot:bilip}In \cite{freedman-etal_1994} a bilipschitz constant
is defined as any number $L>0$ such that $L^{-1}d_\gamma(u,v)|\le|\gamma(u)-\gamma(v)|\le Ld_\gamma(u,v)$
holds for all $u,v\in\R/\Z$.
If $\gamma$ is parametrized by arclength then the infimum of those $L$
is $\bilip_I(\g)^{-1}$.}
\begin{equation}\label{eq:def-bilip}
\bilip_I(\g):=\inf_{\substack{u,v\in I\\u\ne v}}\frac{|\g(u)-\g(v)|}{|u-v|_{\R/\Z}}
\end{equation}
on an interval $I\subset\R$ from below, is closely related to
controlling the local distortion $\delta(\g,\cdot)$ at some
scale related to $I$, if the absolutely continuous parametrization $\g$
has positive
speed $v_\g=\essinf_{\R/\Z}|\g'|$, i.e., if $\g$ is an immersed curve.

The seminorm $\lfloor \g'\rfloor $ defining fractional Sobolev spaces allows us to bound
$\bilip(\g)$ as  in the following lemma, which is essentially contained
in \cite[Lemma 2.1]{blatt_2012a}; see also \cite[Lemma 2.1]{blatt-etal_2024}.


\begin{lemma}\label{lem:seminorm-bilip}
Let $I\subset\R$ be an interval and $\g:I\to\R^n$ an absolutely continuous
immersed curve with positive speed $v_\g=\essinf_{I}|\g'|$. 
Then one has for all $s,t\in I$ with $s<t$
\begin{equation}\label{eq:seminorm-bilip}
|\g(t)-\g(s)|^2\ge\Big\{v_\g^2-\frac12\int_s^t\int_s^t\frac{|\g'(u)-\g'(v)|^2}{|u-v|^2}dudv\Big\}|t-s|^2.
\end{equation}
\end{lemma}
As an immediate consequence one deduces
\begin{corollary}[Fractional seminorm controls bilipschitz constant]
\label{cor:seminorm-bilip}
If $\g\in W^{\frac32, 2}(I,\R^n)$ is arclength parametrized, then
\begin{equation}\label{eq:seminorm-bilip2}
|\g(t)-\g(s)|^2\ge\big(1-\frac12 \lfloor\g'\rfloor^2_{\frac12,2,I}\big)|t-s|^2\quad\Foa
s,t\in I.
\end{equation}
\end{corollary}

\begin{proof}[Proof of Lemma {\ref{lem:seminorm-bilip}}]

For parameters $s,t\in I$ with $s<t$ estimate
\begin{gather*}
|\g(s) -\g(t)|^2  
\textstyle
= \int_s^t\int_s^t\langle\g'(\sigma),\g'(\tau)\rangle_{\R^n}d\sigma 
d\tau
 \textstyle
= \frac12  \int_s^t\int_s^t \big(
|\g'(\tau)|^2+
|\g'(\sigma)|^2-|\g'(\tau)-\g'(\sigma)|^2\big)d\sigma d\tau\\
\textstyle
\ge v_\g^2|t-s|^2-\frac12\int_s^t\int_s^t|\g'(\tau)-\g'(\sigma)|^2d\sigma d\tau
\ge\textstyle
|t-s|^2\big\{v_\g^2-\frac12\int_s^t\int_s^t
\frac{|\g'(\tau)-\g'(\sigma)|^2}{|\tau-\sigma|^2}d\sigma d\tau\big\}.\qedhere
\end{gather*}

\end{proof}

We observe in \eqref{eq:seminorm-bilip2} that a small fractional seminorm
yields a bilipschitz  estimate, which is the key ingredient for the proof 
of the fractional stability of knot equivalence.

\noindent
{\it Proof of Corollary \ref{cor:fractional-stability}.}\,








Due to the absolute continuity of the double integral defining the
fractional seminorm there is a radius $\rho=\rho(\g)\in (0,\frac14]$  such
that $\sup_{x\in\R/\Z}\lfloor \g'\rfloor_{\frac12,2,B_\rho(x)} <\frac1{2\sqrt{2}}.$
Therefore,
\begin{equation}\label{eq:eta-seminorm}
\textstyle
\sup_{x\in\R/\Z}\lfloor \eta' \rfloor_{\frac12,2,B_\rho(x)}
\le
\sup_{x\in\R/\Z}\lfloor \g' \rfloor_{\frac12,2,B_\rho(x)}+\lfloor
\eta'-\g' \rfloor_{\frac12,2} < \frac1{\sqrt{2}}
\end{equation}
for all $\eta \in B_{\frac1{2\sqrt{2}}}(\g)\subset W^{\frac32,2}(\R/\Z,\R^3)$. By
means of Corollary \ref{cor:seminorm-bilip} we infer
\begin{equation}\label{eq:bilip-gamma-eta}
\textstyle
\min\big\{|\g(t)-\g(s)|,|\eta(t)-\eta(s)|\big\}>\frac{\sqrt{3}}2 
|t-s|\ge\frac{\sqrt{3}}2 d_\g(t,s)
=\frac{\sqrt{3}}2 d_\eta(t,s)
\end{equation}
for all arclength parametrized curves $\eta\in B_{\frac1{2\sqrt{2}}}(\g)\subset
W^{\frac32,2}(\R/\Z,\R^3)$ and all parameters $s,t\in\R/\Z$ with
intrinsic distance $d_\g(t,s)\equiv d_\g(\g(s),\g(t))=|t-s|_{\R/\Z}=
d_\eta(\eta(s),\eta(t))\equiv d_\eta(t,s)<2\rho.$

On the other hand,
$$
\textstyle
\sigma_\g:=
\inf\{|\g(t)-\g(s)|:d_\g(s,t)=|t-s|_{\R/\Z}\ge 2\rho\}\in (0,\frac12].
$$
By Sobolev embedding there is a constant $C_E$ such that $\|\zeta\|_{L^\infty}
\le C_E\|\zeta\|_{W^{\frac32,2}}$ for all $\zeta\in W^{\frac32,2}(\R/\Z,\R^3)$,
so that
\begin{equation}\label{eq:infty-distance-eta-gamma}
\textstyle
\|\eta-\gamma\|_{L^\infty}< \frac{\sigma_\g}{16}\quad\Foa\eta\in B_{\epsilon_\g}(\g)
\subset W^{\frac32,2}(\R/\Z,\R^3),
\end{equation}
where we have set $\epsilon_\g:=\min\{\frac1{2\sqrt{2}},\frac{\sigma_\g}{16C_E}\}$.
Therefore, for all $s,t\in\R/\Z$ with $d_\g(s,t)=d_\eta(s,t)
\ge 2\rho$ one has
\begin{equation}\label{eq:euclid-eta-gamma-global}
\textstyle
\min\big\{|\g(t)-\g(s)|,|\eta(t)-\eta(s)|\big\}>\frac{7}{8}\sigma_\g
>\frac{1}{2}\sigma_\g.
\end{equation}
Defining the common scale $r_{\g}:=\frac{\sigma_\g}4$ we find in view of 
\eqref{eq:bilip-gamma-eta} and \eqref{eq:euclid-eta-gamma-global}
\begin{equation}\label{eq:max-eta-gamma-distortion}
\textstyle
\max\big\{\delta(\g,r_\g),\delta(\eta,r_\g)\big\}\le\frac{2}{\sqrt{3}}<g_3
\end{equation}
for all arclength parametrized curves $\eta\in B_{\epsilon_\g}(\g)\subset
W^{\frac32,2}(\R/\Z,\R^3)$, since 
$g_3=\frac{\sqrt{32}}{\sqrt{27}}\frac{\pi}{\sqrt{8}}\in 
(\frac2{\sqrt{3}},\frac{\pi}2)$.
Inequality \eqref{eq:infty-distance-eta-gamma} allows us to apply
Corollary \ref{cor:equiv-knots} to conclude. Notice that we also used
the fact that arclength parametrized $W^{\frac32,2}$-knots have finite
M\"obius energy according to \cite[Theorem~1.1]{blatt_2012a}, and
are therefore tame \cite[Theorem~4.1]{freedman-etal_1994}, which is needed
in Corollary \ref{cor:equiv-knots}.\hfill $\Box$

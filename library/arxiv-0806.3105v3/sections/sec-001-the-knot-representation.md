---
doc_id: arxiv-0806.3105v3
doc_title: "KNOTS AND PREONS"
section_id: sec-001-the-knot-representation
section_title: "The Knot Representation"
section_number: null
pages: 3-7
source_pdf: 0806.3105v3.pdf
source_sha256: a37b4f2e96365d30
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.989
doc_brief: "KNOTS AND PREONS — It is shown that the four quantum trefoil solitons that are described by the irreducible representations D3/2 mm′ of the quantum algebra SLq(2) (and that may be identiﬁed with the"
---
We replace the point particles of standard theory with quantum
knots by attaching to each normal mode a knot state just as one
introduces spin by attaching a spin state.  The knot states and
the corresponding fields are defined only up to a gauge
transformation and the action is required to be invariant under
these gauge transformations.

We assume that the kinematical quantum states of the knot are
derived from the 
irreducible representations of the symmetry algebra of the knot,
namely$^3$
\be
{\cal{D}}^j_{mm^\prime}(a,b,c,d) = \sum_{\scriptstyle s\leq n_+
\atop\scriptstyle t\leq n_-} 
{\cal{A}}^j_{mm^\prime}(q,s,t)\delta(s+t,n_+^\prime)
a^sb^{n_+-s}c^td^{n_--t}
\ee
where
\begin{eqnarray}
n_\pm &=& j\pm m \\
n_\pm^\prime &=& j\pm m^\prime
\end{eqnarray}
and the arguments of ${\cal{D}}^j_{mm^\prime}$ obey the algebra
of $SL_q(2)$ as follows:
\be
\left.
\begin{array}{l}
ab = qba \\ ac = qca
\end{array} \right. \quad \left.
\begin{array}{l}
bd = qdb \\ cd = qdc
\end{array} \right. \quad \left.
\begin{array}{l}
bc = cb \\ \hfil 
\end{array} \right. \quad \left.
\begin{array}{l}
ad-qbc=1 \\ da-q_1cb=1 
\end{array} \right.  \qquad
q_1=q^{-1}
\ee

We shall refer to (2.4) as the ``knot algebra".  This algebra and
${\cal{D}}^j_{mm^\prime}(a,b,c,d)$ are defined only up to the
following gauge transformation
\be
\left.
\begin{array}{l}
a^\prime = e^{i\varphi_a}a \\ d^\prime = e^{-i\varphi_a}d
\end{array} \right. \qquad \left.
\begin{array}{l}
b^\prime = e^{i\varphi_b}b \\ c^\prime = e^{-i\varphi_b}c
\end{array} \right.
\ee
Eqs. (2.5) leave the algebra (2.4)
invariant and induce on the elements
of every representation the following transformation$^3$
\be
\begin{array}{rcl}
{\cal{D}}^j_{mm^\prime}(a^\prime,b^\prime,c^\prime,d^\prime)
&=& e^{i(m+m^\prime)\varphi_a}e^{i(m-m^\prime)\varphi_b}
{\cal{D}}^j_{mm^\prime}(a,b,c,d) \\
&=& e^{im(\varphi_a+\varphi_b)}e^{im^\prime(\varphi_a-\varphi_b)}
{\cal{D}}^j_{mm^\prime}(a,b,c,d)
\end{array}
\ee
We now associate ${\cal{D}}^j_{mm^\prime}$ with the geometrical
knot by setting
\be
\begin{array}{rcl}
j &=& \frac{N}{2} \\
m &=& \frac{w}{2} \\
m^\prime &=& \frac{r+1}{2}
\end{array}
\ee
where $w$ and $r$ are the writhe and rotation respectively and
where $N$ is the number of crossings.
The writhe and the rotation are topological invariants and we
shall also assume that $N$ is a dynamical invariant.  
The kinematic states of the quantum knot may be labelled by 
these three
invariants of the motion.  Then by (2.6) and (2.7)
\be
\begin{array}{rcl}
{\cal{D}}^{N/2}_{\frac{w}{2}\frac{r+1}{2}}
(a^\prime,b^\prime,c^\prime,d^\prime)&=& e^{i\frac{w}{2}
\varphi_w} e^{i\frac{r+1}{2}\varphi_r}
{\cal{D}}^{N/2}_{\frac{w}{2}\frac{r+2}{2}}(a,b,c,d) \\
&=& e^{-\frac{i}{k}Q(w)\varphi_w}
e^{-\frac{i}{k}Q(r)\varphi_r}
{\cal{D}}^{N/2}_{\frac{w}{2}\frac{r+1}{2}}(a,b,c,d)
\end{array}
\ee
where
\begin{eqnarray}
Q(w) &=&-k\frac{w}{2} \\
Q(r) &=& -k\frac{r+1}{2}
\end{eqnarray}
and $k$ is a constant to be determined.  $Q(w)$ and $Q(r)$ are two
topological
integrals of the motion.  The gauge transformations (2.8)
operate on all the normal modes and therefore on all fields.
We require that the 
action be invariant under these gauge transformations since
they are induced by the transformations (2.5) that leave the
defining
algebra (2.4) invariant.  Therefore 
by Noether's theorem $Q(w)$ and $Q(r)$ behave as
conserved charges and will be called the writhe charge and the
rotation charge.

We shall now make a direct comparison between $Q(w)$ and $Q(r)$ 
of the quantum knot and the charge and hypercharge of the 4
fermion families, each denoted by $(f_1,f_2,f_3)$.$^3$

\begin{table}[h]
\begin{center}
\begin{tabular}{ccccc|ccccc}
\multicolumn{5}{c}{\underline{Standard Representation}} &
\multicolumn{5}{c}{\underline{Knot Representation}} \\
\underline{$(f_1,f_2,f_3)$} & \underline{$t$} & 
\underline{$t_3$} &
\underline{$t_0$} & \underline{$Q_e$} & \underline{$(w,r)$} &
\underline{${\cal{D}}^{N/2}_{\frac{w}{2}\frac{r+1}{2}}$} &
\underline{$Q_w$} & \underline{$Q_r$} & \underline{$Q_w+Q_r$} \\
$(e,\mu,\tau)$ & $\frac{1}{2}$ & $-\frac{1}{2}$ & $-\frac{1}{2}$
& $-e$ & (3,2) & ${\cal{D}}^{3/2}_{\frac{3}{2}\frac{3}{2}}$ &
$-k\left(\frac{3}{2}\right)$ & $-k\left(\frac{3}{2}\right)$ &
$-3k$ \\
$(\nu_e,\nu_\mu,\nu_\tau)$ & $\frac{1}{2}$ & $\frac{1}{2}$ &
$-\frac{1}{2}$ & 0 & (-3,2) & ${\cal{D}}^{3/2}_{-\frac{3}{2}
\frac{3}{2}}$ & $-k\left(-\frac{3}{2}\right)$ &
$-k\left(\frac{3}{2}\right)$ & 0 \\
$(d,s,b)$ & $\frac{1}{2}$ & $-\frac{1}{2}$ & $\frac{1}{6}$ &
$-\frac{1}{3}e$ & (3,-2) & ${\cal{D}}^{3/2}_{\frac{3}{2}-\frac
{1}{2}}$ & $-k\left(\frac{3}{2}\right)$ & $-k\left(-\frac{1}{2}
\right)$ & $-k$ \\ 
$(u,c,t)$ & $\frac{1}{2}$ & $\frac{1}{2}$ & $\frac{1}{6}$ &
$\frac{2}{3}e$ & (-3,-2) & ${\cal{D}}^{3/2}_{-\frac{3}{2}
-\frac{1}{2}}$ & $-k\left(-\frac{3}{2}\right)$ &
$-k\left(-\frac{1}{2}\right)$ & $2k$ \\
\end{tabular}
\end{center}
\end{table}
\begin{center}
{\bf Table 1.}
\end{center}

\no In this table $Q_w$ and $Q_r$ are given by (2.9) and 
(2.10), and we have adopted a particular relative order of
the four trefoils with respect to the four families of fermions.
For this order we find
\begin{eqnarray}
Q_w &=& et_3 \\
Q_r &=& et_0 \\
Q_w + Q_r &=& Q_e
\end{eqnarray}
\underline{if and only if $k=e/3$}.  These relations are in
agreement with the following independent equation of standard theory:
\be
Q_e = e(t_3+t_0)
\ee
If one aligns the trefoils and the families in any other relative
order, one needs more than one value of $k$.  In this respect
the correspondence between the two sets is unique. 

The correspondence between the quantum knots and the isospin and
charge of the elementary fermions may be summarized by the
following relations, which may also be read directly from Table 1:
\be
\left.
\begin{array}{l}
t~=\frac{N}{6} \\ t_3=-\frac{w}{6} \\ t_0=-\frac{r+1}{6} \\
Q_e=-\frac{e}{6}~(w+r+1) 
\end{array} \right. \qquad \mbox{or}  \qquad \left.
\begin{array}{l}
t~=\frac{j}{3} \\ t_3=-\frac{m}{3} \\ t_0=-\frac{m^\prime}{3} \\
Q_e=-\frac{e}{3}~(m+m^\prime)
\end{array} \right.
\ee
Note also that
\be
Q_e=-\frac{e}{N}\left(\frac{w+r+1}{2}\right) \quad \mbox{and}
\quad Q_e = -e\left(\frac{m+m^\prime}{2j}\right)
\ee
holds for all the elementary fermions.

While $t_3$ and $t_0$ are initially defined in the standard
theory with respect to $SU(2)\times U(1)$, here they label the
gauge transformations on the knot algebra, and are also
described by $(w,r)$ and $(m,m^\prime)$ as shown in Table 1 and
Eq. (2.15).  In the limit of the standard theory, where
$q=1$, $t_3$ and $t_0$ assume their usual meaning in
$SU(2)$ and $U(1)$ respectively.

The states labelled by the quantum numbers $(j,m,m^\prime)$ or
$(t,t_3,t_0)$ are the multinomials lying in the algebra (2.4) and
given by (2.1).  These multinomials are associated with the knot
$(N,w,r)$ and, like the Jones (Laurent) polynomial, label the
knot.

These conclusions may be summarized by assigning ${\cal{D}}^{3t}_{-3t_3-3t_0}$ to the fermion families with $(t,t_3,t_0)$.
The members of each family are described by the quantum states
${\cal{D}}^{3t}_{-3t_3-3t_0}|n\rangle$ where $|n\rangle$ are the
states defined by the knot algebra.$^3$

\no {\it Remark:}  Although the ${\cal{D}}^{3/2}_{\frac{w}{2}
\frac{r+1}{2}}$ representation permits a unified description
of the electroweak properties of the four families, it does 
\underline{not} also imply that they transform 
under a 4-dimensional
representation of $SL_q(2)$.  Rather Eq. (2.8) is the only
formal property of ${\cal{D}}^{N/2}_{\frac{w}{2}\frac{r+1}{2}}
(a,b,c,d)$ that has been invoked.  The only new invariance 
beyond the standard theory that
has been introduced is invariance under the global gauge
transformations of the knot algebra that are expressed by (2.5)
and (2.6).

\ve

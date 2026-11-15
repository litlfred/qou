---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE"
section_id: sec-002-12-algebraic-k-groups-and-associated-units
section_title: "Algebraic K-groups and associated units"
section_number: 1.2
pages: 4-6
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.982
doc_brief: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn ="
---
\label{sub.intro.Ktheory} 

A second main theme of the paper concerns the relation to the algebraic 
$K$-theory of fields. The group $B(F)$ was introduced by Bloch as a concrete 
model for the abstract \hbox{$K$-group} $K_3(F)$. It was proved by 
Suslin~\cite{Suslintwo} that, if $F$ is a number field, then 
(up to \hbox{2-torsion}) $K_3(F)$ is an extension of~$B(F)$ by the roots 
of unity in~$F$, and in this case one also knows by results of
Borel and Suslin--Merkurjev~\cite{SuslinTorsion}, \cite{Suslin}, \cite{Weibel} 
that $K_3(F)$ has the structure
\be
\label{K3F} 
K_3(F) \;\cong\; \Z^{r_2(F)}\;\oplus\quad 
\begin{cases} \Z/w_2(F)\Z & \text{if $r_1(F)=0$,}
\\ \Z/2w_2(F)\Z \,\oplus\,(\Z/2\Z)^{r_1(F)-1}& \text{if $r_1(F)\ge1$,}
\end{cases}
\ee
where $(r_1(F),r_2(F))$ is the signature of $F$ and $w_2(F)$ is the integer
\be 
\label{eq.w2F} 
w_2(F) \=  2\,\prod_pp^{\nu_p}\,,\qquad  
\nu_p \,:=\:\max\bigl\{\nu\in\Z\mid\z_{p^\nu}+\z_{p^\nu}\i\in F\bigr\}\,. 
\ee
For a detailed introduction to the algebraic $K$-theory of number 
fields, see~\cite{Weibel}.

Theorem~\ref{thm.R} is then a companion of the following result \changed{
expressed in terms of $K_3(F)$ rather than the Bloch group $B(F)$}:

\begin{theorem}
\label{thm.c}
Let $F$ be a number field. Then there is a canonical map 
\be
\label{eq.cmap}  
c_\z:\, K_3(F)/\nn K_3(F)\map 
\bigl(\OL_{S,\nn}^{\times}/\OL_{S,\nn}^{\times \nn}\bigr)^{\chi\i}
\;\subset\;\bigl(F_\nn^{\times}/F_\nn^{\times \nn}\bigr)^{\chi\i}
\ee
defined using the theory of Chern classes
for some finite set~$S$ of primes depending only on~$F$. If $\nn$ is prime 
to a certain integer $M_F$ depending on~$F$, then the map \changed{$c_\z$} is
injective and its image is contained 
in~$\bigl(\OL_\nn^{\times}/\OL_\nn^{\times \nn}\bigr)^{\chi\i}$, and equal to this 
if~$\nn$ is prime.














\end{theorem}

We note that the proof of Theorem~~\ref{thm.R} relies upon the precise 
computation of~$K_3(F)$ and the properties of~$c_{\z}$ given above.
Finally, in view of the near isomorphism between~$B(F)$ and $K_3(F)$, one 
might guess that the two maps $P_\z$ and $c_\z$ are the same, at least up to 
a simple scalar.


This is the content of our next theorem. 

\begin{theorem}
\label{thm.cR}
For $\nn$ prime to~$M_F$, the map $R_\z$ equals $c_\z^\gamma$ for some 
$\gamma\in(\Z/\nn\Z)^{\times}$.
\end{theorem}
The constant~$\gamma$ does not depend on the underlying field;
both our construction and the Chern class map are well behaved in finite 
extensions, so we can compare the maps over any two fields with
the maps in their compositum. 
We conjecture that the constant~$\gamma$ is, up to sign, a power 
of~$2$ that is independent of \frankchanged{both~$F$} and~$\nn$. \frankchanged{More
optimistically, one might
further guess that~$\gamma$ is exactly~$2$.}
To \frankchanged{motivate} our conjecture,
and to determine~$\gamma$, it suffices 
to compute the image under both maps~$R_\z$ and $c_\z$ of some element of 
$K_3(F)/\nn K_3(F)$ of exact 
order~$\nn$. For each root of unity~$\z$ of order~$\nn$, there is a specific 
element~$\eta_{\z}$ (eq.~\eqref{eq.etaz})
of the finite Bloch group~$B(\Q(\z+\z\i))$ that is of 
exact order~$\nn$. Using the relation of the map $R_\z$ to the radial 
asymptotics of certain $q$-series called Nahm sums discussed in 
Section~\ref{sec.nahm}, we will prove
\be
\label{CompRz}
R_\z(\eta_\z) \= \z^2
\ee
(Theorem~\ref{thm.eta}). On the other hand, certain expected functorial 
properties of the map $c_\z$, discussed in Section~\ref{subsection:speculative} 
indicate that up to sign and a small power of~$2$, we have:
\be
\label{Compcz}
c_\z(\eta_\z) \overset{?} 
\= \z\,,
\ee
and in combination with~\eqref{CompRz} this justifies our conjecture
concerning $\gamma$.

The above-mentioned relation between our \emph{mod~$n$ regulator map} 
on Bloch groups and the asymptotics of Nahm sums near roots of unity is also 
an ingredient of our proof of Nahm's conjecture (under some 
restrictions) relating the modularity of his sums to torsion in the Bloch 
group.  The argument, described in Section~\ref{sub.nahmconj}, uses the full 
strength of Theorem~\ref{thm.R} and gives a nice demonstration of the 
usefulness, despite its somewhat abstract statement, of that theorem.

Theorem \ref{thm.R} \changed{also}
motivates a mod~$\nn$ (or \emph{\'etale}) version of the 
Bloch group of a number field~$F$, defined by
\be
\label{BFn}
B(F;\Z/\nn\Z) \= A(F;\Z/\nn\Z)/(\nn Z(F)+ C(F))\,,
\ee
where $A(F;\Z/\nn\Z)$ is the kernel of the map 
$d:Z(F)\to\wedge^2(F^\times/F^{\times\,\nn})$ induced by~$d$. This  is studied 
in Section~\ref{sec.K2F}, where we establish the following relation 
to~$K_2(F)$.

\begin{theorem}
\label{thm.K2}
The \'etale Bloch group is related to the original Bloch group by an exact 
sequence
\be
\label{Skype}
0 \map B(F)/\nn B(F) \map B(F;\Z/\nn \Z) \map K_2(F)[\nn] \map 0 \,,
\ee

where $K_2(F)[\nn]$ is the $\nn$-torsion in the $K$-group $K_2(F)$.
\end{theorem}

There is a corresponding exact sequence (Equation~\eqref{eq:kshort})
with~$B(F)/\nn B(F)$ \changed{and $B(F;\Z/\nn \Z)$ replaced by Galois
cohomology groups, and these sequences coincide for~$\nn = p^m$
prime to the number~$w_F$ of roots of unity of~$F$.}





\smallskip
A large part of the story that we have told here for the Bloch group 
$B(F)$ and the third $K$-group $K_3(F)$ can be generalized to higher Bloch 
groups $B_m(F)$ and $K_{2m-1}(F)$ with~$m\ge2$, and here the \'etale version 
really comes into its own, because the higher Bloch groups as originally 
introduced in~\cite{Za:texel} have several alternative definitions that 
are only conjecturally isomorphic and are difficult or impossible to compute 
rigorously, whereas their \'etale versions turn out to have a canonical 
definition and be \changed{more} amenable to \changed{numerical} computations.  The study of the 
higher cases has many \changed{points} in common with the $m=2$ case studied here, 
but there are also many new aspects, and the discussion will therefore be 
\changed{left to a future time}.




\subsection{Nahm's Conjecture}
\label{sub.intro.nahm}

The \changed{$S$}-unit constructed in Section~\ref{sub.intro.bloch} 
also appears in connection with the asymptotics near roots of unity
of certain $q$-hypergeometric series called Nahm sums. These series are 
defined by
$$
f_{A,B,C}(q) \=
\sum_{m\in\Z_{\ge0}^r} \frac{q^{\frac12 m^tAm + Bm+C}}{(q)_{m_1}\cdots(q)_{m_r}} \,,
$$
\changed{where~$(q)_r=\prod_{k=1}^r(1-q^k)$ is the quantum $r$-factorial},
$A \in M_r(\Q)$ is a positive definite symmetric matrix, $B$ 
an element of $\Q^r$, and~$C$ a rational number. Based on ideas coming from
characters of rational conformal field theories, Nahm conjectured a relation
between the modularity of the associated holomorphic function 
$\tf_{A,B,C}(\tau)=f_{A,B,C}(e^{2\pi i\tau})$ in the complex upper half-plane 
and the vanishing of a certain element or elements in the Bloch group 
of~$\Qbar$.
(See \cite{Nahm},~\cite{Zagier}, and Section~\ref{sec.nahm} for more details.)
This relation conjecturally goes in both directions, but with the implication
from the vanishing of the Bloch elements to the modularity of certain Nahm
sums not yet having a sufficiently precise formulation to be studied. 
The conjectural implication from modularity to vanishing of Bloch elements, 
on the other hand, had a completely precise formulation, as follows. Let~$A$ 
be as above and $(X_1,\dots,X_r)$ the unique solution in~$(0,1)^r$ 
of {\it Nahm's equation}
$$
1 \m X_i \=  \prod_{j=1}^r X_j^{a_{ij}} \qquad (i=1,\dots,r) \,.
$$
Then Nahm shows that the element $\xi_A=\sum_{i=1}^r [X_i]$ belongs to
$B(\BR\cap\Qbar)$, and his assertion is the following theorem, which we will
prove as a consequence of the injectivity statement in Theorem~\ref{thm.R}.

\begin{theorem}[Nahm's Conjecture]
\label{thm.half.nahm}
If the function $\tf_{A,B,C}(\tau)$ is modular for some $A$, $B$ and $C$ as 
above, then $\xi_A$ vanishes in the Bloch group of $\Qbar$.
\end{theorem}

We remark that the vanishing condition can be (and often is) stated by 
saying that $\xi_A$ is a torsion element in the Bloch group of the smallest 
real (but in general not totally real) number field containing all the~$X_i$, 
but when we take the image of this Bloch group in the Bloch group 
of~$\Qbar$ or~$\BC$, then the torsion vanishes,
\changed{because~$B(\Qbar)$ and~$B(\BC)$ are
  
  uniquely divisible~\cite[Theorem~6.3]{Suslinclosed} and so in
  particular are torsion free.}

\changed{

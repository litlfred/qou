---
doc_id: arxiv-math-0607416v6
doc_title: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES"
section_id: sec-007-33-closed-circular-domains-and-their-boundaries
section_title: "Closed Circular Domains and Their Boundaries"
section_number: 3.3
pages: 17-20
source_pdf: 0607416v6.pdf
source_sha256: 0705075947ce4a3d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.948
doc_brief: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES — We characterize all linear operators on ﬁnite or inﬁnite-dimensio- nal polynomial spaces that preserve the property of having"
---
\label{ss33}

Recall Definitions~\ref{def1} and~\ref{def-circ}, Notation~\ref{not-sets} and 
the linear operators
$\phi_n$ introduced in Notation~\ref{not-fi}. In particular, an $H$-stable 
polynomial in the sense of Definition~\ref{def-circ} is precisely a stable
polynomial in the sense of Definition~\ref{def1}.

\begin{lemma}\label{save}
Let $T : \CC_n[z] \rightarrow \CC_m[z]$ be a linear operator and suppose $m$ 
is minimal, i.e., $m= \max\{\deg T(f): f \in \CC_n[z]\}$. Let further 
$C=\Phi^{-1}(H)$ be an open circular domain, where $\Phi$ is a M\"obius 
transformation as in \eqref{mobius}, and let 
$S : \CC_n[z] \rightarrow \CC_m[z]$  be the linear operator defined by 
$S= \phi^{-1}_m T \phi_n$. 
The following are equivalent: 
\begin{itemize}
\item[(i)] $T(f)$ is $C$-stable or zero whenever $f$ is of degree $n$ and 
$C$-stable, 
\item[(ii)] $S(f)$ is $H$-stable or zero whenever $f$ is of degree $n$ and 
$H$-stable,  
\item[(iii)] $S(f)$ is $H$-stable or zero whenever $f$ is of degree at most 
$n$ and $H$-stable.  
\end{itemize}
The following are also equivalent: 
\begin{itemize}
\item[(iv)] $T(f)$ is $\partial C$-stable or zero whenever $f$ is of degree 
$n$ and $\partial C$-stable, 
\item[(v)] $S(f)$ is $\RR$-stable or zero whenever $f$ is of degree $n$ and 
$\RR$-stable,  
\item[(vi)] $S(f)$ is $\RR$-stable or zero whenever $f$ is of degree at most 
$n$ and $\RR$-stable. 
\end{itemize}
\end{lemma}

\begin{proof}
Note first that the equivalences (ii)$\Leftrightarrow$ (iii) and 
(v)$\Leftrightarrow$ (vi) are simple consequences of the density argument 
used in \S \ref{ss22}. Let us now show that (i) $\Leftrightarrow$ (ii). 
This  is obvious if $C$ is an open half-plane, i.e., if $c=0$ 
(cf.~\eqref{assum}). Therefore we assume that $c \neq 0$ and 
that the boundary of $C$ is a circle. If $C$ is an open disk then $a/c$ is in 
the open lower half-plane, so that $-cz+a$ is $H$-stable. Moreover, 
$-d/c\in\partial C$ and thus $cz+d$ is $C$-stable. Hence $f$ is $H$-stable 
if and only if $\phi_n(f)$ is $C$-stable so the assertion follows in this 
case as well. 

It remains to prove that (i) $\Leftrightarrow$ (ii) in the case when $C$ is 
the open complement  of a (closed) disk, which we proceed to do. 

\medskip

(i) $\Rightarrow$ (ii). Clearly, we may assume that $T$ is not the trivial 
(identically zero) operator. 
Let $p(z)=\sum_{k=0}^na_kz^k$ be an $H$-stable polynomial of degree $n$ and 
suppose first that $\sum_{k=0}^na_ka^kc^{n-k}\neq 0$. Then $\phi_n(p)$ is a 
$C$-stable polynomial of degree   
$n$ so that by assumption $T(\phi_n(p))$ is $C$-stable or zero. If 
$S(p) \neq 0$ it follows that 
that we can express $S(p)$ uniquely as 
$S(p) = (-cz+a)^{r(p)}S_0(p)$,  
where $S_0(p)$ is $H$-stable and $r(p)$ is a non-negative integer. By a 
continuity argument and an application of Hurwitz' theorem we have that a 
factorization as above holds for any $H$-stable polynomial of degree $n$.
 Since the set of $H$-stable polynomials  
of degree $n$ is dense in $\pi_n(H')\cup \{0\}$ -- that is, the set of 
$H$-stable polynomials of degree at most $n$ union the zero 
polynomial -- we deduce that such a 
factorization holds for the image under $S$ of any $H$-stable polynomial $p$ 
of degree at most $n$, namely 
$$S(p) = (-cz+a)^{r(p)}S_0(p),$$   
where $S_0(p)$ is $H$-stable or zero and $r(p)$ is a non-negative integer.

Fix a basis $\{p_j(z)\}_{j=0}^n$ of  $\CC_n[z]$ consisting of 
{\em strictly $H$-stable} (that is, $\overline{H}$-stable) polynomials of 
degree $n$. We distinguish two cases:

Suppose first that $S(f) \neq 0$ for all strictly $H$-stable polynomials $f$ 
of degree $n$. Since the topological space of strictly stable polynomials of 
degree $n$ is (path-) connected we  have by Hurwitz' theorem that $r(f)$ is 
constant on the set  of strictly $H$-stable polynomials of degree $n$. 
Thus, by the minimality assumption on $m$ and the fact that $\phi_n$ is 
invertible we must 
have $\deg(T(\phi_n(p_k)))=m$ for some $k$. It follows that $r(p_k)=0$ hence
$S(f)=S_0(f)$ for any strictly $H$-stable polynomial $f$ of degree $n$. 
Using again a standard density argument and Hurwitz' theorem we deduce that 
$S$ preserves ($H$-)stability up to degree $n$. 

Suppose now that  $S(f) = 0$ for some strictly $H$-stable polynomial $f$ of 
degree $n$ and let $g \in \CC_n[z]$. Clearly, $f + \epsilon g$ is strictly 
$H$-stable for all $\epsilon>0$ small enough. By the above we have that 
$$
S(g)=\epsilon^{-1}S(f+\epsilon g)= (-cz+a)^{r(g)}S_0(g),
$$
where $S_0(g)$ is $H$-stable or zero. It follows that $V:=S(\CC_n[z])$ is a 
$\CC$-linear space such that every non-zero polynomial in $V$ is a 
$(-cz+a)^r$-multiple of an $H$-stable polynomial. We know that $r(p_k)=0$ 
for the strictly $H$-stable polynomial $p_k$ above. Assume that 
$h \in \CC_n[z]$ is such that $r(h)\neq 0$. Since $r(p_k)=0$ and 
$$
S(h) + \delta S(p_k)=S(h+\delta p_k)
=(-cz+a)^{r(h+\delta p_k)}S_0(h+\delta p_k)\in V,
$$ 
where $S_0(h+\delta p_k)$ is $H$-stable or zero, we conclude that 
$S(h) + \delta S(p_k)$ is $H$-stable or zero for all $\delta \neq 0$. 
Letting $\delta \rightarrow 0$ we have by Hurwitz' theorem that either 
$S(h)=0$ or $S(h)$ is $H$-stable. However, this contradicts the fact that 
$a/c\in H$ and $S(h)(a/c)=0$, which follows from the assumption that 
$r(h)\neq 0$. Hence all non-zero polynomials in $V$ are $H$-stable and thus 
we deduce that $S$ 
preserves ($H$-)stability up to degree $n$ in this case as well. 

\medskip

(ii) $\Rightarrow$ (i). Since the set of $H$-stable polynomials of degree $n$ 
is dense in the set of $H$-stable polynomials of degree at most $n$ it 
follows that $S$ preserves $H$-stability on the latter set 
(i.e., $S$ preserves $H$-stability up to degree $n$). Let $f$ be a 
$C$-stable polynomial of degree $n$. Then $\phi_n^{-1}(f)$ is $H$-stable. 
Hence so is $S(\phi_n^{-1}(f))$ and thus 
$T(f)=\phi_m\big(S(\phi_n^{-1}(f))\big)$ is a $C$-stable polynomial (note 
that $-d/c\in\partial C$). 

\medskip

The equivalence (iv) $\Leftrightarrow$ (v) follows just as above by 
replacing ``strictly $H$-stable'' with ``strictly hyperbolic'', that is, 
real- and simple-rooted. 
\end{proof}

\begin{notation}\label{not-fifi}
Given a polynomial $f \in \CC[z,w]$ 
of degree at most $m$ in $z$ and at most $n$ in $w$ and a M\"obius 
transformation $\Phi$ as in \eqref{mobius} we let 
$$\phi_{m,z}(f)(z,w)= (cz+d)^mf(\Phi(z),w),\quad 
\phi_{n,w}(f)(z,w)= (cw+d)^nf(z,\Phi(w)).$$
\end{notation}

\begin{lemma}\label{fifi} 
Let $f(z,w) \in \CC[z,w]$ be of degree at most  $m$ in $z$ and at most $n$ in 
$w$ and let $\Phi : C \rightarrow H$ be a M\"obius transformation  as 
in \eqref{mobius}. If either
\begin{itemize}
\item[(a)] $C$ is not the exterior of a disk, or 
\item[(b)] $C$ is the exterior of a disk and 
\begin{itemize} 
\item[(b1)] the degree in $z$ of $\phi_{m,z}(f)(z,w)$ is $m$, and 
\item[(b2)] the degree in $w$ of $\phi_{n,w} \phi_{m,z}(f)(z,w)$ is $n$, 
\end{itemize} 
\end{itemize}
then $f$ is $H$-stable if and only if $\phi_{n,w}\phi_{m,z}(f)$ is $C$-stable.
\end{lemma}

\begin{proof}
The equivalence is clear when $C$ is a disk or a half-plane since in these 
cases $-cz+a$ is $H$-stable and $cz+d$ is $C$-stable (cf.~\eqref{assum}). 
Hence we may assume that $C$ is the exterior of a disk. Note that if $g(z)$ 
is a polynomial of degree $k$ then $a/c$ is not a zero of 
$\phi_k^{-1}(g)(z)$. In particular, if  $g(z)$ is a $C$-stable polynomial of 
degree $k$ then $\phi_k^{-1}(g)(z)$ is an $H$-stable polynomial of 
degree $k$.  Now since $-d/c \in \partial C$ we have that 
$cz+d$ is $C$-stable and therefore $\phi_{n,w} \phi_{m,z}(f)$ is $C$-stable 
if $f$ is $H$-stable, which proves one of the implications. 

Conversely, suppose that 
$G(z,w):=\phi_{n,w} \phi_{m,z}(f)(z,w)= \sum_{k=0}^nQ_k(z)w^k$ 
is $C$-stable. Then so is 
$\lambda^{-n}G(z,\zeta +\lambda(w-\zeta))$ whenever $\lambda \geq 1$, where 
$\zeta$ is the center of 
$C'$. Letting $\lambda \rightarrow \infty$ we see by Hurwitz' theorem that 
$(w-\zeta)^nQ_n(z)$ is $C$-stable. Hence, so is $Q_n(z)$. For every 
$z_0 \in C$ the degree of $G(z_0,w)$ is $n$, from which it follows that 
$\phi^{-1}_{n,w}(G)(z,w)=\phi_{m,z}(f)(z,w) \neq 0$ whenever 
$z \in C$, $w \in H$. Similarly, 
if $\phi_{m,z}(f)(z,w)= \sum_{k=0}^m P_k(w)z^k$ then $P_m(w)$ is $H$-stable 
so that 
$\phi_{m,z}(f)(z,w_0)$ has degree $m$ for every $w_0 \in H$. We conclude that 
$f(z,w)=\phi^{-1}_{m,z}\phi^{-1}_{n,w}(G)(z,w)$ is $H$-stable, as claimed.
\end{proof}

The following lemma is a simple consequence of Hurwitz' theorem since 
boundedness prevents zeros from escaping to infinity. 

\begin{lemma}\label{m}
Let $\Omega_1$ be a path-connected subset of $\CC$ and let $\Omega_2$ be a 
bounded subset of $\CC$. If $T : \CC_n[z] \rightarrow \CC[z]$ is a linear 
operator 
such that 
$T : \pi_n(\Omega_1)\setminus \pi_{n-1}(\Omega_1) \rightarrow \pi(\Omega_2)$ 
then 
all polynomials in the image of  
$\pi_n(\Omega_1)\setminus \pi_{n-1}(\Omega_1)$ have the same degree. 
\end{lemma}

Note that in the hypothesis of Lemma~\ref{m} we do not allow the identically 
zero polynomial to be in the image of 
$\pi_n(\Omega_1)\setminus \pi_{n-1}(\Omega_1)$. 

\begin{proof}[Proof of Theorem~\ref{circularregion}]
Suppose that $T : \CC_n[z] \rightarrow \CC_m[z]$, where as before $m$ is  
minimal in the sense that $m = \max\{\deg T(f): f \in \CC_n[z]\}$. By 
combining Lemma~\ref{save} with Hurwitz' theorem we see that 
$T : \pi_n(C')\setminus \pi_{n-1}(C') \rightarrow \pi(C')\cup\{0\}$ if 
and only if 
$\phi^{-1}_mT\phi_n : \pi_n(H') \rightarrow \pi(H')\cup\{0\}$.  
The case  $\dim_{\bC} T(\CC_n[z]) \leq1$ is clear. 
If $\dim_{\bC} T(\CC_n[z]) >1$ then by Theorem \ref{finitestab} we 
have $\phi_m^{-1}T\phi_n : \pi_n(H') \rightarrow \pi(H')\cup\{0\}$ if and only 
if $f(z,w):=\phi^{-1}_{m}T\phi_n\left[(z+w)^n\right]$ is $H$-stable. 
Now the polynomial in (b) of Theorem~\ref{circularregion} is precisely 
$\phi_{n,w} \phi_{m,z}(f)$. Moreover, by Lemma~\ref{fifi} (a) we may assume 
that $C$ is the exterior of a disk. Therefore, in order to complete the 
proof it only remains to show that conditions (b1) and (b2) of 
Lemma~\ref{fifi} are satisfied. 

If there were two different  $\overline{C}$-stable polynomials of degree 
$n$ that were mapped by $T$ on polynomials of different degrees then by 
Lemma~\ref{m} there would be a  $\overline{C}$-stable polynomial $g$ of 
degree $n$ in the kernel of $T$. However, since $\phi^{-1}_n(g)$ is 
strictly $H$-stable it would then 
follow from Lemmas \ref{degenerate} and \ref{spaces} 
that $\phi_m^{-1}T\phi_n$ and hence also $T$ has range of dimension at most 
one, which is not the case. We infer that  $\deg T(h)=m$ for any 
$\overline{C}$-stable polynomial $h$ of degree $n$.

Clearly, $\phi_{m,z}(f)(z,w)=T[\phi_{n,z}\big((z+w)^n \big)]$. Let 
$w_0 \in H\setminus\{-a/c\}$.  The only zero of the degree $n$ polynomial  
$$p_{w_0}(z):=\phi_{n,z}\big( (z+w_0)^n \big)=\big( (a+w_0c)z+b+w_0d\big)^n$$ 
is $\Phi^{-1}(-w_0)\in \overline{C}'$, so $p_{w_0}(z)$ 
 is $\overline{C}$-stable. By the previous paragraph we then have
$$\deg(\phi_{m,z}(f)(z,w_0))= \deg (T[p_{w_0}(z)])=m,$$ 
which verifies condition (b1) of Lemma~\ref{fifi}. 

Note next that coefficient of $w^n$ in the polynomial defined in (b) 
of Theorem~\ref{circularregion} is $T[(2acz+bc+ad)^n]$. 
We claim that the polynomial $(2acz+bc+ad)^n$ is $\overline{C}$-stable and 
of degree $n$. Since the image of any $\overline{C}$-stable polynomial of 
degree $n$ is of degree $m$ this would verify condition (b2) of 
Lemma~\ref{fifi}. To prove the claim note first that since $C$ is the 
exterior of a disk we have that $ac\neq 0$ so $\deg(2acz+bc+ad)^n=n$. Let 
$\zeta=-b/a$ and $\eta= -d/c$. Since $\Phi(\zeta)=0$ and 
$\Phi(\eta)=\infty$ we have that $\zeta, \eta \in \partial C$, which 
implies -- again by the assumption that $C$ is the exterior of a 
disk --  that the zero of $(2acz+bc+ad)^n$
$$
-\frac {bc+ad}{2ac} = \frac {\zeta + \eta}{2}, 
$$
is in $\overline{C}'$. Thus $(2acz+bc+ad)^n$ is $\overline{C}$-stable and 
of degree $n$, as required.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{circle}]
Let $m = \max\{\deg T(f): f \in \CC_n[z]\}$. By Lemma~\ref{save} we have 
that  $T : \pi_n(\partial C) \rightarrow \pi(\partial C)\cup\{0\}$ if and 
only if 
$\phi_m^{-1}T\phi_n : \pi_n(\RR) \rightarrow \pi(\RR)\cup\{0\}$. Using this 
and Theorem~\ref{finitehypC} it is not difficult to verify the theorem in the 
case $\dim_{\bC} T(\CC_n[z]) \leq 2$. Let 
$f(z,w)=\phi_m^{-1}T\phi_n [(z+ w)^n]$. To settle the remaining cases note 
first that by Theorem~\ref{finitehypC} (c) and (d) we have that 
$T : \pi_n(\partial C) \rightarrow \pi(\partial C)\cup\{0\}$ if and only if  
$f(z,w)$ or $f(z,-w)$ is a complex multiple of a real stable polynomial.  
Now the condition  that $f(z,w)$ is a complex multiple of a real stable 
polynomial is equivalent to saying that $f(z,w)$ is both 
$H$-stable and $H^r$-stable, see \cite[Proposition 3]{BBS} 
(note that $H^r=-H$). By Theorem~\ref{circularregion} we know that 
$f(z,w)$ is $H$-stable if and only if the polynomial in (c) of 
Theorem~\ref{circle}, that is, $\phi_{n,w} \phi_{m,z}(f)(z,w)$, is 
$C$-stable. On the other hand, since 
$-cz+a$ is $H^r$-stable and $cz+d$ is $C^r$-stable (since $C^r$ is not the 
exterior of a disk) we also have that $f(z,w)$ is $H^r$-stable if and only if 
$\phi_{n,w} \phi_{m,z}(f)$ is $C^r$-stable. The proof of 
the fact that condition (d) in Theorem~\ref{circle} is equivalent to saying 
that $f(z,-w)$ is a complex multiple of a real stable polynomial follows in 
similar fashion. This completes the proof of the theorem.    
\end{proof}

Corollary~\ref{alg-circularregion} and Corollary~\ref{cor-circle} are 
immediate consequences of Theorem~\ref{circularregion} and 
Theorem~\ref{circle}, respectively.

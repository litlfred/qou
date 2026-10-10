---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INV ARIANTS"
section_id: sec-016-4-laplace-transform-andrews-identity-and-frobeni
section_title: "Laplace transform, Andrews identity and Frobenius maps"
section_number: 4
pages: 15-16
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
text_source: latex
latex_prose_ratio: 0.652
latex_coverage_ratio: 0.959
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariant s."
---
\label{map-frob}
The aim of this section is to define the Laplace transform
 and to study its image.



\subsection{Laplace transform}
To define the unified invariant we have to compute
$${\sum_n}^\xi q^{b\frac{n^2-1}{4}} A(n,k)$$
where  terms depending on $n$ in $A(n,k)$ look as follows
$$\prod^k_{i=0} (q^n+q^{-n}-q^i-q^{-i})\,=(-1)^{k+1}\;(q^n;q)_{k+1}\;
(q^{-n};q)_{k+1}\, .$$
Formally, the last expression can be considered as a Laurent polynomial
in $q$ and $q^{n}$. Hence we only have to compute
$${\sum_n}^\xi q^{b\frac{n^2-1}{4}} q^{na}\; ,$$
which can be easily done by the square completing argument.
Let us state the result.

Suppose $r$ is an odd number,  $b$ is positive integer and
$$ c:= (r,b), \quad b_1:= b/c, \quad r_1:=r/c.$$
\newcommand{\Tor}{{\rm Tor}}
\begin{lemma}{\rm [Beliakova--Le]}
\label{33}
One has
\begin{equation}
 \gamma_b(\xi) = c \,\gamma_{b_1}(\xi^c). \label{02}
 \end{equation}
\begin{equation}{\sum_{n}}^\xi q^{b \frac{n^2-1}{4}}\, q^{an} = \begin{cases}
0
&\text{if $c\, \nmid \, a$;}\\
 (\xi^c)^{-a_1^2 b_1^*}\; \gamma_b(\xi)  & \text{if $a=ca_1$},
 \end{cases}
 \end{equation}
where $b_1^\ast$ is an integer satisfying $b_1 b_1^* \equiv 1 \pmod{r_1}$.
\end{lemma}


This computation inspired us to introduce the following operator,
called the Laplace transform. Remember that $\int e^{ax^k} f(x)\, dx$
is called the Laplace transform
of $f$ of order $k$.

Let $\cL_{b,c;n}: \BZ[q^{\pm n},q^{\pm 1}] \to \BZ[q^{\pm  c/b}]$ be
the $\BZ[q^{\pm 1}]$--linear operator, called the (discrete)
Laplace transform (of the second order),
defined by
\be\label{four}
\cL_{b,c;n}(q^{na}) := \begin{cases}
0
&\text{if $c\, \nmid\,  a$;}\\
q^{-a^2/b}   & \text{if $a=ca_1$},
 \end{cases}
\ee
\begin{lemma} {\rm [Beliakova--Le]}
Suppose  $f \in \BZ[q^{\pm n},q^{\pm 1}]$. Then
$$ {\sum_{n}}^\xi q^{b\frac{n^2-1}{4}}  f = \gamma_b(\xi) \,
\ev_\xi(\cL_{b,c;n}(f)).
$$
\label{1000}
\end{lemma}




The point is that $\cL_{b,c;n}(f)$, unlike the left hand side
${\sum_{n}^\xi}  q^{b\frac{n^2-1}{4}} f$, does not depend on $\xi$.
To prove Theorem \ref{0078} we need  to show that
$\cL_{b,c;n} ((q^{n};q)_{k+1}\; (q^{-n};q)_{k+1})$ is divisible by
$(q^{k+1};q)_{k+1}$.
 For  this we use the remarkable identity
discovered by Andrews.


\subsection{Andrews identity}
To warm up
we start with the  identity from the Ramanujan ``Lost'' Notebook:
$$\prod_{k\geq 1}\frac{1}{(1-q^{5k-4})(1-q^{5k-1})}=\sum_{n\geq 0}
\frac{q^{n^2}}{(1-q)(1-q^2)\dots (1-q^n)} $$


Only in the
60s, MacMahon gave a combinatorial interpretation of this identity
as follows.
Let $\lambda=(\lambda_1, \lambda_2, \dots, \lambda_t)$ with
$\sum_i\lambda_i=n$ be a partition of $n$ into non--increasing integers.
Then the identity can derived from the fact that
the number of partitions of $n$ with all $\lambda_i$ of the
 form $5k+1$ or $5k+4$
is equal to the number of partitions where $\lambda_{i}-\lambda_{i+1}\geq 2$
for all $i$.

 This identity is a very special
case of the Andrews identity we used  in \cite{BBL}: For any numbers $b_i,c_i,
i=1,\dots,k$ and positive integer $N$ we have
\begin{multline*}  1+ \sum_{n =1}^N  q^{kn+Nn} (1+ q^n)  \frac{(q^{-N})_n}{(q^{N+1})_n} \prod_{i=1}^k
\frac{(b_i)_{n}}{b_i^{n}} \frac{(c_i)_{n}}{c_i^{n}}
\frac{1}{(\frac{q}{b_i})_n (\frac{q}{c_i})_n}=
\\
\frac{(q)_N\,  (\frac{q}{b_kc_k})_N}{(\frac{q}{b_k})_N\,
(\frac{q}{c_k})_N} \sum_{n_k \ge n_{k-1} \ge \dots \ge n_2 \ge n_1=0}
 \frac{q^{n_k} (q^{-N})_{n_k} (b_k)_{n_k}
(c_k)_{n_k}}{(q^{-N}b_kc_k)_{n_k}}\prod_{i=1}^{k-1}\frac{q^{n_i}
\frac{(b_i)_{n_i}}{b_i^{n_i}} \frac{(c_i)_{n_i}}{c_i^{n_i}}
(\frac{q}{b_i c_i})_{n_{i+1}-n_i} }{(q)_{n_{i+1}-n_i}
(\frac{q}{b_i})_{n_{i+1}}  (\frac{q}{c_i})_{n_{i+1}}} \label{1002}
\end{multline*}
where $(a)_n=(a;q)_n$.

The point is that (for a special choice of parameters)
the left hand side of the identity
 can be identified with
$\cL_{b,c;n}\left((q^{n};q)_{k+1}\; (q^{-n};q)_{k+1}\right)$, where
 the right hand side is a sum with all summands
divisible by $(q^{k+1};q)_{k+1}$.



In the case $b=\pm 1$, the computations are especially simple and we get
that
$$\cL_{-1,1;n}((q^{n};q)_{k+1}\; (q^{-n};q)_{k+1})=2(q^{k+1};q)_{k+1}\, .$$
The same holds also for $\cL_{1,1;n}$ up to units.
This allows to write the explicit formula for $I_M$ given in the introduction.

\subsection{Frobenius isomorphism}
It remains to
show that the image of the
Laplace transform
belongs to $\R_b$, i.e. that
certain roots of $q$ exist in $\R_b$.


In \cite{BBL} we proved the following.


\begin{Thm}\label{frob}{\rm [Beliakova--B\"uhler--Le]}
The Frobenius endomorphism
 $F_b: \Z[1/b][q]^{\N_b} \to \Z[1/b][q]^{\N_b}$, sending $q$ to $q^b$,
 is an isomorphism.
\end{Thm}


This implies the
existence of the $b$th root of $q$ in $\calS_{b,0}$
defined by
\[
q^{1/b}:=F^{-1}_b (q)  \in \calS_{b,0}\,.
\]



Let us mention that this result does not hold over $\Q$, i.e.
for  $y \in\Q^{\N_b}$ with $y^b=1$ we have $y=\pm 1$.

Further, we introduce
another Frobenius homomorphism
$$G_m : R[q]^{\N_b} \to R[q]^{m\N_b} \quad \text{ by } \qquad G_m(q) = q^m.$$
Since $\Phi_{mr}(q)$ always divides $\Phi_{r}(q^m)$,  $G_m$ is well--defined.

This map allows us to transfer $q^{1/b}$ from $\calS_{p,0}$
to $\calS_{p,i}$ with $i> 0$, and hence to define a
realization of $q^{a^2/b}$ in $\calS_p$ with the correct evaluation.


\subsection{Integrality}
The proof of integrality of the SO(3) WRT invariants for
all  roots of unity and for all 3--manifolds is given in \cite{BL}.
Note that even restricted to rational homology 3--spheres,
this fact requires a separate proof, since
 the existence
of $I_M \in \R_b$ does not imply  integrality of the WRT invariants,
unless $b= 1$. In this subsection
we define a subring $\Gamma_b \subset \R_b$, such that
for any $f\in \Gamma_b$, $\ev_\xi(f)\in \Z[\xi]$.


The fact that $I_{M,1}$ belongs
to this subring was proved in \cite{BL}. We conjecture that
this holds in general.

For any divisor $c$ of $b$, let us decompose
$\N=\cup_{c|b}\; c\; \N_{b/c}$. Then
$$\Z[1/b][q]^\N=\prod_{c|b} \Z[1/b][q]^{c\,\N_{b/c}}\, .$$
Analogously, we have
$\Gamma_b=\prod_{c|b} \Gamma_{b,c}$, where
$\Gamma_{b,c} \subset \Z[1/b][q]^{c\, \N_{b/c}}$ is defined as follows.

Let $A_{b,c}=\Z[e_c][q^{\pm 1}, q^{\pm c/b}]$.
Put $t=q^{c/b}$ and let $A^{(m)}_{b,c}$ be the algebra generated over  $A_{b,c}$
by
$$\frac{(t;t)_m}{(q^c;q^c)_{m}}\;
 \frac{(e_c;e_c)_{(c-1)/2}}{\widetilde {(q;q)_m}}\; $$
where $$\widetilde{(q;q)_m}=\prod^m_{i=1, c\, \nmid\,  i}(1-q^i)\, .$$
Then
every element $f\in \Gamma_{b,c}$ has a presentation
$$f=\sum^\infty_{m=0} f_m \; \frac{(q^{m+1};q)_{m+1}}{1-q}
$$
with $f_m\in A^{(m)}_{b,c}$.
For any root of unity $\xi$ of odd order $r$ with $(r,b)=c$
and $f\in \Gamma_{b,c}$, we have
$$ \ev_\xi (f)= \ev_\xi \left(\sum^{(r-3)/2}_{m=0} f_m \frac{(q^{m+1};q)_{m+1}}{1-q}
\right)\; .$$








Observe that for $m<(r-1)/2$,
$$
\ev_\xi (\widetilde {(q;q)_{m}}) \; \mid\;
(e_c;e_c)_{(c-1)/2}
\;\;\text{and}\;\;
\ev_\xi \left(\frac{(t;t)_m}{(q^c;q^c)_{m}}
\right) \in \Z[\xi]\, .$$



\begin{conjecture}
For any $M\in \M_b$,
there exists an invariant $I'_M \in \Gamma_b$, such that
for any root of unity $\xi$ of odd order
$\ev_\xi(I'_M)=\tau_M(\xi)$.
\end{conjecture}

We also expect that $\Gamma_{b,b}$ is determined by its Taylor
expansion at $e_b$.

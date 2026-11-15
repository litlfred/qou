---
doc_id: arxiv-math-0607416v6
doc_title: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES"
section_id: sec-006-32-the-transcendental-characterization
section_title: "The Transcendental Characterization"
section_number: 3.2
pages: 14-17
source_pdf: 0607416v6.pdf
source_sha256: 0705075947ce4a3d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.916
latex_coverage_ratio: 0.957
doc_brief: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES — We characterize all linear operators on ﬁnite or inﬁnite-dimensio- nal polynomial spaces that preserve the property of having"
---
\label{ss32}

We will need the following lemma due to 
Sz\'asz, see \cite[Lemma 3]{szasz}. 
\begin{lemma}[Sz\'asz]\label{szasz} 
Let $m,n\in\bN$ with $m\le n$ and $f(z)=\sum_{k=m}^{n}c_kz^k\in\bC[z]$. If
$f(z)\in\HH_1(\CC)$ and $c_mc_n \neq 0$ then for any $r\ge 0$ one has  
$$
|f(z)| \leq |c_m|r^m\exp \left(r\frac{|c_{m+1}|}{|c_m|}
+3r^2\frac{|c_{m+1}|^2}{|c_m|^2}+3r^2\frac{|c_{m+2}|}{|c_m|}\right) 
$$
whenever $|z| \leq r$. 
\end{lemma} 

For $k,n \in \NN$ let $(n)_k = k!\binom n k = n(n-1)\cdots (n-k+1)$ if 
$k \leq n$ and $(n)_k =0$ if $n<k$ denote as usual the Pochhammer symbol.  

\begin{theorem}\label{genpol}
Let $F(z,w)=\sum_{k=0}^{\infty}P_k(z)w^k$ be a formal power series in $w$ 
with polynomial coefficients. Then $F(z,w) \in \HC_2(\CC)$ if and only if 
$\sum_{k=0}^n(n)_ k P_k(z) w^k \in \HH_2(\CC)\cup\{0\}$ for 
all $n \in \NN$. 
\end{theorem}

\begin{proof}
Suppose that  $F(z,w)=\sum_{k=0}^\infty P_{k}(z)w^k\in \HC_2(\CC)$ has 
polynomial coefficients. Given $n \in \NN$, the sequence $\{(n)_k\}_{k=0}^n$ 
is a 
multiplier sequence, and since it is non-negative it is a stability preserver 
by Theorem~\ref{trichotomy}.  By   
Corollary~\ref{cor-algstab} and Lemma~\ref{extension} we have that this 
multiplier extends 
to a map $\Lambda : \HH_2(\CC) \rightarrow \HH_2(\CC)\cup\{0\}$. Now, if  
$\tilde{F}_m(z,w) = \sum_{k=0}^{N_m}P_{m,k}(z)w^k$ is a sequence of
 polynomials in $\HH_2(\CC)$ converging to $F(z,w)$, uniformly on compacts, 
then 
$P_{m,k}(z) \rightarrow P_k(z)$ as $m \rightarrow \infty$  uniformly on 
compacts for fixed $k \in \NN$. But then  
$\Lambda[\tilde{F}_m(z,w)] \rightarrow \Lambda[F(z,w)]$ uniformly on 
compacts, which gives $\sum_{k=0}^n(n)_ k P_k(z) w^k \in \HH_2(\CC)\cup\{0\}$.

Conversely, suppose that 
$\sum_{k=0}^n(n)_ k P_k(z) w^k \in \HH_2(\CC)\cup\{0\}$ for all $n \in \NN$ 
and let 
$F_n(z,w) = \sum_{k=0}^n(n)_ k n^{-k}P_k(z) w^k$. 

\medskip

{\em Claim.} Given $r>0$ there is a constant $C_r$ such that 
$$
|F_n(z,w)| \leq C_r \mbox{ for } |z| \leq r, |w| \leq r 
\mbox{ and all } n \in \NN. 
$$

This claim proves the theorem since $\{ F_n(z,w) \}_{n=0}^\infty$ is then a 
normal family whose 
convergent subsequences converge to $F(z,w)$ (by the fact that 
$n^{-k}(n)_k\rightarrow 1$ for all $k \in \NN$ as $n \rightarrow \infty$). 

We first prove the Claim in the special case 
when $P_k(z) \in \RR[z]$ for all $k\in \NN$ and $P_K(z)$ is a non-zero 
constant, where $K$ is the first index 
for which $P_K(z) \neq 0$. 

\medskip

{\em Proof of the Claim in the special case.} Let $|P_K(z)|=A$, 
$B_r =\max\{ |P_{K+1}(z)| : |z|\leq r\}$ and 
$D_r =\max\{ |P_{K+2}(z)| : |z|\leq r\}$. Then, 
if we fix $\zeta \in \CC$ with $\Im(\zeta)>0$, we have that 
$F_n(\zeta, w) \in \HH_1(\CC) \cup\{0\}$ and by Lemma \ref{szasz} 
\begin{equation}\label{uppskatta}
|F_n(\zeta,w)| \leq  
Ar^K\exp\!\left(r\frac{B_r}{A}+3r^2\frac{B_r^2}{A^2}+3r^2\frac{D_r}{A}\right)  
\end{equation}
whenever $\Im(\zeta)>0$, $|\zeta| \leq r$ and $|w| \leq r$. If 
$\zeta \in \CC$ is fixed with  $\Im(\zeta)<0$ then $F_n(\zeta,-w) 
\in \HH_1(\CC)$ (since 
$F_n(z,w)$ has real coefficients and 
$\overline{F_n(z,w)}=F_n(\overline{z}, \overline{w})$).  
By Lemma \ref{szasz} this means that \eqref{uppskatta} holds also 
for $\Im(\zeta)<0$ and by continuity also for $\zeta \in \RR$, which proves 
the Claim. 

Next we assume that $\deg(P_K(z)) =d \geq 1$. An application of 
Theorem \ref{finitestab} verifies that $T = d/dz$ preserves stability, and 
by Lemma \ref{extension} $T= \partial/\partial z$ preserves stability in two 
variables. Hence 
$\frac{\partial F_n(z,w)}{\partial z} \in \HH_2(\RR)\cup\{0\}$ if 
$F_n(z,w) \in \HH_2(\RR)\cup\{0\}$. To deal with this case it is therefore 
enough to prove that if 
$\left|\frac{\partial F_n(z,w)}{\partial z}\right| \leq C_r$ for 
$|z| \leq r, |w| \leq r$ and all $n \in \NN$ then there 
is a constant $D_r$ such that $|F_n(z,w)| \leq D_r$ for 
$|z| \leq r, |w| \leq r$ and all $n \in \NN$. 
Clearly, $F_n(0,w) \in \HH_1(\RR) \cup \{0\}$ for all $n\in \NN$. 
Moreover, if $m$ is the first index 
such that $P_m(0) \neq 0$ then for $n \geq m$ we have 
$$
F_n(0,w)=
(n)_mn^{-m}P_m(0)w^m +(n)_{m+1}n^{-m-1}P_{m+1}(0)w^{m+1}+\ldots\in \HH_1(\RR),
$$
which by Lemma \ref{szasz} gives  
$$
|F_n(0,w)| \leq  |P_m(0)|r^m\exp \left(r\frac{|P_{m+1}(0)|}{|P_{m}(0)|}
+3r^2\frac{|P_{m+1}(0)|^2}{|P_{m}(0)|^2}
+3r^2\frac{|P_{m+2}(0)|}{|P_{m}(0)|}\right) =: E_r
$$
for $|z| \leq r$. Here we have used that $(n)_kn^{-k} \leq 1$ and 
$(n)_{k+1}n^{-k-1}/(n)_kn^{-k} \leq 1$  for $0 \leq k \leq n$. 
Suppose that 
$$
\left|\frac{\partial F_n(z,w)}{\partial z}\right| \leq C_r
$$
for $n \in \NN$ and $|z|\leq r$, $|w|\leq r$. Then, 
$$
F_n(z,w) = F_n(0,w)+ z\int_0^1 \frac{\partial F_n}{\partial z}(zt,w) dt,
$$
so 
$$
|F_n(z,w)| \leq E_r + rC_r \ \  \mbox{ for } |z| \leq r, 
|w| \leq r \mbox{ and all } n \in \NN. 
$$ 


Next we prove the above Claim in the general case. For this we need a 
property of multivariate stable polynomials that was established in 
\cite[Corollary 1]{BBS}: 

\medskip

{\em Fact.} If $h =g+if \in \HH_n(\CC)$ then $f,g \in \HH_n(\RR)$. 

\medskip

Now this means that if we let $P_k(z)= R_k(z)+i I_k(z)$ then we may write 
$$F_n(z,w) = F^{\Re}_n(z,w) + iF^{\Im}_n(z,w)$$ 
with $F^{\Re}_n(z,w), F^{\Im}_n(z,w) \in \HH_2(\RR)\cup\{0\}$, where 
$F^{\Re}_n(z,w), F^{\Im}_n(z,w)$ are given by 
$$F^{\Re}_n(z,w) = \sum_{k=0}^n(n)_ k n^{-k}R_k(z) w^k,\quad 
F^{\Im}_n(z,w) = \sum_{k=0}^n(n)_ k n^{-k}I_k(z) w^k.$$ 
By the above there are constants $A_r$ and $B_r$ such that 
$$|F^{\Re}_n(z,w)| \leq A_r\text{ and }|F^{\Im}_n(z,w)| \leq B_r
\text{ for }|z| \leq r, |w| \leq r\text{ and all }n \in \NN.$$ 
Hence  $|F_n(z,w)| \leq \sqrt{ A_r^2+B_r^2}$ 
for $|z| \leq r, |w| \leq r$ and all $n \in \NN$, which proves the Claim in 
the general case.
\end{proof}

We can now prove the transcendental characterizations of hyperbolicity and 
stability preservers, respectively. 

\begin{proof}[Proof of Theorems \ref{tranR} and \ref{tranC}]
We only prove Theorem~\ref{tranC} since the proof of Theorem~\ref{tranR} is 
almost identical. 
Theorem~\ref{tranC} follows quite easily from 
Theorem~\ref{genpol} and Corollary~\ref{cor-algstab}. Indeed, note that 
$T[(1-zw)^n] \in \HH_2(\CC)$ if and only if 
$T[(z+w)^n] \in \HH_2(\CC)$. Since
$$
T[(1-zw)^n] = \sum_{k=0}^n (n)_k \frac{(-1)^kT(z^k)}{k!} w^k 
$$
for all $n\in\bN$ we deduce the desired conclusion by comparing the above 
expression with the modified symbol $G_T(z,w)$ introduced in 
Notation~\ref{not2}.
\end{proof}

Finally, we show how P\'olya-Schur's algebraic and transcendental 
characterizations of multiplier sequences (Theorem~\ref{ps}) 
follow from our results. 

\begin{proof}[Proof of Theorem \ref{ps}]
We may assume that  $\lambda(0)=1$. Statements (i)--(iv) are all true 
if $\dim_{\bR}T(\RR[z]) \leq 2$ since 
then $\lambda(j)=0$ for all $j \geq 2$. Hence we may assume that 
$\dim_{\bR}T(\RR[z]) >2$. 
Corollary \ref{cor-alghyp} implies that either 
$$
T[(1-zw)^n]=\sum_{k=0}^n(-1)^k\binom n k \lambda(k) (zw)^k  \in \HH_2(\RR)
$$
for all $n \in \NN$ or  
$$
T[(1+zw)^n]  = \sum_{k=0}^n \binom n k \lambda(k) (zw)^k \in \HH_2(\RR)
$$
for all $n \in \NN$. We claim that if  $f(z) \in \RR[z]$ then
$
f(zw) \in \HH_2(\RR) 
$
if and only if all the zeros of $f$ are real and non-negative. Suppose first 
that $f(zw)$ is real stable. Letting $z=w=t$ we see that 
$f(t^2)$ is hyperbolic, which can only happen if all the zeros of $f$ are 
non-negative (since $a+t^2$ is hyperbolic if and only if $a \leq 0$). On the 
other hand, if $f$ has only real non-positive zeros then $f(zw)$ factors as   
$f(zw)=C\prod_{j=0}^n(zw+\alpha_j),$
where $\alpha_j \in \RR$, $1 \leq j \leq n$. 
Now $zw+\alpha_j \in \HH_2(\RR)$ if and only if $\alpha_j \leq 0$. Hence (i) 
$\Leftrightarrow$ (iv) and by 
Theorem \ref{tranR} we also have (ii)  $\Leftrightarrow$ (iv). The 
equivalence of (ii) and (iii) is Laguerre's 
classical result. 
\end{proof}

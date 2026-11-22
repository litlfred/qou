---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-027-101-chevalley-and-kashiwara-operators
section_title: "Chevalley and Kashiwara operators"
section_number: 10.1
pages: 75-80
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.927
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
Let us recall the definition of several functors on modules over \KLRs \ which  are used to categorify $\Um_{\Z[q^\pm 1]}^\vee$.
\begin{definition} Let $\beta\in\rtl^+$.
\bnum
\item For $i \in I$ and $1 \le a \le |\beta|$, set
$$ e_a(i)=\sum_{\nu \in I^\beta,\nu_a=i}e(\nu)\in R(\beta).$$
\item We take conventions:
\begin{align*}
&E_iM=e_1(i)M, \allowdisplaybreaks\\
&E^*_iM=e_{|\beta|}(i)M,
\end{align*}
which are functors from $R(\beta) \gmod$ to $R(\beta-\al_i) \gmod$.
\item For a simple module $M$, we set
\begin{align*}
&\eps_i(M)=\max\set{n\in\Z_{\ge0}}{E_i^nM\not=0},\\
&\eps^*_i(M)=\max\set{n\in\Z_{\ge0}}{E_i^{*\;n}M\not=0},\\
& \widetilde{F}_iM = q_i^{\ve_i(M)} L(i) \hconv M, \allowdisplaybreaks\\
& \widetilde{F}^*_iM = q_i^{\ve^*_i(M)} M \hconv L(i), \allowdisplaybreaks\\
& \widetilde{E}_iM = q_i^{1-\ve_i(M)} \soc(E_iM) \simeq q_i^{\ve_i(M)-1} \hd(E_iM), \allowdisplaybreaks\\
& \tE^*_iM = q_i^{1-\ve^*_i(M)} \soc(E^*_iM) \simeq q_i^{\ve^*_i(M)-1}
\hd(E_i^*M),\\
&\tE_i^{\,\max} M=\tE_i^{\eps_i(M)}M\quad\text{and}\quad
\tE_i^{*\;\max} M=\tE_i^{*\;\eps^*_i(M)}M.
\end{align*}
\item For $i \in I$ and $n \in \Z_{\ge 0}$, we set
$$L(i^n)=q_i^{n(n-1)/2} \underbrace{L(i)\conv \cdots \conv L(i)}_n.$$
Here $L(i)$ denotes the $R(\al_i)$-module $R(\al_i)/R(\al_i)x_1$.
Then  $L(i^n)$ is a self-dual real simple  $R(n\alpha_i)$-module.
\ee
\end{definition}
 Note that, under the isomorphism in Theorem \ref{thm:categorification 1}, the functors $E_i$ and $E_i^*$ correspond to the linear operators $e_i$ and $e_i^*$  on
 $ \An_{\Z[q^{\pm 1}]} =  \iota(\Um_{\A}^\vee) \subset \An$, respectively.
Note also that,  for a simple $R(\beta)$-module $S$, we have
$\tE_i \tF_i S \simeq S$, and $\tF_i \tE_i S \simeq S$ if $\eps_i(M) >0$.



In the course of  proving the following propositions, we use the following notations.

\begin{align} \label{eq: overQ}
\overline{Q}_{i,j}(x_a,x_{a+1},x_{a+2}) \seteq
\dfrac{Q_{i,j}(x_a,x_{a+1})-Q_{i,j}(x_{a+2},x_{a+1})}{x_a-x_{a+2}}.
\end{align}
Then we have
$$\tau_{a+1}\tau_a\tau_{a+1}-\tau_{a}\tau_{a+1}\tau_{a}
=\sum_{i,j\in I}\overline{Q}_{i,j}(x_a,x_{a+1},x_{a+2})
e_a(i)e_{a+1}(j)e_{a+2}(i).$$
\begin{prop} \label{prop: La i}
Let $\beta \in \rl^+$ with $n=|\beta|$. Assume that an $R(\beta)$-module $M$ satisfies $E_iM=0$. Then the left $R(\al_i)$-module homomorphism $R(\alpha_i) \tens M \Lto
q^{(\alpha_i,\beta)}M \conv R(\alpha_i)$ given by
\begin{align} \label{eq: pre-form}
e(i) \tens u \longmapsto \tau_1 \cdots \tau_n(u \tens e(i))
\end{align}
extends uniquely to an $(R(\alpha_i+\beta),R(\alpha_i))$-bilinear homomorphism
\begin{align} \label{eq: ext-form}
R(\alpha_i) \conv M \Lto q^{(\alpha_i,\beta)}M \conv R(\alpha_i)
\end{align}
\end{prop}

\begin{proof} {\rm (i)} First note that, for $1 \le a \le n$,
\begin{equation} \label{eq: e_a(i) vanish}
\tau_1 \cdots \tau_{a-1}e_a(i)\tau_{a+1}\cdots\tau_n\big( u \tens e(i) \big) =
\tau_{a+1}\cdots\tau_n\big(e_1(i)\tau_1 \cdots \tau_{a-1}(u \tens e(i))  \big)=0
\end{equation}
since $E_iM =0$. \\
\noindent
{\rm (ii)} In order to see that \eqref{eq: ext-form} is a well-defined $R(\alpha_i+\beta)$-linear homomorphism, it is enough
to show that \eqref{eq: pre-form} is $R(\beta)$-linear. \\
\noindent
{\rm (a)} Commutation with $x_a\in R(\beta)$ $(1\le a \le n)$: We have
\begin{align*}
x_{a+1}\tau_1 \cdots \tau_n\big(u \tens e(i)\big) &=  \tau_1 \cdots \tau_{a-1}x_{a+1}\tau_{a} \cdots \tau_n\big(u \tens e(i)\big) \allowdisplaybreaks \\
 &=  \tau_1 \cdots \tau_{a-1}\big( \tau_{a} x_{a}+ e_a(i) \big) \tau_{a+1}\cdots \tau_n\big(u \tens e(i) \big) \allowdisplaybreaks \\
 &=  \tau_1 \cdots  \tau_n  x_{a}\big(u \tens e(i)\big)
\end{align*}
by \eqref{eq: e_a(i) vanish}.  \\
\noindent
{\rm (b)} Commutation with $\tau_a\in R(\beta)$ $(1\le a < n)$:
  We have
\begin{align*}
&\tau_{a+1}\tau_1 \cdots \tau_n\big(u \tens e(i)\big) \\
& \hspace{5ex} =  \tau_1 \cdots \tau_{a-1}(\tau_{a+1}\tau_{a}\tau_{a+1})\tau_{a+2} \cdots \tau_n\big(u \tens e(i)\big) \allowdisplaybreaks \\
& \hspace{5ex} =  \tau_1 \cdots \tau_{a-1}\big(\tau_{a}\tau_{a+1}\tau_{a}+\sum_{j}\overline{Q}_{i,j}(x_{a},x_{a+1},x_{a+2})e_a(i)e_{a+1}(j) \big)\tau_{a+2}\cdots \tau_n\big(u \tens e(i) \big) \allowdisplaybreaks \\
& \hspace{5ex} =  \tau_1 \cdots  \tau_n  \tau_{a}\big(u \tens e(i)\big) \allowdisplaybreaks \\
& \hspace{10ex} + \sum_{j}\tau_1 \cdots \tau_{a-1}\overline{Q}_{i,j}(x_{a},x_{a+1},x_{a+2})e_a(i)e_{a+1}(j)\tau_{a+2}\cdots \tau_n\big(u \tens e(i) \big).
\end{align*}
The last term vanishes because $E_iM=0$ implies
\begin{align*}
& \tau_1 \cdots \tau_{a-1}f(x_{a},x_{a+1})g(x_{a+2})e_a(i)\tau_{a+2}\cdots \tau_n\big(u \tens e(i) \big) \\
& \hspace{18ex} = g(x_{a+2})\tau_{a+2}\cdots \tau_n e_1(i)\tau_1 \cdots \tau_{a-1}f(x_{a},x_{a+1})\big(u \tens e(i) \big)=0
\end{align*}
for any polynomial $f(x_{a},x_{a+1})$ and $g(x_{a+2})$. \\
\noindent
{\rm (iii)} Now let us show that \eqref{eq: ext-form} is right $R(\alpha_i)$-linear. By \eqref{eq: e_a(i) vanish}, we have
\begin{align*}
 \tau_1 \cdots \tau_{a-1} x_a \tau_a \cdots \tau_{n}\big(u \tens e(i) \big) & =
\tau_1 \cdots \tau_{a-1} \big(\tau_a x_{a+1}-e_{a}(i) \big)\tau_{a+1}\cdots \tau_{n} \big(u \tens e(i) \big) \\
& = \tau_1 \cdots \tau_{a} x_{a+1} \tau_{a+1} \cdots \tau_{n}\big(u \tens e(i) \big)
\end{align*}
for $1 \le a \le n$. Therefore we have
$$ x_{1}\tau_1 \cdots \tau_n\big(u \tens e(i)\big) = \tau_1 \cdots \tau_n x_{n+1}\big(u \tens e(i)\big)=\tau_1 \cdots \tau_n \big(u \tens e(i)x_{1}\big). \qedhere$$
\end{proof}


 Recall that  for $m,n\in\Z_{\ge0}$,
we denote by $w[{m,n}]$ the element of $\sym_{m+n}$  defined by
\eq
&&w[{m,n}](k)=\begin{cases}k+n&\text{if $1\le k\le m$,}\\
k-m&\text{if $m<k\le m+n$}.\end{cases}
\eneq
Set $\tau_{w[{m,n}]}:=\tau_{i_1} \cdots \tau_{i_r}$, where $s_{i_1} \cdots s_{i_r}$ is a reduced expression
of $w[{m,n}]$.
Note that $\tau_{w[{m,n}]}$ does not depend on the choice of reduced expression (\cite[Corollary 1.4.3]{K^3}).

\begin{prop} Let $M \in R(\beta) \gmod$  and $N \in R(\gamma) \gmod$, and set $m=|\beta|$ and
$n=|\gamma|$. If $E_iM=0$ for any $i \in \supp(\gamma)$, then
\begin{align*}
v \tens u \longmapsto \tau_{w[m,n]}(u \tens v)
\end{align*}
gives a well-defined $R(\beta+\gamma)$-linear homomorphism $N \conv M \Lto q^{(\beta,\gamma)} M \conv N$.
\end{prop}

\begin{proof} The proceeding proposition implies that
$$ v \tens u \longmapsto \tau_{w[m,n]}(u \tens v) \quad \text{ for } u \in M, v \in R(\gamma)$$
gives a well-defined $R(\beta+\gamma)$-linear homomorphism $R(\gamma) \conv M \to M \conv R(\gamma)$. Hence
it is enough to show that it is right $R(\gamma)$-linear. Since we know that it commutes with
the right multiplication of $x_k$, it is enough to show that it commutes with the right
multiplication of $\tau_k$. For this, we may assume that $n = 2$ and $k = 1$. Set $\gamma = \alpha_i +\alpha_j$.

Thus we have reduced the problem to  the equality
\begin{align*}
\tau_1(\tau_2\tau_1)\cdots(\tau_{m+1}\tau_m)\big( u \tens e(i) \tens e(j) \big)
= (\tau_2\tau_1)\cdots(\tau_{m+1}\tau_m) \tau_{m+1}\big( u \tens e(i) \tens e(j) \big)
\end{align*}
for $u \in M$, which is a consequence of
\begin{equation*}
\begin{aligned}
& (\tau_2\tau_1)\cdots(\tau_{a}\tau_{a-1})\tau_a(\tau_{a+1}\tau_{a})\cdots(\tau_{m+1}\tau_m)\big( u \tens e(i) \tens e(j) \big) \allowdisplaybreaks \\
& \hs{5ex} = (\tau_2\tau_1)\cdots(\tau_{a+1}\tau_{a})
\tau_{a+1}(\tau_{a+2}\tau_{a+1})\cdots(\tau_{m+1}\tau_m)\big( u \tens e(i) \tens e(j) \big)
\end{aligned}
\end{equation*}
for $1 \le a \le m$. Note that
\begin{align*}
& \tau_a(\tau_{a+1}\tau_{a})\cdots(\tau_{m+1}\tau_m)\big( u \tens e(i) \tens e(j) \big) \allowdisplaybreaks \\
& \hspace{10ex} = \tau_a(\tau_{a+1}\tau_{a})e_{a+1}(i)e_{a+2}(j)(\tau_{a+2}\tau_{a+1})\cdots(\tau_{m+1}\tau_m)\big( u \tens e(i) \tens e(j) \big)
\end{align*}
and
\begin{align*}
& \tau_a(\tau_{a+1}\tau_{a})e_{a+1}(i)e_{a+2}(j) \allowdisplaybreaks \\
& \hspace{10ex} = (\tau_{a+1}\tau_{a})\tau_{a+1} e_{a+1}(i)e_{a+2}(j)-\overline{Q}_{ji}(x_{a},x_{a+1},x_{a+2})e_{a}(j)e_{a+1}(i)e_{a+2}(j).
\end{align*}
Hence it is enough to show
\begin{align*}
& (\tau_2\tau_1)\cdots(\tau_{a}\tau_{a-1})\overline{Q}_{j,i}(x_{a},x_{a+1},x_{a+2})
e_a(j)
\allowdisplaybreaks\\
& \hspace{20ex}(\tau_{a+2}\tau_{a+1})\cdots (\tau_{m+1}\tau_{m})\big( u \tens e(i) \tens e(j) \big)=0.
\end{align*}
This follows from
\begin{align*}
&(\tau_2\tau_1)\cdots(\tau_{a}\tau_{a-1})f(x_a)g(x_{a+1},x_{a+2}) e_a(j)
(\tau_{a+2}\tau_{a+1})\cdots(\tau_{m+1}\tau_m)
\big( u\tens e(i)\tens e(j)\big)\allowdisplaybreaks\\
& \hspace{10ex}=(\tau_2\cdots\tau_a)
(\tau_1\cdots\tau_{a-1})f(x_a)g(x_{a+1},x_{a+2}) e_a(j) \allowdisplaybreaks\\
&\hspace{35ex}(\tau_{a+2}\tau_{a+1})\cdots(\tau_{m+1}\tau_m)
\big( u\tens e(i)\tens e(j)\big)\allowdisplaybreaks\\
&\hspace{10ex}=(\tau_2\cdots\tau_a)
g(x_{a+1},x_{a+2})(\tau_{a+2}\tau_{a+1})\cdots(\tau_{m+1}\tau_m)\allowdisplaybreaks\\
&\hspace{35ex}
e_1(j)(\tau_1\cdots\tau_{a-1})f(x_a)\big( u\tens e(i)\tens e(j)\big)\allowdisplaybreaks\\
&\hspace{10ex}=0
\end{align*}
for $1 \le a \le m$ and $f(x_a) \in \ko[x_{a}]$, $g(x_{a+1},x_{a+2}) \in \ko[x_{a+1},x_{a+2}]$.
\end{proof}

Let $P(i^n)$ be a projective cover of
$L(i^n)$.
 Define  the functor
$$E_i^{(n)} : R(\beta) \Mod \to R(\beta - n \alpha_i) \Mod$$
 by
$$E_i^{(n)}(M) := P(i^n)^\psi \tens_{R(n\al_i)}E_i^nM, $$
where
$P(i^n)^\psi $ denotes the right $R(n\al_i)$-module obtained from the left
$R(\beta)$-module $P(i^n)$  via the anti-automorphism $\psi$.
 We define the functor $E_i^{*\,(n)}$ in a similar way.
 Note that $$E_i^n\simeq  [n]_i ! E_i^{(n)}.$$


\Cor Let $R$ be a symmetric \KLR.
Let $i\in I$ and $M$ a simple module.
Then we have
\eqn
&&\tLa\bl L(i),M\br=\eps_i(M),\\
&&\La\bl L(i),M\br=2\eps_i(M)+\lan h_i,\wt(M)\ran=\eps_i(M)+\vphi_i(M).\\
\eneqn
\encor
\Proof
Set $n=\eps_i(M)$ and $M_0=E_i^{(n)}(M)$.
Then the preceding proposition implies
$\La(L(i),M_0)=\bl \al_i,\wt(M_0)\br$.
Hence we have $\tLa(L(i),M_0)=0$, which implies
$$\tLa(L(i),M)=\tLa(L(i), L(i^n)\circ M_0)
=\tLa\bl L(i), L(i^n)\br+\tLa(L(i),M_0)=n.$$
\QED




\begin{prop}\label{prop: Econv} Let $M$, $N$ be modules
and $m,n \in \Z_{\ge 0}$.
\begin{enumerate}
\item[{\rm (i)}] If $E_i^{m+1}M=0$ and $E_i^{n+1}N=0$, then we have
\begin{align*} 
E_i^{(m+n)} (M \conv N) \simeq q^{mn+n \lan h_i, \wt(M) \ran}
 E_i^{(m)} M \conv  E_i^{(n)}N.
\end{align*}
\item[{\rm (ii)}] If $E_i^{*\,m+1}M=0$ and $E_i^{*\,n+1}N=0$, then we have
\begin{align*} 
E_i^{*\,(m+n)} (M \conv N) \simeq
q^{mn+m \lan h_i, \wt(N) \ran} E_i^{*\,(m)} M \conv E_i^{*\,(n)} N.
\end{align*}
\end{enumerate}
\end{prop}

\begin{proof}
 Our assertions follow from the shuffle lemma (\cite[Lemma 2.20]{KL09}).
\end{proof}

The following corollaries are  immediate consequences of Proposition~\ref{prop: Econv}.
\Cor\label{cor:Ereal} Let $i\in I$ and let $M$ be a real simple module.
Then $\tE_i^{\,\max}M$ is also real simple.
\encor

\Cor
Let $i\in I$ and let $M$ be a  simple module with $\eps_i(M)=m$ .
Then we have $\tE_i^{m} M \simeq E_i^{(m)} M$.
\encor


\begin{prop} \label{prop: acted on left only}
Let $M$ and $N$ be simple modules.
 We assume that one of them is real.
If $\ve_i(M \hconv N)=\ve_i(M)$,
then we have an isomorphism in $R\gmod$
$$ \widetilde{E}^{\,\max}_i (M \hconv N) \simeq (\widetilde{E}^{\,\max}_i M) \hconv N.$$
Similarly, if  $\ve^*_i(N \hconv M)=\ve^*_i(M)$, then we have
$$ \widetilde{E}^{*\max}_i (N \hconv M) \simeq (N \hconv \widetilde{E}^{*\max}_i M).$$
\end{prop}

\begin{proof}
Set $n=\ve_i(M \hconv N) = \ve_i(M)$ and $M_0=\widetilde{E}^{\,\max}_i M$.
Then $M_0$ or $N$ is real.
Now we have
$$ L(i^n) \otimes M_0 \otimes N \monoto
E_i^n(M\hconv N)\simeq L(i^n) \otimes \widetilde{E}^{\,\max}_i (M \hconv N),$$
which induces a non-zero map $M_0 \otimes N \to
\widetilde{E}^{\,\max}_i (M \hconv N)$. Hence we have a surjective map
$$M_0 \conv N \twoheadrightarrow \widetilde{E}^{\,\max}_i (M \hconv N).$$
Since $M_0$ or $N$ is real by Corollary~\ref{cor:Ereal}, $M_0\conv N$ has a simple head
and we obtain the desired result.  A similar proof works for the second statement.
\end{proof}

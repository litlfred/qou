---
doc_id: arxiv-2111.12409v4
doc_title: "On the generalisation of Roth’s theorem"
section_id: sec-006-4-roths-theorem-for-adelic-curves-a
section_title: "Roth's theorem for adelic curves (A)"
section_number: 4
pages: 13-17
source_pdf: 2111.12409v4.pdf
source_sha256: 3f0b94ee06fe79bf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.8
latex_coverage_ratio: 0.99
doc_brief: "On the generalisation of Roth’s theorem — We present two generalisations of Roth’s approximation theorem on proper adelic curves, assuming some technical conditions on the behavior of the logarithmic"
---
\label{mainsect}


\begin{defn}\label{st_muequi}
A proper adelic curve $\mathbb X=(\mathbb K,\Omega, \mu)$ satisfies the \emph{ strong $\mu$-equicontinity condition} if for any measurable set $S\subset\Omega$ of finite measure and any real number $\varepsilon>0$ there exists a finite measurable cover $C_1,\ldots, C_m$ of $S$ satisfying the following conditions: for all $\beta\in\mathbb K^\times$ there exists a measurable set $U_{\beta}\subset\Omega_\infty$ such that $\mu(U_\beta)=0$ and
\[
\left\vert-\log^-\vert\beta\vert_{\omega}+\log^-\vert\beta\vert_{\omega'} \right\vert<\varepsilon h(\beta)\,,\quad \forall \omega,\omega'\in C_j\setminus U_\beta\,,\; \forall j=1,\ldots, m
\]
\end{defn}


The following lemma is a simplified version of \cite[Lemma 8.10]{vo}. It can be seen as a generalisation of the Arzel\`a-Ascoli theorem for measure spaces, with the advantage that one doesn't need to provide a uniform bound for the involved family of functions.

\begin{lem}\label{unif_conv}
Let $\mathbb X=(\mathbb K,\Omega, \phi)$ be a proper adelic curve satisfying the strong $\mu$-equicontinuity condition. Fix $\alpha\in \mathbb K^\times$ and a measurable subset $S\subset\Omega$ of finite measure. Let $\{\beta_k\}$ be a sequence in $\mathbb K^\times$ such that $\beta_k\neq\alpha$,  and $h(\beta_k)\to+\infty$. Then for any $\varepsilon>0$  there exists a subsequence $\left\{\beta_{k_j}\right\}$  such that for any $j,\ell\in\mathbb N$  big enough  the following inequality holds  on $S\setminus U$, where $U\subset\Omega_{\infty}$ and $\mu(U)=0$:
\[
\left\vert-\frac{\log^-\vert\alpha-\beta_{k_j}\vert_{\omega}}{h(\beta_{k_j})}+\frac{\log^-\vert\alpha-\beta_{k_{\ell}}\vert_{\omega}}{h(\beta_{k_{\ell}})} \right\vert<\varepsilon 
\]
\end{lem}
\proof 
Put $h_0=\min_k h(\beta_k)$ and $\lambda_k(\omega)=-\log^-\vert \alpha-\beta_k\vert_\omega$. Fix $\varepsilon>0$ and let $C_1,\ldots, C_r$ be a finite measurable cover as in Definition \ref{st_muequi}. Clearly by possibly passing to a refinement we can assume that the cover is made of mutually disjoints sets. Let $k\in\mathbb N$; if $i\in\{1,\ldots, r\}$ is such that $\mu(C_i)=0$ we define $m_{k,i}=0$, otherwise if $i$ is such that $\mu(C_i)>0$ we put 
\[
m_{k,i}=\inf\left\{t\in\mathbb R\colon \mu\left(\left\{\omega\in C_i\colon \frac{\lambda_k(\omega)}{h(\beta_k)}\ge t\right\}\right)\le \frac{\mu(C_i)}{2}\right\}
\]
Notice that the sets:
\[
V_{k,i}=\{\omega\in C_i\colon \lambda_k(\omega) \le h(\beta_k) m_{k,i}\}\,,\quad  T_{k,i}=\{\omega\in C_i\colon \lambda_k(\omega) \ge h(\beta_k) m_{k,i}\}
\]
have both measure at least $\frac{\mu(C_i)}{2}$. Hence we get:
\begin{equation}\label{ee1}
\frac{\mu(C_i)}{2} h(\beta_k) m_{k,i}\le \int_{T_{k,i}} h(\beta_k) m_{k,i} d\mu \le \int_{T_{k,i}} \lambda_k d\mu\le\int_S \lambda_k d\mu
\end{equation}
But by Proposition \ref{properties}(6) we know that
\begin{equation}\label{ee2}
\int_S \lambda_k d\mu\le h(\beta_k)\left(\frac{\log 2}{h(\beta_k)}+\frac{h(\alpha)}{h(\beta_k)}+1\right)\le h(\beta_k)\left(\frac{\log 2}{h_0}+\frac{h(\alpha)}{h_0}+1\right)
\end{equation}
So by putting $c_i=\frac{2}{\mu(C_i)}\left(\frac{\log 2}{h_0}+\frac{h(\alpha)}{h_0}+1\right)$, equations  (\ref{ee1}) and (\ref{ee2}) show that $m_{k,i}\le c_i$. Note that the constant $c_i$ doesn't depend on $k$. It follows that all the vectors $\bm{m}_{k}=(m_{k,1},\ldots, m_{k,r})\in\mathbb R^r$,   lie in the hyper-parallelepiped $\prod^r_{i=1}[0,c_i]$. Now consider the small hyper-cubes $Q_k=\prod^r_{i=1}[m_{k,i}-\varepsilon,m_{k,i}+\varepsilon]$, clearly there exists an index $\overline{k}\in\mathbb N$ and a sequence  $\{k_j\}$ such that $\bm{m}_{k_j}\in Q_{\overline k}$ for any $j\in\mathbb N$. We now show that the subsequence $\{\beta_{k_j}\}$ has exactly the properties that we are searching for.

 Consider any two elements $\beta_{k_j}$ $\beta_{k_{\ell}}$ of the subsequence and  $\omega\in S\setminus( U_{\beta_{k_j}}\cup U_{\beta_{k_\ell}})$. Let $i$ be the unique index such that $\omega\in C_i$; pick $\omega'\in C_i
\setminus U_{\beta_{k_j}}$  and  $\omega''\in C_i
\setminus U_{\beta_{k_\ell}}$ such that:
\[
\lambda_{k_j}(\omega')\le m_{k_j,i} h(\beta_{k_j})\,,
\]
\[
\lambda_{k_\ell}(\omega'')\ge m_{k_\ell,i} h(\beta_{k_\ell})\,.
\]
Note that this is possible since $V_{k_j,i}$ and $T_{k_\ell,i}$ have positive measure.  In the following chain of inequalities we use twice  the strong $\mu$-equicontinuity condition (first for $\omega,\omega'$ and later for $\omega,\omega''$) and the fact that $|m_{k_j,i}-m_{k_\ell,i}|<2\varepsilon$.

\[
\frac{\lambda_{k_j}(\omega)}{h(\beta_{k_j})}< \frac{\lambda_{k_j}(\omega')}{h(\beta_{k_j})}+ \frac{h(\alpha-\beta_{k_j})}{h(\beta_{k_j})}\varepsilon<\!^{(\text{Pr. \!\!\ref{properties}(4)})}\frac{\lambda_{k_j}(\omega')}{h(\beta_{k_j})}+\left(1+\frac{\log 2+h(\alpha)}{h(\beta_{k_j})}\right)\varepsilon \le 
\]
\[
\le m_{k_j,i}+\left(1+\frac{\log 2+h(\alpha)}{h(\beta_{k_j})}\right)\varepsilon\le m_{k_\ell,i}+\left(3+\frac{\log 2+h(\alpha)}{h(\beta_{k_j})}\right)\varepsilon\le \frac{\lambda_{k_\ell}(\omega'')}{h(\beta_{k_\ell})}+\left(3+\frac{\log 2+h(\alpha)}{h(\beta_{k_j})}\right)\varepsilon< 
\]
\[
<\frac{\lambda_{k_\ell}(\omega)}{h(\beta_{k_\ell})}+\left(4+\frac{\log 2+h(\alpha)}{h(\beta_{k_j})}+\frac{\log 2+h(\alpha)}{h(\beta_{k_\ell})}\right)\varepsilon
\]
Since $h(\beta_k)\to +\infty$  for $j$ and $\ell$ big enough the above inequalities say:
\[
\frac{\lambda_{k_j}(\omega)}{h(\beta_{k_j})}< \frac{\lambda_{k_\ell}(\omega)}{h(\beta_{k_\ell})}+5\varepsilon
\]
By swapping the roles of $j$ and $\ell$ we obtain in the same way
\[
\frac{\lambda_{k_\ell}(\omega)}{h(\beta_{k_\ell})}< \frac{\lambda_{k_j}(\omega)}{h(\beta_{k_j})}+5\varepsilon
\]
 The claim finally follows by the arbitrariness of $\varepsilon$.
\endproof
 \begin{comment}
Remember that with $\overline{\mK}_{\omega}$ we denote the algebraic closure the completion $\mK_\omega$ (with respect to the absolute value $\vert\cdot\vert_{\omega}$). In this case $\vert\cdot\vert_{\omega}$  extends uniquely to an absolute value of $\overline{\mK}_{\omega}$ and by an abuse of notation we will continue to denote this extension with the symbol $\vert\cdot\vert_{\omega}$. Theorem \bref{thm:main}{A} will be equivalent to the following theorem:
\begin{thm}\label{smallroth}
Let $\mathbb X=(\mathbb K,\Omega, \phi)$ a proper adelic curve satisfying the $\mu$-equicontinuity condition. Fix some distinct elements $\alpha_1,\dots ,\alpha_n\in\mathbb K$. Let $S=S_1\sqcup S_2\sqcup\ldots\sqcup S_n$ be a measurable  subset of $\Omega$ with finite measure. Then for any $\varepsilon>0$ there exists a real constant $C>0$ (depending on the fixed data) such that for any $\beta\in \mathbb K$  with  $h_{\mathbb X}(\beta)>C$   
it holds that:
\[
\sum^n_{i=1}\int_{S_i}\log^-\vert \beta-\alpha_i\vert_\omega d\mu(\omega)>-(2+\varepsilon)h_\mathbb X(\beta)
\]
\end{thm}
Before proving this theorem, let's show its equivalence with  Theorem \bref{thm:main}{A}.
\begin{prop}
Theorem \ref{smallroth} is equivalent to Theorem \bref{thm:main}{A}.
\end{prop}
\proof
One direction is obvious, so we only have to show that  Theorem \ref{smallroth} implies Theorem \bref{thm:main}{A}. First of all we can assume that the set $\{\alpha_1,\ldots,\alpha_n\}$ is $\Gal({\overline{\mK}/\mK})$ invariant, since adding all conjugates to the set  of $\alpha_i's$ actually provides a stronger Roth inequality. Moreover put $\mK'=\mK(\alpha_1,\ldots\alpha_n)$ and construct the adelic curve $\mathbb X'=(\mK',\Omega',\mu')$, but note that $\mK'$ is now a finite Galois extension of $\mK$. For any index $i$, the embeddings $\iota_{\omega,i}$ can be then glued together to an embedding 
$\iota_\omega\colon\mK'\hookrightarrow \overline{\mK}_{\omega}$ so that:
$$
\sum^n_{i=1}\log^-\vert \iota_{\omega,i}(\beta-\alpha_i)\vert_\omega= \sum^n_{i=1}\log^-\vert \iota_{\omega}(\beta-\alpha_i)\vert_\omega
$$
Now fix $i_0\in\{1,\ldots,n\}$let $S'_{i_0}:= \pi^{-1}_{\mK'|\mK}(S_{i_0})$ and assume that Theorem \ref{smallroth} holds for the adelic curve $\mathbb X'$ and the set $S'$, then the following chain of equalities show that Theorem \bref{thm:main}{A} holds true. Notice that at a certain point we will use equation (\ref{extproper})  and the fact that, since $\mK'|\mK$ is finite and Galois, we have:
$N_{\mK'|\mK}(\beta-\alpha_{i_0})=\prod^n_{i=1}(\beta-\alpha_{i})$:
$$
\int_{S'_{i_0}} \log^-\vert \beta-\alpha_{i_0}\vert_\nu d\mu'(\nu)=^{\textrm{eq.}(\ref{extproper})}\frac{1}{[\mK':\mK]}\int_{S_{i_0}} \log^-\vert N_{\mK'|\mK}(\beta-\alpha_{i_0})\vert_\omega d\mu(\omega)=
$$
$$
=\frac{1}{[\mK':\mK]}\int_{S_{i_0}} \log^-\left\vert \prod^n_{i=1}(\beta-\alpha_{i})\right\vert_\omega d\mu(\omega)=\frac{1}{[\mK':\mK]}\int_{S_{i_0}} \left(\sum^n_{i=1}\log^-\vert (\iota_{\omega}(\beta-\alpha_{i})\vert_\omega\right) d\mu(\omega)\,.
$$

\endproof

\end{comment}

\textbf{Proof of theorem \bref{thm:main}{(A)}.}
When  $n \le 2$, from  Proposition \ref{properties}$(6)$ we deduce that  any approximant $\beta$ such that 
$$
h(\beta)>\frac{n\log 2+\sum^n_{i=1}h(\alpha_i)}{2-n+\varepsilon}
$$
satisfies the desired inequality.\\
 

 Assume $n\ge 3$. We consider the following matrix of dimension $n\times N$, where $N>21^2\log 2n$ will be a big enough fixed integer:
\[
T=\begin{pmatrix}
 \alpha_1& \alpha_1  &\ldots &\alpha_1 \\
 \alpha_2& \alpha_2  &\ldots &\alpha_2\\
\vdots & \vdots  & \vdots & \vdots\\
\alpha_n& \alpha_n  &\ldots &\alpha_n\\
\end{pmatrix}
\]
notice that we have repeated $N$ times the same column vector. Assume by contradiction that the theorem is false. Namely that there exists an $\varepsilon_0>0$ such that the inequality
\begin{equation}\label{negationroth}
\sum^n_{i=1}\int_{S_i}\log^-\vert \beta_k-\alpha_i\vert_\omega d\mu(\omega)\le-(2+\varepsilon_0)h_\mathbb X(\beta_k)
\end{equation}
is satisfied by  a sequence $\{\beta_k\}_{k\in\mathbb N}$ in $\mathbb K$ with the properties that $h(\beta_k)\to+\infty$. Pick a constant:
\[
L>  \log\left(4^{2N!}\prod^n_{i=1}H(\alpha_i)^{\frac{2N!}{n}}\right) 
\]
Since $h(\beta_k)\to+\infty$, by eventually passing to a subsequence,  we can assume that  $\{h(\beta_k)\}$ is increasing and bounded from below by a very  big value. Therefore we can assume
\begin{equation}\label{magg-eps}
\varepsilon_0>\frac{2L}{h(\beta_k)}+\frac{L+h(\beta_k)}{h(\beta_k)}\frac{8\sqrt{\log 2n}}{\sqrt N}\,,\quad \forall  k\in\mathbb N
\end{equation}
Choose  any $N$ elements from the sequence $\{\beta_{k}\}$, call them $\beta^{(1)},\ldots\beta^{(N)}$ and consider the following matrix $T(\bm\beta)$:
\[
T(\bm\beta)=\begin{pmatrix}
 \alpha_1& \alpha_1  &\ldots &\alpha_1 \\
 \alpha_2& \alpha_2  &\ldots &\alpha_2\\
\vdots & \vdots & \vdots & \vdots\\
\alpha_n& \alpha_n  &\ldots &\alpha_n\\
\beta^{(1)}& \beta^{(2)}  &\ldots &\beta^{(N)}
\end{pmatrix}
\]


We are ready to construct some functions  $\theta_k\in L^1(S,\mu)$ which will give the desired contradiction. We define them as  piecewise functions by putting for any $\omega\in  S_i$ and any $k\in\mathbb N$:
\[
\theta_k(\omega)=\frac{-\log^- \vert \beta_k-\alpha_i\vert_{\omega}}{L+h(\beta_k)}
\]
  Now we can write
\begin{equation}\label{magg-int}
\int_{S} \theta_k d\mu =\sum^n_{i=1}\int_{S_i} \theta_k d\mu=\frac{-1}{L+h(\beta_k)}\sum^n_{i=1}\int_{S_i}\log^- \vert \beta_k-\alpha_i\vert_{\omega} d\mu(\omega)\ge^{\!\!\textrm{eq.} (\ref{negationroth})}\frac{(2+\varepsilon_0)h(\beta_k)}{L+h(\beta_k)}
\end{equation}
By plugging inequality (\ref{magg-eps}) inside (\ref{magg-int}) and simplifying the expressions, we finally get:
\begin{equation}\label{magg-inte}
\int_{S}\theta_k d\mu >2+\frac{8\sqrt{\log 2n}}{\sqrt N} \qquad \forall k\in\mathbb N
\end{equation}
Thanks to Proposition \ref{properties}(6):
\[
\int_{S_i} \theta_k \le \frac{B_i+h(\beta_k)}{L+h(\beta_k)}
\]
for $B_i\in\mathbb R_{>0}$. So, if $B=\max_{i}\{B_i\}$ we obtain:
$$
\int_S\theta_k d\mu\le \frac{nB+nh(\beta_k)}{L+h(\beta_k)}\le n\,.
$$
Then after possibly passing to a subsequence of $\{\theta_k\}$, we can assume that $\int_{S}\theta_k d\mu$ admits limit and by inequality (\ref{magg-inte}):
\begin{equation}\label{key_in}
\lim_{k\to\infty }\int_{S}\theta_k d\mu\ge 2+\frac{8\sqrt{\log 2n}}{\sqrt N}>2+\frac{7\sqrt{\log 2n}}{\sqrt N}\,.
\end{equation}
Put by simplicity $\lambda_{i,k}(\omega):=-\log^- \vert \beta_k-\alpha_i\vert_{\omega}$ for $\omega\in S_i$, so 
$$\theta_k(\omega)=\frac{\lambda_{i,k}(\omega)}{L+h(\beta_k)}\,.$$
Then we have:
$$
\theta_k(\omega)=\frac{\lambda_{i,k}(\omega)}{h(\beta_k)}A_k
$$
where $A_k:=1-\frac{L}{L+h(\beta_k)}<1$ and $A_k\to 1$. By Lemma \ref{unif_conv} from $\left\{\frac{1}{A_k}\theta_k\right\}$ we can extract a subsequence  $\left\{\frac{1}{A_{k_j}}\theta_{k_j}\right\}$ uniformly convergent to a function $\theta$  on $S\setminus U$, where $\mu(U)=0$. We extend $\theta$ on the whole $S$ by putting $\theta_{|U}=0$. Since on a set of finite measure the uniform convergence implies the $L^1$-convergence, we can write:
\begin{equation}\label{final_contr}
    \begin{aligned}
\int_{S} \theta d\mu=\int_{S\setminus U} \theta d\mu=\lim_{j\to\infty}\int_{S\setminus U} \frac{1}{A_{k_j}}\theta_{k_j} d\mu=\lim_{j\to\infty}\int_{S} \frac{1}{A_{k_j}}\theta_{k_j} d\mu=\\
=\left(\lim_{j\to\infty}\frac{1}{A_{k_j}}\right)\left(\lim_{j\to\infty} \int_{S}\theta_{k_j} d\mu\right)> 2+\frac{7\sqrt{\log 2n}}{\sqrt N}\,.
\end{aligned}
\end{equation}
Consider a positive real number $C$ such that
\[
C\mu(S) < \int_S\theta d\mu - \left ( 2+ \frac{7\sqrt{\log 2n}}{\sqrt N} \right)
\]
and define the set
\[
T:=\{\omega\in S\colon \theta(\omega)< C\}\,.
\]
Note that $T$ contains the previously introduced $U$. We obtain the following chain of inequalities:
\[
\int_T \theta d\mu \le C\mu(T) \le C\mu(S) < \int_S\theta d\mu- \left ( 2+ \frac{7\sqrt{\log 2n}}{\sqrt N} \right)
\] 
which gives
\[
\int_{S\setminus T} \theta d\mu > 2+\frac{7\sqrt{\log 2n}}{\sqrt N}
\]
Now we define the function $\hat\theta: S\to \mathbb R_{\ge 0}$  such that
\begin{equation*}
\hat \theta(\omega)=\begin{cases}
\theta(\omega) & \text{if } \omega\in S\setminus T\\
0 & \text{otherwise}
\end{cases}
\end{equation*}
Clearly $\hat\theta(\omega)\ge C$ for any $\omega\in S\setminus T$ and moreover
\[
\int_{S} \hat\theta d\mu=\int_{S\setminus T} \theta d\mu > 2+\frac{7\sqrt{\log 2n}}{\sqrt N}\,.
\]
We can choose $\gamma\in\, ]0,1[$ such that
\begin{equation}\label{modification}
\int_{S}\gamma\hat\theta  d\mu > 2+\frac{7\sqrt{\log 2n}}{\sqrt N} \,.
\end{equation}
We want to show that  the function $\gamma\hat\theta$ satisfies  the hypotheses of Theorem \ref{teoremadue}. Choose $\delta\in\mathbb R_{>0}$ such that
\[
0<\delta<(1-\gamma)C
\]
so that for any $\omega\in S\setminus T $ we have
\[
\gamma\hat\theta(\omega) <\hat\theta(\omega)-\delta\,.
\]
Denote by $\{\theta_m\}$ the previously extracted subsequence that converges uniformly to $\theta$ on $S\setminus T$. We can find a positive integer $M$ such that if $m>M$ the following chain of inequalities holds for any $\omega\in S\setminus T$:
\begin{equation}\label{modification1}
0 < \gamma\hat\theta(\omega) < \hat\theta(\omega)-\delta<\theta_m(\omega)<\frac{-\log^{-}\vert\beta_{m}-\alpha_i\vert_\omega}{h(\beta_{m})+\log\left(4^{2N!}\prod^n_{i=1}H(\alpha_i)^{\frac{2N!}{n}}\right) }
\end{equation}
 We choose $\bm\beta:=(\beta^{(1)},\ldots,\beta^{(N)})$ in the set $\{\beta_m\}_{m>M}$ with the following properties:
\begin{itemize}
\item The elements $\beta^{(j)}$ are separated by big enough gaps, so that the matrix $T(\bm\beta)$ satisfies the $h$-gap condition.

\item  The elements $\beta^{(j)}$ are chosen in a way that $\vert \beta^{(j)}-\alpha_i\vert_\omega \le 1$ for any $i=1,\ldots, n$ and any $\omega\in S\setminus T$. Note that this is possible because we can iterate $n$-times Lemma \ref{unif_conv} starting with the sequence $\{\beta_m\}$ and extracting at each step $i=1,\ldots,n$ a sequence $\{\beta_j\}$ such that $\omega\mapsto\frac{-\log^-\vert\beta_j-\alpha_i\vert_\omega}{h(\beta_j)}$  converges uniformly almost everywhere to a function bounded from below by a positive number. In this way inequality (\ref{modification1}) ensures that $\gamma\hat\theta$ is column bounding.
\end{itemize}


\begin{comment}
Now we show that since   $h(\beta_k)\to+\infty$, the elements $\beta^{(1)},\ldots,\beta^{(N)}$ can be chosen, along the above subsequence $\left\{\beta_{m}\right\}$, where $m=k_j$, in a way that the following two conditions are satisfied.
\begin{itemize}
\item $T(\beta)$ satisfies the h-gap condition. This is obvious by choosing the $\beta^{(j)}$ separated by big enough gaps.
\item The function $\theta$ is column bounding for $T(\beta)$. In fact for $\varepsilon>0$ small enough  and  for infinitely many big enough indexes $m$, thanks to the choice of the constant $L$, we have the following inequalities for any $i=1,\ldots, n$ and any $\omega\in S_i$:
$$\theta(\omega)<\theta_{m}(\omega)+\varepsilon<\frac{-\log^{-}\vert\alpha_i-\beta_{m}\vert_\omega}{h(\beta_{m})+\log\left(4^{2N!}\prod^n_{i=1}H(\alpha_i)^{\frac{2N!}{n}}\right) }$$
\end{itemize}
\end{comment}
Finally we can apply Theorem \ref{teoremadue} for $\gamma\hat\theta$  to get:
$$
\int_{ S}\gamma \hat\theta d \mu<2+\frac{7\sqrt{\log 2n}}{\sqrt{N}}
$$
which  contradicts inequality (\ref{modification}).\hfill{$\square$}


\vspace{1ex}
Now we show that Theorem \ref{CorCorv} can be immediately recovered from Theorem \bref{thm:main}{(A)}.


\begin{prop}\label{im_cor}
    Theorem \bref{thm:main}{(A)} implies Theorem \ref{CorCorv}.
\end{prop}
\proof
Let $\mathbb K$  be the Galois closure of $k(\alpha_1,\ldots,\alpha_n)$ over $k$ and consider the adelic curve  $\mathbb X= (\mathbb K,\Omega, \mu)$  naturally lying over $(k,\mathcal V_k)$. The strong $\mu$-equicontinuity condition trivially holds on $\mathbb X$ since all singletons of $\Omega$ are measurable and $\inf_{\omega\in\Omega}\mu(\{\omega\})>0$. For any  $v_i$ of Theorem \ref{CorCorv} consider the set
\[
\widetilde S_i:=\{\omega\in\Omega \colon \text{$\omega$ extends $v_i$}\}=\{\omega_{ij}\colon j=1,\ldots, r(i)\}\quad \text{for $i=1,\ldots,n$}
\]
The set $\widetilde S_i$ are orbits under the action of $\Gal(\mathbb K/k)$ on $\Omega$. For each $i,j$ there is $\alpha_{ij}\in \mathbb K$ such that
\[
\vert \beta-\alpha_{ij}\vert_{\omega_{ij}}=\vert \beta-\alpha_{i}\vert_{v_i},\quad \forall\beta\in k
\]
Now we apply Theorem \bref{thm:main}{(A)} on the set $\widetilde S=\cup_\ell\widetilde S_\ell$ partitioned along the fibers of the map $\omega_{ij}\mapsto a_{ij}$. Hence we get the following inequality
\[
\sum_{i,j}\int_{\{\omega_{ij}\}}\log^-\vert \beta-\alpha_{ij}\vert_{\omega_{ij}} d\mu(\omega)>-(2+\varepsilon) h_{\mathbb X}(\beta).
\]
Note that the summation over $i$ and $j$ doesn't reflect the partition. But 
\[
\sum_{i,j}\int_{\{\omega_{ij}\}}\log^-\vert \beta-\alpha_{ij}\vert_{\omega_{ij}} d\mu(\omega)=\sum_{ij} \log^-\vert \beta-\alpha_{ij}\vert_{\omega_{ij}}\mu(\{\omega_{ij}\})=
\]

\[
=\sum_i\left(\log^-\vert \beta-\alpha_{i}\vert_{v_i}\sum_j\mu(\{\omega_{ij}\})\right)=\sum_i\log^-\vert \beta-\alpha_{i}\vert_{v_i}
\]
Where the last equality follows from \cite[Ch. II, Corollary 8.4]{Neu}:
\[
\sum^{r(i)}_{j=1}\mu(\{\omega_{ij}\})=\sum^{r(i)}_{j=1}\frac{[\mathbb K_{\omega_{ij}}\colon k_{v_i}]}{[\mathbb K\colon k]}=1\,.
\]
\endproof

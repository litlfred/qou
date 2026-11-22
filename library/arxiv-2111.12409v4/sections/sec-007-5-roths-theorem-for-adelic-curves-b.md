---
doc_id: arxiv-2111.12409v4
doc_title: "On the generalisation of Roth’s theorem"
section_id: sec-007-5-roths-theorem-for-adelic-curves-b
section_title: "Roth's theorem for adelic curves (B)"
section_number: 5
pages: 17-19
source_pdf: 2111.12409v4.pdf
source_sha256: 3f0b94ee06fe79bf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.822
latex_coverage_ratio: 0.994
doc_brief: "On the generalisation of Roth’s theorem — We present two generalisations of Roth’s approximation theorem on proper adelic curves, assuming some technical conditions on the behavior of the logarithmic"
---
\label{mainsect2}

We weaken Definition \ref{st_muequi} by requiring the ``equicontinuity property'' outside from sets of arbitrary small measure:
\begin{defn}\label{muequi}
A proper adelic curve $\mathbb X=(\mathbb K,\Omega, \mu)$ satisfies the \emph{$\mu$-equicontinuity condition} if for any measurable set $S\subset\Omega$ of finite measure and any real numbers $\varepsilon,\delta>0$ there exists a finite measurable cover $C_1,\ldots, C_m$ of $S$ satisfying the following conditions. For all $\beta\in\mathbb K^\times$ there exists a measurable set $U_\beta\subset\Omega_\infty$ such that $\mu(U_\beta)<\delta$ and
\[
\left\vert-\log^-\vert\beta\vert_{\omega}+\log^-\vert\beta\vert_{\omega'} \right\vert<\varepsilon h(\beta)\,,\quad \forall \omega,\omega'\in C_j\setminus U_\beta\,,\; \forall j=1,\ldots, m
\]
\end{defn}

In \cite[Proposition 8.9]{vo} it is shown that  arithmetic function fields satisfy the $\mu$-equicontinuity condition. 





\begin{defn}\label{un_int}
A proper adelic curve $\mathbb X=(\mathbb K,\Omega, \mu)$ satisfies the \emph{uniform integrability condition} if for  any $\varepsilon>0$ there exists $\delta>0$ such that if $T\subset\Omega_{\infty}$ is a measurable subset satisfying $\mu(T)<\delta$, then 
$$\int_T -\log^-|\beta|_\omega d\mu(\omega)<\varepsilon h_{\mathbb X}(\beta)\,,\quad \forall\beta\in\mathbb K^\times\,.$$
\end{defn}

Vojta shows that arithmetic function fields satisfy the uniform integrability condition in \cite[Lemma 8.8]{vo}.  The following lemma provides a key step in our proof:
\begin{lem}\label{vo8.12}
Let $\mathbb X=(\mathbb K,\Omega, \phi)$ be a proper adelic curve satisfying the $\mu$-equicontinuity condition  and the uniform integrability condition. Assume that Theorem \bref{thm:main}{(B)} doesn't hold for certain $S$, $\alpha_1,\ldots,\alpha_n\in\mathbb K$, $\varepsilon_0\in\mathbb R_{>0}$ and $c\in\mathbb R$. Let $N>0$ an integer, $\varepsilon\in\,]0,\varepsilon_0[$, and $r_0,r_1 >1$ two real numbers. Then there exist $\beta^{(1)},\ldots,\beta^{(N)}\in\mathbb K$ satisfying the following conditions:
\begin{itemize}
\item[$(1)$] $h(\beta^{(1)})>r_0$ 
\item[$(2)$] $\frac{h(\beta^{(k)})}{h(\beta^{(k-1)})}>r_1$ for any $k=2,\ldots, N$.
\item[$(3)$] There is a partition $S=S_1\sqcup\ldots\sqcup S_n$ such that:
$$\sum^n_{i=1}\int_{S_i}\, \min_{1\le k\le N}\left(\frac{-\log^-|\beta^{(k)}-\alpha_i|_\omega}{h(\beta^{(k)})}\right )d\mu(\omega)>2+\varepsilon$$
\end{itemize}
\end{lem}
\proof
The rather technical  proof can be found in \cite[Proposition 8.12]{vo} for arithmetic function fields, and it can be repeated line by line for our case. The proof uses \cite[Lemmas 8.10, 8.11]{vo}, that in turn rely on $3$ assumptions denoted in \cite{vo} by (i), (ii), (iii). Vojta needs to show that such assumptions are satisfied in his case, and the proofs are quite involved. On the other hand, we now  explain why the assumptions hold immediately in our setting: assumption (i) follows by the integral Liouville inequality (see Proposition \ref{properties}(6)) if we put $\Xi=\{\beta_k\}$, $q=n$, $\lambda_{\beta_k,j}=-\log^-\vert\alpha_j-\beta_k\vert$ and  $c_9= \log 2+\max_j h(\alpha_j)$ for $j=1,\ldots, n$. Assumption (ii) is the $\mu$-equicontinuity condition. Assumption (iii) is the uniform integrability condition.

Finally,  note that in the statement of \cite[Proposition 8.12]{vo} the condition $(1)$ is not explicitly mentioned as a consequence of the hypotheses, but it can be easily deduced from the proof.
\endproof




\textbf{Proof of theorem \bref{thm:main}{(B)}.}
When $n=1$, from  Proposition \ref{properties}$(6)$ we deduce that  any approximant $\beta$ such that 
$$h(\beta)>\frac{\log 2+h(\alpha_1)+c}{1+\varepsilon}
$$
satisfies the desired inequality.\\
 

 Fix $n\ge 2$. Assume by contradiction that the theorem is false for some  $\varepsilon_0>0$ and that the counterexample is given by a sequence of approximants $\{\beta_k\}$ such that $h(\beta_k)\to+\infty$.  We apply Lemma \ref{vo8.12}; so for any  $r_0,r_1>1$ and $\varepsilon<\varepsilon_0$  there exist $\beta^{(1)},\ldots,\beta^{(N)}\in\{\beta_m\}$ satisfying the properties $(1)$-$(3)$. Consider the matrix constructed with the vector $\bm{\beta}=(\beta^{(1)},\ldots,\beta^{(N)})$:
\[
T(\bm{\beta})=\begin{pmatrix}
 \alpha_1& \alpha_1  &\ldots &\alpha_1 \\
 \alpha_2& \alpha_2  &\ldots &\alpha_2\\
\vdots & \vdots  & \vdots & \vdots\\
\alpha_n& \alpha_n  &\ldots &\alpha_n\\
\beta^{(1)}& \beta^{(2)}  &\ldots &\beta^{(N)}
\end{pmatrix}
\] 
 Pick a constant:
\[
L>  \log\left(4^{2N!}\prod^n_{i=1}H(\alpha_i)^{\frac{2N!}{n}}\right) 
\]
 We are ready to construct a function  $\theta\in L^1(S,\mu)$ which will give the desired contradiction. We define it as a piecewise function by putting for any $\omega\in S_i$:
\[
\theta|_{S_i}(\omega)=\min_k\frac{-\log^- \vert \beta^{(k)}-\alpha_i\vert_{\omega}}{L+h(\beta^{(k)})}= \min_k \frac{-\log^- \vert \beta^{(k)}-\alpha_i\vert_{\omega}}{h(\beta^{(k)})}A_k
\]
where $A_k=1-\frac{L}{L+h(\beta^{(k)})}$. Let's fix the set:
\[
\hat S_i:=\{\omega\in S_i\colon \vert\beta^{(k)}-\alpha_i\vert_\omega < 1\,, \text{ for } k=1,\ldots, N\}
\]
 and put $\hat S=\bigcup^n_{i=1} \hat S_i$; note that $\theta|_{S\setminus\hat S}=0$.  We can choose  $h(\beta^{(1)})\gg L\gg N> 21^2\log 2n $ in a way that we can assume: 

\begin{equation}\label{theepss}
\varepsilon>\frac{2}{A_1}+\frac{7\sqrt{\log 2n}}{A_1\sqrt N}-2>0
\end{equation}
By using property $(3)$ of Lemma \ref{vo8.12} and  $(\ref{theepss})$ we get:
\begin{eqnarray}\label{final_contr1}
\int_{\hat S}\theta d\mu =\int_{ S} \theta d\mu=\sum^n_{i=1}\int_{S_i}\theta|_{S_i}d\mu>A_1\sum_{i=1}^n\int_{S_i}\min_{k}\frac{-\log^-|\beta^{(k)}-\alpha_i|_\omega}{h(\beta^{(k)})}d\mu(\omega)> \nonumber \\
>A_1\left(2+\varepsilon\right)>2+\frac{7\sqrt{\log 2n}}{\sqrt N}\,.
\end{eqnarray}

Now we want to show that we can apply Theorem \ref{teoremadue}.
\begin{itemize}
\item[$\bullet$]$T(\bm{\beta})$ satisfies the h-gap condition since we can choose the $\beta^{(k)}$ such that the heights $h(\beta^{(k)})$ are separated enough by property $(2)$ of Lemma \ref{vo8.12}.
\item[$\bullet $]  Since $\vert\alpha_i-\beta^{(k)}\vert_\omega < 1$ for $\omega\in \hat S_i$,  the function $\theta$ is column bounding for $T(\bm{\beta})$  on $\hat S$. Indeed for any $k=1,\ldots, N$ and $\omega\in \hat S_i$ we have that:
$$\theta(\omega)\le \frac{-\log^- \vert \beta^{(k)}-\alpha_i\vert_{\omega}}{L+h(\beta^{(k)})}\le \frac{-\log^{-}\vert\beta^{(k)}-\alpha_i\vert_\omega}{\log\left(4^{2N!}\prod^n_{i=1}H(\alpha_i)^{\frac{2N!}{n}}\right) + h(\beta^{(k)})}$$
\end{itemize}
Therefore we can apply Theorem \ref{teoremadue} to conclude that:
$$
\int_{\hat S}\theta d \mu<2+\frac{7\sqrt{\log 2n}}{\sqrt{N}}
$$
which  contradicts inequality (\ref{final_contr1}).

\hfill{$\square$}
{}\\

Note that in the proofs of Theorems \bref{thm:main}{(A)} and \bref{thm:main}{(B)} we didn't assume Northcott property for our adelic curve.





\begin{expl}\label{Qbar}  Consider the adelic curve  $\mathbb X=(\mathbb Q,\Omega, \id)$ naturally obtained from the field $\mathbb K=\mathbb Q$ as in Example (\ref{counting}). We prove that the adelic curve $\overline{\mathbb X}=(\overline{\mathbb Q},\overline{\Omega}, \id)$ doesn't satisfy the (strong) $\mu$-equicontinuity condition by showing that the generalised Roth's theorem doesn't hold.  

The Thue equation $X^3-2Y^3=1$ has infinitely many solutions $(x_k,y_k)=\left (\sqrt[3]{2k^3+1}, k\right)$ for $k=1,2,\ldots$ in the algebraic integers. Note that by a theorem of Mahler  such solutions cannot be contained in a number field (see for instance \cite[Theorem 3.12]{Z}). Consider now the approximants $\beta_k=\frac{x_k}{y_k}=\sqrt[3]{2+\frac{1}{k^3}}$ for $\alpha=\sqrt[3]{2}$. First of all notice that
\[
h\left(\sqrt[3]{2+\frac{1}{k^3}}\right)=\log k+ O(1)
\]
whereas by using the identity $\zeta^2_3+\zeta_3+1=0$ where $\zeta_3$ is a primitive cubic root of the unity we obtain the following equality for the euclidean absolute value:

\[
-\log\left\vert \beta_k-\alpha\right\vert=-\log\left\vert \frac{x_k-\sqrt[3]{2}y_k}{k}\right\vert=-\log\left\vert\frac{x^3_k-2y^3_k}{k(x_k-\zeta_3\sqrt[3]{2}y_k)(x_k-\zeta^2_3\sqrt[3]{2}y_k)}\right\vert=
\]
 \[
 =\log k+\log\left\vert x_k-\zeta_3\sqrt[3]{2}y_k \right\vert + \log\left \vert x_k-\zeta^2_3\sqrt[3]{2}y_k \right\vert=3\log k+ O(1)
 \]
With the same strategy employed in the proof of Proposition \ref{im_cor}  it is easy to show that these calculations give a counterexample to Theorem \bref{thm:main}{(A)} for the adelic curve $\overline{\mathbb X}$. Hence we conclude that $\overline{\mathbb X}$ cannot satisfy the (strong) $\mu$-equicontinuity condition.
 
 
 
 
 
 \begin{comment}
 The measure on $\overline{\Omega}$ is denoted by $\chi$, whereas the measure on $\Omega$ is $\mu$. In the following discussion for simplicity of presentation we often identify the primes of a number field with the induced absolute value.

First of all notice that singletons of $\overline{\Omega}$ are measurable thanks to \cite[Lemma 2.2.1]{CM2}; we are going to show that they have measure $0$.  Let $K$ be a finite extension of $\mathbb Q$  and let $\mu_K$ be the measure on the adelic curve naturally constructed on $K$. For any $\omega\in\Omega_K$ extending $p\in\mathbb Q$, thanks to properties of the measure $\chi$ discussed in \cite[Section 2.2]{GR}  we have:
\[
\chi(M_{\overline{\mathbb Q},\omega})=\mu_K(\{\omega\})=\frac{[K_\omega\colon \mathbb Q_p]}{[K\colon \mathbb Q]}=\frac{[K\colon \mathbb Q]}{\#(M_{K,p})}\frac{1}{[K\colon \mathbb Q]}=\frac{1}{\#(M_{K,p})}
\]
Where $M_{\overline{\mathbb Q} ,\omega}$ is the set of places of $\overline{\mathbb Q}$ lying over $\omega$ and $M_{K,p}$ is the set of places of $K$ lying over $p$. By \cite[Th\'eor\`eme 2.9]{GR} we can find a tower of finite extensions:
\[
\mathbb Q\subset K_1\subset\ldots\subset K_n\subset\ldots
\]
such that the sequence $\{\#(M_{K_n,p})\}_n$ is increasing. So, it follows that singletons have measure $0$.


It means that we can construct a subset $S\subset\overline{\Omega}$ of finite measure that lies on infinitely many primes of $\mathbb Q$. Then for any finite measurable partition $C_1\sqcup C_2\sqcup,\ldots \sqcup C_r=S$ there is a set $C_j$ that lies over infinitely many primes of $\mathbb Q$. Now consider a prime number $p$ such that $C_j$ contains an absolute value $\omega_0$ that  restricts to $\vert\cdot\vert_p$, then for any other non-archimedean $\omega\in C_j$ not lying over $\vert\cdot\vert_p$ we have that:
\[
\vert-\log^-\vert p\vert_{\omega_0}+\log^-\vert p\vert_\omega\vert=\log p
\]
independently from any choice of a subset $U\subseteq\Omega_{\infty}$.
\end{comment}
\end{expl}












\begin{appendices}

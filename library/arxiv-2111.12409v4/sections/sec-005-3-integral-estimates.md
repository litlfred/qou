---
doc_id: arxiv-2111.12409v4
doc_title: "On the generalisation of Roth’s theorem"
section_id: sec-005-3-integral-estimates
section_title: "Integral estimates"
section_number: 3
pages: 8-19
source_pdf: 2111.12409v4.pdf
source_sha256: 3f0b94ee06fe79bf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.853
latex_coverage_ratio: 0.985
doc_brief: "On the generalisation of Roth’s theorem — We present two generalisations of Roth’s approximation theorem on proper adelic curves, assuming some technical conditions on the behavior of the logarithmic"
---
\label{estimates}
This technical section is ``the heart'' of the proof of our results since here we will prove some integral bounds for very particular integrable functions $\theta:S\subset\Omega\to \mathbb R_{\ge 0}$. We continue with all the notations fixed in section \ref{aux} since we want to make full use of Proposition \ref{interpolationpoly}. 

Consider an adelic curve $(\mathbb K,\Omega, \phi)$ and a set of vectors $\bm{\alpha}_1,\ldots,\bm{\alpha}_n,\bm{\beta}\in\mathbb K^N$ which are componentwise different. We construct the following  matrices $T:=T(\bm{\alpha}_1,\ldots\bm{\alpha}_n)\in M(n\times N,\mathbb K)$ and $T(\bm{\beta})\in M(n+1\times N,\mathbb K)$:


\[
T:=\begin{pmatrix}
 \alpha^{(1)}_1& \alpha^{(2)}_1  &\ldots &\alpha^{(N)}_1 \\
 \alpha^{(1)}_2& \alpha^{(2)}_2  &\ldots &\alpha^{(N)}_2\\
\vdots & \vdots & \vdots & \vdots\\
\alpha^{(1)}_n& \alpha^{(2)}_n  &\ldots &\alpha^{(N)}_n
\end{pmatrix};\quad
T(\bm{\beta})=\begin{pmatrix}
 \alpha^{(1)}_1& \alpha^{(2)}_1  &\ldots &\alpha^{(N)}_1 \\
 \alpha^{(1)}_2& \alpha^{(2)}_2  &\ldots &\alpha^{(N)}_2\\
\vdots & \vdots  & \vdots  &\vdots\\
\alpha^{(1)}_n& \alpha^{(2)}_n  &\ldots &\alpha^{(N)}_n\\
\beta^{(1)}& \beta^{(2)}  &\ldots &\beta^{(N)}
\end{pmatrix}
\]
We denote by $\bm{\alpha}^{(j)}$, $j=1,\ldots, N$ the columns of $T$, that is:
\begin{equation*}
\bm{\alpha}^{(j)}=\begin{pmatrix}
 \alpha^{(j)}_1 \\
 \alpha^{(j)}_2\\
\vdots \\
\alpha^{(j)}_n
\end{pmatrix}
\end{equation*} 
and by $\bm{\alpha}_{h}$, for  $h\in\{1,2,\dots ,n\}$, the rows:
\begin{equation*}
\bm{\alpha}_{h}=\begin{pmatrix}
 \mathbb \alpha^{(1)}_h, \alpha^{(2)}_h,\ldots, \alpha^{(N)}_h
 \end{pmatrix}
\end{equation*}
Note that we are asking for the matrices $T$ and $T(\bm{\beta})$ to have componentwise different rows. Now we need to define a list of properties depending on the aforementioned matrices:
\begin{defn}\label{boxing}
For the matrix $T(\bm{\beta})$, consider the following real numbers for any $j=1,\ldots, N$: 
\begin{equation}\label{pivot}
\rho_{j}:=4^{2N!}H(\beta^{(j)})\prod_{h=1}^{n}H(\alpha_h^{(j)})^{\frac{2N!}{n}}
\end{equation}
\begin{equation}\label{pivotdue}
\rho'_{j}:=4^{N!}H(\beta^{(j)})\prod_{h=1}^{n}H(\alpha_h^{(j)})^{\frac{N!}{2n}}
\end{equation}
We say that $T(\bm{\beta})$ satisfies the \emph{$h$-gap property} if the following inequality is satisfied:
$$
\frac{{\rm{log}}\, \rho_j }{{\rm{log}}\,\rho'_{j+1}}<\frac{1}{4nN^2N!},\qquad \forall j=1,\ldots, N-1
$$
\end{defn}

\begin{defn}\label{bounding} Fix a measurable set $S=S_1\sqcup\ldots\sqcup S_n$. We say that an integrable function $\theta\colon S\to\mathbb R_{\ge 0}$ is a \emph{column bounding function for} $T(\bm{\beta})$ on $S$ if 
the following inequality holds:
\begin{equation}\label{boundingbis}
-\frac{1}{\log \rho_{j}}{\log}\vert \alpha^{(j)}_h-\beta^{(j)}\vert_\omega\ge\theta (\omega)\qquad \forall j=1,\ldots,N\,,\; \forall h=1,\ldots,n\,,\; \forall\omega\in S_h 
\end{equation}
\end{defn}

\begin{defn}
Fix a measurable set $S=S_1\sqcup\ldots\sqcup S_n$. For any column $\bm{\alpha}^{(j)}\in\mathbb K^N$  of the matrix $T$ and any $b\in\mathbb K$ we define the following quantity:
$$
\lambda(\bm{\alpha}^{(j)},b):=\frac{1}{V(s)}{\rm{log}}4+h(b)+\frac{1}{V(s)}\sum_{h=1}^{n}V(t_h)h(\alpha_{h}^{(j)})
$$
\end{defn}

\begin{defn}\label{lambda_gap} We say that  $T(\bm{\beta})$ satisfies the \emph{$\lambda$-gap property} of width $\eta\in\mathbb R_+$ if
$$
\max_{1\leq j\leq N-1}\frac{\lambda(\bm{\alpha}^{(j)},\beta^{(j)})}{\lambda(\bm{\alpha}^{(j+1)},\beta^{(j+1)})}<\frac{\eta}{2n}
$$
\end{defn}


\begin{defn}\label{lambda_bou} Fix a matrix $T(\bm{\beta})$. An integrable function $\theta\colon S\to \mathbb R_{\ge 0}$ is \emph{$\lambda$-bounding} if:
\begin{equation}\label{pequality}
\frac{-1}{\lambda(\bm{\alpha}^{(j)},\beta^{(j)})}
{\log}\vert \alpha^{(j)}_h-\beta^{(j)}|_{\omega} \ge\theta(\omega)\qquad \forall j=1,\dots ,N;\;\forall h=1,\dots,n;\;\forall \omega\in S_h
\end{equation}
\end{defn}

\begin{rem}\label{rem_forthelemma}
Note that if $\theta$ is $\lambda$-bounding or column bounding then it follows immediately that $\vert \alpha^{(j)}_h-\beta^{(j)}|_{\omega}\le 1$ for any  $j=1,\dots ,N$, $h=1,\dots,n$, $\omega\in S_h$.
\end{rem}


 The following easy lemma will be useful:
\begin{lem}\label{log2}
Let $x,y\in \mathbb K$ and let $\omega$ such that $\vert x-y\vert_\omega\le 1$. Then   $\log^+\vert x\vert_\omega\le \log^+\vert 2\vert_\omega+\log^+\vert y\vert_{\omega}$.
\end{lem}
\proof
 We distinguish two cases:\\
\emph{$\vert\cdot\vert_\omega$ is  ultrametric.} Then  
$$
\vert x\vert_\omega=\vert x-y+y\vert_\omega\le \max\left\{ \vert x-y\vert_{\omega}, \vert y\vert_{\omega}\right\}\le \max\left\{1, \vert y\vert_{\omega}\right\}\,.
$$
If $\vert y\vert_{\omega}\ge 1$, then clearly $\log^+\vert x\vert_\omega\le     \log^+\vert y\vert_\omega$. If $\vert y\vert_{\omega}<1$, then $\vert x\vert_{\omega}\le 1$ which means  $0=\log^+\vert x\vert_{\omega}\le \log^+\vert 2\vert_\omega+\log^+\vert y\vert_{\omega}$.


\emph{$\vert\cdot\vert_\omega$ is  archimedean}. By  Ostrowski's theorem $\vert\cdot\vert_\omega=\vert\cdot\vert^{\varepsilon(\omega)}$, therefore
$$
\vert x\vert^{\frac{1}{\varepsilon(\omega)}}_\omega\le\vert x-y\vert^{\frac{1}{\varepsilon(\omega)}}_{\omega}+\vert y\vert^{\frac{1}{\varepsilon(\omega)}}_\omega\le 1+\vert y\vert^{\frac{1}{\varepsilon(\omega)}}_\omega\,.
$$
This clearly means $\vert x\vert^{\frac{1}{\varepsilon(\omega)}}_\omega\le 2\max\left\{1, \vert y\vert^{\frac{1}{\varepsilon(\omega)}}_\omega\right\}$. After raising each side to the power of $\varepsilon(\omega)$ and applying $\log^+$ we get the claim.
\endproof




Now we prove the analogue of \cite[Proposition 3.1]{C}.  






\begin{prop}\label{corvajaprop3.1} Let $(\mathbb K,\Omega, \phi)$ be a proper adelic curve. Fix a matrix $T(\bm{\beta})$. Let $\eta,s,t_1,\ldots,t_n\in\mathbb R$ such that all the hypotheses of Proposition \ref{interpolationpoly} are satisfied. Assume that $T(\bm{\beta})$ satisfies the $\lambda$-gap property of width $\eta$  (see Definition \ref{lambda_gap}) and that $\theta\colon S\to \mathbb R_{\ge 0}$ is $\lambda$-bounding for $T(\bm{\beta})$ (see Definition \ref{lambda_bou}), then
$$
\sum_{h=1}^{n}\begin{pmatrix}t_h-s-\frac{2\eta N^2}{V(s)}\end{pmatrix}\int_{ S_h}\theta d \mu\le N
$$
\end{prop}
\begin{proof} Fix a real number $D>0$, and for every $j=1,\dots, N$, we  put 
$$
d_{j}:=\frac{D}{\lambda(\bm{\alpha}^{(j)},\beta^{(j)})}
$$ 
and $d:=\prod^N_{j=1} d_j$. Note that here we use the $\lambda$-gap property to ensure that $\frac{d_{}j+1}{d_j}<\gamma$ since $\eta=2n\gamma$ as explained before Proposition \ref{interpolationpoly}. So, the hypotheses of Proposition \ref{interpolationpoly} are all satisfied and we have the interpolation polynomial $\delta$ such that $\delta(\bm{\beta})\neq 0$. We start by distinguishing two cases.


{\emph{First case: $\omega\in S_h$}}.  By the Taylor expansion for $\delta$ at $\bm{\alpha}_h$ we write
\begin{equation}\label{bound_pol}
\delta(\bm{\beta})=\sum_{{\bm i}}\Delta^{{\bm i}}\delta(\bm{\alpha}_h)\prod_{j=1}^{N}(\beta^{(j)}- \alpha_{h}^{(j)})^{i_j}\quad \textrm{where }{\bm{i}}=(i_1,\ldots, i_N)
\end{equation}
Notice that each term 
$$
 \Delta^{{\bm i}}\delta(\bm{\alpha}_h)\prod_{j=1}^{N}(\beta^{(j)}- \alpha_{h}^{(j)})^{i_j}
$$
is bounded from above by:
$$
\left(\max_{\bm{i}}\Delta^{{\bm i}}\delta(\bm{\alpha}_h)\right)\;\left(\max^\ast_{\bm{i}}\prod_{j=1}^{N}(\beta^{(j)}- \alpha_{h}^{(j)})^{i_j}\right)\,,
$$
where  in order to simplify the notation we define
$$
\max^\ast_{\bm{i}}:=\max_{\substack {\bm{i}\\ \Delta^{{\bm i}}\delta(\bm{\alpha}_h)\neq 0}}
$$
Let's put $M:=\prod^N_{j=1} (1+\deg_{X_j}\delta)$; so by taking the absolute value $\vert\cdot\vert_{\omega}$ in equation (\ref{bound_pol}) we get
\begin{equation}\label{bound_pol1}
\log|\delta(\bm{\beta})|_{\omega}\le \log^+\vert M\vert_\omega+\max_{\bm i}\,\log \left\vert\Delta^{{\bm i}}\delta(\bm{\alpha}_h)\right\vert_\omega+\max^\ast_{\bm{i}}\,\log
\left\vert\prod_{j=1}^{N}(\beta^{(j)}- \alpha_{h}^{(j)})^{i_j}\right\vert_{\omega}
\end{equation}
 The last summand of equation (\ref{bound_pol1}) is bounded from above by
$$
-{\Ind}_{\bm{\alpha}_h, \bm{d}}(\delta)\,\min\left\{d_1\log\frac{1}{\vert\beta^{(1)}- \alpha_{h}^{(1)}\vert_\omega},\ldots , 
d_N\log\frac{1}{\vert\beta^{(N)}- \alpha_{h}^{(N)}\vert_\omega}\right\}\,.$$
We  use Lemma \ref{corvajalemmepag166} to give an upper bound for $\log \left\vert\Delta^{{\bm i}}\delta(\bm{\alpha}_h)\right\vert_\omega$, hence from equation (\ref{bound_pol1}) we  deduce:
$$
\int_{ S_h}\log\vert \delta(\bm{\beta})\vert_\omega d \mu(\omega)\leq
$$
$$
\leq \int_{S_h}\log^+\lvert M\vert_\omega d\mu(\omega)+ \int_{ S_h}\left(h_\omega(\delta)+\log^+ \lvert M\rvert_\omega+\sum_{j=1}^{N}(\log^+\vert 2\vert_\omega+\log^+\vert\alpha_{h}^{(j)} \vert_\omega)\deg_{X_j}\delta\right)d\mu(\omega) +
$$
$$
-\int_{ S_h}\Ind_{\bm{\alpha}_h, \bm{d}} (\delta)\,\min\left\{d_1\log\frac{1}{\vert\beta^{(1)}- \alpha_{h}^{(1)}\vert_\omega},\ldots , 
d_N\log\frac{1}{\vert\beta^{(N)}- \alpha_{h}^{(N)}\vert_\omega}\right\}d\mu(\omega)
$$

So, by rearranging the terms  and summing over all $h=1,\ldots,n$ we get
\begin{multline}\label{long_ext1}
\sum^n_{h=1}\Ind_{\bm{\alpha}_h, \bm{d}} (\delta)\int_{ S_h}\min\left\{d_1\log\frac{1}{\vert\beta^{(1)}- \alpha_{h}^{(1)}\vert_\omega},\ldots , 
d_N\log\frac{1}{\vert\beta^{(N)}- \alpha_{h}^{(N)}\vert_\omega}\right\}d\mu(\omega)\leq -\int_{ S}\log\vert \delta(\bm{\beta})\vert_\omega d \mu(\omega)\\
+ 2\int_S \log^+\vert M\vert_\omega d\mu(\omega)+\int_{S}h_\omega(\delta) d\mu(\omega) +\sum_{h=1}^n\int_{S_h}\sum_{j=1}^{N}(\log^+\vert 2\vert_\omega+\log^+\vert\alpha_{h}^{(j)} \vert_\omega)\deg_{X_j}\delta d\mu(\omega)
\end{multline}
At this point  we can use Lemma \ref{log2} and Remark \ref{rem_forthelemma} for the following bound:
\begin{equation}\label{lastimachiave}
\sum_{h=1}^n\int_{S_h}\sum_{j=1}^{N}(\log^+\vert 2\vert_\omega+\log^+\vert\alpha_{h}^{(j)} \vert_\omega)\deg_{X_j}\!\!\delta d\mu(\omega)\le \int_{S} \sum_{j=1}^{N}(\log^+\vert 4\vert_\omega+\log^+\vert\beta_{h}^{(j)} \vert_\omega)\deg_{X_j}\!\!\delta d\mu(\omega)\,
\end{equation}
 to obtain
\begin{multline}\label{long_ext1}
\sum^n_{h=1}\Ind_{\bm{\alpha}_h, \bm{d}} (\delta)\int_{ S_h}\min\left\{d_1\log\frac{1}{\vert\beta^{(1)}- \alpha_{h}^{(1)}\vert_\omega},\ldots , 
d_N\log\frac{1}{\vert\beta^{(N)}- \alpha_{h}^{(N)}\vert_\omega}\right\}d\mu(\omega)\leq -\int_{S}\log\vert \delta(\bm\beta)\vert_\omega d \mu(\omega)+\\
+  2\int_S \log^+\vert M\vert_\omega d\mu(\omega)+\int_{ S}h_\omega(\delta) d\mu(\omega)+\int_{ S} \sum_{j=1}^{N}(\log^+\vert 4\vert_\omega+\log^+\vert\beta_{h}^{(j)} \vert_\omega)\deg_{X_j}\!\!\delta d\mu(\omega)\,.
\end{multline}


{\it{ Second case: $\omega\not\in  S$.}} Consider the expression:
$$
\delta(\bm{\beta})=\sum_{\bm i}\Delta^{\bm i}\delta(\bm{0})\beta^{(1)_{i_1}}\ldots \beta^{(N)_{i_N}} \quad \textrm{where }{\bm {i}}=(i_1,\ldots, i_N)
$$
We take the absolute value:
$$ \log\vert \delta(\bm{\beta})\vert_\omega\leq h_\omega(\delta)+\sum_{j=1}^{N}(\log^+\vert\beta^{(j)}\vert_\omega\deg_{X_j}\!\!\delta)+ \log^+\vert M\vert_\omega
$$
Hence
\begin{equation}\label{intermedioarchimedeo}
\int_{\Omega\setminus S}\log\vert \delta(\bm{\beta})\vert_\omega d\mu(\omega)\leq \int_{\Omega\setminus  S}h_\omega(\delta)d\mu(\omega)+\sum_{j=1}^{N}\int_{\Omega\setminus   S}(\log^+\vert\beta^{(j)}\vert_\omega\deg_{X_j}\!\!\delta\,)d\mu(\omega)+\int_{\Omega\setminus S}\log^+\vert M\vert_\omega d \mu(\omega)
\end{equation}
Since $(\mathbb K,\Omega, \phi)$ is proper
\begin{equation}\label{ad_prod}
-\int_{ S} \log \vert\delta(\bm{\beta})\vert_\omega d\mu(\omega)=\int_{\Omega\setminus  S} \log \vert\delta(\bm{\beta})\vert_\omega d\mu(\omega)\,.
\end{equation}
The distinction of the two cases is now finished, so by using equation (\ref{ad_prod}) and estimate  (\ref{intermedioarchimedeo}) inside (\ref{long_ext1}) we get 
\begin{multline}\label{verylongext}
\sum^n_{h=1}\Ind_{\bm{\alpha}_h, \bm{d}} (\delta)\int_{ S_h}\min\left\{d_1\log\frac{1}{\vert\beta^{(1)}- \alpha_{h}^{(1)}\vert_\omega},\ldots , 
d_N\log\frac{1}{\vert\beta^{(N)}- \alpha_{h}^{(N)}\vert_\omega}\right\}d\mu(\omega)\leq 2h(M) +\\
+\int_{\Omega}h_\omega(\delta)d\mu(\omega)+\sum_{j=1}^{N}\int_{\Omega\setminus  S}(\log^+\vert\beta^{(j)}\vert_\omega\deg_{X_j}\!\!\delta\,)d\mu(\omega)+\int_{ S} \sum_{j=1}^{N}(\log^+\vert 4\vert_\omega+\log^+\vert\beta_{h}^{(j)} \vert_\omega)\deg_{X_j}\!\!\delta d\mu(\omega)
\end{multline}
 Since we can always assume that $\mu$ is adequately normalised, we have $\int_{\Omega}\log^{+}\vert 4\vert_\omega d\mu(\omega)=h(4)\le\log 4$, therefore:
\begin{multline*}
\sum_{j=1}^{N}\int_{\Omega\setminus  S}(\log^+\vert\beta^{(j)}\vert_\omega\deg_{X_j}\!\!\delta\,)d\mu(\omega)+\int_{ S} \sum_{j=1}^{N}(\log^+\vert 4\vert_\omega+\log^+\vert\beta_{h}^{(j)} \vert_\omega)\deg_{X_j}\!\!\delta d\mu(\omega)\leq\\
\leq \sum_{j=1}^{N}\left(h(\beta^{(j)})+\log 4\right)\deg_{X_j}\!\!\delta
\end{multline*}
By plugging everything inside equation (\ref{verylongext}) we get
\begin{multline}\label{Vlong}
\sum^n_{h=1}\Ind_{\bm{\alpha}_h, \bm{d}} (\delta)\int_{ S_h}\min\left\{d_1\log\frac{1}{\vert\beta^{(1)}- \alpha_{h}^{(1)}\vert_\omega},\ldots, d_N\log\frac{1}{\vert\beta^{(N)}- \alpha_{h}^{(N)}\vert_\omega}\right\}d\mu(\omega)\leq \\
\leq 2h(M)+h(\delta)+\sum_{j=1}^{N}\left(h(\beta^{(j)})+\log 4\right)\deg_{X_j}\!\!\delta
\end{multline}
By the $\lambda$-bounding hypothesis for $T(\bm{\beta})$ 
we can write 
$$
-\frac{D}{{\lambda(\bm{\alpha}^{(j)},\beta^{(j)})}}\log\vert\beta^{(j)}- \alpha_{h}^{(j)}\vert_\omega \ge D\theta(\omega)\,. 
$$
Then we use Proposition \ref{interpolationpoly}$(3)$, so we can conclude 
\begin{multline}\label{sinistro}
D\sum_{h=1}^{n}dV(s)\left(t_h-s-\frac{2N^2\eta}{V(s)} \right)\int_{S_h}\theta d\mu\le\\
\leq\sum^n_{h=1}\Ind_{\bm{\alpha}_h, \bm{d}} (\delta)\int_{S_h}\min\left\{d_1\log\frac{1}{\vert\beta^{(1)}- \alpha_{h}^{(1)}\vert_\omega},\ldots, d_N\log\frac{1}{\vert\beta^{(N)}- \alpha_{h}^{(N)}\vert_\omega}\right\}d\mu(\omega)
\end{multline}
Now we are going to use again Proposition \ref{interpolationpoly}  to find upper bounds for the terms on the right hand side of equation (\ref{Vlong}). By Proposition \ref{interpolationpoly}$(2)$:
 \begin{equation}\label{destro}
 \sum_{j=1}^{N}\left(h(\beta^{(j)})+\log 4\right)\deg_{X_j}\!\!\delta\leq \sum_{j=1}^{N}\left( h(\beta^{(j)})+\log 4\right)(dd_jV(s)+O(d))\,.
 \end{equation}
Proposition \ref{interpolationpoly}$(4)$ says that,
\begin{equation}
h(\delta)\leq d\sum_{j=1}^{N}d_j\left(\log 2+ \sum_{h=1}^{n}V(t_h)h(\alpha^{(j)}_{h})\right)+O(d\log d)
\end{equation}
So now (\ref{Vlong}) can be written in the following way:
 \begin{multline}\label{thefinal}
 D\sum_{h=1}^{n}dV(s)\left(t_h-s-\frac{2N^2\eta}{V(s)} \right)\int_{ S_h}\theta d\mu\leq 2h(M)+d\sum_{j=1}^{N}d_j\left(\log 2+ \sum_{h=1}^{n}V(t_h)h(\alpha^{(j)}_{h})\right)+ \\
 +O(d\log d)+\sum_{j=1}^{N}\left( h(\beta^{(j)})+\log 4\right)(dd_jV(s)+O(d))
\end{multline}
Notice that since $s\le 1$ and $N\ge 2$ then $V(s)\le\frac{1}{2}$, which is equivalent to the inequality $V(s)\log 4+\log 2\leq \log 4$. Then the expression
$$
d\sum_{j=1}^{N}d_j\left(\log 2+ \sum_{h=1}^{n}V(t_h)h(\alpha^{(j)}_{h})\right)+O(d{\rm{log}}d)+\sum_{j=1}^{N}\left( h(\beta^{(j)})+\log 4\right)(dd_jV(s)+O(d))
$$
is bounded by 
$$
d\sum_{j=1}^{N}d_j\left(V(s) h(\beta^{(j)})+\log 4+   \sum_{h=1}^{n}V(t_h)h(\alpha^{(j)}_{h})\right)+O(d\log d)
$$
But by the definitions of $d_j$ and the function $\lambda$ it holds that
\begin{equation}
dV(s)\sum_{j=1}^{N}d_j\left(h(\beta^{(j)})+\frac{\log 4}{V(s)}+   \sum_{h=1}^{n}\frac{V(t_h)}{V(s)}h(\alpha^{(j)}_{h})\right)=dV(s)ND\,.
\end{equation}
Therefore equation (\ref{thefinal}) becomes
$$
 dDV(s)\sum_{h=1}^{n}\left(t_h-s-\frac{2N^2\eta}{V(s)} \right)\int_{ S_h}\theta d\mu\leq dV(s)ND+O(d\log d)
$$
since the terms $2h(M)$ and $O(d)$ can be put together inside $O(d\log d)$. Finally we divide both sides by $dDV(s)$ and we take the limit for $D\to+\infty$ (i.e. $d\to+\infty$) to conclude the proof.
\end{proof}


\begin{thm}\label{teoremadue}  Let $(\mathbb K,\Omega, \phi)$ be a proper adelic curve. Assume that the matrix $T(\bm{\beta})\in M(n\times N,\mathbb K)$ satisfies the h-gap property (see Definition \ref{boxing}). Moreover fix $N>21^2\log 2n$ and let $\theta\colon S\to\mathbb R_{\ge 0}$ be a column-bounding function for $T(\bm{\beta})$ (see Definition \ref{bounding}). Then
$$
\int_{ S}\theta d \mu<2+\frac{7\sqrt{\log 2n}}{\sqrt{N}}
$$
\end{thm}

\proof The proof is based on the exact calculation of the volume $V(s)$ of \cite[Chap. 2, Lemma 5A, 5B]{schm}. It shows that for  $N\geq 2$, $s,\rho\in\mathbb R_{>0}$ with $0<s\leq 1$ and $0<\rho <\frac{N}{2}$, we have:
\begin{equation}\label{stima_sch}
V(s)= \frac{s^N}{N!}
\end{equation}
\begin{equation}\label{stima_sch2}
V\left(\frac{N}{2}-\rho\right)<e^{\frac{-\rho^2}{N} }
\end{equation}
We take $t_1=t_2=\ldots= t_n=\frac{N}{2}-\rho$, $\eta=\frac{1}{2N^2 N!}$ where $\rho$ is a number such that:
$$
V\left(\frac{N}{2}-\rho\right)=\frac{1-\eta N^2}{n}
$$
Note that $\frac{1-\eta N^2}{n}>\frac{1}{2n}$. Now from equation (\ref{stima_sch2}) we get
$$
\frac{-\rho^2}{N}>\log\left(\frac{1-\eta N^2}{n}\right)
$$
which implies easily
$$
\rho< \sqrt {N\log2n}\,.
$$
Now let's take $s$ as a solution of:
\begin{equation}\label{stimavol}
(1+\eta)^{N}-1+\eta N^2<V(s)< 2N\eta +\eta N^2
\end{equation}
Here recall that $1-\eta N^2=nV(t_h)=\sum^n_{h=1} V(t_h)$ (compare with the condition (\ref{basicinequality})).
From equation (\ref{stimavol}) we get the following two conditions
\[
N!<\frac{1}{V(s)}<2N!
\]
\[
\frac{N!}{2n}<\frac{V(t_h)}{V(s)}<\frac{2N!}{n}
\]

Now we show that by using such conditions since $T(\bm{\beta})$ satisfies $h$-gap property, then it satisfies also the $\lambda$-gap property of width $\eta$. First let's use the inequalities $\frac{1}{V(s)}<2N!$  and $\frac{V(t_h)}{V(s)}<\frac{2N!}{n}$ to bound $\lambda(\bm{\alpha}^{(j)},\beta^{(j)})$ from above:
\[
\lambda(\bm{\alpha}^{(j)},\beta^{(j)})=\frac{1}{V(s)}{\rm{log}}4+h(\beta^{(j)})+\frac{1}{V(s)}\sum_{h=1}^{n}V(t_h)h(\alpha_{h}^{(j)})<
\]
\[
< 2N!\log4+h(\beta^{(j)})+\frac{2N!}{n}\sum_{h=1}^{n}h(\alpha_{h}^{(j)})=\log \rho_j\,.
\]
Then we use the inequalities $N!<\frac{1}{V(s)}$ and $\frac{N!}{2n}<\frac{V(t_h)}{V(s)}$ to bound $\lambda(\bm{\alpha}^{(j+1)},\beta^{(j+1)})$ from below:
\[
\lambda(\bm{\alpha}^{(j+1)},\beta^{(j+1)})=\frac{1}{V(s)}{\rm{log}}4+h(\beta^{(j+1)})+\frac{1}{V(s)}\sum_{h=1}^{n}V(t_h)h(\alpha_{h}^{(j+1)})>
\]
\[
> N!\log4+h(\beta^{(j+1)})+\frac{N!}{2n}\sum_{h=1}^{n}h(\alpha_{h}^{(j+1)})=\log \rho'_j\,.
\]
Therefore now:
\[
\frac{\lambda(\bm{\alpha}^{(j)},\beta^{(j)})}{\lambda(\bm{\alpha}^{(j+1)},\beta^{(j+1)})}<\frac{\log \rho_j}{\log \rho'_j}<\frac{1}{4nN^2N!}=\frac{\eta}{2n}\,.
\]

Note that as an immediate consequence of the last inequality  it follows that all the hypotheses of Proposition \ref{interpolationpoly} are satisfied.  Moreover, since $\theta$ is a column-bounding function for $T(\bm{\beta})$, then it is $\lambda$-bounding for $T(\bm{\beta})$. It means that we can apply Proposition \ref{corvajaprop3.1} to get:
\begin{equation}\label{lastupb}
\int_{ S}\theta d \mu\le \frac{N}{\frac{N}{2}-\rho-s-\frac{2\eta N^2}{V(s)} }
\end{equation} 
Since  $\rho< \sqrt{N\log 2n}$,  $N^2\eta<V(s)$ and in particular  $N>\max\left\{\frac{36}{\log 2n}, 9\log 2n\right\}$, we obtain:

\[
\frac{2(\rho+s)}{N}+\frac{4\eta N}{V(s)}<\frac{2\sqrt{N\log2n}+2+4}{N}<\frac{3\sqrt{N\log 2n}}{N}=\frac{3\sqrt{\log 2n}}{\sqrt N}<1
\]
Therefore
\[
\frac{N}{\frac{N}{2}-\rho-s-\frac{2\eta N^2}{V(s)}}=\frac{2}{1-\frac{2(\rho+s)}{N}-  \frac{4\eta N}{V(s)}}<\frac{2}{1-\frac{3\sqrt{\log 2n}}{\sqrt N}}<2+\frac{7\sqrt{\log 2n}}{\sqrt{N}}\,.
\]
Where the last inequality follows by the assumption $N>21^2\log 2n$.
\endproof




\section{Roth's theorem for adelic curves (A)}\label{mainsect}


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





\section{Roth's theorem for adelic curves (B)}\label{mainsect2}

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

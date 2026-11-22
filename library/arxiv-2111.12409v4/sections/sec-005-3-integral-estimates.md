---
doc_id: arxiv-2111.12409v4
doc_title: "On the generalisation of Roth’s theorem"
section_id: sec-005-3-integral-estimates
section_title: "Integral estimates"
section_number: 3
pages: 8-13
source_pdf: 2111.12409v4.pdf
source_sha256: 3f0b94ee06fe79bf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.984
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

---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-005-42-a-fractional-leibniz-rule
section_title: "A fractional Leibniz rule"
section_number: 4.2
pages: 10-18
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 0.995
doc_brief: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case — We prove the analyticity of smooth critical points for generalized integral Menger cur- vature"
---
\label{subsec:FractionalLeibnizRule}

The remainder term $R^{(p)}$ contains amongst others the factor $\Gamma$, which is basically given as a product of two functions multiplied with a singular weight. By applying a Bessel potential space norm, we obtain a sort of fractional Leibniz rule which will subsequently be discussed for $\Gamma$ and its derivatives. 


We observe that the $l$-th derivative of $R^{(p)}$ leads to $k$-th derivatives of $\Gamma$, where $k\leq l+1$. Applying the generalized Leibniz rule to the $ k$-th derivative of $\Gamma$ in the next step, we obtain
\[
\begin{split}
& \frac {\d^{k}} {\d u^{k}} \Gamma(u,v,w,s_1,s_2)  = \frac{1}{|v|^{p-2}|w|^{p-2}|v-w|^{p}} \\
& \cdot  \sum_{o=0}^{k} \binom{k}{o} \left(\gamma^{(k-o+1)}(u+x_1) - \gamma^{(k-o+1)}(u+x_2) \right) \otimes \left( \gamma^{(o+1)}(u+x_3) - \gamma^{(o+1)}(u+x_4) \right),
\end{split}
\]
where we have the four cases 
\[
\begin{split}
\textbf{Case 1:} & \quad (x_1,x_2,x_3,x_4) =(s_1w,s_1v, s_2w, s_2v), \\
\textbf{Case 2:} & \quad (x_1,x_2)=(x_3,x_4) = (s_1w,s_2w), \\
\textbf{Case 3:} & \quad (x_1,x_2)=(x_3,x_4) = (s_1v, s_2v), \\
\textbf{Case 4:} & \quad (x_1,x_2)=(x_3,x_4) = (v+s_1(w-v), v+s_2(w-v)).
\end{split}
\]
The key observation here is that $\Gamma$ as well as its derivatives can be broken down into sums of products of the form
\[
	\left(\gamma_i^{(k-o+1)}(u+x_1) - \gamma_i^{(k-o+1)}(u+x_2) \right) \cdot \left( \gamma_j^{(o+1)}(u+x_3) - \gamma_j^{(o+1)}(u+x_4) \right),
\]
where $i,j=1,\ldots,n$ and $o=0,\ldots, k$. The difference in the component functions and the additional factor $|v|^{2-p}|w|^{2-p}|v-w|^{-p}$ indicate a fractional derivative of the arising products. This motivates to deduce the following general statement, which can therefore be interpreted as fractional Leibniz rule.

\begin{theorem}\label{thm:fracLeibnizrule}
	Let $m> \frac{1}{2}$, $s_1,s_2 \in [0,1]$ and $p \in (\frac 73,\frac 83)$. Then there exists a positive constant $C_L = C_L(m, p) < \infty$  such that for all $f,g \in  C^\infty(\R/\Z,\R)$
	\begin{align*}\label{eq:fracLeibnizrule}
	& \iint_D   \frac{ \left\| \left(f(\cdot+x_1) - f(\cdot+x_2) \right) \left(g(\cdot+x_3) - g(\cdot+x_4) \right) \right\|_{H^m}}{|v|^{p-2}|w|^{p-2}|v-w|^{p}}  \d v \d w \nonumber  \\
	&  \leq C_L ( \|f\|_{H^{m+ \frac 32 p -3}} \|g\|_{H^{m+ \frac 32 p -3 }} ),
	\end{align*}
	where 
	\[
	\begin{split}
	\textbf{Case 1:} & \quad (x_1,x_2,x_3,x_4) =(s_1w,s_1v, s_2w, s_2v), \\
	\textbf{Case 2:} & \quad (x_1,x_2)=(x_3,x_4) = (s_1w,s_2w), \\
	\textbf{Case 3:} & \quad (x_1,x_2)=(x_3,x_4) = (s_1v, s_2v), \\
	\textbf{Case 4:} & \quad (x_1,x_2)=(x_3,x_4) = (v+s_1(w-v), v+s_2(w-v)).
	\end{split}
	\]
\end{theorem}
\begin{proof}
	We first of all note that $H^m$ is a Banach algebra due to $m>\frac 12$ (see \eqref{prop:Banachalgebra}), which implies 
	\begin{align*}
	& \iint_D   \frac{ \left\| \left(f(\cdot+x_1) - f(\cdot+x_2) \right) \left(g(\cdot+x_3) - g(\cdot+x_4) \right) \right\|_{H^m}}{|v|^{p-2}|w|^{p-2}|v-w|^{p}}  \d v \d w \nonumber  \\
	& \leq C(m) \iint_D   \frac{ \left\| f(\cdot+x_1) - f(\cdot+x_2) \right\|_{H^m} \left\|g(\cdot+x_3) - g(\cdot+x_4) \right\|_{H^m}}{|v|^{p-2}|w|^{p-2}|v-w|^{p}}  \d v \d w \nonumber  \\
	& \leq C(m) \left(\iint_D   \frac{ \left\| f(\cdot+x_1) - f(\cdot+x_2) \right\|^2_{H^m}}{|v|^{p-2}|w|^{p-2}|v-w|^{p}}  \d v \d w \right)^{\frac 12}  \left(\iint_D   \frac{\left\|g(\cdot+x_3) - g(\cdot+x_4) \right\|^2_{H^m}}{|v|^{p-2}|w|^{p-2}|v-w|^{p}}  \d v \d w \right)^{\frac 12}
	\end{align*}
	for some positive constant $C(m)$ only depending on $m$. 
	
	
	We start with \textbf{Case 1}. We first see by the definition of the fractional Sobolev norm that
	\begin{align*}
	& \iint_D   \frac{ \left\| f(\cdot+s_1w) - f(\cdot+s_1 v) \right\|^2_{H^m}}{|v|^{p-2}|w|^{p-2}|v-w|^{p}}  \d v \d w \\
	& = \iint_D  \sum_{k\in\Z} (1+k^2)^m  |(\widehat{f(\cdot+s_1w) - f(\cdot+s_1v)})(k)|^2   \frac{\d v \d w }{|v|^{p-2}|w|^{p-2}|v-w|^{p}} .
	\end{align*}
	By substitution and the periodicity of $f$, we can rewrite the Fourier coefficients to 
	\begin{align}\label{eq:FouriercoeffCOV}
	|\widehat{\left(f(\cdot+s_1w) - f(\cdot+s_1v)\right)}(k)| & =  \left|\int_0^1 (f(u+s_1w) -  f(u+s_1v)) e^{-2\pi i k u}\d u\right| \nonumber \\
	& =  \left|e^{2\pi i k s_1 w}\right| \, \left|\int_0^1 (f(u) -  f(u+s_1(v-w))) e^{-2\pi i k u}\d u\right| \nonumber \\
	& = |(\widehat{f(\cdot+s_1(v-w))-f(\cdot)})(k)|,
	\end{align}
	which implies 
	\[
	\left\| f(\cdot+s_1w) - f(\cdot+s_1 v) \right\|_{H^m} = \left\|  f(\cdot+s_1 (v-w)) - f(\cdot)\right\|_{H^m}.
	\]
	Then, as in the proof of \cite[Lemma 4.4]{BlattReiter:2015:Menger}, respectively \cite[Lemma 1]{BlattReiter:2015:Menger}, we substitute with $\Phi:(v,w) \mapsto (t,\tilde{w}):= (\frac{v}{v-w}, s_1(v-w))$, $|\det D\Phi(v,w)| = \frac{s_1}{|v-w|}$,  $\Phi(D)\subset [0,1]\times [-1,0]$, such that
	\begin{align*}
	&\iint_D   \frac{ \left\| f(\cdot+s_1w) - f(\cdot+s_1 v) \right\|^2_{H^m}}{|v|^{p-2}|w|^{p-2}|v-w|^{p}}  \d v \d w \\
    &  = \iint_D   \frac{ \left\|  f(\cdot+s_1 (v-w)) - f(\cdot)\right\|^2_{H^m}}{|v|^{p-2}|w|^{p-2}|v-w|^{p}}  \d v \d w \\
	& \leq  s_1^{-1} \int_0^1 \int_{-1}^0 \frac{ \left\|  f(\cdot+\tilde{w}) - f(\cdot)\right\|^2_{H^m}} {|t \frac{\tilde{w}}{s_1}|^{p-2}|(t-1)\frac{\tilde{w}}{s_1}|^{p-2}|\frac{\tilde{w}}{s_1}|^{p-1}}  \d \tilde{w} \d t \\
	& = s_1^{3p-6}  \left( \int_{-1}^{0} \frac{ \left\|  f(\cdot+\tilde{w}) - f(\cdot)\right\|^2_{H^m}}{|\tilde{w}|^{3p-5}} \d \tilde{w} \right) \smash{\underbrace{\left(\int_0^1 \frac{dt}{|t(1-t)|^{p-2}} \right)}_{< \infty}}\\
	& \leq C(p)  \int_{-1}^{0} \frac{ \left\|  f(\cdot+\tilde{w}) - f(\cdot)\right\|^2_{H^m}}{|\tilde{w}|^{3p-5}} \d \tilde{w}.
	\end{align*}
	Note that the positive constant $C(p)$ in the previous estimate does not depend on $s_1$ since $3p-6 >1$ and by definition  $0\leq s_1 \leq 1$.
	
	Now we find again by the definition of the fractional Sobolev norm 
	\begin{align*}
	\int_{-1}^{0} \frac{ \left\|  f(\cdot+\tilde{w}) - f(\cdot)\right\|^2_{H^m}}{|\tilde{w}|^{3p-5}} \d \tilde{w} = \int_{-1}^{0} \sum_{k\in\Z} (1+k^2)^m |(\widehat{f(\cdot+\tilde{w}) - f(\cdot)})(k)|^2 \frac{d \tilde{w}}{|\tilde{w}|^{3p-5}},
	\end{align*}
	whose Fourier coefficients have the form
	\begin{align*}
	\left|(\widehat{f(\cdot+\tilde{w}) - f(\cdot)})(k)\right|^2 & =  \left|\int_0^1 f(u+\tilde{w}) e^{-2\pi i k u} \d u  - \int_0^1 f(u) e^{-2\pi i k u} \d u\right|^2 \\
	& = |e^{2\pi i k \tilde{w}} - 1|^2  | \hat{f}(k)|^2. 
	\end{align*}
	Since we get by Euler's formula 
	\begin{align} \label{eq:orderk}
	\begin{split}
	\int_{-1}^{0} |e^{2\pi i k \tilde{w}} - 1|^2  \frac{d \tilde{w}}{|\tilde{w}|^{3p-5}} & = 2 \int_0^1 (1-\cos(2\pi k\tilde{w}) ) \, \frac{d \tilde{w}}{\tilde{w}^{3p-5}} \\
	& \leq 2 (2\pi |k|)^{3p-6} \underbrace{\int_0^\infty \frac{1-\cos(\bar{w})}{\bar{w}^{3p-5}} \d \bar{w}}_{<\infty} \\
	& \leq \widetilde C(p)\,  |k|^{3p-6}, 
	\end{split}
	\end{align}
	for some positive constant $\widetilde C(p)$ only depending on $p$, 
	as well as  the elementary inequality 
	\begin{align}\label{eq:elementariest}
	|k|^{3p-6} \leq (1+k^2)^{\frac{3p-6}{2}}, 
	\end{align}
	we obtain together with Beppo Levi's monotone convergence theorem
	\begin{align*}
	\int_{-1}^{0} \frac{ \left\|  f(\cdot+\tilde{w}) - f(\cdot)\right\|^2_{H^m}}{|\tilde{w}|^{3p-5}} \d \tilde{w} & = \int_{-1}^{0} \sum_{k\in\Z} (1+k^2)^m | \hat{f}(k)|^2   |e^{2\pi i k w} - 1|^2\frac{d \tilde{w}}{|w|^{3p-5}} \\
	& \leq \widetilde C(p)  \sum_{k\in\Z} (1+k^2)^{m+\frac 32 p -3} | \hat{f}(k)|^2 \\
	& = \widetilde C(p) \|f\|_{H^{m+\frac 32 p -3}}^2. 
	\end{align*}
	After applying the same reasoning for the second factor, we finally achieve for \textbf{Case 1}
	\begin{align*}
	& \iint_D   \frac{ \left\| \left(f(\cdot+s_1w) - f(\cdot+s_1v) \right) \left(g(\cdot+s_2w) - g(\cdot+s_2v) \right) \right\|_{H^m}}{|v|^{p-2}|w|^{p-2}|v-w|^{p}}  \d v \d w \\
	& \leq C(m,p) \|f\|_{H^{m+\frac 32 p -3}} \|g\|_{H^{m+\frac 32 p -3}},
	\end{align*}
	for some new positive constant $C(m,p)$ depending on $m$ and $p$.

	
	In \textbf{Case 2}, we start by change of variables, cf.\ the proof of \cite[Lemma 4.4]{BlattReiter:2015:Menger}, such that
	\begin{align}\label{eq:startcase2}
	& \iint_D   \frac{ \left\| f(\cdot+s_1w) - f(\cdot+s_2w) \right\|^2_{H^m}}{|v|^{p-2}|w|^{p-2}|v-w|^{p}}  \d v \d w \nonumber \\
	& \leq \int_{0}^{\frac 23}  \frac{ \left\| f(\cdot+s_1w) - f(\cdot+s_2w) \right\|^2_{H^m}}{w^{p-2}}  \left( \int_0^{\frac 23 - w} \frac{1}{v^{p-2}(v+w)^{p}} \d v \right) \d w \nonumber \\
	& \leq \int_{0}^{\frac 23}  \frac{ \left\| f(\cdot+s_1w) - f(\cdot+s_2w) \right\|^2_{H^m}}{w^{p-2}}  \left( \int_0^{\infty} \frac{1}{(tw)^{p-2}(w(t+1))^{p}} w \d t \right) \d w\nonumber\\
	& \leq \int_{0}^{\frac 23}  \frac{ \left\| f(\cdot+s_1w) - f(\cdot+s_2w) \right\|^2_{H^m}}{w^{3p-5}} \underbrace{ \left( \int_0^{\infty} \frac{1}{t^{p-2}(1+t)^{p}} \d t \right) }_{<\infty} \d w \nonumber \\
	& \leq C (p) \int_{0}^{\frac 23}  \frac{ \left\| f(\cdot+s_1w) - f(\cdot+s_2w) \right\|^2_{H^m}}{w^{3p-5}}  \d w, 
	\end{align}
	where $C(p)$ is a positive constant depending on $p$.
	The definition of the fractional Sobolev norm gives us 
	\begin{align*}
	\int_{0}^{\frac 23}  \frac{ \left\| f(\cdot+s_1w) - f(\cdot+s_2w) \right\|^2_{H^m}}{w^{3p-5}}  \d w = \int_{0}^{\frac 23} \sum_{k\in\Z} (1+k^2)^m  |(\widehat{f(\cdot+s_1w) - f(\cdot+s_2w)})(k)|^2  \frac{dw}{w^{3p-5}}.
	\end{align*}
	We then observe for the Fourier coefficients of the series, recalling of the periodicity of $f$,
	\begin{align*}
	|(\widehat{f(\cdot+s_1w) - f(\cdot+s_2w)})(k)|^2 & =  \left|\int_0^1 f(u+s_1w) e^{-2\pi i k u}\d u - \int_0^1  f(u+s_2w)e^{-2\pi i k u}\d u\right|^2 \\
	& =  |e^{2\pi i k s_1 w} \hat{f}(k) - e^{2\pi i k s_2 w} \hat{f}(k)|^2 \\
	& = |e^{2\pi i k (s_1 -s_2)w}-1|^2 |e^{2\pi i k s_2 w}|^2 |\hat{f}(k)|^2, 
	\end{align*}
	and hence 
	\begin{align*}
	\int_{0}^{\frac 23}  \frac{ \left\| f(\cdot+s_1w) - f(\cdot+s_2w) \right\|^2_{H^m}}{w^{3p-5}}  \d w = \int_{0}^{\frac 23} \sum_{k\in\Z} (1+k^2)^m |\hat{f}(k)|^2   |e^{2\pi i k (s_1 -s_2)w}-1|^2 \frac{dw}{w^{3p-5}}.
	\end{align*}
	Now again by Euler's formula and change of variables, we get similarly to \eqref{eq:orderk}
	\begin{align*}
	\int_{0}^{\frac 23}  |e^{2\pi i k (s_1 -s_2)w}-1|^2 \frac{dw}{w^{3p-5}} & = 2 \int_{0}^{\frac 23}  1-\cos (2\pi  k (s_1 -s_2)w) \frac{dw}{w^{3p-5}} \leq \widetilde C(p) |k|^{3p-6}
	\end{align*}
    where $\widetilde C(p)$ is a positive constant depending on $p$ and we used that $\abs{s_1-s_2} \le 2$.
	Therefore, we obtain by \eqref{eq:elementariest} and Beppo Levi's monotone convergence theorem
	\begin{align}\label{eq:case2}
	\int_{0}^{\frac 23}  \frac{ \left\| f(\cdot+s_1w) - f(\cdot+s_2w) \right\|^2_{H^m}}{w^{3p-5}}  \d w & \leq \widetilde C(p)  \sum_{k\in\Z} (1+k^2)^{m+\frac 32 p -3} |\hat{f}(k)|^2  \nonumber\\
	& = \widetilde C (p) \|f\|^2_{H^{m+\frac 32 p -3}}. 
	\end{align}
	After applying the same arguments for the factor of $g$, we conclude in \textbf{Case 2}
	\begin{align*}
	& \iint_D   \frac{ \left\| \left(f(\cdot+s_1w) - f(\cdot+s_2w) \right) \left(g(\cdot+s_1w) - g(\cdot+s_2w) \right) \right\|_{H^m}}{|v|^{p-2}|w|^{p-2}|v-w|^{p}}  \d v \d w \\
	& \leq C(m,p) \|f\|_{H^{m+\frac 32 p -3}} \|g\|_{H^{m+\frac 32 p -3}}
	\end{align*}
	for some positive constant $C(m,p)$ depending on $m$ and $p$.

	\textbf{Case 3} directly follows from \textbf{Case 2}. \\
	
	Now only \textbf{Case 4} remains. Along the lines of \textbf{Case 1} and \textbf{Case 2}, in particular \eqref{eq:FouriercoeffCOV} and \eqref{eq:startcase2}, we transform with respect of the Fourier coefficients 
	\begin{align*}
	& \iint_D   \frac{ \left\| f(\cdot+v+s_1(w-v)) - f(\cdot+v+s_2(w-v)) \right\|^2_{H^m}}{|v|^{p-2}|w|^{p-2}|v-w|^{p}}  \d v \d w \\
	& \le \int_0^{2/3} \, \int_0^{2/3-w} \frac{ \left\| f(\cdot+s_1(w+v)) - f(\cdot+s_2(w+v)) \right\|^2_{H^m}}{|w|^{p-2}} \left(  \frac{1}{v^{p-2}(v+w)^p} \right) \d v  \d w \\
	& \leq \int_{0}^{2/3}  \frac{ \left\| f(\cdot+s_1\tilde{w}) - f(\cdot+s_2\tilde{w}) \right\|^2_{H^m}}{\tilde{w}^{3p-5}}  \underbrace{\left( \int_0^{\infty} \frac{1}{t^{p-2}(1+t)^{p}} \d t \right)}_{<\infty} \d \tilde{w}.
	\end{align*}
	We are now in the position to apply \eqref{eq:case2} and the statement for \textbf{Case 4}
	\begin{align*}
	& \iint_D   \left\| \left(f(\cdot+v + s_1(w-v)) - f(\cdot+v + s_1(w-v)) \right) \cdot\right.\\
    & \qquad \left.\cdot \left(g(\cdot+v + s_1(w-v)) - g(\cdot+v + s_1(w-v)) \right) \right\|_{H^m} \frac {\d v \d w} {|v|^{p-2}|w|^{p-2}|v-w|^{p}}  \\
	& \leq C(m,p) \|f\|_{H^{m+\frac 32 p -3}} \|g\|_{H^{m+\frac 32 p -3}}
	\end{align*}
	for some positive constant $C(m,p)$ only dependent on $m$ and $p$
	follows. 
\end{proof}





\subsection{Estimate of the remainder term \texorpdfstring{$\Rpt$}{R(p)}} 





We may find an estimate for of $\partial^l \Rpt(\gamma)$ with respect to a fractional Sobolev norm.
\begin{lemma}
    \label{lemma:estimateRemainder}
    Let $\gamma \in C^\infty(\R/\Z,\R^n)$ be parametrized by arc-length and $m > \tfrac 12$.
    Then there exist constants $C=C(\gamma,m,n,p)>0$ and
     $r= r(\gamma,m,n,p)>0$  such that
    \begin{align*}
    	& \norm[H^m]{\partial^l \Rpt(\gamma)} \\
    	& \leq C \sum_{j_1 + \ldots + j_{K-1} = l+1} \binom{l+1}{j_1, \ldots, j_{K-1}} \ p^{(3n)}_{j_1} \left( \left\{\frac{(|\alpha|+1)!}{r^{|\alpha|+1}} \right\}_{|\alpha|\leq j_1}, \{ \| \gamma^{(j+1)} \|_{H^{m+ \frac 32 p -3}}\}_{\substack{j =1, \ldots, j_1\\ i = 1, \ldots, 3n}} \right) \\
    	& \phantom{\le} \cdot \prod_{i=2}^{K-1} {\|\gamma^{(j_i+1)}\|_{H^{m+ \frac 32 p -3}}}.
    \end{align*}
    Note that the second set of coefficients of $p^{(3n)}_{j_1}$ is independent of $i$, we need that parameter only for dimensional reasons.
\end{lemma}

\begin{proof}
	First note that $\Gp \circ |.|$ is an analytic function away from zero and by the fundamental theorem of calculus 
	\[
	\begin{split}
		&\Gp\left(\frac {|\difference{v,w} \gamma|} {|v-w|}, \frac {|\difference{v,0} \gamma|} {|v|}, \frac {|\difference{w,0} \gamma|} {|w|} \right)\\
        &= (\Gp \circ |.|) \left(\int_0^1 \gamma'(u+tw)\d t, \int_0^1 \gamma'(u+tv)\d t, \int_0^1 \gamma'(u+t(w-v))\d t \right).
	\end{split}
	\]
	Now by the generalized Leibniz formula and Faà di Bruno's formula as in \thref{lem:FaadiBruno}, we observe
	\[
	\begin{split}
	& \frac {\d^{l+1}} {\d u^{l+1}} g_k^p(u,v,w;s_1, \ldots, s_{K-2})
	\\
	& = \sum_{k_1 + \ldots + k_{K-2} = l+1} \binom{l+1}{k_1, \ldots, k_{K-2}}
	\\
	&\cdot p^{(3n)}_{k_1}\Biggl(
	\set*{ \partial^\alpha (\Gp \circ |. |) \left(\int_0^1 \gamma'(u+tw)\d t, \int_0^1 \gamma'(u+tv)\d t, \int_0^1 \gamma'(u+t(w-v))\d t \right)}_{\abs{\alpha}\leq k_1}, 
	\\
	& \qquad 
	\left\{ \int_0^1 \gamma^{(j+1)}_i (u+t(x-y)) \d t \right\}_{\substack{i=1,\ldots,n, \, j =1, \ldots, k_1 ,\\ (x,y) = (v,w), (v,0), (w,0)}} \Biggr)
	\\
	& \cdot  \frac {\d^{k_2}} {\d u^{k_2}} \Gamma(u,v,w,s_1,s_2)  \\
	& \cdot  \left( \bigotimes_{i=3}^{K_1} \gamma^{(k_i + 1)}(u+ s_i v) \right) \otimes \left(\bigotimes_{i=K_1 +1}^{K_2} \gamma^{(k_i + 1)}(u + s_i w) \right) \otimes \left(\bigotimes_{i=K_2 +1}^{K-2} \gamma^{(k_i + 1)}(u+v + s_i (w-v)) \right).
	\end{split}
	\]
	We then apply the $H^m$-norm on $\partial^l \Rpt(\gamma)$ for some $m> \tfrac 12$ and obtain by the Banach algebra property of $H^m (\R/\Z, \R^n)$, cf. \eqref{prop:Banachalgebra},  together with \thref{lemma:estimateFaaDiBrunoBanachAlgebra} that 
	\[
    \numberthis
    \label{lemma:estimateRemainder:eq:firstStep}
	\begin{split}
	& \left\| \partial^l \Rpt(\gamma) \right\|_{H^m}
	\\
	& \leq c(m,n,p) \sum_{k=1}^{k_{\max}} \iint_{D} \idotsint\limits_{[0,1]^K} \left\| \partial^{l+1} g_k^p(\cdot,v,w;s_1, \ldots, s_{K-2})\right\|_{H^m} \d\theta_{1}\cdots\d\theta_{K}\d v \d w
	\\
	& \leq \tilde c(m,n,p,K)   \sum_{k=1}^{k_{\max}} \iint_{D} \idotsint\limits_{[0,1]^K}  \sum_{k_1 + \ldots + k_{K-2} = l+1} \binom{l+1}{k_1, \ldots, k_{K-2}}
	\\
	&\cdot p^{(3 n)}_{k_1}\Biggl(\!
	\set*{b^{\abs{\alpha}} \norm*[H^m]{\partial^\alpha (\Gp \circ |.|) \left(\int_0^1 \gamma'(\cdot+tw)\d t, \int_0^1 \gamma'(\cdot+tv)\d t, \int_0^1 \gamma'(\cdot+t(w-v))\d t  \right)}}_{\hspace{-0.4em}\abs{\alpha}\leq k_1}\hspace{-2em},
	\\
	& \qquad 
	\left\{ \left\| \int_0^1 \gamma^{(j+1)}_i (\cdot+t(x-y)) \d t \right\|_{H^m}\right\}_{\substack{i=1,\ldots,n, \, j =1, \ldots, k_1 ,\\ (x,y) = (v,w), (v,0), (w,0)}} \Biggr)
	\\
	& \cdot \left\|\partial^{k_2}\Gamma(\cdot,v,w,s_1,s_2) \right\|_{H^m}
	\cdot \prod_{i=3}^{K-2} \norm*[H^m]{\gamma^{(k_i+1)}} \d\theta_{1}\cdots\d\theta_{K}\d v \d w
	\end{split}
	\]
    where $b = b(m) := \sup_{\eta_1,\eta_2 \in H^m(\R/\Z,\R)} \frac {\norm[H^m]{\eta_1}\norm[H^m]{\eta_2}} {\norm[H^m]{\eta_1\eta_2}}$ is a finite constant stemming from the Banach algebra property  and $c(n,m,p)$ is an upper bound for the operator norms of $\cdot \otimes e_o : H^m(\R/\Z,\R^n) \to H^m(\R/\Z,\R^n)$.
    
	Since $G^{(p)}\circ |.|$ is an analytic function away from the origin and $\gamma$ is smooth with bounded bilipschitz constant \cite[Proposition~2.1]{BlattReiter:2015:Menger},
	 we get from the proof of \cite[Lemma~7.2]{BlattVorderobermeier:2019:CriticalMoebius} that 
	$$
	b^{\abs{\alpha}}\norm*[H^m]{\partial^\alpha (\Gp \circ |.|) \left(\int_0^1 \gamma'(\cdot+tw)\d t, \int_0^1 \gamma'(\cdot+tv)\d t, \int_0^1 \gamma'(\cdot+t(w-v))\d t  \right)} 
	\leq C_{G}  \frac{(|\alpha|+1)!}{r^{|\alpha|+1}}
	$$
	for some positive constants $C_{G} = C_{G} (\gamma, m, n, p)$ and $r= r(\gamma,m,n,p)$ which also absorb $b$. Furthermore, we have by the triangle inequality
	\[
		\left\| \int_0^1 \gamma^{(j+1)}_i (\cdot+t(x-y)) \d t \right\|_{H^m} \leq \| \gamma^{(j+1)}_i \|_{H^m} \leq  \| \gamma^{(j+1)} \|_{H^m}.
	\]
	Note that these bounds are independent of $s_3, \ldots, s_{K-2}$.
	
	To estimate the term $\iint_D \iint_{[0,1]^2} \left\| \partial^{k_2} \Gamma(\cdot,v,w,s_1,s_2) \right\|_{H^m} \d \theta_1 \d \theta_2 \d w \d v$, we first observe by the generalized Leibniz rule
	\[
	\begin{split}
		& \frac {\d^{k_2}} {\d u^{k_2}} \Gamma(u,v,w,s_1,s_2)  = \frac{1}{|v|^{p-2}|w|^{p-2}|v-w|^{p}} \\
		& \cdot \sum_{o=0}^{k_2} \binom{k_2}{o} \left(\gamma^{(k_2-o+1)}(u+x_1) - \gamma^{(k_2-o+1)}(u+x_2) \right) \otimes \left( \gamma^{(o+1)}(u+x_3) - \gamma^{(o+1)}(u+x_4) \right),
	\end{split}
	\]
	where we have the four cases 
	\[
	\begin{split}
	\textbf{Case 1:} & \quad (x_1,x_2,x_3,x_4) =(s_1w,s_1v, s_2w, s_2v), \\
	\textbf{Case 2:} & \quad (x_1,x_2)=(x_3,x_4) = (s_1w,s_2w), \\
	\textbf{Case 3:} & \quad (x_1,x_2)=(x_3,x_4) = (s_1v, s_2v), \\
	\textbf{Case 4:} & \quad (x_1,x_2)=(x_3,x_4) = (v+s_1(w-v), v+s_2(w-v)).
	\end{split}
	\]
	Hence we get by \thref{thm:fracLeibnizrule} 
	\[
	\begin{split}
	&\iint_{[0,1]^2} \iint_D  \left\| \partial^{k_2} \Gamma(\cdot,v,w,s_1,s_2) \right\|_{H^m}  \d w \d v \d \theta_1 \d \theta_2  \\
	& \leq C(m,n,p) \sum_{i=1}^n \sum_{j=1}^n \sum_{o=0}^{k_2} \binom{k_2}{o} \iint_{[0,1]^2} \iint_D  \frac{1}{|v|^{p-2}|w|^{p-2}|v-w|^{p}} \\
	& \cdot \norm[H^m]{\gamma_i^{(k_2-o+1)}(\cdot +x_1) - \gamma_i^{(k_2-o+1)}(\cdot +x_2)} \norm[H^m]{\gamma_j^{(o+1)}(\cdot+x_3) - \gamma_j^{(o+1)}(\cdot +x_4)} \d w \d v \d \theta_1 \d \theta_2\\
	& \leq \widetilde C(m,n,p) \sum_{i=1}^n \sum_{j=1}^n \sum_{o=0}^{k_2} \binom{k_2}{o} \iint_{[0,1]^2} \| \gamma_i^{(k_2-o+1)}\|_{H^{m+ \frac 32 p -3}} \|\gamma_j^{(o+1)}\|_{H^{m+ \frac 32 p -3 }}  \d \theta_1 \d \theta_2 \\
	& \leq \widetilde C(m,n,p) \sum_{o=0}^{k_2} \binom{k_2}{o} \| \gamma^{(k_2-o+1)}\|_{H^{m+ \frac 32 p -3}} \|\gamma^{(o+1)}\|_{H^{m+ \frac 32 p -3 }}
	\end{split}
	\]
    where $C(m,n,p)$ is an upper bound for the operator norms of $e_i\otimes e_j$ on $(H^m(\R/\Z,\R))^2$.
    We may combine the sum over $o$ and the binomial coefficient $\binom{k_2}{o}$ with the sum over $k_1, \ldots, k_{K-2}$ and the multinomial coefficient $\binom{l+1}{k_1,\ldots,k_{K-2}}$ from \eqref{lemma:estimateRemainder:eq:firstStep} into the sum over $j_1 + \ldots + j_{K-1}$ and the multinomial coefficient $\binom{l+1}{j_1, \ldots, j_{K-1}}$ by setting $j_2 := o$, $j_{K-1} := k_2-o$ and $j_i := k_i$ for all other $i$.
    This allows us to integrate the two derivatives of $\gamma$ into the bigger product.
    
    Then, the
	statement follows from the embedding $H^s(\R/\Z,\C^n) \subseteq H^t(\R/\Z,\C^n)$ for any $s>t$, $s,t \geq 0$. 
    Since these estimates are uniform over all $g_k$, we may use an additional factor of $k_{\max}$ in order to leave out the sum.
\end{proof}
Note that $\Gamma$ is the only term for whose upper bound we need the higher-order $H^{m+\frac 3 2 p -3}$-norms.
We estimated all $H^m$-norms by these in order to get a simpler structure which will serve us in the proof of the main theorem, especially in \thref{lemma:iteratedEstimateMainTerm}.

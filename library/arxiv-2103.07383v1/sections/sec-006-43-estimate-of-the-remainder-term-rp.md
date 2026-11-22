---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-006-43-estimate-of-the-remainder-term-rp
section_title: "Estimate of the remainder term R(p)"
section_number: 4.3
pages: 15-18
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.991
doc_brief: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case — We prove the analyticity of smooth critical points for generalized integral Menger cur- vature"
---
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

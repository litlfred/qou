---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG"
section_id: sec-007-15-acknowledgements
section_title: "Acknowledgements"
section_number: 1.5
pages: 7-13
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
doc_brief: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG — In this paper, we study the asymptotics of the colored Jones polynomials of the Whitehead chains with one belt colored by"
text_source: latex
latex_prose_ratio: 0.748
latex_coverage_ratio: 0.987
---
The author would like to thank Tian Yang for the valuable comments and suggestions to this work.

# Asymptotics of $J_{M_1,M_2}(WL,e^{\frac{2\pi i}{N+\frac{1}{2}}})$ {#formula}

## Potential functions of $J_{M_1,M_2}(WL,e^{\frac{2\pi i}{N+\frac{1}{2}}})$

In this section, we compute the potential function of the $(M_1,M_2)$-th unnormalized colored Jones polynomials for the Whitehead link $WL$, where $M_1,M_2$ are sequences of positive integers in $N$. First of all, the formula of the $(M_1,M_2)$-th unnormalized colored Jones polynomials of the Whitehead link is given by [@HZ07] $$J_{M_1,M_2} (WL, t) = t^{\frac{M_2^2-1}{2}} (t^{\frac{1}{2}}-t^{-\frac{1}{2}})^{-1}\sum_{n=0}^{M_2-1} (t^{\frac{M_1(2n+1)}{2}}-t^{-\frac{M_1(2n+1)}{2}})  \cdot \tilde{C}(n,t; M_2) ,$$ where $$\tilde{C}(n,t; M_2) = t^{\frac{M_2(M_2-1)}{2}} \sum_{l = 0}^{M_2-1-n} t^{-M_2(l+n)} \prod_{j=1}^{n} \frac{(1-t^{M_2-l-j})(1-t^{l+j})}{1-t^j}.$$ Put $t = e^{\frac{2\pi i}{N+\frac{1}{2}}}$. By direct computation, we have $$\begin{aligned}
\label{t0}
 (t^{\frac{1}{2}}-t^{-\frac{1}{2}})^{-1} = \frac{1}{2i\sin\left(\frac{\pi}{N+\frac{1}{2}}\right)}
\end{aligned}$$ $$\begin{aligned}
 t^{\frac{M_1(2n+1)}{2}}-t^{-\frac{M_1(2n+1)}{2}} 
&= t^{\frac{(N+\frac{1}{2})(2n+1)}{2} + \frac{(M_1 - (N+\frac{1}{2}))(2n+1)}{2}} - t^{-\frac{(N+\frac{1}{2})(2n+1)}{2} - \frac{(M_1 - (N+\frac{1}{2}))(2n+1)}{2}}  \notag \\
&= -\left[ e^{2\pi i(\frac{M_1}{N+\frac{1}{2}} -1) (n+\frac{1}{2})} - e^{-2\pi i (\frac{M_1}{N+\frac{1}{2}} -1)(n+\frac{1}{2})} \right]  \notag \\
&= -\left[ e^{\pi i\left(\frac{M_1}{N+\frac{1}{2}}-1\right)}e^{2\pi i\left(\frac{M_1}{N+\frac{1}{2}} -1\right) (n)} - e^{-\pi i\left(\frac{M_1}{N+\frac{1}{2}}-1\right)}e^{-2\pi i \left(\frac{M_1}{N+\frac{1}{2}} -1\right)(n)} \right]  \notag \\
&= (-1)^{M_1 - N}i\left[ e^{\pi i\left(\frac{M_1}{N+\frac{1}{2}}-1\right)}e^{\frac{N+\frac{1}{2}}{2\pi i}\left[(2\pi i)\left(\frac{M_1}{N+\frac{1}{2}} -1\right)\right] \left[2\pi i \left(\frac{n}{N+\frac{1}{2}}-\frac{1}{2}\right)\right]} \right. \notag\\
&\qquad\qquad\qquad\qquad\qquad \left. + e^{-\pi i\left(\frac{M_1}{N+\frac{1}{2}}-1\right)}e^{-\frac{N+\frac{1}{2}}{2\pi i}\left[(2\pi i)\left(\frac{M_1}{N+\frac{1}{2}} -1\right)\right] \left[2\pi i \left(\frac{n}{N+\frac{1}{2}}-\frac{1}{2}\right)\right]} \right]
\label{t1}
\end{aligned}$$ Besides, $$\begin{aligned}
t^{\frac{M_2^2 - 1}{2} + \frac{M_2(M_2-1)}{2}}
&= e^{\frac{2\pi i}{N+\frac{1}{2}}(M_2^2 - \frac{M_2}{2} - \frac{1}{2})} 
\\\notag\\
t^{-M_2(l+n)} 
&=  e^{-2\pi i (\frac{M_2}{N+\frac{1}{2}}-1) (l+n)} \notag \\
&= e^{- \frac{N+\frac{1}{2}}{2\pi i} \left[ 2\pi i \left(\frac{M_2}{N+\frac{1}{2}} -1 \right) \left[ 2\pi i \left(\frac{l}{N+\frac{1}{2}}\right) + 2\pi i \left( \frac{n}{N+\frac{1}{2}}\right) \right] \right]} \label{t5}
\end{aligned}$$ Next, for any odd integer $r=2N+1\geq 3$, we consider the following version of the quantum dilogarithm function $\varphi_r(z)$ (see [@F95; @FKV01], or Section 2.3 in [@WY20] for a review of its properties) defined by $$\begin{aligned}
\varphi_r (z) = \frac{4\pi i}{r}\int_\Omega \frac{e^{(2z - \pi)x} }{4x \sinh(\pi x) \sinh (\frac{2\pi x}{r} )} dx,
\end{aligned}$$ where $$\begin{aligned}
\Omega = (-\infty, - \epsilon] \cup \{ z \in {\mathbb C}\mid |z| = \epsilon, \im z >0\} \cup [ \epsilon, \infty)
\end{aligned}$$ for some $\epsilon \in (0,1)$ and $$\begin{aligned}
z \in \left\{ z \in {\mathbb C}\left\vert - \frac{\pi}{2N+1} < \Re z < \pi + \frac{\pi}{2N+1}\right. \right\}
\end{aligned}$$ For any $z \in {\mathbb C}$ with $0 < \Re z < \pi$, the quantum dilogarithm function satisfies the functional equation (Lemma 2.1)1) in [@WY20]) $$\begin{aligned}
1 - e^{2i z} = \exp \left(\frac{N+\frac{1}{2}}{2\pi i}\left( \varphi_r \left( z - \frac{\pi }{2N+1} \right) - \varphi_r \left( z + \frac{\pi }{2N+1} \right) \right)\right)
\end{aligned}$$ Furthermore, let $\Li: {\mathbb C}\backslash (1,\infty) \to {\mathbb C}$ be the dilogartihm function defined by $$\Li(z) = - \int_0^z \frac{\log(1-u)}{u} du$$ For any $z$ with $0<\Re z < \pi$, the quantum dilogarithm function satisfies (Lemma 2.3 in [@WY20]) $$\begin{aligned}
\varphi_r (z) = \Li(e^{2iz}) + \frac{2\pi^2 e^{2iz}}{3(1-e^{2iz})} \frac{1}{(2N+1)^2} + O\left(\frac{1}{(N+\frac{1}{2})^3}\right) \label{QtoC},
\end{aligned}$$ and as $N \to \infty$, $\varphi_r(z)$ uniformly converges to $\Li(e^{2iz})$ on any compact subset of $\{z \in {\mathbb C}\mid 0 < \Re z < \pi \}$.

Using the functional equation of the quantum dilogarithm function, we have $$\begin{aligned}
 \prod_{j=1}^{n} (1-t^{M_2-l-j}) 
=&\prod_{j=1}^n \left(1 - e^{2\pi i \left(\frac{M_2}{N+\frac{1}{2}} - \frac{l}{N+\frac{1}{2}} - \frac{j}{N+\frac{1}{2}}\right)}\right)\notag \\
=&\exp\left(\frac{N+\frac{1}{2}}{2\pi i} \sum_{j=1}^n \left( \varphi_r \left(\frac{M_2 \pi }{N+\frac{1}{2}} - \frac{l\pi}{N+\frac{1}{2}} - \frac{(j+\frac{1}{2})\pi}{N+\frac{1}{2}}\right) \right. \right.\notag\\
&\left. \left.\qquad - \varphi_r\left( \frac{M_2\pi}{N+\frac{1}{2}} - \frac{l\pi}{N+\frac{1}{2}} - \frac{(j-\frac{1}{2})\pi}{N+\frac{1}{2}}\right)  \right) \right) \notag\\
=& \exp \left(\frac{N+\frac{1}{2}}{2\pi i} \left(\varphi_r \left( \frac{M_2\pi}{N+\frac{1}{2}} - \frac{l\pi}{N+\frac{1}{2}} - \frac{n\pi}{N+\frac{1}{2}} - \frac{\pi}{2N+1}\right) \right.\right.\notag\\
&\left.  \left.\qquad - \varphi_r\left(\frac{M_2\pi}{N+\frac{1}{2}} - \frac{l\pi}{N+\frac{1}{2}} - \frac{\pi}{2N+1}\right)  \right)  \right)\label{t6}
\end{aligned}$$ $$\begin{aligned}
 \prod_{j=1}^{n} (1-t^{l+j})
=&\prod_{j=1}^n \left(1 - e^{2\pi i \left(\frac{l}{N+\frac{1}{2}} + \frac{j}{N+\frac{1}{2}}\right)}\right)\notag \\
=&\exp\left(\frac{N+\frac{1}{2}}{2\pi i} \sum_{j=1}^n \left( \varphi_r \left(\frac{l\pi}{N+\frac{1}{2}} + \frac{(j-\frac{1}{2})\pi}{N+\frac{1}{2}}\right)  - \varphi_r\left( \frac{l\pi}{N+\frac{1}{2}} + \frac{(j+\frac{1}{2})\pi}{N+\frac{1}{2}}\right)  \right) \right)\notag \\
=&\exp\left(\frac{N+\frac{1}{2}}{2\pi i} \left( \varphi_r \left(\frac{l\pi}{N+\frac{1}{2}} + \frac{\pi}{2N+1}\right)  - \varphi_r\left( \frac{l\pi}{N+\frac{1}{2}} + \frac{n\pi}{N+\frac{1}{2}}+\frac{\pi}{2N+1}\right)  \right) \right)\label{t7}
\\ \notag\\
 \prod_{j=1}^{n} (1-t^{j})
=&\prod_{j=1}^n \left(1 - e^{2\pi i \left(\frac{j}{N+\frac{1}{2}}\right)}\right) \notag\\
=&\exp\left(\frac{N+\frac{1}{2}}{2\pi i} \left(\sum_{j=1}^n \left( \varphi_r \left( \frac{(j-\frac{1}{2})\pi}{N+\frac{1}{2}}\right)  - \varphi_r\left( \frac{(j+\frac{1}{2})\pi}{N+\frac{1}{2}}\right)  \right) \right)\right)\notag \\
=&\exp\left(\frac{N+\frac{1}{2}}{2\pi i} \left( \varphi_r \left(  \frac{\pi}{2N+1}\right)  - \varphi_r\left( \frac{n\pi}{N+\frac{1}{2}} + \frac{\pi}{2N+1}\right)   \right) \right) \label{t8}
 
\end{aligned}$$

Altogether, by ([\[t0\]](#t0){reference-type="ref" reference="t0"}) - ([\[t8\]](#t8){reference-type="ref" reference="t8"}), we have $$\begin{aligned}
&\quad J_{M_1, M_2} (WL, e^{\frac{2\pi i}{N+\frac{1}{2}}}) \notag \\
&=  \frac{ (-1)^{(M_1 - N) }  e^{\frac{2\pi i}{N+\frac{1}{2}}(M_2^2 - \frac{M_2}{2} - \frac{1}{2})}}{2\sin(\frac{\pi}{N+\frac{1}{2}})} \notag \\
&\qquad \times \sum_{n=0}^{M_2-1} 
\left[ e^{\pi i\left(\frac{M_1}{N+\frac{1}{2}}-1\right)}e^{\frac{N+\frac{1}{2}}{2\pi i}\left[(2\pi i)\left(\frac{M_1}{N+\frac{1}{2}} -1\right)\right] \left[2\pi i \left(\frac{n}{N+\frac{1}{2}}-\frac{1}{2}\right)\right]} \right. \notag\\
&\qquad\qquad\qquad\qquad\qquad \left. + e^{-\pi i\left(\frac{M_1}{N+\frac{1}{2}}-1\right)}e^{-\frac{N+\frac{1}{2}}{2\pi i}\left[(2\pi i)\left(\frac{M_1}{N+\frac{1}{2}} -1\right)\right] \left[2\pi i \left(\frac{n}{N+\frac{1}{2}}-\frac{1}{2}\right)\right]} \right] \notag \\
&\qquad  \times \sum_{l=0}^{M_2-1-n}   e^{- \frac{N+\frac{1}{2}}{2\pi i} \left[ 2\pi i \left(\frac{M_2}{N+\frac{1}{2}} -1 \right) \left[ 2\pi i \left(\frac{l}{N+\frac{1}{2}}\right) + 2\pi i \left( \frac{n}{N+\frac{1}{2}}\right) \right] \right]} \notag\\ 
&\qquad \times \exp\left(\frac{N+\frac{1}{2}}{2\pi i} \left(\varphi_r \left(\frac{M_2\pi}{N+\frac{1}{2}} - \frac{l\pi}{N+\frac{1}{2}} - \frac{n\pi}{N+\frac{1}{2}} - \frac{\pi}{2N+1}\right)\right. \right. \notag\\
&\qquad\qquad\qquad  - \varphi_r\left(\frac{M_2\pi}{N+\frac{1}{2}} - \frac{l\pi}{N+\frac{1}{2}} - \frac{\pi}{2N+1}\right) \notag \\
&\qquad\qquad\qquad  + \varphi_r \left(\frac{l\pi}{N+\frac{1}{2}} + \frac{\pi}{2N+1}\right)  - \varphi_r\left( \frac{l\pi}{N+\frac{1}{2}} + \frac{n\pi}{N+\frac{1}{2}} + \frac{\pi}{2N+1}\right) \notag\\
&\left.\left.\qquad\qquad\qquad  - \varphi_r \left(  \frac{\pi}{2N+1}\right)  + \varphi_r\left( \frac{n\pi}{N+\frac{1}{2}} + \frac{\pi}{N+\frac{1}{2}}\right) \right)\right) 
\end{aligned}$$ Define the limiting ratio $s_1$ and $s_2$ by $$s_1 = \lim_{N \to \infty} \frac{M_1}{N+\frac{1}{2}} \quad\text{ and }\quad s_2 = \lim_{N \to \infty} \frac{M_1}{N+\frac{1}{2}},$$ Then we have $$\begin{aligned}
J_{M_1, M_2} (WL, e^{\frac{2\pi i}{N+\frac{1}{2}}}) 
&=  \frac{ (-1)^{(M_1 - N) }  e^{\frac{2\pi i}{N+\frac{1}{2}}(M_2^2 - \frac{M_2}{2} - \frac{1}{2})}}{2\sin(\frac{\pi}{N+\frac{1}{2}})} \exp\left(  -\varphi_r \left(  \frac{\pi}{2N+1}\right)\right)
 (I_+ + I_-)
\end{aligned}$$ where $$\begin{aligned}
I_\pm =
& e^{\pm\pi i \left(\frac{M_2}{N+\frac{1}{2}} - 1\right) }\sum_{n=0}^{M_2-1} \sum_{l=0}^{M_2-1-n} \exp\left( \left(N+\frac{1}{2}\right)\Phi^{\pm(s_1, s_2)}_{M_1, M_2} \left(\frac{n}{N+\frac{1}{2}},\frac{l}{N+\frac{1}{2}}\right) \right)
\end{aligned}$$ with $$\begin{aligned}
\Phi^{\pm(s_1, s_2)}_{M_1, M_2} (z_1,z_2) 
&= \frac{1}{2\pi i}\left\{ \pm \left(2\pi i \left(\frac{M_1}{N+\frac{1}{2}} - 1\right)\right) \left(2\pi i \left(z_1 -\frac{1}{2} \right)\right) \right. \notag \\
&\qquad \left.  - \left(2\pi i \left(\frac{M_2}{N+\frac{1}{2}} - 1\right)\right)(2\pi i z_1 + 2\pi i z_2) \right. \notag \\
&\qquad  + \left[\varphi_r \left( \frac{M_2\pi}{N+\frac{1}{2}}  - \pi z_1 - \pi z_2 -\frac{\pi}{2N+1}\right) \right.  \notag\\
&\qquad  - \varphi_r\left(  \frac{M_2\pi}{N+\frac{1}{2}} - \pi z_2- \frac{\pi}{2N+1}\right) \notag \\
&\qquad  + \varphi_r \left(\pi z_2 + \frac{\pi}{2N+1}\right)  - \varphi_r\left( \pi z_1 + \pi z_2 + \frac{\pi}{2N+1}\right) \notag\\
&\left.\left.\qquad  + \varphi_r\left( \pi z_1 + \frac{\pi}{2N+1}\right) \right] \right\}
\end{aligned}$$ defined on $\left\{ (z_1,z_2) \in {\mathbb C}\mid 0 \leq \Re z_1 , \Re z_2 \leq \pi, \Re z_1 + \Re z_2 < \frac{M_2}{N+\frac{1}{2}} \right\}$. Take $N\to \infty$, we obtain the potential functions $$\begin{aligned}
\Phi^{\pm(s_1, s_2)} (z_1,z_2) 
&=  \frac{1}{2\pi i} \left[ \pm \left(2\pi i \left( s_1 - 1\right)\right) \left(2\pi i \left(z_1 -\frac{1}{2} \right)\right)  - (2\pi i (s_2-1))(2\pi i z_1 + 2\pi i z_2)  \right. \\
&\qquad + \Li\left(e^{2\pi i (s_2-1) - 2\pi i z_1 - 2\pi i z_2}\right) - \Li\left( e^{2\pi i (s_2-1) - 2\pi i z_2 }\right) \\
&\qquad \left.+ \Li \left(e^{2\pi i z_2}\right) - \Li\left(e^{2\pi iz_1+ 2\pi i z_2}\right) + \Li\left(e^{2\pi i z_1}\right)  \right]
\end{aligned}$$ defined on $\left\{ (z_1,z_2) \in {\mathbb C}\mid \Re z_1 , \Re z_2 >0, \Re z_1 + \Re z_2 < s_2 \right\}$.

The following lemma estimates the difference between $\Phi^{\pm(s_1, s_2)}_{M_1, M_2} (z_1,z_2)$ and $\Phi^{\pm\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} (z_1,z_2)$.

::: lemma
[]{#EM_2 label="EM_2"} On any compact subset of $\left\{ (z_1,z_2) \in {\mathbb C}\mid \Re z_1 , \Re z_2 >0, \Re z_1 + \Re z_2 < s_2 \right\}$, $$\begin{aligned}
\Phi^{\pm(s_1,s_2)}_{M_1,M_2}(z_1, z_2 )
= \Phi^{\pm\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} (z_1,z_2) +\frac{1}{N+\frac{1}{2}}E_{M_2}(z_1,z_2) + O\left(\frac{1}{\left(N+\frac{1}{2}\right)^2}\right),
\end{aligned}$$ where $$\begin{aligned}
E_{M_2}(z_1,z_2) 
&= \frac{1}{2}\left[ \log\left(1-e^{2\pi i \left(\frac{M_2}{N+\frac{1}{2}}-1\right) - 2\pi i z_1 - 2\pi i z_2 }\right)
- \log\left(1-e^{2\pi i \left(\frac{M_2}{N+\frac{1}{2}}-1\right) - 2\pi i z_2 } \right) \right.\notag\\
&\left.\qquad - \log\left(1- e^{2\pi i z_2 } \right)
+ \log\left(1- e^{2\pi iz_1+ 2\pi i z_2} \right) 
- \log\left(1-  e^{2\pi i z_1 } \right) \right]
\end{aligned}$$
:::

::: proof
*Proof.* From ([\[QtoC\]](#QtoC){reference-type="ref" reference="QtoC"}), we have $$\begin{aligned}
&\Phi^{+(s_1,s_2)}_{M_1,M_2}(z_1, z_2 ) \notag\\
&=  \frac{1}{2\pi i} \left[ \pm \left(2\pi i \left( \frac{M_1}{N+\frac{1}{2}} - 1\right)\right) \left(2\pi i \left(z_1 -\frac{1}{2} \right)\right)  - \left(2\pi i \left(\frac{M_2}{N+\frac{1}{2}}-1\right)\right)(2\pi i z_1 + 2\pi i z_2)  \right. \notag\\
&\qquad + \Li\left(e^{2\pi i \left(\frac{M_2}{N+\frac{1}{2}}-1\right) - 2\pi i z_1 - 2\pi i z_2 - \frac{\pi i}{N+\frac{1}{2}}}\right) - \Li\left( e^{2\pi i \left(\frac{M_2}{N+\frac{1}{2}}-1\right) - 2\pi i z_2 - \frac{\pi i}{N+\frac{1}{2}}}\right) \notag\\
&\qquad \left.+ \Li \left(e^{2\pi i z_2 + \frac{\pi i}{N+\frac{1}{2}}}\right) - \Li\left(e^{2\pi iz_1+ 2\pi i z_2 + \frac{\pi i}{N+\frac{1}{2}}}\right) + \Li\left(e^{2\pi i z_1 + \frac{\pi i}{N+\frac{1}{2}}}\right)  \right] + O\left(\frac{1}{(N+\frac{1}{2})^2}\right)
\end{aligned}$$ By considering the Talyor series expansion of $\Li\left(e^{2\pi i \left(\frac{M_2}{N+\frac{1}{2}}-1\right) - 2\pi i z_1 - 2\pi i z_2 + v}\right)$ with respect to $v$, we have $$\begin{aligned}
&\Li\left(e^{2\pi i \left(\frac{M_2}{N+\frac{1}{2}}-1\right) - 2\pi i z_1 - 2\pi i z_2 - \frac{\pi i}{N+\frac{1}{2}}}\right) \notag\\
&= \Li\left(e^{2\pi i \left(\frac{M_2}{N+\frac{1}{2}}-1\right) - 2\pi i z_1 - 2\pi i z_2}\right)+\frac{\pi i}{N+\frac{1}{2}}\log\left(1-e^{2\pi i \left(\frac{M_2}{N+\frac{1}{2}}-1\right) - 2\pi i z_1 - 2\pi i z_2}\right)
+  O\left(\frac{1}{(N+\frac{1}{2})^2}\right)
\end{aligned}$$ The result follows by applying the same argument to all the dilogarithm terms. ◻
:::

## The asymptotics expansion formula for $J_{N,N}(WL, e^{\frac{2\pi i}{N+\frac{1}{2}}})$ {#WLNN}

Next, we consider the $(N,N)$-th colored Jones polynomials for the Whitehead Link. Note that in this case, ([\[t1\]](#t1){reference-type="ref" reference="t1"}) and ([\[t5\]](#t5){reference-type="ref" reference="t5"}) can be simplified as $$\begin{aligned}
 t^{\frac{N(2n+1)}{2}}-t^{-\frac{N(2n+1)}{2}} 
&= 2i\sin\left( \frac{\pi(n+\frac{1}{2})}{N+\frac{1}{2}} \right) \\
t^{-N(l+n)} 
&= e^{\pi i\left( \frac{l}{N+\frac{1}{2}} + \frac{n}{N+\frac{1}{2}} \right)}
\end{aligned}$$ Define $$\begin{aligned}
\tilde\Phi^{(1,1)}_{N,N} (z_1,z_2) 
&= \frac{1}{2\pi i} \left[\varphi_r \left( \frac{N\pi}{N+\frac{1}{2}}  - \pi z_1 - \pi z_2 -\frac{\pi}{2N+1}\right) \right. \notag\\
&\qquad  - \varphi_r\left(  \frac{N\pi}{N+\frac{1}{2}} - \pi z_2- \frac{\pi}{2N+1}\right) \notag \\
&\qquad  + \varphi_r \left(\pi z_2 + \frac{\pi}{2N+1}\right)  - \varphi_r\left( \pi z_1 + \pi z_2 + \frac{\pi}{2N+1}\right) \notag\\
&\left.\qquad  + \varphi_r\left( \pi z_1 + \frac{\pi}{2N+1}\right) \right] 
\end{aligned}$$ We can see that $$\begin{aligned}
&\lim_{N\to\infty} \tilde\Phi^{(1,1)}_{N,N} (z_1,z_2) \\
&= \Phi^{\pm(1,1)}(z_1,z_2)\\
&=  \frac{1}{2\pi i} \left[ \Li\left(e^{- 2\pi i z_1 - 2\pi i z_2}\right) - \Li\left( e^{ - 2\pi i z_2 }\right) + \Li \left(e^{2\pi i z_2}\right) - \Li\left(e^{2\pi iz_1+ 2\pi i z_2}\right)
 + \Li\left(e^{2\pi i z_1}\right)  \right]
\end{aligned}$$

Since $\Phi^{+(1,1)}(z_1,z_2)$ and $\Phi^{-(1,1)}(z_1,z_2)$ are the same, for simplicity we use $\Phi^{(1,1)}(z_1,z_2)$ to denote $\Phi^{\pm(1,1)}(z_1,z_2)$. Recall that for $\theta \in (0,\pi)$, we have $$\Li (e^{2i\theta}) = \Li(1) + \theta(\pi - \theta) + 2i \Lambda(\theta)  ,$$ where $\Lambda$ is the Lobachevsky function defined by $$\Lambda(\theta) = -\int_0^\theta \log|2\sin t| dt$$ Also, the Lobachevsky function $\Lambda$ is an odd function. Let $$\Delta = \{(x,y) \in [0,1]^2 \mid x+y \leq 1\}$$ Then for $(z_1,z_2) \in \Delta$, the real part of $\Phi^{(1,1)}(x_1,x_2)$ is given by $$\begin{aligned}
\Re \Phi^{(1,1)} (x_1,x_2) 
&=  \frac{1}{\pi } \left[ \Lambda\left(- \pi  z_1 - \pi  z_2\right) - \Lambda\left(  - \pi  z_2 \right) + \Lambda \left(\pi  z_2\right) - \Lambda\left(\pi z_1+ \pi  z_2\right) + \Lambda\left(\pi z_1\right) \right] \\
&= \frac{1}{\pi} [-2 \Lambda(\pi x_1 + \pi x_2) + 2\Lambda(\pi x_2) + \Lambda(\pi x_1)]\\
&= \frac{1}{\pi} f(x_1,x_2)
\end{aligned}$$

Note that this function $f(x_1, x_2)$ is the function appeared in Equation (3.22) of [@HZ07]. In particular, the real part of $\Phi^{(1,1)}(x_1,x_2)$ has a unique maximum at $(\frac{1}{2}, \frac{1}{4})$ in the $\Delta$, with maximum value $$\Re\Phi^{(1,1)} \left(\frac{1}{2}, \frac{1}{4}\right) = \frac{1}{\pi}f \left(\frac{1}{2}, \frac{1}{4}\right) = \frac{1}{2\pi} \left[8\Lambda\left(\frac{\pi}{4}\right)\right] = \frac{1}{2\pi} v_8 = \frac{1}{2\pi} \operatorname{Vol}(WL)$$ Furthermore, the critical point equations of the potential function are given by

::: empheq
align &(1-e\^-2i z_1 - 2i z_2) + (1 - e\^2i z_1 + 2i z_2) - (1 - e\^2i z_1) = 0 []{#1meridian1 label="1meridian1"}\
\
&(1-e\^-2i z_1 - 2i z_2) + (1 - e\^2i z_1 + 2i z_2) - (1 - e\^- 2i z_2) - (1 - e\^2i z_2) = 0 []{#1long1 label="1long1"}
:::

Note that the point $(z_1, z_2) =  \left(\frac{1}{2}, \frac{1}{4}\right)$ indeed solves the equations $(\ref{1meridian1})$ and $(\ref{1long1})$. Moreover, at this critical point, $$\begin{aligned}
\frac{\partial^2}{\partial z_1^2} \Phi^{(1,1)} \left(\frac{1}{2}, \frac{1}{4}\right) &= (2\pi i) \left( \frac{i}{1-i} - \frac{ -i}{1+i} + \frac{-1}{2} \right) = 2\pi i \left( \frac{2i-1}{2} \right) \\ 
\frac{\partial^2}{\partial z_2^2} \Phi^{(1,1)} \left(\frac{1}{2}, \frac{1}{4}\right) &= (2\pi i) \left( \frac{i}{1-i} - \frac{-i}{1+i} - \frac{-i}{1+i} + \frac{i}{1-i} \right) = 2\pi i (2i)\\
\frac{\partial^2}{\partial z_1 \partial z_2} \Phi^{(1,1)}  \left(\frac{1}{2}, \frac{1}{4}\right) &= (2\pi i) \left( \frac{i}{1-i} - \frac{ -i}{1+i} \right) = 2\pi i (i)
\end{aligned}$$

As a result, since $$\begin{aligned}
-\det (\text{Hess} \Phi^{(1,1)})  \left(\frac{1}{2}, \frac{1}{4}\right)  = -4\pi^2 (1+i) \neq 0,
\end{aligned}$$ $\Phi^{(1,1)}(z_1,z_2)$ has a non-degenerate critical point at $\left(\frac{1}{2},\frac{1}{4}\right)$ with critical value $$\begin{aligned}
&\Phi^{(1,1)}\left(\frac{1}{2},\frac{1}{4}\right)  \notag\\
&= \frac{1}{2\pi i} \left[ 2\Li(i) - 2\Li(-i) + \Li(-1) \right] \notag \\
&= \frac{1}{2\pi i} \left[ 2\left(\Li(1) + \left(\frac{\pi}{4}\right)\left(\pi - \frac{\pi}{4}\right) + 2i \Lambda\left(\frac{\pi}{4}\right) \right) - 2 \left(\Li(1) + \left(\frac{3\pi}{4}\right)\left(\pi - \frac{3\pi}{4}\right) + 2i \Lambda\left(\frac{3\pi}{4}\right) \right) - \frac{\pi^2}{12} \right] \notag\\
&= \frac{1}{2\pi} \left[ 8\Lambda\left(\frac{\pi}{4}\right) + \frac{\pi^2 i}{12} \right] \notag\\
&= \frac{1}{2\pi} \left[ \operatorname{Vol}({\mathbb S}^3\backslash WL) + \frac{\pi^2 i}{12} \right] 
\end{aligned}$$

We denote this non-degenerate critical point by $\mathbf{z}^{(1,1)}$. Similarly, we let $\mathbf{z}^{(1,1)}_{N,N}$ to be the critical point of the function $\tilde\Phi^{(1,1)}_{N,N}(z_1,z_2)$ with $\lim_{N\to \infty}\mathbf{z}^{(1,1)}_{N,N}= (\frac{1}{2},\frac{1}{4})$.

Next, we are going to study the asymptotic expansion formula for $J_{N,N}(WL, e^{\frac{2\pi i}{N+\frac{1}{2}}})$ and show that the exponential growth is given by the critical value of $\Phi^{(1,1)} \left(\mathbf{z}^{(1,1)}\right)$. From previous discussion, since the critical value is the unique maximum of $\Re\Phi(z_1,z_2)$ on $\Delta$, it sufficies to study the asymptotic expansion formula near this critical point.

Since $\mathbf{z}^{(1,1)}$ is a critical point, we can find a 4 real dimension ball $B_R \subset {\mathbb C}^2 \cong {\mathbb R}^4$ centred at the non-degenerate critical point with radius $R$ such that whenever $(x_1\pm\eta i,x_2), (x_1, x_2\pm\eta i) \in B_R$. we have $$\begin{aligned}
\label{ball}
 \left| \frac{d}{d \eta} \Re\Phi(x_1\pm\eta i,x_2) \right|, \left| \frac{d}{d\eta} \Re\Phi(x_1, x_2\pm\eta i)  \right| < \pi 
\end{aligned}$$ In particular, we may choose $R$ small enough such that the intersection $\partial B_R \cap \Delta$ is a circle centered at the critical point. Let $$\begin{aligned}
S^\pm_1 &= \{ (x_1\pm\eta i, x_2) \mid (x_1,x_2) \in \partial B_R \cap \Delta, \eta \in [0,R /2]  \}
\cup \{ (x_1\pm ( R/2 ) i, x_2) \mid (x_1,x_2) \in B_R \cap \Delta \} \\
S^\pm_2 &= \{ (x_1, x_2\pm\eta i) \mid (x_1,x_2) \in \partial B_R \cap \Delta, \eta \in [0,R /2]  \} 
\cup \{ (x_1, x_2\pm ( R/2 ) i) \mid (x_1,x_2) \in B_R \cap \Delta \}
\end{aligned}$$ For every points on $S_1^\pm$, we have $$\begin{aligned}
\label{S1}
\Re\Phi^{(1,1)}(x_1 \pm \eta i, x_2) - \Re\Phi^{(1,1)}(\mathbf{z}^{(1,1)}) \leq \left[\Re\Phi^{(1,1)}(x_1,x_2) - \Re\Phi^{(1,1)}(\mathbf{z}^{(1,1)}) \right] + \pi \eta < 2\pi \eta
\end{aligned}$$ Similarly, for every points on $S_2^\pm$, we have $$\begin{aligned}
\label{S2}
\Re\Phi^{(1,1)}(x_1, x_2 \pm \eta i) - \Re\Phi^{(1,1)}(\mathbf{z}^{(1,1)}) \leq \left[\Re\Phi^{(1,1)}(x_1,x_2) - \Re\Phi^{(1,1)}(\mathbf{z}^{(1,1)}) \right] + \pi \eta < 2\pi \eta
\end{aligned}$$ Thus, by the Poisson Summation Formula (Proposition 4.6, Remark 4.7 and 4.8 in [@O52]), we have $$\begin{aligned}
&J_{N,N} (WL, e^{\frac{2\pi i}{N+\frac{1}{2}}}) \notag\\
&=  \frac{ e^{\frac{2\pi i}{N+\frac{1}{2}}(N^2 - \frac{N}{2} - \frac{1}{2})}}{\sin(\frac{\pi}{N+\frac{1}{2}})} \exp\left(  -\varphi_r \left(  \frac{\pi}{2N+1}\right)\right)\sum_{n=0}^{N-1}\sum_{l=1}^{N-1-n} \sin\left( \pi \left(\frac{n}{N+\frac{1}{2}}\right) + \frac{\pi}{2N+1} \right) e^{\pi i \left(\frac{n}{N+\frac{1}{2}}+\frac{l}{N+\frac{1}{2}}\right)} \notag\\
&\qquad \times
\exp\left( \left(N+\frac{1}{2}\right) \tilde\Phi^{\pm(1,1)}_{N,N} \left(\frac{n}{N+\frac{1}{2}},\frac{l}{N+\frac{1}{2}}\right) \right) \notag \\
&\stackrel[N \to \infty]{\sim}{} \frac{ e^{\frac{2\pi i}{N+\frac{1}{2}}(N^2 - \frac{N}{2} - \frac{1}{2})}}{\sin(\frac{\pi}{N+\frac{1}{2}})} \exp\left(  -\varphi_r \left(  \frac{\pi}{2N+1}\right)\right) \left(N+\frac{1}{2}\right)^2\notag\\
&\qquad \times \int\int_{B_R \cap \Delta} \sin\left( \pi z_1 + \frac{\pi}{2N+1} \right) e^{\pi i \left(z_1+z_2\right)} 
\exp\left( \left(N+\frac{1}{2}\right) \tilde\Phi^{(1,1)}_{N,N} \left(z_1,z_2\right) \right) dz_1 dz_2
\end{aligned}$$

Next, we want to apply the Saddle point approximation. A key observation is that we can choose $r$ as small as possible such that the assumption in Proposition 3.5 in [@O52] is automatically satisfied. Moreover, by Lemma A.3 of [@O52], we have $$\begin{aligned}
\label{QDFcoe}
\exp\left(-\varphi^h \left( \frac{\pi}{2N+1} \right) \right) 
&= \exp\left(- \frac{N+\frac{1}{2}}{2\pi i} \frac{\pi^2}{6} - \frac{1}{2}\log (N+\frac{1}{2}) - \frac{\pi i}{4} + \frac{\pi i}{12 (N+\frac{1}{2})} \right) \notag\\
&\stackrel[N \to \infty]{\sim}{ } e^{-\frac{\pi i}{4}}(N+\frac{1}{2})^{-\frac{1}{2}}\exp\left( \left( N+\frac{1}{2}\right) \frac{\pi i}{12} \right)
\end{aligned}$$

Altogether, by the saddle point approximation (Proposition 3.5 in [@O52]), we have $$\begin{aligned}
&\quad J_{N, N} (WL, e^{\frac{2\pi i}{N+\frac{1}{2}}}) \notag  \\
&\stackrel[N \to \infty]{\sim}{}  - e^{-\frac{\pi i}{4}} \frac{(N+\frac{1}{2})^{\frac{1}{2}}}{\pi}\exp\left( \frac{N+\frac{1}{2}}{2\pi } \frac{\pi^2 i}{6} \right) 
(N+\frac{1}{2})^2 \notag \\
&\qquad \int\int_{B_R \cap \Delta} \sin\left( \pi z_1 + \frac{\pi}{2N+1} \right) e^{\pi i \left(z_1+z_2\right)} 
\exp\left( \left(N+\frac{1}{2}\right) \tilde\Phi^{(1,1)}_{N,N} \left(z_1,z_2\right) \right) dz_1 dz_2 \notag \\
&\stackrel[N \to \infty]{\sim}{}  \frac{\pi(N+\frac{1}{2})^{3/2}}{\sqrt{ -4 \pi^2(1+i) }} 
\times\exp\left( \left(N+\frac{1}{2}\right)\left( \tilde\Phi^{(1,1)}_{N,N} (\mathbf{z}^{(1,1)}_{N,N}) + \frac{\pi i}{12} \right)  \right) \left(1 + O\left(\frac{1}{N}\right) \right)
\end{aligned}$$

with $$\begin{aligned}
\lim_{N\to \infty}
\left[ \tilde\Phi^{(1,1)}_{N,N} (\mathbf{z}^{(1,1)}_{N,N}) + \frac{\pi i}{12} \right]
= \frac{1}{2\pi}\left[ \operatorname{Vol}({\mathbb S}^3\backslash WL) + \frac{\pi^2 i }{4} \right]
= \frac{1}{2\pi}[\operatorname{Vol}({\mathbb S}^3\backslash WL)+ i \operatorname{CS}({\mathbb S}^3\backslash WL)]
\end{aligned}$$

::: remark
If we use the normalization in [@HZ07] and [@V08], then there will be an extra factor $$\frac{t^{\frac{1}{2}}-t^{-\frac{1}{2}}}{t^{N/2}-t^{-N/2}} = \frac{2i\sin\left(\pi (\frac{1}{N+\frac{1}{2}}) \right)}{2i\sin\left(\pi (\frac{N}{N+\frac{1}{2}}) \right)} \stackrel[N \to \infty]{\sim}{} 2$$ In particular, the exponent of $(N+\frac{1}{2})$ is $\frac{3}{2}$, which agrees with the result in [@HZ07] and [@V08].
:::

## The asymptotics expansion formula for $J_{M_1,M_2}(WL,e^{\frac{2\pi i}{N+\frac{1}{2}}})$ {#WLs}

In this section, we generalize the previous argument to study the asymptotics expansion formula for $J_{M_1,M_2}(WL,e^{\frac{2\pi i}{N+\frac{1}{2}}})$. Recall that the potential functions $\Phi^{\pm(s_1, s_2)} (z_1,z_2)$ are given by

$$\begin{aligned}
\Phi^{\pm(s_1, s_2)} (z_1,z_2) 
&=  \frac{1}{2\pi i} \left[ \pm \left(2\pi i \left( s_1 - 1\right)\right) \left(2\pi i \left(z_1 -\frac{1}{2} \right)\right)  - (2\pi i (s_2-1))(2\pi i z_1 + 2\pi i z_2)  \right. \\
&\qquad + \Li\left(e^{2\pi i (s_2-1) - 2\pi i z_1 - 2\pi i z_2}\right) - \Li\left( e^{2\pi i (s_2-1) - 2\pi i z_2 }\right) \\
&\qquad \left.+ \Li \left(e^{2\pi i z_2}\right) - \Li\left(e^{2\pi iz_1+ 2\pi i z_2}\right) + \Li\left(e^{2\pi i z_1}\right)  \right]
\end{aligned}$$

From now on, for simiplicity we consider the potential function $\Phi^{+(s_1,s_2)}(z_1,z_2)$. The same arguement works for the potential function $\Phi^{-(s_1,s_2)}(z_1,z_2)$. The following lemma gaurantees the existence of the critical points for the potential functions.

::: lemma
There exists a neighborhood $U\subset {\mathbb C}^2$ of $(1,1) \in {\mathbb C}^2$ and two holomorphic families of non-degenerate critical points $\{\mathbf{z}^{\pm(s_1,s_2)} \}_{(s_1,s_2) \in U}$ for the families of potential functions $\Phi^{\pm(s_1,s_2)}(z_1,z_2)$ such that $\mathbf{z}^{\pm(1,1)} = \left(\frac{1}{2}, \frac{1}{4} \right)$.
:::

::: proof
*Proof.* First of all, we pick a small enough neighborhood $U \subset {\mathbb C}^2$ of the point $(1,1)\in {\mathbb C}^2$ such that the function $F: U\times B_R \to {\mathbb C}$ defined by $$F(s_1,s_2, z_1,z_2) = \Phi^{+(s_1,s_2)}(z_1,z_2)$$ is well-defined and holomorphic. Consider the function $G:U \times B_R \to {\mathbb C}^2$ given by $$G(s_1,s_2,z_1,z_2) = \left(\frac{\partial}{\partial z_1} F(s_1,s_2, z_1,z_2), \frac{\partial}{\partial z_2} F(s_1,s_2, z_1,z_2)\right)$$ By direct computation, we have $$\begin{aligned}
\frac{\partial}{\partial z_1} F(s_1,s_2, z_1,z_2)
&= 2\pi i\left[(s_1 - 1) - (s_2 - 1) \right] + \log(1-e^{2\pi i (s_2 -1)}e^{-2\pi i z_1 - 2\pi i z_2})  \notag\\
& \qquad + \log(1 - e^{2\pi i z_1 + 2\pi i z_2}) - \log(1 - e^{2\pi i z_1}) \\
\frac{\partial}{\partial z_2} F(s_1,s_2, z_1,z_2) 
&= -  2\pi i  (s_2 - 1) + \log(1-e^{2\pi i (s_2 -1)}e^{-2\pi i z_1 - 2\pi i z_2}) \notag\\
&\qquad + \log(1 - e^{2\pi i z_1 + 2\pi i z_2}) - \log(1 - e^{2\pi i (s_2 - 1) - 2\pi i z_2}) \notag \\
&\qquad - \log(1 - e^{2\pi i z_2}) 
\end{aligned}$$ Moreover, $$\begin{aligned}
\frac{\partial}{\partial s_1} \left( \frac{\partial}{\partial z_1} F(s_1,s_2, z_1,z_2) \right)
&= 2\pi i  \\
\frac{\partial}{\partial s_2} \left( \frac{\partial}{\partial z_1} F(s_1,s_2, z_1,z_2) \right)
&= 0 \\
\frac{\partial}{\partial s_2} \left( \frac{\partial}{\partial z_2} F(s_1,s_2, z_1,z_2) \right)
&= -2\pi i - \frac{2\pi i e^{2\pi i (s_2 -1)}e^{-2\pi i z_1 - 2\pi i z_2}}{1-e^{2\pi i (s_2 -1)}e^{-2\pi i z_1 - 2\pi i z_2}} + \frac{2\pi i e^{2\pi i (s_2 -1)}e^{- 2\pi i z_2}}{1-e^{2\pi i (s_2 -1)}e^{- 2\pi i z_2}} 
\end{aligned}$$ As a result, we have $$\begin{aligned}
\begin{vmatrix}
\frac{\partial}{\partial s_1} \left( \frac{\partial}{\partial z_1} F \right)
&
\frac{\partial}{\partial s_2} \left( \frac{\partial}{\partial z_1} F \right) \\
\frac{\partial}{\partial s_1} \left( \frac{\partial}{\partial z_2} F \right) 
&
\frac{\partial}{\partial s_2} \left( \frac{\partial}{\partial z_2} F\right)
\end{vmatrix}
\left(1,1,\frac{1}{2}, \frac{1}{4}\right)
= -2\pi i (1+i) 
\neq 0
\end{aligned}$$ The result follows from the implicit function theorem. ◻
:::

Note that on the surfaces $S_1^+$, from ([\[S1\]](#S1){reference-type="ref" reference="S1"}) we have $$\begin{aligned}
\Re\Phi^{(1,1)}(x_1 \pm \eta i, x_2) - \Re\Phi^{(1,1)}(\mathbf{z}^{(1,1)}) 
< 2\pi \eta
\end{aligned}$$ Since $S_1^+$ is a compact set, by continuity, we may choose $\delta$ small enough such that $$\begin{aligned}
\Re\Phi^{(s_1,s_2)}(x_1 + \eta i, x_2) - \Re\Phi^{(s_1,s_2)}(\mathbf{z}^{+(s_1,s_2)}) 
< 2\pi \eta
\end{aligned}$$ for any $1-\delta<s_1,s_2 \leq 1$. The same argument works for $S_1^-, S_2^+$ and $S_2^-$.

As a result, the assumptions for applying the Poisson Summation formula are satisfied. Finally, for the same reason, we can choose $\delta>0$ small enough such that the conditions for applying the saddle point approximation are automatically satisfied. Together with Lemma [\[EM_2\]](#EM_2){reference-type="ref" reference="EM_2"}, the asymptotic expansion formula of $J_{M_1,M_2}(WL,e^{\frac{2\pi i}{N+\frac{1}{2}}})$ is given by

$$\begin{aligned}
&\quad J_{M_1, M_2} (WL, e^{\frac{2\pi i}{N+\frac{1}{2}}}) \notag  \\
&= \frac{ (-1)^{(M_1 - N) }  e^{\frac{2\pi i}{N+\frac{1}{2}}(M_2^2 - \frac{M_2}{2} - \frac{1}{2})}}{2\sin(\frac{\pi}{N+\frac{1}{2}})} \exp\left(  -\varphi_r\left(  \frac{\pi}{2(N+\frac{1}{2})}\right)\right)\notag \\
&\qquad  \left[e^{\pi i \left(\frac{M_1}{N+\frac{1}{2}} - 1\right) }\sum_{n=0}^{M_2-1} \sum_{l=0}^{M_2-1-n} \exp\left( \left(N+\frac{1}{2}\right)\Phi^{+(s_1,s_2)}_{M_1,M_2} \left(\frac{n}{N+\frac{1}{2}},\frac{l}{N+\frac{1}{2}}\right) \right) \right. \notag \\
&\qquad \quad \left. + e^{-\pi i \left(\frac{M_1}{N+\frac{1}{2}} - 1\right) }\sum_{n=0}^{M_2-1} \sum_{l=0}^{M_2-1-n} \exp\left( \left(N+\frac{1}{2}\right)\Phi^{-(s_1,s_2)}_{M_1,M_2} \left(\frac{n}{N+\frac{1}{2}},\frac{l}{N+\frac{1}{2}}\right) \right) \right] \notag \\
&\stackrel[N \to \infty]{\sim}{}  \frac{ e^{-\frac{\pi i}{4}} (-1)^{(M_1 - N) }  e^{\frac{2\pi i}{N+\frac{1}{2}}(M_2^2 - \frac{M_2}{2} - \frac{1}{2})}}{2\pi} \left(N+\frac{1}{2}\right)^{\frac{1}{2}}\exp\left( \frac{N+\frac{1}{2}}{2\pi } \frac{\pi^2 i}{6} \right)\left(N+\frac{1}{2}\right)^2   \notag  \\
& \qquad\qquad\left[ e^{\pi i (\frac{M_1}{N+\frac{1}{2}} -1)} \int\int_{B_R \cap \Delta}  E_{M_2}(z_1,z_2)\exp \left( \left(N+\frac{1}{2}\right) \Phi^{+\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} (z_1, z_2) \right) dz_1 dz_2 \right. \notag  \\
& \qquad\qquad\qquad \left.  + e^{-\pi i (\frac{M_1}{N+\frac{1}{2}} -1)} \int\int_{B_R \cap \Delta}  E_{M_2}(z_1,z_2)\exp \left( \left(N+\frac{1}{2}\right) \Phi^{-\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} (z_1, z_2) \right) dz_1 dz_2 \right] \notag  \\
&\stackrel[N \to \infty]{\sim}{}  \frac{e^{-\frac{\pi i}{4}} (-1)^{(M_1 - N) }  e^{\frac{2\pi i}{N+\frac{1}{2}}(M_2^2 - \frac{M_2}{2} - \frac{1}{2})}}{2} \exp\left( \frac{N+\frac{1}{2}}{2\pi } \frac{\pi^2 i}{6} \right) \left(N+\frac{1}{2}\right)^\frac{3}{2}   \notag  \\
& \qquad\quad\left[ e^{\pi i \left(\frac{M_1}{N+\frac{1}{2}} -1\right)}E_{M_2}(\mathbf{z}^{+(s_1,s_2)}_{M_1,M_2} ) \frac{ \exp\left( \left(N+\frac{1}{2}\right) \Phi^{+\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} \left(\mathbf{z}^{+\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} \right) \right)}{ \sqrt{-\det\Hess \Phi^{+\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} \left(\mathbf{z}^{+\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)}\right)}}  \right. \notag\\
&\qquad\qquad\qquad \left.  + e^{-\pi i \left(\frac{M_1}{N+\frac{1}{2}} -1\right)}E_{M_2}(\mathbf{z}^{-(s_1,s_2)}_{M_1,M_2} )  \frac{ \exp\left( \left(N+\frac{1}{2}\right) \Phi^{-\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} \left(\mathbf{z}^{-\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} \right) \right)}{ \sqrt{-\det\Hess \Phi^{-\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} \left(\mathbf{z}^{-\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} \right)}}  \right] ,
\end{aligned}$$ where the last line holds because those terms do not cancel out with each other. In fact, at the end of Section [\[diffsame\]](#diffsame){reference-type="ref" reference="diffsame"}, we will show that for $s_1,s_2$ sufficiently close to $1$, $$\Phi^{+(s_1,s_2)}(\mathbf{z}^{+(z_1,z_2)}) = 
\Phi^{-(s_1,s_2)}(\mathbf{z}^{-(z_1,z_2)})$$ and $$\Re\Phi^{+(s_1,s_2)}(\mathbf{z}^{+(z_1,z_2)})
= \Re\Phi^{-(s_1,s_2)}(\mathbf{z}^{-(z_1,z_2)})
= \operatorname{Vol}\left({\mathbb S}^3 \backslash WL, u_1 = 2\pi i (1 - s_1), v_2=4\pi i (1 - s_2)\right),$$ where $\operatorname{Vol}\left({\mathbb S}^3 \backslash WL, u_1 = 2\pi i (1 - s_1), v_2=4\pi i (1 - s_2)\right)$ is the hyperbolic volume of the Whitehead link complement equipped with the incomplete hyperbolic structure such that the logarithm of the holonomy of the meridian of the belt and the logarithm of the holonomy of the longitude of the clasp are $u_1 = 2\pi i (1 - s_1)$ and $v_2=4\pi i (1 - s_2)$ respectively. As a result, by choosing $\delta>0$ sufficiently small, for any $1-\delta < s_1,s_2 \leq 1$, we have

$$\begin{aligned}
 J_{M_1, M_2} (WL, e^{\frac{2\pi i}{N+\frac{1}{2}}})
&\stackrel[N \to \infty]{\sim}{}  \frac{e^{-\frac{\pi i}{4}} (-1)^{(M_1 - N) }  e^{\frac{2\pi i}{N+\frac{1}{2}}(M_2^2 - \frac{M_2}{2} - \frac{1}{2})}}{2} \exp\left( \frac{N+\frac{1}{2}}{2\pi } \frac{\pi^2 i}{6} \right) \left(N+\frac{1}{2}\right)^\frac{3}{2}   \notag  \\
& \qquad\quad \left[ \frac{e^{\pi i \left(\frac{M_1}{N+\frac{1}{2}} -1\right)}E_{M_2}(\mathbf{z}^{+(s_1,s_2)}_{M_1,M_2} )}{ \sqrt{-\det\Hess \Phi^{+\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} \left(\mathbf{z}^{+\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)}\right)}}  \right.\notag\\
& \left.\qquad\quad +
\frac{e^{-\pi i \left(\frac{M_1}{N+\frac{1}{2}} -1\right)}E_{M_2}(\mathbf{z}^{-(s_1,s_2)}_{M_1,M_2} )}{ \sqrt{-\det\Hess \Phi^{-\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} \left(\mathbf{z}^{-\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)}\right)}} \right]\notag\\
&\qquad \qquad \exp\left( \left(N+\frac{1}{2}\right) \Phi^{+\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} \left(\mathbf{z}^{+\left(\frac{M_1}{N+\frac{1}{2}}, \frac{M_2}{N+\frac{1}{2}}\right)} \right) \right)
\end{aligned}$$

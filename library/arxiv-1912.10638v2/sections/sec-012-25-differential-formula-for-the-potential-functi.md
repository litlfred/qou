---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains"
section_id: sec-012-25-differential-formula-for-the-potential-functi
section_title: "Differential formula for the potential function"
section_number: 2.5
pages: 21-32
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.714
latex_coverage_ratio: 0.635
doc_brief: "Asymptotics of some quantum invariants of the Whitehead chains — In this paper, we study the asymptotics of the colored Jones polynomials of the Whitehead chains with one belt colored by M1 and all"
---
[]{#diffsame label="diffsame"} After we associate a triangulation of the link complement to the potential functions, we need to prove that the critical values of the potential functions $\Phi^{\pm(s_1,s_2)}(\mathbf{z}^{\pm(z_1,z_2)})$ are indeed the sum of the hyperbolic volume of the tetrahedra. This can be done by using the following differential formula satisfied by the potential functions.

::: lemma
Write $z_k = x_k + i y_k$ for $k=1,2$. The real part of the potential function satisfies the following differential equation: $$\begin{aligned}
\Re \Phi^{\pm(s_1,s_2)}(z_1,z_2) = \frac{1}{2\pi} V^{\pm(s_1,s_2)}(z_1,z_2) + \sum_{k=1}^2 y_k \frac{\partial}{\partial y_k} \Re \Phi^{\pm(s_1,s_2)}(z_1,z_2),
\end{aligned}$$ where $$\begin{aligned}
V^{\pm(s_1,s_2)}(z_1,z_2) 
&= D(e^{2\pi i(s_2-1) - 2\pi i z_1 - 2\pi i z_2}) - D(e^{2\pi i (s_2-1) - 2\pi i z_2}) + D(e^{2\pi i z_2}) \notag \\
&\qquad - D(e^{2\pi i z_1 + 2\pi i z_2}) + D(e^{2\pi i z_1}) 
\end{aligned}$$ and $D(z)$ is the Bloch-Wigner function $$\begin{aligned}
D(z) = \im\Li(z) + \log|z|\Arg(1-z)
\end{aligned}$$
:::

::: proof
*Proof.* First of all, for $z = x + i y$, since $$\begin{aligned}
\frac{d}{dz} \frac{\Li (e^{2\pi i z})}{2\pi i} &= -\log(1-e^{2\pi i z}) 
\end{aligned}$$ we have $$\begin{aligned}
\im \frac{d}{dz} \frac{\Li (e^{2\pi i z})}{2\pi i} &= - \Arg(1-e^{2\pi i z})
\end{aligned}$$ By the Cauchy Riemann equations, we have $$\begin{aligned}
 \frac{\partial}{\partial y} \Re \frac{\Li (e^{2\pi i z})}{2\pi i} =  \Arg(1-e^{2\pi i z})
\end{aligned}$$ Therefore, $$\begin{aligned}
\Re \frac{\Li(e^{2\pi i z})}{2\pi i} 
&= \frac{\im \Li(e^{2\pi i z})}{2\pi} \\
&= \frac{D(e^{2\pi i z}) - \log |e^{2\pi i z}| \Arg(1-e^{2\pi i z})}{2\pi}\\
&= \frac{D(e^{2\pi i z})}{2\pi} + y\frac{\partial}{\partial y} \Re \frac{\Li(e^{2\pi i z})}{2\pi i} 
\end{aligned}$$ Following the same arguments, it is easy to show that $$\begin{aligned}
\Re \frac{\Li(e^{-2\pi i z})}{2\pi i} &= \frac{D(e^{-2\pi i z})}{2\pi} + y\frac{\partial}{\partial y} \Re \frac{\Li(e^{-2\pi i z})}{2\pi i} 
\end{aligned}$$ Thus, $$\begin{aligned}
\Re \frac{\Li(e^{2\pi i(s_2 - 1) - 2\pi i z_1 - 2\pi i z_2})}{2\pi i} &= \frac{D(e^{2\pi i(s_2 - 1) - 2\pi i z_1 - 2\pi i z_2})}{2\pi} + \sum_{k=1}^2 y_k\frac{\partial}{\partial y_k} \Re \frac{\Li(e^{2\pi i(s_2 - 1) - 2\pi i z_1 - 2\pi i z_2)})}{2\pi i} \\
\Re \frac{\Li(e^{2\pi i(s_2 - 1) - 2\pi i z_2})}{2\pi i} &= \frac{D(e^{2\pi i(s_2 - 1) - 2\pi i z_1 - 2\pi i z_2})}{2\pi} +  y_2\frac{\partial}{\partial y_2} \Re \frac{\Li(e^{2\pi i(s_2 - 1)  - 2\pi i z_2)})}{2\pi i} 
\end{aligned}$$ Besides, for the linear terms in $z_1,z_2$, it is straight forward to verify that $$\begin{aligned}
\Re\frac{1}{2\pi i} \left[ \pm \left(2\pi i \left( s_1 - 1\right)\right) \left(2\pi i \left(z_1 -\frac{1}{2} \right)\right) \right]&= y_1 \frac{\partial}{\partial y_1}\Re\frac{1}{2\pi i} \left[ \pm \left(2\pi i \left( s_1 - 1\right)\right) \left(2\pi i \left(z_1 -\frac{1}{2} \right)\right) \right]\\
\Re\frac{1}{2\pi i}  \left[ - (2\pi i (s_2-1))(2\pi i z_1 + 2\pi i z_2) \right]&= \sum_{k=1}^2 y_k \frac{\partial}{\partial y_k} \Re\frac{1}{2\pi i}  \left[ - (2\pi i (s_2-1))(2\pi i z_1 + 2\pi i z_2) \right]
\end{aligned}$$ As a result, by direct computation, we get the differential formula. ◻
:::

Together with the discussion in previous subsection, we have $$\begin{aligned}
\Re \Phi^{\pm(s_1,s_2)}(\mathbf{z}^{\pm(z_1,z_2)})
= \frac{1}{2\pi} V^{\pm(s_1,s_2)} (\mathbf{z}^{\pm(z_1,z_2)}) 
= \frac{1}{2\pi}\operatorname{Vol}\left({\mathbb S}^3 \backslash WL, u_1 = \pm 2\pi i (1 - s_1), v_2 = 4\pi i(1-s_2)\right)
\end{aligned}$$ By the Theorem 3 in [@NZ85], since $v_2$ is even in $u_1$ and the volume function is an even function in the variable $u_1$, we have $$\operatorname{Vol}\left({\mathbb S}^3 \backslash WL, u_1 = 2\pi i (1 - s_1), v_2 = 4\pi i(1-s_2)\right)=\operatorname{Vol}\left({\mathbb S}^3 \backslash WL, u_1 = - 2\pi i (1 - s_1), v_2 = 4\pi i(1-s_2)\right)$$ Thus we have $$\begin{aligned}
\Re \Phi^{\pm(s_1,s_2)}(\mathbf{z}^{\pm(z_1,z_2)})
= \frac{1}{2\pi}\operatorname{Vol}\left({\mathbb S}^3 \backslash WL, u_1 =  2\pi i (1 - s_1), v_2 = 4\pi i(1-s_2)\right)
\end{aligned}$$

Next, from the definitions of the functions $\Phi^{\pm(s_1,s_2)}(\mathbf{z}^{\pm(z_1,z_2)})$, if we regard $s_1,s_2$ as complex variables, then we get two holomorphic functions in $s_1,s_2$. In particular, for each fixed $s_2\in {\mathbb R}$ sufficiently close to $1$, we have two holomorphic functions for $s_1$ sufficiently close to $1$ given by $$N^\pm(s_1) = \Phi^{\pm(s_1,s_2)}(\mathbf{z}^{+(z_1,z_2)})$$ with the same real part $$\Re N^\pm (s_1) = \frac{1}{2\pi}\operatorname{Vol}\left({\mathbb S}^3 \backslash WL, u_1 =  2\pi i (1 - s_1), v_2 = 4\pi i(1-s_2)\right)$$ Besides, when $s_1=1$, we have $N^+(1)=N^-(1)$. As a result, $N^+(s_1)=N^-(s_1)$ for all real $s_1 \sim 1$. Since this is true for all $s_2\sim 1$, we have $$\begin{aligned}
 \Phi^{+(s_1,s_2)}(\mathbf{z}^{+(z_1,z_2)})
= \Phi^{-(s_1,s_2)}(\mathbf{z}^{-(z_1,z_2)})
\end{aligned}$$ for all $s_1,s_2\sim 1$. This completes the proof of Theorem [\[mainthmWL\]](#mainthmWL){reference-type="ref" reference="mainthmWL"}.

Finally, to prove Corollary [\[WLVolsym\]](#WLVolsym){reference-type="ref" reference="WLVolsym"}, note that by Theorem [\[mainthmWL\]](#mainthmWL){reference-type="ref" reference="mainthmWL"}, we have $$\begin{aligned}
\lim_{N\to\infty} \frac{1}{N+\frac{1}{2}}\log\left|J_{M_1,M_2}(WL, e^{\frac{2\pi i}{N+\frac{1}{2}}})\right| &= \operatorname{Vol}({\mathbb S}^3\backslash WL, u_1 = 2\pi i(1-s_1), v_2= 4\pi i(1-s_2)) \\
\lim_{N\to\infty} \frac{1}{N+\frac{1}{2}}\log\left|J_{M_2,M_1}(WL, e^{\frac{2\pi i}{N+\frac{1}{2}}})\right| &= \operatorname{Vol}({\mathbb S}^3\backslash WL, u_1 = 2\pi i(1-s_2), v_2= 4\pi i(1-s_1))
\end{aligned}$$ By exchanging the components of the Whitehead link, we have $$\begin{aligned}
\lim_{N\to\infty} \frac{1}{N+\frac{1}{2}}\log\left|J_{M_1,M_2}(WL, e^{\frac{2\pi i}{N+\frac{1}{2}}})\right| 
=
\lim_{N\to\infty} \frac{1}{N+\frac{1}{2}}\log\left|J_{M_2,M_1}(WL, e^{\frac{2\pi i}{N+\frac{1}{2}}})\right|
\end{aligned}$$ This proves ([\[Volsym1\]](#Volsym1){reference-type="ref" reference="Volsym1"}). Besides, recall that $u_2=0$ if and only if $v_2=0$. ([\[Volsym2\]](#Volsym2){reference-type="ref" reference="Volsym2"}) follows from ([\[Volsym1\]](#Volsym1){reference-type="ref" reference="Volsym1"}) by putting $s_2=1$.

# Generalization to $J_{M_1,M_2}(W_{a,1,c,d},e^{\frac{2\pi i}{N+\frac{1}{2}}})$ {#gen}

## Potential functions for $J_{M_1,M_2}(W_{a,1,c,d},e^{\frac{2\pi i}{N+\frac{1}{2}}})$

In this section, we compute the potential functions of the $\tilde{J}_{M_1,M_2}(W_{a,1,c,d}, e^{\frac{2\pi i}{N+\frac{1}{2}}})$ with the belt colored by $M_1$ and all the other components colored by $M_2$. First of all, recall from [@V08] that the unnormalized $J_{M_1,M_2}(W_{a,1,c,d})$ is given by [^1] $$\begin{aligned}
J_{M_1,M_2} (W_{a,1,c,d}) = \frac{1}{t^{\frac{1}{2}}-t^{-\frac{1}{2}}} \sum_{n=0}^{M_2-1} (t^{\frac{M_1(2n+1)}{2}}-t^{-\frac{M_1(2n+1)}{2}}) \times t^{an(n+1)} \times \tilde{C}(n,t; M_2)^c \times \tilde{C}(n,t^{-1}; M_2)^d
\end{aligned}$$ where $$\tilde{C}(n,t; M_2) =  t^{\frac{M_2(M_2-1)}{2}} \sum_{l = 0}^{M_2-1-n} t^{-M_2(l+n)} \prod_{j=1}^{n} \frac{(1-t^{M_2-l-j})(1-t^{l+j})}{1-t^j}.$$

Note that the contribution of the twists is given by $$\begin{aligned}
t^{an(n+1)} 
&= e^{a \left(\frac{N+\frac{1}{2}}{2\pi i}\right) \left[ 2\pi i \left(\frac{n}{N+\frac{1}{2}} \right) \right] \left[ 2\pi i \left( \frac{n}{N+\frac{1}{2}} + \frac{1}{N+\frac{1}{2}} \right) \right] } \notag \\
&= e^{a \left(\frac{N+\frac{1}{2}}{2\pi i}\right) \left[ 2\pi i \left(\frac{n}{N+\frac{1}{2}} - \frac{1}{2} \right) \right] \left[ 2\pi i \left( \frac{n}{N+\frac{1}{2}} - \frac{1}{2} + \frac{1}{N+\frac{1}{2}} \right) \right] }
\times e^{a \pi i - \frac{a}{4}(2\pi i)(N+\frac{1}{2})} \notag \\
&= (-1)^a e^{ - \frac{a}{4}(2\pi i)(N+\frac{1}{2})}\times e^{a \left(\frac{N+\frac{1}{2}}{2\pi i}\right) \left[ 2\pi i \left(\frac{n}{N+\frac{1}{2}} - \frac{1}{2} \right) \right] \left[ 2\pi i \left( \frac{n}{N+\frac{1}{2}} - \frac{1}{2} + \frac{1}{N+\frac{1}{2}} \right) \right] }\label{t'3}
\end{aligned}$$

Besides, for the colored Jones polynomials of the mirror clasp, note that $$\begin{aligned}
 \prod_{j=1}^{n} (1-t^{-(M_2-l-j)}) 
=&\prod_{j=1}^n (1-t^{- M_2 + (N+\frac{1}{2}) +l +j}) \notag\\
=&\prod_{j=1}^n \left(1 - e^{2\pi i \left(-\left(\frac{M_2}{N+\frac{1}{2}} -1\right) + \frac{l}{N+\frac{1}{2}} + \frac{j}{N+\frac{1}{2}}\right)}\right)\notag \\
=&\exp\left(\frac{N+\frac{1}{2}}{2\pi i}\sum_{j=1}^n \left( \varphi_r \left(-\pi \left(\frac{M_2}{N+\frac{1}{2}} -1\right) + \frac{l\pi}{N+\frac{1}{2}} + \frac{(j-\frac{1}{2})\pi}{N+\frac{1}{2}}\right) \right. \right.\notag\\
&\left. \left.\qquad - \varphi_r\left(  -\pi\left(\frac{M_2}{N+\frac{1}{2}} -1\right) + \frac{l\pi}{N+\frac{1}{2}} + \frac{(j+\frac{1}{2})\pi}{N+\frac{1}{2}}\right)  \right) \right) \notag\\
=& \exp \left(\frac{N+\frac{1}{2}}{2\pi i} \left( \varphi_r \left( -\pi  \left(\frac{M_2}{N+\frac{1}{2}} -1\right) + \frac{l\pi}{N+\frac{1}{2}} + \frac{\pi}{2N+1}\right) \right.\right.\notag\\
&\left. \left.\qquad - \varphi_r\left( -\pi  \left(\frac{M_2}{N+\frac{1}{2}} -1\right) + \frac{l\pi}{N+\frac{1}{2}} + \frac{n\pi}{N+\frac{1}{2}} + \frac{\pi}{2N+1}\right)  \right)\right)\label{t9}
\end{aligned}$$

Besides, $$\begin{aligned}
 \prod_{j=1}^{n} (1-t^{-(l+j)})
=&\prod_{j=1}^n \left(1 - e^{2\pi i \left(1 - \frac{l}{N+\frac{1}{2}} - \frac{j}{N+\frac{1}{2}}\right)}\right)\notag \\
=&\exp\left(\frac{N+\frac{1}{2}}{2\pi i}\sum_{j=1}^n \left( \varphi_r \left(\pi -\frac{l\pi}{N+\frac{1}{2}} - \frac{(j+\frac{1}{2})\pi}{N+\frac{1}{2}}\right)  - \varphi_r\left( \pi -\frac{l\pi}{N+\frac{1}{2}} - \frac{(j-\frac{1}{2})\pi}{N+\frac{1}{2}}\right)  \right) \right)\notag \\
=&\exp\left(\frac{N+\frac{1}{2}}{2\pi i}\left( \varphi_r \left(\pi-\frac{l\pi}{N+\frac{1}{2}} - \frac{n\pi}{N+\frac{1}{2}} - \frac{\pi}{2N+1}\right)  - \varphi_r\left( \pi -\frac{l\pi}{N+\frac{1}{2}}-\frac{\pi}{2N+1}\right)   \right)\right)\label{t10}
\\ \notag\\
 \prod_{j=1}^{n} (1-t^{-j})
=&\prod_{j=1}^n \left(1 - e^{2\pi i \left(1 - \frac{j}{N+\frac{1}{2}}\right)}\right) \notag\\
=&\exp\left(\frac{N+\frac{1}{2}}{2\pi i} \sum_{j=1}^n \left( \varphi_r \left(\pi -\frac{(j+\frac{1}{2})\pi}{N+\frac{1}{2}}\right)  - \varphi_r\left(\pi -\frac{(j-\frac{1}{2})\pi}{N+\frac{1}{2}}\right)  \right) \right)\notag \\
=&\exp\left(\frac{N+\frac{1}{2}}{2\pi i} \left( \varphi_r\left( \pi -\frac{n\pi}{N+\frac{1}{2}} - \frac{\pi}{2N+1}\right) - \varphi_r \left( \pi - \frac{\pi}{2N+1}\right) \right) \right) \label{t11}
 
\end{aligned}$$

For each $i = 1,2,\dots,c$, define the function $\psi_{i,M_1,M_2}^{(s_1,s_2)}(z_1,z_{i+1})$ by $$\begin{aligned}
\psi_{i,M_1,M_2}^{(s_1,s_2)} (z_1,z_{i+1})
&= \frac{1}{2\pi i}\left\{ - \left(2\pi i \left(\frac{M_2}{N+\frac{1}{2}} - 1\right)\right)(2\pi i z_1 + 2\pi i z_{i+1}) \right. \notag \\
&\qquad  + \left[\varphi_r \left(\frac{M_2\pi}{N+\frac{1}{2}} - \pi z_1 - \pi z_{i+1} -\frac{\pi}{2N+1}\right) \right.  \notag\\
&\qquad  - \varphi_r\left( \frac{M_2\pi}{N+\frac{1}{2}} - \pi z_{i+1}- \frac{\pi}{2N+1}\right) \notag \\
&\qquad  + \varphi_r \left(\pi z_{i+1} + \frac{\pi}{2N+1}\right)  - \varphi_r\left( \pi z_1 + \pi z_{i+1} + \frac{\pi}{2N+1}\right) \notag\\
&\left.\left.\qquad  + \varphi_r\left( \pi z_1 + \frac{\pi}{2N+1}\right) \right] \right\}
\end{aligned}$$

For each $i = 1,2, \dots, d$, define the function $\kappa_{i,M_1,M_2}^{(s_1,s_2)} (z_1, z_{c+i+1})$ by $$\begin{aligned}
\kappa_{i,M_1,M_2}^{(s_1,s_2)} (z_1,z_{c+i+1})
&= \frac{1}{2\pi i}\left\{  \left(2\pi i \left(\frac{M_2}{N+\frac{1}{2}} - 1\right)\right)(2\pi i z_1 + 2\pi i z_{c+i+1}) \right. \notag \\
&\qquad  -  \left[\varphi_r \left( -\pi  \left(\frac{M_2}{N+\frac{1}{2}} -1\right) + \pi z_1 + \pi z_{c+i+1} + \frac{\pi}{2N+1}\right) \right.  \notag\\
&\qquad  - \varphi_r\left( -\pi  \left(\frac{M_2}{N+\frac{1}{2}} -1\right) + \pi z_{c+i+1} + \frac{\pi}{2N+1}\right) \notag \\
&\qquad  + \varphi_r \left( \pi -\pi z_{c+i+1} - \frac{\pi}{2N+1}\right)  - \varphi_r\left( \pi - \pi z_1 - \pi z_{c+i+1} - \frac{\pi}{2N+1}\right) \notag\\
&\left.\left.\qquad  + \varphi_r\left( \pi - \pi z_1 - \frac{\pi}{2N+1}\right) \right] \right\}
\end{aligned}$$

Altogether, by ([\[t1\]](#t1){reference-type="ref" reference="t1"}) - ([\[t8\]](#t8){reference-type="ref" reference="t8"}) and ([\[t\'3\]](#t'3){reference-type="ref" reference="t'3"}) - ([\[t11\]](#t11){reference-type="ref" reference="t11"}), we have $$\begin{aligned}
 J_{M_1, M_2} (W_{a,1,c,d}, e^{\frac{2\pi i}{N+\frac{1}{2}}})
&=   \frac{(-1)^{(M_1 - N+a) } e^{\frac{2\pi i}{N+\frac{1}{2}}(M_2^2 - \frac{M_2}{2} - \frac{1}{2})}  e^{- \frac{a}{4}(2\pi i)(N+\frac{1}{2})} e^{\frac{2\pi i}{N+\frac{1}{2}}\frac{(c-d)M_2(M_2-1)}{2}}}{2\sin(\frac{\pi}{N+\frac{1}{2}})} \notag\\
&\qquad \times 
\exp\left(  -\varphi_r \left(  \frac{\pi}{2N+1}\right)\right)^{c}
\exp\left(  \varphi_r \left(\pi  - \frac{\pi}{2N+1}\right)\right)^{d}
\times (I_+ + I_-) 
\end{aligned}$$ where $$\begin{aligned}
I_\pm =
&  
\sum_{n=0}^{M_2-1} \sum_{l_1=0}^{M_2-1-n}\dots \sum_{l_c=0}^{M_2-1-n} \sum_{l_1'=0}^{M_2-1-n}\dots \sum_{l_d'=0}^{M_2-1-n} \notag\\
&\qquad \exp\left( \left(N+\frac{1}{2}\right)\Phi^{\pm(s_1, s_2);a,c,d}_{M_1, M_2} 
\left(\frac{n}{N+\frac{1}{2}},\frac{l_1}{N+\frac{1}{2}},\dots, \frac{l_c}{N+\frac{1}{2}}, \frac{l_1'}{N+\frac{1}{2}},\dots, \frac{l_d'}{N+\frac{1}{2}} \right) \right)
\end{aligned}$$ with $$\begin{aligned}
&\Phi^{\pm (s_1,s_2);a,c,d}_{M_1,M_2} (z_1, z_2, \dots, z_{c+1}, z_{c+2},\dots, z_{c+d+1}) \\
&=  \frac{1}{2\pi i} \left\{  \pm2\pi i  \left( \frac{M_1}{N+\frac{1}{2}} - 1\right) \left(2\pi i \left(z_1 -\frac{1}{2} \right)\right) 
+ a \left[2\pi i \left(z_1-\frac{1}{2} \right) \right] \left[ 2\pi i \left(z_1-\frac{1}{2}+ \frac{1}{N+\frac{1}{2}}  \right) \right]\right\}  \\
&\qquad  + \sum_{i=1}^c \psi_{M_1,M_2,i}^{(s_1,s_2)} (z_1,z_{i+1}) + \sum_{i=1}^d \kappa_{M_1,M_2,i}^{(s_1,s_2)}(z_1,z_{c+i+1})
\end{aligned}$$

Take $N \to \infty$, we have $$\begin{aligned}
\psi_{i}^{(s_1,s_2)} (z_1, z_{i+1})
&= \frac{1}{2\pi i} \left[ - 2\pi i(s_2 -1)(2\pi i z_1 + 2\pi i z_{i+1} )  \right.\\
&\qquad + \Li\left(e^{2\pi i (s_2-1) - 2\pi i z_1 - 2\pi i z_{i+1}}\right) - \Li\left( e^{2\pi i (s_2-1) - 2\pi i z_{i+1} }\right) \\
&\qquad \left. + \Li \left(e^{2\pi i z_{i+1}}\right) - \Li\left(e^{2\pi iz_1+ 2\pi i z_{i+1}}\right) + \Li\left(e^{2\pi i z_1}\right) \right] ,\\
\kappa_i^{(s_1,s_2)}(z_1,z_{c+i+1}) 
&= \frac{1}{2\pi i} [ 2\pi i(s_2 -1)(2\pi i z_1 + 2\pi i z_{c+i+1} ) \\
&\qquad - \Li\left(e^{-2\pi i (s_2-1) + 2\pi i z_1 + 2\pi i z_{c+i+1}}\right) + \Li\left( e^{-2\pi i (s_2-1) + 2\pi i z_{c+i+1} }\right) \\
&\qquad - \Li \left(e^{-2\pi i z_{c+i+1}}\right) + \Li\left(e^{-2\pi iz_1- 2\pi i z_{c+i+1}}\right) - \Li\left(e^{-2\pi i z_1}\right) ]
\end{aligned}$$ and $$\begin{aligned}
&\Phi^{\pm (s_1,s_2);a,c,d}  (z_1, z_2,z_3, \dots, z_{c+1}, z_{c+2},\dots, z_{c+d+1})  \\
&=  \frac{1}{2\pi i} \left\{  \pm2\pi i  \left( s_2 - 1\right) \left(2\pi i \left(z_1 -\frac{1}{2} \right)\right)
 + a \left[2\pi i \left(z_1-\frac{1}{2} \right) \right]^2  \right\} \\
&\qquad + \sum_{i=1}^c \psi^{(s_1,s_2)}_i (z,z_{i+1}) + \sum_{i=1}^d \kappa_i^{(s_1,s_2)}(z_1,z_{c+i+1})
\end{aligned}$$

As an analogue of Lemma [\[EM_2\]](#EM_2){reference-type="ref" reference="EM_2"}, we let $$\begin{aligned}
R_{M_2}(z_1,z_2) 
&= \frac{1}{2}\left[ \log\left(1-e^{-2\pi i \left(\frac{M_2}{N+\frac{1}{2}}-1\right) + 2\pi i z_1 + 2\pi i z_2 }\right)
- \log\left(1-e^{-2\pi i \left(\frac{M_2}{N+\frac{1}{2}}-1\right) + 2\pi i z_2 } \right) \right.\notag\\
&\left.\qquad - \log\left(1- e^{-2\pi i z_2 } \right)
+ \log\left(1- e^{-2\pi iz_1- 2\pi i z_2} \right) 
- \log\left(1-  e^{-2\pi i z_1 } \right) \right]
\end{aligned}$$

Following the proof of Lemma [\[EM_2\]](#EM_2){reference-type="ref" reference="EM_2"}, we have

::: lemma
[]{#EM_2' label="EM_2'"} On any compact subset of $$\left\{ (z_1,z_2,\dots,z_{c+d+1}) \in {\mathbb C}\mid \Re z_1 , \dots, \Re z_{c+d+1} >0, \Re z_1 + \Re z_k < s_2 \text{ for }k=2,\dots, c+d+1\right\},$$ we have $$\begin{aligned}
&\Phi^{\pm(s_1,s_2);a,c,d}_{M_1,M_2} (z_1, z_2,z_3, \dots, z_{c+1}, z_{c+2},\dots, z_{c+d+1}) \notag\\
&= \Phi^{\pm (s_1,s_2);a,c,d}  (z_1, z_2,z_3, \dots, z_{c+1}, z_{c+2},\dots, z_{c+d+1}) \notag\\
&\qquad+\frac{1}{N+\frac{1}{2}}E_{M_2}^{a,c,d} (z_1, z_2,z_3, \dots, z_{c+1}, z_{c+2},\dots, z_{c+d+1})+ O\left(\frac{1}{\left(N+\frac{1}{2}\right)^2}\right),
\end{aligned}$$ where $$\begin{aligned}
&\quad E_{M_2}^{a,c,d} (z_1, z_2,z_3, \dots, z_{c+1}, z_{c+2},\dots, z_{c+d+1})\notag\\
&= -4\pi^2 a \left(z_1-\frac{1}{2}\right) + \sum_{i=1}^c E_{M_2}(z_1,z_i+1) + \sum_{i=1}^d R_{M_2}(z_1,z_{c+i+1})
\end{aligned}$$
:::

Note that $$\begin{aligned}
\frac{\partial}{\partial z_1}  \psi_i (z_1,z_{i+1})
&=  \log(1-e^{2\pi i (s_2-1)}e^{-2\pi i z_1 - 2\pi i z_{i+1}}) + \log(1 - e^{2\pi i z_1 + 2\pi i z_{i+1} }) - \log(1 - e^{2\pi i z_1}) \notag \\
& \qquad  -2\pi i(s_2 - 1)\\
\frac{\partial}{\partial z_{i+1}}  \psi_i (z_1,z_{i+1})
&= \log(1-e^{2\pi i (s_2 -1)}e^{-2\pi i z_1 - 2\pi i z_{i+1}}) + \log(1 - e^{2\pi i z_1 + 2\pi i z_{i+1}}) \notag\\
&\quad   - \log(1 - e^{2\pi i (s_2 - 1) - 2\pi i z_{i+1}}) - \log(1 - e^{2\pi i z_{i+1}})  -2\pi i(s_2 - 1)  \\
\frac{\partial}{\partial z_1}  \kappa_i (z_1,z_{c+i+1})
&=  \log(1-e^{-2\pi i (s_2-1)}e^{2\pi i z_1 + 2\pi i z_{c+i+1}}) + \log(1 - e^{-2\pi i z_1 - 2\pi i z_{c+i+1} }) \notag\\
& \qquad - \log(1 - e^{-2\pi i z_1})  +2\pi i(s_2 - 1)\\
\frac{\partial}{\partial z_{c+i+1}}  \kappa_i (z_1,z_{c+i+1})
&= \log(1-e^{-2\pi i (s_2 -1)}e^{2\pi i z_1 + 2\pi i z_{c+i+1}}) + \log(1 - e^{-2\pi i z_1 - 2\pi i z_{c+i+1}}) \notag\\
&\quad   - \log(1 - e^{-2\pi i (s_2 - 1) + 2\pi i z_{c+i+1}}) - \log(1 - e^{-2\pi i z_{c+i+1}})  + 2\pi i(s_2 - 1)  
\end{aligned}$$

As a result, the critical point equations for the potential function $\Phi^{\pm (s_1,s_2);a,c,d}(z_1, z_2,z_3, \dots, z_{c+d+1})$ are given by

::: empheq
align &\_i=1\^c\
&+ \_i=1\^d\
&= 2i[]{#sbm1 label="sbm1"}\
\
&(1-e\^2i (s_2 -1)e\^-2i z_1 - 2i z\_i+1) + (1 - e\^2i z_1 + 2i z\_i+1)\
&- (1 - e\^2i (s_2 - 1) - 2i z\_i+1) - (1 - e\^2i z\_i+1)\
&= 2i (s_2 - 1)\
\
&(1-e\^-2i (s_2 -1)e\^2i z_1 + 2i z\_c+i+1) + (1 - e\^-2i z_1 - 2i z\_c+i+1)\
&- (1 - e\^-2i (s_2 - 1) + 2i z\_c+i+1)- (1 - e\^-2i z\_c+i+1)\
&= -2i (s_2 - 1)
:::

Put $Z_{i}=e^{2\pi i z_{i}}$, $U_i = \frac{1}{Z_1 Z_{i+1}}$ and $B_l = e^{2\pi i s_l}$ for $i=1,2,\dots, c+d$ and $l = 1,2$. After taking exponential, we have

::: empheq
align (Z_1\^2)\^a&= B_1\^\
&= B_2\
&= B_2\^-1
:::

## Asymptotics of $J_{N, N}(W_{a,1,c,d},e^{\frac{2\pi i}{N+\frac{1}{2}}})$

When $M_1=M_2=N$, the potential function becomes $$\begin{aligned}
&\Phi^{(1,1);a,c,d}  (z_1, z_2,z_3, \dots, z_{c+d+1})\\ 
&=  \frac{1}{2\pi i} \left(  a \left(2\pi i \left(z_1-\frac{1}{2} \right) \right)^2  \right)
 + \sum_{i=1}^c \psi^{(1,1)}_i (z_1,z_{i+1}) + \sum_{i=1}^d \kappa_i^{(1,1)}(z_1,z_{c+i+1})
\end{aligned}$$ Besides, the critical point equations of the potential function are given by

::: empheq
align & \_i=1\^c\
& - \_i=1\^d\
&= -4i a(z_1 - ) []{#a1cd1 label="a1cd1"}\
\
& (1-e\^-2i z_1 - 2i z\_i+1) + (1 - e\^2i z_1 + 2i z\_i+1) - (1 - e\^ - 2i z\_i+1) - (1 - e\^2i z\_i+1)\
& = 0 []{#a1cd2 label="a1cd2"}\
\
& (1-e\^2i z_1 + 2i z\_c+i+1) + (1 - e\^-2i z_1 - 2i z\_c+i+1) - (1 - e\^ 2i z\_i+1) - (1 - e\^-2i z\_c+i+1)\
& = 0 []{#a1cd3 label="a1cd3"}
:::

It is straightforward to verify that $(z_1,z_2,\dots,z_c, z_{c+1},\dots, z_{c+d+1}) = \left(\frac{1}{2},\frac{1}{4},\dots, \frac{1}{4}\right)$ is a solution of equations ([\[a1cd1\]](#a1cd1){reference-type="ref" reference="a1cd1"}) - ([\[a1cd3\]](#a1cd3){reference-type="ref" reference="a1cd3"}). Besides, it is the unique maximum point on the region $$D = \{ (z_1,\dots, z_{c+d+1})\in [0,1]^{c+d+1} \mid z_1 + z_i \leq 1 \text{ for $i=2,\dots, c+d+1$} \}$$ Moreover, since $$\begin{aligned}
\psi^{(1,1)}_i \left( \frac{1}{2}, \frac{1}{4} \right) &= \frac{1}{2\pi i} [2\Li (i) - 2\Li(-i) + \Li(-1)] = \frac{1}{2\pi} \left[ 8L \left(\frac{\pi}{4}\right) + \frac{\pi^2 i}{12} \right] \\
\kappa^{(1,1)}_i \left( \frac{1}{2}, \frac{1}{4} \right) &= \frac{1}{2\pi i} [2\Li (i) - 2\Li(-i) - \Li(-1)] = \frac{1}{2\pi} \left[ 8L \left(\frac{\pi}{4}\right) - \frac{\pi^2 i}{12} \right] 
\end{aligned}$$ the critical value is given by $$\begin{aligned}
\Phi^{(1,1);a,c,d} \left(\frac{1}{2},\frac{1}{4},\dots, \frac{1}{4}\right)
= \frac{1}{2\pi i} \sum_{i=1}^c \psi_i \left(\frac{1}{2},\frac{1}{4}\right) + \frac{1}{2\pi i} \sum_{i=1}^d \kappa_i \left(\frac{1}{2},\frac{1}{4} \right)
= \frac{1}{2\pi} \left[8(c+d)L\left(\frac{\pi}{4}\right) + (c-d)\frac{\pi^2 i}{12} \right]
\end{aligned}$$ Besides, by Lemma A.3 of [@O52], we have $$\begin{aligned}
\label{QDFcoe}
\exp\left(-\phi^h \left( \frac{\pi}{2N+1} \right) \right) 
&\stackrel[N \to \infty]{\sim}{ } e^{-\frac{\pi i}{4}}(N+\frac{1}{2})^{-\frac{1}{2}}\exp\left( \frac{N+\frac{1}{2}}{2\pi} \frac{\pi^2 i}{6} \right) \\
\exp\left(\phi^h \left(\pi - \frac{\pi}{2N+1} \right) \right) 
&\stackrel[N \to \infty]{\sim}{ } e^{\frac{\pi i}{4}}(N+\frac{1}{2})^{-\frac{1}{2}}\exp\left( \frac{N+\frac{1}{2}}{2\pi} \left(\frac{-\pi^2 i}{6}\right) \right)
\end{aligned}$$

Nevertheless, the Hessian of $\Phi^{(1,1);a,c,d}(\frac{1}{2},\frac{1}{4},\dots, \frac{1}{4})$ is given by $$\Hess\left(\Phi^{(1,1);a,c,d}\left(\frac{1}{2},\frac{1}{4},\dots, \frac{1}{4}\right)\right) = 2\pi i
\begin{pmatrix}
    (c+d)i - \frac{c-d}{2} +2a & i  & i & i &\dots  & i\\
    i & 2i  & 0 & 0 &\dots  &0\\
    i & 0& 2i &0 &\dots  &0\\
    &&&\vdots\\
    i & 0 & 0 &\dots &0 & 2i\\
\end{pmatrix}$$ For any $a_1,a_2,a_3 \in {\mathbb C}$, one can verify that the determinant of the $(c+d+1)\times (c+d+1)$ matrix $$\begin{pmatrix}
a_1&a_2&a_2&a_2&\dots&a_2 \\
a_2&a_3&0&0&\dots&0 \\
a_2&0&a_3&0&\dots&0 \\
\vdots&\vdots&\vdots&\vdots&\vdots\\
a_2&0&0&0&\dots&0 \\
a_2&0&0&0&\dots&a_3
\end{pmatrix}$$ is given by $$\begin{vmatrix}
a_1&a_2&a_2&a_2&\dots&a_2 \\
a_2&a_3&0&0&\dots&0 \\
a_2&0&a_3&0&\dots&0 \\
\vdots&\vdots&\vdots&\vdots&\vdots\\
a_2&0&0&0&\dots&0 \\
a_2&0&0&0&\dots&a_3
\end{vmatrix}
=
a_3^{c+d-1}[a_1a_3-(c+d)a_2^2]$$ In particular, if we put $a_1=(c+d)i - \frac{c-d}{2}+2a, a_2=i$ and $a_3=2i$, one can show that $$\begin{aligned}
\det\left(-\Hess\left(\Phi^{(1,1);a,c,d}\left(\frac{1}{2},\frac{1}{4},\dots, \frac{1}{4}\right)\right) \right)
\neq 0
\end{aligned}$$ for any $a\in {\mathbb Z}, c,d\in {\mathbb N}\cup\{0\}$ with $c+d\geq 1$. Theorem [\[CJWNN\]](#CJWNN){reference-type="ref" reference="CJWNN"} then follows by similar argument as in Section [\[WLNN\]](#WLNN){reference-type="ref" reference="WLNN"}.

## Triangulation of the ${\mathbb S}^3\backslash W_{0,1,c,0}$

The triangulation of ${\mathbb S}^3 \backslash WL_{0,1,c,0}$ is similar to that for the Whitehead link complement. First of all, we prepare $c$ ideal octahedra. Next, we glue the top of the cylinder to the bottom of the next cylinder by the rule $C_2 \to C_1$ and $A_2 \to A_1$ (Figure [1](#f14){reference-type="ref" reference="f14"}), then we obtain a decomposition of the boundary torus into paralleograms. Note that this torus is exactly the boundary torus of a tubular neighborhood of the belt component of $WL_{0,1,c,0}$.\

![decomposition of the boundary torus into parallelograms](f14){#f14 width="0.8\\linewidth"}

Originally, each tetrahedron has its own assignment of shape parameters $Z_1=e^{2\pi i z_1}, W_i=e^{2\pi i z_{i+1}}$ and $U_i=\frac{1}{Z_1W_i}$. If we put $z_1=z_2=\dots=z_{c+1}=z$, $w_1=w_1=\dots=w_{c+1}=w$ and $u_1=u_2=\dots=u_{c+1}=u$, by similar calculation in Section [\[geoWL\]](#geoWL){reference-type="ref" reference="geoWL"}, one can verify that the edges equations can be reduced to a single equation $$\begin{aligned}
\left(\frac{U'}{W'} \right) \left( \frac{(B_2 U)''}{(B_2^{-1}W)''}\right) = 1
\end{aligned}$$

On the other hand, the critical point equations for the potential function $\Phi^{(1,1);0,c,0}  (z_1, z_2,z_3, \dots, z_{c+1})$ are given by

::: empheq
align &\_i=1\^c\
&= 2i[]{#W01c01 label="W01c01"}\
\
&(1-e\^2i (s_2 -1)e\^-2i z_1 - 2i z\_i+1) + (1 - e\^2i z_1 + 2i z\_i+1)\
&- (1 - e\^2i (s_2 - 1) - 2i z\_i+1) - (1 - e\^2i z\_i+1)\
&= 2i (s_2 - 1) []{#W01c02 label="W01c02"}
:::

By similar argument in Section [\[geoWL\]](#geoWL){reference-type="ref" reference="geoWL"}, one can show that the holonomy of the meridian of the belt component and the holonomy of the longitude of every clasps components are exactly $B_1$ and $B_2$ respectively. Theorem [\[mainthmWa1c0\]](#mainthmWa1c0){reference-type="ref" reference="mainthmWa1c0"} then follows from similar arguments in Section [\[WLs\]](#WLs){reference-type="ref" reference="WLs"}-[\[geoWL\]](#geoWL){reference-type="ref" reference="geoWL"}.

# Volume conjecture for $TV_r(W_{a,b,c,d}, e^{\frac{2\pi i}{r}})$ with $b\geq 1$ {#TV}

Let $r=2N+1$. Recall from Theorem [\[relationship\]](#relationship){reference-type="ref" reference="relationship"} that the $r$-th Turaev-Viro invariants for the link complement ${\mathbb S}^3 \backslash L$ is related to the colored Jones polynomials of the link as follows: $$\begin{aligned}
TV_{r}\left({\mathbb S}^3 \backslash L, e^{\frac{2\pi i}{r}}\right) = 2^{n-1}\left( \frac{2\sin(\frac{2\pi}{r})}{\sqrt{r}}\right)^{2} \sum_{1\leq \vec{M} \leq \frac{r-1}{2}}\left|{J}_{\vec{M}}\left(L,e^{\frac{2\pi i }{N+\frac{1}{2}}}\right)\right|^2 ,
\end{aligned}$$ From the formula of $J_{\vec{M}}(W_{a,b,c,d},e^{\frac{2\pi i}{N+\frac{1}{2}}})$, it is easy to see that the colored Jones polynomials of the belt tangle and twist tangle grow at most polynomially. Thus, in order to find an upper bound for the exponential growth rate of $J_{\vec{M}}(W_{a,b,c,d},e^{\frac{2\pi i}{N+\frac{1}{2}}})$, we only need to find that for the clasp tangle $\tilde{C}(n,e^{\frac{2\pi i}{N+\frac{1}{2}}}; M_2)$.

::: lemma
[]{#uppbdW label="uppbdW"} For any $n \in \{1,2,\dots,M-1\}$, $l \in \{1,2,\dots, M-1-n\}$, let $$c_{M}(n,l;t) = \prod_{j=1}^{n} \left|\frac{(1-t^{M-l-j})(1-t^{l+j})}{1-t^j}\right|$$ For each $M$, let $n_M\in \{1,2,\dots,M-1\}$ and $l_M \in \{1,2,\dots, M-1-n\}$ such that $c_M(n_M,l_M)$ achieves the maximum among all $c_{M}(n,l)$. Assume that $\frac{M}{N+\frac{1}{2}} \to s \in [0,1]$, $\frac{n_M}{N+\frac{1}{2}} \to n_s$ and $\frac{l_M}{N+\frac{1}{2}} \to l_s$. Then we have $$\lim_{N \to \infty} \frac{1}{N+\frac{1}{2}} \log(c_M(n,l;e^{\frac{2\pi i}{N+\frac{1}{2}}})) \leq \frac{\operatorname{Vol}({\mathbb S}^3\backslash WL)}{2\pi}$$ Furthermore, the equality holds if and only if $s=1, n_s = \frac{1}{2} \text{ and } l_s = \frac{1}{4}$.
:::

::: proof
*Proof.* Define $$f(x,y,s) = \frac{1}{\pi}[\Lambda(\pi s - \pi x - \pi y) - \Lambda(\pi s - \pi y) + \Lambda(\pi y) - \Lambda(\pi x + \pi y) + \Lambda(\pi x)],$$ where $\Delta_s=\{(x,y,s) \in {\mathbb R}^3 \mid 0\leq x,y \leq \pi, 0\leq x + y \leq s, s\in [0,1]\}$. One can show that when $$s=\lim_{N\to \infty} \frac{M}{N+\frac{1}{2}}, x=\lim_{N\to\infty} \frac{n}{N+\frac{1}{2}} \text{ and } y=\lim_{N\to\infty} \frac{l}{N+\frac{1}{2}},$$ we have $$\lim_{N \to \infty} \frac{1}{N+\frac{1}{2}} \log(c_M(n,l;e^{\frac{2\pi i}{N+\frac{1}{2}}})) = f(x,y,s)$$ In order to find out the maximum of $f$ inside the region $\Delta_s$, we will first find out all the critical point of $f$ on $\Delta_s$, and then estimate the value of $f$ along the boundary. Note that

::: empheq
align f_x &= \|2(s - x - y)\| + \|2(x + y)\| - \|2(x)\|\
f_y &= \|2(s - x - y)\| - \|2 (s - y)\| - \|2(y)\| + \|2(x + y)\|\
f_s &= -\|2(s - x - y)\| + \|2(s - y)\|
:::

1.  To find out the critical point of $f$, note that $$\begin{aligned}
    {2}
    f_s = 0 
    &\implies \log|2\sin(\pi s - \pi x - \pi y)| = \log|2\sin(\pi s - \pi y)|  \label{*}\\
    &\implies \qquad\qquad\qquad\qquad x=0 \quad\text{or} \quad x+2y = 2s-1 \label{**}
    \end{aligned}$$ By putting ([\[\*\]](#*){reference-type="ref" reference="*"}) into the equation $f_y=0$, we get $x=0$ or $x+2y=1$. As a result, $f_y=f_s=0$ imply $x=0$ or $s=1$. In both cases, the critical point lies on the boundary.

2.  To estimate the value of $f$ along the boundary, note that

    1.  on the boundary where $s=1$, $(x,y,s) = \left(\frac{1}{2}, \frac{1}{4}, 1 \right)$ is a unique maximum point with maximum value $f\left(\frac{1}{2}, \frac{1}{4}, 1 \right) = \frac{1}{2\pi} \operatorname{Vol}({\mathbb S}^3 \backslash WL)$.

    2.  on the boundary where $x=0$, we have $f(0,y,s)=0$.

    3.  when $y=0$ or $x+y=s$, the function $f$ is given by

        ::: empheq
        align\* f(x,0,s) &= \[(s - x) - (s)\]\
        f(x,s-x,s) &= \[((y) - (s)\]
        :::

        In both cases, we have $$|f| \leq \frac{1}{\pi} \left[ 2\Lambda\left(\frac{\pi}{3}\right)\right] \leq \frac{1}{2\pi}\left[6\Lambda\left(\frac{\pi}{3}\right)\right] = \frac{1}{2\pi} \operatorname{Vol}({\mathbb S}^3 \backslash 4_1) < \frac{1}{2\pi} \operatorname{Vol}({\mathbb S}^3 \backslash WL)$$

    where the last inequality follows from the fact that the figure eight knot complement can be obtained by doing surgery along the belt component of the Whitehead link. This completes the proof.

 ◻
:::

From Theorem [\[relationship\]](#relationship){reference-type="ref" reference="relationship"} and Lemma [\[uppbdW\]](#uppbdW){reference-type="ref" reference="uppbdW"}, we can see that $$\begin{aligned}
\limsup_{\substack{ r\to \infty \\r \text{ odd}}}\frac{2\pi}{r}\log \left(TV_{r}({\mathbb S}^3\backslash W_{a,b,c,d},e^{\frac{2\pi i}{r}})\right) 
\leq (c+d)\operatorname{Vol}({\mathbb S}^3\backslash WL) = \operatorname{Vol}({\mathbb S}^3\backslash W_{a,b,c,d})
\end{aligned}$$

Besides, from Theorem [\[relationship\]](#relationship){reference-type="ref" reference="relationship"} and Theorem [\[CJWNN\]](#CJWNN){reference-type="ref" reference="CJWNN"}, for $r=2N+1$, since $$\begin{aligned}
\frac{2\pi}{r}\log \left(TV_{r}({\mathbb S}^3\backslash W_{a,b,c,d},e^{\frac{2\pi i}{N+\frac{1}{2}}})\right) 
&\geq \frac{2\pi}{r}\log \left| J_{\vec{N}}\left(({\mathbb S}^3\backslash W_{a,1,c,d},e^{\frac{2\pi i}{r}})\right) \right|^2 
\end{aligned}$$ and $$\begin{aligned}
\lim_{N\to \infty}\frac{2\pi}{2N+1}\log \left| J_{\vec{N}}\left(({\mathbb S}^3\backslash W_{a,1,c,d},e^{\frac{2\pi i}{N+\frac{1}{2}}})\right) \right|^2 &= \operatorname{Vol}({\mathbb S}^3\backslash W_{a,1,c,d}) = v_3||{\mathbb S}^3\backslash W_{a,b,c,d}||,
\end{aligned}$$ Corollary [\[TVW\]](#TVW){reference-type="ref" reference="TVW"} follows from squeeze theorem.

[^1]: when $c+d=1$, there is an extra factor $t^{\frac{M_2^2-1}{2}}$ coming from the framing. Since it does not affect the exponential growth rate of the colored Jones polynomials, for simplicity we ignore this factor.

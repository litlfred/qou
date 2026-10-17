---
doc_id: arxiv-1110.6212v2
doc_title: "On calibrated representations and the Plancherel Theorem for aﬃne Hecke algebras"
section_id: sec-011-31-the-rank-1-algebras
section_title: "The rank 1 algebras"
section_number: 3.1
pages: 16-31
source_pdf: 1110.6212v2.pdf
source_sha256: 1923b6a0bfdc810f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.993
doc_brief: "On calibrated representations and the Plancherel Theorem for aﬃne Hecke algebras — This paper has two main purposes."
---
\noindent(1) The $\tilde{A}_1(q)$, $L=Q$, algebra has generators $T=T_1$ and $x=x^{\alpha_1^{\vee}}$ with relations
\begin{align*}
T^2=1+(q^{\frac{1}{2}}-q^{-\frac{1}{2}})T,\qquad
Tx=x^{-1}T+(q^{\frac{1}{2}}-q^{-\frac{1}{2}})(1+x).
\end{align*}
Let $\pi_t=\mathrm{Ind}_{\CC[Q]}^{\scH}(\CC v_t)$ be the principal series representation with central character~$t\in\CC^{\times}$, where $x\cdot v_t=t v_t$. Let $\pi$ be the $1$-dimensional representation of $\scH$ with 
$$
\pi(T)=-q^{-\frac{1}{2}}\qquad\textrm{and}\qquad \pi(x)=q^{-1}.
$$
Let $\chi_t$ be the character of $\pi_t$ and let $\chi$ be the character of $\pi$.
\smallskip

\noindent(2) The $\tilde{A}_1(q)$, $L=P$, algebra has generators $T=T_1$ and $x=x^{\omega_1}$ with relations
\begin{align*}
T^2=1+(q^{\frac{1}{2}}-q^{-\frac{1}{2}})T,\qquad
Tx=x^{-1}T+(q^{\frac{1}{2}}-q^{-\frac{1}{2}})x.
\end{align*}
Let
$
\pi_t=\mathrm{Ind}_{\CC[P]}^{\scH}(\CC v_t)
$
be the principal series representation with central character~$t\in\CC^{\times}$, where $x\cdot v_t=t v_t$. Let $\pi^1$ and $\pi^2$ be the $1$-dimensional representations of $\scH$ with 
$$
\pi^1(T)=-q^{-\frac{1}{2}},\quad\pi^1(x)=q^{-\frac{1}{2}},\qquad\textrm{and}\qquad\pi^2(T)=-q^{-\frac{1}{2}},\quad \pi^2(x)=-q^{-\frac{1}{2}}.
$$
Let $\chi_t$, $\chi^1$, and $\chi^2$ be the characters of $\pi_t$, $\pi^1$, and $\pi^2$ (respectively).
\smallskip

\noindent(3) The $\tilde{BC}_1(q_0,q_1)$, $L=Q$, algebra has generators $T=T_1$, $x=x^{\alpha_1^{\vee}/2}$ with relations
\begin{align*}
T^2=1+(q_1^{\frac{1}{2}}-q_1^{-\frac{1}{2}})T,\qquad
Tx=x^{-1}T+(q_1^{\frac{1}{2}}-q_1^{-\frac{1}{2}})x+(q_0^{\frac{1}{2}}-q_0^{-\frac{1}{2}}).
\end{align*}
Let $\pi_t=\mathrm{Ind}_{\CC[Q]}^{\scH}(\CC v_t)$ be the principal series representation with central character~$t\in\CC^{\times}$, where $x\cdot v_t=t v_t$. Let $\pi^{1}$, $\pi^{2}$ and $\pi^{3}$ be the $1$-dimensional representations of $\scH$ with 
$$
\begin{aligned}
\pi^1(T)&=-q_1^{-\frac{1}{2}}\\
\pi^1(x)&=q_0^{-\frac{1}{2}}q_1^{-\frac{1}{2}}
\end{aligned}\qquad
\begin{aligned}
\pi^2(T)&=-q_1^{-\frac{1}{2}}\\
\pi^2(x)&=-q_0^{\frac{1}{2}}q_1^{-\frac{1}{2}}
\end{aligned}\qquad
\begin{aligned}
\pi^{3}(T)&=q_1^{\frac{1}{2}}\\
\pi^3(x)&=-q_0^{-\frac{1}{2}}q_1^{\frac{1}{2}}
\end{aligned}
$$
Let $\chi_t$, $\chi^1$, $\chi^2$, and $\chi^3$ be the characters of $\pi_t$, $\pi^1$, $\pi^2$, and $\pi^3$ (respectively).


\begin{thm} Let $h\in\scH$. In the cases (1), (2) and (3) above we have, respectively:
\begin{align*}
\Tr(h)&=\frac{1}{2q}\int_{\TT}\frac{\chi_t(h)}{|c(t)|^2}\,dt+\frac{q-1}{q+1}\chi(h)\\
\Tr(h)&=\frac{1}{2q}\int_{\TT}\frac{\chi_t(h)}{|c(t)|^2}\,dt+\frac{q-1}{2(q+1)}\left(\chi^{1}(h)+\chi^{2}(h)\right)\\
\Tr(h)&=\frac{1}{2q_1}\int_{\TT}\frac{\chi_t(h)}{|c(t)|^2}\,dt+\frac{q_0q_1-1}{(q_0+1)(q_1+1)}\chi^{1}(h)+\frac{|q_0-q_1|}{(q_0+1)(q_1+1)}\times\begin{cases}\chi^2(h)&\textrm{if $q_0<q_1$}\\
\chi^3(h)&\textrm{if $q_1<q_0$},
\end{cases}
\end{align*}
where the $c$-functions are (respectively)
\begin{align*}
c(t)&=\frac{1-q^{-1}t^{-1}}{1-t^{-1}},&
c(t)&=\frac{1-q^{-1}t^{-2}}{1-t^{-2}},&
c(t)&=\frac{(1-q_0^{-\frac{1}{2}}q_1^{-\frac{1}{2}}t^{-1})(1+q_0^{\frac{1}{2}}q_1^{-\frac{1}{2}}t^{-1})}{1-t^{-2}}.
\end{align*}
\end{thm}
 
\begin{proof} Let us prove the $\tilde{BC}_1(q_0,q_1)$ case. If $q_0=q_1$ there is some simplification, so suppose that $q_0\neq q_1$. Write $g(t)=g_t(h)$ and $f(t)=f_t(h)$. From (\ref{eq:prelim_main}) we have
$$
\Tr(h)=\frac{1}{q_1}\int_{q_0^{-\frac{1}{2}}q_1^{-\frac{1}{2}}a\TT}\frac{f(t)}{c(t)c(t^{-1})}\,dt
$$
where $0<a<1$. Note that the integrand has at most removable singularities on~$t\in\TT$, and that the poles of the integrand that lie between the contours $q_0^{-\frac{1}{2}}q_1^{-\frac{1}{2}}a\TT$ and $\TT$ are at $t=q_0^{-\frac{1}{2}}q_1^{-\frac{1}{2}}$, $t=-q_0^{\frac{1}{2}}q_1^{-\frac{1}{2}}$ (in the case that $q_0<q_1$) and $t=-q_0^{-\frac{1}{2}}q_1^{\frac{1}{2}}$ (in the case that $q_1<q_0$). Computing residues (using $dt=\frac{1}{2\pi}d\theta=\frac{1}{2\pi i}\frac{dz}{z}$) gives
$$
\Tr(h)=
\frac{1}{q_1}\int_{\TT}\frac{f(t)}{|c(t)|^2}\,dt+\frac{q_0q_1-1}{(q_0+1)(q_1+1)}f(q_0^{-\frac{1}{2}}q_1^{-\frac{1}{2}})+\frac{|q_0-q_1|}{(q_0+1)(q_1+1)}\cdot
\begin{cases}
f(-q_0^{\frac{1}{2}}q_1^{-\frac{1}{2}})&\textrm{if $q_0<q_1$}\\
f(-q_0^{-\frac{1}{2}}q_1^{\frac{1}{2}})&\textrm{if $q_1<q_0$}.
\end{cases}
$$
Using Proposition~\ref{prop:prelim_main} we have
$$
\frac{1}{q_1}\int_{\TT}\frac{f(t)}{|c(t)|^2}\,dt=\frac{1}{2q_1}\int_{\TT}\frac{f(t)+f(t^{-1})}{|c(t)|^2}\,dt=\frac{1}{2q_1}\int_{\TT}\frac{\chi_t(h)}{|c(t)|^2}\,dt,
$$
and Lemma~\ref{lem:1dim} gives $f(q_0^{-\frac{1}{2}}q_1^{-\frac{1}{2}})=\chi^1(h)$, $f(-q_0^{\frac{1}{2}}q_1^{-\frac{1}{2}})=\chi^2(h)$, and $f(-q_0^{-\frac{1}{2}}q_1^{\frac{1}{2}})=\chi^3(h)$.
\end{proof}




\subsection{The $\tilde{A}_2(q)$ algebras with $L=Q$}\label{sect:A2Q}

This case is treated in \cite{PS}, and so we will just state the result here. The coroot system is 
$
R=\pm\{\alpha_1^{\vee},\alpha_2^{\vee},\alpha_1^{\vee}+\alpha_2^{\vee}\}
$.
The affine Hecke algebra has generators $T_1,T_2,x_1=x^{\alpha_1^{\vee}},x_2=x^{\alpha_2^{\vee}}$ and relations
\begin{align*}
T_1^2&=1+(q^{\frac{1}{2}}-q^{-\frac{1}{2}})T_1& T_1x_1&=x_1^{-1}T_1+(q^{\frac{1}{2}}-q^{-\frac{1}{2}})(1+x_1) & T_1T_2T_1&=T_2T_1T_2\\
T_2^2&=1+(q^{\frac{1}{2}}-q^{-\frac{1}{2}})T_2 & T_2x_2&=x_2^{-1}T_2+(q^{\frac{1}{2}}-q^{-\frac{1}{2}})(1+x_2)& x_1x_2&=x_2x_1\\
T_1x_2&=x_1x_2T_1^{-1} & T_2x_1&=x_1x_2T_2^{-1}.
\end{align*}

Let $\pi_t=\mathrm{Ind}_{\CC[Q]}^{\scH}(\CC v_t)$ be the principal series representation of the affine Hecke algebra~$\scH$ with central character~$t=(t_1,t_2)\in(\CC^{\times})^2$, where $\CC v_t$ is the $1$-dimensional representation of $\CC[Q]$ with $x_1\cdot v_t=t_1v_t$ and $x_2\cdot v_t=t_2v_t$. 

Let $\scH_1$ be the subalgebra of $\scH$ generated by $T_1,x_1$ and~$x_2$. Let $s\in\CC^{\times}$ and let $\CC u_s$ be the $1$-dimensional representation of $\scH_1$ with
\begin{align*}
T_1\cdot u_s&=-q^{-\frac{1}{2}}u_s,& x_1\cdot u_s&=q^{-1}u_s,& x_2\cdot u_s&=q^{\frac{1}{2}}s u_s.
\end{align*}
Let
$
\pi_s^{1}=\mathrm{Ind}_{\scH_1}^{\scH}(\CC u_s)
$ be the induced representation of $\scH$. 

Let $\pi^{2}$ be the $1$-dimensional representation of $\scH$ with 
\begin{align*}
\pi^{2}(T_1)&=-q^{-\frac{1}{2}},&\pi^{2}(T_2)&=-q^{-\frac{1}{2}},&\pi^{2}(x_1)&=q^{-1},&\pi^{2}(x_2)&=q^{-1}.
\end{align*}
Let $\chi_t$, $\chi_s^1$, and $\chi^2$ be the characters of $\pi_t$, $\pi_s^1$, and $\pi^2$ (respectively). 


\begin{thm} for all $h\in\scH$ we have 
$$
\Tr(h)=\frac{1}{6q^3}\int_{\TT^2}\frac{\chi_t(h)}{|c(t)|^2}\,dt+\frac{(q-1)^2}{q^2(q^2-1)}\int_{\TT}\frac{\chi_s^{1}(h)}{|c_1(s)|^2}\,ds+\frac{(q-1)^3}{q^3-1}\chi^{2}(h),
$$
where 
\begin{align*}
c(t)&=\frac{(1-q^{-1}t_1^{-1})(1-q^{-1}t_2^{-1})(1-q^{-1}t_1^{-1}t_2^{-1})}{(1-t_1^{-1})(1-t_2^{-1})(1-t_1^{-1}t_2^{-1})},&c_1(s)&=\frac{1-q^{-\frac{3}{2}}s^{-1}}{1-q^{\frac{1}{2}}s^{-1}}.
\end{align*}
\end{thm}



\subsection{The $\tilde{A}_2(q)$ algebras with $L=P$}


The root system is as in Section~\ref{sect:A2Q}. The fundamental coweights are $\omega_1=\frac{2}{3}\alpha_1^{\vee}+\frac{1}{3}\alpha_2^{\vee}$ and $\omega_2=\frac{1}{3}\alpha_1^{\vee}+\frac{2}{3}\alpha_2^{\vee}$, and the coweight lattice is $P=\ZZ\omega_1+\ZZ\omega_2$. The affine Hecke algebra is generated by $T_1$, $T_2$, $x_1=x^{\omega_1}$ and $x_2=x^{\omega_2}$ with relations
\begin{align*}
T_1^2&=1+(q^{\frac{1}{2}}-q^{-\frac{1}{2}})T_1& T_1x_1&=x_1^{-1}x_2T_1+(q^{\frac{1}{2}}-q^{-\frac{1}{2}})x_1 & T_1T_2T_1&=T_2T_1T_2\\
T_2^2&=1+(q^{\frac{1}{2}}-q^{-\frac{1}{2}})T_2 & T_2x_2&=x_1x_2^{-1}T_2+(q^{\frac{1}{2}}-q^{-\frac{1}{2}})x_2& x_1x_2&=x_2x_1\\
T_1x_2&=x_2T_1 & T_2x_1&=x_1T_2.
\end{align*}

Let $\pi_t=\mathrm{Ind}_{\CC[P]}^{\scH}(\CC v_t)$ be the principal series representation of the affine Hecke algebra $\scH$ with central character~$t=(t_1,t_2)\in(\CC^{\times})^2$, where $\CC v_t$ is the $1$-dimensional representation of $\CC[P]$ with $x_1\cdot v_t=t_1v_t$ and $x_2\cdot v_t=t_2v_t$. 

Let $\scH_1$ be the subalgebra generated by $T_1,x_1$ and $x_2$. Let $s\in\CC^{\times}$, and let $\pi_s^{1}=\scH\otimes_{\scH_1}(\CC u_s)$ be the $3$-dimensional representation of $\scH$ induced from the $1$-dimensional representation $\CC u_s$ of $\scH_1$ given by
\begin{align*}
T_1\cdot u_s&=-q^{-\frac{1}{2}}u_s,& x_1\cdot u_s&=q^{-\frac{1}{2}}su_s,& x_2\cdot u_s&=s^2u_s.
\end{align*}
The module $\pi_s^1$ has basis $\{1\otimes u_s,T_2\otimes u_s,T_1T_2\otimes u_s\}$ and support $\mathrm{supp}\,\pi_s^1=\{t,s_2t,s_1s_2t\}$, where $t\in\Hom(P,\CC^{\times})$ is the character with $(t^{\omega_1},t^{\omega_2})=(q^{-1/2}s,s^2)$. It is not hard to show (see the proof of Lemma~\ref{lem:C2Q}) that the character of $\pi_s^1$ satisfies
\begin{align}\label{eq:A2_char}
\chi_s(h)=f_t(h)+f_{s_2t}(h)+f_{s_1s_2t}(h)\qquad\textrm{for all $s\in\CC^{\times}$ and all $h\in\scH$}.
\end{align}




Let $\pi^{2}$, $\pi^{3}$ and $\pi^{4}$ be the $1$-dimensional representations of $\scH$ given by (where $\omega=e^{2\pi i/3}$)
\begin{align*}
\pi^2(T_1)&=-q^{-\frac{1}{2}} & \pi^2(T_2)&=-q^{-\frac{1}{2}} & \pi^2(x_1)&=q^{-1} & \pi^2(x_2)&=q^{-1}\\
\pi^3(T_1)&=-q^{-\frac{1}{2}} & \pi^3(T_2)&=-q^{-\frac{1}{2}} & \pi^3(x_1)&=\omega q^{-1} & \pi^3(x_2)&=\omega^{-1}q^{-1}\\
\pi^4(T_1)&=-q^{-\frac{1}{2}} & \pi^4(T_2)&=-q^{-\frac{1}{2}} & \pi^4(x_1)&=\omega^{-1}q^{-1} & \pi^4(x_2)&=\omega q^{-1}.
\end{align*}
Let $\chi_t$, $\chi_s^1$, $\chi^2$, $\chi^3$ and $\chi^4$ be the characters of $\pi_t$, $\pi^1_s$, $\pi^2$, $\pi^3$, and $\pi^4$ (respectively).





\begin{thm} For all $h\in\scH$ we have
$$
\tau(h)=\frac{1}{6q^3}\int_{\TT^2}\frac{\chi_t(h)}{|c(t)|^2}\,dt+\frac{(q-1)^2}{q^2(q^2-1)}\int_{\TT}\frac{\chi_s^{1}(h)}{|c_1(s)|^2}\,ds+\frac{(q-1)^3}{3(q^3-1)}\left(\chi^{2}(h)+\chi^{3}(h)+\chi^{4}(h)\right)
$$
where 
\begin{align*}
c(t)&=\frac{(1-q^{-1}t_1^{-2}t_2)(1-q^{-1}t_1t_2^{-2})(1-q^{-1}t_1^{-1}t_2^{-1})}{(1-t_1^{-2}t_2)(1-t_1t_2^{-2})(1-t_1^{-1}t_2^{-1})},& c_1(s)&=\frac{1-q^{-\frac{3}{2}}s^{-3}}{1-q^{\frac{1}{2}}s^{-3}}.
\end{align*}
\end{thm}


\begin{proof}
The series $G_t(h)$ converges whenever $|t^{\alpha_1^{\vee}}|,|t^{\alpha_2^{\vee}}|<q^{-1}$, and hence the series converges whenever $|t_1|,|t_2|< q^{-1}$, where $t_1=t^{\omega_1}$ and $t_2=t^{\omega_2}$. Fix $h\in\scH$, and write $f_t(h)=f(t)$. Therefore
$$
\Tr(h)=\frac{1}{q^3}\int_{q^{-1}a\TT}\int_{q^{-1}b\TT}\frac{f(t)}{c(t)c(t^{-1})}\,dt_1 dt_2
$$
where $0<a,b<1$. Fix a number $0<c<1$ very close to $1$. Consider the inner integral. The $t_1$-poles of the integrand lying between the contours $q^{-1}a\TT$ and $c\TT$ are at the points where $t_1^2=q^{-1}t_2$. We compute the residues (using $dt_1=\frac{1}{2\pi i}\frac{dz_1}{z_1}$) to be
$$
\Res_{t_1=\pm q^{-1/2}t_2^{1/2}}\frac{f(t)}{c(t)c(t^{-1})}=-\frac{q(q-1)^2}{2(q^2-1)}\frac{f(\pm q^{-\frac{1}{2}}t_2^{1/2},t_2)}{c_1(\mp t_2^{1/2})c_1(\mp t_2^{-1/2})}.
$$
Using $\frac{1}{2}\int_{r\TT}(f(t^{1/2})+f(-t^{1/2}))dt=\int_{r^{1/2}\TT}f(t)dt$ it follows that
$$
\Tr(h)=\frac{1}{q^3}\int_{q^{-1}a\TT}\int_{c\TT}\frac{f(t)}{c(t)c(t^{-1})}\,dt_1dt_2+\frac{(q-1)^2}{q^2(q^2-1)}\int_{q^{-\frac{1}{2}}a^{\frac{1}{2}}\TT}\frac{f(q^{-\frac{1}{2}}s,s^2)}{c_1(s)c_1(s^{-1})}\,ds.
$$
Interchange the order of integration in the double integral. The $t_2$-poles of the integrand between the contours $q^{-1}a\TT$ to $\TT$ are at the points where $t_2^2=q_1^{-1}t_1$ and where $t_2=q^{-1}t_1^{-1}$. Computing residues gives
$$
\Tr(h)=\frac{1}{q^3}\int_{c\TT}\int_{\TT}\frac{f(t)}{|c(t)|^2}\,dt_2dt_1+\frac{(q-1)^2}{q^2(q^2-1)}(I_1+I_2+I_3),
$$
where
\begin{align*}
I_1&=\int_{q^{-\frac{1}{2}}a^{\frac{1}{2}}\TT}\frac{f(q^{-\frac{1}{2}}s,s^2)}{c_1(s)c_1(s^{-1})}\,ds& I_2&=\int_{c^{\frac{1}{2}}\TT}\frac{f(s^2,q^{-\frac{1}{2}}s)}{c_1(s)c_1(s^{-1})}\,ds& I_3&=\int_{q^{\frac{1}{2}}c\TT}\frac{f(q^{-\frac{1}{2}}s,q^{-\frac{1}{2}}s^{-1})}{c_1(s)c_1(s^{-1})}\,ds
\end{align*}
where we have set $s=t_1^{1/2}$ in $I_2$ and $s=q^{\frac{1}{2}}t_1$ in $I_3$. The $t_1$-contour in the double integral can be shifted to $\TT$ without encountering any poles. 

The plan is to shift each of the contours in $I_1,I_2$ and $I_3$ to the unit contour $\TT$. However we need to be careful with the possible singularities of $f(t)$. Therefore we write $f(t)=g(t)/d(t)$, with $g(t)$ analytic. Then the integrands of the integrals $I_1,I_2$ and $I_3$ are
\begin{align*}
\frac{f(q^{-\frac{1}{2}}s,s^2)}{c_1(s)c_1(s^{-1})}&=\frac{(1-q^{\frac{1}{2}}s^3)g(q^{-\frac{1}{2}}s,s^2)}{(1-s^{-2})(1-q^{\frac{1}{2}}s^{-1})(1-q^{-\frac{3}{2}}s^{-3})(1-q^{-\frac{3}{2}}s^3)}\\
\frac{f(s^2,q^{-\frac{1}{2}}s)}{c_1(s)c_1(s^{-1})}&=\frac{(1-q^{\frac{1}{2}}s^3)g(s^2,q^{-\frac{1}{2}}s)}{(1-s^{-2})(1-q^{\frac{1}{2}}s^{-1})(1-q^{-\frac{3}{2}}s^{-3})(1-q^{-\frac{3}{2}}s^3)}\\
\frac{f(q^{-\frac{1}{2}}s,q^{-\frac{1}{2}}s^{-1})}{c_1(s)c_1(s^{-1})}&=\frac{(1-q^{\frac{1}{2}}s^{-3})(1-q^{\frac{1}{2}}s^3)g(q^{-\frac{1}{2}}s,q^{-\frac{1}{2}}s^{-1})}{(1-q)(1-q^{-\frac{3}{2}}s^{-3})(1-q^{-\frac{3}{2}}s^3)(1-q^{\frac{1}{2}}s^{-1})(1-q^{\frac{1}{2}}s)}.
\end{align*}
In particular, the integrands of $I_1$ and $I_2$ have singularities on~$\TT$. So instead we shift all contours to $c\TT$. For the integrals $I_2$ and $I_3$ we encounter no poles, and so the shift is for free. For the integral $I_1$ we pick up simple residues at the points $s^3=q^{-\frac{3}{2}}$, and computing residues gives
$$
I_1=\int_{c\TT}\frac{f(q^{-\frac{1}{2}}s,s^2)}{c_1(s)c_1(s^{-1})}\,ds+\frac{q^2(q-1)(q^2-1)}{3(q^3-1)}\left(f(q^{-1},q^{-1})+f(\omega q^{-1},\omega^{-1}q^{-1})+f(\omega^{-1}q^{-1},\omega q^{-1})\right).
$$
Therefore
\begin{align*}
\Tr(h)&=\frac{1}{q^3}\int_{\TT^2}\frac{f(t)}{|c(t)|^2}\,dt+\frac{(q-1)^2}{q^2(q^2-1)}\int_{c\TT}\frac{f(q^{-\frac{1}{2}}s,s^2)+f(s^2,q^{-\frac{1}{2}}s)+f(q^{-\frac{1}{2}}s,q^{-\frac{1}{2}}s^{-1})}{c_1(s)c_1(s^{-1})}\,ds\\
&\qquad+\frac{(q-1)^3}{3(q^3-1)}\left(f(q^{-1},q^{-1})+f(\omega q^{-1},\omega^{-1}q^{-1})+f(\omega^{-1}q^{-1},\omega q^{-1})\right).
\end{align*}
By (\ref{eq:A2_char}) the numerator of the single integral is $\chi_s(h)$, and is therefore defined on~$\TT$ and so the contour of the single integral can be shifted to~$\TT$. Proposition~\ref{prop:prelim_main} deals with the double integral, and Lemma~\ref{lem:1dim} deals with the $3$ constant terms.
\end{proof}



\subsection{The $\tilde{C}_2(q_1,q_2)$ algebras with $L=Q$}\label{sect:C2Q}




The dual root system is $R^{\vee}=\pm\{\alpha_1^{\vee},\alpha_2^{\vee},\alpha_1^{\vee}+\alpha_2^{\vee},\alpha_1^{\vee}+2\alpha_2^{\vee}\}$. Writing $x_1=x^{\alpha_1^{\vee}}$ and $x_2=x^{\alpha_2^{\vee}}$, the Hecke algebra has generators $T_1,T_2,x_1,x_2$ with relations
\begin{align*}
T_1^2&=1+(q_1^{\frac{1}{2}}-q_1^{-\frac{1}{2}})T_1& T_1x_1&=x_1^{-1}T_1+(q_1^{\frac{1}{2}}-q_1^{-\frac{1}{2}})(1+x_1) & T_1T_2T_1T_2&=T_2T_1T_2T_1\\
T_2^2&=1+(q_2^{\frac{1}{2}}-q_2^{-\frac{1}{2}})T_2 & T_2x_2&=x_2^{-1}T_2+(q_2^{\frac{1}{2}}-q_2^{-\frac{1}{2}})(1+x_2)& x_1x_2&=x_2x_1\\
T_1x_2&=x_1x_2T_1^{-1} & T_2x_1&=x_1x_2^2T_2^{-1}-(q_2^{\frac{1}{2}}-q_2^{-\frac{1}{2}})x_1x_2.
\end{align*}

Let $\pi_t=\mathrm{Ind}_{\CC[Q]}^{\scH}(\CC v_t)$ be the principal series representation of $\scH$ with central character $t=(t_1,t_2)\in(\CC^{\times})^2$, where $\CC v_t$ is the $1$-dimensional representation of $\CC[Q]$ with $x_1\cdot v_t=t_1v_t$ and $x_2\cdot v_t=t_2v_t$. 

Let $\scH_1$ be the subalgebra generated by $T_1,x_1,x_2$ and let $\scH_2$ be the subalgebra generated by $T_2,x_1,x_2$. Let $s\in\CC^{\times}$, and let $\pi_s^{1}=\mathrm{Ind}_{\scH_1}^{\scH}(\CC u_s^1)$ and $\pi_s^2=\mathrm{Ind}_{\scH_2}^{\scH}(\CC u_s^2)$ be the $4$-dimensional representations induced from the $1$-dimensional representation $\CC u_s^1$ of $\scH_1$ and the $1$-dimensional representation $\CC u_s^2$ of $\scH_2$
given by
\begin{align*}
T_1\cdot u_s^1&=-q_1^{-\frac{1}{2}}u_s^1 & x_1\cdot u_s^1&=q_1^{-1}u_s^1 & x_2\cdot u_s^1&=q_1^{\frac{1}{2}}su_s^1\\
T_2\cdot u_s^2&=-q_2^{-\frac{1}{2}}u_s^2 & x_1\cdot u_s^2&=q_2su_s^2 & x_2\cdot u_s^2&=q_2^{-1}u_s^2.
\end{align*}


Let $\pi^j$ ($j=3,4,5,6,7$) be the $1$-dimensional representations of $\scH$ with
\begin{align*}
\pi^3(T_1)&=-q_1^{-\frac{1}{2}} & \pi^3(T_2)&=-q_2^{-\frac{1}{2}} & \pi^3(x_1)&=q_1^{-1} & \pi^3(x_2)&=q_2^{-1}\\
\pi^4(T_1)&=-q_1^{-\frac{1}{2}} & \pi^4(T_2)&=-q_2^{-\frac{1}{2}} & \pi^4(x_1)&=q_1^{-1} & \pi^4(x_2)&=-1\\
\pi^5(T_1)&=-q_1^{-\frac{1}{2}} & \pi^5(T_2)&=q_2^{\frac{1}{2}} & \pi^5(x_1)&=q_1^{-1} & \pi^5(x_2)&=-1\\
\pi^6(T_1)&=q_1^{\frac{1}{2}} & \pi^6(T_2)&=-q_2^{-\frac{1}{2}} & \pi^6(x_1)&= q_1 & \pi^6(x_2)&= q_2^{-1}\\
\pi^7(T_1)&=-q_1^{-\frac{1}{2}} & \pi^7(T_2)&=q_2^{\frac{1}{2}} & \pi^7(x_1)&=q_1^{-1} & \pi^7(x_2)&=q_2.
\end{align*}


Suppose that $q_1\neq q_2$ and $q_1\neq q_2^2$. Let $\pi^8=M_J(t)$ be the representation with
\begin{align*}
(t^{\alpha_1^{\vee}},t^{\alpha_2^{\vee}})&=(q_1^{-1},q_2)&J^{\vee}&=\{\alpha_2^{\vee}\}&F_J(t)&=\{s_2,s_1s_2,s_2s_1s_2\}
\end{align*}
(since $q_1\neq q_2$ and $q_1\neq q_2^2$ we compute $N(t)^{\vee}=\{\alpha_1^{\vee},\alpha_2^{\vee}\}$ and $D(t)^{\vee}=\emptyset$). The matrices for $\pi^8$ are given in Example~3 of Section~\ref{sect:examples}.

Let $\chi_t$, $\chi_s^1$, $\chi_s^2$, and $\chi^j$ be the characters of $\pi_t$, $\pi_s^1$, $\pi_s^2$, and $\pi^j$ respectively ($j=3,\ldots,8$).

\begin{lemma}\label{lem:C2Q}
Let $t,u\in\Hom(Q,\CC^{\times})$ be $(t^{\alpha_1^{\vee}},t^{\alpha_2^{\vee}})=(q_1^{-1},q_1^{\frac{1}{2}}s)$ and $(u^{\alpha_1^{\vee}},u^{\alpha_2^{\vee}})=(q_2s,q_2^{-1})$ where $s\in\CC^{\times}$. For all $h\in\scH$ and all $s\in\CC^{\times}$ we have
\begin{align}
\label{eq:extend}\chi_s^1(h)&=f_{t}(h)+f_{s_2t}(h)+f_{s_1s_2t}(h)+f_{s_2s_1s_2t}(h)\\
\label{eq:extend2}\chi_s^2(h)&=f_u(h)+f_{s_1u}(h)+f_{s_2s_1u}(h)+f_{s_1s_2s_1u}(h).
\end{align}
\end{lemma}


\begin{proof} Let us prove (\ref{eq:extend}) ((\ref{eq:extend2}) is similar). Suppose that $s\in\CC^{\times}$ is not one of the isolated points of $\CC^{\times}$ which give $t^{\alpha^{\vee}}=1$ for some $\alpha\in R_0^+$. Then $\pi_s^1$ is irreducible (for example it can be constructed using Theorem~\ref{thm:repmain} in these cases) and each $f_{vt}(h)$ is defined (for $v\in W_0$ and $h\in\scH$). Moreover $\pi_s^1$ has basis $\{1\otimes u_s^1,\tau_2\otimes u_s^1,\tau_1\tau_2\otimes u_s^1,\tau_2\tau_1\tau_2\otimes u_s^1\}$ (this is proved in a similar way to the corresponding statement in the proof of Proposition~\ref{prop:prelim_main}).

The diagonal entries of each matrix $\pi_s^1(\tau_w)$ relative to this basis are~$0$. This is easily seen once it is observed that $\tau_1\otimes u_s^1=0$ (which can be seen by direct calculation, or by (\ref{eq:tausquared})). Since 
$$\pi_s^1(x^{\lambda})=\mathrm{diag}(t^{\lambda},(s_2t)^{\lambda},(s_1s_2t)^{\lambda},(s_2s_1s_2t)^{\lambda})\qquad\textrm{for all $\lambda\in Q$}$$
it follows that
$$
\chi_s^1(\tau_w x^{\lambda})=\delta_{w,1}\big(t^{\lambda}+(s_2t)^{\lambda}+(s_1s_2t)^{\lambda}+(s_2s_1s_2t)^{\lambda}\big)\quad\textrm{for all $w\in W_0$ and $\lambda\in Q$}.
$$ 
Thus Lemma~\ref{lem:milage} gives (\ref{eq:extend}) provided $s$ is not one of the isolated points of $\CC^{\times}$ that gives $t^{\alpha^{\vee}}= 1$ for some $\alpha\in R_0^+$. But by construction, $\chi_s^1(h)$ is a polynomial in $s$ and $s^{-1}$ (for fixed $h\in\scH$) and the right hand side of (\ref{eq:extend}) is a rational function in $s$. Hence the result.
\end{proof}





\begin{thm}\label{thm:C_2Q} For all $h\in\scH$ we have
\begin{align*}
\Tr(h)&=\frac{1}{8q_1^2q_2^2}\iint_{\TT^2}\frac{\chi_t(h)}{|c(t)|^2}\,dt+\frac{q_1-1}{2q_1q_2^2(q_1+1)}\int_{\TT}\frac{\chi_s^{1}(h)}{|c_1(s)|^2}\,ds+\frac{q_2-1}{2q_1^2q_2(q_2+1)}\int_{\TT}\frac{\chi_s^{2}(h)}{|c_2(s)|^2}\,ds\\
&\quad+A\chi^{3}(h)+B\left(\chi^{4}(h)+\chi^{5}(h)\right)+|C|\times\begin{cases}
\chi^6(h)&\textrm{if $q_1<q_2$}\\
\chi^8(h)&\textrm{if $q_2<q_1<q_2^2$}\\
\chi^7(h)&\textrm{if $q_2^2<q_1$},
\end{cases}
\end{align*}
where $c(t)$, $c_1(s)$, $c_2(s)$, $A$, $B$, and $C$ are as in Appendix~\ref{app:C2Q}. If $q_1=q_2$ or $q_1=q_2^2$ then the final term in the Plancherel Theorem is~$0$.
\end{thm}

\begin{proof}
The trace functional is given by
\begin{align}\label{eq:TrC2}
\Tr(h)=\frac{1}{q_1^2q_2^2}\int_{q_1^{-1}a\TT}\int_{q_2^{-1}b\TT}\frac{f(t)}{c(t)c(t^{-1})}\,dt_2dt_1,
\end{align}
where $0<a,b<1$ and where $f(t)=f_t(h)$. Choose $a$ with $a<q_1q_2^{-1}$. 

\smallskip

\noindent\textit{Step 1: Shifting the $t_2$-contour}. Let $0<c<1$ with $c^2>q_1^{-1}$, $c>q_2^{-1}$, $c>q_1q_2^{-1}$ (if $q_1<q_2$) and $c>q_1^{-1}q_2$ (if $q_2<q_1$). We will shift the $t_2$-contour from $q_2^{-1}b\TT$ to $c\TT$. The integrand has exactly one $t_2$-pole between these contours, at $t_2=q_2^{-1}$. Thus
$$
\Tr(h)=\frac{1}{q_1^2q_2^2}\int_{q_1^{-1}a\TT}\int_{c\TT}\frac{f(t)}{c(t)c(t^{-1})}\,dt_2dt_1+I_1,
\quad\textrm{where}\quad
I_1=-\frac{1}{q_1^2q_2^2}\int_{q_1^{-1}a\TT}\Res_{t_2=q_2^{-1}}\frac{f(t)}{c(t)c(t^{-1})}\,dt.
$$


\noindent\textit{Step 2: Shifting the $t_1$-contour.} Interchange the order of integration in the double integral. We will shift the $t_1$-contour from $q_1^{-1}a\TT$ to $\TT$. By the conditions on $a$ and $c$ the $t_1$-poles of the integrand between these contours are at $t_1=q_1^{-1}$, $t_1=q_1^{-1}t_2^{-2}$, and $t_1=q_2^{-1}t_2^{-1}$. Therefore
$$
\Tr(h)=\frac{1}{q_1^2q_2^2}\int_{c\TT}\int_{\TT}\frac{f(t)}{c(t)c(t^{-1})}\,dt_1dt_2+I_1+I_2+I_3+I_4,
$$
where
$$
I_j=-\frac{1}{q_1^2q_2^2}\int_{c\TT}\Res_{t_1=z_j}\frac{f(t)}{c(t)c(t^{-1})}\,dt_2\qquad\textrm{for $j=2,3,4$},
$$
with $z_2=q_1^{-1}$, $z_3=q_1^{-1}t_2^{-2}$, and $z_4=q_2^{-1}t_2^{-1}$. In the double integral we may now revert back to the original order of integration, and shift the $t_2$-contour to $\TT$ without encountering any poles.

\smallskip

\noindent\textit{Step 3: Shifting the contours in the integrals $I_j$.} Straightforward calculations give
\begin{align*}
I_1&=\frac{(q_2-1)^2}{q_1^2q_2(q_2^2-1)}\int_{q_1^{-1}q_2^{-1}a\TT}\frac{f(q_2s,q_2^{-1})}{c_2(s)c_2(s^{-1})}\,ds &
I_2&=\frac{(q_1-1)^2}{q_1q_2^2(q_1^2-1)}\int_{q_1^{-\frac{1}{2}}c\TT}\frac{f(q_1^{-1},q_1^{\frac{1}{2}}s)}{c_1(s)c_1(s^{-1})}\,ds\\
I_3&=\frac{(q_1-1)^2}{q_1q_2^2(q_1^2-1)}\int_{q_1^{\frac{1}{2}}c\TT}\frac{f(s^{-2},q_1^{-\frac{1}{2}}s)}{c_1(s)c_1(s^{-1})}\,ds &
I_4&=\frac{(q_2-1)^2}{q_1^2q_2(q_2^2-1)}\int_{c\TT}\frac{f(q_2^{-1}s^{-1},s)}{c_2(s)c_2(s^{-1})}\,ds,
\end{align*}
where we have set $s=q_2^{-1}t_1$ in $I_1$, $s=q_1^{-\frac{1}{2}}t_2$ in $I_2$, $s=q_1^{\frac{1}{2}}t_2$ in $I_3$, and $s=t_2$ in $I_4$. 

We now shift each contour to $\TT$. As in the $\tilde{A}_2$ case we need to be a little careful with possible singularities of $f(t)$. Thus we write $f(t)=g(t)/d(t)$. Then the integrands of $I_1,I_2,I_3$ and $I_4$ are
\begin{align*}
\frac{f(q_2s,q_2^{-1})}{c_2(s)c_2(s^{-1})}&=\frac{q_2s(1-s)g(q_2s,q_2^{-1})}{(q_2-1)n_2(s)n_2(s^{-1})}&
\frac{f(q_1^{-1},q_1^{\frac{1}{2}}s)}{c_1(s)c_1(s^{-1})}&=\frac{q_1^{\frac{1}{2}}s(1-s^2)g(q_1^{-1},q_1^{\frac{1}{2}}s)}{(q_1-1)n_1(s)n_1(s^{-1})}\\
\frac{f(s^{-2},q_1^{-\frac{1}{2}}s)}{c_1(s)c_1(s^{-1})}&=\frac{(1-s^{-2})g(s^{-2},q_1^{-\frac{1}{2}}s)}{(1-q_1)n_1(s)n_1(s^{-1})}&
\frac{f(q_2^{-1}s^{-1},s)}{c_2(s)c_2(s^{-1})}&=\frac{(1-s)g(q_2^{-1}s^{-1},s)}{(1-q_2)n_2(s)n_2(s^{-1})},
\end{align*}
where $n_1(s)$ and $n_2(s)$ are the numerators of $c_1(s)$ and $c_2(s)$. Each integrand is nonsingular on~$\TT$ (with removable singularities in the cases $q_1=q_2$ or $q_1=q_2^2$).

The poles of the integrand of $I_1$ which lie between the contours $q_1^{-1}q_2^{-1}a\TT$ and $\TT$ are at $s=q_1^{-1}q_2^{-1}$, $s=q_1^{-1}q_2$ (if $q_2<q_1$) and at $s=q_1q_2^{-1}$ (if $q_1<q_2$). Calculating residues gives
$$
I_1=\frac{(q_2-1)^2}{q_1^2q_2(q_2^2-1)}\int_{\TT}\frac{f(q_2s,q_2^{-1})}{|c_2(s)|^2}\,ds+Af(q_1^{-1},q_2^{-1})+C\times\begin{cases}f(q_1^{-1}q_2^2,q_2^{-1})&\textrm{if $q_2<q_1$}\\
-f(q_1,q_2^{-1})&\textrm{if $q_1<q_2$}.
\end{cases}
$$

The poles of the integrand of $I_2$ which lie between the contours $q_1^{-\frac{1}{2}}b\TT$ and $\TT$ are at $s=-q_1^{-\frac{1}{2}}$, $s=q_1^{\frac{1}{2}}q_2^{-1}$ (if $q_2<q_1<q_2^2$), and $s=q_1^{-\frac{1}{2}}q_2$ (if $q_2^2<q_1$). Calculating residues gives
$$
I_2=\frac{(q_1-1)^2}{q_1q_2^2(q_1^2-1)}\int_{\TT}\frac{f(q_1^{-1},q_1^{\frac{1}{2}}s)}{c_1(s)c_1(s^{-1})}\,ds+2Bf(q_1^{-1},-1)+C\times\begin{cases}
f(q_1^{-1},q_1q_2^{-1})&\textrm{if $q_2<q_1<q_2^2$}\\
-f(q_1^{-1},q_2)&\textrm{if $q_2^2<q_1$}.
\end{cases}
$$

The poles of the integrand of $I_3$ which lie between the contours $q_1^{\frac{1}{2}}c\TT$ and $\TT$ are at $s=q_1^{-\frac{1}{2}}q_2$ (if $q_2<q_1<q_2^2$) and $s=q_1^{\frac{1}{2}}q_2^{-1}$ (if $q_2^2<q_1$). Noting that $\TT$ is inside $q_1^{\frac{1}{2}}c\TT$ gives
$$
I_3=\frac{(q_1-1)^2}{q_1q_2^2(q_1^2-1)}\int_{\TT}\frac{f(s^{-2},q_1^{-\frac{1}{2}}s)}{c_1(s)c_1(s^{-1})}\,ds+C\times\begin{cases}
f(q_1q_2^{-2},q_1^{-1}q_2)&\textrm{if $q_2<q_1<q_2^2$}\\
-f(q_1^{-1}q_2^{2},q_2^{-1})&\textrm{if $q_2^2<q_1$}.
\end{cases}
$$

The integrand of $I_4$ has no poles between $c\TT$ and $\TT$. Therefore
\begin{align*}
\Tr(h)&=\frac{1}{q_1^2q_2^2}\iint_{\TT^2}\frac{f(t)}{|c(t)|^2}\,dt+\frac{(q_1-1)^2}{q_1q_2^2(q_1^2-1)}\int_{\TT}\frac{f(q_1^{-1},q_1^{\frac{1}{2}}s)+f(s^{-2},q_1^{-\frac{1}{2}}s)}{|c_1(s)|^2}\,ds\\
&\quad+\frac{(q_2-1)^2}{q_1^2q_2(q_2^2-1)}\int_{\TT}\frac{f(q_2s,q_2^{-1})+f(q_2^{-1}s^{-1},s)}{|c_2(s)|^2}\,ds+Af(q_1^{-1},q_2^{-1})+2Bf(q_1^{-1},-1)\\
&\quad+|C|\times\begin{cases}
f(q_1,q_2^{-1})&\textrm{if $q_1<q_2$}\\
f(q_1^{-1}q_2^2,q_2^{-1})+f(q_1^{-1},q_1q_2^{-1})+f(q_1q_2^{-2},q_1^{-1}q_2)&\textrm{if $q_2<q_1<q_2^2$}\\
f(q_1^{-1},q_2)&\textrm{if $q_2^2<q_1$}.
\end{cases}
\end{align*}


\noindent\textit{Step 4: Matching with the representations.} By Proposition~\ref{prop:prelim_main} the double integral in the above formula is
$$
\int_{\TT^2}\frac{f(t)}{|c(t)|^2}\,dt=\frac{1}{8}\int_{\TT^2}\frac{\chi_t(h)}{|c(t)|^2}\,dt.
$$
The first single integral is
$$
\frac{1}{2}\int_{\TT}\frac{f(q_1^{-1},q_1^{\frac{1}{2}}s)+f(s^{-2},q_1^{-\frac{1}{2}}s)+f(q_1^{-1},q_1^{\frac{1}{2}}s^{-1})+f(s^2,q_1^{-\frac{1}{2}}s^{-1})}{|c_1(s)|^2}\,ds=\frac{1}{2}\int_{\TT}\frac{\chi_s^1(h)}{|c_1(s)|^2}\,ds,
$$
where we have used Lemma~\ref{lem:C2Q}. A similar analysis applies to the second single integral. Using Lemma~\ref{lem:1dim} we have $f(q_1^{-1},q_2^{-1})=\chi^3(h)$ and $2f(q_1^{-1},-1)=\chi^4(h)+\chi^5(h)$. Furthermore, for parameters $q_1<q_2$ the central character $(t_1,t_2)=(q_1,q_2^{-1})$ is regular (for $t^{\alpha_1^{\vee}+\alpha_2^{\vee}}=q_1q_2^{-1}<1$ and $t^{\alpha_1^{\vee}+2\alpha_2^{\vee}}=q_1q_2^{-2}<1$), and so Lemma~\ref{lem:1dim} gives $f(q_1,q_2^{-1})=\chi^6(h)$. Similarly we have $f(q_1^{-1},q_2)=\chi^7(h)$ for parameters $q_2^2<q_1$. Finally by Proposition~\ref{prop:calc} we have 
$$f(q_1^{-1}q_2^2,q_2^{-1})+f(q_1^{-1},q_1q_2^{-1})+f(q_1q_2^{-2},q_1^{-1}q_2)=\chi^8(h)$$
for all parameters in the range $q_2<q_1<q_2^2$ (as the central character is regular).
\end{proof}




\subsection{The $\tilde{C}_2(q_1,q_2)$ algebras with $L=P$}\label{sect:C2P}



The root system is as in Section~\ref{sect:C2Q}, and the fundamental coweights are given by $\omega_1=\alpha_1^{\vee}+\alpha_2^{\vee}$ and $\omega_2=\frac{1}{2}\alpha_1^{\vee}+\alpha_2^{\vee}$. Writing $x_1=x^{\omega_1}$ and $x_2=x^{\omega_2}$, the Hecke algebra has presentation given by generators $T_1,T_2,x_1,x_2$ with relations
\begin{align*}
T_1^2&=1+(q_1^{\frac{1}{2}}-q_1^{-\frac{1}{2}})T_1& T_1x_1&=x_1^{-1}x_2^2T_1+(q_1^{\frac{1}{2}}-q_1^{-\frac{1}{2}})x_1 & T_1T_2T_1T_2&=T_2T_1T_2T_1\\
T_2^2&=1+(q_2^{\frac{1}{2}}-q_2^{-\frac{1}{2}})T_2 & T_2x_2&=x_1x_2^{-1}T_2+(q_2^{\frac{1}{2}}-q_2^{-\frac{1}{2}})x_2& x_1x_2&=x_2x_1\\
T_1x_2&=x_2T_1 & T_2x_1&=x_1T_2.
\end{align*}
The representation theory of $\scH$ is closely related to the representation theory of the Hecke algebra from Section~\ref{sect:C2Q}.


Let $\pi_t=\mathrm{Ind}_{\CC[P]}^{\scH}(\CC v_t)$ be the principal series representation of $\scH$ with central character $t=(t_1,t_2)\in(\CC^{\times})^2$, where $\CC v_t$ is the $1$-dimensional representation of $\CC[P]$ with $x_1\cdot v_t=t_1v_t$ and $x_2\cdot v_t=t_2v_t$. 

Let $\scH_1$ be the subalgebra generated by $T_1,x_1,x_2$. 
Let $s\in\CC^{\times}$, and let $\pi_s^{\pm}=\mathrm{Ind}_{\scH_1}^{\scH}(\CC u_s^{\pm})$ be the $4$-dimensional representations of $\scH$ induced from the representations $\CC u_s^{\pm}$ of $\scH_1$ with
\begin{align*}
T_1\cdot u_s^{\pm}&=-q_1^{-\frac{1}{2}}u_s^{\pm}& x_1\cdot u_s^{\pm}&=q_1^{-\frac{1}{2}}su_s^{\pm}& x_2\cdot u_s^{\pm}&=\pm su_s^{\pm}.
\end{align*}
Let $\scH_2$ be the subalgebra generated by $T_2,x_1,x_2$. Let $s\in\CC^{\times}$, and let $\pi_s^2=\mathrm{Ind}_{\scH_2}^{\scH}(\CC u_s^2)$ be the $4$-dimensional representation of $\scH$ induced from the representation $\CC u_s^2$ of $\scH_2$ with
\begin{align*}
T_2\cdot u_s^2&=-q_2^{-\frac{1}{2}}u_s^2& x_1\cdot u_s^2&=s^2u_s^2& x_2\cdot u_s^2&=q_2^{-\frac{1}{2}}su_s^2.
\end{align*}


Let $\pi^j_{\pm}$ ($j=3,4,5$) be the $1$-dimensional representations
\begin{align*}
\pi^3_{\pm}(T_1)&=-q_1^{-\frac{1}{2}}& \pi^3_{\pm}(T_2)&=-q_2^{-\frac{1}{2}} & \pi^3_{\pm}(x_1)&=q_1^{-1}q_2^{-1} & \pi^3_{\pm}(x_2)&=\pm q_1^{-\frac{1}{2}}q_2^{-1}\\
\pi^4_{\pm}(T_1)&=q_1^{\frac{1}{2}} & \pi^4_{\pm}(T_2)&=-q_2^{-\frac{1}{2}} & \pi^4_{\pm}(x_1)&=q_1q_2^{-1} & \pi^4_{\pm}(x_2)&=\pm q_1^{\frac{1}{2}}q_2^{-1}\\
\pi^5_{\pm}(T_1)&=-q_1^{-\frac{1}{2}} & \pi^5_{\pm}(T_2)&=q_2^{\frac{1}{2}} & \pi^5_{\pm}(x_1)&=q_1^{-1}q_2 & \pi^5_{\pm}(x_2)&=\pm q_1^{-\frac{1}{2}}q_2.
\end{align*}

Let $\pi^6=M_J(t)$ be the $2$-dimensional representation with
\begin{align*}
(t^{\omega_1},t^{\omega_2})&=(-q_1^{-1},q_1^{-\frac{1}{2}})&J^{\vee}&=\emptyset&F_J(t)&=\{1,s_2\}
\end{align*}
(we have $N(t)^{\vee}=\{\alpha_1^{\vee},\alpha_1^{\vee}+2\alpha_2^{\vee}\}$ and $D(t)^{\vee}=\emptyset$). Coincidentally, $\pi^6\cong\mathrm{Ind}_{\scH_Q}^{\scH}(\CC u)$ where $\scH_Q$ is the algebra from Section~\ref{sect:C2Q} and where $\CC u$ is the $1$-dimensional representation of $\scH_Q$ with 
$
T_1\cdot u=-q_1^{-1/2}u$, $T_2\cdot u=-q_2^{-1/2}u$, $x^{\alpha_1^{\vee}}\cdot u=q_1^{-1}u$, and $x^{\alpha_2^{\vee}}\cdot u=-u$. The matrices for $\pi^6$ are given in Example~1 of Section~\ref{sect:examples}.

Suppose that $q_1\neq q_2$ and $q_1\neq q_2^2$. Let $\pi^7_{\pm}=M_J(t_{\pm})$ be the $3$-dimensional representations with
\begin{align*}
(t_{\pm}^{\omega_1},t_{\pm}^{\omega_2})&=(q_1^{-1}q_2,\pm q_1^{-\frac{1}{2}}q_2)&J^{\vee}&=\{\alpha_2^{\vee}\}&F_J(t_{\pm})&=\{s_2,s_1s_2,s_2s_1s_2\}
\end{align*}
(we calculate $N(t_{\pm})^{\vee}=\{\alpha_1^{\vee},\alpha_2^{\vee}\}$ and $D(t)^{\vee}=\emptyset$). 



\begin{thm} 
For all $h\in\scH$ we have
\begin{align*}
\Tr(h)&=\frac{1}{8q_1^2q_2^2}\iint_{\TT^2}\frac{\chi_t(h)}{|c(t)|^2}\,dt+\frac{(q_1-1)^2}{4q_1q_2^2(q_1^2-1)}\int_{\TT}\frac{\chi_s^+(h)+\chi_s^-(h)}{|c_1(s)|^2}\,ds+\frac{(q_2-1)^2}{2q_1^2q_2(q_2^2-1)}\int_{\TT}\frac{\chi_s^2(h)}{|c_2(s)|^2}\,ds\\
&\quad+\frac{A}{2}\left(\chi^3_+(h)+\chi^3_-(h)\right)+B\chi^6(h)+\frac{|C|}{2}\times\begin{cases}
\chi^4_+(h)+\chi^4_-(h)&\textrm{if $q_1<q_2$}\\
\chi^7_+(h)+\chi^7_-(h)&\textrm{if $q_2<q_1<q_2^2$}\\
\chi^5_+(h)+\chi^5_-(h)&\textrm{if $q_2^2<q_1$}
\end{cases}
\end{align*}
where $c(t)$, $c_1(s)$, $c_2(s)$ are as in Appendix~\ref{app:C2P} and $A,B,C$ are as in Appendix~\ref{app:C2Q}. If $q_1=q_2$ or $q_1=q_2^2$ then the final term in the Plancherel Theorem is~$0$.
\end{thm}


\begin{proof} The series $G_t(h)$ converges for $|t^{\alpha_1^{\vee}}|<q_1^{-1}$ and $|t^{\alpha_2^{\vee}}|<q_2^{-1}$. Since $\alpha_1^{\vee}=2\omega_1-2\omega_2$ and $\alpha_2^{\vee}=-\omega_1+2\omega_2$ the series converges whenever $|t_1^2t_2^{-2}|<q_1^{-1}$ and $|t_1^{-1}t_2^2|<q_2^{-1}$. Thus, writing $|t_1|=q_1^{-1}q_2^{-1}a$ and $|t_2|=q_1^{-1/2}q_2^{-1}b$, the series converges for $b^2<a<b<1$, and so
$$
\Tr(h)=\frac{1}{q_1^2q_2^2}\int_{q_1^{-1}q_2^{-1}a\TT}\int_{q_1^{-1/2}q_2^{-1}b\TT}\frac{f(t)}{c(t)c(t^{-1})}\,dt_2dt_1.
$$
From here one can either perform the contour shifts as in the $L=Q$ case, or change variables $t_1=u_1u_2$ and $t_2^2=u_1u_2^2$ to transform the above integral into $\frac{1}{2}$ times the $L=Q$ integral (\ref{eq:TrC2}) with the numerator of its integrand replaced by $f'(u_1,u_2)=f(u_1u_2,u_1^{1/2}u_2)+f(u_1u_2,-u_1^{1/2}u_2)$.
We omit the details.
\end{proof}


\subsection{The $\tilde{G}_2(q_1,q_2)$ algebras with $L=Q$}\label{sect:G2}


The coroot system is
$
R^{\vee}=\pm\{\alpha_1^{\vee},2\alpha_1^{\vee}+3\alpha_2^{\vee},\alpha_1^{\vee}+3\alpha_2^{\vee},\alpha_2^{\vee},\alpha_1^{\vee}+2\alpha_2^{\vee},\alpha_1^{\vee}+\alpha_2^{\vee}\},
$
and the reflections $s_1$ and $s_2$ are given by $s_1(\alpha_2^{\vee})=\alpha_1^{\vee}+\alpha_2^{\vee}$ and $s_2(\alpha_1^{\vee})=\alpha_1^{\vee}+3\alpha_2^{\vee}$. Writing $x_1=x^{\alpha_1^{\vee}}$ and $x_2=x^{\alpha_2^{\vee}}$, the Hecke algebra $\scH$ has generators $T_1$, $T_2$, $x_1$ and $x_2$ with relations
\begin{align*}
T_1^2&=1+(q_1^{\frac{1}{2}}-q_1^{-\frac{1}{2}})T_1& T_1x_1&=x_1^{-1}T_1+(q_1^{\frac{1}{2}}-q_1^{-\frac{1}{2}})(1+x_1)\\
T_2^2&=1+(q_2^{\frac{1}{2}}-q_2^{-\frac{1}{2}})T_2 & T_2x_2&=x_2^{-1}T_2+(q_2^{\frac{1}{2}}-q_2^{-\frac{1}{2}})(1+x_2)\\
T_1T_2T_1T_2T_1T_2&=T_2T_1T_2T_1T_2T_1 & T_2x_1&=x_1x_2^3T_2^{-1}-(q_2^{\frac{1}{2}}-q_2^{-\frac{1}{2}})x_1x_2(1+x_2)\\
 x_1x_2&=x_2x_1 &
 T_1x_2&=x_1x_2T_1^{-1}.
\end{align*}

Let $\pi_t=\mathrm{Ind}_{\CC[Q]}^{\scH}(\CC v_t)$ be the principal series representation of $\scH$ with central character $t=(t_1,t_2)\in(\CC^{\times})^2$, where $\CC v_t$ is the $1$-dimensional representation of $\CC[Q]$ with $x_1\cdot v_t=t_1v_t$ and $x_2\cdot v_t=t_2v_t$. 

Let $\scH_1$ be the subalgebra of $\scH$ generated by $T_1,x_1,x_2$, and let $\scH_2$ be the subalgebra generated by $T_2,x_1,x_2$. Let $s\in\CC^{\times}$, and let $\pi_s^1=\mathrm{Ind}_{\scH_1}^{\scH}(\CC u_s^1)$ and $\pi_s^2=\mathrm{Ind}_{\scH_2}^{\scH}(\CC u_s^2)$ be the $6$-dimensional representations induced from the $1$-dimensional representation $\CC u_s^1$ of $\scH_1$ and the $1$-dimensional representation $\CC u_s^2$ of $\scH_2$ given by 
\begin{align*}
T_1\cdot u_s^1&=-q_1^{-\frac{1}{2}}u_s^1 & x_1\cdot u_s^1&=q_1^{-1}u_s^1 & x_2\cdot u_s^1&=q_1^{\frac{1}{2}}su_s^1\\
T_2\cdot u_s^2&=-q_2^{-\frac{1}{2}}u_s^2 & x_1\cdot u_s^2&=q_2^{\frac{3}{2}}su_s^2 & x_2\cdot u_s^2&=q_2^{-1}u_s^2.
\end{align*}

Let $\pi^3,\pi^4$ and $\pi^5$ be the $1$-dimensional representations of $\scH$ with
\begin{align*}
\pi^3(T_1)&=-q_1^{-\frac{1}{2}}& \pi^3(T_2)&=-q_2^{-\frac{1}{2}}& \pi^3(x_1)&=q_1^{-1}& \pi^3(x_2)&=q_2^{-1}\\
\pi^4(T_1)&=q_1^{\frac{1}{2}}&\pi^4(T_2)&=-q_2^{-\frac{1}{2}}&\pi^4(x_1)&=q_1&\pi^4(x_2)&=q_2^{-1}\\
\pi^5(T_1)&=-q_1^{-\frac{1}{2}}&\pi^5(T_2)&=q_2^{\frac{1}{2}}&\pi^5(x_1)&=q_1^{-1}&\pi^5(x_2)&=q_2.
\end{align*}

Suppose that $q_1\neq q_2$, $q_1\neq q_2^2$, $q_1^2\neq q_2^3$, $q_1\neq q_2^3$. Let $\pi^6=M_J(t)$ the the $5$-dimensional representation with 
\begin{align*}
(t^{\alpha_1^{\vee}},t^{\alpha_2^{\vee}})&=(q_1^{-1},q_2)&J^{\vee}&=\{\alpha_2^{\vee}\}&F_J(t)&=\{s_2,s_1s_2,s_2s_1s_2,s_1s_2s_1s_2,s_2s_1s_2s_1s_2\}.
\end{align*}


Let $\pi^7_{\pm}=M_J(t_{\pm})$ be the $3$-dimensional representations with
\begin{align*}
(t_{\pm}^{\alpha_1^{\vee}},t_{\pm}^{\alpha_2^{\vee}})&=(q_1,\pm q_1^{-\frac{1}{2}}q_2^{\frac{1}{2}})&J^{\vee}&=\{\alpha_1^{\vee}+2\alpha_2^{\vee}\}&F_J(t_{\pm})&=\{s_2s_1s_2s_1,s_1s_2s_1s_2s_1,s_2s_1s_2s_1s_2s_1\},
\end{align*}
where we assume that $q_1\neq q_2$ and $q_1\neq q_2^3$ for $M_J(t_+)$. When $q_1=q_2$ or $q_1=q_2^3$ we define $\pi_+^7$ differently, as explained in Example~2 of Section~\ref{sect:examples}.




Let $\pi^8=M_J(t)$ be the $2$-dimensional representation with
\begin{align*}
(t^{\alpha_1^{\vee}},t^{\alpha_2^{\vee}})&=(q_1,\omega)&J^{\vee}&=\{\alpha_1^{\vee}+3\alpha_2^{\vee}\}&F_J(t)&=\{s_1s_2s_1s_2s_1,s_2s_1s_2s_1s_2s_1\}.
\end{align*}


Let $\chi_t$, $\chi_s^1$, $\chi_s^2$, $\chi^3$, $\chi^4$, $\chi^5$, $\chi^6$, $\chi^7_{\pm}$ and $\chi^8$ be the characters of the above representations.



\begin{thm} For all $h\in\scH$ we have
\begin{align*}
\Tr(h)&=\frac{1}{12q_1^3q_2^3}\iint_{\TT^2}\frac{\chi_t(h)}{|c(t)|^2}\,dt+\frac{(q_1-1)^2}{2q_1q_2^3(q_1^2-1)}\int_{\TT}\frac{\chi_s^{1}(h)}{|c_1(s)|^2}\,ds+\frac{(q_2-1)^2}{2q_1^3q_2^2(q_2^2-1)}\int_{\TT}\frac{\chi_s^{2}(h)}{|c_2(s)|^2}\,ds\\
&\qquad+A\chi^3(h)+B_+\chi^7_+(h)+B_-\chi^7_-(h)+C\chi^8(h)+|D|\times\begin{cases}
\chi^4(h)&\textrm{if $q_1<q_2^{3/2}$}\\
\chi^6(h)&\textrm{if $q_2^{3/2}<q_1<q_2^2$}\\
\chi^5(h)&\textrm{if $q_2^2<q_1$}
\end{cases}
\end{align*}
where $c(t),c_1(s),c_2(s),A,B_{\pm},C,D$ are as in Appendix~\ref{app:G2Q}. If $q_1=q_2^{3/2}$ or $q_1=q_2^2$ then the final term in the Plancherel Theorem is~$0$. 
\end{thm}



\begin{proof}
Writing $f(t)=f_t(h)$, the trace functional is given by
$$
\Tr(h)=\frac{1}{q_1^3q_2^3}\int_{q_1^{-1}a\TT}\int_{q_2^{-1}b\TT}\frac{f(t)}{c(t)c(t^{-1})}\,dt_2dt_1
$$
with $0<a,b<1$. Choose $0<a,b<1$ both very close to $0$. Let $0<c<1$ be very close to~$1$.
Consider the inner integral. The integrand has exactly one $t_2$-pole between the contours $q_2^{-1}b\TT$ and $c\TT$, at $t_2=q_2^{-1}$. Thus we can shift the $t_2$-contour to $c\TT$ at the cost of including this residue contribution. Now interchange the order of integration in the double integral. Since $|t_2|=c$ we see that the $t_1$-poles of the integrand between the contours $q_1^{-1}a\TT$ and $\TT$ are at the points where $t_1=q_1^{-1}$, $t_1=q_1^{-1}t_2^{-3}$, $t_1=q_2^{-1}t_2^{-2}$, $t_1=q_2^{-1}t_2^{-1}$ and $t_1^2=q_1^{-1}t_2^{-3}$. After shifting the $t_1$-contour to $\TT$ we interchange the order of integration again, and since there are no $t_2$-poles between $c\TT$ and $\TT$ we shift the $t_2$-contour to $\TT$. Thus
$$
\Tr(h)=\frac{1}{q_1^3q_2^3}\iint_{\TT^2}\frac{f(t)}{|c(t)|^2}\,dt+I_1+I_2+I_3+I_4+I_5+I_6^++I_6^-
$$
where
\begin{align*}
I_1&=-\frac{1}{q_1^3q_2^3}\int_{q_1^{-1}a\TT}\Res_{t_2=z_1}\frac{f(t)}{c(t)c(t^{-1})}\,dt_1&I_6^{\pm}&=-\frac{1}{q_1^3q_2^3}\int_{c\TT}\Res_{t_1=\pm z_6}\frac{f(t)}{c(t)c(t^{-1})}dt_2\\
I_j&=-\frac{1}{q_1^3q_2^3}\int_{c\TT}\Res_{t_1=z_j}\frac{f(t)}{c(t)c(t^{-1})}dt_2& (j&=2,3,4,5),
\end{align*}
where $z_1=q_2^{-1}$, $z_2=q_1^{-1}$, $z_3=q_1^{-1}t_2^{-3}$, $z_4=q_2^{-1}t_2^{-2}$, $z_5=q_2^{-1}t_2^{-1}$, and $z_6=q_1^{-\frac{1}{2}}t_2^{-\frac{3}{2}}$

Use $\frac{1}{2}\int_{r\TT}(f(t^{1/2})+f(-t^{1/2}))dt=\int_{r^{1/2}\TT}f(t)dt$ to write $I_6^++I_6^-=I_6$ as a single integral. Straightforward calculations give
\begin{align*}
I_1&=\frac{(q_2-1)^2}{q_1^3q_2^2(q_2^2-1)}\int_{q_1^{-1}q_2^{-\frac{3}{2}}a\TT}\frac{f(q_2^{\frac{3}{2}}s,q_2^{-1})}{c_2(s)c_2(s^{-1})}\,ds 
& 
I_2&=\frac{(q_1-1)^2}{q_1q_2^3(q_1^2-1)}\int_{q_1^{-\frac{1}{2}}c\TT}\frac{f(q_1^{-1},q_1^{\frac{1}{2}}s)}{c_1(s)c_1(s^{-1})}\,ds\\
I_3&=\frac{(q_1-1)^2}{q_1q_2^3(q_1^2-1)}\int_{q_1^{\frac{1}{2}}c\TT}\frac{f(q_1^{\frac{1}{2}}s^{-3},q_1^{-\frac{1}{2}}s)}{c_1(s)c_1(s^{-1})}\,ds
&
I_4&=\frac{(q_2-1)^2}{q_1^3q_2^2(q_2^2-1)}\int_{q_2^{\frac{1}{2}}c\TT}\frac{f(s^{-2},q_2^{-\frac{1}{2}}s)}{c_2(s)c_2(s^{-1})}\,ds\\
I_5&=\frac{(q_2-1)^2}{q_1^3q_2^2(q_2^2-1)}\int_{q_2^{-\frac{1}{2}}c\TT}\frac{f(q_2^{-\frac{3}{2}}s^{-1},q_2^{\frac{1}{2}}s)}{c_2(s)c_2(s^{-1})}\,ds
&
I_6&=\frac{(q_1-1)^2}{q_1q_2^3(q_1^2-1)}\int_{c^{\frac{1}{2}}\TT}\frac{f(q_1^{-\frac{1}{2}}s^{-3},s^2)}{c_1(s)c_1(s^{-1})}\,ds
\end{align*}
where we have put $s=q_2^{-\frac{3}{2}}t_1,q_1^{-\frac{1}{2}}t_2,q_1^{\frac{1}{2}}t_2,q_2^{\frac{1}{2}}t_2,q_2^{-\frac{1}{2}}t_2,t_2$ in $I_1,I_2,I_3,I_4,I_5,I_6$ respectively. 

One now shifts each contour to $\TT$. As we discuss below, some complications arise when $q_1=q_2$ or $q_1=q_2^3$, and so suppose for now that $q_1\neq q_2$ and $q_1\neq q_2^3$. As in the $\tilde{C}_2$, $L=Q$, case the integrands of $I_1,\ldots,I_6$ are all nonsingular on~$\TT$. Moreover, assuming that $q_1\neq q_2$ and $q_1\neq q_2^3$ all singularities are simple poles, and at the special values $q_1^2=q_2^3$ or $q_1=q_2^2$ there are some removable singularities. Write $I_1^u,\ldots,I_6^u$ for the integrals over the contour~$\TT$. A lengthy analysis (using the fact that $a$ is close to $0$ and $c$ is close to $1$) gives
\begin{align*}
\Tr(h)&=\frac{1}{q_1^3q_2^3}\iint_{\TT^2}\frac{f(t)}{|c(t)|^2}\,dt+I_1^u+\cdots+I_6^u+Af(q_1^{-1},q_2^{-1})+B_+\sigma_++B_-\sigma_-\\
&\qquad+C\left(f(q_1^{-1},\omega)+f(q_1^{-1},\omega^{-1})\right)+|D|\times\begin{cases}
f(q_1,q_2^{-1})&\textrm{if $q_1<q_2^{3/2}$}\\
\sigma&\textrm{if $q_2^{3/2}<q_1<q_2^2$}\\
f(q_1^{-1},q_2)&\textrm{if $q_2^2<q_1$},
\end{cases}
\end{align*}
where $\sigma_{\pm}=f(\pm q_1^{-1/2}q_2^{3/2},q_2^{-1})+f(q_1^{-1},\pm q_1^{1/2}q_2^{-1/2})+f(\pm q_1^{1/2}q_2^{-3/2},\pm q_1^{-1/2}q_2^{1/2})$ and 
\begin{align*}
\sigma&=f(q_1^{-1}q_2^3,q_2^{-1})+f(q_1^{-1},q_1q_2^{-1})+f(q_1^2q_2^{-3},q_1^{-1}q_2)+f(q_1^{-2}q_2^3,q_1q_2^{-2})+f(q_1q_2^{-3},q_1^{-1}q_2^2).
\end{align*}
As in the previous sections it is easy to show that
$$
I_1^u+\cdots+I_6^u=\frac{(q_1-1)^2}{2q_1q_2^3(q_1^2-1)}\int_{\TT}\frac{\chi_s^{1}(h)}{|c_1(s)|^2}\,ds+\frac{(q_2-1)^2}{2q_1^3q_2^2(q_2^2-1)}\int_{\TT}\frac{\chi_s^{2}(h)}{|c_2(s)|^2}\,ds.
$$
Proposition~\ref{prop:calc} gives $f(q_1^{-1},\omega)+f(q_1^{-1},\omega^{-1})=\pi^8(h)$ and $\sigma=\pi^6(h)$ (note that $\pi^6$ only occurs for parameters $q_2^{3/2}<q_1<q_2^2$, and in this range $\pi^6$ is defined and has regular central character). We also have $\sigma_{\pm}=\pi_{\pm}^7(h)$. For $\pi_+^7$ it is important that $q_1\neq q_2$ and $q_1\neq q_2^3$, for otherwise $\pi_+^7$ does not have a regular central character and things become complicated (see below). Lemma~\ref{lem:1dim} gives $f(q_1^{-1},q_2^{-1})=\chi^3(h)$. Since we exclude $q_1=q_2$ the representation $\pi^4$ has regular central character for parameters $q_1<q_2^{3/2}$, and so Lemma~\ref{lem:1dim} gives $f(q_1,q_2^{-1})=\chi^4(h)$. Similarly $f(q_1^{-1},q_2)=\chi^5(h)$ for all $q_2^2<q_1$ with $q_1\neq q_2^3$.


It remains to discuss the cases $q_1=q_2$ and $q_1=q_2^3$. Let us briefly outline the working involved. Consider the $q_1=q_2$ case (the $q_1=q_2^3$ case is similar). 
 The integrands of $I_1,\ldots,I_6$ are still nonsingular on $\TT$, and the contours in the integrals $I_3,I_4$ and $I_6$ can all be shifted to $\TT$ without encountering any poles. This leaves $I_1,I_2$ and $I_5$ to consider. Writing $f(t)=g(t)/d(t)$ the integrands of $I_1$, $I_2$ and $I_5$ are (respectively)
\begin{align*}
\frac{qs^2(1-s^2)g(q^{\frac{3}{2}}s,q^{-1})}{(1-q)(1-q^{-\frac{1}{2}}s^{-1})^2(1+q^{-\frac{1}{2}}s^{-1})(1-q^{-\frac{5}{2}}s^{-1})(1-q^{-\frac{1}{2}}s)^2(1+q^{-\frac{1}{2}}s)(1-q^{-\frac{5}{2}}s)}\\
\frac{s^4(1-s^2)g(q^{-1},q^{\frac{1}{2}}s)}{(1-q)(1-q^{-\frac{3}{2}}s^{-3})(1-q^{-1}s^{-2})(1-q^{-\frac{3}{2}}s^{-1})(1-q^{-\frac{3}{2}}s^3)(1-q^{-1}s^2)(1-q^{-\frac{3}{2}}s)}\\
\frac{q^{-\frac{1}{2}}s(1-s^2)g(q^{-\frac{3}{2}}s^{-1},q^{\frac{1}{2}}s)}{(q-1)(1-q^{-\frac{1}{2}}s^{-1})^2(1+q^{-\frac{1}{2}}s^{-1})(1-q^{-\frac{5}{2}}s^{-1})(1-q^{-\frac{1}{2}}s)^2(1+q^{-\frac{1}{2}}s)(1-q^{-\frac{5}{2}}s)}.
\end{align*}
The relevant poles are at $s=q^{-\frac{1}{2}}$ (a double pole for $I_1$, $I_2$, and $I_5$), $s=q^{-\frac{1}{2}}$ (a single pole for $I_1$, $I_2$, and $I_5$), $s=\omega^{\pm1}q^{-\frac{1}{2}}$ (single poles for $I_2$ only), and $s=q^{-\frac{5}{2}}$ (a single pole for $I_1$ only). The residue contributions from $s=-q^{-\frac{1}{2}}$ make up the $\chi_-^7(h)$ term, the contributions from $s=\omega^{\pm1}q^{-\frac{1}{2}}$ give the $\chi^8(h)$ term, and the contribution from $s=q^{-\frac{5}{2}}$ gives the $\chi^3(h)$ term. All that remains is to analyse the contribution from the double poles of each integral at $s=q^{-\frac{1}{2}}$. 



We claim that the combined residue contribution from the point $s=q^{-\frac{1}{2}}$ is
\begin{align}\label{eq:entangled}
R_1+R_2+R_5=\frac{q(q-1)^3}{6(q+1)^2(q^3-1)}\left(\chi_+^7(h)+2\chi^4(h)\right).
\end{align}
We do not have a conceptual proof of this fact, but it can be obtained by direct calculation as follows. As in Remark~\ref{rem:explicit} the functions $g(t)=g_t(h)$ can be explicitly computed (since one only needs to know the values $g_t(T_w)$ for $w\in W_0$, as $g_t(T_wx^{\lambda})=t^{\lambda}g_t(T_w)$). Then the residue contributions can be explicitly calculated (making $12$ separate calculations, one for each $h=T_wx^{\lambda}$ with $w\in W_0$). On the other hand, using the explicit matrices (Example~2 of Section~\ref{sect:examples}) for the representations $\pi_+^7$ and $\pi^4$ one can compute the expression $\chi_+^7(T_wx^{\lambda})+2\chi^4(T_wx^{\lambda})$ and compare. This completes the proof. 
\end{proof}





\subsection{The $\tilde{BC}_2(q_0,q_1,q_2)$ algebras with $L=Q$}


The root system is $R=\pm\{\alpha_1,\alpha_2,\alpha_1+\alpha_2,\alpha_1+2\alpha_2,2\alpha_2,2(\alpha_1+\alpha_2)\}$, giving dual root system $R^{\vee}=\pm\{\alpha_1^{\vee},\alpha_2^{\vee},\alpha_1^{\vee}+\alpha_2^{\vee},2\alpha_1^{\vee}+\alpha_2^{\vee},\alpha_2^{\vee}/2,\alpha_1^{\vee}+\alpha_2^{\vee}/2\}$. The affine Hecke algebra has generators $T_1,T_2,x_1=x^{\alpha_1^{\vee}}$ and $x_2=x^{\alpha_2^{\vee}/2}$ with relations
\begin{align*}
T_1^2&=1+(q_1^{\frac{1}{2}}-q_1^{-\frac{1}{2}})T_1& T_1x_1&=x_1^{-1}T_1+(q_1^{\frac{1}{2}}-q_1^{-\frac{1}{2}})(1+x_1)\\
T_2^2&=1+(q_2^{\frac{1}{2}}-q_2^{-\frac{1}{2}})T_2 & T_2x_2&=x_2^{-1}T_2+(q_2^{\frac{1}{2}}-q_2^{-\frac{1}{2}})x_2+(q_0^{\frac{1}{2}}-q_0^{-\frac{1}{2}})\\
T_1T_2T_1T_2&=T_2T_1T_2T_1 & T_2x_1&=x_1x_2^2T_2^{-1}-(q_0^{\frac{1}{2}}-q_0^{-\frac{1}{2}})x_1x_2\\
 x_1x_2&=x_2x_1 &
T_1x_2&=x_1x_2T_1^{-1}.
\end{align*}

Let $\pi_t=\mathrm{Ind}_{\CC[Q]}^{\scH}(\CC v_t)$ be the principal series representation of $\scH$ with central character $t=(t_1,t_2)\in(\CC^{\times})^2$, where $\CC v_t$ is the $1$-dimensional representation of $\CC[Q]$ with $x_1\cdot v_t=t_1v_t$ and $x_2\cdot v_t=t_2v_t$. 


Let $\scH_1$ be the subalgebra generated by $T_1,x_1,x_2$ and let $\scH_2$ be the subalgebra generated by $T_2,x_1,x_2$. Let $s\in\CC^{\times}$, and let $\pi_s^{1}=\mathrm{Ind}_{\scH_1}^{\scH}(\CC u_s^1)$ and $\pi_s^j=\mathrm{Ind}_{\scH_2}^{\scH}(\CC u_s^j)$ ($j=2,3,4$) be the $4$-dimensional representations induced from the $1$-dimensional representation $\CC u_s^1$ of $\scH_1$ and the $1$-dimensional representations $\CC u_s^j$ ($j=2,3,4$) of $\scH_2$
given by
\begin{align*}
T_1\cdot u_s^1&=-q_1^{-\frac{1}{2}}u_s^1 & x_1\cdot u_s^1&=q_1^{-1}u_s^1 & x_2\cdot u_s^1&=q_1^{\frac{1}{2}}su_s^1\\
T_2\cdot u_s^2&=-q_2^{-\frac{1}{2}}u_s^2 & x_1\cdot u_s^2&=q_0^{\frac{1}{2}}q_2^{\frac{1}{2}}su_s^2 & x_2\cdot u_s^2&=q_0^{-\frac{1}{2}}q_2^{-\frac{1}{2}}u_s^2\\
T_2\cdot u_s^3&=-q_2^{-\frac{1}{2}}u_s^3 & x_1\cdot u_s^3&=q_0^{-\frac{1}{2}}q_2^{\frac{1}{2}}su_s^3 & x_2\cdot u_s^3&=-q_0^{\frac{1}{2}}q_2^{-\frac{1}{2}}u_s^3\\
T_2\cdot u_s^4&=q_2^{\frac{1}{2}}u_s^4 & x_1\cdot u_s^4&=q_0^{\frac{1}{2}}q_2^{-\frac{1}{2}}su_s^4 & x_2\cdot u_s^4&=-q_0^{-\frac{1}{2}}q_2^{\frac{1}{2}}u_s^4.
\end{align*}

Let $\pi^j$ $(j=5,\ldots,11)$ be the $1$-dimensional representations of $\scH$ with
\begin{align*}
\pi^5&=(-q_1^{-\frac{1}{2}},-q_2^{-\frac{1}{2}},q_1^{-1},q_0^{-\frac{1}{2}}q_2^{-\frac{1}{2}})&
\pi^6&=(-q_1^{-\frac{1}{2}},-q_2^{-\frac{1}{2}},q_1^{-1},-q_0^{\frac{1}{2}}q_2^{-\frac{1}{2}})\\
\pi^7&=(q_1^{\frac{1}{2}},-q_2^{-\frac{1}{2}},q_1,q_0^{-\frac{1}{2}}q_2^{-\frac{1}{2}})&\pi^8&=(q_1^{\frac{1}{2}},-q_2^{-\frac{1}{2}},q_1,-q_0^{\frac{1}{2}}q_2^{-\frac{1}{2}})\\
\pi^9&=(-q_1^{-\frac{1}{2}},q_2^{\frac{1}{2}},q_1^{-1},q_0^{\frac{1}{2}}q_2^{\frac{1}{2}})&
\pi^{10}&=(-q_1^{-\frac{1}{2}},q_2^{\frac{1}{2}},q_1^{-1},-q_0^{-\frac{1}{2}}q_2^{\frac{1}{2}})\\
\pi^{11}&=(q_1^{\frac{1}{2}},q_2^{\frac{1}{2}},q_1,-q_0^{-\frac{1}{2}}q_2^{\frac{1}{2}}),
\end{align*}
where in each case we list the quadruples $(\pi^j(T_1),\pi^j(T_2),\pi^j(x_1),\pi^j(x_2))$.


Let $\pi^{12}=M_J(s)$, $\pi^{13}=M_J(t)$, and $\pi^{14}=M_J(u)$ be the $3$-dimensional representations with
\begin{align*}
(s^{\alpha_1^{\vee}},s^{\alpha_2^{\vee}/2})=(q_1^{-1},q_0^{\frac{1}{2}}q_2^{\frac{1}{2}}),\quad (t^{\alpha_1^{\vee}},t^{\alpha_2^{\vee}/2})=(q_1^{-1},-q_0^{-\frac{1}{2}}q_2^{\frac{1}{2}}),\quad (u^{\alpha_1^{\vee}},u^{\alpha_2^{\vee}/2})=(q_1^{-1},-q_0^{\frac{1}{2}}q_2^{-\frac{1}{2}})
\end{align*}
and $J=\{\alpha_2\}$. We assume that $q_1\neq q_0q_2$ and $q_1^2\neq q_0q_2$ for $\pi^{12}$, that $q_1\neq q_0^{-1}q_2$ and $q_1^2\neq q_0^{-1}q_2$ for $\pi^{13}$, and that $q_1\neq q_0q_2^{-1}$ and $q_1^2\neq q_0q_2^{-1}$ for $\pi^{14}$, so that
$N(s)=N(t)=N(u)=\{\alpha_1,\alpha_2\}$ and $D(s)=D(t)=D(u)=\emptyset$,
and hence $F_J(s)=F_J(t)=F_J(u)=\{s_2,s_1s_2,s_2s_1s_2\}$. 





Finally, let $\pi^{15}=M_J(t)$ and $\pi^{16}=M_J(u)$ be the $2$-dimensional representations with
\begin{align*}
(t^{\alpha_1^{\vee}},t^{\alpha_2^{\vee}/2})&=(-q_0,q_0^{-\frac{1}{2}}q_2^{-\frac{1}{2}})&(u^{\alpha_1^{\vee}},u^{\alpha_2^{\vee}/2})&=(-q_2,q_0^{-\frac{1}{2}}q_2^{-\frac{1}{2}})&J&=\emptyset.
\end{align*}


\begin{thm} For all $h\in\scH$ we have
\begin{align*}
\Tr(h)&=\frac{1}{8q_1^2q_2^2}\iint_{\TT^2}\frac{\chi_t(h)}{|c(t)|^2}\,dt+C_6\int_{\TT}\frac{\chi_s^1(h)}{|c_1(s)|^2}\,ds+C_7\int_{\TT}\frac{\chi_s^2(h)}{|c_2(s)|^2}\,ds+C_8\int_{\TT}\frac{\chi(h)}{|c_3(s)|^2}\,ds\\
&\quad+C_1\chi^5(h)+|C_2|\times\begin{cases}
\pi^7(h)&\textrm{if $q_1<q_0^{\frac{1}{2}}q_2^{\frac{1}{2}}$}\\
\pi^{12}(h)&\textrm{if $q_0^{\frac{1}{2}}q_2^{\frac{1}{2}}<q_1<q_0q_2$}\\
\pi^9(h)&\textrm{if $q_0q_2<q_1$}
\end{cases}\,\,+\,\,\begin{cases}X_1&\textrm{if $q_0<q_2$}\\
X_2&\textrm{if $q_2<q_0$}
\end{cases}
\end{align*}
where $\chi(h)=\chi_s^3(h)$ if $q_0<q_2$ and $\chi(h)=\chi_s^4(h)$ if $q_2<q_0$, and where
\begin{align*}
X_1&=|C_3|\chi^{15}(h)+|C_4|\chi^6(h)+|C_5|\times\begin{cases}
\chi^8(h)&\textrm{if $q_1<q_0^{-\frac{1}{2}}q_2^{\frac{1}{2}}$}\\
\chi^{13}(h)&\textrm{if $q_0^{-\frac{1}{2}}q_2^{\frac{1}{2}}<q_1<q_0^{-1}q_2$}\\
\pi^{10}(h)&\textrm{if $q_0^{-1}q_2<q_1$}
\end{cases}\\
X_2&=|C_3|\chi^{16}(h)+|C_5|\pi^{10}(h)+|C_4|\times\begin{cases}
\pi^{11}(h)&\textrm{if $q_1<q_0^{\frac{1}{2}}q_2^{-\frac{1}{2}}$}\\
\pi^{14}(h)&\textrm{if $q_0^{\frac{1}{2}}q_2^{-\frac{1}{2}}<q_1<q_0q_2^{-1}$}\\
\pi^6(h)&\textrm{if $q_0q_2^{-1}<q_1$},
\end{cases}
\end{align*}
with $c(t),c_1(s),c_2(s),c_3(s),C_1,\ldots,C_8$ as in Appendix~\ref{app:BC2Q}. 
\end{thm}



\begin{proof}
The series $G_t(h)$ converges for $|t_1|<q_1^{-1}$ and $|t_2|<q_0^{-\frac{1}{2}}q_2^{-\frac{1}{2}}$, and so writing $f(t)=f_t(h)$ we have
$$
\Tr(h)=\frac{1}{q_1^2q_2^2}\int_{q_1^{-1}a\TT}\int_{q_0^{-\frac{1}{2}}q_2^{-\frac{1}{2}}b\TT}\frac{f(t)}{c(t)c(t^{-1})}\,dt_2dt_1
$$
whenever $0<a,b<1$. We choose $a$ and $b$ both very close to $0$, and choose $0<c<1$ very close to~$1$. 
The $t_2$-poles of the integrand between the contour $q_0^{-\frac{1}{2}}q_2^{-\frac{1}{2}}b\TT$ and $c\TT$ are at $t_2=q_0^{-\frac{1}{2}}q_2^{-\frac{1}{2}}$, at $t_2=-q_0^{\frac{1}{2}}q_2^{-\frac{1}{2}}$ (if $q_0<q_2$) and at $t_2=-q_0^{-\frac{1}{2}}q_2^{\frac{1}{2}}$ (if $q_2<q_1$). Thus we can shift the $t_2$-contour to $c\TT$ at the cost of residue contributions from the above points. 
Now interchange the order of integration in the double integral. The $t_1$-poles of the integrand between $q_1^{-1}a\TT$ and $\TT$ are at $t_1=q_1^{-1}$, $t_1=q_1^{-1}t_2^{-2}$, $t_1=q_0^{-\frac{1}{2}}q_2^{-\frac{1}{2}}t_2^{-1}$, $t_1=-q_0^{\frac{1}{2}}q_2^{-\frac{1}{2}}t_2^{-1}$ (if $q_0<q_2$) and $t_1=-q_0^{-\frac{1}{2}}q_2^{\frac{1}{2}}t_2^{-1}$ (if $q_2<q_0$). Computing the associated residues gives
$$
\Tr(h)=\frac{1}{q_1^2q_2^2}\int_{\TT^2}\frac{f(t)}{|c(t)|^2}\,dt+I_1+I_2+I_3+I_4+\begin{cases}I_5+I_6&\textrm{if $q_0<q_2$}\\
I_5'+I_6'&\textrm{if $q_2<q_0$},
\end{cases}
$$
where
\begin{align*}
I_1&=\frac{q_0q_2-1}{q_1^2q_2(q_0+1)(q_2+1)}\int_{q_0^{-\frac{1}{2}}q_1^{-1}q_2^{-\frac{1}{2}}a\TT}\frac{f(q_0^{\frac{1}{2}}q_2^{\frac{1}{2}}s,q_0^{-\frac{1}{2}}q_2^{-\frac{1}{2}})}{c_2(s)c_2(s^{-1})}\,ds&&\textrm{where $s=q_0^{-\frac{1}{2}}q_2^{-\frac{1}{2}}t_1$}\\
I_2&=\frac{q_1-1}{q_1q_2^2(q_1+1)}\int_{q_1^{-\frac{1}{2}}c\TT}\frac{f(q_1^{-1},q_1^{\frac{1}{2}}s)}{c_1(s)c_1(s^{-1})}\,ds&&\textrm{where $s=q_1^{-\frac{1}{2}}t_2$}\\
I_3&=\frac{q_1-1}{q_1q_2^2(q_1+1)}\int_{q_1^{\frac{1}{2}}c\TT}\frac{f(s^{-2},q_1^{-\frac{1}{2}}s)}{c_1(s)c_1(s^{-1})}\,ds&&\textrm{where $s=q_1^{\frac{1}{2}}t_2$}\\
I_4&=\frac{q_0q_2-1}{q_1^2q_2(q_0+1)(q_2+1)}\int_{c\TT}\frac{f(q_0^{-\frac{1}{2}}q_2^{-\frac{1}{2}}s^{-1},s)}{c_2(s)c_2(s^{-1})}\,ds&&\textrm{where $s=t_2$}\\
I_5&=\frac{q_2-q_0}{q_1^2q_2(q_0+1)(q_2+1)}\int_{q_0^{\frac{1}{2}}q_1^{-1}q_2^{-\frac{1}{2}}a\TT}\frac{f(q_0^{-\frac{1}{2}}q_2^{\frac{1}{2}}s,-q_0^{\frac{1}{2}}q_2^{-\frac{1}{2}})}{c_3(s)c_3(s^{-1})}\,ds&&\textrm{where $s=q_0^{\frac{1}{2}}q_2^{-\frac{1}{2}}t_1$}\\
I_5'&=\frac{q_0-q_2}{q_1^2q_2(q_0+1)(q_2+1)}\int_{q_0^{-\frac{1}{2}}q_1^{-1}q_2^{\frac{1}{2}}a\TT}\frac{f(q_0^{\frac{1}{2}}q_2^{-\frac{1}{2}}s,-q_0^{-\frac{1}{2}}q_2^{\frac{1}{2}})}{c_3(s)c_3(s^{-1})}\,ds&&\textrm{where $s=q_0^{-\frac{1}{2}}q_2^{\frac{1}{2}}t_1$}\\
I_6&=\frac{q_2-q_0}{q_1^2q_2(q_0+1)(q_2+1)}\int_{c\TT}\frac{f(q_0^{\frac{1}{2}}q_2^{-\frac{1}{2}}s^{-1},-s)}{c_3(s)c_3(s^{-1})}\,ds&&\textrm{where $s=-t_2$}\\
I_6'&=\frac{q_0-q_2}{q_1^2q_2(q_0+1)(q_2+1)}\int_{c\TT}\frac{f(q_0^{-\frac{1}{2}}q_2^{\frac{1}{2}}s^{-1},-s)}{c_3(s)c_3(s^{-1})}\,ds&&\textrm{where $s=-t_2$}.
\end{align*}
Now shift the contours in all integrals $I_j$, $I_j'$ to $\TT$. We omit the details of this long calculation.
\end{proof}

\begin{appendix}

\newpage

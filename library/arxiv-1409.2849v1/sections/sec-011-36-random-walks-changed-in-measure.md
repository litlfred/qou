---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-011-36-random-walks-changed-in-measure
section_title: "Random walks changed in measure"
section_number: 3.6
pages: 20-24
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.951
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
\label{subsec:randomwalkchange}
In this section, we shall make a brief excursion in the higher dimensions. Since we do not want to enter details on mod-Gaussian convergence for random vectors (for which we refer the reader to \cite{KN12} and \cite{FMN13}), we shall only consider the simple case $X=(X^{(1)},\ldots,X^{(d)})$ is a random vector with values in $\R^d$ such that $\mathbb E[\exp(z_1 X^{(1)}+\cdots+z_d X^{(d)})]$ is entire in $\CC^d$. We shall say that the sequence $(X_n)$ of random vectors converges in the complex  mod-Gaussian sense with parameter $t_n$ and limiting function $\psi(z_1,\cdots,z_d)$ if the following convergence holds locally uniformly on compact subsets of $\CC^d$:
$$\psi_n(t)= \mathbb E[\exp(z_1 X_n^{(1)}+\cdots+z_d X_n^{(d)})]\exp\left(-t_n \frac{(z_1)^2+\cdots+(z_d)^2}{2}\right)\to \psi(z_1,\ldots,z_d).$$
In this vector setting, the assumptions (A) and (B) of Section \ref{sec:l1} now simply amount to the fact that the convergence above holds locally uniformly for $t=(t^{(1)},\cdots,t^{(d)})\in\R^d$ and that $\psi_n$ and $\psi$ are both in $\mathrm{L}^1(\R^d)$.\bigskip

Following the case $d=1$ we denote $\proba_n$ the law of $X_n$ on $\R^d$, 
$$
\qproba_n[dx]=\frac{\E^{\frac{\|x\|^2}{2t_n}}}{\esper\!\left[\E^{\frac{\|X_n\|^2}{2t_n}}\right]}\,\,\proba_n[dx],
$$
and $Y_n$ a random variable under the new law $\qproba_n$. Note that here again hypothesis \eqref{hyp:l1mod} implies that $Z_n=\esper[\E^{\|X_n\|^2/2t_n}]$ is finite for all $n \in \N$. Indeed, with the notation $\langle u,v\rangle=u_1v_1+\cdots+u_dv_d$, we have
\begin{align*}
\int_{\R^d} \psi_n(t)\,dt &= \esper\!\left[\int_{\R^d} \E^{\langle t, X_n\rangle-\frac{t_n \,\|t\|^2}{2}}\,dt\right] \\
&=\esper\!\left[\E^{\frac{(\|X_n\|^2}{2t_n}}\,\left(\int_{\R^d} \E^{-\frac{\|X_n-t_n t\|^2}{2t_n}}\,dt\right)\right]=\left(\frac{2\pi}{t_n}\right)^{d/2}\,\,\esper\!\left[\E^{\frac{\|X_n\|^2}{2t_n}}\right].
\end{align*}


Therefore, the new probabilities $\qproba_n$ are well-defined and $$Z_n=\esper[\E^{\|X_n\|^2/2t_n}]=\left(\frac{t_n}{2\pi}\right)^{d/2}\int_{\R^d} \psi_n(t)\,dt.$$
Then it is clear that Proposition \ref{prop:enlemma} holds with $G_n$ being a Gaussian vector with covariance matrix $1/t_n\; I_d$ where $I_d$ is the identity matrix of size $d$. Similarly one can establish an analogue of Theorem \ref{thm:mainl1} in $\R^d$.
\bigskip

Let $W_n$ be a simple random walk on the lattice $\Z^{d\geq 2}$: at each step, each of the $2d$ neighbors of the state that is occupied has the same probability of transition $(2d)^{-1}$. The $d$-dimensional characteristic function of $W_n=(W_n^{(1)},\ldots,W_n^{(d)})$ is
$$\esper[\E^{z_1W_n^{(1)}+\cdots+z_dW_n^{(d)}}]=\left(\frac{\cosh z_1 + \cdots + \cosh z_d}{d}\right)^n.$$
Therefore, one has the asymptotics 
\begin{align*}&\log\,\esper\!\left[\E^{\frac{z_1W_n^{(1)}+\cdots+z_dW_n^{(d)}}{n^{1/4}}}\right]\\
&=n \log\left(1+\frac{(z_1)^2+\cdots+(z_d)^2}{2dn^{1/2}} +\frac{(z_1)^4+\cdots+(z_d)^4}{24dn}+o\left(\frac{1}{n}\right) \right)\\
&=n^{1/2}\,\frac{(z_1)^2+\cdots+(z_d)^2}{2d} -\frac{3((z_1)^2+\cdots+(z_d)^2)^2-d((z_1)^4+\cdots+(z_d)^4)}{24d^2}+o(1).
\end{align*}
One obtains a $d$-dimensional complex mod-Gaussian convergence of $X_n=n^{-1/4}\,W_n$ with parameters $\frac{n^{1/2}}{d}$ and limiting function
$$\psi(z_1,\ldots,z_d)=\exp\left(-\frac{3\,((z_1)^2+\cdots+(z_d)^2)^2-d\,((z_1)^4+\cdots+(z_d)^4)}{24d^2}\right).$$
In \cite{FMN13}, we used this mod-convergence to prove quantitative estimates regarding the breaking of the radial symmetry when one considers random walks conditioned to be of large size (of order $n^{3/4}$ instead of the expected order $n^{1/2}$). With the notion of $\mathrm{L}^1$-mod-Gaussian convergence, one can give another interpretation, but only for $d=2$ or $d=3$. Restricted to $\R^d$, the limiting function is indeed not integrable for $d \geq 4$: if $t_2,\ldots,t_d \in [-1,1]$, then 
\begin{align*}
3\,((t_1)^2+\cdots+(t_d)^2)^2-d\,&((t_1)^4+\cdots+(t_d)^4) \leq 3\,((t_1)^2+(d-1))^2-d\,(t_1)^4\\
&\leq (3-d)(t_1)^4 + 6(d-1)(t_1)^2 + 3(d-1)^2.
\end{align*}
So, restricted to the domain $\R\times [-1,1]^{d-1}$, $\psi(t_1,\ldots,t_d) \leq K\,\exp(a (t_1)^4 - b (t_1)^2)$ for some positive constants $a$, $b$ and $K$; therefore, this function is not integrable.\bigskip

On the other hand, if $d=2$ or $d=3$, then $\psi$ is integrable on $\R^d$, and one has $\mathrm{L}^1$-mod-Gaussian convergence. Indeed, when $d=2$, the limiting function is 
\begin{equation}\psi(t_1,t_2)=\exp\left(-\frac{(t_1)^4+(t_2)^4 + 6 (t_1t_2)^2}{96}\right),\label{eq:limitwalk2}\end{equation}
which is clearly integrable; and the residues
$$\psi_n(t_1,t_2)=\esper\left[\E^{\frac{t_1W_n^{(1)} + t_2W_n^{(2)}}{n^{1/4}}}\right]\,\E^{-\frac{n^{1/2}((t_1)^2+(t_2)^2)}{4}}$$
converge locally uniformly on $\R^2$ to $\psi(t_1,t_2)$, but also in $\mathrm{L}^1(\R^2)$. Indeed,
\begin{align*}
\int_{\R^2} \psi_n(t_1,t_2)\,dt_1\,dt_2 &= \int_{\R^2} \left(\frac{\cosh \frac{t_1}{n^{1/4}}+\cosh \frac{t_2}{n^{1/4}}}{2}\right)^n \E^{-\frac{n^{1/2}((t_1)^2+(t_2)^2)}{4}}\,dt_1\,dt_2\\
&= n^{1/2} \int_{\R^2} \left(\frac{\cosh u_1 + \cosh u_2}{2}\,\E^{-\frac{(u_1)^2+(u_2)^2}{4}}\right)^n\,du_1\,du_2,
\end{align*}
and the function $(u_1,u_2)\mapsto \frac{\cosh u_1 + \cosh u_2}{2}\,\E^{-\frac{(u_1)^2+(u_2)^2}{4}}$ reaches its unique global maximum at $u_1=u_2=0$, with Taylor expansion $$1-\frac{(u_1)^4+(u_2)^4 + 6 (u_1u_2)^2}{96}+o(\|u\|^4)$$ around this point (see Figure \ref{fig:function2}). 

\begin{center}
\begin{figure}[ht]
\vspace{-8mm}
\includegraphics[scale=0.7]{function2.png}\caption{The function $f(u_1,u_2)=\frac{\cosh u_1 + \cosh u_2}{2}\,\E^{-\frac{(u_1)^2+(u_2)^2}{4}}$. \label{fig:function2}}
\end{figure}
\end{center}

Thus, by using the multi-dimensional Laplace method, one sees that the limit of the integral $\int_{\R^2} \psi_n(t_1,t_2)\,dt_1\,dt_2$ is $\int_{\R^2} \psi(t_1,t_2)\,dt_1\,dt_2$, and the $\mathrm{L}^1$ convergence is shown. Similarly, when $d=3$, the limiting function is
 \begin{equation}
\psi(t_1,t_2,t_3)=\exp\left(-\frac{(t_1t_2)^2+(t_1t_3)^2+(t_2t_3)^2}{36}\right),\label{eq:limitwalk3} 
 \end{equation}
 and the following computation shows that it is integrable:
 \begin{align*}
 \int_{\R^3}\psi(x,y,z)\,dx\,dy \,dz&= \int_{\R^2}\E^{-\frac{(yz)^2}{36}}\left(\int_{\R}\E^{-\frac{y^2+z^2}{36}\,x^2}dx\right)dy\,dz\\
 &=6\sqrt{\pi}\int_{\R^2}\frac{\E^{-\frac{(yz)^2}{36}}}{\sqrt{y^2+z^2}}\,dy\,dz \\
 &=3\sqrt{\pi}\int_{r=0}^\infty \int_{\theta=0}^{\pi} \E^{-\frac{r^4\,\sin^2 \theta}{144}}\,dr\,d\theta \end{align*}
\begin{align*}
 &=12\sqrt{3\pi}\int_{r=0}^\infty \E^{-r^4}\,dr \int_{\theta=0}^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{\sin \theta}}< + \infty
 \end{align*}
since $\frac{1}{\sqrt{\sin \theta}}$ is integrable at $0$. On the other hand, the residues
$$\psi_n(t_1,t_2,t_3)=\esper\left[\E^{\frac{t_1W_n^{(1)} + t_2W_n^{(2)}+t_3W_n^{(3)}}{n^{1/4}}}\right]\,\E^{-\frac{n^{1/2}((t_1)^2+(t_2)^2+(t_3)^2)}{6}}$$
converge to $\psi(t_1,t_2,t_3)$ locally uniformly on $\R^3$ and in $\mathrm{L}^1(\R^3)$. Indeed, one has again
$$\int_{\R^3} \psi_n(t_1,t_2,t_3)\,dt = n^{1/2}\int_{\R^3} \left(\frac{\cosh u_1 + \cosh u_2 + \cosh u_3}{3}\,\E^{-\frac{(u_1)^2+(u_2)^2+(u_3)^2}{6}}\right)^n\,du$$
and the function in the brackets reaches its unique maximum at $u_1=u_2=u_3=0$, with Taylor expansion corresponding to the limiting function $\psi$ after application of the Laplace method.\bigskip

The multidimensional analogue of Theorem \ref{thm:mainl1} thus yields the following multidimensional extension of the limit theorem for the Curie-Weiss model:

\begin{theorem}
Let $W_n$ be a simple random walk in dimension $d \leq 3$. If $V_n$ is obtained from $W_n$ by a change of measure by the factor $\exp(d\,\|W_n\|^2/2n)$, then 
$$\frac{V_n}{n^{3/4}} \rightharpoonup_{n \to \infty} \frac{\psi(x)\,dx}{\int_{\R^3}\psi(x)\,dx},$$
where $\psi(x)=\exp(-x^4/12)$ in dimension $1$, and $\psi$ is given by Formulas \eqref{eq:limitwalk2} and \eqref{eq:limitwalk3} in dimension $2$ and $3$.
\end{theorem}
\medskip

\begin{remark}
Suppose $d=2$. Then, there is a limit in law not only for $\frac{V_n}{n^{3/4}}$, but in fact for the whole random walk $(\frac{V_k}{n^{3/4}})_{k \leq n}$, viewed as a random element of $\mathcal{C}(\R_+,\R^2)$ or of the Skorohod space $\mathcal{D}(\R_+,\R^2)$, see Figure \ref{fig:saw}.
\figcap{saw.pdf}{A $2$-dimensional random walk changed in measure by $\E^{\|W_n\|^2/n}$, here with $n=10000$.\label{fig:saw}} 
\end{remark}
\bigskip
\bigskip

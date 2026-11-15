---
doc_id: arxiv-math-9910147v1
doc_title: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999"
section_id: sec-012-71-formulae-on-basic-hypergeometric-functions
section_title: "Formulae on Basic Hypergeometric Functions."
section_number: 7.1
pages: 26-28
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.976
doc_brief: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999 — We study the tensor product of principal unitary representations of the quantum Lorentz Group, prove a decomposition theorem and compute the associated"
---
In the sequel we shall frequently use the following notations:

$\forall x \in \CC, \forall k \in \NN,$ $$\begin{aligned}
&&\hskip -1.2cm [x]=\frac{q^x-q^{-x}}{q-q^{-1}}\;,\;\;\;\;d_x=2x+1\;,\;\;\;\;[x]_k=\prod_{n=1}^{ k} [x+n-1]\;,\;\;\;\;[k]!=[1]_k,\;\;\;\;\;v_x^{1/4}=e^{i\frac{\pi}{2}x}q^{-\frac{1}{2}x(x+1)}.  
\end{aligned}$$ In this article, the square root of a complex number is defined by: $$\begin{aligned}
\forall x\in \CC, \sqrt{x}=\sqrt{\vert x \vert}e^{i \frac{Arg(x)}{2}},  
\mbox{where}\;\; x=\;\vert x \vert e^{i  Arg(x)}, Arg(x) \in ]-\pi,\pi],   
\end{aligned}$$ and for all complex number $z$ with non zero imaginary part, we define $\epsilon(z)=\;\mbox{sign}\; (Im(z)).$

We will define the following basic functions: $\forall \alpha,\beta,\gamma \in \CC, \forall n \in {\mathbb Z},$ $$\begin{aligned}
&&(\alpha)_{\infty}=(q^{2\alpha},q^2)_{\infty}=  
\prod_{k=0}^{+\infty}(1-q^{2\alpha+2k})\;,\;\;\;\;\;\;\;\;\;\;\;\;  
(\alpha)_{n}=\frac{(\alpha)_{\infty}}{(\alpha+n)_{\infty}},\\  
&&\nu_{\infty}(\alpha)=\prod_{k=0}^{+\infty}\sqrt{1-q^{2\alpha+2k}}  
\;,\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\nu_{n}(\alpha)=\frac{\nu_{\infty}(\alpha)}{\nu_{\infty}(\alpha+n)},  
\end{aligned}$$ $$\begin{aligned}
&&\;\;\;\;\;  
\omega(\alpha;\beta,\gamma)=\frac{\nu_{\infty}(\alpha+\beta+\gamma+2)\nu_{\infty}(\alpha+\beta-\gamma+1)\nu_{\infty}(\alpha-\beta+\gamma+1)}{\nu_{\infty}(-\alpha+\beta+\gamma+1)}.  
\end{aligned}$$

The q-factorials satisfy the following relations: $\forall \alpha \in \CC, \forall n \in \ZZ,$ $$\begin{aligned}
&&(\alpha)_{-n}(1-\alpha)_{n}=(-1)^{n}q^{-2n\alpha +n(n+1)} \;\;\mbox{(inversion relation)},\label{inversionrelation}\\  
&&\lim_{\alpha \rightarrow +\infty}(\alpha)_{n}=1,\;\;\;\;\;\;\;\;\;\;\;\;  
(\alpha)_{n}\sim_{\alpha \rightarrow -\infty} (-1)^{n}q^{2n\alpha+n(n-1)}.  
\end{aligned}$$

In order to control the signs of the expressions in our article, we are led to introduce the following functions $\varphi:\CC\times{\onehalf}\ZZ\rightarrow \CC$, defined by: $$\varphi_{(\alpha,n)}=\frac{\nu_{\infty}(\alpha-n+1)\nu_{\infty}(n-\alpha)}{\nu_{\infty}(\alpha+1)\nu_{\infty}(-\alpha)}q^{-n\alpha+\onehalf n(n-1)}\;\;,\forall \alpha\in \CC, \forall n\in {\onehalf}\ZZ.$$ This function $\varphi$ satisfies the two following relations: $$\begin{aligned}
&&\varphi_{(\alpha, n)}\varphi_{(\alpha-n, p)}=\varphi_{(\alpha, n+p)}, \forall\alpha \in \CC, \forall n,p\in {\onehalf}\ZZ\\  
&&\frac{\varphi_{(\alpha,n)}^2}{\varphi_{(\alpha,p)}^2}=(-1)^{n-p}, \forall \alpha \in \CC,\forall n,p \in \onehalf\ZZ\;, (n-p) \in \ZZ,   
\end{aligned}$$ The last equation implies in particular that $\varphi_{(\alpha,n)}^2=(-1)^{n},   
\forall \alpha \in \CC,\forall n\in \ZZ.$ Note that when $n$ is half an odd integer, $\varphi_{(\alpha,n)}$ is not a fourth root of unity.

With our choice of square root, we have the more precise results: $$\begin{aligned}
&&\varphi_{(\alpha,n)}=e^{-i\frac{\pi}{2}\; n \; \epsilon(q^{\alpha})}, \forall n \in\ZZ, \forall \alpha\in\CC,\\  
&&\vert \varphi_{(-1+i\rho, n)} \vert^2 = e^{i\pi (p+1/2+\epsilon(q^{i\rho}))}\varphi_{(i\rho, -p)}^2,\forall n,p \in \onehalf+\ZZ \;, \forall \rho \in \RR.  
\end{aligned}$$

We will also make an extensive use of the following basic hypergeometric functions, associated to complex numbers $\alpha_0, \cdots, \alpha_n, \beta_1, \cdots, \beta_n$ and defined by: $$\begin{aligned}
&&\forall Z\in \CC, \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;{}_{n+1}\!\Phi_n  
\left[\!\!\begin{array}{ccccc} \alpha_0 &\!\!\alpha_1 &\!\!\cdots &\!\!\!\!\alpha_n &\\  
&\!\!\!\!\!\!\!\!\beta_1 &\!\!\!\!\!\!\!\!\cdots &\!\!\!\!\!\!\!\beta_n & \; ; Z\end{array} \!\!\right]\!=\sum_{k=0}^{+\infty}\frac{\prod_{i=0}^{n}(\alpha_i)_k}{(1)_k\prod_{i=1}^{n}(\beta_i)_k}q^{2kZ},\nonumber\\  
&&{}_{n+3}W_{n+2}(\alpha_0\; ; \;\alpha_1, \cdots, \alpha_n \; ; \; Z)\!= \sum_{k=0}^{+\infty}\frac{(1-q^{2\alpha_0+4k})}{(1-q^{2\alpha_0})}\frac{\prod_{i=0}^{n}(\alpha_i)_k}{(1)_k\prod_{i=1}^{n}(1+\alpha_0-\alpha_i)_k}q^{2kZ}.  
\end{aligned}$$ In an expression involving ${}_{n+1}\!\Phi_n$ or ${}_{n+1}\!W_n,$ if $Z$ is not specified it will mean that $Z=1$.\
Let us recall some properties of basic hypergeometric functions which are proved for example in [@GR]: $$\begin{aligned}
&&\hskip -1cm {}_{2}\!\Phi_1  
\left[\!\!\begin{array}{ccc} \alpha_0 &\!\!\alpha_1, &\\  
&\!\!\!\!\!\!\!\!\beta_1 & \; ; \beta_1\!-\!\alpha_0\!-\!\alpha_1\end{array} \!\!\right]=  
\frac{(\beta_1\!-\!\alpha_0)_{\infty}(\beta_1\!-\!\alpha_1)_{\infty}}{(\beta_1)_{\infty}(\beta_1\!-\!\alpha_0\!-\!\alpha_1)_{\infty}}\label{heine},\\  
&&\hskip -1cm{}_{4}\!\Phi_3\left[\!\!\begin{array}{cccc} -n &\!\!\alpha_1 &\!\!\alpha_2 &\!\!\!\!\alpha_3 \\&\!\!\!\!\!\!\!\!\beta_1 &\!\!\!\!\!\!\!\!\beta_2 &\!\!\!\!\!\!\!\beta_3 \end{array} \!\!\right]\!=  
\frac{ {}_{4}\!\Phi_3\left[\!\!\begin{array}{cccc} -n &\;\;\;\;\;\alpha_1 &\;\;\;\;\;\beta_1\!-\!\alpha_2 &\;\;\;\;\;\beta_1\!-\!\alpha_3 \\ &\!\!\!\!\!\!\!\!\beta_1 &\!\!1\!-\!n\!+\!\alpha_1\!-\!\beta_2 &1\!-\!n\!+\!\alpha_1\!-\!\beta_3 \end{array} \!\!\right]  
}{q^{2n\alpha_1} (\beta_2-\alpha_1)^{-1}_{n}(\beta_3-\alpha_1)^{-1}_{n}  (\beta_2)_{n}(\beta_3)_{n}}  
\!\label{sears},\\  
&&\hskip -1cm{}_{6}W_{5}(\alpha_0\; ; \;\alpha_1, \alpha_2, -n \; ; \; 1\!+\!n\!+\!\alpha_0\!-\!\alpha_1\!-\!\alpha_2 )=  
\frac{(1+\alpha_0)_{\infty}(1\!+\!\alpha_0\!-\!\alpha_1\!-\!\alpha_2)_{\infty}}{(1\!+\!\alpha_0\!-\!\alpha_1)_{\infty}(1\!+\!\alpha_0\!-\!\alpha_2)_{\infty}}.\label{phi65}  
\end{aligned}$$ Relation ([\[heine\]](#heine){reference-type="ref" reference="heine"}) is called Heine formula, relation ([\[sears\]](#sears){reference-type="ref" reference="sears"}) is the Sears Identity.

Let us now recall the definitions of $q-$Racah polynomials $p_n^{(R)}$, of the $q-$Racah discrete measure $w^{(R)}$, and of the square of the norm of these polynomials [@W][@AW1]: $$\begin{aligned}
&&\hskip -0.5cm \forall x\in \CC, \forall \alpha,\beta,\gamma,\delta\in \CC,  
\mu(x)=q^{-2x}\!+\!q^{2x+2+2\gamma+2\delta},\nonumber\\  
&&\hskip -0.5cm p_n^{(R)}(\mu(x);q^{2\alpha},q^{2\beta},q^{2\gamma},q^{2\delta})={}_{4}\!\Phi_3  
\left[\!\!\begin{array}{cccc} -n & n\!+\!1\!+\!\alpha\!+\!\beta & -x  & \gamma\!+\!\delta\!+\!x\!+\!1 \\  
&\!\!\!\!\!\!\!\!\!\alpha\!+\!1 &\!\!\!\!\!\!\!\!\beta\!+\!\delta\!+\!1 &\!\!\!\!\!\!\!\gamma\!+\!1\end{array} \!\!\right],\nonumber\\  
&&\hskip -0.5cm w^{(R)}(x;q^{2\alpha},q^{2\beta},q^{2\gamma},q^{2\delta})=\frac{(\gamma\!+\!\delta\!+\!1,\alpha\!+\!1,\beta\!+\!\delta\!+\!1,\gamma\!+\!1)_x (1-q^{2(2x+\gamma+\delta+1)})}{q^{2x(\alpha+\beta+1)}(1,\gamma\!+\!\delta\!+1-\!\alpha,\gamma\!-\!\beta\!+\!1,\delta\!+\!1)_x(1-q^{2(\gamma+\delta+1)})}\nonumber,\\  
&&\hskip -0.5cm h^{(R)}_n(q^{2\alpha},q^{2\beta},q^{2\gamma},q^{2\delta})=  
\frac{q^{2n(\gamma+\delta+1)}  
(1-q^{2(\alpha+\beta+1)})  
(1,\beta\!+\!1,\alpha\!-\!\delta\!+\!1,\alpha\!+\!\beta\!-\!\gamma\!+\!1)_n}  
{(1-q^{2(2n+\alpha+\beta+1)})  
(\alpha\!+\!\beta\!+\!1,\alpha\!+\!1,\beta\!+\!\delta\!+\!1,\gamma\!+\!1)_n}  
\times\nonumber\\  
&&\hskip 3.5cm \times \frac{(\gamma\!+\!\delta\!+\!2,\gamma\!-\!\alpha\!-\!\beta,\delta\!-\!\alpha, -\beta)_{\infty}}  
{(\gamma\!+\!\delta\!-\!\alpha\!+\!1,\gamma\!-\!\beta\!+\!1,\delta\!+\!1,\!-\!\alpha\!-\!\beta\!-\!1)_{\infty}}\label{defracahpol}.
\end{aligned}$$ The definition of Askey-Wilson polynomials $p_n^{(AW)},$ of the Askey-Wilson measure $w^{(AW)}$ and of the square of the norm of these polynomials is [@AW2]: $$\begin{aligned}
&&\hskip -1cm \forall z\in \CC, \forall \alpha,\beta,\gamma,\delta\in \CC,\tau(z)=\frac{1}{2}(q^{2z}+q^{-2z})\nonumber\\  
&&\hskip -1cm \frac{p_n^{(AW)}(\tau(z);q^{2\alpha},q^{2\beta},q^{2\gamma},q^{2\delta})}{  
q^{-2n\alpha}(\alpha\!+\!\beta,\alpha\!+\!\gamma,\alpha\!+\!\delta)_n   
}=\;{}_{4}\!\Phi_3 \!  
\left[\!\!\begin{array}{cccc} -n & n\!+\!\alpha\!+\!\beta\!+\!\gamma\!+\!\delta\!-\!1 & \alpha\!+\!z  & \alpha\!-\!z  \\  
&\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\alpha\!+\!\beta &\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\alpha\!+\!\gamma\! &\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\alpha\!+\!\delta\end{array} \!\!\right],  
\nonumber 
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1cm w^{(AW)}(z;q^{2\alpha},q^{2\beta},q^{2\gamma},q^{2\delta})=  
\frac{  
(2z, -2z)_{\infty}}  
{(\alpha+z,\alpha\!-\!z,\beta\!+\!z,\beta\!-\!z,\gamma\!+\!z,\gamma\!-\!z,\delta\!+\!z,\delta\!-\!z)_{\infty}},\label{defaskeypol}\\  
&&\hskip -1cm h^{(AW)}_n(q^{2\alpha},q^{2\beta},q^{2\gamma},q^{2\delta})=  
\frac{(\alpha\!+\!\beta\!+\!n)_{\infty}^{-1}(n+1)_{\infty}^{-1}  
(\alpha\!+\!\beta\!+\!\gamma\!+\!\delta\!+\!2n)_{\infty}  
(\alpha\!+\!\beta\!+\!\gamma\!+\!\delta\!+\!n\!-\!1)_{n}}  
{(\alpha\!+\!\gamma\!+\!n,  
\alpha\!+\!\delta\!+\!n,\beta\!+\!\gamma\!+\!n,\beta\!+\!\delta\!+\!n,\gamma\!+\!\delta\!+\!n)_{\infty}}.\nonumber 
\end{aligned}$$

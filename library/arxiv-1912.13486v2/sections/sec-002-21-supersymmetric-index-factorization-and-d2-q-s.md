---
doc_id: arxiv-1912.13486v2
doc_title: "Index for a Model of 3d-3d Correspondence for Plumbed 3-Manifolds"
section_id: sec-002-21-supersymmetric-index-factorization-and-d2-q-s
section_title: "Supersymmetric index, factorization, and D2 q S1 partition function"
section_number: 2.1
pages: 3-9
source_pdf: 1912.13486v2.pdf
source_sha256: 9a8dbc1a143f7448
toc_source: outline
text_source: latex
latex_prose_ratio: 0.916
latex_coverage_ratio: 0.966
doc_brief: "Index for a Model of 3d-3d Correspondence for Plumbed 3-Manifolds — We consider the S2 ×q S1 supersymmetric index of a 3d N = 2 theory T[M3] when M3 is a plumbed 3-manifold."
---
[]{#ssec:factorization label="ssec:factorization"}

We begin with a brief review on the formula for the index of the 3d $\mathcal{N}=2$ theory with a Lagrangian description at the UV.

### Supersymmetric index on $S^2 \times_q S^1$

The supersymmetric index on $S^2 \times_q S^1$ with fugacities for flavor symmetries turned on was obtained in [@Kapustin-Willett] based on [@KimS; @Imamura-Yokoyama]. The 1-loop contributions from the vector multiplet and the chiral mutiplet are $$\begin{aligned}
I_{\text{vect}} (z =e^{i h }, m , q) &= \prod_{\alpha \in \Delta_G } q^{-\frac{1}{4} | \alpha(s) |} (1- e^{i \alpha(h)} q^{\frac{1}{2}|\alpha(s)|}) \\
I_{\text{chiral}} (z =e^{i h }, m , q) &= \prod_{\rho \in \mathcal{R}_{\Phi}} \big( q^{\frac{1}{2}(1-R(\Phi))} \prod_{j} e^{-i\rho(h)} \prod_{a} t_a^{-f_a(\Phi)} \big)^{\frac{1}{2}| \rho(m) | } 
\frac{(e^{-i\rho(h)} t_a^{-f_a(\Phi)} q^{\frac{1}{2} |\rho(m)| +1 -\frac{1}{2} R(\Phi)} ; q)_\infty}{e^{i\rho(h)} t_a^{f_a(\Phi)} q^{\frac{1}{2} |\rho(m)| + \frac{1}{2} R(\Phi)} ; q)_\infty}
\end{aligned}$$ where $z_j$ are the Wilson lines, $m_j$ are the magnetic fluxes, $\mathcal{R}_\Phi$ is the representation of a chiral multiplet $\Phi$ under the gauge group $G$, $t_a$'s are the fugacities for the global symmetries, $f_a(\Phi)$ is the charge of a chiral multiplet $\Phi$ under the global symmetries, and $R(\Phi)$ is the $R$-charge of $\Phi$. The contribution from the Chern-Simons (CS) term for $G=U(N)$ with a level $k$ is $$\begin{aligned}
I_{\text{CS}}(z=e^{ih}, m) = e^{i k \sum_{j} h_j m_j} = \prod^{N}_{j=1} z_j^{k m_j} \,  .
\end{aligned}$$ The index is given by $$\begin{aligned}
\mathcal{I}_{S^1 \times S^2} = \sum_{\mathbf{m}} \frac{1}{|\mathcal{W}_{\mathbf{m}}|} \oint_{\mathbb{T}^{\text{rank} G}} \frac{d\mathbf{z}}{2 \pi i \mathbf{z}} \, I_{\text{vect}} \, I_{\text{chirals}} \, I_{\text{CS}}
\end{aligned}$$ where $\mathcal{W}_{\mathbf{m}}$ is a symmetrization factor from the Weyl group of the gauge group that is unbroken in the presence of the magnetic flux $\mathbf{m}$, which is given by $\prod_{l} \text{rank}(G_l)!$ when the gauge group is broken to $\otimes_{l} G_l$.

In particular, when the gauge group is $G=SU(N)$, the contributions from the vector multiplet and the adjoint chiral multiplet charged $+1$ under the global symmetry $U(1)_t$ with $R$-charge $R$ are given by $$\begin{aligned}
I_{\text{vect}} (z,m,q) &= \prod_{1\leq i \neq j \leq N} q^{-\frac{1}{4} |m_i-m_j|} (1- z_i z_j^{-1} q^{\frac{1}{2} |m_i-m_j|}) \,  ,   \label{sci-vect}    \\
I_{\text{adj}} (z,m,t, R, q) &=  \frac{( t^{-1} q^{ 1 -\frac{R}{2} };q)^{N-1}_\infty}{( t  q^{\frac{R}{2} };q)_\infty^{N-1}} 
\prod_{1 \leq i \neq j \leq N} (-q^{\frac{1}{2} (1-R)} t^{-1})^{\frac{1}{2} |m_i-m_j|} \frac{(z_i^{-1} z_j t^{-1} q^{\frac{1}{2} |m_i-m_j| +1 -\frac{R}{2} };q)_\infty}{(z_i z_j^{-1} t  q^{\frac{1}{2} |m_i-m_j| +\frac{R}{2} };q)_\infty} \,  ,   \label{sci-adj}
\end{aligned}$$ respectively, where $\prod_{j=1}^N z_j=1$ and $\sum_{j=1}^N m_j = 0$ are imposed.[^1] Also, the $q$-Pochhammer symbol, $$\begin{aligned}
(x;q)_\infty = \prod_{n=0}^{\infty} (1-xq^n)    \,  ,
\end{aligned}$$ is used. We will consider only $G=SU(N)$, in particular, $G=SU(2)$ in this paper.[^2]

### Factorization of index

The index can be factorized as a fusion of two $D^2 \times_q S^1$ partition functions [@Beem-Dimofte-Pasquetti; @Pasquetti-3d].[^3] For the vector multiplet $V$, $$\begin{aligned}
I_{\text{vect}} &= \prod_{i \neq j} q^{-\frac{1}{4}|m_i - m_j|} (1-z_i z_j^{-1} q^{\frac{1}{2} |m_i-m_j| })     \label{vect-ind}    \\
&= \prod_{1 \leq i <j \leq N} (s_i^{1/2} s_j^{-1/2} -s_i^{-1/2} s_j^{1/2}) (\tilde{s}_i^{1/2} \tilde{s}_j^{-1/2} -\tilde{s}_i^{-1/2} \tilde{s}_j^{1/2})
=: \prod_{1 \leq i <j \leq N} \| (s_i^{1/2} s_j^{-1/2} -s_i^{-1/2} s_j^{1/2}) \|_{\text{id}}^2  \label{vect-factor}
\end{aligned}$$ where $\| \cdot \|_{\text{id}}$ denotes the identity fusion [@Beem-Dimofte-Pasquetti] of half- and anti-half-index with $s_j = z_j q^{m_j/2}$ and $\tilde{s}_j = z_j^{-1} q^{m_j/2}$.\
For the adjoint chiral multiplet $\Phi_{R}^{\pm}$ charged $\pm1$ under the global symmetry $U(1)_t$ with $R$-charge $R$, $$\begin{aligned}
I^{\pm,R}_{\text{adj}} &= \frac{( t^{\mp} q^{ 1 -\frac{R}{2} };q)^{N-1}_\infty}{( t^{\pm}  q^{\frac{R}{2} };q)_\infty^{N-1}}  
\prod_{1\leq i \neq j \leq N} \frac{(z_i^{-1} z_j t^{\mp} q^{-\frac{1}{2} (m_i-m_j) +1 -\frac{R}{2} };q)_\infty}{(z_i z_j^{-1} t^{\pm}  q^{-\frac{1}{2} (m_i-m_j) +\frac{R}{2} };q)_\infty} (z_i^{-1/2} z_j^{1/2})^{-(m_i-m_j)}     \label{adj-factor-D}    \\
&= \|( t^{\mp} q^{ 1 -\frac{R}{2} };q)_\infty \|_{\text{id}}^{N-1}
\prod_{1\leq i \neq j \leq N} \bigg\| \frac{(s_i^{-1} s_j v^{\mp} q^{1 -\frac{R}{2} };q)_\infty }{\theta(-q^{1/2} s_i^{-1} s_j;q)^{1/2}} \bigg\|_{\text{id}}^2  \label{adj-block-D}
\end{aligned}$$ where $\tilde{q}=q^{-1}$, $v=t q^{n/2}$, and $\tilde{v}=t^{-1} q^{n/2}$. We also set the magnetic flux for $U(1)_t$ symmetry to zero, $n=0$, so $v=t$ and $\tilde{v}=t^{-1}$. Here, $$\begin{aligned}
\theta(x;q) = (-q^{1/2} x ;q)_\infty (-q^{1/2} x^{-1};q)_\infty
\end{aligned}$$ is the Jacobi theta function. In [\[adj-block-D\]](#adj-block-D){reference-type="eqref" reference="adj-block-D"}, we may also choose $\prod_{1 \leq i \neq j \leq N} \theta((-q^{1/2})^b s_i^{-1} s_j v^{c} ;q)$ in [\[adj-block-D\]](#adj-block-D){reference-type="eqref" reference="adj-block-D"} with arbitrary $b, c \in \mathbb{Z}$ and zero flux $n=0$ for $U(1)_t$, which gives the same index after the identity fusion. Or, since the square root to the Jacobi theta function is rather unusual, we may also replace the theta function part with other Jacobi theta functions such as $\prod_{1 \leq i < j \leq N} \theta(s_i^{-1} s_j;q)^{-1}$, which gives the same index upon the identity fusion.

The index for the adjoint chiral multiplet can also be written in another way, $$\begin{aligned}
I^{\pm,R}_{\text{adj}} &= \frac{( t^{\mp} q^{ 1 -\frac{R}{2} };q)^{N-1}_\infty}{( t^{\pm}  q^{\frac{R}{2} };q)_\infty^{N-1}} 
\prod_{1\leq i \neq j \leq N} \frac{(z_i^{-1} z_j t^{\mp} q^{\frac{1}{2} (m_i-m_j) +1 -\frac{R}{2} };q)_\infty}{(z_i z_j^{-1} t^{\pm}  q^{\frac{1}{2} (m_i-m_j) +\frac{R}{2} };q)_\infty} (z_i^{-1/2} z_j^{1/2})^{(m_i-m_j)}    \label{adj-factor-N}    \\
&= \frac{1}{ \| ( v^{\pm}  q^{\frac{R}{2} };q)_\infty \|_{\text{id}}^{N-1} }  
\prod_{1\leq i \neq j \leq N} \bigg\| \frac{\theta(-q^{1/2} s_i^{-1} s_j;q)^{1/2}}{(s_i s_j^{-1} v^{\pm} q^{\frac{R}{2} };q)_\infty } \bigg\|_{\text{id}}^2 \,  .   \label{adj-block-N}
\end{aligned}$$

We note that when $t$ is turned off, $t=1$, the contribution to the index from the adjoint chiral multiplets $\Phi^{\pm}_R$ with $R=2$ and $R=0$ become $$\begin{aligned}
 I^{\pm,R=2}_{\text{adj}} \Big|_{t \rightarrow 1} &= \frac{( t^{\mp} ;q)^{N-1}_\infty}{( t^{\pm}  q;q)_\infty^{N-1}} \bigg|_{t \rightarrow 1} \prod_{1\leq i < j \leq N} (-1)^{m_i-m_j} \| (s_i^{1/2} s_j^{-1/2} - s_i^{-1/2} s_j^{1/2}) \|_{\text{id}}^2   \,  ,   \label{adj2-factor-unref}   \\
 I^{\pm,R=0}_{\text{adj}} \Big|_{t \rightarrow 1} &= \frac{( t^{\mp} q;q)^{N-1}_\infty}{( t^{\pm} ;q)_\infty^{N-1}} \bigg|_{t \rightarrow 1} \prod_{1\leq i < j \leq N} (-1)^{m_i-m_j} \| (s_i^{1/2} s_j^{-1/2} - s_i^{-1/2} s_j^{1/2}) \|_{\text{id}}^{-2}     \,  ,   \label{adj0-factor-unref}
\end{aligned}$$ and they need to be regularized. As in [@Gukov-Pei-Putrov-Vafa; @Pei-Ye], we may take $t=q^{\epsilon}$ and multiply an overall factor $\epsilon^{-N+1}$ and $\epsilon^{N-1}$ to [\[adj2-factor-unref\]](#adj2-factor-unref){reference-type="eqref" reference="adj2-factor-unref"} and [\[adj0-factor-unref\]](#adj0-factor-unref){reference-type="eqref" reference="adj0-factor-unref"}, respectively. Then for the case of $R=2$, upon $\epsilon \rightarrow 0$, $\frac{( t^{\mp} ;q)^{N-1}_\infty}{( t^{\pm}  q;q)_\infty^{N-1}} \epsilon^{-N+1} \Big|_{t \rightarrow 1}$ becomes $(\pm \log q)^{N-1}$. Similarly, $\frac{( t^{\mp} q;q)^{N-1}_\infty}{( t^{\pm} ;q)_\infty^{N-1}} \epsilon^{N-1} \Big|_{t \rightarrow 1}  \rightarrow (\mp \log q)^{-N+1}$ for the case of $R=0$. Or we may rescale [\[adj2-factor-unref\]](#adj2-factor-unref){reference-type="eqref" reference="adj2-factor-unref"} and [\[adj0-factor-unref\]](#adj0-factor-unref){reference-type="eqref" reference="adj0-factor-unref"} by multiplying $\frac{( t^{\pm}  q;q)_\infty^{N-1}}{( t^{\mp} ;q)^{N-1}_\infty}$ and $\frac{( t^{\pm} ;q)_\infty^{N-1}}{( t^{\mp} q;q)^{N-1}_\infty}$, respectively.[^4] In this paper, when $t=1$ we will consider the regularized index for the adjoint chiral multiplets, $$\begin{aligned}
 I^{\pm,R=2}_{\text{adj}} \Big|_{t \rightarrow 1} &\simeq \prod_{1\leq i < j \leq N} (-1)^{m_i-m_j} \| (s_i^{1/2} s_j^{-1/2} - s_i^{-1/2} s_j^{1/2}) \|_{\text{id}}^2   \,  ,   \label{adj2-factor-unref-reg}   \\
 I^{\pm,R=0}_{\text{adj}} \Big|_{t \rightarrow 1} &\simeq \prod_{1\leq i < j \leq N} (-1)^{m_i-m_j} \| (s_i^{1/2} s_j^{-1/2} - s_i^{-1/2} s_j^{1/2}) \|_{\text{id}}^{-2}        \,  ,   \label{adj0-factor-unref-reg}
\end{aligned}$$ up to an overall factor, $(\pm \log q)^{N-1}$ and $(\mp \log q)^{-N+1}$, respectively. The contribution from the adjoint chiral multiplet $\Phi_{R=0}^0$ with $R=0$ and $U(1)_t$ charge 0 is given by [\[adj0-factor-unref-reg\]](#adj0-factor-unref-reg){reference-type="eqref" reference="adj0-factor-unref-reg"} after the regularization or the rescaling of $t\rightarrow 1$ limit [\[adj0-factor-unref\]](#adj0-factor-unref){reference-type="eqref" reference="adj0-factor-unref"}. In particular, when $G=SU(2)$, since $m_1=-m_2$, [\[adj2-factor-unref-reg\]](#adj2-factor-unref-reg){reference-type="eqref" reference="adj2-factor-unref-reg"} and [\[adj0-factor-unref-reg\]](#adj0-factor-unref-reg){reference-type="eqref" reference="adj0-factor-unref-reg"} with $R=2$ and $R=0$, respectively, are equal and are inverse precisely to $I_{\text{vect}}$ in [\[vect-factor\]](#vect-factor){reference-type="eqref" reference="vect-factor"}.\
The $D^2 \times_q S^1$ partition function with given $\mathcal{N}=(0,2)$ boundary conditions on 3d $\mathcal{N}=2$ multiplets and with boundary degrees of freedom was studied in [@Gadde-Gukov-Putrov-wall; @Gadde-Gukov-Putrov-4manifold; @Yoshida-Sugiyama; @Dimofte-Gaiotto-Paquette]. The contribution from the 3d bulk vector multiplet for $G=SU(N)$ with the Neumann boundary condition [@Yoshida-Sugiyama] is given by $$\begin{aligned}
\prod_{1 \leq i \neq j \leq N} e^{\frac{1}{4 \hbar} (\log s_i s_j^{-1})^2} (s_i s_j^{-1};q)_\infty
= \prod_{1 \leq i < j \leq N} e^{\frac{1}{2 \hbar} (\log s_i s_j^{-1})^2 } (s_i s_j^{-1};q)_\infty (s_i^{-1} s_i;q)_\infty  \label{vect-loc}
\end{aligned}$$ where $q=e^{\hbar}$. We note that the asymptotic expansion of the Jacobi theta function terminates at $\hbar^1$ $$\begin{aligned}
\theta(x;q) = (-q^{1/2} x;q )_\infty (-q^{1/2} x^{-1};q )_\infty \simeq C^{-1} e^{-\frac{1}{2 \hbar} (\log x)^2 }   \   \text{as }  \hbar \rightarrow 0 \label{theta-appr}
\end{aligned}$$ where $C = e^{\frac{\pi^2}{6 \hbar} - \frac{\hbar}{24}}$. Since we take $|q|<1$ (*i.e.* $q \neq 1$) in the calculation of the homological block or the index, we can use the approximation [\[theta-appr\]](#theta-appr){reference-type="eqref" reference="theta-appr"} in [\[vect-loc\]](#vect-loc){reference-type="eqref" reference="vect-loc"}. Or such replacement of exponential term in [\[vect-loc\]](#vect-loc){reference-type="eqref" reference="vect-loc"} by the theta function can be regarded as the elliptic completion of a partition function of quantum mechanics on $\mathbb{R}_+$ of $D^2 \times S^1 \simeq \mathbb{R}_+ \times T^2$ [@Beem-Dimofte-Pasquetti]. Then, the exponential term in [\[vect-loc\]](#vect-loc){reference-type="eqref" reference="vect-loc"} can be expressed as $$\begin{aligned}
\begin{split}
\prod_{i<j} e^{\frac{1}{2 \hbar} (\log s_i s_j^{-1})^2} 
&= \prod_{i<j} e^{\frac{1}{4 \hbar} (\log s_i s_j^{-1})^2 + \frac{1}{2\hbar} (\log s_i s_j^{-1}) (\pi i + \hbar/2) } e^{\frac{1}{4 \hbar} (\log s_i s_j^{-1})^2 - \frac{1}{2\hbar} (\log s_i s_j^{-1}) (\pi i + \hbar/2) }  \\
&\simeq \prod_{i<j} \theta(-q^{1/2} s_i s_j^{-1};q)^{-1/2} \theta(-q^{-1/2} s_i s_j^{-1};q)^{-1/2}  \,
\end{split} 
\end{aligned}$$ up to an irrelevant overall constant factor and the theta function ambiguity.[^5] Therefore, in the region $|q|<1$, [\[vect-loc\]](#vect-loc){reference-type="eqref" reference="vect-loc"} can be expressed as $$\begin{aligned}
&\prod_{1 \leq i < j \leq N} e^{\frac{1}{2 \hbar} (\log s_i s_j^{-1})^2 } (s_i s_j^{-1};q)_\infty (s_i^{-1} s_j;q)_\infty
\simeq \prod_{1\leq i < j \leq N} \frac{(s_i s_j^{-1};q)_\infty (s_i^{-1} s_j;q)_\infty}{\theta(-q^{1/2} s_i s_j^{-1};q)^{1/2} \theta(-q^{-1/2} s_i s_j^{-1};q)^{1/2}}  \label{vec-loc1}    \\
&= \prod_{1\leq i < j \leq N} \bigg( \frac{\theta(-q^{1/2} s_i s_j^{-1};q)}{\theta(-q^{-1/2} s_i s_j^{-1};q)} \bigg)^{1/2} (1-s_i s_j^{-1}) 
= \prod_{1\leq i < j \leq N} q^{-1/4} (s_i^{1/2} s_j^{-1/2} - s_i^{-1/2} s_j^{1/2}) \label{vect-loc2}
\end{aligned}$$ and this agrees with the factorization in [\[vect-factor\]](#vect-factor){reference-type="eqref" reference="vect-factor"} up to an irrelevant overall factor $q^{-1/4}$. We can also see that the original expression [\[vect-loc\]](#vect-loc){reference-type="eqref" reference="vect-loc"} and [\[vect-loc2\]](#vect-loc2){reference-type="eqref" reference="vect-loc2"} give the same index $\prod_{i<j} \| (s_i^{1/2} s_j^{-1/2} - s_i^{-1/2} s_j^{1/2}) \|_{\text{id}}^2$ upon the identity fusion.\
Similarly, the contribution from the 3d bulk adjoint chiral multiplet $\Phi_{R,N}^{\pm}$ and $\Phi_{R,D}^{\pm}$ with the Neumann or the Dirichlet boundary condition[^6] [@Yoshida-Sugiyama] are given by, respectively, $$\begin{aligned}
Z_{\text{adj}}^{\pm, (N)}(s_j, v, R, q) &= \prod_{1 \leq i , j \leq N} e^{ -\frac{1}{4 \hbar} \big( \log s_i/s_j +(\frac{\hbar}{2} + \pi i) (R-1) + \log v^{\pm 1} \big)^2 + \frac{\hbar}{48}} (s_i s_j^{-1} v^{\pm 1} (-q^{1/2})^{R};q)_\infty^{-1}\,, \label{adj-loc-N}   \\
Z_{\text{adj}}^{\pm, (D)}(s_j, v, R, q) &= \prod_{1 \leq i , j \leq N} e^{ \frac{1}{4 \hbar} \big( \log s_i/s_j +(\frac{\hbar}{2} + \pi i) (R-1)+ \log v^{\pm 1} \big)^2 - \frac{\hbar}{48}} (s_i^{-1} s_j v^{\mp 1} (-q^{1/2})^{2-R};q)_\infty\,.  \label{adj-loc-D}
\end{aligned}$$ As discussed above, the exponential factor in [\[adj-loc-N\]](#adj-loc-N){reference-type="eqref" reference="adj-loc-N"} and [\[adj-loc-D\]](#adj-loc-D){reference-type="eqref" reference="adj-loc-D"} can be approximated to the exact asymptotic expansion of, for example, $\prod_{1 \leq i , j \leq N} \theta((-q^{1/2})^{1-R} s_i^{-1} s_j v^{-1};q)^{\pm 1/2}$ or $\prod_{1 \leq i , j \leq N} \theta((-q^{1/2})^{\#} s_i^{-1} s_j )^{\pm 1/2}$ $\times \theta((-q^{1/2})^{1-R} v^{-1};q)^{\pm 1/2}$ up to irrelevant constant factors.

The exponential factors and the Jacobi theta function in the contributions to $D^2 \times_q S^1$ partition function above can be regarded as the factors that cancel out the (mixed) CS contributions that the $q$-Pochhammer symbols have. Putting differently, each contributions [\[vect-loc\]](#vect-loc){reference-type="eqref" reference="vect-loc"}, [\[adj-loc-N\]](#adj-loc-N){reference-type="eqref" reference="adj-loc-N"}, and [\[adj-loc-D\]](#adj-loc-D){reference-type="eqref" reference="adj-loc-D"} above are regarded as the contributions purely from the supermultiplet without any CS levels.\
Summarizing the calculations above, there are two equivalent expressions for each contribution from vector multiplets and adjoint chiral multiplets in the perspective of the index. When $G=SU(2)$, for the vector multiplet with the Neumann boundary condition, we had $$\begin{aligned}
e^{\frac{1}{2\hbar} (\log s^2)^2 } (s^{-2};q)_\infty (s^{2};q)_\infty   \,  \label{vect-loc-summ1}
\end{aligned}$$ from the localization [\[vect-loc\]](#vect-loc){reference-type="eqref" reference="vect-loc"}, and $$\begin{aligned}
s-s^{-1}        \label{vect-loc-summ2}
\end{aligned}$$ from the factorization of the index [\[vect-factor\]](#vect-factor){reference-type="eqref" reference="vect-factor"} and also from the approximation to [\[vect-loc-summ1\]](#vect-loc-summ1){reference-type="eqref" reference="vect-loc-summ1"} up to an irrelevant overall factor and the theta function ambiguity. They all give the same contribution to the index, which is [\[vect-ind\]](#vect-ind){reference-type="eqref" reference="vect-ind"}.[^7]

Similarly, for the adjoint chiral multiplets, $\Phi^{+}_{R=2, N}$, $\Phi^{-}_{R=0,D}$, and $\Phi^{0}_{R=0,N}$, the contributions to the half-index are, respectively, $$\begin{aligned}
\begin{split}
\hspace{-25mm}
e^{ -\frac{1}{2\hbar} (\log s^2)^2 } \big( (s^{-2} t q ;q)_\infty (s^{2} t q ;q)_\infty ( t q ;q)_\infty \big)^{-1} ,   \hspace{1mm}    
e^{ \frac{1}{2\hbar} (\log s^2)^2 } (s^{-2} t q;q)_\infty (s^{2} t q;q)_\infty ( t q ;q)_\infty ,   \hspace{1mm}
e^{ -\frac{1}{2\hbar} (\log s^2)^2 } \big( (s^{-2} ;q)_\infty (s^{2} ;q)_\infty \big)^{-1}  \quad\label{adj-loc-summ1}
\end{split}
\end{aligned}$$ from the localization where we ignore the background CS contributions, and $$\begin{aligned}
\hspace{-5mm}
\frac{\theta(-q^{1/2} s^{-2};q)^{1/2} \theta(-q^{1/2} s^{2};q)^{1/2}}{(s^{-2} t q ;q)_\infty (s^{2} t q ;q)_\infty ( t q;q)_\infty} \,  ,   \quad   
\frac{(s^{-2} t q;q)_\infty (s^{2} t q;q)_\infty ( t q;q)_\infty}{\theta(-q^{1/2} s^{-2};q)^{1/2} \theta(-q^{1/2} s^{2};q)^{1/2}}   \,  ,   \quad   
\frac{\theta(-q^{1/2} s^{-2};q)^{1/2} \theta(-q^{1/2} s^{2};q)^{1/2}}{(s^{-2} ;q)_\infty (s^{2} ;q)_\infty} \label{adj-loc-summ2}
\end{aligned}$$ from the factorization of the index [\[adj-block-D\]](#adj-block-D){reference-type="eqref" reference="adj-block-D"} and [\[adj-block-N\]](#adj-block-N){reference-type="eqref" reference="adj-block-N"} and also from the approximation to [\[adj-loc-summ1\]](#adj-loc-summ1){reference-type="eqref" reference="adj-loc-summ1"} up to theta function ambiguity and an irrelevant overall factor.[^8] They all give the same contributions to the index, [\[adj-factor-D\]](#adj-factor-D){reference-type="eqref" reference="adj-factor-D"} or [\[adj-factor-N\]](#adj-factor-N){reference-type="eqref" reference="adj-factor-N"}. In particular, when $t=1$, we have $$\begin{aligned}
\hspace{-5mm}
e^{-\frac{1}{2\hbar} (\log s^2)^2 } \big( (s^{-2} q ;q)_\infty (s^{2} q ;q)_\infty \big)^{-1}   \,  ,   \quad   
e^{\frac{1}{2\hbar} (\log s^2)^2 } (s^{-2} q;q)_\infty (s^{2} q;q)_\infty   \,  ,   \quad   
e^{-\frac{1}{2\hbar} (\log s^2)^2 } \big( (s^{-2} ;q)_\infty (s^{2} ;q)_\infty \big)^{-1}   \,  \label{adj-loc-summ-unref1}
\end{aligned}$$ from [\[adj-loc-summ1\]](#adj-loc-summ1){reference-type="eqref" reference="adj-loc-summ1"} and $$\begin{aligned}
s-s^{-1}    \,  ,   \quad   
(s-s^{-1})^{-1} \,  ,   \quad   
(s-s^{-1})^{-1} \,  ,   \label{adj-loc-summ-unref2}
\end{aligned}$$ from [\[adj-loc-summ2\]](#adj-loc-summ2){reference-type="eqref" reference="adj-loc-summ2"}, respectively, up to an overall factor.

### Homological block and $D^2 \times_q S^1$ partition function

It was discussed in [@Gukov-Putrov-Vafa; @Gukov-Pei-Putrov-Vafa] that the Witten-Reshetikhin-Turaev (WRT) invariants for closed 3-manifolds can be expressed in terms of $q$-series with integer powers and integer coefficients, which was called the homological block. Interestingly, the homological blocks are labeled by abelian flat connections, *i.e.* it can be regarded as the contribution from abelian flat connections to the partition function of analytically continued Chern-Simons theory whose gauge group is complex, $G_\mathbb{C}$, and at the same time it contains all the information of the contribution from non-abelian flat connections [@Gukov-Marino-Putrov]. In the perspective of the 3d-3d correspondence, this means that the homological block of $M_3$ which is labeled by an abelian flat connection corresponds to the $D^2 \times_q S^1$ partition function of the corresponding 3d $\mathcal{N}=2$ theory with a boundary condition given by the abelian flat connection [@Wfiveknots; @DGG].

Since the homological block is the $D^2 \times_q S^1$ partition function with a boundary condition, the index of $T[M_3]$ on $S^2 \times_q S^1$ is also expected to be expressed as the identity fusion of homological block and anti-homological block, $$\begin{aligned}
\mathcal{I} = \sum_{m} \frac{1}{|\mathcal{W}_m|} \oint_{|z|=1} \frac{dz}{2 \pi i z} \big\| \text{Integrand}[Z_{D^2 \times_q S^1}(q;s, \cdots)] \big\|^2_{\text{id}} \label{id-fusion}
\end{aligned}$$ where $\text{Integrand}[Z_{D^2 \times_q S^1}(q;s, \cdots)]$ denotes the integrand of the integral expression of homological blocks.

In the next section, we discuss how the discussion above fits in the case of the lens space.

[^1]: The expression for $I_{\text{adj}}$ in [\[sci-adj\]](#sci-adj){reference-type="eqref" reference="sci-adj"} comes from [@Dimofte-Gaiotto-Gukov-index; @Beem-Dimofte-Pasquetti] where there is an additional phase factor $\prod_{1 \leq i \neq j \leq N} (-1)^{\frac{1}{2}|m_i-m_j|}$ in [\[sci-adj\]](#sci-adj){reference-type="eqref" reference="sci-adj"} compared to the expression in [@Imamura-Yokoyama; @Kapustin-Willett].

[^2]: If we include a factor $\prod_{1 \leq i \neq j \leq N}(-1)^{\frac{1}{2}|m_i-m_j|}$ in [\[sci-vect\]](#sci-vect){reference-type="eqref" reference="sci-vect"} or include it in [\[sci-adj\]](#sci-adj){reference-type="eqref" reference="sci-adj"}, the analysis on the $G=SU(2)$ case in this paper where such a factor is 1 would be generalized to $G=SU(N)$ or $U(N)$ cases.

[^3]: See also [@Hwang-Park] for adjoint chiral multiplets.

[^4]: This could also be regarded as introducing extra $N-1$ free chiral multiplets with $U(1)_R \times U(1)_t$ charge $(0, \mp 1)$ and $(2, \mp 1)$ by hand, respectively.

[^5]: Here, what we mean by theta function ambiguity is that there can be various theta functions that gives the same contribution to the index upon the identity fusion. For example, contributions from $\theta(s^2;q)$ and $\theta(s;q)^4$ to the index are the same. But at the level of the half-index, only specific types of expressions of the Jacobi theta function arise from the $\mathcal{N}=(0,2)$ boundary degrees of freedom, so not all Jacobi theta functions can have a proper interpretation in the 3d-2d system on $D^2 \times_q S^1$ as contributions from boundary $\mathcal{N}=(0,2)$ chiral or Fermi multiplets.

[^6]: In this paper, we work with $\text{Tr} (-1)^R \cdots$ instead of $\text{Tr} (-1)^F \cdots$. They are equivalent when $R$-charges are integer, which is the case in our example. We replace $-q^{1/2}$ with $q^{1/2}$ if we want to use $\text{Tr} (-1)^F$ [@Beem-Dimofte-Pasquetti].

[^7]: For explicitness, the identity fusion for $e^{\frac{1}{2\hbar} (\log s^2)^2}$ is given by $e^{\frac{1}{2\hbar} (\log s^2)^2} e^{-\frac{1}{2\hbar} (\log \tilde{s}^2)^2}$.

[^8]: Also from $s^{-1} \theta(-q^{1/2} s^{-2};q)$ instead of $\theta(-q^{1/2} s^{-2};q)^{1/2} \theta(-q^{1/2} s^{2};q)^{1/2}$, we have the same desired result $(s-s^{-1})^{\pm1}$ upon $t=1$ limit. We could choose a different Jacobi theta functions, *e.g.* $\theta(s^{-2};q)$, which gives the same contribution to the index, but with this expression, we don't have $(s-s^{-1})^{\pm1}$ when $t=1$.

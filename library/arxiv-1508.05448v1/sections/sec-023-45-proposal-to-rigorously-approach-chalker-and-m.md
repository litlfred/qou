---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-023-45-proposal-to-rigorously-approach-chalker-and-m
section_title: "Proposal to Rigorously Approach Chalker and Mehlig's Result"
section_number: 4.5
pages: 83-89
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.992
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
There are various ways to try to prove Chalker and Mehlig's formula for the bulk behavior of $\mathcal{O}_N^{(2)}$. One way is to try to fill in the details to make Chalker and Mehlig's argument rigorous. Their idea is to express $\mathcal{O}_N^{(2)}$ in terms of the expectation of a function of the eigenvalues, and then use the known eigenvalue marginal for the complex Ginibre ensemble.

Here we want to propose a second method. The formula for $\mathcal{O}_N^{(2)}(z_1,z_2)$ is the determinant of a 5-diagonal matrix. One may express such a determinant through a recursion relation, although the recursion relation is significantly more complicated than in the tridiagonal case. It is higher order, and it is a vector valued recursion relation for a vector with dimension greater than $1$. We will not explicate this, here. It is well-known, it just follows from Cramer's rule, and it is widely used in numerical codes.

Instead, what we want to advocate here is solving recursion relations, at least asymptotically for large $N$, using adiabatic theory. We have not tried this yet for $\mathcal{O}_N^{(2)}(z_1,z_2)$. There may be formidable difficulties which obstruct this approach, but let us demonstrate the idea for an easier problem: re-deriving the formula for $\mathcal{R}_N^{(1)}(z)$. This leads to an easier problem. The key trick for this particular problem is to realize that $\mathcal{R}_N^{(1)}(z)$, at least for the leading-order asymptotic formula, is constant in $z$ for $|z|<1$.

## The Recurrence Relation for $\mathcal{R}_N^{(1)}(z)$ Using Matrices

We are treating the case of $\mathcal{R}_N^{(1)}(z)$ as a simpler toy model, in lieu of treating the real problem of interest which is $\mathcal{O}_N^{(2)}(z_1,z_2)$. We hope to be able to handle $\mathcal{O}_N^{(2)}(z_1,z_2)$ later, in another paper.

Recall from ([\[eq:RD\]](#eq:RD){reference-type="ref" reference="eq:RD"}) that $\mathcal{R}_N^{(1)}(z) = \pi^{-1} [(N-1)!]^{-1} \exp(-N |z|^2) D_{N-1}(z)$, which means from Stirling's formula that $$\mathcal{R}_N^{(1)}(z)\, \sim\, \frac{1}{\pi} \cdot \frac{1}{\sqrt{2 \pi N}}\, e^{-(N-1)\ln(N)+N(1-|z|^2)} D_{N-1}(z)\, .$$ Moreover, recall that there is a recursion relation in ([\[eq:Dr\]](#eq:Dr){reference-type="ref" reference="eq:Dr"}). Namely, defining $D_{N-1}(\sigma^{-2},z) = D_{N-1}(\sigma^{-1}N^{-1/2}z)$, it happens that $$D_{n+1}(\sigma^{-2},z)\, =\, (\sigma^{-2}|z|^2+n+1) D_n(\sigma^{-2},z)-\sigma^{-2}n|z|^2D_{n-1}(\sigma^{-2},z)\, .$$ Let us fix $\sigma^2=N^{-1}$ as Chalker and Mehlig do. Then $$D_{n+1}(N,z)\, =\, (N|z|^2+n+1) D_n(N,z)-Nn|z|^2D_{n-1}(N,z)\, .$$ Also, since the answer only depends on the magnitude of $z$, let us write $r=|z|$ so $$D_{n+1}(N,r)\, =\, (Nr^2+n+1) D_n(N,r)-Nnr^2D_{n-1}(N,r)\, .$$ We want to calculate $\mathcal{R}_N^{(1)}(r)$ which is asymptotically given by $$\mathcal{R}_N^{(1)}(r)\, \sim\, \frac{1}{\pi} \cdot \frac{1}{\sqrt{2 \pi N}}\, e^{-(N-1)\ln(N)+N(1-r^2)} D_{N-1}(N,r)\, .$$ Now since we have a second-order recursion relation, let us define a two-dimensional vector $v_n = [D_{n-1}(N,r),D_n(N,r)]^*$. (All our vectors and matrices will be real but we use the adjoint instead of the transpose because we want to keep the symbol $T$ for other purposes.) Then the recursion relation says that $$v_{n+1}\, =\, A_n v_n\, ,\qquad
A_n\, =\, 
\begin{bmatrix} 0 & 1 \\
-Nnr^2 & N r^2+n+1
\end{bmatrix}\, ,$$ and we want $D_{N-1}(N,r) = e_2^* v_{N-1}$, where $\{e_1,e_2\}$ is the standard basis for $\mathbb{R}^2$. In order to have a simpler formula, we note that we can write $v_1 = A_0 e_2$, for $A_0$ defined as above. In seeking $\mathcal{R}_N^{(1)}(r)$, we really have $$\mathcal{R}_N^{(1)}(r)\, \sim\, \frac{1}{\pi} \cdot \frac{1}{\sqrt{2 \pi N}} \, e^{-(N-1)\ln(N)+N(1-r^2)} e_2^* A_{N-2} \cdots A_1 A_0 e_2\, .$$ The idea is to try to express this using the spectral decomposition of the matrices $A_n$, where we use the fact that the matrices $A_n$ are *varying slowly* in $n$, as much as possible. This is why we call this the *adiabatic approach.*

## Spectral Formulas and Summary of Main Contribution

We may summarize the spectral information as $$\begin{gathered}
\lambda_n^{\pm}\, =\, \frac{N}{2} \left(r^2+\frac{n+1}{N} \pm \sqrt{\left(\frac{n+1}{N}-r^2\right)^2+4r^2N^{-1}}\right)\, ,\quad \\
V_n^{\pm}\, =\, \begin{bmatrix} 1 \\ \lambda_n^{\pm} \end{bmatrix}\, ,\quad
W_n^{\pm}\, =\, \pm\frac{1}{\lambda_n^+ - \lambda_n^-} \begin{bmatrix} - \lambda_n^{\pm} \\ 1 \end{bmatrix}\, ;\\
A_n V_n^{\pm}\, =\, \lambda_n^{\pm} V_n^{\pm}\, ,\qquad
(W_n^{\pm})^* A_n\, =\, \lambda_n^{\pm} (W_n^{\pm})^*\, ,\qquad
(W_n^{\sigma})^* V_n^{\tau}\, =\, \delta_{\sigma,\tau}\, ,\ \text{ for $\sigma,\tau \in \{+1,-1\}$.}
\end{gathered}$$ In particular, $A_n = \lambda_n^+ V_n^+ (W_n^+)^* + \lambda_n^- V_n^- (W_n^-)^*$. Therefore, we can rewrite the conclusion of the recursion relation as $$\begin{split}
\mathcal{R}_N^{(1)}(r)\, 
\sim\, \frac{1}{\pi} \cdot \frac{1}{\sqrt{2 \pi N}} \, e^{-(N-1)\ln(N)+N(1-r^2)} e_2^* A_{N-2} \cdots A_1 A_0  e_2\\
=\, \frac{1}{\pi} \cdot \frac{1}{\sqrt{2 \pi N}} \, e^{-(N-1)\ln(N)+N(1-r^2)}
\sum_{\sigma \in \{+1,-1\}^{N-1}} \left(\prod_{n=0}^{N-2} \lambda_n^{\sigma(n)}\right)
([W_0^{\sigma(0)}]^* e_2) (e_2^* V_{N-2}^{\sigma(N-2)}) \\
&\hspace{9cm}
\cdot \left(\prod_{n=0}^{N-1} [W_{n+1}^{\sigma(n+1)}]^* V_n^{\sigma(n)}\right)\, .
\end{split}$$ Anticipating that the main contribution to this sum will be $\sigma(0)=\dots=\sigma(N-1)=+1$, we may rewrite this as $$\mathcal{R}_N^{(1)}(r)\, 
\sim\, \frac{1}{\pi} \cdot \frac{1}{\sqrt{2 \pi N}} \, e^{-(N-1)\ln(N)+N(1-r^2)} \mathcal{M}_N(r) \mathcal{P}_N(r)\, ,$$ where $\mathcal{M}_N(r)$ is the "main term" $$\mathcal{M}_N(r)\,
=\,
\left(\prod_{n=0}^{N-2} \lambda_n^{+}\right)
([W_0^{+}]^* e_2) (e_2^* V_{N-2}^{+}) 
\cdot \left(\prod_{n=0}^{N-1} [W_{n+1}^{+}]^* V_n^{+}\right)\, ,$$ and $\mathcal{P}_N(r)$ will be a series of perturbations $$\mathcal{P}_N(r)\,
=\, 
\sum_{\sigma \in \{+1,-1\}^{N-1}} 
\left(\prod_{n=0}^{N-2} \frac{\lambda_n^{\sigma(n)}}{\lambda_n^+}\right)
\frac{([W_0^{\sigma(0)}]^* e_2) (e_2^* V_{N-2}^{\sigma(N-2)})}{([W_0^{+}]^* e_2) (e_2^* V_{N-2}^{+})}
\cdot \left(\prod_{n=0}^{N-1} \frac{[W_{n+1}^{\sigma(n+1)}]^* V_n^{\sigma(n)}}
{[W_{n+1}^{+}]^* V_n^{+}}\right)\, .$$ We know that we are trying to find that the leading order behavior of $\mathcal{R}_N^{(1)}(r)$ is as follows: it is constant, equal to $\pi^{-1}$, for $r<1$, and it is exponentially small for $r>1$. We will not try to recover the boundary behavior near $r=1$ in this note. (In fact, what we hope to be able to do in a later paper is to calculate $\mathcal{O}_N^{(2)}(z_1,z_2)$ in a similar way, and especially to determine the edge behavior when $z_1$ and $z_2$ are near the circle.) Let us quickly note how we may dispense with the $r>1$ case so that we may focus on $r<1$.

The largest contribution to $\mathcal{M}_N(r)$ comes from the product of eigenvalues $$\begin{gathered}
\left(\prod_{n=0}^{N-2} \lambda_n^{+}\right)
=\, \exp\left[\sum_{n=0}^{N-2} \ln( \lambda_n^{+})\right]\\
=\,e^{(N-1) \ln(N)} \exp\left(\sum_{n=0}^{N-2} \ln\left[ 
\frac{1}{2}\left(r^2+\frac{n+1}{N} + \sqrt{\left(\frac{n+1}{N}-r^2\right)^2+4r^2N^{-1}}\right)
\right]
\right)\, .
\end{gathered}$$ Moreover, defining $t_{n+1} = (n+1)/N$, the sum is $(N-1)$ times a Riemann sum approximation so that: $$\begin{split}
\frac{1}{N}\ln\left[e^{-(N-1)\ln(N)} \left(\prod_{n=0}^{N-2} \lambda_n^{+}\right)\right]\, 
&=\,
\int_0^1 \ln\left(\frac{1}{2}\left(r^2+t+\sqrt{(t-r^2)^2+4r^2N^{-1}}\right)\right)\, dt + o(1)\\
&=\, \int_0^1 \ln\left(\frac{1}{2}\left(r^2+t+\sqrt{(t-r^2)^2}\right)\right)\, dt + o(1)\\
&=\, \int_0^1 \ln(\max\{r^2,t\})\, dt + o(1)\, ,
\end{split}$$ where the remainder term $o(1)$ is a quantity which converges to $0$ as $N \to \infty$. Hence we may see, by integrating, that $$\lim_{N \to \infty} \frac{1}{N}\ln\left[e^{-(N-1)\ln(N)} \left(\prod_{n=0}^{N-2} \lambda_n^{+}\right)\right]\, 
=\, \begin{cases} \ln(r^2) & \text{ if $r\geq 1$,}\\
r^2-1 & \text{ if $r \in [0,1]$.}
\end{cases}$$ This means that, incorporating the exponential part of the prefactor for $\mathcal{R}_N^{(1)}(r)$, $$\lim_{N \to \infty} \frac{1}{N}\ln\left[e^{-(N-1)\ln(N)+N(1-r^2)} \left(\prod_{n=0}^{N-2} \lambda_n^{+}\right)\right]\, 
=\, \begin{cases} 0 & \text { if $r \in [0,1]$,}\\
\ln(r^2)-1+r^2 & \text{ if $r>1$,}
\end{cases}$$ and it is easy to see that $\ln(x) \leq x-1$ for all $x \in (0,\infty)$ by convexity of $-\ln(x)$. For $r>1$ this is exponentially small: to leading order $e^{N[\ln(r^2)-1+r^2]}$. We claim that no other factor is exponentially large, so that we obtain $$\lim_{N \to \infty} N^{-1} \ln(\mathcal{R}_N^{(1)}(r))\, 
=\, \begin{cases} 0 & \text { if $r \in [0,1]$,}\\
\ln(r^2)-1+r^2 & \text{ if $r>1$.}
\end{cases}$$ Therefore, we will henceforth assume $r<1$.

When $r<1$, we claim that we need to do a more careful analysis of the product. The time scale $t_n=n/N$ is too rough when $t_n$ is near $r^2$. The purely discrete scale $n$ is too fine. Therefore, we use the intermediate time scale $T_n = (t_n-r^2)N^{1/2}$, instead. Then we may rewrite $$\begin{gathered}
\lambda_n^{+}\,
=\, N \exp(\psi^{+}(T_{n+1}))\, ,\qquad \\
\psi^{+}(T_{n+1})\, =\, \ln\left(r^2 + \frac{1}{2}\, N^{-1/2} T_{n+1} + \frac{1}{2}\, N^{-1/2} \sqrt{T_{n+1}^2 + 4 r^2}\right)
\end{gathered}$$ so that $$\left(\prod_{n=0}^{N-2} \lambda_n^{+}\right)\,
=\, N^{N-1} \exp\left(\sum_{n=0}^{N-1} \psi^+(T_{n+1})\right)\, .$$ Then we use the Euler-Maclaurin summation formula to obtain all other terms in the asymptotic series which are significant, including some boundary terms that come with the Euler-Maclaurin formula. (To do an integral such that $\int_{-r^2 N^{1/2}}^{(1-r^2)N^{1/2}} \psi^+(T)\, dT$, one may find it useful to define $T=2r\sinh(x)$ so that $dT = 2r \cosh(x)\, dx$ and $\sqrt{T^2+4r^2} = 2r \cosh(x)$, as well. Doing all this leads to $$\left(\prod_{n=0}^{N-2} \lambda_n^{+}\right)\, \sim\, e \cdot r (1-r^2) e^{N\ln(N) - N(1-r^2)}\, .$$ It is also easy to use the definitions of $V_n^+$ and $W_n^+$ to show that $$^* e_2\,
\sim\, N^{-1} r^{-2}\quad \text{ and } \quad
e_2^* V_{N-2}^+\, \sim\, N\, .$$ Using the Euler-Maclaurin summation formula, one may also prove that $$\prod_{n=0}^{N-1} [W_{n+1}^{+}]^* V_n^{+}\,
\sim\,  \frac{r}{1-r^2}\, N^{-1/2}\, .$$ The details of the Euler-Maclaurin summation formula for this product as well as for the product of the eigenvalues are not trivial. (The product of the eigenvalues is harder than the product of the inner-products.) They may be done, in particular, by using the intermediate time-scale parameter $T_n$. Therefore, we obtain $$\mathcal{M}_N(r)\, =\, e \sqrt{N}\, e^{(N-1)\ln(N) - N(1-r^2)}\, .$$ Therefore, since $$\mathcal{R}_N^{(1)}(r) \sim \pi^{-1} (2\pi N)^{-1/2} \exp(-(N-1)\ln(N)+N(1-r^2)) \mathcal{M}_N(r) \mathcal{P}_N(r)$$ we see that $$\mathcal{R}_N^{(1)}(r)\, \sim\, \pi^{-1}\, \frac{e}{\sqrt{2\pi}}\,   \mathcal{P}_N(r)\, .$$ Now we will argue that $\mathcal{P}_N(r)$ is actually independent of $r$, to leading order.

---
doc_id: arxiv-2111.04763v2
doc_title: "Resurgence of Chern-Simons theory at the trivial flat connection"
section_id: sec-012-34-u-state-integrals
section_title: "(u,) state-integrals"
section_number: 3.4
pages: 33-35
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.911
latex_coverage_ratio: 0.9
doc_brief: "Resurgence of Chern-Simons theory at the trivial flat connection — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
[]{#sub.41statex label="sub.41statex"}

In parallel to the discussion in Sections [\[sub.AK41new\]](#sub.AK41new){reference-type="ref" reference="sub.AK41new"} and [\[sub.3x3state\]](#sub.3x3state){reference-type="ref" reference="sub.3x3state"}, we now introduce a new state-integral which depends on $\tau$, but also on a variable $u$. Let us consider the state-integral $$\mathcal{Z}_\mathcal B(u,\tau) = -\frac{{\rm i}}{2\mathsf{b}}\frac{\sinh(\pi \mathsf{b}^{-1} u)}
  {\sinh(\pi \mathsf{b}u)}
  \int_{\mathcal B} \tanh(\pi\mathsf{b}^{-1}v)
  \frac{\Phi_\mathsf{b}(-v+\frac{{\rm i}}{2}\mathsf{b}^{-1}+u)}
  {\Phi_\mathsf{b}(v-\frac{{\rm i}}{2}\mathsf{b}^{-1}+u)}
  {\rm e}^{2\pi{\rm i}u(v-\frac{{\rm i}}{2}\mathsf{b}^{-1})} {\rm d}v,$$ where the contour of integral $\mathcal B$ is not specified yet. The integrand reduces to that of [\[car\]](#car){reference-type="eqref" reference="car"} in the limit $u\rightarrow 0$. For generic $\mathsf{b}^2\in\mathbb{C}'$ so that $\mathop{\mathrm{Re}}\mathsf{b}>0$, the integrand has the following poles and zeros $$\begin{aligned}
    &\text{Poles}:\; \left\{\pm {\rm i}\mathsf{b}\left(\frac{1}{2}+m\right),\;
      \pm u -{\rm i}\mathsf{b}\left(\frac{1}{2}+m\right)-{\rm i}\mathsf{b}^{-1}n\;\big|\;
      m,n=0,1,2,\ldots
    \right\}\\
    &\text{Zeros}:\; \left\{
      \pm u +{\rm i}\mathsf{b}\left(\frac{1}{2}+m \right)+{\rm i}\mathsf{b}^{-1}(1+n)\;\big|\;
      m,n=0,1,2,\ldots
    \right\} \,.
  \end{aligned}
  \label{eq:PZ41x}$$ We can choose for the integral the contour $\mathcal{A}_N$ in the upper half plane that wraps the following poles, as in the left panel of Fig. [\[contours-fig\]](#contours-fig){reference-type="ref" reference="contours-fig"},

$$\label{vm-poles}
  v_m = {\rm i}\mathsf{b}\left(\frac{1}{2}+m\right),\quad m=0,1,2,\ldots,N-1.$$ By summing over the residues of these poles, the integral evaluates as follows

$$\mathcal{Z}_{\mathcal{A}_N}(u_{\mathsf{b}},\tau) = \sum_{n=0}^{N-1}(-1)^n
  q^{-n(n+1)/2}(qx;q)_n(qx^{-1};q)_n,\qquad
  x= {\rm e}^{u},\, q={\rm e}^{2\pi{\rm i}\tau} \,,$$

where we defined $u_{\mathsf{b}}=u/(2\pi \mathsf{b})$, as in [@GGM:peacock Eqn.(2)]. When $x = q^N$ this is none other than the colored Jones polynomial of the knot $\mathbf{4}_1$

$$\label{aint-habiro}
  \mathcal{Z}_{\mathcal{A}_N}({\rm i}N\mathsf{b},\mathsf{b}^2) = J_N^{\mathbf{4}_1}(q) =
  \sum_{n=0}^{N-1}(-1)^n
  q^{-n(n+1)/2}(q^{1+N};q)_n(q^{1-N};q)_n.$$

Alternatively, we can choose for the integral the contour $\mathcal{C}$ as in the right panel of Fig. [\[contours-fig\]](#contours-fig){reference-type="ref" reference="contours-fig"}, which is asymptotic to a horizontal line slightly below $\mathop{\mathrm{Im}}(v) = \mathop{\mathrm{Re}}(\mathsf{b}^{-1})$, but deformed near the origin in such a way that all the poles

$$v^{\pm}_{m,n} = \pm u -{\rm i}\mathsf{b}\left(\frac{1}{2}+m\right)-
  {\rm i}\mathsf{b}^{-1}n,\quad m,n=0,1,2,\ldots
  \label{eq:vmn}$$

are below the contour $\mathcal{C}$. Let $\mathcal{Z}(u,\tau):= \mathcal{Z}_{\mathcal{C}}(u,\tau)$ denote the corresponding state-integral. Similar to the discussion in Section [\[sub.AK41new\]](#sub.AK41new){reference-type="ref" reference="sub.AK41new"}, as the integrand has non-trivial contributions from infinity in the upper half plane, the two integrals $\mathcal{Z}_{\mathcal{A}_N}(u,\tau)$ and $\mathcal{Z}(u,\tau)$ are different. On the other hand, since the integrand does have vanishing contributions from infinity in the lower half plane, we can smoothly deform the contour $\mathcal{C}$ downwards so that $\mathcal{Z}(u,\tau)$ can be evaluated by summing over residues at the poles $v^{\pm}_{m,n}$, and we find

$$\begin{aligned}
  \mathcal{Z}(u,\tau)=
  &\mathcal{C}_0(x,q)
    +\frac{\tilde{x}^{-1}{\rm e}^{\frac{3\pi{\rm i}}{4}-\frac{\pi{\rm i}}{4}(\tau+\tau^{-1})}}
    {\tau^{1/2}}
    \mathcal{A}_0(x,q)\left(L\mathcal{A}_{0}(\tilde{x},\tilde{q}^{-1})
    +\frac{1-\tilde{x}}{2}\mathcal{A}_{0}(\tilde{x},\tilde{q}^{-1})\right)\nonumber \\
  &\phantom{==}
    +\frac{\tilde{x}^{-1}{\rm e}^{\frac{3\pi{\rm i}}{4}-\frac{\pi{\rm i}}{4}(\tau+\tau^{-1})}}
    {\tau^{1/2}}
    \mathcal{B}_0(x,q)\left(L\mathcal{B}_{0}(\tilde{x},\tilde{q}^{-1})
    +\frac{1-\tilde{x}}{2}\mathcal{B}_{0}(\tilde{x},\tilde{q}^{-1})
    \right),
    \label{eq:Ixq}
\end{aligned}$$ where $L\mathcal{A}_{\mu}(x,q),L\mathcal{B}_{\mu}(x,q)$ are defined as in [\[Lx12\]](#Lx12){reference-type="eqref" reference="Lx12"} with Roman letters $A,B,C$ replaced by caligraphic letters $\mathcal{A},\mathcal{B},\mathcal{C}$. As mentioned above, the change of integration contour implements the Habiro inversion of [@park-inverted]: the integration over $\mathcal{A}_N$ gives the Habiro series ([\[aint-habiro\]](#aint-habiro){reference-type="ref" reference="aint-habiro"}), while the integration over $\mathcal{C}$ involves $\mathcal{C}_0(x,q)$, which was interpreted in [@park-inverted] as an inverted Habiro series. This contribution comes from the poles $-v_m$ in the lower half-plane.

The integral $\mathcal{Z}(u,\tau)$ can also be identified with the Borel resummation of the perturbative series $\Phi^{(\sigma_j)}(x;\tau)$ for $j=0,1,2$. By inverting the matrix $M_R(\tilde{x},\tilde{q})$ in [\[eq:GMsPhix\]](#eq:GMsPhix){reference-type="eqref" reference="eq:GMsPhix"}, we can also express the Borel resummation $s_R(\Phi)(x,\tau)$ in any cone $R$ in terms of combinations of $(x,q)$- and $(\tilde{x},\tilde{q})$-series, and they can be then compared with the right hand side of [\[eq:Ixq\]](#eq:Ixq){reference-type="eqref" reference="eq:Ixq"}. For instance, in the cones $I$ and $IV$ respectively, we find $$\begin{align}
  \mathcal{Z}(u,\tau) =
  &s_I(\Phi^{(\sigma_0)})(x;\tau) -
    \frac{\tilde{x}^{1/2}-\tilde{x}^{-1/2}}
    {2(x^{1/2}-x^{-1/2})}\tau^{-1/2}s_I(\Phi^{(\sigma_2)})(x;\tau), \label{eq:Isphi-1}
  \\ =
  &s_{IV}(\Phi^{(\sigma_0)})(x;\tau) +
  \frac{\tilde{x}^{1/2}-\tilde{x}^{-1/2}}{2(x^{1/2}-x^{-1/2})}\tau^{-1/2}s_{IV}(\Phi^{(\sigma_2)})(x;\tau).
  \label{eq:Isphi-2}
\end{align}$$ This also implies that for positive real $\tau$, $$\label{eq:Isphi-3}
  \mathcal{Z}(u,\tau) =s_{\text{med}}(\Phi^{(\sigma_0)})(x;\tau) \,.$$

Finally, we can introduce the descendants of the integral $\mathcal{Z}(u,\tau)$ as follows $$\mathcal{Z}_{\lambda,\mu}(u,\tau) =
  -\frac{{\rm i}}{2\mathsf{b}}\frac{\sinh(\pi \mathsf{b}^{-1} u)}
  {\sinh(\pi \mathsf{b}u)}
  \int_{\mathcal{C}} \tanh(\pi\mathsf{b}^{-1}v)
  \frac{\Phi_\mathsf{b}(-v+\frac{{\rm i}}{2}\mathsf{b}^{-1}+u)}
  {\Phi_\mathsf{b}(v-\frac{{\rm i}}{2}\mathsf{b}^{-1}+u)}
  {\rm e}^{2\pi{\rm i}u(v-\frac{{\rm i}}{2}\mathsf{b}^{-1})-2\pi(\lambda\mathsf{b}-\mu\mathsf{b}^{-1})v}
  {\rm d}v.$$ The integrand has the same poles and zeros as in [\[eq:PZ41x\]](#eq:PZ41x){reference-type="eqref" reference="eq:PZ41x"}. To ensure convergence, the contour $\mathcal{C}$ needs slight modification: it is asymptotic to a horizontal line slightly below $\mathop{\mathrm{Im}}(v) = \frac{1}{2}\mathop{\mathrm{Re}}(\mathsf{b}^{-1})
-|\mathop{\mathrm{Re}}(\lambda\mathsf{b}-\mu\mathsf{b}^{-1})|$, and it is deformed near the origin in such a way that all the poles [\[eq:vmn\]](#eq:vmn){reference-type="eqref" reference="eq:vmn"} are below the contour $\mathcal{C}$.

Similarly, by smoothly deforming the contour downwards we can evaluate this integral by summing up residues of all the poles in the lower half plane, and we find $$\begin{aligned}
  \mathcal{Z}_{\lambda,\mu}(u,\tau) =
  &(-1)^\mu q^{\lambda/2}\left(
    \mathcal{C}_\lambda(x,q)
    +\frac{\tilde{x}^{-1}{\rm e}^{\frac{3\pi{\rm i}}{4}-\frac{\pi{\rm i}}{4}(\tau+\tau^{-1})}}
    {\tau^{1/2}}
    \mathcal{A}_\lambda(x,q)\left(L\mathcal{A}_{-\mu}(\tilde{x},\tilde{q}^{-1})
    +\frac{1-\tilde{x}}{2}\mathcal{A}_{-\mu}(\tilde{x},\tilde{q}^{-1})\right)\right.\nonumber \\
  &\left.\phantom{==}
    +\frac{\tilde{x}^{-1}{\rm e}^{\frac{3\pi{\rm i}}{4}-\frac{\pi{\rm i}}{4}(\tau+\tau^{-1})}}
    {\tau^{1/2}}
    \mathcal{B}_\lambda(x,q)\left(L\mathcal{B}_{-\mu}(\tilde{x},\tilde{q}^{-1})
    +\frac{1-\tilde{x}}{2}\mathcal{B}_{-\mu}(\tilde{x},\tilde{q}^{-1})\right)
    \right).
\end{aligned}$$

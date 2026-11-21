---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-015-push-forward-and-pull-back
section_title: "Push-forward and pull-back."
section_number: null
pages: 18-20
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 1.0
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
[]{#def:defmaps label="def:defmaps"} For spaces $X$ and $Y$ and a kernel $\Phi\colon X\to Y$ define the push-forward on Hochschild homology $\Phi_*\colon \mathop{\mathrm{HH}}_\bullet(X)\to \mathop{\mathrm{HH}}_\bullet(Y)$ as follows $$\Phi_*\left(\raisebox{-.45\height}{}\right):=\raisebox{-.45\height}{}.$$ For the reader still unhappy with diagrams, for $v\in
\mathop{\mathrm{Hom}}^\bullet(\Sigma_X^{-1},\mathsf {Id}_X)$, define $\Phi_*(v)\in \mathop{\mathrm{Hom}}^\bullet(\Sigma_Y^{-1},\mathsf {Id}_Y)$ as the following composite, which is read from the above diagram by reading upwards from the bottom: $$\begin{aligned}
  \Sigma^{-1}_Y
  &\xrightarrow{\gamma}
  \Phi\circ \Phi^{\scriptscriptstyle\vee}
  \xrightarrow{\mathsf {Id}\circ\eta\circ\mathsf {Id}}
  \Phi\circ\Sigma_X^{-1}\circ\Sigma_X\circ \Phi^{\scriptscriptstyle\vee}
  \xrightarrow{\mathsf {Id}\circ v\circ\mathsf {Id}\circ\mathsf {Id}} \Phi\circ\Sigma_X\circ
  \Phi^{\scriptscriptstyle\vee}\xrightarrow{{\begin{turn}{270}$\!\!\!\epsilon\ $\end{turn}}} \mathsf {Id}_Y.
\end{aligned}$$

Similarly define the pull-back $\Phi^*\colon \mathop{\mathrm{HH}}_\bullet(Y)\to
\mathop{\mathrm{HH}}_\bullet(X)$ as follows $$\Phi^*\left(\raisebox{-.45\height}{}\right):=\raisebox{-.45\height}{}.$$ These operations depend only on the isomorphism class of the kernel as shown by the following.

::: Proposition
[]{#prop:indepiso label="prop:indepiso"} If kernels $\Phi$ and $\hat\Phi$ are isomorphic then they give rise to equal push-forwards and equal pull-backs: $\Phi_*=\hat\Phi_*$ and $\Phi^*=\hat\Phi^*$.
:::

::: Proof
This follows immediately from the fact that the 2-morphisms $\gamma_\Phi$, $\gamma_{\hat\Phi}$, ${\begin{turn}{270}$\!\!\!\epsilon\ $\end{turn}}_\Phi$ and ${\begin{turn}{270}$\!\!\!\epsilon\ $\end{turn}}_{\hat\Phi}$ of Section [\[subsec:yphimphi\]](#subsec:yphimphi){reference-type="ref" reference="subsec:yphimphi"} are natural and thus commute with the given kernel isomorphism $\Phi\cong\hat\Phi$.
:::

The push-forward and pull-back operations are functorial in the following sense.

::: Theorem
[]{#thm:functorial label="thm:functorial"} If $\Phi\colon X\to Y$ and $\Psi\colon Y\to Z$ are kernels then the push-forwards and pull-backs compose appropriately, namely: $$(\Psi\circ\Phi)_*=\Psi_*\circ \Phi_*\colon
  \mathop{\mathrm{HH}}_\bullet(X)\to\mathop{\mathrm{HH}}_\bullet(Z)$$ and $$(\Psi\circ\Phi)^*=\Phi^*\circ \Psi^*\colon
  \mathop{\mathrm{HH}}_\bullet(Z)\to\mathop{\mathrm{HH}}_\bullet(X).$$
:::

::: Proof
This follows from the fact that the right adjunction $\tau_R$ is a 2-functor. The adjoint of $\Psi\circ\Phi$ is canonically $\tau_R(\Phi)\circ\tau_R(\Psi)$, i.e., is $\Sigma_X\circ\Phi^{\scriptscriptstyle\vee}\circ\Sigma_Y\circ\Psi^{\scriptscriptstyle\vee}$. This means that the unit of the adjunction $\mathsf {Id}\Rightarrow
  \Psi\circ\Phi\circ\Sigma_X\circ\Phi^{\scriptscriptstyle\vee}\circ\Sigma_Y\circ\Psi^{\scriptscriptstyle\vee}$ is given by the composition $\mathsf {Id}\Rightarrow\Psi\circ\Sigma_Y\circ\Psi^{\scriptscriptstyle\vee}\Rightarrow
  \Psi\circ\Phi\circ\Sigma_X\circ\Phi^{\scriptscriptstyle\vee}\circ\Sigma_Y\circ\Psi^{\scriptscriptstyle\vee}$. This gives $$(\Psi\circ\Phi)_*(w)=\raisebox{-.45\height}{}=\Psi_*\left(\Phi_*(w)\right).
  \qedhere$$
:::

::: Theorem
[]{#thm:adjadj label="thm:adjadj"} If $\Phi\colon X\to Y$ and $\Psi\colon Y\to X$ are adjoint kernels, $\Phi\dashv\Psi$, then we have $$\Phi_*=\Psi^*\colon \mathop{\mathrm{HH}}_\bullet(X)\to\mathop{\mathrm{HH}}_\bullet(Y).$$
:::

::: Proof
By the uniqueness of adjoints we have a canonical isomorphism, $\Psi\cong\tau_R(\Phi)$ and by Proposition [\[prop:indepiso\]](#prop:indepiso){reference-type="ref" reference="prop:indepiso"} $\Psi^*=(\tau_R(\Phi))^*$. It therefore suffices to show that $\Phi_*=(\tau_R(\Phi))^*$. Observe that $$\tau_R(\tau_R(\Phi))=\tau_R(\Sigma_X\circ\Phi^{\scriptscriptstyle\vee})\cong
  \tau_R(\Phi^{\scriptscriptstyle\vee})\circ
  \tau_R(\Sigma_X)\cong\Sigma_Y\circ\Phi^{{\scriptscriptstyle\vee}{\scriptscriptstyle\vee}}\circ \Sigma_X^{-1},$$ and similarly $$\tau_L(\tau_R(\Phi))\cong
 \Phi\circ\Sigma_X^{-1}\circ \Sigma_X.$$ Of course the latter is isomorphic to $\Phi$ but the Serre kernels are left in so to make the adjunctions more transparent. We now get the unit for adjunction $\tau_R(\Phi)\dashv\tau_R(\tau_R(\Phi))$ and the counit for the adjunction $\tau_L(\tau_R(\Phi))\dashv\tau_R(\Phi)$ as follows: $$\raisebox{-.45\height}{};\quad\raisebox{-.45\height}{}.$$ Thus $$\tau_R(\Phi)^*\left(w\right)
 =\raisebox{-.45\height}{}= \raisebox{-.45\height}{}=\Phi_*(w). \qedhere$$
:::

---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-072-2312-birkhoff-guenther-normal-form
section_title: "Birkhoff-Guenther normal form"
section_number: 23.1.2
pages: 119-121
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.908
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
There is a unique $\alpha \in {\mathbf C}$ such that, setting $v := u - \alpha$, the unique formal solution of $a z \sigma_qf - f = v$ is convergent. Indeed, putting $v = \sum\limits_{k >> - \infty} v_{k} z^{k}$, from the relation $a q^{n-1} f_{n-1} - f_{n} = v_{n}$, we draw that $\sum\limits_{n \in {\mathbf Z}} a_{n} q^{-n(n-1)/2} v_{n} = 0$, which also writes: $\alpha = {\mathcal{B}_{q,1}}u(a^{-1})$, where, as usual (see definition [\[defi:qBorel\]](#defi:qBorel){reference-type="ref" reference="defi:qBorel"}, page ), ${\mathcal{B}_{q,1}}u(\xi) = \sum\limits_{k >> - \infty} u_{k} q^{-k(k-1)/2} \xi^{k}$. (The letter $\xi$ is traditional for the Borel plane.) Note that the value ${\mathcal{B}_{q,1}}u(a^{-1})$ is well defined, for ${\mathcal{B}_{q,1}}u$ is an entire function. The Birkhoff-Guenther normal form of $\begin{pmatrix} 1 & u \\ 0 & a z \end{pmatrix}$ is therefore $\begin{pmatrix} 1 & {\mathcal{B}_{q,1}}u(a^{-1}) \\ 0 & a z \end{pmatrix}$.

### "Algebraic" summation

For any $a \in {\mathbf C}^{*}$, we shall set: $$\label{not100}
\theta_{q,a}(z) := {\theta_{q}}(z/a).$$ (See [\[eqn:thq\]](#eqn:thq){reference-type="eqref" reference="eqn:thq"} in the general notations of section [\[section:generalnotations\]](#section:generalnotations){reference-type="ref" reference="section:generalnotations"}.) One looks for a solution of [\[eqn:qEuler\]](#eqn:qEuler){reference-type="eqref" reference="eqn:qEuler"} in the form $f = g/\theta_{q,\lambda}$, with $g \in {\mathcal{O}}({\mathbf C}^{*})$ and $\lambda$ adequately chosen in ${\mathbf C}^{*}$. We are led to solve the equation: $a \lambda \sigma_qg - g = u \theta_{q,\lambda}$. Identifying the coefficients of the Laurent series, one gets the unique solution: $$g = \sum\limits_{n \in {\mathbf Z}} 
\dfrac{\left[u \theta_{q,\lambda}\right]_{n}}{a \lambda q^{n} - 1} z^{n},$$ which makes sense if, and only if, $\lambda \not\in [a^{-1};q]$. (Note that we write $\left[h\right]_{n} := a_{n}$ []{#not101 label="not101"} when $h = \sum a_{n} z^{n}$.) Thus, for all "authorized directions of summation" $\lambda$, we get the unique solution for [\[eqn:qEuler\]](#eqn:qEuler){reference-type="eqref" reference="eqn:qEuler"} with only simple poles over $[-\lambda;q]$: $$S_{\lambda} \hat{f} := \dfrac{1}{\theta_{q,\lambda}}
\sum\limits_{n \in {\mathbf Z}} 
\dfrac{\left[u \theta_{q,\lambda}\right]_{n}}{a \lambda q^{n} - 1} z^{n},$$

### "True" summation

Since the polar condition that uniquely characterizes the solution $S_{\lambda} \hat{f}$ only depends on $\overline{\lambda} := \lambda \pmod{q^{{\mathbf Z}}} \in {\mathbf{E}_{q}}$, or (equivalently) on $\Lambda := [\lambda;q]$, we shall also write: $$S_{\overline{\lambda}} \hat{f} := S_{\Lambda} \hat{f} := S_{\lambda} \hat{f}.$$ We now make this dependency explicit. From the equality $u \theta_{q,\lambda} = \sum u_{k} q^{-\ell(\ell+1)/2} z^{k} (z/\lambda)^{\ell}$, we draw: $$\left[u \theta_{q,\lambda}\right]_{n} =
\sum_{k + \ell = n} u_{k} q^{-\ell(\ell+1)/2} \lambda^{-\ell} =
\sum_{k} u_{k} q^{-(n-k)(n-k+1)/2} \lambda^{k-n},$$ so that: $$q^{n(n+1)/2} \lambda^{n} \left[u \theta_{q,\lambda}\right]_{n} =
\sum_{k} u_{k} q^{n k-k(k-1)/2} \lambda^{k} = {\mathcal{B}_{q,1}}u(q^{n} \lambda).$$ On the other hand, iterating the relation $\theta_{q,\lambda}(z) = \frac{z}{q \lambda} \theta_{q,q \lambda}(z)$ yields $\theta_{q,\lambda}(z) = 
\frac{z^{n}}{q^{n(n+1)/2} \lambda^{n}} \theta_{q,q^{n} \lambda}(z)$, whence: $$\label{not102}
S_{\overline{\lambda}} \hat{f} = S_{\Lambda} \hat{f} =
\sum_{n \in {\mathbf Z}} \dfrac{q^{-n(n+1)/2} \lambda^{-n} {\mathcal{B}_{q,1}}u(q^{n} \lambda)}
{z^{n} q^{-n(n+1)/2} \lambda^{-n} \theta_{q,q^{n} \lambda}(z) (a \lambda q^{n} - 1)} 
~ z^{n} =
\sum_{\mu \in \Lambda} \dfrac{{\mathcal{B}_{q,1}}u(\mu)}{(a \mu - 1) \theta_{q,\mu}(z)}
~ z^{n}.$$

::: rema
In [@RS1; @RS2; @RS3], one computes the residue of the meromorphic function $\overline{\lambda} \mapsto S_{\overline{\lambda}} \hat{f}$ at the pole $\overline{a^{-1}} \in {\mathbf{E}_{q}}$. According to the above formula, one finds: $$\text{Res}_{\overline{\lambda} = \overline{a^{-1}}} 
S_{\overline{\lambda}} \hat{f} =
\dfrac{1}{2 {\text{i}}\pi} ~ \dfrac{{\mathcal{B}_{q,1}}u(a^{-1})}{\theta_{q}(az)} \cdot$$ Indeed, for any $b \in {\mathbf C}^{*}$ and for any map $f: {\mathbf C}^{*} \rightarrow {\mathbf C}$ analytic in a neighborhood of $[b;q]$, setting: $$\forall \overline{\lambda} \in {\mathbf{E}_{q}}~,~
F\left(\overline{\lambda}\right) :=
\sum_{\mu \in [\lambda;q]} \dfrac{f(\mu)}{\mu - b},$$ defines a meromorphic map $F$ with a simple pole at $\overline{b} \in {\mathbf{E}_{q}}$ and the corresponding residue: $$\text{Res}_{\overline{\lambda} = \overline{b}} 
S_{\overline{\lambda}} \hat{f} =
\dfrac{1}{2 {\text{i}}\pi} ~ \dfrac{f(b)}{b} \cdot$$ Note that the residue of a function here makes sense, because of the canonical generator $dx = \dfrac{1}{2 {\text{i}}\pi} ~ \dfrac{dz}{z}$ of the module of differentials, which allows one to flatly identify maps on ${\mathbf{E}_{q}}$ with differentials. (Here, as usual, $z = e^{2 {\text{i}}\pi x}$, where $x$ is the canonical uniformizing parameter of ${\mathbf{E}_{q}}= {\mathbf C}/({\mathbf Z}+ {\mathbf Z}\tau)$.)
:::

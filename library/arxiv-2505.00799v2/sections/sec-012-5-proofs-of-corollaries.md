---
doc_id: arxiv-2505.00799v2
doc_title: "Quantum Modular Forms and Resurgence"
section_id: sec-012-5-proofs-of-corollaries
section_title: "Proofs of Corollaries"
section_number: 5
pages: 28-30
source_pdf: 2505.00799v2.pdf
source_sha256: cc9d2ab4c6c79b50
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.945
doc_brief: "Quantum Modular Forms and Resurgence — In 2010, Zagier described a new phenomenon which he called quantum mod- ularity."
---
[]{#sec: corollaries label="sec: corollaries"}

Here we show that the presentations that are more familiar for these modular obstructions are readily obtained from the Borel-Laplace sum representation. We first show that the modular obstruction in Corollary [\[cor: eichler\]](#cor: eichler){reference-type="ref" reference="cor: eichler"} has the stated form. This is all that is left to prove after proving Theorem [\[thm: Main\]](#thm: Main){reference-type="ref" reference="thm: Main"}.

::: prop
[]{#prop: obstruction label="prop: obstruction"} Suppose $c>0$ and $\tilde{f}$ is of Type 4. Then we have that $$\begin{aligned}
\mathcal{L}^0_1(\mathcal{B}_1(\varphi_{-d/c})) &=
  \frac{(-2\pi i)^{k-1}}{\Gamma(k-1)} \int_{-d/c}^{i\infty} f(\tau)\left(\tau- z\right)^{k-2}\;d\tau, \quad \quad (z > -d/c).
\end{aligned}$$
:::

::: proof
*Proof.* We begin with the asymptotic expansion $$\begin{aligned}
\tilde{f}(z) \sim \varphi_{-d/c}(z) = \varepsilon_d^{2k} \left( \frac{c}{d}\right)   \sum_{n=0}^\infty \frac{(-1)^{n+1-k}}{\Gamma(k-1-n) c^{2-k}} \sum_{m=1}^\infty \frac{a_f(m)\zeta_c^{am}m^{1-k}}{\left( \frac{2\pi i m}{c^2}\right)^{n+2-k}}( z+d/c)^{n}.
\end{aligned}$$ Computing the Borel transform with shift $1$ with respect to $z+d/c$ gives $$\begin{aligned}
\mathcal{B}_1(\varphi_{-d/c})(u) 

&= \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right) }{\Gamma(k-1)} \sum_{m=1}^\infty \frac{a_f(m)\zeta_c^{am}m^{1-k}(-1)^{1-k}}{c^{2-k}\left( \frac{2\pi i m}{c^2}\right)^{2-k}} \sum_{n=0}^\infty \frac{\Gamma(k-1)}{\Gamma(k-1-n) \Gamma(n+1)}\frac{(-1)^nu^{n}}{\left( \frac{2\pi i m}{c^2}\right)^{n}}
\end{aligned}$$ The second sum is equal to $(1- \frac{u}{2\pi im/c^2})^{k-2}$ for $|u| < 2\pi m/c^2$, and $$(2\pi i m/c^2)^{k-2} \left(1- \frac{u}{2\pi im/c^2}\right)^{k-2} = (2\pi i m/c^2 - u)^{k-2}$$ when $-\pi/2 < \arg(u) < \pi$. Then the above equals $$\begin{aligned}
\frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right) }{\Gamma(k-1)}  \sum_{m=1}^\infty \frac{a_f(m)\zeta_c^{am}m^{1-k}(-1)^{1-k}}{c^{2-k}\left( \frac{2\pi i m}{c^2}- u \right)^{2-k}} .
\end{aligned}$$ At this point, we compute $\mathcal{L}^0_1(u)(t)$. After a change of variables, this is given by an integral expression of the form $$\begin{aligned}
    \int_0^\infty e^{-u} \mathcal{B}_1(\varphi_{-d/c})(ut)\;du, 
\end{aligned}$$ where $t>0$. We compute $$\begin{aligned}
    \int_0^\infty e^{-u} \mathcal{B}_1(\varphi_{-d/c})(ut)\;du &= \int_0^\infty e^{-u} \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right)  }{\Gamma(k-1)}  \sum_{m=1}^\infty \frac{a_f(m)\zeta_c^{am}m^{1-k}(-1)^{1-k}}{c^{2-k}\left( \frac{2\pi i m}{c^2}- u t\right)^{2-k}}\;du\\
    &=\frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right)  (-1)^{1-k}}{c^{2-k}\Gamma(k-1)}\sum_{m=1}^\infty a_f(m) \zeta_c^{am}m^{1-k}\int_{0}^\infty \frac{e^{-u}}{\left( \frac{2\pi i m}{c^2}- u t\right)^{2-k} }\;du.
\end{aligned}$$ We now switch the order of integration and summation, and after making the change of variables $u = -2\pi i m (\tau-a/c)$ in each integral, we obtain $$\begin{aligned}
&\frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right)  (-1)^{1-k}}{c^{2-k}\Gamma(k-1)}\sum_{m=1}^\infty a_f(m) \zeta_c^{am}m^{1-k}(-2\pi i m) \int_{0}^{i\infty} \frac{e^{2\pi i m (\tau-a/c)}}{\left( \frac{2\pi i m}{c^2}+ 2\pi i m(\tau-a/c) t\right)^{2-k} }\;d\tau   \\

&= \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right)  (-1)^{1-k}}{c^{2-k}\Gamma(k-1)}\sum_{m=1}^\infty a_f(m) \frac{-2\pi i m^{2-k}}{(2\pi i m)^{2-k}} \int_{a/c}^{i\infty} \frac{e^{2\pi i m \tau}}{(\tau - a/c)^{2-k}\left(\frac{ 1}{c^2(\tau-a/c)}+ t\right)^{2-k} }\;d\tau.    
\end{aligned}$$ Using that $\frac{1}{c^2(\tau- a/c)} = \frac{-d}{c} - \frac{d\tau -b}{-c\tau +a}$ and changing variables $t=z+d/c$, we obtain $$\begin{aligned}
 \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right)}{\Gamma(k-1)}\sum_{m=1}^\infty \frac{ a_f(m)}{(2\pi i)^{1-k}} \int_{a/c}^{i\infty} \frac{(-c\tau + a)^{k-2} e^{2\pi i m \tau}}{\left(-\frac{d\tau -b}{-c\tau+a}+ z\right)^{2-k} }\;d\tau,   
\end{aligned}$$ noting that collecting $-1/c$ with $\tau+a/c$ under the square root introduced a sign. Interchanging the order of integration and summation once again, the above becomes $$\begin{aligned}
\frac{(2\pi i)^{k-1}}{\Gamma(k-1)}\varepsilon_d^{2k} \left( \frac{c}{d}\right)  \int_{a/c}^{i\infty} \frac{(-c\tau + a)^{k-2} \sum_{m=1}^\infty a_f(m) e^{2\pi i m \tau}}{\left(-(\frac{d\tau -b}{-c\tau+a}- z\right))^{2-k} }\;d\tau,
\end{aligned}$$ which under the change of variables $\tau \mapsto \gamma(\tau)$ gives $$\begin{aligned}
\frac{(2\pi i)^{k-1}}{\Gamma(k-1)} \int_{i\infty}^{\gamma^{-1}(i\infty)} \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right) (c\tau +d)^{2-k} \sum_{m=1}^\infty a_f(m) e^{2\pi i m \gamma(\tau)}}{\left(-(\tau - z\right))^{2-k} }\;\frac{d\tau}{(c\tau +d)^2}.
\end{aligned}$$ Using the fact that $f$ is a modular form of weight $k$, as well as introducing an extra sign from pulling the $-1$ from under the square root, this becomes $$\frac{(-2\pi i)^{k-1}}{\Gamma(k-1)} \int_{-d/c}^{i\infty} f(\tau)\left(\tau- z\right)^{k-2}\;d\tau. \qedhere$$ ◻
:::

 

The same argument as above, taking into consideration differing signs at a few steps, allows us to also show the following.

::: prop
Suppose $c<0$ and $\tilde{f}$ is of Type 4. Then we have that $$\mathcal{L}^\pi_1(\mathcal{B}_1(\varphi_{-d/c})) =
 \frac{(-2\pi i)^{k-1}}{\Gamma(k-1)} \int_{-d/c}^{i\infty} f(\tau)\left(\tau- z\right)^{k-2}\;d\tau, \quad \quad (z > -d/c).$$
:::

Corollary [\[cor: eichler\]](#cor: eichler){reference-type="ref" reference="cor: eichler"} follows from the above since by Theorem [\[thm: Main\]](#thm: Main){reference-type="ref" reference="thm: Main"}, the obstruction to modularity equals the Borel-Laplace sum $\mathcal{L}^0_1(\mathcal{B}_1(\varphi_{-d/c}))$ or $\mathcal{L}^\pi_1(\mathcal{B}_1(\varphi_{-d/c}))$ depending on the sign of $c$.

We remark that the above arguments also work in the case of integer weight Eichler integrals. However, the following shows how we can see the coefficients of the period polynomial explicitly from our resurgence methods.

::: prop
[]{#prop: polynomial label="prop: polynomial"} Suppose $g$ is of Type 3 for $\text{SL}_2(\mathbb{Z})$. Then if $g$ is the Eichler integral of $f$, we have that $$\mathcal{L}^0_1(\mathcal{B}_1(\varphi_{0}))(z) = \frac{(-2\pi i)^{k-1}}{\Gamma(k-1)} \sum_{n=0}^{k-2}{k-2\choose n} i^{n-1}\Lambda(f; n+1)z^n.$$
:::

::: proof
*Proof.* Our work in Section [\[subsec: asymptotics\]](#subsec: asymptotics){reference-type="ref" reference="subsec: asymptotics"} computed $\varphi_0(z)$ for $g$ of *Type 3* to be $$\sum_{n=0}^{k-2}  \frac{L(f; n+1)i^{n-k}}{(2\pi)^{n+2-k}{\Gamma(k-1-n)} } z^n.$$ Since this is just a polynomial, it is equal to its own Borel-Laplace sum, and so we can manipulate it directly. Multiplying by $$\frac{\Gamma(k-1)\Gamma(n+1)}{\Gamma(k-1)\Gamma(n+1)}$$ and collecting terms gives the desired result. ◻
:::

---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-031-72-an-exchangeable-pair
section_title: "An exchangeable pair"
section_number: 7.2
pages: 41-43
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.973
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
The first step consists in building a $d$-tuple $\tilde{W}_d^*$, such that $(\tilde{W}_d,\tilde{W}_d^*)$ is an exchangeable pair. The construction that we will describe here is due to Fulman [@FulmanFluctuationChA2].

His construction uses Markov chains, so let us begin by fixing some terminology. Let $X$ be a finite set. A Markov chain $M$ on $X$ is the data of transition probability $M(x,y)$ indexed by pairs of elements of $X$ with $$M(x,y) \ge 0 \text{ and } \sum_{y \in X} M(x,y) =1.$$ If $x$ is a random element of $X$ distributed with probability $\mathbb{P}$, then, applying once the Markov chain $M$, we obtain by definition a random element $y$ of $X$, defined on the same probability space as $x$, whose conditional distribution is given by: $$P ( y= y_0 | x=x_0 ) = M(x_0,y_0).$$ Using the notation above, the Markov chain $M$ is termed *reversible* with respect to $\mathbb{P}$ if the distribution of $(x,y)$ is the same as the distribution of $(y,x)$, or equivalently, for any $x_0,y_0$ in $X$, $$\mathbb{P}(\{x_0\}) M(x_0,y_0) = \mathbb{P}(\{y_0\}) M(y_0,x_0).$$ Reversible Markov chains can be used to construct exchangeable pairs as follows. Let $M$ be a reversible Markov chain on a finite set $X$ with respect to a probability measure $\mathbb{P}$. Consider also a $\mathbb{R}^d$-valued function $W$ on $X$. We consider a random element $x$ distributed with respect to $\mathbb{P}$ and $y$ obtained by applying the Markov chain $M$ to $\mathbb{P}$. Then, directly from the definition, one sees that $(W(x),W(y))$ is exchangeable.

So, to construct an exchangeable pair for $\tilde{W}_d$, it is enough to construct a reversible Markov chain with respect to Jack measure. We present now Fulman's construction of such a Markov chain.

Let $\tau \vdash n-1$ and $\lambda \vdash n$. If $\tau$ is not contained in $\lambda$ (as Young diagrams), then define $\phi^{(\alpha)}(\lambda/\tau) =0$. Otherwise, denote by $\lambda / \tau$ the box which is in $\lambda$ and not in $\tau$. Let $C_{\lambda / \tau}$ ($R_{\lambda / \tau}$, respectively) be the column (row, respectively) of $\lambda$ that contains $\lambda / \tau$. We define $$\phi^{(\alpha)}(\lambda/\tau) = \prod_{\Box \in C_{\lambda / \tau} \setminus R_{\lambda / \tau}} \frac{(\alpha a_\lambda(\Box) + \ell_\lambda(\Box)
+1) 
(\alpha a_\tau(\Box) + \ell_\tau(\Box)+\alpha)}{(\alpha a_\lambda(\Box) + \ell_\lambda(\Box)
+\alpha) 
(\alpha a_\tau(\Box) + \ell_\tau(\Box)+1)}.$$ Let $$c_\lambda^{(\alpha)} = \prod_{\Box \in \lambda} (\alpha a(\Box) + \ell(\Box)
+1)$$ and $$(c'_\lambda)^{(\alpha)} = \prod_{\Box \in \lambda} (\alpha a(\Box) + \ell(\Box)
+\alpha).$$ We recall that $j_\lambda^{(\alpha)}=c_\lambda^{(\alpha)}(c'_\lambda)^{(\alpha)}.$ For $\lambda, \rho \vdash n$ we define two functions: $$\label{eq:TransitionM}
M^{(\alpha)}(\lambda,\rho) = \frac{(c'_\lambda)^{(\alpha)}}{n \alpha c_\rho^{(\alpha)}} \sum_{\tau \vdash n-1} \frac{\phi^{(\alpha)}(\lambda/\tau)\phi^{(\alpha)}(\rho/\tau) c_\tau^{(\alpha)}}{(c'_\tau)^{(\alpha)}}$$ and $$\label{eq:TransitionL}
L^{(\alpha)}(\lambda,\rho) = \frac{1}{\alpha^n n! j_\rho^{(\alpha)}}\sum_{\mu \vdash n}(z_\mu)^2 \alpha^{2\ell(\mu)}\theta_\mu(\lambda)\theta_\mu(\rho)\theta_\mu((n-1,1)).$$

As explained by Fulman [@FulmanFluctuationChA2], both $M^{(\alpha)}$ and $L^{(\alpha)}$ are defined to be a deformation of a certain Markov chain which is reversible with respect to Plancherel measure. Roughly speaking, this Markov chain remove one box from a given Young diagram with certain probability and add another box with some probability to obtain a new Young diagram of the same size as the one from which we started. Fulman [@FulmanFluctuationChA2] proved the following:

::: proposition
[@FulmanFluctuationChA2 Section 4] []{#prop:FulmanComputations label="prop:FulmanComputations"}

1.  If $\rho \neq \lambda$ then $$L^{(\alpha)}(\lambda,\rho) = \frac{\alpha(n-1) + 1}{\alpha(n-1)} M^{(\alpha)}(\lambda,\rho);$$

2.  Let $\lambda \vdash n$. Then $$\sum_{\rho \vdash n} L^{(\alpha)}(\lambda, \rho) = \sum_{\rho \vdash n} M^{(\alpha)}(\lambda, \rho) = 1;$$

3.  $L^{(\alpha)}$ (hence $M^{(\alpha)}$ as well) is reversible with respect to Jack measure.
:::

For more details about this construction (and in particular, the intuition behind it), we refer to Fulman [@FulmanFluctuationChA2].

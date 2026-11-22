---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-008-22-talagrands-isoperimetric-inequality
section_title: "Talagrand's Isoperimetric Inequality"
section_number: 2.2
pages: 19-28
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
The concentration of measure inequality presented in this section is also due to Talagrand. In [@Talagrand], a theory of isoperimetric inequaliies on product spaces is developed. The theorem presented here is just one of the many isoperimetric inequalities proved and applied in that work. Once the necessary notions of distance are defined and the theorem proved, the applications of the theorem are vast and obtained quickly. Before stating the theorem, we need to set up our product space and define a special notion of distance on the space.

We will begin with a probability space which we will denote by $(\Omega, \mathcal{F}, P)$. To give an idea of what we mean when we talk about a product probability space, we will give an example of the product of two probability spaces.

Suppose that we have two probability spaces given by $(\Omega_1,\mathcal{F}_1, P_1)$ and $(\Omega_2, \mathcal{F}_2, P_2)$. We want to form a product space which is the \"product\" of these two probability spaces. For ease of notation, we will usually just denote the product space by $\Omega_1\times \Omega_2$, leaving the sigma algebras and the measures implicit. Our new measure space is just the cross product $\Omega_1\times\Omega_2$. The new sigma algebra is given by the tensor product $\mathcal{F}_1\otimes \mathcal{F}_2$. We define the product measure $P_1\times P_2$ by $(P_1\times P_2)(F_1\times F_2)=P_1(F_1)P_2(F_2)$ for all $F_1\in\mathcal{F}_1$ and $F_2\in \mathcal{F}_2$. We can then define a product of $n$ probability spaces by extending this notion.

Given our probability space $(\Omega,\mathcal{F},P)$, we will be considering the product space $\Omega^n$. Given $A\subseteq\Omega^n$, Talagrand's isoperimetric inequality gives us bounds on the measure of the set of points that are within a specified distance of this set $A$. Before we can state the inequality, we need to develop a notion of distance.

For $x\in\Omega^n$ and $A\subset\Omega^n$, we define Talagrand's convex distance to be $$d_T(x,A)=\min\left\{ t \; : \;\forall \{\alpha_i\}, \;\exists y\in A \;\mathrm{such}\;\mathrm{that}\; \sum_{i=1}^n \alpha_i
\mathbbm{1}\{x_i\not = y_i\}\leq t\left(\sum_{i=1}^n \alpha_i ^2 \right)^{\frac{1}{2}}\right\}$$ The similarity between $d_T(x,A)$ and Hamming's distance $$d_H(x,A)=\inf_{y\in A} \sum_{i=1}^n \mathbbm{1}(x_i\not = y_i)$$ should be noted. Notice that if all $\alpha_i=n^{-1/2}$, then Talagrand's convex distance is always at least as large as $n^{-1/2}$ times the Hamming distance. One of the main reasons that we use $d_T(x,A)$ instead of $d_H(x,A)$, is that $d_T(x,A)$ not only allows us to weight the summands differently, it allows us to choose weights that explicitly depend on the values of the $x_i$. This flexibility allows the inequality to be applied to a much wider range of problems.

A second (and equivalent) way of defining Talagrand's convex distance is by $$\label{conv}
d_T(x,A)=\sup\left\{z_{\alpha}\; : \;z_{\alpha}=\inf_{y\in A}\sum_{i=1}^n \alpha_i(x)\mathbbm{1}(x_i\not = y_i) \;\mathrm{and}\; \sum_{i=1}^N\alpha_i^2(x)\leq 1\right\}$$

To gain a bit of understanding about the convex distance, let us look at a simple example. Suppose that we are working in one dimension. Let $x\in\mathbb{R}$ and let our set $A$ just be $\{y\}$, the set containing only the point $y\in\mathbb{R}$. Then $$d_T(x,\{y\})=\min\{t\geq 0\; : \; \forall \alpha\in\mathbb{R}_{>0}, \; \; \; \alpha\mathbbm{1}(x\not = y)\leq t\|\alpha\|\}$$ $$=\left\{
     \begin{array}{lr}
       1 & \;\mathrm{if}\; y\not = x\\
       0 & \;\mathrm{if}\; y=x
     \end{array}
   \right.$$

Given $A\subset\omega^n$, we define $$A_t=\{x\in\Omega^n \; : \;d_T(x,A)\leq t\}$$ In other words, $A_t$ is the set of all points that are within a distance $t$ of $A$. The following inequality can be found in [@Talagrand] and tells us that for a set $A$ of \"reasonable size\", $P(A_t)$ is close to $1$.

::: thm
[]{#tal label="tal"} For every $A\subset\Omega^n$, we have $$\int_{\Omega^n}\exp\left(\frac{1}{4}d_T^2(x,A)\right)dP(x)\leq \frac{1}{P(A)}$$ and consequently $$P(d_T(x,A)>t)\leq \frac{e^{-t^2/4}}{P(A)}$$ and $$P(A_t)\geq 1-\frac{e^{-t^2/4}}{P(A)}$$
:::

It should be noted that the proof given here more closely follows the proof as given in [@Steele] as opposed to [@Talagrand]. The method is basically the same as Talagrand's original proof although some components are presently slightly differently and appear in a different order.

Before we can begin the proof of the theorem, we need a deeper understanding and a different characterization of the convex distance. We will begin by defining a set $U_A(x)$. Elements of this set will be elements of $\mathbb{R}^n$ containing only $0$'s and $1$'s. We will begin with the set $U'_A(x)$, which is the set of all vectors $u_y=(\mathbbm{1}(x_1\not= y_1), \mathbbm{1}(x_2\not = y_2),\dots ,\mathbbm{1}(x_n\not = y_n))$ for $y\in A$. We then let $U_A(x)$ be the set which includes all of these vectors in addition to all vectors we can obtain from $U'_A(x)$ by switching some of the $0$'s to $1$'s. In other words, $u\in U_A(x)$ if and only if $u-u_y\geq 0$ for all $y\in A$. We then define the set $V_A(x)$ to be the convex hull of $U_A(x)$. By convex hull, we mean the set of all convex combinations of vectors in $U_A(x)$. We then have the following dual characterization of $d_T(x,A)$.

::: prop
$$d_T(x,A)=\min\{\|v\|_2: v\in V_A(x)\}$$
:::

::: proof
*Proof.* Begin with $$\min_{y\in A}\sum_{i=1}^n \alpha_i\mathbbm{1}(x_i\not = y_i)$$ Using the definition of $U_A(x)$, this is $$\min_{u\in U_A(x)} \sum_{i=1}^n\alpha_i u_i$$ Using the fact that the minimum of a linear functional on a convex set is equal to the minimum over the set of extreme points, we have that the above is equal to $$\min_{v\in V_A(x)}\sum_{i=1}^n\alpha_i v_i$$ Next, we apply the Cauchy-Schwarz inequality to get $$\leq \min_{v\in V_A(x)}\left\{\sum_{i=1}^n\alpha_i^2\right\}^{1/2}\left\{\sum_{i=1}^n v_i\right\}^{1/2}$$ $$=\left\{\sum_{i=1}^n\alpha_i ^2\right\} \min \{\|v\|_2: v\in V_A(x)\}$$ Recalling Talagrand's convex distance, $$d_T(x,A)=\min\left\{ t \; : \;\forall \{\alpha_i\}, \;\exists y\in A \;\mathrm{such}\;\mathrm{that}\; \sum_{i=1}^n \alpha_i
\mathbbm{1}\{x_i\not = y_i\}\leq t\left(\sum_{i=1}^n \alpha_i ^2 \right)^{\frac{1}{2}}\right\}$$ we immediately have $$d_T(x,A)\leq\min \{\|v\|_2\; : \;v\in V_A(x)\}$$ by our last inequality.

Now we need to prove the reverse inequality. By the linear functional characterization of the Euclidean norm, there is an $\alpha$ with $\|\alpha\|_2=1$ such that for all $v\in V_A(x)$, we have $$\sum_{i=1}^n\alpha_i v_i \geq \min \{\|v\|_2\; : \;v\in V_A(x)\}$$ By definition of $V_A(x)$, this implies that for all $y\in A$, we have $$\sum_{i=1}^n\alpha_i \mathbbm{1}(x_i\not = y_i)\geq \min \{\|v\|_2\; : \;v\in V_A(x)\}$$ Using equation (2.2), this immediately applies the reverse inequality ◻
:::

Now that this result is established, we can prove Talagrand's isoperimetric inequality.

::: proof
*Proof.* (*of Theorem 2.2.1)* To prove the theorem, we will use induction on the dimension of the product space. To prove the base case, we will start with $n=1$. In this case we have $$d_T(x,A)=\min \{\|v\|_2\; : \;v\in V_A(x)\}$$ which is $$\left\{
     \begin{array}{lr}
       1 & : x \notin A\\
       0 & : x \in A
     \end{array}
   \right.$$ Plugging this into the integral from Talagrand's theorem, we have $$\int_{\Omega}\exp\left(\frac{1}{4}d_T^2(x,A)\right)dP(x)=e^0\int_A dP(x)+e^{1/4}\int_{A^c}dP(x)$$ $$=P(A)+e^{1/4}(1-P(A))$$ If we can show that this quantity is $\leq 1/P(A)$, the base case will be proved. This will be relatively easy to show, using a little bit of calculus. For ease of notation, let $p=P(A)$. Then (multiplying on both sides of the equation by $p$), we need to prove that $$p^2+e^{1/4}p(1-p)\leq 1$$ To prove this, we will take derivatives to find the $p$ that maximizes $p^2+e^{1/4}p(1-p)-1$. Taking the derivative and solving for $p$ gives $p\approx 2.26$. Hence, on the interval $[0,1]$, $p^2+e^{1/4}p(1-p)$ obtains its maximum at $1$. At $p=1$, the inequality is satisfied, so the base case is proved.

Now we will proceed with the inductive step. Assume that for any $A\subseteq\Omega^n$, we have $$\int_{\Omega^n}\exp\left(\frac{1}{4}d_T(x,A)^2\right)dP(x)\leq \frac{1}{P(A)}$$ where $P(A)$ now represents our product measure on $\Omega^n$. We need to check and make sure that the inequality holds for dimension $n+1$. We start with an arbitrary $A\subseteq \Omega^{n+1}$. We will begin by writing $\Omega^{n+1}$ as $\Omega^n\times \Omega$. Let $x\in\Omega^n$ and $\omega\in \Omega$. Then $(x,\omega)\in\Omega^{n+1}$. We will consider two different sets. Following Steele, we will define the following as the $\omega$ section of $A$, given by $$A(\omega)=\{x \; :\;(x,\omega)\in A\}\subset\Omega^n$$ and the projection of $A$, given by $$B=\bigcup_{\omega\in\Omega}A(\omega)=\{x\; :\; \exists  (x,\omega)\in A\}\subset\Omega^n$$ To prove the theorem, we will show that $d_T(x,A)$ (in $n+1$ dimensions) can be bounded in terms of the convex distances for the $\omega$ sections and the projections. To do this, we prove the following lemma.

::: lem
For all $0\leq t\leq 1$ and $A(\omega)$ and $B$ as defined above, we have $$d_T^2((x,\omega), A)\leq t(d_T^2(x,A(\omega)))+(1-t)(d_T(x,B))^2 +(1-t)^2$$
:::

Using the alternative characterization of $d_T$ from Proposition 2.2.2, we can find vectors $v_1\in V_{A(\omega)}(x)$ and $v_2\in V_B(x)$ such that $d_T(x,A(\omega)=\|v_1\|$ and $d_T(x,B)=\|v_2\|$.

First we note that $(v_1,0)\in V_A(x,\omega)$. To see this, use the fact that since $v_1\in V_{A(\omega)}(x)$, we know that $v_1^{(i)}$ (the $i$th component of $v_1$) is equal to $\mathbbm{1}(x_i\not = y_i)$ for some $y\in A(\omega)$ for all $i$. Then, if $y\in A(\omega)$, we know that $(y,\omega)\in A$. Hence, $v_1^{n+1}=\mathbbm{1}(\omega\not =\omega)=0$.

Next, we note that $(v_2,1)\in V_A(x,\omega)$. This follows immediately from the fact that starting from a vector in $U_A'(x,\omega)$, we can always change $0$'s to $1$'s and remain in $U_A(x,\omega)$, and hence in $V_A(x,\omega)$.

Since $V_A(x,\Omega)$ is convex, $$t(v_1,0)+(1-t)(v_2,1)=(tv_1+(1-t)v_2,1-t)$$ is also in $V_A(x,\Omega)$. Notice that by our alternative characterization of $d_T$, $\|(tv_1+(1-t)v_2,1-t)\|$ is an upper bound on $d_T((x,\omega),A)$. $$\|(tv_1+(1-t)v_2,1-t)\|^2=\sum_{i=1}^n(tv_1^{(i)}+(1-t)v_2^{(i)})^2+(1-t)^2$$ $$\leq t\|v_1\|_2^2+(1-t)\|v_2\|_2^2+(1-t)^2$$ Using $d_T(x,A(\omega))=\|v_1\|$ and $d_T(x,B)=\|v_2\|$, we have proved the lemma.

Keeping $\omega$ fixed, define $I_n(\omega)$ to be the $n$-fold integral given by $$I_n(\omega)=\int_{\Omega^n}\exp\left(\frac{1}{4} d_T^2((x,\omega),A)\right)dP(x)$$ Using Lemma 2.2.3, we have that $$I_n(\omega)\leq \int_{\Omega^n}\exp\left(\frac{1}{4}(t d_T^2(x,A)+(1-t)d_T^2(x,B)+(1-t)^2)\right)dP(x)$$ $$=\exp\left(\frac{(1-t)^2}{4}\right) \int_{\Omega^n}\exp\left(\frac{t}{4}d_T^2(x,A)\right)\exp\left(\frac{1-t}{4} d_T^2(x,B)\right) dP(x)$$ Recall that Holder's inequality says that $$\int |fg| \; d\mu\leq \left(\int |f|^p\;d\mu\right)^{1/p}\left(\int|g|^p\;d\mu\right)^{1/q}$$ Applying this to (2.7) with $p=1/t$ and $q=1/(1-t)$ gives $$I_n(\omega)\leq \exp\left(\frac{(1-t)^2}{4}\right)\left(\int_{\Omega^n}\exp\left(\frac{1}{4}d_T^2(x,A)\right)dP(x)\right)^t\left(\int_{\Omega_k}\exp\left(\frac{1}{4}d_T^2(x,B)\right)dP(x)\right)^{1-t}$$ Now, by the induction hypothesis, we have $$I_n(\omega)\leq \exp\left(\frac{(1-t)^2}{4}\right)\left(\frac{1}{P(A(\omega))}\right)^t\left(\frac{1}{P(B)}\right)^{1-t}$$ $$=\frac{1}{P(B)}\left(\frac{P(A(\omega))}{P(B)}\right)^{-t}\exp\left(\frac{(1-t)^2}{4}\right)$$ Since $A(\omega)\subset A(B)$, we know that $P(A(\omega))\leq P(B)$. In order to complete the proof of the theorem, we need the following lemma.

::: lem
For all $0\leq r\leq 1$, we have $$\inf_{0\leq t\leq 1}r^{-t}\exp\left(\frac{1}{4}(1-t)^2\right)\leq 2-r$$
:::

The proof of this lemma is essentially a calculus exercise, but we will give an outline. Taking the derivative of $r^{-t}\exp\left(\frac{1}{4}(1-t)^2\right)$ with respect to $t$ gives $$-\exp \left(\frac{1}{4}(1-t)^2\right)r^{-t}(\ln(r)+1/2(1-t)$$ Optimizing in $t$ gives $t=1+2\ln(r)$, which can be shown to be a minimum. Plugging back into $r^{-t}\exp\left(\frac{1}{4}(1-t)^2\right)$ gives $$r^{-1+2\ln(r)}\exp(1/4(1-1-ln(r))^2)$$ After some simplification, we get that the above $$=r^{2\ln(r)+1}$$ To show that $r^{2\ln(r)+1}\leq 2-r$, we just need to show that $r+r^{2\ln(r)+1}\leq 2$. Using calculus, one can show that $r+r^{2\ln(r)+1}$ is decreasing on $0\leq r\leq 1$ and therefore, the inequality is true. This concludes the proof of the lemma.

Applying this lemma to equation (2.8) gives $$I_n(\omega)\leq \frac{1}{P(B)}\left(2-\frac{P(A(\omega))}{P(B)}\right)$$ This can now be integrated with respect to $\omega$, which gives $$\int_{\Omega^{n+1}}\exp\left(\frac{1}{4}d_T((x,\omega),A)\right)dP(x)dP(\omega)\leq\frac{1}{P(B)}\left(2-\frac{P(A)}{P(B)}\right)$$ $$=\frac{1}{P(A)}\frac{P(A)}{P(B)}\left(2-\frac{P(A)}{P(B)}\right)$$ Notice that if we can prove that $$\frac{P(A)}{P(B)}\left(2-\frac{P(A)}{P(B)}\right)\leq 1$$ then our proof will be complete. Letting $x=\frac{P(A)}{P(B)}$, we want to determine for which $x$, $x(2-x)\leq 1$, or equivalently, for which $x$, $x^2-2x+1\geq 0$. Since this factors as $(x-1)^2$, this inequality is true for all $x$, which completes the proof. ◻
:::

As previously mentioned, although the setup and proof of this theorem took a fair amount of work, most applications of the theorem are elegant and quick. See [@Steele] for a discussion and explanation of common applications. In addition, we will see an application in a later chapter.

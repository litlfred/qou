---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-008-52-restrictions-to-3-strands-and-the-ocneanu-tra
section_title: "Restrictions to 3 strands, and the Ocneanu trace"
section_number: 5.2
pages: 21-22
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
toc_source: outline
text_source: latex
latex_prose_ratio: 0.919
latex_coverage_ratio: 0.893
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
We recall that the notation $MT_3(M)$ was defined in section \ref{sectH3}. We note that
$$
t_3^H(1) = \left( \frac{y+1}{x} \right)^2 \ \  
t_3^H(s_1) =\frac{y+1}{x}  \ \  
t_3^H(s_1s_2) = 1 \ \  
$${}
and define additional elements $t_3^S$, $t_3^K$
of $MT_3(M)$ by
$$
t_3^S(1) = a^3,\ \ \ \ t_3^S(s_1) = t_3^S(s_1s_2) = 0, \ \ \ \ 
t_3^S((s_1s_2^{-1})^2)=  x^2(2a+x),
$$
{}
$$
t_3^K(1) = \delta_K^2,\ \ \ \ t_3^K(s_1) = \delta_K,\ \ \ \ t_3^K(s_1s_2) = 1,
\ \ \ \ \delta_K =  \frac{y^2 - ax+y}{xy}, 
$${}
$$
 t_3^K((s_1 s_2^{-1})^2) = x^3 y(y+1) + x^2(y^2 + 2a + \frac{a}{y}) - x(1+y) - (y + a + \frac{a}{y}).
$$
\begin{prop} \label{prop:MT3bmw} Let $t \in MT_3(M)$ factorizing through $\WBMW_3$.
\begin{enumerate}
\item  The trace $t$ is uniquely
determined by $t(1)$, $t(s_1)=t(s_2)$ and $t(s_1s_2)$. 
\item If $x(a^2-y^2)$ is invertible in $M$ then $t$ is  uniquely determined by $t(1)$ and $t(s_1s_2)$.
\item If $x^2(a^2-y)$ is invertible in $M$ then $t$ is  uniquely determined by $t(s_1)$ and $t(s_1s_2)$.
\item If $x(a^2-y^2)$ and $x^2(a^2-y)$ are invertible in $M$ then $t$ is uniquely determined by $t(s_1s_2)$.
\end{enumerate}
\end{prop}
\begin{proof} Let $t \in MT_3(M)$ factorizing though $\WBMW_3$. With the notations of proposition \ref{propMT3}
we write $t = \alpha e_1^* + \beta e_2^* + \gamma e_3^* + \delta e_4^*$. By direct calculation,
we check that the equation $t(\mathcal{R}_1s_1) = 0$ means
$$0=-{x}^{2} \left( {a}^{2}+ax+y \right) \alpha +
 {\frac {x \left( 2\, \left( y+1 \right) {a}^{3}+2\,x \left( y+1 \right) {a}^{2}+a \left( {x}^{2}+y \left( y+1
 \right)  \right) +yx \right) }{a}}\beta $${}$$+{\frac {- \left( y+1 \right) ^{2}{a}^{3}-x \left( y+1 \right) ^{2}{a}^{2}+a \left( -{x}^{2}-2\,{x}^{2}y+y \left( {y}^{
2}+y+1 \right)  \right) -yx \left( y+1 \right) }{a}} \gamma + {y}^{2} \delta
$$ 
and, since $y$ is invertible, this proves that $t$ is determined by $\alpha, \beta$ and $\gamma$,
meaning that $t$ is uniquely determined by $t(1)$, $t(s_1)$ and $t(s_1s_2)$, which proves (i).
Similarly, we get that $t(s_1^{-1}\mathcal{R}_1)=0$ reads
$$
(a^2-y^2) \left( x t(s_1) - (y+1) t(s_1s_2) \right) = 0
$$
and $t(\mathcal{R}_1)=0$ means
$$
x^2(a^2-y) t(1) = \frac{(a^2-y)(y+1) - x(y-1)a}{a} \left( x t(s_1) - (y+1) t(s_1s_2) \right) + \frac{x}{a}(y+1)(a^2-y) t(s_1)
$$
which easily implies (ii)-(iv).
\end{proof}

\begin{cor} Let $(t_n)$ be a Markov trace factoring through $(\WBMW_n)$ with values in $M$.
If  $x(a^2-y^2)$ and $x^2(a^2-y)$ are invertible in $M$ then $(t_n)$ is a multiple of $(t_n^H)$ composed
with some morphism $R \to M$.
\end{cor}
\begin{proof}
Immediate consequence of (iv) together with proposition \ref{prop:unicitetracegen}.
\end{proof}

Recall that $S^{\dagger} = S/(a^2-y) = R[x^{-1}]/(a^2-y)$ and $BMW_n^{\dagger} = \WBMW_n \otimes_R S^{\dagger}$.

\begin{prop} \label{propmarkovypas1} Let $t'_n$ be the composite of $t_n$ with $M \to M \otimes_R S^{\dagger}[ (y-1)^{-1}]$.
 Then $(t'_n)$ is a scalar multiple of the composite of $t_n^H$ with some morphism $R \to M$ and with $M \to M \otimes_R S^{\dagger}[ (y-1)^{-1}]$.
 \end{prop}
\begin{proof}
Inside $S^{\dagger}[(y-1)^{-1}]$ we have $a^2 -y^2 = y(1-y)$, hence by proposition \ref{prop:MT3bmw} (ii)
we have that $t'_3$ is uniquely determined by $t'_3(1)$ and $t'_3(s_1s_2)$,
and more precisely the equation $t'_3(s_1^{-1}\mathcal{R}_1)=0$ means
$t'(s_1) = \frac{y+1}{x} t'(s_1 s_2)$. Let $t_n^{\circ} = t'_n - t'_3(s_1s_2) t_n^H$.
Then $t_3^{\circ}(s_1s_2) = 0$ hence $t_3^{\circ}(s_1) = 0$ and therefore $t_3^{\circ} =  a^{-3}t_3^{\circ}(1) t_3^S$.
Let $\tau = t_4^{\circ} \circ \iota_3$, where $\iota_3 : \WBMW_3 \to \WBMW_4$ is the natural map. Again by
 \ref{prop:MT3bmw} (ii) we know that $\tau$ is uniquely determined by $\tau(1)$ and $\tau(s_1s_2)$. Moreover
 $\tau(s_1s_2) = t_4^{\circ}(s_1s_2) = t_4^{\circ}(s_2s_3) = t_3^{\circ}(s_2) = t_3^S(s_2) = 0$.
 It follows that $\tau(s_1) = 0$, since $\tau(s_1) = \frac{y+1}{x} \tau(s_1 s_2)$.
 But $\tau(s_1) =  t_4^{\circ}(s_1) =t_4^{\circ}(s_3) = t_3^{\circ}(1)$, hence $t_3(1) = 0$ and
 $t_3^{\circ} = 0$. We prove by induction on $n$ that $t_n^{\circ}(1) = 0$. Assume we
 know that $t_r^{\circ}(1) = 0$ for all $r \leq n$, and consider the composite $\tau$ of $t_{n+1}^{ \circ}$
 with the natural map $\WBMW_3 \to \WBMW_{n+1}$. We have $\tau(s_1s_2) = t_{n+1}^{\circ}(s_1 s_2)
 = t_{n+1}^{\circ}(s_{n-1} s_{n})= t_{n-1}^{\circ}(1) = 0$. It follows as before that $\tau(s_1) = 0$,
 hence $t_n^0(1) = t_{n+1}^0(s_n) = t_{n+1}^0(s_1) = \tau(s_1) = 0$. It follows that $t_n^{\circ}(1) = 0$,
 and the claim follows by induction because of proposition \ref{unicitetn1}.
\end{proof}

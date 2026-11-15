---
doc_id: arxiv-2006.02042v1
doc_title: "The Strong AJ Conjecture for the Figure 8 Knot"
section_id: sec-009-26-step-6-applying-initial-conditions
section_title: "Step 6: Applying initial conditions"
section_number: 2.6
pages: 8-9
source_pdf: 2006.02042v1.pdf
source_sha256: 9de75ced3a3360bb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.907
doc_brief: "The Strong AJ Conjecture for the Figure 8 Knot — Motivated by the theory of quantum A-ideals of Frohman-Gelca-LoFaro, the theory of q-holonomicity of quantum invariants of Garoufalidis-Le and the AJ"
---
Now we take into account the initial conditions \eqref{eq: 2}--\eqref{eq}. Firstly, we note that equations \eqref{eq: 2} and \eqref{eq: -2} hold true since we chose $p_2(t,M)=  p_{-2}(t,M)=1.$ Secondly, by taking $t=1$ in $p_1(t,M) = p_{-1}(t,M^{-1})$ we have $p_1(1,M) = p_{-1}(1,M^{-1})$. This implies that $p_1(1,M) = \tilde{a}_{1}(M)$ if and only if $p_{-1}(1,M)= \tilde{a}_{-1}(M)$. Meaning equations  \eqref{eq: 1} and \eqref{eq: -1} are equivalent. 

Thirdly,  by taking $t=1$ in equation \eqref{eq:Dio1} we have 
$$A_1(1,M)p_0(1,M)+B_1(1,M)p_1(1,M)=C_1(1,M).$$
By a direct calculation we can check that  $A_1(1,M)\tilde{a}_{0}(M)+B_1(1,M) \tilde{a}_{1}(M)=C_1(1,M)$. This implies that $p_1(1,M) = \tilde{a}_{1}(M)$ if and only if
$p_0(1,M)= \tilde{a}_{0}(M)$. Meaning equations  \eqref{eq: 1} and \eqref{eq} are equivalent. Hence we have shown that the initial conditions \eqref{eq: 2}--\eqref{eq} reduce to a single equation $p_1(1,M) = \tilde{a}_{1}(M)$. 

Since $$p_1(1,M)=\tilde p_1(1,M)+\frac{f(1,M)A_2(1,M)}{\gcd(A_2(1,M), B_2(1,M))},$$ by a direct calculation we see that the condition $p_1(1,M) = \tilde a_1(M)$ is equivalent to $f(1, M) = M^{-8} - M^{-6} + 35 M^{-4} + 18 M^{-2} + 29 + 20 M^{2}$. This suggests that we may consider the polynomial $f(t,M)$ in equation \eqref{eq:f} of the following form
$$f(t, M) = M^{-8} - M^{-6} + 35 M^{-4} + 18 M^{-2} + 29 + 20 M^{2} + (t^2 - 1) h(t, M)$$
for some  unknown function $h(t,M)$. Now it remains to find $h(t,M)$ explicitly.

With the change of variable $h(t, M) = t^8 M^{-6} k(t, M)$, equation \eqref{eq:f} becomes  
\begin{eqnarray*}
&& k(t, M) + k(t, M^{-1}) \\
&=&  2 t^4 + 2 t^6 + (1 + t^2 - 11 t^4 - 11 t^6 + 12 t^8 + 12 t^{10}) (M^2 +M^{-2}) \\ 
 && + \, (1 + t^2 - 5 t^4 - 5 t^6 + 7 t^8 + 7 t^{10} + t^{12} + t^{14}) (M^4 + M^{-4}) 
 \\
 && + \, (2 + 2 t^2 - 10 t^4 - 10 t^6 + 9 t^8 + 9 t^{10} - 2 t^{12} - 2 t^{14} - 
  2 t^{16} - 2 t^{18}) (M^6 + M^{-6}) \\
  && + \,  (1 + t^2 - 7 t^4 - 7 t^6 + 7 t^8 + 7 t^{10}) (M^8 + M^{-8}).
\end{eqnarray*}
It is easy to see that a solution of this equation is
\begin{eqnarray*}
k(t, M) 
&=&   t^4 +  t^6 + (1 + t^2 - 11 t^4 - 11 t^6 + 12 t^8 + 12 t^{10}) M^2  \\ 
 && + \, (1 + t^2 - 5 t^4 - 5 t^6 + 7 t^8 + 7 t^{10} + t^{12} + t^{14}) M^4 
 \\
 && + \, (2 + 2 t^2 - 10 t^4 - 10 t^6 + 9 t^8 + 9 t^{10} - 2 t^{12} - 2 t^{14} - 
  2 t^{16} - 2 t^{18}) M^6 \\
  && + \,  (1 + t^2 - 7 t^4 - 7 t^6 + 7 t^8 + 7 t^{10}) M^8.
\end{eqnarray*}

With this we have an explicit solution $f(t,M)$ and hence an explicit solution $b_0$. More precisely, we have
$$
b_0(t, M) = -\frac{(-1 + M) (1 + M) (1 + M^2) t^4 (-M^2 - M^4 - M^6 + 
     t^4 + M^8 t^4 - M^4 t^8)}{
  M^2 (M - t) (M + t) (-1 + M t) (1 + M t) (M^2 + t^2) (1 + M^2 t^2)}.
$$

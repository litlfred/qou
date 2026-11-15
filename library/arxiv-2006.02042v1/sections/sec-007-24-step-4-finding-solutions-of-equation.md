---
doc_id: arxiv-2006.02042v1
doc_title: "The Strong AJ Conjecture for the Figure 8 Knot"
section_id: sec-007-24-step-4-finding-solutions-of-equation
section_title: "Step 4: Finding solutions of equation (??)"
section_number: 2.4
pages: 6-7
source_pdf: 2006.02042v1.pdf
source_sha256: 9de75ced3a3360bb
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.884
doc_brief: "The Strong AJ Conjecture for the Figure 8 Knot — Motivated by the theory of quantum A-ideals of Frohman-Gelca-LoFaro, the theory of q-holonomicity of quantum invariants of Garoufalidis-Le and the AJ"
---
We see that  equation \eqref{eq:Dio1} 
is reminiscent of a Diophantine equation.
Recall for $a,b,c,x,y\in \BZ$, the equation
$$ax+by=c$$
has the following solutions
$$
x = x_0 + \frac{b}{\gcd(a,b)}k, \qquad
y=y_0 - \frac{a}{\gcd(a,b)}k,
$$
where $(x_0,y_0)$ is a particular solution of the equation, $k\in \BZ$, and $\gcd(a,b)$ is the greatest common divisor of $a,b$.

We will apply the same idea to our problem, except that our ring is a polynomial ring. Given a particular solution $(\tilde p_0, \tilde p_1)$ of equation \eqref{eq:Dio1}, a family of solutions is given by
\begin{eqnarray*}
p_0(t,M)&=&\tilde p_0(t, M) - \frac{f(t, M) B_2(t, M)}{\gcd(A_2,B_2)},\\
p_1(t,M)&=&\tilde p_1(t, M) + \frac{f(t, M) A_2(t, M)}{\gcd(A_2,B_2)},
\end{eqnarray*}
where 
$\gcd(A_2,B_2)$ is the greatest common divisor between $A_2,B_2$, and $f$ is an arbitrary polynomial. 
To find a particular solution $(\tilde p_0, \tilde p_1)$, we express $C_2$ in terms of the Groebner basis $\mathrm{gb}$ and then we express the Groebner basis in terms of $A_2,B_2$ using the matrix $\mathrm{mat} = \{m_{ij}\}$. Indeed, recall that $C_2=q_1 g_1 + q_2 g_2 + q_3 g_3 + q_4 g_4$. Moreover
 \begin{eqnarray*}
g_1 &=& m_{11} A_2 + m_{12} B_2,\\
g_2 &=& m_{21} A_2 + m_{22} B_2,\\
g_3 &=& m_{31} A_2 + m_{32} B_2,\\
g_4 &=& m_{41} A_2 + m_{42} B_2.
\end{eqnarray*}
Hence $C_2 = A_2 \tilde p_0+B_2 \tilde p_1$
where
\begin{eqnarray*}
\tilde p_0 &=& q_1 m_{11}+q_2 m_{21} + q_3 m_{31} + q_4 m_{41},\\
\tilde p_1 &=& q_1 m_{12}+q_2 m_{22} + q_3 m_{32} + q_4 m_{42}.
\end{eqnarray*}
Explicitly, we have
\begin{eqnarray*}
\tilde p_0 &=&\frac{1}{M^4 t^{10}} (-M^4 t^2 - M^6 t^2 - M^8 t^2 + 2 M^{12} t^2 + M^{14} t^2 + t^6
   - M^2 t^6 \\
   && + \, 14 M^4 t^6 + 5 M^6 t^6 - 2 M^8 t^6 + 3 M^{10} t^6 - 
     10 M^{12} t^6 - 6 M^{14} t^6 - M^{16} t^6 \\
     && - \, M^{18} t^6 - 12 t^{10} + 
     6 M^2 t^{10} + 18 M^4 t^{10} + 17 M^6 t^{10} + 6 M^8 t^{10}- 12 M^{10} t^{10} \\
     && - \, 14 M^{12} t^{10} - 19 M^{14} t^{10} + 4 M^{16} t^{10} + 8 M^{18} t^{10} - 13 t^{14}+ 6 M^2 t^{14} \\
     && + \,  35 M^4 t^{14} + 23 M^6 t^{14} + 
     2 M^8 t^{14} - 10 M^{10} t^{14} - 26 M^{12} t^{14} -  25 M^{14} t^{14} \\
     && + \,  4 M^{16} t^{14} + 6 M^{18} t^{14} - 12 t^{18} + 6 M^2 t^{18} + 20 M^4 t^{18} + 17 M^6 t^{18} +  3 M^8 t^{18} \\
     && - \,  12 M^{10} t^{18} - 15 M^{12} t^{18} - 
     18 M^{14} t^{18} + 4 M^{16} t^{18} + 7 M^{18} t^{18} - M^2 t^{22} \\
     &&  + \,  13 M^4 t^{22} + 7 M^6 t^{22} - 3 M^8 t^{22} - 10 M^{12} t^{22} - 6 M^{14} t^{22} + 2 M^4 t^{26} -  M^6 t^{26} \\
     && - \, 2 M^8 t^{26} - M^{10} t^{26} + 
     2 M^{12} t^{26} + 2 M^{14} t^{26} - 2 M^{16} t^{26} - 2 M^8 t^{30}+ 2 M^{12} t^{30}), \\
\tilde p_1&=&\frac{1}{M^4 t^{10}}
   (-1 + M^2 t^4 + M^8 t^4 + M^{10} t^4 + 2 M^{12} t^4 + M^{14} t^4 + 
     M^6 t^8\\
     && - \, 14 M^8 t^8 - 7 M^{10} t^8 - 12 M^{12} t^8 - 8 M^{14} t^8 + 
     13 M^4 t^{12} + 6 M^6 t^{12} - M^8 t^{12} \\
     && + \, 2 M^{10} t^{12} - 10 M^{12} t^{12} - 6 M^{14} t^{12} + 13 M^4 t^{16} + 7 M^6 t^{16} - 2 M^8 t^{16} \\
     &&- \, 11 M^{12} t^{16} - 7 M^{14} t^{16} + 12 M^4 t^{20} + 
     6 M^6 t^{20} + 10 M^8 t^{20} + 6 M^{10} t^{20} \\
     && + \, M^6 t^{24} + 2 M^{12} t^{24} - 2 M^8 t^{28}).
\end{eqnarray*}

---
doc_id: arxiv-2006.02042v1
doc_title: "The Strong AJ Conjecture for the Figure 8 Knot"
section_id: sec-008-25-step-5-imposing-condition-on-solutions
section_title: "Step 5: Imposing condition (??) on solutions"
section_number: 2.5
pages: 7-8
source_pdf: 2006.02042v1.pdf
source_sha256: 9de75ced3a3360bb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.75
latex_coverage_ratio: 0.7
doc_brief: "The Strong AJ Conjecture for the Figure 8 Knot — Motivated by the theory of quantum A-ideals of Frohman-Gelca-LoFaro, the theory of q-holonomicity of quantum invariants of Garoufalidis-Le and the AJ"
---
We now implement the condition $b_0(t,M^{-1})=-b_0(t,M)$. Since $$b_0(t,M)=-\frac{a_0(t,t^2 M)-a_1(t,t^2 M) p_1(t,M)}{a_1(t,M)a_1(t,t^2 M)},$$ we see that $b_0(t,M^{-1})=-b_0(t,M)$ is equivalent to
\begin{eqnarray*}
&& (M^8 t^{14} - M^4 t^{10}) p_1(t, M) - (M^8 t^{10} - M^4 t^{14}) p_1(t, M^{-1}) \\
&=&
  1 + M^{12} - M^2 t^4 - M^4 t^4 - M^8 t^4 - M^{10} t^4 - M^4 t^8 - 
   M^8 t^8 + M^4 t^{16} \\
   && + \,  M^8 t^{16} + M^2 t^{20} + M^4 t^{20} + M^8 t^{20} + 
   M^{10} t^{20} - t^{24} - M^{12} t^{24}.
\end{eqnarray*}

By replacing $p_1(t,M)=\tilde p_1(t,M)+\frac{f(t,M)A_2(t,M)}{\gcd(A_2, B_2)}$, the above equation is equivalent to
\begin{eqnarray}\label{eq:f}
&&
M^{14} t^8 f(t, M) + M^2 t^8 f(t, M^{-1}) \\
&=& \nonumber
-1 - 2 M^2 - M^4 - M^6 - M^{10} - M^{12} - 2 M^{14} - M^{16}  \nonumber\\  
    && + \, 8 t^4 + 12 M^2 t^4 + 6 M^4 t^4 + 12 M^6 t^4
    - 2 M^8 t^4 + 12 M^{10} t^4 + 6 M^{12} t^4 + 12 M^{14} t^4  \nonumber\\
    && + \,  8 M^{16} t^4 + 6 t^8 + 10 M^2 t^8 + 6 M^4 t^8 + 13 M^6 t^8 + 13 M^{10} t^8 + 6 M^{12} t^8 + 
    10 M^{14} t^8  \nonumber\\
    && + \,  6 M^{16} t^8 + 7 t^{12} + 11 M^2 t^{12} + 6 M^4 t^{12} + 
    12 M^6 t^{12} + 12 M^{10} t^{12} + 6 M^{12} t^{12} \nonumber\\
    && + \, 11 M^{14} t^{12} + 7 M^{16} t^{12} + M^4 t^{16} + M^{12} t^{16} - 2 M^2 t^{20} - 2 M^{14} t^{20}. \nonumber
\end{eqnarray}

---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-012-61-definition
section_title: "Definition"
section_number: 6.1
pages: 24-26
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.898
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
We define an algebra $F_n$ over $A = \Q[a,x,x^{-1}]/(a^2 = 1)$ by generators
$s_1,\dots,s_{n-1}$, $e_1,\dots,e_{n-1},C$ and relations
\begin{enumerate}
\item $s_i s_{i+1} s_i  = s_{i+1} s_i s_{i+1}$, $s_i s_j = s_j s_j$
\item $(s_i -a)(s_i^2 -x s_i+1)=0$
\item $e_i = a \left( \frac{ s_i^{-1} + s_i}{x} - 1 \right)$
\item $s_i e_i = a e_i$
\item $e_i s_{i+1} e_i =  e_i+C$
\item $e_i s_{i-1} e_i =  e_i+C$
\item $e_i s_{i+1}^{-1} e_i =  e_i+C$
\item $e_i s_{i-1}^{-1} e_i =  e_i+C$
\item $s_i C = C s_i = a C$.
\end{enumerate}
Letting  $\tilde{\delta} = 2 - ax $, we have $e_i^2= \tilde{\delta}x^{-1} e_i$. 
Immediate consequences of these relations are
$s_i^{-1} C = C s_i^{-1} = a C$, $e_i C = C e_i = x^{-1} \tilde{\delta}C$,
$C^2 = (x^{-2} \tilde{\delta}^2 a - x^{-1} \tilde{\delta})C = x^{-1} \tilde{\delta}(a x^{-1} \tilde{\delta} - 1) C
= 2x^{-2} \tilde{\delta}( a-x) C$. Note
that, in the specializations $x = a$ and $x = 2a$, we have $C^2 = 0$.

The following is easily checked
\begin{prop} \label{propbasiqueFn}
\begin{enumerate}
\item The $S^{\dagger\dagger}$-algebra $F_n \otimes_A S^{\dagger\dagger}$ is a quotient of $H_n \otimes_R S^{\dagger\dagger}$ through $s_i \mapsto s_i$ and $A \to S^{\dagger\dagger}$ being given by $x \mapsto b+c$. This quotient factorizes through $BMW_n^{\dagger\dagger}$.
\item There is a surjective morphism of $S^{\dagger\dagger}_{\pm}$-algebras $F_n \otimes_A S^{\dagger\dagger}_{\pm} \onto BMW_n^{\pm} \otimes_{S_{\pm}} S^{\dagger\dagger}_{\pm}$ satisfying
$s_i \mapsto s_i$, $e_i \mapsto e_i$, $C \mapsto 0$. Its kernel is the linear span of $C$.
\item The automorphism and antiautomorphism of $A$-algebras of the group algebra $A B_n$
defined by $s_i \mapsto s_i^{-1}$ induce an automorphism and a antiautomorphism of $F_n$.
\item Every Markov trace $(t_n)$ factorizing through $F_n$ is uniquely determined by $t_3(1)$, $t_3(s_1)$
and $t_3(s_1s_2)$.
\end{enumerate}
\end{prop}

\begin{proof}
We start with (i). Only the fact that we have a factorization through $BMW_n^{\dagger\dagger}$ requires a justification.
According to proposition \ref{proppresWBMWidemp}, it is sufficient to show that $s_1 e_2s_1$ and $s_2^{-1} e_1 s_2^{-1}$
are mapped to the same element. Using the same computations as in the proof of proposition \ref{propWBMWetendbien}
we easily get that both are sent to $x e_1 s_2^{-1} + ax C + x e_2 s_1 - s_2 e_1 s_2^{-1}$, and this proves the claim. 
(ii) is easy, because the linear span of $C$ is clearly a two-sided ideal of $F_n$. (iii) is easily checked from the defining relations of $F_n$.
We now prove (iv). From the arguments of proposition \ref{prop:unicitetracegenplus}  one
easily gets that such a Markov trace is uniquely determined by $t_3$ together with the collection of the $t_n(C)$,
since $C = e_{n-1} s_n e_{n-1} - e_{n-1}$.  Because $Cs_n = aC$ we get $a t_{n+1}(C) = t_n(C)$, whence the Markov trace is uniquely determined by $t_3$, and
therefore by $t_3(1)$, $t_3(s_1)$ together with $t_3(s_1s_2)$ by proposition \ref{prop:MT3bmw}. 


\end{proof}

\begin{cor} If $(t_n)$ is a Markov trace factoring through $F_n$, then the associated link invariant
does not distinguish mirrors and does not detect non-invertible links.
\end{cor}
\begin{proof} This follows from the items (iii) and (iv) of the proposition : the mirror of the closed braid $\hat{\beta}$
is the closure of the image of $\beta$ under the automorphism $s_i \mapsto s_i^{-1}$,  the mirror of the inverse is the closure of the image of $\beta$
under the antiautomorphism $s_i \mapsto s_i^{-1}$. Since $t_3(s_1) = t_3(s_1^{-1})$,
$t_3(1) = t_3(1^{-1})$, $t_3(s_1s_2) = t_3(s_1^{-1} s_2^{-1})$, such a Markov trace coincides by (iv) with its 
composite with the (anti-)automorphisms defined in (iii), whence the conclusion. 
\end{proof}

\begin{prop} \label{proprelrecutraceFn} If $(t_n)$ is a Markov trace factoring through $F_n$, then
\begin{enumerate}
\item $\forall n \geq 3 \ \ t_{n+1}(C) = a t_n(C)$
\item $\forall n \geq 2\ \ t_{n+1}(C) = a t_{n+1}(1) - a x^{-1}(\tilde{\delta} + 2)t_n(1) +2a \tilde{\delta} x^{-2} t_{n-1}(1)$
\item For all $n \geq 1$,
$$t_{n+3}(1)=   \left( a+\frac{\tilde{\delta} + 2}{x}\right)t_{n+2}(1) -\frac{1}{x} \left(2 \frac{\tilde{\delta}}{x}+a(\tilde{\delta} + 2) \right) t_{n+1}(1) 
 +2a \frac{\tilde{\delta}}{x^2} t_{n}(1)$$
\end{enumerate}
\end{prop}
\begin{proof} (i) is trivially deduced from $s_n C = a C$ and the Markov property.
From $C = e_{n-1} s_n e_{n-1} - e_{n-1}$ we get
$t_{n+1}(C) = t_{n+1}(e_{n-1}^2 s_n) - t_3(e_{n-1}) = \tilde{\delta}x^{-1}t_{n+1}(e_{n-1} s_n) - t_{n+1}(e_{n-1})
= \tilde{\delta}x^{-1}t_n(e_{n-1}) - t_{n+1}(e_n)$ by the Markov property and because $e_{n-1}$ and $e_n$ are conjugates.
Expanding $e_i = (a/x)(s_i + s_i^{-1}) - a$ and using the Markov property again we
get
$t_{n+1}(C) = \tilde{\delta}x^{-1}(2a/x t_{n-1}(1) - a t_n(1)) - (2a/x t_n(1) - a t_{n+1}(1)) =
a t_{n+1}(1) - a x^{-1}(\tilde{\delta} + 2)t_n(1) +2a \tilde{\delta} x^{-2} t_{n-1}(1)$, namely (ii).
By (i) we know $t_{n+1}(C) = a t_{n+2}(C)$ hence, by (ii), we get
$t_{n+1}(C) = a t_{n+2}(C) =  t_{n+2}(1) -  x^{-1}(\tilde{\delta} + 2)t_{n+1}(1) +2 \tilde{\delta} x^{-2} t_{n}(1)$
 hence, again by (ii),  $t_{n+2}(1) -  x^{-1}(\tilde{\delta} + 2)t_{n+1}(1) +2 \tilde{\delta} x^{-2} t_{n}(1) = 
a t_{n+1}(1) - a x^{-1}(\tilde{\delta} + 2)t_n(1) +2a \tilde{\delta} x^{-2} t_{n-1}(1)$
hence 
$$t_{n+2}(1)=   \left( a+\frac{\tilde{\delta} + 2}{x}\right)t_{n+1}(1) -\frac{1}{x} \left(2 \frac{\tilde{\delta}}{x}+a(\tilde{\delta} + 2) \right) t_{n}(1) 
 +2a \frac{\tilde{\delta}}{x^2} t_{n-1}(1)$$
which proves (iii).
\end{proof}

At this stage, $C$ could well be $0$. We now prove that this is not the case.

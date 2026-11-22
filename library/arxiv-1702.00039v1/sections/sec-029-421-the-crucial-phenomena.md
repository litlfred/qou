---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-029-421-the-crucial-phenomena
section_title: "The crucial phenomena"
section_number: 4.2.1
pages: 22-25
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.962
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
\begin{st}\label{st}
The category $\mathcal{B}(S_3)$ is stable under product. 
\end{st}

\begin{proof}
It is obvious that we just need to prove that we can write any product of two elements of $\II$ as a direct sum of shifts of elements in $\II.$


One important fact about $R$ is that if $p\in R$, then $p-s\cdot p \in (y-x)R^s.$  For example, if $p=3xy^2z^7+ yz$, 
 \begin{align*}
p-s\cdot p &=3xy^2z^7+ yz -3yx^2z^7- xz \\
&= (y-x)(3xyz^7+z).
\end{align*}
 
 It is an easy exercise to convince oneself of this fact (hint: start with monomials). One can also see this fact more conceptually by noticing that the polynomial $p-s\cdot p$ vanishes in the hyperplane defined by the equation $y=x$. 
The same result stands for $r$. The element $p-r\cdot p$ is  $(z-y)$ multiplied by some element of $R^r.$ We define $\alpha_s:=y-x$ and $\alpha_r:=z-y$. If we define $$P_s(p)=\frac{p+s\cdot p}{2} \in R^s \  \ \mathrm{ and  } \ \  \del_s(p)=\frac{p-s\cdot p}{2\alpha_s} \in R^s$$
 then we have the decomposition \begin{equation}\label{p}p=P_s(p)+\alpha_s\del_s(p).\end{equation} This equality gives rise to an isomorphism of graded  $R^s$-bimodules
 \begin{equation}\label{Rgr}
 R\cong R^s\oplus R^s(-2).
 \end{equation}




As a direct consequence of this equation we obtain the isomorphism
\begin{eqnarray}\label{BsBs}
B_sB_s &\cong& R\otimes_{R^s}R\otimes_{R^s}R(2) \nonumber\\
&\cong&  R\otimes_{R^s}R(2)\,  \oplus \,  R\otimes_{R^s}R \nonumber\\
&=& B_s(1)\oplus B_s(-1)
\end{eqnarray}
Compare this isomorphism with the equality $b_sb_s=vb_s+v^{-1}b_s$ in the Hecke algebra. 
We also obtain the following isomorphism
\begin{eqnarray}\label{BsBsrs}
B_sB_{srs} &\cong& R\otimes_{R^s}R\otimes_{R^{s,r}}R(4) \nonumber\\
&\cong&  B_{srs}(1) \oplus  B_{srs}(-1).
\end{eqnarray}
Compare this isomorphism with the equality $b_sb_{srs}=vb_{srs}+v^{-1}b_{srs}$ in the Hecke algebra. 

Let us recall a classic result of invariant theory. There is an isomorphism of $R^{s,r}$-bimodules (see, for example  \cite[ch. IV, cor. 1.11 a.]{Hi})
\begin{equation}\label{sr} R\cong \bigoplus_{w\in S_3}R^{s,r}(-2l(w))\end{equation}

This isomorphism implies  that 
\begin{equation}\label{w0}
B_{srs}B_{srs}\cong B_{srs}(-3)\oplus B_{srs}(-1)^{\oplus 2}\oplus B_{srs}(1)^{\oplus 2}\oplus B_{srs}(3)
\end{equation}
Compare this isomorphism with the equality $$b_{srs}b_{srs}=(v^{-3}+2v^{-1}+2v^{1}+v^3)b_{srs}$$ in the Hecke algebra.


To finish the proof of the Baby Stability Theorem \ref{st} we just need to prove the following isomorphism (that one should compare with the formula  in the Hecke algebra $b_sb_rb_s=b_{srs}+b_s).$

\subsection{$B_sB_rB_s\cong B_{srs}\oplus B_s$}\label{dec}
 

 For this we need first to define four morphisms of $R$-bimodules. The first one is the multiplication morphism $m_s\in \mathrm{Hom}(B_s, R)$
\begin{align*}
m_s: R\otimes_{R^s}R(1)&\rightarrow R\\
p\otimes q &\mapsto pq
\end{align*}
that is obviously a (degree $1$) morphism. The second morphism  $m_s^a\in \mathrm{Hom}(R, B_s)$ is its adjoint, in a sense that will become clear in Section \ref{adjunction} (thus explaining the notation  used for this morphism).
\begin{align*}
m_s^a: R &\rightarrow R\otimes_{R^s}R(1)\\
1 &\mapsto \alpha_s\otimes 1+ 1\otimes \alpha_s
\end{align*}

To check that this is  a (degree $1$) morphism of $R$-bimodules we need to check that for any $p\in R$ we have  $m_s^a(1)p=pm_s^a(1).$ This is
\begin{align*}
\alpha_s\otimes p+ 1\otimes \alpha_sp&=\alpha_sP_s(p)\otimes1+\alpha_s\del_s(p)\otimes\alpha_s+P_s(p)\otimes\alpha_s +\del_s(p)\alpha_s^2\otimes1\\
 &= p\alpha_s\otimes 1+p\otimes \alpha_s.
\end{align*}
For the first equality we used equation (\ref{p}) and the fact that $$\alpha_s^2=(x+y)^2-4xy\in R^s.$$
The following  morphism $j_s\in \mathrm{Hom}(B_sB_s, B_s)$ has  degree $-1$
\begin{align*}
j_s: R\otimes_{R^s}R\otimes_{R^s}R(2)&\rightarrow R\otimes_{R^s}R(1)\\
p\otimes q \otimes h&\mapsto p\del_s(q)\otimes h
\end{align*}
If it is a well defined map it is obvious that it is an $R$-bimodule morphism. So one just needs to check that $j_s(pr^s\otimes q \otimes h)=j_s(p\otimes r^s q \otimes h)$ and that $j_s(p\otimes q r^s\otimes h)=j_s(p\otimes  q \otimes r^sh)$, for any $r^s\in R^s.$ Both equations follow from the fact that $\del_s$ is a morphism of left (or right) $R^s$-modules (this is easy to check). 

And finally, the last morphism, the adjoint of $j_s$ (also of degree $-1$)
\begin{align*}
j_s^a: R\otimes_{R^s}R(1)  & \rightarrow   R\otimes_{R^s}R\otimes_{R^s}R(2)\\
p\otimes q & \mapsto p\otimes 1\otimes q
\end{align*}

\begin{nota}\label{cucu}
When it is clear from the context we will not write the identity morphisms. For example if we write $m_r$ for a morphism in $\mathrm{Hom}(B_sB_rB_s,B_sB_s)$ we mean $\mathrm{id}\otimes m_r\otimes \mathrm{id}.$ 
\end{nota}

\begin{ef}
The morphism $e:=   - m_r^a \circ j_s^a\circ j_s\circ m_r\in \mathrm{End}(B_sB_rB_s)$ is an idempotent (here we are using Notation \ref{cucu}).
\end{ef}
\begin{proof}
It is enough to check that $j_s\circ m_r\circ m_r^a \circ j_s^a=-\mathrm{id}\in \mathrm{End}(B_s),$ which is trivial. 
\end{proof}
From this fact we deduce that 
\begin{equation}\label{e}B_sB_rB_s=\mathrm{im}(1-e)\oplus \mathrm{im}(e),\end{equation} because if $e$ is an idempotent $1-e$ is easily checked to be an idempotent orthogonal to $e$. It is obvious that $m_r$ and $j_s$ are surjective and that $m_r^a$ and $j_s^a$ are injective morphisms. This implies that $$\mathrm{im}(e)\cong \mathrm{im}(m_r^a \circ j_s^a)\cong B_s.$$

To finish the proof we need to check the following isomorphism of graded $R$-bimodules

\subsection{$\mathrm{im}(1-e)\cong B_{srs}.$}\label{achi}
 
Let $1^{\otimes}:=1\otimes 1\otimes 1\otimes 1\in R\otimes_{R^s}R\otimes_{R^r}R\otimes_{R^s}R$
and let us denote  by $\langle 1^{\otimes} \rangle$   the $R$-bimodule generated by    $1^{\otimes}$.
We will prove the Lemma in two steps.

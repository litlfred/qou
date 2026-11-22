---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-012-necessity-of-legs-relations
section_title: "Necessity of Legs Relations"
section_number: null
pages: 60-70
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.994
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
\label{sec:legsnecessary}
This section exhibits all coherence data. See notation \ref{coherencenotations}. The reader is urged to reference the graphical summary of the proofs whenever possible.

\begin{mycom}
\textbf{(Important comment)} Before we prove that some of the prime relations of $P$ are redundant, we need to make an important observation.

There is an important geometric relation which shall play a role in the proofs. It is the relation we introduced earlier in comment \ref{criticalrelations}: \[
[p \setminus \operatorname{int}(D^3 \sqcup D^3)] = m \circ ([p \setminus \operatorname{int}(D^3)] \otimes id_{S^2}) \circ \lambda^{-1}_{S^2}= m \circ (id_{S^2} \otimes [p \setminus \operatorname{int}(D^3)] ) \circ \rho ^{-1}_{S^2}
.\]
where the second equality is the same as legs relations for $L$, and the morphism $[p\setminus \operatorname{int}(D^3)] : \emptyset \to S^2$ is interpreted as a prime unit. This equality, along with the simple $[p\setminus \operatorname{int}(D^3)] = [p\setminus \operatorname{int}(D^3 \sqcup D^3)] \circ 1$, showed that there is a bijection between the $G_1 $ generators and the $G_2 $ generators. 






It is necessary and important to stress that these two equalities do not constitute relations for either $G_1 $ or $G_2 $ presentations, as they are expressed in terms of a mix of $P$ generators (on the left hand sides) and $L$ generators (on the right hand sides). \footnote{These two equalities could be thought of as ``consistency conditions'' or ``compatibility conditions'' (across $P$ and $L$, along with the existing commutative Frobenius generators). Topology forces these conditions to be true in $\operatorname{Cob}(3)_{S^2} $.}

Note, however, if one chooses to express the right hand side $L$ generators in terms of the $P$ generators using $[p\setminus \operatorname{int}(D^3)] = [p\setminus \operatorname{int} (D^3 \sqcup D^3)] \circ 1$ 
then they do become genuine relations. The conditions read 
\begin{equation}\label{eqn:consistency}
p^{\times \times}  = m \circ \left( (p^{\times \times}  \circ 1) \otimes id_{S^2} \right) \circ \lambda^{-1}_{S^2} = m \circ \left( id_{S^2} \otimes \left( p^{\times \times}  \circ 1 \right)  \right)  \circ \rho ^{-1}_{S^2}
\end{equation}
which we will show is equivalent to legs relations for $P$.
\end{mycom}

\begin{lemma}\label{lem:consistencyislegs}
The following two terms are both equal to $p^{\times \times} $ if and only if the legs relations for $P$ holds:
\[
m \circ \left( (p^{\times \times}  \circ 1) \otimes id_{S^2} \right) \circ \lambda^{-1}_{S^2} ,\quad   m \circ \left( id_{S^2 } \otimes  (p^{\times \times}  \circ 1)  \right) \circ \rho ^{-1}_{S^2} \]
\end{lemma}

\begin{proof}

Given the legs relation $m\circ \left( p^{\times \times}  \otimes id_{S^2} \right) = m \circ \left( id_{S^2} \otimes p^{\times \times} \right) $, precompose both sides with $(1 \otimes id_{S^2}) \circ \lambda^{-1}_{S^2}$, to get \[
m\circ \left( \left( p^{\times \times}  \circ 1 \right)  \otimes id_{S^2} \right) \circ \lambda^{-1}_{S^2} = m \circ \left( 1 \otimes  p^{\times \times} \right) \circ \lambda ^{-1}_{S^2}
.\]
The left hand side is in the desired form. We just need the right to be $p^{\times \times} $. Rewrite the middle term on the right hand side as  $\left(1 \otimes id_{S^2}\right) \circ \left( id_\emptyset \otimes p^{\times \times}  \right) $, and use naturality of the unitor $ \lambda ^{-1}_{S^2} \circ p^{\times \times}  = (id_\emptyset \otimes p^{\times \times} ) \circ \lambda^{-1}_{S^2}$, the right hand side becomes \[
m\circ (1 \otimes id_{S^2}) \circ \lambda^{-1}_{S^2} \circ p^{\times \times}  = id_{S^2} \circ p^{\times \times}  =p^{\times \times}  
\]
where the first equality is due to $1$ being the multiplicative unit.

Note that similarly by precomposing both sides with $(id_{S^2} \otimes 1)\circ \rho ^{-1}_{S^2}$ one can show that legs relations give \[
	p^{\times \times}  = m\circ \left( id_{S^2} \otimes \left( p^{\times \times} \circ 1 \right)  \right) \circ \rho ^{-1}_{S^2}
.\]
which does not come as a surprise-- the right hand sides are related by braiding and commutativity, or can be thought of as a legs relations for $L$ in disguise.

Now for the only if direction, which is summarized in figure \ref{fig:plegsfromconsistency}, given that 
\[
p^{\times \times}  = m\circ \left(\left( p^{\times \times}  \circ 1 \right)  \otimes id_{S^2}\right) \circ \lambda_{S^2}^{-1} = m \circ \left(id_{S^2} \otimes \left( p^{\times \times}  \circ 1 \right)  \right) \circ \rho _{S^2}^{-1}
.\]
Substitute this into $m\circ (p^{\times \times}  \otimes id_{S^2})$to get \[
m \circ (p^{\times \times}  \otimes id_{S^2}) = m\circ \left( \left(  m \circ (id_{S^2} \otimes \left( p^{\times \times}  \circ 1 \right) ) \circ \rho _{S^2}^{-1}
\right) \otimes id_{S^2}  \right) 
.\]
By bifunctoriality of $\otimes $, this is \[
=m\circ (m \otimes id_{S^2}) \circ \left( (id_{S^2} \otimes \left( p^{\times \times}  \circ 1 \right) ) \otimes id_{S^2} \right)  \circ (\rho ^{-1}_{S^2} \otimes id_{S^2})
.\]

Use the precise form of associativity $m\circ (m \otimes id_{S^2})= m\circ (id_{S^2} \otimes m) \circ \alpha_{S^2, S^2, S^2}$ on the left most two terms giving \[
=m \circ (id_{S^2} \otimes m) \circ \alpha _{S^2,S^2,S^2} \circ \left(\left(id_{S^2}\otimes \left( p^{\times \times}  \circ 1 \right) \right)\otimes id_{S^2}\right) \circ (\rho ^{-1}_{S^2} \otimes id_{S^2})
.\]

by naturality of the associator, we may pass it through the right, giving \[
=m\circ (id_{S^2} \otimes m) \circ (id_{S^2} \otimes \left(\left( p^{\times \times}  \circ 1 \right)  \otimes id_{S^2}\right)) \circ \alpha_{S^2, \emptyset, S^2} \circ (\rho ^{-1}_{S^2} \otimes id_{S^2})
.\]
which we rewrite using bifunctoriality as \[
=m\circ \left(id_{S^2} \otimes \left(m \circ \left(\left( p^{\times \times}  \circ 1 \right)  \otimes id_{S^2}\right)\right)\right) \circ \left(\alpha_{S^2, \emptyset, S^2} \circ \left(\rho ^{-1}_{S^2} \otimes id_{S^2}\right)\right)
.\]
By coherence of the unitors and the associators, $\alpha_{S^2, \emptyset, S^2} \circ (\rho ^{-1}_{S^2} \otimes id_{S^2}) = id_{S^2} \otimes \lambda_{S^2}^{-1}$. We may use bifunctoriality again to get \[
=m\circ \left( id_{S^2} \otimes \left( m \circ \left( \left( p^{\times \times}  \circ 1 \right) \otimes id_{S^2}\right) \circ \lambda_{S^2}^{-1} \right)  \right) 
.\]
henceforth we reach the desired right hand side $m\circ (id_{S^2} \otimes p^{\times \times} )$.
\begin{figure}[ht]
    \centering
    \incfig{plegsfromcf}
\caption[$G_{1,2}$ bijection induces $G_2$ legs relations]{The only if direction of lemma \ref{lem:consistencyislegs}.}
    \label{fig:plegsfromconsistency}
\end{figure}



\end{proof}

\begin{rmk}
Notice that the two terms in the lemma above are equal due to braiding and commutativity, the proof of which is apparent once one interprets $[p\setminus \operatorname{int}(D^3 \sqcup D^3)]\circ 1 = [p\setminus \operatorname{int}(D^3)] : \emptyset \to S^2$ as a prime unit. The proof for legs relation for $L$ (which uses commutativity) applies directly. However, we do \textit{not} need this fact for the if and only if statement to be true, so commutativity is not involved in the proof of the lemma.
\end{rmk}

\begin{mycom}
\textbf{Important comment continued} The proofs of following propositions require that the legs relations hold, or equivalently that all three terms in lemma \ref{lem:consistencyislegs} are equal. 
This means that, with the exception of legs relations and commutative Frobenius relations, all other prime relations of $G_2 $ are redundant.
\end{mycom}

\begin{notations}
Due to the repeated occurrence of the term $p^{\times \times}  \circ 1$ in the following proofs, we will adopt the short hand $x=p^{\times \times}  \circ 1$. The reason not to use the equality of composition $[p\setminus \operatorname{int}(D^3)] = [p\setminus \operatorname{int}(D^3 \sqcup D^3)] \circ 1 = p^{\times \times} \circ 1$ is that the left hand side is naturally interpreted as a generator of $G_1 $. We write $x$ to remind ourselves that $x$ is generated by $G_2$.
\end{notations}







































\begin{prop} \label{waistfromCF}
Waist relations for $P$ are implied by legs relations and associativity of the commutative Frobenius relations.
\end{prop}

\begin{proof} 
We need to show that $p^{\times \times} \circ m = m\circ (p^{\times \times} \otimes id_{S^2})$ is induced by commutative Frobenius relations. This proof is graphically summarized by figure \ref{fig:waistfromcf}

First, by lemma \ref{lem:consistencyislegs}, the following relations hold  \[
p^{\times \times}  = m\circ (x \otimes id_{S^2}) \circ \lambda_{S^2}^{-1} = m \circ (id_{S^2} \otimes x) \circ \rho _{S^2}^{-1}
.\]
where $x = p^{\times \times}  \circ 1 : \emptyset \to S^2$. Substitute this for $p^{\times \times} $ on the left hand side to get \[
m\circ (x \otimes id_{S^2} ) \circ \left( \lambda_{S^2} ^{-1} \circ m \right) 
.\]

Unitors are natural isomorphisms. By the naturality of the left unitor $\lambda$, the following diagram commutes 

\[\begin{tikzcd}
A & {1_\otimes \otimes A} \\
B & {1_\otimes \otimes B}
\arrow["{\lambda_A^{-1}}", from=1-1, to=1-2]
\arrow["f", from=1-1, to=2-1]
\arrow["{id_{1_\otimes} \otimes f}", from=1-2, to=2-2]
\arrow["{\lambda_B^{-1}}", from=2-1, to=2-2]
\end{tikzcd}\]
for all $f:A\to B$ in the monoidal category. In particular when $f$ is $m: S^2 \sqcup S^2 \to S^2$, we learn that $\lambda_{S^2}^{-1} \circ m = \left( id_{\emptyset} \otimes m  \right) \circ \lambda^{-1}_{S^2 \sqcup S^2} $. Substituting this to the right most parentheses, we get \[
m \circ (x \otimes  id_{S^2}) \circ (id_{\emptyset }\otimes m) \circ \lambda^{-1}_{S^2 \sqcup S^2}
.\]

By a coherence\cite{kelly_maclanes_1964} of unitors and associators, the following diagram commutes 

\[\begin{tikzcd}
{A \otimes B} & {1_\otimes\otimes(A\otimes B)} \\
& {(1_\otimes\otimes A)\otimes B}
\arrow["{\lambda^{-1}_{A\otimes B}}", from=1-1, to=1-2]
\arrow["{\lambda^{-1}_A \otimes id_B}"', from=1-1, to=2-2]
\arrow["{\alpha_{1_\otimes, A, B}}"', from=2-2, to=1-2]
\end{tikzcd}\]
In particular for $A=B=S^2$, we learn that $\lambda^{-1}_{S^2\sqcup S^2} = \alpha_{\emptyset, S^2, S^2} \circ \lambda^{-1}_{S^2} \otimes id_{S^2}$. Substituting in to get \[
m\circ (x \otimes id_{S^2} ) \circ (id_{\emptyset } \otimes m) \circ \alpha _{\emptyset, S^2, S^2} \circ (\lambda^{-1}_{S^2} \otimes id_{S^2})
.\]
We will use bifunctoriality $(x \otimes id_{S^2}) \circ (id_{\emptyset } \otimes m) = x \otimes m = (id_{S^2} \otimes m) \circ (x \otimes (id_{S^2} \otimes  id_{S^2}))$, and pass the associator to the left using naturality to get \[
m \circ (id_{S^2} \otimes m) \circ \alpha _{S^2, S^2, S^2} \circ ((x \otimes id_{S^2}) \otimes id_{S^2}) \circ (\lambda^{-1}_{S^2} \otimes id_{S^2})
.\]
Now use associativity on the left most two terms, giving \[
m\circ (m \otimes id_{S^2}) \circ ((x \otimes id_{S^2}) \otimes id_{S^2}) \circ (\lambda^{-1}_{S^2} \otimes id_{S^2})
.\]
Combine the terms to get \[
m\circ \left( \left( m\circ \left( x \otimes id_{S^2} \right) \circ \lambda^{-1}_{S^2} \right) \otimes id_{S^2} \right) 
.\]
and henceforth we reach the desired right hand side $m\circ (p^{\times \times}  \otimes id_{S^2})$

\begin{figure}[ht]
    \centering
    \incfig{waistfromcf}
    \caption[Redundancy of $G_2$ waist relations]{Redundancy of $G_2$ waist relations.}
    \label{fig:waistfromcf}
\end{figure}




\end{proof}

\begin{prop} \label{primecommfromCF}
The prime commutativity relations are implied by legs relations and associativity and commutativity of the commutative Frobenius relations.
\end{prop}

\begin{proof}
We need to show that $p^{\times \times}  \circ p^{\times \times \prime}  = p^{\times \times \prime} \circ p^{\times \times} $ is a consequence of associativity and commutativity. The idea of the proof is summarized in figure \ref{fig:primecommfromcf}.

First, by lemma \ref{lem:consistencyislegs}, consider the relations  \[
p^{\times \times}  = m\circ (x \otimes id_{S^2}) \circ \lambda_{S^2}^{-1} = m \circ (id_{S^2} \otimes x) \circ \rho _{S^2}^{-1}
.\]
where $x = p^{\times \times}  \circ 1 : \emptyset \to S^2$. Similarly let $x' = p^{\times \times \prime}  \circ 1 : \emptyset \to S^2$ and write \[
p^{\times \times \prime}  = m\circ (x' \otimes id_{S^2}) \circ \lambda_{S^2}^{-1} = m \circ (id_{S^2} \otimes x') \circ \rho _{S^2}^{-1}
.\]

Substitute $m\circ (x \otimes id_{S^2}) \circ \lambda_A^{-1}$ for $p^{\times \times} $ and $m\circ (id_{S^2}^{-1} \otimes x') \circ \rho _{S^2}^{-1}$ for $p^{\times \times \prime}$ to get \[
p^{\times \times} \circ p^{\times \times \prime}  = m \circ (x \otimes id_{S^2}) \circ \lambda^{-1}_{S^2} \circ m \circ (id_{S^2} \otimes x') \circ \rho ^{-1}_{S^2}
.\]

By naturality of the left unitor explained in the proof of proposition \ref{waistfromCF}, we have $\lambda^{-1}_{S^2} \circ m = (id_{\emptyset} \otimes m) \circ \lambda^{-1}_{S^2 \sqcup S^2}$. So our expression is the same as \[
m\circ (x \otimes id_{S^2}) \circ (id_{\emptyset } \otimes m) \circ \lambda^{-1}_{S^2 \sqcup S^2} \circ (id_{S^2}\otimes  x') \circ \rho ^{-1}_{S^2}
.\]
We may use naturality of $\lambda$ again to obtain $\lambda^{-1}_{S^2 \sqcup S^2} \circ (id_{S^2} \otimes x') = (id_{\emptyset } \otimes (id_{S^2} \otimes x')) \circ \lambda^{-1}_{S^2 \sqcup \emptyset}$, and use bifunctoriality of $\otimes $ to turn the above expression to \[
m\circ  (id_{S^2 } \otimes m) \circ \left( x \otimes (id_{S^2} \otimes x') \right) \circ \lambda^{-1}_{S^2 \sqcup \emptyset} \circ \rho ^{-1}_{S^2}
.\]
By associativity $m\circ (m \otimes id_{S^2}) = m\circ (id_{S^2} \otimes m) \circ \alpha_{S^2, S^2, S^2}$, we may rewrite the left most two terms and get \[
m\circ  (m \otimes id_{S^2}) \circ \alpha^{-1}_{S^2, S^2, S^2} \circ \left( x \otimes (id_{S^2} \otimes x') \right) \circ \lambda^{-1}_{S^2 \sqcup \emptyset} \circ \rho ^{-1}_{S^2}
.\]
Passing the associator $\alpha ^{-1}_{S^2, S^2, S^2}$ to the right using naturality, we get  \[
m\circ  (m \otimes id_{S^2}) \circ  \left( \left( x \otimes id_{S^2} \right)  \otimes x' \right) \circ \alpha_{\emptyset, S^2, \emptyset} \circ \lambda^{-1}_{S^2 \sqcup \emptyset} \circ \rho ^{-1}_{S^2}
.\]

Noting that a coherence condition of \cite{kelly_maclanes_1964} introduced in the proof of proposition \ref{waistfromCF}, when $B = \emptyset$ and  $A = S^2$, gives  $\alpha ^{-1}_{\emptyset, S^2, \emptyset} \circ \lambda^{-1}_{S^2 \sqcup \emptyset }  =\lambda^{-1}_{S^2} \otimes id_{\emptyset}$, we can combine the resulting terms by bifunctoriality and arrive at the expression \[
m\circ \left( m \circ (x \otimes id_{S^2}) \circ \lambda^{-1}_{S^2}  \right) \otimes (id_{S^2} \circ x' \circ id_{\emptyset }) \circ \rho^{-1}_{S^2}
.\]
Apply the leg relation for $L$, we get \[
m \circ \left( m\circ (id_{S^2} \otimes x) \circ \rho_{S^2}^{-1} \right) \otimes \left( id_{S^2} \circ x' \circ id_{\emptyset } \right) \rho ^{-1}_{S^2}
.\]
Next, we reorganize the terms by bifunctoriality in preparation of a use of associativity: \[
m\circ (m \otimes id_{S^2}) \circ \left( (id_{S^2} \otimes x) \otimes x'  \right) \circ (\rho ^{-1}_{S^2} \otimes  id_{\emptyset}) \circ \rho ^{-1}_{S^2}
.\]
Use associativity, and pass the resulting associator to the right using naturality to get \[
m\circ (id_{S^2} \otimes m) \circ \left( id_{S^2} \otimes (x \otimes x') \right) \circ \alpha_{S^2, \emptyset, \emptyset} \circ (\rho ^{-1}_{S^2} \otimes id_{\emptyset}) \circ \rho ^{-1}_{S^2}
.\]
Combine the second and third terms, we reach the expression \[
[p] \circ [p'] = m\circ \left( id_{S^2} \otimes (m \circ (x \otimes x')) \right)  \circ \alpha_{S^2, \emptyset, \emptyset} \circ  \left( \rho ^{-1}_{S^2} \otimes id_{\emptyset} \right) \circ \rho ^{-1}_{S^2}
.\]
A critical observation is that, by braiding, commutativity, and  naturality of the unitors, $m\circ (x \otimes x') = m\circ (x' \otimes x)$. So we have in fact reached an expression which is invariant under the exchange $p^{\times \times}  \leftrightarrow p^{\times \times \prime} $ and $x \leftrightarrow x'$. Therefore we have the desired equality $p^{\times \times}  \circ p^{\times \times \prime} = p^{\times \times \prime}  \circ p^{\times \times} $. Note that we explicitly used associativity in one of our steps and commutativity is the symmetric exchange.
\begin{figure}[ht]
    \centering
    \incfig{primecommfromcf}
    \caption[Redundancy of prime commutativity]{Redundancy of prime commutativity. Note that the final figure is symmetric under the exchange of $p^{\times \times} _1 \circ 1 \leftrightarrow p^{\times \times} _2 \circ 1$.}
    \label{fig:primecommfromcf}
\end{figure}




\end{proof}


\begin{prop} \label{cowaistfromCF}
Cowaist relations are implied by legs relations and Frobenius.
\end{prop}

\begin{proof}
We want to show $(p^{\times \times}  \otimes id_{S^2}) \circ m^\vee = m^\vee \circ p^{\times \times}  $ is induced by the legs relations and the Frobenius relation. This proof is summarized graphically by figure \ref{fig:cowaistfromcf}

First, by lemma \ref{lem:consistencyislegs}, consider the relations  \[
p^{\times \times}  = m\circ (x \otimes id_{S^2}) \circ \lambda_{S^2}^{-1} = m \circ (id_{S^2} \otimes x) \circ \rho _{S^2}^{-1}
.\]
where $x = p^{\times \times}  \circ 1 : \emptyset \to S^2$. Substitute the first equality into the left hand side, we get \[
\left( \left( m\circ \left( x  \otimes id_{S^2} \right) \circ \lambda^{-1}_{S^2} \right) \otimes id_{S^2}  \right) \circ m^\vee
.\]

Rewrite this in a more convenient form \[
\left( m \otimes id_{S^2} \right) \circ \left( \left(x \otimes id_{S^2} \right) \otimes id_{S^2} \right) \circ \left( \lambda^{-1}_{S^2} \otimes id_{S^2} \right) \circ m^\vee
.\]
and recall the consistency condition of \cite{kelly_maclanes_1964} that $\lambda^{-1}_{S^2} \otimes id_{S^2} = \alpha^{-1}_{\emptyset, S^2, S^2} \circ \lambda^{-1}_{S^2 \sqcup S^2}$, we can substitute it into the expression above and use naturality of the associator to pass it to the left, giving \[
\left( m \otimes id_{S^2} \right) \circ \alpha^{-1}_{S^2, S^2, S^2} \circ \left( x  \otimes id_{S^2 \sqcup S^2} \right) \circ \lambda^{-1}_{S^2 \sqcup S^2} \circ m^\vee
.\]
By naturality of the left unitor, \[
\left( m \otimes id_{S^2} \right) \circ \alpha ^{-1}_{S^2, S^2, S^2} \circ \left( id_{S^2} \otimes id_{S^2 \sqcup S^2} \right) \circ \left( x \otimes m^\vee \right) \circ \lambda^{-1}_{S^2}
.\]
Rewrite this as \[
\left( m \otimes id_{S^2} \right) \circ \alpha ^{-1}_{S^2, S^2, S^2} \circ \left( id_{S^2} \otimes m^\vee \right) \circ \left( x  \otimes id_{S^2} \right) \circ \lambda^{-1}_{S^2}
.\]
and use the Frobenius relation on the first three terms, giving \[
m^\vee \circ m \circ \left( x \otimes id_{S^2} \right) \circ \lambda^{-1}_{S^2}
.\]
which gives the desired right hand side upon using lemma \ref{lem:consistencyislegs}.

\begin{figure}[ht]
    \centering
    \incfig{cowaistfromcf}
    \caption[Redundancy of $G_2$ cowaist relations]{Redundancy of cowaist relations.}
    \label{fig:cowaistfromcf}
\end{figure}
\end{proof}

\begin{rmk}
The other cowaist relation also holds by essentially the same proof \[
\left( id_{S^2} \otimes p^{\times \times}  \right) \circ m^\vee = m^\vee \circ p^{\times \times} 
.\]
therefore we have the following
\end{rmk}

\begin{prop} \label{colegsfromCF}
Colegs relations are implied by legs relations and the Frobenius relation.
\end{prop}

\begin{proof}
We want to show $\left( p^{\times \times}  \otimes id_{S^2} \right) \circ m^\vee = \left( id_{S^2} \otimes p^{\times \times}  \right) \circ m^\vee$. By legs relations and Frobenius, cowaist relations make both sides equal to $m^\vee \circ p^{\times \times} $.
\end{proof}

\begin{mycom}
The last remaining question is: are the legs relations redundant as well, despite the fact that they hold in $\operatorname{Cob}(3)_{S^2}$ due to topology? To phrase the question differently, are the legs relations implied by commutative Frobenius relations alone? Then answer is negative-- the legs relations for $P$ are not a consequence of just commutative Frobenius relations. 
\end{mycom}

\begin{prop} \label{Plegsnecessary}
Legs relations for $P$ are not induced by commutative Frobenius relations.
\end{prop}

\begin{proof}
Let $\mathbb{R}^2$ be the commutative Frobenius algebra with the Hadamard product. Namely, the multiplication map $m: \mathbb{R}^2 \otimes \mathbb{R}^2 \to \mathbb{R}^2$ is given by $(a,b) \cdot (c,d) = (ac,bd)$. The unit with respect to this multiplication is the element $(1,1)$. Let $e_1 = (1,0)$ and $e_2 = (0,1)$ be the standard basis. The comultiplication is defined by $m^\vee (e_1) = e_1 \otimes e_1 $ and $m^\vee (e_2 ) = e_2 \otimes e_2 $, then extended by linearity. Trace is given by $tr(a,b) = a+b$. One easily verifies that this is a commutative Frobenius algebra.

Let $Gra_2$ be the graph with $\left\{ \sqcup^{i\geq 0} S^2 \right\}\cong Z_{\geq 0}$ as the vertex set, and $G_2 $ and all its monoidal products as directed edges, and $F(Gra_2)$ the free symmetric monoidal category on the graph $Gra_2$. Let $F(Gra_2) /CF$ be the quotient category by the least congruence containing commutative Frobenius relations (see appendix \ref{defn:Free Category}, \ref{defn:Quotient Category} for the definitions used here).

Suppose that the commutative Frobenius algebra $(\mathbb{R}^2, \text{Hadamard})$ is $Z(S^2)$ for some symmetric monoidal functor $Z: F(Gra_2)/CF \to \text{Vect}$. Fix a connected closed irreducible 3-manifold $p$. Consider the assignment $Z(p^{\times \times} ) = $ rotation clockwise by $\pi/2$. Send the remaining prime endomorphisms to the identity. Then \[
Z(m) \circ \Big(Z(p^{\times \times} ) \otimes Z(id_{S^2})\Big) (e_1 \otimes  e_2 ) = -e_2 \cdot e_2 =-e_2 
\]
while \[
Z(m) \circ \Big(Z(id) \otimes Z(p^{\times \times} )\Big) (e_1 \otimes e_2 ) = e_1 \cdot e_1 =e_1 
\]

So it is not true that $m \circ (p^{\times \times} \otimes id_{S^2}) = m\circ (id_{S^2} \otimes p^{\times \times} )$.

Therefore the legs relations are not in the least congruence containing commutative Frobenius relations. 












\end{proof}






\begin{thm}\label{thm:trueG2thm}
$\operatorname{Cob}( 3)_{S^2} $ has a presentation with $G_2$ generators under commutative Frobenius relations and legs relations. These relations are necessary.
\end{thm}

\begin{proof}
By theorem \ref{mainthmG2}, $G_2 $ generates homs of $\operatorname{Cob}(3)_{S^2}$, and commutative Frobenius relations, co/legs and co/waist relations, and prime commutativity relations are sufficient. By propositions \ref{waistfromCF} - \ref{cowaistfromCF}, co/waist relations, prime commutativity, and colegs relations are induced by commutative Frobenius relations and legs relations, therefore they are not necessary. Theorem \ref{thm:Cob2Cob3CFIso} shows that commutative Frobenius relations are necessary, and proposition \ref{Plegsnecessary} shows that the legs relations are also necessary. Therefore the commutative Frobenius relations and legs relations are sufficient and necessary.
\end{proof}

\newpage
\textbf{Sumary Page}

Define the following morphisms of $\operatorname{Cob}( 3)_{S^2} $ :
\begin{align*}
id_{S^2} &= \left[ S^2 \times I \right]  \\
m &= \left[ S^3 \setminus \operatorname{int}(\sqcup_{}^3 D^3) \right]  : S^2 \sqcup S^2 \to S^2 \\
1 &= \left[ D^3  \right] : \emptyset \to S^2\\
m^\vee &= \left[ S^3 \setminus \operatorname{int}(\sqcup_{}^3 D^3)  \right] : S^2  \to S^2\sqcup S^2 \\
\tr &= \left[ D^3 \right]  :S^2 \to \emptyset
\end{align*}

$\operatorname{Cob}( 3)_{S^2}$ has two sets of generators:
\begin{align*}
G_1& = C \cup F \cup L \cup \text{orientation reversal}\\
G_2 &= C \cup F \cup P \cup \text{orientation reversal}
\end{align*}
where 
\begin{align*}
C &= \left\{ 1, m \right\} \\
F &= \left\{ tr, m^\vee \right\} \\
P &= \left\{ p^{\times \times} = \Big[ p\setminus \operatorname{int}(D^3 \sqcup D^3) \Big] :S^2 \to S^2 \mid p\text{ oriented irreducible} \right\} \\
L &= \left\{ p^\times = \Big[ p \setminus \operatorname{int}(D^3) \Big] : \emptyset \to S^2 \mid p \text{ oriented irreducible} \right\}  
\end{align*}

The $G_2 $ presentation of $\operatorname{Cob}( 3)_{S^2} $ satisfy the following complete list of relations: \[
\begin{cases}
\begin{aligned}
&m \circ (1 \otimes id_{S^2}) = id_{S^2}, &\text{unit}\\
&(tr \otimes id_{S^2}) \circ m^\vee = id_{S^2}, &\text{counit}\\
&m\circ (m \otimes id_{S^2}) = m\circ (id_{S^2} \otimes m), &\text{associativity}\\
&(m^\vee \otimes id_{S^2}) \circ m^\vee = (id_{S^2} \otimes m^\vee) \circ m^\vee, &\text{coassociativity} \\
&m^\vee \circ m = (m \otimes id_{S^2}) \circ \alpha^{-1}_{S^2, S^2, S^2} \circ (id_{S^2} \otimes m^\vee), &\text{Frobenius relation}\\
&[p] \circ [p'] = [p'] \circ [p], &\text{prime commutativity*}\\
&m\circ ([p]\otimes id_{S^2}) = m \circ (id_{S^2} \otimes [p]), &\text{legs relations}\\
&[p] \circ m = m \circ ([p] \otimes id_{S^2}), &\text{waist relations*}\\
&([p] \otimes id_{S^2}) \circ m^\vee = (id_S^2 \otimes [p])\circ m^\vee, &\text{colegs relations*}\\
&m^\vee \circ [p] = ([p] \otimes id_{S^2}) \circ m^\vee ,& \text{cowaist relations*}
\end{aligned}
\end{cases}
\]
The relations marked * are implied by the non-* relations.

The $G_1 $ presentation of $\operatorname{Cob}( 3)_{S^2} $ satisfy the following complete list of relations: \[
\begin{cases}
\begin{aligned}
&m \circ (1 \otimes id_{S^2}) = id_{S^2}, &\text{unit}\\
&(tr \otimes id_{S^2}) \circ m^\vee = id_{S^2}, &\text{counit}\\
&m\circ (m \otimes id_{S^2}) = m\circ (id_{S^2} \otimes m), &\text{associativity}\\
&(m^\vee \otimes id_{S^2}) \circ m^\vee = (id_{S^2} \otimes m^\vee) \circ m^\vee, &\text{coassociativity} \\
&m^\vee \circ m = (m \otimes id_{S^2}) \circ \alpha _{S^2, S^2, S^2} \circ (id_{S^2} \otimes m^\vee), &\text{Frobenius relation}\\

&m\circ ([p]\otimes id_{S^2}) = m \circ (id_{S^2} \otimes [p]), &\text{legs relations*}
\end{aligned}
\end{cases}
\]
The relation marked * is implied by the non-* relations.

\newpage
\chapter{Passing through TFTs} \label{ch:throughZ}

---
doc_id: arxiv-math-0305423v3
doc_title: "Stein's method and Plancherel measure of the symmetric group"
section_id: sec-003-4-steins-method-and-kerovs-central-limit-theorem
section_title: "Stein's method and Kerov's central limit theorem"
section_number: 4
pages: 10-14
source_pdf: 0305423v3.pdf
source_sha256: e4554f9084ba4935
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.988
doc_brief: "Stein's method and Plancherel measure of the symmetric group — We initiate a Stein’s method approach to the study of the Plancherel measure of the symmetric group."
---
\label{provebound}

	In this section we prove Theorem \ref{maintheorem}. Recall
	that $W(\lambda) = \frac{(n-1)}{\sqrt{2}}
	\frac{\chi^{\lambda}(12)}{dim(\lambda)}$ and that the
	Plancherel measure chooses a partition $\lambda$ with
	probability $\frac{dim(\lambda)^2}{n!}$. If $n=1$ we use the convention that $W=0$. Then Lemma
	\ref{countsol} implies the known fact that the mean and
	variance of $W$ are $0$ and $1-\frac{1}{n}$ respectively. This
	will also follow from Stein's method.

	In fact there is an explicit formula (due to Frobenius
\cite{Fr}) \[ \frac{\chi^{\lambda}(12)}{dim(\lambda)} = \frac{1}{{n
\choose 2}} \sum_i {\lambda_i \choose 2} - {\lambda_i' \choose 2} \]
where $\lambda_i$ is the length of row $i$ of $\lambda$ and
$\lambda_i'$ is the length of column $i$ of $\lambda$. We shall use
this formula only once.

	Throughout this section and the remainder of the paper, $W^*$ denotes $W(\lambda^*)$, where given $\lambda$, the partition $\lambda^*$ is $\mu$ with probability $J(\lambda,\mu)$ from Example 1 of Section \ref{harmonic}. Recall that $(W,W^*)$ is an exchangeable pair. We also use the notation that $\chi^{\lambda}$ denotes the character of the irreducible representation of the symmetric group parameterized by the partition $\lambda$. We let $|\lambda|$ denote the size of a partition.

	Proposition \ref{1strelate} shows that the hypothesis needed to apply the Stein method bound are satisfied. It also tells us that $W$ is an eigenvector for the Markov chain $J$, with eigenvalue $(1-\frac{2}{n+1})$. We shall generalize this observation in Section \ref{decompose}. 

\begin{prop} \label{1strelate} $E^W(W^*) = (1-\frac{2}{n+1}) W$. \end{prop}

\begin{proof} For $n=1$ we have that $W=0$ by convention. Otherwise, \begin{eqnarray*} E^{\lambda}(W^*) & = & \sum_{|\mu|= n} \frac{n-1}{\sqrt{2}} \frac{\chi^{\mu}(12)}{dim(\mu)} \frac{dim(\mu)}{(n+1) dim(\lambda)} |parents(\mu,\lambda)|\\
& = & \frac{n-1}{\sqrt{2}} \frac{1}{(n+1)dim(\lambda)} \sum_{|\mu| =n}
|parents(\mu,\lambda)| \chi^{\mu}(12). \end{eqnarray*} From the
representation theory of the symmetric group \cite{Sa},
$|parents(\mu,\lambda)|$ is equal to the multiplicity of $\chi^{\mu}$
in $Res^{S_{n+1}}_{S_n}(Ind_{S_n}^{S_{n+1}} (\chi^{\lambda}))$, since
inducing to $S_{n+1}$ corresponds to the possible ways of adding a box
to each corner of the partition $\lambda$, and restricting to $S_n$
corresponds to the possible ways of removing a corner box. Hence \[
E^{\lambda}(W^*) = \frac{n-1}{\sqrt{2}} \frac{1}{(n+1)dim(\lambda)}
Res^{S_{n+1}}_{S_n}(Ind_{S_n}^{S_{n+1}} (\lambda))[(12)] .\] Applying
Lemma \ref{induced}, this simplifies to \[ \frac{n-1}{\sqrt{2}}
\frac{\chi^{\lambda}(12)}{(n+1)dim(\lambda)} (n-1) =
(1-\frac{2}{n+1})W .\] Since $E^{\lambda}(W^*)$ depends on $\lambda$
only through $W$, it is equal to $E^W(W^*)$. \end{proof}

	As a consequence of Proposition \ref{1strelate}, we obtain a Stein's method proof that the mean $E(W)$ is equal to 0.

\begin{cor} $E(W)=0$. \end{cor} \begin{proof} Since the pair $(W,W^*)$ is exchangeable, $E(W^*-W)=0$. Using Proposition \ref{1strelate}, we see that \[ E(W^*-W)  =  E(E^W(W^*-W))
 = -\frac{2}{n+1} E(W) .\] Hence $E(W)=0$. \end{proof}

	Next we shall use Stein's method to compute $E^{\lambda}(W^*)^2$. Recall that this notation means the expected value of $(W^*)^2$ given $\lambda$. This will be useful for analyzing the error term in Theorem \ref{maintheorem}.  

\begin{prop} \label{forterm1} \begin{eqnarray*} E^{\lambda}((W^*)^2)
& = & (1-\frac{1}{n}) + \frac{2(n-1)(n-2)^2}{n(n+1)} \frac{\chi^{\lambda}((123))}{dim(\lambda)}\\
& &  +\frac{(n-1)(n-2)(n-3)^2}{2n(n+1)} \frac{\chi^{\lambda}((12)(34))}{dim(\lambda)}.\end{eqnarray*} Here we use the convention that if $n \leq 3$, $\chi^{\lambda}((12)(34))=0$, and if $n \leq 2$, $\chi^{\lambda}(123)=0.$ \end{prop} 

\begin{proof} If $n=1$ the result is clear. Otherwise, 
\begin{eqnarray*} E^{\lambda}(W^*)^2 & = & \frac{(n-1)^2}{2} \sum_{|\mu|=n} \frac{1}{n+1} |parents(\mu,\lambda)| \frac{dim(\mu)}{dim(\lambda)} \left(\frac{\chi^{\mu}(12)}{dim(\mu)} \right)^2\\
& = &  \frac{(n-1)^2}{2(n+1)} \frac{1}{dim(\lambda)} \sum_{|\mu|=n} |parents(\mu,\lambda)| \frac{\chi^{\mu}(12)^2}{dim(\mu)}. \end{eqnarray*} Applying Lemma \ref{parents}, this can be rewritten as \begin{eqnarray*}
& & \frac{(n-1)^2}{2(n+1)} \frac{1}{dim(\lambda)} \sum_{|\mu|=n} \frac{\chi^{\mu}(12)^2}{dim(\mu)} \frac{1}{n!} \sum_{g \in S_n} \chi^{\mu}(g) \chi^{\lambda}(g) (n_1(g)+1)\\
& = & \frac{(n-1)^2}{2(n+1)} \frac{1}{dim(\lambda)} \sum_{g \in S_n} \chi^{\lambda}(g) (n_1(g)+1) \frac{1}{n!} \sum_{|\mu|=n} \frac{\chi^{\mu}(12)^2 \chi^{\mu}(g)}{dim(\mu)}. \end{eqnarray*}

	The next step is to observe that using Lemmas \ref{real} and \ref{countsol}, one can compute the expression $\frac{1}{n!} \sum_{|\mu|=n} \frac{\chi^{\mu}(12)^2 \chi^{\mu}(g)}{dim(\mu)}$ for any permutation $g$. Indeed, it is simply $\frac{1}{{n \choose 2}^2}$ multiplied by the number of ordered pairs $(\tau_1,\tau_2)$ of transpositions whose product is $g$. Thus when this expression is non-zero, there are 3 possibilities for the cycle type of $g$: the identity, a 3-cycle, or a product of two 2-cycles on disjoint symbols. In all cases it is elementary to enumerate the number of pairs $(\tau_1,\tau_2)$, and these 3 possibilities yield the 3 terms in the statement of the proposition. 
\end{proof}

	As a consequence of Lemma \ref{forterm1}, we compute $Var(W)$. 

\begin{cor} $Var(W)=(1-\frac{1}{n})$. \end{cor}

\begin{proof} Since $W$ has mean $0$, $Var(W)=E(W^2)$. Since $W$ and $W^*$ have the same distribution, it follows that \[ E(W^2)=E(W^*)^2=E(E^{\lambda}(W^*)^2).\] The quantity $E^{\lambda}(W^*)^2$ was computed in Proposition \ref{forterm1} as a sum of three terms. The Plancherel measure average of the first term is $(1-\frac{1}{n})$. The Plancherel measure averages of the other terms both vanish. Indeed, if $g$ is any nonidentity element of the symmetric group, the Plancherel average of the function $\frac{\chi^{\lambda}(g)}{dim(\lambda)}$ is equal to \[ \frac{1}{n!} \sum_{\lambda} dim(\lambda) \chi^{\lambda}(g)
= \frac{1}{n!} \sum_{\lambda} \chi^{\lambda}(1) \chi^{\lambda}(g), \]
which vanishes by Lemma \ref{orth1}. \end{proof}

	In order to prove Theorem \ref{maintheorem}, we have to
	analyze the error terms in Theorem \ref{steinbound}. To begin
	we study \[ E\left(-1+\frac{n+1}{4} E^{\lambda}(W^*-W)^2
	\right)^2, \] obtaining an exact formula. From a well known
	general principle used in \cite{St1} (see Lemma 5 of
	\cite{Fu4} for a proof) the fact that $W$ is determined by
	$\lambda$ implies that \[ E[E^W(W^*-W)^2]^2 \leq
	E[E^{\lambda}(W^*-W)^2]^2 .\] Hence Proposition \ref{term1}
	gives an upper bound on \[ E\left(-1+\frac{n+1}{4}
	E^W(W^*-W)^2 \right)^2. \]

\begin{prop} \label{term1} \[ E \left(-1+\frac{n+1}{4} E^{\lambda}(W^*-W)^2 \right)^2 = \frac{3n^2-5n+6}{4n^3}.\] \end{prop}

\begin{proof} First observe (using Proposition \ref{1strelate} in the second equality)
 that \[ E^{\lambda}(W^*-W)^2 = W^2 - 2WE^{\lambda} W^* + E^{\lambda}(W^*)^2 =
 (\frac{4}{n+1}-1)W^2 + E^{\lambda}(W^*)^2.\] Combining this with Proposition
 \ref{forterm1}, it follows that $-1+\frac{n+1}{4} E^{\lambda}(W^*-W)^2$ is
 equal to $A+B+C+D$ where \begin{enumerate}
\item $A= \left( \frac{n+1}{4}(1-\frac{1}{n}) - 1 \right)$
\item $B= \frac{(n-1)(n-2)(n-3)^2}{8n} \frac{\chi^{\lambda}((12)(34))}{dim(\lambda)}$
\item $C= \frac{(n-1)(n-2)^2}{2n} \frac{\chi^{\lambda}(123)}{dim(\lambda)}$
\item $D= -\frac{n+1}{4}(1-\frac{4}{n+1}) \frac{(n-1)^2}{2} \left( \frac{\chi^{\lambda}(12)}{dim(\lambda)} \right)^2$
\end{enumerate} 

	We need to compute the Plancherel measure average of
$(A+B+C+D)^2$. Since $A^2$ is constant, the average of $A^2$ is
$\left( \frac{n+1}{4}(1-\frac{1}{n}) - 1 \right)^2$. The Plancherel
averages of $B^2$,$C^2$ can both be computed using Lemma
\ref{orth1}. One gets $\frac{(n-1)(n-2)(n-3)^3}{8n^3}$ and
$\frac{3(n-1)(n-2)^3}{4n^3}$ respectively. To compute the Plancherel
average of $D^2$ one uses Lemma \ref{countsol} to reduce the
computation to counting the number of ordered triples
$(\tau_1,\tau_2,\tau_3)$ of transpositions whose product is a
transposition, which is easy to do. The Plancherel averages of $2AB$,
$2AC$, $2BC$ are all 0 by Lemma \ref{orth1}. The Plancherel average of
$2AD$ is computed by Lemma \ref{orth1}. The Plancherel average of
$2BD$ is reduced to counting the number of ordered pairs of
transpositions whose product consists of two disjoint 2 cycles by
Lemma \ref{countsol}, and similarly the average of $2CD$ is reduced to
counting the number of ordered pairs of transpositions whose product
is a 3 cycle. Thus all of the enumerations are elementary and adding
up the terms yields the proposition. \end{proof}

	The final ingredient needed to prove Theorem \ref{maintheorem}
	is an upper bound on $E|W^*-W|^3$. Typically this is the
	crudest term in applications of Stein's method. It is the only
	point in the argument where we use Frobenius' explicit formula
	for $W$ (and as noted in the introduction even this could be
	avoided).

\begin{prop} \label{term2} \[ E|W^*-W|^3 \leq \left(\frac{4e \sqrt{2}}{\sqrt{n}} \right)^3 + 2e^{-2e \sqrt{n}} (2 \sqrt{2})^3 \]
\end{prop} 

\begin{proof} From Frobenius' formula, \[ W= \frac{\sqrt{2}}{n} \sum_i {\lambda_i \choose 2} - {\lambda_i' \choose 2} .\] Given this and the way that $\lambda^*$ is constructed from $\lambda$, it follows that \[|W^*-W| \leq \frac{\sqrt{2}}{n} 2 max(\lambda_1,\lambda_1').\] Indeed, suppose that $\lambda^*$ is obtained from $\lambda$ by moving a box from row $a$ and column $b$ to row $c$ and column $d$. Then \[ W^*-W = \frac{\sqrt{2}}{n} \left( \lambda_c + \lambda_b' - \lambda_a - \lambda_d' \right).\] 

	Suppose that $\lambda_1$ (the size of the first row of $\lambda$) and $\lambda_1'$ (the size of the first column of $\lambda$) are both at most $2e \sqrt{n}$. Then by the previous paragraph \[ |W^*-W| \leq \frac{4e \sqrt{2}}{\sqrt{n}}.\] 

	Next note by the first paragraph, even if $\lambda_1>2e \sqrt{n}$ or $\lambda_1'>2e \sqrt{n}$ occurs, $|W^*-W| \leq 2 \sqrt{2}$. We claim that the chance that at least one of the events $\lambda_1>2e \sqrt{n}$ or $\lambda_1'>2e \sqrt{n}$ occurs is at most $2e^{-2e \sqrt{n}}$. Indeed, it is a simple lemma proved on page 7 of \cite{Ste} that the chance that the longest increasing subsequence of a random permutation is at least $2e \sqrt{n}$ is at most $e^{-2e \sqrt{n}}$. But it follows from the Robinson-Schensted-Knuth correspondence (see for instance \cite{Sa}) that when $\lambda$ is chosen from the Plancherel measure of the symmetric group on $n$ symbols, both $\lambda_1$ and $\lambda_1'$ have the same distribution as the longest increasing subsequence of a random permutation on $n$ symbols. So as claimed, the chance that at least one of the events $\lambda_1>2e \sqrt{n}$ or $\lambda_1'>2e \sqrt{n}$ occurs is at most $2e^{-2e \sqrt{n}}$. 

	Combining these observations proves the proposition. \end{proof}

	To close this section, we prove Theorem \ref{maintheorem}.

\begin{proof} We use Theorem \ref{steinbound}, which is applicable with $\tau=\frac{2}{n+1}$ by Propositions \ref{constructchain} and \ref{1strelate}. Since $n \geq 2$, Proposition \ref{term1} implies that the term \[ 2 \sqrt{E[1-\frac{1}{2 \tau}E^W
(W^*-W)^2]^2} \] in Stein's bound is at most $\sqrt{3} n^{-1/2} \leq \sqrt{3} n^{-1/4}$. So using Proposition \ref{term2} and the fact that $e^{-2e \sqrt{n}} \leq n^{-3/2}$, the bound of Theorem \ref{steinbound} becomes \[ \sqrt{3} n^{-1/4} + (2 \pi)^{-1/4} \sqrt{\frac{n+1}{2} \left( (\frac{4e\sqrt{2}}{\sqrt{n}})^3 + \frac{2 (2 \sqrt{2})^3}{n^{3/2}} \right)} \leq 40.1 n^{-1/4}.\] \end{proof}

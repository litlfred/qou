---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-008-33-crystals
section_title: "Crystals"
section_number: 3.3
pages: 7-7
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 1.0
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
We recall the definition of a crystal. 

\begin{Definition} [\cite{Kash90}] A \textbf{$\fg$-crystal} is a finite set $\bB$ together with maps:
	$$\tilde{e}_i,\tilde{f}_i:\bB \rightarrow \bB\sqcup \{0\}, \quad \eps_i,\phi_i : \bB\rightarrow \ZZ, \quad \wt: \bB \rightarrow X$$
	for all $i \in I$, such that:
	\begin{enumerate}
		\item for any $b,b' \in \bB$, $\tilde{e}_i(b)=b'$ if and only if $b=\tilde{f}_i(b')$ ,
		\item for all $b \in \bB$, if $\tilde{e}_i(b) \in \bB$ then $\wt(\tilde{e}_i(b))=\wt(b)+\alpha_i$, and if $\tilde{f}_i(b) \in \bB$ then $\wt(\tilde{f}_i(b))=\wt(b)-\alpha_i$,
		\item for all $b \in \bB$, $\eps_i(b)=\max\{n \in \ZZ~:~\tilde{e}^n_i(b) \neq 0\}$, $\phi_i(b)=\max\{n \in \ZZ~:~\tilde{f}^n_i(b)\neq 0\}$,
		\item for all $b \in \bB$, $\phi_i(b)-\eps_i(b)=\left\langle \wt(b),h_i\right\rangle$.
	\end{enumerate}
\end{Definition}

Any $U_q(\fg)$-representation $V$ has a corresponding $\fg$-crystal $\bB=\bB_V$.  The underlying set of $\bB$ is in natural bijection with a particular basis of $V$ (the ``global crystal basis'' or ``canonical basis'').  The maps $\tilde{e}_i,\tilde{f}_i$ are related to the raising and lowering Chevalley operators; vaguely speaking they encode information about the leading terms of the Chevalley operators acting on this basis. In particular, for an integral dominant weight $\la$, the canonical basis $\bB(\la)$ of $L(\la)$ carries a natural crystal structure \cite{GL92}.

The crystal  of $V$ naturally arises via categorical representation theory. Namely, as we describe in the next proposition, if $\cC$ is a categorification of $V$, then $\Irr(\cC)$ carries a crystal structure isomorphic to $\bB_V$. This follows  from \cite[Proposition 5.20]{CR} and \cite{LV}, and is explained in detail in \cite{BDcryst}.  

\begin{Proposition}(\cite[Theorem 4.31]{BDcryst})\label{prop:cryst}
	The set $\Irr(\cC)$ together with:
	\begin{itemize}
	 \item Kashiwara operators defined as $\widetilde{\sE}_i(X)=\operatorname{soc}{\sE_i(X)}$, $\widetilde{\sF}_i(X)=\operatorname{soc}{\sF_i(X)}$ for $X \in \Irr(\cC)$, 
	 \item $\wt(X) = \mu$ for $X \in \cC_\mu$, and
	 \item $\varepsilon(X)=max\{ n \;|\; \sE_i^n(X)\neq 0\}$, and $\varphi(X)=max\{ n \;|\; \sF_i^n(X)\neq 0\}$,
	 \end{itemize}
	  is a $\fg$-crystal isomorphic to the crystal $\bB=\bB_V$.
\end{Proposition}

---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-007-41-a-connection-between-young-lattice-and-gross
section_title: "A connection between Young lattice and Gross-Witten-Wadia model"
section_number: 4.1
pages: 13-15
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.947
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
The Gross-Witten-Wadia model is a well studied unitary matrix model in physics. The partition function for this model is defined over an ensemble of $N\times N$ unitary matrices with a real potential $\Tr U+\Tr U^{\dagger}$, where the $trace$ is taken over fundamental representations. The partition function of GWW model is given by

\be\label{eq:GWWPF}
\cZ_{GWW} = \int [dU] \ e^{ \frac N{\lambda} (\Tr U+\Tr U^{\dagger})}, \quad \lambda\geq 0 .
\ee

Gross and Witten \cite{gross-witten} (and independently, Wadia \cite{wadia}) studied this matrix model in the context of lattice QCD and observed that the system undergoes a third order phase transition at $\lambda=2$. Different phases of this model are characterised by the topology of distribution of eigenvalues of the unitary matrix $U$ on a unit circle. The strong coupling phase ($\lambda>2$) corresponds to a gap-less distribution of eigenvalues whereas weak coupling phase ($\lambda <2$) shows a finite gap in eigenvalue distribution. 

A close cousin of GWW model \cite{Aharony:2003sx,AlvarezGaume:2005fv} is given by

\be\label{eq:cZ}
\cZ_{c} = \int [dU] \ e^{a \Tr U\Tr U^{\dagger}}.
\ee

The phase structure and eigenvalue distributions of this model are similar to those of GWW up to a redefinition of parameters : $a \langle \Tr U\rangle = N/\lambda$ \cite{duttadutta}. Expanding the exponential in (\ref{eq:cZ}) we get

\be
\cZ_{c} = \int [dU] \ \sum_{k=0}^{\infty} \frac{a^k}{k!} (\Tr U)^k (\Tr U^{\dagger})^k.
\ee

Using Frobenius formula for the characters of symmetric group we can write

\be
(\Tr U)^k = \sum_R \chi_R(1^k) \Tr_RU, \quad\text{and} \quad (\Tr U^{\dagger})^k = \sum_R \chi_R(1^k) \Tr_RU^\dagger
\ee

where the sum is over representations of $U(N)$ (or $SU(N)$) and $\chi_R(1^k)$ is the character of conjugacy class $(1^k)$ of symmetric group $S_k$ in representation $R$. Finally using the normalization condition for the characters of unitary group

\be
\int [dU] \Tr_RU\Tr_{R'} U^{\dagger} = \delta_{RR'}
\ee

we arrive at the final expression for $\cZ_{c}$ written in terms of sum over representations of $U(N)$ \cite{duttagopakumar}

\ben\label{eq:cZ2}
\cZ_{c} = \sum_{k=0}^{\infty} a^k \sum_{R} \frac{(\chi_R(1^k))^2}{k!} .
\een

It is well known that the character of the conjugacy class $(1^k)$ of symmetric group $S_k$ in representation $R$ is equal to the dimension of the representation \cite{hamermesh}

\be
\chi_R(1^k) = \text{dim} R.
\ee

Representations of $U(N)$ can be expressed in terms of Young diagrams. Since $\chi_R(1^k)$ is non-zero only when total number of boxes in the Young diagram is $k$ we have

\be\label{eq:PFcGWR}
\cZ_{c} = \sum_{k=0}^{\infty} a^k \sum_{\lambda_k} \frac{(\text{dim} \lambda_k)^2}{k!} \delta(k-|\lambda_{k}|).
\ee


Thus we see that the partition function for (cousin of) GWW model is same as that of a Young lattice with the coupling constant $a$ playing the role of fugacity. The rank of the gauge group $SU(N)$ in GWW model plays the role of the cut-off $N$ in (\ref{eq:GCPF3}).

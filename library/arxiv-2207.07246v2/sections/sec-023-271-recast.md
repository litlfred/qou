---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-023-271-recast
section_title: "Recast"
section_number: 2.7.1
pages: 47-50
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.873
latex_coverage_ratio: 0.908
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#Recast label="Recast"}

We need to recast Eq.([\[PIMCopexpdetailshorttime\]](#PIMCopexpdetailshorttime){reference-type="ref" reference="PIMCopexpdetailshorttime"}) into a form that is suitable for PIMC calculations. We set the total time $\tau$ as $\tau=\tau_1+\tau_2=N \Delta \tau$, and we insert $N$ short-time propagators $U(\Delta \tau)$ in Eq.([\[PIMCopexpdetailshorttime\]](#PIMCopexpdetailshorttime){reference-type="ref" reference="PIMCopexpdetailshorttime"}) as well as inserting corresponding identity operators in Eqs.([\[identityRS\]](#identityRS){reference-type="ref" reference="identityRS"}) at each of them, then Eq.([\[PIMCopexpdetailshorttime\]](#PIMCopexpdetailshorttime){reference-type="ref" reference="PIMCopexpdetailshorttime"}) with short-time propagator becomes, $$\begin{aligned}
\resizebox{.95\hsize}{!}{
$
\!\! \langle  \hat{O} (\Delta \tau) \rangle  \!=\!
\frac{ Re \! \sum\limits_{\mathcal{S}'} \! \int \! \mathcal{D} \mathcal{R}'   \langle \Psi_T| R_0 S_0\rangle
\langle R_0 S_0 |U(\Delta \tau) | R_1 S_1 \rangle...\langle R_I S_I |\hat{O} | R_{I\!+\!1} S_{I\!+\!1} \rangle ...
\langle R_{N\!+\!1} S_{N\!+\!1}  | \Psi_T \rangle  }
{ Re \! \sum\limits_{\mathcal{S}} \! \int \! \mathcal{D} \mathcal{R}  \langle \Psi_T| R_0 S_0\rangle
\langle R_0 S_0 | U(\Delta \tau) | R_1 S_1 \rangle ... \langle R_{N\!-\!1} S_{N\!-\!1} | U(\Delta \tau) | R_N S_N \rangle
\langle R_{N} S_{N}  | \Psi_T \rangle }, ~~
$}
\label{Oraw}
\end{aligned}$$ where $\sum\limits_{\mathcal{S}'}$ and $\int \mathcal{D} \mathcal{R}'$ in the numerator means $\sum\limits_{S_0,...,S_{N+1}}$ and $\int d R_0 ... dR_{N+1}$, and $\sum\limits_{\mathcal{S}}$ and $\int \mathcal{D} \mathcal{R}$ in the denominator means $\sum\limits_{S_0,...,S_{N}}$ and $\int d R_0 ... dR_{N}$.

For any local operator $\hat{O}$ in Eq.([\[Oraw\]](#Oraw){reference-type="ref" reference="Oraw"}), we can write down, $$\begin{aligned}
\langle R_I S_I |\hat{O} | R_{I+1} S_{I+1} \rangle
= \langle S_I | O_I | S_{I+1} \rangle \langle R_I | R_{I+1} \rangle
= \langle S_I | O_I | S_{I+1} \rangle \delta (R_I-R_{I+1}) ,
\label{Orawreduce}
\end{aligned}$$ where $O_I$ means operator $\hat{O}$ with spatial configuration $R_I$. Note that Eq.([\[Orawreduce\]](#Orawreduce){reference-type="ref" reference="Orawreduce"}) allows us to remove $R_{I+1}$ from the integral in the numerator of Eq.([\[Oraw\]](#Oraw){reference-type="ref" reference="Oraw"}). So the $N+2$ configurations $R_0$ to $R_{N+1}$ in the numerator can finally be reduced to $N+1$ configurations from $R_0$ to $R_{N}$ after relabeling. So the actual number of beads in the numerator is the same as in the denominator.

For the propagator in Eq.([\[Oraw\]](#Oraw){reference-type="ref" reference="Oraw"}) we insert $\sum_{S_I}  |S_I \rangle \langle S_{I} | =1$ in Eq.([\[identityS\]](#identityS){reference-type="ref" reference="identityS"}) and we can write down,

::: flalign
& \_S_I R\_I-1 S\_I-1 \| U_S() \| R_I S_I R_I S_I \| U_S() \| R\_I+1 S\_I+1\
& = \_S_I { S\_I-1 \| R\_I-1 \| e\^- e\^-T e\^- \| R_I \| S_I\
&         S_I \| R_I \| e\^- e\^-T e\^- \| R\_I+1 \| S\_I+1 }\
&= S\_I-1 \| e\^- e\^- e\^- e\^- \| S\_I+1 G\^f\_R\_I-1 R_I G\^f\_R\_I R\_I+1 , []{#eHrawreduce label="eHrawreduce"}
:::

where $\mathcal{V}_I$ means the potential operator $\mathcal{V}$ with spatial configuration $R_I$, and $e^{- \frac{\mathcal{V}_{I} \Delta \tau }{2}}$ is calculated by Eq.([\[propagatorv6half\]](#propagatorv6half){reference-type="ref" reference="propagatorv6half"}). The free particle propagator $G^f_{R_I R_J}=\langle R_{I} | e^{-T \Delta \tau} | R_J \rangle$ can be calculated by Eq.([\[propagatorFree\]](#propagatorFree){reference-type="ref" reference="propagatorFree"}). By repeatedly using Eq.([\[eHrawreduce\]](#eHrawreduce){reference-type="ref" reference="eHrawreduce"}) in Eq.([\[Oraw\]](#Oraw){reference-type="ref" reference="Oraw"}) we can remove any $S_I$ sandwiched between two short-time propagators $U(\Delta \tau)$. Finally we are left with 2 spin-isospin symbols in the trial wave functions to be summed over, we label them $S_0$ and $S_N$, where $S_0$ is for the trial wave function on the left $\langle \Psi_T | R_0 S_0 \rangle$, and $S_N$ is for the trial wave function on the right $\langle R_N S_N   | \Psi_T \rangle$.

Furthermore, consider the $l$ and $r$ order picked from the trial wave function $\Psi_T$ as shown in Eqs.([\[lorderdef\]](#lorderdef){reference-type="ref" reference="lorderdef"},[\[rorderdef\]](#rorderdef){reference-type="ref" reference="rorderdef"}), the approximated expectation value $\langle \hat{O}(\Delta \tau) \rangle$ in Eq.([\[Oraw\]](#Oraw){reference-type="ref" reference="Oraw"}) for PIMC calculations can finally be written as a general form,

::: flalign
()&= \_=\_l_r Re\[f()\_lr\] \
&= \_l_r { } \|Re\[ f()\_lr\] \| \
&= \_l_r B\_lr () P\_lr () \
&= \|\_ {l,r,} P\_lr() , []{#OABP label="OABP"}
:::

where we use symbol $\mathcal{R}$ to denote all the spatial configurations $\{R_0,R_1,...R_N \}$, $$\mathcal{R} \equiv \{R_0,R_1,...R_N \} ,
\label{defmathcalR}$$ and its integral is the spatial integral over all the configurations $R_I$, $$\int \mathcal{D} \mathcal{R} \equiv  \prod_{I=0}^N \int d R_I . \label{defmathcalRint}$$

In Eq.([\[OABP\]](#OABP){reference-type="ref" reference="OABP"}), $A_{lr} (\mathcal{R})$ and $B_{lr} (\mathcal{R})$ are real functions, $$\begin{aligned}

A_{lr} (\mathcal{R}) &= \frac{Re[ g(\mathcal{R})_{lr}]}{|Re[ f(\mathcal{R})_{lr}]|  } ,
\label{Alrform}
\\
B_{lr} (\mathcal{R}) &= \frac{Re[ f(\mathcal{R})_{lr}]}{|Re[ f(\mathcal{R})_{lr}]|  } ,
\label{Blrform}
\end{aligned}$$ and we can see that $B_{lr} (\mathcal{R})$ is either 1 or -1.

In Eq.([\[OABP\]](#OABP){reference-type="ref" reference="OABP"}), $P_{lr} (\mathcal{R})$ is the probability distribution, $$P_{lr} (\mathcal{R}) = \frac{|Re[ f(\mathcal{R})_{lr}]|}{ \mathcal{N}  },  \label{PlrR}$$ which is normalized to one in the following way, $$\sum_{l}\sum_{r} \int \mathcal{D} \mathcal{R} P_{lr}(\mathcal{R}) =1,$$ and its normalization factor is $\mathcal{N}=\sum_l \sum_r \int \mathcal{D} \mathcal{R} |Re[ f(\mathcal{R})_{lr}]|$.

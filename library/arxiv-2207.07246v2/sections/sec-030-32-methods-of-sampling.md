---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-030-32-methods-of-sampling
section_title: "Methods of Sampling"
section_number: 3.2
pages: 64-66
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 0.99
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#secSamplingMethod label="secSamplingMethod"}

In this section, we apply the Monte Carlo method described in section [\[MarkovChian\]](#MarkovChian){reference-type="ref" reference="MarkovChian"} to our PIMC algorithm. The $P_{lr} (\mathcal{R})$ in Eq.([\[PlrR\]](#PlrR){reference-type="ref" reference="PlrR"}) is exactly the $\pi(s)$ in section [\[MarkovChian\]](#MarkovChian){reference-type="ref" reference="MarkovChian"}. State $s$ in $\pi(s)$ means a particular choice of {$l,r,\mathcal{R}$}, and $\sum_s$ in Eq.([\[Fave\]](#Fave){reference-type="ref" reference="Fave"}) is the same as $\sum_l \sum_r \int d \mathcal{R}$ in Eq.([\[OABP\]](#OABP){reference-type="ref" reference="OABP"}). We have $$\begin{aligned}
s &= \{ l,r,\mathcal{R} \},
\label{state_s}\\
\pi(s)  &= \mathcal{P}_{lr}(\mathcal{R}), \\
\sum_s \pi(s) &= \sum_l \sum_r \int \mathcal{DR} \mathcal{P}_{lr}(\mathcal{R}) =1 .
\end{aligned}$$

The proposed transition probability $T(s \rightarrow s')$ can be decomposed into two parts. First we propose a transition for the left and right order of the trial wave function $\{ l,r \}$ to transit to a new pair $\{ l',r' \}$, mark it $T_{lr \rightarrow l'r'}$. Then, based on the new $\{ l',r' \}$, we choose a new configuration $\mathcal{R}'$ based on the new proposed transition probability $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')$. In such a way we have $$T(s \rightarrow s') = T_{lr \rightarrow l'r'} T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}').$$ We can just randomly pick $\{l',r'\}$ so that $T_{lr \rightarrow l'r'}$ equal to its inverse transition probability $T_{l'r' \rightarrow lr}$, so they are canceled in Eq.([\[Accptequation\]](#Accptequation){reference-type="ref" reference="Accptequation"}). Considering Eqs.([\[PlrR\]](#PlrR){reference-type="ref" reference="PlrR"},[\[fRlr\]](#fRlr){reference-type="ref" reference="fRlr"},[\[gRlr\]](#gRlr){reference-type="ref" reference="gRlr"}), we can write down, $$\frac{\pi(s')T(s'\rightarrow s)}{\pi(s) T(s\rightarrow s')} = \frac{ f^V_{l'r'}(\mathcal{R}') g^F(\mathcal{R}')  T_{lr}(\mathcal{R}' \rightarrow \mathcal{R})  }
{ f^V_{lr}(\mathcal{R}) g^F(\mathcal{R}) T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}') }, \label{Acc2}$$ and we can judge if we accept the new state $s'$ by Eq.([\[Accptequation\]](#Accptequation){reference-type="ref" reference="Accptequation"}) which now becomes, $$A (s\rightarrow s') \! = \!
\min \! \left[  1,
\frac{ f^V_{l'r'}(\mathcal{R}') g^F(\mathcal{R}')  T_{lr}(\mathcal{R}' \! \rightarrow \! \mathcal{R})  }
{ f^V_{lr}(\mathcal{R}) g^F(\mathcal{R}) T_{l'r'}(\mathcal{R} \! \rightarrow \! \mathcal{R}') }
\right] .
\label{Accptequationdetail1}$$

In the program, we do an equivalent two-stage judgement. At stage one, we randomly pick $\{l',r'\}$, and judge if we accept the new order by $$A (s\rightarrow s') \! = \!
\min \! \left[  1,
\frac{ f^V_{l'r'}(\mathcal{R}) g^F(\mathcal{R})  }
{ f^V_{lr}(\mathcal{R}) g^F(\mathcal{R})  }
\right] .$$ No matter $\{l',r'\}$ is accepted or not (the acceptance rate for $\{l,r\} \rightarrow \{l',r'\} \approx 99\%$), we mark the left and right order after the judgement as $\{l,r\}$. At the stage two, we propose the new configuration $\mathcal{R}'$ and judge if it is accepted or not by $$A (s\rightarrow s') \! = \!
\min \! \left[  1,
\frac{ f^V_{lr}(\mathcal{R}') g^F(\mathcal{R}')  T_{lr}(\mathcal{R}' \! \rightarrow \! \mathcal{R})  }
{ f^V_{lr}(\mathcal{R}) g^F(\mathcal{R}) T_{lr}(\mathcal{R} \! \rightarrow \! \mathcal{R}') }
\right] .$$

Since $f^V_{l'r'}(\mathcal{R}')$ and $f^V_{lr}(\mathcal{R})$ are sandwiched between the trial wave functions, there is no obvious ways to cancel them out in the numerator and denominator, so we leave them alone. However, the proposed probability $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')$ is something we can deal with. There can usually be two choices.

Choice 1

:   Make the proposed probability as, $$T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}') = T_{lr}(\mathcal{R}' \rightarrow \mathcal{R})  ,
    \label{tlrnewtlrold}$$ and by doing this, Eq.([\[Acc2\]](#Acc2){reference-type="ref" reference="Acc2"}) can be simplified as, $$\frac{\pi(s')T(s'\rightarrow s)}{\pi(s) T(s\rightarrow s')} =
    \frac{ f^V_{l'r'}(\mathcal{R}') g^F(\mathcal{R}')  }{ f^V_{lr}(\mathcal{R}) g^F(\mathcal{R})  }, \label{acc2simp2}$$ and then we can judge if we accept the new state $s'$ by, $$A(s\rightarrow s')=
    \min \left[  1, \frac{ f^V_{l'r'}(\mathcal{R}') g^F(\mathcal{R}')  }{ f^V_{lr}(\mathcal{R}) g^F(\mathcal{R})  } \right] .
    \label{Accptequationsimp2}$$

Choice 2

:   Make the proposed transition probability $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')$ and $T_{lr}(\mathcal{R}' \rightarrow \mathcal{R})$ in a way such that $$g^F(\mathcal{R}') T_{lr}(\mathcal{R}' \rightarrow \mathcal{R}) = g^F(\mathcal{R}) T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')   ,
    \label{gtnewgtold}$$ and by doing this, Eq.([\[Acc2\]](#Acc2){reference-type="ref" reference="Acc2"}) can be simplified as, $$\frac{\pi(s')T(s'\rightarrow s)}{\pi(s) T(s\rightarrow s')} = \frac{ f^V_{l'r'}(\mathcal{R}') }{ f^V_{lr}(\mathcal{R})  }, \label{acc2simp}$$ and then judge if we accept the new state $s'$ by the simplified version of Eq.([\[Accptequation\]](#Accptequation){reference-type="ref" reference="Accptequation"}), $$A(s\rightarrow s')=
    \min \left[  1, \frac{ f^V_{l'r'}(\mathcal{R}') }{ f^V_{lr}(\mathcal{R})  }\right] .
    \label{Accptequationsimp}$$

In our work, different methods of sampling means different choices of proposed transition probability $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')$ and $T_{lr}(\mathcal{R}' \rightarrow \mathcal{R})$. No matter what the choice is, they all correspond to the same target distribution $\pi(s)$. However, different choices of proposed transition probability will lead to different convergence speed. So in order to achieve the target distribution $\pi(s)$ efficiently and quickly, we need to mainly use efficient proposed transition probabilities.

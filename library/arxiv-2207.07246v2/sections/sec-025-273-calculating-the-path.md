---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-025-273-calculating-the-path
section_title: "Calculating the Path"
section_number: 2.7.3
pages: 53-57
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.875
latex_coverage_ratio: 0.983
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#secCalcPath label="secCalcPath"}

In order to write down the expressions for $f^V_{lr}(\mathcal{R})$ and $g^V_{lr,M}(\mathcal{R})$, as illustrated in Fig. [\[PIMCbeads\]](#PIMCbeads){reference-type="ref" reference="PIMCbeads"}, we define states $| \psi^r_M (\mathcal{R}) \rangle$ and $| \psi^l_M (\mathcal{R})\rangle$ along the path for computational convenience. Following the computation rule described in chapter. [\[secPathDiagrams\]](#secPathDiagrams){reference-type="ref" reference="secPathDiagrams"}, the states $| \psi^r_M (\mathcal{R}) \rangle$ and $| \psi^l_M (\mathcal{R})\rangle$ are defined as $$\begin{aligned}

&& | \psi^r_M (\mathcal{R}) \rangle \nonumber \\
&  \!\!\!\! \! \equiv & \! \!\!
\begin{cases}
\underbrace{  \sum\limits_{S}
   e^{\frac{- \mathcal{V}_M  \Delta \tau }{2}}  e^{\frac{- \mathcal{V}^\dagger_M  \Delta \tau }{2}} \bm{\mathcal{G}}
e^{\frac{- \mathcal{V}_{M\!+\!1}  \Delta \tau }{2}}  e^{\frac{- \mathcal{V}^\dagger_{M\!+1\!}  \Delta \tau }{2}} \bm{\mathcal{G}}
...
e^{\frac{- \mathcal{V}^\dagger_{N\!-\!1}  \Delta \tau }{2}} \bm{\mathcal{G}}
e^{\frac{- \mathcal{V}_N  \Delta \tau }{2}}
| S \rangle \langle R_N  S | \psi^r_T \rangle,
}_{ M \neq  N,  0.} \\
\underbrace{ \sum\limits_{S}
e^{\frac{- \mathcal{V}_N  \Delta \tau }{2}}
| S \rangle \langle R_N  S | \psi^r_T \rangle,
}_{M = N.} \\
\underbrace{  \sum\limits_{S} \! e^{\frac{- \mathcal{V}^\dagger_0  \Delta \tau }{2}} \bm{\mathcal{G}}
   e^{\frac{- \mathcal{V}_1  \Delta \tau }{2}}  e^{\frac{- \mathcal{V}^\dagger_1  \Delta \tau }{2}} \bm{\mathcal{G}}
e^{\frac{- \mathcal{V}_{2}  \Delta \tau }{2}}  e^{\frac{- \mathcal{V}^\dagger_{2}  \Delta \tau }{2}} \bm{\mathcal{G}}
 ...
e^{\frac{- \mathcal{V}^\dagger_{N\!-\!1}  \Delta \tau }{2}} \bm{\mathcal{G}}
e^{\frac{- \mathcal{V}_N  \Delta \tau }{2}}
| S \rangle \langle R_N  S | \psi^r_T \rangle.
}_{M =0.}
\end{cases} \label{psirmRdef}
\end{aligned}$$ $$\begin{aligned}
&&| \psi^l_M (\mathcal{R}) \rangle \nonumber \\
&  \!\!\!\! \! \equiv & \! \!\!
\begin{cases}
\underbrace{ \sum\limits_{S}
\left( \bm{\mathcal{G}}  e^{\frac{- \mathcal{V}_1  \Delta \tau }{2}}  e^{\frac{- \mathcal{V}^\dagger_1  \Delta \tau }{2}}
\bm{\mathcal{G}}
...
\bm{\mathcal{G}}
 e^{\frac{- \mathcal{V}_{M}  \Delta \tau }{2}}  e^{\frac{- \mathcal{V}^\dagger_{M}  \Delta \tau }{2}}
 \right) ^\dagger
e^{\frac{- \mathcal{V}_{0}  \Delta \tau }{2}}
| S \rangle \langle R_0 S | \psi^l_T \rangle,
}_{M\neq 0,N.} \\
\underbrace{ \sum\limits_{S}
e^{\frac{- \mathcal{V}_{0}  \Delta \tau }{2}}   | S \rangle \langle R_0  S | \psi^l_T \rangle,
}_{M=0.} \\
\underbrace{ \sum\limits_{S}\!   e^{\frac{- \mathcal{V}^\dagger_{N}  \Delta \tau }{2}}
\left( \bm{\mathcal{G}}  e^{\frac{- \mathcal{V}_1  \Delta \tau }{2}}  e^{\frac{- \mathcal{V}^\dagger_1  \Delta \tau }{2}}
\bm{\mathcal{G}}
...
\bm{\mathcal{G}}
 e^{\frac{- \mathcal{V}_{N-1}  \Delta \tau }{2}}  e^{\frac{- \mathcal{V}^\dagger_{N-1}  \Delta \tau }{2}} \bm{\mathcal{G}}
 \right) ^\dagger
e^{\frac{- \mathcal{V}_{0}  \Delta \tau }{2}}
| S \rangle \langle R_0 S | \psi^l_T \rangle.
}_{M=N.}
\end{cases} \label{psilmRdef}
\end{aligned}$$

Both $| \psi^l_M (\!\mathcal{R}\!)\rangle$ and $| \psi^r_M (\!\mathcal{R}\!)\rangle$ can be expanded by the $N_{\rm{tot}}$ spin isospin basis states $| S \rangle$ with accordingly probability amplitude $\phi^r_{M}(\mathcal{R},S)$ and $\phi^l_{M}(\mathcal{R},S)$, $$\begin{aligned}
\phi^r_{M}(\mathcal{R},S) &= \langle S | \psi^r_M (\!\mathcal{R}\!) \rangle ,
\label{phirMR}\\
\phi^l_{M}(\mathcal{R},S)  &= \langle S | \psi^l_M (\!\mathcal{R}\!)\rangle .
\label{philMR}
\end{aligned}$$ So that,

::: flalign
\| \^r_M () &= \_S \| S S \| \^r_M () = \_S \^r\_M(,S) \| S , []{#phirMexpansion label="phirMexpansion"}\
\| \^l_M ()&= \_S \| S S \| \^l_M ()= \_S \^l\_M(,S) \| S . []{#philMexpansion label="philMexpansion"}
:::

Function $g^V_{lr,M}(\mathcal{R})$ depends on which bead $M$ the operator $\hat{O}$ is placed at. For a given $M$, it is calculated as $$g^V_{lr,M}(\mathcal{R}) =
\begin{cases}
\langle \psi^l_{M\!-\!1}  (\mathcal{R}) | \bm{\mathcal{G}}
   e^{\frac{- \mathcal{V}_M  \Delta \tau }{2}} \hat{O}_M   e^{\frac{- \mathcal{V}^\dagger_M  \Delta \tau }{2}} \bm{\mathcal{G}}
| \psi^r_{M\!+\!1} (\mathcal{R}) \rangle,
 &  M \neq 0, N . \\
\sum\limits_{S} \langle \psi^l_T| \hat{O} | R_0 S\rangle \langle S | \psi^r_0 (\mathcal{R}) \rangle,
 &  M=0. \\
\sum\limits_{S} \langle \psi^l_N (\mathcal{R}) | S \rangle \langle R_N S| \hat{O} | \psi^r_T \rangle,
 & M=N .
\end{cases}
\label{gVRlrdef2}$$ In particular, if the operator $\hat{O}$ commutes with Hamiltonian, then $\hat{O}$ can be moved to leftmost or the rightmost position, and the result Eq.([\[PIMCopexpdetail\]](#PIMCopexpdetail){reference-type="ref" reference="PIMCopexpdetail"}) can then be written as Eq.([\[PIMCopexpdetailOH\]](#PIMCopexpdetailOH){reference-type="ref" reference="PIMCopexpdetailOH"}), and the corresponding $g(\mathcal{R})_{lr}$ becomes, $$g(\mathcal{R})_{lr} =  \frac{1}{2}
\left[ g^V_{lr,M}(\mathcal{R}) |_{M=0} + g^V_{lr,M}(\mathcal{R}) |_{M=N}  \right]
g^F(\mathcal{R}) .
\label{gRlrOH}$$ This is for example how we calculate the ground state energy $\hat{O}=H$.

For the AV6' interaction which does not have a spin-orbit term, the $\bm{\mathcal{G}}$ in Eq.([\[gVRlrdef2\]](#gVRlrdef2){reference-type="ref" reference="gVRlrdef2"}) is just 1. Note that the integer $M$ in $g^V_{lr,M}(\mathcal{R})$ is usually set at the middle between 0 and N, such that $e^{\frac{- \mathcal{V}_M  \Delta \tau }{2}} \hat{O}  e^{\frac{- \mathcal{V}^\dagger_M  \Delta \tau }{2}}$ is exactly placed in the middle of all the beads, so we make sure operator $\hat{O}$ is truly sandwiched between the same state which is the ground state if total imaginary time $\tau$ is big enough.

The function $f^V_{lr}(\mathcal{R})$ does not depend on $M$. Its value is the same as long as the left and right order $l$, $r$, and $\mathcal{R}$ are the same. For any integer $M$ from 0 to $N-1$, it can be calculated as, $$\begin{aligned}

f^V_{lr}(\mathcal{R})
= \langle \psi^l_M (\mathcal{R}) |
\bm{\mathcal{G}}
| \psi^r_{M+1} (\mathcal{R}) \rangle
= \sum_S \langle \psi^l_M (\mathcal{R}) | S \rangle
\langle S| \bm{\mathcal{G}} | \psi^r_{M+1} (\mathcal{R}) \rangle,
\label{fVRlrN2LOdef2}
\end{aligned}$$ where

::: flalign
& S\| \| \^r\_M+1 ()\
&= S \| {1 + \_i\<j v_7(r\^M\_ij) } \|\^r\_M+1 () , []{#propagatorN2LORSf label="propagatorN2LORSf"}
:::

and the definitions of $r^M_{ij}$, $\bm{r}^M_{ij}$ and $\Delta \bm{r}^{M,M+1}_{ij}$ are the same form as for $r'_{ij}$, $\bm{r}'_{ij}$ and $\Delta \bm{r}^{R',R}_{ij}$ used in Eq.([\[propagatorN2LORS\]](#propagatorN2LORS){reference-type="ref" reference="propagatorN2LORS"}). The $M$ and $M+1$ simply mean the configurations $R_M$ and $R_{M+1}$. For the AV6' interaction we have $\mathcal{G}=1$ so $f^V_{lr}(\mathcal{R})$ is simplified to the following form, $$\begin{aligned}

f^V_{lr}(\mathcal{R})
&= \langle \psi^l_M (\mathcal{R}) | \psi^r_{M+1} (\mathcal{R}) \rangle \nonumber \\
&= \sum_S \langle \psi^l_M (\mathcal{R}) | S \rangle \langle S |\psi^r_{M+1} (\mathcal{R}) \rangle \nonumber \\
&= \sum_{S} {\phi^{l}_{M}}^*(\mathcal{R},S) \phi^r_{M+1}(\mathcal{R},S).
 \label{fVRlrdef2}
\end{aligned}$$

In our PIMC code, the spin, isospin states are written in binary representation ([@Koonin91]) and we label the $A$ particles from 0 to $A-1$. In the code, we use 0 for neutron and spin down, 1 for proton and spin up. We use a 2 dimensional complex array $a(l_i,l_s)$ to represent a state. For example, in Eq.([\[philMexpansion\]](#philMexpansion){reference-type="ref" reference="philMexpansion"}), a certain basis state is $\phi^r_{M}(\mathcal{R},S) | S \rangle$, if $|S\rangle=| n \uparrow n \downarrow p \uparrow p \uparrow  \rangle$, then this basis state can be stored as $a(3,11)=\phi^r_{M}(\mathcal{R},S)$. Integer $l_i=3$ for the isospin in binary is 0011 which, from right to left, means and particles are protons, and particles are neutrons, so it is $| nnpp \rangle$. Integer $l_s=11$ for the spin in binary is 1011, means that the and particles are spin up, particles is spin down, one is spin up, so it is $| \uparrow \downarrow \uparrow \uparrow \rangle$. All those $| \psi^l_M (\!\mathcal{R}) \rangle$ and $| \psi^r_M (\!\mathcal{R}) \rangle$ states defined in Eqs.([\[phirMexpansion\]](#phirMexpansion){reference-type="ref" reference="phirMexpansion"},[\[philMexpansion\]](#philMexpansion){reference-type="ref" reference="philMexpansion"}) for each bead, are represented by their coefficients $\phi^r_{M}(\mathcal{R},S)$ and $\phi^l_{M}(\mathcal{R},S)$ defined in Eqs.([\[phirMexpansion\]](#phirMexpansion){reference-type="ref" reference="phirMexpansion"},[\[philMexpansion\]](#philMexpansion){reference-type="ref" reference="philMexpansion"}), and therefore stored in those 2 dimensional complex arrays like $a(l_i,l_s)$. All the quantities can be calculated from $| \psi^r_M (\!\mathcal{R}) \rangle$ and $| \psi^l_M (\!\mathcal{R})\rangle$.

It will be slow if we calculate $f^V_{lr}(\mathcal{R})$ and $g^V_{lr,M}(\mathcal{R})$ by first calculating all the $N_{\rm{tot}}$ by $N_{\rm{tot}}$ matrices of $\langle S' |e^{\frac{- \mathcal{V}_I  \Delta \tau }{2}} | S \rangle$ and $\langle S' |\bm{\mathcal{G}} | S \rangle$ along all the beads in Fig. [\[PIMCbeads\]](#PIMCbeads){reference-type="ref" reference="PIMCbeads"}, then multiplying all of them. This is because these matrices are sparse. Any 2-body charge conserving operator will only have either 4 or 8 nonzero entries in a row or column.

We can instead from right to left directly calculate $| \psi^r_{N-1} (\mathcal{R}) \rangle$ from $| \psi^r_N (\mathcal{R}) \rangle$, then $| \psi^r_{N-2} (\mathcal{R}) \rangle$ from $| \psi^r_{N-1} (\mathcal{R}) \rangle$, \..., until $| \psi^r_{M+1} (\mathcal{R}) \rangle$ from $| \psi^r_{M+2} (\mathcal{R}) \rangle$. Also, from left to right, we can calculate $| \psi^l_{1} (\mathcal{R}) \rangle$ from $| \psi^l_0 (\mathcal{R}) \rangle$, then $| \psi^l_{2} (\mathcal{R}) \rangle$ from $| \psi^l_{1} (\mathcal{R}) \rangle$, \..., until $| \psi^l_{M} (\mathcal{R}) \rangle$ from $| \psi^l_{M-1} (\mathcal{R}) \rangle$. The recursion relations from Eqs.([\[psirmRdef\]](#psirmRdef){reference-type="ref" reference="psirmRdef"}) and ([\[psilmRdef\]](#psilmRdef){reference-type="ref" reference="psilmRdef"}), can be written as, $$\begin{aligned}

 | \psi^r_M (\mathcal{R}) \rangle  =
\begin{cases}
 \sum\limits_{S}
 \left(  e^{\frac{- \mathcal{V}_M  \Delta \tau }{2}}  e^{\frac{- \mathcal{V}^\dagger_M  \Delta \tau }{2}}
\bm{\mathcal{G}} \right) | S \rangle
\langle S| \psi^r_{M+1} (\mathcal{R}) \rangle,
 & M \neq  N,  0. \\
 \sum\limits_{S}
e^{\frac{- \mathcal{V}_N  \Delta \tau }{2}}
| S \rangle \langle R_N  S | \psi^r_T \rangle,
 &  M = N. \\
  \sum\limits_{S} \! e^{\frac{- \mathcal{V}^\dagger_0  \Delta \tau }{2}} \bm{\mathcal{G}}
  | S \rangle \langle S | \psi^r_1 (\mathcal{R}) \rangle,
 &  M =0.
\end{cases} \label{phirMRrecur}
\end{aligned}$$ $$\begin{aligned}
| \psi^l_M (\mathcal{R})\rangle  =
\begin{cases}
 \sum\limits_{S}
\left( \bm{\mathcal{G}}   e^{\frac{- \mathcal{V}_M  \Delta \tau }{2}}  e^{\frac{- \mathcal{V}^\dagger_M  \Delta \tau }{2}}
 \right)^\dagger | S \rangle
\langle S | \psi^l_{M-1} (\mathcal{R}) \rangle,
 & M\neq 0,N. \\
 \sum\limits_{S}
e^{\frac{- \mathcal{V}_{0}  \Delta \tau }{2}}   | S \rangle \langle R_0  S | \psi^l_T \rangle,
 &  M=0. \\
 \sum\limits_{S}\!   e^{\frac{- \mathcal{V}^\dagger_{N}  \Delta \tau }{2}} \bm{\mathcal{G}}^\dagger | S \rangle
\langle S | \psi^l_{N-1} (\mathcal{R}) \rangle,
 &  M=N.
\end{cases} \label{philMRrecur}
\end{aligned}$$

<figure id="FigdirectCalcStates2">
<embed src="Figures/directCalcStates2.eps" />
<figcaption>Illustration of calculating <span class="math inline">|<em>ψ</em><sub><em>K</em> − 1</sub><sup><em>r</em></sup>(ℛ)⟩</span> from <span class="math inline">|<em>ψ</em><sub><em>K</em></sub><sup><em>r</em></sup>(ℛ)⟩</span> from right to left directly.</figcaption>
</figure>

Once we have the corresponding $| \psi^r_{M} (\mathcal{R}) \rangle$ and $| \psi^l_{M} (\mathcal{R}) \rangle$ calculated, we can use Eqs.([\[fVRlrN2LOdef2\]](#fVRlrN2LOdef2){reference-type="ref" reference="fVRlrN2LOdef2"}) and ([\[gVRlrdef2\]](#gVRlrdef2){reference-type="ref" reference="gVRlrdef2"}) to calculate $f^V_{lr}(\mathcal{R})$ and $g^V_{lr,M}(\mathcal{R})$ and then $A_{lr}(\mathcal{R})$ and $B_{lr}(\mathcal{R})$ and thus $\langle \hat{O} (\Delta \tau)  \rangle$. This updating strategy for $| \psi^r_{M} (\mathcal{R}) \rangle$ and $| \psi^l_{M} (\mathcal{R}) \rangle$ is much faster than direct $N_{\rm{tot}}$ by $N_{\rm{tot}}$ sparse matrix multiplication method. This is why we define states $| \psi^r_M (\!\mathcal{R}\!) \rangle$ and $| \psi^l_M (\!\mathcal{R}\!)\rangle$ and use Eqs. ([\[phirMRrecur\]](#phirMRrecur){reference-type="ref" reference="phirMRrecur"}) and ([\[philMRrecur\]](#philMRrecur){reference-type="ref" reference="philMRrecur"}) to calculate them and then finally calculate $f^V_{lr}(\mathcal{R})$ and $g^V_{lr,M}(\mathcal{R})$ by using Eqs.([\[fVRlrN2LOdef2\]](#fVRlrN2LOdef2){reference-type="ref" reference="fVRlrN2LOdef2"}) and ([\[gVRlrdef2\]](#gVRlrdef2){reference-type="ref" reference="gVRlrdef2"}).

Fig. [1](#FigdirectCalcStates2){reference-type="ref" reference="FigdirectCalcStates2"} illustrates the right to left direct calculation of $| \psi^r_{K-1} (\mathcal{R}) \rangle$ from $| \psi^r_K (\mathcal{R}) \rangle$. In the direct calculation $| \psi^r_{K-1} (\mathcal{R}) \rangle$ and $| \psi^r_K (\mathcal{R}) \rangle$ are always treated as column vectors, we directly operate the $\bm{\mathcal{G}}$, $e^{\frac{-\mathcal{V}^\dagger \Delta t}{2}}$ and $e^{\frac{-\mathcal{V} \Delta t}{2}}$ on the column vector $| \psi^r_K (\mathcal{R}) \rangle$ and get new column vectors each time until we get the next column vector $| \psi^r_{K-1} (\mathcal{R}) \rangle$. By doing that we prevent writing each of the operators as $N_{\rm{tot}}$ by $N_{\rm{tot}}$ sparse matrix and doing the slow matrix multiplications.

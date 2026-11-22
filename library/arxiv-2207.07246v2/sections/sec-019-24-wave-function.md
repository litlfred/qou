---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-019-24-wave-function
section_title: "Wave Function"
section_number: 2.4
pages: 35-42
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.982
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
From Eq.([\[PIMCopexp\]](#PIMCopexp){reference-type="ref" reference="PIMCopexp"}) we know that an initial trial wave function $\Psi_T$ is needed. Like all QMC calculations, the closer the trial wave function $\Psi_T$ is to the ground state, the faster and the lower variance the calculation will become. In fact, obtaining a high quality trial wave function is always an important task for QMC.

The state of the trial wave function $| \Psi_T \rangle$ in this work takes the following form ([@CarlsonRMP15a]), $$|\Psi_T \rangle = \mathcal{F} |\Phi \rangle, \label{PsiTstateF}$$ where $| \Phi \rangle$ is the model state, and $\mathcal{F}$ is the correlation operator.

Since nucleons are fermions, the model state $|\Phi \rangle$ has to be antisymmetric under the exchange of the labels between any of the two particles. For $A\leq 4$ it can be decomposed as a spatial part and a spin isospin part, $$|\Phi \rangle =  |\Phi_\textrm{R} \rangle \otimes | \Phi_\textrm{S} \rangle.\label{Phi}$$ The spatial part $|\Phi_\textrm{R} \rangle$ is symmetrized which can be chosen as, $$|\Phi_\textrm{R} \rangle
= \int dR  | R \rangle, \label{PhiR}$$ such that $$\langle R'|\Phi_\textrm{R} \rangle=\int dR \langle R'  | R \rangle = \int dR \delta(R'-R)=1. \label{normPhiR}$$

Since the spatial part is symmetric, the spin-isospin part $|\Phi_\textrm{S} \rangle$ has to be antisymmetric under the exchanges of labels between any of the two particles. For light nuclei with $A\leqq 4$, we can pick a basis state $|S' \rangle \equiv  | {s'_1}^1\rangle \otimes | {s'_2}^2 \rangle \otimes .. \otimes | {s'_A}^A \rangle
\equiv | {s'_1}^1 {s'_2}^2 ...{s'_A}^A \rangle$ from any one of the $N_S=\binom {A}{Z}\times 2^A$ spin-isospin basis $| S \rangle$, then construct $|\Phi_\textrm{S} \rangle$ using $A$ by $A$ Slater determinant of single particle states in such a form, $$\begin{aligned}
|\Phi_\textrm{S} \rangle \!=\!
\mathcal{A}   | {s'_1}^1 {s'_2}^2 .. {s'_A}^A \rangle
= \sum_{N=1}^{N_S} \phi_{N} | N \rangle,
\label{PhiS}
\end{aligned}$$ where the number $\phi_{N}$ is either -1, 1 or 0 depends on whether a certain spin-isospin state $| N \rangle$ from the $N_S$ states $| S \rangle$ has odd permutation (exchanging the particle labels between two particles), even permutation or any overlap with the chosen $| S' \rangle$ under any permutation or not.

The projection of $|\Phi_\textrm{S} \rangle$ on state $| S \rangle \equiv | s^1_1 s^2_2 s^3_3 s^4_4 \rangle$ is the amplitude $\langle S | \Phi_\textrm{S} \rangle$ which is calculated by, $$\begin{aligned}
\langle S |\Phi_\textrm{S} \rangle =
\left |
\begin{array}{ccccc}
\langle s^1_1 | {s'}^1_1  \rangle & \langle s^2_2 | {s'}^2_1 \rangle & ... &  \langle s^{A-1}_{A-1} | {s'}^{A-1}_1 \rangle & \langle s^A_A| {s'}^A_1 \rangle  \\
\langle s^1_1 | {s'}_2^1  \rangle & \langle s^2_2 | {s'}^2_2 \rangle & ... & \langle s^{A-1}_{A-1} | s^{A-1}_2 \rangle & \langle s^A_A | s^A_2 \rangle  \\
\vdots & \vdots &  \ddots & \vdots & \vdots  \\
\langle s^1_1 | s^1_{A-1}  \rangle & \langle s^2_2 | {s'}^2_{A-1} \rangle & ... & \langle s^{A-1}_{A-1} | s^{A-1}_{A-1} \rangle & \langle s^A_A | s^A_{A-1} \rangle  \\
\langle s^1_1 | s^1_A  \rangle &\langle s^2_2 | {s'}^2_{A} \rangle & ... & \langle s^{A-1}_{A-1} | s^{A-1}_A \rangle & \langle s^A_A | s^A_A \rangle
\end{array}
\right |
= \phi_S,
\label{SPhiS}
\end{aligned}$$ where the overlap between the spin-isospin state $| {s'}^N_j  \rangle$ of particle $N$ and $| {s'}^M_j  \rangle$ of particle $M$ is, $$\langle s^M_i | {s'}^N_j  \rangle = \langle s_i | {s'}_j  \rangle \delta_{MN} = \delta_{s_i,{s'}_j} \delta_{MN} .$$

Note that $\langle S | \Phi_\textrm{S} \rangle$ is a fermion wave function and it is antisymmetric under the particle label exchange between two particles. If $| S''  \rangle$ is obtained from $| S \rangle$ by exchanging the $i$ and $j$ particle labels, then $\langle S'' | \Phi_\textrm{S} \rangle$ is the determinant in Eq.([\[SPhiS\]](#SPhiS){reference-type="ref" reference="SPhiS"}) with $i$ and $j$ columns exchanged, which obviously becomes $-\langle S | \Phi_\textrm{S} \rangle$.

By using Eqs.([\[normPhiR\]](#normPhiR){reference-type="ref" reference="normPhiR"}--[\[SPhiS\]](#SPhiS){reference-type="ref" reference="SPhiS"}), the wave function $\langle RS | \Phi\rangle$ is calculated as, $$\langle RS | \Phi\rangle
= \langle R | \Phi_\textrm{R} \rangle
\langle S | \Phi_\textrm{S} \rangle
=\sum_{N=1}^{N_S} \phi_N \langle S | N \rangle
=\phi_S. \label{RSPhi}$$

Again, take $^4$He as an example, we can pick any one of the states from the 96 basis, and then antisymmetrize it to form the spin isospin part $| \Phi_\textrm{S} \rangle$ which will then be a linear combination of $4!=24$ non-zero basis states. We can pick a basis state $|S' \rangle= | {n \uparrow}^1 {n \downarrow}^2 {p \uparrow}^3 {p \downarrow}^4  \rangle$ from the basis, then antisymmetrize it to form $| \Phi_\textrm{S} \rangle$ of $^4$He, $$|\Phi_\textrm{S} \rangle
= \sum_{N=1}^{96}  | N \rangle \langle N | \Phi_\textrm{S} \rangle
= \sum_{N=1}^{96} \phi_N | N \rangle  , \label{PhiSHe4}$$

where $\phi_N=\langle N | \Phi_N\rangle$ is either $-1$ or $1$ depending on the antisymmetrization for each of the 24 basis states, and 0 for the rest 72 basis states. For example, using Eq.([\[SPhiS\]](#SPhiS){reference-type="ref" reference="SPhiS"}) one can find if $| N\rangle =| {n \uparrow}^1 {n \downarrow}^2 {p \uparrow}^3 {p \downarrow}^4  \rangle$ then $\phi_N$ is 1, if $| N \rangle =| {n \uparrow}^2 {n \downarrow}^1 {p \uparrow}^3 {p \downarrow}^4  \rangle$ then $\phi_N$ is -1, if $| N\rangle =| {n \uparrow}^2 {n \downarrow}^1 {p \uparrow}^3 {p \uparrow}^4  \rangle$ then $\phi_N$ is 0, etc.

The correlation operator $\mathcal{F}$ is represented by the products of two-body correlation operators $F_{ij}$, $${\mathcal F} =  {\mathcal S} \prod_{i<j} F_{ij} \, , \label{coropF}$$ where $\mathcal{S}$ is the symmetrization operator, and $F_{ij}$ is, $$F_{ij} =  \sum_{p=1}^6 f_{ij}^p O_{ij}^p \, , \label{coropFij}$$ where $O_{ij}^p$ are the same AV6' operators, and $f_{ij}^p$ is the corresponding correlation function operator ([@Lomnitz1981NPA]). After operating on $| R \rangle$, $f_{ij}^p$ will become a function $f_{ij}^p (r_{ij})$ which only depends on the distance $r_{ij}$ between particle $i$ and $j$.

By using Eqs.([\[basisRS\]](#basisRS){reference-type="ref" reference="basisRS"}--[\[coropFij\]](#coropFij){reference-type="ref" reference="coropFij"}), the trial wave function $\langle R S | \Psi_T  \rangle$ is calculated as, $$\langle R S | \Psi_T  \rangle \! = \!
\langle R  | \otimes  \langle S | \mathcal{F} |\Phi_{\textrm{R}} \rangle \otimes | \Phi_{\textrm{S}} \rangle
\!=\!
\left\langle S \left|
{\mathcal S}  \prod_{i<j}
\left[
\sum_{p=1}^6   f_{ij}^p (r_{ij})  O_{ij}^p
\right]
\sum_{N=1}^{N_S} \phi_N \right| N \right\rangle
 . \label{RSPsiT}$$

The trial wave function $\langle R S | \Psi_T  \rangle$ with correlation operators Eq.([\[coropFij\]](#coropFij){reference-type="ref" reference="coropFij"}) enriches the structure of the wave function, especially, it has the important tensor structure ([@CarlsonRMP15a]), and thus is an improvement over those without $O_{ij}^p$ operators.

However, such a trial wave function is usually expensive to calculate. Even if $O^p$ are just 1, it will take at least $96 \times 6= 576$ operations for a given pair. And we have 4 particles so 6 pairs, so $576\times 6=3456$ operations. Then there is a symmetrizer $\mathcal{S}$ which contribute another factor of $6!=720$. So totally at least $3456*720=2488320$ operations for computing just one $\langle R S | \Psi_T  \rangle$. In general, for a nuclei, without further simplifying $\langle R S | \Psi_T  \rangle$, brute force calculation for AV6' can take at least $\binom{A}{Z} \times 2^{A} \times 6 \times [A(A-1)/2] \times [A(A-1)/2]!$ operations. This is computationally too expensive. Because of that, in this work, as well as in most other QMC methods like AFDMC ([@Schmidt99a]), it is sampled instead of summing over all the $[A(A-1)/2]!$ symmetrized terms.

In our calculation, we use '$l$' to denote a sampled order $\langle \Psi^l_T |$ from $\langle \Psi_T |$, and use '$r$' to denote a sampled order $| \Psi^r_T \rangle$ from $| \Psi_T \rangle$. So, it is, $$\begin{aligned}
\langle \Psi_T | & = \sum  _l\langle \Psi^l_T |,  \\
| \Psi_T \rangle &= \sum_r | \Psi^r_T \rangle.
\end{aligned}$$ We can write $\langle \Psi_T | RS\rangle$ and $\langle RS | \Psi_T \rangle$ as, $$\begin{aligned}

\langle \Psi_T | RS \rangle &= \sum  _l\langle \Psi^l_T |  RS \rangle , \label{lorderdef}\\
\langle RS | \Psi_T \rangle &= \sum_r \langle RS | \Psi^r_T \rangle, \label{rorderdef}
\end{aligned}$$ and $\langle R S | \Psi_T^r  \rangle$ and $\langle \Psi_T^l | R S \rangle$ are, $$\begin{aligned}
\langle R S | \Psi_T^r  \rangle &= \!
\left\langle S \left|
\sideset{}{^r}
 \prod_{i<j}
\left[
\sum_{p=1}^6   f_{ij}^p (r_{ij})  O_{ij}^p
\right]
\sum_{N=1}^{96} \phi_N
\right| N \right\rangle
, \label{RSPsiTr} \\
\! \! \! \! \! \!  \langle \Psi_T^l | R S \rangle &= \!
 \sum_{N=1}^{96} \left\langle N \left|\phi^*_N
\sideset{}{^l} \prod_{i<j}
\left[
\sum_{p=1}^6  {f_{ij}^p}^* (r_{ij})   O_{ij}^p
\right]
\right| S \right\rangle ,\label{RSPsiTl}
\end{aligned}$$ where we use symbols $\sideset{}{^r} \prod_{i<j}$ and $\sideset{}{^l} \prod_{i<j}$ to denote a particular chosen '$r$' and '$l$' order from ${\mathcal S} \prod_{i<j}$. This $l$ and $r$ order sampling totally reduces the cost by the factor of $\left\{[A(A-1)/2]!\right\}^2$. For $^4$He that is $(6!)^2=518400$. Since the operator commutators are relatively small, so all the $[A(A-1)/2]!$ terms from either $\langle \Psi^l_T |$ or $| \Psi^r_T \rangle$ are almost the same, therefore the variance increase from sampling this operator order is also small.

It needs to be pointed that, $|\Phi_\textrm{S} \rangle$ (and therefore $|\Phi \rangle$) does not have to be just one Slater determinant, it can be (sometime it better be) a linear combination of several different Slater determinants formed from different antisymmetrized basis states. Overall, that is to say, using a linear combination of Slater determinant to form $| \Phi \rangle$ may be required to obtain the correct quantum numbers for a nucleus. To say the least, the deuteron ground state must have $J=S=1$ ([@SiemensJensenbook]).

For the $A> 4$ system, merely the four spin-isospin states $|n\uparrow \rangle$, $|n\downarrow \rangle$, $|p\uparrow \rangle$ and $|p\downarrow \rangle$ are not enough to form the antisymmetric state $| \Psi \rangle$ in Eq.([\[PsiTstateF\]](#PsiTstateF){reference-type="ref" reference="PsiTstateF"}). If we were to use single-particle states to form $| \Psi \rangle$ by Slater determinants, they have to contain some orbital quantum number information. For example we can use single particle orbital ([@zengjinyanQMbook; @Xuzizong2009book]) inspired from shell model ([@mayer1964shell]).

<figure id="singleobitalstates">
<embed src="Figures/singleobitalstates.eps" />
<figcaption>Single-particle orbital states <span class="math inline">|<em>s</em><sub><em>i</em></sub><sup><em>K</em></sup>⟩<sub><em>n</em><em>l</em><em>j</em><em>m</em><sub><em>j</em></sub></sub></span>. </figcaption>
</figure>

We can mark such a shell-model-like single-particle state as $| s^K_i \rangle_{nljm_j}$ as illustrated in Fig. [1](#singleobitalstates){reference-type="ref" reference="singleobitalstates"}. The symbol $K$ means it is the state of particle $K$. Letter $i$ can be from 0 to 4 and they denote spin-isospin state $n\uparrow$, $n\downarrow$, $p\uparrow$, $n\downarrow$ accordingly. Quantum number $n$ is the radial quantum number, $l$ is the orbit angular momentum quantum number, $j$ is the total angular momentum quantum number and $m_j$ is the $j$ projection quantum number. For simplicity, we can use $|\phi^K_\alpha\rangle$ to denote $| s^K_i \rangle_{nljm_j}$, $$|\phi^K_\alpha\rangle \equiv | s^K_i \rangle_{nljm_j} ,$$ where symbol $\alpha$ contains all the spin-isospin information $s_i$ and orbital information $nljm_j$, $$\alpha=\{s_i,nljm_j\}.$$ and the amplitude between $|\phi^K_\alpha\rangle$ and particle $M$'s basis $| \bm{r}^M_j s_j^M \rangle$ is $\langle \bm{r}^M_j s_j^M|\phi^K_\alpha\rangle$ which can be written as, $$\langle \bm{r}^M_j s_j^M|\phi^K_\alpha\rangle= \phi_\alpha(\bm{r}_j,s_j) \delta_{s_j,s_i} \delta_{MK}.
\label{rsphialpha}$$ The function $\phi_\alpha(\bm{r}_j,s_j)$ is usually called an orbital and it can be written as, $$\phi_\alpha(\bm{r}_j,s_j) = R_{nl}(r_j) \mathscr{Y} _l^{jm_j},$$ where $R_{nl}(r)$ is a radial function which can be found from the solution of some central potential such as Woods-Saxon potential ([@Lonardoni2018PRC]), and $\mathscr{Y} _l^{jm_j}$ is a simultaneous eigenfunction of $\bm{l}^2$, $\bm{s}^2$ and $\bm{j}^2$ called spin-angular function ([@sakurai1993]). $\mathscr{Y} _l^{jm}$ is a spin spherical harmonic $Y_l^m$ multiplied by some coefficients which are functions of $l$, $j$ and $m_j$. ,

Assuming there are $n_\phi$ ways to pick $A$ suitable single-particle states $|\phi^K_\alpha\rangle$ which can produce the correct total angular momentum $J$, parity $\pi$ and total isospin quantum number $T$ of a give A-nucleon nucleus, and the state $|\Phi\rangle$ can be written as a linear combination of $n_\phi$ Slater determinants $| \mathcal{D}_{\Phi}^q \rangle$, $$|\Phi\rangle = \sum_{q=1}^{n_\phi} c_q | \mathcal{D}_{\Phi}^q \rangle,
\label{PhiSlaterDsum}$$ where $c_q$ is some coefficient and the amplitude $\langle RS | \mathcal{D}_{\Phi}^q \rangle$ can be calculated by using Eq.([\[rsphialpha\]](#rsphialpha){reference-type="ref" reference="rsphialpha"}) as, $$\begin{aligned}
\langle RS | \mathcal{D}_{\Phi}^q \rangle
= \left |
\begin{array}{ccc}
\langle \bm{r}^1_1 s_1^1 | {\phi}^1_1  \rangle  & ...  & \langle \bm{r}^{A}_{A} s_{A}^{A} | {\phi}^A_1 \rangle  \\
\vdots  &  \ddots  & \vdots  \\
\langle \bm{r}^1_1 s_1^1 | {\phi}^1_A  \rangle &  ...  & \langle \bm{r}^{A}_{A} s_{A}^{A} | {\phi}^A_A \rangle
\end{array}
\right |
=
\left |
\begin{array}{ccc}
\phi_1(\bm{r}_1 s_1)  & ...  & \phi_1(\bm{r}_A s_A)   \\
\vdots  &  \ddots  & \vdots  \\
\phi_A(\bm{r}_1 s_1)   \rangle &  ...  & \phi_A(\bm{r}_A s_A)
\end{array}
\right |.
\end{aligned}$$

<figure id="O16shell">
<embed src="Figures/O16shell.eps" />
<figcaption>Single-particle orbital states of <span class="math inline"><sup>16</sup></span>O<span class="math inline">(0<sup>+</sup>,0)</span> </figcaption>
</figure>

For example, consider $^{16}$O$(0^+,0)$ whose total angular momentum quantum number and parity is $J^\pi=0^+$ and isospin quantum number is $T=0$. From the knowledge of shell model, as illustrated in Fig. [2](#O16shell){reference-type="ref" reference="O16shell"}, we know that $^{16}$O$(0^+,0)$ is a closed shell nucleus. All the 16 particles fully occupy the $N=1$ and $N=2$ shells. Among them, 4 occupy the $1S_{1/2}$ states, 4 occupy the $1P_{1/2}$ states and 8 occupy the $1P_{3/2}$ states. So totally 16 particles occupy 16 different orbital. So we can form one 16 by 16 Slater determinant to describe the wave function of $^{16}$O.

However, for open-shell nuclei, there are more single-particle orbital states than the number of nucleons $A$. Therefore in order to form the $|\Phi \rangle$ in Eq.([\[PhiSlaterDsum\]](#PhiSlaterDsum){reference-type="ref" reference="PhiSlaterDsum"}), all the possible orbital states may need to be picked to form the accordingly total number of $n_\phi$ Slater determinants. E.g., $^6$He$(0^+,1)$ needs 9 Slater determinants, $^6$Li$(1^+,0)$ needs 32 and $^12$C$(0^+,0)$ needs 119 ([@Lonardoni2018PRC]). Also, considering each Slater determinants needs to be operated by the correlation operator $\mathcal{F}$ in Eq.([\[coropF\]](#coropF){reference-type="ref" reference="coropF"}) in order to form $|\Psi_T \rangle$ in Eq.([\[PsiTstateF\]](#PsiTstateF){reference-type="ref" reference="PsiTstateF"}), the computational cost of calculating open-shell nuclei is much higher than closed-shell nuclei.

Last but not least, it needs to be pointed out that, the wave function does not have to be formed by the Slater determinants using single-particle orbital. We can also use paired states to form the antisymmetrized fermion wave functions in the Pfaffian form ([@Bouchaud1988a; @Bajdich2006PRL]). In fact, making the wave function relatively cheap to calculate while making it containing as much of ground state information as possible is one of the most important tasks in QMC calculations.

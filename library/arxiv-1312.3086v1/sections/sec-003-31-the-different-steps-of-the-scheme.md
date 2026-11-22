---
doc_id: arxiv-1312.3086v1
doc_title: "Quantum repeater with Rydberg blocked atomic ensembles in ﬁber-coupled cavities"
section_id: sec-003-31-the-different-steps-of-the-scheme
section_title: "The different steps of the scheme"
section_number: 3.1
pages: 3-5
source_pdf: 1312.3086v1.pdf
source_sha256: ff328e7c7cbdc70c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 1.0
doc_brief: "Quantum repeater with Rydberg blocked atomic ensembles in ﬁber-coupled cavities — 10 sections: Front matter; Introduction; The model"
---
Initially, all the cavities are empty and all ensemble atoms are in the reservoir state $\left|s\ldots s\right\rangle$. The first step consists in entangling pairs of neighboring subnodes $\left(R_{k},L_{k+1}\right)$ (see Fig. [\[Fig1\]](#Fig1){reference-type="ref" reference="Fig1"}c). To this end, one applies the sequence of operations given in Table [1](#EntanglementGeneration){reference-type="ref" reference="EntanglementGeneration"}. In this table, dashed-line arrows are used for non-resonant couplings to the intermediate states. Moreover, the "ensemble" nature of pulses is emphasized by a $\sqrt{N_{a}}$ factor above the concerned arrows. Finally, we indicate when a cavity mode is involved in a transition $\left|s\right\rangle \leftrightarrow\left|\varphi_{\pm}\right\rangle$ by writing "single photon $\pm$" above the corresponding arrow.

::: widetext
::: centering
::: {#EntanglementGeneration}
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *i*) simultaneous $\pi$ pulses (same Rabi frequency) on ensemble $\left(k\right)$
  $\left\{ \begin{array}{c}
  \left|s\right\rangle \overset{\sqrt{N_{a}}}{\dashrightarrow}\left|\varphi_{-}\right\rangle \dashrightarrow\left|r_{-}\right\rangle \\
  \left|s\right\rangle \overset{\sqrt{N_{a}}}{\dashrightarrow}\left|\varphi_{+}\right\rangle \dashrightarrow\left|r_{+}\right\rangle 
  \end{array}\right.$
  *ii*) $\pi$ pulse on ensemble $\left(k\right)$ $\left|r_{-}\right\rangle \dashrightarrow\left|\varphi_{-}\right\rangle \overset{\textrm{single photon -, }\sqrt{N_{a}}}{\dashrightarrow}\left|s\right\rangle$
  *iii*) $\pi$ pulse on ensemble $\left(k\right)$ $\left|s\right\rangle \overset{\sqrt{N_{a}}}{\dashrightarrow}\left|\varphi_{-}\right\rangle \dashrightarrow\left|r_{-}\right\rangle$
  *iv*) $\pi$ pulse on ensemble $\left(k\right)$ $\left|r_{+}\right\rangle \dashrightarrow\left|\varphi_{+}\right\rangle \overset{\textrm{single photon +, }\sqrt{N_{a}}}{\dashrightarrow}\left|s\right\rangle$
  *v*) $\pi$ pulse on ensemble $\left(k\right)$ $\left|s\right\rangle \overset{\sqrt{N_{a}}}{\dashrightarrow}\left|\varphi_{+}\right\rangle \dashrightarrow\left|r_{+}\right\rangle$
  *vi*) $\pi$ pulse on ensemble $\left(k\right)$ $\left|r_{-}\right\rangle \dashrightarrow\left|\varphi_{-}\right\rangle \dashrightarrow\left|0_{R}\right\rangle$
  *vii*) $\pi$ pulse on ensemble $\left(k\right)$ $\left|r_{+}\right\rangle \dashrightarrow\left|\varphi_{+}\right\rangle \dashrightarrow\left|1_{R}\right\rangle$
  *viii*) **Transfer** **of the photon** through the fiber
  from cavity $\left(k\right)$ to cavity $\left(k+1\right)$
  *ix*) $\pi$ pulse on ensemble $\left(k+1\right)$ $\left|s\right\rangle \overset{\textrm{single photon -, }\sqrt{N_{a}}}{\dashrightarrow}\left|\varphi_{-}\right\rangle \dashrightarrow\left|r_{-}\right\rangle$
  *x*) $\pi$ pulse on ensemble $\left(k+1\right)$ $\left|r_{-}\right\rangle \dashrightarrow\left|\varphi_{-}\right\rangle \dashrightarrow\left|0_{L}\right\rangle$
  *xi*) $\pi$ pulse on ensemble $\left(k+1\right)$ $\left|s\right\rangle \overset{\textrm{single photon +, }\sqrt{N_{a}}}{\dashrightarrow}\left|\varphi_{+}\right\rangle \dashrightarrow\left|r_{+}\right\rangle$
  *xii*) $\pi$ pulse on ensemble $\left(k+1\right)$ $\left|r_{+}\right\rangle \dashrightarrow\left|\varphi_{+}\right\rangle \dashrightarrow\left|1_{L}\right\rangle$
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : The different steps of the entanglement generation procedure.
:::
:::
:::

The first seven pulses $\left(i-vii\right)$ in Table [1](#EntanglementGeneration){reference-type="ref" reference="EntanglementGeneration"} prepare the subnode $\left(R_{k}\right)$ and the cavity $\left(k\right)$ in the entangled state $\left(\left|\bar{0}_{R}\right\rangle \otimes\left|-\right\rangle +\left|\bar{1}_{R}\right\rangle \otimes\left|+\right\rangle \right)/\sqrt{2}$ where $\left|\pm\right\rangle$ denotes the number state $\left|n_{\pm}=1\right\rangle$ of the cavity mode $\pm$. The photon thus released is then transferred to the cavity $\left(k+1\right)$ through the fiber (step $viii$). The last four pulses $\left(ix-xii\right)$ of the sequence translate the photonic excitation into an atomic excitation of the ensemble $\left(k+1\right)$ : a "$-$" photon is translated into a $\left|0_{L}\right\rangle$ excitation, a "$+$" photon into a $\left|1_{L}\right\rangle$ excitation. Finally, the two subnodes $\left(R_{k},L_{k+1}\right)$ are left in the state $\left(\left|\bar{0}_{R}\right\rangle _{k}\otimes\left|\bar{0}_{L}\right\rangle _{k+1}+\left|\bar{1}_{R}\right\rangle _{k}\otimes\left|\bar{1}_{L}\right\rangle _{k+1}\right)/\sqrt{2}$. The sequence of states along which the system evolves during the series of operations described in Table [1](#EntanglementGeneration){reference-type="ref" reference="EntanglementGeneration"} can be found in Table [2](#EntanglementGenerationStates){reference-type="ref" reference="EntanglementGenerationStates"}.

::: widetext
::: centering
::: {#EntanglementGenerationStates}
  $\left|s\ldots s\right\rangle _{k}\otimes\left|\textrm{vac}\right\rangle _{k}\otimes\left|s\ldots s\right\rangle _{k+1}\otimes\left|\textrm{vac}\right\rangle _{k+1}$
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $\quad\overset{i)}{\rightarrow}\left(\left|N_{r_{-}}=1\right\rangle _{k}+\left|N_{r_{+}}=1\right\rangle _{k}\right)/\sqrt{2}\otimes\left|\textrm{vac}\right\rangle _{k+1}\otimes\left|s\ldots s\right\rangle _{k+1}\otimes\left|\textrm{vac}\right\rangle _{k+1}$
  $\quad\overset{ii)}{\rightarrow}\left(\left|s\ldots s\right\rangle _{k}\otimes\left|-\right\rangle _{k}+\left|N_{r_{+}}=1\right\rangle _{k}\otimes\left|\textrm{vac}\right\rangle _{k}\right)/\sqrt{2}\otimes\left|s\ldots s\right\rangle _{k+1}\otimes\left|\textrm{vac}\right\rangle _{k+1}$
  $\quad\overset{iii)}{\rightarrow}\left(\left|N_{r_{-}}=1\right\rangle _{k}\otimes\left|-\right\rangle _{k}+\left|N_{r_{+}}=1\right\rangle _{k}\otimes\left|\textrm{vac}\right\rangle _{k}\right)/\sqrt{2}\otimes\left|s\ldots s\right\rangle _{k+1}\otimes\left|\textrm{vac}\right\rangle _{k+1}$
  $\quad\overset{iv)}{\rightarrow}\left(\left|N_{r_{-}}=1\right\rangle _{k}\otimes\left|-\right\rangle _{k}+\left|s\ldots s\right\rangle _{k}\otimes\left|+\right\rangle _{k}\right)/\sqrt{2}\otimes\left|s\ldots s\right\rangle _{k+1}\otimes\left|\textrm{vac}\right\rangle _{k+1}$
  $\quad\overset{v)}{\rightarrow}\left(\left|N_{r_{-}}=1\right\rangle _{k}\otimes\left|-\right\rangle _{k}+\left|N_{r_{+}}=1\right\rangle _{k}\otimes\left|+\right\rangle _{k}\right)/\sqrt{2}\otimes\left|s\ldots s\right\rangle _{k+1}\otimes\left|\textrm{vac}\right\rangle _{k+1}$
  $\quad\overset{vi)}{\rightarrow}\left(\left|\bar{0}_{R}\right\rangle _{k}\otimes\left|-\right\rangle _{k}+\left|N_{r_{+}}=1\right\rangle _{k}\otimes\left|+\right\rangle _{k}\right)/\sqrt{2}\otimes\left|s\ldots s\right\rangle _{k+1}\otimes\left|\textrm{vac}\right\rangle _{k+1}$
  $\quad\overset{vii)}{\rightarrow}\left(\left|\bar{0}_{R}\right\rangle _{k}\otimes\left|-\right\rangle _{k}+\left|\bar{1}_{R}\right\rangle _{k}\otimes\left|+\right\rangle _{k}\right)/\sqrt{2}\otimes\left|s\ldots s\right\rangle _{k+1}\otimes\left|\textrm{vac}\right\rangle _{k+1}$
  $\quad\overset{viii)}{\rightarrow}\left[\begin{array}{c}
  \left|\bar{0}_{R}\right\rangle _{k}\otimes\left|\textrm{vac}\right\rangle _{k}\otimes\left|s\ldots s\right\rangle _{k+1}\otimes\left|-\right\rangle _{k+1}\\
  +\left|\bar{1}_{R}\right\rangle _{k}\otimes\left|\textrm{vac}\right\rangle _{k}\otimes\left|s\ldots s\right\rangle _{k+1}\otimes\left|+\right\rangle _{k+1}
  \end{array}\right]/\sqrt{2}$
  $\quad\overset{ix)}{\rightarrow}\left[\begin{array}{c}
  \left|\bar{0}_{R}\right\rangle _{k}\otimes\left|\textrm{vac}\right\rangle _{k}\otimes\left|N_{r_{-}}=1\right\rangle _{k+1}\otimes\left|\textrm{vac}\right\rangle _{k+1}\\
  +\left|\bar{1}_{R}\right\rangle _{k}\otimes\left|\textrm{vac}\right\rangle _{k}\otimes\left|s\ldots s\right\rangle _{k+1}\otimes\left|+\right\rangle _{k+1}
  \end{array}\right]/\sqrt{2}$
  $\quad\overset{x)}{\rightarrow}\left[\begin{array}{c}
  \left|\bar{0}_{R}\right\rangle _{k}\otimes\left|\textrm{vac}\right\rangle _{k}\otimes\left|\bar{0}_{L}\right\rangle _{k+1}\otimes\left|\textrm{vac}\right\rangle _{k+1}\\
  +\left|\bar{1}_{R}\right\rangle _{k}\otimes\left|\textrm{vac}\right\rangle _{k}\otimes\left|s\ldots s\right\rangle _{k+1}\otimes\left|+\right\rangle _{k+1}
  \end{array}\right]/\sqrt{2}$
  $\quad\overset{xi)}{\rightarrow}\left[\begin{array}{c}
  \left|\bar{0}_{R}\right\rangle _{k}\otimes\left|\textrm{vac}\right\rangle _{k}\otimes\left|\bar{0}_{L}\right\rangle _{k+1}\otimes\left|\textrm{vac}\right\rangle _{k+1}\\
  +\left|\bar{1}_{R}\right\rangle _{k}\otimes\left|\textrm{vac}\right\rangle _{k}\otimes\left|N_{r_{+}}=1\right\rangle _{k+1}\otimes\left|\textrm{vac}\right\rangle _{k+1}
  \end{array}\right]/\sqrt{2}$
  $\quad\overset{xii)}{\rightarrow}\left[\begin{array}{c}
  \left|\bar{0}_{R}\right\rangle _{k}\otimes\left|\textrm{vac}\right\rangle _{k}\otimes\left|\bar{0}_{L}\right\rangle _{k+1}\otimes\left|\textrm{vac}\right\rangle _{k+1}\\
  +\left|\bar{1}_{R}\right\rangle _{k}\otimes\left|\textrm{vac}\right\rangle _{k}\otimes\left|\bar{1}_{L}\right\rangle _{k+1}\otimes\left|\textrm{vac}\right\rangle _{k+1}
  \end{array}\right]/\sqrt{2}$

  : Evolution of the state vector during the entanglement generation procedure.
:::
:::
:::

The entanglement generation procedure described above cannot be applied simultaneously on all pairs $\left(R_{k},L_{k+1}\right)$ : indeed, the pair of nodes to be entangled must be isolated from the others for the photon exchange. One can, however, deal with all the pairs $\left(R_{2k-1},L_{2k}\right)_{1\leq k\leq N/2}$ in parallel. Once entanglement has been successfully established among these pairs, one can then treat the remaining pairs $\left(R_{2k},L_{2k+1}\right)_{1\leq k\leq N/2-1}$. Omitting the auxiliary subnodes and the cavity modes which are all empty, one can write the final state of the system under the form $\prod_{k=1}^{N-1}\left(\left|\bar{0}_{R}\right\rangle _{k}\otimes\left|\bar{0}_{L}\right\rangle _{k+1}+\left|\bar{1}_{R}\right\rangle _{k}\otimes\left|\bar{1}_{L}\right\rangle _{k+1}\right)/\sqrt{2}$.

To complete the scheme, we now need to swap entanglement, *i.e.* to entangle the left and right subnodes $\left(R_{k}\right)$ and $\left(L_{k}\right)$ in every ensemble and decouple the first and last nodes from all the others. This constitutes the second step of the method (see Fig. [\[Fig1\]](#Fig1){reference-type="ref" reference="Fig1"} c). To this end, one first simultaneously applies to each pair of subnodes $\left(R_{k},L_{k}\right)_{k=2,\ldots,N-1}$ the unitary transformation $\left(U_{L}\otimes U_{R}\right)\times P_{LR}\times\left(\mathbb{I}_{L}\otimes V_{R}\right)$, where $U=\exp\left(-\mathrm{i}\frac{\pi}{2}\sigma_{z}\right)\times\exp\left(-\mathrm{i}\frac{\pi}{4}\sigma_{y}\right)$ and $V=\exp\left(-\mathrm{i}\frac{\pi}{2}\sigma_{x}\right)\times\exp\left(-\mathrm{i}\frac{\pi}{2}\sigma_{z}\right)\times\exp\left(-\mathrm{i}\frac{\pi}{4}\sigma_{y}\right)$ are simply achieved through applying the appropriate laser-induced pulses $\left|0_{L,R}\right\rangle \leftrightarrow\left|1_{L,R}\right\rangle$ and $P_{LR}=\left(\begin{array}{cccc}
-1 & 0 & 0 & 0\\
0 & -1 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & -1
\end{array}\right)$ is implemented through the following sequence of pulses : $$\begin{aligned}
\pi\textrm{ pulse :}\left|0_{L}\right\rangle  & \rightarrow & \left|r_{-}\right\rangle \\
2\pi\textrm{ pulse :}\left|1_{R}\right\rangle  & \longleftrightarrow & \left|r_{+}\right\rangle \\
\pi\textrm{ pulse :}\left|r_{-}\right\rangle  & \rightarrow & \left|0_{L}\right\rangle .
\end{aligned}$$ (Note that all these processes are driven by classical laser beams, via the intermediate states $\left|\varphi_{\pm}\right\rangle$.) Finally one measures all subnodes $\left(R_{k},L_{k}\right)_{k=2,\ldots,N-1}$ through state-selective ionization. This step can be achieved in parallel on the different subnodes. The average time needed for the entanglement swapping operation is hence the time needed for performing the gate and the measurement on a single ensemble.

At the end of the whole procedure, the subnodes $\left(R_{1}\right)$ and $\left(L_{N}\right)$, are decoupled from all the others and reduced in one of the four entangled states $\left\{ \left(\left|00\right\rangle \pm\left|11\right\rangle \right)/\sqrt{2},\left(\left|01\right\rangle \pm\left|10\right\rangle \right)/\sqrt{2}\right\}$. The unitary $W$ one has to apply on the qubit stored in $\left(L_{N}\right)$ -- through driving the appropriate pulse $\left|0_{L}\right\rangle \leftrightarrow\left|1_{L}\right\rangle$, to get the desired state $\left(\left|00\right\rangle +\left|11\right\rangle \right)/\sqrt{2}$ is determined from the outcomes of the measurements : it is indeed obtained as the product of $\left(N-2\right)$ transformations $W=\prod_{k=2}^{N-1}W_{k}$, where $W_{k}$ depends on the values $\left(i_{L_{k}},i_{R_{k}}\right)_{k=2,\ldots,\left(N-1\right)}$ found for the qubits stored in the left and right subnodes of the ensemble $\left(k\right)$: $$\begin{aligned}
\left(i_{L_{k}},i_{R_{k}}\right) & = & \left(0,0\right)\Rightarrow W_{k}=I\\
\left(i_{L_{k}},i_{R_{k}}\right) & = & \left(0,1\right)\Rightarrow W_{k}=\sigma_{x}\\
\left(i_{L_{k}},i_{R_{k}}\right) & = & \left(1,0\right)\Rightarrow W_{k}=\sigma_{z}\\
\left(i_{L_{k}},i_{R_{k}}\right) & = & \left(1,1\right)\Rightarrow W_{k}=\sigma_{z}\sigma_{x}
\end{aligned}$$ where $\sigma_{x}\equiv\left(\begin{array}{cc}
0 & 1\\
1 & 0
\end{array}\right)$ and $\sigma_{z}\equiv\left(\begin{array}{cc}
1 & 0\\
0 & -1
\end{array}\right)$ are the usual Pauli matrices.

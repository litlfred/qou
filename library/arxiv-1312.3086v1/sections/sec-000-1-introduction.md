---
doc_id: arxiv-1312.3086v1
doc_title: "Quantum repeater with Rydberg blocked atomic ensembles in ﬁber-coupled cavities"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1312.3086v1.pdf
source_sha256: ff328e7c7cbdc70c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.606
latex_coverage_ratio: 1.0
---
A possible route towards scalable quantum computers and quantum communication networks combines small quantum processor nodes which communicate via the exchange of moving information carriers, the so-called *flying qubits*, which will typically be photons. The direct exchange of a photon, either through free space or a fiber, between a pair of nodes does not have unit success probability, and to safely communicate quantum states, one can instead apply entangled state in teleportation protocols [@B93; @B96], where the entanglement of two remote nodes can be achieved, e.g. after multiple attempts until a suitable heralding detection event certifies the establishment of the state. For long distances, photon loss makes the success probability small, and hence the average time needed to establish a state for transmission of a single bit of quantum informsation very long. This problem, however, can be solved by the quantum repeater setup [@BDCZ98] which divides the transmission path between the nodes into smaller segments with auxiliary nodes over which losses are strongly diminished. The auxiliary nodes are first entangled with their nearest neighbors in a heralded way followed by a succession of local measurements which cause the graduate projection on quantum states with entanglement distributed over longer and longer distances (entanglement swapping). The implementation of this approach is compatible with different physical setups involving atomic ensembles and linear optical operations. The most influential proposal is the so-called DLCZ protocol [@DLCZ01], whose feasibility was experimentally considered in its two-node version in [@KBBDCDBK03].

This manuscript presents a quantum repeater scenario, based on the Rydberg blockade phenomenon. Rydberg blockade refers to the strong dipole-dipole interaction between pairs of highly excited atoms, which after laser excitation of a single atom shifts the resonance condition for all the other atoms and hence blocks further excitation by the laser field. Rydberg blockade forbids the resonant excitation of more than one Rydberg atom in an atomic mesoscopic sample [@CP10], and has been experimentally observed, e.g., in [@VVZCCP06; @UJHIYWS09]. In [@JCZRCL00] it was proposed to take advantage of Rydberg blockade in quantum information processing, leading to an intensive current field of research [@SWM10]. Different theoretical proposals have been recently put forward, which allow to take advantage of the full spectroscopic richness of Rydberg interactions for quantum information purposes [@BMM07; @BPMCS07; @BPM07], and a novel framework for quantum information encoding and computing has been proposed [@LFCD01; @BMS07; @BPSM08; @SWM10], in which register qubit states are physically implemented by the (symmetric) occupational states $\left|n_{i}=0,1\right\rangle$ of internal atomic levels $\left\{ \left|i\right\rangle ,\: i=1,\ldots,K\right\}$ in an ensemble of $N_{a}$ $(>K$) identical atoms.

The collective laser manipulation of the system combined with the Rydberg blocking interaction allows one to store and universally process information in the subspace of symmetric ensemble states containing at most one atom in each internal level. The primary advantage of ensembles over single atoms consists in their enhanced coupling to external control fields, which allows for efficient and rapid processing. A secondary practical advantage is that even in a multi-qubit register, one merely needs to address the atoms collectively, contrary to individual-atom encoding of qubits which requires the precise control of each and every single particle in the system.

In the quantum repeater we propose here, the nodes are *$N$* identical atomic ensembles, placed in cavities which are linked via optical fibers. The internal structure of the atoms is such that each ensemble $k=1,\ldots,N$ accomodates three logical subnodes, called the left $(L_{k})$, the right $(R_{k})$, and the auxiliary subnode $(A_{k})$ in the following. In the first step of our protocol, we entangle the logical state of the subnode $(R_{k})$ in the cavity $k$ with the polarization state of a single photon released in the cavity. This photon is then transmitted to the neighboring cavity where it is absorbed by the left subnode $\left(L_{k+1}\right)$ degree of freedom of the atomic ensemble in that cavity, which thus becomes entangled with $\left(R_{k}\right)$. A conditional gate applied to subnodes $(L_{k+1})$ and $(A_{k+1})$, followed by appropriate ionization detection is used to ensure that no error occurred during the entanglement generation, in particular that the photon was not lost during the transfer through the fiber between the cavities. If needed, subnodes $\left(R_{k},L_{k+1}\right)$ are reset so that the entanglement generation operation can be repeated until successful. Once all pairs $\left(R_{k},L_{k+1}\right)$ have been correctly entangled, entanglement is swapped by ensemble operations on every pair $\left(L_{k},R_{k}\right)$. Measurements using Rydberg blockade and ionization detection on all subnodes $\left\{ L_{k},R_{k},k=2,\ldots,\left(N-1\right)\right\}$ finally heralds the entangled state of the remote pair $\left(R_{1},L_{N}\right)$ which can be transformed into any required Bell state by application of a unitary operation on $\left(L_{N}\right)$ prescribed by the results of the measurements. If one of the measurements fails, the procedure must be repeated.

We note that the use of Rydberg blocked ensembles as quantum repeaters has been proposed in [@ZMHZ10; @HHHLS10]. Though related our proposal, however, never makes use of photon detection to generate entanglement between neighbouring nodes, we solely rely on ensemble laser manipulations (including ionizing pulses), ion detection whose efficiency can be made very close to one $\eta_{d}\sim1$, and photon transmissions through optical fibers. This allows for a shortened entanglement generation average time whose expression is derived in the Appendix.

The paper is structured as follows. In Sec. II, we present our quantum repeater scheme using Rydberg blockaded ensembles in optical cavities coupled by optical fibers. In Sec. III, we analyze the different steps of our protocol with emphasis on their robustness against errors, and we compute the average duration of our scheme. In Sec. IV, we suggest a physical implementation. In Sec. V, we compare our scheme with other schemes for quantum repeaters, and we conclude in Sec. VI.

# The model[]{#SecII label="SecII"}

Our quantum repeater setup consists of $N$ atomic ensembles placed in cavities which are linked by optical fibers (see Fig. [1](#Fig1){reference-type="ref" reference="Fig1"}a). Neighboring cavities are separated by the distance $L_{0}$.

The atomic level structure is represented in Fig. [1](#Fig1){reference-type="ref" reference="Fig1"}b. All the atoms are initially prepared in the "reservoir" state $\left|s\right\rangle$, and the atoms have, in addition, six metastable states denoted by $\left|0_{L}\right\rangle ,\left|1_{L}\right\rangle ,\left|0_{R}\right\rangle ,\left|1_{R}\right\rangle ,\left|0_{A}\right\rangle ,\left|1_{A}\right\rangle$, three excited states $\left|\varphi_{+}\right\rangle ,\left|\varphi_{-}\right\rangle ,\left|\varphi_{A}\right\rangle$ and three high-lying Rydberg states $\left|r_{+}\right\rangle ,\left|r_{-}\right\rangle ,\left|r_{A}\right\rangle$. We assume that the transitions given in Table [1](#Transitions){reference-type="ref" reference="Transitions"} can be independently and selectively addressed by appropriately tuned laser beams. In particular, it implies that we can couple pairs of states, $\left|s\right\rangle \leftrightarrow\left|r_{\pm,A}\right\rangle$, $\left|0_{L,R}\right\rangle \leftrightarrow\left|r_{-}\right\rangle$, $\left|1_{L,R}\right\rangle \leftrightarrow\left|r_{+}\right\rangle$ and $\left|0_{A}\right\rangle ,\left|1_{A}\right\rangle \leftrightarrow\left|r_{A}\right\rangle$ via the intermediate states $\left|\varphi_{+}\right\rangle$, $\left|\varphi_{-}\right\rangle$ or $\left|\varphi_{A}\right\rangle$.

We further suppose that the atomic samples are small enough to operate in the full Rydberg blockade regime, $i.e.$ their size should not exceed a few $\mu$m. As a consequence, when driving the transition $\left|s\right\rangle \leftrightarrow\left|r_{\pm,A}\right\rangle$ on a sample with $N_{a}$ atoms initially in the state $\left|s\ldots s\right\rangle$, multiply excited states are out of resonance due to the strong dipole-dipole interaction among Rydberg excited atoms, and the transfer of more than a single atom to the Rydberg state $\left|r_{\pm,A}\right\rangle$ is blocked. The fields are applied symmetrically to all atoms in each sample, and they hence excite the symmetric collective state with a single Rydberg excitation, $\left(\left|r_{k}s\ldots s\right\rangle +\left|sr_{k}s\ldots s\right\rangle +\ldots+\left|s\ldots sr_{k}\right\rangle \right)/\sqrt{N_{a}}$. The associated coupling strength is easily seen to be magnified by the factor $\sqrt{N_{a}}$ with respect to the coupling strength of the single atom transition $\left|s\right\rangle \leftrightarrow\left|r_{k}\right\rangle$. Applying a $\pi$ pulse on the collective ensemble transition, followed by the single-particle transition $\left|r_{k}\right\rangle \rightarrow\left|j\right\rangle$ $\left(j=0_{L},1_{L},0_{R},1_{R},0_{A},1_{A}\right)$, prepares the sample in a stable symmetric collective state $\left|N_{0_{L}},N_{1_{L}},N_{0_{R}},N_{1_{R}},N_{0_{A}},N_{1_{A}}\right\rangle$ where the $N_{j}$'s denote the populations of the different internal levels, restricted to values $0$ and $1$. Unitary operations can be applied in the eight-dimensional subspace of collective states, $\left\{ \left|N_{0_{L}},\left(1-N_{0_{L}}\right),N_{0_{R}},\left(1-N_{0_{R}}\right),N_{0_{A}},\left(1-N_{0_{A}}\right)\right\rangle \right\}$, by simply driving the corresponding single-atom transitions $\left|0_{L,A,R}\right\rangle \leftrightarrow\left|1_{L,A,R}\right\rangle$ and/or $\left|0_{L,A,R}\right\rangle ,\left|1_{L,A,R}\right\rangle \leftrightarrow\left|r_{+,-,R}\right\rangle$, as described in [@BMS07; @BPM07]. The collective state pairs ($\left|0_{L}\right\rangle ,\left|1_{L}\right\rangle$), ($\left|0_{R}\right\rangle ,\left|1_{R}\right\rangle$), and ($\left|0_{A}\right\rangle ,\left|1_{A}\right\rangle$) at each repeater node can thus be associated with three qubits, referred to as the left $\left(L\right)$, right $\left(R\right)$ and auxiliary $\left(A\right)$ subnodes, in the following.

We shall use a simplified notation for ensemble states, denoting the collective internal state population as $\bar{0}$ and $\bar{1}$, such that, e.g., $\left|\bar{0}_{L};\bar{1}_{R};\bar{1}_{A}\right\rangle$ denotes the state $\left|N_{0_{L}}=N_{1_{R}}=N_{1_{A}}=1;\, N_{1_{L}}=N_{0_{R}}=N_{0_{A}}=0\right\rangle$, where both the right and the auxiliary subnodes occupy the logic state 1, while the left subnode is in state $0$.

::: centering
::: {#Transitions}
               $\left|0,1_{A}\right\rangle \leftrightarrow\left|\varphi_{A}\right\rangle$
  ----------------------------------------------------------------------------------------------------
               $\left|0_{L,R}\right\rangle \leftrightarrow\left|\varphi_{-}\right\rangle$
               $\left|1_{L,R}\right\rangle \leftrightarrow\left|\varphi_{+}\right\rangle$
   $\left|s\right\rangle \overset{\sigma_{\pm}}{\longleftrightarrow}\left|\varphi_{\pm}\right\rangle$
                $\left|\varphi_{A}\right\rangle \leftrightarrow\left|r_{A}\right\rangle$
              $\left|\varphi_{\pm}\right\rangle \leftrightarrow\left|r_{\pm}\right\rangle$
               $\left|0_{L,R,A}\right\rangle \leftrightarrow\left|1_{L,R,A}\right\rangle$

  : The transitions required by our protocol.
:::
:::

<figure id="Fig1">
<div class="centering">
<img src="Fig1" style="width:9cm" />
</div>
<figcaption>(Color online) a) <em>The physical set-up for our quantum repeater</em>. <span class="math inline"><em>N</em></span> atomic ensembles are placed in two-mode cavities linked by optical fibers. b) <em>Atomic level structure</em>. The figure shows the “quantum-classical” two-photon transitions, <span class="math inline">|<em>s</em>⟩ ↔︎ |<em>r</em><sub>±</sub>⟩</span> driven via the intermediate states <span class="math inline">|<em>φ</em><sub>±</sub>⟩</span> with coupling strength <span class="math inline"><em>g</em><sub>±</sub></span> to the quantized cavity field modes <span class="math inline">±</span> and with Rabi frequencies <span class="math inline"><em>Ω</em><sub>±</sub></span> detunings <span class="math inline"><em>Δ</em><sub>±</sub></span> to the classical laser control fields. c) <em>The three steps of our scheme</em>. (1) entanglement of pairs of neighboring subnodes <span class="math inline">(<em>R</em><sub><em>k</em></sub>,<em>L</em><sub><em>k</em> + 1</sub>)</span>, entanglement swapping through two-bit gates (2) on each pair <span class="math inline">(<em>L</em><sub><em>k</em></sub>,<em>R</em><sub><em>k</em></sub>)</span> and measurement (3) of all subnodes but <span class="math inline">(<em>R</em><sub>1</sub>,<em>L</em><sub><em>N</em></sub>)</span>.</figcaption>
</figure>

It is a further requirement of our protocol that the transitions $\left|s\right\rangle \longleftrightarrow\left|\varphi_{\pm}\right\rangle$ couple non-resonantly to two different modes, $\pm$, with equal frequency and with detunings $\Delta_{\pm}$ with respect to the atomic transitions, but different polarization in the cavity (this will legitimate the assumptions we make below on the fiber transmission/losses). Driving the upper transition $\left|r_{\pm}\right\rangle \longleftrightarrow\left|\varphi_{\pm}\right\rangle$ with a laser field with detuning $\Delta_{\pm}$ and Rabi frequency $\Omega_{\pm}$, induces a second-order quantum-classical process, described by the single-atom effective Hamiltonian $\frac{\hbar g_{\pm}\Omega_{\pm}}{\Delta_{\pm}}a_{\pm}^{\dagger}\left|s\right\rangle \left\langle r_{\pm}\right|+h.c.$ where $a_{\pm}$ denotes the annihilation operator of the cavity mode $\pm$ and $g_{\pm}$ its coupling strength. This Hamiltonian derives from the adiabatic elimination of the intermediate state $\left|\varphi_{\pm}\right\rangle$ [@BPM07-1], and is valid for $\left|\Delta_{\pm}\right|\gg\left|\Omega_{\pm}\right|,\left|g_{\pm}\right|$. Performing an ensemble $\pi$ pulse on the quantum-classical two-photon transition $\left|s\right\rangle \leftrightarrow\left|\varphi_{\pm}\right\rangle \leftrightarrow\left|r_{\pm}\right\rangle$ hence converts a collective Rydberg excitation $\left|r_{\pm}\right\rangle$ into a cavity photon $\pm$ and the other way around, with the coupling strength **$\hbar\sqrt{N_{a}}g_{\pm}\Omega_{\pm}/\Delta_{\pm}$**. We emphasize that, though only a *single* cavity photon is emitted/absorbed during the process, the coupling can be made strong, thanks to the atomic ensemble magnification factor **$\sqrt{N_{a}}$** [@GBEM10]. To avoid spurious interference effects we suggest to apply different detuning parameters for the two transitions proceeding via the same intermediate state $\left|\varphi_{\pm}\right\rangle$.

Optical fibers [@P97] couple the cavities to each other, and we simply assume that the fiber between two neighboring cavities $\left(k,k+1\right)$ achieves the coupling $$V_{k,k+1}=\sum_{j=0,1}\hbar\alpha_{k,j}\left[a_{k,j}a_{k+1,j}^{\dagger}+a_{k,j}^{\dagger}a_{k+1,j}\right]\label{FiberCoupling}$$ with a coupling strength $\alpha_{k,j}$ between the modes $j=+,-$ in the $k^{th}$ cavity with annihilation operator $a_{k,j}$, and the same modes in the $\left(k+1\right)^{th}$ cavity. Since the modes $\left(+,-\right)$ differ by their polarizations but have the same frequency, we make the reasonable assumption that the $\alpha_{k,j}$'s have the same value $\alpha$ for all $\left(k,j\right)$. We moreover suppose that the coupling between two neighboring cavities can be switched on and off, for instance by a controlled Pockels cell : this will allow us to isolate and separately deal with pairs of coupled nodes.

Due to fiber loss, the transmission of a photon from one cavity to its neighbor is not perfect. We shall assume that the transmission efficiency is the same for all fiber connections and can be written under the form $\eta_{t}=\exp\left(-L_{0}/L_{att}\right)$ where $L_{att}$ is the attenuation length, typically of the order of $22$km (corresponding to losses of $0.2$dB/km). The probability for loosing one photon $\left(+,-\right)$ during the transmission along a fiber mode of length $L_{0}$ is thus given by $\left(1-\eta_{t}\right)$.

# The scheme []{#sec:The-scheme label="sec:The-scheme"}

In this section, we describe how to entangle two remote nodes using the model we presented in the previous section. First, we briefly sketch the different steps of our scheme in the ideal case without losses. Then, we show how to make our method immune to photon loss and spontaneous emission from the Rydberg level. Finally, we analyze the effects of other possible errors on the performance of our protocol.

## The different steps of the scheme

Initially, all the cavities are empty and all ensemble atoms are in the reservoir state $\left|s\ldots s\right\rangle$. The first step consists in entangling pairs of neighboring subnodes $\left(R_{k},L_{k+1}\right)$ (see Fig. [1](#Fig1){reference-type="ref" reference="Fig1"}c). To this end, one applies the sequence of operations given in Table [2](#EntanglementGeneration){reference-type="ref" reference="EntanglementGeneration"}. In this table, dashed-line arrows are used for non-resonant couplings to the intermediate states. Moreover, the "ensemble" nature of pulses is emphasized by a $\sqrt{N_{a}}$ factor above the concerned arrows. Finally, we indicate when a cavity mode is involved in a transition $\left|s\right\rangle \leftrightarrow\left|\varphi_{\pm}\right\rangle$ by writing "single photon $\pm$" above the corresponding arrow.

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

The first seven pulses $\left(i-vii\right)$ in Table [2](#EntanglementGeneration){reference-type="ref" reference="EntanglementGeneration"} prepare the subnode $\left(R_{k}\right)$ and the cavity $\left(k\right)$ in the entangled state $\left(\left|\bar{0}_{R}\right\rangle \otimes\left|-\right\rangle +\left|\bar{1}_{R}\right\rangle \otimes\left|+\right\rangle \right)/\sqrt{2}$ where $\left|\pm\right\rangle$ denotes the number state $\left|n_{\pm}=1\right\rangle$ of the cavity mode $\pm$. The photon thus released is then transferred to the cavity $\left(k+1\right)$ through the fiber (step $viii$). The last four pulses $\left(ix-xii\right)$ of the sequence translate the photonic excitation into an atomic excitation of the ensemble $\left(k+1\right)$ : a "$-$" photon is translated into a $\left|0_{L}\right\rangle$ excitation, a "$+$" photon into a $\left|1_{L}\right\rangle$ excitation. Finally, the two subnodes $\left(R_{k},L_{k+1}\right)$ are left in the state $\left(\left|\bar{0}_{R}\right\rangle _{k}\otimes\left|\bar{0}_{L}\right\rangle _{k+1}+\left|\bar{1}_{R}\right\rangle _{k}\otimes\left|\bar{1}_{L}\right\rangle _{k+1}\right)/\sqrt{2}$. The sequence of states along which the system evolves during the series of operations described in Table [2](#EntanglementGeneration){reference-type="ref" reference="EntanglementGeneration"} can be found in Table [3](#EntanglementGenerationStates){reference-type="ref" reference="EntanglementGenerationStates"}.

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

To complete the scheme, we now need to swap entanglement, *i.e.* to entangle the left and right subnodes $\left(R_{k}\right)$ and $\left(L_{k}\right)$ in every ensemble and decouple the first and last nodes from all the others. This constitutes the second step of the method (see Fig. [1](#Fig1){reference-type="ref" reference="Fig1"} c). To this end, one first simultaneously applies to each pair of subnodes $\left(R_{k},L_{k}\right)_{k=2,\ldots,N-1}$ the unitary transformation $\left(U_{L}\otimes U_{R}\right)\times P_{LR}\times\left(\mathbb{I}_{L}\otimes V_{R}\right)$, where $U=\exp\left(-\mathrm{i}\frac{\pi}{2}\sigma_{z}\right)\times\exp\left(-\mathrm{i}\frac{\pi}{4}\sigma_{y}\right)$ and $V=\exp\left(-\mathrm{i}\frac{\pi}{2}\sigma_{x}\right)\times\exp\left(-\mathrm{i}\frac{\pi}{2}\sigma_{z}\right)\times\exp\left(-\mathrm{i}\frac{\pi}{4}\sigma_{y}\right)$ are simply achieved through applying the appropriate laser-induced pulses $\left|0_{L,R}\right\rangle \leftrightarrow\left|1_{L,R}\right\rangle$ and $P_{LR}=\left(\begin{array}{cccc}
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

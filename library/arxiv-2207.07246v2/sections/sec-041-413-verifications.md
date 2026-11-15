---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-041-413-verifications
section_title: "Verifications"
section_number: 4.1.3
pages: 98-103
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.895
latex_coverage_ratio: 0.991
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#secVerify label="secVerify"}

In order to further support our conclusion that $\tau=0.2\textrm{ MeV}^{-1}$ indeed projected out the ground state and therefore our PIMC results are reliable, we calculate the potential $V=V^{NN}+V^{EM}$ along all the beads on the path. This is a typical quantity to calculate in PIMC calculations ([@Schmidt2000JCP]). The calculation is done in the same way as introduced in section [\[Recast\]](#Recast){reference-type="ref" reference="Recast"}. We just need to use the potential operator $V$ as the operator $\hat{O}$, and we place the $V$ at each imaginary time position from bead 0 to the last bead $N$ on the path. In other words, the $g^V_{lr,M}(\mathcal{R})$ in Eq.([\[gVRlrdef2\]](#gVRlrdef2){reference-type="ref" reference="gVRlrdef2"}) needs to be calculated from $M=0$ to $M=N={\tau}/{\Delta \tau}$. In this way, we are actually calculating $\langle {V}(\tau_1) \rangle$ which is, $$\begin{aligned}
\langle {V}(\tau_1) \rangle
= \frac{ Re  \langle \Psi_T| e^{-H \tau_1}  \left(V^{NN}+V^{EM}\right) e^{-H (\tau-\tau_1) } | \Psi_T \rangle  }
{ Re \langle \Psi_T| e^{-H \tau} | \Psi_T \rangle} ,
\label{potentialbeads}
\end{aligned}$$ where $\tau_1$ ranges from 0 MeV$^{-1}$ to $\tau$ as we put the $V$ operator from bead 0 to bead $N$. $\langle {V}(\tau_1) \rangle$ is symmetric around $\tau_1=\tau/2$. When $\tau/2$ is big enough to project out the ground state, $\langle {V}(\tau/2) \rangle$ is the ground state potential energy.

<figure id="potential">
<embed src="Figures/potential.eps" />
<figcaption>The potential energy along the beads for <span class="math inline"><em>τ</em> = 0.2</span> and 0.3 <span class="math inline">MeV<sup>−1</sup></span> for <span class="math inline"><sup>4</sup></span>He based on the AV6’ interaction. </figcaption>
</figure>

<figure id="potentialN2LO">
<embed src="Figures/potentialN2LO.eps" />
<figcaption>The potential energy along the beads for <span class="math inline"><em>τ</em> = 0.2</span> and 0.3 <span class="math inline">MeV<sup>−1</sup></span> for <span class="math inline"><sup>4</sup></span>He based on the local chiral N<span class="math inline"><sup>2</sup></span>LO interaction.</figcaption>
</figure>

In Fig. [1](#potential){reference-type="ref" reference="potential"}[^1], we show the results of $\langle {V}(\tau_1) \rangle$ as a functions of $\tau_1$ for $\tau=0.2$ MeV$^{-1}$ and $\tau=0.3$ MeV$^{-1}$. On the upper panel of Fig. [1](#potential){reference-type="ref" reference="potential"}, we show for different time step $\Delta \tau$ how $\langle {V}(\tau_1) \rangle$ change as $\tau_1$ from 0 MeV$^{-1}$ to the total imaginary time $\tau=0.2$ MeV$^{-1}$. As expected, since PIMC is projecting out the Hamiltonian's ground state, and the Hamiltonian's ground state is not the same as the potential operator's eigenstate, the time step error introduced by $\Delta \tau$ will have noticeable impact on $\langle {V}(\tau_1) \rangle$. That is why the curve of $\langle {V}(\tau_1) \rangle$ vs. $\tau_1$ are different for different $\Delta \tau$. However, as $\Delta \tau$ decreases, time step error will become smaller and smaller. And indeed, as we can see, the result for $\Delta \tau=1.5\times 10^{-4}$ MeV$^{-1}$ almost coincides with that of $\Delta \tau=2.5\times 10^{-4}$ MeV$^{-1}$. $\langle {V}(\tau_1) \rangle$ is about $-127\sim-123$ MeV. It looks like $\langle {V}(\tau_1) \rangle$ has converged when $\Delta \tau \leq 2.5\times 10^{-4}$ MeV$^{-1}$. This is a clear signal that a stable eigenstate of the Hamiltonian for $\tau=0.2$ MeV$^{-1}$ has been reached, and smaller $\Delta \tau$ and therefore more beads will not improve the convergence. Furthermore, in order to verify if this eigenstate is truly the ground state, we calculate for a larger total imaginary time of $\tau=0.3$ MeV$^{-1}$ with a similar time step $\Delta \tau=2 \times 10^{-4}$ MeV$^{-1}$, i.e. 1501 beads. The result is in the lower panel of Fig. [1](#potential){reference-type="ref" reference="potential"}. Indeed, the curve of $\langle {V}(\tau_1) \rangle$ vs. $\tau_1$ is almost the same as the $\tau=0.2$ MeV$^{-1}$ and $\Delta \tau \leq 2.5\times 10^{-4}$ MeV$^{-1}$ cases. This means further increasing the total time $\tau$ will not change the state, so the stable state reached for $\tau=0.2$ MeV$^{-1}$ must be the ground state.

Therefore, the ground state of the Hamiltonian is indeed reached when $\tau=0.2$ MeV$^{-1}$, and $\Delta \tau$ around $1.5\sim2.5\times 10^{-4}$ MeV$^{-1}$ is small enough. Besides, from Fig. [1](#potential){reference-type="ref" reference="potential"} we can see that in the area when $0.075\textrm{ MeV}^{-1}\leq\tau_1\leq0.125\textrm{ MeV}^{-1}$ for $\tau=0.2$ MeV$^{-1}$, and the area when $0.075\textrm{ MeV}^{-1}\leq\tau_1\leq0.225\textrm{ MeV}^{-1}$ for $\tau=0.3$ MeV$^{-1}$, the curves of $\langle {V}(\tau_1) \rangle$ vs. $\tau_1$ are almost flat. So that even $\tau=2\times0.075=0.15$ MeV$^{-1}$ may be sufficient to project out the ground state. Fig. [2](#potentialN2LO){reference-type="ref" reference="potentialN2LO"} is a similar graph for the local chiral interaction which also indicates $\tau=0.2$ MeV$^{-1}$ is sufficient[^2].

<figure id="figPIMCstructR">
<embed src="Figures/PIMCstructR.eps" style="width:95.03%" />
<figcaption>PIMC leading order structure function <span class="math inline"><em>R</em><sub>S</sub><sup>(1)</sup>(<em>τ</em>,<em>Δ</em><em>τ</em>)</span>. </figcaption>
</figure>

Besides checking the potential along the beads, the robustness of the ground state energy PIMC calculation can be understood as follows.

The trial state $| \Psi_T \rangle$, after operating with $\left[U(\Delta \tau)\right]^N$, can be expanded by the eigenstates of the Hamiltonian, $$\begin{aligned}
\left[U(\Delta \tau)\right]^N |\Psi_T \rangle = \sum_{n=0}^{\infty} A_n(\tau,\Delta \tau) |\Phi_n\rangle
=A_0(\tau,\Delta \tau)\left[ | \Phi_0 \rangle  +  \sum_{i=1}^{+\infty} \frac{A_i(\tau,\Delta \tau)}{A_0(\tau,\Delta \tau)} | \Phi_i \rangle \right] . ~~~
\label{UdtNexp}
\end{aligned}$$ where $A_n(\tau,\Delta \tau)$ are the coefficients which depend on $\tau$ and $\Delta \tau$ for $|\Phi_n\rangle$. We know that $\lim\limits_{\Delta \tau \rightarrow 0} \left[U(\Delta \tau)\right]^N= e^{-H \tau}$ and we also notice from Eq.([\[eHPsiT\]](#eHPsiT){reference-type="ref" reference="eHPsiT"}) that, $$e^{-H \tau} |\Psi_T \rangle =
a_0 e^{-E_0 \tau}
\left[ | \Phi_0 \rangle +  \sum_{i=1}^{\infty}\frac{a_i}{a_0}e^{-(E_i-E_0) \tau} | \Phi_i \rangle  \right],
\label{eHPsiTau}$$ So, comparing Eq.([\[UdtNexp\]](#UdtNexp){reference-type="ref" reference="UdtNexp"}) and Eq.([\[eHPsiTau\]](#eHPsiTau){reference-type="ref" reference="eHPsiTau"}) we find that for $\Delta \tau \rightarrow 0$,

::: flalign
\_ A_0(,) & = a_0 e\^-E_0 ,\
\_ &= e\^-(E_n-E_0) \_ []{#ratioAnA0 label="ratioAnA0"} .
:::

We calculate the ground state energy by using Eq.([\[PIMCopexpdetailE0dtau\]](#PIMCopexpdetailE0dtau){reference-type="ref" reference="PIMCopexpdetailE0dtau"}), the two parts in it are essentially the same and we pick one of them to take a closer look. We find $$\frac{\langle \Psi_T| H [U(\Delta \tau)]^N  | \Psi_T \rangle}{\langle \Psi_T| [U(\Delta \tau)]^N  | \Psi_T \rangle}
= E_0 \frac{1+ \sum_{i=1}^{+\infty}\frac{a_i^* A_i(\tau,\Delta \tau) E_i }{a_0^* A_0(\tau,\Delta \tau) E_0 }  }
{1+ \sum_{i=1}^{+\infty}\frac{a_i^* A_i(\tau,\Delta \tau) }{a_0^* A_0(\tau,\Delta \tau) }  }
\equiv E_0 R_{\text{S}}(\tau,\Delta \tau) ,
\label{PIMCstrucfull}$$ since Eq.([\[PIMCstrucfull\]](#PIMCstrucfull){reference-type="ref" reference="PIMCstrucfull"}) is real, we define a real function $R_{\text{S}}(\tau,\Delta \tau)$ as our PIMC error structure function, $$R_{\text{S}}(\tau,\Delta \tau)
\equiv Re \frac{1+ \sum_{i=1}^{+\infty}\frac{a_i^* A_i(\tau,\Delta \tau) E_i }{a_0^* A_0(\tau,\Delta \tau) E_0 }  }
{1+ \sum_{i=1}^{+\infty}\frac{a_i^* A_i(\tau,\Delta \tau) }{a_0^* A_0(\tau,\Delta \tau) }  } ,
\label{PIMCstrucRs}$$ and we can define its cutoff functions $R^{(n)}_{\text{S}}(\tau,\Delta \tau)$ such that $$R^{(n)}_{\text{S}}(\tau,\Delta \tau)
\equiv Re \frac{1+ \sum_{i=1}^{n}\frac{a_i^* A_i(\tau,\Delta \tau) E_i }{a_0^* A_0(\tau,\Delta \tau) E_0 }  }
{1+ \sum_{i=1}^{n}\frac{a_i^* A_i(\tau,\Delta \tau) }{a_0^* A_0(\tau,\Delta \tau) }  } .
\label{PIMCstrucRsn}$$ Considering Eq.([\[ratioAnA0\]](#ratioAnA0){reference-type="ref" reference="ratioAnA0"}), $R_{\text{S}}(\tau,\Delta \tau)$ and $R^{(n)}_{\text{S}}(\tau,\Delta \tau)$ will converge to 1 when $\tau$ is big enough and $\Delta \tau$ is small enough, and the energy will converge to $E_0$. We find that the structure Eq.([\[PIMCstrucfull\]](#PIMCstrucfull){reference-type="ref" reference="PIMCstrucfull"}) may be much less sensitive to $\Delta \tau$ than one may expect. We can assume the errors in Eq.([\[PIMCstrucfull\]](#PIMCstrucfull){reference-type="ref" reference="PIMCstrucfull"}) are mostly coming from the leading order errors in its denominator and the numerator. If the leading order error is from the first excited state, Eq.([\[PIMCstrucfull\]](#PIMCstrucfull){reference-type="ref" reference="PIMCstrucfull"}) can be approximated as $$\frac{\langle \Psi_T| H [U(\Delta \tau)]^N  | \Psi_T \rangle}{\langle \Psi_T| [U(\Delta \tau)]^N  | \Psi_T \rangle}
\approx E_0 \times Re \frac{1+ \frac{a_1^* A_1(\tau,\Delta \tau) E_1 }{a_0^* A_0(\tau,\Delta \tau) E_0 }  }
{1+ \frac{a_1^* A_1(\tau,\Delta \tau) }{a_0^* A_0(\tau,\Delta \tau) }  }
=E_0 R^{(1)}_{\text{S}}(\tau,\Delta \tau) ,
\label{PIMCstruc1}$$ and since Eq.([\[PIMCstrucfull\]](#PIMCstrucfull){reference-type="ref" reference="PIMCstrucfull"}) is real, we can assume $\frac{a_1^* A_1(\tau,\Delta \tau) }{a_0^* A_0(\tau,\Delta \tau) }$ in Eq.([\[PIMCstruc1\]](#PIMCstruc1){reference-type="ref" reference="PIMCstruc1"}) is mostly real and we can define a real function $B_1(\tau,\Delta \tau)$ as $$B_1(\tau,\Delta \tau) = Re \frac{a_1^* A_1(\tau,\Delta \tau) }{a_0^* A_0(\tau,\Delta \tau) }
\label{PIMCstrucB1}$$ such that $$R_{\text{S}}(\tau,\Delta \tau) \approx
R^{(1)}_{\text{S}}(\tau,\Delta \tau) \approx
\frac{ 1+B_1(\tau,\Delta \tau) \frac{E_1}{E_0} }{1+B_1(\tau,\Delta \tau)}.
\label{PIMCstrucRsB1}$$

Therefore, our result $E(\Delta \tau)$ in Eq.([\[PIMCopexpdetailE0dtau\]](#PIMCopexpdetailE0dtau){reference-type="ref" reference="PIMCopexpdetailE0dtau"}) will be very close to the true expectation $E_0$, as long as Eq.([\[PIMCstrucRsB1\]](#PIMCstrucRsB1){reference-type="ref" reference="PIMCstrucRsB1"}) is close to 1. In Fig. [3](#figPIMCstructR){reference-type="ref" reference="figPIMCstructR"} we plot the contour graph and show how the value of the leading order structure function $R^{(1)}_{\text{S}}(\tau,\Delta \tau)$ changes as $B_1(\tau,\Delta \tau)$ and $E_1/E_0$ change. We find as long as $B_1(\tau,\Delta \tau) \in [-0.1,0.1]$ (which is a reasonable range for a proper $\Delta \tau$), $R^{(1)}_{\text{S}}(\tau,\Delta \tau)$ will be close to 1 (the green area), it fluctuates from 0.9 to 1.1 so $E(\Delta \tau)$ will be around $E_0$ with at most $10\%$ error or so. In fact, our results in section [\[secResultCalc\]](#secResultCalc){reference-type="ref" reference="secResultCalc"} shows that $E(\Delta \tau)$ in PIMC works even better. From Figs. [\[energyall\]](#energyall){reference-type="ref" reference="energyall"} and [\[energyallN2LO\]](#energyallN2LO){reference-type="ref" reference="energyallN2LO"} we see that even with a wide range of $\Delta \tau$, the difference between $E(\Delta \tau)$ and $E_0$ is less than $3\%$ which is well below $10\%$. The robust $E(\Delta \tau)$ value also indicates the ground state path is robust, so the expectation values of other operators should be reliable too.

[^1]: Note that the potential operators and the Hamiltonian do not commute, so the eigenstates of the potential operators and the Hamiltonian are not the same. So even when the system reaches the ground state of its Hamiltonian, this ground state $| \Phi_0 \rangle$ is not an eigenstate of the potential operators. So $\langle {V}(\tau_1) \rangle$ has larger fluctuations than $\langle H(\tau_1) \rangle$. So in order to make Fig. [1](#potential){reference-type="ref" reference="potential"} look 'smooth', we need to take a longer computation time than computing the ground state energy.

[^2]: In order to save computation time, we did not include spin-orbit interaction, but it does not alter the conclusion. Fig. [2](#potentialN2LO){reference-type="ref" reference="potentialN2LO"} is not as smooth as Fig. [1](#potential){reference-type="ref" reference="potential"} simply because we used fewer core hours for it than we did for Fig. [1](#potential){reference-type="ref" reference="potential"}.

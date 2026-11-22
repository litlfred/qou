---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-008-free-fermions-and-the-discrete-bessel-kernel
section_title: "Free fermions and the discrete Bessel kernel"
section_number: null
pages: 10-11
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 1.0
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
[]{#sec:discrete-bessel label="sec:discrete-bessel"} We now derive the sideband correlation kernel for the Toeplitz scattering matrix [\[eq:ToeplitzS\]](#eq:ToeplitzS){reference-type="eqref" reference="eq:ToeplitzS"} acting on a zero-temperature Fermi sea [@MoskBuett2002; @PedersenBuett1998]. This requires specifying how the static scattering matrix $\mathcal U$ and the reservoir structure enter. The factored form $S^{\alpha\beta}_{nm}=\mathcal U^{\alpha\beta}(E)J_{n-m}(A)$ allows the $\mathcal U$ prefactors to be pulled out of the sideband sum in [\[eq:C\]](#eq:C){reference-type="eqref" reference="eq:C"}: $$C^{(\alpha)}_{np}(E)
  = \sum_m J_{n-m}(A)\,J_{p-m}(A)\;\underbrace{\sum_\beta \abs{\mathcal U^{\alpha\beta}(E)}^2 f_\beta(E_m)}_{\displaystyle\equiv\;\bar f_\alpha(E_m)}.
  \label{eq:Cgeneral}$$ Here $\bar f_\alpha(E_m)$ is the effective occupation seen in the outgoing lead $\alpha$: a weighted average of the reservoir distributions, with weights given by the static transmission probabilities $|\mathcal U^{\alpha\beta}|^2$.

In general $\bar f_\alpha$ is a smooth function of $m$ (not a sharp step), because different reservoirs contribute at different chemical potentials. The clean discrete Bessel kernel emerges when $\bar f_\alpha$ reduces to a sharp Fermi step. This happens in two physically transparent cases:

-   *Identical reservoirs.* If all reservoirs share the same distribution $f_\beta=f$ for every $\beta$, then $\bar f_\alpha(E_m)=f(E_m)\sum_\beta|\mathcal U^{\alpha\beta}|^2 = f(E_m)$ by unitarity of $\mathcal U$.

-   *Single populated reservoir.* If a single incoming channel dominates the outgoing lead (e.g., one reservoir completely fills the incoming mode and others are empty), then $\bar f_\alpha$ reduces to the occupation of that reservoir.

In either case, for each fixed central energy $E$ the effective occupation is a sharp step in the sideband index at zero temperature: $$\bar f_\alpha(E_m) = \Theta\!\big(m_F(E)-m\big),
  \label{eq:Fermistep}$$ where $$m_F(E) := \left\lfloor\frac{\mu-E}{\hbar\Omega}\right\rfloor
  \label{eq:mF-def}$$ is the largest integer $m$ for which $E_m=E+m\hbar\Omega\le\mu$ (with $\mu$ the chemical potential). We derive the discrete Bessel kernel and its Airy limit under this single-step assumption. The extension to the experimentally important two-terminal case is given at the end of this section. Inserting [\[eq:Fermistep\]](#eq:Fermistep){reference-type="eqref" reference="eq:Fermistep"} into [\[eq:Cgeneral\]](#eq:Cgeneral){reference-type="eqref" reference="eq:Cgeneral"} gives $$C_{np}(E)
  = \sum_{m\le m_F(E)} J_{n-m}(A)J_{p-m}(A).
  \label{eq:CToeplitz}$$ Shift the summation index by $r=m_F(E)-m\in\mathbb N_0$ and define $$\nu := n-m_F(E),\qquad \lambda := p-m_F(E).$$ Then $$K_A^{\rm (disc)}(\nu,\lambda)
  := C_{np}(E)
  = \sum_{r=0}^{\infty} J_{\nu+r}(A)J_{\lambda+r}(A).
  \label{eq:discreteBessel}$$ This is the *discrete Bessel kernel*. Mathematically, it is the same kernel that arises in the Poissonized Plancherel measure on partitions and in discrete orthogonal polynomial ensembles [@Johansson2001; @Borodin2000]; here it emerges from the physics of Floquet scattering. It is the outgoing correlation kernel of the Floquet sideband process, expressed in the shifted indices $\nu=n-m_F(E)$, $\lambda=p-m_F(E)$ that measure the distance from the Fermi cutoff. (We use $\lambda$ for the second index to avoid collision with the chemical potential $\mu$ in Eq. [\[eq:mF-def\]](#eq:mF-def){reference-type="eqref" reference="eq:mF-def"}.) The edge of the kernel---where Bessel functions cross over from oscillatory to exponentially decaying---lies at $\nu\sim A$, corresponding to outgoing sideband $n\sim m_F(E)+A$.

Physically, the kernel encodes the fact that the drive redistributes incoming fermions across sidebands with Bessel-function amplitudes, and the Fermi step cuts off the sum from below. At $T=0$ with a single sharp step, the kernel is a *projection kernel*: $K_A^{\rm(disc)}$ is idempotent ($K^2=K$), reflecting the Slater-determinant structure of the incoming state [@FetterWalecka]. At finite temperature or with a multi-step occupation, the kernel is no longer a projection but remains a quasi-free (non-projection) kernel with eigenvalues in $[0,1]$; the correlation structure is modified [@Johansson2007; @DeanLeDoussal2015; @DeanLeDoussal2016], but the process remains determinantal because the incoming state is a Slater determinant and the scattering map is linear: all $k$-point correlation functions of the outgoing occupations are determinants built from the two-point kernel $K_A^{\rm (disc)}$. In particular, if $N_\nu=b_\nu^\dagger b_\nu$ denotes the sideband number operator, then Wick's theorem [@FetterWalecka] implies $$\langle N_\nu\rangle = K_A^{\rm (disc)}(\nu,\nu),
  \qquad
  \langle N_\nu N_\lambda\rangle_c = -\abs{K_A^{\rm (disc)}(\nu,\lambda)}^2\qquad (\nu\neq\lambda).
  \label{eq:determinantal}$$ Thus the kernel determines all joint occupation statistics for any finite subset of sideband indices at fixed central energy $E$. We emphasize the qualifier "at fixed $E$": the sideband process is determinantal separately at each $E$, and different values of $E$ contribute independently. The full process on the product space $\mathbb Z\times[0,\hbar\Omega)$ (sideband index $\times$ central energy) is itself determinantal, with a kernel that is diagonal in $E$ [@FetterWalecka]. However, if one projects onto sideband index alone---as a physical detector does when it integrates over $E$---the marginal occupancies $\widetilde N_\nu=\int_0^{\hbar\Omega}(dE/2\pi\hbar)\,N_\nu(E)$ are sums of independent Bernoulli variables (one per $E$ slice). They take values in $\{0,1,2,\ldots\}$ rather than $\{0,1\}$ and do *not* form a determinantal point process. The simple form [\[eq:determinantal\]](#eq:determinantal){reference-type="eqref" reference="eq:determinantal"} applies only at fixed $E$.

The kernel also admits a useful closed form via a Christoffel--Darboux-type identity [@Watson1944; @Forrester2010] (see Appendix [\[app:CD\]](#app:CD){reference-type="ref" reference="app:CD"} for the proof). For $\nu\neq\lambda$, $$K_A^{\rm (disc)}(\nu,\lambda)
  = \frac{A}{2}\,\frac{J_{\nu-1}(A)J_\lambda(A)-J_\nu(A)J_{\lambda-1}(A)}{\nu-\lambda}.
  \label{eq:CD}$$ This representation makes the integrable structure of the kernel manifest and is the starting point for the edge analysis in the next section.

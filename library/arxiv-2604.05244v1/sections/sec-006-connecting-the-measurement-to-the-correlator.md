---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-006-connecting-the-measurement-to-the-correlator
section_title: "Connecting the measurement to the correlator"
section_number: null
pages: 7-9
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.996
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
[]{#sec:bridge label="sec:bridge"} With the detection kernel defined on the instrument side and the correlator $C$ defined on the device side, we can now state the central identity that connects them. A closely related signal-processing viewpoint on electronic coherences has been developed independently in the electron quantum optics literature [@Roussel2017]. The physics is simple: because the output signal $\hat Y_\alpha(t)$ is bilinear in the outgoing field operators, and because the detection kernel is a linear weighting in time, the measured expectation value is a bilinear functional of $C$, weighted by the detector response $c_{\rm det}$. The analysis frequency $\omega_0$ then acts as a tunable selector that picks out a specific off-diagonal block of the Floquet correlator.

Concretely, assume that the detector is sensitive to a linear, number-conserving output observable in lead $\alpha$ [@Clerk2010]. Any such observable is a one-body operator, bilinear in the outgoing field, and can be expanded in the Floquet basis [@Sambe1973; @MoskBuett2002] as $$\hat Y_\alpha(t)
  = \sum_{n,p\in\mathbb Z}\int_0^{\hbar\Omega}\frac{dE}{2\pi\hbar}
    \,e^{i(n-p)\Omega t}\,\mathcal G^{(\alpha)}_{np}(E)
    \,b^\dagger_{\alpha n}(E)b_{\alpha p}(E),
  \label{eq:Yexpand}$$ where the coupling matrix $\mathcal G^{(\alpha)}_{np}(E)$ depends on the specific transducer and is in general *not* diagonal in the sideband indices; for example, a current operator mixes different sidebands through the velocity matrix elements. The decomposition [\[eq:Yexpand\]](#eq:Yexpand){reference-type="eqref" reference="eq:Yexpand"} is the most general number-conserving one-body form at fixed central energy $E$; it excludes anomalous terms ($b\,b$ or $b^\dagger b^\dagger$) by the number-conservation assumption. The key observation is that the time dependence of each term is carried entirely by the phase $e^{i(n-p)\Omega t}$, so the detection kernel acts on it through the detector response evaluated at the detuning $\omega_0-(n-p)\Omega$.

Inserting [\[eq:Yexpand\]](#eq:Yexpand){reference-type="eqref" reference="eq:Yexpand"} into [\[eq:Kphys\]](#eq:Kphys){reference-type="eqref" reference="eq:Kphys"} and taking the expectation value gives the projection identity $$\langle \hat u_0^{(\alpha)}(\omega_0;t_0)\rangle
  = \sum_{n,p\in\mathbb Z}\int_0^{\hbar\Omega}\frac{dE}{2\pi\hbar}
    \,\mathcal G^{(\alpha)}_{np}(E)
    \,c_{\rm det}\!\big(\omega_0-(n-p)\Omega\big)
    \,C^{(\alpha)}_{np}(E).
  \label{eq:projection}$$ The derivation is a one-line substitution: the time integral over $K_{\rm phys}\cdot e^{i(n-p)\Omega t}$ produces $c_{\rm det}(\omega_0-(n-p)\Omega)$ by definition [\[eq:cdet\]](#eq:cdet){reference-type="eqref" reference="eq:cdet"}, and $\langle b^\dagger_{\alpha n}b_{\alpha p}\rangle = C^{(\alpha)}_{np}$. The physical content is that the analysis frequency $\omega_0$ selects the $(n-p)$-th off-diagonal block of $C$ [@Clerk2010]: setting $\omega_0=0$ probes the diagonal (sideband populations), while $\omega_0=k\Omega$ probes the $k$-th off-diagonal (inter-sideband coherences).

This selection becomes exact---with zero spectral leakage---when the time gate spans an integer number of drive periods and the analysis frequency is set to an integer multiple of $\Omega$.

::: lemma
[]{#lem:block label="lem:block"} Assume $W$ is the indicator function of an interval of length $L=NT$ containing an integer number of periods, and assume $h\equiv 1$ over that interval. Set $\omega_0=k\Omega$ with $k\in\mathbb Z$. Then $$c_{\rm det}\!\big((k-(n-p))\Omega\big)
  = e^{-i(k-(n-p))\Omega(t_0-L/2)}\,L\,\delta_{k,\,n-p},$$ where the Kronecker delta is between the integers $k$ and $n-p$. Hence the choice $\omega_0=k\Omega$ selects the $k$-th off-diagonal of $C$ exactly, with no leakage between different values of $n-p$.
:::

::: proof
*Proof.* With $c_{\rm det}(\Delta\omega)=\int_{t_0-L}^{t_0}e^{-i\Delta\omega t}\,dt$ and setting $\Delta\omega=(k-(n-p))\Omega$, one obtains $$c_{\rm det}\big((k-(n-p))\Omega\big)
  = e^{-i(k-(n-p))\Omega(t_0-L/2)}\,L\,\mathrm{sinc}\!\left((n-p-k)\pi N\right).$$ Since $n-p-k$ is an integer, the sinc vanishes unless $n-p=k$, in which case it equals $1$. ◻
:::

This is Fourier orthogonality at work [@Harris1978]: a commensurate gate gives an exact discrete Fourier projection onto the Floquet harmonics.

#### Phase reference and block selection.

With an integer-period gate and $\omega_0=k\Omega$, the detuning on the selected block vanishes, so the gate-position phase $e^{i\cdot 0\cdot(t_0-L/2)}=1$ drops out. The measured first moment reduces to $$\langle\hat u_0(k\Omega)\rangle = L\sum_n\int_0^{\hbar\Omega}\frac{dE}{2\pi\hbar}\;\mathcal G_{n,n-k}(E)\,C_{n,n-k}(E).
  \label{eq:u0-block}$$ The quantity [\[eq:u0-block\]](#eq:u0-block){reference-type="eqref" reference="eq:u0-block"} is a $\mathcal G$-weighted, energy-integrated sum over the $k$-th off-diagonal of $C$---not an individual matrix element. It is real-valued for $k=0$ (diagonal block) and complex for $k\neq 0$.

For $k\neq 0$, the complex phase of [\[eq:u0-block\]](#eq:u0-block){reference-type="eqref" reference="eq:u0-block"} depends on the *relative phase between the local oscillator (LO) and the drive*, not on the gate position. If the LO is derived from the same oscillator as the drive (synchronous detection [@Bjorklund1983]), this relative phase is stable and $\langle\hat u_0(k\Omega)\rangle$ is a well-defined complex amplitude. If the LO is free-running, the relative phase drifts and the first moment averages to zero over many shots; off-diagonal correlations are then accessible only through *second-order* observables (intensity, noise power [@Clerk2010]), as discussed below.

#### Linear versus quadratic observables.

The projection identity [\[eq:projection\]](#eq:projection){reference-type="eqref" reference="eq:projection"} and its block-selected form [\[eq:u0-block\]](#eq:u0-block){reference-type="eqref" reference="eq:u0-block"} concern the first moment $\langle\hat u_0\rangle$---a *linear* functional of the one-body correlator $C$. However, many experimentally relevant quantities---noise power, photon-number variance, zero-frequency noise spectral density---are second-order in the field and therefore involve a *quadratic* functional of $C$. For Gaussian or free-fermion states, Wick's theorem [@FetterWalecka] factorizes the requisite fourth-order correlators into products of $C$ entries. Schematically, the measured intensity decomposes as $$\langle |\hat u_0(\omega_0)|^2\rangle
  = \abs{\langle\hat u_0\rangle}^2
  + \mathrm{Var}(\hat u_0),
  \label{eq:intensity}$$ where the variance $\mathrm{Var}(\hat u_0) = \langle |\hat u_0|^2\rangle - |\langle\hat u_0\rangle|^2$ involves a double sum over sideband pairs weighted by $|c_{\rm det}|^2$ and by connected Wick contractions [@FetterWalecka] of $C$. The precise form depends on the coupling matrix $\mathcal G$ and is not needed here; the key structural point is that the variance is present even when the first moment vanishes (free-running gate, $k\neq 0$), and it provides a second, independent route to the sideband correlator.

For the diagonal block ($k=0$), the first moment [\[eq:u0-block\]](#eq:u0-block){reference-type="eqref" reference="eq:u0-block"} yields a $\mathcal G$-weighted sum of populations $C_{nn}(E)$, integrated over $E$; no phase reference is needed. For off-diagonal blocks ($k\neq 0$, inter-sideband coherences), one must either maintain a stable LO--drive phase reference to access the complex amplitude through the first moment, or work with the noise power (quadratic observable) which accesses weighted quadratic functionals of $C$ without phase sensitivity. In either case, the measurement returns a weighted aggregate over the block, not individual matrix elements, unless additional sideband or energy resolution is available.

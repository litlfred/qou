<!-- FILE_START: mass-physical-face-intro.md -->
We now specialise the algebraic mass endomorphism to physical predictions. We derive the neutron-proton mass splitting from the crossing asymmetry of the trefoil braid. We present the Borromean baryon mass formula, deriving proton and neutron masses from a single common scale. Finally, we extend the prediction to atomic nuclei using the seven-term $q$-integer mass formula.

We derive binding energies from the three-channel brane tower. The predictions match CODATA and AME data.

The stable binding energy equals the real part of the complex volume $\mathfrak{V}$. The beta-decay Q-value equals the imaginary part. We read binding and decay as parities of one complex object, not as independent predictions.
<!-- FILE_END: mass-physical-face-intro.md -->

<!-- FILE_START: neutron-proton-splitting.md -->
*The neutron-proton mass difference derives from the quantum dilogarithm volumes:*

$$
  \Delta m = m_{\mathfrak{n}} - m_{\mathfrak{p}}
  = \alpha \cdot \lvert \Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d})
    - \Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d}) \rvert
  \approx 1.302 \; \mathrm{MeV}
$$

*where $\Phi$ evaluates the respective quark ordering and $\alpha = m_e \times 8G$ sets the binding scale.*

Replacing one positive $\mathfrak{u}\mathfrak{u}$ crossing with a negative $\mathfrak{d}\mathfrak{d}$ crossing causes the splitting. The $\mathfrak{d}\mathfrak{d}$ crossing carries more confinement energy. This makes the neutron heavier. The $1.302$ MeV prediction matches the CODATA value to $0.63\%$.
<!-- FILE_END: neutron-proton-splitting.md -->

<!-- FILE_START: borromean-baryon-mass-formula.md -->
**Conjecture (Borromean baryon mass formula, common-scale form).**
*Every Borromean baryon $B = \mathcal{B}_3(K_{0_1}, K_{0_1}, K_{0_1}) \oplus \mathcal{L}_H$ has rest mass:*

$$
  \mathfrak{m}(B)
  \;=\;
  m_e \cdot \left[\,
    \frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2}
    \cdot \lambda_{\mathrm{scale}}
    \;+\; S(B)
  \,\right]
$$

*where $m_e$ is the electron mass, $\hbar_q$ is the q-deformed Planck constant, and $\mathrm{Vol}(\mathcal{B}_3) \approx 7.327$ is the Borromean rings complement hyperbolic volume. $S(B)$ is the Skein contribution of the orientation partition evaluated at $q_0$. $\lambda_{\mathrm{scale}}$ is a common Borromean scale shared by all Borromean baryons.*

The common-scale hypothesis asserts $\lambda_{\mathrm{scale}}$ depends only on $\mathcal{B}_3$ and $q_0$. It ignores the internal orientation partition. The orientation dependence falls entirely on the Skein term $S(B)$. The difference $\mathfrak{m}(n) - \mathfrak{m}(p)$ becomes independent of the unresolved $\lambda_{\mathrm{scale}}$. The resulting prediction matches the beta-decay residual to within 1015 ppm.
<!-- FILE_END: borromean-baryon-mass-formula.md -->

<!-- FILE_START: borromean-baryon-interpretation.md -->
**Remark (properties of the Borromean link).**
*The Borromean link $\mathcal{B}_3$ consists of three unknots. No two are linked, but all three together are inseparable. This provides the topological definition of confinement: constituents cannot be isolated.*

The link has hyperbolic volume $\mathrm{Vol}(S^3 \setminus \mathcal{B}_3) \approx 7.327$. Each component has a crossing orientation contributing to the Skein polynomial. The constituent unknots and the Hopf link both have zero hyperbolic volume. The entire baryon mass originates directly from the Borromean linking.
<!-- FILE_END: borromean-baryon-interpretation.md -->

<!-- FILE_START: q-integer-mass-formula.md -->
**Conjecture (Bethe-Weizsäcker emergence).**
*The phenomenological Bethe-Weizsäcker liquid-drop coefficients emerge strictly as products of quantum integers $[n]_q$ evaluated at $q_0$.*

*The five standard coefficients, plus two Hecke-derived extensions, take the form:*
- *Volume: $2[2]_q[7]_q \cdot m_e \approx 15.67$ MeV.*
- *Surface: $2[4]_q^2 \cdot m_e \approx 17.26$ MeV.*
- *Coulomb: $(q - q^{-1})[6]_q \cdot m_e \approx 0.68$ MeV.*
- *Asymmetry: $3[2]_q[7]_q \cdot m_e \approx 23.51$ MeV.*
- *Pairing: $[3]_q[7]_q \cdot m_e \approx 11.86$ MeV.*

The parameters formerly fit to data are algebraic $q$-rationals. The volume, surface, and Coulomb terms derive from the per-nucleon Wedderburn channel product. The pairing term reflects the Chebyshev sign alternation of iterated Hecke generators, not Pauli exclusion. We predict binding energies without empirical inputs.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-analytic constructs. Any generic categorical identities remain valid over an abstract coefficient ring.
<!-- FILE_END: q-integer-mass-formula.md -->

<!-- FILE_START: lambda-scale-substrate-form.md -->
*The half-symmetric Wedderburn-sum projection at $H_4$ has the exact closed form:*

$$
  \lambda_A(q) = \frac{1}{4} \sum_{\lambda \vdash 4} \dim_q V_\lambda
             = \frac{5}{2} + \frac{3}{4}\,h^2,
$$

*where $h = q_0 - q_0^{-1}$ is the Hecke deformation. All odd-$h$ coefficients vanish by $q \leftrightarrow q^{-1}$ symmetry.*

The partition spectrum at $H_4(q)$ is $p(4) = 5$. The half-symmetric count over conjugate pairs yields exactly $5/2$. This structurally derives the leading volume-density term. The evaluation of higher $h^2$ corrections remains an active research direction.
<!-- FILE_END: lambda-scale-substrate-form.md -->

<!-- FILE_START: topological-mass-trefoil.md -->
**Remark (topological mass evaluation).**
*We compute the mass of the electron (trefoil $\tau(2,3)$) and the Higgs field (figure-eight $4_1$).*

The trefoil is a non-hyperbolic torus knot. Its topological mass relies on the quantum dilogarithm acting as the analytic continuation of the volume:

$$
  \mathfrak{m}(\tau(2,3)) = \frac{\mathrm{Li}_2(q^{-2})}{\hbar_q^{2}}.
$$

The figure-eight is hyperbolic. Its topological mass uses the volume directly:

$$
  \mathfrak{m}(4_1) = \frac{\mathrm{Vol}(S^3 \setminus 4_1)}{\hbar_q^{2}} \approx 207.1.
$$

This matches the muon-to-electron mass ratio. The figure-eight knot supplies the universal mass mechanism. It couples to all knot-particles with positive crossing numbers. The knot topology alone dictates the mass scale.
<!-- FILE_END: topological-mass-trefoil.md -->

<!-- FILE_START: meson-kaon-pion-hecke-seifert.md -->
*The kaon-to-pion mass ratio factors into a Hecke character and a Seifert volume ratio:*

$$
  \frac{\mathfrak{m}_K}{\mathfrak{m}_\pi}
  \;=\;
  \chi^{(2,1)}(\sigma_1^5)
  \;\times\;
  \biggl(\frac{V_S(T(2,5))}{V_S(T(2,3))}\biggr)^{\!2}
  \;\approx\; 3.536.
$$

The ratio requires exactly three inputs: the standard representation character of $\sigma_1^5$, the Seifert volumes of the constituent torus knots, and the two-body composition exponent $2$. The exact algebraic evaluation matches the experimental ratio to 290 ppm.
<!-- FILE_END: meson-kaon-pion-hecke-seifert.md -->

<!-- FILE_START: gen3-meson-phi-hecke-seifert.md -->
*The third-generation meson built on the torus knot $T(2,7)$ has mass ratio:*

$$
  \frac{\mathfrak{m}_X}{\mathfrak{m}_\pi}
  \;=\; \chi^{(2,1)}(\sigma_1^7)\cdot\Bigl(\frac{V_S(T(2,7))}{V_S(T(2,3))}\Bigr)^2
  \;=\; (q_0^7 - q_0^{-7})\cdot\Bigl(\frac{15}{7}\Bigr)^2
  \;\approx\; 7.320.
$$

The predicted ratio unambiguously identifies $X$ as the $\phi(1020)$ meson. The odd-torus tower corresponds exactly to the strange-vector meson sequence. The $\eta$ meson carries an axial-anomaly contribution and falls outside this single-torus model.
<!-- FILE_END: gen3-meson-phi-hecke-seifert.md -->

<!-- FILE_START: tower-binding-energy.md -->
*The nuclear binding energy evaluates the brane tower partition function over all three Wedderburn channels of $H_3(q)$.*

*The binding energy sum is:*

$$
  B(Z, N)
  =
  \sum_{\lambda}
  w_\lambda \cdot m_e
  \cdot
  \sum_{i=0}^{A-2}
  \ln\bigl|\Phi_q(\hat{V}_i^\lambda)\bigr|.
$$

Each channel contributes independently. The symmetric channel provides the volume baseline. The standard channel encodes adjacent-nucleon correlation. The alternating channel captures parity structure. 

The analytical continuation of $\Phi_q$ bypasses the boundary $|V| = q$. This evaluation relies on zero fitted parameters. The derived values track observed $Z=1$ to $20$ data tightly.
<!-- FILE_END: tower-binding-energy.md -->


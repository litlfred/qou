## Proved Convention-D hierarchy vs open higher-order projections

Under Convention D ($z_D = q^3/(q^2 + 1)$), the ladder product $\Pi_{\mathrm{op}}(u) = \prod_{k=2}^\infty (1 + c_k u^k) = 1 + \sum_{n=2}^\infty p_n u^n$ separates cleanly into proved structural theorems and open higher-order operator identifications:

1. **All-order analytic control and distinct-partition inversion (`ConventionDAllOrderCkGeneratingFunction`):** In the bar-even variable $H = (q - q^{-1})^2$, every Wedderburn weight, GPMT modified quantum dimension $|d_D(S^{(1^3)})|^2 = 1/((H + 4)(H + 3)^2)$, Kohno–Drinfeld full-twist character $C_{\mathrm{KD}}^{(6)}(q) = 1 + \frac{9}{2}H + 3H^2 + \frac{1}{2}H^3$, and connected Borromean QED trace $\Delta\mathrm{tr}_{\mathrm{QED,conn}}(V^3) = H^2(4H + 9)/9$ is a rational function of $H$. Inverting $u_{\mathrm{bar}}^2(H) = H^2(H + 3)/(16(H + 4))$ hits its nearest algebraic branch point where $2H^2 + 15H + 24 = 0$, namely $H_* = (-15 + \sqrt{33})/4 \in (-3, -2)$, establishing the Lagrange–Bürmann convergence radius $R_u = \sqrt{u_{\mathrm{bar}}^2(H_*)} \approx 0.36900873$. Distinct-partition expansion bijects $(p_2, \ldots, p_{10})$ onto $(c_2, \ldots, c_{10})$ over any commutative ring ($c_2 = p_2$, $c_3 = p_3$, $c_4 = p_4$, $c_5 = p_5 - c_2 c_3$, $c_6 = p_6 - c_2 c_4$, $\ldots$), and $u(q_0)/R_u \approx 0.02308 < 1/40$ forces the $N \ge 9$ tail below $10^{-16}$.
2. **Quartic rung $c_4$ candidates and experimental envelope (`ConventionDC4QuarticCumulantDerivation`):** Unlike the negative historical Convention-C fit $-2 b^4 \approx -1.125$, first-principles Convention-D operator projections at $q \to 1$ yield positive rational quartic rungs:
   - the $m = 2$ divided-power Kashiwara crystal cosine coefficient $c_4^{\mathrm{Kash}}(q) = [2]_q / ([3]_q [4]_q) \to +1/6$, which coincides identically with the variance-matched Convention-D Jucys–Murphy content kurtosis rung $\frac{1}{2} + \gamma_2^D(1)/6 = +1/6$ ($\kappa_4^D(1) = -1/8$, $\gamma_2^D(1) = -2$);
   - the three-block GPMT+ modified-trace kurtosis rung $+101/288$ ($\kappa_4^{\mathrm{GPMT+}}(1) = -516/2401$).
   Because $u(q_0)^4 \approx 5.263 \times 10^{-9} < 6 \times 10^{-9}$ and $u(q_0)^5 < 5 \times 10^{-11}$, the entire $k \ge 4$ tail lies strictly below $10^{-4}\,\sigma_{\mathrm{exp}}(m_n)$ ($< 0.05\,\mathrm{ppt}$ of $m_n$).
3. **Open derivation paths for $k \ge 4$ uniqueness and $k \ge 5$ closed forms:**
   - *Finite-$q$ Khovanov–Rozansky link homology:* Evaluating $\mathrm{Kh}(L)(q, t)$ for the typed-$B_3$ Markov closure at finite $q_0$ to determine whether homological grading selects $+1/6$, $+101/288$, or a mixed QED-connected combination at $k = 4$ and supplies closed forms for $c_5, c_6, c_7$.
   - *Per-block KLR canonical-basis trace formula:* Computing the canonical-basis Markov trace at orders $\hbar_q^8, \hbar_q^{10}, \hbar_q^{12}$ across the Wedderburn sectors of $H_3(q)$.

## Historical Convention-C comparison and calibration record

Prior to the retirement of Convention C ($z_C = \sqrt{q}/(q + 1)$) and the inadmissible $z = 1$ coordinate-sum cell, four empirical closed forms were compared against target-sweep extractions:

| Rung | Historical Convention-C guess | Residual against retired sweep | Proposed pattern |
|:----:|:-----------------------------:|:------------------------------:|------------------|
| $c_4^{\mathrm{hist}}$ | $c_3 \cdot b^4 = -2 b^4$ | $0.9\%$ | Hopf–Jones seed $\times$ $b^4$ |
| $c_5^{\mathrm{hist}}$ | $-(b^2 + 1/2)$ | $2.4\%$ | Kashiwara $b^2$ plus half-integer offset |
| $c_6^{\mathrm{hist}}$ | $c_3^2 \cdot b^2 = 4 b^2$ | $14\%$ | Hopf–Jones squared $\times$ $b^2$ |
| $c_7^{\mathrm{hist}}$ | $c_3^3 = -8$ | $+114\%$ signed | Hopf–Jones cubed |

Those figures belong strictly to the retired Convention-C cell and carry no predictive status under the three-calibration discipline:

1. **Convention and base separation.** Under Convention C on the retired $z = 1$ cell, a five-rung product reached a $+6.02\,\mathrm{ppb}$ residual at $N = 3$, whereas the bare single-sector Convention-D Markov trace at $z_D = q^3/(q^2 + 1)$ without GPMT/Two-Term completion sits at $0.4447\,\mathrm{MeV}$ ($1.668 \times 10^8\,\mathrm{ppb}$ miss on the per-observable status table), and the Two-Term + GPMT + Habiro–Kashiwara Convention-D chain (`ConventionDC3AndTailSelectionDerivation`) operates on the canonical $z_D$ base.
2. **Provenance of historical sweep numbers.** On the Convention-C single-rung inversion, the proton-pin value is $c_3 = -2.06934257711516783787971951725$ (muon CODATA-2022: $-2.019860311874005$; superseded pre-reanchoring record: $-2.0098$). The historical sweep entries $(-1.1435, -1.2229, +3.4976, +57.149)$ for $c_4, \ldots, c_7$ have no live producer because inverting a target residual rung-by-rung is a calibration fit rather than a derivation; they are preserved solely to document why `defaultQBetaCKClosedForms` is a plain `def` rather than a typeclass `instance`.

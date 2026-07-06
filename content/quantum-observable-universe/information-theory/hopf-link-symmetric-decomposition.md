*Lean sibling: a field $R$ carrying the $q$-data (AGENTS.md §7c); the identity is purely algebraic modulo the Hecke relation.*

**Proposition (Hopf-link symmetric decomposition).** *The Hopf element $\sigma_1^2$ of $H_2(q)$ weights the two blocks of [`def:van-der-waals-hopf-channel`](#def:van-der-waals-hopf-channel) by the squared block eigenvalues:*

$$
  \sigma_1^2 = q^2 e_+ + q^{-2} e_-.
$$

*Equivalently, cleared of the $[2]_q = q+q^{-1}$ denominator:*

$$
  [2]_q \sigma_1^2 = q^2 (\sigma_1+q^{-1}) + q^{-2} (q-\sigma_1).
$$

*This follows from the Hecke relation $\sigma_1^2 = (q-q^{-1})\sigma_1 + 1$ (Lean `hopf_symmetric_decomposition`, sorry-free, verified Lean 4.24.0).*

The Hopf element $\sigma_1^2$ ([`prop:trm-hopf-sigma1-sq-closed-form`](#prop:trm-hopf-sigma1-sq-closed-form)) splits between the symmetric $e_+$ and antisymmetric $e_-$ blocks. At $q_0$, the symmetric weight fraction is $q^2/(q^2+q^{-2}) \approx :val[vdw_sigma1sq_pct_symmetric]{precision=1, witness=computations/hbond-vdw-sdp.witness.json}\%$. This $\approx 60/40$ split is not dominant. The van der Waals force does not correspond to the $e_+$ block. It corresponds to the bar-odd residual $\sinh(2\lambda)(e_+-e_-)$ that the canonical $P_{\mathrm{avg}}$ projection discards (`prop:vdw-pskew-isolation`). The symmetric block $e_+$ (Markov $q$-dimension $\approx :val[vdw_e_plus_qdim]{precision=3, witness=computations/hbond-vdw-sdp.witness.json}$) is the retained $\cosh$ carrier, distinct from the antisymmetric block $e_-$ ($q$-dimension $\approx 0.304$). Neither block alone constitutes van der Waals.

This completes the structural identification. The molecular dispersion energy scale poses a separate archimedean (inter-molecular-separation) question. The bare $e_+$ resides at the $\hbar_q$-scale. This Hecke decomposition does not fix the long-distance suppression to the $\sim 0.5\,\mathrm{kJ/mol}$ molecular van der Waals energy.

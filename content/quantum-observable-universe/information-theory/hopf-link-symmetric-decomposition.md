*Lean sibling: a field $R$ carrying the $q$-data (CLAUDE.md §7c); the identity is purely algebraic modulo the Hecke relation.*

**Proposition (Hopf-link symmetric decomposition).** *The Hopf element
$\sigma_1^2$ of $H_2(q)$ weights the two blocks of
[`def:van-der-waals-hopf-channel`](#def:van-der-waals-hopf-channel) by the
squared block eigenvalues:*

$$
  \sigma_1^2 \;=\; q^2\, e_+ \;+\; q^{-2}\, e_-,
$$

*equivalently, cleared of the $[2]_q = q+q^{-1}$ denominator,*

$$
  [2]_q\,\sigma_1^2 \;=\; q^2\,(\sigma_1+q^{-1}) \;+\; q^{-2}\,(q-\sigma_1),
$$

*which follows from the Hecke relation $\sigma_1^2 = (q-q^{-1})\sigma_1 + 1$
(Lean `hopf_symmetric_decomposition`, sorry-free, verified Lean 4.24.0).*

Thus the van der Waals correlation — the Hopf link
([`prop:trm-hopf-sigma1-sq-closed-form`](#prop:trm-hopf-sigma1-sq-closed-form)) —
is **dominantly the symmetric $e_+$ block**: its symmetric fraction
$q^2/(q^2+q^{-2})$ is $\approx :val[vdw_sigma1sq_pct_symmetric]{precision=1, witness=computations/hbond-vdw-sdp.witness.json}$
at $q_0$. The operator-selection SDP (witness `hbond-vdw-sdp`) confirms the
independent-channel reading: the symmetric block $e_+$ has Markov
$q$-dimension $\approx :val[vdw_e_plus_qdim]{precision=3, witness=computations/hbond-vdw-sdp.witness.json}$
— the genuine van der Waals channel, distinct from the directional
hydrogen-bond block $e_-$ ($q$-dimension $\approx 0.304$).

This is the structural identification; the molecular dispersion **energy** scale
is a separate, archimedean (inter-molecular-separation) question — the bare $e_+$
is $\hbar_q$-scale, and the long-distance suppression to the $\sim 0.5\,$kJ/mol
molecular van der Waals energy is not fixed by this Hecke decomposition.

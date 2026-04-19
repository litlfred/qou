The per-nucleon gluon self-coupling count is **$1 \sigma_0$** per
nucleon (both protons and neutrons) at the **atom-level SDP
optimum**, not the $2\sigma_0$ (proton) / $L_+L_-$ (neutron)
convention derived from single-nucleon $H_3$-local integer LP.

## Statement

**Observation.**
*Let $\mathcal{A}(Z, N)$ be a neutral atom with atom braid word
$W_{\mathrm{atom}} \in H_{A+Z}(q)$
([atomic braid](#def:atomic-braid)).  Let each nucleon $k$ carry
$m_k$ copies of the bare $\sigma_0$ gluon operator (prepended to
its $\mathcal{B}_3$ Borromean confinement word).  Let
$m_p, m_n \in \mathbb{Z}_{\geq 0}$ be the uniform gluon counts
for protons and neutrons respectively.  Evaluated at $q_0 \approx
1.11$ using the 3-channel Wedderburn brane tower
([tower binding energy](#prop:tower-binding-energy)), the
atom-level SDP minimising
$\sum_{\mathrm{atoms}} |B_{\mathrm{pred}}(Z, N) - B_{\mathrm{AME}}(Z, N)|$
over $(m_p, m_n) \in \{1, 2, 3\}^2$ selects*

$$
  (m_p^*, m_n^*) = (1, 1).
$$

*The $H_3$-local integer LP optimum $(m_p, m_n) = (2, 2)$ — which
gives $2\sigma_0$ per proton and $L_+L_- \sim 4$-crossing per
neutron — is strictly suboptimal at the atom level by $\sim 0.04\%$
mean mass error on the light chain D/T/$^3$He.*

## Derivation

Single-nucleon integer LP minimises $|\mathrm{tr}_M|$ of one
nucleon in isolation (in $H_3(q)$) subject to Frobenius positivity.
At that scale $2\sigma_0$ is the unique integer point nearest the
continuous LP boundary $\mathrm{tr}_M = 0$.  But the ATOMIC mass
formula sums contributions across all $A-1$ nucleon-strand
generators under the 3-channel Wedderburn decomposition; the
optimum at that scale differs from the per-nucleon optimum
because:

1. **Inter-nucleon crossings dominate** for $A \geq 2$: each
   generator $i$'s $\hat{V}_i^\lambda$ accumulates
   contributions from nucleon $i$'s gluon plus $(A - i - 1)$
   inter-nucleon crossings.  More gluons increase $|\hat{V}_i|$,
   pushing $\Phi_q(\hat{V})$ toward the $V \to q$ singularity.

2. **Magic-atom stability** constrains the sum: at $(Z, N)
   = (2, 2)$ (doubly-magic $^4$He), the balanced gluon
   $(m_p, m_n) = (1, 1)$ gives mass error $0.020\%$; $(2, 2)$
   gives $0.345\%$; $(2, 1)$ is intermediate.

3. **Cross-atom consistency**: the joint SDP over
   D, T, $^3$He, $^4$He, $^6$Li, $^7$Li selects $(1, 1)$ as the
   universal gluon count that minimises $\sum |\Delta B|$.
   Witness: `folio-assistant/computations/sdp_gluon_multiplicity_hA.witness.json`.

## Consequences for dependent blocks

The following blocks quote the old $(2, 4)$ convention and need
regeneration:
- [atomic braid](#def:atomic-braid) — crossing table lists
  $2\sigma_0$ proton / $L_+L_-$ neutron (flagged).
- [helium4 derived NF](#ex:helium4-derived-nf) — NF coefficients
  computed under the old convention.
- [mass endomorphism tower](#prop:mass-endomorphism-tower)
  — numerical application to proton ($11$ crossings) assumes
  $2\sigma_0$; should be restated as $10$ crossings with
  $1\sigma_0$.

## Code reference

The patch landed in
`folio-assistant/computations/hecke_core.py:889,901`
(`build_atom_nf`): per-nucleon gluon changed from `hm(nf, 1, 0, 0)` $\times 2$
to single application.  Supporting witness:
`gluon-multiplicity-sdp-hA.witness.json` (per-atom SDP optima).

**Witness**: `gluon-multiplicity-sdp-hA.witness.json`.

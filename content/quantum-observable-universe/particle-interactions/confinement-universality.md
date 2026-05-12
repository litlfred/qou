The nucleon normal form is **independent** of the photon
polarization parameters $(\varphi_0, \varphi_1, \varphi_{01})$
that created the constituent quarks.

## Statement

**Proposition.**
*Let $\gamma_k = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ be a 4-term photon
([Breit--Wheeler](#def:breit-wheeler-pair-production)).
Let $\mathfrak{N}(\varphi_0, \varphi_1, \varphi_{01})$ denote the
nucleon NF obtained by the derivation chain
([4-term pair nucleon](#prop:four-term-pair-nucleon)):
$\gamma\gamma \to q\bar{q} \to \mathcal{B}_3 \cdot \mathrm{crossings} \to \mathfrak{N}$.*

*Then for all $\varphi_0, \varphi_1, \varphi_{01} \in \mathbb{R}$:*

$$
  \mathfrak{N}(\varphi_0, \varphi_1, \varphi_{01})
  =
  \mathfrak{N}(0, 0, 0)
  =
  \mathrm{NF}(\mathcal{B}_3 \cdot \mathrm{crossings}).
$$

*The nucleon NF depends only on $q$ and the quark flavor assignment.*

## Proof

The derivation chain has two stages:

1. **Pair production**: $\gamma_k \cdot \gamma_k'$ produces a
   6-component NF vector with coefficients depending on
   $\varphi_0, \varphi_1, \varphi_{01}$.

2. **Confinement**: $\mathcal{B}_3 \cdot C(f_1, f_2; \sigma_0)
   \cdot C(f_1, f_3; \sigma_0) \cdot C(f_2, f_3; \sigma_1)$.

Stage 2 takes as input only the quark types ($\mathfrak{u}$ or
$\mathfrak{d}$), not the photon color weights.  The quark
extraction from the pair production NF selects the crossing
channel ($\sigma_0$ for up, $\sigma_0 - \tfrac{1}{2}H_A$ for
down) — these typed crossings are fixed by the quark flavor and
do not depend on $\varphi$.

Therefore, the confinement computation
$\mathcal{B}_3 \cdot \mathrm{crossings}$ is identical for all
photon polarizations.  The photon initial conditions determine
*which* quark type is produced at each vertex, but once the
quark types are fixed, the nucleon NF is determined by $q$ alone.

## Physical interpretation

This is the categorical expression of **asymptotic freedom**:
the strong interaction ($\mathcal{B}_3$ confinement) washes out
the electromagnetic initial conditions ($\varphi$ parameters).
At short distances (inside the Borromean braid), only the quark
flavor matters — the photon polarization is a long-distance
electromagnetic property that decouples under confinement.

**Witness**: `four-term-photon-to-atoms.witness.json`
(Phase 5: $\varphi_{01}$ sweep with constant nucleon NF).

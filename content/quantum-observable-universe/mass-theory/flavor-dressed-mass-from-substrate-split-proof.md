Combine two identities:

1. **Substrate side** ([`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md)):

   $$
     \frac{m_n - m_p}{M_N}
     \;\approx\;
     \frac{(q-1)^2 (1 - q^{-4})}{3}.
   $$

2. **Skein side** (proved via [`lem:pair-skein-mass-formula`](../observations/pair-skein-mass-formula.md)
   applied to the Borromean baryon braids of the proton and neutron):

   $$
     m_n - m_p
     \;=\;
     \frac{q + q^{-1}}{q^{1/2} + q^{-1/2}}
     \cdot
     (\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}).
   $$

Solving (2) for $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ and
substituting (1) gives the closed-form expression above.

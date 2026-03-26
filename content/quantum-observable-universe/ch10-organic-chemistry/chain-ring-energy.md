The linear $\mathrm{C}_6$ chain
([linear C₆](#ex:carbon-chain-c6)) and benzene
([benzene ring](#ex:benzene-ring)) illustrate the chain-versus-ring
energy landscape predicted by the ring-closure barrier
([ring-closure barrier](#prop:ring-closure-barrier)).

**Energy accounting.**
The chain $\mathcal{C}_6^{(1)}$ has 5 bonds.  The ring
$\mathcal{R}_6^{(1)}$ has 6 bonds plus the rearrangement cost.
The full energy difference is:

$$
  \Delta E_{\mathrm{close}}(6, 1)
  \;=\;
  E_{\mathrm{bond}}(1)
  \;+\;
  \Delta E_{\mathrm{closure}}(6, 1)
  \;\geq\;
  E_{\mathrm{bond}}(1)
  \;+\;
  2 \, |q + q^{-1}|.
$$

The first term ($E_{\mathrm{bond}}$) is **negative** — forming
a bond releases energy.  The second term
($\Delta E_{\mathrm{closure}}$) is **positive** — braid
rearrangement costs energy.  The net sign determines the
thermodynamics:

- If $|E_{\mathrm{bond}}| > \Delta E_{\mathrm{closure}}$: the
  ring is thermodynamically favourable (benzene is more stable
  than the chain in isolation).

- The **barrier height** is $\Delta E_{\mathrm{closure}}$ alone,
  because the transition state must pay the rearrangement cost
  before gaining the bond energy.

**The spring analogy.**
Think of the open chain as a spring held apart at its endpoints.
The interior bonds store elastic energy in the tridiagonal linking
structure.  Bringing the endpoints together requires:

1. **Folding**: the chain must bend in 3-space to bring
   $\mathcal{A}_1$ near $\mathcal{A}_6$ — this costs bending
   energy (Reidemeister II moves at interior atoms).

2. **Threading**: the first and last strands of the braid must
   pass through the intervening strands — this is the
   Yang–Baxter rearrangement cost.

3. **Snapping shut**: once the strands are adjacent, the final
   Hopf link forms, releasing $E_{\mathrm{bond}}$.

Step 2 is the bottleneck.  The chain is stable not because the
ring is unfavourable, but because reaching the ring requires
climbing over the rearrangement barrier — kinetic protection
from a topological origin.

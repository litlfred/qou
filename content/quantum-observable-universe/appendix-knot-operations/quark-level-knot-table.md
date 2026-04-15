The **quark-level knot table** decomposes each nucleon and light atom
into its constituent knot normal forms within $H_3(q)$.  For each atom
the table records the Markov trace $\mathrm{tr}_M$, net (sum of NF
coefficients), and knot-type classification of the leading terms.

| Atom | Content | $A$ | NF terms | $\mathrm{tr}_M$ | net |
|------|---------|-----|----------|-----------------|-----|
| Proton | $B_3(u,u,d)$ | 3 | 4 | $\approx -0.065$ | $\approx -0.14$ |
| Neutron | $B_3(u,d,d)$ | 3 | 4 | $\approx -0.145$ | $\approx -0.30$ |
| Protium | proton $+ e^-$ | 4 | 4 | $\approx -0.067$ | $\approx -0.14$ |
| Deuterium | $p + n + e^-$ | 7 | 135 | — | — |
| Tritium | $p + 2n + e^-$ | 10 | 14,067 | — | — |
| ${}^3$He (nuclear) | $2p + n$ | 9 | 7,480 | — | — |

The NF basis is $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$.
For light nucleons (proton, neutron), only four basis elements
have non-zero coefficients.  Heavier atoms generate thousands
of NF terms as the braid word grows combinatorially with $A$.

**Knot-type classification of NF terms:**

- **Identity** ($\gamma$): unknot — vacuum / neutrino channel.
- **Single generator** ($\sigma_i$): torus knot $T_{2,1}$ — single crossing.
- **Two-generator product** ($\sigma_i \sigma_j$): torus link — Hopf-link channel.
- **Three-generator** ($\sigma_i \sigma_j \sigma_k$): trefoil $T_{2,3}$ — electron channel.
- **Higher words**: composite braids with classification via Garside normal form.

The full NF decomposition (21,694 entries across 6 atoms) is generated
by running `quark-level-knot-table.py`.  The witness file is not
committed to the repository due to size (8.7 MB); regenerate with:

```
cd folio-assistant/computations && python3 quark-level-knot-table.py
```

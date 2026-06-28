## Open

Open problems for the
[recursive atom-knot atlas](#prop:recursive-atom-knot-atlas):

- **Principled derivation for ${}^{6}$Li, ${}^{7}$Li (and any new atom)**: the only
 admissible path is a **joint SDP on the full mass tower** — over all
 confinement levels $\ell$ and all atoms simultaneously — with
 **Gröbner–Shirshov filtration tracking** and **jet-order tracking**,
 yielding a canonical $T_w \in H_{n_0}(q_0)$ *per atom* as a structured
 certificate. Status: **certificate format proof-of-concept complete**
 ([`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb_filtration_jet_tracker.py)
 + [`gb-filtration-jet-order.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb-filtration-jet-order.witness.json)).
 The reducer computes filtration grade + jet-order events exactly in
 symbolic $q$ via SymPy on the test cases $\sigma_1^3$ (electron) and
 $(\sigma_1 \sigma_2^{-1})^3$ (proton/neutron body). The joint-tower
 SDP solver consumes this certificate format. The Markov closure of $T_w$ is then taken in $S^3$ and
 $\mathrm{Vol}_{\mathrm{hyp}}$ is computed at $\geq 50$ decimal digits
 via `hp_volume_of_link_closure(braid_word, digits=50)`; comparison to
 the AME binding energy happens *a posteriori*. Per-atom volume-match search is FORBIDDEN as a
 derivation route — the SDP must be joint over the tower so the GB
 filtration and the jet ordering are consistent across confinement
 levels. Until that joint SDP is run, no principled ${}^{6}$Li / ${}^{7}$Li
 entry exists.
- **Structural rule for $\rho$ in $B = \rho \cdot m_e \cdot \mathrm{Vol}(K)$**:
 the pattern $\rho \in \{1, 2\}$ for $\ell \leq 2$ atoms does not extend to
 ${}^{6}$Li, ${}^{7}$Li. Open:
 derive $\rho(Z, N)$ from ILP / confinement structure.
- **Hyperbolic-knot identification beyond $\ell = 2$**: ${}^{9}$Be, ${}^{11}$B,
 ${}^{14}$N — no entries are in scope until a *principled* (GB-NF) derivation
 exists. Volume-match search will not be used.
- **Photon $\rho$-factor**: photon mass $= 0$ by definition (no $\rho$
 needed), but for the recursive structure may tie to gauge-boson
 Higgs coupling.

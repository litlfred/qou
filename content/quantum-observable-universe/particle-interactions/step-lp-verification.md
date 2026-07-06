*We verify each atom to be LP-stable at every construction step. For each strand $k$ added to the braid:*

- *We compute the three Wedderburn channels (symmetric, standard, alternating) independently.*
- *No channel eigenvalue product is zero at any step.*
- *The symmetric and alternating channels maintain distinct signs. This prevents the channel-mixing annihilation that destabilizes the bare hydrogen atom.*

*We verify all $20$ atoms (all pass all-channel-nonzero at every step): ${}^1\mathrm{H}$, ${}^4\mathrm{He}$, ${}^7\mathrm{Li}$, ${}^9\mathrm{Be}$, ${}^{11}\mathrm{B}$, ${}^{12}\mathrm{C}$, ${}^{14}\mathrm{N}$, ${}^{16}\mathrm{O}$, ${}^{19}\mathrm{F}$, ${}^{20}\mathrm{Ne}$, ${}^{23}\mathrm{Na}$, ${}^{24}\mathrm{Mg}$, ${}^{27}\mathrm{Al}$, ${}^{28}\mathrm{Si}$, ${}^{31}\mathrm{P}$, ${}^{32}\mathrm{S}$, ${}^{35}\mathrm{Cl}$, ${}^{40}\mathrm{Ar}$, ${}^{39}\mathrm{K}$, ${}^{40}\mathrm{Ca}$.*

*We verify full LP stability (existence of an annihilator in the complete $H_n(q)$) for ${}^1\mathrm{H}$ (dressed, stable), the proton $\mathfrak{p}$ (stable), and the neutron $\mathfrak{n}$ (stable).*

**Witness**: `atom-mass-complete-wedderburn.witness.json`, Rust certificates in `tools/hecke-engine/certificate-*.json`.

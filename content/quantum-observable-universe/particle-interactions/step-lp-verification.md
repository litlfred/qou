*Each atom is verified to be LP-stable at every construction step.
For each strand $k$ added to the braid:*

- *The three Wedderburn channels (symmetric, standard, alternating)
  are computed independently.*
- *No channel eigenvalue product is zero at any step.*
- *The symmetric and alternating channels maintain distinct signs,
  preventing the channel-mixing annihilation that destabilises the
  bare hydrogen atom.*

*Verified atoms (all 20 pass all-channel-nonzero at every step):
${}^1\mathrm{H}$, ${}^4\mathrm{He}$, ${}^7\mathrm{Li}$,
${}^9\mathrm{Be}$, ${}^{11}\mathrm{B}$, ${}^{12}\mathrm{C}$,
${}^{14}\mathrm{N}$, ${}^{16}\mathrm{O}$, ${}^{19}\mathrm{F}$,
${}^{20}\mathrm{Ne}$, ${}^{23}\mathrm{Na}$, ${}^{24}\mathrm{Mg}$,
${}^{27}\mathrm{Al}$, ${}^{28}\mathrm{Si}$, ${}^{31}\mathrm{P}$,
${}^{32}\mathrm{S}$, ${}^{35}\mathrm{Cl}$, ${}^{40}\mathrm{Ar}$,
${}^{39}\mathrm{K}$, ${}^{40}\mathrm{Ca}$.*

*Full LP stability (existence of an annihilator in the complete
$H_n(q)$) is verified for ${}^1\mathrm{H}$ (dressed, stable),
proton $\mathfrak{p}$ (stable), and neutron $\mathfrak{n}$
(stable).*

**Witness**: `atom-mass-complete-wedderburn.witness.json`,
Rust certificates in `tools/hecke-engine/certificate-*.json`.

**Proposition (per-new-nucleon additive linearity).**
*The atomic Markov-trace denominator
$D(u) = 2^{2A+1} \cdot u^{\mathrm{shift}} \cdot (1 + u^{2})^{3A-1}$
of canonical pppnnn ordering
([`docs/audits/-w3-habiro-unblocked.md`](../../docs/audits/-w3-habiro-unblocked.md))
has shift exponent satisfying the additive-linearity recurrence:*

$$
  \mathrm{shift}(Z+1, N) \;-\; \mathrm{shift}(Z, N) \;=\; 18,
  \qquad
  \mathrm{shift}(Z, N+1) \;-\; \mathrm{shift}(Z, N) \;=\; 21,
$$

*for $Z, N \geq 1$ (i.e.\ $A \geq 2$).  Together with the base
case $\mathrm{shift}(D) = \mathrm{shift}(1, 1) = 40$, this fixes the
closed form*

$$
  \boxed{\;\;\mathrm{shift}(Z, N) \;=\; 18Z + 21N + 1\;\;}
$$

*on every atom in the canonical pppnnn ordering for $A \geq 2$.*

### Verified atoms

See [Table 1](#tbl:per-nucleon-shift-additive-linearity-table1-data).

(Witness: [`per-nucleon-shift-derivation.witness.json`](../../computations/per-nucleon-shift-derivation.witness.json),
5/5 assertions pass.  Cross-validated against
`term6-residues-at-roots.witness.json` for ${}^{5}$Li.)

### Generator-count decomposition

The additive linearity is structural: each new nucleon adds exactly
12 generators to the canonical-ordered braid in $H_{3A}(q)$:

See [Table 2](#tbl:per-nucleon-shift-additive-linearity-table2-data).

(11 from the nucleon's intrinsic structure
+ 1 from its incoming interface generator
in
[`mass_endomorphism.proton_cross`/`neutron_cross`](../../computations/mass_endomorphism.py).)

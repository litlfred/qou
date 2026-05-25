**Conjecture (atom-braid exterior-algebra structure).** *Let `A = Z + N` with $Z \geq 1$, $N \geq 0$, and let $T_w(Z, N) \in B_{3A}$ denote the canonical atom-braid word `atom_braid_word_3A(Z, N)` (`mass_at_3A_proper.py` recipe). Its image in the Iwahori–Hecke algebra $H_{3A}(q)$ under the standard $\sigma_i \mapsto T_i$ representation generates a sub-algebra whose GB-NF filtration shape is given by*

$$
\dim_R \bigl(F_k(T_w(Z, N))\bigr) \;=\; \binom{3A - Z}{\,k - (Z - 1)\,} \qquad (k = Z - 1, Z, \ldots, 3A - 1).
$$

*Equivalently, the sub-algebra is isomorphic (as a graded $R$-vector space, $R$ any field of characteristic 0 — typically $\mathbb{Q}$ for the GB-NF rational arithmetic, $\mathbb{R}$ for the substrate evaluation at $q_0 \in \mathbb{R}$) to the **exterior algebra** $\Lambda^*(R^{3A - Z})$, with grade shift $\delta = Z - 1$, total dimension $2^{3A - Z}$.*

## Empirical verification (PR following R5-full ⁴He registry extension)

The conjecture is verified across all 4 atoms with canonical `atom_braid_word_3A` recipes implemented in the Rust R5-SDP solver (post-`BraidLetter` extension):

| Atom | $(Z, N)$ | $n_0 = 3A$ | $3A - Z$ | $\delta = Z - 1$ | Filtration shape | Total |
|---|---|---|---|---|---|---|
| D ²H | (1, 1) | 6 | 5 | 0 | $\{1, 5, 10, 10, 5, 1\} = \binom{5}{k}$ | $2^5 = 32$ |
| T ³H | (1, 2) | 9 | 8 | 0 | $\{1, 8, 28, 56, 70, 56, 28, 8, 1\} = \binom{8}{k}$ | $2^8 = 256$ |
| ³He | (2, 1) | 9 | 7 | 1 | $\{1, 7, 21, 35, 35, 21, 7, 1\} = \binom{7}{k}$ | $2^7 = 128$ |
| ⁴He | (2, 2) | 12 | 10 | 1 | $\{1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1\} = \binom{10}{k}$ | $2^{10} = 1024$ |

Each row's shape is **exactly Pascal's triangle row $(3A - Z)$** with the appropriate grade shift, and totals are $2^{3A - Z}$.

## Structural interpretation

The exterior-algebra structure says: the canonical atom-braid lives in a **fermion Fock-space subalgebra** of $H_{3A}(q)$, with each "interface" between adjacent strands contributing one $\mathbb{Z}/2\mathbb{Z}$ degree of freedom. The proton-count $Z$ enters twice:

1. **Dimension reduction** ($\Lambda^*(R^{3A - Z})$ instead of $\mathbb{C}^{3A}$): each proton imposes one constraint, removing one degree of freedom.
2. **Grade shift** ($\delta = Z - 1$): each proton beyond the first shifts the filtration's lower bound by one — analogous to a chemical-potential or fermion-number offset.

This is fundamentally different from the standard Wedderburn decomposition $H_n(q) \cong \bigoplus_\lambda V_\lambda^{\oplus d_\lambda}$ (which for $H_{12}$ has dimension $12! \approx 5 \times 10^8$, **8 orders of magnitude larger** than the observed $2^{10} = 1024$ for ⁴He).

## Crystal-basis connection (open)

The exterior algebra $\Lambda^*(V)$ arises in Kashiwara–Lusztig theory as the **fermion Fock space** (the *q*-deformed sector of the Heisenberg-Weyl algebra at $|q| < 1$). The Z-dependent grade shift looks like a **charge sector** label in this framework. Open: identify the specific crystal-basis projection $H_{3A}(q) \to \Lambda^*(\mathbb{C}^{3A - Z})$ that the canonical atom-braid factors through.

A categorical proof would likely use:
1. Schur–Weyl duality $H_n(q) \otimes \mathrm{GL}_m \curvearrowright V^{\otimes n}$ at appropriate $V$ choice
2. The specific structure of `_PROTON_G0 / _PROTON_G1 / _NEUTRON_G0 / _NEUTRON_G1` 3-strand patterns (cf. `mass_at_3A_proper.py`)
3. KLR diagrammatics to identify the fermion-sector subalgebra

## Cross-references

- [`folio-assistant/computations/mass_at_3A_proper.py`](../../../folio-assistant/computations/mass_at_3A_proper.py) — canonical `atom_braid_word_3A` recipe
- [`tools/hecke-engine/src/gb_nf_reducer.rs`](../../../tools/hecke-engine/src/gb_nf_reducer.rs) — `BraidLetter` + `right_mul_t_avg` (R5-full extension supporting σ_avg)
- [`tools/hecke-engine/src/bin/joint_tower_sdp.rs`](../../../tools/hecke-engine/src/bin/joint_tower_sdp.rs) — joint-tower SDP solver (registry with 4 canonical-3A test atoms + ⁴He)
- [`folio-assistant/computations/joint-tower-sdp-rust.witness.json`](../../../folio-assistant/computations/joint-tower-sdp-rust.witness.json) — observed filtration shapes
- [`prop:per-braid-mass-tower`](per-braid-mass-tower.md) — canonical mass formula that consumes this structure
- [`prop:lepton-bring-surface-h3-3channel`](lepton-bring-surface-h3-3channel.md) — bring-surface analog for lepton sector

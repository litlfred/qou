# convention-auditor — detail file: which functional, and which bond topology

Read on demand. Summarised in `MEMORY.md`; this file carries the measurements.
Findings from bean `t7qv`, 2026-08-31/09-01, probes under `computations/probes/`.

## THE FUNCTIONAL — three tests that settle Markov vs q-Plancherel

Two weightings are in circulation and they are **not** interchangeable:

* **Markov** `y_lambda` — convention D: `y_sym = (h^2+2)/(h^2+4)`,
  `y_std = 1/[2]_q^2`, **`y_alt = 0`**.
* **q-Plancherel** `W_lambda = d_q^2 / sum d_q^2` — what
  `pyhecke.regime_scanner._compute_h3_wedderburn_weights` uses, and what the
  Lean `silver_lp_coincidence` cost vector turns out to be.

If you are unsure which one a piece of code is on, these three decide it, and
all three reject Plancherel for anything the substrate builds
(`which_functional_the_substrate_extremises_probe.py`):

1. **Markov property.** `tr(x . T_n)/tr(x)` must be a constant `z`. Markov gives
   `z` on both `H_2` basis elements; Plancherel gives `h/2` on `gamma` and
   `-2q^3/(q^6+2q^4-2q^2-1)` on `s0` — not even constant, so it carries no
   Markov parameter and is not a link invariant.
2. **The Gram radical.** Convention D's defining fact is `det G = 0` with the
   radical the three-strand q-antisymmetriser, which IS `y_alt = 0`. Plancherel
   has `W_alt = q^2/D != 0`, so its Gram is **nonsingular** — a different cone
   from the one every SDP in this corpus is posed over.
3. **Multiplicativity on disjoint strand blocks.** This is what gives
   `t^(A) = t^(x)A` and hence the whole atom construction. Re-running
   `h3a_frobenius_gram_offdiagonal_probe`'s own `H_6` test with Plancherel
   weights: **36 of 36 pairs fail**, worst relative error `10.9`. Not a
   normalisation — `gamma(x)gamma`, `gamma(x)s0`, `s0(x)gamma` all miss by
   `+4.0346` but `s0(x)s0` misses by `-2.0556`, **sign flipped**.

**Consequence worth knowing before quoting a metallic result.** The silver
coincidence is real and generalises — under Plancherel `T(sigma) = (h/2) T(gamma)`
identically at every `n`, so the cost coincidence sits at `h = 2 = delta_silver`
for every strand count, which extends the sorry-free Lean `silver_lp_coincidence`
from its `n = 2` statement. But it is a theorem about a functional that is not a
link invariant, has the wrong cone, and cannot build an atom. Under the Markov
trace the same coincidence moves to the **supergolden ratio** `q^3 = q^2 + 1`
(`q = 1.4655712318767680`). Do not transport a metallic result across that line.

## THE BOND TOPOLOGY — two builders in `pyhecke.atom` disagree, undocumented

For `A >= 3` these give different bond counts and nobody had written it down:

| A | `atom_gen_chains` (all pairs) | `atom_braid_word_3A` (chain) |
|---|---:|---:|
| 2 | 1 = `C(A,2)` | 1 = `A-1`  ← agree |
| 3 | 3 | 2 |
| 4 | 6 | 3 |
| 6 | 15 | 5 |

`atom_gen_chains` appends a bond for every pair (`for prev in range(k)`);
`atom_braid_word_3A` places them only between **adjacent** nucleons
(`if include_inter and k < A - 1`), at generator `3k+2`.

**Which is load-bearing depends on what you are doing.** The arity law
`c_atom = 2A - #(odd bonds) = A + 1` needs exactly `A-1` odd bonds — that is what
the census probe's `chain_bonds` counts and what Lean
`QOU.MassTheory.ClassicalTraceFloor` proves, so the **chain** is what the arity
results rest on. But on the binding evidence the **all-pairs** reading is better:
it nearly halves the `A`-scaling error against AME and is 3.4-3.7x less sensitive
to the nucleon ordering, which is a labelling convention a physical nucleus does
not have. Both facts measured in `chain_telescopes_and_ordering_sensitivity_probe`
and `all_pairs_bonds_and_saturation_probe`.

**Do not silently pick one.** The choice changes numbers by 16 % (chain) versus
4 % (all-pairs) under a mere relabelling of which nucleon is which.

## THE COLOUR CONVENTION SPLITS BETWEEN SCALES, deliberately

`atom.py` types crossings by flavour pair, and the like-flavour cases are exact
at both scales — `uu`/`pp` -> `beta 0`, `dd`/`nn` -> `beta 1`. The unlike case
is where they part:

* quark level `ud` -> `-h/2`, **colour-BLIND**, `beta` exactly `1/2`;
* nucleon level `pn` -> `D_PN = pn_interface_offset(q0)`, **colour-WEIGHTED**,
  `beta = 0.49965607229824338`, canonical by owner ruling 2026-08-15 (R3).

`atom.py` says of the quark-level ones, verbatim: *"nothing here establishes what
convention a u-d crossing should carry."* That is still open. Measured impact if
the quark `ud` crossings were switched to colour-weighted: the dual-vertex
transitions move by `-1.30e-4` and `+5.63e-5` — negligible for anything currently
riding on them.

## FORCE CHANNELS ARE ASSIGNED BY GENERATOR

Quoted from `atom.py`, not invented: `atom_gen_chains` — *"Inter-nucleon
crossings (strong force, gen 0)"*; `build_atom_nf` — *"Electrons: pe crossing
(EM channel, gen=1)"*. Lifted to the `3A`-strand braid: `3k+2` strong, `3k+1` EM,
`3k` intra.

The rate is set by the **generator, not by `beta`**. The same `sigma^-1`
(`beta = 1`) crossing gives `+0.907262` on a strong generator, `-0.599674` (p) /
`-0.784421` (n) on an EM one, `+0.437360` / `+0.506808` on an intra one — same
operator, **opposite sign**. Strong is flavour-independent; EM and intra are not.
The channels are exactly independent (cross-channel interference `6.7e-16` where
the strong channel self-interferes at `-2.4e-1`).

**Scope trap this creates:** `AME` binding energies are *nuclear* and carry no
electron content, so the quantity to compare against them is the **strong channel
alone**. Including the EM term moves `L(3H)/L(3He)` from `1.20` to `2.97` against
an experimental `1.10`. And `atom_braid_word_3A` has **no electrons at all** —
the EM channel exists only in the collapsed `H_3` formalisms.

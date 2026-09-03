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

## WHAT THE ALL-PAIRS CHOICE ACTUALLY BUYS — and what it costs

The section above says "do not silently pick one" and leaves it there. Measured
since (`three_body_term_has_the_wrong_sign_probe`), the difference between the
two topologies has a name and a mechanism:

* The **chain** attachment functional `P -> tr(P.A)/tr(P)` is **exactly rank
  one** — one constant over 20 random prefix words, spread `< 1e-12`. That is
  why the chain telescopes and why `A = 4` is reachable without `H_12`.
* The **all-pairs** attachment is **not** — `0.196 .. 0.696` on the same
  prefixes. The gap between them is the entire many-body content of the model.

The mechanism is the band generator `(T5 T4 T3)(T2+d)(T3 T4 T5)^-1`: it routes a
non-adjacent bond **through the intervening nucleon's strands**, so it does not
commute past the prefix. Two consequences you need before quoting either
topology:

1. **The three-body term is NEGATIVE at every A=3 flavour ordering**, `-9.04 %`
   to `-15.04 %` of the naive pairwise sum. All-pairs therefore *reduces*
   binding relative to summing bond constants — so **a naive all-pairs sum is an
   overestimate**, and quoting it as a prediction overstates binding by ~10 %.
2. **It privileges the MIDDLE nucleon.** Reversal is exact (`pnn` = `nnp` to
   `0.0`), but permutation is not: `pnp` vs `ppn` differ by `4.1686 %` and `npn`
   vs `nnp` by `5.0477 %` on *identical bond multisets*. The only difference is
   which nucleon the routing passes through. A physical nucleus has no middle,
   so this is a labelling artifact of embedding the bond graph in a line — the
   `~4 %` ordering sensitivity measured earlier, now with a cause.

**And the ceiling this implies, which is the number to know before spending more
time on bond topology at all:** `B(2H)` is exact (one bond admits no many-body
term) and the naive `B(4He)` contains no many-body term, so
`B(4He)/B(2H) <= 6.0643` against an AME `12.7196` — **short by `2.0975x`, with
`alpha` cancelling**. No normalisation fixes a ratio. Closing it needs large
*positive* many-body terms; all eight measured are negative.

## TRAP — comparing a far bond against the wrong adjacent one

In ordering `ppn` the far bond spans nucleons 1 and 3, which are `p` and `n`, so
it must be compared against the adjacent **p-n** bond at generator 5 — not the
`p-p` bond at generator 2. Against the wrong one it reads as a `0.187`
discrepancy and looks exactly like distance decay; against the right one it
agrees to `1.11e-15`. An assertion caught this mid-probe. If you think you have
found distance decay in the trace, check the bond *types* first.

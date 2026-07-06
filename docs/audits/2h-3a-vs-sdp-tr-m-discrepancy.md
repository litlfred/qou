# ²H — 3A-strand vs SDP-witness `tr_M`: two conventions, not a bug

**Earlier framing (commits `8a3bcb44`, `c0204970`).** The two
representations of ²H gave different `tr_M(q_0)` — flagged as an
internal-consistency issue.

**Resolution.** The two "T_w(²H)" Hecke elements **are not Markov-
equivalent representatives of the same braid**. They are different
constructions that the framework labels "²H" through different
conventions:

## 3A-strand convention

Defined in `computations/mass_at_3A_proper.py`
(`atom_braid_word_3A`). Lives in H_{3A}(q) — for ²H that's H_6.

For each nucleon k of the atom, three strands per nucleon:

- intra g_0 chain at generator σ_{3k}: 5 Hecke factors `(c, d)`
  realising the quark chain (uud for proton, udd for neutron) via
  `nucleon_gen_chains` in `hecke_core.py`.
- intra g_1 chain at generator σ_{3k+1}: 5 more Hecke factors.
- inter-crossing at σ_{3k+2} (when k < A−1): 1 factor matching the
  pp / pn / nn convention (e.g. pn = `(1, −h/2)`).

These are Hecke factors `c·T_g + d·I`, NOT pure braid generators.
For ²H the resulting element is a 23-factor product in H_6 living
on 6 strands.

The "3A-strand atom braid" is therefore a particular Hecke
element of H_6, custom-built from quark-chain plus inter-crossing
data. Its tr_M(q_0) is `0.388286471547...`.

## SDP-witness convention

Recorded in
[`joint-tower-sdp-rust.witness.json`](../../computations/joint-tower-sdp-rust.witness.json)
under `per_atom_certificates[name="deuteron-2H"]`. Lives in
H_{n_0}(q) at native strand count `n_0 = 3` for ²H. The braid word

  `[1, -2, 1, 1, 1, -2]   →   σ_1 σ_2^{-1} σ_1 σ_1 σ_1 σ_2^{-1}`

is a **pure braid** in B_3 (just σ_1, σ_2, σ_2^{-1}). Its closure
is some knot or link in S_3. Its tr_M(q_0) is `0.288326...`.

## Why the two differ

They're different mathematical objects:

| Property | 3A-strand | SDP-witness |
|---|---|---|
| Hecke algebra | H_6 | H_3 |
| Element type | 23 generic Hecke factors `(c, d, g)` | 6-letter pure braid word |
| Construction source | `atom_braid_word_3A` (quark chain + inter) | joint-tower SDP feasible solution |
| tr_M(q_0) | 0.388286 | 0.288326 |
| Native to atom-knot mass identity? | No | Yes (per master prop) |

The 3A-strand convention is a sub-pipeline used by some scripts
(`atom_nf_symbolic_D.py`, `binding_canonical.py`,
`atom_per_generator_volumes`) to inspect the per-quark-channel
contributions. It's a useful analytical tool but it is not the
canonical Hecke element T_w(²H) that the master proposition's
mass identity B(²H) = m_e · ρ · tr_M(T_w(²H)) refers to.

## Which is canonical for the mass identity

Per
[`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
algorithm step 1:

> Run the joint mass-tower confinement SDP on all ℓ' ≤ ℓ atoms
> simultaneously. Output: a structured certificate per atom
> recording the canonical Hecke element T_w ∈ H_{n_0}(q_0) in GB-NF.

So the **SDP-witness** convention is the canonical one. The
deuteron's canonical T_w is the 6-letter B_3 pure braid in
`joint-tower-sdp-rust.witness.json`. Its tr_M(q_0) ≈ 0.288326 is
the value entering the Term-1 contribution to B(²H).

The 3A-strand element of H_6 is a separate construction used for
quark-channel-decomposition analysis — useful but not the mass-
identity's canonical input.

## Implications for earlier audits

- Commit `c256ba88`'s claim that "²H's 3A-strand atom braid has
  tr_M ≡ 0 in ℚ(q)" was based on an earlier stale witness; the
  current 3A-strand value is `0.388286`, NOT zero. Walked back in
  commit `8a3bcb44` already.
- Commit `8a3bcb44`'s "internal-consistency issue" between the two
  ²H representations is THIS document's clarification. The two
  values are correct; they just compute different objects.
- The `historical_K_comparison` field for ²H in
  `atomic-tr-m-wenzl-bridge.witness.json` should use the SDP-
  witness `tr_M = 0.288326`, not the 3A-strand `0.388286`. (Both
  are recorded; the SDP value is the one to compare against
  J_{6_2}, modulo the post-Archimedean ribbon caveat in
  `markov-test-is-post-archimedean.md`.)

## Implications for 1 ppb

The Term-1 contribution to B(²H) is `m_e · ρ · |tr_M(T_w)|`. With
ρ = 1 (per witness) and tr_M = 0.288326 (canonical SDP value):

  Term-1(²H) = 0.51100 · 1 · 0.288326 = 0.14733 MeV

vs B_AME(²H) = 2.22458 MeV. So Term-1 is about 6.6% of the total ²H
binding energy — the rest comes from Terms 2-6 of the unified mass
formula (mass-endomorphism tower, pair-tower, Frobenius co-Casimir,
chirality, jet residues).

The 3A-strand 0.388286 is NOT used directly in the canonical
Term-1; it features in the pre-six-term `atom_mass_*.py` analysis
scripts that decompose mass into per-quark-channel contributions.
Those scripts produce different witnesses (e.g., `mass-table-best
.witness.json`'s family-1 entries via `mass_endomorphism.py`).

## Action items

1. **No action needed on the value discrepancy.** They're correct,
   computing different things.
2. **Update `atomic-tr-m-wenzl-bridge.witness.json` description**
   to clarify the SDP-witness `tr_M` is the canonical one for the
   mass identity (already implicit; making explicit will prevent
   future confusion).
3. **Mark scripts that use 3A-strand** (`atom_nf_symbolic_D.py`,
   `mass_at_3A_proper.py`, `atom_per_generator_volumes`) as
   "quark-channel decomposition analysis", not "canonical Term-1".
   Optional cleanup; not blocking.

## What this rules out as a 1 ppb lead

The "3A vs SDP discrepancy" is no longer a structural anomaly to
chase. The path forward for 1 ppb stays:

- **Plan F** — MPFR @ 50 dps for Term-1 (already done for proton/
  neutron/D via Wenzl bridge in `atomic-tr-m-wenzl-bridge.witness.json`)
- **Terms 2-6 in MPFR** — the bulk of the mass; not yet 50-dps
- **R5-full SDP-as-solver** — produces canonical T_w for atoms
  beyond the current registry (⁶Li, ⁷Li, …)

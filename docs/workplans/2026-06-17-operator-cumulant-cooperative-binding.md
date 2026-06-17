# Cooperative α-term = the connected (cumulant) part of the multi-interface operator product (option 3, 2026-06-17)

**Branch:** `claude/operator-cumulant-cooperative-2026-06-17`
**Picks up:** the Δ_λ-route arc (merged #2405/#2417/#2426). Option 3 = a
**principled** operator-magnitude derivation. **Discipline:** formalize-first;
no fit, no production rewire.

> **Status (2026-06-17): route gated, then closed — recorded as a conceptual
> result, not an open plan.** The operator-cumulant idea below is sound (the
> cooperativity must live in the connected operator non-factorization, invisible
> to the scalar trace per #2405). But realizing `Δ_coop` for a bound state first
> requires selecting `𝓑₃` as the confinement operator, and
> [`2026-06-17-delta-lambda-two-remaining-directions-closed.md`](../audits/2026-06-17-delta-lambda-two-remaining-directions-closed.md)
> (merged #2433) shows **no continuous variational principle selects the Borromean
> signature** (signature-cos ≈ 0 for every candidate). So the build plan below is
> **not actionable** until the genuine dense Wedderburn-projector SDP is
> implemented (the one open compute lever that, if it selects the Borromean
> signature, unlocks this route). Do **not** re-open the unchecked boxes as a
> quick task — the lever is bounded, not pending.

## The conceptual advance — *where* the cooperativity must live

The whole arc (LP → quadratic → Bring → chirality → scalar-magnitude variants)
searched for a **scalar per-block magnitude** or a **trace functional** that
supplies the cooperative α-binding. **#2405 proves that search is doomed:**

> `B_sym = α·ln(tr_free/tr_atom)` is **exactly** the additive (A−1)-bond chain,
> to the 50-dps floor. So the scalar Markov trace **factorizes exactly over
> bonds** — it carries **zero** cooperative (many-body) content.

Therefore the cooperative term is **not any function of the scalar trace** —
which kills every scalar-magnitude and trace-functional candidate at a stroke
(and explains why all of them failed).

But the operator combiner `A^λ_{ξν}(I)` carries **more** than the scalar trace:
it is the operator on the joint multiplicity space encoding the **inter-nucleon
correlation** at each interface. So the cooperativity can only live in the
**operator non-factorization between interfaces** — the **connected (cumulant)
part** of the multi-interface operator product:

> **`Δ_coop = (full multi-interface operator product) − (factorized product)`**

This object is the first candidate that is simultaneously:
1. **consistent with #2405** — its scalar trace vanishes (the scalar trace
   factorizes exactly), so it does **not** disturb `B_sym`;
2. **genuinely cooperative** — it is exactly the failure of the interface
   operators to commute/factorize (many-body by construction);
3. **derived, not fitted** — it is `product − factorized`, not a chosen
   norm/trace (the fit-risk that sank the scalar variants and the bare-norm
   operator candidates).

That is the non-fit target the arc was missing. It says: the α-binding is the
**operator entanglement between the inter-nucleon bonds**, invisible to the
(exactly-factorizing) scalar trace.

## Build plan (multi-session — honest)

1. **Pull the kernel.** `A^λ_{ξν}(I)` = `computations/a_operator/a_operator_recursive.py::interface_blocks()`
   (sibling `wenzl-a3-intertwiner-or3` / `f393badec0`; not on main). Cherry-pick
   or coordinate-merge; it runs A≤4 self-contained.
2. **Construct the multi-interface product.** ⁴He's `(2,2)` chain in the
   **canonical strand order `['p']·Z + ['n']·N = p-p-n-n`** (fixed by the
   production `atom_braid_word_3A`, #2405 — the ordering is load-bearing: a
   permutation like `p-n-p-n` would give bonds `{pn, np, pn}` and a different
   product) has the 3 adjacent-bond interfaces `{pp, pn, nn}`. Compose the
   interface operators along that chain (the operator analogue of
   `tr_atom = Π tr_bond`).
3. **Extract the connected part** `Δ_coop = product − Π(factorized)` (the cumulant
   / non-commutator content).
4. **Derive-or-refute.** Does `Δ_coop`, scaled by the *existing* `E₀`/`m_e`
   (NO new constant), give the right **sign** and **rough magnitude** of the
   ⁴He α-residual (`B_AME − B_sym ≈ 16.3 MeV`)? Across the α-band (⁴He, ⁸Be,
   ¹²C, elevated per #2405) does it track? If yes → the cooperative term is
   derived; if no → operator-cumulant refuted, fall to option 2 (α-cluster).

## Fit-risk management (STRICT)

- `Δ_coop` is **structurally fixed** (`product − factorized`), not searched.
- The **scale** must be the existing `E₀ = m_e/(q₀(q₀−1))`; introducing any new
  constant = a fit = blocked (CAL-4 / three-calibration discipline).
- If the magnitude needs a free multiplier to match AME, that is a **refutation**
  (per the deuteron `C_knot` retraction), not a result.

## Caveat — extracting a *scalar* from Δ_coop routes back through the LP gate

A formalize-first check before building: since #2405 forces the scalar trace to
factorize exactly, **`Tr(Δ_coop) = 0`** — the cumulant operator is nonzero but
**traceless in the binding observable**. So a *scalar* binding (MeV) cannot be a
trace of `Δ_coop`; it needs a **non-trace functional**. The principled (non-fit)
one is the **master-formula expectation** on the bound state `T=𝓑₃`:
`⟨Δ_coop⟩_T = Σ_{i,j∈A*} u_i (G⁻¹)_{ij} ⟨Δ_coop,b_j⟩`
([`prop:confinement-frobenius-reciprocity`](../../content/quantum-observable-universe/particle-interactions/confinement-frobenius-reciprocity.md))
— **not** an ad-hoc norm/eigenvalue (those are the fit-risk).

But `⟨·⟩_T` needs the **LP active set**, which #2417/#2426 left **OPEN** (the
indefinite-Gram `𝓑₃`-selection problem: the min-action LP returns the trivial
`tr_M=0` vertex, not `𝓑₃`). **So option 3 routes back through the LP-selection
gate.** The map is now complete and the three Δ_λ-route opens are revealed to be
**one interconnected problem**:

> **(i) LP `𝓑₃`-selection** (the bound state / active set) ⊗
> **(ii) the cumulant operator `Δ_coop`** (where cooperativity lives) ⊗
> **(iii) the master-formula scalar `⟨Δ_coop⟩_T`** (the non-fit MeV).

(ii) is now identified; (iii) is the principled extraction; both are gated on
(i), the indefinite-Gram selection. **Closing (i) closes all three.**

**Implication for path choice.** The **α-cluster recursion (option 2)** is the
**non-trace / geometric** route (`B_magic = m_e·Vol·ρ`, ⁴He as magic input) —
it **sidesteps the entire trace ⊗ operator ⊗ LP web** above. So if the operator
route stays gated on the open LP selection, option 2 is the cleaner path to a
non-fit α-magnitude. (Recorded so the operator build isn't pursued blind into
the LP wall.)

## Status

Opened. The conceptual target (connected operator-cumulant) is the contribution
of this doc; the compute (steps 1–4) is the multi-session build. Findings below
as they land.

## Cross-links
- `docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md` — `B_sym` exact factorization (the "zero scalar cooperativity" fact).
- `docs/audits/2026-06-17-chirality-delta-lambda-binding-sweep.md` — the scalar-magnitude refutations (#2417).
- `docs/workplans/2026-06-17-operator-magnitude-binding.md` — the option-2 triage (#2426): `A^λ_{ξν}(I)` is a reconstruction kernel, not a magnitude.
- PR #2403 (`wenzl-a3-intertwiner-or3`) — the `A^λ_{ξν}(I)` kernel owner.

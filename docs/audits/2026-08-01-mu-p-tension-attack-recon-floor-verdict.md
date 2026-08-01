# μ–p tension attack (qou-ph2a) — recon + verdict: irreducible substrate floor, not a fittable gap

**Date:** 2026-08-01. **Bean:** `qou-ph2a`. **Scope:** does operator-valued
branching / Δ_λ structure *predict* or *close* the 210 ppb μ–p tension
(m_μ +210 ppb, 9.5σ, proton-pinned q₀)? **Verdict below:** the tension is most
likely the framework's **irreducible substrate floor** — a locked 9.5σ
*prediction*, publishable as such — not a bug to fit away. One un-refuted
derivation route survives (Σ(2,3,5) WRT / s5-so3 keystone) and is attacked in a
sibling commit under formalize-first discipline.

This doc is the corpus-grep record (AGENTS.md §Before declaring "open"/"refuted")
so the μ–p tension is not re-attacked from scratch. It **re-scopes** nothing to
scope-(b); every refutation cited below is quoted from the artifact that proved
it.

## 1. What the μ–p tension IS (not a mass-formula error)

The canonical absolute nucleon mass is CODATA-matching to ppb
(`canonical_mass.proton_mass_mev()` → +1.35 ppb; see
`docs/canonical-mass-formula-guardrail.md`). The tension is **relational**, in the
overdetermined H¹(Bring) datum:

- **Muon pin (CAL-2):** `m_μ/m_e = Vol(4₁)/ℏ_q²` fixes q₀ → `1.10997859555…`.
- **Proton pin:** `m_p = 2(m_μ·F_Bor − 6m_e)` with `F_Bor = |tr_M(β_Bor)|·[3]_q!/q³`
  fixes q₀ → `1.10997858275…`.
- **No single q₀ reconciles both.** Pinning on the more precise proton ratio
  (0.06 ppb) leaves m_μ a **prediction** that misses CODATA by ~210 ppb = **9.5σ**.

Per `docs/audits/2026-05-28-mu-p-tension-substrate-floor.md`, this is an
**irreducible ~240 ppb floor in m_p / ~11.5 ppb in q₀ / ~210 ppb in m_μ**. That
audit's standing warning: *"any fit that closes an observable below this floor is
modelling the tension = noise."*

## 2. The structural mechanism is identified — GAP-A-4 — and OPEN

`content/quantum-observable-universe/lean/QOU/BraidsAndKnots/GapA4MuonBranching.lean`
scaffolds the honest hypothesis: the bare anchor `m_μ = m_e·Vol(4₁)/ℏ_q²` is a
**scalar (ℓ=1) evaluation**; under an operator-valued generation tower the muon
(ℓ=2) lives in the **dim-5 icosahedral irrep** (the (3,2) block of `H_5`, tied to
Bring's quintic surface), and its mass should carry a Wedderburn-trace correction
`F(E_{(3,2)}, q₀)`.

Concretely, the `GapA4MuonMass` **structure** carries `wedderburn_correction` as a
free field, and `target_correction_constraint` is a `def … : Prop` **predicate**
pinning it to `0.999999788` (the 210 ppb) — neither the field nor the predicate
*derives* the value. Per AGENTS.md §"Axiomatization is NOT a Proof": a structure
field plus a target predicate does **not** discharge the math. GAP-A-4 is **open**.

## 3. The most natural realization is REFUTED (#2584, merged)

The q-deformed **projector-weight shift** on the `H_5` Markov trace — the obvious
way to make the (3,2) block break the scalar symmetry — was tested and refuted
(`docs/audits/2026-06-22-keystone-qdeform-projector-shift.md`):

- It gives `δ = T_μ − T_e = 0.2075` — **6–7 orders of magnitude too large** for
  209.8 ppb.
- It is **bar-mixed**, failing the **bar-even precondition** the 210 ppb correction
  must satisfy (the muon anchor is amphichiral-4₁ / bar-symmetric).

Consequence (s5-so3 ledger): *"the Markov-trace surface is now exhausted; any
surviving q-closure must leave the trace-weighting entirely."* So the
magnitude+parity of the correction is doubly constrained, and the naive
trace-reweighting route is dead.

## 4. The empirical closures are sub-floor fits = noise

`MmuR9V9Closure.lean` reaches m_μ to 0.036× the L2 target via
`m_μ = m_e·Vol(4₁)/ℏ_q²·(1 − δ_R9 − δ_V9)`, `δ_R9 = ℏ_q⁶·q/5`,
`δ_V9 = ℏ_q⁸·[3]_q/25`. The `/5`, `/25 = 5²` gesture at the icosahedral `H_5`
structure, but the file is explicitly **NEAR-MATCH, NOT DERIVED** ("promotion →
derived requires the 5 theorems"; no class instance constructed). Per §1's floor,
a closure this far below 240 ppb is **modelling noise**, not physics. It is a fit;
it does **not** wire to production as canonical (AGENTS.md anti-laundering).

## 5. Verdict

**The 210 ppb μ–p tension is most likely the framework's genuine irreducible
substrate floor.** Two independent q₀ pins that no single value reconciles is
*content*, not error: it is a locked **9.5σ prediction** on m_μ, publishable **as a
prediction** (a co-determined deviation), exactly as the substrate-floor audit
frames it. The honest L2 dashboard should show m_μ at 210 ppb (FAIL vs 100×) and
say so — not fit it green.

**One derivation route remains un-refuted:** the s5-so3 keystone's colored
**Σ(2,3,5) WRT / Habiro q-series** whose q₀-evaluation must reproduce the `W_λ`
family (`docs/coordination/s5-so3-keystone.md`, bean `s5bb`). This is a hard,
long-horizon quantum-topology object, not a quick win. It is attacked separately
(sibling commit) **formalize-first**: state the two invariants any realization must
satisfy — **(i) bar-even parity** (from #2584) and **(ii) the heat-kernel-defect
coefficient** `144·C(n) = −n(n−1)(2n−13)` with the `n=7` sign change
(`WLambdaDefectClosedForm.lean`, sorry-free) — before any numerics.

## 6. Anti-recurrence note

Do **not** re-attack the μ–p tension via Markov-trace reweighting / projector-weight
shift (refuted #2584) or via integer-tower / R9V9-style fits (sub-floor = noise).
Only a **derived** bar-even correction from the surviving Σ(2,3,5) WRT route — or an
independent geometric evaluation of `E_{(3,2)}` — would change the verdict. Until
then, the floor stands and m_μ is reported at 210 ppb (FAIL), honestly.

## Cross-refs

- `docs/audits/2026-05-28-mu-p-tension-substrate-floor.md` — the floor magnitude.
- `docs/audits/2026-06-22-keystone-qdeform-projector-shift.md` — projector-shift refutation.
- `docs/coordination/s5-so3-keystone.md` — the surviving WRT route.
- `docs/coordination/2026-08-01-l2-strategy-q0-observed-delta-lambda-scope.md` — L2 strategy context.
- `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/GapA4MuonBranching.lean` — the open scaffold.
- `content/quantum-observable-universe/lean/QOU/BraidKnot/MmuR9V9Closure.lean` — the labelled fit.

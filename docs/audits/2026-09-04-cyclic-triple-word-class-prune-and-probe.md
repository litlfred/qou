# The non-monotone word class, formalize-first: only the cyclic triple carries a cross term, and on the production words it is intensive-suppressed — ≤ 1 MeV, shrinking with A, against a 7–27 MeV extensive residual

**Date:** 2026-09-04 · **Beans:** `qou-sorn` (this), `qou-kru4` (corrected + closed), `qou-ls86`,
`qou-brng` (frontier), `qou-5vhf` · **Arc:** many-body collective term / carrier question ·
**Scope:** a Lean prune (sorry-free) that collapses the class to one shape, then a probe on the
production ²H/³H/³He/⁴He words with **no fitted count**. Verdict: **scope-(a) negative** for the
cyclic-triple class under the production binding law. **Nothing is wired, nothing is fitted, no
production number moves.**

> **🛑 LAW SUPERSEDED THE SAME DAY (retraction of this note's MeV column, `qou-rp9i`).** Every
> MeV figure and the verdict in §3–§4 below use `B = Q_β·(tr_free − tr_atom)`. #6611 (merged
> 2026-09-04 09:17 UTC) refutes that law at every scale and leaves `B = E₀·ln(tr_free/tr_atom)`,
> `E₀ = m_e/(q₀(q₀−1))`, standing. Under the log law this class is **extensive** (per-bond
> shifts p–p 3.77 / p–n 5.65 / n–n 14.09 MeV, A-independent) and **over-shoots by 3–8× with the
> retracted asymmetry sign** — still a scope-(a) negative, for a different reason. Read
> `2026-09-04-cyclic-triple-under-log-law.md` for the live numbers; §2 (the Lean prune) and the
> 32/32 kernel agreement here are law-independent and stand.

## 1. The question, and the order it was answered in

PR #6561's audit left one option open: *"a formalize-first probe of a non-monotone word class,
gated on a structural argument for why an inter-nucleon bond would re-cross after its
neighbour"*. The owner chose it. Formalize-first means the structural question was settled in
Lean **before** anything was computed, and it changed the probe: the argument the option asked
for turned out to be **false** — a bond re-crossing after its neighbour carries no cross term
at all — and the class collapsed to a single shape with an exactly known value.

## 2. Lean — which departures from monotonicity carry a cross term

`content/quantum-observable-universe/lean/QOU/MathlibExt/RevisitClassCrossTerm.lean`
(namespace `QOU.MathlibExt.RevisitClass`), over the corpus's `MarkovTrace` structure, generic
`CommRing R` / `Ring A`; `lean`-direct exit 0, zero `sorry`, `#print axioms` on all eight
declarations `= {propext, Classical.choice, Quot.sound}`:

| revisit pattern, prefix `x ∈ H m` | cross term vs the monotone word of the same content | declaration | needs |
|---|---|---|---|
| `x gₘ gₘ₊₁ gₘ` — one step up and back | **none** | `oneStepRevisit_eq_monotone` | cyclicity + one Markov move |
| `x gₘ gₘ₊₂ gₘ` — skip the neighbour | **none** | `skipRevisit_eq_monotone` | far commutation |
| `x gₘ gₘ₊₁ gₘ₊₂ gₘ` — climb two, come back | **none** | `twoStepClimbRevisit_eq_monotone` | far commutation + Markov |
| `x gₘ gₘ₊₁ gₘ gₘ₊₁` — the **cyclic square** `(gₘ gₘ₊₁)²` | **`(z² − hz − 1) · tr x`** | `cyclicSquare_cross_term` | braid + quadratic |

Also: `tr_hopfChain` (`(hz+1)² tr x`), `tr_cyclicSquare` (`(hz(hz+1) + z²) tr x`),
`interleaved_eq_stab_cyclicSquare` (`tr(g₀g₁g₀g₂g₁) = z · tr((g₁g₀)²)`), and
`cyclicSquare_cross_term_neg_convD` (the cross term is `< 0` for real `q > 0`).

**What the prune says.** A cross term is produced exactly when two *adjacent* generators
*alternate* — three adjacent strands braided cyclically, closure the torus knot `T(3,2)` (one
component) against the Hopf chain `gₘ² gₘ₊₁²` (three components). Re-crossing a neighbour,
reaching over it and returning, or stacking a bond as a clasp `B²` all leave the monotone trace.

**Correction of my own earlier claim, and where it propagated.** #6513 and its audit
(`2026-09-03-markov-trace-not-bond-multiplicative-n4.md`), the Lean docstring of
`MarkovTraceInterleavedCrossTerm`, the probe docstring, bean `qou-kru4` and #6561's audit all say
`n = 4` is "the smallest instance where the product formula fails". **It is not.** At `n = 3`,
content `(2, 2)`, `tr((g₀g₁)²) − tr(g₀²g₁²) = z² − hz − 1` exactly — the convention-D Markov
defect with no `z` prefactor; the `n = 4` word is that object stabilised once. `qou-ls86`'s
`n = 3` identity concerned content `(2, 1)` only. The two audit docs and the bean carry the
correction; the #6513 Lean/probe docstrings are left as records (their theorems are correct;
only the "smallest" gloss is wrong) and are named here so nobody re-derives from them.

## 3. The probe — one class, no count

`computations/probes/cyclic_triple_bond_cross_term_probe.py` (**32/32**; mpmath 50 dps; the
general-word Rust kernel `pyhecke_native.chi_lambda_all_partitions_mpfr` with per-letter
`avg_shifts` for the colour-weighted p–n letter — validated first by reproducing the production
`tr_m_atom_zn` **byte-for-byte** on ²H, ³H, ³He and ⁴He; ⁴He kernel calls cost ~8 min each and
sit behind `--full`, its closed forms are always printed).

Two facts the probe established on the way:

- **The production evaluator cannot see this class at all.** `chi_monotone_transfer.chi_all_lambda`
  raises `ValueError("non-monotone word …")`, and `reduced_block_kernel` composes the chain walk
  by construction. Monotonicity is not just what the word does — it is what the kernel assumes.
- **The closed-form factorization holds on production.** `∏ tr(run)` (each run collapsed by
  `affine_mul_affine`) equals the production `tr_M(atom)` and `tr_M(free)` to 50 dps for all four
  nuclei — `MonotoneWordTraceFactorizes.tr_affineWord`, checked on the real words.

**The modification (choice-free member of the class).** At each bond `k` the single bond letter
`B` at `3k+2` is doubled and its two crossings alternate with the last two intra crossings of
nucleon `k` at `3k+1`:

    production   … L₁L₂L₃L₄ · B     · suffix
    hopf-clasp   … L₁L₂L₃L₄ · B B   · suffix        (same content as cyclic, monotone)
    cyclic       … L₁L₂L₃ · B · L₄ · B · suffix     ((g₃ₖ₊₁ g₃ₖ₊₂)²)

Predicted by `cyclicSquare_cross_term` + multilinearity in the affine letters, and **confirmed
by the kernel to 50 dps at every bond of ²H, ³H, ³He**:

    tr(cyclic) − tr(hopf-clasp) = b(L₁L₂L₃) · (z² − hz − 1) · tr(prefix) · ∏ tr(suffix runs).

Binding law: the production `binding_canonical`, `B = Q_β(n) · (tr_M(free) − tr_M(atom))`,
`Q_β = 0.78233 MeV`. AME from `codata_constants.ame_binding_mev`.

### Result (proton pin, convention D)

| nucleus | `B_prod` | `B_AME` | residual | ΔB per bond, pure interleaving (left) | Σ all bonds cyclic | % of residual |
|---|---:|---:|---:|---|---:|---:|
| ²H | 0.4354 | 2.2246 | **1.789** | +0.779 | **+0.779** | 43.5 % |
| ³H | 0.6951 | 8.4818 | **7.787** | +0.310, +0.401 | **+0.711** | 9.1 % |
| ³He | 0.6986 | 7.7180 | **7.019** | +0.453, +0.547 | **+1.000** | 14.2 % |
| ⁴He | 0.8761 | 28.2957 | **27.420** | +0.181, +0.218, +0.281 | **+0.680** | 2.5 % |

(MeV throughout. "Pure interleaving" is cyclic-minus-hopf-clasp, the part the Lean theorem
prices. Doubling the bond alone *lowers* B by 0.11–0.45 MeV per bond: a two-crossing clasp binds
less than a single crossing under this law. The mirror variant — alternating with nucleon
`k+1`'s first two crossings, numeric only — is 0.32–0.36× the left one at every bond.)

## 4. Verdict — scope-(a) negative, and why it is structural rather than numerical

1. **Right sign, wrong size.** The cross term binds (every kernel check `tr(cyclic) < tr(hopf)`
   passes), but the total for all bonds is 0.7–1.0 MeV against residuals of 7–27 MeV.
2. **Wrong direction in `A`.** The total *falls* from ³He (1.00 MeV) to ⁴He (0.68 MeV) while the
   residual *rises* from 7.0 to 27.4 MeV. This is not a coefficient to be found: the cross term is
   `(z² − hz − 1) · tr(prefix) · ∏ tr(suffix)`, and every factor in that product is a sub-unit
   letter trace, so the term is **multiplied down by the rest of the nucleus**. It is intensive
   in exactly the sense `qou-brng`'s frontier note gives for every bond-graph route: "no per-block
   weight converts an intensive quantity into an extensive one". Here the block is the whole
   word and the weight is a reorder.
3. **Law-dependence, stated.** Under a logarithmic binding law (the `qou-y0mc` `S`-vs-`H`
   ambiguity is open) the same reorder would read as 2–4 nats per bond — because the cyclic
   trace is driven close to zero (`0.0079` at ³H bond 1), not because of any extensive
   mechanism. A near-zero trace under a log law is a fragility, not a result; recorded so nobody
   reads it as one.

So: **the word-level route to the collective term is closed for this class**, and the reason
is the same intensive/extensive gap the bond-graph routes died of. A cross term in `tr_M` of a
single word cannot be the extensive object; it inherits the product structure it is a
correction to.

## 5. What this does not exclude (honest scope)

- **The cyclic coordination graph at `A ≥ 3`** (three nucleons mutually bonded). On the linear
  strand layout the closing bond needs a band generator with an over/under choice the algebra
  does not make; not probed. Its cross term would still be a multiplicative correction to a
  product of sub-unit traces, so the scaling argument in §4.2 applies to it unchanged — that is
  an argument, not a measurement.
- **The intra-nucleon cyclic square** — the three strands of one nucleon braided cyclically (the
  Borromean/`T(3,2)` shape, which is what the corpus's proton carrier `(σ₁σ₂⁻¹)³` actually is).
  It changes the nucleon, not the bond, so it is not a binding term and was not probed.
- **A different binding law.** §4.3.

## 6. Options for the author (default first; recommendation is judgement)

- **Default — nothing changes.** Production words stay monotone; the class is recorded as closed
  at scope (a) with the mechanism named. Cost 0.
- **Stop looking inside `tr_M` for the extensive term.** Four bond-graph routes (`qou-brng`) and
  now the only word-level route all die of the same intensive/extensive gap. The honest reading
  is that the collective term is *not a functional of the single atom word's Markov trace*. This
  is the recommendation, marked as judgement: it does not say what the term is, it says where
  it is not, and it is consistent with every closure on the record.
- **Resolve `qou-y0mc` first** if anyone wants to revisit §4.3 — the law decides whether a
  near-zero trace is 1 MeV or 3 nats, and no word-class result is interpretable until it does.

## 7. Verification

- Lean: `lean`-direct exit 0 on `RevisitClassCrossTerm.lean`; eight declarations axiom-clean;
  zero `sorry`. `MonotoneWordTraceFactorizes.lean` re-verified after a docstring-only edit.
- Probe: 32/32; four of the checks are direct numerical instances of the four Lean theorems
  (`n = 3` cyclic square, `n = 3` one-step revisit, `n = 4` climb-and-back, `n = 4` = `z ×`
  cyclic square).
- Precision preflight: `scripts/precision-gates.sh --changed` run on the new probe (result
  recorded in the PR body); no witness is emitted by this probe.
- Repo CI is `workflow_dispatch`-only; this agent verification is the gate.

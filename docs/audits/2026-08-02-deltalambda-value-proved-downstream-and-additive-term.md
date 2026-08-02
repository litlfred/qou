# Δ_λ value proved — downstream implications, wiring status, and where the missing additive term comes from

**Date:** 2026-08-02 · **Epic:** `qou-r2nh` (Δ_λ arc) · **Tier:** analysis / coordination
(no fit, no AME inversion, nothing wired to production in this doc).

Consolidates the just-merged Δ_λ arc (#4553 → #4574 / #4580 / #4581 / #4586)
with a corpus + compute audit of what the proof unblocks, what it does **not**,
and the honest state of the missing many-body binding term — including the
owner's "charm side?" question.

---

## 0. TL;DR (three sentences)

1. **Proved (sorry-free, general-n):** the per-partition binding **value**
   `Δ_λ = (-1)^{n(λ)}·dim V_λ` (signed Springer dimension) — sign = jet-order
   valuation parity, magnitude = Wedderburn dimension, both substrate-derived.
2. **Still open (external / separate):** (a) the single-degree **geometric
   concentration** that would name that value a Behrend-signed DT count — proved
   to need an *external* Springer-geometry input, not forceable from the
   substrate weights (`y_λ` is the q-Plancherel measure, not a Green function);
   (b) the **many-body binding magnitude** — the deuteron/light-nucleus
   `r* ≈ 1.585` deficit — which is what all six ansätze *actually* failed, and
   which the value proof does **not** touch.
3. **The missing piece is an additive, non-normalized, irreducibly ≥3-body
   extensive term** — provably *not* a per-block Δ_λ reweight and *not* the
   pairwise log-det cumulant; **charm/heavy-flavor is a category error** for it,
   though the *higher-representation* instinct is correct (nuclear spin-isospin
   SU(4), not quark flavor).

---

## 1. What the arc proved — and the framing correction

| Claim | Status | Lean |
|---|---|---|
| `Δ_λ = (-1)^{n(λ)}·dim V_λ` value, n = 5 anchor | proved | `DeltaLambdaDTIndex.lean` (#4553) |
| same, **general n** (no n ≤ 5 restriction) | proved | `DeltaLambdaDTIndexGeneralN.lean` (`dtEulerG_eq_deltaLambdaG`) |
| same, unconditional capstone (value + chirality sign) | proved | `DeltaLambdaGeneralNUnconditional.lean` (`dtEuler_eq_deltaLambda_unconditional`, #4580) |
| no *count* / *SDP* / *valuation* route forces the concentration | proved | `DeltaLambdaDTModuliUnderdetermined` / `…TopDegreeConcentration` / `…JetOrderDegreeSelection` (#4574) |
| no *algebraic grading* forces it (unified CANCELLATION) | proved | `DeltaLambdaGradedConcentration.lean` (#4581) |
| the concentration input is **external Springer geometry** | recorded | `RossmannCCBridge.lean` + audit `2026-08-02-rossmann-cc-bridge-…` (#4586) |

**Framing correction (governs everything downstream).** The "Δ_λ gate — six
ansätze failed on the deuteron" was **never about the per-partition value**. The
six ansätze (Frobenius co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius,
crystal-graph, augmented Markov) failed to derive the **many-body magnitude
scalar** `r* ≈ 1.585` (the deuteron `C_knot` deficit). So the correct new status
everywhere is:

> **Δ_λ value proved (signed Springer dimension, general-n, sorry-free);
> geometric concentration + many-body magnitude external.**

Do **not** rewrite any status note to "gate closed" — that would be the
"sorry-free ≠ derived" error. The magnitude and the concentration are both still
open.

---

## 2. Downstream wiring status — the one concrete unblocked step

Every production consumer is currently **gate-open / unavailable**:

- `computations/binding_K_direct.py` (`load_delta_lambda`, L141–178) reads
  `delta_lambda_per_atom` from `delta-lambda-witness.json` — **that witness does
  not exist**, so every atom flags `delta_lambda_unavailable`. The consumer is
  wired and waiting.
- `computations/binding_energy_categorical_deuteron.py` L96 `status =
  "delta_lambda_gate_open"`; `C_knot = 5.852` is explicitly labelled a fit.
- Appendix `appendix-mass-binding-algorithms/mba-sidecar-delta-lambda-closure.*`
  — `status: "experimental"`, script `option_e_v9_all_symmetries.py`, tag
  `open-gate`.
- `conj:binding-manybody-eq-jet-filtration` — blocked by the **magnitude / R(q,x)**
  leg, which the value proof does not touch.

**The single unblocked action:** emit `delta-lambda-witness.json` with
`delta_lambda_per_atom = (-1)^{n(λ)}·dim V_λ` from the proved closed form
(general-n), moving `binding_K_direct.py` off `delta_lambda_unavailable`. This is
**derivation-legal** (the value is proved from the drivers, not fitted). It does
**not** produce accurate binding — the magnitude scalar `r*` stays a separate
open input; the witness must say so.

---

## 3. Stale status notes to amend (value proved; keep magnitude/concentration open)

Amend — do **not** delete — the "open gate / six ansätze failed" wording in:

1. `AGENTS.md` §"Δ_λ gate" (~L910–916) — annotate "VALUE now proved general-n;
   anti-fit magnitude rule still stands."
2. `content/…/appendix-mass-binding-algorithms/mba-sidecar-delta-lambda-closure.md`
   (L1, 17, 60) + `.ts` (L5 title, L13 status, L19 tag).
3. `…/appendix-mass-binding-algorithms/mba-step09b-per-isotope-binding.md` (L33).
4. `…/appendix-mass-binding-algorithms/mba-intro.md` (L13 legend).
5. `…/mass-theory/binding-manybody-jet-filtration.md` (L53) — cross-ref the value proof.
6. `content/…/lean/QOU/BraidKnot/DeltaLambdaRefutation.lean` (L8–11) — header prose
   "enforced only by reviewer vigilance" is now dated (value is Lean-proved).
7. `docs/precision-goals.md` (~L311–319) + `docs/audits/2026-07-13-delta-lambda-gate-open-for-all.md`.
8. `docs/coordination/option-e.md`, `docs/coordination/delta-lambda-magnitude-derivation.md`,
   `docs/audits/2026-07-05-delta-lambda-gate-status.md`.
9. `computations/binding_energy_categorical_deuteron.py` (L96 note).

Beans closeable (value leg): `qou-f0ny` (DT→value), `qou-r0xk` (general-n (†),
now proved via `aStat_eq_sumChoose2_conjugate`), `qou-dr7h`. Keep OPEN: `qou-7ygi`
(concentration external) and the magnitude beans.

---

## 4. Where the missing additive extensive term comes from

**Two proved constraints bracket it:**

- **Intensive proof** (`2026-06-02-binding-intensive-vs-extensive-derivation.md`):
  the trace binding `B = E₀·Δtr_M` saturates (~3–4 MeV, 1.65× A-growth vs 12.72×
  needed); *"no per-block weight Δ_λ can convert an intensive quantity into an
  extensive one"* — the missing object is an **additive extensive term**.
- **Pairwise-cap proof** (`2026-07-18-deltalambda-saturation-det-ceiling.md`):
  the isospin-even log-det cumulant `b_A = −ln det(I + m·G_A)` saturates but is
  **capped** `ρ_A ≤ C(A,2) = A(A−1)/2` for all m; strong targets
  (`ρ_strong(4) ≈ 13 > 6`) exceed it robustly ⇒ the missing term is
  **super-pairwise** (irreducibly ≥3-body).

**The framework already localizes it — the inter-nucleon channel.** The
`conj:inter-nucleon-channel-color-tube` diagnostic: per-isotope error correlates
with inter-nucleon **arc count** at `R² = 0.83` (vs signed-h weight `R² = 0.26`)
— the extensive `∝ A` signature. The arc structure (A−1 inter-nucleon Hecke
generators) is the extensive backbone; the color-tube weight `W_{c₁c₂}` (now
**derived**, 8→0 free params, `2026-08-01-color-tube-weight-fully-determined.md`)
fixes the *p/n asymmetry / sign*, **not** the extensive magnitude.

**The magnitude `r* ≈ 1.585` is bracketed out of every single-Markov-trace
route** (Borromean 3-body cluster near-misses at 0.63×; sub-link channel sum
[Brunnian wall]; operator-branching ≡ scalar trace; Vassiliev/finite-type;
Habiro fibre; geometric `W_λ` overshoots ~30×). What survives is genuinely
**cross-channel / non-normalized**:

| Surviving candidate | Why it survives | Ledger |
|---|---|---|
| **Non-normalized extensive generating kernel** — q-Gaussian `S(m)=Σ dim_q(λ)` + Habiro tower (`z2bn`) | both anchor proofs point here ("additive, non-normalized weighting"); structure pinned, magnitude downstream | option-e.md:248–263 |
| **Operator-valued cross-channel / super-Berezinian cross-sector** | the *only* A=3-magnitude route not excluded (reaches O(1)); currently a fit unless `B,C` derived from the DM q-cubic period (`qou-jqof`, open) | option-e.md:877–903 |
| **Whitehead-chain higher-volume object** (Vol=4G, positive-sum) | fresh 2026-08-02; irreducible ≥3-body enhancement of the single 3-body trace | `2026-08-02-whitehead-chain-positive-sum-route.md` |
| **Weighted isospin-even determinant** (Perron eigenvalue → 1 breaks `C(A,2)`) | named as "what would move it" in the cap audit; no construction yet | `2026-07-18-…-det-ceiling.md:190–197` |

Genuine higher-representation super-pairwise object in binding: **Wigner
spin-isospin SU(4)** — the `[1⁴]` α-cluster antisymmetrizer (trace `= C(4,A)`,
zero for A>4 → ⁴He doubly-magic locality, `SU4SupermultipletGate.lean`). This is
*nuclear* spin-isospin, **not** quark flavor.

---

## 5. The charm / heavy-flavor hypothesis — category error (with the right qualification)

**Charm does not enter nuclear binding anywhere in the corpus.** Where charm lives:

- **`𝔠` (charm) = a torus-knot mass label** — `T(2,7)`/`7₁`
  (`knot-notation-convention-table1-data.md:9`), a *single-particle mass* in the
  heavy-flavor spectrum. Notation-mandated distinct from color `c`.
- **`flavor-dressing-functor.md`** restricts to the doublet `{𝔲,𝔡}` and leaves
  heavy-flavor `μ_q` **explicitly undetermined** (L14) — forward-compatibility
  placeholders.
- Strange/hyperons appear **only** in the dense-matter / neutron-star sector
  (color-superconductivity, strangelets), never in light-nucleus binding.

**Why charm-as-additive-term is a category error here.** The framework derives
masses from **knot/Hecke categorical data**, not a QCD flavor Lagrangian. A
`T(2,7)` charm knot is a single-particle mass label carrying no coupling into the
`{u,d}`-only inter-nucleon trace; to make it supply the A≥3 extensive term one
would have to (a) assign `μ_c` (open) and (b) invent a heavy-flavor→SU(4)-binding
coupling with **no categorical home**. That is importing QCD-flavor intuition
into a theory that does not represent nucleons as containing dynamical charm.

**The correct reading of the instinct.** In the binding sector "flavor" means
**nucleon flavor = isospin** (p/n), and the higher-representation object is the
**spin-isospin SU(4) supermultiplet** — the genuine "higher rep" super-pairwise
term (the α-cluster antisymmetrizer). There is also a color↔flavor swap
(`c-from-color-flavor-swap`), but it is **charge conjugation C on `{u,d}`**, not
charm. So: right instinct (an internal higher-representation sector supplies the
term), wrong particle (spin-isospin SU(4) + a non-normalized cluster kernel, not
QCD charm).

---

## 6. The shared s5-so3 keystone

`conj:s5-so3-fiber-action` is the joint bottleneck: it supplies **both**
(a) the color-tube weight `W_{c₁c₂}` (the p/n-asymmetry structure of the
inter-nucleon channel) and (b) is the same keystone the Δ_λ concentration
frontier is framed against (`S5SO3FiberAction.lean` / `RossmannCCBridge`).
Closing it advances the many-body channel and the per-partition realization at
once. In scope for all agents (2026-07-11 general reversal); the anti-fit
discipline still gates *how*.

---

## 7. Next steps (beaned)

- `qou-l39s` — emit `delta-lambda-witness.json` (proved value) + appendix sync
  (value-proved wording; magnitude/concentration kept open).
- `qou-i8oq` — land the Lean proof of the `ρ_A ≤ C(A,2)` pairwise cap
  (deferred on disk-space in the 2026-07-18 audit) → cements super-pairwise.
- `qou-0c19` — localize the additive term to the inter-nucleon channel; test the
  A=4 color-tube magic-shell saturation.
- `qou-zcjg` — the shared s5-so3 keystone.
- `qou-q6lw` — charm assessment: **category error** (this doc §5).
- `qou-kkds` — this referee-facing write-up.

## References
- Merged Lean: #4553, #4574, #4580, #4581, #4586 (`QOU/BraidsAndKnots/DeltaLambda*`, `RossmannCCBridge`).
- `docs/audits/2026-06-02-binding-intensive-vs-extensive-derivation.md`
- `docs/audits/2026-07-18-deltalambda-saturation-det-ceiling.md`
- `docs/audits/2026-08-02-rossmann-cc-bridge-deltalambda-realization.md`
- `docs/coordination/option-e.md` (magnitude-route ledger)
- `content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md`

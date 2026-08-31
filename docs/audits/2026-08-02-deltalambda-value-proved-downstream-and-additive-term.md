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

**~~The framework already localizes it — the inter-nucleon channel.~~
🛑 RETRACTED 2026-08-30 — the cited diagnostic does not say this.** The paragraph
below stood here and should not be relied on; it is kept struck through because
it was quoted onward into bean `qou-0c19`'s title and into
`brings-surface/inter-nucleon-channel-color-tube.md:34`.

> ~~The `conj:inter-nucleon-channel-color-tube` diagnostic: per-isotope error
> correlates with inter-nucleon **arc count** at `R² = 0.83` (vs signed-h weight
> `R² = 0.26`) — the extensive `∝ A` signature.~~

**What the cited source actually records.**
`computations/low-isotope-sign-flip-diagnostic.witness.json` contains no `0.83`
anywhere. Its two fits are `err_pct ~ n_inter` at **`R² = 0.2653`** and
`err_pct ~ signed_h` at **`R² = 0.0018`**, over **n = 5** nuclei of which the two
`A = 1` rows are anchors with `|err_pct| < 10⁻³`. Its own recorded verdict is
*"**WEAK** correlation between err_pct and inter-nucleon channel counts/weights.
Sign-flips are **NOT** explained by simple linear channel models."* — the
opposite of the conclusion drawn from it here. Note also that the `0.26`
attributed above to *signed-h* is, to three digits, the witness's *arc-count*
value.

**And the claim as written was degenerate anyway.** Read as the "extensive `∝ A`
signature" — i.e. on absolute error — it cannot discriminate, for two exact
algebraic reasons: `R²` is invariant under scaling the response, so a model short
by a constant *fraction* gives `R²(err ~ X) = R²(B ~ X)` for every `X`, and
`R²(B_AME ~ arc) = 0.9943` on the 2449 AME2020 nuclei with `2 ≤ A ≤ 240` with no
model at all; and `R²` is invariant under affine reparametrisation of the
regressor, so `arc = A − 1` scores *exactly* what bare `A` scores. (That second
argument applies to the absolute-error reading used in this audit and in the
bean; the witness itself fits *relative* error, for which a constant fractional
shortfall has zero variance — the two readings are kept separate in the probe.)

This does **not** refute `conj:inter-nucleon-channel-color-tube`, which may hold
on the categorical argument; it removes the empirical evidence cited for it here.
The clone used is shallow, so an earlier version of the witness carrying `0.83`
cannot be excluded — the statement is about the witness as committed today, which
is what a reader following the citation finds. Probe:
`computations/probes/arc_count_diagnostic_degeneracy_probe.py` (6/6).

The arc structure (A−1 inter-nucleon Hecke generators) is still the extensive
backbone as a *structural* statement; the color-tube weight `W_{c₁c₂}` (now
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

## 5. The charm / heavy-flavor hypothesis — NOT a category error (owner correction, 2026-08-02)

An earlier draft of this section called charm-as-additive-term a "category
error." **That was wrong**, and the owner's free-vs-bound argument corrects it.
The refined, corpus-grounded position:

**Free charm carries zero volume — and that is the point.** `𝔠` (charm) `= T(2,7)`
/ `7₁` is a **torus knot**: Seifert-fibered, non-hyperbolic,
`Vol(S³∖T(2,7)) = 0`, and (per
[`bring-hyperbolic-knot-bloch-decomposition.md`](../../content/quantum-observable-universe/predicted-spectra/bring-hyperbolic-knot-bloch-decomposition.md))
it contributes **zero to the Bloch-Wigner image** — "only mass-bearing knots
carry Bloch-Wigner content." A free torus knot's invariant is the **Chern-Simons
functional, not the hyperbolic volume**
([`chern-simons-as-knot-invariant.md`](../../content/quantum-observable-universe/predicted-spectra/chern-simons-as-knot-invariant.md),
[`em-coupling-chern-simons.md`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.md)).
This is the framework's *own* statement of the physical fact the owner named:
**charm has no directly-observable free mass.**

**Bound = composed torus operators DO acquire hyperbolic volume — the framework's
actual mass mechanism.** The same block states: "The Bloch group is generated by
the normal-form elements **and the torus-knot operators `T_{m,n}`**. Iterated
composition reaches every corresponding Bloch-Wigner value," via closures
`b_i · β(T_{m,n}) · b_j`. So a torus operator (Vol=0 free) **composed** in the
Hecke algebra closes to a **hyperbolic, volume-bearing** knot — nonzero
Bloch-Wigner = observable mass. This is exactly the owner's mechanism:
*bound charm hyperbolizes*; you see it only through the composite, ending (on
decay) in charm + an observable partner.

**Consequence for the additive term.** The inter-nucleon channel *is* a
composition (gg-production) channel, so torus-operator / heavy-flavor content can
in principle contribute hyperbolic **volume** (= binding) there. This **upgrades**
the charm hypothesis from "category error" to a **live mechanism with untested
magnitude**.

**Honest skepticism (magnitude, not mechanism).** The *leading* inter-nucleon
demand channels are generated by the **light** torus operators
(`T_{1,0}, T_{2,1}, T_{2,2}, T_{2,3}, T_{2,5}` for `H_3` — same block); charm
`T(2,7)` enters only at higher `n`, so **charm specifically is likely
subleading**. But the *general* mechanism — **torus-operator composition →
hyperbolic closure → Bloch-Wigner volume → binding** — is precisely the right
shape for the super-pairwise additive term, and is un-refuted. The right probe is
therefore not "does charm bind" but: **compute the Bloch-Wigner volumes of the
inter-nucleon composition closures `b_i · β(T_{m,n}) · b_j` and test whether they
supply the missing `∝A` magnitude** (bean `qou-q6lw` re-scoped; new probe bean).

**Also legitimate (orthogonal, nuclear side).** In the binding sector "flavor"
also means **nucleon isospin** (p/n), and the **spin-isospin SU(4)
supermultiplet** (α-cluster antisymmetrizer) is a genuine higher-rep
super-pairwise object. So there are two internal-sector routes — the torus-operator
Bloch-Wigner route (above) and spin-isospin SU(4) — not one; the owner's
heavy-flavor instinct picks out the former.

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

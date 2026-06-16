# Q_β residue-A — the per-block collapse-order test (S2 + S3): research scope (2026-06-05)

## Status: owner-authorized exploration (strategy S2 + S3)

Owner directed exploration of the canonical-derivation cheat-sheet **§9.2
"unused lever"**: the scalar Markov trace

$$\mathrm{tr}_M \;=\; \sum_{\lambda \vdash n} y_\lambda\,\chi^\lambda$$

**collapses the per-block content at step 5 — *before* the archimedean functor
`τ` at step 9.** The cheat-sheet's guiding principle is *"stay in the fibre as
long as possible, observe last."* This doc scopes the **unique, non-duplicative**
test of that lever for the Q_β `c_3` residue-A. It is **scope only** — no result
claim, no fit; the compute is for a focused session.

## 🟢 Owner-confirmed (2026-06-05): the coherent-collapse cancellation IS the mechanism

> **🔴 UPDATE 2026-06-06 — REFUTED by the heavy per-λ probe (the negative branch this falsifiable design anticipated).**
> The test below was run — [`qbeta_perlambda_collapse_cancellation_probe.py`](../../computations/qbeta/qbeta_perlambda_collapse_cancellation_probe.py),
> verdict [`2026-06-05-qbeta-perlambda-collapse-cancellation-refuted.md`](../audits/2026-06-05-qbeta-perlambda-collapse-cancellation-refuted.md).
> **Result: NO cancellation.** The per-λ n↔p contributions are all the **same
> sign** (every `Δχ^λ < 0`, every Wenzl `y_λ > 0`), so `cancellation_ratio = 1.0000`
> under **both** Plancherel and canonical-Wenzl weightings: `coherent = incoherent`,
> observe-last recovers **nothing**. The `c_3` order gap is therefore **NOT** a
> collapse artifact — the amplification is the genuine **f-map / anchor-dependent
> brane-tower level** `ℓ(K,q₀)` (#1887's surviving possibility; #1900's kernel).
> **What STANDS** (independent of this refutation): the bar-parity results
> (`h=2 sinh η` bar-odd, `c_3` = odd-sinh sector), the **Φ₂ = bar-odd
> reconciliation**, and the **binding A≥3 `θ_λ`** application (a *different* object —
> the per-block Reeb phase, not the n-p character difference). The §9.2
> "observe-last" *principle* is untouched; only its specific `c_3`-via-collapse
> *application* is refuted.

The owner confirmed that the **cancellation imposed by the coherent scalar
collapse** `Σ_λ y_λ χ^λ` — *not* an external f-map — is the long-sought source
of the `c_3` order gap ("this is what I have been pushing at"). This promotes the
§9.2 lever from a posed question to the **load-bearing hypothesis** of the
residue-A program.

**Unification — the same lever is the A≥3 binding gate (§9.3).** The identical
coherent collapse is the open frontier on the *binding* side: the scalar trace
collapses the per-block q-Reeb phase `θ_λ` before observation, and A≥3 absolute
binding needs the **un-collapsed** per-λ vector (`binding_reeb_phase_decomposition.py`
already emits it). So *"don't collapse coherently / observe last"* is **one**
structural lever across the framework's two open frontiers — Q_β `c_3` (this doc)
and A≥3 absolute binding (cheat-sheet §9.3). A positive result here is direct
evidence for the same fix there; a negative result constrains both. This is also
the same cut as `Im(q)` discipline, `prop:delta-pre-archimedean`, and the
fibre-vs-observable wall — all instances of *"preserve information until
observation."*

## What the active siblings already settled (build on, don't repeat)

| Sibling | Established | Consequence for this test |
|---|---|---|
| **#1887** (Reeb-sinh parity) | **Lean-proved**: `cosh(kη)` bar-EVEN, `sinh(kη)` bar-ODD ⇒ only the `sinh` term can source the first bar-antisymmetric coefficient `c_3` (S3). The scalar Reeb-`sinh` matches `c_3`'s **sign** but is `O(1)` vs `dc_3/dη ≈ 4.26e6`. **f-map `sinh(ℓη)/u^k` REFUTED**: the swing-lock identity ⇒ no fixed-ℓ closed-form f-map absorbs the `c_3` cross-anchor swing. | S3 (bar-odd localization) is **done**. The scalar amplifier is **refuted**. The amplification is *not* a closed-form scalar f-map. |
| **#1742** (bar-pairing binding) | The archimedean **observation stays `|χ^λ(q₀)|`** (Im(q₀)=0), **not** the mirror bar-pairing (which underbinds −70%). **~half the Wedderburn channels are *growth* channels** (`χ(q₀)·χ(q₀⁻¹) < 0`, the arccosh/hyperbolic regime). The bar is a **fibre-only** tool. | The per-λ structure carries a **rotation/growth sign split** that the scalar `Σ_λ` mixes. Observe-last must use `|χ^λ(q₀)|` per block — never bar-ify the observation. |
| **#1839** (residue-A kernel) | **C-finite recurrence** engine for the `c_k` (Lean, sorry-free): `c_n = -(q₀)⁻¹ Σ_j …`. | The per-λ generating structure should reproduce this constant-recursion; a per-λ source must be consistent with it. |
| **#1521** (α_EM Habiro) | `[2]_q·(1−h²α)` **is** a closed fermion-loop in the fundamental rep — a fibre-level Habiro element. | The residue-A element is the analogous **bar-odd** fibre object; `α_EM` is the bar-even template. |

**Net:** S3 is proved, the scalar f-map is refuted, the observation is pinned to
`|χ^λ(q₀)|`, and the per-λ channels carry a rotation/growth sign split. The one
thing **no sibling has tested** is whether the **collapse itself** is the source
of the order gap.

## The unique test — does `Σ_λ` *cancel* the `c_3`-carrying order?

PR #1593's ε-order gap: the scalar per-block `Δtr_M` sits at `O(√u)·ε¹`, the
ladder `c_3` at `u³·ε⁶`. #1887 showed the bridge is **not** a closed-form scalar
f-map. The §9.2 lever proposes a different origin for the gap entirely:

> **Hypothesis (falsifiable).** The per-λ summands
> `y_λ·[χ^λ(𝓑_n) − χ^λ(𝓑_p)]` contain order-`u³` (ε⁶) components that **cancel
> in the scalar sum** `Σ_λ` — because the rotation channels and growth channels
> (per #1742's sign split) carry opposite-sign higher-order terms — but
> **survive** if `τ` acts **per block** (via the per-λ q-Reeb phase
> `θ_λ = arccos(χ^λ/d_λ)`, or per-block `|χ^λ(q₀)|`), summed *after* the
> nonlinear step.

- **If the `u³ε⁶` component exists per-λ and cancels in `Σ_λ`:** the collapse
  **is** the artifact. Observe-last (per-λ `θ_λ` or `|χ^λ|`, then sum) recovers
  `c_3` at the right order **with no fitted amplifier** — a genuine mechanism,
  and exactly the "observe last" the cheat-sheet predicts.
- **If no per-λ `u³` component exists:** S2 is **refuted** as the order-gap
  source; the amplification is genuinely elsewhere (consistent with #1887's
  brane-tower refutation). A clean negative that closes the lever.

Either branch is a *derive-or-refute* structural result, not a curve fit.

## The exp(kη) refinement — `c_3` is the odd-`sinh` sector (owner directive 2026-06-05)

Substitute `q = exp(η)`, `η = log q₀`. The Hecke generators **are** the bar-graded
hyperbolic functions (symbolically verified):

- `h  = q − q⁻¹ = 2 sinh η` — the **bar-ODD** generator (the `c_3` sector);
- `[2]_q = q + q⁻¹ = 2 cosh η` — the **bar-EVEN** generator (the `c_2` sector);
- the two Hecke eigenvalues are `q = exp(+η) = cosh η + sinh η` and `−q⁻¹ = −(cosh η − sinh η)`.

Since every `χ^λ(β)` is a polynomial in the eigenvalues, its bar-decomposition
**is** its `cosh`/`sinh` decomposition, so **`c_3` lives in the odd-`sinh`
(odd-`h`) part of the n↔p character difference**. Confirmed: the amphichiral
torus traces `P_m(h) = cosh((2m+1)η)/(2 cosh η)` are **pure cosh** (zero bar-odd
part) — the `sinh`/`c_3` sector requires the **chiral n↔p asymmetry**, not the
symmetric knot content.

**This makes the owner's cancellation claim an explicit identity.** With each
per-block odd part written `y_λ·sinh(k_λ η)`:

| collapse mode | form | opposite-chirality blocks, equal weight |
|---|---|---|
| **coherent** (`sinh`-extract AFTER `Σ_λ`) | `Σ_λ y_λ sinh(k_λ η)` | `(y − y′) sinh` → **nulls** (#1742 rotation/growth opposite signs) |
| **observe-last** (`\|·\|` per block, THEN `Σ_λ`) | `Σ_λ y_λ \|sinh(k_λ η)\|` | `(y + y′) sinh` → **survives** |

**And it dissolves #1887's f-map obstruction.** #1887 refuted a *fixed-ℓ*
`sinh(ℓη)/u^k` and noted the survivor needs a non-trivial η-shape factor. The
observe-last sum `Σ_λ y_λ |sinh(k_λ η)|` **is** that η-shape — a weighted sum of
different-order sinhs whose effective order is η-dependent (Bessel-like), with
**no single ℓ to anchor-lock**. So the probe should expand in `h = 2 sinh η`
(not `u`), track the **odd-`h` part per λ**, and read the `c_3` cross-anchor
swing as `d/dη` of the surviving odd-`sinh` sum.

**Compute finding (mechanism probe, 2026-06-05 — `qbeta_coherent_collapse_sinh_cosh.py`).**
The generator identities above are verified exact, and the channel structure is
*sharper* than "transpose pair": the **bar-odd `sinh` content and the growth
channel both live in the `(2,1)` block** — `χ^(2,1)(σ_1) = q − q⁻¹ = h = 2 sinh η`
(pure bar-odd), with `χ·χ̄ = −h² < 0` (growth) — while **both 1-dim reps are
rotation channels** (`χ·χ̄ = 1 > 0`). So the cancellation is a
**rotation-vs-`(2,1)`-growth** effect, *not* a 1-dim transpose-pair effect.
Whether the actual `c_3` cancellation occurs still depends on the real Wenzl
weights `y_λ` and the proton↔neutron character difference — the heavy per-λ probe
(steps 1–5 below). Lean (generator level): `QOU/QBeta/CoherentCollapseSinhCosh.lean`.
Witness: `qbeta-coherent-collapse-sinh-cosh.witness.json`.

**Reconciliation with the merged `cos(Φ(u))` reframe (#1887, on main) — Φ₂ IS the
bar-odd carrier.** The merged phase reframe writes `c_2 = −Φ₁²/2`, `c_3 = −Φ₁Φ₂`.
Verified (witness §E): with **Φ₁ = √2** (anchor-independent, **swing 0 ⇒ bar-EVEN**)
→ `c_2 = −1`; and `c_3 = −Φ₁Φ₂` → −2.0693 (proton) / −2.0202 (muon), with **Φ₂'s
cross-anchor swing (0.023748) identically EQUAL to the c_3 swing** ⇒ **Φ₂ carries
the bar-ODD part**. So the trig `cos(Φ)` avatar (#1887) and this hyperbolic
`sinh/cosh` avatar are the **same object** (cheat sheet §4: `cos_q ↔ cosh`): Φ₁ ↔
the bar-even `[2]_q = 2 cosh η` sector (`c_2`), Φ₂ ↔ the bar-odd `h = 2 sinh η`
sector (`c_3`). This unifies #1887's merged result with the S2+S3 mechanism here.

## Probe design (for a focused compute session)

1. **Per-λ data over ℚ(q)** for the canonical proton `𝓑_p` and neutron `𝓑_n`
   braids, `λ ⊢ 3` = {(3), (2,1), (1,1,1)}: `y_λ(q)`, `χ^λ(𝓑_p)`, `χ^λ(𝓑_n)`,
   `d_λ`, `θ_λ = arccos(χ^λ/d_λ)`, and the rotation/growth label `sign(χ^λ(q₀)·χ^λ(q₀⁻¹))`.
   Sources: `y_lambda_wenzl_bridge.py`, `hecke_characters.chi_lambda_braid`,
   the Phase-5l.1 closed-form `χ^λ` Laurent rationals.
2. **Order expansion** of each per-λ summand in `u = b·ℏ_q²` to `O(u³)`; record
   the `u^k` coefficient **per λ** and per channel.
3. **Cancellation test:** scalar `Σ_λ y_λ Δχ^λ` order structure vs the per-λ
   structure — does a `u³` term exist per-λ that **cancels** in the sum?
4. **Observe-last variants:** `Σ_λ y_λ |χ^λ(q₀)|` and `θ_λ`-weighted forms;
   compare their `u`-order + cross-anchor swing to `c_3`.
5. **Swing-lock cross-check (vs #1887):** proton vs muon `q₀` — does an
   observe-last form carry the `0.02375` `c_3` swing **structurally**, without a
   fitted `ℓ`? (If yes, it evades #1887's fixed-ℓ refutation precisely because
   the per-λ collapse, not a scalar f-map, is the mechanism.)

## Discipline gates

- **3-calibration; NO 7th fit** — this is a structural derive-or-refute test.
- **Fibre vs observation (the whole point):** per-λ `θ_λ` / bar lives in the
  **fibre**; the observation is `|χ^λ(q₀)|` at `Im(q₀)=0` (per #1742). Collapse
  **last**; never bar-ify the observation.
- **Im(q) / regime discipline:** growth channels are `arccosh` (imaginary
  `arccos`) — keep the rotation/growth split explicit, never silently `.real`.
- **Report TIERED** (proved / near-match / fitted); nothing wired to production;
  `c_3` stays cal-anchored.

## Cross-refs

- Cheat sheet **§9.2** (the lever), **§4** (`Φ_q`/`Li_2^q` bar-parity), steps 5/6/9.
- [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) — residue A ≈ 1.804e-15.
- [`docs/scope/2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`](2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md) — parent strategy menu (this is S2+S3).
- PRs: **#1887** (bar-odd source + f-map refutation), **#1742** (observation = `|χ(q₀)|`, growth-channel split), **#1839** (C-finite `c_k`), **#1521** (α_EM Habiro), #1593 (ε-order gap), #1739 (f-map keystone).

# Step-9 binding closure — coordination ledger (flag-bearer hub)

**Flag-bearer:** PR #1871 (`claude/confident-newton-R8lIx`), 2026-06-05.
**Workplan:** [`docs/workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md`](../workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md).
**Common infra everyone rows toward (use these, do not fork):**
- Per-step status table — [`canonical-derivation-cheat-sheet.md §0/§9`](../canonical-derivation-cheat-sheet.md) (the step-9 box).
- This ledger — sibling roster + direction + report-backs.
- Watcher queues — `todos/{proof,canonical,compute,detangler}-*-queue.json`.
- Precision dashboards — `onepb-status-dashboard.witness.json` (L1), `per-observable-100x-status.witness.json` (L2).
- Anchor regression: the magic-A ⁴He **+5.87% no-fit** number is the falsification target for any ρ·A / n=4 claim.

---

## 0. The direction (which way to row)

Binding is **extensive / additive many-body**, not a per-block density (Δ_λ-as-density is dead, cheat §9.3). The closure is:

$$B(K)=\sum_n B_n,\quad \text{body-order }n=\text{jet/vertical degree }n=\lambda_{\mathrm{SW}}^{(n)},\quad B_n=m_e\!\sum_{p\in\mathcal S_c^{\mathrm{hyp}}}\!\operatorname{Res}_p\lambda_{\mathrm{SW}}^{(n)}.$$

- **Many-body series = jet-order filtration.** 2-body / 3-body / 4-body are jet orders of one generating function `G(x;q)=Σ B_n x^n`.
- **Each term = SW period = residue sum** over **hyperbolic** link-components (non-hyperbolic ⇒ Vol=0).
- **Scale rule ρ·A is OUTPUT** of the q-difference equation `G(qx)=R(q,x)G(x)` (→ Dirac/SW PDE post-τ), **not a fit**.
- **γγ / Breit–Wheeler** = the A≥3 validation channel (bar-even C-even vs bar-odd difference).

---

## 1. Sibling roster + per-PR direction (report-backs appended here)

| PR / branch | Their problem | Which way to row | Report back |
|---|---|---|---|
| **#1784** | binding-link assignment heuristic, chain-vs-Borromean | link-volume = **hyperbolic components of `λ_SW^(n)`**; magic-A `8G` is the n=4 instance — the assignment is the hyperbolicity gate (L4), not a free choice | _pending_ |
| **#1790** | 3-body joint-trace destructive (honest negative for A=3) | don't treat A=3 in isolation — it's the **n=3 term of the body-order series**; the q-difference recursion (L3) couples it to n=2/n=4 | _pending_ |
| **#1778** | all-pairs combiner, A=3 to −13% | structure the combiner as a **body-order series** (2+3+4), not flat all-pairs; this is the additive-series host | _pending_ |
| **#1839** | Residue-A kernel deepening (Lean engine, SDP-zero) | residue-A may **BE** the SW-period residue `Res_p λ_SW^(n)`; align on one residue engine (L1) | _pending_ |
| **#1789** | nuclear-binding derivation-completeness ledger | register the **SW-residue / jet-filtration** framing as the active step-9b direction; share completeness metric | _pending_ |
| **#1762** | 1ppQ roadmap + VolDensity bridge + 5-option attack | step-9a per-knot `VolDensity` wire-up is C1 here; fold the SW-residue route in as the step-9b option | _pending_ |
| **#1811 / #1880** | Q_β fibre / c_3 generating-function recurrence | same **q-difference machinery** (L3); the binding `G` and the Q_β `c_k` recursion share the Habiro kernel — reuse `R(q,x)` extraction | _pending_ |
| **#1888** (GAP-A `gap-a-path-b-lambda`) | per-atom λ(K) substrate-derivability | **adjacent axis, reciprocal cross-link established** — 3 intersection points: per-knot `Vol(K)`, per-block-vs-global density gate, bar-odd binding-difference observable | ✓ cross-linked (their ledger ↔ this) |

---

## 2. The ask to every sibling

1. **Report relevant findings here** (append a row in §1 or comment on #1871) — esp. negatives that constrain the q-difference kernel or the hyperbolicity gate.
2. **Use the common infra above** (cheat §9 step-table + this ledger), don't fork a parallel status doc.
3. **Anchor to the ⁴He +5.87% magic-A number** for any n=4 / ρ·A claim.

_Append report-backs below this line._

---

## 3. Sibling intel folded in (2026-06-05, agent scope-pull) — two sharpenings

Coordination comments posted on #1765, #1839, #1778, #1789, #1762.

**Sharpening 1 — the SW-period residue already has a zero-param form (#1765).**
The selection rule `λ(L) = (1/(c+1))·Σ_{λ⊢c+1} dim_q` reproduces the muon (c=1, exact ∀q) and proton (Family-A, c=3) anchors exactly. This **is** the SW-period residue (link components → partition rank → quantum-dim trace). Lemma **L1 is therefore not new** — it must be shown *equivalent* to #1765's rule, and the open *"why rank = c+1"* = the **body-order grading** (`c+1` = body order = jet vertical degree). #1765's planned A-polynomial saddle for ³He/⁴He = our n=3/n=4 SW periods.

**Sharpening 2 — the q-difference kernel must be FIBRE-derived, not data-extracted (#1839, #1811).**
#1839's precision-floor result `σ(c_k)=σ_R/u^k` makes c₄⁺ **unmeasurable**; #1811 shows residue-A is fibre-level and **rigid** (2.5×10⁷× scale-invariant). ⇒ **C5/L3 revised**: derive `R(q,x)` from the **fibre root-of-unity singularity structure of λ_SW**, NOT by fitting `B_n`/`c_k` data. Extraction is data-blocked above c₃ (#1880 closed that axis).

**Caveat — link-volume not 100% derivable (#1789, #1790).** The 3-body residual (~13%) is **genuine many-body** (NOT joint-trace, refuted #1790), and the link-volume superposition interface can't be fully derived. Lemma **L4** must treat the n=3 SW period as an irreducible many-body term, not a missing weight.

**Compatible/adjacent:** #1733 (r=15 q-Pochhammer ⁴He +1.79% — candidate n=4 refinement, "is r=15 structural?" open), #1808 (Markov stabilization = the body-order n:2→3 induction functor), #1811 (fibre infra + Hopf c₃ source).

---

## 4. Report-back from #2089 (2026-06-10) — per-bond kernel DERIVED (fibre-level), form bug identified

Per §2 ask. Branch `claude/derive-10A-minus-5-2026-06-10`; audits
`2026-06-10-binding-gs-filtration-multiplicative-suppression.md` +
`2026-06-10-binding-bond-graph-compute-audit-and-derivation.md`.

**Finding (positive instance of Sharpening 2).** The inter-nucleon bond's
trace kernel is **fibre-derived, not data-extracted**: each bridge crossing
`c·σ+d` contributes its Markov conditional expectation

    f_bond(q) = c·z + d ,  z = √q/(q+1)
    f_pp = z ,  f_nn = z − h ,  f_pn = z − h(½ − δ/4)

(formal q; only archimedean step is q→q₀). Validated: `∏_chain f_bond` ==
measured `tr_atom/tr_free` to 1.1e-15 on D/T/³He/⁴He. The GS NF is binomial
over bonds (`C(A−1,k)` term counts; bridges far-commute).

**Form bug (mechanism of the 5–40× undershoot).** `tr_atom = tr_free·∏f_bond`
⇒ the linear `Δtr` SATURATES (B = Q_β·Δtr bounded by ~0.78 MeV, never
extensive); the extensive invariant is `log(tr_free/tr_atom) = Σ_bonds
log(1/f_bond)` — the §1/#1762 `log|tr_M|` scale-gate observable, now
mechanistically derived. Log-ratio binding at E_0 lands 0.57–2.36× (chain) /
0.57–1.20× (complete graph) vs 4.8–39.7× linear.

**Caveat honored (§3 many-body).** Per-bond energies are substrate-fixed
(pp 2.91 / pn 3.89 / nn 5.18 MeV); the open piece is the **edge set**
(chain under-binds, complete over-binds light nuclei; D anomalously loose,
⁴He doubly-magic) — consistent with §3's "genuine many-body" residual; NOT
re-claimed as a closure, no 7th ansatz.

**Infra delivered.** Lossless per-λ χ caches D/T/³He/⁴He (matrix-M `max_dim`
cap purged — it was a silent ~1e-3 truncation; producer lossless by default),
⁴He via Rust `chi_q_via_gp` (77/77, 3.1s); ⁵Li/⁶Li in flight. Cross-posted:
#2062 (kernel handoff), #2078 (scale-gate corroboration + A=4 χ), #2090
(depth-1 Z_q kernel sibling on the c_k axis).

---

## 5. Report-back from #2612 (2026-06-23) — lever-1 selection-rule unification + coordinate

Branch `claude/bold-mendel-5994kg` (rebased onto main +119). Three Δ_λ-gate
levers worked (audit `2026-06-23-delta-lambda-three-lever-status.md`):

- **Lever 1 (kernel R(q,x)) — algebraically closed.** The depth-2 `det=1`
  kernel `R=x²−τx+1` (proved: S₅/A₅ Schur + symplectic) is generated by ONE
  selection rule `lw(c)=(1/(c+1))·Σ_{λ⊢c+1} dim_q` via the canonical q-hook
  `dim_q`: `lw(1)=1`, `lw(2)=(q+1)²/(3q)` (c=2 Hopf, **derivation-tight** —
  closes the former gate, not fabricated), `lw(3)=Family-A` (= production
  `linking_weight_family_a` bit-for-bit). `τ(q₀)=2.6424`. Producer
  `binding_selection_rule_tau_closure.py`. **Residual:** the geometric↔algebraic
  identification `a_D^(n)=lw(n−1)` = the **W_λ geometric-origin frontier of
  #2488** (SW period = selection-rule value); owner-gated DG, NOT touched here.
- **Lever 2 (edge-set).** Pauli→pp/nn-unbound formalized
  (`QOU/Hecke/PauliChannelBinding.lean`, sorry-free). Z·N count + deuteron
  magnitude still gated.
- **Lever 3 (universal-ρ).** A=3 mirror **ratio** is a ρ-free prediction
  (1.67%, no fit); absolute ρ fitted/CAL-4-gated (= the Δ_λ gate per-λ).
- **Mass + binding wiring.** `lw(c)` wired into MBA step-9a (mass linking
  weight) + step-9b (binding kernel anchors).

Coordinated (intent posted): **#2488** (keystone W_λ — my residual = their
frontier), **#2325** (parallel depth-2 b-ladder + `m_sym` log-trace match),
**#2461** (Pauli-channel — `PauliChannelBinding` cherry-pickable). Over-zealous
binding-closure prose rescoped in 6 docs
(`2026-06-23-over-zealous-binding-closure-review.md`).

---

## 6. Report-back from #2795 (2026-06-25) — the depth-2/super-exp fork SETTLED + conserved-integral Lean

Branch `claude/sw-lambda-jet-prolongation-2026-06-25` (rebased onto main +34).
Refines §5's "Lever-1 kernel R algebraically closed": the depth-2 `R=x²−τx+1`
is closed **only at n≤4** (deuteron n=2, ⁴He magic-shell n=4); the **global**
`a_D^(n)` is **super-exponential**, so the true kernel is q-Bessel, not SL₂.

- **Fork settled three ways** (audit `2026-06-25-sw-jet-prolongation-explicit-and-fork.md`,
  probe `sw_period_growth_probe.py`): (i) √-branch Puiseux `X^(n)~(z−z_k)^{1/2−n}`
  ⇒ factorial; (ii) the corpus's own `prop:sw-period-residue-sum` — residues =
  per-block Wedderburn `dim_q` ⇒ `a_D^(n)=Σ_λ dim_q = lw` (the §5 selection rule,
  stated by the corpus); (iii) the Lean below. lw vs depth-2 split hard at n≥6
  (13.56 vs 11.62).
- **Jet-form caveat RESOLVED from corpus** (corpus-grep over-flag): `λ_SW^(n)` is
  a meromorphic 1-form (`prop:sw-period-residue-sum`); `prop:mi-sw-abelianisation`
  bridges the fuller `J^n` MI∫ tensor to the 1-form period.
- **Lean keystone** `prop:sl2-period-conserved-quantity` (content-block,
  `QOU.Mass.sl2Invariant_succ`/`_eq_zeroth`, sorry-free, generic `[CommRing R]`):
  the depth-2 recurrence's **conserved first integral**
  `H_n = a(n+1)²−τa(n+1)a(n)+a(n)²`, `H_n=H_0`. A super-exp period has `H_n→∞`
  ⇒ no first integral ⇒ **no depth-2 recurrence** — the formal reason the SL₂ τ
  is the n≤4 germ. Verified lean-direct exit 0.

Coordinated (intent posted): **#2800** (`lever1-keystone-na-stokes-3b` — parallel
Lean: their `BindingHyperbolicRecurrence`/`BindingJacobiAngerBridge` `τ²−4` conic
is the level-set side of my `H_n` invariant; no file collision content-block vs
`QOU/Mass/` lib; consolidation question = who proves the orbit integral, posted).
**#2793** (τ [2]_q assembly — coordinated 3×, Lean-landing noted). The geometric
origin `a_D^(n)=lw(n−1)` (= SW period ≡ selection-rule value) remains the
**#2488 W_λ DG frontier**, owner-gated, untouched here.

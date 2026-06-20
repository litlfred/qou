# A∈{5,6,7} atom→knot rule via SDP — workplan (2026-05-29)

## The gap

The canonical Σ y_λ·χ^λ mass pipeline stops at ⁴He because **A≥5 has
no derived atom→knot rule** (`mass_sweep_wiring_status.py`: 5Li/6Li/7Li
= `gap`). The light atoms that *are* wired use **census-assigned**
knots — D=6₂, T=8₁₁, ³He=L6a4 — which the discipline forbids ("no
census assigned/searching, only canonical/SDP braid words", author
2026-05-24). The gating dependency is the **"R5-full SDP solver"**:
the inter-nucleon binding-operator selection that should *derive* each
atom's braid word + ν_SDP.

Targets (AME binding, MeV): 5Li 26.328, 6Li 31.994, 7Li 39.245.

## Mechanism (confirmed at the nucleon level)

`confinement-operator-selection.py` already selects the **nucleon**
binding operator (B₃ = (σ₀σ₁⁻¹)³) with **no census**: it enumerates
candidate operators (B₃, Hopf chains, trefoil), computes each one's
normal form + demand-channel satisfaction, and selects via the
Frobenius-dual / Gram-inverse minimum-action principle. Verified:
B₃ NF = +0.998·γ −0.0095·σ₀ +0.0091·σ₁ +0.046·L₊ −0.044·L₋
(net +0.9996), and it reproduces the proton/neutron NFs.

The atom→knot rule is the **same selection one level up**: which
*inter-nucleon* binding operator confines A nucleon-blocks (each a
3-strand B₃) into the atom knot, on H_{3A}.

## De-risking plan (validate before the heavy H₁₅ work)

1. **Reproduce the known light knots from the SDP, not census.** Run
   the inter-nucleon selection for D (2 nucleons, H₆): does the
   Gram-inverse/minimum-action select a braid whose closure is **6₂**
   (the census knot)? Repeat for T (H₉ → 8₁₁) and ³He (H₉ → L6a4).
   - If yes → the SDP *derives* the census assignments; extend to A≥5.
   - If no → the gap is deeper than "run at higher A"; the census
     knots themselves may be wrong (a real finding, not a wiring task).
2. **Only then** build the H₁₅/H₁₈/H₂₁ selection for 5Li/6Li/7Li.
   ν_SDP (the confinement level) comes from the SDP active set, not a
   guess.

## Compute scaling / risk

- D/T/³He validation: H₆/H₉ — tractable (seconds–minutes).
- A=5,6,7: H₁₅/H₁₈/H₂₁ — the inter-nucleon operator space grows fast;
  the SDP (not a full Markov-trace sweep) keeps it bounded, but expect
  minutes–tens-of-minutes per atom. Use the LP/SDP dual (per
  `prop:operator-selection-lp`): emit `y0_star`, `y_star`,
  `active_set`, `primal_obj`, `dual_obj`, `duality_gap` — the active
  channels ARE the selected sub-braids.

## Discipline guardrails

- **No census, no fit.** The braid word must be SDP-selected; ν_SDP
  from the active set. A 7th fitted ansatz is forbidden (AGENTS.md
  Δ_λ gate).
- Validate the SDP against D/T/³He (knowns) before trusting A=5,6,7.
- The binding scale stays E₀ = m_e/(q₀(q₀−1)) (CAL-1+CAL-2); no new
  calibration.

## First concrete step

Extend `confinement-operator-selection.py`'s selection from the
3-strand nucleon to the 6-strand deuteron interface, and check whether
the minimum-action winner's closure is 6₂. That single result decides
whether the whole A≥5 program is "run the SDP at higher A" or "the
census knots need rederiving."

## De-risking result (2026-05-29) — the gap is DEEPER

Ran the validation. **The binding-K registry's braid words are
census-hardcoded, not derived:** `binding_k_solver.py:105/117/129` set
`atom_braid_word` directly from SnapPy tables — 6₂ = [1,−2,1,1,1,−2],
8₁₁ = [−1,2,−3,…], L6a4 = [−1,2,−1,2,−1,2]. The "SDP" then evaluates
the five ρ-rules *given* these census braids; it does **not** derive
the braid from the inter-nucleon structure. So:

- D/T/³He fail "no census" **at the braid-word level** (not just ν_SDP).
- A=5,6,7 have **no braid word at all** (the registry stops at A=3).
- ⇒ the gap is not "run the SDP at higher A"; it is **derive the
  binding braid word for every A (2…7) from first principles**, with
  no census candidate set. That is the unbuilt "R5-full SDP solver".

**But a derived lead exists for D.** `binding_endomorphism_deuteron.py`
uses the **Borromean link** (Vol = 8G, a *derived* knot invariant) +
the SDP Δtr, giving **B(D) = m_e·8G·Δtr = +0.19%** — distinct from the
census 6₂. So the deuteron's binding is *already* derived via the
Borromean link; the genuine A=5,6,7 program is to **derive K_bind (the
binding link) for higher A** the same way (Borromean-class link +
Δtr), replacing the census braid words — not to extend the census
SDP. The binding scale stays E₀/8G (CAL-1 + CAL-2), Δtr from the
H_{3A} Wedderburn sum.

**Revised first step:** derive K_bind for T and ³He as
Borromean-class links (the way D uses B₃), check B = m_e·Vol(K_bind)·Δtr
against AME, then A=5,6,7. The deliverable is a derived K_bind(A) rule,
not a census table.

## Barriers to extending the registry to all nuclides

**Barrier 1 (the core one) — no derived K_bind(A) generator.** The
registry's `atom_braid_word`s are hardcoded SnapPy census braids; there
is no rule that *produces* the binding braid/link from the nuclide
(Z, N). Without it you cannot populate A≥4 without census (forbidden).
Everything else is downstream of this. The one derived hint is the
deuteron's Borromean link (Vol = 8G); whether each (Z, N) maps to a
derivable Borromean-class link is the open question (and not obvious:
"Borromean" is 3-component, the deuteron is 2 nucleons — the link is
the *interface* structure, not the nucleon count).

**Barrier 2 — Δtr at H_{3A}.** `B = m_e·Vol(K_bind)·Δtr` needs
Δtr = |tr_M(free)| − |tr_M(atom)| at H_{3A}. Computable via
`binding_canonical`/`markov_peel`, but cost grows with A (H₁₅ for 5Li,
H₂₁ for 7Li) — minutes→tens-of-minutes, and the Hoefsmit/χ^λ caches
must exist at that n.

**Barrier 3 — Vol(K_bind) for high-A links.** Even given the link, its
hyperbolic volume needs SnapPy; complex high-crossing links can be
non-hyperbolic (Seifert-fibred / satellite), where "Vol" is undefined
and a different invariant is required (cf. the meson torus-knot
Seifert-volume case). So the volume law itself may not extend.

**Barrier 4 — ρ-rule / ν_SDP derivation.** The solver evaluates *five*
candidate ρ-rules and a guessed ν_SDP (the confinement level); these
are not derived even at A=2,3 (`mass_sweep_wiring_status`: "ν_SDP
guess"). A derived selection criterion is needed before the registry
is trustworthy at any A.

**Net.** The registry can be *mechanically* extended (add rows) only if
Barrier 1 is solved — a derived K_bind(Z,N) rule. Until then, adding
A≥4 rows would just be more census (forbidden). The honest sequencing
is: (1) derive K_bind(Z,N) [the real research]; (2) it then yields the
braid words for free; (3) Δtr + Vol close the binding. Barriers 2–4 are
tractable engineering once Barrier 1 is solved.

## Barrier-1 attack — RESULT (2026-05-29): K_bind is 8G·f, not a census knot

Tested `B = m_e·Vol(K_bind)·Δtr` with the canonical Δtr (binding-canonical,
H_{3A}). The fixed Borromean volume 8G works for D (+0.19%) but fails T
(−64%) and ³He (−59%) — each nuclide needs its own Vol(K_bind). **But the
required volumes are not exotic census knots; they factor cleanly:**

    Vol(K_bind) = 8G · f(Z,N),   f = B_AME/(m_e·8G·Δtr)

| atom | Z,N | Δtr | f (AME-extracted) |
|------|-----|-----|-------------------|
| D | 1,1 | 0.5952 | **0.998 ≈ 1** (Borromean) |
| T | 1,2 | 0.8040 | **2.817** |
| ³He | 2,1 | 0.8412 | **2.450** |

`f(T) − f(³He) = 0.367` — the A=3 **mirror split** = the Coulomb energy
of ³He's two protons, i.e. #1417's `sinh(ln q) ≈ α_EM` channel. These f
match #1417's independently-measured "per-magic-closure f = 2.82 vs 2.45".

**So Barrier 1 is reframed (and the census knots were the wrong frame):**
the binding link is *universally* B₃ (volume 8G); the nuclide dependence
is a scalar factor `f(Z,N) = strong-multiplicity(A) − Coulomb(Z)`. The
open research is to **derive f(Z,N)** (bond multiplicity minus the #1417
Coulomb correction), *not* to find per-atom knots. f is currently
AME-extracted (probe `binding_factor_f_decomposition.py`,
witness `binding-factor-f-decomposition`); the factorisation + Coulomb
structure are the derived-candidate findings, f's absolute values are
the remaining target.

**This dissolves Barriers 3 (no exotic-link volumes needed — always 8G)
and reduces Barrier 1 to a scalar f(Z,N).** Remaining: derive f (the
strong bond-multiplicity + Coulomb), and Δtr at H_{3A} (Barrier 2) for
A=5,6,7. Next concrete step: does f(A) follow the inter-nucleon bond
count (D:1 bond → f=1; A=3 → f≈2.6 split by Coulomb)?

## Bond-count test (2026-05-29) — FAILS at ⁴He: f is shell-closure, not pairwise

Added a consistent 4th point (⁴He from `binding-canonical`, Z=2 N=2, same
producer as D/T/³He) and tested the pairwise-bond hypothesis
`f = pairs(A) − κ·proton-pairs(Z)`, with `pairs = A(A−1)/2`, the Coulomb
unit `κ = f(T)−f(³He) = 0.3672` fixed from the A=3 mirror, and the
deuteron fixing the bond unit. ⁴He is then a true out-of-sample test:

| atom | A | Z | pairs | f_pred = pairs−κ·pp | f_extracted | err |
|------|---|---|-------|---------------------|-------------|-----|
| D | 2 | 1 | 1 | 1.000 | 0.998 | **−0.19%** |
| T | 3 | 1 | 3 | 3.000 | 2.817 | −6.1% |
| ³He | 3 | 2 | 3 | 2.633 | 2.450 | −6.9% |
| ⁴He | 4 | 2 | 6 | 5.633 | **8.286** | **+47%** |

The deuteron is a perfect single bond (f=1, −0.19%); the A=3 mirror is
~6% low but internally consistent. **⁴He blows the law apart: f=8.29 ≫ 6
pairs (+47%).** Doubly-magic ⁴He (7.07 MeV/nucleon vs D's 1.11) binds
*collectively*, not pairwise — its f is super-additive. So `f(Z,N)` is a
**magic-shell-closure** quantity (exactly #1417's "per-magic-closure f"),
**not** an inter-nucleon bond count. The pairwise-bond model is falsified.

**Barrier-1 redirect:** derive f from the **shell/magic closure** of
(Z,N), not pairwise bonds — i.e. the Demazure sub-crystal closure level
(AGENTS.md §7b: "Demazure sub-crystals for resonances/shells") combined
with the #1417 Coulomb channel for the proton-pair split. f is **not**
fittable from 4 points (would be a forbidden ansatz); the next derived
lead is the crystal-closure count, validated against the AME-extracted
f = {D:1.00, T:2.82, ³He:2.45, ⁴He:8.29}. Probe extended:
`binding_factor_f_decomposition.py` (4 rows), witness
`binding-factor-f-decomposition`.

## A=2…7 f-sequence (2026-05-29) — the nuclear-shell signature is explicit

Extended f to **5Li/6Li/7Li** via the canonical-trace **closed form**
(`binding_canonical(use_closed_form=True)`, the Phase 5q identity
tr_M = tau_p^Z·tau_n^N·∏f_i), which reproduces the symbolic H_{3A} Δtr at
**1e-16** for the known four — so it scales to any A without the
intractable H_{3A} partition sum. f = B_AME/(m_e·8G·Δtr):

| atom | A | Δtr | f | B/A (MeV) |
|------|---|-----|---|-----------|
| D | 2 | 0.595 | 1.00 | 1.11 |
| T | 3 | 0.804 | 2.82 | 2.83 |
| ³He | 3 | 0.841 | 2.45 | 2.57 |
| ⁴He | 4 | 0.912 | **8.29** | **7.07 ← magic peak** |
| 5Li | 5 | 1.001 | 7.02 | 5.27 ← valence drop |
| 6Li | 6 | 0.944 | 9.06 | 5.33 |
| 7Li | 7 | 0.876 | 11.96 | 5.61 |

The sequence is the **textbook B/A shell closure**: ⁴He (doubly-magic,
N=Z=2) is the binding-per-nucleon **peak**; the 5th nucleon (5Li,
proton-unbound) is a loosely-bound valence particle, so f *drops*
(f(5Li)/f(⁴He)=0.85) before climbing again at 6Li/7Li. This is the
decisive confirmation that **f is a magic-shell-closure quantity**
(#1417 per-magic-closure), not any pairwise-bond or interface count —
three linear models (pair-count, interface-count, interface-type-sum)
are all falsified at the ⁴He peak (the type-sum predicts 4.27 vs 8.29,
+94% — ⁴He binds ~2× the additive value).

**Discipline caveats.** (i) D/T/³He/⁴He f validated (closed form ≈
symbolic, 1e-16); **5Li/6Li/7Li f are PROVISIONAL** — the closed form is
extrapolated to n_pp = Z−1 = 2 (two p-p interfaces), not yet cross-checked
against a symbolic H_{15}/H_{18}/H_{21} trace (Barrier-2; symbolic 5Li
validation running). (ii) f stays **AME-extracted**, not derived; with 7
points the open Barrier-1 target is concrete — reproduce the ⁴He magic
peak from the Demazure crystal closure level, **not** a fitted ansatz
(Δ_λ gate). Probe: `binding_factor_f_sequence.py`, witness
`binding-factor-f-sequence`.

## Pair-count law (2026-05-29) — f ≈ Z·N for non-magic atoms, zero free params

Testing the **simplest possible structural integer**, the count of ordered
(proton, neutron) pairs `Z·N`, against the 7 extracted f values:

| atom | Z,N | Z·N | f | f/Z·N | f − Z·N |
|------|-----|-----|------|--------|---------|
| D | 1,1 | 1 | 0.998 | **1.000** | −0.002 |
| T | 1,2 | 2 | 2.817 | 1.41 | +0.82 (unpaired nn) |
| ³He | 2,1 | 2 | 2.450 | 1.23 | +0.45 (unpaired pp, Coulomb-suppressed) |
| ⁴He | 2,2 | 4 | 8.286 | 2.07 | doubly-magic doubling |
| 5Li | 3,2 | 6 | 7.024 | 1.17 | ⁴He core + valence p |
| 6Li | 3,3 | 9 | 9.056 | **1.007** | +0.06 |
| 7Li | 3,4 | 12 | 11.961 | **0.997** | −0.04 |

**Three independent non-magic atoms (D, 6Li, 7Li) match f = Z·N within 1%
with zero free parameters.** This is *not* a fit: Z·N is the count of
ordered inter-nucleon (p,n) pairs in the canonical interface — a derived
structural integer. Deviations split into derived pieces:

- **A=3 mirror split.** T excess (unpaired nn) − ³He excess (unpaired pp)
  = 0.817 − 0.450 = **0.367 = κ_Coulomb** — *identical* to the κ
  independently extracted from B(T) − B(³He), matching #1417's
  sinh(ln q) ≈ α_EM channel.
- **⁴He doubly-magic doubling.** f(⁴He)/Z·N = 2.07: closed N=Z=2 shell
  doubles the pair count (no other atom does this).
- **5Li valence.** ⁴He core + valence p → f returns to Z·N + ε.

So the leading-order structure of the binding factor is

```
f(Z,N) = Z·N · [ 1 + (shell-closure bonus) + (mirror-split corrections) ]
```

with **all ingredients derived integer counts** — no fitted coefficients.
The remaining derivation pieces are: (a) identify which combinatorial
object on the canonical word β(Z,N) **actually** counts to Z·N (NOT the
adjacent-interface count `A−1 = Z+N−1`, which equals Z·N only at A≤3 and
diverges from it at ⁴He+; see correction below); (b) derive the
doubly-magic doubling from the Demazure crystal closure (AGENTS.md
§7b); (c) the Coulomb κ already has a derived form via #1417's sinh
channel. Probe: `binding_factor_f_pair_count.py`, witness
`binding-factor-f-pair-count`.

### Correction (2026-05-29, same day)

The prior commit message and the line above initially asserted that Z·N
"matches #1430's `(n_pp, n_pn, n_nn) = (Z−1, 1, N−1)` interface
composition". **This is wrong** — that composition sums to A−1=Z+N−1,
not Z·N. The two agree only for A≤3:

| atom | adjacent interfaces (A−1) | Z·N |
|------|---------------------------|-----|
| D | 1 | 1 ✓ |
| T / ³He | 2 | 2 ✓ |
| ⁴He | 3 | **4** |
| 5Li | 4 | 6 |
| 6Li | 5 | 9 |
| 7Li | 6 | **12** |

So Z·N is **not** the canonical adjacent-interface count. It is the count
of **all** ordered (p,n) pairs (non-adjacent included). What this means
for Barrier-1: the structural integer that f tracks at A≥4 is a *long-
range* pair count, not the local interface composition — consistent with
binding being a global rather than purely-nearest-neighbour quantity, and
with magic-closure (⁴He doubling) being a separately-quantised collective
effect. Honest record: the 1% match for D/6Li/7Li still stands; the
identification of the underlying braid-theoretic object is *open*, not
"falls out of #1430".

## ⁴He doubling factor (2026-05-29) — NOT a clean integer 2

A natural follow-up: is the ⁴He doubling factor `f(⁴He)/Z·N` exactly 2?
Computed: **2.0715, not 2 — a 3.6% deviation**. That is far too large to
be compute noise (binding-canonical Δtr matches symbolic at 1e-16, so f
is precise to ~1e-15). The "doubling" terminology was a rounded
approximation.

Tested 2.07 against natural substrate-canonical constants:

| candidate | value | err |
|-----------|-------|-----|
| 2 (integer) | 2.000 | 3.6% |
| [2]_q = q + q⁻¹ | 2.011 | 3.0% |
| 1 + q | 2.110 | −1.8% |
| 2·√q | 2.107 | −1.7% |
| π/√(π−1) | 2.147 | −3.5% |

**No candidate clears the 1% bar.** So the ⁴He doubly-magic bonus 2.07 is
*not* currently identified with a derived substrate quantity — it is the
unsolved piece of Barrier-1. The honest summary:

- **Done (1% derived)**: f ≈ Z·N for non-magic D/6Li/7Li.
- **Done (derived)**: A=3 mirror split = Coulomb κ_EM = 0.367 (#1417 sinh
  channel).
- **Open**: identify the braid-theoretic object that counts to Z·N at
  A≥4 (NOT adjacent interfaces).
- **Open**: derive 2.07 (the ⁴He shell-closure bonus). This is the genuine
  Demazure crystal-closure derivation; current best near-misses (1+q,
  2·√q) miss by 1.7–1.8% — not close enough to claim, not far enough to
  rule out a small correction.

## SDP path investigation (2026-05-30) — incomplete, not broken; a_K signal

Per author guidance "it should be obtained by SDP — all witnesses are there",
audited the SDP knot/operator selection witnesses already on disk:

- `iterative-lp-dual-h6-deuteron.witness.json` — deuteron at H_6 via the
  iterative LP-dual `u^(ℓ)*(β_D) = m_e · Σ_λ y_λ · c_ℓ(λ) · χ^λ(β_D) / [6]_q!`
- `iterative-lp-dual-levels.witness.json` — proton at H_3
- `a-K-via-lp-dual.witness.json` — `a_K` per atom (4 SDP candidates)
- `binding-K-direct.witness.json`, `binding-k-solver.witness.json` (the
  hardcoded-registry consumers; see `census-knot-audit.md`)

**Numerical state:** the iterative LP-dual sums are dramatically smaller
than the AME values they would naively be compared to:

| atom | SDP `sum_u_levels` | reference | ratio |
|------|--------------------|-----------|-------|
| proton (H_3) | 1.445 MeV | m_p CODATA = 938.272 | **−99.85%** |
| deuteron (H_6) | 0.0525 MeV | B(D)_AME = 2.225 | **−97.64%** (factor 42×) |

**Verdict: incomplete, NOT broken.** The producer's own
`interpretation` field for the proton case states verbatim:

> *"Σ_ℓ u^(ℓ)*(p) at H_3 does NOT recover m_p; the sum captures only the
> H_3-internal structure. The full iterative LP-dual unification (per
> term7-alpha5) is at H_n with n = 3A, where atomic-braid binding and
> gluon dressing are encoded. The H_3 levels reported here are necessary
> infrastructure but not sufficient for absolute mass."*

So the iterative LP-dual at H_n computes the **H_n-internal confinement
piece** — the structural correction *within* the Hecke algebra — not the
absolute mass / binding. The archimedean realization (Vol/ℏ², ν_SDP) lives
in a separate factor that multiplies the SDP slice.

This **is** the missing-`ν_SDP` problem flagged at workplan line 41
("ν_SDP comes from the SDP active set, not a guess"); the iterative LP-dual
gives the right *kind* of object (H_n-internal correction) at the wrong
*amplitude*. The archimedean bridge — call it `ν_SDP(K)` — is exactly the
`Vol(K_bind)/8G = f(Z,N)` ratio that this PR's f-decomposition extracts
from AME. The two are the **same missing object** in two languages.

### Concrete signal: a_K(D) ≈ f(⁴He)/Z·N

`a-K-via-lp-dual.witness.json` carries per-atom SDP shadow prices
`a_K_D_chi_abs`:

| atom | SDP `a_K` | my `f/Z·N` (from §pair-count) |
|------|----------|-------------------------------|
| D | 2.0757 | 0.998 |
| T | 2.2894 | 1.41 |
| ³He | 2.0836 | 1.22 |
| ⁴He | 2.1033 | **2.07** ← match |
| 5Li | (no entry) | 1.17 |

**`a_K(deuteron) = 2.0757` matches my `f(⁴He)/Z·N = 2.0725` within 0.15%.**
This is too close to be coincidence at 4-digit precision — the deuteron's
SDP shadow price is carrying the ⁴He shell-bonus structure. And
**`a_K(⁴He) = 2.103` matches `1+q ≈ 2.110`** (one of the ⁴He doubling
near-misses, 0.3% off). These cross-atom signals are consistent with the
operator-valued LR branching `A^λ_{μν}(I)` that #1443 just authored as a
proposition — the scalar `tr_M` *collapses* what should be an operator-
valued object, and the missing structure is what `f` and `a_K` are both
proxies for.

### Coordination posted

- #1442 (meson EM, `(1+ℏ_q)` universal substrate): tested whether
  `(1+ℏ_q)^k` bridges SDP→AME on the deuteron — it does NOT
  (`log_(1/ℏ_q)(42.36) = 1.62`, non-integer). So the universal `(1+ℏ_q)`
  factor is real but is NOT the SDP-completion factor by itself.
- #1443 (Hecke-branching trace decomposition): the operator-valued
  `A^λ_{μν}(I)` proposition is the categorical mechanism that should
  derive the SDP-completion bridge. Asked whether the proposition is
  expected to yield it.

### What's next

The honest Barrier-1 completion path is now:

1. **Wait on #1443 / `prop:hecke-branching-trace-decomposition`** — the
   operator-valued `A^λ_{μν}(I)` is the structural object that should
   derive `ν_SDP(K)` directly from the SDP active set, not require it
   as a guess. This is research, not within #1431's scope.
2. **The census-knot registry triplication** (workplan §barriers + the
   new `census-knot-audit.md`) stays as audit material per author
   direction; not deprecating.
3. **f remains AME-extracted**; the structural patterns recorded here
   are leads for #1443's operator-valued derivation, not derivations.

#1431 ships as: workplan + structural probes (5 probes, 0 fits) +
2026-05-30 SDP/census audit. Nothing wired to production.

## Critical-discipline audit (2026-05-30) — retracting 3 near-match claims

Per author guidance "be critical, we want only canonical derived",
re-auditing every numerical claim on this PR against the strict bar:

> A derivation must reach **compute-precision** (≪ 1 ppb at 50 dps), or
> at minimum the experimental σ of the target. A 0.1–1% near-match is
> a **suggestive structural lead**, not a derivation. Selection of "best
> of N candidates" by AME-match is the **selection-bias form of fitting**.

### Failures (retracted as derivations; remain leads)

| claim | residual | verdict |
|-------|----------|---------|
| κ_Coulomb ≈ 2√3/(3π) (= Bring × √3 from #1444) | **−935 ppm** | retracted: 0.1% off ≠ derivation |
| f ≈ Z·N for D | 0.19% | retracted: not within compute precision |
| f ≈ Z·N for 6Li | 0.62% | retracted |
| f ≈ Z·N for 7Li | 0.33% | retracted |
| ⁴He shell bonus 2.07 ≈ 1+q | 1.8% | retracted (was already flagged below) |
| ⁴He shell bonus 2.07 ≈ 2√q | 1.7% | retracted (already flagged) |

### What survives the bar

| structural piece | status |
|------------------|--------|
| `Δtr = |tr_M(free)| − |tr_M(atom)|` from canonical `atom_braid_word_3A` | derived |
| `Vol(Borromean) = 8G` (Catalan/dilog) | derived (knot invariant identity) |
| `B(D) = m_e · 8G · Δtr` (+0.19%) | derived **under** the universal-Borromean *assumption* — and even +0.19% is not compute-precision |
| Factorization `B = m_e · Vol(K_bind) · Δtr` (Kashaev-class identity) | derived in form; per-atom `Vol(K_bind)` is unknown |
| A=3 mirror split structure | confirmed phenomenology, not derived |
| ⁴He doubly-magic bump | confirmed phenomenology, not derived |
| `f(Z,N) = B_AME/(m_e·8G·Δtr)` | AME-extracted (definition), not a derivation |

### Retraction posted on sibling

[#1444 retraction comment](https://github.com/litlfred/qou/pull/1444#issuecomment-4581427035):
withdrew the §6 escalation that asked the author to extend
`em-coupling-bring-zero-mode.md` to κ. 935 ppm is a numerical near-match,
not a derivation; same critique I'm applying to my own f≈Z·N.

### Net honest status of #1431

This PR contributes:
1. **An audit** (`census-knot-audit.md`) showing the binding-K registry
   is triplicated-census-hardcoded across 3 production files, and the
   `Vol(K_bind)=8G` deuteron derivation is one labelled-volume away from
   the canonical braid.
2. **A clarification** (workplan + SDP-incomplete section) that the
   iterative LP-dual is structurally incomplete (H_n-internal piece only;
   author's own interpretation field), not broken — the missing scale
   is the archimedean realization that #1443's `A^λ_{μν}(I)` should
   derive.
3. **Five structural probes** that extract `f(Z,N)` from AME under the
   universal-Borromean assumption. None of the resulting patterns
   (Z·N near-match, κ ≈ Bring×√3, ⁴He bump ≈ 1+q) clear the canonical-
   derived bar. **All retracted as derivations.** They remain
   **suggestive leads** for #1443's operator-valued derivation, recorded
   as such; not wired to production.

**Nothing in #1431 should be treated as deriving an observable.** It
is a research-side audit + probe set + honest retraction record.

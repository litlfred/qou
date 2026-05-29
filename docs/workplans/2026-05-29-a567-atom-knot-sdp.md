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
  from the active set. A 7th fitted ansatz is forbidden (CLAUDE.md
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
(CLAUDE.md §7b: "Demazure sub-crystals for resonances/shells") combined
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

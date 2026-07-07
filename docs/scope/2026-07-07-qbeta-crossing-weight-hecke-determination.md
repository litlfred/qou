# Independent determination of the Q_β crossing weight `w(q)` — formalize-first scope

**Date:** 2026-07-07 · **Axis:** z→c_k f-map keystone — the forward direction
· **Follows:** [KC19 affine narrowing](../audits/2026-07-07-qbeta-crossing-weight-affine-narrowing.md)
(PR #3473) · **Status:** FORMALIZE-FIRST SCOPE (hypothesis + pre-registered
decidable gates). **No `c_k` value, no wiring** (registry §8 guard).

## 1. What KC19 leaves open — a single scalar

PR #3473 (KC19) reduced the keystone to a scalar: the Q_β ladder is the image of
the **crossing-weight departure** `w(u) − 1` under a fixed anchor-rigid map,

`w(u) − 1 = −(h−2)/2 · Σ_{k≥2} c_k u^k`,  prefactor `(h−2)/2 = (q²−2q−1)/(2q)`,

with the leading `[u²]` term derived (`c_2 = −1`) and the `[u³]` coefficient
`= −(q²−2q−1)/(2q)·c_3` — **the sole open scalar is `c_3`, carried entirely by
`w(q)`'s fibre structure** (the evaluation map contributes nothing anchor- or
nonlinearity-wise). This scope opens the **independent determination of `w(q)`**
— i.e. computing the crossing weight from the Hecke/Markov structure itself,
*not* by inverting the observed ladder (which would be circular).

## 2. The structure to exploit — Frobenius pairing, two loop values

Both canonical functionals on `H₃(q)` are the same Frobenius pairing
`⟨x, y⟩_G = tr_M(x·y)` against different elements
([net-ansatz Path A audit](../audits/2026-06-16-q-beta-net-ansatz-path-a-counit-vs-trace.md)):

- **mass tower** = `tr_M(β) = ⟨β, 𝟙⟩_G` (pair with the unit; loop value `z`);
- **Q_β observable** = `ε(β) = ⟨β, ω⟩_G`, `ω = G⁻¹𝟙` (pair with the cointegral;
  loop value `z = 1`, the topological limit).

The nucleon difference `(n−p)` has its top-weight `L₊` term cancel; what survives
is the `{γ, σ_i}` sector, and there `ε` (weight 1) beats `tr_M` (weight `z ≈ 0.5`)
— `ε` reproduces `Q_β` to +0.17%. The **effective crossing weight `w`** of the
observable is therefore `1` at leading order (the counit), and the `c_k` ladder is
its departure toward the `q`-weighted trace.

## 3. Hypothesis class for `w(q)`

**H-W (interpolation hypothesis).** The observable's effective weight is a
Frobenius pairing against an element `ω(u)` interpolating the cointegral `ω`
(`u→0`, counit) and the higher-`N` Markov-stabilized weight, with
`w(u) = ⟨σ, ω(u)⟩_G / ⟨σ, ω(0)⟩_G` and `w(0) = 1`. The `u`-dependence enters
through the **H₃ → H₄ Markov stabilization** of the nucleon braid: the `N=0`
truncation gives the counit; each stabilization step `Ind_{H_n}^{H_{n+1}}`
dresses the trace by one loop, contributing the next `u`-order.

Sub-questions (each decidable once `pyhecke` is available):

- **W1.** Compute the H₃ nucleon-braid NF difference `(n−p)` as an exact vector
  in the 6-dim `[γ,σ₀,σ₁,L₊,L₋,e⁻]` basis; confirm `⟨(n−p), ω⟩_G = ε(n−p) =
  h²/2 − h` symbolically (reproduces the KC18 counit).
- **W2.** Compute one Markov-stabilization step `H₃ → H₄` on `(n−p)`; extract the
  induced weight `w₁(q)` and confirm the departure is **bar-even** and **O(u²)**
  in `u = b·ℏ_q²` (i.e. no `u¹` term — the forbidden `c_1`).
- **W3.** Check whether the `[u²]` coefficient of the stabilized `w` reproduces
  the derived `c_2 = −1` prefactor `(q²−2q−1)/(2q)` (KC19). **This is the
  keystone gate:** a PASS means the stabilization independently derives the one
  known rung; a FAIL scopes-(a) the interpolation hypothesis H-W.
- **W4 (only if W3 passes).** Read the `[u³]` coefficient — the open `c_3`. Its
  cross-anchor stability is the acceptance test (proton+muon swing < 1%, per
  registry §8); a swing confirms the fibre/root-of-unity structure (KC19).

## 4. Pre-registered gates (decidable; stated BEFORE any run)

| gate | PASS | KILL (scope-(a)) |
|---|---|---|
| **W1** | `⟨(n−p), G⁻¹𝟙⟩_G = h²/2 − h` exactly | ≠ counit ⇒ pairing model wrong |
| **W2** | departure bar-even, leading order `u²` | odd part, or `u¹` present ⇒ H-W wrong |
| **W3** | `[u²]` coeff `= (q²−2q−1)/(2q)` (= `−c_2` prefactor) | ≠ ⇒ stabilization ≠ ladder; H-W scope-(a) refuted |
| **W4** | `[u³]` cross-anchor swing < 1% | swing ⇒ fibre structure (consistent, not a kill) |

**Discipline.** W3 is the make-or-break; it is a **derivation check of an
already-known rung** (`c_2`), so it is non-circular (it does not use `c_3` or
CODATA). Only if W3 passes does W4 read `c_3` — and even then no value is wired
until it clears the §8 cross-anchor test (which `c_3` has historically failed).

## 5. Compute status — GATED on `pyhecke`

The W1–W4 gates need the `H_n(q)` Gram matrix `G`, `TR_M` constants, and the
Markov-stabilization `Ind_{H_n}^{H_{n+1}}` — all in the `pyhecke` /
`pyhecke-native` layer. **`pyhecke` is not importable in the current sandbox**
(firewalled), so the numerical W1–W4 runs are **deferred**; this scope is the
formalize-first setup (compute-author §3.3: narrow the class and pre-register
the gates before the run). The abstract algebraic backbone (KC18/KC19,
`QOU.QBeta.CrossingWeightAffine`) is already Lean-proved and needs no `pyhecke`.

**Next executable step (when `pyhecke` is available):** implement W1 as
`computations/qbeta/qbeta_crossing_weight_hecke_probe.py` against the existing
`gram.G` / `gram.TR_M` / `PROTON_NF` / `NEUTRON_NF` constants, emitting a
witness with the W1–W3 assertions. Reuse `qbeta_h4_nucleon_assembly.py` for the
H₃→H₄ stabilization step rather than re-deriving it.

## 6. Coordination

- Downstream of PR #3473 (KC19) — cite, do not re-derive the affine narrowing.
- Overlaps the #3449 keystone tranche (same forward direction); intent to be
  posted there. Does **not** touch registry §9 (KC19 is #3473's).
- The "why the mass difference is a counit" question (net-ansatz forward
  direction) is the physical content this scope operationalizes.

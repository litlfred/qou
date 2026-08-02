# Gemini "q-deformed saddle-offset" brainstorm — salvage + refutation audit (2026-08-02)

Branch `claude/q-deformed-saddle-offsets-bdn992`, PR #4573.

Two long external (Gemini) brainstorms — "q-deformed saddle-point offsets" and
"Bring's surface in QFT" — were reviewed adversarially for salvageable content.
**Most of the dialogue is confabulation or already-in-corpus.** This audit
records the verdicts with scope classification (per AGENTS.md §"Before
declaring refuted"), so future agents do not re-chase them.

## Salvageable (real, kept)

1. **Two real papers**, verified (one with a Gemini author-hallucination):
   - **Garoufalidis–Yoon, "1-loop equals torsion for two-bridge knots"**
     (arXiv:2411.03801) — 1-loop invariant = adjoint Reidemeister torsion.
   - **Ormeño Bastías–Martin–Ryom-Hansen, "On the spherical partition algebra"**
     (arXiv:2402.01890) — Gemini misattributed this to "Bowman–Orellana".
   Both uploaded to `uploads/`. Neither yet in `references.ts`.

2. **Verified Lean lemma** (`QOU/Mass/ColorCubicDiscriminantPositive.lean`,
   sorry-free, lean-direct exit 0): the trefoil colour-cubic discriminant
   `Δ(z) = −(16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16)` (sympy symbolic-exact; **degree 6
   ⇒ 6 saddle points**, confirming the corpus) is **palindromic** (q↔q⁻¹
   bar-symmetry) and **strictly positive on ℝ** (exact SOS certificate) ⇒
   `Δ(z) < 0` for all real z ⇒ **no real branch point**: all 6 saddle points are
   strictly off the real spacetime axis. This is the rigorous tier of the
   owner's offset question (a torus-knot offset relative to a complex saddle
   orbit has nonzero angle by construction).

### The 6 saddle points, explicitly

Roots of `Δ(z) = 0` (the colour-cubic discriminant sextic), cross-validating the
two Lean theorems:

| # | Re z | Im z | \|z\| | arg |
|--:|--:|--:|--:|--:|
| 1 | −0.9748 | −0.2230 | 1.0000 | −167.1° |
| 2 | +0.1190 | −1.0536 | 1.0603 | −83.6° |
| 3 | +0.1058 | −0.9371 | 0.9431 | −83.6° |
| 4 | +0.1058 | +0.9371 | 0.9431 | +83.6° |
| 5 | +0.1190 | +1.0536 | 1.0603 | +83.6° |
| 6 | −0.9748 | +0.2230 | 1.0000 | +167.1° |

3 complex-conjugate pairs (all strictly off the real axis ⇒ confirms
`discSextic_pos`), with **reciprocal magnitude pairs** {0.9431, 1.0, 1.0603}
(0.9431 × 1.0603 = 1 ⇒ confirms `discSextic_palindromic`, the q↔q⁻¹ bar-symmetry),
at angles ±83.6° and ±167.1° (≈ 2×). The offset angle (tier-1,
`lagrangeResolvent_cyclic_eigenvalue`) is the C₅/S₃ stabilizer root of unity
carried on this complex orbit.

## Refuted (durable declarations, scoped)

- **Option A — "ν_SDP = 1-loop torsion" — REFUTED, scope-(a).** Implemented the
  Dimofte–Garoufalidis 1-loop invariant directly from SnapPy NZ data
  (`computations/probes/one_loop_vs_nu_sdp_probe.py`; no Sage needed). Result:
  |τ(6₂)| = 2.217 vs ν_SDP = 1; |τ(8₁₁)| = 8.805 vs ν_SDP = 2. τ is a
  transcendental/algebraic **complex** invariant, not the integer ν_SDP; the
  flattening/± ambiguity cannot bridge the magnitude gap. (4₁ control lands in
  its trace field ℚ(√−3), |τ|=√3/2 — implementation sound.) Scope-(a): the
  identification is false *as stated*; Garoufalidis–Yoon's 1-loop=torsion
  remains a valid analytic bridge, just not to ν_SDP.

- **Option B (coarse) — "ν_SDP = dim SP_k" — REFUTED, scope-(a).** The real
  paper (Thm 2) gives `rk SP_k = bp_k = #bipartite partitions of k = A002774 =
  (1,2,9,31,109,…)` — never the multiplicity {1,2}; for the atoms' k∼6,9 it is
  in the hundreds. Category error (whole-algebra dimension vs single-block
  multiplicity). **Not fully dead:** ν_SDP could still equal a *specific* SP_k(n)
  decomposition number (the paper's Sym^k(CS_n) decomposition is where 1,2 live),
  but only via an unproven bimodule iso QOU-Wedderburn-block ↔ SP_k(n)-module.

## Confabulated / already-in-corpus (do not chase — bean qou-fk19)

- `v_offset(q)` sinh/cosh ODE — no derivation; internally inconsistent (deuteron
  offset given as both −1/sinh λ and −9.566 in one dialogue).
- `q = exp(2πiτ) → q₀≈1.11` — dimensionally broken (|q|<1 for τ∈UHP vs q₀>1
  real); owner rejected it in-dialogue.
- closed-form `R(q,x)=θ₁θ₁·Δ_Bring` — pure assertion.
- Toroidal-JSJ elliptic overshoot (≈4.37) — already in corpus + overclaim-audited
  (`2026-07-19-qbeta-toroidal-tower-overclaim-audit.md`).
- "Conjecture 10.14.8 ρ_F=ν_SDP" — Gemini's "novel" identity **is** the corpus's
  own `conj:kashaev-density-equals-sdp-multiplicity` (open, single Lean sorry).

## Knot-assignment solver — the real open gap (bean qou-vd7j)

Ran `all_nuclides_sdp_admissibility.py` over 3558 nuclides: scalar-LP 2221/3558
but **Frobenius per-nucleus admissibility 0/3558**. The deuteron SDP shows the
Frobenius **Gram is indefinite at q₀** (neg-norm blocks (3,1,1,1),(2,2,1,1),(1⁶))
+ 2/6 encodings ANSATZ-flagged. So the operator-selection SDP does not yet derive
K_w/ν_SDP. Open R5 sub-gaps (per `conj:canonical-knot-id-sdp`): finitude of the
NF candidate set; rigorous SDP search bounds; structural K(𝔥)∈H_{3A}(q₀). No fit
wired (hand-assigning knots by volume-match to hit B_AME would be a fit).

## Net

The `ρ_F·m_e·Vol` binding route (3 census atoms: +1.1% / −0.16% / −2.97%; ⁴He no
knot) is dominated by the still-open knot-assignment gap; nothing here approaches
ppq (an L1 compute leg, already met). Both external "close the ν_SDP gap"
proposals are refuted; `conj:kashaev-density-equals-sdp-multiplicity` stays
honestly open. Deliverables: 1 verified Lean lemma, 2 probes, 5 beans, this doc.

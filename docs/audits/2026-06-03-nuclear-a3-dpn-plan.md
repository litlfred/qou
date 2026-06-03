# Nuclear A=3 binding + Δ_pn — derivation plan and baseline

**Status:** SCAFFOLD. Work tranche for two of the four error-reduction
items in the 2026-06-03 workplan: (2) per-nucleus A=3 binding (triton ³H,
helion ³He) and (3) the proton–neutron mass difference Δ_pn. Sibling
tranches: Q_β SDP strict-complementarity (PR #1752) and m_μ lepton
torus-tower (PR #1753).

## Governance (read first)

Both targets are formally below the ~780 ppb CAL-2 floor (Δ_pn 100×
target ≈ 4.7 ppb; the binding-energy ratios sit far below that), which is
owner-declined Subgoal-2 territory (substrate-derivation of q₀, declined
2026-05-08; see [`docs/precision-goals.md`](../precision-goals.md)). The
in-scope deliverable here is **reducing the prediction error from a
categorical/braid derivation** — not formally passing a sub-floor 100×
gate. Where the floor binds, it is reported, not crossed.

No empirical fits. The Δ_λ gate forbids a seventh fit-based ansatz
(six have failed on the deuteron); see
[`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md).

## Baseline (canonical Jones–Markov trace, current q₀)

From `binding_canonical.py` at q₀ ≈ 1.1099786, Q_β = 0.782333 MeV (CAL-3):

| Atom | A | 3A | B_AME (MeV) | B_pred (MeV) | \|Δm/m\| |
|------|---|----|-------------|--------------|----------|
| D    | 2 | 6  | 2.225       | +0.466       | 0.094 %  |
| T    | 3 | 9  | 8.482       | +0.629       | 0.279 %  |
| ³He  | 3 | 9  | 7.718       | +0.658       | 0.251 %  |
| ⁴He  | 4 | 12 | 28.296      | +0.714       | 0.735 %  |

Observation: the canonical trace `B = 𝔈₀·(|tr_M(W_free)| −
|tr_M(W_atom)|)` **underpredicts** the absolute binding by a large factor
(D: 0.466 vs 2.225 MeV). The per-nucleus comparison is currently carried
as a fractional-mass quantity (the `|Δm/m|` column), not as the absolute
binding. The A=3 task is to close the gap between the canonical trace and
the absolute B_AME for the two A=3 nuclei **without fitting**.

## A=3 plan (item 2)

Categorical object for A=3 is the H₉ atomic braid word (3A = 9
generators), `atom_braid_word_3A(Z, N)`:
- triton ³H (Z=1, N=2): (p-block, n-block, n-block) + inter-nucleon crossings;
- helion ³He (Z=2, N=1): (p-block, p-block, n-block) + inter-nucleon crossings.

Concrete first step (per scoping): explicit H₉ Wedderburn character sum
weighted by canonical Jones–Wenzl (Ocneanu) weights `ω_λ`, then scaled by
the binding-link hyperbolic volume (³H → 8₁₁ knot; ³He → L6a4 / Borromean
8G = 5.688). Compare residual vs AME (³H 8.482, ³He 7.718 MeV). If the
residual lands inside the error budget with no free parameters, escalate
to the GAP-A-3 categorical selector (which partition selects which brane
level).

Existing scripts to build on: `binding_canonical.py`,
`binding_threebody_joint_trace.py` (H₉ all-pairs joint trace),
`phase5/phase3_triton_binding_convention_b.py`,
`binding_a3plus_full_theta_assembly.py` (full-order θ_λ assembly; latest
attempt ³He at +17.4 % without fit).

## Δ_pn plan (item 3)

Re-derive the p–n mass difference against the current proton-anchored q₀
via the p–n channel asymmetry already implemented as
`pn_convention="bring_color_weighted"` in `closed_form_tau_M.py`. Confirm
the current 773.9 ppb error originates from a stale-q₀ evaluation vs a
structural gap, and whether the bring-color-weighted asymmetry closes it
at the current anchor.

## Findings (2026-06-03)

### The A=3 −60% deficit is robust across six independent readings

Every parameter-free reading of the binding gives the deuteron near AME but
A=3 short by ~−60 %:

| reading | D | T | ³He |
|---------|----|----|-----|
| canonical signed trace `E₀(tr_free − tr_atom)` | (small) | −92 % | — |
| scalar modulus `E₀(\|Σyχ_free\| − \|Σyχ_atom\|)` | +12 % | −60.3 % | −54.4 % |
| **per-block magnitude `E₀(Σy\|χ_free\| − Σy\|χ_atom\|)`** | **+3.6 %** | **−61.7 %** | **−55.1 %** |
| single-link volume `m_e·Vol·Δtr` | +0.2 % | −59.9 % | −59.2 % |
| 3-bond all-pairs joint trace | — | −64.1 % | −58.9 % |

(`binding_per_block_magnitude_a3_probe.py`, `binding_link_volumes.py`,
`binding_threebody_joint_trace.py`.)

### What this rules out

- **Not the observation modulus.** The per-block / superselection reading
  (`|·|` per Wedderburn block — the natural extension of the q₀-real
  bar/modulus result) closes the deuteron (+3.6 %) but fails A=3 the same
  ~−60 %. So the deficit is not a modulus-ordering artifact. The
  per-block-closes-A≥3 hypothesis is **refuted**; not formalized.
- **Not a per-partition Δ_λ choice.** All readings are parameter-free
  (no Δ_λ) and all land at ~−60 %; the gap is not a free per-block weight.

### Where the gap actually is (sharpened diagnosis)

The deficit is in the **inter-nucleon binding structure / multiplicity**,
not the observation or the per-block weights. Evidence: A=2 (one interface)
works; ⁴He works via the *fully-linked* Borromean (8G) structure; A=3 with
the linear-chain braid word (`β_p·I₁₂·β_n·I₂₃·β_block`, adjacent interfaces
only) gives only ~1.5× the deuteron, while AME B(A=3) ≈ 3–4× the deuteron
— roughly the **number of nucleon pairs** (3 for A=3). The canonical trace
returns a single collective number, not the pairwise-additive sum.

**Next lead (parameter-free, testable):** pairwise-additive binding
`B(A=3) = Σ_{pairs} B_pair` (T: B_pn+B_pn+B_nn; ³He: B_pp+B_pn+B_pn), each
pair computed deuteron-style. A sibling branch
`claude/binding-extensive-bond-sum-2026-06-02` already explores extensive
bond sums — **coordinate, do not duplicate**.

## Done / next

- [x] Branch + baseline established.
- [x] A=3 per-block / superselection reading — **refuted** (closes A=2 only).
- [x] Six-reading robustness of the −60 % deficit established → gap is the
      inter-nucleon multiplicity, not observation or Δ_λ.
- [ ] Pairwise-additive `B = Σ_pairs B_pair` test (coordinate with the
      extensive-bond-sum sibling).
- [ ] Δ_pn: re-derive at current q₀ via bring-color-weighted asymmetry.

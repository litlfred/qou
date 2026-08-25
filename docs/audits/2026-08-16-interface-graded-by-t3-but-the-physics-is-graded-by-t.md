# The interface is graded by `T₃`; the bound/unbound split is graded by `T`

**Date:** 2026-08-16
**Branch:** `claude/l2-1ppq-mass-binding-mh643j`
**Beans:** `qou-7nwg`, `qou-0pzi`, `qou-pjx4`, `qou-brg3`
**Lean:** [`QOU/QBeta/SingleCrossingAlwaysBinds.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SingleCrossingAlwaysBinds.lean) (sorry-free)
**Probes:** `two_nucleon_sector_sign_probe.py`, `stacked_interface_writhe_normalised_probe.py`
**Sources:** owner-uploaded, commit `2e5bfdd` — [`library/arxiv-nucl-th-0006014v1/0006014v1.pdf`](../../library/arxiv-nucl-th-0006014v1/0006014v1.pdf)
(Machleidt, *CD-Bonn*, arXiv:nucl-th/0006014, Phys. Rev. C 63 024001),
[`library/arxiv-1105.2919v1/1105.2919v1.pdf`](../../library/arxiv-1105.2919v1/1105.2919v1.pdf) (Machleidt–Entem,
*Chiral EFT and nuclear forces*, arXiv:1105.2919, Phys. Rept. 503 1)

---

## 1. The measurement that decides it

Machleidt CD-Bonn §III, Eqs. (3.1)–(3.3) + Table XI, S-wave scattering lengths
(`N` = nuclear part, electromagnetic effects removed):

| channel | `T` | `T₃` | scattering length | bound? |
|---|:--:|:--:|---:|---|
| pp `¹S₀` | 1 | +1 | `a^N_pp = −17.3` fm | no (virtual) |
| nn `¹S₀` | 1 | −1 | `a^N_nn = −18.9 ± 0.4` fm | no (virtual) |
| np `¹S₀` | 1 | 0 | `a_np = −23.740 ± 0.020` fm | no (virtual) |
| **np `³S₁`** | **0** | 0 | **`a_t = +5.419 ± 0.007` fm** | **YES — the deuteron** |

The sign of `a` is the bound-state diagnostic: negative ⇒ virtual state, positive
⇒ bound state.

Read the table by quantum number and the structure is unambiguous:

* **Across `T₃` at fixed `T = 1`** (the three top rows): all negative, all
  unbound, spread `−17.3 → −23.7`. CD-Bonn Eq. (3.6) quantifies it as
  `Δa_CIB = a^N_pp − a_np = 6.44 ± 0.40` fm — a **~25 % modulation** on a
  ~20 fm scale, and the paper calls it "a small amount of CSB and a clear
  signature of CIB."
* **Across `T`** (rows 1–3 vs row 4): the scattering length **changes sign**,
  `−23.7 → +5.4`. This is not a modulation, it is the difference between having a
  bound state and not.

So: `T₃` is the small effect. `T` is the qualitative one.

## 2. What the framework grades by

The strong-isospin interface is graded by the **crossing sign** — stated
explicitly in [`WeakIsospinT3Grading.lean`](../../content/quantum-observable-universe/lean/QOU/ParticleInteractions/WeakIsospinT3Grading.lean):

> "the strong-isospin interface uses `σ_g` (positive) for the `pp` channel and
> `σ_g⁻¹` (negative) for the `nn` channel"

with the offsets `d_pp = 0` (σ), `d_nn = −h` (σ⁻¹), `d_pn` colour-weighted in
between. Crossing sign **is** the writhe, and the corpus derives writhe → `I₃`
([`2026-08-10-writhe-level-of-definition.md`](2026-08-10-writhe-level-of-definition.md)).

**So the framework's interface grading is `T₃`.** That is a principled choice, not
an arbitrary one — and it is aimed at the ~25 % effect. There is **no** grading by
`T` anywhere in the interface, which is why the sign never flips.

This is the same defect `content_keyed_interface_refuted` found from the other
side (a species-pair-keyed interface cannot separate the two np rows, which share
content but differ in `T`). The scattering lengths say what the missing grading
*is*, and how big the effect it must produce is.

## 3. Why no repair inside the single-crossing family can work

Proved sorry-free in `SingleCrossingAlwaysBinds.lean`: the single-crossing scalar
is `μ = z + d` with `z = q³/(q²+1)`, `d ∈ [−h, 0]`, and

    z < 1  ⟺  q³ < q² + 1,

which at `q₀ ≈ 1.10998` reads `1.3676 < 2.2321`. The family is increasing in `d`,
so `μ ≤ z < 1` throughout and `B = −α log μ > 0` **always**. Unbinding needs
`q > 1.46557…` (real root of `q³ = q²+1`); the substrate sits 24 % below.

Consequences:

* no re-grading of `d` — by `T₃`, by `T`, by colour, by anything — unbinds;
* the writhe normalisation makes it strictly worse (it multiplies `μ` by a factor
  in `(0,1)`, i.e. binds harder);
* the Hecke projectors, which **do** supply `T` (`μ₊`/`μ₋` are the symmetric /
  antisymmetric = `T=1` / `T=0` channels), are a two-element sub-family of exactly
  this interval — which is why `mu_sum_eq_one` cannot unbind either. That result
  is now a corollary of the interval statement rather than a separate fact.

## 4. The resolution, stated as a conjunction

A repair must do **two independent things**:

1. **Grade by `T`, not only `T₃`.** The algebra already supplies this — the Hecke
   spectral projectors `P±` are the `T=1`/`T=0` split, and their scalars are the
   `n=2` Wedderburn weights `y_(2)`, `y_(1,1)`. No new parameter is needed.
2. **Escape `μ ≤ z < 1`.** Proved impossible with one crossing. `stacked_interface_writhe_normalised_probe.py`
   shows the writhe-normalised **even negative** stacked powers `σ^{-2}, σ^{-4}, …`
   have `μ_eff > 1` and do unbind — outside the theorem, because they are not
   single crossings.

Neither alone suffices: (1) without (2) still binds every channel; (2) without (1)
unbinds without knowing which channel should unbind. And (2)'s magnitudes are
currently wrong — `σ^{-2}` gives `−0.613 MeV` where the `¹S₀` channels sit at
`≈ −0.07 MeV`, 6–9× too large.

## 5. Correction to this session's earlier diagnosis

I first reported that the split is **spin-tensor** (`³S₁–³D₁` coupling) and that
the framework's colour-only fibre — Schur–Weyl having killed the spinor `ℂ²` —
therefore *structurally cannot* host it (bean `qou-7nwg` as originally filed).

That was over-stated. For two nucleons in a relative S-wave, antisymmetry ties
spin and isospin: `(S,T) = (1,0)` or `(0,1)`. So the split is expressible **either**
as `S` or as `T`, and `T` is available in the Hecke algebra without any spin
degree of freedom. The framework does not need a spinor fibre to see it; it needs
to grade by `T` rather than `T₃`, and to leave the single-crossing family. The
tensor force is the *mechanism* in nuclear physics; it is not the only route to
the *quantum number*.

`qou-7nwg` is re-scoped accordingly — the question is not "can a colour-only fibre
host this" (it can, via `T`) but "what construction supplies `T`-grading **and**
`μ > 1`".

## 6. Corpus-grep performed

- `references.ts`: **no** Machleidt, **no** NN partial-wave analysis, **no**
  scattering lengths. The two-nucleon values used throughout this axis
  (`pp ≈ −0.1`, `nn ≈ −0.1`, `pn ¹S₀ ≈ −0.066` MeV) trace to an unsourced table in
  [`2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md`](2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md).
  These two uploads are the first citable source for the data the framework's
  two-nucleon predictions are falsified against; adding them to `references.ts`
  is follow-on work.
- Writhe corpus reviewed before writing: `WritheMarkovInvariance.lean`,
  `WritheLevelParity.lean`, `WritheIndependenceCriterion.lean`,
  `SecondCrossingInvariant.lean`, `WeakIsospinT3Grading.lean`, and the five
  `docs/audits/*writhe*` documents. The `T₃`-grading identification above is the
  corpus's own, quoted, not a new claim.
- The 2026-08-10 level-of-definition ruling (observable = trace at the **minimal**
  tower level, a canonical section of the vertical move) was checked against the
  stacking probe: `σ^m` stacks on an **existing** generator, so the strand count
  is unchanged and no destabilisation applies. The probe is consistent with the
  ruling.

## 7. Scope

Section 3 is **scope-(b)** with the invariant named (`μ ≤ z < 1`), narrow to
single crossings. Sections 1–2 are measurement and quotation. Section 4 is a
statement of requirements, **not** a proposed construction — nothing is fitted,
nothing is wired, and the `Δ_λ` no-seventh-ansatz gate is untouched.

# α_EM F-construction T5 — the assembly; milestone complete (2026-07-19)

**Bean:** `qou-bc35` (T5), closing milestone `qou-a46k`. Upstream, all
merged: T1 ([#4039](https://github.com/litlfred/qou/pull/4039)), T2
([#4040](https://github.com/litlfred/qou/pull/4040)), T3
([#4042](https://github.com/litlfred/qou/pull/4042)), T4
([#4061](https://github.com/litlfred/qou/pull/4061)).

**Probe:** [`computations/alpha_em/alpha_em_f_t5_assembly_probe.py`](../../computations/alpha_em/alpha_em_f_t5_assembly_probe.py)
→ [`alpha-em-f-t5-assembly.witness.json`](../../computations/alpha_em/alpha-em-f-t5-assembly.witness.json)
— 3/3 PASS (one-pass exact re-verification of the merged joints).

**Scope guard (STRICT):** conditional on R1+R2 below; neither asserted nor
derived; no instance fabricated; no fit; nothing wired; `1/(8π)` stays
phase-4.

## The assembled conditional theorem

Let F be the cover-monodromy functor of the T1 cover (Deligne–Mostow /
McMullen species). By the merged bricks, F satisfies every requirement of
the [#4035](https://github.com/litlfred/qou/pull/4035) target
specification at the level established:

| Spec | Status | Brick |
|---|---|---|
| S1 — F(channel pair) = the χ=±i eigenline pair | **forced** | #3960 + T1 |
| S2 — module structure at q=i | **exact** (explicit conjugation to the Jordan block) | T2 |
| S3 — F∘ρ = conj∘F | **proved** (deck reality, sorry-free Lean) | T3 |
| S4 — Markov weights at the decategorification point | **derived** ((¾,¼) = one shared invariant, no freedom) | T4 + B4a |
| S5 — discharge into `TauRhoHodgeLift` ⟹ measure `½·a₀` | **in place** | #4035 + #3999 + B-plan |

## The residual — the wall's entire surviving open content

- **(R1) Framework identification.** The framework's archimedean τ-functor
  restricts to F on the H₂-channel data — i.e. the categorical action the
  framework assigns to the substrate braiding is the braid monodromy of the
  T1 cover. This is a **naturality check against the corpus's existing
  brings-surface bridge** (`braid-group-action`, the ℤ₅/𝒳₅ machinery, the
  weight-identification blocks) — a corpus-internal verification target,
  not new mathematics.
- **(R2) Loop-weight provenance.** The α_EM tower's one-loop insertion is
  `F(b_s/[2]_q at q=1)` weighted by the B3-inherited heat unit `a₀·α` — the
  physics identification. Phase-4 per the owner ruling (`dd55a5748`); only
  the owner lifts it.
- (fibre) General-q weight transport — open, **not** measure-relevant.

## Where the wall stands (end of the F-construction arc)

```
Session start:      "1/(8π) is an unexplained phase-4 factor"
After the B-plan:   wall = one named premise (Reality realization)
After numerics:     wall = irreducibly categorical (all parameter-free
                    candidates excluded, machine-checked)
After F (T1–T5):    wall = TWO named statements about the framework's own τ:
                    R1 (naturality vs the existing Bring bridge) and
                    R2 (loop-weight provenance, phase-4)
```

Every step is machine-verified (17 merged PRs of probes + sorry-free Lean),
nothing is fitted, and nothing is wired. The natural next tranche — for a
fresh session — is **R1**: walk the brings-surface chapter's braid-action
blocks and check the naturality square against F.

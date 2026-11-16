---
# qou-sgv5
title: 'chi-matrix-m family does not distinguish proton from neutron: tr_M identical, so Delta(n-p)=0'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T14:18:01Z
updated_at: 2026-11-16T18:04:00Z
parent: qou-wp3h
---

## The observation

In the `chi-*-at-q0-50dps-matrix-m` family, proton and neutron carry the
**identical** `tr_M(q₀)`, to every stored digit. Same for tritium and
helium-3:

    OLD (convention C, as committed)      NEW (convention D, regenerated)
      proton  : 1.6331535900562524882…     proton  : 1.8843194672549750250…
      neutron : 1.6331535900562524882…     neutron : 1.8843194672549750250…
      tritium : 1.0860240058218428921…     tritium : 2.5115533409057651119…
      helium-3: 1.0860240058218428921…     helium-3: 2.5115533409057651119…

**Not a regression from the convention-D migration** — the old committed
values were equal too. It is a pre-existing property of this path, surfaced
by regenerating it (`qou-lt8x`).

## Why it matters

`Δ = tr_M(n) − tr_M(p)` is not incidental. It is the quantity the
operator-valued split uses to set the energy scale — cf.
`probes/homflypt_operator_valued_probe`, which computes

    E₀ = Q_β / |Δtr_M|

and whose whole premise is that the averaged crossings **break** the
amphicheirality that makes the pure-braid HOMFLYPT give P(p) = P(n). In this
family that break does not happen: Δ = 0 exactly, so any consumer reading
these witnesses for a p–n asymmetry gets nothing, and an E₀ derived from them
would divide by zero.

## CONFIRMED (2026-08-15): the sign is read from a field that is always +1

Measured, closing steps 1 and 2 below. `_word_for_braid_word_3a(1,0)` and
`(0,1)` return **byte-identical** words, so the degeneracy is in the word
builder — not the engine, not the sign marshalling.

The reason is one line
([`derived_chi_catalogue_matrix_m.py:655`](../computations/derived_chi_catalogue_matrix_m.py)):

    word = [(1 if c >= 0 else -1, gen_0based + 1) for (c, _d, gen_0based) in triples]

`atom_braid_word_3A` returns `(c, d, gen_idx)` triples, and **`c` is not the
crossing sign.** Measured across the whole range, `c ≡ +1` for every crossing
of every nucleus:

    proton    n= 11  c-values={1: 11}   distinct-d=3
    neutron   n= 11  c-values={1: 11}   distinct-d=3
    deuteron  n= 23  c-values={1: 23}   distinct-d=4
    He-4      n= 47  c-values={1: 47}   distinct-d=5
    Li-6      n= 71  c-values={1: 71}   distinct-d=5

The σ / σ⁻¹ / averaged distinction lives entirely in **`d`**, as that
function's own docstring says — *"every crossing is a template
{0, −h, −h/2, −h(½−δ/4)}"*. Decoding `d` back reproduces exactly the counts
this bean recorded from the other word source, so the two agree and the
earlier "either the word source is species-independent or the distinction is
lost further down" was a false dichotomy — it is the *translation* between
them:

    proton   σ:6  σ⁻¹:3  averaged:2      (d = 0, −h, −h/2)
    neutron  σ:5  σ⁻¹:4  averaged:2

So `_word_for_braid_word_3a` reads the sign off the constant field and
discards the field that carries it. Every word collapses to an all-positive
braid whose only remaining content is the generator-index pattern — which is
a function of A alone. Hence p ≡ n and tritium ≡ ³He *identically, by
construction*, at every q and in both conventions. That is why the old
committed C-era values were equal too.

This is **not** the documented `sign_for_ctype` lossiness (σ→+1, σ⁻¹→−1,
averaged→0, magnitude unrepresentable). It is worse: a genuine sign-only
encoding would still separate p from n by their σ⁻¹ counts, 3 vs 4. This one
maps everything to +1, so it is sign-*free*, while the witness `convention`
field advertises `"sign-only-crossings"`.

### Why the obvious fix does not work

Deriving the sign from `d` via the canonical vocabulary
(`classify_crossing` → `sign_for_ctype`) would restore σ vs σ⁻¹ — but
`sign_for_ctype` sends *averaged* to `0`, and `0` is not a braid generator.
The `(sign, gen)` wire format has nowhere to put an averaged crossing. That
is precisely the open representation question in `qou-gdtb`: a
`(gen_idx, ctype)` pair cannot express an operator-valued interface.

So the answer to step 3 is: **this family cannot carry the p–n split**, and
should say so rather than let a reader take Δ = 0 for physics. Recorded in
the producer's witness description rather than left to inference.

## The original hypothesis, superseded by the measurement above

The `matrix-m` route goes through the Rust engine, whose wire format carries
a **sign** per crossing. `canonical_braid_crossings.sign_for_ctype` maps
BOTH averaged interfaces — colour-blind `averaged` and colour-weighted
`averaged_weighted` — to `0`, because a sign cannot carry a magnitude. That
projection is documented (`qou-gdtb`, `qou-8zjd`) and is exactly where the
p–n colour weighting `-h(1/2 - δ/4)` is unrepresentable.

But that alone does not explain it: the proton and neutron braid words differ
in their σ / σ⁻¹ counts (measured: p `{σ:6, avg:2, σ⁻¹:3}`, n `{σ:5, avg:2,
σ⁻¹:4}`), so even a sign-only encoding should distinguish them. Either this
producer's word source (`_word_for_braid_word_3a`) is species-independent for
A = 1, or the distinction is lost further down. **Confirm before acting** —
this is a hypothesis, not a finding.

## To close

1. Print `_word_for_braid_word_3a(Z, N)` for (1,0) vs (0,1) and diff them.
   If identical, the degeneracy is in the word builder, not the engine.
2. If the words differ, trace where equality is introduced — the sign
   marshalling is the first suspect.
3. Decide whether this family is *supposed* to carry the p–n split. If the
   sign wire format genuinely cannot, say so in the witness description
   rather than letting a reader infer that Δ = 0 is physics.
4. Cross-check against a path that does carry it (the bridge / exact-triple
   route, which matches markov_peel to 3.6e-51 per `qou-gdtb`).

Related: `qou-gdtb` (representation decision still open — a `(gen_idx, ctype)`
pair cannot express an operator-valued interface), `qou-pb4c` (downstream
sweep of this family).

## 2026-11-16 — All 4 diagnostic steps executed, verified at 50 dps, and stamped on all 11 matrix-m witnesses (PR #8145)

Probe [`computations/probes/chi_matrix_m_isospin_degeneracy_diagnostic_probe.py`](../computations/probes/chi_matrix_m_isospin_degeneracy_diagnostic_probe.py) (`computations/probes/chi-matrix-m-isospin-degeneracy-diagnostic-probe.witness.json`, 7/7 assertions passed, PR #8145 at `ed78b60a0ffe233f132df45a37bb1456ec237832`):

1. **Step 1 (Word diff):** `_word_for_braid_word_3a(1, 0) == _word_for_braid_word_3a(0, 1)` (`n=3`, 11 crossings, `diff_count == 0`) and `_word_for_braid_word_3a(1, 2) == _word_for_braid_word_3a(2, 1)` (`n=9`, 35 crossings, `diff_count == 0`).
2. **Step 2 (Root cause in `(c, d, gen) -> (sign, gen)`):** `atom_braid_word_3A(Z, N)` returns `(c, d, gen_0based)` triples with `c == +1.0` across all crossings of all nuclei, while the crossing type (`sigma`: `d=0`, `sigma_inv`: `d=-h`, `averaged`: `d=-h/2`, `averaged_weighted`: `d=-h*(1/2 - delta/4)`) is carried in `d` (proton vs neutron differ at 2 crossing indices `[6, 8]`; tritium vs helium-3 differ at 4 indices `[11, 18, 20, 23]`). Because `_word_for_braid_word_3a` reads `1 if c >= 0 else -1` off the constant `c == +1` field and discards `d`, every word collapses to an all-positive braid word whose generator sequence depends on `A = Z + N` alone.
3. **Step 3 (50-dps verification & witness stamping):** Verified `tr_M_sign(p) == tr_M_sign(n) == 1.54087323577941695436552...` and `tr_M_sign(T) == tr_M_sign(3He) == 1.37334463951319234744119...` (borromean) / `2.51155334090576511198573...` (grouped) to all 50 digits (`Delta == 0` identically). Stamped `ISOSPIN_DEGENERACY_NOTE` (`isospinDegeneracyNote`), `pn_split_carried: false`, and `pn_split_note` across `derived_chi_catalogue_matrix_m.py`, `chi_at_q0_via_matrix_m_mpfr.py`, `chi_via_rust_lossless.py`, `chi_4he_via_rust_lossless.py`, and all 11 `chi*matrix-m*.witness.json` files.
4. **Step 4 (Exact-triple cross-check):** Verified against the exact-triple Hoefsmit (`chi-{atom}-h{n}-at-q0-50dps.witness.json`) and closed-form Wenzl bridge (`closed_form_tau_M.py`) routes where `Delta tr_M(n - p) = -0.1541948850472397056592555...` and `Delta tr_M(3He - T) = +0.0294522112934643148617025...`, matching `closed_form_tau_M` to `< 3e-51`.

Status kept `in-progress` pending owner review / merge of PR #8145.

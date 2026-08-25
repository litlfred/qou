# Impact of fixing the 1-loop determinant — what changes, and what is downstream

**Date:** 2026-08-07 · **Bean:** `qou-fl4t` · **Follows:** PR #4691, #4697, #4700, #4706

## Headline

**A correct implementation already exists in this repo**, and it is
triangulation-invariant. The defect is confined to a cluster of five probes
that share a *different, wrong* determinant. **Nothing in `content/`, no Lean,
and nothing production depends on any of them** — #4671's "audit-only" claim
is verified below, not assumed.

But the fix is **not** a copy-paste, and the reason is the important part: the
correct in-repo implementation was **one-cusped only**, and the entire `c_σ`
arc lives on 2- and 3-cusped links.

> **Superseded in part (2026-08-07, later).** The multi-cusp case has since been
> derived and implemented —
> `docs/audits/2026-08-07-one-loop-multicusp-derivation.md`. Read the two
> corrections below in order; the "blocker" this document names was withdrawn,
> and the residual caveat moved to the overall normalization constant.

## Three implementations, three answers

| script | construction | `\|τ(4₁)\|` | triangulation-invariant? |
|---|---|---|---|
| `whitehead_c_sigma_torsion.py` | `A − B·z/(1−z)`, no ½ | **√3** | **NO** — 8 values for `5_2` |
| `probes/one_loop_vs_nu_sdp_probe.py` | DG/GY Def 2.1, with ½ + flattening | **√3/2** | **YES** — verified below |
| `probes/torsion_nu_sdp_probe.py` | Porti adjoint torsion via Fox calculus | **3** | (value-validated separately) |

The middle one is correct: `√3/2` is exactly Dimofte–Garoufalidis' own worked
figure-eight example (1202.6268, eq. 3.2). The first is exactly **twice** it —
the `½` its docstring claims is unnecessary.

### Verified: the correct construction IS invariant

Re-running `one_loop_vs_nu_sdp_probe.py`'s construction over ~19 randomized
triangulations each (controls: `is_isometric_to` + geometric solution only):

```
4_1   (1 cusp, 2 tet)  |τ| = 0.866025403784   1 distinct value   INVARIANT
5_2   (1 cusp, 3 tet)  |τ| = 1.161162738134   1 distinct value   INVARIANT
6_2   (1 cusp, 5 tet)  |τ| = 2.216589930891   1 distinct value   INVARIANT
```

Against `5_2`'s **8** distinct values and `6_2`'s **17** under the other
construction. This is the direct confirmation that the non-invariance measured
in PR #4691 is an implementation defect, exactly as DG's §3 invariance proof
predicts.

**New trustworthy reference values** (were not available before):
`|τ(5_2)| = 1.161162738134`, `|τ(6_2)| = 2.216589930891`.

Note `|τ(5_2)| = 1.16116…` is **not** `√ρ = 1.15096…`, the generator of the
ambiguity group found in PR #4697. The invariant and the ambiguity generator
are different numbers, as they should be.

## The blocker: the correct implementation is one-cusped only

```python
def mu(A):
    B = A[:N].copy().astype(float); B[-1] = A[mer]; return B
```

It replaces **one** edge row with **one** meridian row. That is right for
`c = 1` and wrong for `c ≥ 2`, where `N − c` edges and `c` meridians are
needed. Run as-is on the links:

```
L5a1  (2 cusp)  |τ| = 0.000000000000
L6a4  (3 cusp)  |τ| = 0.000000000000
```

Degenerate. And DG Definition 1.2 is itself **stated for one-cusped
manifolds**.

> **CORRECTION (2026-08-07, later).** An earlier version of this audit said the
> multi-cusp case "is their §4.5". **That is wrong.** §4.5 is the
> *character-variety* generalization — still one cusp, but deformed
> representations with meridian eigenvalue `m`. The multi-cusp formula is **not
> in the paper at all**. DG list it in §1.9 among extensions, and state plainly:
> *"The generalization to multiple cusps is also quite straightforward, but
> left out mainly for simplicity of exposition."*
>
> So there is **no published multi-cusp formula to implement** in the source we
> have — it has to be derived. And "straightforward" is the authors' judgement,
> not a recipe: the one-cusped derivation uses an identity DG state for one
> cusp —
>
> > *"For a one-cusped manifold, every edge begins and ends at the cusp, which
> > implies `Σ_I G_Ii = Σ_I G'_Ii = Σ_I G''_Ii = 2`"*
>
> — and it is what makes the `N` edge equations dependent in the way the
> construction needs.

> **SECOND CORRECTION (2026-08-07, later still).** The paragraph above
> originally continued *"— and that fails for `c ≥ 2`"*. **That is wrong, and
> it was the stated blocker.** The identity holds at **every** cusp number,
> measured directly on 13 manifolds by
> `probes/one_loop_multicusp_derivation_probe.py`. It is not a cusp statement:
> each tetrahedron has six edges in three opposite pairs, one pair per shape
> type, each glued into exactly one edge class, so the column sum is 2 with no
> reference to cusps. I turned a quoted sentence into a structural obstruction
> without testing the sentence.
>
> **The multi-cusp case is now derived and implemented** — see
> `docs/audits/2026-08-07-one-loop-multicusp-derivation.md`. The real
> obstruction was elsewhere and much narrower: an independent *subset* of edge
> rows can generate a proper **sublattice** of the edge lattice (index 2
> observed), so the rows must be a Hermite-normal-form **basis** of that
> lattice. `|τ(L5a1)| = √2`, `|τ(L6a4)| = 8`, validated per cusp against
> SnapPy's cusp shapes to ~1e−59.

**So the `c_σ` arc — L5a1 (c=2) and L6a4 (c=3) — sat entirely in a regime the
implementation did not cover.** That, not the missing flattening, was the real
size of the job; it is now done, with one caveat that matters for `c_σ`
specifically (see "What moves when it is fixed").

## What needs to change

| # | file | change | blocked on |
|---|---|---|---|
| 1 | `whitehead_c_sigma_torsion.py` | replace determinant, restore ½ + flattening monomial | ~~multi-cusp derivation~~ **unblocked** — `one_loop()` now answers at c=2 |
| 2 | `probes/borromean_nz_adjoint_torsion.py` | same wrong form `a − b·z/(1−z)`; source of `\|det\| = 64` | ~~multi-cusp derivation~~ **unblocked** (L6a4, c=3, `\|τ\| = 8`) |
| 3 | `probes/borromean_cusp_framing_factor.py` | its premise is superseded — see below | ditto |
| 4 | `probes/jones_1loop_c0_calibration_fig8.py`, `probes/borromean_jones_1loop_torsion.py` | the `exp(2c₀) = 1/\|det J\|` calibration chain | recheck against corrected `\|τ\|` |
| 5 | both 1-loop probes | `np.linalg.det` and `complex(s['rect'])` are float64 | independent of the above |

### (3) deserves its own note — the corpus already saw the ambiguity

`borromean_cusp_framing_factor.py` records:

> all `2^c` framings of L6a4 gives `|det| ∈ {64, 128, 256, 512} = 2^{6..9}`

So the instability was observed a week ago and attributed to **framing
choice**. PR #4691 found the same quantity taking `2^{3}…2^{6}` under
**retriangulation** at fixed framing. Two different explanations for one
phenomenon, and the DG formula says neither is the cause: the object simply is
not the invariant. The `2^c`-framings idea is also where the per-cusp factor
`2^{(c−1)/2}` appears to originate — so fixing the construction likely
dissolves that whole line rather than repairing it.

## A calibration target that may itself be wrong

`whitehead_c_sigma_torsion.py` justifies dropping the `½` because its result
"reproduces the known figure-eight value `|τ(4₁)| = √3`". But this repo's own
**value-validated** Porti probe (`torsion_nu_sdp_probe.py`, PR #4576) gives
`𝕋_μ(4₁) = −3.00003`, i.e. `|𝕋_μ| = 3` — and DG give `√3/2`. Three
normalizations, and `√3` is none of them.

`one_loop_vs_nu_sdp_probe.py` already flags this explicitly:

> its normalization does NOT match Porti's (4₁: |τ|=√3/2 here vs 3 there; the
> two conventions differ by units). **Do NOT read the τ values here as the
> adjoint torsion** — use `torsion_nu_sdp_probe.py` for that.

That warning exists, and the `c_σ` script did the thing it warns against:
treated a 1-loop determinant as the adjoint torsion, against a calibration
target matching neither convention.

## Blast radius: contained

Checked, not assumed:

* **`content/` blocks:** no `.ts` computes or consumes any of this. The only
  hits for `c_sigma` / `det J_NZ` / `1-loop` are `content/schema/references.ts`
  (a citation) and one open-problems `.md` (prose).
* **Lean:** none. (Established in PR #4696's survey — the two apparent hits
  were `c_σ₀`/`c_σ₁` braid-generator coefficients and a Dimofte–**Gaiotto**–Gukov
  citation, both false positives.)
* **Witness consumers:** `whitehead-c-sigma-torsion.witness.json` is read by no
  code — only beans, audits, and the probes themselves.
* **Production / canonical chain:** nothing. #4671's "audit-only; not wired to
  any production dashboard or the canonical chain" **holds**.

Total affected: **5 probes, 3 audit docs, 4 beans**. No content, no Lean, no
dashboards.

## What moves when it is fixed

**Retracted:** `|τ(L5a1)| = 2^{5/2}`, `|τ(L6a4)| = 2^6 = 64`, the per-cusp
factor `2^{(c−1)/2}`, the `exp(2c₀) = 2^{c−1}/|det J|` unified law, and
`c_σ = 2^{−3/4}` as a *derivation* (already reverted to IDENTIFICATION in
`qou-pn5j`).

**Unaffected:** the numerical value `c_σ = 2^{−3/4}` at ~20 digits — pinned by
`whitehead_c_sigma_hiprec.py`, pure mpmath, no SnapPy and no `det J`. Also
unaffected: `qou-r307`'s scope-(a) verdict (1-loop ≠ ν_SDP), which its own
docstring notes is normalization-robust.

**Still not settled, now that the multi-cusp case exists:** the *overall
constant* at `c ≥ 2`. The `½` is DG's, fixed at `c = 1` by their `4_1` example.
Triangulation invariance cannot see a factor depending only on `c`, and neither
can the change-of-curve law, which is a ratio — so a normalization
`2^{α(c−1)}·½` would pass every test the derivation runs. **That is exactly the
shape of the per-cusp factor `2^{(c−1)/2}` this arc wanted.** Having a
multi-cusp formula therefore does *not* revive it, and `c_σ = 2^{−3/4}` stays at
IDENTIFICATION. Pinning it needs an external multi-cusp reference value, and
nothing in `library/` supplies one — Garoufalidis–Yoon prove 1-loop = adjoint
torsion for **two-bridge knots**, which are one-cusped.

## Recommended order

1. **Fix the 1-cusped case first.** `one_loop_vs_nu_sdp_probe.py`'s
   construction is correct and invariant — promote it to a shared helper and
   point `borromean_nz_adjoint_torsion.py`'s 4₁ calibration at it. Cheap,
   and it establishes a trusted base.
2. ~~**Then DERIVE the multi-cusp extension** for `c ≥ 2`.~~ **DONE** —
   `docs/audits/2026-08-07-one-loop-multicusp-derivation.md`. `Σ_I G_Ii = 2`
   turned out to hold at every cusp number, so it was never the obstruction;
   the real one was that the edge rows must form a lattice **basis**, not just
   an independent subset.

   The cusp-shape lead recorded here was the right one and it paid off, though
   not as a source of `c`-dependence: the per-cusp **change-of-curve law**
   (swap cusp `k`'s meridian row for its longitude row, `τ` scales by that
   cusp's shape) is what validates the construction from outside, to ~1e−59 at
   `c = 1, 2, 3`.
3. **Then** revisit the per-cusp factor — noting it may not survive, since its
   apparent origin (the `2^c` framing count) is one of the explanations the DG
   formula displaces.
4. Drain the float64 in both probes (bean `qou-t0rf`'s class) — independent,
   do it whenever.

**Unit tests available now:** DG's own 4₁ worked example (`√3/2`), and the two
new invariant values `|τ(5_2)| = 1.161162738134`, `|τ(6_2)| = 2.216589930891`.
Garoufalidis–Yoon (arXiv:2411.03801, already in `library/`) proves 1-loop =
adjoint torsion **for two-bridge knots**, which covers `4₁`, `5_2` and `6_2` —
so the 1-cusped leg can be validated against a theorem, not just against
self-consistency.
